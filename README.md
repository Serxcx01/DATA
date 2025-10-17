--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2FD6632BA02C48C54BFE8087F|name:calmpfbig|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9H3/ZTyM/YmWkf5oXixDcJFqf+/JY2IQZcFvLad8naEL/aiUN0l2oR11+LvGgcS/VutmNmKvcACumMZcIbMt+AG8WZ8S8uOoBkReaMbXGe9tJDYzV3cibLWy+hEV732HnH9Q2Mo++Ya6t2zBqcBNRpQXR+orSNW0EQpYmC98iqFUM4iZ+bmXSlkC4YW4scSEHLwE/BTn78sfzhr85VMZu7ejp9sHmLwgbFEDjC43KJgnPFLVhNzjai8UFKe3H2G5vY1RBWxcUOGIEBQAvcXNcL7naIpk2O4DQGu3MRCNfolsz23/n3LEluVo1p8tGESFjFaffKM9oQ7wU+H4avvTgRB4+GjvsasTxRs3tM7g4ClBbsANJmu4mqOltVn6etrxM6+MdiKxrbI5MAcR03eCjNHCsMieU5oF6Ov40gM+6NxAisgLZgSp2ul9I4X26vW+6FewfgNDUA1qiqbAU+YOQ61u8vs9U8lgR7X81WKMhD8|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9FCF51B7509409EC63203F894|name:wecopywee|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3Oqw5niPzRC9Mjho3GueOiVqJ2Gcxp1zSfdHBiM736StGWByVXqw01vhXS9Vr1fmhzqaP3/bC62PLNnVzR6NL7ri6aykXwomhdu3yuuHmHoPng2uVwT8nFL2U/gvs1V4QPcahJ8Fs14KrxPdFUIqocXPOBZjx5LuhipbTUlaFUCYAdKChtiUGx0O1Y3wEfXvgMYxwwWnSCVJ/hJNMX7Hp3oy2jIW46ZQYG4akjetjZalKwePNVSaH8Kpzu3nk70RK9LsepkTLi3RPvsLORHDAzfvxpfpQibKv7aUGORSvXKWB+K7tiG5wuaHZ/BlT9JQl44um4CZ78Kg2e/ufAkjfflD2uol3rzfmVaTra7Pkja4no01R/jSuCyZq7dSqQfX6qrznBIeIJLfUKDAPuXT/t7ELSLllPBlKHE+xnG23nlC2cdDzIBEpyh8eMRtA1O+kbB5WIKucIC+3oEGXOhBTUlIaAtjsODb32jP3SbELRh|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FE7E6DC427014EA3921EF58B27|name:vctickodd|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3BtP6iMIppHZFJloEl23BHD5ATqhur56Z/FYN4VCGYfrinQRspPkQLGvjBe2bpbfEe/ErOUnNG6sWuD17lt6+OVM+aEoAHihg8CLqM/cBA7RLeJy45EGhHdWMTryiHZk44kbGsmO4Zz3VYdtjncdS/a5ixHs1ug1BshGIWvJwKcERF34MYD3/wD/Nks6UXNIswIruh06Ovev+gC7NsKlCi1ewSNjmKakZLlUiua9gl4H4+uf2U+ClxXSUXYKWTnXymeEXjznaEw9hcO8TrGpKPcySZXrsjqpfQqsP8OrTn2jtGfeK+uBhBbSFBNFJpBCz6Uklp4ah9IEWm4woMClY9QC4m3OakLWjfMuhyTMqMT18mAIYL1indzM9K1wvsu6P5o/pfDFZ3BQGbppyxE5o8VJMaCPC8fMsxeum1QXbZ7uKJpSUIbgiIWkhwmqoo1EQmRVEoKSxwaTtcOF7tOXkl000k9kTN97v8cg6BR+hYz|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F765887342044DB374340C1FDD|name:mzzonerug|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3x62KTtGeO6tm/fgN8GIIGlgU5SO3fdrw58r3y3sYw7V2yFuxhkbRplUOGKnNWPwfGerKtx1JZaAQrQm5F0O/iliumDQbi2qWEvtmgeVdMVilM8MP34eHltDHpET9iwxFLY/CuiNQxlRwjaDas7s1W+A/91Bb8oeU4TrsWGGzIpgtKQR5ztA6P1NRhwDx/TWS9seKBalZDFlGuBIZ24bWEd706mCxUEoWIbAD0NNo0Hbq11oz7KIuX2/uizL8Ntia7VagB55gB/B7XyltyALRGrOz5CbNuDg111msHTXb1g/FSN+EEu0NGIAD0UGFlcPI65ZGGutIrIoEKGLRiEzCHn93PDQ8OS7jtSEXjpMpZObmkEMD2lkRjIzHkMo7vmpcWDcYXb62V+7DjVpSpbLoYqDefbwCpP+7t9gT6qST6N4xoago+0T+IJEL33XK7w2fJeZk6hpL36EqtagnAQDUNrJGlCkHu5SjsOpysCyYuP|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E7D5530B940AFB2932EA934582|name:ndrwishlow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dzN/q20V6kRuyG7bn1B66HK6yB3YxWoSbFuQ/cVKoEKiEOSAZMCsd/MgcUcT8nvvhcYT/+5jNAGLXR8hWj0u+h/ege+cCLHNOLA4fCBU1LQOfuH1GRqDySPpBiG0WTpM+s/HVYo547gkWYUpzG0wUSg4aF2wLWgXr8hStuwNL0zzBj+LLvKqu5fXYipoPUuQ5fXkdJjfl1foBThgZSavtU7NufMpeutmFRlOajPiH4dr5DQJlbexHZ9A94IoXhQQmy/hVBqb7a3UGH0+djTdlRKZoixSennlNNf4HyDlGnaByvKt06rqkZQBhCg4IhVxEq1hMNFHSmKMcD4oZzGwLxHQ3AyBVsnKnSnB4lT5QmwJZQldfjD0LJHupDrOOyKfpg52jVyETP7l3tcjClYYPwd4iAlvLULyHR8tMz5+LpRYIge8KXcxIgIQzdQLx7rKph2WaUXSs7pliz4b+SvIRkU8q0psq77A2b6dDR2ohRhw|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9F893232308F4AA7967776711|name:cnmevanshy|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo9tqbT11lQtRQYb+Qx45r1l40c2jtAsYQudcid3cCKnUHJXNRMyMWTbqvcw+TgLRuQVar6gaLqGVG8u43lhW5FkR2+cWITTYTGK/W7sX3lIo9BWyFLA78FWlJZtcv2RPDV2sK0eqzNWFMb9Em23zySk/54Dr1xh5dhKRMiCIYw6Dq0mBVJ3pDtLClXwxwWcPPGd9OUpTrYgL2BAVlmslPSCayIzMPAIobKPRQlDIoMrptOHQNsV8yj7cgB7WuoX8uzvBE/CryepAtnQlI5JE8nt1gHCo87GpUAY/izTtm589cJ2aY2SKAf5nz5X1mhJWrAowu6PL+c0L22AKohGdFaOfLylXiwVuBcbtrziPnGRrfb3Kla7Oy8xw1hcpL/oSxgMJN9OvJVMys8zZpcY0R9HV9X9r53zw3IbSHg18oHb18LB+XD3KR/r0QDsn1HxsXvJz8U9QQCwb+AI71ItJZc2xLtCymgTIJKkjXjP9hyPa|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F213C56680031BB34200595C19|name:ahkroadowe|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo5khgig06Elo/tHn9yOJZKYe+FKcCeQII8jaYRZNorxVDu0AiMMbOMjBY7HLSSO0GQghimWiwzP9dCBZ3RUts7MsGBviaJcPxZhDbfXMGi02BxXoPOXnAzNwjlqU2YlsuRg8ahz3Cjp4018kOqe0B0EBqx7eT0VAce/lwJgvdfR7tm0Ru6jUKWkJckUH43vtaDN7ch7wM/1M+Mm0Di28+krAEgBgkY8wds63LQMpPu5qSKJg9V9k4b4OupUYkWnusWpgj0qVCyTEyfwPW2p9n+jzWZspBSoWLYxl66p3la9EEHS4Arb0fi0KqxtBetWQMiuk9+/0BxoV5f0/zjWmLe4l+lLsuiKz0o6ynNS1vI3O2n+k8NJOwHxzremVDrN48IEgc52ePsDOpFkmeIbWvTsR2E5PZobrkQmU+0TATYwMKsP50cNCg5zQ5Qs9SNNMnHXovRIfkuZaRar6NMKhtNu/+/SPPCh4AvLqUlVSVGf8|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5F34E99410A3A9F768D53CC66|name:dmpsgnuice|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo6tQRyDTKYbU8H1IcYwRENyrZ0t8hz/03GX/n3XjSCdhMQxvWN8I5Rh50sGYmwW/lO9HegkNPk279ErCWVvfo7HhaYZtZEb1BKsBtkikoQtPcOWDJ7wTdoCTL8kcOvXmTByTvF51A2IlsklXBWszSPnhxZkR/Zxn5Q5XmoK0ruJKHzHL7UFVyJpIv3nuNHjdn4hhzprx+yrfTt5CDFNn7g/23FPHJDjImZKrYol41FJjTh0SNx3WeLFUjvi3ve7/oYIS/LtTydIEjagXuabUVDbHxFH56jbP1wQH4nURXT+X36k1qmVCS2YQ13kbrh6Iv/wYIBORAcCGxvubQL4kvNXJrJuEHd2nvaOPQ14EnGQREz6UfwEEQjVkfbTiTIFIn8PpDCyGi5Rj/feqlhTvQnWbPkKUi98c9+z14ve5xY/a1iC8U9dZ1AWhL6NNZHh01tMSrFaqUlvIx6fsJHF5E1NN45tRH85uyjcbnnjAZEw2|vid:




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
