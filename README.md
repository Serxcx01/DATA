b = getBot()
local me = b.getWorld and b:getWorld() and b:getWorld():getLocal() or nil
local ex = math.floor((me.posx or 0) / 32)
local ye = math.floor((me.posy or 0) / 32)
b:hit(ex, ye-1)
