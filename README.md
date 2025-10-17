--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E626EA110405991EAFE4C52C04|name:vploderid|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d3fC2gAoCzofB+VjACQz9FW7XSgSAKD8jDAc+8CO+VLfvwVVXT1y57WhYHnWIlPhtxv62G4LHfF4uVv98Wc2XJ5xUCfndx0J9lEiN7mfDVnZiZVuNu81Uq+svvqDLX7RWpniWf29HSn0I8p/sPjkLQC2xpRwRb3eTGPOnGlN3zH08O57vigYQJ7Kt/sryI7LR9IrfJuraoApfTxlmg757TFWGHJxMsA+gtPB/LqciO7V8zilgW5Q2C+VSKxHScU7d2HS6orQCix4ksxKYJov1aK/ibjOdOnKTGNFJlk/bAF4wBvEEyIZTV7T3rB51yljM2JWXRu2VAL7XQjGCLfOaeRK5i7m9QEA0s1SpAc+Nf/s22I22l8lkSC+N7ybZGwVcA1hfoT06t8OeFR6UwF0sfRzyqNFsWKX1qGyUWd7wgOIJA+sToAiyKC+qitsyGmcRtP6WC7gcVv3NMVvAAAdIYgIWu3rtXGT8PtGXU0pH4ms|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F327B6B6600431B7B438B0C711|name:uzqicylow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d0lr2qSJnSiOcnxGq7e3nK1QiS7NTTtfOLG3S0gCtrTTB3Nvl/a11f021yzdUy61Y1sLp779yBX1jMaL+7c7BkcyeKsd8iLNRcJBPAutFwOAHR5Dhrdaavu7rxm1F8VgxqZXrhqqyPUOLvCuTasqW+97cPexG53T21NS/oalm0RVo882wMRCuq/vvTqzMH1RfIgpfl7k38n6mi3rxg4eQeCMF1KynFVApG/H2zeavEjwwyOh3kaV4s9CMMw4MSwKCUfHH0Dk11y/LJhVi7TgwxIBvM/BWWGyoFWSY7N2koDCFPysqJ0BJLONmpIIXSZoABnVY/iBqmNq+oXZYCSFaxRPnyX4t4bpbBl1E/9oGc5QxTwFlj0A50c1KmjRSF8/p9oGx+R2+8GSRhSiIOgSj4JCvFlNjwMOf5S+PeFqpT02eFPb6TWgG2lTLY6o5NJUveMvYR+yjCLDwY5FGQycFEmjbPqo9pfEjermervY0Guy|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2CEA741390A90B8E3054605D2|name:lbrsighwet|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d87onnxF1QkKkl+CmsPyLOAaRdztidxyKxwkpPuB8qAzgfhKFF3nucH/CcqwmJi4iSS5f/HLV9j8clk+bBJvajR4RXEgUQcNLkx9BeOITfg0wl39B8+cT1mqGB1l0BpSQyPJQt/fdTM4yFX6MuCNbCLszDn0vI9XjYrhjhx1AO1cLieOnpIZWRPDtNn3E/Iv3bdd7hBBh1okAKq3FOqH0r+j2i0PWTktP5NG3QTk8qY22PtCpNZb8vZ/TtJmQUQT7eskePZX1JaipoEq0hMYu10EIgeOA3JTclTGKolm2u2B1QQoC6htCm7IQThV5cUmm3Q8WAvBSGHRJdHsShqz2SH7d3ntDvVwHCHMuMUFIMAmh7CVaNnHc3RQC0Vj0T2N8X58/ftg4HUb9/Mt5/OgcXOms2n5b1Ye/MpXjroPGtL0Y4UyEHrinzIHL0twtVvhugpidynGdZETm+hTZh6KoxrIBDh5xJ9J6adqA7liwlvV|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB2154042CC23074E258756D22276|name:pzrbullpay|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9lrQLKZaz+dnJHDjxn66W1e4vYeOrqMclQqEUf1IKhqZ2N/HYXFm9kjAlb3rl3qSZ9M1VNvfcROpqh/9AhfTei5bdo3kK6S/Vqlor00OPDuulgg/jtaTSYN3gmSvIO922AiaYkU86gjAvmp8zUoNlPm0V1pWWDjA0afZRCk2/AJlFaEpKQAofBekhgP5PxYZr2oVppWo4DBxjLcnNJfqA3aaOVYbfnzftH9thczmpzV9/q95AuYXD0bcoeKjtVbPYWadt8qH5w2E3PBa1/CBIFsC1+h7gmRQAnPnyVtT/2s0UOkDy1oBMH0VJ+ToPrp7klysHupwRg3Sv+W9bSovx4mLb/wFM+pYmwyFWiRVFbsOCACmNk6pVhCgrG0c6Nt4uEDNyY6d8DUNlfAqNL67WLtD8JMpxnhOM3SAHQkc11iYdGNngIEe8iiOhAeNpEHdncmtSlCw2DyeqNcGT4eAWLQ27ZMcXeAcPeajzxJZq9P|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB216A93B85870402ED33011B6EB2|name:bbrichear|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dz/YUJODZkkyNORTCaH9mxej7UbwBqeFOFpMAJKtZpaf7FZSwhtQRd4HVI4BlO2QuoKYVPlPPLm48jrQwMmEDCHuVgkQC/uqVMkak3JKGudWxf2cLf6Ji7EGWC+L+bcwfcpu/6DEqPoliyMMgV5ZIwV9TSzKgTfMrmTrI9m3+vkCL45q1pnE9bUQiTPmqGXAGEHzljdvc/d6HpVhYEAzped39z8xN5UQ4PzUPbHJFJE/HOJhCpPL340wHMDYdDVX+ccc23xU9qiRRFjv9LejPsPM7jA02T7RvePT6nbXwGOUKxKosLSIVoB6aYaz8bhLjLZjIiJ1yxZWziAX69vRyfPdeoXlzYdWT19CANRWhNOL1N8oGFPzO4JUbLjayc6E//BofHunP+bP6ZaUim0R1Ob+KvhMRW8Os9Nh3k1b6Hb7RG1noUaZoODJ4CpFMy9Qb0eyWFi+9iCzd5Sbkv40ycNhRl/GhVKLwZ+x0+g2VssI|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E9633C766809DC8F50BF7BC07E|name:eaaejawtag|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d4noffVLGLpuPXTBPz3w9XFg2Euy1ulQ9coQsEkIo4u4pKB6VzjqYNRvnbkC7tUbFSjP+bLNcQpnXprOnXMTeP8oiNP9LIjpg1KcOpmMtUM2pYMvUK1Cy/HEupNoc3f96/YHYdf2U36ebimRr25TWj06wRduI/rSVKJ3jf6yXm52cQHmvgruBHrWR2dsecnDHM9TRtwvITXGFtgxv1/9X+ZEJSjmNLyMeZ4jRg+CS5V+wA39SDnaeCV6YoL4VLkeQLi81t3XGb5OMcRk3A74MZbWaN1yQYhWkksp5/ZyVwQTj9AD4iwqkgh9SvS6zyic8Ke8QheKtlZB+52h5rD6DhMIRTXrwULgWY1Oy2sE+80gf/tXyOZ2PAZ74whWdxYQEOhAbOnfN6a70p+ItPgBsXpaEmWNGJ10OfFFY5wI6JmZk9OE2SCBDcixn3ARv0iq+NK5anU/+KTJJ8lQuYAv4Fsaafb1+ZgG2s5s1b8lbpA/|vid:




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
