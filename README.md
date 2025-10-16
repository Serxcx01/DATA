--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FA797A300A012B4FEF4EDA17C3|name:typefirdc|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ646BGSidmrWCCHLo6n9egQrcx922NYGD9fRmafb+ebkC+sgTNYwpuuCjSL1edqRx2mVSTmUUrKa2RoNYsxmi1IwaRTmBRTGq7rg1u8+cOB2x7GUjnAg7bh5ZeC5By/py+bb7fNFx6ygNqHQ4iM3JgZzMjmyh54FEPDwavK6ra8K9+lCqn9Q+MJ6vh8EANqGZtGpb2SsPwMWqo4e1q5m0WvCWlEN7EIXAHhRvZmHWtH92teVsFwJW2eP5nm71ye0EDzCQlDieH0SDaIidFbgi1pyv8fz61W5kWZFntbKQdxFxkrzOyr5cjRdRsRkYXtGJkVxOCXxIpN4VW6fGWd20I/facZd8SVqLh/Qo7eJ9Ljs2g6EMyyPPh0DFalOea29GjntH3xQLsfxS+sQX4jSPC//t8akFDJagOPmpLByLF7QEot8bIzMELX6+/ec5KArBNSZOdQI9CMMhpEqqA8qwsDOjTAs+WYuwOxP2pNBnbpl4|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F681CE4C0F088010D5EC63BFC7|name:redhubiyno|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65gkNT7532CiiWotk99/LhD1FlUFuMeG9s61izFlaUMCAk7u4SISDh5Lf4LB1iB0IWdR1BVI5rj8Czeb9rpM4CSb8GR0sjWo9SfFyE2Zx2bzxnlwN+tXtGMb9Fy317Mv1f8d3wvKRDiO0qukBO/+b06rYVq9w4bjs/hQdKDUS3JzskZCbgHD8YqymBn+rdzGkhf5ztka+J2/2wrZw1Qr+IRzZwk8o/oCCgcOc91LTXcJlZtTLJQxUgUk5HnfbhZsV6Gm3XrVsZfMa7oOfA/Ys6wMR5udYIh26sHtFGosWwXT/A/sz7bQehIlmTOBn25LaxTHWCQcFOUCabaZuEb5qMC7S9XXE9+Z8NId5+lzgAKM6jbcL1UNY6tCOxS+H7D+pAaTEyLj1zsD0LXCU0SSh7t2Ri/9E0qR5N+eDWgDBhZQraK/Nu6cMr8j+7Y12EMFbxVzu6NfRQz+qa/GmglNgF6p4Re1ynDjwrCFt212eTmr|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F48535EA8B08DCF71EAEEC40BC|name:ioiusipnew|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ61CUTLffaxF9T6lt/oZogX0AAbVI/5jaLJI2iBbjg/jY531lolAxuLeZzRKkSg/zHFdVD5VJ4rM7S2X0v9H4gbJa6d70g3WqyICiIV0gFZLIG4/BJ3Ck/Bxl3nn9A+u7vw4zQHj/grmvyvksNFTEnOPYN5reCjY1eclarkPq7XKUYaPQdWmE+ZC629Nl4yd5+6GFm1UAJR3ArDkV/CzySVItQUrO+G2eqUBR7md/LGGcvqVtdxrfba0zonO1qm9eIhG7VvZBpGLFE7A6Co4jngxszB0w92vUTQFkPee0vrgQMY2lXYQJr/u1ZeeDqY+KuIM8P4NmCxRw+zockEdkKTGrWkhIP9pEpfxslcJSXYLSebfT8GvRY9mjhrS+dfTM53dGioA1r5sZ7SPCaDTId5M4/q+urko9h3h+sb7TA/txhJTMAZntxYFsMWvnVAEhu+esnPgb+2t4NDbKG6Semlwi47brU//CGQbwhIn3hYlN|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC55440A7D07A506C1F26BD0DC|name:uyhmputtan|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcE6PPzsMjADzTeZMJRr0sY85RynEcLjureoRWx8yoqI2AuvxyR669DKOZcne+ISQ+eF4scwmcRZjkEjle9B2jLSszjS7bXhwrij8Ycoe499lB6+GGUBsV8/cYZQSgV5f28O75rG7N4S0cVTtDVrAkxo1elCCkpD5XeH7sn2CQZH5S1A4ocLQ8YrkJcK2m5tatPfyG82Qc5+2+uUzSkkTVdcUFXy8xg0gdY02iFHc5JkgEDGZcEwqFOm0803UvN9yTnFToFOU0I8kwJiQvz/DWITSR2MX2+KaNHtYUNmI//uRvE0DKpe4stO/vPCaf2bsTfwqVRp1M+zVLiXLvHOzl4rsVHIBzP7YnrL6RK728IzFaIracEBdpxcgZA/kdPHyyDtqgaUZfnTb7FF1N4uVIyYgh+2DiDJl7r23yiYrQsU55cZwWpxGmW4QxyceaxIDyPwBcGiNr0WrRJeLk/DvpJNGFHaq6X8IlbMC+MaY70ID|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhXl3aw1VAts2/EM8Ehge7EaguNLHbBx7yQTQ+QMzZyIYlSkFpRpNDhYI7rdE8SQ1Zc0CjwCMqDWHDxXOQVy7Mr7IBV21B9rlL4Nz13lgDXKFU5JcFBa1aXFUprRV5ECJP6aP32dxrJOZQo5sPCcg1vygxvORpAzdpCMPaNpcppJ3v0XD46YgyrL5Gj1fjro5tSLPUISQysHQLMNtXre9VU9ycp6Y5mgXD2ICnfp7zNJa/VoDgCZsn6Nl53QqBAqlDMCvgDvF05/RbV07oVuy4mOfbbrmRxmFzwkNn5UQKEvMPIEHVAvXjkSD8A7Ycmq9MM3WFOm8COQ3NCrGh4EpohA1qJaPyPU41907DBa5KablDI/l508+jMNbACd7CHlrobLiRZVYCEc72Mtl5BrYRac8WttIw6B4T1e/Ao84foJ4i3pu6/vR5wn34EUIy78pefc45KJf6SrA0w/bI1syHWp|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95DC91960A3703A49EE5EFD64573|name:layoclhsip|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63wWDrvyp9CJ5SP6rHuDhZxg3paRx7xwKVou1txP2a8fMqDUpx82oUpHMxjCON751Cx8JZP0+/qRzo2yBazuO1VT9udRv+WAJ/hxhETw0eAnPa95YdatErNnj1MR8G8Wb+RrYUtXBQND2qPyz5nOssmVik+cYxcUTEIU8P0SWAyoGe5bgYOrl4FSCTvmYVyjJ8e6y1Z/ps6j4N7+OWrJIp3XTa/e17Mas3Jo6dAgQxASD20sd+U77nMoNuwRKpCIPZp7s1ks4wH83ywu5Jx4FAdPKNMqLE3VhwZdCIWNXcZZkusRqAVaNv/GS4IWkebA6nqw1FE/NMxFonWh9LZsWAg4KVJp2KqsSvegPyxz6S2CcOwHaK2Zwi/EYzDA15GVMzTN0Yv2gkaL2ZNtv+Lh9v50U6YUwKoInq7HmU20dvX+xyrXffAFlqng9qEFmsgkl3zSE4orleYHoTr+2u389JZp9D0eeDdDSQRn62o4tq0Q|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etaNc3B6JeTHgaq7xmt8kZJZQMGzC5aObUKf1WoYtDDY9Z0v3OytC9mpBqNObsWNq44jDWn0DParBgdsnChx5MF13CV/hsQcdUDRW9zzR9oEBhnShh1ZJduxN5/aiG/8FqZzgQv+lr0JXGSacZANGZFjh1k+R8iuRWvuH7bRh3ZontplSuKJXMxvGVavFbV+0OeXflfVcI48sPArYHkqaWJJzf18cbbj8+AcfKswKfzNDuSsgFELzfhwyOkWtPy+xLboPJ1F0u69+eHr+osDL2RfxWM3DrRHxT2dy6wsGQU25WgmyVxkReQ9AxgiDzJ3FOR3o6hXd6Ld5ZvLZUua8Y9dbG+l1W+hEbFiPH+cn/aa6YINr6EHthRTVADX4AegM37AywlG8ba0/EYu/zY+tqVJ7pW6fpSRe2h071XKFFcehcSJ09PDdSC0B9FLJ9YVVswrS5/TkuQPM4VfDbnF+1GI|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FB9D4E9CE8083502FCAB4EBA68|name:deboarwet|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6zoUhjFQo4FPfkz007UwCClFiUNspXkc7RsGwQl5Zhx6eNym4evxrQpN3lzdZpBAusnSxWrqQ/izydnyh74e1Sq5dl0eu96pe93Q9grrNmhr010JlAOzT7Q7RDWcbLR9fH7xPMp5jQoZ7hMohI3rkwUqMfQpcf7SLku3+hB9HED4ObNoljYHdv+K85/3HYWHTDHhOSkv0xFIYZavGvkJ3O2Asvl5oaJ+8ZUPYZBAYKDiuHjCblSzqSVsAcmje+Ect9Q61/lW7a5RWqyF3wK1Y631z5LZdXmvHHdx7AlVgJVLevpBsjkfymZg+GgVIuWmmkT9UTUx8wZ6w5Tq6bwBDo5dqphUt/jJF9vJadgWEyqAJPYLP4UgL8EVozuoDjMYAPWx41Fslt/Polkxli8BDI4LBiDmarKKDKul7BbK741F5taFMAB/SEjE0GOt2lyofMyIGYUQ1XRLE/ylf+8CCOk+0wvd/MXQ5ly5e/dKxON2|vid:

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
