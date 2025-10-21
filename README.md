--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2FD6632BA02C48C54BFE8087F|name:calmpfbig|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9H3/ZTyM/YmWkf5oXixDcJiMOYMx6Awe5f8rzCCY+xA7jGKpZp7Wi3CDZtun9M98gCB57rmIDJIFCv61XU/Q5dGgiE6huMYxlRo7cP2pin8Tf6Nbg6O1BmZk7Iq+rOSffj3NVEGf26+6sf96mUhLPnOOb6MHD/FkMTQpvmkGu7FINo823nVi50E0C0GQUSYpFyxKMCB8tikIbKa6ih03QrCaR8LQo7+JXYUfssHk1vFPJI4o3yajiGjPew4dI1Uy97dlcn08mV4uGzdFKM97MdlqPaJxoBFGQr/YoxaUkxELMBfAYIhJgDy7AE8sH/C36i3eq2R/EO5crwcodEFg7rU28E7qLXVVmD3q/dF5mFVL2YHUjVS7xl/MNlMX2sW5qE4ewGSabMM3cs9kqG0mBHDF+pQ8LipwVNCg7oX4EV2zBdp+cWIfn6cuY1+KGL0Zd6tumyo1VhZgtWx68lkFQxGVKGjYhLhZ5EZvx28TTfo|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9FCF51B7509409EC63203F894|name:wecopywee|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3Oqw5niPzRC9Mjho3GueOjftmZcgln8S1C5VVs3nWPhjJ2lI80YyvEw6lRTiCIMZK3gzvPGW6ktTFaPM1NKCMaexq2DL6sPiEhiafGOCd+gL6juoCzXDkJtRlJBD/xOyXmYlsrPJJFh94yxR2rASqqIpw6q+VhWYZDl2+hg+rqf6SBMLDfmalDc6ztAPSnJTKbZWbY1tPxRvi1FX2J2hL6Y+y29HMMmlc6V8grbSFpcpZH72v9IwGPFTZMomrMOk+3rRZH7Z1ofGKjoBsXdDuiTQ6GpTP7an1WXSV5NFmaUU4x9779Wu51mnEk/zmAv1QDt3KuvTmFPfx/06AsqmQXF8gvlVmTkqMOVEDQHldzrMgHzsjhrKtKu9TYCyVte3WnSMwuvD5TvXOxgiWcAQMc0zap1MQzJiRJGjvc122PBv9aFbH++fQpu95+rtWFgEr3MxdGEft9NWOKmmcKawV3f8mAt9qsf/Stos3iV42SY|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F213C56680031BB34200595C19|name:ahkroadowe|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo5khgig06Elo/tHn9yOJZKYBC0EgcLa6MYGpzdEwCkw0qUgpJWw01aN76EHTgGZjp/p/UeqZ4s6pykTQ1AkiKF2+qTyutJLkpV5JE8pNG67/B3dZzr9tx/qJ9+MxwHaHsKOV/G6tKzvbFla/Ihko5D2h/45icK/dSBiwwsGcbLWQjBZS5ib+nm0iqbPbbaRqtdHMQlKTiFRmMwzBw3EuhV7xa3yWxNP5vDwIBuaKWHqHQVPmO5LZ05UqZR8XJHK2sMOJ7dyogUP2cNdTy2Sh4J93sO6dFkLl/rXygDqkzexKSPROWyj70OjyU8JX2JW4uFDwYbIK/Omps21NZTiT7LfuEjVfVZQcJrX5tF6kW1e3tMwGdFrDYi2uT+KAloFyvz46FYGYNfZ+oeEhLWCNwMa/z1HwZaKgpSVuXN+Id1P9hAFzUd+Xc1dFiZVo9GRNBpB7uHAiT5L+W3AdvC5/EWj8wA0H1ta2FKCV0JkPhDvq|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FE7E6DC427014EA3921EF58B27|name:vctickodd|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3BtP6iMIppHZFJloEl23BF3vYAHWio5vhZwlW+o+F3Zfzz2AfBvhC5BExMfVl1s7RtGXE1bSf0i1OqzJvgEZzw4tDM8jkhZgryf255MEuUjCOJJI0TS8XPMcuLPMdqM7EJfHIUaUuOahgEClOJllbWgWwuEdJ8hfpxJxE8lu7pB6UvJ9ZvA7GULElsaQbwTOcSGsRpBIHqVtOaXksQbS31YRgp0q9pKhOnvJWojBuS0W74LV0fcrfim1+ylOEE1oi+5UnDevQwZcimBCHBn1bk16/XCuBJe8GK2Cq6yEAGn/r8gPldXK0XqV24XFjJzedo1mSGNB9frloWOY4GBbj+hbtjWR+Q2mQLowDaQl/aBuM1z7cebPSAzd6D87bFei7roDdUGLF1+xEch6edbmgrazOdJ/aPbHAt862VrtEQV4SHGobkMuWukDf7Wth2oEyOLEHiVTOLdHNrJPBQHL3SMBvRC8KkpVyvCWdhbLGRQ|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E7D5530B940AFB2932EA934582|name:ndrwishlow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dzN/q20V6kRuyG7bn1B66HL9soROLfKklKw2C15nqisaHnannj3fJFjD5yIvbosKfixrsa4t+IqWY2SetbGOp5hiBonNzfnPIjPOnzypKPtg3bvCFNHRw9lyBm0hsR4V+unMt1B6fKOMH2XXnNNtLlP65/pRRhc0AdkZgc1NrbE8jamqjquiv/2L24wRHNFjh4St3tFRIoJGvWPFQKaFKFCKo/t/OEHMGBbz6T1CXV4qzZl8YoORYIC5igxhVsFuMb0ppDRRmnzbuw96djkzYTNW4eBd3TLrsSPagmD6wwblF6I13xuo+YO4aZIk9uvXms8PbEXNjn9gUbwk1oY0/tI2DK1+87qwx+5c93yxt1D3fEabMkjk9nKnq239KWW2gyPWE5KgF/02KeWGeWRvABvP8EgCGRX96d0YLIUiGprnRX9LuGBdScLVvotTDqPvuk7spri7/AzL27iVpSm7XSoFuP1UI6u/VKWIMYQSH1Xk|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9F893232308F4AA7967776711|name:cnmevanshy|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo9tqbT11lQtRQYb+Qx45r1n9nLJGnLwvbi++iBZr59TXuSMZPTimk/Ytlsrn8SukqjDmKCMzl0Wexyx8+OrNM0X4oB7eSoT+qLSEfyklZyCIFehvsyMT0oSYunaK5VLiYABny5eFT/QeWxb/ZWaAsVF8tGO+D+lw4MtDPla6O4WpmgShcnISISrWdKR5X9kj46mFO2zglXWDWPDgXO/5atnO3KL/wIOOWHGxeulcRBLFpnxXBwo6yEFpfERksLGKYUbIpV89R80GeCxuuLrUyTA747EmYr6acpkqVeHZlCzT+zBb06TCQPNSVWc3SxxQgazYuF7uhiwtR4fJmU80oqQDXvm7wIZ3ZhyAYkNHv+EQZY0rlq6RxVPrVyY5kiI/lLZbswLP4NwYPi9WEohffz9L5/cHFyxVCRcxPEfVthDevpUUBPxh3+24baCkkGGf+Rk/hP3HvU7DAfEIXSXE23h63ONj5D5yRH+JEAP/Ynm6|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F765887342044DB374340C1FDD|name:mzzonerug|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3x62KTtGeO6tm/fgN8GIIHYVYcLercpFVUckUPY8veptw8I0+GwCX7XXSJAJ8/nZfQ4OoUTyUGKziEEAfofP7w5YcpcQ9yAw4OaqEefcymaHZF9UHGb8uADdMGiXRxU80fshXsH+a9nzH0YBY9btzN3ZEt1mFBPBtYIFuWgGRPsGeg4wBsqfH3EP4U91PLAjF+ff/1OkE4wRf72CZUZVA5TK8B0OXD18gS8GCFjkYPuMKAXnY2S8+K5gIJhHZgsBrgz0QNS+b+PtF5tD+1jZUSZarFTAeUrFeNhIfbJtFf/2FtG4G/gNEp62TY9eWpTVEUD9vbgGN0pqcFX2GftGgMQfjPHx5GfxAi+c5DIRL8NF33YJ/OItPH9FAvLKvy/PDj1asXF8IUSZpQAHzKi4N1I0Wjap01nO83xad7L170F40d/3jlF90/D+JvzPe1vQJN+t1Z6vxUT8h6ZDC8nKpqr7YK2LgX+IkmUpxeWhe5n|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5F34E99410A3A9F768D53CC66|name:dmpsgnuice|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo6tQRyDTKYbU8H1IcYwRENx420t6jqjOhvqzJc59Itgm7X7RDu4QzZPoCUj9idNWlOFhvq8XcZh9NtivuQbA3RnTZ8f/0XlSnRiG8DkVBdKK11odiQ+ZFKA/lVtUfTKtr0HwO5xqqTfPZPrsEKOwrQGyUDXGzHqwm4TOsSFhJtarEf7kOk1gDBQ2KdhZPhoymKNv0Fb+i6Voy0g7zhkvoJlFu731+Vj1cFnEFboykq8gKCShjx4RFqtUPSQqAdAHoQkJvaeo3VWbtuxCtjsI3AvBGxk6tqoz8YWB59wNTJWpEdLqCscJC4PwFkLYw+QZZeg7W9IaPrJrt89HfbEYzb648DlyQcgKDy4+xfxKUcukc9uePz8/yrbdbexhCc9DmSSnfHdf2Odf13KWUBIQXYLc+yckHW1aB5le64UCjcL1IZL/Ee3mKEmctqWSBIbT/NM2Q8SNoEXh3G3CMT3FXfgGg5cZF8YFsFQU9jxRFKeG|vid:





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
