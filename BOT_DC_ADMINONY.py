# discord_bot_jobs.py
# Python 3.10+, discord.py 2.x
import os, json, asyncio, time
from typing import Dict, Any, List
import discord
from discord import app_commands
from discord.ext import tasks
import aiofiles

# ========= KONFIGURASI =========
# Ambil token dari environment agar aman (wajib: set DISCORD_TOKEN di environment)
TOKEN = os.getenv("DISCORD_TOKEN") or ""
GUILD_ID = None  # isi int kalau mau register slash command hanya di 1 guild; None = global

JOB_DIR = os.path.dirname(os.path.abspath(__file__))
WORLDS = os.path.join(JOB_DIR, "worlds.txt")
INPROG = os.path.join(JOB_DIR, "inprogress.txt")
DONE   = os.path.join(JOB_DIR, "done.txt")
META   = os.path.join(JOB_DIR, "jobs_meta.json")

# Role Discord yang dianggap admin (boleh lihat semua/mengelola)
# Ganti ID di bawah dengan role-id admin di server-mu
ADMIN_ROLE_IDS = {867849626072907776}

# ========= UTIL FILE / META =========
_meta_lock = asyncio.Lock()

def _load_lines(path: str) -> List[str]:
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

def _is_admin(member: discord.Member) -> bool:
    # Admin server langsung lolos
    if getattr(member, "guild_permissions", None) and member.guild_permissions.administrator:
        return True
    # Atau punya salah satu role khusus admin
    return any((r.id in ADMIN_ROLE_IDS) for r in getattr(member, "roles", []))

def _parse_world_line(line: str):
    # Format worker lama: WORLD|DOOR|BID|SW|SD (SW, SD opsional)
    # Kita hanya butuh WORLD, DOOR, BID
    parts = line.split("|")
    if len(parts) < 3:
        return None, None, None, None, None
    W, D, BID = parts[0].strip(), parts[1].strip(), parts[2].strip()
    SW = parts[3].strip() if len(parts) > 3 else None
    SD = parts[4].strip() if len(parts) > 4 else None
    return W, D, BID, SW, SD

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
    # kalau masih ada di worlds.txt → waiting
    for ln in _load_lines(WORLDS):
        w = ln.split("|")[0].upper() if ln else ""
        if w == wu:
            return "waiting"
    return "unknown"

# ========= DECORATOR & ERROR HANDLER ADMIN =========
def admin_only():
    async def predicate(interaction: discord.Interaction):
        member = interaction.user if isinstance(interaction.user, discord.Member) else None
        if member and _is_admin(member):
            return True
        raise app_commands.CheckFailure("Khusus admin.")
    return app_commands.check(predicate)

# ========= DISCORD CLIENT =========
intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # perlu agar Member.roles / permissions lengkap

class JobBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        if GUILD_ID:
            guild_obj = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild_obj)
            await self.tree.sync(guild=guild_obj)
        else:
            await self.tree.sync()
        self.poll_status.start()

    @tasks.loop(seconds=2.0)
    async def poll_status(self):
        # polling status -> perbarui jobs_meta.json
        async with _meta_lock:
            meta = _load_meta()
            changed = False
            for world, info in list(meta.items()):
                new_status = _status_of(world)
                if info.get("status") != new_status:
                    info["status"] = new_status
                    meta[world] = info
                    changed = True
            if changed:
                _save_meta(meta)

client = JobBot()

# Error handler supaya gagal check admin balas ephemeral rapi
@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CheckFailure):
        try:
            await interaction.response.send_message(str(error), ephemeral=True)
        except discord.InteractionResponded:
            await interaction.followup.send(str(error), ephemeral=True)
    else:
        # Opsional: log error lain biar kelihatan di console
        print("Command error:", repr(error))

# ========= PRESENCE / STATUS LOOP =========
def count_jobs():
    worlds_file = os.path.join(JOB_DIR, "worlds.txt")
    inprog_file = os.path.join(JOB_DIR, "inprogress.txt")

    total_jobs = 0
    inprogress = 0

    if os.path.exists(worlds_file):
        with open(worlds_file, "r") as f:
            total_jobs = len([ln for ln in f if ln.strip()])

    if os.path.exists(inprog_file):
        with open(inprog_file, "r") as f:
            inprogress = len([ln for ln in f if ln.strip()])

    return total_jobs, inprogress

@tasks.loop(seconds=30)  # update status tiap 30 detik
async def update_status():
    total, inprog = count_jobs()
    status_text = f"Jobs: {total} | Progress: {inprog}"
    await client.change_presence(activity=discord.Game(name=status_text))

@client.event
async def on_ready():
    print(f"Bot login sebagai {client.user}")
    if not update_status.is_running():
        update_status.start()

# ========= HELPER EPHEMERAL =========
async def ephem(interaction: discord.Interaction, content: str):
    # Kirim pesan ephemeral (hanya pengirim yang melihat)
    try:
        await interaction.response.send_message(content, ephemeral=True)
    except discord.InteractionResponded:
        await interaction.followup.send(content, ephemeral=True)

# ========= COMMANDS =========
WORLD_FILE = os.path.join(JOB_DIR, "worlds.txt")  # alias, sama dengan WORLDS

# --- ADMIN ONLY: /uploadjobs ---
@app_commands.default_permissions(administrator=True)  # sembunyikan dari non-admin di UI
@client.tree.command(name="uploadjobs", description="Upload file daftar job (WORLD|DOOR).")
@admin_only()
async def file_upload(
    interaction: discord.Interaction,
    file: discord.Attachment,
    block_id: int,
    storage: str,
    storage_door: str
):
    temp_path = os.path.join(JOB_DIR, f"temp_{file.filename}")
    await file.save(temp_path)

    added = 0
    async with aiofiles.open(temp_path, mode="r", encoding="utf-8") as f:
        lines = await f.readlines()

    async with aiofiles.open(WORLD_FILE, mode="a", encoding="utf-8") as out:
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

            # === Simpan meta owner & status ===
            async with _meta_lock:
                meta = _load_meta()
                meta[world_u] = {
                    "owner_id": interaction.user.id,
                    "created_at": int(time.time()),
                    "door": door.strip(),
                    "bid": str(block_id),
                    "storage": storage.strip(),
                    "storage_door": storage_door.strip(),
                    "status": "waiting"
                }
                _save_meta(meta)

    os.remove(temp_path)
    await ephem(interaction, f"✅ Ditambahkan {added} job ke worlds.txt")

# --- (BISA PILIH) Jadikan /addjob admin-only juga ---
@app_commands.default_permissions(administrator=True)
@client.tree.command(name="addjob", description="Tambahkan job ke worlds.txt (private ke pengirim)")
@admin_only()
@app_commands.describe(world="Nama world", door="Nama door", bid="Block ID (angka)", sw="(opsional) seed world", sd="(opsional) seed door")
async def addjob(interaction: discord.Interaction, world: str, door: str, bid: int, sw: str = None, sd: str = None):
    member = interaction.user if isinstance(interaction.user, discord.Member) else None
    if member is None:
        return await ephem(interaction, "Perintah hanya bisa dalam server.")

    world_u = world.upper().strip()
    line = f"{world_u}|{door}|{bid}"
    if sw and sd:
        line = f"{line}|{sw}|{sd}"

    # Tulis ke worlds.txt (worker lama tetap kompatibel)
    _append_line(WORLDS, line)

    # Simpan meta owner & status
    async with _meta_lock:
        meta = _load_meta()
        meta[world_u] = {
            "owner_id": interaction.user.id,
            "created_at": int(time.time()),
            "door": door,
            "bid": str(bid),
            "status": "waiting"
        }
        _save_meta(meta)

    await ephem(interaction, f"✅ Job ditambahkan: `{line}`\nPemilik: <@{interaction.user.id}> (private).")

# --- /myjobs: tetap private untuk user ---
@client.tree.command(name="myjobs", description="Lihat job milik kamu sendiri (private).")
async def myjobs(interaction: discord.Interaction):
    async with _meta_lock:
        meta = _load_meta()
    my_id = interaction.user.id
    rows = []
    for w, info in sorted(meta.items()):
        if info.get("owner_id") == my_id:
            rows.append(f"{w} | door={info.get('door')} | bid={info.get('bid')} | status={info.get('status')}")
    if not rows:
        return await ephem(interaction, "Kamu belum punya job.")
    dump = "```\n" + "\n".join(rows) + "\n```"
    await ephem(interaction, f"📋 **Job kamu:**\n{dump}")

# --- /status: pemilik atau admin ---
@client.tree.command(name="status", description="Cek status 1 world (pemilik atau admin).")
@app_commands.describe(world="Nama world")
async def status(interaction: discord.Interaction, world: str):
    w = world.upper().strip()
    async with _meta_lock:
        meta = _load_meta()
    info = meta.get(w)
    if info is None:
        st = _status_of(w)
        return await ephem(interaction, f"Status `{w}`: **{st}** (tidak ada meta / mungkin bukan job yang dibuat lewat bot).")

    member = interaction.user if isinstance(interaction.user, discord.Member) else None
    if member and (info.get("owner_id") == member.id or _is_admin(member)):
        st = _status_of(w)
        await ephem(interaction, f"Status `{w}`: **{st}**\nOwner: <@{info.get('owner_id')}> door={info.get('door')} bid={info.get('bid')}")
    else:
        await ephem(interaction, "Kamu bukan pemilik job ini.")

# --- /cancel: hanya owner & masih waiting ---
@client.tree.command(name="cancel", description="Batalkan job milik sendiri (kalau masih waiting).")
@app_commands.describe(world="Nama world")
async def cancel(interaction: discord.Interaction, world: str):
    w = world.upper().strip()
    async with _meta_lock:
        meta = _load_meta()
        info = meta.get(w)
        if not info or info.get("owner_id") != interaction.user.id:
            return await ephem(interaction, "Job tidak ditemukan atau bukan milik kamu.")

        # hanya boleh cancel jika masih waiting
        if _status_of(w) != "waiting":
            return await ephem(interaction, "Tidak bisa dibatalkan: job sudah berjalan/selesai.")

        # hapus dari worlds.txt
        lines = _load_lines(WORLDS)
        new_lines = [ln for ln in lines if not (ln.upper().startswith(w))]
        _write_lines(WORLDS, new_lines)

        # hapus dari meta
        meta.pop(w, None)
        _save_meta(meta)

    await ephem(interaction, f"❎ Job `{w}` sudah dibatalkan.")

# --- ADMIN ONLY: /admin_jobs ---
@app_commands.default_permissions(administrator=True)
@client.tree.command(name="admin_jobs", description="(Admin) Lihat semua job.")
@admin_only()
async def admin_jobs(interaction: discord.Interaction):
    async with _meta_lock:
        meta = _load_meta()
    rows = []
    for w, info in sorted(meta.items()):
        rows.append(f"{w} | owner=<@{info.get('owner_id')}> | status={info.get('status')} | door={info.get('door')} | bid={info.get('bid')}")
    if not rows:
        return await ephem(interaction, "Belum ada job di meta.")
    dump = "```\n" + "\n".join(rows) + "\n```"
    await ephem(interaction, f"🛠️ **All Jobs (meta):**\n{dump}")

# ========= MAIN =========
if __name__ == "__main__":
    os.makedirs(JOB_DIR, exist_ok=True)
    for path in (WORLDS, INPROG, DONE):
        if not os.path.exists(path):
            _write_lines(path, [])
    if not os.path.exists(META):
        _save_meta({})

    if not TOKEN:
        raise RuntimeError("ENV DISCORD_TOKEN belum di-set. Set dulu lalu jalankan ulang.")

    client.run(TOKEN)
