LIST_WORLD_BLOCK = {"FOZEEZ2|NOWXX123"}

MODE = "SULAP"
-- SULAP
-- PNB

STORAGE_SEED, DOOR_SEED     = "FENCEPAPA1", "NOWXX123"
STORAGE_MALADY, DOOR_MALADY = "COKANJI", "XX1"
ID_BLOCK                    = 8640
LIMIT_SEED_IN_BP            = 70
JUMLAH_TILE_BREAK           = 3
DELAY_RECONNECT             = 20000
DELAY_BAD_SERVER            = 120000
DELAY_BREAK                 = 170
DELAY_PUT                   = 115
DELAY_WARP                  = 7000

-- ##################### BATAS SCRIPT #####################
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

-- ##################### UTIL / RECONNECT #####################
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
  end

  if WORLD and DOOR then WARP_WORLD((WORLD or ""):upper(), DOOR)
  elseif WORLD then       WARP_WORLD((WORLD or ""):upper()) end

  if POSX and POSY then local b=getBot and getBot() or nil; if b and b.findPath then b:findPath(POSX,POSY) end end
end

function ZEE_COLLECT(state)
  local b=getBot and getBot() or nil; if not b then return end
  if state then b.auto_collect=true; b.ignore_gems=true; b.collect_range=5; b.object_collect_delay=200
  else b.auto_collect=false end
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

-- helper kecil: ambil tile dengan guard batas & pcall
local function _safeTile(w, x, y)
  if x < 0 or x > WORLD_MAX_X or y < 0 or y > WORLD_MAX_Y then return nil end
  local ok, t = pcall(function() return w:getTile(x, y) end)
  if not ok then return nil end
  return t
end

function tilePunch(x, y)
  local b = getBot and getBot() or nil
  local w = b and b.getWorld and b:getWorld() or nil
  if not w then return false end

  for _, num in ipairs(TILE_BREAK) do       -- urutan TERJAGA
    local tx, ty = x + 1, y + num
    local t = _safeTile(w, tx, ty)
    -- punch hanya kalau ADA foreground (bg tidak relevan buat seed)
    if t and (t.fg or 0) ~= 0 then
      return true
    end
  end
  return false
end

function tilePlace(x, y)
  local b = getBot and getBot() or nil
  local w = b and b.getWorld and b:getWorld() or nil
  if not w then return false end

  for _, num in ipairs(TILE_BREAK) do       -- urutan TERJAGA
    local tx, ty = x + 1, y + num
    local t = _safeTile(w, tx, ty)
    -- place cukup cek foreground kosong; background boleh ada
    if t and (t.fg or 0) == 0 then
      return true
    end
  end
  return false
end


-- ##################### GET DATA WORLD TUTORIAL #####################
function findHomeWorld(variant, netid)
    if variant:get(0):getString() == "OnRequestWorldSelectMenu"
        and variant:get(1):getString():find("Your Worlds") then
        local text = variant:get(1):getString()
        local lines = {}
        for line in text:gmatch("[^\r\n]+") do
        table.insert(lines, line)
        end
        for i, value in ipairs(lines) do
        if i == 3 then
            local kalimat = lines[3]
            -- ambil nama world diantara '|' lalu hilangkan spasi
            local nilai = kalimat:match("|([a-zA-Z0-9%s]+)|")
            if nilai then
            nilai = nilai:gsub("%s", "")
            worldTutor = nilai
            print("Tutorial World: " .. worldTutor)
            end
        end
        end
    end
end

function checkTutor()
    local bot=getBot and getBot()
    -- keluar ke EXIT terlebih dahulu
    while bot:isInWorld() do
        bot:leaveWorld()
        sleep(3000)
    end

    worldTutor = ""
    noHomeWorld = false
    print("Checking Tutorial/Home World")

    addEvent(Event.variantlist, findHomeWorld)

    for _ = 1, 3 do
        -- guard: bot:getWorld() bisa nil
        local w = (bot and bot.getWorld and bot:getWorld() and bot:getWorld().name) or ""
        if worldTutor == "" and w:upper() == "EXIT" then
        bot:sendPacket(3, "action|world_button\nname|_16")
        listenEvents(5)
        end
    end

    if worldTutor == "" then
        printCrit("Doesn't Have Tutorial/Home World!")
        callNotif("Doesn't Have Tutorial/Home World!", true)
        noHomeWorld = true
    end

    sleep(100)
    removeEvent(Event.variantlist)
    end

    local function get_current_world_upper()
    local w = ""
    if bot and bot.getWorld and bot:getWorld() and bot:getWorld().name then
        w = bot:getWorld().name
    elseif bot and bot.world then
        w = bot.world
    elseif getBot and getBot().world then
        w = getBot().world
    end
    return (w or ""):upper()
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

function clearConsole()
    local bot = (getBot and getBot()) or nil
    for i = 1, 50 do
        bot:getConsole():append("")
    end
end

function checkMalady()
    local b = (getBot and getBot()) or nil
    if b and b.isInWorld and b:isInWorld() and (b.status == BotStatus.online or b.status == 1) then
        if type(clearConsole)=="function" then clearConsole() end
        sleep(100)
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


-- Tunggu kalau malady < 60s, lalu ambil malady saat sudah hilang
function waitMaladyThenTake()
    local has, secs = checkMalady()

    -- Kalau tidak ada malady: langsung ambil
    if not has then
        return take_malady(STORAGE_MALADY, DOOR_MALADY, { step_ms = 700, rewarp_every = 120 })
    end

    -- Kalau >= 60s, jangan nunggu (biar tidak block lama); keluar saja
    if (secs or 0) >= 60 then
        print(("[MALADY] %ds left (>=60s): skip waiting now."):format(secs or -1))
        return false
    end

    -- Di sini: 0 < secs < 60 → tunggu sampai habis
    print(("[MALADY] %ds left (<60s): waiting until it clears..."):format(secs or -1))

    local deadline = os.time() + 120  -- failsafe 2 menit biar nggak ke-lock
    local last = secs or 60

    while true do
        local ok, s = checkMalady()

        -- kalau sudah tidak ada / sisa <= 0 → selesai nunggu
        if (not ok) or (s or 0) <= 0 then break end

        -- proteksi kalau timer “naik” tiba-tiba (server lag/parse)
        if s > last + 2 then
            print("[MALADY] timer jumped up; abort waiting, retry later.")
            return false
        end
        last = s

        -- tidur pendek menyesuaikan sisa waktu (hindari spam /status)
        local step_ms = math.max(250, math.min(1000, math.floor(s * 500)))
        sleep(step_ms)
    end

    -- double-check agar yakin sudah clear, baru take
    local ok2 = select(1, checkMalady())
    if not ok2 then
        print("[MALADY] cleared. Taking malady now...")
        return take_malady(STORAGE_MALADY, DOOR_MALADY, { step_ms = 700, rewarp_every = 120 })
    else
        print("[MALADY] still reported after countdown; will retry later.")
        return false
    end
end





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


-- ##################### TAKE BLOCK #####################
-- === FIX kecil di TAKE_BLOCK(): hindari variabel w/d yang tidak ada ===
function TAKE_BLOCK(world, door)
    local b = getBot and getBot() or nil
    local TARGET_ID = ID_BLOCK
    local inv = b:getInventory()
    local have = inv:getItemCount(TARGET_ID)

    if have < 20 then
        WARP_WORLD(world, door); sleep(250)
        SMART_RECONNECT(world, door)  -- FIX: pakai argumen yang benar

        local MAX_ROUNDS, WAIT_MS = 10, 1200
        ZEE_COLLECT(true)
        pcall(function()
            for _ = 1, MAX_ROUNDS do
                if inv:getItemCount(TARGET_ID) > 0 then break end
                local objs = (getObjects and getObjects()) or {}
                local me = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
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
                    local tx, ty = math.floor(best.x/32), math.floor(best.y/32)
                    SMART_RECONNECT(world, door, tx, ty)
                    b:findPath(tx, ty)
                    sleep(WAIT_MS)
                else
                    SMART_RECONNECT(world, door)
                    sleep(WAIT_MS)
                end
                inv = b:getInventory() -- refresh
            end
        end)
        ZEE_COLLECT(false)
    end
end


-- ##################### PNB SULAP #####################
function pnb_sulap()
    local b = getBot and getBot() or nil
    if not b then return end

    if (worldTutor or "") == "" then
        checkTutor()
    end
    local w = worldTutor
    if (w or "") == "" then
        print("[PNB] Tidak punya Tutorial/Home World. Abort.")
        return
    end

    -- warp + jaga koneksi
    WARP_WORLD(w); sleep(100)
    waitMaladyThenTake(); sleep(100)
    SMART_RECONNECT(w); sleep(100)

    -- gunakan tile posisi saat ini sebagai acuan
    local me = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
    if not me then return end
    local ex = getBot().x
    local ye = getBot().y

    local counter = 0
    local WAIT_MS = 1200

    -- REFRESH inventory setiap iterasi
    local inv = b:getInventory()
    ZEE_COLLECT(true)

    -- Logika: sulap block -> seed sampai jumlah seed mencapai batas
    -- Loop berlanjut selama masih ada block dan seed di bawah batas
    while inv:getItemCount(ID_BLOCK) > 0 and inv:getItemCount(ID_SEED) < LIMIT_SEED_IN_BP do

        -- PLACE: isi celah kosong di depan + offset vertikal
        while tilePlace(ex, ye) do
            for _, i in pairs(TILE_BREAK) do
                local t = b:getWorld():getTile(ex + 1, ye + i)
                if t.fg == 0 and t.bg == 0 then
                    b:place(ex + 1, ye + i, ID_BLOCK)
                    sleep(DELAY_PUT)
                    SMART_RECONNECT(w); sleep(100)
                    counter = counter + 1
                    if counter == 150 then
                        counter = 0
                        if b.disconnect then b:disconnect() elseif type(disconnect)=="function" then disconnect() end
                        sleep(WAIT_MS)
                        SMART_RECONNECT(w); sleep(100)
                    end
                else
                    -- sudah terisi, keluar dari for ini untuk re-check tilePlace
                    break
                end
            end
            inv = b:getInventory() -- refresh setelah aksi
            if inv:getItemCount(ID_BLOCK) <= 0 then break end
        end

        -- PUNCH: hancurkan tile yang ada untuk jadi seed
        while tilePunch(ex, ye) do
            for _, i in pairs(TILE_BREAK) do
                local t = b:getWorld():getTile(ex + 1, ye + i)
                if t.fg ~= 0 or t.bg ~= 0 then
                    b:hit(ex + 1, ye + i)
                    sleep(DELAY_BREAK)
                    SMART_RECONNECT(w); sleep(100)
                    counter = counter + 1
                    if counter == 150 then
                        counter = 0
                        if b.disconnect then b:disconnect() elseif type(disconnect)=="function" then disconnect() end
                        sleep(WAIT_MS)
                        SMART_RECONNECT(w); sleep(100)
                    end
                end
            end
            inv = b:getInventory() -- refresh setelah aksi
            if inv:getItemCount(ID_SEED) >= LIMIT_SEED_IN_BP then
                -- seed sudah mencapai batas, sudahi
                break
            end
        end

        -- refresh terakhir untuk syarat while
        inv = b:getInventory()
    end
    ZEE_COLLECT(false)
    if inv:getItemCount(ID_SEED) >= LIMIT_SEED_IN_BP then
      DROP_ITEMS_SNAKE(STORAGE_SEED, DOOR_SEED, {ID_SEED}, {tile_cap=3000, stack_cap=20})
    end
end


function main_sulap(world_block, door_block)
    while true do
        TAKE_BLOCK(world_block, door_block)
        pnb_sulap()
    end
end



if true then
    if MODE == "SULAP" then
        if not CHECK_WORLD_TUTORIAL then
            checkTutor()
            CHECK_WORLD_TUTORIAL = true
        end
        for i =1,#LIST_WORLD_BLOCK do
            
            if getBot().level < 12 then
                LEVEL_RENDAH = true
            end

            local split_data = {}
            for w in LIST_WORLD_BLOCK[i]:gmatch("([^|]+)") do 
                table.insert(split_data, w) 
            end
            world_block = split_data[1]
            door_block = split_data[2]
            main_sulap(world_block, door_block)
        end
    elseif MODE == "PNB" then
    else
        print("PLEAS INPUT MODE !!!!")
    end
end
