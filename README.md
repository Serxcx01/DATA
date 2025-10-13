--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF109F3B6F290797ABA0269B9D58|name:lardsewxsv|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsiSWbGB29FToZHymitML/4YhwImH3JtkhYfA75Kegg5fxqL/qWKiUBXhtVJMAacjGaIpHl+F6RK9buS802Lbe+ZU3CthcS8CwWs+Sb3G1lb/T/cd45+WjyvSD0xzXs+e9J9541iuu+ych/C9oP7wYtU0I1g3CKUZhvX0DBPKPii/GNNeC1flla3xVl39BCOjCoKhYOy2YvWA6Vnq06nGyuxyRoL3Hzfs3tahWJE7ocIGVLyOncJMJfJHQ2JtrtNtZVwg/R5hjKT6IT/a9RZHJ7wht0OzuPSbT+18sLvDJejIyKoMxPleEJG1cDVEtzMfz6vtqboK66B3NBB9mDs648zLqkSubBPbphTAaqP6To94VeD0TvLEj5vMFk488NbcepHEomx6cUFAHe/B919/RkI+41hK2Gw8NxVEKQsHA9oWLK61ROqjyGNOihIdiILyaMXsbZ8OL4BI5nUfZJynMFT1ICd3tm6Jrm81Rmm8Y9Gix|vid:AEB7CDD6-9935-4CED-B85C-CDADF8FCEF9E
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF12557BB7C7049415C464764F3F|name:kvknitpop|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsiSzqMi5DQqca2/ZeDJjrlyzxVGO9bw7nV6d9tybquHkmyhiei6/5k0etexytfdTxyBoRm+rCVTlpxISq8KuDzwJQBtB72WexGmGI0iu/1+qVuCVKGXxttyouLJ6XX2twEFzCbbNMjDM35o7IxXI+d++ocWcJGE0ZqqB5puIoTtb2j7lhJsmZ+bJrY5ayygmH9zun22IzN8ymHWyjTDBEiMyisHc/fT1aksRF+AhL3y6fS6c/MOoc0rIkfEiHuXOBUbjOfSoZkzmfbtaEL9PozEO6fcvFCd8bgQ/B1NRyiqbPqrmX9KP3tgqJJakkyyUC6U4KAwE0GxSRU+tm6sRInaMBjbm/x5PFspHziLPT29qONjsB3abEFYvEWZ2DjRQZSfEtGMv/H6a52VrsPB80h+ra5p6NJxRF2ePJLceXAedyI3rPwLkL1oxZW7Bdj11E+vKkUzbP8neNEXR5ZGLR0Ms15g+qWZFvg1VgvGOyzmNc|vid:4B2BE914-CEB7-45B4-81F7-A258661B4BD6
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF13215145720AFCCCF8D6747E10|name:rrglowfix|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsiVPyqFXBarrNUD9giF1vb7eHPM8Qa7Xp8hUCZANWvISRcvBJ9wH5wF/XCvcSKnYQXJqcB4vSkWqFjXWYYHHVl4JqjleJXWOU5q3RHUL/CFdyWZySfGWrLR+5ILBgsZ1gcBjR+Xc3TZo/mO1OcqtWpgLtrM6nFbyWOFm7bbUDe9wVK2O9Jxi/RdRP4z6SEEYwA3EhhFZjR4GjrSbX9Zc7GkpdVyRi/W6EYdBvIr3uGOs3MbB2NM3ve9kl1/psU8rgy716hbN37T42US3bCHgIqdnEJEouIQLPYIRE5ubtbyTRjYpdeYnmj9FvyWFvn4D8Ap4Cl3NXwtH7kieV8BzTnHaurBtq4YyO0mtML7yayGlxdWZRPwtyxL2ahvLhO/O+Da+sfraHmSi2t9hC1SPqj9OyDBbNhyvMOzQLASt+yU/vgHKzGkViDNrq3eEUoXyblweG8H99uVuQJUYv+7eQCU75x83bsdk/+4N+Uvw+0RSP|vid:62BBA843-A180-40B5-9D48-C8DE1D3F60A7
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF17AFCD9099071F4AF267A3280E|name:luckerxmug|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2Ctsib4REB1aCC43YXmgBLs3rVy7PZ6htFckLpDR0xeO9cYioRppjl2h2+RP08X+NBAOgtp2Gu3IoOVw31uBmcV4QcZNihTHxiTmV+v7NzD2vcwsNVrZ00HWUMOO7LtnVIPzH6gEIiGujLU2Fzz5o1luf6WyIOmLKsFQd1P3rGjq8pW+1n0I/QePHLd3lKR5NkV3xIfWem8Bq1YgsXChVJYJhb9lIXdVh5tqcaB4HKsecsZjn/xvHth3l6GHPL6meWiLEcVoC487H7SjQV1Y67/rSxL/7r2zwEfTYiOQMQjXtnmArQN7TpmWEIF/nidXpYyfhTqdVJXPz+syDB1O3N33MP1s0p2Oe/CRaph9mKVbWJSU23Q8K60h0VGyfrSSEs32aCT3EH1DTdRWItdA3TdGzp+OVtEbVKadnjld2xn1Zx5OqckKCZ32R3Xzbfd8GO1TCOb2meYFxWRQ1ARdkQrcerrYv/wOrMsaU0cE/viPvSNP|vid:5B2CB6B3-DE35-4171-AE9C-F75FD222C922
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF1E7630EABF08B2B17FBCA078FA|name:nullyotnew|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2Ctsic/00ZKQ5uxLWlTAZNeiFTCh9kByhSvYo0yh6r/1pnvoAywf3a3zbVpPl2PnGL5JTl9XWbTHNuPtX5+lOzD7dAQkB7omYuPMUw7wlilNMHEYgAojmBTjUUtKSkkkTK2+nNBS/mEf414AcjwVxDe+jKAPwIVpLudDCCbrpTtFiN84JwDi0/buV5hNIpnlpEd0mr9gwrKw14VVDZhHds5dZpRJbvH/cOQaVa1uIaurumeo0sCt+v8QSUMuGreUav+e9y6Hwz0yPZC8rAj1UG2Zo7Q0Oe9pWAGg89a0jnU6b2scadh0hF2AtXRekzdrXsvEEg6C2iOb7K5tZiOnvTYgsV2q7wPYVUNLE56SWMQPgPVBIxxDhZrRl4RLenNM5cfBpB9+yBez2NF0CvhbIqsXB3uOIp2wpWFyNDYGWaNFZhZ55nqPDL//sfRP6YPlRO0RyZ3WDjSTPN3J0IM9arpkbG9HygLpkbyrbRwJasW2X26i|vid:A2E62224-C651-4B9D-9DE6-551C0A6BBB3D
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF1B8947595701C6E37E6E5C072C|name:foglethiln|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsiY015X8a1LY8jlOBqujjsdzK2yqibDlYBym3ns3LtLDynrvkGPucYSQsbdL9+okJ8Y9PiqwnMX3/U4xoqiHwEuiOWu7BwkbmORM7cZie4xcUh4JlxNIYbQTw6U8/tcL+wBVoeo2fZh3TKHKEz/BVb4Q8TjU7FWB+9281r8AvuQT5EZk5ArBP+BynBhFKvi2EaojtfuAffpQMaUUGCbNx7jhL4dSnNO3Cl4W9I7uwgD/TdmLRzrmYtOaxbdj84sNZW5MPVfV3KlkhJpfR6MskoKRF4+8JvyBclltrQIaO3mlxyJkU2zemAsM54SjXc4l6IrRE7gGTkUJxb+TtzHsV4KnPglHO+zDxG1MTt/AXShe94Y6qHoiHHuaA4sCjqBm2Stqb4jSRXUD58m3fuGnkQ2KxkvUYoLPoTXxEyUWTFr5RJhVZP9oxmHRM+Yz7TvtSweDsuNcadFTYVLBkFTq+Ks04WC0QOzWwQPRgBTKu9nWG|vid:8CC3E635-0101-4A8E-B94D-5DA826C1DAD7
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF122C013B6405EF68575A2E5CA9|name:debtgbehum|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsidgOYJuqw1lO34sNUbIlTroxs/rkZNvWfPHAIBI/Mz7VES/E19+d6OF70RQM1asdyjKxltUD7ThZiRckpmMhBBIqDWzEdBTqbeTMQEYrKYxfkcp63EsI0Noe3/L8UZs8sQc2IKPEfXhTUBKp/QalDlj7fZqeJg/eVnSYC8GJ0w6acdxQkURQVZeIGYWoEO23t2wa0n3v3rnrZtCry4g10/zlY1iXfkOzVwqIvycK8JynQ3OmA3o7yVtSTPx5ahYeHJnrXTH5R/kPqiSS6iemiw3Si2VYVegcpOfgoqcD/o5E6Pt/jNryzxbRqGYEr9RJD+HAJDXVhTuVxGepUQS4w+CWaAoah5ODDm91p2ew5we4+BklEiQKfhcMAGbzbontW4BdplgeJan8rs/wtdl1vPwOtw87SKJOgbq/JIfr/PVl1h/C4oxtEXcMUIEnL6mEkNAdN0wJoQx7syIji+kcNj1EZe/OqmtlguxjWgCayk2J|vid:7E0E279E-4C10-44AC-8A98-CE2FEF32B548
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF1B306DBDB4061ADB9DFF6FADAD|name:xedusttub|cbits:1536|playerAge:25|token:m7UvsPXEkkgAYSol2CtsiXdcbIRWqHNuU6cEQFvrr0oH5XxAlJTXTIOvS4h4WyrSEVN3Eu2vg9RscEXJmGpdK9w8tMyqInHC9DvCghSOeW9XLdklbfRyoqa42d1pt4iF67T6pbxK6yUarmcF9AltC/OrUVAg6cHFk2G+ifHRWr861GbkV6isyb9pwVcZR2AHoUMHZGs6rMHPTxp+xPyphjdcuUeGKpVOPfn+AAVsivOXXMsjUEBrAwDeX8qoWztMTM/9XRU0u6/lkKj2ukP400feC4v7MwXLS/LJm6z1DYFWCWep31YewGwLVWmym9L1H6UCugOWtAXAdKNelWjTw6CVmaa6d9DmgiEZt4c3rlhBNpGcbCWRqSlsJcxPGVLqWuxefkcLyAy2iU2CNDUi6QXm3ywu9XCqvvs/f5oo0KZJiF+aoyYn/3INWs0rtq/Vy9qHWX6oHcwDQgEnfRokS/aI0cfiZIKKoSqAbpNdal5cGCw2wDOxQV4Mx9mloAh8|vid:EE40F667-8CF9-4BB4-85E9-B0F0EFCFEBA1

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
