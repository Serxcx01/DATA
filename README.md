local bot = getBot()

local function here()
  local p = bot:getWorld():getLocal()
  return math.floor(p.posx/32), math.floor(p.posy/32)
end

local x0, y0 = here()
bot:place(x0-1, y0-1, 226)
sleep(110)
bot:hit(x0-1, y0-1)
sleep(160)
