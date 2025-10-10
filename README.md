local tokens = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F1C83AA04A01005AE2EF0B375A|name:icydewkabn|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65nkwTjaPqSk0DNgoAND5w7R4VvNvl/IPChVqZFddc1WNdpCTMgvfvrdH01FQcBLCFIk2zwvWCDSol3WSWobA4PKRaoZq9u6ntZVCYdjAXQeMfIEiJnqmcnGVaahfi46p2xy+hybRJBdXnZ0zUa1JtHkUxh9hQpIOfGQpkNHfe53kH7OLOTjpPKhB4VzSJc2k5AN18LpTXOzq/axa2QwwRxcO+7I8LBfdWi6PVVUu2SvE639EBjdyNflgWmaBOTZyHF8JzGJJG2KsSkQ41I9LWzGJUbGXlf5CA57ulyNBgze3QMl8cHC2w8Ag78TiSQcw2O4y9fhifmeQ9N928NygMHzXFtWZ1H/nXbaoR1OKprV4cCE1hyTLSyqIVAYXp3/T/Is9SYce14/wNqvVFegKEDdaXHFda0VM6RXnqglEfXbN1iwRXMkZoynP0B6Uld4UZ/SN9e4WdVWwtJi0UHsWSPmwGgl8xw0gWgp6HilgleD|vid:24C059E7-7CC8-4833-874D-660A4AE312AC


]]

local useProxy   = false
local connectBot = true

local function trim(s) return (s:gsub("^%s+",""):gsub("%s+$","")) end

local function parseTokenLine(line)
  line = trim(line or "")
  if line == "" then return nil end

  local bot = {}
  for key_value in line:gmatch("[^|]+") do
    local key, value = key_value:match("([^:]+):(.+)")
    if key and value then
      bot[trim(key)] = trim(value)
    end
  end
  if not bot.token or bot.token == "" then return nil end
  return bot
end

local function configureAndAddBot(src)
  local bot = {}
  for k,v in pairs(src) do bot[k]=v end

  bot.connect = connectBot

  -- proxy hanya jika belum ada field proxy di data & flag aktif
  if useProxy and bot.proxy == nil then
    bot.proxy = "auto"
  end

  -- mode TOKEN vs normal
  if type(calculateBackpackCost) == "function" then
    bot.type = (rawget(_G, "TOKEN") ~= nil) and TOKEN or "TOKEN"
    bot.name = bot.name or bot.token
  else
    bot.name     = bot.name or bot.token
    bot.platform = tonumber(bot.platform) or bot.platform
  end

  -- HINDARI print token
  -- for k,v in pairs(bot) do if k ~= "token" then print(k..": "..tostring(v)) end end

  local handle = addBot(bot)
  if not handle then
    print("[WARN] Gagal menambahkan bot: "..(bot.name or "Unknown"))
    return
  end

  print("Bot has been added: "..(handle.name or bot.name or "Unknown"))

  -- console (cek nil)
  if type(handle.getConsole) == "function" then
    local c = handle:getConsole()
    if c then c.enabled = true end
  end

  -- opsi keamanan & tutorial (cek nil)
  handle.auto_ban = true

  local t = handle.auto_tutorial
  if t then
    t.enabled            = true
    t.auto_quest         = true
    t.set_as_home        = true
    t.set_high_level     = true
    t.set_random_skin    = false
    t.set_random_profile = false
  end
end

for line in tokens:gmatch("[^\r\n]+") do
  local parsed = parseTokenLine(line)
  if parsed then configureAndAddBot(parsed) end
end
