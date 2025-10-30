--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E2FD6632BA02C48C54BFE8087F|name:calmpfbig|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12d9H3/ZTyM/YmWkf5oXixDcLqQNdMrbKVvwMT3TTz42KtJeSXUQ42qHuHNkE+VpF5vx35MacOjJyah0kyJOA8j3M7y1x5ZdrTER5xZmrqGAdH1KBIHD6vtOYJQFtM1BW+9sK7fg3kn+jKBkHoob2wo199PpTeCjSU9gNnZFl6p19wjs4Mg7OAJSilRbJXq/g3KJZaFZstzHDRdoXE/A+TQ9JTWETDbAId95ZJzLAgNBIY6wp6QGBXXtOiR0YKF5GvgjaV1rx07PNO2fZWz6awjSg3iFlGqJcmfHKyfAlcsqEp2sa9gUWQ7m+V0ErF2Yx/K7Sw33aTsKFGBNisspyPKizgvtwrcMuuhAU3e3yrvX5H1mYLstBJ3mX/NOey6k9OWz6xK/XpbxtU/FShAQqfH6gNfNt1rAsGL0dEau8bvu0BsELVgui/Q9QgNh6xvEb6arJoI/nhMQnuRUvQnAA93TKMjeJ7w7GNJFJfYzsVRjaJ|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F213C56680031BB34200595C19|name:ahkroadowe|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo5khgig06Elo/tHn9yOJZKbb5/ublxRgCjTy1xqyos90kXqs8/P4TWsqcyjrc6iwhrqN0/mmw/FY6KXT1TFOgT3bGYFRyJg0okGFIm4eCFgpJ8kghhlqD9l58lpGkguwXCOg4wGsr+04x7TwRq2eCAtHSdLLanJI8Gv11EE9zt2oJAhPOc8pcIDQt7tb1RE2GhvfLqvU+iAoJ7EFcB9NUdhjQ7IRyPTbVG7g0aQuYOiHIMH+YjQ8zPws2EYjQ5AYiuBW7+pRyTmdFiJ8coVSMZ0AFahVH7ERYlOUCz2wUOa9jZ/qkrhQBzh7NNjr4wjauzvgNy7SrqAPg8U82E+WfQcO214nGIIyKt5MtB5At00OyqNouRKGceyR9qoG6VNpfVwTIQOJprrUAmZ4ZatzbTQMgYBwRSFLXXsnHGkhYFkRcCLSJqAwDRWlC9nnsjzmhAE8tOX69kfw3enefQ8xgXiF3ksgrT8Vw+3+zc8D91DO|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1E7D5530B940AFB2932EA934582|name:ndrwishlow|cbits:1536|playerAge:25|token:xxuOdCeUD5bmWH5J8i12dzN/q20V6kRuyG7bn1B66HLqQsCiFTQJ86zSgF4a3WGjBUBzR3d3AdGUZNJChAyPW+4qXkk4FR9iT5iISNupnqbBWlgq5ZpaEq6BLmx34EjxNNzJp5mA71xLPtUA6W0LqDEQfGuQeYXm5Dbyq8rYsIQLtlyFxOkh1xAfyzduRSoiJSF21Pcvmw39r5Uzhd7gMYavHDejW0XHuQ+0sfz56RfZnleuHb4lSMQsGga7xM81JIXcdN1teivtFyvWk8ZaW5a2ar/okw5amiL+iBoOy5IQWNd8qCerwsiNlljN0vWMxDo6QMsx+/s0m26wUid8PNu09V1Uz1sPVBhIKT5OlIouHMl4su7ATYUDb0bTHfB9ZvfAcdSfBAERldXxRUFCsDvLWnfqE9BR9FCq2D1/04uPkVTo8tp2R8ZNBjjcozlaP1ZZmzUTLv9HOmrHYiczMX/QLi1v9TSILQqEDpiB6wdxzmGDCGk7MGDw0kYUVr3q|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9FCF51B7509409EC63203F894|name:wecopywee|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3Oqw5niPzRC9Mjho3GueOi3gjkrev/jJEtwn+lXhYFs07ih3z9B8ai8CBM38u8EajMTIkB/6ZL+jFohMQSvqRgR1XA5JPpDTua2nX1mxiY6JVluY6fNlJ+OsF8ncE+hZcpPYz9MBMsLE+sw7nJfkwyJNf04/0ocKegBEaMTq+wFzRxBrCIQrSKxreTtoWfoK7GWWG2tU7qQGwsWT14xaWu8I5UsgTdBR3qj7RbO+Jud0WHoSOjRIpP/FHGygtp1eE1JBBw+pDRutoTR7NIWOBSAOjE793CWw2aJc4yxHo0wtabkPPvVdESFcU5Noj6OSh0w4A2Moo5Fd4KTHk1JVq5ytMuo3W5Aal0W0+dhPXLXdPVbZI4x9gRfzmDNRzdFhXJnQBxUeojUEG/fNxBb74Auza0wivbRV2Jt/+wz7Cncicv/rgl/uKlLsjMrj9V/cF9FcZsBw5cWJiSVgvYkoa3yA4pmJAc64n/T7Qc5n2zs|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F765887342044DB374340C1FDD|name:mzzonerug|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3x62KTtGeO6tm/fgN8GIIEnhhl/Ow2jKoYwZiUQGAWq4Iyf05qbLN8ooST0RtIsOFeXLKlNO4KV9MMItsu55gMgq6PjtawyeumZ4groEz5781vOhC0pl2mdZZB1IehzJk2uB/jMq40eUHhWcy+RWxXCz4qE9yqEjm7uZy5Xnn5QH18aqM8N6l4pe6RZYIHRUnBtErnUW5SC8FzrOYibdWMhfTKET5tkzFH1n5exoYTxO6EfKtfbfMjlnQpya5XIEXmgwPGrsWY/5okO6ZXaHj4x4aIfL47CKgcUeYQPK1xI+RxVdQneLgf2VgELCKVE/g3E5yWQmaBaV92GzKidCecXWJ0k14zDS2dJCtt3myvqyEF4XOPa1ZxDWuLLswodDu0cCrNf5xc7HFaDFOMCcAwAfU9WB/Plt3UfKVtk76jm5mklTDoYhHIgm4OOuRWZBSu90IdSPH+CQKA494mGQaFYdP0MwNMVJRUbDfcisp4a|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F9F893232308F4AA7967776711|name:cnmevanshy|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo9tqbT11lQtRQYb+Qx45r1l8zmXe4h095qxBsQCBveamrsIAJxk6O3vsH0kJAdSB7fP7oKKNyQcXQ8bYO/Lu+KHeeWyG8ya2HSsnfke/Br0WPwckEbeILgWbdXcXhKdSpdanXLsP9C4PGR7FS6nry9BKz1BdJr3C2dMPxPRCGMsaUr5B5Ye68+Vsigo35CCSnHpgekQVO4QkYBCY1O73vhPHNTzKsrkQmdbK/shRRjRcWIVDtqL1Q1uzNQrJKTs+k5q4FmBtlOuAjkbFk5IdG8rEg8g66E0k0pD71hPByFQwzXInnLNnUAEtQjHLc9UNGCEEGZUbID+H6JjwLxYTE47t23EkyMCs35u/SY7n1soo6gBxx3q8ORoRZlkEZyoMayC4C2+IZ911EtN+557d298GHV3nFdF1/BG81jcx5adROgBp79HaNovE1fNcDPgb7YeclMo/cUloP7PYc7H664aukFx0W5QzJQpwNkNhnvxc|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FE7E6DC427014EA3921EF58B27|name:vctickodd|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo3BtP6iMIppHZFJloEl23BFoYphyMqWsDYTnUJl0Iw7BJ0NVQKC6UjQlAYRpsmRibBqLbU0lfmvs/4WOdn54QV6sK9iNETPDdcl8gCGBWoU47tMZu4TsF4xsH2EwTVSJ3Kat5ujewznuWhNUhCijTrwoqGqDpPTkTqX2n494BOdbkmAdGSQ50dUyAXDO0lQeLP/ZdrrYxWeFmc8jYT/whCeNF0VIu4eSQ5XhrqnMG8AwsIXGrIIDdQyESQOYzIxMyzDGYmnrpF+FkVJIws3XhSRdjuI/RLviLKqPWtimQERFIyeUGR0kLkGlxFc2da6j2oiFoNgLrcwd9mIFvT9Fr2KOQJG77f2qEm/P6Jst7dKSDyLJ5AD5dMoQx3kcQKr6pADqyVl9y2oGghmEoIBz5d00hA6/1uvF+uYSdSDFOGINsMRe8UtnU26hhkeyEJL5RaA+Mr8z1nL4JsSKqDlk106H4jOkSnARwsbHChl/WYXN|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1F5F34E99410A3A9F768D53CC66|name:dmpsgnuice|cbits:1536|playerAge:25|token:0E/9VCkXpy18kQXSVkrBo6tQRyDTKYbU8H1IcYwRENy0cdlCqSxCPOPC6AFubIgMpoRd6HEcRiLwxYFnauuKy2KcT0c3t0IW1jkP5WWGw3L/imFqlzcosJBqGT99gSxvCInKfpfndrK1p0n8XnQjQnuZrMmC4hGR1rCpJP4+4NE62CtG87ERcK4NPlNDdkOnkdteszcvocmaGLabcYRTAbIEOlv81KAlrLksPLd9fkFaYBaQmoVKc1RgSOMecfPktykrZ+uXFv2yvmi1UnY09PsDytRYsKO+XL41tb9hehHwKwdFK2Siv0WSBiL4UdmF9Jl5b1/Y/OjhiTGu+nMMCK6EA/rsmx4GtBe4r9UKu/0Vei4Clwg0OI52IQ/XfDR4V7+AJdz4wktUbJsSYBZ1KBu61x6Og7wR1oPMLR8w4NS+gxMaNGwmd24zbrEXOETmD3ppqf2sWG+HajR5OU5HmhgKIA1420TuxkpfXrjwsGtLVzlgyGm21MDRODPaDcX7|vid:





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
