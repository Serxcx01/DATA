storageWorld = "FENCEPAPA1"

local bot = getBot()

local function round(n)
  return (n % 1) >= 0.5 and math.ceil(n) or math.floor(n)
end

local function faceSide2()
  local packet = GameUpdatePacket.new()
  packet.type  = 0
  packet.flags = 32
  bot:sendRaw(packet)
end

local function get_current_world_upper()
  -- Gunakan bacaan world yang aman
  local w = ""
  if bot and bot.getWorld and bot:getWorld() and bot:getWorld().name then
    w = bot:getWorld().name
  elseif bot and bot.world then
    -- fallback bila SDK expose .world langsung
    w = bot.world
  elseif getBot and getBot().world then
    w = getBot().world
  end
  return (w or ""):upper()
end

local function warp(world)
  local target = (world or ""):upper()
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

  local have = bot:getInventory():getItemCount(id)
  if have > 1 then
    faceSide2()
    sleep(100)
    bot:drop(id, have - 1)  -- sisakan 1
    sleep(400)
    bot:leaveWorld()
  end
end

take(226)
