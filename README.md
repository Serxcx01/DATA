--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB0EF10AE0C0A4D6F4683BA4F47|name:auparkfly|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZILde9CF746LmtNj+KscIS+EgVXmQ7gLcoBSYQbj8+ndftvdopn3WzUgCKJ7IRUL1JsSYch5zdpSHCBiou+TPggfMGFVDSbaPRekVETrfA2hqag+yYPKVzwgztOfuK2K4RWWenElqplsEi7qM9zfR2SK8EfknJBN3fsBulYaEMm4D1vx9GpC5rU9SaimsEv42oYtq/ar6aim/WowaBUKvpjSqLMaJOKgr9/AGSX2+ryZrEXUoV01AvURF0+mTgkdZ63OlaJAGUsPi8S5urZAwNEY+qVMMImE30PA3dplPXNxIYb6BV6mVbeMtANzLn7LXJd94shodvBxy8WDVTT2J+X0HEbxZCwcQALvkVjaj8EONWKXx+UKIJh3kbcM67cq48ZMA9ZO4DT2gwpORVXMeoOgv6kIpVmeWDmthmyLO9wyV+m8piRwRUJl5E5XjTgOGp7cQMtKT3g4GGJqWfCcAZlzF/4T0a+AaY5Y28NH3psd|vid:4869CF2D-D16C-4B79-8524-D6DC6890FAA4
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB98D1C9F29042916C1CA1F1BD3|name:vpfangill|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZKoagXSs2LtcBhsLrY/2R63YgtVtETh/imfnwyHcK0LwhiEud+hk+4XLciyDp6XyE7i0V/USYw/QmDJ2CeBX1hi6oLgoa8DK3rphzOoLv50G/sz7eT/P6yboBB/AIIJuXp7J23IUIOy8nVXNnYCpmsQ8mGVnx87YrWs5EM5144JThNnKMwGykZLTvJW1MsB6S8fXQmSBXYZQPKIGPLaWVqjqYznk9uQduJp2JcpX3qVwQJq4buWAXcYa4x05WGUD+K/LonZXxjTZjYB5Ad9bnbMv6QTHL4lIklWHFmYnvJqlbXT98CePaaBRTOrq51slyzXceL53HlDGYPrr9dYhKhNU2PG0veNX6e1qwAtL+q8Rs2s5hG9ko6lsMxqNSMzsXKVnNnZolV5lTCgKeJG/Ltxq6AbdweNlfxdZAkHnjgG590zKaCLjQZnZLsCqAx6aIvmpWghBrVsA1+fBtTrZvS3w1DLTtV7H4ucHsTAj4PtL|vid:B53BB626-D81C-4775-B51A-251748672997
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB287EB0B6903B633F5A40C2806|name:yyzastaydo|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZGn2iZwj5Kzq4i9XnyUmBPIWWdh1ZvyhTM61KTvdlqD8OxLvF3FqFs9+wOZmkbEufr8hoons6twryfeemAbLMzoRtPFpA6ezylZNut45laDWdELO1YEWNPovgciWCqX/LugtZZFcYJSinORNFOsiV2LGu9KieJ1KN7Bsd57PuuSEMhdnKHIFAdJzY7AJE3eMr8VwqUrwGYTu/njTRBKroXTQIJXANneiAo9cyFjY5YPGWOee/vMM1ahXEdIVFvSMT+2+ZzuyPpAYQkdK6gHSCizwyYGhMoJZY3QJoSwaE+0bB73HDmNTT6bd2ZY5zU8PMYSkcgXHFdHcTy8cq3ZyP32IWiliOeh0qerrsv4Rs+emKhoxp6eBSdVwCLh2q5bQupzGXcPM2ircs4DYRMd2Vk8ltu3wfUtZeRBz1Un3zevwSJY0i0T637gZ0SkTYGIbaiXXcKaEy7Lj47nKrG0es5zVDGNCPe4vw5DfN5MwEM3P|vid:C5A6BF67-A58E-47CF-B578-BC7876786D73
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB25627629B03AE99091A97B04C|name:grubbquse|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZEtfVswdXctbjUmeCaoqiou4NVLhqLqW1GPrzofjvEozikbjOHRwy2X3m4PEHNaipW0cq59l4Om4TdLq7pi6o4DV+UqFgNChuqHCFQsmW9seGSRdG8pGcCVK5Qu6vfUBHHd/LgcbspdA6kaG9DrY9zEvoCNy3Z8aPPRddVJOOrlwwRX8lhQbKsOh4BL6euIkFT+CrgLBErNwLizi5S6ae99cKue3ACagF/SXnMzupDyfxQU/ssDmsFG4w26sNvl9qpjxoKZhXt25ZMQYX5vWALi/GHqrp6DcUO/kWPA/8owQrFGkHHPW+JlBm+Gnjxz+leTjJ95gRuwM8/crDYS7YrQ4ZkOG7/Nv5cFODD6B8QKC1pHmsmmW+zNrKwpEHxss1BNqbjIIsCN8fEq+Bve+oZQ5fNqyi9KymmvmD+BiMaT437vTdWxeiFQ/MfqcLbV07N5R3UhezBNiVY+9v8FrCwEnueGr+NeyxoqvB4w7QG8Y|vid:DBC68F9B-C726-406C-972C-2617DB5BDD45
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AEB77D9D7A705ACDB9FD4A0C13F|name:kijdewodd|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZBniCpVabYTrPgnY4fLwYGUEk+K6LROxdTqdgc/2qLaeKfcPdlLwfr62GnPCr30+vGksS4oiQ/nkaJzjOq9PnSEUJ10ISTwvOpTjuJ0+Rvf24XeaP/F8yEAiTVdFEUpkCjsEIsO7HSeFaqcKFAxY42PSk/hW2dmZmzhdZky2r++pV2dmaMYQWgFrL8FQuglGtwB4ZKWh7lFi5tVa+zQcUF/ddcaVYjv8ntOQfTvXIJJBVsPX+K9rydY2KVEpFqKzxCUxLfjwA1SXvPhFhWkk9xnUvnbzD2BZU4swCu/gEjRjOLuNPyyuyJKTKIgkzVnTk9KX644TWnUlTHXCAiC0B60VHX9iGmolTrrLBUF+JG8Lh0uCxnAjpyflpkD8wXmD9LmXPrMgdP2Rtvxw/R8gpFy3xFZF+RNyBojD48Jl6zXjppyOo8ApXx2WwvAqexBuciR3z/vHCG6Y6p7GtxAqLAX+kgYZfJYE9xjybvVXVp8Y|vid:4B939BFF-CAE6-4EBB-AA97-E3AE129AC841
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB010CBC99D08C50B824898E69E|name:ranktryay|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZK7+CUV1XcBnSOo/+ow8yDKIUPTNU4zfMT/trsfGK8/YF9SiUhbqYBPEKVyiGyaTdEOBrOlfRQrdQjWb2ggH/Jsyp3Tc/EecU7O0P7drSthMVZDgSA+yunhykWWOCCRouDjFrTwslxsM+j+ZL9mfxQKhb6kIePLBOW+2+z/vrZXt0bPMwOh5iveqx5soTqNb6GvW4WKdpLafD7RnichW+C2ALBOgTM4Cp8P+qCxPW4XQR5QM2vp/uV7ps8rdIP/StFhron2P+L4/4YIh6KzA0C0HWcP4My5HDMGK84sZH8yVuD03sooDwYpNARDA0Q7X+9RyUr6JLSCX7hLEKH+IzeZeluhD+NVbRYS+7KZw7DPlf9UBiT5bHCdJ03y2Vks/MfbjzuDe6OnT/jdGawVkD1z6HQ899M7XO+I2HXGACbIEDH8lZM+K/lFDgemoz58tI7dFlPsgKQLMmcf87mOfe+BysoTZVpOIfr2u1awe6bgk|vid:705AA108-62BF-437C-A378-EDE9A7112E44
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AB67D06DE9A0095D1CE7CEC7E46|name:ldhbakesad|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZBLxH3UOP/BXlWQtYio9KWhcINA99wL9auR6eLJKcTZYN/imQtvrrQLFkSkoQDFlwtA1nzJfAcSmnt3QK8eEFG55Znb2O1LRse9wsDwRVR1D1qibhFoT78wmI1NlBOVKjPxACJKpk4li8zwtlJ2QCTTlgvN39sJ9ATmTLflPY8KGv3nxpuswmcGspWAnMIPAp+qesIY5kSBJMWCy2hPAyjCfVVNsZskEA95nFAWVAp7a0ebwx7RBDI6R+q9KC6/iIGLfIMDoBzRt55a8/Ftel+eR13Ec0//tJN2uuYSeSDMfmCcg7fVVp+c0QlasN7sKfVacOiIbVRmjMVBHklh60h6cTv3dedSF6du8zEaMAsaEe+cMjQf8IJd7B++l1QbWwlQMcYorvny5crhd9f3dvu+B3RHFfP0sbtHBzULImCNwy/g0Bq2LhB0usQ3JwuRcqz9uW9sbTzktV7CNIPBOyMDPUZ8j3os09HaA/Om85/i1|vid:E1286E33-D3A3-4BB8-AC5D-E098E22D54F1
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AD647E0369D06ED48DCD3D8A393|name:patdamwylm|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZBl411jQe9HYmh5xF5C0g+O5ClZgXYSMhoEt2kyNQ97PeSF0BkeWB271McxPpGbazBTLvrcFPpWHFLAw65uV8u+RtYuYwI8yjPR++L+LvNc/ar3TD9Z1cAXc8F8ICQTYRHN9N6Y8sDO2W4dAdv8fvLnzDi/qQ5Kl6ETDUak+nDsM6x2o/ivdR+cQrUNpRnYRPrLP2YA9QV1HXturAPjqqjN+kavu29nXUpSthWFaT+lfTNkDFmmf4Tqq54DiwJXAo60pTvJ13zTsjmAB7mtHenREFK8dMuK2LGv3vFOPhzSemR/4f6uV5TqvYQBCjuOBKrtektMv9DjB+Eadx0IPi7DU+iefLiReqoiHM0AeiivgF9LMkqIiFM/ui73nJo6AqzK9d5kWuQtj5o0BxDigIoY8KqqQPSorI1k5gp3pSUeq5vFdb5gYkLFZQHzWgKQ0QfXppSna4+xaRqAYSxlNer/jjU7uLPbiGRrwjGCllj1m|vid:0886D3DA-6C61-4DDB-9D50-74317AEC494C

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
