storageWorld = "FENCEPAPA1"

local bot = getBot()
worldTutor = ""   -- tetap global krn dipakai lintas fungsi

local function round(n)
  return (n % 1) >= 0.5 and math.ceil(n) or math.floor(n)
end

local function faceSide2()
  local packet = GameUpdatePacket.new()
  packet.type  = 0
  packet.flags = 32
  bot:sendRaw(packet)
end

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

local function warp(world)
  local target = (world or ""):upper()
  if target == "" then return end  -- guard: jangan spam warp ke empty

  local attempts, max_attempts = 0, 7
  local nuked = false

  while get_current_world_upper() ~= target and not nuked do
    bot:warp(target)
    sleep(3500)
    attempts = attempts + 1
    if attempts >= max_attempts then
      nuked = true
    end
  end
end

local function wait_inventory_increase(id, before_cnt, timeout_ms)
  local t0 = os.clock()
  local max_s = math.max(0.05, (timeout_ms or 5000) / 1000)
  while (os.clock() - t0) < max_s do
    local now = bot:getInventory():getItemCount(id)
    if now > before_cnt then return true end
    sleep(150)
  end
  return false
end

local function take(id)
  local have = bot:getInventory():getItemCount(id)
  if have == 1 then
    return
  end

  warp(storageWorld)
  sleep(150)

  -- siapkan parameter collect sebelum bergerak
  bot.collect_range = 5
  bot.ignore_gems   = true
  bot.auto_collect  = true

  local inv_before = bot:getInventory():getItemCount(id)

  for _, obj in pairs(getObjects() or {}) do
    if obj.id == id then
      local tx = round(obj.x / 32)
      local ty = math.floor(obj.y / 32)
      bot:findPath(tx, ty)
      -- beri waktu pathing + pickup
      if wait_inventory_increase(id, inv_before, 5000) then
        break
      end
    end
  end

  -- reset behavior collect
  bot.auto_collect = false
  bot.ignore_gems  = false

  have = bot:getInventory():getItemCount(id)
  if have > 1 then
    faceSide2()
    sleep(100)
    bot:drop(id, have - 1)  -- sisakan 1
    sleep(400)
    bot:leaveWorld()
  end
end

local function here()
  local w = bot and bot.getWorld and bot:getWorld() or nil
  local p = w and w.getLocal and w:getLocal() or nil
  if not p then return 0, 0 end
  return math.floor(p.posx/32), math.floor(p.posy/32)
end

-- ====== eksekusi ======
take(226)
checkTutor()

if worldTutor ~= "" and not noHomeWorld then
  warp(worldTutor)
  local x0, y0 = here()
  -- SIGNAL JAMMER
  bot:place(x0 - 1, y0 - 1, 226)
  sleep(500)
  bot:hit(x0 - 1, y0 - 1)
  sleep(500)
else
  printWarn("Skip placing jammer: no tutorial/home world found.")
end
