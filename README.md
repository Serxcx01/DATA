-- SC LOGI LIN STORE (versi aman)

-- Contoh format per baris (tanpa spasi):
-- token:ABCD123|platform:2|name:MyBot|proxy:auto
-- Minimal: token:<isi>
local tokens = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4450DB19371908EA4CF8E8605ADF|name:aoxspinday|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjKgdxY3k8o9II0HAcWBovXDB3PFb6h2ZLeEEm9x+KlU+XJnjEbkZtX5hMXTwWts+z+fO+O5GbH4vNFfW06q8t7iq1nvDVX3dV2OBXFa7RDRsHLE9Mw/jYDLWvN3rARgYf4kXLPwRLsSrWT/Y05MLE4fmPEwO2cqOzoOLUYbXphQ6Y8vUxJDphYg6Ba9e4jRWN/pYtNkIjJicSTwRiLyrMDXkwsHpYLfR2THtIWIvlbE04SFoCc+XFtJcpdpTj5oadg+uS1cDLyeDJmmZS4YIjY4va9MpScqpJenjaaa2wG2uG8PNQwdd2dBz1rv2yvrqWOI3hZhGQD45Fa6fR4UPpLFIbO8ENdIj2JTj/J/c5eNDqU8XZ+1dHIQyTLXx8NI2uIkiFV8+9Hz1YllUtO2ExbdzABWUz1K1VBS5mm4A9v4ZubAqU3h8UCanG2pMZi2YaIubzpR9A7izP3gtlgddoom8xRLT3bGmzxImr2yhartT|vid:CC668BAE-8F8A-419B-A0CA-07F0A05A4B4F

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
    t.set_random_profile= false
  end
end

-- Proses setiap baris token
for line in tokens:gmatch("[^\r\n]+") do
  local parsed = parseTokenLine(line)
  if parsed then
    configureAndAddBot(parsed)
  end
end
