# BOT_DC_ADM_PROXY_FIXED4.py
# Fix focus: prevent closing shared connector during warm-up by setting connector_owner=False
# Includes: proxy support, fast ack, followup replies, non-blocking file I/O, logging

import os, json, time, asyncio
from typing import Dict, Any, List
from urllib.parse import urlparse

import discord
from discord import app_commands
from discord.ext import tasks
from discord.utils import setup_logging

import aiofiles
import aiohttp

# ===== Config =====
TOKEN     = ""           # or use ENV DISCORD_TOKEN
GUILD_ID  = None         # int or None
# PROXY_URL = "socks5://rdp:123456@103.148.44.31:1080"           # "socks5://user:pass@IP:PORT" or ""
# PROXY_URL = "socks5://ayfvwzhi:st8j7xhop6md@198.23.239.134:6540"           # "socks5://user:pass@IP:PORT" or ""
PROXY_URL = "socks5://ayfvwzhi-rotate:st8j7xhop6md@p.webshare.io:80"           # "socks5://user:pass@IP:PORT" or ""

ADMIN_ROLE_IDS = {867849626072907776}

JOB_DIR = os.path.dirname(os.path.abspath(__file__))
WORLDS  = os.path.join(JOB_DIR, "worlds.txt")
INPROG  = os.path.join(JOB_DIR, "inprogress.txt")
DONE    = os.path.join(JOB_DIR, "done.txt")
META    = os.path.join(JOB_DIR, "jobs_meta.json")

_meta_lock = asyncio.Lock()
client: "discord.Client | None" = None

# ===== File utils =====
def _load_lines(path: str):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [ln.rstrip("\n") for ln in f]

def _write_lines(path: str, lines: List[str]):
    with open(path, "w", encoding="utf-8") as f:
        for ln in lines:
            f.write(ln + "\n")

def _append_line(path: str, line: str):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def _load_meta() -> Dict[str, Any]:
    if not os.path.exists(META):
        return {}
    with open(META, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def _save_meta(obj: Dict[str, Any]):
    with open(META, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def _status_of(world: str) -> str:
    wu = world.upper()
    for ln in _load_lines(INPROG):
        w = ln.split("|")[0].upper() if ln else ""
        if w == wu:
            return "inprogress"
    for ln in _load_lines(DONE):
        w = ln.split("|")[0].upper() if ln else ""
        if w == wu:
            return "done"
    for ln in _load_lines(WORLDS):
        w = ln.split("|")[0].upper() if ln else ""
        if w == wu:
            return "waiting"
    return "unknown"

# ===== Permissions =====
def _is_admin(member: discord.Member) -> bool:
    if getattr(member, "guild_permissions", None) and member.guild_permissions.administrator:
        return True
    return any((r.id in ADMIN_ROLE_IDS) for r in getattr(member, "roles", []))

def admin_only():
    async def predicate(interaction: discord.Interaction):
        member = interaction.user if isinstance(interaction.user, discord.Member) else None
        if member and _is_admin(member):
            return True
        raise app_commands.CheckFailure("Khusus admin.")
    return app_commands.check(predicate)

# ===== Ack & responses =====
async def fast_ack(interaction: discord.Interaction, ephemeral: bool = True):
    if not interaction.response.is_done():
        try:
            await interaction.response.defer(ephemeral=ephemeral, thinking=False)
        except discord.HTTPException:
            pass

async def ephem(interaction: discord.Interaction, content: str):
    await fast_ack(interaction, ephemeral=True)
    await interaction.followup.send(content, ephemeral=True)

# ===== Presence =====
def count_jobs():
    total = 0
    prog = 0
    if os.path.exists(WORLDS):
        with open(WORLDS, "r", encoding="utf-8", errors="ignore") as f:
            total = len([ln for ln in f if ln.strip()])
    if os.path.exists(INPROG):
        with open(INPROG, "r", encoding="utf-8", errors="ignore") as f:
            prog = len([ln for ln in f if ln.strip()])
    return total, prog

from typing import Tuple
@tasks.loop(seconds=30)
async def update_status():
    if not isinstance(client, discord.Client) or not client.is_ready():
        return
    total, prog = await asyncio.to_thread(count_jobs)
    await client.change_presence(activity=discord.Game(name=f"Jobs: {total} | Progress: {prog}"))

# ===== Commands =====
@app_commands.command(name="uploadjobs", description="Upload file daftar job (WORLD|DOOR). (Admin)")
@app_commands.default_permissions(administrator=True)
@admin_only()
async def uploadjobs(
    interaction: discord.Interaction,
    file: discord.Attachment,
    block_id: int,
    storage: str,
    storage_door: str
):
    await fast_ack(interaction)

    temp_path = os.path.join(JOB_DIR, f"temp_{file.filename}")
    await file.save(temp_path)

    added = 0
    async with aiofiles.open(temp_path, mode="r", encoding="utf-8") as f:
        lines = await f.readlines()

    async with aiofiles.open(WORLDS, mode="a", encoding="utf-8") as out:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                world, door = line.split("|", 1)
            elif ":" in line:
                world, door = line.split(":", 1)
            else:
                continue

            world_u = world.strip().upper()
            formatted = f"{world_u}|{door.strip()}|{block_id}|{storage.strip()}|{storage_door.strip()}\n"
            await out.write(formatted)
            added += 1

            async with _meta_lock:
                meta = await asyncio.to_thread(_load_meta)
                meta[world_u] = {
                    "owner_id": interaction.user.id,
                    "created_at": int(time.time()),
                    "door": door.strip(),
                    "bid": str(block_id),
                    "storage": storage.strip(),
                    "storage_door": storage_door.strip(),
                    "status": "waiting"
                }
                await asyncio.to_thread(_save_meta, meta)

    try:
        os.remove(temp_path)
    except Exception:
        pass

    await interaction.followup.send(f"✅ Ditambahkan {added} job ke worlds.txt", ephemeral=True)

@app_commands.command(name="addjob", description="Tambahkan satu job (Admin, private).")
@app_commands.default_permissions(administrator=True)
@admin_only()
@app_commands.describe(world="Nama world", door="Nama door", bid="Block ID (angka)", sw="(opsional) seed world", sd="(opsional) seed door")
async def addjob(interaction: discord.Interaction, world: str, door: str, bid: int, sw: str = None, sd: str = None):
    await fast_ack(interaction)

    world_u = world.upper().strip()
    line = f"{world_u}|{door}|{bid}"
    if sw and sd:
        line = f"{line}|{sw}|{sd}"

    await asyncio.to_thread(_append_line, WORLDS, line)

    async with _meta_lock:
        meta = await asyncio.to_thread(_load_meta)
        meta[world_u] = {
            "owner_id": interaction.user.id,
            "created_at": int(time.time()),
            "door": door,
            "bid": str(bid),
            "status": "waiting"
        }
        await asyncio.to_thread(_save_meta, meta)

    await interaction.followup.send(
        f"✅ Job ditambahkan: `{line}`\nPemilik: <@{interaction.user.id}> (private).",
        ephemeral=True
    )

@app_commands.command(name="myjobs", description="Lihat job milik kamu sendiri (private).")
async def myjobs(interaction: discord.Interaction):
    await fast_ack(interaction)

    async with _meta_lock:
        meta = await asyncio.to_thread(_load_meta)
    my_id = interaction.user.id
    rows = [
        f"{w} | door={i.get('door')} | bid={i.get('bid')} | status={i.get('status')}"
        for w, i in sorted(meta.items())
        if i.get("owner_id") == my_id
    ]
    if not rows:
        await interaction.followup.send("Kamu belum punya job.", ephemeral=True)
        return
    dump = "```\n" + "\n".join(rows) + "\n```"
    await interaction.followup.send(f"📋 **Job kamu:**\n{dump}", ephemeral=True)

@app_commands.command(name="status", description="Cek status 1 world (pemilik atau admin).")
@app_commands.describe(world="Nama world")
async def status_cmd(interaction: discord.Interaction, world: str):
    await fast_ack(interaction)

    w = world.upper().strip()
    async with _meta_lock:
        meta = await asyncio.to_thread(_load_meta)
    info = meta.get(w)

    member = interaction.user if isinstance(interaction.user, discord.Member) else None
    can_view = bool(member and (_is_admin(member) or (info and info.get("owner_id") == member.id)))

    st = await asyncio.to_thread(_status_of, w)
    if info and can_view:
        await interaction.followup.send(
            f"Status `{w}`: **{st}**\nOwner: <@{info.get('owner_id')}> door={info.get('door')} bid={info.get('bid')}",
            ephemeral=True
        )
    elif info is None:
        await interaction.followup.send(
            f"Status `{w}`: **{st}** (tidak ada meta / mungkin bukan job yang dibuat lewat bot).",
            ephemeral=True
        )
    else:
        await interaction.followup.send("Kamu bukan pemilik job ini.", ephemeral=True)

@app_commands.command(name="cancel", description="Batalkan job milik sendiri (kalau masih waiting).")
@app_commands.describe(world="Nama world")
async def cancel(interaction: discord.Interaction, world: str):
    await fast_ack(interaction)

    w = world.upper().strip()
    async with _meta_lock:
        meta = await asyncio.to_thread(_load_meta)
        info = meta.get(w)
        if not info or info.get("owner_id") != interaction.user.id:
            await interaction.followup.send("Job tidak ditemukan atau bukan milik kamu.", ephemeral=True)
            return

        st = await asyncio.to_thread(_status_of, w)
        if st != "waiting":
            await interaction.followup.send("Tidak bisa dibatalkan: job sudah berjalan/selesai.", ephemeral=True)
            return

        lines = await asyncio.to_thread(_load_lines, WORLDS)
        new_lines = [ln for ln in lines if not (ln.upper().startswith(w))]
        await asyncio.to_thread(_write_lines, WORLDS, new_lines)

        meta.pop(w, None)
        await asyncio.to_thread(_save_meta, meta)

    await interaction.followup.send(f"❎ Job `{w}` sudah dibatalkan.", ephemeral=True)

@app_commands.command(name="admin_jobs", description="(Admin) Lihat semua job.")
@app_commands.default_permissions(administrator=True)
@admin_only()
async def admin_jobs(interaction: discord.Interaction):
    await fast_ack(interaction)

    async with _meta_lock:
        meta = await asyncio.to_thread(_load_meta)
    rows = [
        f"{w} | owner=<@{i.get('owner_id')}> | status={i.get('status')} | door={i.get('door')} | bid={i.get('bid')}"
        for w, i in sorted(meta.items())
    ]
    if not rows:
        await interaction.followup.send("Belum ada job di meta.", ephemeral=True)
        return
    dump = "```\n" + "\n".join(rows) + "\n```"
    await interaction.followup.send(f"🛠️ **All Jobs (meta):**\n{dump}", ephemeral=True)

# ===== Client =====
intents = discord.Intents.default()
intents.guilds = True

class JobBot(discord.Client):
    def __init__(self, connector=None):
        super().__init__(intents=intents, connector=connector)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.add_command(uploadjobs)
        self.tree.add_command(addjob)
        self.tree.add_command(myjobs)
        self.tree.add_command(status_cmd)
        self.tree.add_command(cancel)
        self.tree.add_command(admin_jobs)

        if GUILD_ID:
            guild_obj = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild_obj)
            await self.tree.sync(guild=guild_obj)
        else:
            await self.tree.sync()

        if not update_status.is_running():
            update_status.start()

async def on_ready_event():
    print(f"Bot login sebagai {client.user}")

# ===== Warm proxy (connector_owner=False agar konektor tidak tertutup) =====
async def warm_proxy(connector):
    if connector is None:
        return
    import aiohttp
    try:
        async with aiohttp.ClientSession(connector=connector, connector_owner=False) as s:
            for url in ("https://discord.com/api/v10/gateway", "https://gateway.discord.gg/"):
                try:
                    async with s.get(url, timeout=10) as r:
                        await r.text()
                except Exception as ie:
                    print(f"[WARM] sub-warn {url}: {ie}")
        print("[WARM] proxy path warmed")
    except Exception as e:
        print(f"[WARM] warn: {e}")


# ===== Build proxy connector robustly =====
def build_proxy_connector(url: str):
    from aiohttp_socks import ProxyConnector
    try:
        conn = ProxyConnector.from_url(url)
        print(f"[PROXY] Using {url}")
        return conn
    except Exception as e1:
        try:
            u = urlparse(url)
            host = u.hostname
            port = u.port or 1080
            user = u.username
            pwd  = u.password
            try:
                from aiohttp_socks import ProxyType
                conn = ProxyConnector(proxy_type=ProxyType.SOCKS5, host=host, port=port,
                                      username=user, password=pwd, rdns=True)
            except Exception:
                from aiohttp_socks import SocksVer
                conn = ProxyConnector(socks_ver=SocksVer.SOCKS5, host=host, port=port,
                                      username=user, password=pwd, rdns=True)
            print(f"[PROXY] Using socks5://{host}:{port} (rdns=True)")
            return conn
        except Exception as e2:
            raise RuntimeError(f"Gagal init proxy: {e1} / fallback: {e2}")

# ===== Main =====
async def main():
    setup_logging(level=20)  # INFO

    global client
    tok = TOKEN or os.getenv("DISCORD_TOKEN") or ""
    if not tok.strip():
        raise RuntimeError("TOKEN belum diisi. Isi variabel TOKEN atau set ENV DISCORD_TOKEN.")

    connector = None
    if PROXY_URL:
        try:
            connector = build_proxy_connector(PROXY_URL)
        except Exception as e:
            print(f"[PROXY] {e}")

    os.makedirs(JOB_DIR, exist_ok=True)
    for path in (WORLDS, INPROG, DONE):
        if not os.path.exists(path):
            _write_lines(path, [])
    if not os.path.exists(META):
        _save_meta({})

    await warm_proxy(connector)

    global client_session_closed
    client = JobBot(connector=connector)
    client.tree.on_error = lambda i, e: asyncio.create_task(ephem(i, f"Terjadi kesalahan: {e}"))
    client.event(on_ready_event)

    await client.start(tok)

if __name__ == "__main__":
    asyncio.run(main())
