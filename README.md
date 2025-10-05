-- =========================
-- KONFIG & LIST
-- =========================
LIST_WORLD_BLOCK = {
  "WORU15|NOWXX123",
  "BOHKARA|NOWXX123",
  "FENCEMM1|NOWXX123",
}

STORAGE_SEED = {
  "AFILFENCE10|NOWXX123",
  "LEOD83|NOWXX123",
  "FENCEMM100|NOWXX123",
}

MODE                            = "SULAP"   -- SULAP | PNB
STORAGE_MALADY, DOOR_MALADY     = "COKANJI", "XX1"
SHOW_PUNCH                      = false
RANDOM_WORLD_AFTER_CHANGE_WORLD = true
JUMLAH_RANDOM_WORLD             = 6
LIMIT_SEED_STORAGE              = 54000  -- kapasitas per world
ID_BLOCK                        = 8640
LIMIT_SEED_IN_BP                = 190
JUMLAH_TILE_BREAK               = 3
DELAY_RECONNECT                 = 20000
DELAY_BAD_SERVER                = 120000
DELAY_BREAK                     = 170
DELAY_PUT                       = 115
DELAY_WARP                      = 7000
DELAY_EXE                       = 2000


-- ##################### BATAS SCRIPT #####################
Bot = {}
for slot=1,8 do Bot[slot] = {slot=slot} end
for nomor, bb in pairs(getBots()) do if getBot().name:upper() == bb.name:upper() then index = nomor end end
MY_SLOT = Bot[index].slot
sleep( DELAY_EXE * ( index - ( 1 - 1 ) ) )
TILE_BREAK = {}
worldTutor = ""
ID_SEED = ID_BLOCK + 1
CHECK_WORLD_TUTORIAL = false
NUKED_STATUS         = false
WORLD_MAX_X = WORLD_MAX_X or 99
WORLD_MAX_Y = WORLD_MAX_Y or 59
local FULL_CACHE, BAD_CACHE = {}, {}
local function _key(x,y) return x..":"..y end
function mark_full(x,y) FULL_CACHE[_key(x,y)]=true end
function mark_bad (x,y) BAD_CACHE [_key(x,y)]=true end
function is_full_or_bad(x,y) return FULL_CACHE[_key(x,y)] or BAD_CACHE[_key(x,y)] end
function reset_caches() FULL_CACHE={}; BAD_CACHE={} end
getBot().auto_reconnect = false

-- RING STATE storage seed
_SEED_RING = _SEED_RING or { list=nil, idx=1, full={} }

-- (NEW) safe stub if not provided elsewhere: count items on a tile
if _countOnTile == nil then
  function _countOnTile(cx,cy)
    local objs = (getObjects and getObjects()) or {}
    local total, stacks = 0, 0
    for _, o in pairs(objs) do
      local tx, ty = math.floor((o.x or 0)/32), math.floor((o.y or 0)/32)
      if tx == cx and ty == cy then
        local cnt = tonumber(o.count or o.amount or 1) or 1
        total = total + cnt
        stacks = stacks + 1
      end
    end
    return total, stacks
  end
end

-- (NEW) nudge helper stub used by WARP_WORLD if not present
_nudge_and_warp = _nudge_and_warp or function(WORLD, DOOR, tries)
  local b=getBot and getBot() or nil
  for _=1,(tries or 1) do
    if b and b.warp then
      if DOOR and DOOR ~= "" then b:warp((WORLD or "").."|"..DOOR) else b:warp(WORLD or "") end
    end
    if type(listenEvents)=="function" then listenEvents(5) end
    sleep(math.max(1000, math.floor(DELAY_WARP/2)))
  end
  return true
end

-- =========================
-- [ANTI-SPAM NUKED] COUNTERS
-- =========================
WORLD_COUNTER = WORLD_COUNTER or {
  block = {},   -- [WORLD] = { fails=0, until=0 }
  seed  = {},   -- [WORLD] = { fails=0, until=0 }
}

local function log_fail(w, d, reason)
  print(string.format("[WORLD] %s|%s -> %s", tostring(w or ""), tostring(d or ""), tostring(reason or "unknown")))
end

-- kalkulasi cooldown (exponential-ish) : 1->300s, 2->600s, >=3->900s
local function _cooldown_secs(fails)
  if fails <= 1 then return 300 end
  if fails == 2 then return 600 end
  return 900
end

-- NAikkan counter & pasang cooldown (REPLACE versi lama)
local function mark_world_nuked(kind, WORLD, DOOR)
  WORLD = tostring(WORLD or ""):upper()
  kind  = (kind == "seed") and "seed" or "block"
  local now = os.time()
  local t = WORLD_COUNTER[kind][WORLD] or { fails=0, until_ts=0 }  -- <== ganti
  t.fails    = math.min(99, (t.fails or 0) + 1)
  t.until_ts = now + _cooldown_secs(t.fails)                        -- <== ganti
  WORLD_COUNTER[kind][WORLD] = t
  print(string.format("[WORLD] %s|%s -> nuked(%s)#%d cool=%ds",
        WORLD, tostring(DOOR or ""), kind, t.fails, _cooldown_secs(t.fails)))
end

-- Apakah world sedang cooldown (REPLACE versi lama)
local function should_skip_world(kind, WORLD)
  WORLD = tostring(WORLD or ""):upper()
  kind  = (kind == "seed") and "seed" or "block"
  local t = WORLD_COUNTER[kind][WORLD]
  if not t then return false end
  local now = os.time()
  return now < (t.until_ts or 0)                                     -- <== ganti
end


-- clear counter saat sukses dipakai lagi (opsional)
-- Clear counter saat sukses (REPLACE versi lama)
local function clear_world_counter(kind, WORLD)
  WORLD = tostring(WORLD or ""):upper()
  kind  = (kind == "seed") and "seed" or "block"
  if WORLD_COUNTER[kind][WORLD] then
    WORLD_COUNTER[kind][WORLD] = { fails=0, until_ts=0 }             -- <== ganti
  end
end

local function remaining_cooldown(kind, WORLD)
  WORLD = tostring(WORLD or ""):upper()
  kind  = (kind == "seed") and "seed" or "block"
  local t = WORLD_COUNTER[kind][WORLD]
  if not t then return 0 end
  local left = (t.until_ts or 0) - os.time()
  return (left > 0) and left or 0
end


-- quick checker: nuked-only (memakai listener)
function is_world_nuked(WORLD, DOOR)
  WORLD = tostring(WORLD or ""):upper()
  local tryDoor = (DOOR or "") ~= ""
  if WORLD == "" then return false, "ok" end
  NUKED_STATUS = false
  local added=false
  if type(addEvent)=="function" then addEvent(Event.variantlist, checkNukeds); added=true end
  local b = getBot and getBot() or nil
  for _=1,2 do
    if b and b.warp then
      if tryDoor then b:warp(WORLD.."|"..DOOR) else b:warp(WORLD) end
    end
    if type(listenEvents)=="function" then listenEvents(5) end
    sleep(700)
    if NUKED_STATUS then
      if added and type(removeEvent)=="function" then removeEvent(Event.variantlist) end
      return true, "nuked"
    end
  end
  if added and type(removeEvent)=="function" then removeEvent(Event.variantlist) end
  return false, "ok"
end

-- =========================
-- UTIL / RECONNECT
-- =========================
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
    if STATUS_BOT_NEW().status=="online" then
      ensureMalady(6, { wait_confirmations = 2, recheck_ms = 500, guard_secs = 120 })

    end
  end

  if WORLD and DOOR then WARP_WORLD((WORLD or ""):upper(), DOOR)
  elseif WORLD then       WARP_WORLD((WORLD or ""):upper()) end

  if POSX and POSY then local b=getBot and getBot() or nil; if b and b.findPath then b:findPath(POSX,POSY) end end
end

function ZEE_COLLECT(state)
  local b=getBot and getBot() or nil; if not b then return end
  if state then b.auto_collect=true; b.ignore_gems=true; b.collect_range=5; b.object_collect_delay=200
  else b.auto_collect=false end
  if SHOW_PUNCH then b.legit_mode=true else b.legit_mode=false end
  malady = b.auto_malady
  malady.enabled = true
  malady.auto_refresh = true
  malady.auto_grumbleteeth = false
  malady.auto_chicken_feet = false
  malady.auto_surgery_station = false
  malady.auto_vial = false
end

function scan(id)
  local count = 0
  for _, object in pairs(getObjects()) do
    if object.id == id then
      count = count + (object.count or 1)
    end
  end
  return count
end

-- sumber karakter
local LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local DIGITS  = "0123456789"
local BOTH    = LETTERS .. DIGITS

local function random_kata(len, mix)
  local src = mix and BOTH or LETTERS
  local out = {}
  for i = 1, (len or 0) do
    local k = math.random(#src)
    out[i] = src:sub(k, k)
  end
  return table.concat(out)
end

function _random_world_list()
  if not RANDOM_WORLD_AFTER_CHANGE_WORLD then return end
  local n = tonumber(JUMLAH_RANDOM_WORLD) or 0
  for _ = 1, math.max(0, n) do
    local wr = random_kata(4, true)
    WARP_WORLD(wr) ; sleep(100)
    SMART_RECONNECT(wr) ; sleep(15000)
  end
end


-------------------- FACE KANAN --------------------
function faceSide2()
  local b=getBot and getBot() or bot; if not b then return end
  local packet=GameUpdatePacket.new(); packet.type=0; packet.flags=32; b:sendRaw(packet)
end

-- ##################### CARA PNB #####################
for i = math.floor(JUMLAH_TILE_BREAK/2),1,-1 do
  i = i * -1
  table.insert(TILE_BREAK,i)
end
for i = 0, math.ceil(JUMLAH_TILE_BREAK/2) - 1 do
  table.insert(TILE_BREAK,i)
end

-- helper: ambil tile aman dengan guard batas
local function _safeTile(w, x, y)
  if x < 0 or x > WORLD_MAX_X or y < 0 or y > WORLD_MAX_Y then return nil end
  local ok, t = pcall(function() return w:getTile(x, y) end)
  return ok and t or nil
end

function tilePunch(x, y)
  local b = getBot and getBot() or nil
  local w = b and b.getWorld and b:getWorld() or nil
  if not w then return false end
  for _, num in ipairs(TILE_BREAK) do
    local t = _safeTile(w, x + 1, y + num)
    if t and (t.fg or 0) ~= 0 then return true end
  end
  return false
end

function tilePlace(x, y)
  local b = getBot and getBot() or nil
  local w = b and b.getWorld and b:getWorld() or nil
  if not w then return false end
  for _, num in ipairs(TILE_BREAK) do
    local t = _safeTile(w, x + 1, y + num)
    if t and (t.fg or 0) == 0 then return true end
  end
  return false
end

-- ##################### GET DATA WORLD TUTORIAL #####################
function findHomeWorld(variant, netid)
  if variant:get(0):getString() == "OnRequestWorldSelectMenu"
      and variant:get(1):getString():find("Your Worlds") then
    local text = variant:get(1):getString()
    local lines = {}
    for line in text:gmatch("[^\r\n]+") do table.insert(lines, line) end
    for i, value in ipairs(lines) do
      if i == 3 then
        local kalimat = lines[3]
        local nilai = kalimat:match("|([a-zA-Z0-9%s]+)|")
        if nilai then nilai = nilai:gsub("%s", ""); worldTutor = nilai; print("Tutorial World: " .. worldTutor) end
      end
    end
  end
end

function checkTutor()
  local bot=getBot and getBot()
  while bot:isInWorld() do bot:leaveWorld(); sleep(3000) end
  worldTutor = ""; noHomeWorld = false
  print("Checking Tutorial/Home World")
  addEvent(Event.variantlist, findHomeWorld)
  for _ = 1, 3 do
    local w = (bot and bot.getWorld and bot:getWorld() and bot:getWorld().name) or ""
    if worldTutor == "" and (w:upper() == "EXIT") then
      bot:sendPacket(3, "action|world_button\nname|_16"); listenEvents(5)
    end
  end
  if worldTutor == "" then printCrit("Doesn't Have Tutorial/Home World!"); callNotif("Doesn't Have Tutorial/Home World!", true); noHomeWorld = true end
  sleep(100); removeEvent(Event.variantlist)
end

-- ##################### GET WARP #####################
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

function _current_tile_fg_safe(polls,wait_ms)
  polls=polls or 12; wait_ms=wait_ms or 120
  for _=1,polls do local fg=_current_tile_fg(); if fg and fg>=0 then return fg end; sleep(wait_ms) end
  return -1
end

function _world_public_safe()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return nil end
  local okW,w=pcall(function() return b:getWorld() end); if not okW or not w then return nil end
  local okP,pub=pcall(function() return w.public end); if not okP then return nil end
  return pub and true or false
end

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

-- ===========================================================
-- TAKE MALADY / checkMalady / ensureMalady
-- (…bagian ini sama seperti file kamu, tidak diubah logikanya…)
-- ===========================================================
-- ===========================================================
-- TAKE MALADY (ID 8542) — BLOCKING TANPA COOLDOWN
-- Stay di WORLD itu, tunggu sampai ada item 8542, ambil, pakai.
-- ===========================================================
function _gotoExact(world, door, tx, ty, path_try, step_ms)
  local b = getBot and getBot() or nil; if not b then return false end
  path_try = path_try or 10
  step_ms  = step_ms  or 700

  -- local helper to read current tile
  local function meTile()
    local w = b.getWorld and b:getWorld() or nil
    local me = w and w.getLocal and w:getLocal() or nil
    if not me then return -999,-999 end
    return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
  end

  local last_mx, last_my = nil, nil
  local stale_ticks = 0
  local backoff     = 0         -- tambahan jeda kecil saat stuck

  for _ = 1, path_try do
    local mx, my = meTile()
    if mx == tx and my == ty then return true end

    -- coba pathing
    b:findPath(tx, ty)

    -- jeda + reconnect ringan (tanpa guard door di sini)
    sleep(step_ms + backoff)
    SMART_RECONNECT(world, door)

    -- cek apakah bergerak
    local cmx, cmy = meTile()
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

function _ensure_single_item_in_storage(item_id, keep, storageW, storageD, opts)
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
      b:drop(item_id, drop_try)         -- use numeric id
      sleep(STEP_MS); SMART_RECONNECT();
      inv = b:getInventory()            -- refresh inv
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

function take_malady(WORLD, DOOR, opts)
  local b = getBot and getBot() or nil
  if not b or (USE_MALADY == false) then return false end

  opts = opts or {}
  local TARGET_ID     = 8542
  local STEP_MS       = tonumber(opts.step_ms or 800)
  local REWARP_EVERY  = tonumber(opts.rewarp_every or 180)
  local LOG_PREFIX    = "[TAKE_MALADY-BLOCK]"
  local storageW      = (STORAGE_MALADY and STORAGE_MALADY ~= "") and STORAGE_MALADY or ""
  local storageD      = (DOOR_MALADY    and DOOR_MALADY    ~= "") and DOOR_MALADY    or ""

  local function _same_world(targetW)
    local w = b.getWorld and b:getWorld() or nil
    local cw = (w and (w.name or (w.getName and w:getName()))) or ""
    return tostring(cw):upper() == tostring(targetW or ""):upper()
  end
  local function _ensure_in_world(w, d)
    if (not b:isInWorld()) or (not _same_world(w)) then
      WARP_WORLD(w, d); sleep(250); SMART_RECONNECT(w, d)
      faceSide2()
    end
  end
  local function _nearest_target_tile()
    local objs = (getObjects and getObjects()) or {}
    local me   = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
    local best, bestd2 = nil, 1e18
    for _, o in pairs(objs) do
      if o.id == TARGET_ID then
        local tx, ty = math.floor(o.x/32), math.floor(o.y/32)
        if me then
          local mx, my = math.floor(me.posx/32), math.floor(me.posy/32)
          local d2 = (tx - mx)*(tx - mx) + (ty - my)*(ty - my)
          if d2 < bestd2 then best, bestd2 = {x = tx, y = ty}, d2 end
        else
          best, bestd2 = {x = tx, y = ty}, 0
        end
      end
    end
    return best
  end

  local inv = b:getInventory()
  local last_warp = os.time()

  print(string.format("%s Menunggu item %d di %s ...", LOG_PREFIX, TARGET_ID, tostring(WORLD)))

  while true do
    _ensure_in_world(WORLD, DOOR)

    inv = b:getInventory()
    if inv:getItemCount(TARGET_ID) > 0 then
      local sw, sd = storageW, storageD
      if (sw or "") == "" then sw, sd = WORLD, DOOR end
      _ensure_single_item_in_storage(TARGET_ID, 1, sw, sd,
        {chunk=200, step_ms=600, path_try=10, tile_cap=4000, stack_cap=20, tile_retries=2})

      inv = b:getInventory()
      if inv:getItemCount(TARGET_ID) > 0 then
        b:use(TARGET_ID); sleep(250)
        print(string.format("%s Dapat & pakai item %d. Selesai.", LOG_PREFIX, TARGET_ID))
        ZEE_COLLECT(false)
        return true
      end
      -- kalau ke-drop semua saat normalize → lanjut tunggu
    end

    local tgt = _nearest_target_tile()
    if tgt then
      ZEE_COLLECT(true)
      SMART_RECONNECT(WORLD, DOOR, tgt.x, tgt.y)
      b:findPath(tgt.x, tgt.y)
      sleep(STEP_MS)
    else
      ZEE_COLLECT(true)
      SMART_RECONNECT(WORLD, DOOR)
      faceSide2()
      sleep(STEP_MS)
    end

    if (os.time() - last_warp) >= REWARP_EVERY then
      WARP_WORLD(WORLD, DOOR); sleep(200); SMART_RECONNECT(WORLD, DOOR)
      faceSide2()
      last_warp = os.time()
    end

    if opts.stop_flag and _G[opts.stop_flag] then
      print(string.format("%s Dihentikan oleh flag %s", LOG_PREFIX, tostring(opts.stop_flag)))
      ZEE_COLLECT(false)
      return false
    end
  end
end


function findStatus()
    local bot = (getBot and getBot()) or nil
    for _, con in pairs(bot:getConsole().contents) do
        if con:find("Status:") and bot.status == BotStatus.online then
            return true
        end
    end
    return false
end


function checkMalady()
    local b = (getBot and getBot()) or nil
    if b and b.isInWorld and b:isInWorld() and (b.status == BotStatus.online or b.status == 1) then
        if b.say then b:say("/status") end
        sleep(700)

        if type(findStatus)=="function" and findStatus() and b.getConsole then
            local conso = b:getConsole()
            if conso and conso.contents then
                for _, con in pairs(conso.contents) do
                    if type(con)=="string" and con:lower():find("malady:") then
                        local name = con:match("[Mm]alady:%s*([^!]+)")
                        if name then name = name:gsub("%s+$","") end

                        local h = tonumber(con:match("(%d+)%s*hours?")) or 0
                        local m = tonumber(con:match("(%d+)%s*mins?"))  or 0
                        local s = tonumber(con:match("(%d+)%s*secs?"))  or 0
                        local total = h * 3600 + m * 60 + s

                        maladyName, maladyHours, maladyMins, maladySecs, totalSeconds =
                            name, h, m, s, total

                        print(("Malady: %s. Time Left: %d hours, %d mins, %d secs")
                            :format(name or "None", h, m, s))
                        return true, total, name
                    end
                end
            end
        end
    end
    return false, nil, nil
end

-- ============================================================
----------------------------------------------------------------
-- Map kode malady -> nama (opsional, untuk log)
----------------------------------------------------------------
local MALADY_CODES = {
  [1]="Torn Punching Muscle",[2]="Gem Cuts",[3]="Chicken Feet",[4]="Grumbleteeth",
  [5]="Broken Heart",[6]="Chaos Infection",[7]="Moldy Guts",[8]="Brainworms",
  [9]="Lupus",[10]="Ecto-Bones",[11]="Fatty Liver"
}

----------------------------------------------------------------
-- Deteksi ganda (checkMalady + getBot().malady) dengan polling
-- Return: has, max_secs, code, name
--  - has       : true kalau konsensus masih ada malady (dari salah satu sumber)
--  - max_secs  : maksimum sisa detik yang teramati selama polling (nil kalau tak ada)
--  - code      : kode malady terakhir yang terlihat (0 jika tak ada)
--  - name      : nama malady terakhir (bisa nil)
----------------------------------------------------------------
local function _detect_malady_dual(polls, delay_ms)
  polls     = polls or 4
  delay_ms  = delay_ms or 1000

  local b = getBot and getBot() or nil
  local code_seen, max_secs, name_seen = 0, nil, nil
  local positive_votes, negative_votes  = 0, 0

  for i=1,polls do
    local code = 0
    if b and b.malady ~= nil then
      -- beberapa framework expose .malady sebagai integer
      code = tonumber(b.malady) or 0
    end

    local has1, secs1, name1 = checkMalady()         -- sumber /status
    local have_secs = nil
    if has1 == true then have_secs = tonumber(secs1 or 0)
    elseif has1 == false then have_secs = nil
    end

    -- gabungkan
    local any_has = (code and code>0) or (has1 == true and (have_secs or 0) > 0)

    if any_has then
      positive_votes = positive_votes + 1
      if code and code>0 then code_seen = code end
      if have_secs then
        max_secs = math.max(max_secs or 0, have_secs)
      end
      if name1 and name1 ~= "" then name_seen = name1 end
    else
      negative_votes = negative_votes + 1
      -- tetap update nama jika /status bilang None
      if name1 and name1 ~= "" then name_seen = name1 end
    end

    if i < polls then sleep(delay_ms) end
  end

  local has = (positive_votes > 0)         -- kalau salah satu polling mendeteksi masih ada, anggap "ada"
  if not has then
    max_secs = nil
    code_seen = 0
    name_seen = nil
  end
  return has, max_secs, code_seen, name_seen or (MALADY_CODES[code_seen] or nil)
end

----------------------------------------------------------------
-- Tunggu clear dengan konfirmasi berturut-turut (anti false clear)
-- syarat_clear: butuh N konfirmasi berurutan "tidak ada malady"
----------------------------------------------------------------
-- local function _wait_until_clear_consecutive(N, recheck_ms, guard_secs)
--   N = N or 3
--   recheck_ms = recheck_ms or 1000
--   local start = os.time()
--   local ok_streak = 0

--   while true do
--     local has, secs = _detect_malady_dual(1, 100)  -- single poll cepat
--     if (not has) or (secs or 0) <= 0 then
--       ok_streak = ok_streak + 1
--       if ok_streak >= N then return true end
--     else
--       ok_streak = 0
--     end
--     sleep(recheck_ms)
--     if guard_secs and (os.time() - start) >= guard_secs then
--       return false, "timeout_wait"
--     end
--   end
-- end

-- Drop-in: selalu selesai, anti-spam, dan ringkas
local function _wait_until_clear_consecutive(N, recheck_ms, guard_secs)
  N = tonumber(N) or 2
  recheck_ms = math.max(100, tonumber(recheck_ms) or 500)
  guard_secs = math.max(1, tonumber(guard_secs) or 120)

  local start = os.time()
  local ok_streak, checks = 0, 0
  local last_secs, last_change_clock = nil, os.clock()
  local max_checks = math.floor((guard_secs * 1000) / recheck_ms) + 10
  local backoff = 1.25

  while true do
    local ok, has, secs = pcall(_detect_malady_dual, 1, 100)
    if not ok then return false, "detect_error" end

    local sleft = tonumber(secs or 0) or 0

    -- kalau sisa sangat panjang, jangan tunggu di sini
    if has and sleft >= 600 then
      return false, "too_long_left"
    end

    if (not has) or sleft <= 0 then
      ok_streak = ok_streak + 1
      if ok_streak >= N then return true, "cleared" end
    else
      ok_streak = 0
    end

    -- nilai tidak berubah ≥15 dtk → anggap macet
    if last_secs ~= nil and sleft == last_secs then
      if (os.clock() - last_change_clock) >= 15 then
        return false, "stuck_value"
      end
    else
      last_secs, last_change_clock = sleft, os.clock()
    end

    checks = checks + 1
    if checks >= max_checks then return false, "max_checks" end
    if (os.time() - start) >= guard_secs then return false, "timeout_wait" end

    -- delay adaptif (anti-spam) + backoff ringan
    if sleft >= 3600 then
      recheck_ms = math.max(recheck_ms, 30000)      -- ≥1 jam → 30 dtk
    elseif sleft >= 300 then
      recheck_ms = math.max(recheck_ms, 5000)       -- ≥5 menit → 5 dtk
    elseif sleft >= 60 then
      recheck_ms = math.max(recheck_ms, 1000)       -- ≥1 menit → 1 dtk
    elseif sleft >= 6 then
      recheck_ms = math.max(recheck_ms, 500)        -- ≥6 dtk → 0.5 dtk
    else
      recheck_ms = math.min(recheck_ms, 300)        -- <6 dtk → cepat
    end
    if sleft >= 60 then
      recheck_ms = math.min(math.floor(recheck_ms * backoff), 30000)
    end

    sleep(recheck_ms)
  end
end




----------------------------------------------------------------
-- ENSURE MALADY — versi stabil (deteksi ganda + counter)
-- Behaviour:
-- 1) Ada malady & sisa > threshold    => SKIP (false,"over_threshold")
-- 2) Ada malady & sisa ≤ threshold    => WAJIB NUNGGU sampai benar2 clear (konfirmasi Nx)
-- 3) Tidak ada malady dari awal       => langsung TAKE
-- 4) TAKE: while true sampai sukses, tapi tetap ada absolute guard
----------------------------------------------------------------
local function hop_until_leave_exit(max_try)
  max_try = tonumber(max_try) or 50
  local tries = 0

  while true do
    local b = (getBot and getBot()) or nil
    local w = b and b:getWorld() or nil
    local name = (w and w.name) and tostring(w.name):upper() or ""

    -- kalau sudah bukan EXIT, selesai
    if name ~= "EXIT" and name ~= "" then
      return true
    end

    -- batas percobaan biar gak infinite
    if tries >= max_try then
      print("[WARN] Maks percobaan tercapai, masih di EXIT.")
      if b.disconnect then b:disconnect() elseif type(disconnect)=="function" then disconnect() end
      SMART_RECONNECT(); sleep(100)
      local tries = 0
      -- return false
    end

    local wr = random_kata(4, true)
    WARP_WORLD(wr); sleep(100)
    SMART_RECONNECT(wr); sleep(100)

    tries = tries + 1
  end
end

-- pakai:
-- hop_until_leave_exit(50)


-- function ensureMalady(threshold_min, opts)
--   local minutes     = tonumber(threshold_min or 5) or 5
--   local THRESH_SECS = math.floor(minutes * 60)

--   local b = getBot and getBot() or nil
--   local w = b and b:getWorld() or nil
--   hop_until_leave_exit(10)
--   if not w or not w.name or tostring(w.name):upper() == "EXIT" then
--     return false, "not_in_world"
--   end

--   if (not STORAGE_MALADY) or STORAGE_MALADY == "" then
--     return false, "storage_not_set"
--   end
--   local useW, useD = STORAGE_MALADY, (DOOR_MALADY or "")

--   -- 1) Baca konsensus awal (poll 4x) → robust
--   local has, max_secs, code, nm = _detect_malady_dual(2, 1000)

--   -- 2) Kalau masih ada & sisa > threshold → SKIP
--   if has and (max_secs or 0) > THRESH_SECS then
--     -- log kecil (opsional)
--     if code and code>0 then
--       print(string.format("[MALADY] Detected %s (code %d), sisa ~%ds > %d → skip.",
--         nm or "Unknown", code, max_secs or -1, THRESH_SECS))
--     end
--     return false, "over_threshold"
--   end

--   -- 3) Kalau masih ada tetapi sisa ≤ threshold → WAJIB nunggu clear
--   if has and (max_secs or 0) <= THRESH_SECS then
--     print(string.format("[MALADY] Sisa %ds ≤ %d. Menunggu CLEAR dengan konfirmasi beruntun...",
--       max_secs or 0, THRESH_SECS))
--     local ok, why = _wait_until_clear_consecutive(3, 1000, math.max(THRESH_SECS + 120, 240))
--     if not ok then
--       return false, why or "timeout_wait"
--     end
--   end
--   -- titik ini CLEAR (baik dari awal, atau setelah nunggu)

--   -- 4) LOOP TAKE SAMPAI SUKSES (dengan absolute guard)
--   local started = os.time()
--   local attempt = 0
--   local ABS_GUARD_SECS  = 600           -- 10 menit
--   local REWARP_EVERY    = 5             -- re-warp tiap 5 attempt
--   local BACKOFF_MS      = 600

--   while true do
--     attempt = attempt + 1
--     if (attempt % REWARP_EVERY) == 1 then
--       if SMART_RECONNECT then pcall(SMART_RECONNECT, useW, useD) end
--       if WARP_WORLD then pcall(WARP_WORLD, useW, useD) end
--       sleep(300)
--     end

--     local ok = take_malady(useW, useD, opts or { step_ms = 700, rewarp_every = 180 })
--     if ok then
--       return true, "taken"
--     end

--     sleep(BACKOFF_MS)
--     if (os.time() - started) >= ABS_GUARD_SECS then
--       return false, "take_timeout"
--     end

--     -- ekstra defensif: kalau tiba2 terdeteksi malady lagi (efek visual / lag), tunggu sebentar
--     local h2, s2 = _detect_malady_dual(2, 800)
--     if h2 and (s2 or 0) > 0 then
--       -- bila ternyata muncul lagi & sisa kecil, tunggu clear lagi
--       if (s2 or 0) <= THRESH_SECS then
--         _wait_until_clear_consecutive(2, 1000, math.max(THRESH_SECS + 60, 180))
--       else
--         -- sisa besar → hentikan (caller bisa panggil ensureMalady lagi nanti)
--         return false, "over_threshold"
--       end
--     end
--   end
-- end


function ensureMalady(threshold_min, opts)
  opts = opts or {}
  local minutes     = tonumber(threshold_min or 5) or 5
  local THRESH_SECS = math.floor(minutes * 60)

  -- pastikan tidak di EXIT (dan refresh w setelah hop)
  if hop_until_leave_exit then pcall(hop_until_leave_exit, 10) end
  local b = (getBot and getBot()) or nil
  local w = b and b:getWorld() or nil
  local wname = (w and w.name) and tostring(w.name):upper() or ""
  if wname == "" or wname == "EXIT" then
    return false, "not_in_world"
  end

  if (not STORAGE_MALADY) or STORAGE_MALADY == "" then
    return false, "storage_not_set"
  end
  local useW, useD = STORAGE_MALADY, (DOOR_MALADY or "")

  -- 1) Konsensus awal (robust & cepat)
  local okDetect, has, max_secs, code, nm = pcall(_detect_malady_dual, 2, 500)
  if not okDetect then
    return false, "detect_error"
  end
  max_secs = tonumber(max_secs or 0) or 0

  -- 2) Jika sisa > threshold → SKIP (jangan tunggu panjang di sini)
  if has and max_secs > THRESH_SECS then
    if code and code > 0 then
      print(string.format("[MALADY] %s (code %d) ~%ds > %d → skip.",
        nm or "Unknown", code, max_secs, THRESH_SECS))
    end
    return false, "over_threshold"
  end

  -- 3) Jika sisa ≤ threshold → tunggu CLEAR singkat (guard kecil supaya tidak nyangkut)
  if has and max_secs <= THRESH_SECS then
    print(string.format("[MALADY] Sisa %ds ≤ %d. Menunggu clear singkat...",
      max_secs, THRESH_SECS))
    local okWait, why = _wait_until_clear_consecutive(2, 400, math.max(THRESH_SECS + 30, 45))
    if not okWait then
      return false, why or "timeout_wait"
    end
  end
  -- titik ini dianggap CLEAR (dari awal atau setelah wait singkat)

  -- 4) Coba TAKE (bounded attempts; tidak pakai while true)
  local MAX_TRY       = tonumber(opts.max_try or 12)  -- ~12 percobaan
  local REWARP_EVERY  = tonumber(opts.rewarp_every or 4)
  local BACKOFF_MS    = tonumber(opts.backoff_ms or 600)
  local started       = os.time()
  local ABS_GUARD_SECS= tonumber(opts.take_guard_secs or 120) -- guard total ambil (2 menit)

  for attempt = 1, MAX_TRY do
    if (attempt % REWARP_EVERY) == 1 then
      if SMART_RECONNECT then pcall(SMART_RECONNECT, useW, useD) end
      if WARP_WORLD      then pcall(WARP_WORLD,      useW, useD) end
      sleep(250)
    end

    local okTake = false
    local okCall, whyCall = pcall(function()
      okTake = take_malady(useW, useD, { step_ms = 650, rewarp_every = 180 })
    end)
    if okCall and okTake then
      return true, "taken"
    end

    -- jika tiba-tiba terdeteksi malady lagi, putuskan cepat (jangan loop lama)
    local okD2, h2, s2 = pcall(_detect_malady_dual, 2, 500)
    if okD2 and h2 and (s2 or 0) > 0 then
      s2 = tonumber(s2 or 0) or 0
      if s2 <= THRESH_SECS then
        _wait_until_clear_consecutive(2, 400, math.max(THRESH_SECS + 30, 45))
      else
        return false, "over_threshold"
      end
    end

    if (os.time() - started) >= ABS_GUARD_SECS then
      return false, "take_timeout"
    end
    sleep(BACKOFF_MS)
  end

  return false, "take_exhausted"
end


-------------------- SMART DROP SNAKE & MULTI STORAGE --------------------
WORLD_MAX_X, WORLD_MAX_Y = WORLD_MAX_X or 99, WORLD_MAX_Y or 23
function REFRESH_WORLD_BOUNDS()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return end
  local w=b:getWorld(); if not w then return end
  local wx=(w.width and (w.width-1)) or WORLD_MAX_X
  local wy=(w.height and (w.height-1)) or WORLD_MAX_Y
  WORLD_MAX_X, WORLD_MAX_Y = wx, wy
end

function _my_xy()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return 0,0 end
  local w=b:getWorld(); local me=w and w:getLocal() or nil; if not me then return 0,0 end
  return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
end
function _is_in_bounds(x,y) return x>=0 and x<=WORLD_MAX_X and y>=0 and y<=WORLD_MAX_Y end
function _is_walkable(tx,ty)
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return false end
  local w=b:getWorld(); local t=w and w:getTile(tx,ty) or nil
  return (t~=nil) and ((t.fg or 0)==0)
end

-- … (DROP_ITEMS_SNAKE dari file kamu, tidak diubah) …
-------------------- SMART DROP SNAKE (kanan→atas, fallback kiri) --------------------
WORLD_MAX_X, WORLD_MAX_Y = WORLD_MAX_X or 99, WORLD_MAX_Y or 23 -- map kecil: x:0..99, y:0..23
function REFRESH_WORLD_BOUNDS()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return end
  local w=b:getWorld(); if not w then return end
  local wx=(w.width and (w.width-1)) or WORLD_MAX_X
  local wy=(w.height and (w.height-1)) or WORLD_MAX_Y
  WORLD_MAX_X, WORLD_MAX_Y = wx, wy
end

function _my_xy()
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return 0,0 end
  local w=b:getWorld(); local me=w and w:getLocal() or nil; if not me then return 0,0 end
  return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
end
function _is_in_bounds(x,y) return x>=0 and x<=WORLD_MAX_X and y>=0 and y<=WORLD_MAX_Y end
function _is_walkable(tx,ty)
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return false end
  local w=b:getWorld(); local t=w and w:getTile(tx,ty) or nil
  return (t~=nil) and ((t.fg or 0)==0)
end

function _probe_slot(cx,cy,tile_cap,stack_cap)
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

function _scan_row_right(start_x, cy, tile_cap, stack_cap)
  local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
  while cx<=WORLD_MAX_X do if _probe_slot(cx,cy,tile_cap,stack_cap) then return cx,cy end; cx=cx+1 end
  return nil,nil
end
function _scan_row_left(start_x, cy, tile_cap, stack_cap)
  local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
  while cx>=0 do if _probe_slot(cx,cy,tile_cap,stack_cap) then return cx,cy end; cx=cx-1 end
  return nil,nil
end

function _nextDropTileSnake_auto(sx,sy,cursor,tile_cap,stack_cap)
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


-- ===== helper normalize & scan stable (dipakai ring storage) =====
local function _normalize_storage_list(list)
  local out = {}
  if type(list) ~= "table" then return out end
  for _, entry in ipairs(list) do
    if type(entry) == "string" and entry ~= "" then
      local w,d = entry:match("^([^|]+)|?(.*)$")
      table.insert(out, { world=tostring(w or ""), door=tostring(d or "") })
    elseif type(entry) == "table" and entry.world then
      table.insert(out, { world=tostring(entry.world), door=tostring(entry.door or "") })
    end
  end
  return out
end

-- [ANTI-SPAM NUKED] warp sync + guard nuked SEED
local function _warp_sync_seed(W, D)
  if (W or "") == "" then return false, "no_world" end
  -- skip kalau sedang cooldown anti-spam
  if should_skip_world("seed", W) then
    return false, "seed_cooldown"
  end
  local ok = WARP_WORLD(W, D)
  sleep(200)
  if not ok or NUKED_STATUS then
    mark_world_nuked("seed", W, D)
    return false, "nuked"
  end
  SMART_RECONNECT(W, D)
  -- sukses → bersihkan counter (opsional)
  clear_world_counter("seed", W)
  return true, "ok"
end

-- scan stabil (ambil maksimum dari 2 pembacaan singkat)
local function _scan_stable(id)
  local a = tonumber(scan(id) or 0) or 0
  sleep(120)
  local b = tonumber(scan(id) or 0) or 0
  return (a > b) and a or b
end

local function _seed_ring_init()
  if _SEED_RING.list and #_SEED_RING.list > 0 then return end
  _SEED_RING.list = _normalize_storage_list(STORAGE_SEED)
  _SEED_RING.idx  = math.min(_SEED_RING.idx or 1, math.max(1, #_SEED_RING.list))
  _SEED_RING.full = {}
end

local function _seed_ring_reset_marks()
  _SEED_RING.full = {}
end

-- pick storage dengan kapasitas (pakai anti-spam)
local function _seed_ring_pick_with_capacity(item_id, per_world_cap)
  _seed_ring_init()
  local cap_max = tonumber(per_world_cap or LIMIT_SEED_STORAGE) or 54000
  local n = #_SEED_RING.list
  if n == 0 then return nil end

  local start_i = _SEED_RING.idx
  local i = start_i
  repeat
    if not _SEED_RING.full[i] then
      local S = _SEED_RING.list[i]
      local W, D = S.world, S.door

      local okSync, why = _warp_sync_seed(W, D)
      if okSync then
        local total_here = _scan_stable(item_id)
        local free_cap   = cap_max - total_here
        if free_cap > 0 then
          _SEED_RING.idx = i
          return i, W, D, free_cap
        else
          _SEED_RING.full[i] = true
          _random_world_list()
        end
      else
        _SEED_RING.full[i] = true
        if why == "nuked" then log_fail(W, D, "nuked(seed)") end
      end
    end
    i = (i % n) + 1
  until i == start_i

  return nil
end

local function _seed_ring_advance()
  if not _SEED_RING.list or #_SEED_RING.list == 0 then return end
  local n = #_SEED_RING.list
  _SEED_RING.idx = (_SEED_RING.idx % n) + 1
end

local function _drop_to_world_limit(item_id, max_to_drop, W, D)
  local b = getBot and getBot() or nil
  if not b then return false end
  max_to_drop = math.max(0, tonumber(max_to_drop or 0) or 0)
  if max_to_drop == 0 then return true end

  local okSync, why = _warp_sync_seed(W, D)
  if not okSync then return false end

  if type(DROP_ITEMS_SNAKE) == "function" then
    DROP_ITEMS_SNAKE(W, D, { item_id }, {
      max_total_to_drop = max_to_drop,
      step_ms = 700, tile_cap = 3000, stack_cap = 20, path_try = 10, tile_retries = 2
    })
    return true
  end

  local CHUNK = 400
  while max_to_drop > 0 do
    local have = b:getInventory():getItemCount(item_id)
    if have <= 0 then return true end
    local to_drop = math.min(CHUNK, have, max_to_drop)
    b:drop(item_id, to_drop)
    sleep(700)
    SMART_RECONNECT(W, D)
    local after = b:getInventory():getItemCount(item_id)
    local dropped = have - after
    if dropped <= 0 then
      WARP_WORLD(W, D); sleep(300)
    else
      max_to_drop = math.max(0, max_to_drop - dropped)
    end
  end
  return true
end

function DROP_SEEDS_MULTI(stor_list, item_id, per_world_cap)
  local b = getBot and getBot() or nil
  if not b then return false, "no_bot" end

  _SEED_RING.list = _normalize_storage_list(stor_list or STORAGE_SEED)
  if #_SEED_RING.list == 0 then return false, "storage_list_empty" end
  if _SEED_RING.idx < 1 or _SEED_RING.idx > #_SEED_RING.list then _SEED_RING.idx = 1 end

  while true do
    local have = b:getInventory():getItemCount(item_id)
    if have <= 0 then return true, "done" end

    local i, W, D, free = _seed_ring_pick_with_capacity(item_id, per_world_cap)
    if not i then
      _seed_ring_reset_marks()
      _SEED_RING.idx = 1
      local ii, WW, DD, free2 = _seed_ring_pick_with_capacity(item_id, per_world_cap)
      if not ii then return false, "all_storage_full" end
      i, W, D, free = ii, WW, DD, free2
    end

    local to_drop = math.min(have, free)
    local ok = _drop_to_world_limit(item_id, to_drop, W, D)
    if ok and to_drop >= free then _SEED_RING.full[i] = true end
    _seed_ring_advance()
  end
end

-- ##################### TAKE BLOCK #####################
function TAKE_BLOCK(world, door, opts)
  local b = getBot and getBot() or nil
  if not b then return false, "no_bot" end

  -- [ANTI-SPAM NUKED] skip jika world sedang cooldown
  if should_skip_world("block", world) then
    return false, "block_cooldown"
  end

  local TARGET_ID = ID_BLOCK
  opts = opts or {}
  local target_min     = tonumber(opts.min_stack or 20)
  local max_rounds     = tonumber(opts.max_rounds or 40)
  local wait_ms        = tonumber(opts.wait_ms or 1200)
  local max_miss       = tonumber(opts.max_miss or 5)
  local max_time_secs  = tonumber(opts.max_time_secs or 180)

  -- Cek inventory awal
  local inv = b:getInventory()
  if inv:getItemCount(TARGET_ID) >= target_min then
    clear_world_counter("block", world)
    return true, "done"
  end

  -- WARP & RECONNECT
  local okW = WARP_WORLD(world, door)
  sleep(250)
  SMART_RECONNECT(world, door)
  if (not okW) or NUKED_STATUS then
    mark_world_nuked("block", world, door)
    return false, "nuked"
  end

  -- Syarat awal: harus terdeteksi ada objek ID_BLOCK
  if not scan or not scan(TARGET_ID) then
    return false, "not_found"
  end

  ZEE_COLLECT(true)
  local start_time = os.time()
  local miss_streak = 0

  for round = 1, max_rounds do
    -- Guard waktu total
    if (os.time() - start_time) >= max_time_secs then
      ZEE_COLLECT(false)
      return false, "timeout"
    end

    -- Cek inventory cukup?
    inv = b:getInventory()
    if inv:getItemCount(TARGET_ID) >= target_min then
      ZEE_COLLECT(false)
      clear_world_counter("block", world)
      return true, "done"
    end

    -- Cari objek terdekat
    local objs = (getObjects and getObjects()) or {}
    local me   = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
    local best, bestd2 = nil, 1e18

    for _, o in pairs(objs) do
      if o.id == TARGET_ID then
        local txo, tyo = math.floor(o.x/32), math.floor(o.y/32)
        if me then
          local mx, my = math.floor(me.posx/32), math.floor(me.posy/32)
          local d2 = (txo-mx)*(txo-mx) + (tyo-my)*(tyo-my)
          if d2 < bestd2 then best, bestd2 = o, d2 end
        else
          best, bestd2 = o, 0
        end
      end
    end

    if best then
      miss_streak = 0
      local tx, ty = math.floor(best.x/32), math.floor(best.y/32)
      SMART_RECONNECT(world, door, tx, ty)
      b:findPath(tx, ty)
      sleep(wait_ms)
    else
      miss_streak = miss_streak + 1
      if miss_streak >= max_miss then
        ZEE_COLLECT(false)
        return false, "not_found"
      end
      SMART_RECONNECT(world, door)
      if NUKED_STATUS then
        ZEE_COLLECT(false)
        mark_world_nuked("block", world, door)
        return false, "nuked"
      end
      sleep(wait_ms)
    end
  end

  ZEE_COLLECT(false)
  return false, (miss_streak >= max_miss) and "not_found" or "timeout"
end

-- ##################### PNB SULAP #####################
function pnb_sulap()
  local b = getBot and getBot() or nil
  if not b then return end

  if (worldTutor or "") == "" then
    if type(checkTutor) == "function" then checkTutor() end
  end
  local w = worldTutor
  if (w or "") == "" then print("[PNB] Tidak punya Tutorial/Home World. Abort."); return end

  WARP_WORLD(w); sleep(100)
  ensureMalady(6, { wait_confirmations = 2, recheck_ms = 500, guard_secs = 120 })

  SMART_RECONNECT(w); sleep(100)

  local function pos_now()
    local me = b:getWorld() and b:getWorld():getLocal() or nil
    if not me then return nil, nil end
    return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
  end

  local counter, COUNTER_MAX = 0, 150
  local function soft_reset()
    counter = counter + 1
    if counter >= COUNTER_MAX then
      counter = 0
      if b.disconnect then b:disconnect() elseif type(disconnect)=="function" then disconnect() end
      sleep(1200)
      SMART_RECONNECT(w); sleep(120)
    end
  end

  local inv = b:getInventory()
  ZEE_COLLECT(true)

  while inv:getItemCount(ID_BLOCK) > 0 and inv:getItemCount(ID_SEED) < LIMIT_SEED_IN_BP do
    -- PLACE
    while true do
      local ex, ye = pos_now(); if not ex then break end
      if not tilePlace(ex, ye) then break end
      local acted = false
      for _, off in ipairs(TILE_BREAK) do
        local wx, wy = ex + 1, ye + off
        local t = b:getWorld():getTile(wx, wy)
        if (t.fg or 0) == 0 then
          local before_fg = t.fg or 0
          b:place(wx, wy, ID_BLOCK); sleep(DELAY_PUT); SMART_RECONNECT()
          local t2 = b:getWorld():getTile(wx, wy)
          if t2 and (t2.fg or 0) ~= before_fg and (t2.fg or 0) ~= 0 then acted = true; soft_reset(); break end
        end
      end
      if not acted then break end
      inv = b:getInventory(); if inv:getItemCount(ID_BLOCK) <= 0 then break end
    end

    -- PUNCH
    while true do
      local ex, ye = pos_now(); if not ex then break end
      if not tilePunch(ex, ye) then break end
      local acted = false
      for _, off in ipairs(TILE_BREAK) do
        local wx, wy = ex + 1, ye + off
        local t = b:getWorld():getTile(wx, wy)
        if (t.fg or 0) ~= 0 then
          b:hit(wx, wy); sleep(DELAY_BREAK); SMART_RECONNECT()
          local t2 = b:getWorld():getTile(wx, wy)
          if t2 and (t2.fg or 0) == 0 then acted = true; soft_reset(); break end
        end
      end
      if not acted then break end
      inv = b:getInventory(); if inv:getItemCount(ID_SEED) >= LIMIT_SEED_IN_BP then break end
    end

    inv = b:getInventory()
  end

  ZEE_COLLECT(false)

  if inv:getItemCount(ID_SEED) >= LIMIT_SEED_IN_BP then
    local inv2 = getBot():getInventory()
    if inv2:getItemCount(ID_SEED) >= (LIMIT_SEED_IN_BP or 18000) then
      local ok, why = DROP_SEEDS_MULTI(STORAGE_SEED, ID_SEED, LIMIT_SEED_STORAGE)
      if not ok and why == "all_storage_full" then
        print(("[SEED] Semua storage ≥ %d. Tambah storage atau kosongkan dulu."):format(LIMIT_SEED_STORAGE))
      end
    end
  end
end

-- ==========================================
-- MAIN SULAP — break kalau block habis, skip nuked (counter)
-- ==========================================
function main_sulap(world_block, door_block)
  -- [ANTI-SPAM NUKED] skip cepat kalau masih cooldown
  if should_skip_world("block", world_block) then
    log_fail(world_block, door_block, "skip(block_cooldown)")
    return false, "block_cooldown"
  end

  while true do
    local ok, reason = TAKE_BLOCK(world_block, door_block, {
      min_stack = 20, max_rounds = 40, wait_ms = 1200, max_miss = 5, max_time_secs = 180
    })

    if ok then
      pnb_sulap()
    else
      if reason == "not_found" then
        print("[SULAP] Block ID_BLOCK sudah tidak ditemukan. Stop loop.")
        break
      elseif reason == "timeout" then
        print("[SULAP] Timeout ambil block. Re-sync world & coba lagi.")
        SMART_RECONNECT(world_block, door_block); sleep(1500)
      elseif reason == "nuked" then
        -- counter sudah di-mark di TAKE_BLOCK
        return false, "nuked"
      elseif reason == "block_cooldown" then
        return false, "block_cooldown"
      else
        print("[SULAP] Gagal ambil block: " .. tostring(reason)); sleep(1200)
      end
    end
  end

  print("[SULAP] Selesai: tidak ada block tersisa.")
  return true, "done"
end

-- ==========================================
-- LOOP GLOBAL
-- ==========================================
while true do
  if MODE == "SULAP" then
    if not CHECK_WORLD_TUTORIAL then checkTutor(); CHECK_WORLD_TUTORIAL = true end
    
    for i = 1, #LIST_WORLD_BLOCK do
      local entry = LIST_WORLD_BLOCK[i]
      if entry and entry ~= "" then
        local world_block, door_block = entry:match("^([^|]+)|?(.*)$")
        world_block = tostring(world_block or ""); door_block  = tostring(door_block or "")
        -- skip cepat jika cooldown
        if should_skip_world("block", world_block) then
          log_fail(world_block, door_block, "skip(block_cooldown)")
        else
          ensureMalady(6, { wait_confirmations = 2, recheck_ms = 500, guard_secs = 120 })

          local ok, rs = main_sulap(world_block, door_block)
          if ok then clear_world_counter("block", world_block) end
          if rs == "nuked" then log_fail(world_block, door_block, "nuked@main") end
        end
      end
      _random_world_list()
    end

    ZEE_COLLECT(false)
    local b = (getBot and getBot()) or nil
    if b and b.leaveWorld then b:leaveWorld() end
    sleep(10*60*1000)  -- 10 menit (ms)
    if b then b.auto_reconnect = true end

  elseif MODE == "PNB" then
    -- jalankan mode PNB kamu di sini (opsional)
  else
    print("PLEASE INPUT MODE !!!!")
  end
end
