--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EE96402E54B03A5AE674A9E26E1|name:wetjoyqcov|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXL8fgECX1OsA0vTqRy9ImRc1AXwp/RDBM1GsgR+6+JNOdjN8lpTG1Bn7SxXikfKZl/+ueRSMypJLY5KY2WTqwHEvaQiEx993HOmMdQ+l04CpdtyqBZw2i7a4alaTEfdJKiRvOrPzDNkgJczLDxUXDSntHz0eYZzChZMzQ5/w0zdbaMK/Jdcq3MMmgMb6XU/e9WccYADnbwwHwKTew3VIDBND3M1o/3Bh+5Dp3jy34kCF+20mKa5DAA4y6SYq+H3JrEMmtijCXa6LAI8LSrO9T0w+I4dcAE20JUF/TBM38yfycJ2Pz0j3f+XOi/SmhqtE0dxJZMeHJRuI0Pg1fZkcfm0JUhFVvKDoJImv5e0n4baqfiO7wTc1dy26QHl1h0GwsZsu6nCm2ZqV4pUIkE0tP0/1aHOtW9nGAYQIdgLDirRExPUeQRGOiSQo11iZ0yvugxBoFkU6ICaqhG6/l9e1tzChnJ77S2BgFr/t8A5yD98IX|vid:37AD683E-AD95-4044-AC26-4190523E16B8
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EE666AA25F00B2AD6FAA50C41AF|name:tapdrshy|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXL0AZ+LJmbdb1qC7i3DYB9/J7+GZ8Oy3fk+SOlXPZ37FL/9wbT9+qp9+l58DohrGq/unx5/weExiOrkGg5oWsbnm5P/UFjP7O6AUYSTsiDkzJ1hYoflrCsLDhQ+tydeY1ih5uE4Mb83x70zK8KisASGeTQ/N9hzoyWr2BtO1Js+AV8g5/0QUUN7HFKhAkJdtfNihwJyf1Ib6HkMODwefZY9wG9JA2wTIT3T73WrV7n+3/osio0sqBX8U0/GUqWj0H2WoKJCXpoC2m3OKF9TTShWWhMDFfr/j6yYbT2IAh+4TOSJy3apDbB+L7QkpNB/CQ0HjlIhbpWYEr29izF/CAZwvyItQ/fArt5eOw1NJ9eN10Ze8WLPNF222fTEh2WpmkkvfJSMVsfHFxjy1dhxDUfduN/jxdLsnv0m0yTKsGKQHmfx95C0lTAs3MmdfK4eU2hcMbs3HUH6NZo5on4UUBp20LGR5twCdr9FZ0PVv1Z1m5|vid:8B7B4302-9584-4BE5-A7F4-EF0343F4096B
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EEA3F4CCC950033B6A62A0C2004|name:vastoddkre|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXL0EJuKTaJfoy7yGZuPwbQ1EynE/29RN7gRLdCezmVFqBh65J26BPPxDDesd8h+nrusu86WTjGalWQ9N0kASWYAbLRwxvkAPoa7Bl3U6dg+xw8gJp4sfE3tBxxko4K02rjDjogxL6omGBUqHeyKRYFeM822Oye/LymTzjKsUlsMZFTYQJ/1/9bHG9BsYamjI8KVNb8Sblo4FN0VjBnDHdRHNjYkt9h7TdYQDtP5bqm5FMJ03IzCikVEJkPqIGTd5ukhxyGuPenGIoTEliIhMuiEKWqZzftdunHBL/XHMi2+eN++Gc2dEgyBJTxVwMB6EH5s6AFD9lXXGXjeMHv0qbp1oqeqNs7b2fzJmLXq5TbGxcnzDodciUM5Rd5f5NdNPn6wiJquWPLi8AkHqPUh2zMyUoT10uiwHR/x9MRD1sX0tV8iZ6qdh7NIapWqkGhw2qvFtgFDfdr4rIW7vhP25fbV+1b8QvhQy/tVS3hagiU4Fr|vid:DAF41B2F-B9B7-4A68-BACA-87AF17654342
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EECF378341800CCFE6B08C074F4|name:bigaskink|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXL4GF7CjJnTwNmrXS58oHfg0TDmvzk+T5HYmIBcWxnyYZ8M5WwfXf1x6690TraHWV2f7Bi+XvNWMX7yZT0db6lCfmlK9Xpq4JDWWIUKdEu3QKSgTJb1qX9yQFikGdJ+zYo/b0MT/p7C/7W6kZlTfTFVakIO3AwusxaroDjhO+nl7rUiRV6JY8ZE9l2ixPmaXgaqMajFG/iAQ9y/safXA08jwKWWumKplb5NVP3blyNhl4ILlP8Z7Gvd1OBhLEcABfHX4ud1CrxKgUOCO2QzeqJics+0DEIjFSGDOwur9E3SWIwX/o3qi2ojZcRNSdspM6HuGJ4FfKO1gkJ2DaTP/Fv2BppjmE88U1GmChshQcMTyvJDeY8i2EasSjCmeUreXIQY1RaJncKTix6iK+IQxnMRNl4ZsO83rBcx5zYP12JBuaOh4T8Y/tmMEIVehEmWYFhLTuANQdHhPRyIz4L+5+i5ycmPnlcz7HObWP6fDnbIaH|vid:03E00560-1ADC-44D4-B039-0849A47ADB04
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EEEE38AC1DC0645889D9AD919F1|name:tinceman|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXL5VYVsHWkJunWZbmX12HFuDjqYm2PPOo2EeSD7kuRzLMSj63HInki6WwhEnw0RkQOEwY7Cm5myKLkyN2wXK7GxBm/7XaW8bnfkONECVP5jVECabpzKtrLyEdZqaNdrsAKPZL+GbJUr9XT/loNmbNKLo6NBl7ivBVgfqYm7vvNtcnYayd2lJmmZB8MrD/jzoq4VeElZxnWZInoouFlxkSu6KW1gWpJywuvJWnlKZzYOAiIZu2fcz2Pl0fZ2vLvtsHGtZh5vhHwBHXZZRby8Ep0slrE+UIJI42o2MddwrS8ux0lTn0meRqY36nRlZbkpI/BkZE3Sv5Oh5RVO2IQuwCPnKckD6Un9W4ZsPsv7zszSEQZQQK+D3td1qMdf1nu5IXRNecG7SebVM1RmYusn4H/t2YYfFzN2HmaVwEqSurIoNdwWyqS1HHRzGYaPujpl5VJ9u0SOeL6XTVqoJjgZX1yc97bFQVohVSKUuqz+2EspS6|vid:C899C7CD-6638-4A73-9A07-949DB6AC2419
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EE40F4E99A00817EAC75F8C8F80|name:smfcoilfix|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXLwdW06BRM4fgjTE10nTvVxH9ploY/IUnzXe8MZpC8Nh1csm3KWuFYuOrpuTqk68mqJ8a7FUVvIRYRBbj+7KJGvD21QQHMXoCGg9XjHab84UGd3wHmZkOKxIWz6lYxgGeSJo4Ci80osxu6tvpr+gNtQvc3iaSS7t8wrxzk5FZoLNrKBQ9yurz8xzwUQJtOlPWAD1mJzYjLhpqQ2XtmIDpzCuvn1Mxd0PFkJC+OnLvJDcPB5cT8fFIRUUoRLPzzTlApHnfSwxF2MLL4xiwFdcbf6HN/+j3/VVtYot1Qr6Nf8nNYTXV/B6vOJEY1O710CKe/OcaMr9QHmyvNvbPCpT+SOf9DYa5xJVtbMNYOUvNOyB8o1b5L0V6fk91yYTCNu7IdBQDRUuz17fEmjB9ReZ+6dPANRJSx0fEhtaGWEqe17J2FEQOWWX+Wwv498somknkeO0TY/IY8wOpDku8ARQ5ruc6fBjitOMLLqlr3zDJwcl5|vid:20C83ED8-D129-4F6E-BE8C-F873531600DF
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EE9ED0FBB5D07E39F86C6E0B36C|name:deepsjdoe|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXLwZ6bsTmdXNAMPkaj9FKnyUPQpr6A8fWLyxUp1xk0zK7+tYN2XULrz1V2jXArw0Www1Kjoi4aMd4X1+QqCVrvsK+n1Z8nsMAxcu6JuIMPO4jfoOlX8j+ENNzwhX/W199OlkxYxVZ+WadZFzpj07ouA8Fh0OSRBerZjvlziLhV+DPz4rnN+iOryJlWeAkTtTZ7fk4A0MdIr4PuC58c3wlt1aPClnq/YoARzX8aZZ+a345vKSzHGDufdoVm8SggTT81qtCsw80sPwSAfxVqAPi8W53w6aVD8/6ZqMPW9JmlSRdUpF73h/OhinceAcuPlfVDlP/NZtiEKE+NqIwb4NCpu5ysm0ABF1yjvdbpnUkq6ag88h0DXb8ilOmsxjqQWsFIjpgGz2LzfFdREOJ9vj48Z1LihlpQA+WJi8MI469OjFiAhzq28VawftvwSj7fs9Ymni5U+F4f//xcc2ewCTMh0D/wFy/kOEJzsf8EjwPRx/k|vid:D27FEB3D-ECC9-4618-B25C-3B799506C5CD
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:024A1EEC93FF629F0B21C738EAE4F63E|name:atmvealhub|cbits:1536|playerAge:25|token:72O/xdE7m5jtuUuzuDoXLwd2SbQx9ZJMtxtCRLCheO0w216ZApVB/971ZNGCQZkklsT7u+eOQlU50MzeX4GFE/Pd4p00gzMW3GrLo5Bm7N/r2x6yQYPN5QYgwfuOz7lE90u5QnXQDN50W6lFfwmGe9VrV7AKjbOBEdOqfhnPcUXQDQQkJala9WFTWbDvKKP9G49m6/rqDghJzT6mD8FNYX5a+wOU4LIGkVPnUo2ZcYrnACmXc+lN5SZVVfNwgruGi7zyqzcTp6JNd6m3FB/TQ3aOs/vR/XiAG+KDCBugCqemzBxgt8fuEiZC4ehp5kExRrmh5WJCMmJD7qQMbAgEreSxqX67PXzdcPzg5HDuhfsrk5Uav//b0ZyNGvw1iRR6a6Cuz01b/PyGVmZhTXoG5JFnFK0kj80KdgSyqf6iZczlH2ex/3Lv2AYFFRCVM6HfmqHws0J/QBFzn2JQcQaP2qMZYQ1HO4FNgUqR3vMVXkxiEKTc7zqF+tMINtKfkJeY|vid:B71AC9E3-DDE0-4EC1-866E-00CFC868ED02





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
