----------------------------------------------------------------
-- MULTI WORLD HARVEST + DROP SNAKE (ANTI-SKIP 2 TILE)
-- + TXT JOB QUEUE (worlds.txt / inprogress.txt / done.txt)
-- + WORK-STEALING ("stale" only) / ASSIST_MODE ("always" / "stale")
-- + SMART MULTI-BOT ASSIGNMENT (AUTO SLOT & AUTO TOTAL_BOTS) [opsional RR/CHUNK]
-- + WARP TAHAN BANTING (NUKED + PUBLIC + BAD_DOOR + SAFE TILE) + LOGGING
-- + GUARD: ANTI-STUCK respawn WHITE DOOR (fg==6)
-- + DROP SNAKE SMART (kanan→atas, fallback kiri, stance walkable, tepi kanan aman)
-- + TAKE_MAGNI: keep exactly 1; sisanya drop ke storage; no double-wear
----------------------------------------------------------------

-------------------- BASE PATH (Windows Desktop) --------------------
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/JOB-ANDRE/"):gsub("[/\\]?$", "/")

local function _ensure_dir(p)
  local is_windows = package.config:sub(1,1) == "\\"
  if is_windows then os.execute(('if not exist "%s" mkdir "%s"'):format(p, p))
  else os.execute(('mkdir -p "%s"'):format(p)) end
end
local function _pjoin(base, name) return (base or "") .. (name or "") end
_ensure_dir(extraFilePath)

-------------------- CONFIG --------------------
USE_TXT_QUEUE = true          -- true: pakai worlds.txt queue


-- >>> NEW: Assist mode <<<
ASSIST_MODE          = (ASSIST_MODE or "always") -- "stale" atau "always"
ASSIST_MODE          = tostring(ASSIST_MODE):lower()
ASSIST_HELPER_LIMIT  = ASSIST_HELPER_LIMIT or 1  -- max helper per world
STEAL_HELP           = STEAL_HELP or true        -- untuk mode stale
STALE_SEC            = STALE_SEC or 30 * 60
LOOP_MODE            = false          -- true: terus loop nunggu job, reconcile + leaveWorld anti diem
DELAY_EXE            = 10000
-- Delay/harvest
USE_MAGNI     = false
DELAY_HARVEST = 170

-- Storage MAGNI (opsional)
STORAGE_MAGNI, DOOR_MAGNI = "", "" -- lokasi kacamata (10158)

-- Storage CAKE (final/idle drop tanpa ambang)
STORAGE_CAKE, DOOR_CAKE = "", ""
cakeList  = {1058,1094,1096,1098,1828,3870,7058,10134,10136,10138,10140,10142,10146,10150,10164,10228,11286}
cekepremium = {1828}
MAX_CAKE_PREMIUM = 2



-- Mode RR/CHUNK (dipakai kalau USE_TXT_QUEUE=false)
LIST_WORLD  = { -- "FARM_WORLD|FARM_DOOR|ITEM_BLOCK_ID|STORAGE_WORLD|STORAGE_DOOR"
}
TOTAL_BOTS   = 8
FARM_PER_BOT = FARM_PER_BOT or 0
ASSIGN_MODE  = ASSIGN_MODE or "rr"
ROTATE_LIST  = (ROTATE_LIST ~= nil) and ROTATE_LIST or false
ROTATE_SEED  = ROTATE_SEED or 12345

-- File queue/log di Desktop
JOB_FILES = {
  worlds     = _pjoin(extraFilePath, "worlds.txt"),
  inprogress = _pjoin(extraFilePath, "inprogress.txt"),
  done       = _pjoin(extraFilePath, "done.txt"),
}
FAIL_LOG_FILE    = _pjoin(extraFilePath, "warp_fail.log")
SUCCESS_LOG_FILE = _pjoin(extraFilePath, "success.log")
local function _touch(path) local f=io.open(path,"a"); if f then f:close() end end
_touch(JOB_FILES.worlds); _touch(JOB_FILES.inprogress); _touch(JOB_FILES.done)
local LOCK_DIR = _pjoin(extraFilePath, "locks/")
_ensure_dir(LOCK_DIR)
-------------------- GLOBAL FLAGS --------------------
NUKED_STATUS    = NUKED_STATUS    or false
WORLD_IS_PUBLIC = WORLD_IS_PUBLIC or nil

CURRENT_WORLD_TARGET, CURRENT_DOOR_TARGET = nil, nil
local __door6_ticks, __last_mx, __last_my = 0, nil, nil


SMART_DELAY      = false
DELAY_RECONNECT  = 20000
DELAY_BAD_SERVER = 120000
DELAY_PNB        = 175
DELAY_PLACE      = 115
DELAY_WARP       = 7000
DELAY_TRASH      = 100

-------------------- AUTO SLOT (WORKER_ID pakai SLOT) --------------------
Bot = {}
bot = getBot()
getBot().auto_reconnect = false
for slot=1,TOTAL_BOTS do Bot[slot] = {slot=slot} end
for nomor, bb in pairs(getBots()) do if getBot().name:upper() == bb.name:upper() then index = nomor end end
MY_SLOT = Bot[index].slot
sleep( DELAY_EXE * ( index - ( 1 - 1 ) ) )
local function _simple_hash(s) local h=1469598107; for i=1,#s do h=(h*131 + s:byte(i)) % 4294967296 end; return h end
local function _auto_slot_and_total()
  local self = getBot and getBot() or nil
  local selfName = self and (self.name or ""):upper() or ""
  local names = {}
  if type(getBots)=="function" then for _, b in pairs(getBots()) do if b and b.name then names[#names+1]=(b.name or ""):upper() end end end
  if #names==0 and selfName~="" then names[1]=selfName end
  table.sort(names)
  local detected = #names
  local cfg_total = tonumber(TOTAL_BOTS or 0) or 0
  local total = (cfg_total>0) and cfg_total or detected
  if total<1 then total=1 end
  if detected>=2 then
    local mypos=1; for i,n in ipairs(names) do if n==selfName then mypos=i; break end end
    local myslot=((mypos-1)%total)+1
    return myslot,total
  end
  local tail=tonumber(selfName:match("(%d+)$") or "")
  if tail and tail>0 then local myslot=((tail-1)%total)+1; return myslot,total end
  local myslot=(_simple_hash(selfName)%total)+1; return myslot,total
end
do local s,t=_auto_slot_and_total(); MY_SLOT=MY_SLOT or s; TOTAL_BOTS=TOTAL_BOTS or t end
local function _detect_my_slot(default_slot)
  local b=getBot and getBot() or nil
  if b then
    if b.slot then return tonumber(b.slot) or default_slot end
    if b.name and type(b.name)=="string" then local num=tonumber((b.name or ""):match("(%d+)$") or ""); if num then return num end end
  end
  return default_slot or 1
end
MY_SLOT = MY_SLOT or _detect_my_slot(1)
WORKER_ID = "SLOT"..tostring(MY_SLOT)
-------------------- ASSIGN (mode RR/CHUNK opsional) --------------------
local function _rotate_list(base, seed)
  if (not ROTATE_LIST) or (#base==0) then return base end
  local off=(seed or 0)%#base; if off==0 then return base end
  local out={}; for i=1,#base do out[i]=base[((i-1+off)%#base)+1] end; return out
end
local function build_worlds_for_bot(base_list, my_slot, total_bots, farm_per_bot, mode)
  local base=_rotate_list(base_list, ROTATE_SEED)
  local out, N={}, #base; if N==0 then return out end
  my_slot=math.max(1, math.min(my_slot or 1, total_bots or 1))
  total_bots=math.max(1, total_bots or 1)
  farm_per_bot=tonumber(farm_per_bot or 0) or 0
  mode=(mode=="chunk") and "chunk" or "rr"
  if mode=="chunk" then
    local len=(farm_per_bot>0 and farm_per_bot or math.ceil(N/total_bots))
    local start=(my_slot-1)*len+1; local last=math.min(N, start+len-1)
    for i=start,last do table.insert(out, base[i]) end
  else
    for i=my_slot, N, total_bots do
      table.insert(out, base[i])
      if farm_per_bot>0 and #out>=farm_per_bot then break end
    end
  end
  print(string.format("[ASSIGN] SLOT=%d/%d MODE=%s ROTATE=%s worlds=%d", my_slot,total_bots,mode,tostring(ROTATE_LIST),#out))
  return out
end

-------------------- BOT INIT --------------------
do local b=getBot and getBot() or nil; if b then b.collect_range=4; b.move_range=4; b.dynamic_delay=true end end

-------------------- UTIL / RECONNECT --------------------
function UPDATE_DELAY_BY_PING()
  if not SMART_DELAY then return end
  local b=getBot and getBot() or nil; local P=(b and b.getPing and b:getPing()) or 0; if P==0 then P=200 end
  if P<=150 then return end
  DELAY_RECONNECT=math.max(20000,P*200); DELAY_BAD_SERVER=math.max(120000,P*600)
  DELAY_PNB=P; DELAY_PLACE=math.floor(P*0.7); DELAY_WARP=math.max(5000,P*30); DELAY_TRASH=math.max(100,math.floor(P*0.5))
end

function STATUS_BOT_NEW()
  local b = getBot and getBot() or nil
  local s = b and b.status or nil
  local Status = "Unknown"

  if     (s == BotStatus.online)  or (s == 1)  then Status = "online"
  elseif (s == BotStatus.offline) or (s == 0)  then Status = "offline"
  elseif s == BotStatus.wrong_password              then Status = "Wrong Password"
  elseif s == BotStatus.account_banned              then Status = "Banned"
  elseif s == BotStatus.location_banned             then Status = "Location Banned"
  elseif s == BotStatus.version_update              then Status = "Version Update"
  elseif s == BotStatus.advanced_account_protection then Status = "Advanced Account Protection"
  elseif s == BotStatus.server_overload             then Status = "Server Overload"
  elseif s == BotStatus.too_many_login              then Status = "Too Many Login"
  elseif s == BotStatus.maintenance                 then Status = "Maintenance"
  elseif s == BotStatus.http_block                  then Status = "Http Block"
  elseif s == BotStatus.captcha_requested           then Status = "Captcha Requested"
  elseif s == BotStatus.error_connecting            then Status = "Error Connecting"
  elseif s == BotStatus.high_ping                   then Status = "High Ping"
  elseif s == BotStatus.logon_fail                  then Status = "Logon Fail"
  else Status = tostring(s or "nil") end

  local world_name = ""
  if b and b.getWorld then
    local w = b:getWorld()
    if w and w.name then world_name = (w.name or ""):upper() end
  end
  local inv = (b and b.getInventory and b:getInventory()) or nil
  return {
    world  = world_name,
    name   = (b and b.name) or "",
    level  = (b and b.level) or 0,
    status = Status,
    gems   = (b and b.gem_count) or 0,
    slots  = (inv and inv.slotcount) or 0
  }
end

function SMART_RECONNECT(WORLD, DOOR, POSX, POSY)
  UPDATE_DELAY_BY_PING()
  while (STATUS_BOT_NEW().status=="Maintenance") or (STATUS_BOT_NEW().status=="Version Update")
    or (STATUS_BOT_NEW().status=="Advanced Account Protection") or (STATUS_BOT_NEW().status=="Http Block")
    or (STATUS_BOT_NEW().status=="Logon Fail") do
    local b=getBot and getBot() or nil; if b and b.connect then b:connect() elseif type(connect)=="function" then connect() end
    sleep(DELAY_BAD_SERVER)
  end
  while (STATUS_BOT_NEW().status=="Banned") do print("[SMART_RECONNECT] Banned. Waiting..."); sleep(DELAY_BAD_SERVER) end
  while (STATUS_BOT_NEW().status~="online") or (STATUS_BOT_NEW().status=="High Ping")
    or (STATUS_BOT_NEW().status=="Server Overload") do
    local b=getBot and getBot() or nil; if b and b.connect then b:connect() elseif type(connect)=="function" then connect() end
    sleep(DELAY_RECONNECT)
  end

  if WORLD and DOOR then WARP_WORLD((WORLD or ""):upper(), DOOR)
  elseif WORLD then       WARP_WORLD((WORLD or ""):upper()) end

  if POSX and POSY then local b=getBot and getBot() or nil; if b and b.findPath then b:findPath(POSX,POSY) end end
end

-------------------- WORLD/TILE HELPERS --------------------
local function _get_tiles()
  return (type(getTilesSafe)=="function" and getTilesSafe())
      or (type(getTiles)=="function" and getTiles())
      or {}
end
-- local function _get_tiles()
--   if type(getTilesSafe) == "function" then return getTilesSafe() end
--   return {}
-- end

function _current_world_upper()
  local b=getBot and getBot() or nil; local w=b and b.world or ""
  if (not w or w=="") and b and b.getWorld then local ww=b:getWorld(); if ww and ww.name then w=ww.name end end
  return (w or ""):upper()
end

local function _current_tile_fg()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return -1 end
  local okW,w=pcall(function() return b:getWorld() end); if not okW or not w then return -1 end
  local okL,me=pcall(function() return w:getLocal() end); if not okL or not me then return -1 end
  local tx=math.floor((me.posx or 0)/32); local ty=math.floor((me.posy or 0)/32)
  local okT,t=pcall(function() return w:getTile(tx,ty) end); if not okT or not t then return -1 end
  return t.fg or -1
end

local function _current_tile_fg_safe(polls,wait_ms)
  polls=polls or 12; wait_ms=wait_ms or 120
  for _=1,polls do local fg=_current_tile_fg(); if fg and fg>=0 then return fg end; sleep(wait_ms) end
  return -1
end

function ZEE_COLLECT(state)
  local b=getBot and getBot() or nil; if not b then return end
  if state then b.auto_collect=true; b.ignore_gems=true; b.collect_range=3; b.object_collect_delay=200
  else b.auto_collect=false end
end

-------------------- CAKE: helper any item exists --------------------
local function includesNumber(t,n) for _,num in pairs(t or {}) do if num==n then return true end end; return false end
function checkCake()
  local bot = getBot and getBot() or nil; if not (bot and bot.getInventory) then return false end
  local inv = bot:getInventory()
  for _, id in pairs(cakeList or {}) do
    local isPremium = includesNumber(cekepremium or {}, id)
    local need = isPremium and MAX_CAKE_PREMIUM or 120
    if inv:getItemCount(id) >= need then return true end
  end
  return false
end
local __next_cake_drop_at_ms, __cake_cooldown_ms = 0, 4000
local function __now_ms() return (os.time() or 0)*1000 end
local function _maybe_drop_cake()
  if not (type(checkCake)=="function" and checkCake()) then return end
  local t=__now_ms(); if t<__next_cake_drop_at_ms then return end
  DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList)
  __next_cake_drop_at_ms = t + __cake_cooldown_ms
end

local function has_any_cake()
  local b=getBot and getBot() or nil; if not (b and b.getInventory) then return false end
  local inv=b:getInventory(); for _,id in pairs(cakeList or {}) do if inv:getItemCount(id)>0 then return true end end
  return false
end

-------------------- FACE KANAN --------------------
function faceSide2()
  local b=getBot and getBot() or bot; if not b then return end
  local packet=GameUpdatePacket.new(); packet.type=0; packet.flags=32; b:sendRaw(packet)
end

-------------------- OBJECT CACHE UNTUK DROP --------------------
local _OBJ_CACHE = { grid={}, last_refresh=0 }
local function _grid_key(x,y) return tostring(x).."|"..tostring(y) end
local function _rebuild_obj_grid()
  _OBJ_CACHE.grid={}
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return end
  local w=b:getWorld(); local objs=(w.getObjects and w:getObjects()) or {}
  for _,o in pairs(objs) do
    local ox=math.floor((o.x+16)/32); local oy=math.floor(o.y/32)
    local k=_grid_key(ox,oy); local g=_OBJ_CACHE.grid[k]
    if not g then g={total=0,stacks=0}; _OBJ_CACHE.grid[k]=g end
    g.total=g.total+(o.count or 0); g.stacks=g.stacks+1
  end
  _OBJ_CACHE.last_refresh=os.time()
end
local function _maybe_refresh_obj_grid() if (os.time()-(_OBJ_CACHE.last_refresh or 0))>=3 then _rebuild_obj_grid() end end
function _countOnTile(tx,ty) _maybe_refresh_obj_grid(); local g=_OBJ_CACHE.grid[tostring(tx).."|"..tostring(ty)]; if g then return g.total,g.stacks end; return 0,0 end

local function _meTile()
  local b=getBot and getBot() or nil; local w=b and b.getWorld and b:getWorld() or nil; local me=w and w.getLocal and w:getLocal() or nil
  if not me then return nil end; return math.floor(me.posx/32), math.floor(me.posy/32)
end

-- ganti fungsi lamamu dengan ini
local function _gotoExact(world, door, tx, ty, path_try, step_ms)
  local b = getBot and getBot() or nil; if not b then return false end
  path_try = path_try or 10
  step_ms  = step_ms  or 700

  local last_mx, last_my = nil, nil
  local stale_ticks = 0
  local backoff     = 0         -- tambahan jeda kecil saat stuck

  for _ = 1, path_try do
    local mx, my = _meTile()
    if mx == tx and my == ty then return true end

    -- coba pathing
    b:findPath(tx, ty)

    -- jeda + reconnect ringan (tanpa guard door di sini)
    sleep(step_ms + backoff)
    SMART_RECONNECT(world, door)

    -- cek apakah bergerak
    local cmx, cmy = _meTile()
    if (cmx == (last_mx or mx)) and (cmy == (last_my or my)) then
      stale_ticks = stale_ticks + 1
      -- kalau 3x tidak berubah, anggap stuck → tambah backoff (maks 600ms)
      if stale_ticks >= 3 then
        if backoff < 600 then backoff = math.min(600, (backoff == 0) and 150 or math.floor(backoff * 2)) end
        -- beri kesempatan server sync dulu sebelum ulangi findPath
        sleep(120)
        -- kalau tetap tidak maju setelah backoff bertambah, gagal total
        if stale_ticks >= 6 then return false end
      end
    else
      -- ada progres → reset indikator stuck & backoff
      stale_ticks = 0
      backoff = 0
    end
    last_mx, last_my = cmx, cmy
  end

  return false
end


-------------------- CACHE TILE (full/bad) --------------------
local FULL_CACHE, BAD_CACHE = {}, {}
local function _key(x,y) return x..":"..y end
function mark_full(x,y) FULL_CACHE[_key(x,y)]=true end
function mark_bad (x,y) BAD_CACHE [_key(x,y)]=true end
function is_full_or_bad(x,y) return FULL_CACHE[_key(x,y)] or BAD_CACHE[_key(x,y)] end
function reset_caches() FULL_CACHE={}; BAD_CACHE={} end

-------------------- SMART DROP SNAKE (kanan→atas, fallback kiri) --------------------
WORLD_MAX_X, WORLD_MAX_Y = 99, 23 -- map kecil: x:0..99, y:0..23
local function REFRESH_WORLD_BOUNDS()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return end
  local w=b:getWorld(); if not w then return end
  local wx=(w.width and (w.width-1)) or WORLD_MAX_X
  local wy=(w.height and (w.height-1)) or WORLD_MAX_Y
  WORLD_MAX_X, WORLD_MAX_Y = wx, wy
end

local function _my_xy()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return 0,0 end
  local w=b:getWorld(); local me=w and w:getLocal() or nil; if not me then return 0,0 end
  return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
end
local function _is_in_bounds(x,y) return x>=0 and x<=WORLD_MAX_X and y>=0 and y<=WORLD_MAX_Y end
local function _is_walkable(tx,ty)
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return false end
  local w=b:getWorld(); local t=w and w:getTile(tx,ty) or nil
  return (t~=nil) and ((t.fg or 0)==0)
end

-- local function _probe_slot(cx,cy,tile_cap,stack_cap)
--   if not _is_in_bounds(cx,cy) then return false end
--   local stanceX,stanceY=cx-1,cy
--   if stanceX<0 then return false end
--   if (not _is_in_bounds(stanceX,stanceY)) or (not _is_walkable(stanceX,stanceY)) then mark_bad(cx,cy); return false end
--   if is_full_or_bad(cx,cy) then return false end
--   local total,stacks=_countOnTile(cx,cy)
--   if (total>=(tile_cap or 3000)) or (stacks>=(stack_cap or 20)) then mark_full(cx,cy); return false end
--   return true
-- end

local function _probe_slot(cx,cy,tile_cap,stack_cap)
  if not _is_in_bounds(cx,cy) then return false end

  -- cek tile world
  local b = getBot and getBot() or nil
  local w = b and b:getWorld() or nil
  local okT, tile = pcall(function() return w:getTile(cx,cy) end)
  if (not okT) or (not tile) then return false end

  -- NEW: pastikan tile kosong (fg==0)
  if (tile.fg or 0) ~= 0 then
    mark_bad(cx,cy)
    return false
  end

  -- stance harus walkable
  local stanceX, stanceY = cx-1, cy
  if stanceX < 0 then return false end
  if (not _is_in_bounds(stanceX,stanceY)) or (not _is_walkable(stanceX,stanceY)) then
    mark_bad(cx,cy); return false
  end

  -- existing capacity check
  if is_full_or_bad(cx,cy) then return false end
  local total,stacks = _countOnTile(cx,cy)
  if (total >= (tile_cap or 3000)) or (stacks >= (stack_cap or 20)) then
    mark_full(cx,cy); return false
  end
  return true
end




local function _scan_row_right(start_x, cy, tile_cap, stack_cap)
  local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
  while cx<=WORLD_MAX_X do if _probe_slot(cx,cy,tile_cap,stack_cap) then return cx,cy end; cx=cx+1 end
  return nil,nil
end
local function _scan_row_left(start_x, cy, tile_cap, stack_cap)
  local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
  while cx>=0 do if _probe_slot(cx,cy,tile_cap,stack_cap) then return cx,cy end; cx=cx-1 end
  return nil,nil
end

local function _nextDropTileSnake_auto(sx,sy,cursor,tile_cap,stack_cap)
  local start_col=sx+1; if start_col>WORLD_MAX_X then start_col=WORLD_MAX_X end; if start_col<0 then start_col=0 end
  local curx=cursor.x or start_col; local cury=math.max(0, math.min(cursor.y or sy, WORLD_MAX_Y))

  -- Pass 1: kanan → lalu naik baris (atas y-1)
  do
    local y=cury; local first_row=true
    while y>=0 do
      local row_start= first_row and math.max(curx,start_col) or start_col
      local rx,ry=_scan_row_right(row_start,y,tile_cap,stack_cap)
      if rx then cursor.x, cursor.y = rx, ry; return rx, ry, cursor end
      y=y-1; first_row=false
    end
  end

  -- Pass 2: fallback kiri ←
  do
    local y=cury; local first_row=true
    while y>=0 do
      local row_start_left= first_row and (math.min(curx,WORLD_MAX_X)-1) or (start_col-1)
      if row_start_left>WORLD_MAX_X then row_start_left=WORLD_MAX_X end
      if row_start_left<0 then row_start_left=start_col-1 end
      local lx,ly=_scan_row_left(row_start_left,y,tile_cap,stack_cap)
      if lx then cursor.x, cursor.y = lx, ly; return lx, ly, cursor end
      y=y-1; first_row=false
    end
  end

  return nil,nil,cursor
end

function DROP_ITEMS_SNAKE(WORLD, DOOR, ITEMS, opts)
  local b = getBot and getBot() or nil
  if not b or type(ITEMS) ~= "table" then return end

  opts = opts or {}
  local CHUNK      = opts.chunk or 400
  local STEP_MS    = opts.step_ms or 700
  local PATH_TRY   = opts.path_try or 10
  local TILE_CAP   = opts.tile_cap or 4000
  local STACK_CAP  = opts.stack_cap or 20
  local RETRIES_TL = opts.tile_retries or 2
  local HARD_LIMIT = 150   -- guard ekstra anti infinite loop per item/tile

  -- helper kecil: setelah drop, beri kesempatan inventory sync
  local function _poll_inv_drop_ok(item_id, before)
    for _ = 1, 4 do
      sleep(math.max(120, math.floor(STEP_MS/4)))
      local now = b:getInventory():getItemCount(item_id)
      if now < before then return true, now end
    end
    return false, b:getInventory():getItemCount(item_id)
  end

  reset_caches(); ZEE_COLLECT(false)
  WARP_WORLD(WORLD, DOOR); sleep(150); SMART_RECONNECT(WORLD, DOOR)
  REFRESH_WORLD_BOUNDS()

  -- posisi awal cursor mengikuti logika lamamu
  local sx, sy = _my_xy()
  local start_col = math.min(sx + 1, WORLD_MAX_X); if start_col < 0 then start_col = 0 end
  local start_row = math.max(0, math.min(sy, WORLD_MAX_Y))
  local cursor    = { x = start_col, y = start_row }

  for _, ITEM in pairs(ITEMS) do
    local have = b:getInventory():getItemCount(ITEM)
    local hard_attempts = 0

    while have > 0 do
      ::seek_slot::
      if hard_attempts > HARD_LIMIT then
        print("[DROP] hard-limit tercapai, pindah cari tile berikutnya untuk item ", ITEM)
        hard_attempts = 0
      end

      local candX, candY
      candX, candY, cursor = _nextDropTileSnake_auto(sx, sy, cursor, TILE_CAP, STACK_CAP)
      if not candX then
        print("[DROP] Area penuh atau habis jangkauan (kanan & kiri).")
        return
      end

      local stanceX, stanceY = candX - 1, candY
      if (stanceX < 0) or (not _is_in_bounds(stanceX, stanceY)) or (not _is_walkable(stanceX, stanceY)) then
        mark_bad(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      if not _gotoExact(WORLD, DOOR, stanceX, stanceY, PATH_TRY, STEP_MS) then
        mark_bad(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      faceSide2()

      local total, stacks = _countOnTile(candX, candY)
      if (total >= TILE_CAP) or (stacks >= STACK_CAP) then
        mark_full(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      local cap = math.max(0, TILE_CAP - total)
      local drop_try = math.min(have, CHUNK, cap)
      if drop_try <= 0 then
        mark_full(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      local attempts_here = 0
      while drop_try > 0 and have > 0 do
        attempts_here = attempts_here + 1
        hard_attempts  = hard_attempts + 1

        local before = b:getInventory():getItemCount(ITEM)
        -- PENTING: pakai numeric ITEM
        b:drop(ITEM, drop_try)

        -- jeda pendek + reconnect ringan (tanpa guard door di inner loop)
        sleep(STEP_MS)
        SMART_RECONNECT()

        local ok, after = _poll_inv_drop_ok(ITEM, before)
        if ok then
          have = after
          attempts_here = 0 -- reset karena ada progres

          -- cek kapasitas tile setelah sebagian turun
          local t2, s2 = _countOnTile(candX, candY)
          if (t2 >= TILE_CAP) or (s2 >= STACK_CAP) then
            mark_full(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            break
          end
          local sisa = TILE_CAP - t2
          if sisa <= 0 then
            mark_full(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            break
          end

          drop_try = math.min(have, CHUNK, sisa) -- lanjut turunkan sisa
        else
          -- gagal turun → kecilkan batch; jika berkali-kali gagal, tandai bad
          if attempts_here >= RETRIES_TL then
            mark_bad(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            goto seek_slot
          end
          drop_try = math.max(1, math.floor(drop_try / 2))
        end

        if hard_attempts > HARD_LIMIT then
          -- guard anti infinite loop
          mark_bad(candX, candY)
          cursor.x = math.min(candX + 1, WORLD_MAX_X)
          goto seek_slot
        end
      end
    end
  end
end


-------------------- NUKED + PUBLIC CHECK --------------------
function checkNukeds(variant, _)
  if variant:get(0):getString() ~= "OnConsoleMessage" then return end
  local message = variant:get(1):getString()
  if message:find("inaccessible") or message:find("That world is inaccessible") then
    NUKED_STATUS = true
  elseif message:find("been banned from that world") then
    NUKED_STATUS = true
  elseif message:find("Players lower than level") then
    NUKED_STATUS = true
  end
end

local function _world_public_safe()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return nil end
  local okW,w=pcall(function() return b:getWorld() end); if not okW or not w then return nil end
  local okP,pub=pcall(function() return w.public end); if not okP then return nil end
  return pub and true or false
end

local function log_fail(world, door, reason)
  local f,err=io.open(FAIL_LOG_FILE,"a"); if not f then print("[LOG] fail open: "..tostring(err)); return end
  local line=string.format("[%s] WORLD=%s | DOOR=%s | REASON=%s\n", os.date("%Y-%m-%d %H:%M:%S"), tostring(world), tostring(door), tostring(reason))
  f:write(line); f:close(); print("[FAIL-LOG]", line)
end
local function log_success(world,door,secs)
  local f,err=io.open(SUCCESS_LOG_FILE,"a"); if not f then print("[LOG] success open: "..tostring(err)); return end
  local line=string.format("[%s] WORLD=%s | DOOR=%s | DURATION=%ds\n", os.date("%Y-%m-%d %H:%M:%S"), tostring(world), tostring(door), tonumber(secs or 0))
  f:write(line); f:close(); print("[SUCCESS-LOG]", line)
end

-------------------- WARP (tahan banting + bad door fix) --------------------
--------------------------------------------------------------------
-- GUARD_DOOR_STUCK (revisi dengan cooldown)
--------------------------------------------------------------------
local __door6_ticks = 0
local __guard_cooldown_until = 0   -- NEW: penanda cooldown global
MAX_WARP_RETRY=10; MAX_DOOR_RETRY=5; MAX_RECOLL_CYCLES=2

local function _nudge_and_warp(WORLD,DOOR,tries)
  local b=getBot and getBot() or nil; if not b then return false end
  tries=tries or 3
  for _=1,tries do
    local okW,w=pcall(function() return b:getWorld() end)
    if okW and w then local okL,me=pcall(function() return w:getLocal() end)
      if okL and me and b.findPath then local mx=math.floor((me.posx or 0)/32); local my=math.floor((me.posy or 0)/32); b:findPath(mx+1,my); sleep(300) end
    end
    if b.warp then b:warp((WORLD or ""):upper().."|"..(DOOR or "")) end
    sleep(DELAY_WARP); local fg=_current_tile_fg_safe(6,100); if fg~=6 then return true end
  end
  return false
end



function GUARD_DOOR_STUCK(WORLD, DOOR)
  local b = getBot and getBot() or nil
  if not b then return end

  -- Cek tile tempat bot berdiri
  local mx,my = _meTile()
  local w = b:getWorld()
  local okT, tile = pcall(function() return w:getTile(mx,my) end)
  if not okT or not tile then return end

  -- Kalau bukan di white door (fg==6) → reset counter
  if (tile.fg or 0) ~= 6 then
    __door6_ticks = 0
    return
  end

  -- Kalau masih cooldown → skip guard
  local now = os.time()
  if now < (__guard_cooldown_until or 0) then
    return
  end

  -- Tambah counter setiap tick stuck di door
  __door6_ticks = __door6_ticks + 1

  -- Kalau stuck 6 kali berturut-turut → lakukan nudge+warp
  if __door6_ticks >= 6 then
    print("[GUARD] Stuck di white door. Nudge+warp...")

    -- Set cooldown supaya tidak langsung dipanggil lagi
    __guard_cooldown_until = now + 3   -- cooldown 3 detik
    __door6_ticks = 0

    _nudge_and_warp(WORLD, DOOR, 3)  -- panggil fungsi aslinya (max tries 3)
  end
end

function WARP_WORLD(WORLD, DOOR)
  WORLD=(WORLD or ""):upper(); if WORLD=="" then return false end
  local tryDoor=(DOOR or "")~=""
  NUKED_STATUS, WORLD_IS_PUBLIC = false, nil

  local listener_added=false
  if type(addEvent)=="function" then addEvent(Event.variantlist, checkNukeds); listener_added=true end
  local function _cleanup() if listener_added and type(removeEvent)=="function" then removeEvent(Event.variantlist) end end

  if _current_world_upper()==WORLD then
    local pub=_world_public_safe(); if pub~=nil then WORLD_IS_PUBLIC=pub end
    local fg=_current_tile_fg_safe(5,80)
    if not tryDoor or (fg~=6) then CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET= tryDoor and DOOR or nil; _cleanup(); return true end
  end

  local cycles=0
  while cycles<(MAX_RECOLL_CYCLES or 1) do
    cycles=cycles+1
    local attempt, ok=0,false
    while attempt<(MAX_WARP_RETRY or 10) do
      UPDATE_DELAY_BY_PING()
      if _current_world_upper()==WORLD then ok=true; break end
      attempt=attempt+1
      local b=getBot and getBot() or nil
      if b and b.warp then if tryDoor then b:warp(WORLD.."|"..DOOR) else b:warp(WORLD) end
      else print("[WARP_WORLD] getBot() not available."); _cleanup(); return false end
      if type(listenEvents)=="function" then listenEvents(5) end
      if NUKED_STATUS then print("[WARP_WORLD] Nuked saat warp."); _cleanup(); return false end
      sleep(DELAY_WARP); SMART_RECONNECT()
      if _current_world_upper()==WORLD then ok=true; break end
    end
    if ok then break end
  end

  if _current_world_upper()~=WORLD then print("[WARP_WORLD] Gagal warp."); _cleanup(); return false end

  local pub=_world_public_safe(); if pub~=nil then WORLD_IS_PUBLIC=pub; print(pub and "[WARP] PUBLIC" or "[WARP] PRIVATE/LOCKED") end

  if tryDoor then
    local fg=_current_tile_fg_safe(15,120)
    if fg>=0 and fg~=6 then CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true end

    if fg<0 then
      for _=1,(MAX_DOOR_RETRY or 5) do
        local b=getBot and getBot() or nil; if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked door."); _cleanup(); return false end
        sleep(DELAY_WARP); SMART_RECONNECT()
        fg=_current_tile_fg_safe(8,120)
        if fg>=0 and fg~=6 then CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true end
      end
      _cleanup(); return false
    end

    if fg==6 then
      for dtry=1,(MAX_DOOR_RETRY or 5) do
        local b=getBot and getBot() or nil; if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked door."); _cleanup(); return false end
        sleep(DELAY_WARP); SMART_RECONNECT()
        fg=_current_tile_fg_safe(8,120)
        if fg>=0 and fg~=6 then CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true end
        print(string.format("[WARP_WORLD] Door attempt %d/%d fail.", dtry,(MAX_DOOR_RETRY or 5)))
      end
      if _nudge_and_warp(WORLD,DOOR,3) then CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true end
      print("[WARP_WORLD] Bad door (masih di white door)."); _cleanup(); return false
    end
  end

  CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET= tryDoor and DOOR or nil; _cleanup(); return true
end

local function warp_ok_and_public(W,D)
  NUKED_STATUS, WORLD_IS_PUBLIC=false,nil
  local ok=WARP_WORLD(W,D)
  if not ok then log_fail(W,D,"warp_failed"); return false, "warp_failed" end
  if NUKED_STATUS then log_fail(W,D,"nuked"); return false,"nuked" end
  local pub=_world_public_safe(); if pub~=nil then WORLD_IS_PUBLIC=pub end
  if WORLD_IS_PUBLIC==false then log_fail(W,D,"not_public"); return false,"not_public" end
  if (D or "")~="" then
    local fg=_current_tile_fg_safe(6,100)
    if fg==6 then
      local b=getBot and getBot() or nil
      for _=1,3 do if b and b.warp then b:warp((W or ""):upper().."|"..D) end; sleep(DELAY_WARP); fg=_current_tile_fg_safe(6,100); if fg~=6 then break end end
      if fg==6 then log_fail(W,D,"bad_door"); return false,"bad_door" end
    end
  end
  return true,"ok"
end

-------------------- FARM CHECKS --------------------
ITEM_BLOCK_ID = 4584; ITEM_SEED_ID = ITEM_BLOCK_ID + 1
local function has_harvestables()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return false end
  local w=b:getWorld()
  for _,t in pairs(_get_tiles()) do local tt=w:getTile(t.x,t.y); if tt and tt.fg==ITEM_SEED_ID and tt:canHarvest() then return true end end
  return false
end
local function checkitemfarm(farmList)
  local inv=getBot():getInventory()
  for _,item in pairs(farmList) do if inv:getItemCount(item)>=190 then return true end end
  return false
end
local function has_any_item_farm(farmList)
  local inv=getBot():getInventory()
  for _,item in pairs(farmList) do if inv:getItemCount(item)>0 then return true end end
  return false
end
-------------------- TAKE MAGNI (keep exactly 1) --------------------
local function _ensure_single_item_in_storage(item_id, keep, storageW, storageD, opts)
  local b=getBot and getBot() or nil; if not b then return end
  keep=keep or 1; opts=opts or {}
  local CHUNK=opts.chunk or 400; local STEP_MS=opts.step_ms or 700; local PATH_TRY=opts.path_try or 10
  local TILE_CAP=opts.tile_cap or 4000; local STACK_CAP=opts.stack_cap or 20; local RETRIES_TL=opts.tile_retries or 2

  local inv=b:getInventory(); local have=inv:getItemCount(item_id)
  if have<=keep then return end
  if (storageW or "")~="" then WARP_WORLD(storageW,storageD); sleep(150); SMART_RECONNECT(storageW,storageD) end
  reset_caches(); ZEE_COLLECT(false)
  local me=b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
  local sx,sy= (me and math.floor(me.posx/32) or 1), (me and math.floor(me.posy/32) or 1)
  local cursor={x=math.min(sx+1,WORLD_MAX_X), y=math.max(0, math.min(sy, WORLD_MAX_Y))}
  local extras=have-keep
  while extras>0 do
    ::seek_slot::
    local candX,candY; candX,candY,cursor=_nextDropTileSnake_auto(sx,sy,cursor,TILE_CAP,STACK_CAP)
    if not candX then print("[MAGNI] Storage area penuh/jangkauan habis."); return end
    local stanceX,stanceY=candX-1,candY
    if (stanceX<0) or (not _is_in_bounds(stanceX,stanceY)) or (not _is_walkable(stanceX,stanceY)) then
      mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot
    end
    if not _gotoExact(storageW,storageD,stanceX,stanceY,PATH_TRY,STEP_MS) then
      mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot
    end
    faceSide2()
    local total,stacks=_countOnTile(candX,candY)
    if (total>=TILE_CAP) or (stacks>=STACK_CAP) then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
    local cap=math.max(0,TILE_CAP-total); local drop_try=math.min(extras,CHUNK,cap); if drop_try<=0 then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
    local attempts_here=0
    while drop_try>0 and extras>0 do
      attempts_here=attempts_here+1
      local before=inv:getItemCount(item_id)
      b:drop(tostring(item_id), drop_try)
      sleep(STEP_MS); SMART_RECONNECT(); GUARD_DOOR_STUCK()
      local after=inv:getItemCount(item_id)
      if after<before then
        local dropped=before-after; extras=math.max(0, extras-dropped)
        local t2,s2=_countOnTile(candX,candY)
        if (t2>=TILE_CAP) or (s2>=STACK_CAP) then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); break end
        local sisa_cap=TILE_CAP-t2; if sisa_cap<=0 then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); break end
        drop_try=math.min(extras,CHUNK,sisa_cap); attempts_here=0
      else
        if attempts_here>=RETRIES_TL then mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
        drop_try=math.max(1, math.floor(drop_try/2))
      end
    end
  end
end

--------------------------------------------------------------------
-- TAKE_MAGNI (cooldown hanya saat magni TIDAK ADA / gagal ambil)
--------------------------------------------------------------------
--------------------------------------------------------------------
-- CONFIG GLOBAL (sekali saja di atas)
--------------------------------------------------------------------
--------------------------------------------------------------------
--------------------------------------------------------------------
--------------------------------------------------------------------
MAGNI_COOLDOWN       = MAGNI_COOLDOWN or {}             -- per-world -> epoch detik
MAGNI_COOLDOWN_MIN   = tonumber(MAGNI_COOLDOWN_MIN or 10)  -- menit
MAGNI_FAILS          = MAGNI_FAILS or {}                -- per-world -> count gagal berturut-turut
MAGNI_FAILS_MAX_TRY  = tonumber(MAGNI_FAILS_MAX_TRY or 3)  -- berapa kali gagal sebelum cooldown
--------------------------------------------------------------------

-- helper
local function _world_key(w) return tostring(w or ""):upper() end
local function _set_cd(w, add_min)
  local mins = tonumber(add_min ~= nil and add_min or MAGNI_COOLDOWN_MIN) or 0
  if mins > 0 then MAGNI_COOLDOWN[_world_key(w)] = os.time() + mins*60 end
end
local function _inc_fail(w)
  local k=_world_key(w); MAGNI_FAILS[k]=(MAGNI_FAILS[k] or 0)+1; return MAGNI_FAILS[k]
end
local function _reset_fail(w) MAGNI_FAILS[_world_key(w)] = 0 end

--------------------------------------------------------------------
-- TAKE_MAGNI (cooldown hanya saat gagal berkali-kali)
--------------------------------------------------------------------
function TAKE_MAGNI(WORLD, DOOR)
  local b=getBot and getBot() or nil; if not b or not USE_MAGNI then return false end
  local TARGET_ID=10158; local inv=b:getInventory()
  local now=os.time()

  -- world untuk pencatatan cooldown/fails: prefer storage, fallback ke WORLD argumen
  local CD_WORLD = ((STORAGE_MAGNI or "") ~= "") and STORAGE_MAGNI or WORLD
  local CDKEY    = _world_key(CD_WORLD)

  -- === cek cooldown pakai CD_WORLD ===
  do
    local cd_until = MAGNI_COOLDOWN[CDKEY]
    if cd_until and now < cd_until then
      local sisa = cd_until - now
      print(string.format("[TAKE_MAGNI] Cooldown aktif %s (%ds)", CD_WORLD, sisa))
      return false
    end
  end

  -- Early: bila >1, normalisasi ke 1 dan pakai
  do
    local have=inv:getItemCount(TARGET_ID)
    if have>1 then
      local storageW,storageD=STORAGE_MAGNI,DOOR_MAGNI
      if (storageW or "")=="" then storageW,storageD=WORLD,DOOR end
      _ensure_single_item_in_storage(TARGET_ID,1,storageW,storageD,
        {chunk=200,step_ms=600,path_try=10,tile_cap=4000,stack_cap=20,tile_retries=2})
      if inv:getItemCount(TARGET_ID)>0 then b:wear(TARGET_ID); sleep(250) end
      return true
    end
  end

  -- helper ambil
  local function _try_take_at(w,d)
    if (w or "")=="" then return false end
    WARP_WORLD(w,d); sleep(250)
    SMART_RECONNECT(w,d)
    txafterwarp, tyafterwarp = b.x, b.y

    local MAX_ROUNDS, WAIT_MS = 10, 1200
    local got=false
    ZEE_COLLECT(true)
    local ok, err = pcall(function()
      for _=1,MAX_ROUNDS do
        if inv:getItemCount(TARGET_ID)>0 then got=true; break end
        local objs=(getObjects and getObjects()) or {}
        local me=b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
        local best,bestd2=nil,1e18
        for _,o in pairs(objs) do
          if o.id==TARGET_ID then
            local txo,tyo=math.floor(o.x/32),math.floor(o.y/32)
            if me then
              local mx,my=math.floor(me.posx/32),math.floor(me.posy/32)
              local d2=(txo-mx)*(txo-mx)+(tyo-my)*(tyo-my)
              if d2<bestd2 then best,bestd2=o,d2 end
            else best,bestd2=o,0 end
          end
        end
        if best then
          local tx,ty=math.floor(best.x/32),math.floor(best.y/32)
          SMART_RECONNECT(w,d,tx,ty); b:findPath(tx,ty); sleep(WAIT_MS)
        else
          SMART_RECONNECT(w,d); sleep(WAIT_MS)
        end
      end
    end)
    ZEE_COLLECT(false)
    return got or (inv:getItemCount(TARGET_ID)>0)
  end

  -- Coba ambil bila belum punya: storage dulu baru farm
  local got = inv:getItemCount(TARGET_ID) > 0
  if not got then
    got = _try_take_at(STORAGE_MAGNI, DOOR_MAGNI) or _try_take_at(WORLD, DOOR)
  end

  -- normalisasi: tepat 1
  do
    local storageW,storageD=STORAGE_MAGNI,DOOR_MAGNI
    if (storageW or "")=="" then storageW,storageD=WORLD,DOOR end
    if txafterwarp and tyafterwarp then
      b:findPath(txafterwarp, tyafterwarp); sleep(400); faceSide2()
    end
    _ensure_single_item_in_storage(10158,1,storageW,storageD,
      {chunk=200,step_ms=600,path_try=10,tile_cap=4000,stack_cap=20,tile_retries=2})
  end

  -- Hasil akhir & manajemen gagal/berhasil
  if inv:getItemCount(10158)>0 then
    b:wear(10158); sleep(250)
    _reset_fail(CD_WORLD)
    return true
  else
    local fails = _inc_fail(CD_WORLD)
    print(string.format("[TAKE_MAGNI] Gagal #%d di %s", fails, CD_WORLD))
    if fails >= (MAGNI_FAILS_MAX_TRY or 3) then
      _set_cd(CD_WORLD)
      print(string.format("[TAKE_MAGNI] Set cooldown %s (%d menit) setelah %d gagal.",
        CD_WORLD, MAGNI_COOLDOWN_MIN or 10, fails))
      _reset_fail(CD_WORLD)
    end
    return false
  end
end




-------------------- HARVEST --------------------
--------------------------------------------------------------------
--------------------------------------------------------------------
-- KONFIG: mode 5 tile terpusat (kiri 2, tengah, kanan 2)
TILE_WINDOW  = tonumber(TILE_WINDOW or 5)     -- harus ganjil; 5 = [-2..2]
CENTERED     = true                           -- pakai anchor di tengah window
local HALF_W = math.floor((TILE_WINDOW - 1) / 2)   -- 2 untuk window 5
local OFFSETS_CENTER = {}
for m = -HALF_W, HALF_W do table.insert(OFFSETS_CENTER, m) end
local TILE_STEP  = TILE_WINDOW                 -- langkah anchor per iterasi
--------------------------------------------------------------------

-- util yang dipakai
local function _sorted_rows_and_bounds(b)
  local rows_map, bounds = {}, {}
  local w = b:getWorld()
  for _, t in pairs(_get_tiles()) do
    local tile = w:getTile(t.x, t.y)
    if tile and tile.fg == ITEM_SEED_ID and tile:canHarvest() and hasAccess(t.x, t.y) > 0 then
      rows_map[t.y] = true
      local bd = bounds[t.y]
      if not bd then
        bounds[t.y] = {min_x = t.x, max_x = t.x}
      else
        if t.x < bd.min_x then bd.min_x = t.x end
        if t.x > bd.max_x then bd.max_x = t.x end
      end
    end
  end
  local rows = {}
  for y,_ in pairs(rows_map) do table.insert(rows, y) end
  table.sort(rows)
  return rows, bounds
end

local function _at_tile(b, x, y)
  local w = b:getWorld(); local me = w and w:getLocal() or nil
  return me and (math.floor(me.posx/32)==x and math.floor(me.posy/32)==y)
end

local function _valid_seed_tile(w, x, y)
  local t = w:getTile(x, y)
  return t and t.fg == ITEM_SEED_ID and t:canHarvest() and hasAccess(x, y) > 0
end

--------------------------------------------------------------------
-- HARVEST_PASS: panen 5 tile terpusat (kiri 2, tengah, kanan 2)
--------------------------------------------------------------------
function HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
  local b = getBot and getBot() or nil; if not b then return false end

  -- MAGNI seperti sebelumnya
  if USE_MAGNI then
    local inv = b:getInventory(); local have = inv:getItemCount(10158); local called = false
    if have == 0 then
      if (STORAGE_MAGNI or "") ~= "" then TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI); called = true end
      if inv:getItemCount(10158) == 0 then TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called = true end
    elseif have > 1 then TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called = true end
    if (not called) and inv:getItemCount(10158) > 0 then b:wear(10158); sleep(200) end
  end

  -- Warp & siap
  WARP_WORLD(FARM_WORLD, FARM_DOOR)
  ZEE_COLLECT(true); sleep(120); SMART_RECONNECT(FARM_WORLD, FARM_DOOR)

  local w = b:getWorld(); if not w then ZEE_COLLECT(false); return false end
  local worldW = (w.getWidth and w:getWidth()) or 200  -- fallback aman
  local did_any = false

  -- baris y yang berisi seed + batas x tiap baris
  local rows, bounds = _sorted_rows_and_bounds(b)

  for i, y in ipairs(rows) do
    _maybe_drop_cake()
    SMART_RECONNECT(FARM_WORLD, FARM_DOOR)

    local bd = bounds[y]
    if bd then
      -- agar anchor di tengah punya ruang 2 tile kiri/kanan, geser batas
      local minA = bd.min_x + HALF_W
      local maxA = bd.max_x - HALF_W
      if minA > maxA then
        -- baris terlalu sempit untuk window 5; tetap dipanen parsial via bound check
        minA, maxA = bd.min_x, bd.max_x
      end

      -- zig-zag: baris ganjil ke kanan, genap ke kiri
      local forward   = (i % 2 == 1)
      local direction = forward and 1 or -1
      local x_start   = forward and minA or maxA
      local x_end     = forward and maxA or minA
      local anchor    = x_start

      while true do
        if forward and anchor > x_end then break end
        if (not forward) and anchor < x_end then break end

        -- path ke anchor (tengah)
        local tries = 0
        while tries < 6 and not _at_tile(b, anchor, y) do
          b:findPath(anchor, y); SMART_RECONNECT(FARM_WORLD, FARM_DOOR); GUARD_DOOR_STUCK(FARM_WORLD, FARM_DOOR)
          tries = tries + 1; sleep(80)
        end

        if _at_tile(b, anchor, y) then
          -- pukul kiri 2 .. kanan 2 dari anchor
          for _, m in ipairs(OFFSETS_CENTER) do
            local hx = anchor + m
            if hx >= 0 and hx < worldW then
              local hit_cnt = 0
              while _valid_seed_tile(w, hx, y) and _at_tile(b, anchor, y) do
                b:hit(hx, y)
                sleep(DELAY_HARVEST)
                SMART_RECONNECT(FARM_WORLD, FARM_DOOR)
                GUARD_DOOR_STUCK(FARM_WORLD, FARM_DOOR)
                hit_cnt = hit_cnt + 1
                if hit_cnt >= 100 then
                  print(string.format("[HARVEST_PASS] Stop 100 hits (%d,%d)", hx, y))
                  break
                end
              end
            end
          end
          did_any = true
        end

        _maybe_drop_cake()
        if checkitemfarm and checkitemfarm(farmListActive) then ZEE_COLLECT(false); return did_any end

        -- geser anchor 5 tile (atau sesuai TILE_WINDOW)
        anchor = anchor + (direction * TILE_STEP)
      end
    end
  end

  _maybe_drop_cake()
  ZEE_COLLECT(false)
  return did_any
end


function HARVEST_UNTIL_EMPTY(FARM_WORLD, FARM_DOOR, STORAGE_WORLD, STORAGE_DOOR, farmListActive, on_tick)
  local ok,reason=warp_ok_and_public(FARM_WORLD, FARM_DOOR)
  if not ok then print("[HARVEST] Skip world (warp/public/door fail):", FARM_WORLD, reason); return end

  local t0=os.time()
  while true do
    if on_tick then pcall(on_tick, FARM_WORLD) end
    local did=HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
    if on_tick then pcall(on_tick, FARM_WORLD) end

    if checkitemfarm(farmListActive) then
      DROP_ITEMS_SNAKE(STORAGE_WORLD, STORAGE_DOOR, farmListActive, {tile_cap=3000, stack_cap=20})
      _maybe_drop_cake()
    end

    if (not did) and (not checkitemfarm(farmListActive)) then
      if not has_harvestables() then print("[HARVEST] Selesai world:", FARM_WORLD); break end
    end
  end
  if has_any_item_farm(farmListActive) then
    DROP_ITEMS_SNAKE(STORAGE_WORLD, STORAGE_DOOR, farmListActive, {tile_cap=3000, stack_cap=20})
  end
  ZEE_COLLECT(false)
  log_success(FARM_WORLD, FARM_DOOR, os.time()-t0)
end

-------------------- RR/CHUNK MODE --------------------
local function _parse_world_entry(s)
  local farmW,farmD,idstr,storeW,storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW or not idstr then return nil end
  return (farmW or ""):upper(), (farmD or ""), tonumber(idstr), (storeW or ""):upper(), (storeD or "")
end

function RUN_MULTI_HARVEST(list_world)
  if USE_MAGNI then TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI) end
  local old_block,old_seed=ITEM_BLOCK_ID, ITEM_SEED_ID
  local specs={}
  for idx,entry in ipairs(list_world or {}) do
    local W,D,BID,SW,SD=_parse_world_entry(entry)
    if W and BID then
      ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
      local perworld={ITEM_BLOCK_ID, ITEM_SEED_ID}
      print(("[MULTI] %d) %s|%s BLOCK=%d SEED=%d -> %s|%s"):format(idx,W,D,ITEM_BLOCK_ID,ITEM_SEED_ID,SW,SD))
      local ok,reason=warp_ok_and_public(W,D)
      if not ok then print(("⏭ Skip %s (%s)"):format(W, tostring(reason))); goto cont end
      specs[#specs+1]={storageW=SW, storageD=SD, farmItems=perworld}
      HARVEST_UNTIL_EMPTY(W,D,SW,SD,perworld)
      ::cont::
    else print("[MULTI] Entry invalid: "..tostring(entry)) end
  end
  ITEM_BLOCK_ID,ITEM_SEED_ID=old_block,old_seed
  print("[MULTI] Final drop per-world...")
  for _,sp in ipairs(specs) do DROP_ITEMS_SNAKE(sp.storageW, sp.storageD, sp.farmItems, {tile_cap=3000, stack_cap=20}) end
  if (STORAGE_CAKE or "")~="" and has_any_cake() then pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20}) end) end
  local b=getBot and getBot() or nil; if b and b.leaveWorld then b:leaveWorld() end; sleep(900); if b then b.auto_reconnect=true end
  print("[MULTI] Done.")
end

-------------------- TXT QUEUE (assist: "stale" / "always") --------------------
local function _read_lines(path)
  local t, f={}, io.open(path,"r"); if not f then return t end
  for line in f:lines() do line=line:gsub("\r",""):gsub("\n",""); if line~="" and not line:match("^%s*;") then table.insert(t,line) end end
  f:close(); return t
end
local function _write_lines(path, lines) local f=io.open(path,"w"); if not f then return false end; for _,ln in ipairs(lines or {}) do f:write(ln.."\n") end; f:close(); return true end
local function _append_line(path,line) local f=io.open(path,"a"); if not f then return false end; f:write(line.."\n"); f:close(); return true end
local function _now() return os.time() end

-- TAMBAHKAN KODE DARI ARTIFACT DI SINI
local function _parse_world_line(s)
  local farmW,farmD,bid,storeW,storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW then return nil end
  return farmW:upper(), (farmD or ""), tonumber(bid), (storeW or ""):upper(), (storeD or "")
end

-- File locking utilities untuk mencegah race condition
-- File locking utilities: atomic via mkdir (cross-platform)
local function _acquire_lock(lockname, timeout_sec)
  timeout_sec = timeout_sec or 5
  local is_windows = package.config:sub(1,1) == "\\"
  local lockdir    = _pjoin(LOCK_DIR, lockname .. ".lck")
  local deadline   = os.time() + timeout_sec

  while os.time() < deadline do
    local cmd = is_windows
      and ('cmd /C mkdir "%s" >NUL 2>&1'):format(lockdir)
      or  ('mkdir "%s" >/dev/null 2>&1'):format(lockdir)

    local ret = os.execute(cmd)
    local ok  = (ret == true) or (ret == 0)  -- Lua 5.1/5.4 kompatibel

    if ok then
      -- simpan owner lock (opsional, buat debugging)
      local f = io.open(_pjoin(lockdir, "owner.txt"), "w")
      if f then f:write(tostring(os.time()) .. "|" .. (WORKER_ID or "?")); f:close() end
      return true
    end
    sleep(100) -- 100 ms
  end
  return false
end

local function _release_lock(lockname)
  local is_windows = package.config:sub(1,1) == "\\"
  local lockdir    = _pjoin(LOCK_DIR, lockname .. ".lck")
  if is_windows then
    os.execute(('cmd /C rmdir /Q /S "%s" >NUL 2>&1'):format(lockdir))
  else
    os.execute(('rm -rf "%s" >/dev/null 2>&1'):format(lockdir))
  end
end


-- Fungsi atomic untuk menambahkan helper dengan limit check
-- Fungsi untuk menghitung helper aktif dengan double-check
local function _count_helpers_for_world_safe(world)
  world = (world or ""):upper()
  if world == "" then return 0, nil end
  
  local rows = _read_lines(JOB_FILES.inprogress)
  local owner_worker = nil
  local helpers = {}
  
  -- Cari owner (entry dengan timestamp terkecil)
  local oldest_ts = math.huge
  for _, ln in ipairs(rows) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and (w:upper() == world) then
      local timestamp = tonumber(ts) or math.huge
      if timestamp < oldest_ts then
        oldest_ts = timestamp
        owner_worker = who
      end
    end
  end
  
  -- Hitung helper (semua worker selain owner)
  for _, ln in ipairs(rows) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and (w:upper() == world) and (who ~= owner_worker) then
      helpers[who] = true
    end
  end
  
  local helper_count = 0
  for _ in pairs(helpers) do helper_count = helper_count + 1 end
  
  return helper_count, owner_worker
end

-- Fungsi atomic untuk menambahkan helper dengan limit check + rollback anti-race
local function _add_helper_atomic(world)
  world = (world or ""):upper()
  if world == "" then return false, "invalid_world" end

  local lockname = "assist_" .. world
  if not _acquire_lock(lockname, 3) then
    return false, "lock_timeout"
  end

  local success, reason = false, "unknown"
  local limit = tonumber(ASSIST_HELPER_LIMIT) or 0
  local just_added = false

  -- Critical section (terlindungi lock)
  do
    local rows = _read_lines(JOB_FILES.inprogress)

    -- 1) Cegah duplikat diri sendiri
    for _, ln in ipairs(rows) do
      local w, who = ln:match("^([^|]+)|([^|]+)|")
      if w and who and (w:upper() == world) and (who == WORKER_ID) then
        success, reason = true, "already_helper"
        break
      end
    end

    if not success then
      -- 2) Tentukan owner = timestamp paling tua (tie-breaker: who terkecil)
      local owner_worker, oldest_ts = nil, math.huge
      for _, ln in ipairs(rows) do
        local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
        if w and who and ts and (w:upper() == world) then
          local t = tonumber(ts) or math.huge
          if (t < oldest_ts) or (t == oldest_ts and (owner_worker == nil or who < owner_worker)) then
            oldest_ts, owner_worker = t, who
          end
        end
      end

      -- 3) Hitung helper unik (selain owner)
      local helpers = {}
      for _, ln in ipairs(rows) do
        local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
        if w and who and ts and (w:upper() == world) and (who ~= owner_worker) then
          helpers[who] = true
        end
      end
      local helper_count = 0
      for _ in pairs(helpers) do helper_count = helper_count + 1 end

      if helper_count >= limit then
        success, reason = false, "limit_reached"
      else
        -- 4) Tambah entry helper kita
        if _append_line(JOB_FILES.inprogress, string.format("%s|%s|%d", world, WORKER_ID, _now())) then
          success, reason, just_added = true, "added", true
        else
          success, reason = false, "file_error"
        end
      end
    end

    -- 5) Safety re-check (rollback) — tetap di DALAM lock & TANPA call fungsi lain (hindari deadlock)
    if success and reason == "added" and just_added then
      local rows2 = _read_lines(JOB_FILES.inprogress)

      -- cari owner terbaru
      local owner_worker2, oldest_ts2 = nil, math.huge
      for _, ln in ipairs(rows2) do
        local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
        if w and who and ts and (w:upper() == world) then
          local t = tonumber(ts) or math.huge
          if (t < oldest_ts2) or (t == oldest_ts2 and (owner_worker2 == nil or who < owner_worker2)) then
            oldest_ts2, owner_worker2 = t, who
          end
        end
      end

      -- hitung helper lagi
      local helpers2 = {}
      for _, ln in ipairs(rows2) do
        local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
        if w and who and ts and (w:upper() == world) and (who ~= owner_worker2) then
          helpers2[who] = true
        end
      end
      local new_count = 0
      for _ in pairs(helpers2) do new_count = new_count + 1 end

      if new_count > limit then
        -- rollback: hapus entry kita (bukan owner)
        local out, removed = {}, false
        for _, ln in ipairs(rows2) do
          local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
          if w and who and (w:upper() == world) and (who == WORKER_ID) and (who ~= owner_worker2) and (not removed) then
            removed = true -- skip satu entry milik kita
          else
            table.insert(out, ln)
          end
        end
        if removed then _write_lines(JOB_FILES.inprogress, out) end
        success, reason = false, "limit_reached_race"
        -- (opsional) print debug:
        print(string.format("[HELP][ROLLBACK] %s di %s (new_count=%d > limit=%d)", WORKER_ID, world, new_count, limit))
      end
    end
  end

  _release_lock(lockname)
  return success, reason
end





-- Cleanup helper dengan lock protection
local function _remove_helper_entry_safe(world, worker_id)
  world = (world or ""):upper()
  worker_id = worker_id or WORKER_ID
  
  local lockname = "assist_" .. world
  if not _acquire_lock(lockname, 3) then
    print(string.format("[HELPER] Tidak bisa hapus %s dari %s - lock timeout", worker_id, world))
    return false
  end
  
  local removed = false
  
  -- Critical section
  do
    local rows = _read_lines(JOB_FILES.inprogress)
    local out = {}
    local owner_worker = nil
    
    -- Cari owner (entry terlama)
    local oldest_ts = math.huge
    for _, ln in ipairs(rows) do
      local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
      if w and who and ts and (w:upper() == world) then
        local timestamp = tonumber(ts) or math.huge
        if timestamp < oldest_ts then
          oldest_ts = timestamp
          owner_worker = who
        end
      end
    end
    
    -- Filter out helper entry (bukan owner)
    for _, ln in ipairs(rows) do
      local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
      if w and who and (w:upper() == world) and (who == worker_id) and (who ~= owner_worker) then
        removed = true
        -- Skip entry ini (tidak masuk ke out)
      else
        table.insert(out, ln)
      end
    end
    
    if removed then
      _write_lines(JOB_FILES.inprogress, out)
    end
  end
  
  _release_lock(lockname)
  
  if removed then
    print(string.format("[HELPER] %s removed from %s helpers", worker_id, world))
  end
  
  return removed
end

-- Cek apakah world masih punya job (masih ada di worlds.txt)
local function _world_has_job(world)
  world = (world or ""):upper()
  if world == "" then return false end
  local rows = _read_lines(JOB_FILES.worlds)
  for _, ln in ipairs(rows) do
    local W = ln:match("^([^|]+)")
    if W and W:upper() == world then return true end
  end
  return false
end

-- REPLACE fungsi PICK_ASSIST_WORLD yang lama dengan ini:
local function PICK_ASSIST_WORLD(mode)
  local prog = _read_lines(JOB_FILES.inprogress)
  if #prog == 0 then return nil, false end

  -- Pilih world kandidat milik orang lain (terlama heartbeat)
  local best, best_age, best_owner = nil, -1, nil
  local now = _now()
  
  for _, ln in ipairs(prog) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who ~= WORKER_ID then
      local age = now - tonumber(ts)
      if age > best_age then
        best, best_age, best_owner = w:upper(), age, who
      end
    end
  end
  
  if not best then return nil, false end

  -- Jika world sudah tidak ada di worlds.txt → cleanup & skip
  if not _world_has_job(best) then
    _cleanup_stale_inprogress(best)
    return nil, false
  end

  if mode == "stale" then
    -- Mode stale: bantu hanya jika macet >= STALE_SEC dan boleh steal
    if best_age < (STALE_SEC or 90) or not STEAL_HELP then
      return nil, false
    end

    -- Steal owner → set owner jadi kita di inprogress
    local rows = _read_lines(JOB_FILES.inprogress)
    local out, stolen = {}, false
    for _, ln in ipairs(rows) do
      local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
      if w and who and ts and w:upper() == best then
        table.insert(out, string.format("%s|%s|%d", w:upper(), WORKER_ID, _now()))
        stolen = true
      else
        table.insert(out, ln)
      end
    end
    if stolen then _write_lines(JOB_FILES.inprogress, out) end
    return best, true
    
  else
    -- Mode "always": bantu dengan atomic limit checking
    local success, reason = _add_helper_atomic(best)
    print("[HELP-RESULT]", WORKER_ID, best, ok and "OK" or "FAIL", why)
    if success then
      if reason == "added" then
        print(string.format("[HELP] %s bergabung sebagai helper di %s", WORKER_ID, best))
      elseif reason == "already_helper" then
        print(string.format("[HELP] %s sudah terdaftar sebagai helper di %s", WORKER_ID, best))
      end
      return best, false
    else
      if reason == "limit_reached" then
        print(string.format("[HELP] %s tidak bisa bantu %s - helper limit tercapai (%d/%d)", 
          WORKER_ID, best, ASSIST_HELPER_LIMIT, ASSIST_HELPER_LIMIT))
      elseif reason == "lock_timeout" then
        print(string.format("[HELP] %s tidak bisa bantu %s - lock timeout", WORKER_ID, best))
      end
      return nil, false
    end
  end
end

local function _set_of_worlds(lines) local S={}; for _,ln in ipairs(lines) do local w=ln:match("^([^|]+)"); if w then S[w:upper()]=true end end; return S end

local function _update_heartbeat(world, who_slot)
  world=(world or ""):upper(); who_slot=who_slot or WORKER_ID
  local now=_now(); local rows=_read_lines(JOB_FILES.inprogress); local out,touched={},false
  for _,ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts then
      if w:upper()==world and who==who_slot then table.insert(out, string.format("%s|%s|%d", w, who_slot, now)); touched=true
      else table.insert(out, ln) end
    end
  end
  if not touched then table.insert(out, string.format("%s|%s|%d", world, who_slot, now)) end
  _write_lines(JOB_FILES.inprogress, out)
end

local function CLAIM_NEXT_JOB()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog=_read_lines(JOB_FILES.inprogress)
  local done=_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog), _set_of_worlds(done)
  for _,ln in ipairs(worlds) do
    local W=ln:match("^([^|]+)")
    if W and (not S_prog[W:upper()]) and (not S_done[W:upper()]) then
      _append_line(JOB_FILES.inprogress, string.format("%s|%s|%d", W:upper(), WORKER_ID, _now()))
      return ln
    end
  end
  return nil
end

local function MARK_DONE(world)
  world=(world or ""):upper()
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if w and w:upper()~=world then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress, out)
  _append_line(JOB_FILES.done, string.format("%s|%s|%d", world, WORKER_ID, _now()))
end

local function QUEUE_STATS()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog=_read_lines(JOB_FILES.inprogress)
  local done=_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog), _set_of_worlds(done)
  local total,unclaimed,inprog,ndone=0,0,0,0
  for _,ln in ipairs(worlds) do
    local W=(ln:match("^([^|]+)") or ""):upper()
    if W~="" then
      total=total+1
      local is_prog=S_prog[W] and true or false
      local is_done=S_done[W] and true or false
      if (not is_prog) and (not is_done) then unclaimed=unclaimed+1 end
      if is_prog then inprog=inprog+1 end
      if is_done then ndone=ndone+1 end
    end
  end
  return {total=total, unclaimed=unclaimed, inprogress=inprog, done=ndone}
end

--- ################### pick asis
-- Hitung jumlah WORKER_ID unik yang terdaftar untuk sebuah world di inprogress.txt
local function _count_unique_workers(world)
  world = (world or ""):upper()
  if world == "" then return 0 end
  local rows = _read_lines(JOB_FILES.inprogress)
  local S = {}
  for _, ln in ipairs(rows) do
    local w, who = ln:match("^([^|]+)|([^|]+)|")
    if w and who and (w:upper() == world) then S[who] = true end
  end
  local n = 0
  for _ in pairs(S) do n = n + 1 end
  return n
end


-- Bersihkan semua entry inprogress untuk world tertentu (owner/helpers yang nyangkut)
local function _cleanup_stale_inprogress(world)
  world = (world or ""):upper()
  if world == "" then return end
  local rows = _read_lines(JOB_FILES.inprogress)
  local out = {}
  for _, ln in ipairs(rows) do
    local W = ln:match("^([^|]+)")
    if not (W and W:upper() == world) then
      table.insert(out, ln)
    end
  end
  _write_lines(JOB_FILES.inprogress, out)
end




-- ################


local function RECONCILE_QUEUE()
  local worlds=_read_lines(JOB_FILES.worlds)
  local done=_read_lines(JOB_FILES.done); local S_done=_set_of_worlds(done)
  local out={}
  for _,ln in ipairs(worlds) do local W=ln:match("^([^|]+)") or ""; if W~="" and (not S_done[W:upper()]) then table.insert(out, ln) end end
  _write_lines(JOB_FILES.worlds, out)
end

local function SPEC_FOR_WORLD(W)
  local worlds=_read_lines(JOB_FILES.worlds)
  for _,ln in ipairs(worlds) do local w,d,bid,sw,sd=_parse_world_line(ln); if w and w==(W or ""):upper() then return w,d,bid,sw,sd end end
  return nil
end

local function FIND_OWN_INPROGRESS()
  local rows=_read_lines(JOB_FILES.inprogress); local bestW,bestTS=nil,-1
  for _,ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who==WORKER_ID then local t=tonumber(ts) or 0; if t>bestTS then bestTS,bestW=t,(w or ""):upper() end end
  end
  return bestW
end

local function UNCLAIM(world)
  world=(world or ""):upper()
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if w and w:upper()~=world then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress, out)
end



function RUN_FROM_TXT_QUEUE()
  -- Auto-resume by SLOT
  local resumeW = FIND_OWN_INPROGRESS()
  if resumeW then
    local W,D,BID,SW,SD = SPEC_FOR_WORLD(resumeW)
    if W and BID then
      ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
      print(string.format("[RESUME] %s lanjut %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
      local hb = function(world) _update_heartbeat(world, WORKER_ID) end
      _update_heartbeat(W, WORKER_ID)
      HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)
      MARK_DONE(W); RECONCILE_QUEUE()
      print(string.format("[RESUME] %s selesai %s", WORKER_ID, W))
    else
      print(string.format("[RESUME] Spec %s tidak ditemukan; unclaim.", tostring(resumeW)))
      UNCLAIM(resumeW)
    end
  end

  while true do
    -- Klaim baru
    local job = CLAIM_NEXT_JOB()
    if job then
      local W,D,BID,SW,SD = _parse_world_line(job)
      if W and BID then
        ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
        print(string.format("[JOB] %s klaim %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
        local hb = function(world) _update_heartbeat(world, WORKER_ID) end
        _update_heartbeat(W, WORKER_ID)
        HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)
        MARK_DONE(W); RECONCILE_QUEUE()
        print(string.format("[JOB] %s selesai %s", WORKER_ID, W))
      end

    else
      -- Tidak ada yang bisa diklaim
      local qs = QUEUE_STATS()

      -- Gating: kalau "stale", TUNGGU sampai unclaimed==0; kalau "always", langsung boleh assist
      if ASSIST_MODE ~= "always" and qs.unclaimed > 0 then
        print(string.format("[QUEUE] Masih ada %d world belum diklaim. Menunggu...", qs.unclaimed))
        sleep(800)
      else
        local assistW, stolen = PICK_ASSIST_WORLD(ASSIST_MODE)

        -- Guard: anti-spam & limit helper
        if assistW then
          -- skip kalau world sudah tidak punya job
          if not _world_has_job(assistW) then
            _cleanup_stale_inprogress(assistW)
            assistW = nil
          end
        end

        if assistW then
          print(string.format("[HELP] %s bantu %s (mode=%s%s)",
            WORKER_ID, assistW, ASSIST_MODE, stolen and " +steal" or ""))
          local worlds = _read_lines(JOB_FILES.worlds)
          for _,ln in ipairs(worlds) do
            local W,D,BID,SW,SD = _parse_world_line(ln)
            if W == assistW then
              ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
              local hb = function(world) _update_heartbeat(world, WORKER_ID) end
              _update_heartbeat(W, WORKER_ID)
              HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)

              -- MARK_DONE hanya jika owner pindah ke kita (steal pada mode "stale")
              local rows = _read_lines(JOB_FILES.inprogress)
              local owner_now = nil
              local oldest_ts = math.huge
              
              -- Cari owner berdasarkan timestamp terlama
              for _,ll in ipairs(rows) do
                local ww,who,ts = ll:match("^([^|]+)|([^|]+)|(%d+)$")
                if ww and who and ts and ww:upper() == W then
                  local timestamp = tonumber(ts) or math.huge
                  if timestamp < oldest_ts then
                    oldest_ts = timestamp
                    owner_now = who
                  end
                end
              end
              
              if owner_now == WORKER_ID then
                MARK_DONE(W); RECONCILE_QUEUE()
                print(string.format("[HELP] %s menutup %s sebagai owner", WORKER_ID, W))
              else
                -- Kita cuma helper, hapus entry helper kita setelah selesai bantu
                _remove_helper_entry_safe(W, WORKER_ID)
                print(string.format("[HELP] %s selesai bantu %s sebagai helper", WORKER_ID, W))
              end
              break
            end
          end
        else
          -- Tidak ada aktif sama sekali
          local qs2 = QUEUE_STATS()
          if LOOP_MODE then
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job aktif (total=%d, inprog=%d, done=%d). Menunggu...",
              qs2.total, qs2.inprogress, qs2.done))
            -- idle actions
            if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
              pcall(function()
                DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList,
                  {tile_cap=3000, stack_cap=20})
              end)
            end
            local b=getBot and getBot() or nil
            if b and b.leaveWorld then b:leaveWorld() end
            sleep(1000)
            if b then b.auto_reconnect = true end
            sleep(1200)
          else
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job aktif (total=%d, inprog=%d, done=%d). LOOP_MODE=false -> exit.",
              qs2.total, qs2.inprogress, qs2.done))
            break
          end
        end
      end
    end
    sleep(350)
  end

  -- Final cleanup
  if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
    pcall(function()
      DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList,
        {tile_cap=3000, stack_cap=20})
    end)
  end
  local b=getBot and getBot() or nil
  if b and b.leaveWorld then b:leaveWorld() end
  sleep(900)
  if b then b.auto_reconnect = true end
end


-------------------- MAIN --------------------
do
  ASSIGN_MODE=(ASSIGN_MODE or "rr"):lower():gsub("%s+",""); if ASSIGN_MODE~="rr" and ASSIGN_MODE~="chunk" then ASSIGN_MODE="rr" end
  print(string.format("[CONFIG] SLOT=%d | WORKER_ID=%s | USE_TXT_QUEUE=%s | ASSIST_MODE=%s | ASSIGN_MODE=%s",
    MY_SLOT, WORKER_ID, tostring(USE_TXT_QUEUE), ASSIST_MODE, ASSIGN_MODE))

  if USE_TXT_QUEUE then
    RUN_FROM_TXT_QUEUE()
  else
    local myList=build_worlds_for_bot(LIST_WORLD, MY_SLOT, TOTAL_BOTS, FARM_PER_BOT, ASSIGN_MODE)
    print(string.format("[CHECK] I am slot %d of %d (mode=%s)", MY_SLOT, TOTAL_BOTS, ASSIGN_MODE))
    if #myList==0 then print(string.format("[ASSIGN] SLOT %d tidak mendapat world. Cek TOTAL_BOTS/ASSIGN_MODE/ROTATE_LIST.", MY_SLOT))
    else
      print("[CHECK] Worlds assigned to me:"); for i,w in ipairs(myList) do print(string.format("  %02d) %s", i,w)) end
      RUN_MULTI_HARVEST(myList)
    end
  end
end
