--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB216A93B85870402ED33011B6EB2|name:bbrichear|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dz/YUJODZkkyNORTCaH9mxc3xS68+rkrPgfNDfdcgBhCbOIYxSpvsekAo9dtfb58GBInwltCdcmKunvOWWfnwCJlvkNMzFi1vUSMqU0BidWB3hGwyVEq21MzSm3J92PjcsP22phuJfQA2lt4ovUwY90lIkP6asPbzLYMdDT6zV4+/7ChRQ4vKtryaJ7lCVxHydKSHBc/fXfX3eo3tKJtL/7Y7Z4iL1EvgUWqKPNLc6zEqaKqanPMhyCMn6rr49Lu+IKG8o4pIYYk5fR8Zul6V7BaOADcMWb0dB0v/iesdMooh7Y8F5YK54A3kdP+loMFK1/6odFArZmDVZsz5fb7vhtxDj6EG0/6h4Mdt+t4bZkTqYoQKxzK/Mys/2NdNuWhaB0mBz9PYIwk6OUAlUZNhw/oM5JJcGdhSVc1A1f9ljEYjezXApWnIpU8iN/sdaU1iXd3JpQqJwQ9wP1XfOQgMXkbstHGitU6xcTn+sfZw/CB|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E9633C766809DC8F50BF7BC07E|name:eaaejawtag|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d4noffVLGLpuPXTBPz3w9XGL76E/Cw7hTDi66BaNUfB4nqN2kpLScKSvKMHLRdYPhy6KwCw4qR5TfZF5a/2G3nb+Kb/k7GZqtBFpm/l84afZ9HMRJ0VaaKg12IU4ETIH9S7p+LH/zfabymCOya05q37A3Fj2T6gjExWFxGcErSIaiecWpDBa9Q9ho5o2CVnbN4C7heNFGLU6gawGEm836PSHY/p8RjDsOuPwaoW6baorYbI26PhlbkmpkJ1hBT83QG2FOIm8AEnYYTP66cr3xJAuLHJ34fMa1qE8uBm6mL5pKQK53xMgyJEauIgit5+ik9DfNY/GjEDIK5Tv/ACWnpCwIl/CPChoVaK274BCIHg06a3vkq7kohAOsZJQGnHZW7jA/RUoFWWxf7NacRpmlMHfENEPB5t0bvjQ8VL+kfbCWT8srwlPSkOWenR/fi5FhMKMgfn55DsYIpvpR+QQW5wu2/kfNipcNoxyJPrK0aMd|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2CEA741390A90B8E3054605D2|name:lbrsighwet|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d87onnxF1QkKkl+CmsPyLODWKm/JsV/KXcNUswuIzCj1JoN9FU2Qm69zEBwivJMFOfj5x2Jxv1imCFYKHXMM0QOkJA4AM35OQzj9ocfFOv3QgDHKdw7snXO3BaPnQrw5z0t8c1AXMhRKB7YECFt97hqymhno3jLwtCq8WowvkqaEwo7RAec/eaqDD+ojwG0RGA6q1cKXqFZEvSNx9a8OADarMVVCDcGMyrAPVdEfKns75xFEsOlaz5okjp2RJFs8uMbdk7LUfu9/Z26L9IRvwHuYI3DS3hr3T6XhdK02CV9oHl+XpTM/5UZPrPsEj9sMqSAgGJn4HpWCe4dZ2KvfUfxXMbU5cBwSki2pa9u3CXsWfAS4MGmKkAFplSwHAv8nixgIS4PyQE04ZkP7cVH3N4WyybJ5UADKtJJz3mC11AClwPDU5JIBSc6dl3I9jJpNHDVtgRdua8zWBkssMSut4ocdEhKGT+FCEjUCAXPTX7Vk|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etZ/tuL/pmleUW1MJQim0wpJiDLCgZRDfHqZzeXWlL0WRo075SEXoaYeE4R2/tK6qjW1q9F1WVAs3Wjk99DQ+gXIcjTpsFY+LwYDZbVyVboVCNH9ONSu52e23ZX/jmYNPDhgbciix7IBqdvQc2phSNpZeoBL0BGDrTB423DlgFy1btiVE8DyMSbYka5aQ4w06QIi+P1RJ7MO0X9mT9+gYRyXjOSp5O2Ah3ZewyFK9Fn78tV4n2DypkoFlYyg+Q+rKynrMz69cYJ1s7H1NUJ5qcSykqF8hhho6WA3dsrQC60Xvwv5U6Pl08FonklFasnFQYp5UoCx4NYDZMJaJWc/2EGT2UviotKTIYl0VyNMka7OHETcd5iZPp3WGKBOeVCZ04uFZwcZQyCfg3Jj0YrDDHIvh4W2fhnYbY8aZlkPqAoDbwWxwR/ySDAnQvO9JcaRYhPzZkU/stmG/XOtAPpHqh9c|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F681CE4C0F088010D5EC63BFC7|name:redhubiyno|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65gkNT7532CiiWotk99/LhC768vz0kyz/3sXRCnB50uFSt5ChAi1uMzPhNV9GNd/E7J0lBmmFub7S/A1qWoWzDL/qtS+2X3W1c135/Sjhk3G4ARNgj6fcJ5vNBdSGE898UkLwBtrUHuT9GDB9q9WtxBzmKS+KsG+YoBygeCRph1Zr8PY5Woe8qvgElvd5XYbOlrliz2s/EsVtxb1gO0OvoLweqc2TRC75WYtFCDdy5IkgdQRwam0dAZzzDYOiK3Drk+BydIyUDzOXhlso1nkjoAFayourapCMde9jjSLZcnKUiVi5GVdUk8bCTPL5pD5W5falH8klAwDaiDAVfobcoS49R5WnY+uktPvIB5IBkJBaPtrVqqrnYlau1PVeGrsh8J2sXXhaP2b73paTY3FJfOL3OLsem8PU/LFtV7Yx0VIYYAuIOPYzhehMeDRD+P3EFluk56OAmrSyHpqoTUC4dcb3QyydRygwvECFLnFbGjV|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhUZtoJ96mUHxvES2HcAv6X6ZixVLhSdF7YtYld0Y8HrvR8wA+u9XyUgUMRSL7Osall10KPfaCYkaILVcR8da4jmiXGmgf4jIPmU3lPUBDMCRFaFt4ABNbIoAXvQeBWtXR7AJKGK01+QHG0y9Xh3s3/mMdr8lh/Fov7ghL2PfRwxxBBUBPLej9MhFlIbbXhGVdyoBWKhYQB3OmYwOrnZdP9XxoGkX3ACq94CbPnPcZlW/vOrUgB6ZZlqwK+GRPP1lxc3fairZ4RqdSfgKV5kT73jhdmg0GBPXOv5uP610xnS65RRnYWevRxwpXf4nzJl9WS78q18BDzK18GCShXtyYO66X070R5no/5wmBU3mZqek62KSIw1xxzG0wCq+Hz/+/C5h8LTleW8xfKb9W9GgAnpqeatR14YnaBk+Xa1VQHDzNmJXjTGvJvj5jqhGMARSY0PEH7ZvdjteGKDHj+DH0Xk|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FA797A300A012B4FEF4EDA17C3|name:typefirdc|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ646BGSidmrWCCHLo6n9egQqdnaHgkwNkR1xAaEG0bxpBSYHK9Bp0dGXSnc2gAkzd9T+m1Fvxj7mzP+SIQwKMBjipiBvR4VxwcsUG/ZAcemrz4foWL7QrAxRrnOJ17F/ntk2ZA4BY6nZ0mZodrRSfkbA72mdS06B1w+y31Qa5UZ+MMA/trI9TS9I/z8q1m94woGX0L2He9bAjl3UqN7iP1bx3xBIpgEDDwQMtXFrVn983EcS3fuLD7l07Vnxp2+LCDE+uuY3zOQlc+5hcWuEqoWtikASJ8oJJWtiTmSSTglcWKYSx5IJL0lSgMHH2XvSTC6tNDxIHnluZhwtk1rxBHW0Dcno8ZiPqIAmbd/hPGDgTLINyhn8lQGxQ0hV096GuTLoRGf8v/AzeQnyxtcU26L8+ZiUj8PW0xd/S6ddewUqzh3AhTayDes4Px86rGIGJ8p5UdGcueYQaXkVP5tmb3szmSGJ6jPT8hFHvw7In5Fk+|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC55440A7D07A506C1F26BD0DC|name:uyhmputtan|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcE6PPzsMjADzTeZMJRr0sY/AdrsDep8iTp4JMXdai6mz0VLw49bhKPtxLBdBblm/xdCFAQmnNdRh6pJrYh0Ri8+DCysGZKCO8GRm80uARDRIuz41y+5OjMQn9DHkm0zupffpYprBtOuMNrWmLM/nbi2KUILbq1XRTFPtofpTfMq2WGxrRMqO2iPXHmIqApbK/4+XD5VsnpJ94MNGpaSHQ/aWyKK8A9XvvBcvUlo7+i9iaOumK/ej3zxgsNBtD36sLWC0svkHssgs7OKvkQsPT7kog9pNurFR2GenJcTz9PbdvtpvpM7wQdE+RRPgWvq0OmjZ1VeCcyO/xdOkf/nq6wfWueKtOS1voWwtM1ssthETlavv710JKEldVGEG/o+aZ28CP663PgITlvN6qU6/OYNRwIAhFs8WbSYJA1DT0f3UUY0tB0CnbUnQCO6ALR1PhJgmrRh30GxwqPYZaC/aAjPQ6JQLYIP/r+4bSc4ru2Ee|vid:





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
