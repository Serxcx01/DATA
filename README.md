--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95E5E7FF68B00183C9EA27C50689|name:kdhzbegget|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65hP9C+Op1nGRyvx2mWbDQOoQnnvyrcQ0DesFQtKr/PvtunS+ypvDYLiipq+GeWP/wgITtdHZz2ETzIANHgxbWWnt8Cf6+1HFYbMiLmUlCmANNlBHFlsFBi+YMsZSgr81su9KH3STv2FWV+nUNOfdjUsnDb12Ns2XV0UViIZp09vzscdiETmp9Hef/F/zKfamDG5QU+dO+LsjjeR2qyVOSVwdzx8ijE3yI76Me3QQlpSP05ks+cP/aACfygWgKy/ZhHjPpG6veUaInU+t6tXLcWvux03o7i9I5KaqYUr/DOwzTsxHt8uzq6+aCDGktLBp8mDsd5s713P4OeKJF597IUFocsNbpLscMsJ2sB/5UlkX3O6B7XpmoaFyUoUSAsCnw3EWinoIyu+HEpoiK4am3EAEj3D7vuJVXjMpLmryx03brTG9/H6Gmfn/r3FUXseo2Zkeq2rQmldkkHIK365TyAyZnKM26sP9UiVIrwoe2T3|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhXdGhBICAo9LaIv5E7o94OE38KfYLbJPtvmqIwnUAJBDG3SyakhmLS4c9L0z6/i3r9QeAD9eoI55LvxLCnLsouG5MKs5S2xJn6Gzk3Bht7Q/3cGQW+jGk3carELAT7skYmhtC0UZSazTnjgBEIWsLVxUPv1trKIQDzTehqUo7y1/2bRYHcOr4t9oi2X5EZ/qCtIFR04EVTf21mmvG7VdlDNKribAoR3uTDkyHvdvwuJlUf4Vq+aXL2VilzJ2AvogKIZ/Cf9iAmc5kD6EMNk9Q67nD3oPIBzUR/L86R6IgItr+5RhWzYqnMi75kziIpND77wXwtb1ReekwQGacrqGDLQDMOPsriLTMiS2/irI6GNkXb1Iwk89OqERg4Y6hCFXQtOIA0u8OgBewdZARUh2OrGLF2ny5/BsU7XxRK8E6VeB85+syYoi2cZWHRKbHqbvcvll7/R+Otn5V9i3qGFD57c|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F48535EA8B08DCF71EAEEC40BC|name:ioiusipnew|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ61CUTLffaxF9T6lt/oZogX1bSjuFbdYYTiBlZqqmF23kNwSW/jRQkZRG0VtzW2L+NIu3sGOI8NBuAmvFsLoAkp6tKbLHNZ0IpWk1D+X6qNr4m0m+uUaZRKU+tZo4go9P2b2GWn2bSTsxeFKedXnUXILtAVvnH2QNeOVI1o5dLwBZC2kJtE7b9M/xbtkaVgbEw+ZIuemYG8NxTQecVOoHiDz+z3ZLHSuodNugFshnGYormE8z+I1ykaxdgM4aotKx+u0YHTv/wasbLO1vxhs75DHtLI0a5DQpX6k+yDcydgVVoV9e8uawUN5ouQv95z/3lY/yTH3LqQueskInKJg3QgPuFSC3M5lyabd6s0KWnNOQVf9I58Q+lndbK/LGnImMJ5DWQlRCwlEg466qQk0DoaQHzNQY7I9Ag66Po+Zwf8oBv1jpYUep0gygiKN7O9+k2XBFvM+9hUjG/d619XhMzaaDM/0D8z3W30e+EwaCgMtl|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC55440A7D07A506C1F26BD0DC|name:uyhmputtan|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcE6PPzsMjADzTeZMJRr0sY/1pRLELq/aHciVb8h9D7f/wUrRIyejhvZHrz8+JdaMekt+fJifCp2Vf4geY5XUaG3prxMrCvJzMr8CRXfLRNGY72vjUCIBYCQAK1mLrgKqV5ojdGJaIcQ8YbAkx83oillxXVmoFaCCC3ylsudRl3VfMqiuD6SBHnc1JA6lnI3xkShEM4aKvML/rUrMlbWU9K7ZSAXjpy220c2C8deK3M6GcLWghVzOuImDG8k5msHkaQ+l565aVrfMDHi3JwyYlfVkIxMe/YOzT2XLVWm2SsUYAUcSoU3EdQx0Q1q5VMYuybJlI+dXH5yTrHJOYOPncPIaCvLIg76q/nPqPFvkD2n0RjHbuaTz5thxVH8BbTHc6rmvcmW6VUCO9JdQZWHTFlYvCIma6Yt0e6t4OFV5Dy49WJPUomcsyCnDjkxgKvmcaCF0MBvXmMIjhNz65KI9NmA7+WQCnDODjL665f3a0sn9|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F681CE4C0F088010D5EC63BFC7|name:redhubiyno|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65gkNT7532CiiWotk99/LhDnVv/okeZKkmASmGfweIfvNPnG+U3l6yI0U16qo4Pb8J9af7qxAxCb/oylGAk9epmwLYsRfgpCnZ7bZsTY/MGz0dD4RRysT0HE6R0ollgOcX5A781aFGxIGtgWboNhkHkz0cu1GRkhf1Wr5cTGRYqIonOlyI7CH2jHpmZ1f4/cIl9eefQFKRsd2creAiCsI88l5kn97ZtxucwVhmtZFEXr7nvJLdVTcsWkxbCvh9G7S8PdgMD9pARqxUIAkfJl8zeuwL+DSpP5kw5uzrtvg7Y6YJ+pU7KwBk3fcF6Yu+Z/jSwVZ3wOUNRzDXN73Gcl+BB15AMUvm/Yw20JuTAK0XEmEgHxrWBrb42LPaLisO0hbkM92k+etLN3WhXew+r9vQm6FQYiJJGIYt4orGmI2j+l7LJmsS6TYrqcgUFBptu3cZ4OgCwTjeoU0bnL+CjvGnm7hNPMigeonfjqYX5KJsPL|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FA797A300A012B4FEF4EDA17C3|name:typefirdc|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ646BGSidmrWCCHLo6n9egQoSzkTHSLKbSa8eCNbXchcbTKVDJoccMuK/fWTmDvBszzQfvNO2ZfMl51CMdMWqJ55cDkEJDwrUVTCZTydiVuu2LyVZJ+u7KYf337cXS2sDJuwdfeOTZHun08HSMjktEFJlTxniMms3qux9PoB+TIgJseMDM6d237TxfUgzzTvY7UyqK9TGKV6ZUlYsnfyMIkXq9vr9DNO1yn9E5dHst9skHVTTSN+y41+xlRdSlmkdPobYogkvnVykXS2/ZpAC8YbtpWaE3zZQVqk6SIOwbnAg/GfDzYu92Qz27gNeHQsTNBlLV7CQYH/9sxnDvzdQpVAyxiFDI75mx/d8U+JmD0ZUHIA6/kJSo//7+0Suyqw5YIpMaH7GbfLFQXjtICLkc7mPrCdbXMSwrDA91aygPlN6P18EfmL9fzVIwjRlBi7wALwqlfCdbCinC5VS32+uBxg7Qs+4q+RIB2yCS9cyul9h|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etZ4I//JSp10nStJTcZbLJxgiV+kBWa6aRPkParPc/mWjV+Z88BJ8TmhX6R1hgMQ/L/M8P33wQPvaqWYQXa+FYndb9XNu3w6Mzoy6meKyFsw3RrNMsJ0uOI5zu1xLIB1ipX7TlgwBUHSkC2hXfuS9g39jcRl5rF2oEVe9ZQs8ykxHJr5UGbs6lYehUkVf5MdwMYmJtwFjD1Qctbp1we1oHnk+wcyjtub7Ut0jQnMqRxjRjQ2TAJ74qQCITs5jKEw/MoIGib2AkDw16nAeKhejBgpbhXmChjf3J2Xd+43fmC2rITfgAJlwlD6Z9HLajoPXZnYmPYYvbEwGvzudMNBSqMuE53Bm4zyVDjcGOKt4kj/PAez2hg3Egu9N5b8joekXuLV3lexcnhTZSZOJevsxsGIq3TLPthH+ye9PXZuwphxPXyI+5dRRmOPNU3Q9elpcV1hqohwSSAB25il241F0qjc|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95DC91960A3703A49EE5EFD64573|name:layoclhsip|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63wWDrvyp9CJ5SP6rHuDhZzVg0Yt/iG1AcJpvnWPWztXj6u84VwlTcDymwzBSntthNNNu2NIjpqw9fmtKTgYApcWDSbhwOQogPFnN8rdc0HybBwBFzQHR9q7WYQbQI23veKfPsQARFs7rTPD0P05FHEWJoR9Dk87o5CCVWrNaQ/2bi1lH43cA1jrppVm8Ek/I8hwm631DUZVy1CR2lvCZgJ+Qrb9fwJ04WyjQnJtV09VQae2jUyg7Wlf2tym48hEnYMNW0TIraJ8hKS+P3sBYaoyOU4M89OOD27OYuV3VMfRPsfcomeddDoBr61tXhv+Y0W4Od2nFNfezgsWz1kEWm5KUtRP+qWWAg5qquPFEJRxlOanJUAawjJWMo/oXrP+ITmqL2kwEVKkCgST2mwt+hMpSh+SaLCb0vXhfcF5vcrlEWfnJc4USDv945JcXFIXzHp3CXwXc4lAvD7tvaB5JIaVD14WseupcwbvzFhruhV/|vid:

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
