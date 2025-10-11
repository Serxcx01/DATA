--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1EDC48504FF0823A4E98EB1A89B|name:aboeasyhug|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEiBDk8Q4Fv5tNOd4u/1eRMsNO4/n/yz4FevD5ry/FkmbCqTbkOo8nCD3dWJPfbO1tVGoLDb3NyN2m8gOXIQVhXwmLSdL45DNIfNbxRP4H9ZwqFG3R5JhR9IfLReEyYiiNTNryj0IBhuojYb6TJf44SBmWET2rLOQIWGH/MoqhfoGYb47vmVVulmIjHVX/Fnvbov8sN0pC0gkPI7UaX5d3IlnA8sN7JCigCo0VOU5xFplvSTCNExq+Vs5+VoLpSl7VwKDqvnEhRbjLQ5R8vncco+BvP3jRbXVe/rMoIe+FeaGnGDhvwQwBMzLQ2ArzYqfu+rcmYyinhBHCyrsx9ErBykEH5L2j7pBCkzHp25bKgbVsimAqESn57jUF5aMQKb5j+NLAcNqAmnPCcpEjZG1YX+xxSdUxo4akoYjRWuDioFGvM9q6pJWQX6Uj8NiU3cpnbBMwsbEO+tUg4RKGrMv0gnqEZtNAMJ5nyeOSMN+qTGB|vid:4DF1E157-A0E5-410D-944B-6BE887A6FE0B
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1EDF6B794BE039FF9EBFDF1F3FF|name:mendifgem|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEujMQr0TTxOwzpVDo/B6mcGltpAEkFpH4/8upsNyG4zPkXhMYfQZUpbDBGXrwHM09emuq03j+zfXAYRcQKRRGIZ1SjvvbUob6Yumr1lE6mrRilyTAU+NYJUgMI9YJ8BdxMUqBuiTRwwoSar38K8VFQtlNpqM7TmNi6W4s1VOGiwkRuAbvFQIQI+anyshpCl/p1Z0LBf3paNP0gzVkbddykIi++irm5lzbO4PmwHl3GYnqBXbjPrvLUA6HzYgWkZ0ynKPQKOOj+rYK1m5bjYY3Cv/MMToAscGwS3yhJxjYcyzXT0Y6Q9L64D8YVqxwIlqfKBUi9DhXyserulBqg4WbbF1JYN4TcPENL4MqVBWSYs27JE8k9ftA0LVYhEdS+4853r/4sQn5Vi7OPKpnqHb5RrUj2juxcNM/abSlO11MfkkzkcNAw9pWyzTs1JsVo/b1/a5f39EyAKn3sGWDOdbkIhusFEkj5G7NHwr5ROVs4M+|vid:EA910A70-9F25-40F3-B10A-834E15608CB4
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F36B7A39F9003C4A76C5C517D0|name:atmeledrun|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEo/E5DKB6Q7tUHsl+Vf7VoKRwNQeVj33Vgcae4Dov2z4prB510fLRhL/bAPKbEyZYpYpgcC0jzdoK1yzWu9POhKr5Z2GDKLPoArbNSZlcXJWzmyXrrL1KSrNqciVydccVMJZbZbpf80HQdUgjk4IWT10is0bCroeQFm/XsPUVPqNPZsU/SJjdA5M68jQ8wGyTuMpjVxxNibwhnXcRLzI2hZ/Fb9V52qITEzU9Mp6WOoLB+MA4nt5Yt5BURTMi0OHfwZWRmfGgaWFnlUeIlzziLEUOwiVg4XutrxPWMJUTkDX0pLoWL7rvEdOHBSkNrZ4vKp+8vu5Xpc66TNB3t+Uw+iGtDy0dRp6b9yX9xslgZcVjSHJE+p9XvWtNCZlQVJpTqjkGt1R0bTQLrPjVjbEd5QerG4KWAXrNVGi9XSyAd4KSdSySIsWBE3+zUa1pwCLeCq+MFRKlA2oMy41txdYTjltYFdmXNW9KxXd5JFu6du6|vid:D79012B5-B750-4A46-86D6-1C05C7078274
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1ED3DBC1D71037307E5922E628C|name:merezmaid|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEmm8lyTt42mgvLNfS4aIyUgLyvKbR6YaUFtcVmNNWwlJRf2dGUkDlVO0aT5aV1bvJHyM9EVUJVhpw9eO2bnlAcvYYnnrvfMfDQXwAcCPVKDuRSSIjvqpPW5DVpSha9Eecp8nQHdq6ZKp7nJ4CFBvcmAxoK6S9vgO9tkEm/1ylSuyeeDMTDM4N9aqifOUWmFzFuKy0to1lAhbx90JgMd0iJ6M8GFL9EnZSNkVQkM/kkGltqfJDR550E0SkG6aF8rCtf4ggypxLV5QGvVslo8sZ1WAGvFeAkkUXjEemtewI9N8+v42fgrxbB0dTsjdrUD/dtYzzzhl0mQcVMLgLx4plKnSse5TW97KxkHDqsBfAu74nosThA338axWJ4Wku59A8sNK8/+lNu44zTw7h8Q5r7FyJVUJRp5BCTaIuLQgHWrgiAlwzkXbpEipZ28x22afymf9sIrlLUCSa4Ygwn55cms2oH3CLUQwjLhvxXXc8rYo|vid:F82C20A9-530A-46A2-B2BD-BDE0D2FB01BC
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F367AE41160600CD69834E3FCA|name:damcjyban|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEol3DHraziM2QVAQlDvieXcJMmpdOg95nwczQBz+qaKOB+9U2e9+pRED+5Emvp/g+CxZ0o9yTHTMxrnqk90wd73Mp9xa1tqZLxiUj9/WvS/JMK52a/XdORRwGGn53a5APR7utBgQ+mMfSWEdXr4H3rXH3o+0wfWj8yrXz+PyHrwvATNNLdmIfAm0kzvyUcirAvKDOZ0FdhfAk9LI3G56kal6S7y9aZW6Lja2SW2oIy5nsuRf0Fc4LF01j7nN+/H18ScWrLopNXiVPmTMyOyAq4j68qj+ZoUWCfnst3PLWA3DPIh92WjASN2GnIzjDqgO13Ri+GktLWDnqgpqZkS4FUOtWtTKxb5qE6wQrr/X0U///5+olT7/41cmMX+jemroat9bJFQIW/FJuo2YotZ3WcvdpUqGeRHpw0oWR7RsIC7XErOw7Tpot0d+gJ1CUHBiBU3SLCpD3P2hl2H7QVXXJKJlktzE4LYpckT01SrN2Dic|vid:60D26C81-1D13-4A32-908B-843E6E8830F7
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F499EF44C303CD58FD4B748033|name:fastuzdo|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvErWjocuarS+VuXgxMFyUTolQSe2GNf0HYaSrV5rLBvz6SM6HVnlhgpE+aRDRc1nPhjff4rEi8a8OZZdBAH+vwAvqmjTx0++arPdmlKvDE5I0SIZAWpbxANhLtGIx97t1jCvkvygi4ZMwdFiYh5VFY2KkK8sJdYtC8xIcIZgdBbJ7F0d/Wx/Jhbp2n7LtQZ2T9jXct3jRbsm2xwNgVk+dwc5ZBbCWF4+ImvLyst0tsLRcTfG0q8XOVlmmlapCFxbmWKYRkNt2NDd4uL35QNvF/C8ct3EoyhsELCB1CKuruuAWN9V8mVUUcLAuLc04KH3GZfOKpWAjbaeVA2VpPNj5vS6v+z6VMR8YL33J9oMEzXKxSiNH05NbnrVbv7dv3zzF6dDzvplk3Qg+XhDJ/izRxN6CZ1YxANfT5cccPFTDj2gzPPy4I6heHhRh/YcmGCBODS/b0z1Tq6CUBTgqzav8hm6OR/TrRpJ6VrdlgrwrcLUj|vid:10E0189F-B1C4-4FEC-8C2F-0A7E2A02F8A5
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1EE04AEB39A00615CE78B476BD5|name:smdwrysea|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEqtfwx0UkiWfySVtf/QNbgd2coifBvI2dN04m4wBm22hRJGiTByx3mt/9LEFYZ2UV1+n7kof31DNH5JtXT+wf2Gw2ZTUFOdKT62tsSMVXEusy/dcJIkd1cIXScX9XywgsNDFNQ0WCe9Smw3sA8JxXbO1K0RmFJL5xNBRS9X3gLYlDlQ+2fAHC8+E3Nn0qBGt2NVZJaU2XbCYnegDcV5ytQhtqIKKm7F74UEr3tGNGDgr5Y0zb5XYkryDo5IVR40eqLxVY5kLJp16B0D1z16VqlCiEoElgZpGivgrY/y+RdzjOGvyXPIFKBNw1/9zovjuLHMhIT9pfhRtFNM/y65tSAmwBXn7se49AIRy+yo+U2Z5tiG5DvTMpFxyQGlIDE6p9zfWU8xL2zeQ1CEHYaYeitgKBBEePALxChosi1DQ7Cijm1D7M53eHjaB6wRM3Lh9tMrO67BBfZu3OBVChiqkimtDDKtgJwGOFZ99WAdrUVt4|vid:0563DCBA-1DCE-47A1-98BB-470599EF1392
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5B476EB6403C6E6439E0EEDFB|name:tinykeysi|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEnLhKaNY7qqTLjMl7TTiDqFWr0LZmp2Cbv6JHk6rJZBtfVG+s8gWw+kXxx9OG6Px3YTC0y7+a2oSiSFPdNjE1HewpOS1qsqHy2LcaO/zFjBgJMrtNCJ96JFEVkd5ZvJaeSjgmxj/VVm+PEeALQvmgajtyuCNTkUUNNvsT0dEhGWuOBydJApRZtOmrErmNXw0+VgoMylcd7WrsFiJrcjZomLbhpXuAk2gLf1VKljJ14uX/6JcW9dbLV+9jU0T3ncDXszEw7y6oPyNSlMnHM4oPj/+ldHOZTgSdVfmbJvPnbytygDe5hDPC/6jXTbeQ/4yUT5nFjlbyHXGdXfrg8g7bYWfBlAuOrqtI9dsMYOW3le3qP6G3nAKmYsyaCAuQjMpgncK9XzU82VBrx7NzBflBRwH0DxOavaDEYYsx6zxa7moK5VT0JDWpEECROEVlbB9UGIw9LigrTjaJk64YZAvkQsJitc+AmuwUDnkOzpUP529|vid:14DE07BE-B1B1-47B0-82BB-46A8D6AEE5E2


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
