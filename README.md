local tokens = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4453A1047BFF041E198F61AA68E4|name:tamemapct|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjGxTkRYyjYm7R6HBnHaY2UXGCyDVY1TyiN2gsR2QXeujHXRBN3EM+E9QyBfFkFLzc6z9SjtTKY1q15kjQTiPi7wbUuEoRuxyxLLmjm/Bul+1LXy6/fSt7bfdzUy2Br8mGOUko1AZUYv11+AUHcqy2GDo+NEPdEShZcxCWmLaU682AQ7iXU8VY/HyW4mvh1FWmWiRD5/ciewocUxmjGpAR58VQzDmfMFhp9fXHTadyQKk3FJAcyb4CmEfhWQh0rnHii4Y4gW9iTdh2BEcgU3OX//on9V9Y9Yy82RsPMY792IUT5pUj0cx2aROeIUf8UQB3HnUxPThWbnXQoT0zKDUikAmLLW2W7elxTsnNPcOtbcCH4Gda4imWTUP3JrhVh/LIW8lCzwBuGm6zALOjbjtiwTNNugTm3CmW9b1fsjg0gp0SOqRVMg7bVAICo5obQ466vEeiuZ4PmD7hUUQ8OkMSiOjAuao0KtLI/lob4gaXgIT|vid:3E4C2B36-F546-4E55-A989-092D4888861A
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D444EDF6F0B4E05F049F50F7AA014|name:wetwwjicy|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjIBaEm9aWiBXQHCW68W5vzG2V4PJL3BXkPoUcyp8/hdRBhCI1AeNF37OcQ0pbOSQLW1tMdmjHFX2GaSwr/Ic8Vk83IADlSvPuexyqaeek452JVfn/BLhcIemP1v8Uo7rtk9KN+ATZ3cugjkb5HPO/diIeSgdUkFJ8/e57cd8rv4+ZnEqrHl5oRxi3C1lAQWqIL+/rpMFNPtLccDchCTQ8w2RhxeaQJkHE0PvKzN7goOYrfS0PME2ysssyP4Sx2tIdfR0Iblgppr7x7xh7nRR1HxSPcnnYR9F5shN3geZ54ewaYWsSNEOCY/xLl41BjvyDBIuXfc55J9qAQmpGDELfPdUrt0JJxUwD4/3OmeDHLcX9/NE0Si8ruWzAeSb3oEONRBmieo8MymiHuj1QwCURulV6k9Ot4iM52TDvO+akSxDqMlHClN49mdcXeJwOlcrcv7LCH+DgL7GygB7vATxzpAHAJK5UazpT1DJWkhY0XDQ|vid:20F44A9E-4E9A-4CD7-939A-B5DE234BD9EB
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4455A410626500876A39AC4AA6B8|name:ynoatmap|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjB/b1rOmBqQ++fB6Q/Zn/47IumbDPYZbqmDaEtK5AhVy7FGlUih5HjI5CP5du6/HrH9sMYEIxfAPceAkv2O3067fL726cqKs9JoolFztnEcUO1a1lDCsSZtBtmEyo/O3MLQeK4a2PhKOOcpVCVqC7hBhELsJ/pbKPGTvokDCgYwMeDkoi8k7Yc4zRVrlZudL7Xg1NRAVnQQxqCvi5wegYF6HCLTVJbh3eS+sHt2g6YkWuolrnY7vq72AfQAbOPFxzyhpHVlLQBhyROLDXXX+jdl/WF47RB+LA+l6rTVSjmYxGbUnjrEBjpk4P5xGIAQp2eVzrTecrG8YZCnQEypy5IGuJ/6eE0qGlsGwDBeHykkOy4DSpYiOGR4HZDa+4JgYq+YrXc1VcXx8Uu8Bef+4Jb7wuTAZPMjGpcCRdDHUi/ZZei8CH+njOvtjcrW6sW3mNQhQ06R1CCUhwoN3Y0QIBTvHJ1FUnLbx/g+EkRglopBG|vid:BDED1A4E-3160-40C1-82B5-5297B3BA751B
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D444BF9E724A901A94E2CBF00192D|name:hardlsaown|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjL2LPdEipnxA3PwfbYx8pJUwJvbJuWdfAFhu06D3BK/Suwwa5Kp7dc7lFKQfq2N9UXserDu8ejAruHQdYudL2mljnZtsJxEwGPOmycWZnAWUHU/tqp95Xl33wADv7C1NvfATMPjplNsLCwuIsfFKvt2LS3RXFe5T4YuF3piEi5+ABIMOQ+EM3I80v6oBumciUn9SRu4t7U/HJnnElFqOOu1JibrEyF2w6YNHP2GjUczq/CbiwGUI280mRL5460q3VyuouMYz0YJqD+WO0KjDTu8JgqyB7o8K8tYsMtCn69RSRZUZPvDWuqU5HgrKxXFRbSI80rrX2WSHFcvGnEHreqjSXqMiXzvI59jIDd7KnpbT17tyyVcq7QQcOXqSdiezg5AWVdhn+R98U2b8Jui9VcRSO4ufnGBBSFors0VJRVUXVeZKmZAgDrjJqOqUX3DZbVq+mhB77QuUoyNYrpNrkPay89cpxsNaoQn06WoKDeg/|vid:62F5A40A-9F33-4229-B165-E4843268E8B6
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4450DB19371908EA4CF8E8605ADF|name:aoxspinday|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjKgdxY3k8o9II0HAcWBovXDB3PFb6h2ZLeEEm9x+KlU+XJnjEbkZtX5hMXTwWts+z+fO+O5GbH4vNFfW06q8t7iq1nvDVX3dV2OBXFa7RDRsHLE9Mw/jYDLWvN3rARgYf4kXLPwRLsSrWT/Y05MLE4fmPEwO2cqOzoOLUYbXphQ6Y8vUxJDphYg6Ba9e4jRWN/pYtNkIjJicSTwRiLyrMDXkwsHpYLfR2THtIWIvlbE04SFoCc+XFtJcpdpTj5oadg+uS1cDLyeDJmmZS4YIjY4va9MpScqpJenjaaa2wG2uG8PNQwdd2dBz1rv2yvrqWOI3hZhGQD45Fa6fR4UPpLFIbO8ENdIj2JTj/J/c5eNDqU8XZ+1dHIQyTLXx8NI2uIkiFV8+9Hz1YllUtO2ExbdzABWUz1K1VBS5mm4A9v4ZubAqU3h8UCanG2pMZi2YaIubzpR9A7izP3gtlgddoom8xRLT3bGmzxImr2yhartT|vid:CC668BAE-8F8A-419B-A0CA-07F0A05A4B4F
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
