----------------------------------------------------------------
-- MULTI WORLD HARVEST + DROP SNAKE (ANTI-SKIP 2 TILE)
-- + TXT JOB QUEUE (worlds.txt / inprogress.txt / done.txt) + WORK-STEALING
-- + AUTO-RESUME + RECONCILE_QUEUE
-- + WARP TAHAN BANTING (NUKED + PUBLIC + BAD_DOOR + SAFE TILE)
-- + GUARD: ANTI-STUCK di WHITE DOOR (fg==6)
-- + USE_MAGNI (keep=1, sisanya drop ke storage, wear sekali)
-- + DROP canggih: cek FG kosong, stance walkable, reachability aware, clamp kanan<=99, atas<=23, fallback kiri
-- + Idle housekeeping anti-spam + deteksi EXIT
-- + JOB OWNER = SLOT-<NN> (bukan nama bot)
----------------------------------------------------------------

-- ===================== PATH DESKTOP + HELPERS =====================
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/JOB-ANDRE/"):gsub("[/\\]?$", "/")

local function _ensure_dir(p)
  local is_windows = package.config:sub(1,1) == "\\"
  if is_windows then
    os.execute(('if not exist "%s" mkdir "%s"'):format(p, p))
  else
    os.execute(('mkdir -p "%s"'):format(p))
  end
end

local function _pjoin(base, name)
  return (base or "") .. (name or "")
end

_ensure_dir(extraFilePath)

-- ===================== KONFIG UTAMA =====================
USE_TXT_QUEUE = true           -- pakai worlds.txt + work-stealing
STEAL_HELP    = true           -- bantu job lain (stale)
STALE_SEC     = 30*60          -- stale 30 menit
LOOP_MODE     = LOOP_MODE ~= nil and LOOP_MODE or true  -- idle: true=standby, false=keluar

-- Idle housekeeping (anti spam leave)
IDLE_ACTION_COOLDOWN = IDLE_ACTION_COOLDOWN or 60
local __last_idle_action = 0

-- MAGNI / HARVEST
USE_MAGNI     = true
DELAY_HARVEST = 170

-- Storage CAKE (global)
STORAGE_CAKE, DOOR_CAKE = "HVKKLL", "XX1"
cakeList  = {1058,1094,1096,1098,1828,3870,7058,10134,10136,10138,10140,10142,10146,10150,10164,10228,11286}

-- Storage MAGNI (opsional)
STORAGE_MAGNI, DOOR_MAGNI = "HVKKLL", "XX2"  -- lokasi kacamata (10158)

-- TXT queue files
JOB_FILES = {
  worlds     = _pjoin(extraFilePath, "worlds.txt"),
  inprogress = _pjoin(extraFilePath, "inprogress.txt"),
  done       = _pjoin(extraFilePath, "done.txt"),
}
-- Log files
FAIL_LOG_FILE    = _pjoin(extraFilePath, "warp_fail.log")
SUCCESS_LOG_FILE = _pjoin(extraFilePath, "warp_success.log")

-- Persiapan file
local function _touch(path) local f=io.open(path,"a"); if f then f:close() end end
_touch(JOB_FILES.worlds); _touch(JOB_FILES.inprogress); _touch(JOB_FILES.done)

-- RR/Chunk (non-TXT)
TOTAL_BOTS   = 8
FARM_PER_BOT = FARM_PER_BOT or 0
ASSIGN_MODE  = ASSIGN_MODE or "rr"
ROTATE_LIST  = (ROTATE_LIST ~= nil) and ROTATE_LIST or false
ROTATE_SEED  = ROTATE_SEED or 12345

-- Global flags
NUKED_STATUS    = NUKED_STATUS    or false
WORLD_IS_PUBLIC = WORLD_IS_PUBLIC or nil

-- Guard WHITE DOOR
CURRENT_WORLD_TARGET, CURRENT_DOOR_TARGET = nil, nil
local __door6_ticks, __last_mx, __last_my = 0, nil, nil

-- Delay default
SMART_DELAY      = false
DELAY_RECONNECT  = 20000
DELAY_BAD_SERVER = 120000
DELAY_PNB        = 175
DELAY_PLACE      = 115
DELAY_WARP       = 7000
DELAY_TRASH      = 100

-- Default (override per-world)
ITEM_BLOCK_ID = 4584
ITEM_SEED_ID  = ITEM_BLOCK_ID + 1

-- ===================== BOT INIT =====================
do local b = getBot and getBot() or nil
  if b then b.collect_range = 4; b.move_range = 4; b.dynamic_delay = true end
end

-- ===================== UTIL / STATUS / PING =====================
function UPDATE_DELAY_BY_PING()
  if not SMART_DELAY then return end
  local b = getBot and getBot() or nil
  local P = (b and b.getPing and b:getPing()) or 0
  if P == 0 then P = 200 end
  if P <= 150 then return end
  DELAY_RECONNECT = math.max(20000, P*200)
  DELAY_BAD_SERVER= math.max(120000, P*600)
  DELAY_PNB       = P
  DELAY_PLACE     = math.floor(P*0.7)
  DELAY_WARP      = math.max(5000, P*30)
  DELAY_TRASH     = math.max(100, math.floor(P*0.5))
end

function STATUS_BOT_NEW()
  local b = getBot and getBot() or nil
  local s = b and b.status or nil
  local Status = "Unknown"
  if (s == BotStatus.online) or (s == 1) then Status = "online"
  elseif (s == BotStatus.offline) or (s == 0) then Status = "offline"
  elseif s == BotStatus.wrong_password then Status = "Wrong Password"
  elseif s == BotStatus.account_banned then Status = "Banned"
  elseif s == BotStatus.location_banned then Status = "Location Banned"
  elseif s == BotStatus.version_update then Status = "Version Update"
  elseif s == BotStatus.advanced_account_protection then Status = "Advanced Account Protection"
  elseif s == BotStatus.server_overload then Status = "Server Overload"
  elseif s == BotStatus.too_many_login then Status = "Too Many Login"
  elseif s == BotStatus.maintenance then Status = "Maintenance"
  elseif s == BotStatus.http_block then Status = "Http Block"
  elseif s == BotStatus.captcha_requested then Status = "Captcha Requested"
  elseif s == BotStatus.error_connecting then Status = "Error Connecting"
  elseif s == BotStatus.high_ping then Status = "High Ping"
  elseif s == BotStatus.logon_fail then Status = "Logon Fail"
  else Status = tostring(s or "nil") end

  local world_name = ""
  if b and b.getWorld then local w=b:getWorld(); if w and w.name then world_name=(w.name or ""):upper() end end
  local inv = (b and b.getInventory and b:getInventory()) or nil
  return { world = world_name, name = (b and b.name) or "", level = (b and b.level) or 0,
           status= Status, gems = (b and b.gem_count) or 0, slots = (inv and inv.slotcount) or 0 }
end

function SMART_RECONNECT(WORLD, DOOR, POSX, POSY)
  UPDATE_DELAY_BY_PING()
  while (STATUS_BOT_NEW().status == "Maintenance") or (STATUS_BOT_NEW().status == "Version Update")
        or (STATUS_BOT_NEW().status == "Advanced Account Protection") or (STATUS_BOT_NEW().status == "Http Block")
        or (STATUS_BOT_NEW().status == "Logon Fail") do
    local bot=getBot and getBot() or nil
    if bot and bot.connect then bot:connect() elseif type(connect)=="function" then connect() end
    sleep(DELAY_BAD_SERVER)
  end
  while (STATUS_BOT_NEW().status == "Banned") do print("[SMART_RECONNECT] Banned. Waiting..."); sleep(DELAY_BAD_SERVER) end
  while (STATUS_BOT_NEW().status ~= "online") or (STATUS_BOT_NEW().status == "High Ping")
        or (STATUS_BOT_NEW().status == "Server Overload") do
    local bot=getBot and getBot() or nil
    if bot and bot.connect then bot:connect() elseif type(connect)=="function" then connect() end
    sleep(DELAY_RECONNECT)
  end

  if WORLD and DOOR then WARP_WORLD((WORLD or ""):upper(), DOOR)
  elseif WORLD then       WARP_WORLD((WORLD or ""):upper()) end

  if POSX and POSY then local b=getBot and getBot() or nil; if b and b.findPath then b:findPath(POSX,POSY) end end
end

-- ===================== WORLD/DOOR HELPERS =====================
local function _get_tiles()
  return (type(getTilesSafe)=="function" and getTilesSafe())
      or (type(getTiles)=="function" and getTiles())
      or {}
end

function _current_world_upper()
  local b=getBot and getBot() or nil
  local w=b and b.world or ""
  if (not w or w=="") and b and b.getWorld then local ww=b:getWorld(); if ww and ww.name then w=ww.name end end
  return (w or ""):upper()
end

local function _current_tile_fg()
  local b = getBot and getBot() or nil
  if not (b and b.getWorld) then return -1 end
  local okW, w = pcall(function() return b:getWorld() end); if not okW or not w then return -1 end
  local okL, me = pcall(function() return w:getLocal() end); if not okL or not me then return -1 end
  local tx = math.floor((me.posx or 0)/32)
  local ty = math.floor((me.posy or 0)/32)
  local okT, t = pcall(function() return w:getTile(tx, ty) end); if not okT or not t then return -1 end
  return t.fg or -1
end

local function _current_tile_fg_safe(polls, wait_ms)
  polls   = polls or 12
  wait_ms = wait_ms or 120
  for _=1,polls do local fg = _current_tile_fg(); if fg and fg >= 0 then return fg end; sleep(wait_ms) end
  return -1
end

function ZEE_COLLECT(state)
  local b=getBot and getBot() or nil; if not b then return end
  if state then b.auto_collect=true; b.ignore_gems=true; b.collect_range=3; b.object_collect_delay=200
  else b.auto_collect=false end
end

function faceSide2()
  local b = getBot and getBot() or bot; if not b then return end
  local packet = GameUpdatePacket.new(); packet.type=0; packet.flags=32; b:sendRaw(packet)
end

-- ===================== EXIT DETECTION =====================
function IS_IN_EXIT()
  local b = getBot and getBot() or nil
  if not b or not b.getWorld then return true end
  local okW, w = pcall(function() return b:getWorld() end)
  if not okW or not w then return true end
  local name = ((w.name or b.world or "") .. ""):upper()
  if name == "EXIT" or name == "" then return true end
  local okW2, width = pcall(function() return w.width end)
  if not okW2 or not width or width <= 0 then return true end
  return false
end

-- ===================== TILE FG HELPERS (AMAN) =====================
local function _world_size()
  local b=getBot and getBot() or nil
  if not (b and b.getWorld) then return 199, 59 end
  local okW,w=pcall(function() return b:getWorld() end)
  if not okW or not w then return 199, 59 end
  local ok1, W = pcall(function() return w.width end)
  local ok2, H = pcall(function() return w.height end)
  W = (ok1 and W) or 199
  H = (ok2 and H) or 59
  return W, H
end

local function _in_bounds(x,y)
  local W,H=_world_size()
  return x and y and x>=0 and y>=0 and x<=W and y<=H
end

local function _safe_tile(x,y)
  if not _in_bounds(x,y) then return nil end
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return nil end
  local okW,w=pcall(function() return b:getWorld() end); if not okW or not w then return nil end
  local okT,t=pcall(function() return w:getTile(x,y) end); if not okT then return nil end
  return t
end

local function _getTileFG(tx, ty)
  local t=_safe_tile(tx, ty)
  if not t or t.fg==nil then return -1 end
  return t.fg
end

local function _is_empty_drop_tile(tx, ty) return _getTileFG(tx, ty) == 0 end
local function _is_walkable(tx, ty) return _getTileFG(tx, ty) == 0 end

-- ===================== POSISI =====================
local function _meTile()
  local b  = getBot and getBot() or nil
  local w  = b and b.getWorld and b:getWorld() or nil
  local me = w and w.getLocal and w:getLocal() or nil
  if not me then return nil end
  return math.floor(me.posx/32), math.floor(me.posy/32)
end

-- ===================== OBJ GRID CACHE (DROP) =====================
local _OBJ_CACHE = { grid = {}, last_refresh = 0 }
local function _grid_key(x,y) return tostring(x).."|"..tostring(y) end
local function _rebuild_obj_grid()
  _OBJ_CACHE.grid = {}
  local b = getBot and getBot() or nil
  if not (b and b.getWorld) then return end
  local w = b:getWorld()
  local objs = (w.getObjects and w:getObjects()) or {}
  for _, o in pairs(objs) do
    local ox = math.floor((o.x + 16)/32)
    local oy = math.floor(o.y/32)
    local k = _grid_key(ox, oy)
    local g = _OBJ_CACHE.grid[k]
    if not g then g = {total=0, stacks=0}; _OBJ_CACHE.grid[k] = g end
    g.total  = g.total  + (o.count or 0)
    g.stacks = g.stacks + 1
  end
  _OBJ_CACHE.last_refresh = os.time()
end
local function _maybe_refresh_obj_grid()
  if (os.time() - (_OBJ_CACHE.last_refresh or 0)) >= 3 then _rebuild_obj_grid() end
end
function _countOnTile(tx, ty)
  _maybe_refresh_obj_grid()
  local g = _OBJ_CACHE.grid[tostring(tx).."|"..tostring(ty)]
  if g then return g.total, g.stacks end
  return 0, 0
end

-- ===================== PATH & GUARD =====================
local function _gotoExact(world, door, tx, ty, path_try, step_ms)
  local b = getBot and getBot() or nil; if not b then return false end
  if not _in_bounds(tx, ty) then return false end
  if _getTileFG(tx, ty) < 0 then return false end
  path_try = path_try or 10
  step_ms  = step_ms  or 700
  for _=1, path_try do
    local mx,my = _meTile()
    if mx == tx and my == ty then return true end
    b:findPath(tx, ty)
    sleep(step_ms)
    SMART_RECONNECT()
    GUARD_DOOR_STUCK()
    local mx2,my2 = _meTile()
    if mx2 == tx and my2 == ty then return true end
  end
  return false
end

-- cache tile full/bad
local FULL_CACHE, BAD_CACHE = {}, {}
local function _key(x,y) return x..":"..y end
local function mark_full(x,y) FULL_CACHE[_key(x,y)] = true end
local function mark_bad (x,y) BAD_CACHE [_key(x,y)] = true end
local function is_full_or_bad(x,y) return FULL_CACHE[_key(x,y)] or BAD_CACHE[_key(x,y)] end
local function reset_caches() FULL_CACHE = {}; BAD_CACHE = {} end

-- next tile (snake) dengan FG==0
local function _nextDropTileSnake(startX, startY, cursor, max_cols, max_rows, world_width, tile_cap, stack_cap)
  local MAX_STACK = tile_cap or 3000
  local MAX_SLOTS = stack_cap or 20
  max_cols    = max_cols    or 40
  max_rows    = max_rows    or 8
  world_width = world_width or 199

  local cx, cy     = cursor.x, cursor.y
  local tried_rows = 0
  local start_col  = startX + 1

  while tried_rows < max_rows do
    if cx < 0 then cx = 0 end
    if cx > world_width then cx = world_width end

    if not is_full_or_bad(cx, cy) then
      if _is_empty_drop_tile(cx, cy) then
        local total, stacks = _countOnTile(cx, cy)
        if (total < MAX_STACK) and (stacks < MAX_SLOTS) then
          cursor.x, cursor.y = cx, cy
          return cx, cy, cursor
        else
          mark_full(cx, cy)
        end
      else
        mark_bad(cx, cy)
      end
    end

    cx = cx + 1
    if cx >= startX + 1 + max_cols then
      tried_rows = tried_rows + 1
      cy = cy - 1
      cx = start_col
    end
  end
  return nil, nil, cursor
end

-- ===================== DROP ITEMS (SNAKE) =====================
function DROP_ITEMS_SNAKE(WORLD, DOOR, ITEMS, opts)
  local b = getBot and getBot() or nil; if not b or type(ITEMS) ~= "table" then return end

  opts = opts or {}
  local CHUNK       = opts.chunk or 400
  local STEP_MS     = opts.step_ms or 700
  local PATH_TRY    = opts.path_try or 10
  local MAX_COLS    = opts.max_cols or 80
  local MAX_ROWS    = opts.max_rows or 23
  local WORLD_W     = opts.world_width or 199
  local TILE_CAP    = opts.tile_cap or 4000
  local STACK_CAP   = opts.stack_cap or 20
  local RETRIES_TL  = opts.tile_retries or 2
  local RIGHT_CAP   = opts.hard_right_cap or 99
  local UP_CAP      = opts.hard_up_cap    or 23
  local TRY_LEFT_IF_FULL = (opts.try_left_fallback ~= false)

  reset_caches()
  ZEE_COLLECT(false)
  WARP_WORLD(WORLD, DOOR); sleep(150); SMART_RECONNECT(WORLD, DOOR)

  local sx, sy = _meTile(); if not sx then return end
  local cursor = { x = sx + 1, y = sy }

  -- clamp area terhadap posisi bot
  local space_right    = math.max(0, (WORLD_W - (sx + 1)))
  local eff_cols_right = math.max(0, math.min(MAX_COLS, RIGHT_CAP, space_right))
  local space_up       = math.max(0, sy)
  local eff_rows_up    = math.max(0, math.min(MAX_ROWS, UP_CAP, space_up))

  -- scan kanan
  local function scan_right_once(item_id)
    local have = b:getInventory():getItemCount(item_id)
    while have > 0 do
      ::seek_slot_right::
      local candX, candY
      candX, candY, cursor = _nextDropTileSnake(sx, sy, cursor, eff_cols_right, eff_rows_up, WORLD_W, TILE_CAP, STACK_CAP)
      if not candX then return have end

      if not _is_empty_drop_tile(candX, candY) then
        mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot_right
      end

      local stanceX, stanceY = candX - 1, candY
      if stanceX < 0 or (not _is_walkable(stanceX, stanceY)) then
        mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot_right
      end

      if not _gotoExact(WORLD, DOOR, stanceX, stanceY, PATH_TRY, STEP_MS) then
        mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot_right
      end

      faceSide2()

      local total, stacks = _countOnTile(candX, candY)
      if (total >= TILE_CAP) or (stacks >= STACK_CAP) then
        mark_full(candX, candY); cursor.x = candX + 1; goto seek_slot_right
      end

      local cap      = math.max(0, TILE_CAP - total)
      local drop_try = math.min(have, CHUNK, cap)
      if drop_try <= 0 then mark_full(candX, candY); cursor.x = candX + 1; goto seek_slot_right end

      local attempts_here = 0
      while drop_try > 0 and have > 0 do
        attempts_here = attempts_here + 1
        local before = b:getInventory():getItemCount(item_id)
        b:drop(tostring(item_id), drop_try)
        sleep(STEP_MS); SMART_RECONNECT(); GUARD_DOOR_STUCK()
        local after = b:getInventory():getItemCount(item_id)

        if after < before then
          have = after
          local t2, s2 = _countOnTile(candX, candY)
          if (t2 >= TILE_CAP) or (s2 >= STACK_CAP) then mark_full(candX, candY); cursor.x = candX + 1; break end
          local sisa = TILE_CAP - t2
          if sisa <= 0 then mark_full(candX, candY); cursor.x = candX + 1; break end
          drop_try      = math.min(have, CHUNK, sisa)
          attempts_here = 0
        else
          if attempts_here >= RETRIES_TL then
            mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot_right
          end
          drop_try = math.max(1, math.floor(drop_try/2))
        end
      end
    end
    return 0
  end

  -- fallback kiri
  local function scan_left_once(item_id)
    local have = b:getInventory():getItemCount(item_id)
    local space_left    = math.max(0, sx)
    local eff_cols_left = math.max(0, math.min(MAX_COLS, RIGHT_CAP, space_left))
    while have > 0 do
      ::seek_slot_left::
      local foundX, foundY = nil, nil
      local tried_rows = 0
      local cy = sy
      while tried_rows < eff_rows_up and (not foundX) do
        local start_col = sx - 1
        local min_col   = math.max(0, sx - eff_cols_left)
        for cx = start_col, min_col, -1 do
          if not is_full_or_bad(cx, cy) then
            if _is_empty_drop_tile(cx, cy) then
              local total, stacks = _countOnTile(cx, cy)
              if (total < TILE_CAP) and (stacks < STACK_CAP) then
                foundX, foundY = cx, cy; break
              else
                mark_full(cx, cy)
              end
            else
              mark_bad(cx, cy)
            end
          end
        end
        cy = cy - 1
        tried_rows = tried_rows + 1
      end

      if not foundX then return have end

      local stanceX, stanceY = foundX + 1, foundY
      if (not _in_bounds(stanceX, stanceY)) or (not _is_walkable(stanceX, stanceY)) then
        mark_bad(foundX, foundY); goto seek_slot_left
      end
      if not _gotoExact(WORLD, DOOR, stanceX, stanceY, PATH_TRY, STEP_MS) then
        mark_bad(foundX, foundY); goto seek_slot_left
      end

      faceSide2()

      local total, stacks = _countOnTile(foundX, foundY)
      if (total >= TILE_CAP) or (stacks >= STACK_CAP) then mark_full(foundX, foundY); goto seek_slot_left end

      local cap      = math.max(0, TILE_CAP - total)
      local drop_try = math.min(have, CHUNK, cap)
      if drop_try <= 0 then mark_full(foundX, foundY); goto seek_slot_left end

      local attempts_here = 0
      while drop_try > 0 and have > 0 do
        attempts_here = attempts_here + 1
        local before = b:getInventory():getItemCount(item_id)
        b:drop(tostring(item_id), drop_try)
        sleep(STEP_MS); SMART_RECONNECT(); GUARD_DOOR_STUCK()
        local after = b:getInventory():getItemCount(item_id)
        if after < before then
          have = after
          local t2, s2 = _countOnTile(foundX, foundY)
          if (t2 >= TILE_CAP) or (s2 >= STACK_CAP) then mark_full(foundX, foundY); break end
          local sisa = TILE_CAP - t2
          if sisa <= 0 then mark_full(foundX, foundY); break end
          drop_try      = math.min(have, CHUNK, sisa)
          attempts_here = 0
        else
          if attempts_here >= RETRIES_TL then
            mark_bad(foundX, foundY); goto seek_slot_left
          end
          drop_try = math.max(1, math.floor(drop_try/2))
        end
      end
    end
    return 0
  end

  for _, ITEM in pairs(ITEMS) do
    local sisa = scan_right_once(ITEM)
    if sisa > 0 and TRY_LEFT_IF_FULL then sisa = scan_left_once(ITEM) end
    if sisa > 0 then
      print(string.format("[DROP] Area habis. Sisa %d item id=%s tidak ter-drop.", sisa, tostring(ITEM)))
    end
  end
end

-- ===================== NUKED / PUBLIC CHECK =====================
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
  local b = getBot and getBot() or nil; if not (b and b.getWorld) then return nil end
  local okW, w = pcall(function() return b:getWorld() end); if not okW or not w then return nil end
  local okP, pub = pcall(function() return w.public end); if not okP then return nil end
  return pub and true or false
end

local function log_fail(world, door, reason)
  local f, err = io.open(FAIL_LOG_FILE, "a"); if not f then print("[LOG] Gagal buka file log: "..tostring(err)); return end
  local line = string.format("[%s] WORLD=%s | DOOR=%s | REASON=%s\n",
    os.date("%Y-%m-%d %H:%M:%S"), tostring(world), tostring(door), tostring(reason))
  f:write(line); f:close(); print("[FAIL-LOG]", line)
end
local function log_success(world, door, secs)
  local f, err = io.open(SUCCESS_LOG_FILE, "a"); if not f then print("[LOG] Gagal buka file success log: "..tostring(err)); return end
  local line = string.format("[%s] WORLD=%s | DOOR=%s | DURATION=%ds\n",
    os.date("%Y-%m-%d %H:%M:%S"), tostring(world), tostring(door), tonumber(secs or 0))
  f:write(line); f:close(); print("[SUCCESS-LOG]", line)
end

-- ===================== WARP TAHAN BANTING =====================
MAX_WARP_RETRY    = 10
MAX_DOOR_RETRY    = 5
MAX_RECOLL_CYCLES = 2

local function _nudge_and_warp(WORLD, DOOR, tries)
  local b = getBot and getBot() or nil; if not b then return false end
  tries = tries or 3
  for _=1,tries do
    local okW, w = pcall(function() return b:getWorld() end)
    if okW and w then
      local okL, me = pcall(function() return w:getLocal() end)
      if okL and me and b.findPath then
        local mx = math.floor((me.posx or 0)/32); local my = math.floor((me.posy or 0)/32)
        b:findPath(mx+1, my); sleep(300)
      end
    end
    if b.warp then b:warp((WORLD or ""):upper().."|"..(DOOR or "")) end
    sleep(DELAY_WARP)
    local fg = _current_tile_fg_safe(6, 100)
    if fg ~= 6 then return true end
  end
  return false
end

function GUARD_DOOR_STUCK()
  local b = getBot and getBot() or nil; if not b then return end
  local fg = _current_tile_fg_safe(2, 60)
  if fg ~= 6 then __door6_ticks = 0; return end

  local okW, w = pcall(function() return b:getWorld() end); if not okW or not w then return end
  local okL, me = pcall(function() return w:getLocal() end); if not okL or not me then return end
  local mx = math.floor((me.posx or 0)/32); local my = math.floor((me.posy or 0)/32)

  if __last_mx == mx and __last_my == my then __door6_ticks = __door6_ticks + 1
  else __door6_ticks = 0; __last_mx, __last_my = mx, my; return end

  if __door6_ticks >= 6 then
    print("[GUARD] Stuck di white door. Coba nudge+warp...")
    if CURRENT_WORLD_TARGET and CURRENT_DOOR_TARGET then
      if not _nudge_and_warp(CURRENT_WORLD_TARGET, CURRENT_DOOR_TARGET, 3) then
        if b.findPath then b:findPath(mx+1, my); sleep(300) end
      end
    else
      if b.findPath then b:findPath(mx+1, my); sleep(300) end
    end
    __door6_ticks = 0
  end
end

function WARP_WORLD(WORLD, DOOR)
  WORLD = (WORLD or ""):upper(); if WORLD == "" then return false end
  local tryDoor = (DOOR or "") ~= ""

  NUKED_STATUS, WORLD_IS_PUBLIC = false, nil

  local listener_added = false
  if type(addEvent) == "function" then addEvent(Event.variantlist, checkNukeds); listener_added = true end
  local function _cleanup() if listener_added and type(removeEvent)=="function" then removeEvent(Event.variantlist) end end

  if _current_world_upper() == WORLD then
    local pub = _world_public_safe(); if pub ~= nil then WORLD_IS_PUBLIC = pub end
    local fg  = _current_tile_fg_safe(5, 80)
    if not tryDoor or (fg ~= 6) then
      CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET  = tryDoor and DOOR or nil
      _cleanup(); return true
    end
  end

  local cycles = 0
  while cycles < (MAX_RECOLL_CYCLES or 1) do
    cycles = cycles + 1
    local attempt, ok = 0, false
    while attempt < (MAX_WARP_RETRY or 10) do
      UPDATE_DELAY_BY_PING()
      if _current_world_upper() == WORLD then ok = true; break end
      attempt = attempt + 1
      local b = getBot and getBot() or nil
      if b and b.warp then if tryDoor then b:warp(WORLD.."|"..DOOR) else b:warp(WORLD) end
      else print("[WARP_WORLD] getBot() tidak tersedia."); _cleanup(); return false end
      if type(listenEvents)=="function" then listenEvents(5) end
      if NUKED_STATUS then print("[WARP_WORLD] Nuked saat warp."); _cleanup(); return false end
      sleep(DELAY_WARP); SMART_RECONNECT()
      if _current_world_upper() == WORLD then ok = true; break end
    end
    if ok then break end
  end

  if _current_world_upper() ~= WORLD then print("[WARP_WORLD] Gagal warp setelah retry maksimal."); _cleanup(); return false end

  local pub = _world_public_safe()
  if pub ~= nil then WORLD_IS_PUBLIC = pub; print(pub and "[WARP] World PUBLIC" or "[WARP] World PRIVATE/LOCKED") end

  if tryDoor then
    local fg = _current_tile_fg_safe(15, 120)
    if fg >= 0 and fg ~= 6 then CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET = DOOR; _cleanup(); return true end

    if fg < 0 then
      for _=1,(MAX_DOOR_RETRY or 5) do
        local b=getBot and getBot() or nil; if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked saat door."); _cleanup(); return false end
        sleep(DELAY_WARP); SMART_RECONNECT()
        fg = _current_tile_fg_safe(8, 120)
        if fg >= 0 and fg ~= 6 then CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET = DOOR; _cleanup(); return true end
      end
      _cleanup(); return false
    end

    if fg == 6 then
      for dtry=1,(MAX_DOOR_RETRY or 5) do
        local b = getBot and getBot() or nil; if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked saat door."); _cleanup(); return false end
        sleep(DELAY_WARP); SMART_RECONNECT()
        fg = _current_tile_fg_safe(8, 120)
        if fg >= 0 and fg ~= 6 then CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET = DOOR; _cleanup(); return true end
        print(string.format("[WARP_WORLD] Door attempt %d/%d belum sukses.", dtry, (MAX_DOOR_RETRY or 5)))
      end
      if _nudge_and_warp(WORLD, DOOR, 3) then CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET  = DOOR; _cleanup(); return true end
      print("[WARP_WORLD] Indicasi door salah / tidak valid (masih di white door)."); _cleanup(); return false
    end
  end

  CURRENT_WORLD_TARGET = WORLD; CURRENT_DOOR_TARGET  = tryDoor and DOOR or nil; _cleanup(); return true
end

local function warp_ok_and_public(W, D)
  NUKED_STATUS, WORLD_IS_PUBLIC = false, nil
  local ok = WARP_WORLD(W, D)
  if not ok then log_fail(W, D, "warp_failed"); return false, "warp_failed" end
  if NUKED_STATUS then log_fail(W, D, "nuked"); return false, "nuked" end
  local pub = _world_public_safe(); if pub ~= nil then WORLD_IS_PUBLIC = pub end
  if WORLD_IS_PUBLIC == false then log_fail(W, D, "not_public"); return false, "not_public" end
  if (D or "") ~= "" then
    local fg = _current_tile_fg_safe(6, 100)
    if fg == 6 then
      local b = getBot and getBot() or nil
      for _ = 1, 3 do if b and b.warp then b:warp((W or ""):upper().."|"..D) end; sleep(DELAY_WARP); fg = _current_tile_fg_safe(6, 100); if fg ~= 6 then break end end
      if fg == 6 then log_fail(W, D, "bad_door"); return false, "bad_door" end
    end
  end
  return true, "ok"
end

-- ===================== CAKE HELPERS =====================
local function has_any_cake()
  local b = getBot and getBot() or nil; if not (b and b.getInventory) then return false end
  local inv = b:getInventory()
  for _, id in pairs(cakeList or {}) do if inv:getItemCount(id) > 0 then return true end end
  return false
end

-- ===================== MAGNI (keep=1) =====================
local function _ensure_single_item_in_storage(item_id, keep, storageW, storageD, opts)
  local b = getBot and getBot() or nil; if not b then return end
  keep = keep or 1; opts = opts or {}
  local CHUNK      = opts.chunk or 200
  local STEP_MS    = opts.step_ms or 600
  local PATH_TRY   = opts.path_try or 10
  local MAX_COLS   = opts.max_cols or 50
  local MAX_ROWS   = opts.max_rows or 20
  local WORLD_W    = opts.world_width or 199
  local TILE_CAP   = opts.tile_cap or 4000
  local STACK_CAP  = opts.stack_cap or 20
  local RETRIES_TL = opts.tile_retries or 2

  local inv = b:getInventory()
  local have = inv:getItemCount(item_id)
  if have <= keep then return end

  if (storageW or "") ~= "" then WARP_WORLD(storageW, storageD); sleep(150); SMART_RECONNECT(storageW, storageD) end
  reset_caches(); ZEE_COLLECT(false)

  local sx, sy = (function()
    local me = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
    if not me then return 1,1 end
    return math.floor(me.posx/32), math.floor(me.posy/32)
  end)()
  local cursor = { x = sx + 1, y = sy }

  local extras = have - keep
  while extras > 0 do
    ::seek_slot::
    local candX, candY
    candX, candY, cursor = _nextDropTileSnake(sx, sy, cursor, MAX_COLS, MAX_ROWS, WORLD_W, TILE_CAP, STACK_CAP)
    if not candX then print("[MAGNI] Storage area penuh/habis jangkauan."); return end

    if not _is_empty_drop_tile(candX, candY) then mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot end

    local stanceX, stanceY = candX - 1, candY
    if stanceX < 0 or (not _is_walkable(stanceX, stanceY)) then mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot end

    if not _gotoExact(storageW, storageD, stanceX, stanceY, PATH_TRY, STEP_MS) then mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot end

    faceSide2()

    local total, stacks = _countOnTile(candX, candY)
    if (total >= TILE_CAP) or (stacks >= STACK_CAP) then mark_full(candX, candY); cursor.x = candX + 1; goto seek_slot end

    local cap      = math.max(0, TILE_CAP - total)
    local drop_try = math.min(extras, CHUNK, cap)
    if drop_try <= 0 then mark_full(candX, candY); cursor.x = candX + 1; goto seek_slot end

    local attempts_here = 0
    while drop_try > 0 and extras > 0 do
      attempts_here = attempts_here + 1
      local before = inv:getItemCount(item_id)
      b:drop(tostring(item_id), drop_try)
      sleep(STEP_MS); SMART_RECONNECT(); GUARD_DOOR_STUCK()
      local after = inv:getItemCount(item_id)
      if after < before then
        local dropped = before - after; extras = math.max(0, extras - dropped)
        local t2, s2 = _countOnTile(candX, candY)
        if (t2 >= TILE_CAP) or (s2 >= STACK_CAP) then mark_full(candX, candY); cursor.x = candX + 1; break end
        local sisa_cap = TILE_CAP - t2
        if sisa_cap <= 0 then mark_full(candX, candY); cursor.x = candX + 1; break end
        drop_try      = math.min(extras, CHUNK, sisa_cap)
        attempts_here = 0
      else
        if attempts_here >= RETRIES_TL then mark_bad(candX, candY); cursor.x = candX + 1; goto seek_slot end
        drop_try = math.max(1, math.floor(drop_try/2))
      end
    end
  end
end

function TAKE_MAGNI(WORLD, DOOR)
  local b = getBot and getBot() or nil
  if not b or not USE_MAGNI then return false end
  local TARGET_ID = 10158
  local inv = b:getInventory()

  -- Early normalize: kalau >1, sisakan 1 & wear, lalu return
  do
    local have = inv:getItemCount(TARGET_ID)
    if have > 1 then
      local storageW, storageD = STORAGE_MAGNI, DOOR_MAGNI
      if (storageW or "") == "" then storageW, storageD = WORLD, DOOR end
      _ensure_single_item_in_storage(TARGET_ID, 1, storageW, storageD,
        {chunk=200, step_ms=600, path_try=10, max_cols=50, max_rows=20, tile_cap=4000, stack_cap=20, tile_retries=2})
      if inv:getItemCount(TARGET_ID) > 0 then b:wear(TARGET_ID); sleep(300) end
      return true
    end
  end

  -- Ambil kalau belum punya
  if inv:getItemCount(TARGET_ID) == 0 then
    local function _try_take_at(w,d)
      if (w or "") == "" then return false end
      WARP_WORLD(w, d); sleep(200)
      local MAX_ROUNDS, WAIT_MS = 10, 1200
      local got=false
      for _=1,MAX_ROUNDS do
        if inv:getItemCount(TARGET_ID) > 0 then got=true; break end
        local objs=(getObjects and getObjects()) or {}
        local me=b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
        local best,bestd2=nil,1e18
        for _,o in pairs(objs) do
          if o.id==TARGET_ID then
            local tx,ty=math.floor(o.x/32),math.floor(o.y/32)
            if me then
              local mx,my=math.floor(me.posx/32),math.floor(me.posy/32)
              local dx,dy=tx-mx,ty-my; local d2=dx*dx+dy*dy
              if d2<bestd2 then best,bestd2=o,d2 end
            else best=o; bestd2=0 end
          end
        end
        if best then
          local tx,ty=math.floor(best.x/32),math.floor(best.y/32)
          SMART_RECONNECT(w,d,tx,ty); ZEE_COLLECT(true); b:findPath(tx,ty); sleep(WAIT_MS)
        else
          ZEE_COLLECT(true); SMART_RECONNECT(w,d); sleep(WAIT_MS)
        end
      end
      ZEE_COLLECT(false)
      return got or (inv:getItemCount(TARGET_ID) > 0)
    end
    if not _try_take_at(WORLD, DOOR) then _try_take_at(STORAGE_MAGNI, DOOR_MAGNI) end
    if inv:getItemCount(TARGET_ID) == 0 then print("[TAKE_MAGNI] Gagal ambil 10158 (MAGNI)."); return false end
  end

  -- Normalisasi & pakai
  local storageW, storageD = STORAGE_MAGNI, DOOR_MAGNI
  if (storageW or "") == "" then storageW, storageD = WORLD, DOOR end
  _ensure_single_item_in_storage(TARGET_ID, 1, storageW, storageD,
    {chunk=200, step_ms=600, path_try=10, max_cols=50, max_rows=20, tile_cap=4000, stack_cap=20, tile_retries=2})

  if inv:getItemCount(TARGET_ID) > 0 then b:wear(TARGET_ID); sleep(300); return true end
  return false
end

-- ===================== HARVEST =====================
local function has_harvestables()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return false end
  local w=b:getWorld()
  for _,t in pairs(_get_tiles()) do local tt=w:getTile(t.x,t.y); if tt and tt.fg==ITEM_SEED_ID and tt:canHarvest() then return true end end
  return false
end

local function checkitemfarm(farmList)
  local inv = getBot():getInventory()
  for _, item in pairs(farmList) do if inv:getItemCount(item) >= 190 then return true end end
  return false
end

local function HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
  local bot=getBot and getBot() or nil; if not bot then return false end

  if USE_MAGNI then
    local inv  = bot:getInventory()
    local have = inv:getItemCount(10158)
    local called_take = false

    if have == 0 then
      if (STORAGE_MAGNI or "") ~= "" then TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI); called_take = true end
      if inv:getItemCount(10158) == 0 then TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called_take = true end
    elseif have > 1 then
      TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called_take = true
    end
    if (not called_take) and inv:getItemCount(10158) > 0 then bot:wear(10158); sleep(200) end
  end

  WARP_WORLD(FARM_WORLD, FARM_DOOR)
  ZEE_COLLECT(true); sleep(120); SMART_RECONNECT(FARM_WORLD, FARM_DOOR)

  local w=bot:getWorld(); local did_any=false
  for _, t in pairs(_get_tiles()) do
    local tile=w:getTile(t.x,t.y)
    if tile and tile.fg==ITEM_SEED_ID and tile:canHarvest() then
      local tries=0
      while tries<6 do
        bot:findPath(t.x,t.y); SMART_RECONNECT(); GUARD_DOOR_STUCK()
        local me=w:getLocal(); if me and math.floor(me.posx/32)==t.x and math.floor(me.posy/32)==t.y then break end
        tries=tries+1
      end
      local cnt=0
      while true do
        local cur=w:getTile(t.x,t.y)
        if not (cur and cur.fg==ITEM_SEED_ID and cur:canHarvest()) then break end
        bot:hit(t.x,t.y); sleep(DELAY_HARVEST); SMART_RECONNECT(); GUARD_DOOR_STUCK()
        cnt=cnt+1; if cnt>=100 then print(string.format("[HARVEST_PASS] Stop 100 hits (%d,%d)",t.x,t.y)); break end
      end
      did_any=true
      if checkitemfarm(farmListActive) then break end
    end
  end
  return did_any
end

function HARVEST_UNTIL_EMPTY(FARM_WORLD, FARM_DOOR, STORAGE_WORLD, STORAGE_DOOR, farmListActive, on_tick)
  local t0 = os.time()
  while true do
    if on_tick then pcall(on_tick, FARM_WORLD) end
    local did = HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
    if on_tick then pcall(on_tick, FARM_WORLD) end
    if checkitemfarm(farmListActive) then
      DROP_ITEMS_SNAKE(STORAGE_WORLD, STORAGE_DOOR, farmListActive, {tile_cap=3000, stack_cap=20})
      if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
        pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20}) end)
      end
    end
    if (not did) and (not checkitemfarm(farmListActive)) then
      if not has_harvestables() then print("[HARVEST] Selesai world:", FARM_WORLD); break end
    end
  end
  ZEE_COLLECT(false)
  print(string.format("[HARVEST] Done %s in %ds", FARM_WORLD, os.time()-t0))
end

-- ===================== RR/CHUNK MODE (opsional) =====================
local function _simple_hash(s)
  local h = 1469598107
  for i = 1, #s do h = (h * 131 + s:byte(i)) % 4294967296 end
  return h
end
local function _auto_slot_and_total()
  local self = getBot and getBot() or nil
  local selfName = self and (self.name or ""):upper() or ""
  local names = {}
  if type(getBots)=="function" then
    for _, b in pairs(getBots()) do if b and b.name then names[#names+1] = (b.name or ""):upper() end end
  end
  if #names == 0 and selfName ~= "" then names[1] = selfName end
  table.sort(names)
  local detected = #names
  local cfg_total = tonumber(TOTAL_BOTS or 0) or 0
  local total = (cfg_total > 0) and cfg_total or detected
  if total < 1 then total = 1 end
  if detected >= 2 then
    local mypos = 1
    for i, n in ipairs(names) do if n == selfName then mypos = i; break end end
    local myslot = ((mypos - 1) % total) + 1
    return myslot, total
  end
  local tail = tonumber(selfName:match("(%d+)$") or "")
  if tail and tail > 0 then
    local myslot = ((tail - 1) % total) + 1
    return myslot, total
  end
  local myslot = (_simple_hash(selfName) % total) + 1
  return myslot, total
end
do
  local s, t = _auto_slot_and_total()
  MY_SLOT    = MY_SLOT    or s
  TOTAL_BOTS = TOTAL_BOTS or t
end
local function _detect_my_slot(default_slot)
  local b = getBot and getBot() or nil
  if b then
    if b.slot then return tonumber(b.slot) or default_slot end
    if b.name and type(b.name)=="string" then
      local num = tonumber((b.name or ""):match("(%d+)$") or ""); if num then return num end
    end
  end
  return default_slot or 1
end
MY_SLOT = MY_SLOT or _detect_my_slot(1)

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-- JOB OWNER DISET KE SLOT-<NN>
local WORKER_NAME = string.format("SLOT-%02d", tonumber(MY_SLOT or 1) or 1)
-- <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

local function _rotate_list(base, seed)
  if (not ROTATE_LIST) or (#base == 0) then return base end
  local off = (seed or 0) % #base
  if off == 0 then return base end
  local out = {}
  for i=1,#base do out[i] = base[((i-1+off) % #base) + 1] end
  return out
end
local function build_worlds_for_bot(base_list, my_slot, total_bots, farm_per_bot, mode)
  local base = _rotate_list(base_list, ROTATE_SEED)
  local out, N = {}, #base
  if N == 0 then return out end
  my_slot    = math.max(1, math.min(my_slot or 1, total_bots or 1))
  total_bots = math.max(1, total_bots or 1)
  farm_per_bot = tonumber(farm_per_bot or 0) or 0
  mode = (mode == "chunk") and "chunk" or "rr"
  if mode == "chunk" then
    local len   = (farm_per_bot > 0 and farm_per_bot or math.ceil(N / total_bots))
    local start = (my_slot - 1) * len + 1
    local last  = math.min(N, start + len - 1)
    for i = start, last do table.insert(out, base[i]) end
  else
    for i = my_slot, N, total_bots do
      table.insert(out, base[i])
      if farm_per_bot > 0 and #out >= farm_per_bot then break end
    end
  end
  print(string.format("[ASSIGN] SLOT=%d/%d MODE=%s ROTATE=%s worlds_assigned=%d",
    my_slot, total_bots, mode, tostring(ROTATE_LIST), #out))
  return out
end

-- ===================== RR/CHUNK WORLD PARSER =====================
local function _parse_world_entry(s)
  local farmW, farmD, idstr, storeW, storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW or not idstr then return nil end
  return (farmW or ""):upper(), (farmD or ""), tonumber(idstr),
         (storeW or ""):upper(), (storeD or "")
end

-- ===================== TXT QUEUE HELPERS =====================
local function _read_lines(path)
  local t, f = {}, io.open(path, "r"); if not f then return t end
  for line in f:lines() do line = line:gsub("\r",""):gsub("\n",""); if line ~= "" and not line:match("^%s*;") then table.insert(t, line) end end
  f:close(); return t
end
local function _write_lines(path, lines)
  local f = io.open(path, "w"); if not f then return false end
  for _,ln in ipairs(lines or {}) do f:write(ln.."\n") end; f:close(); return true
end
local function _append_line(path, line) local f = io.open(path, "a"); if not f then return false end; f:write(line.."\n"); f:close(); return true end
local function _now() return os.time() end

local function _parse_world_line(s)
  local farmW, farmD, bid, storeW, storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW then return nil end
  return farmW:upper(), (farmD or ""), tonumber(bid), (storeW or ""):upper(), (storeD or "")
end

local function _set_of_worlds(lines)
  local S = {}; for _, ln in ipairs(lines) do local w = ln:match("^([^|]+)"); if w then S[w:upper()] = true end end; return S
end

local function _update_heartbeat(world, who)
  world = (world or ""):upper(); who = who or WORKER_NAME
  local now = _now()
  local rows = _read_lines(JOB_FILES.inprogress)
  local out, touched = {}, false
  for _, ln in ipairs(rows) do
    local w, worker, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and worker and ts then
      if w:upper()==world and worker==who then table.insert(out, string.format("%s|%s|%d", w, worker, now)); touched = true
      else table.insert(out, ln) end
    end
  end
  if not touched then table.insert(out, string.format("%s|%s|%d", world, who, now)) end
  _write_lines(JOB_FILES.inprogress, out)
end

local function CLAIM_NEXT_JOB()
  local worlds = _read_lines(JOB_FILES.worlds)
  local prog   = _read_lines(JOB_FILES.inprogress)
  local done   = _read_lines(JOB_FILES.done)
  local S_prog, S_done = _set_of_worlds(prog), _set_of_worlds(done)
  for _, ln in ipairs(worlds) do
    local W = ln:match("^([^|]+)")
    if W and (not S_prog[W:upper()]) and (not S_done[W:upper()]) then
      _append_line(JOB_FILES.inprogress, string.format("%s|%s|%d", W:upper(), WORKER_NAME, _now()))
      return ln
    end
  end
  return nil
end

local function MARK_DONE(world, reason)
  world = (world or ""):upper()
  local rows = _read_lines(JOB_FILES.inprogress); local out = {}
  for _, ln in ipairs(rows) do local w = ln:match("^([^|]+)"); if w and w:upper() ~= world then table.insert(out, ln) end end
  _write_lines(JOB_FILES.inprogress, out)
  _append_line(JOB_FILES.done, string.format("%s|%s|%d|%s", world, WORKER_NAME, _now(), tostring(reason or "ok")))
end

local function QUEUE_STATS()
  local worlds = _read_lines(JOB_FILES.worlds)
  local prog   = _read_lines(JOB_FILES.inprogress)
  local done   = _read_lines(JOB_FILES.done)
  local S_prog, S_done = _set_of_worlds(prog), _set_of_worlds(done)
  local total, unclaimed, inprog, ndone = 0, 0, 0, 0
  for _, ln in ipairs(worlds) do
    local W = (ln:match("^([^|]+)") or ""):upper()
    if W ~= "" then
      total = total + 1
      local is_prog = S_prog[W] and true or false
      local is_done = S_done[W] and true or false
      if (not is_prog) and (not is_done) then unclaimed = unclaimed + 1 end
      if is_prog then inprog = inprog + 1 end
      if is_done then ndone = ndone + 1 end
    end
  end
  return {total=total, unclaimed=unclaimed, inprogress=inprog, done=ndone}
end

local function PICK_ASSIST_WORLD()
  if not STEAL_HELP then return nil end
  local prog = _read_lines(JOB_FILES.inprogress)
  if #prog == 0 then return nil end
  local best, best_age, now = nil, -1, _now()
  for _, ln in ipairs(prog) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts then
      local age = now - tonumber(ts)
      if who ~= WORKER_NAME and age > best_age then best, best_age = w:upper(), age end
    end
  end
  if best and best_age >= STALE_SEC then
    local rows = _read_lines(JOB_FILES.inprogress)
    local out, stolen = {}, false
    for _, ln in ipairs(rows) do
      local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
      if w and who and ts and w:upper()==best then
        table.insert(out, string.format("%s|%s|%d", w:upper(), WORKER_NAME, _now())); stolen = true
      else table.insert(out, ln) end
    end
    if stolen then _write_lines(JOB_FILES.inprogress, out) end
    return best
  end
  return nil
end

-- RECONCILE: hapus world2 yang sudah DONE dari worlds.txt (juga dedup)
function RECONCILE_QUEUE()
  local worlds = _read_lines(JOB_FILES.worlds)
  local done   = _read_lines(JOB_FILES.done)
  local S_done = _set_of_worlds(done)
  local seen   = {}
  local out    = {}
  local removed= 0
  for _, ln in ipairs(worlds) do
    local W = (ln:match("^([^|]+)") or ""):upper()
    if W ~= "" then
      if S_done[W] then
        removed = removed + 1
      elseif not seen[W] then
        table.insert(out, ln); seen[W] = true
      end
    end
  end
  if removed > 0 or (#out ~= #worlds) then
    _write_lines(JOB_FILES.worlds, out)
    print(string.format("[RECONCILE] worlds.txt disinkron: removed=%d, total_now=%d", removed, #out))
  end
end

-- AUTO-RESUME / OWN INPROGRESS
local function _norm_ts(ts) local n = tonumber(ts) or 0; if n > 1e12 then n = math.floor(n/1000) end; return n end
local function SPEC_FOR_WORLD(W)
  local worlds = _read_lines(JOB_FILES.worlds)
  for _, ln in ipairs(worlds) do
    local w, d, bid, sw, sd = _parse_world_line(ln)
    if w and w == (W or ""):upper() then return w, d, bid, sw, sd end
  end
  return nil
end
local function FIND_OWN_INPROGRESS()
  local rows = _read_lines(JOB_FILES.inprogress)
  local bestW, bestTS = nil, -1
  for _, ln in ipairs(rows) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who == WORKER_NAME then
      local t = _norm_ts(ts); if t > bestTS then bestTS, bestW = t, (w or ""):upper() end
    end
  end
  return bestW
end
local function UNCLAIM(world)
  world = (world or ""):upper()
  local rows = _read_lines(JOB_FILES.inprogress); local out = {}
  for _, ln in ipairs(rows) do local w = ln:match("^([^|]+)"); if w and w:upper() ~= world then table.insert(out, ln) end end
  _write_lines(JOB_FILES.inprogress, out)
end

-- ===================== IDLE HOUSEKEEPING (anti-spam) =====================
local function _idle_housekeeping()
  local now = os.time()
  if (now - __last_idle_action) < (IDLE_ACTION_COOLDOWN or 60) then return end
  __last_idle_action = now

  if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
    pcall(function()
      DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20})
    end)
  end

  local b = getBot and getBot() or nil
  if b and b.leaveWorld and (not IS_IN_EXIT()) then
    b:leaveWorld()
    sleep(800)
    b.auto_reconnect = true
  end
end

-- ===================== RUNNER: TXT QUEUE =====================
function RUN_FROM_TXT_QUEUE()
  -- AUTO-RESUME
  local resumeW = FIND_OWN_INPROGRESS()
  if resumeW then
    local W, D, BID, SW, SD = SPEC_FOR_WORLD(resumeW)
    if W and BID then
      ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
      print(string.format("[RESUME] %s melanjutkan %s|%s (BID=%d)", WORKER_NAME, W, (D or ""), BID))
      local ok, why = warp_ok_and_public(W, D)
      if not ok then
        print(string.format("[RESUME] Warp check gagal (%s) -> tandai done(skip).", tostring(why)))
        MARK_DONE(W, why or "skip")
      else
        local hb = function(world) _update_heartbeat(world, WORKER_NAME) end
        _update_heartbeat(W, WORKER_NAME)
        HARVEST_UNTIL_EMPTY(W, D, SW, SD, {ITEM_BLOCK_ID, ITEM_SEED_ID}, hb)
        MARK_DONE(W, "ok")
        print(string.format("[RESUME] %s selesai %s", WORKER_NAME, W))
      end
    else
      print(string.format("[RESUME] Spec %s tidak ditemukan di worlds.txt; unclaim.", tostring(resumeW)))
      UNCLAIM(resumeW)
    end
  end

  while true do
    -- Klaim job baru
    local job = CLAIM_NEXT_JOB()
    if job then
      local W, D, BID, SW, SD = _parse_world_line(job)
      if W and BID then
        ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
        print(string.format("[JOB] %s klaim %s|%s (BID=%d)", WORKER_NAME, W, (D or ""), BID))
        local ok, why = warp_ok_and_public(W, D)
        if not ok then
          print(string.format("[JOB] Warp check gagal (%s) -> tandai done(skip).", tostring(why)))
          MARK_DONE(W, why or "skip")
        else
          local hb = function(world) _update_heartbeat(world, WORKER_NAME) end
          _update_heartbeat(W, WORKER_NAME)
          HARVEST_UNTIL_EMPTY(W, D, SW, SD, {ITEM_BLOCK_ID, ITEM_SEED_ID}, hb)
          MARK_DONE(W, "ok")
          print(string.format("[JOB] %s selesai %s", WORKER_NAME, W))
        end
      end

    else
      -- Tidak ada job baru -> gating assist
      local qs = QUEUE_STATS()
      if qs.unclaimed > 0 then
        print(string.format("[QUEUE] Masih ada %d world belum diklaim. Menunggu...", qs.unclaimed))
        sleep(1200)
        _idle_housekeeping()
      elseif qs.total > 0 and qs.inprogress == 0 and qs.done < qs.total then
        -- tidak unclaimed, tidak inprogress, tapi belum semuanya done -> sinkronisasi
        RECONCILE_QUEUE()
        print(string.format("[QUEUE] Tidak ada job aktif (total=%d, inprogress=%d, done=%d). Menunggu...",
          qs.total, qs.inprogress, qs.done))
        sleep(1200)
        _idle_housekeeping()
      else
        -- semua sudah diklaim -> boleh assist stale
        local assistW = PICK_ASSIST_WORLD()
        if assistW then
          print(string.format("[HELP] %s bantu %s (steal stale)", WORKER_NAME, assistW))
          local wspec = SPEC_FOR_WORLD(assistW)
          if wspec then
            local W, D, BID, SW, SD = wspec
            ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
            local ok, why = warp_ok_and_public(W, D)
            if not ok then
              print(string.format("[HELP] Warp check gagal (%s) pada %s -> lewati.", tostring(why), W))
            else
              local hb = function(world) _update_heartbeat(world, WORKER_NAME) end
              _update_heartbeat(W, WORKER_NAME)
              HARVEST_UNTIL_EMPTY(W, D, SW, SD, {ITEM_BLOCK_ID, ITEM_SEED_ID}, hb)
              -- jika owner saat ini kita (karena steal), tutup job
              local rows = _read_lines(JOB_FILES.inprogress); local owner_now = nil
              for _, l in ipairs(rows) do local ww, who = l:match("^([^|]+)|([^|]+)|"); if ww and ww:upper()==W then owner_now = who; break end end
              if owner_now == WORKER_NAME then MARK_DONE(W, "help_ok"); print(string.format("[HELP] %s menutup %s", WORKER_NAME, W)) end
            end
          end
        else
          -- Idle: tergantung LOOP_MODE
          if LOOP_MODE then
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job/assist (total=%d, inprogress=%d, done=%d). Standby...",
              qs.total, qs.inprogress, qs.done))
            sleep(1200)
            _idle_housekeeping()
          else
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job/assist (total=%d, inprogress=%d, done=%d). Keluar.",
              qs.total, qs.inprogress, qs.done))
            break
          end
        end
      end
    end

    sleep(400)
  end

  -- FINAL cleanup
  if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
    pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20}) end)
  end
  local b = getBot and getBot() or nil
  if b and b.leaveWorld then b:leaveWorld() end
  sleep(1000)
  if b then b.auto_reconnect = true end
end

-- ===================== MODE RR/CHUNK (opsional) =====================
function RUN_MULTI_HARVEST(list_world)
  TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI)
  local old_block, old_seed = ITEM_BLOCK_ID, ITEM_SEED_ID
  local world_specs = {}

  for idx, entry in ipairs(list_world or {}) do
    local W, D, BID, SW, SD = _parse_world_entry(entry)
    if W and BID then
      ITEM_BLOCK_ID = BID; ITEM_SEED_ID  = BID + 1
      local per_world_farm = {ITEM_BLOCK_ID, ITEM_SEED_ID}
      print(("[MULTI] %d) %s|%s BLOCK=%d SEED=%d -> %s|%s"):format(idx, W, D, ITEM_BLOCK_ID, ITEM_SEED_ID, SW, SD))
      local ok, reason = warp_ok_and_public(W, D)
      if not ok then
        if     reason=="nuked"       then print(("⏭ Skip %s: NUKED/BANNED/LEVEL-LIMIT."):format(W))
        elseif reason=="not_public"  then print(("⏭ Skip %s: world tidak PUBLIC/LOCKED."):format(W))
        elseif reason=="bad_door"    then print(("⏭ Skip %s: DOOR '%s' salah / tidak ada."):format(W, tostring(D)))
        else                              print(("⏭ Skip %s: warp gagal (%s)."):format(W, tostring(reason)))
        end
        goto continue
      end
      local t0 = os.time()
      world_specs[#world_specs+1] = {storageW=SW, storageD=SD, farmItems=per_world_farm}
      HARVEST_UNTIL_EMPTY(W, D, SW, SD, per_world_farm)
      log_success(W, D, os.time() - t0)
      ::continue::
    else print("[MULTI] Lewati entry tidak valid: "..tostring(entry)) end
  end

  ITEM_BLOCK_ID, ITEM_SEED_ID = old_block, old_seed

  print("[MULTI] Final drop per-world...")
  for _, spec in ipairs(world_specs) do DROP_ITEMS_SNAKE(spec.storageW, spec.storageD, spec.farmItems, {tile_cap=3000, stack_cap=20}) end
  if (STORAGE_CAKE or "") ~= "" and has_any_cake() then pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20}) end) end
  local b = getBot and getBot() or nil; if b and b.leaveWorld then b:leaveWorld() end; sleep(1000); if b then b.auto_reconnect = true end
  print("[MULTI] Selesai semua.")
end

-- ===================== MAIN =====================
do
  ASSIGN_MODE = (ASSIGN_MODE or "rr"):lower():gsub("%s+", "")
  if ASSIGN_MODE ~= "rr" and ASSIGN_MODE ~= "chunk" then ASSIGN_MODE = "rr" end
  print(string.format("[CONFIG] ASSIGN_MODE=%s | USE_TXT_QUEUE=%s | LOOP_MODE=%s | WORKER=%s",
    ASSIGN_MODE, tostring(USE_TXT_QUEUE), tostring(LOOP_MODE), WORKER_NAME))

  if USE_TXT_QUEUE then
    RUN_FROM_TXT_QUEUE()
  else
    -- Contoh LIST_WORLD jika tak pakai TXT:
    -- LIST_WORLD = {
    --   "WORLD1|DOOR|4584|STORAGE|DOORST",
    -- }
    local myList = build_worlds_for_bot(LIST_WORLD or {}, MY_SLOT, TOTAL_BOTS, FARM_PER_BOT, ASSIGN_MODE)
    print(string.format("[CHECK] I am slot %d of %d (mode=%s)", MY_SLOT, TOTAL_BOTS, ASSIGN_MODE))
    if #myList == 0 then
      print(string.format("[ASSIGN] SLOT %d tidak mendapat world. Cek TOTAL_BOTS/ASSIGN_MODE/ROTATE_LIST.", MY_SLOT))
    else
      print("[CHECK] Worlds assigned to me:"); for i, w in ipairs(myList) do print(string.format("  %02d) %s", i, w)) end
      RUN_MULTI_HARVEST(myList)
    end
  end
end
