local bot = getBot()

local function here()
  local p = bot:getWorld():getLocal()
  return math.floor(p.posx/32), math.floor(p.posy/32)
end

local x0, y0 = here()
-- SIGNAL JAMMER
bot:place(x0-1, y0-1, 226)
sleep(110)
bot:hit(x0-1, y0-1)
sleep(160)
-- ZOMBIE JAMMER
bot:place(x0-1, y0-2, 1278)
sleep(110)
bot:hit(x0-1, y0-2)
sleep(160)
-- WEATHER
bot:place(x0, y0-2, 946)
sleep(110)
bot:hit(x0, y0-2)
sleep(160)
