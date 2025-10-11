--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9FCF51B7509409EC63203F894|name:wecopywee|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3Oqw5niPzRC9Mjho3GueOjpjYauBWLD18OwEq8wy+2OxF4ksVbctoK0yZTOZEqHjd9RfXR8fR1HMIVeXSlzeMiJJuaWAEOXzAyznMBX4nHPppp37yhScuWqhPnmMdORN7otSJ2MtUeh6IEqtQs+rr+QZ+IlLI/txliAlW5ffU96wV+U/HWKvunWZW6UgXOS6JD6ywJztyDI3EfWVJQOuNVgh8qtkXo446wclugLo0ibde/ur1D6stYnLMS6iJOpy404r+YFf33/smFRkGVPTjwSguxSwBhLgAjjF55lZMf2SDTzlptPHkzRZn757YpJ7J0mEAngUE7bacurwa1aga5Wc/7L/GhdBG9qEnFqRdJ0sGJcumSnwHvDJqt6KMCCxdTHJJ1e1i6ubBaSl6T5nm2PbgQBOPaZqELK/BQ2rz6S4ORxeltc61MU9B/gPeyqdRF8ZnH+TLOrFTjheLoKOHzh6KxM23oeo/x9wRmg6p9d|vid:BB605FE1-0970-4B13-9EF9-8D5E66759B1C
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9F893232308F4AA7967776711|name:cnmevanshy|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo9tqbT11lQtRQYb+Qx45r1kZRcjunr14rAzgLTz+SBfrxPlekRChuLwLJw+sePVKnJRYj2kb8w+arrqA7LAh0e60BYi2qq95jytqvLT4sdcmFAhjgOZnvYW9l5GgZD3CUd3jqoSyBAxp2Zq3PeeCqO2BrT8bsXD/OTWmkE8MtgfRyHqY8o8Gfu5LV3+tNv0Mk/siKZ91oguCPUCh2lu9N0cy3Wd0bZ5/aWQ4QnohSEemf4rDODr5spgMUq27nHgrd7kzCI7I1DuXgnJ5EJjC1Zb0aRfVAlAeh1iJJdhK/a3rHxJPQndlh/u0+/xrYpn3/oMZj0BIalC+WFrSUMTjTAr4r4/yhItsj9rEnyvxPyFx8qquiJGP6B5E7oNI0v5GXbrl9K9oOuB/tshx/5Nle5kdD4Wutfa4h++c0bj62YiaRbyOAPig+emwcNeJobjcajdj1OVpaGThAxZZiRiLkx0GHc0vK7kiWDQV1VNocI1t|vid:F9A93A1F-5194-45D6-BDE0-919A627E1B25
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F213C56680031BB34200595C19|name:ahkroadowe|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo5khgig06Elo/tHn9yOJZKbr+RLhsrgyrWKUV2YoOxHoFJ29+lnCTdbDlxOpB4YZ2MHjDJn2+3Ct9hK8n2sKUJfFO2fe3FNC93szrBnfYw8wa7vZvX1PRfu29D3OgVVj+EOzM5n0t1PeextRkXQnLOjdwNPmwujQy9/GNC4DyMAXPrlcKf4coqH5QHU0YCTnsUG9wgtkHK5e0UkzZm0Ig65Ott5o4sYPvA8wjQ53vAN3RH4aTmtUELS6oWMX0cVaXQVjNKq81YRqFZivegt0bvlKymqTyk9Peu/9xriViP2bgewWoBSi98sCKozowopLJ9xvYyTdPsfRUyBsYYF4L9RA94+E1wixwjeQ+8koY0yR7jcEBQXoiEK6MtFJ8P4ixPTkNimkhjdtSm8VUE8oibqrILiGs+2gFzLEkrbwq2VCwAQCbAqg9MLG6xbwuyLlPopnEtwL8tyJddFfPGtauAVh/eMbas1BTCGsPL4eBvkU|vid:9AAC5F0E-51C5-46C4-BB02-79C814927AFE
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F765887342044DB374340C1FDD|name:mzzonerug|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3x62KTtGeO6tm/fgN8GIIFJD/AJTAaj7i+BmwenoklemxViTc7xi7ZF7XGvxClKyyusJDuHqKzOj/PNcrXxMsqaf2kaQMqhMpKS0PCtsMF0LL2QBYkX/q/5REeXPEaonL7o0goIgU+fnRaHI+A2lK3YFANyNePMdX1SKA4qBUTShdxV/H6tYvjFxklpw8eG02ZWPxDydSx6NDp36z4cCbBdaPDU7dj9tvtHHoGTy/NdBURPKF0BNYWykn2ZuFoh7H5ROYAgVvQLFyoY7cGAcNaUJQUQgXDz8Y9YGrla2EQExpSI7ihG0aZiNHUmSQIyGw35bmb8egoi89h4z3e9z/h89i63Z6SnHDFo5tuA227EAhhHgtYh4/nanWWaq0hsDZp0GzGi+qSqJ5bz/K+2A0bgT2CUUrCeVjcpx1GTyBnYNr+jBofGtdSUr10RiMxuqRg05vkxBPhrunQMASQgiC7rgTfEj0dECf/MESiNKSl9|vid:41EA9FD6-C02D-4577-9C1B-70BA286498EB
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FE7E6DC427014EA3921EF58B27|name:vctickodd|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3BtP6iMIppHZFJloEl23BF2EUo7LpHZGtg1C7RDA3Ivn7HgVy/DA0NTZOKsDyHbaDtQ7aLtbuunOfC/DHLgoVxJPUbYsDEmA3Z0dHWKl1TIhQawjcKku1o8dA1TjS8izS7xaCAAKanDTK9fq/Yz3k/dN7FoNi2kWfC3uGcTs9Am6i47f5nfUBEFNVNYVl0U8cFaNTUoEl+w0b0WQrTXRu8UozVamVk6+zbwdN6PrqeWV/pvwWPRI0EY/EE++8L9IIgWFktJHDKSkLsC8w65fJjr5wDeNjysCQGdUAe+br4yMBDbG12k1BEdYw8+w2EjByx1hJZ4oVNe+zP3AzohqxBuwn+NQgxa9Ck4pGTGOQPoOpCTBFeC792Tat007LqFTCH8/vCVgS3yAaJwc6tLS4lCk4AIPvNMhRonRMi1SZ91lqwIqhpqt/KIMST8droLqD2MorG0PON7yK4nODiVPiGhSuZ2WzAaEUOkrknCF/P5|vid:B1B06C15-91EF-4FD7-9873-4ACF2BE9D9E5
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5F34E99410A3A9F768D53CC66|name:dmpsgnuice|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo6tQRyDTKYbU8H1IcYwRENxx0aZfdsLDkwoPh8tb87Ovo9LUgBMz2FMmLwBeBxeiM1LZLfiFmLNHZZKHQpJz84f9ajX3QUB0yfby5YddOfVRd/6DQuh3RDN34lCB+FNxHKlDyBoJmAuhtySn/JRg3La9y2l3MBvN7G9VIeeZoKFvwUlZeGBl2bjQtE+57JfWp3t+4nQZ03ZAIUC18ltqxiEuxEMiO/2Y2kT6orftQC5jj5EJghdyQqQshBhSut5ZzedYiXVx1kb7h82wN/6dMrli6DY099y5aAljfnF1GMSP9Wn7stffYMicFctZ+cNrpbRRSGsUvLfrtv3/DoxHNG1cbtATAjU2ia7BRkpHrYkWl3JvtfRAF7Sjqxn+ZLhRyKCWMBNrevz3/LAmsNmGi2/wsiEDtFbPiFCsx3WKNUvXBo7Q31Q75DFFCH2iU8doNdptAbzAnfNAn/CEPY/KjMZuWu0W+LpzTBIIsyBthsTf|vid:24902AA3-ACFA-41FE-B214-832B0C43A78A
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5277FD06207961E8AA060B21F|name:sgxgtonlie|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBoxQRk4G0scHkcZImRYDxc8J6Crt3K6QZbokMPzcLpdi9bJ4EGlS8jE7AujsimT6zsG0+gzPAfQERyeCM8qhONtZ9hBNHVh1Z9o3xRnFFOke0U+Vo89fo1R3cOrL7U0M6x4oR1OFUT3yT1znjeWaxNgpwwz77Xugv0Q4kQxpADK/3RnMRSaXa+/RZfPGUVZRcFJl4jcZNOUxOek1F77zbcl/99JYdLVH8iE0IzflQlTunOab0yfZPUf+fHRE2t6vYhNbEF+puFjnFbKgND1v5k7V+cGRS9xStTnNXLQQxIt8KRaFIvsG4PU9PpZZkyE3l2uZXaUwtMhM3KLqPYE+KyPsHuPCqi8C4BuJ/vB1kDPauJomKCvKXDti3Nq7oqV5Hd/Nlh69hWWRxc/1HmB64QTIg9kvzps3zgi1XXywTa8SNleQgOwGC0/mr++PoyUXNNlnwyrQMsXc7ZD7G0LkI/77Lcfcn/azqgtMkUsBYM0p7|vid:3EFF34FF-5D66-4808-B063-FDC46B35CD7F
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FAE25B38580680BC00793272C0|name:xbfairodd|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo+AMvRMHu4tZ9RlD5Gg5o90tmofOuDRydvEVp5fG1KhPpbN96ERBiO25V5jGDSh2210hcC0je3T0y1LHRiZclcd304X88g2fOHHe15mQf6nnkNdhIuAgEHJZ8bOA62xxUZmktliSnvqKXEZ0E8Fy81yHkwD8Sde7gw56n6xAQophhJZcqzq7zy68AqMrJdiOun7u//BtbFEfe61cOQ33uDpHIc4rD9na3jxAZ5Pj67C58rOVQd8EvPOm2HvbciJc2j4a4729nED7d6Ne2nZtInvAdN+aBnLRFVdJT5Dq+SvUNvXL+LRTt+FH/8zO73bvdb4Ar9lUiQ3V5KIn8g4Cl6XCv2sO+cQFJQ3qxutiwknDFrdcfhFiVqoLYtJYa+/NBwXXMGbOhg5sNQGBFd9aV9Vbabu9S6msmXOAQn5Vb5NCntuJWJk49P//QHX8mMnys5ddwe1je5HHZZjfAwa/4gIsJ5K0v7ayw1aZThiy+Tq8|vid:1FF5182F-159A-4958-B7AF-BB693E5C556F


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
