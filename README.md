--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhXl3aw1VAts2/EM8Ehge7EaguNLHbBx7yQTQ+QMzZyIYlSkFpRpNDhYI7rdE8SQ1Zc0CjwCMqDWHDxXOQVy7Mr7IBV21B9rlL4Nz13lgDXKFU5JcFBa1aXFUprRV5ECJP6aP32dxrJOZQo5sPCcg1vygxvORpAzdpCMPaNpcppJ3v0XD46YgyrL5Gj1fjro5tSLPUISQysHQLMNtXre9VU9ycp6Y5mgXD2ICnfp7zNJa/VoDgCZsn6Nl53QqBAqlDMCvgDvF05/RbV07oVuy4mOfbbrmRxmFzwkNn5UQKEvMPIEHVAvXjkSD8A7Ycmq9MM3WFOm8COQ3NCrGh4EpohA1qJaPyPU41907DBa5KablDI/l508+jMNbACd7CHlrobLiRZVYCEc72Mtl5BrYRac8WttIw6B4T1e/Ao84foJ4i3pu6/vR5wn34EUIy78pefc45KJf6SrA0w/bI1syHWp|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etaNc3B6JeTHgaq7xmt8kZJZQMGzC5aObUKf1WoYtDDY9Z0v3OytC9mpBqNObsWNq44jDWn0DParBgdsnChx5MF13CV/hsQcdUDRW9zzR9oEBhnShh1ZJduxN5/aiG/8FqZzgQv+lr0JXGSacZANGZFjh1k+R8iuRWvuH7bRh3ZontplSuKJXMxvGVavFbV+0OeXflfVcI48sPArYHkqaWJJzf18cbbj8+AcfKswKfzNDuSsgFELzfhwyOkWtPy+xLboPJ1F0u69+eHr+osDL2RfxWM3DrRHxT2dy6wsGQU25WgmyVxkReQ9AxgiDzJ3FOR3o6hXd6Ld5ZvLZUua8Y9dbG+l1W+hEbFiPH+cn/aa6YINr6EHthRTVADX4AegM37AywlG8ba0/EYu/zY+tqVJ7pW6fpSRe2h071XKFFcehcSJ09PDdSC0B9FLJ9YVVswrS5/TkuQPM4VfDbnF+1GI|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F327B6B6600431B7B438B0C711|name:uzqicylow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d0lr2qSJnSiOcnxGq7e3nK2pcryKDkhg0AxFctC58Xn9GahR/uFLSh+o9AxUJSWdrkrCEJnocZbNvXOLVyxaEkZFtkBD2XpLLKAJdir8Q2Yelv9XqdTQPKRhNR7+g6HA23v+l9EbPBrEdeyrHcOkh0Bf109i2Wd4xhA4Nx8+CF7tJv2ZjTZ/po/AQFFNJqQSRpiuJwxCZCYozXe9ivOKoqgHp6i1bPw8lvxQIW61/jQD2Cp/LxxC3oYuwH9nQZybeAMMEKxOlzToteuQklcol+Ju9eDpqpANZFtCz4IOAdIl8DUoXKlBOBol4vmAjTebAI1G2ToUnvJGVXyZajk9zSCKwwDH188TnKCh4RhZwIsFV7Jhoy6VUe2cBppg3ihJO+Rvb5RV4i/QJA1ip05bOoJv8CYAbLT27p+Zyz/IhEVX47Aym7KaFn0ntGfspRda+owTPuw7vpcBXMrRulJ6FM8QvKcuGE2fu694XhrDcqmj|vid:33679D1C-E41A-4A23-A982-E968DD7A4B55
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2CEA741390A90B8E3054605D2|name:lbrsighwet|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d87onnxF1QkKkl+CmsPyLOA48sJ8KC3VRzdDYBoOulkl1JcKhdAlL3aXNKGPW8zO2VL+FVwEHBUGpD2rmEWbMbevIeUkzHkZNTXGbVnXOEgGOL6YhCchL8j8U56Qss1bG6NV/Dvjyf6RbYn92dc7c/nPcIBhEv+RFLS5q0hGJTe5GU32r0zokBSVwHi9B4XIaBtmy0gXjv2NTdufuolt/Nk8gL8fvYPnXgAB5ja7JJQ5sHMfeBOHJydNYfB51RzQOyOg0GJ7rFjF3J+gEoTrf/TC0ELIgI3DxSHpWy5t88RPt/ES7wm61kiyYUUYLcqQD6ogEAYW/Fuve2KoXZ0QQI6uOwDVP3JqK8cg3oxWY39MhfpRcg9j+Z82sgKPMmeTQf1wBbaIFAVo5DTE+RWAXNTOHhRrbCbfxCpVEk0HN7oDmXLxMH7VtEp0Be7EVwqjDM/4DcTAMap2IYD97pr4UZfn3ccpnstTd7EFSqrnV9HH|vid:6C617421-F26F-496E-A3AD-5E7A6DD93DDA
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E626EA110405991EAFE4C52C04|name:vploderid|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d3fC2gAoCzofB+VjACQz9FVGX+ymeVVra0HZTptqTyvY68ZFYEkphD0A1i2jyRWy0MLD8Ql5YxMplYeruwLmmTW6RrF9XtUBSvEkSpJINgJCsBEmcgP15mnWwJZBktfARe1UFLxiEiO8FaOu5ukoL27a+FJ2o0pX2Q3Ag8EAhDgr6ppoP+fwmgvI33d8Uo2r6+HvVt0duiZo1nnUxkGP1cCDDwdfFYSGUAaAMIjQGfM9fvvGGpiMZILoHu9BbNezCJaVad0AdFa1RVK5jMLvPTZvQxbZObHjE287tZ4ONgFyf0zRgit4HJcYhyc16Oj1MMJKBMWQ2NLci9VDpMA8sOAvprEwn3TL5dCLzbEkW1ecRyUF9Wq+e2iOKpvc2gPmXYthRmaj0En27GBklIdq6YRgyKGb22F8Pf+fz15H86Ogq8HR8eiSXh/5dzhwWEz631wKHppDbaw0ct72ABEh0vvs++Upe15OkX5WcwUi0Uzi|vid:4D19159F-6DF2-4883-ABEF-449C026FB1F5
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB2154042CC23074E258756D22276|name:pzrbullpay|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9lrQLKZaz+dnJHDjxn66W1V8cXAQNVW7lRt7zfkNGJRvIQ72i9wRLX4LlDZwFSeNDdDJUjAHJN+FoMF56EkcX8J42aYNf3hJmIv5HikD9bxb2Phx7Pg1M719HA7k7BqiNyoLudtA6O1X+dqImqH/XXXGOE9FC52NXMKAalY89wU6i9B7UfhJsH/P7LnLhIk+RoFDou/aodV6JwA3749VHUZHSbEarGusnkfYrW+LLv70gpV05ncEC+LwY1T2I60f3xtirEIiwyzy33x5sIkUmaA7hqEd++kvCN4SlpBbXYyzqLn170/OPpJoCQaHi5JeGb6eZXYHR+JI+JsiWhZloIFt9ubKRRpFOreRWKSOvUWrgGETiPYbsErK9Lz10nZwKonEbrFOYq/iuEzqvdDM+uC0tFkh7gPBFrSHRQRQl9r2+k6DTKbzUka3kLbFkklyr38vMfHEAxnCrnn6fmkfuOKAWtvJ0KSdGAFIVSXXrOd|vid:D0330E33-0EDE-43C0-95F6-BBD63CA0597E
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E9633C766809DC8F50BF7BC07E|name:eaaejawtag|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d4noffVLGLpuPXTBPz3w9XGI1KZ4etMnaaY97ms/wTuXrNJA6D/KyJ32FGUcWvdIzV5ghzb1wFvoIrczA+D6ka5NUCaAy9ms+9G1hPPYVDEA6tfJs1RH/0YkTyYuxyOqC5+iuXkw3596hjH6CJ+dkimW76uuWAV0xlyUMtJ3/ys9rLFwS2xL6pIRtpnUmTikkgq3byqZarkvCeQ2NPNqeu0IdBo6OR6T0dSLvP6neXzYCk5rSHHgY7Tei2zqGUYfoXUkp4MmbYthxbUIEWS92wpifj+UiUyccTtgQ672X2syFnkBxDoJn/OKlqoZcLXmCnKcrqpdOH73Je9L5QCQhtMJw/B3Evk6/Expbqdh/GFh5z9HzZblaAEqndtf9ZNgVViQPVJYbymZqALcxh9zWp9HoqdxjfyG+amlQH8HFSIHpqtp47GtUHWG3IwMBJ6uzmGiHS5jp7XSBDwLzi84eN5Drj9isj1RPmPhJWl4kHkH|vid:9B96230A-8C77-49D2-B990-9B2C9E647927
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB216A93B85870402ED33011B6EB2|name:bbrichear|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dz/YUJODZkkyNORTCaH9mxc8tgZGhlc6xON9bl6n9MO663Q7AF5yKTdG8YRlTpFgDt0C7D1tUJdvkXfhkBEABohQPDA3BGkthAKLzVxZ9d25FV81YytOVwVqOOeQZOVbdlYFjy8HYXwq3+bU6vWoGuChTUpsvdMhMyGTv0qEPYO/uNsDUK/gKkmuRcnF9wyImBL/0qONz/XuaR+169PfgUnBRvtU5pvInoMispoOzckFFWLGrD+7YihHJ1WEo8QjhSzSUlCm/4k8GYCsZ0WW+vksMReekh3j+D95coQpy1Mz0KDqJ3IfA3fUvloaiLzBh5GAMmIGk2rym60wEfvP00wgh6bZYFFe8MRlJ42G7jJutXWer8t1G813h7kDkrQu2ccYZUCVt5iTjaTTXfH8ZIbX6Qe3lICdmyL7iknGw6ciVv9I7tbYSUphL8GAmKUYlAsffIaGHQsRenX/5D1uIVoJ7BBlytPJtCHFUEtCgeLu|vid:89621781-8BAF-4FEA-A88E-98912E99A473




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
