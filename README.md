LIST_WORLD_BLOCK = {"COKANJI|XX1"}



MODE = "SULAP"
-- SULAP
-- PNB

ID_BLOCK = 8640




DELAY_RECONNECT  = 20000
DELAY_BAD_SERVER = 120000
DELAY_BREAK      = 170
DELAY_PUT        = 115
DELAY_WARP       = 7000

-- ##################### BATAS SCRIPT #####################
worldTutor = ""
ID_SEED = ID_BLOCK + 1
CHECK_WORLD_TUTORIAL = false


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







function main_sulap(world, door)

end





while true do
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
            -- main_sulap(world_block, door_block)
            WARP_WORLD(world_block, door_block)
            WARP_WORLD(worldTutor)
        end
    elseif MODE == "PNB" then
    else
        print("PLEAS INPUT MODE !!!!")
        break
    end
end
