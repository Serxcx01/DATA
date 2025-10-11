--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F777A36C2302A417C92C43118F|name:kmopenoar|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcLoKJzRk8kpGZnp/w609BNMRp/L1RpWNZ8NW1yRkV8/3FEE247hKqRCuRQZM3jRUljEtuZmMJ9reidykI75ivkk/FB90YdWk3EIMJXOB9oaIci3KqvkL5T4VNdKoBP3EOs2/wGbiNCK65dpQwp7jTYiw+WAhypwWLw+gYU5+5LL310zpJz9yhSIeaVN/ZFZbHRNdSPNGwpT9bTrhzL+qKqRlkLhinJgJBtJxt4Cs8q5cRtUiio98XvlnDI5eRdah3vMg8K8KkMyB1SDrSLECBfUNELumBl5O1ThE7P3ZtZ+8WOsSTgFbaxV/a99D8N2a6b6Uktm5tEfcvuhtcDYPjjVYPdMbmDCYTjRD5pv56ePr54Sv1wR1OZ3fWD2cBX6Jwc74OuC4E8UhUAO6nuBGkJTF/A/OkAK2GDPxTUVRvoqmG4BjTusA3FfM5MPBvYlSHfjOLxkNxhf5zZzaP8Z1czWBt4cfwvnmWZaKa76IlovX|vid:1CC0BD3B-DEF0-4A93-97FC-F905ADD81382
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F7D5BE98250975DEC37CD10E81|name:tipdpzmshy|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcGgBBe5XBmGjMzcyJJV1bTzaJ1PojzXw3Dc/ExLAuiGNYpYfN6X9phoZa987a5oQb4mEk+FI9B51pbHJD4nhhxsPNg6aJXggyygONVRJ0stvawrhIwF+5uJzQK5qF7CGh5sGO8FaqzWTM5TFGifCLeV4UodeejKFqo5seUWB2gYRrWXpwSEwE4aTmed3CkJGou+wHEOvYtX3zBZK4j+OISSi9c3YOz3YuskeXER+o4HAjhrtKEoHQ2pKRYsaU+Xxjw6xsb6gIEnJzjxmzIpO04QqJNNhZSOaKsabSiahFeFmD1Fn7CX1Ezfnifg+gG9Wh6iEipyLBbLN8ZwxhEHhrKVJ+TcOzdRb5L1jx7B157Wik3LpyDwCVPkCJ9hp3fpu+25uePNXOZ6b2ahr7+8+eM7gjkrxU6hC/XZ1Ob8ZQFmiRR435YEFW3GIRrGnaYHLELAlaxIwXVvuJCrErwfCv3w3cFWOX42ArWrUd72HHwA+|vid:87ADD4A5-44B0-4D3D-9CB4-D84EAC1603BF
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F961EF9A2E063112DF002596AB|name:sowfvzdud|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcGkukl6hayMNC9PkgH7VbEytqZ1R9uURv3mjxq+bGwJVxEi0C5w5s++78+PjUiAhTWEgTkGU8hdtwCcyUJbCzf2tn8JOmgSj1iA/1Qjiql5hOwt7HdaCg36GtOV0iavvyQjkUSuw+d3DZJUy7S34fZ27HyMXdZ0bS0B+cFilxZC3KXMnQ0cywuiwpYsEbQOyJErCBYvfTk/+HinZ+CnaoGep6cqej6XSAylhZ2bQYWnLNVC07inv342slnr/DBQRWFIEeclUdcCqg37t2qFEAwPrBYA4+v5DdEbt1n4UEQt4aqGLoLTkguTOp7H7BJN1Kz4TKHeJokIRnf39ixXEG3Fxk8XSFja+BO6iIilX6VeQ9S1k9hap3osjV29TUJn510w4NlaHg0pywwgmOZQHI5GKkjM/X2/AbJdg9j5JgXMC4UXsKz7nsE+UijXMf5BOQU7xG3uDOYQB0o9Pdn+w0FFmj4MzXv/XW4VQDKSxmILa|vid:50EC0C70-F667-4368-9318-7BB5F004C74E
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F758164D5A01C5DE2E3DA743AC|name:glibymhit|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcHt4ivV7A83uFwBHEbcKTrgU7X2FZuqRwQ2DKSiYwGs8zAhp2yD1RiwViRJrN3bOnFKztRZbZ47HqrkUoREl37ea24Eq2hYM0E8TyTwVg50wp00O4DB5mi3FiH22dPZ/JcFJmw6lH8pfZjs1XTAslzBYz1s2jidhdsyHCRrCnrw4Anihec21kXdt2iDwgoSnzRd4US7ZWp3VyeVf+tgsGJlca3/sTSBLblf9FMy2gEJ4xULSTYSYji+d/Nuwkf7UDQXgOMixUajjsLMRwLsSa8q/P0PvQdGFKsUfP+zdpOt2aUi7ui7ujPyGpYPxuL1irqL/gM8zgvA4ar0eZIw9EDlCXsqSLmPnmSt9kCSQYI6ApSFla71WrxrAUNnGjohUH0PeFy/VLSFK3+MOC6U3/aVDTGW9dbAAomfzi6MqqFsZ4PKgqD/SmBiAkZ84AElW0dTVKnWzszcXwgTzbcQWW4fx3J+IhIWPY35ZZCzcC4er|vid:CE786FB7-4E73-412B-B00F-BA9D34C67A28
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F7B708CC0D043F7E14CDFF2791|name:voneedrot|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcKK7ZVYRA1IxGvl6n/eNlLN8b2C+BJWi7poI/jjaz3bFKqaB66cZ4tzRNGAz5AYE/h0tD5Oqiw0nUU7RoJAiD8zQ6sIB0SwwNeBJFjMDvAIuYfbgWgdM3o4pYiy45DNsRsLKUJE4rNhVJ1KpKTOYKZ2QYo101jpOXLI3o+EER1qowak4cH7r6Pjf8P4Jh/Fm0XHn6vHYNRPusoWrozvY9W7AGWt6GPd87IOSbR/gSXkxBsSQn/rNSsoNRbDXL0iCZf4Ci4stxdc5fKO/5ebmEp2jjxHo8GgIHcz593WSziQ6DeEqnVsbQNI/TxCohp0lJ0xhdN7w4NPr4yCkSLZZFCEKkXm37Nmw2MBd6DJmOVVr8+jClyBQlqoXfVkj8ivXns2Je4qlsRmZtdOOX3smMIGr2yswEKOiNFh2Um63Sk7KCu78eOdc4+GR0eiFAgjgeo5JaFs8zyxCrdi6AWumLMWOyQkohwpFiC0uuV7tmzPj|vid:863E5DA4-5A67-4FDC-8270-CC4BD263D3C3
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F7D66AA19909AAD464A999A3AB|name:vefryark|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcLKscvHhPQU+N1+dHaXx0gORrz1P4MQyqafg9xOqynKSReuRTZU4N3YcJOVFsaFmeU8Nvol4pl9D8h2VeCK9/EzVrCz3BzmJYyp3dA94Vtn9ZJbDSqPyoRboF+aPkvfFNQibO1D8mXdhudIpY0Vtz8Wt8mixpdUaSqKEzOEX+Cn7ZdvSpu4XF84tOZWqr1RsAaiepFA8yqQ8A86SrA3p5V1L8UTmiCIsJB7ILAIkl9xtGtp3wqa42mA1gfBYZgissNyyYV4D3Z7fDk8wON5MT4MhQwfYNngKHlul4J3shVM6v23zmuRsM0XxkG11+Mb6ikrgTWgM1sZRPn0/Gt2iz92OISdEPHZhQpELFdfDxCzalW58ykQj9RYciTqb3USQvBguZGTO5pVkUFLL0A4R1EAlEYiRJDaMavsOenJKIh2nvu2rGIUAjuuTA5Zgayq965itVDOleO74hJMvSxffncklsG4ZGdWRH8cWOpbpoLcs|vid:996A0084-E824-402E-88C7-62DBF715F93E
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC9AD961A609DBC81885134684|name:aumbluewet|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcApukfNLtuDHRywwtHesnrEqCn31gqj0GWc/jn3DfCyt3+yGAc0oEfK4EGTX0331+MWwjnV7wZCAwQ1+nOwuEefTXyP9FAKR6d61CMf8Y7NY6pET6rQPfky40+PheR0qE7d1VCGeMYlJG5TzLGIJ9OMljmked7BFpcN39F8PBddzL26OoDR/ETRJbjIyLt0fHDbbSzl+EOwxzLA2Pt6nYe/d9ruqFiUTPYY5MaKPaqOL9juJOcXJXbJSoBjVgFQoXp3N1f5wWkDT/wMnxir2Vyyaq2WPz6cmnZegy6XtPUdSCivAgpT3AEUI+Vobc3HF1nowma4Y1zvrUYN35b9UZuk363kmWZI3GQ2DsGaNuH5bu9gRgT8Tv9UWmQ4gYpQazEr+vIwRZrset/kYrAg5cMGDJEchN4b3tJfG8/Lz1/GKEQzbm4cEjETrJ8c1wsaSeVTQgJRxIDAVb9XBp+4SEGmVski2AHnzUV1Drv0+hetM|vid:1879CB77-046A-4DBE-A208-DA22D8F5F412
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC55440A7D07A506C1F26BD0DC|name:uyhmputtan|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcE6PPzsMjADzTeZMJRr0sY+yxjj1AmHSwV3f/b+z/OB0/Q7v+6cwVuHlU5WcmgyxmaFvUX9mxLakfhGK+5XXYRpMBdPoVHIsCXMqhwQbj8SGrngt5xHseCJmI+/VV4G7D0iDjAH2N0cCVjjkvtTTuJsgWeZwTRyRs7AO82pezk9Tc5Ew7bJ0+PUEGA637vt+s7LILFeFLKJsGLOkEwfpkIZvYMEaFzjuoIw7ix62dSrf33CfHVYsiXyMUJlRBZ5BwclAT9bkp3hTXhRlSDAoh7ecbYBirMYV69YoPJu4TCN1Lk0RycenOe0MxFJjYKeWNDAPRCGv4itk8nu/gDjQKsCLH4t3SSPTeLMfpbMiqAfzvICxRsmi37GiTlbC1m63QVrrjuMNc0icot5f5VUWX8aV/2UaU+vqm+LhW5xGy37DIzKxySTyow5sFsRb1dZJHBVAKklhYHQF85Y2N2OKAd4KkAlAmD6TGeXgH2nTSMIr|vid:A9692943-DB5D-46E2-8DB7-D3AED3C3178C


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
