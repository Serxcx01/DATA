--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABE67E5B079083FDF28477597B6|name:wabeanbox|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZMSW8T0at9zoM1N08SqhBbREvKMiXaawUBAnzQ0oQ6s0qfSyEZaQApHI5KesHhJyoMBFqYWkkTb9ng6XGe069eLzEa6OyX4tNplxXdQnh0LmggkyBT560mjzffuiMi/NFeYB1v4nXYcCpBTiGaSP+RX6PaoC/8s7ljih5I0urq47BTi5EYQe7DoysS3cW6GGYLP146UlbwRcghXZ1B5zLmm8bN4a11shdpgEsmh3mezm0qtlkA/AIZlqH/N4Ea3rAHE56dC4nPh1EEuNCL48jCMfQNuUkPzqcLay7ivskQvNxJSN7+Z7G9gWh/1reeRyv/yL+uB5zEUec+peBqQd8JixibFTbf7Dv7jvQ5TxW8TE6QdmdVZ/xXDnjhUykeORcO3t1M+IJHFNbyl3cEUkh21P9k8TQC72thqcaIkjxuxtacdqLKTEuSj9946iLA9VKbgJo515cpVhB9+vtJfxDfljaL11z3NmIlToPYAgIFRo|vid:1D2CB1B6-9E11-4C42-9523-71E4F8264F23
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABC56CA6DCD08EB0A8D836D77A0|name:slowedwet|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZKYaNGoayjOE8Fk5DF4xTTc67GNRPQ/ceoLcTiHMnyc7uEXrNDef3XVgNFP1Y3AZ+lrzzbMs/+pQCYjft/T+xdG6dzvyfUM8mbHbEH2yh4tokVx+yW73JhI+jAbSppJ1yoUV1axRvpKmsqlQD+QM0FRq0/c2D65pwnQ3uY7z/bJJdOEiAPZ9x8JC1ot37FyrV9g+wRgMtQSEwu1dYUOcg9XDW6YnLypQbN4cXumWRr4BZCB0glCPWvKzegmTWUKaRunAV47lviu78wVjM9tDGilMHLAa9TdK6Qz+Eb3nrOarEbdNR4CSvKBLoakEw9SkC/i/y3CFTZwjJ3Dkp/x/35UJAPngRRRUv1zhSyPGS3q2tYIYJckK+xgBIQluamM25EtGxE1wvilA/QB4PL6+kS9WEH8hDCA63+RiH7rZWyYWY5kks9c/NYFKJIb+fZ5aids5oJyLLOov3zS/hIxgmKXlitmEPUDE5h158obbiqi9|vid:73FD3999-281D-4E14-985F-F73F8436D4F3
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC1D948AE2C08E48D0D95659920|name:dmlniceshy|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZJPUrxLzxZFzsyGrXlPf7Gc4F01iQwvPUqTZNIBg2x5vsqi9ndhV4hcoBjamrvRBspSEFz4ROVmO7C+BQde9fvJJZUpaA71E0+FNE+IopofY8RV9snWebrHVQXvUXNfbh45T83ntrQ92naN7gPCsXWjzx9b8WrVv25L2LgN7+cgRrsk7B6U1FADzRtFl50av5cszzVGWPCbUt26OYm0fWOpW1sLZIbnIHoYFvP8yN3o0x7pRdcSgHivccU9E9nV9gPKxDqDleFHbke8ViNwWmdpsvsmG6SEfX6NlSZRYi8nHp+1yw+i0EQlnQTh+pSZ2pgxx3UgfRP8G5jpl+sMPmEzTD6kd/jp/h+RKyaGCth/yu0BJmWMcIdAVNpC6lBMp6sMGirQO1ckIV/iplzBRB5C59sDV4q23vpHSAFlPKL0cy4TDiZDlgkDE4oaZx0+MnOR72PM/jJhbB5DAktq1ngqvAwTmnODvqju4j1RrdyNT|vid:8290C055-D795-4A0F-AE31-488973EE1ADC
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABC4248AA630273AFB0DF4B522C|name:workspyabf|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZI4FEJasxwvtrY3sJxwlp19zsmrIoJVdFcP5LQ4kJm67KkPiaM84zHks2yrTH+g99Jztus2R+nORbBmcsU3Kk5s2MC6nQpqyfHWA6D/AwVCBrLkcdzv3Y8K7fh+JMdLz2Jx7zPZ7ug4qwEwqzA0Jq8SVzeA21huoqEPZL3g0jpCNSYlDsEziCKDyoM8i9I6rhcj6L4S0wwuAmXPej1qcqSAc2yQew1lX5DA2pVrYWbS+cGHYIOwJXe79MiIeeJvKyihnqzYCY6QpvgC5S0Lpyid3+CSdnd6pVXNuR8YZz1g0KiRrrBuruqjX6e16pH+oU3MCCD2OMj2xJIInW1B+JhjfQRBW/moXSK3DvltiQ9WmafqLdnogyQh/hVjWG/4kNqjDhnv8KLe+ARGZUUQL4/P13p/KStLpWGW5EnpsCBeH9t51yIHVLHHc6hTHeRAR0uJPBGV0toIwhXVIFCpI3Qq4ty1eYt79m+msChe2qbdw|vid:79E3B2CA-BF11-4D45-A662-2FCEF7100E33
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC00563B5EE09A03B36C2BAECC9|name:ovalgfdry|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZISh0a7468XlxdyoooNv3Q8p+2mXSOjwwfifKmgNZXNuFWTff+lUpUBBCE2/CLLY9WQ6lAYz0HTC1HyGg2dkZRuVMkx+pDeePeORBIWcNHgLClbhN8JnbcY7gcAsuvwB+m2DE5ixJD0Hjsvjt6shxM937dOhhXarL5C5fLBY9beB1EmqDpMhEPwc11SDcSF9rESZfPtiF4Hc8Nj+tveVHJ2fpGm3cUsF54eOBHMsQUBHZG1rjBh5xI3Ya1TYOAPJP9bjuTpFI3mGQoZbJiW0uSBIyyHUcf8kFaaQsdghXU4ZJ56Wnd4N2O+NZZxqTu5XJHkLMEKKUNpk7HSw/Fy/d39fjMljjFmqIqwMSVRbdmKt4mXvhWY4ourlIDLnwaO1OtCTT36M3k7lp4GxTFRfSkoGy2ejipielB21ufRzgel0Ju59NKGDzqamlMzYpu0tRsTstMexEZvWNU/zHD8xUFUtbwNVH5cy6Kh//FhMXCBT|vid:DCE23401-615B-4FF7-8638-9D3BC1431E62
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABE63C2A7BC067B7E5B1731277E|name:qbklateset|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZB7zKdAkp7Ywxqj+gXBKoJ00JQwEn7tlwkUTaZTMh7Rq82D0/1kwjn9FDtuhKiC6qk3IHXjneTleUn6vH266+/G64rwErbDfzepD3+y1038dlEpD8IRlLbqd8Eb1+MTLLMIqsYluV3OQqmLnGn1EfWipBh9lXWRkFHABcUjQlO6ut5jzskYgHwisH28ilFFe5E4IqrEsDzSek3xf7pRilUztAxc4SUrjFDlXxZ5cJWhoje5E1SrZF76gvVvYZ9KvIKSfnzdjQBi7NI3DRZyC6Unw8qQ1Sxnwwf3B54lhlu1cvTGhcj+TM0d34X5X1rE8Wz6gpYDPOJJ5phahUbY2OSo3+iwkcG1IEgydIlNOnI04mMsEJqn91pOi8dMXiMSYMh4kp1JmrLJAWjaIxASpf8lctz8YSSo3yWxpG3UZQ5oacTwFPouWwKWSHJFzYoL3dtMHyqSKL9kmkE+CfqJKm8D0/06LKNsi7S+/yIn+Y/Oc|vid:26884567-0773-45E2-98FC-00C54D8629CC
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC1ED8BF5070530EFA8B116A7FE|name:ngripejet|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZL2lU/HguIoVz24+JXcX7cH3l1m6HHcc6RhmBiOFVOstoE5WIEoiOKTBeHhcfPtqGJKbEDUB1r8KrlvZjfUFw+aLnd68WjeqI5Ylv9qY1b+xZR+hGvnDAiV5Yxx06UPKLjZhOsDKrmatSd7WeZtaEe3augIdxsxz0Ix1TeFGtExKuAbirKqXDK6tTX2vdqQWE7jgdXETfYwPUBTY/4xm4Cd8DRUzfG3OIXvXTjQz1qPMYgBlb7BDbY9G+GD2bB2F1q/DKF4CJvHeCXb0BMX0zYGzc8ozCvdx/CG8+iFLOknUyAHEba5E1JWhlX3QLCpjRHojiZ9GdI9SHR00SzohTK0tr/OaQrXq3nirl4OozZSEy4I14rKysAvrfG51LhdTTCEb1qIeJV2RYKkP09TJf6JjL3/uIKvJ8NORiQuTalwtsmDDtRvGnBRCKDphxS+Z5rLR5uQFsxK5XCRh6ys+ACUFbEBYF9pXVStu08at3zJY|vid:6851ECC8-BCF2-44C2-B597-C9B55D184126
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABD62D3413C07BE6D41A1C96691|name:nbtgskycod|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZFpdMD8oZZn8eJCuooaBSmhsqClCXMP90O2KCqRUWPJUDFaeWeY8NxuoybzVCBIc7GMXOacUQlCH4uqWVuLoLIqJgCBZ6rD1Op5gP2Rzsti93BW3EhvOh+zItzRewFM+h4ZnOat3dut3RktDfMX3/9WHbkGsEGJ5/0aMgET0Qgqxcv5TqJegjkmAt7Zhlzwa7qJRiUuVhhLTxgH4k6qw3fjiHXvLojKARfhfIzFy7O2YZ0C4C7etqoy3veZh3DO/3locWqWtpCNs4M5bnLzu52rxqHnE0dy0fd06MDSq/Vk3h1DdUQpBk3qVSh582uUY6xtFkaThcwZeuSMRqJtDToTpk089gQeEYrkb6bScbGkqOdbBXNiP9P8lomnF5OGuxVzXWUbBUaWnCZ7X1VHsFViGsoiUM76daoMLow9v7HtpiJgKyx2XS5KjwNU2RoiAT+2sZWb2ihASotC/7pVZzSEjfcLeSNmx6B8bzLCSDGla|vid:91F34FFA-385E-435F-A5EC-E96430FD29C3


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
