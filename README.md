-- =========================
-- KONFIG & LIST
-- =========================

-- Normalisasi base path (default ke folder kamu)
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/JOB-PNB/")
  :gsub("[/\\]?$", "/")   -- pastikan selalu berakhir dengan "/"
-- Lokasi file
local FILE_BLOCK = extraFilePath .. "WORLD_BLOCK.txt"
local FILE_SEED  = extraFilePath .. "WORLD_SEED.txt"

-- LIST_WORLD_BLOCK = {
--   "FENCEMM1|NOWXX123",
--   "WORU15|NOWXX123",
--   "BOHKARA|NOWXX123",
-- }

-- STORAGE_SEED = {
--   "AFILFENCE10|NOWXX123",
--   "LEOD83|NOWXX123",
--   "FENCEMM100|NOWXX123",
-- }

USE_TXT_QUEUE                            = true      -- list world use is txt
MODE                                     = "SULAP"   -- SULAP | PNB
STORAGE_MALADY, DOOR_MALADY, AUTO_MALADY = "COKANJI", "XX1", true
STORAGE_JAMMER, DOOR_JAMMER, AUTO_JAMMER = "COKANJI", "XX1", true
POS_DROP_MALADY, POS_DROP_JAMMER         = 3, 15 -- POS BG
MALADY_NAME                              = 2               -- 1=Moldy Guts, 2=Brainworms, 3=Lupus, 4=Ecto-Bones, 5=Fatty Liver
SHOW_PUNCH                               = false
RANDOM_WORLD_AFTER_CHANGE_WORLD          = true
JUMLAH_RANDOM_WORLD                      = 4
DELAY_AFK_AFTER_ALL_WORLD                = 10 -- MENITE
LIMIT_SEED_STORAGE                       = 81000  -- kapasitas per world
ID_BLOCK                                 = 8640
LIMIT_SEED_IN_BP                         = 190
JUMLAH_TILE_BREAK                        = 3
DELAY_RECONNECT                          = 20000
DELAY_BAD_SERVER                         = 120000
DELAY_BREAK                              = 180
DELAY_PUT                                = 120
DELAY_WARP                               = 7000
DELAY_EXE                                = 2000

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
MALADY_NOT_FASTER = MALADY_NOT_FASTER or 0  -- init sekali
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

-- ##################### GET TXT #####################

-- (opsional) buat folder jika belum ada (Windows-only, aman diabaikan jika ada)
os.execute(('mkdir "%s" 2>nul'):format(extraFilePath))

-- cache untuk deteksi perubahan (tanpa dependency lfs)
local _LIST_CACHE = {
  block = {hash="", data={}},
  seed  = {hash="", data={}},
}

local function _trim(s) return (s or ""):gsub("^%s+",""):gsub("%s+$","") end
local function _is_comment_or_empty(line)
  local t = _trim(line)
  return t == "" or t:match("^#") or t:match("^//") or t:match("^%-%-")
end

local function _read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local all = f:read("*a"); f:close()
  return all or ""
end

local function _hash(s)
  -- hash sederhana agar ringan: panjang + jumlah byte
  local sum, len = 0, #(s or "")
  for i=1,len do sum = (sum + string.byte(s, i)) % 2147483647 end
  return tostring(len) .. ":" .. tostring(sum)
end

local function _parse_world_list(text)
  -- Keluaran: array string "WORLD|DOOR"
  local out = {}
  for line in (text or ""):gmatch("[^\r\n]+") do
    if not _is_comment_or_empty(line) then
      local t = _trim(line)
      -- Normalisasi: huruf besar, strip spasi di sekitar '|'
      t = t:upper():gsub("%s*|%s*", "|")
      -- Valid minimal: ada WORLD, DOOR opsional
      if t:match("^[A-Z0-9_%-]+|?[A-Z0-9_%-]*$") then
        table.insert(out, t)
      end
    end
  end
  return out
end

local function _load_one(kind, path)
  local text = _read_file(path)
  if not text then return false, "no_file" end
  local h = _hash(text)
  if _LIST_CACHE[kind].hash == h and #_LIST_CACHE[kind].data > 0 then
    return false, "no_change"
  end
  local parsed = _parse_world_list(text)
  _LIST_CACHE[kind].hash = h
  _LIST_CACHE[kind].data = parsed
  return true, "updated"
end

-- Panggil ini sekali di awal
function load_world_lists_from_txt()
  _load_one("block", FILE_BLOCK)
  _load_one("seed",  FILE_SEED )

  -- Fallback: kalau TXT kosong/ga ada, pakai default lama (kalau mau)
  if #_LIST_CACHE.block.data == 0 then
    _LIST_CACHE.block.data = {
      -- "FENCEMM1|NOWXX123", "WORU15|NOWXX123", "BOHKARA|NOWXX123"
    }
  end
  if #_LIST_CACHE.seed.data == 0 then
    _LIST_CACHE.seed.data = {
      -- "AFILFENCE10|NOWXX123", "LEOD83|NOWXX123", "FENCEMM100|NOWXX123"
    }
  end

  -- Tetap sediakan variabel global lama agar kode lain tidak perlu diubah
  LIST_WORLD_BLOCK = _LIST_CACHE.block.data
  STORAGE_SEED     = _LIST_CACHE.seed.data
end

-- Panggil ini berkala (mis. tiap loop) agar bisa hot-reload saat TXT di-edit
function reload_world_lists_if_changed()
  local bUp = _load_one("block", FILE_BLOCK)
  local sUp = _load_one("seed",  FILE_SEED )
  if bUp or sUp then
    LIST_WORLD_BLOCK = _LIST_CACHE.block.data
    STORAGE_SEED     = _LIST_CACHE.seed.data
    print("[LIST] World lists reloaded from TXT.")
  end
end


-- ##################### BATAS #####################


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
    ensureMalady(true)
  end

  if WORLD and DOOR then WARP_WORLD((WORLD or ""):upper(), DOOR)
  elseif WORLD then       WARP_WORLD((WORLD or ""):upper()) end

  if POSX and POSY then local b=getBot and getBot() or nil; if b and b.findPath then b:findPath(POSX,POSY) end end
end

function ZEE_COLLECT(state, Range_Collect)
  local b = (getBot and getBot()) or nil
  if not b then return end

  -- default 5 kalau tidak diisi (atau tidak bisa dikonversi ke number)
  local range = (Range_Collect ~= nil and tonumber(Range_Collect)) or 5
  if range < 1 then range = 1 end  -- opsional: jaga-jaga biar gak 0/negatif

  if state then
    b.auto_collect = true
    b.ignore_gems = true
    b.collect_range = range
    b.object_collect_delay = 200
  else
    b.auto_collect = false
  end

  b.legit_mode = SHOW_PUNCH and true or false
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


-- GLOBAL storage (dipakai handler & checker)
worldTutor = ""
noHomeWorld = false

-- Handler dialog "My Worlds"
function WorldMenu(var, netid)
  local v0 = var and var:get(0)
  if not v0 or v0:getString() ~= "OnDialogRequest" then return end

  local v1 = var:get(1)
  if not v1 then return end

  local s = v1:getString() or ""
  -- cari tab myWorlds (case-insensitive, tanpa pola regex berat)
  if s:lower():find("myworldsuitab", 1, true) then
    -- ambil label tombol pertama "add_button|<WORLD>|..."
    local nilai = s:match("add_button|([^|]+)|")
    if nilai then
      nilai = (nilai:gsub("%s+", ""))  -- bersihkan spasi
      worldTutor = nilai
      print("Tutorial World: " .. worldTutor)
    end
  end
end

function checkTutor()
  local bot = (type(getBot) == "function") and getBot() or nil
  if not bot then
    printCrit("Bot object not available"); return false, "no_bot"
  end

  -- reset global sebelum listen event
  worldTutor  = ""
  noHomeWorld = false

  local MAX_TRY_ENTER = 15
  local tries = 0

  -- Masuk ke world apa saja sampai in-world
  while (not bot:isInWorld()) and tries < MAX_TRY_ENTER do
    local wr = random_kata(4, true)
    WARP_WORLD(wr)
    sleep(100)
    if type(SMART_RECONNECT) == "function" then SMART_RECONNECT(wr) end
    sleep(7000)
    tries = tries + 1
  end

  if not bot:isInWorld() then
    printCrit("Failed to enter any world after retries")
    return false, "enter_world_failed"
  end

  -- Pasang listener dan pastikan dilepas
  addEvent(Event.variantlist, WorldMenu)
  local function _cleanup()
    pcall(removeEvent, Event.variantlist)
  end

  -- Kirim paket untuk buka dialog "My Worlds"
  local lc = (type(getLocal) == "function") and getLocal() or nil
  if not lc or not lc.netid then
    _cleanup()
    printCrit("Local player not ready")
    return false, "local_not_ready"
  end

  bot:sendPacket(2, "action|wrench\n|netid|" .. tostring(lc.netid))
  sleep(1000)
  bot:sendPacket(2,
    "action|dialog_return\ndialog_name|popup\nnetID|" ..
    tostring(lc.netid) .. "|\nbuttonClicked|my_worlds"
  )

  -- Tunggu event mengisi worldTutor
  listenEvents(5)
  sleep(5000)

  print("ini nilai world tutorial: " .. (worldTutor or ""))

  if worldTutor == "" then
    printCrit("Doesn't Have Tutorial/Home World!")
    if type(callNotif) == "function" then
      callNotif("Doesn't Have Tutorial/Home World!", true)
    end
    noHomeWorld = true
  end

  _cleanup()
  return (not noHomeWorld), (worldTutor ~= "" and worldTutor or nil)
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

-- Tambahan kecil yang dipakai berulang
local function _force_reconnect()
  local b = (getBot and getBot()) or nil
  if b and b.disconnect then
    print("[WARP_WORLD] 4x gagal. Force disconnect -> reconnect...")
    pcall(function() b:disconnect() end)
    sleep(1200)
  end
  if type(SMART_RECONNECT) == "function" then
    SMART_RECONNECT()
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
    if not tryDoor or (fg~=6) then
      CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET= tryDoor and DOOR or nil; _cleanup(); return true
    end
  end

  local cycles=0
  while cycles<(MAX_RECOLL_CYCLES or 1) do
    cycles=cycles+1
    local attempt, ok = 0, false
    local fail_streak = 0  -- <== counter 4x gagal untuk warp world

    while attempt<(MAX_WARP_RETRY or 10) do
      if _current_world_upper()==WORLD then ok=true; break end
      attempt=attempt+1

      local b=getBot and getBot() or nil
      if b and b.warp then
        if tryDoor and DOOR~="" then b:warp(WORLD.."|"..DOOR) else b:warp(WORLD) end
      else
        print("[WARP_WORLD] getBot() not available."); _cleanup(); return false
      end

      if type(listenEvents)=="function" then listenEvents(5) end
      if NUKED_STATUS then print("[WARP_WORLD] Nuked saat warp."); _cleanup(); return false end

      sleep(DELAY_WARP); if type(SMART_RECONNECT)=="function" then SMART_RECONNECT() end
      if _current_world_upper()==WORLD then ok=true; break end

      -- == LOGIKA COUNTER 4x GAGAL ==
      fail_streak = fail_streak + 1
      if fail_streak >= 4 then
        _force_reconnect()
        fail_streak = 0 -- reset setelah forced reconnect
      end
      -- ===============================
    end

    if ok then break end
  end

  if _current_world_upper()~=WORLD then
    print("[WARP_WORLD] Gagal warp."); _cleanup(); return false
  end

  local pub=_world_public_safe(); if pub~=nil then WORLD_IS_PUBLIC=pub; print(pub and "[WARP] PUBLIC" or "[WARP] PRIVATE/LOCKED") end

  if tryDoor then
    local fg=_current_tile_fg_safe(15,120)
    if fg>=0 and fg~=6 then
      CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true
    end

    -- Door tidak kebaca (fg<0) → ulangi dengan counter 4x juga
    if fg<0 then
      local fail_streak_door = 0
      for _=1,(MAX_DOOR_RETRY or 5) do
        local b=getBot and getBot() or nil
        if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked door."); _cleanup(); return false end
        sleep(DELAY_WARP); if type(SMART_RECONNECT)=="function" then SMART_RECONNECT() end

        fg=_current_tile_fg_safe(8,120)
        if fg>=0 and fg~=6 then
          CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true
        end

        -- == LOGIKA COUNTER 4x GAGAL DI DOOR ==
        fail_streak_door = fail_streak_door + 1
        if fail_streak_door >= 4 then
          _force_reconnect()
          fail_streak_door = 0
        end
        -- ======================================
      end
      _cleanup(); return false
    end

    -- Masih di white door (fg==6) → coba lagi, dengan counter 4x juga
    if fg==6 then
      local fail_streak_door = 0
      for dtry=1,(MAX_DOOR_RETRY or 5) do
        local b=getBot and getBot() or nil
        if b and b.warp then b:warp(WORLD.."|"..DOOR) end
        if type(listenEvents)=="function" then listenEvents(5) end
        if NUKED_STATUS then print("[WARP_WORLD] Nuked door."); _cleanup(); return false end
        sleep(DELAY_WARP); if type(SMART_RECONNECT)=="function" then SMART_RECONNECT() end

        fg=_current_tile_fg_safe(8,120)
        if fg>=0 and fg~=6 then
          CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true
        end

        print(string.format("[WARP_WORLD] Door attempt %d/%d fail.", dtry,(MAX_DOOR_RETRY or 5)))

        -- == LOGIKA COUNTER 4x GAGAL DI DOOR ==
        fail_streak_door = fail_streak_door + 1
        if fail_streak_door >= 4 then
          _force_reconnect()
          fail_streak_door = 0
        end
        -- ======================================
      end

      if _nudge_and_warp and _nudge_and_warp(WORLD,DOOR,3) then
        CURRENT_WORLD_TARGET=WORLD; CURRENT_DOOR_TARGET=DOOR; _cleanup(); return true
      end
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


-- ============================================================
----------------------------------------------------------------
-- Map kode malady -> nama (opsional, untuk log)
----------------------------------------------------------------
function _malady_status(status_take)
    malady = getBot().auto_malady
    malady.enabled = AUTO_MALADY
    malady.auto_surgery_station = false
    malady.auto_vial = status_take
    malady.auto_chicken_feet = false
    malady.auto_grumbleteeth = false
    malady.auto_refresh = true
    malady.storage = STORAGE_MALADY.."|"..DOOR_MALADY
    malady.vial = MALADY_NAME
end

local MALADY_CODES = {
  [1]  = "Torn Punching Muscle",
  [2]  = "Gem Cuts",
  [3]  = "Chicken Feet",
  [4]  = "Grumbleteeth",
  [5]  = "Broken Heart",
  [6]  = "Chaos Infection",
  [7]  = "Moldy Guts",
  [8]  = "Brainworms",
  [9]  = "Lupus",
  [10] = "Ecto-Bones",
  [11] = "Fatty Liver"
}

function untill_malady()
    local b = getBot and getBot() or nil
    local m = b.malady
    if m == 0 then
        if m == MALADY_CODES[m] then 
            return false
        end
        return true
    end
    return false
end


function _drop_item_more(world, door, TARGET_ID, pos_droped)
  local b = (type(getBot)=="function") and getBot() or nil
  if not b then return false, "no_bot" end

  local storageW  = (world and world ~= "") and world or nil
  local storageD  = (door  and door  ~= "") and door or nil

  -- helper: matikan collect dengan aman
  local function collect_off()
    if type(ZEE_COLLECT)=="function" then pcall(ZEE_COLLECT, false) end
  end

  -- PAKSA OFF di awal, dan PASTIKAN OFF di semua jalur keluar
  collect_off()
  local function finalize_off()
    collect_off()
  end

  -- count aman
  local function count()
    local inv = b.getInventory and b:getInventory() or nil
    return inv and inv:getItemCount(TARGET_ID) or 0
  end

  if count() <= 0 then finalize_off(); return false, "no_item" end

  -- pastikan posisi storage bila diberikan
  local function ensureAtStorage(max_try)
    if not storageW then return true end
    max_try = max_try or 5
    for i = 1, max_try do
      local w = b:getWorld()
      local name = (w and w.name) and w.name or ""
      if name:upper() == tostring(storageW):upper() then
        return true
      end
      if WARP_WORLD then WARP_WORLD(storageW, storageD) end
      sleep(300)
      if SMART_RECONNECT then SMART_RECONNECT(storageW, storageD) end
      sleep(400)
    end
    return false
  end

  if not ensureAtStorage(6) then
    finalize_off(); return false, "failed_warp_storage"
  end

  -- optional: hadap depan biar pathing stabil
  if type(faceSide2)=="function" then pcall(faceSide2) end

  -- cari tile drop target sekali saja
  local pos_x, pos_y
  if pos_droped and pos_droped ~= 0 then
    for _, t in pairs(getTiles()) do
      if t.fg == pos_droped or t.bg == pos_droped then
        pos_x, pos_y = t.x, t.y
        break
      end
    end
    if not pos_x then
      finalize_off(); return false, "tile_drop_not_found"
    end
  end

  local safety = 0
  while true do
    local n = count()
    if n <= 0 then break end

    -- jaga tetap di storage jika ditentukan
    if storageW then
      local w = b:getWorld()
      local name = (w and w.name) and w.name or ""
      if name:upper() ~= storageW:upper() then
        if not ensureAtStorage(2) then
          finalize_off(); return false, "lost_world_and_failed_return"
        end
      end
    end

    -- path ke tile drop (kalau ada), kalau tidak drop di posisi sekarang
    if pos_x and pos_y then
      pcall(function() b:findPath(pos_x, pos_y) end)
      if SMART_RECONNECT then SMART_RECONNECT(storageW, storageD, pos_x, pos_y) end
      sleep(100)
    end

    -- lakukan drop semua sisa item (atau batasi batch via math.min(n, 200))
    local ok = pcall(function() b:drop(TARGET_ID, n) end)
    sleep(200)

    local now = count()
    if (not ok) or (now >= n) then
      safety = safety + 1
      if safety >= 10 then
        finalize_off(); return false, "no_progress_drop_timeout"
      end
      if storageW and SMART_RECONNECT then SMART_RECONNECT(storageW, storageD) end
      sleep(300)
    else
      safety = 0
    end
  end

  finalize_off()
  return true, "dropped_all"
end




function droped_all_more()
  if STORAGE_JAMMER and DOOR_JAMMER and POS_DROP_JAMMER then
    _drop_item_more(STORAGE_JAMMER, DOOR_JAMMER, 226, POS_DROP_JAMMER)
  end
  if STORAGE_MALADY and DOOR_MALADY and POS_DROP_MALADY then
    _drop_item_more(STORAGE_MALADY, DOOR_MALADY, 8542, POS_DROP_MALADY)
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
      SMART_RECONNECT(WORLD, DOOR, tgt.x, tgt.y)
      b:findPath(tgt.x, tgt.y)
      sleep(STEP_MS)
      ZEE_COLLECT(true,1)
    -- else
    --   ZEE_COLLECT(true)
    --   SMART_RECONNECT(WORLD, DOOR)
    --   faceSide2()
    --   sleep(STEP_MS)
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

-- ====== STATE CACHE UNTUK HEMAT CPU ======
function clearConsole()
    local b = (getBot and getBot()) or nil
    if not b then
      return false, "no_bot"
    end
    for i = 1, 50 do
        b:getConsole():append("")
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
        clearConsole()
        sleep(100)
        if b.say then b:say("/status") end
        sleep(1000)
        if type(findStatus)=="function" and findStatus() and b.getConsole then
            local conso = b:getConsole()
            if conso and conso.contents then
                for _, con in pairs(conso.contents) do
                    if type(con)=="string" and con:lower():find("malady:") then
                        local name = con:match("[Mm]alady:%s*([^!]+)")
                        if name then name = name:gsub("%s+$","") end

                        -- cari hanya di bagian dalam tanda kurung
                        local time_part = con:match("%(([%d%sa-zA-Z,]+)%)") or ""
                        local h = tonumber(time_part:match("(%d+)%s*hour")) or 0
                        local m = tonumber(time_part:match("(%d+)%s*min")) or 0
                        local s = tonumber(time_part:match("(%d+)%s*sec")) or 0

                        local total = h * 3600 + m * 60 + s
                        print(("BOT %s , Malady: %s. Time Left: %d hours, %d mins, %d secs")
                            :format(b.name, name or "None", h, m, s))
                        return true, total, name
                    end
                end
            end
        end
    end
    print("BOT "..b.name.." , NotFound Malady")
    return false, nil, nil
end

function ensureMalady(faster)
  if not AUTO_MALADY then return false, "disabled" end
    local b = (getBot and getBot()) or nil
    local useW, useD  = STORAGE_MALADY, DOOR_MALADY
    -- found_m, secs_m, name_m = true, true, true
    SMART_RECONNECT()
    if faster then
      found_m, secs_m, name_m = checkMalady()
    else
      return false
    end
    
    while found_m and secs_m < 300 do
      SMART_RECONNECT()
      print("Bot "..b.name.." waiting ".. secs_m .."s until malady is gone")
      sleep(30000)
      found_m, secs_m, name_m = checkMalady()
    end

    while not found_m and not secs_m do
      found_m, secs_m, name_m = checkMalady()
      if not found_m and not secs_m then
        okTake = take_malady(useW, useD, { step_ms = 650, rewarp_every = 180 })
        if not okTake then sleep(8000) end
      end
    end
    if found then droped_all_more() return false end
end

------------------------------- AUTO JAMMER ------------------------------
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
      sleep(STEP_MS); SMART_RECONNECT(storageW,storageD);
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

function _take_item_x(WORLD, DOOR, TARGET_ID, opts)
  local b = getBot and getBot() or nil

  opts = opts or {}
  local STEP_MS       = tonumber(opts.step_ms or 800)
  local REWARP_EVERY  = tonumber(opts.rewarp_every or 180)
  local LOG_PREFIX    = "[TAKE-ITEM-ID-"..TARGET_ID.."]"
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
        sleep(250)
        print(string.format("%s Dapat item %d. Selesai.", LOG_PREFIX, TARGET_ID))
        ZEE_COLLECT(false)
        return true
      end
      -- kalau ke-drop semua saat normalize → lanjut tunggu
    end

    local tgt = _nearest_target_tile()
    if tgt then
      SMART_RECONNECT(WORLD, DOOR, tgt.x, tgt.y)
      b:findPath(tgt.x, tgt.y)
      ZEE_COLLECT(true, 1)
      sleep(STEP_MS)
    else
      ZEE_COLLECT(true, 1)
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


-- letakkan / aktifkan jammer (item 226) di tile (x-1, y-1)
function ensure_jammer_left_top(target_world)
  local b = (getBot and getBot()) or nil
  if not b then return false, "no_bot" end

  local function get_world_name()
    local wb = (b.getWorld and b:getWorld()) or nil
    return (wb and wb.name) and tostring(wb.name):upper() or ""
  end

  local function tile_ok(x, y)
    return x and y and x >= 0 and y >= 0 and x < 200 and y < 100
  end

  local function reconnect()
    if target_world and target_world ~= "" then
      SMART_RECONNECT(target_world)
      b = (getBot and getBot()) or b
    else
      SMART_RECONNECT(get_world_name())
      b = (getBot and getBot()) or b
    end
  end

  local function pos_now()
    local me = b:getWorld() and b:getWorld():getLocal() or nil
    if not me then return nil, nil end
    return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
  end


  local x, y = pos_now()
  if not x then return false, "no_position" end
  local tx, ty = x-1, y-1
  if not tile_ok(tx, ty) then return false, "tile_oob" end

  local wname = get_world_name()
  local want  = (target_world and target_world ~= "") and target_world:upper() or wname
  if wname == "" or wname ~= want then
    reconnect()
    wname = get_world_name()
    if wname ~= want then return false, "wrong_world" end
  end

  local inv = b.getInventory and b:getInventory() or nil
  local function count_jammer()
    inv = b.getInventory and b:getInventory() or nil
    return inv and inv.getItemCount and inv:getItemCount(226) or 0
  end

  -- Pastikan punya item 226
  if count_jammer() == 0 and getTile(tx, ty).fg == 0 then
    if _take_item_x then
      _take_item_x(STORAGE_JAMMER, DOOR_JAMMER, 226)
      reconnect()
    end
  end
  if count_jammer() == 0 then return false, "no_item_226" end

  -- Jika tile kosong, tempatkan
  if (getTile(tx, ty).fg or 0) == 0 then
    local place_tries = 0
    while (getTile(tx, ty).fg or 0) == 0 and count_jammer() > 0 and place_tries < 8 do
      b:place(tx, ty, 226)
      sleep(450)
      reconnect()
      place_tries = place_tries + 1
    end
    if (getTile(tx, ty).fg or 0) ~= 226 then
      return false, "place_failed"
    end
  end

  -- Opsional: aktifkan (toggle) dengan hit sekali-dua kali sampai flag berubah
  local old_flags = getTile(tx, ty).flags
  local hit_tries = 0
  while hit_tries < 6 do
    b:hit(tx, ty)
    sleep(700)
    reconnect()
    local now_flags = getTile(tx, ty).flags
    if now_flags ~= old_flags then
      return true, "toggled"
    end
    hit_tries = hit_tries + 1
  end

  -- Jika tidak berubah, anggap sudah aktif atau tidak perlu toggle
  return true, "placed_or_already_active"
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
  local cap_max = tonumber(per_world_cap or LIMIT_SEED_STORAGE) or 81000
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
  ensureMalady(true)

  SMART_RECONNECT(w); sleep(100)

  local function pos_now()
    local me = b:getWorld() and b:getWorld():getLocal() or nil
    if not me then return nil, nil end
    return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
  end

  if AUTO_JAMMER then
    ensure_jammer_left_top(w)
    droped_all_more()
  end
  SMART_RECONNECT(w); sleep(100)

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
          -- b:place(wx, wy, ID_BLOCK); sleep(DELAY_PUT); ensureMalady(); SMART_RECONNECT(w)
          b:place(wx, wy, ID_BLOCK); sleep(DELAY_PUT); SMART_RECONNECT(w)
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
          -- b:hit(wx, wy); sleep(DELAY_BREAK); ensureMalady(); SMART_RECONNECT(w)
          b:hit(wx, wy); sleep(DELAY_BREAK); SMART_RECONNECT(w)
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
    reload_world_lists_if_changed() -- cek perubahan file, auto-update tabel
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
load_world_lists_from_txt()
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
    if b then b.auto_reconnect = true end
    sleep(DELAY_AFK_AFTER_ALL_WORLD*60*1000)  -- 20 menit (ms)
    reload_world_lists_if_changed() -- cek perubahan file, auto-update tabel
    
  elseif MODE == "PNB" then
    -- jalankan mode PNB kamu di sini (opsional)
  else
    print("PLEASE INPUT MODE !!!!")
  end
end
