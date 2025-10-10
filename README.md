-- SC LOGI LIN STORE (versi aman)

-- Contoh format per baris (tanpa spasi):
-- token:ABCD123|platform:2|name:MyBot|proxy:auto
-- Minimal: token:<isi>
local tokens = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F1C83AA04A01005AE2EF0B375A|name:icydewkabn|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65nkwTjaPqSk0DNgoAND5w7R4VvNvl/IPChVqZFddc1WNdpCTMgvfvrdH01FQcBLCFIk2zwvWCDSol3WSWobA4PKRaoZq9u6ntZVCYdjAXQeMfIEiJnqmcnGVaahfi46p2xy+hybRJBdXnZ0zUa1JtHkUxh9hQpIOfGQpkNHfe53kH7OLOTjpPKhB4VzSJc2k5AN18LpTXOzq/axa2QwwRxcO+7I8LBfdWi6PVVUu2SvE639EBjdyNflgWmaBOTZyHF8JzGJJG2KsSkQ41I9LWzGJUbGXlf5CA57ulyNBgze3QMl8cHC2w8Ag78TiSQcw2O4y9fhifmeQ9N928NygMHzXFtWZ1H/nXbaoR1OKprV4cCE1hyTLSyqIVAYXp3/T/Is9SYce14/wNqvVFegKEDdaXHFda0VM6RXnqglEfXbN1iwRXMkZoynP0B6Uld4UZ/SN9e4WdVWwtJi0UHsWSPmwGgl8xw0gWgp6HilgleD|vid:24C059E7-7CC8-4833-874D-660A4AE312AC

]]

local useProxy   = false
local connectBot = true

-- util trim
local function trim(s)
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function parseTokenLine(line)
  line = trim(line or "")
  if line == "" then return nil end

  local bot = {}
  for key_value in line:gmatch("[^|]+") do
    local key, value = key_value:match("([^:]+):(.+)")
    if key and value then
      key = trim(key)
      value = trim(value)
      bot[key] = value
    end
  end
  -- minimal harus punya token
  if not bot.token or trim(bot.token) == "" then
    return nil
  end
  return bot
end

local function configureAndAddBot(src)
  -- salin supaya nggak ngubah sumber
  local bot = {}
  for k, v in pairs(src) do bot[k] = v end

  bot.connect = connectBot

  -- Opsi proxy otomatis
  if useProxy and not bot.proxy then
    bot.proxy = "auto"
  end

  -- Penentuan mode: jika environment punya calculateBackpackCost → asumsi mode TOKEN
  if type(calculateBackpackCost) == "function" then
    if rawget(_G, "TOKEN") ~= nil then
      bot.type = TOKEN
    else
      bot.type = "TOKEN"  -- fallback aman
    end
    -- name opsional; jika tak ada, pakai token sebagai identitas tampilan
    bot.name = bot.name or bot.token
  else
    -- mode biasa: wajib ada name + platform (opsional)
    bot.name = bot.name or bot.token
    bot.platform = tonumber(bot.platform) or bot.platform
  end

  -- (Opsional) debug print — hati-hati menampilkan token ke log
  -- for k, v in pairs(bot) do print(k .. ": " .. tostring(v)) end

  -- Tambahkan bot dan ambil handle
  local handle = addBot(bot)
  if not handle then
    print("[WARN] Gagal menambahkan bot: " .. (bot.name or "Unknown"))
    return
  end

  print("Bot has been added: " .. (handle.name or bot.name or "Unknown"))

  -- Enable console jika ada
  if type(handle.getConsole) == "function" then
    local c = handle:getConsole()
    if c then
      c.enabled = true
    end
  end

  -- Pengaturan keamanan & tutorial (cek nil)
  handle.auto_ban = true

  local t = handle.auto_tutorial
  if t then
    t.enabled           = true
    t.auto_quest        = true
    t.set_as_home       = true
    t.set_high_level    = true
    t.set_random_skin   = false
    t.set_random_profile= true
  end
end

-- Proses setiap baris token
for line in tokens:gmatch("[^\r\n]+") do
  local parsed = parseTokenLine(line)
  if parsed then
    configureAndAddBot(parsed)
  end
end
