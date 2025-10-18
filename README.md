--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F36B7A39F9003C4A76C5C517D0|name:atmeledrun|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEo/E5DKB6Q7tUHsl+Vf7VoIpiynjPN6EQPhmMSvillWhivZFdgfm9i6mRWFnlEd0O2YpJLcMP3ZlAL5PePHBMflKRYBtfk+bKwSRiYFMMMH0xLnCwSTI522SCcBJWn6mAH+XSGKmFzg//xjnNpz2kdjAm9JjMHCjlvH1bRRYhK78p1+Y2Cr5QhucG5nyk1NhmuZDjmVphqdNOSa5zRg9kGMn4htKDqpQLU95jjLkgn3XTZbtYWupA0y408PuYMLkG68fukPP/3+fAWUBZ2ey6iA82xNe3gh13g4xGHrokz3oOk655wkzPlo2MqB5J5R21BHyLR88Jlu9SG6s6sG/Sj6h35g+zFwFc3pZYAd2ZDV0LTBY402xSJ5W0FEyXdgk2cMX5VNyUwpaRX/EdE5lkT2xopVrM/Ko1hw0zMeVe1x7+DDMiX6x9xaQp2cm8C7H9SshebPcyvO1QuLaSnq6JWw81Ttzv9dNrVito7dCxcl9|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F367AE41160600CD69834E3FCA|name:damcjyban|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEol3DHraziM2QVAQlDvieXdlaZqYlBJMVfJ4duKt3CoseT9su2UE16lPdhuJlS7grz4auxr7u5WvB9C2jGgXJI7Cn9Uzkm0LLnbFMu4cHoVSIDn94EbD50l4+gI2Ldvq8NfXIU43y/6rzYpE443ED9vLw0H+keKZ13wAOZZPx36KfTFeVJNH/mxTlZ3Sk0hp/98zX5taSgp1QaubCdUXFlg8sAk+LIMXSeAoO9WHMnT5MZN0dZ67re4hMiFPcO927+d9dk7HYb5MCPaRwPhvxVj2bBInxqx0ZBgIOyI7HexECDFoD6AWAfd3hTus5Ud1c5ydiVwWoZkhBoCII8YEJMrGiSDw0EFWkMYxaMoDUeO8Q5Yx/3smlXO3/PNsKsTX/z1mU+Dm7E/MRsecvg3LdXbnCFvW4S8iCVL1uBiSWSWfJmTj8avosSBWOR3/Nxh3bN47fHmF8pRhwdSY5I2iewAZooiEYzMk/RMUGM2MqGts|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F499EF44C303CD58FD4B748033|name:fastuzdo|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvErWjocuarS+VuXgxMFyUTomwz9QeaVhqGiYAqHijNwNyRhKCaghZ8s6Fsfr2Gijx6C6kmYm7diD8rLGtveRqQ2i/V7ksA/WsNr0LI+EF1b5LBFFB0LfVAt+AK/5PXE2d5u0uBJiPbGUAQ1W87ntbH4h40b8oQrWQtiDWr1shKV0Qss3T7yepTtaoLZ2gcLmFHeG7GXDjRXZxzTwn/1shwM+VIhPpxvx6NJc2pJqXYOphKa7+y/eLdinbxTCKdyOZcO46orGmJIycMmQmQqFRpR0Fq8QOZh/CfluPoO98KH4rtfz57eVIb+8YfBNtsPHaBv/ondTodBuW6oCV2G0HYWJ/9oTKTPKZLq/ID45YAy86QeaIehGe/DmGTJjkV9WJqrierrW8F492RDfAXNqyxeYvNU4u3k/34ouLdE0kMnTrp6LTZfkqVPxWacusqpsR+Wi9dCrdPCad+K8/Zf2yVPa/6hcDNvMBWQ/Xkv5quhLu|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1ED3DBC1D71037307E5922E628C|name:merezmaid|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEmm8lyTt42mgvLNfS4aIyUgSjSryAjQwCGam135/dtGqGp4bX+UvkqzbeU7FTzHBMNXalzz2cYfhLNdN8fFa35/7Q70DpRiTnLau/ENCuM0G/IZa3aQQ/qPEj56N1tlT8F7uhgVFyzRnLiUnOxljdLoC7Tx+3MV2C6b1C/yERq21dc0x9+pIOpclA559gsIPGW0bMd0RAnasAhtKLAbh0qlH9YHLJtnQKxsW3pmC87zFd9IfbAP6ZKB5rq6bC+49ZZZQH/g4mQJ0voTP3hz89f5EItReL8za6kDQrec8VnjVI4YdmVAMHhShJwrrv0PUUs/oG+hr7m6ufgsRYsWb0znMz90zDicZqgX+ntGITLtXLXaufOlBO/VS7g/VAwamLEi2GPse+597Be2N3fh/7M+gj9TKtHYfaeGBGE6ygTewPXf01eWVidm6l3F3kyLTjecALhFwU8JmKR+oyg9efNfO6ZDQhL56vWmGqoLLMHsT|vid:




]]

-- util
local function trim(s) return (s and s:gsub("^%s+",""):gsub("%s+$","")) or "" end

-- parser format 1: key:value|key:value...
local function parse_kv_line(line)
  local t = {}
  for seg in line:gmatch("[^|]+") do
    local k,v = seg:match("([^:]+):(.+)")
    if k and v then t[trim(k:lower())] = trim(v) end
  end
  if next(t) then
    return {
      email   = t.email,                 -- opsional di format ini (kalau ada)
      mac     = t.mac,
      rid     = t.rid,
      wk      = t.wk,
      ltoken  = t.token or t.name or t.ltoken, -- pakai 'token' sebagai ltoken
      platform= tonumber(t.platform),
    }
  end
end

-- parser format 2: email|mac:rid:wk:ltoken[:platform]
local function parse_compact_line(line)
  local email, rest = line:match("^([^|]+)|(.+)$")
  if not email or not rest then return nil end
  local parts = {}
  for p in rest:gmatch("[^:]+") do parts[#parts+1] = p end
  -- parts: mac (boleh berisi ':'), rid, wk, ltoken, [platform]
  if #parts < 4 then return nil end
  local mac  = parts[1]
  local rid  = parts[2]
  local wk   = parts[3]
  local ltok = table.concat(parts, ":", 4, #parts-((#parts>=5 and tonumber(parts[#parts])~=nil) and 1 or 0))
  local plat = tonumber((#parts>=5 and parts[#parts]) or nil)
  return {
    email   = trim(email),
    mac     = trim(mac),
    rid     = trim(rid),
    wk      = trim(wk),
    ltoken  = trim(ltok),
    platform= plat
  }
end

local function parse_account(line)
  line = trim(line)
  if line == "" or line:sub(1,2) == "--" then return nil end
  if line:find(":%S") and line:find("|") then
    -- ada pola k:v| → coba parser kv
    local t = parse_kv_line(line)
    if t and (t.mac or t.rid or t.ltoken) then return t end
  end
  -- fallback coba compact
  return parse_compact_line(line)
end

for account in accounts:gmatch("[^\r\n]+") do
  local p = parse_account(account)
  if p and p.ltoken and p.rid and p.mac then
    local details = {
      -- SESUAI PERMINTAAN:
      ["display"]  = p.email or "",      -- wajib: email → kalau tak ada di data, jadi ""
      ["secret"]   = p.email or "",      -- sama dengan display
      ["name"]     = p.ltoken,           -- isinya token
      ["rid"]      = p.rid,
      ["mac"]      = p.mac,
      ["wk"]       = p.wk or "NONE0",
      ["platform"] = tonumber(p.platform) or 0, -- platform dari data; fallback 0
    }

    local bot = addBot(details)
    if bot then
      -- aktifkan console aman
      if type(bot.getConsole) == "function" then
        local c = bot:getConsole()
        if c then c.enabled = true end
      end

      -- bypass opsional
      if rawget(_G, "bot_bypass") and bot_bypass == true then
        bot.bypass_logon = true
      end

      -- tutorial aman
      local tutorial = bot.auto_tutorial
      if tutorial then
        tutorial.enabled            = true
        tutorial.auto_quest         = true
        tutorial.set_as_home        = true
        tutorial.set_high_level     = true
        tutorial.set_random_skin    = true
        tutorial.set_random_profile = true
      end

      bot.dynamic_delay = true
      -- print("Bot added: "..(bot.name or details.name or "Unknown"))  -- hindari print token/email bila sensitif
    else
      print("[WARN] addBot gagal untuk rid="..tostring(p.rid))
    end
  end
end
