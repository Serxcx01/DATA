--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F36B7A39F9003C4A76C5C517D0|name:atmeledrun|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEo/E5DKB6Q7tUHsl+Vf7VoL6Q9bUET0GKMPINxXs95hhcY96k+8viRTaB9ObKtJEKB9hC7QE7zSpe/wp0lkdkIXCyQsg789Y8v/9YudfWmVbnVMr3oyuqlBiBhSSb3+RNAbuaTWPUbI4HE7cHoBu7qRFYomuaw2kUPPra2OGd4PrH6EYEsHM/TI3hNro/XmyYbfX2xn3vKm89jDWkT7/vhzZp3Km7fVnpWwwNZl2T6MQDWEwdGbY5CnKZARi4FsnW6TSZOiut2Jadr2mBYzzy/H3fKec+ze7SuDf2c9uAlfA5z3lCiN+T3FihMBEhs2hcwLyl+apGjex6VXDDJdUXpLuD8+kDRZgoCHG/NaZo1hDSK504r6eh6zNEwnqP1PVlZX5VCfkocva6apqL5c55fLQq0TchT0DZwunVstKJST8U5+ocDXOEsX+HXxSwcMhyG1MliFGqUySxV5B/DSB+4jPmaKFChvFi+JFf7cGuyqt|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F499EF44C303CD58FD4B748033|name:fastuzdo|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvErWjocuarS+VuXgxMFyUTonIErqho73Bg70W93endrZf01aQtp15n/22HLe2YBU9xiQLZGEJtD4QDwqwm+urU+reJA92jnkOwMDApHJf217cj94BJeUbpaMp2o5+r2Qpq8J8anIet081jjGHagriGbRL8GcJuqdWL0wj31gfzgfq7V914a47DBfLSPyANR8bocwev5fazjVO0dp4w0JimsR6g3qnfWJMAnnTqC7f3lBVWmZ/eZedjaXy1DBjpFP1gQ94vPXfka3QCHzqly9R7t/mJQcMZXOodRZ945bc6uv77g+jxH6TOmfE6+GqXXjcUEMQkQoGEtfhMvPT6V+o4pw8yhTKeTbWcJBKmj35aHJKqV4uExWmbbXcFIU8y/1zSwb0+5zTjMOKvNmnAF9J6ys8KIWQd8GtaIPJoiT4o3vsHGB53ssChGABedkPzdxrW7WWnK4G8JgSWzcDTOzDWoQZdvDea+gaZimHarA/V9Ja|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F367AE41160600CD69834E3FCA|name:damcjyban|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEol3DHraziM2QVAQlDvieXepc7KCUd3ihqjvVZT+h0BaCGnAUPhrS4lVja4RJKHs+dilodjmh5Pt5Qw5g3UvupMVi5I/T63Px/0i38cOUi+JruOl/2V07PMP4vVb091gdE+zGe/dFijRCBAkQDVvviiSaxe6XK4oA4FHQpNhCBWeC8iEB6YfcrIi8HuW3cl7WTWClkno7mYdYbbPN+4VCMzfluwYmqLjKmYORssJ1P8wqFd2XlQg8UDxTaCpzGgOA8yqY7lPNKNZkAhHKurJvaO26vcUxHT6fOML62dOloY7scIXd3gc+J74aR4yl4j/qSpe6WJBK1sMDpm8T7C/swGmu+Z1r8Osp4wzjn2bEdcRnjl4qXJDK+ptZRUUArMoYLHvHJJFAZVU5LVa1w4MbffU0d+zjtWVyVhWJWmmXasktjI2N/VgjgkDfJrjI+nWGef5wgFyhwamngSOddo4Oa+hpcGO2BEXfvfTMVODqSSM|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1ED3DBC1D71037307E5922E628C|name:merezmaid|cbits:1536|playerAge:25|token:lpc5/9GGqH8Z07yuYcIvEmm8lyTt42mgvLNfS4aIyUhL5rQZfW3TeHmjbH+EJ5l1bUWa6CUzr8AkmIItzrN7ZUE09gHpyAktKIMdXlv76jNvuEdJ8qRl9a7hHEtgDXz0OZKZyvZqmb1YZHOZ6nzRhAa3FramXPUnb8JjykGgmuI3cST2QDJXh4YxL5SLSP34h00pk2Bz/7A9AkyAxHaf5g+Qon3fdls2uSWHdbND5h2tnKjT12T8DxcwaWtO9zcKkvtml+oaMfvK28B11KRRLz4aCa58SfoO34PbXgtVDw/NYHa+dtDlxHHLHMxGqHAr3z9ALC3SOph2T0eNPsXi5HltZMFCVw0Fbd129fg09jLpQYWt0Ll2vwYz6FaHkkUEHpQyfjQgDJYFED/oh4TV2OhcOAmgqYaYgpGMyiVf+ZRtSKIw5HCBbMss3DLON3tfBdGgo5Q5SUu4InY3vzJoee6HCVcZw32eghR09eRqpC3QBPW5gB3mzmcU2mNbxjI+|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F327B6B6600431B7B438B0C711|name:uzqicylow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d0lr2qSJnSiOcnxGq7e3nK2L+Ngfzxo16Qbg5WctfzDHd7p+BumOpDUllvp0FEgzqkczFzO5VrFJyYngh1dt2HyUMsqkahBU0vpHcc9UZueHeGCBxNUg06sw2IaEwVYdO5hdeOuuSZJS25GtICbjZ9Ls/Bj8ayLvJfajUQ0Qv9qMTnT4HidrH8ZUyUMkRqZI7ak43l7GWjPaHhom5m6JMM4ILbQsjB68YqQql51O94uiRGJr87LuvR4NuWxfr6bG6hbjMsRDNa5uC3AASFnJc2ft9sHyp4Yp0uVI2ukyCDjFaPNl0nDDlAhJVpDxfNfCRyRQirInIsT4X9ZNf1cEi7PMrJkxSDm/diHrKSPnUvf3TQsJSRAKLlrjfBAx0JQQN5x4Vv1xPj6ErXacgYBUlYqJ2HpQF8zq9CWidBdMHXGDweI5OUP7UhMGoh2nOdKPPVH6FAZ9hEu8p3YjACgdnJTBnsNg++nd7UzYiFPDf+1H|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB2154042CC23074E258756D22276|name:pzrbullpay|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9lrQLKZaz+dnJHDjxn66W24MPnr5XlWjYfmpatgJpY4Ujj3AqoP248Xcrn2i6k1FxdwslneKZNfAifsupAHmjN9Fqpr5ADcr5h9QvEUrdJ2qYJXuKmtUlhLVkeAulKVuJ9Wp8iC803s6EOv+KjN1B+EN/Rxf+P3n+V8++mqQRSQl8QI4a/Tn1+i+dUwjC+R0TNjn9vbDynAlsCjaT56jcgC5BGx/e6WXbf8ry0aii1qN74LfqKLgL4sA+j2fRyIWm3kgcShgIumplYtFP5SHSjgVQPUBZ7herTt7Ba/4RDzZGBz8wWGkLqWP3Fkf5oeBC/CFcnplZRM0z4curEYF2wvS8u3Q8rxl7ru/8OP290SwdqZ2c4aRNo28Yz23HPm4b0wQLWmbmE8CJ5nX52d5KJsCxFAiMEY/7N3WkkCoL21AuRup5uS7EeQqcWa/3B/W/ozgOomvyDRWAxor+LHACQf/iN6BiMDQS2IudzO2hZe|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E626EA110405991EAFE4C52C04|name:vploderid|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d3fC2gAoCzofB+VjACQz9FVSv9QGogIKWTMzpnUylWpF2eys91iaxJ3bwE/CarHENNLPp9uGjHDkkQ0Hhm0r44avgR8qTyqUOTXr58yQJ2ryBk7ujdSMwaiAznODvq1BvT5Q8r/ED7CNa/EjyHkELgSyCx0o/C39QNI6Rj0mxY6KKDzpigJgUiO5Ii9rem3DHBtb5RRO0ZJtQ9tE7OeOGbVc1H/evDVvAGvM2P8FOMPxVHWWGtGvF7G/j6VDfco4ZOKI7Q/svwRFeqfr9ucYSo/GeU/M7/ettx/J+p3GvhFcesDqFJYJmZ3oEhvfmz17dT4dx0JmGdHp/Y7CDmbwC/598icJc7UYopSXKxyaWIeWP9VBMNd8mMxd3/ysGJYV4a34Xch7xrg6sNGztyBZTAc8e9Wbt2BbzlDwpcn9xGlokg7I58Bjk844bWqMjranG6su3N3txotMq7PbCrWAfvSeJevyqtE0nYmZAABN58nH|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5277FD06207961E8AA060B21F|name:sgxgtonlie|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBoxQRk4G0scHkcZImRYDxc8IlKBYGp9w3ZkjsVjOX+F00BxyMDFCQcuzJdm+Kbcc46FRwdhzHxcWY828gomWPUKp9yR5DDOcQ7fd5kSeaorgBUDObvrOy57gAl2+z20ef5rLeJGLD8p9M9Rcb3izjRI8LMdRk7Sm7Usfo7oTGF1lGiYOQRTYmcudYsFGaGzkh+zFHZHpEpGCEql9z3cBh/3BxwLHzcWis8n7PTy10sbpGw3eM5DF4QWpajwdfBCFImRgCrwWjFe6RohaS2dv40t8m9fPGcqhkC5o5eJv6V2j7pTi3z3SH0x6zLgWbmWELvSubqrOG9299SyNO51q0oaVZW97ZxeJZyIkgw0QGhMRm/mx6381iKtKxhtbCiO/4y6mMyXV7Ovd0WKkY5WJuuNEefVKk73Z8FRzPv69UYrcoXf6i/OFZfnD/Kiye2MEbksR/UPJiIzDvj9i61GpeP0wDwGJzK6wbrIO9AyVo1a9M|vid:





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
