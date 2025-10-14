--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023EB1FC55440A7D07A506C1F26BD0DC|name:uyhmputtan|cbits:1536|playerAge:25|token:GOks0lkU2x+b6QTK0L/OcE6PPzsMjADzTeZMJRr0sY+yxjj1AmHSwV3f/b+z/OB0/Q7v+6cwVuHlU5WcmgyxmaFvUX9mxLakfhGK+5XXYRpMBdPoVHIsCXMqhwQbj8SGrngt5xHseCJmI+/VV4G7D0iDjAH2N0cCVjjkvtTTuJsgWeZwTRyRs7AO82pezk9Tc5Ew7bJ0+PUEGA637vt+s7LILFeFLKJsGLOkEwfpkIZvYMEaFzjuoIw7ix62dSrf33CfHVYsiXyMUJlRBZ5BwclAT9bkp3hTXhRlSDAoh7ecbYBirMYV69YoPJu4TCN1Lk0RycenOe0MxFJjYKeWNDAPRCGv4itk8nu/gDjQKsCLH4t3SSPTeLMfpbMiqAfzvICxRsmi37GiTlbC1m63QVrrjuMNc0icot5f5VUWX8aV/2UaU+vqm+LhW5xGy37DIzKxySTyow5sFsRb1dZJHBVAKklhYHQF85Y2N2OKAd4KkAlAmD6TGeXgH2nTSMIr|vid:A9692943-DB5D-46E2-8DB7-D3AED3C3178C
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhWXkC4G+W6UnhdNOedYUx3M+7Z0YeO4GIthmHZrHQ7Jz99pQF99PTbgG04GstRZAE/2kpw1MTh/Xgi1bagzkKwOCccu9WtT+ph2H6aBH76kvN9/e+UqP2ywDCnlKtfx6kY+pSN9cNIDHtthELVl1J3LOEdKVv6xflILmOWKM7N66AC+CfuRhsoKtulW42yEkglTkF9+9Q6XcOVzOb8pCwnOFbWtZHBH1x6h9vsSKz1oajKxOSH0VJzNRJktXQMmpzmoAi5tC1rXljLe7FX2FpZ/eh6M6Db8QnXmx2dIFKWzmaehCd/4R/KP0iTsMPPVuPcHqmzFxUytthxsBWsPUNbEVMQWO5fo1LqG41q1MjHZ2k2/GltnvKWeVVu333azg7AjcHkuZN2aSh/a+/AAQnUDs9bP3c1z+5zh5cZVQljWQPh7DR9tNaLN2X3nuPnRFt5+0gVeOQjSLuZ7Yg/InPqB|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F681CE4C0F088010D5EC63BFC7|name:redhubiyno|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65gkNT7532CiiWotk99/LhDePxdQBKDhY4yPQdM7A0D5sXL6edy+fJsy94U++rK/KAsJUaSk8VmMuOW5/0dKV9UStevj5PiO2sLbg1HkEfJ+gqoE8tonr9wX7EWaPzKLK+RqnCAKrXTAOLgoEyvIP9FhDnu2qQWgywri8FNJ5/6ckk4NRKdIuDl4pw0AjKDK0ZDmvfC8jEo2gNsYm/1NyJoRwvgJzhSs8/Wniwr9ixIXRlwFj219yWJjqlMxskehkD/mB0rB3dC71bPFkMKjbNmK5fN2FE4t/R46WfEVyFviFHZ6BBdOm1tC+pIwMPfayjLRilbnuGShrCLqeCJU2RYESQNYHKXPJz8YdmpNu/nZ1/pnG/IIDjuSHWfIYBU5p8jR4oujSfJOovI8Hv+w7rpE1k5RQ+uSCzJP+IKti2STxdC6+D85fZdS6R9IGaEg45uiOIcZvq5Rjw/a/MSUqLhxC0rQ5hmYFmXzG5yo73ED|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F48535EA8B08DCF71EAEEC40BC|name:ioiusipnew|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ61CUTLffaxF9T6lt/oZogX0u6GWKUu3idIWsdzyZZ63e5jus/HPyGgMW9069gGK3bvmSvU3R5uLr340P2VrSoEPSpXQ3W3TDW1ofbhBYbOgmugqZdzADxxiXwB/rTrFUcwJJbdc0gbeIbUPQG54BS0T9aOZ4RIrcMBCkZt1z8/CIcLod7YapYsSQK6PhxBd2CcNwpghyRrwDLhTpCn2dkqi9/kU2VADGq9z+jw6nqTSgUeT0emkfnuvwHzc+YAVV87S+3P1jCC67xTJG42RouspZFstZeKOGVjVzJLGky5S6qeNFMg0w2K2rGawf5TK4LBbtuz0ykKh0YsllkztAFd3PygPb+Rer6C9faQwnUKfgVqFhziixwxKSVueobvEgLCDA8ecXJpamNO1ncpwiBBPwK5bS2fXLTgR4Cv7Wy0nfxGew8gBFlK3IMz62nl6Mhsj1RMKfXa06VzP0xOSjTdk4epe8Nd4a/zfgt9LafQA/|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etbhCQt1DknZFwh6I+tOHT5QyLsVVEMccC6D/xEnWnCyYsvz0rH403Qphk/DLbgFLE8hXuukvJc077YJWe27Im1tKKBKafOSidIx9KdZ54Cmv8wD3kWW+hNKvF1Xf59pryNRBl3/pgWo9Z4F878BI7uUox7bEep61XVeQsxTOtVdo37D2qg9J0w8dW00t9riNO2Jmbl9O8LTJIXHCluGtxJipkKvdlGcQ121FT3cXz0V0RijRoWTwx9R3EloYxMl+VrY3XP3AHFdJwk69JI09ryqU3SnQwWEkfRARa/sb6e3JCtXNG847XMakfaPS5exgp89m07N/3GgJxAlxsRtZQ0oHtNU5ZZzyFJUo/ZboO8PYbE4f6onTazFLfscS0pvHMyHXBoZoKeKPL29QKUb9EcDZxl+8dtQGcadKu5EzM1q5GJJ8BmqL3rS9vRuHnU+C+xOIcVKQEVOkHy8lG1UHeZW|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FA797A300A012B4FEF4EDA17C3|name:typefirdc|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ646BGSidmrWCCHLo6n9egQrKO6wOHOR+1Og5coLSSRLFON1lB0gIyBvjR8x0rT1QjjDKwUXQ13ggGDNrw2Bsr25x3h69s2uV/xp2t0dgPyhXRUURmbkqaG8fNbLgt1TsAyulgVbUlohoE5X4F79Eq6MWKAm103HlUiuI2GjJHgOBwg1vDlKGACKKvwIkeLgszLEWNXCeaIucE1vpy6yab5ekj12BV5k1vPe4ZxBkhdQmmOUq9mZeJ5LwYbdZIHAdSzfjdtXYP/W5vGnxvoO1M5vvzI2pDUaldcJ0R1iAEbGl3V/LsDpfnt5RAr8CORzhWA8B2MGOfDEbOZgttyn7IhqTVgAo0m65MIB/1NQ+EDqmiUTqcTPjqIqvs6f7HVLnChgyqUki7HQSKDb9ojyLPwM9qA2v6c6xvKdTRknsDIFK+BnO1hejyqBT7+P5ZGqCyxQKkv7sea7AXUau4vRRFhPUYOGp7C9v9IMrFcU+h8Qn|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95DC91960A3703A49EE5EFD64573|name:layoclhsip|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63wWDrvyp9CJ5SP6rHuDhZy8J0WJbyKWbDVjjMjOOy8LEB6MqEfJ5vLe5S9sImWhjbl1jn4aR2HsRC3/ZV1ANv6vqCh8SAGqd3IrWsUMGLiU9aes+Pub1l4z0HVMg++vYSK60IYAUlMEehiXdLXoSa5IDGQxZC/TVG44zAsxzqW7isP0TRu0GQqkgy5JFhYZ+WXFu2H91faUoAKvud+KxaWjB1EckJ0Q9AulxyaUplEtjZZQn/e81Rbjhhe0RL4UCF7LQGzOpDqqvsJWfxEDHp81kcw3p91VZiXPfNmL8S7VHUnfuaVr9XzFHTWfchr7sBPixtVE6de2wU8FuR9G4UIxu/B0+NPV44epp9CXFzIYbb15qH4MrPv6iO5LHi1bqs2Po3TnX/1oDFqyUgimZfUDRmfQglce+zU9XV11m5Yb3m758t6dgQh17XVj/6+7dPkEwDd88/xWlvRTnHiuNF4a9aWCZUkYsPj+d/jBmYO3|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95E5E7FF68B00183C9EA27C50689|name:kdhzbegget|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65hP9C+Op1nGRyvx2mWbDQOfcEFkzKFMKxZjUIY3PaEk+U2ngdgw99kUU527zb1+kD0/VVTjYcNmrYo18FSpAVUvueQbNCUMDAVzQ96cRR+FkOnfR9LmuAt8SMBiFGy3MGN0l4mF9tVIMuOAIflLE8XXQwCOz4U8JVDUUDQR1RqaNaqqGYPly1x4Kkkm6pdIDFexKYXQi5nI2d8NSN52TMUqlEgHay8wbtasLguwR4rIVR4biD5YzOT7+IzoCC13YlRuI17GEir+jl5X/yOKlvelPSv6umV5mr7C3EJJfzDhgx7hrURfJ71X9cINvXr89E62cXVP9Iy/uypitWrZJnY9O+yY7FtecAxZyC3x2lxr3cxEeafWDNPaPphLyq4sgTpOaxHW1DG1usInVjtBeRrlEOf64h24/1U8GtzNXO6MNetXJHPE5w8ixDeZmcZl73V/Tlk/bbR6xRuXb2e0aSOHoK6pJ19Nux3Tg4VRLYFv|vid:

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
