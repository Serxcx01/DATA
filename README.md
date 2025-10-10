--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)
-- mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F1C83AA04A01005AE2EF0B375A|name:icydewkabn|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65nkwTjaPqSk0DNgoAND5w7R4VvNvl/IPChVqZFddc1WNdpCTMgvfvrdH01FQcBLCFIk2zwvWCDSol3WSWobA4PKRaoZq9u6ntZVCYdjAXQeMfIEiJnqmcnGVaahfi46p2xy+hybRJBdXnZ0zUa1JtHkUxh9hQpIOfGQpkNHfe53kH7OLOTjpPKhB4VzSJc2k5AN18LpTXOzq/axa2QwwRxcO+7I8LBfdWi6PVVUu2SvE639EBjdyNflgWmaBOTZyHF8JzGJJG2KsSkQ41I9LWzGJUbGXlf5CA57ulyNBgze3QMl8cHC2w8Ag78TiSQcw2O4y9fhifmeQ9N928NygMHzXFtWZ1H/nXbaoR1OKprV4cCE1hyTLSyqIVAYXp3/T/Is9SYce14/wNqvVFegKEDdaXHFda0VM6RXnqglEfXbN1iwRXMkZoynP0B6Uld4UZ/SN9e4WdVWwtJi0UHsWSPmwGgl8xw0gWgp6HilgleD|vid:24C059E7-7CC8-4833-874D-660A4AE312AC

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95EBE2A534C002B3234D807B5913|name:combsadrs|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63z6DUSbWX/eB2JAjCyixhWeccQa450qJfGGXn+3fUKY0qqvUFA57ewA62Zt2Q7aKi8cdK0Cqr/d2HfXPBNh2s3ytrsRNjXDIbVnlhZ18wCzdyhUOn1cvZggvUlpRNzN3qU8wRJcrDYwR0KlwQvB5GyXHIRCq2TLq7XzJpekN0qpyQSqvrn1tjaD2kszQPOzeShHa0mJG7BPjI+dYzf+v/2f6Z/mf5dJIKkH/X2UgcpArILAJJfxlrtO8Lsl/eB6gPuePiHQNufvU0SiE9Woou6qAoSC1K+SWW5gsQx0OK11BcZQWJVQxgBjg1oZdYY+X3ZJWp8FqC1sXsZ4stiH739X2JLVHyf04EEhSgc2lGkulb+iYrT4GkPGopT838WiUoXWn5mNRuTAo7IY+1y2HKNqOD25B/7Fn27ZWn7GqZnBFFlsiqNwRx1LzWgNZh+HMlQivbBU7mpRyjcXPS3DUMQdWzTJ6T/jFaHgi39RIUF2|vid:FE524324-2C8F-491C-A5E2-3D0499CCC875
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F48535EA8B08DCF71EAEEC40BC|name:ioiusipnew|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ61CUTLffaxF9T6lt/oZogX1OXpOy+JMeIUSTFwUxB8aLJtnXC7+lRCMGTpgv6FfMvTJUdaWqJ8IEac8QBRk0gNb1ETqZ4xfiquGZEhexeqcNipUhAovP0mu5SwKwiMbxX9h1zHGNx4bb8hNXPqY1gNW1nCQGx0bmjY090n4QqShyWdum/OJij9fTOhUNgIKFmfZ8enyAu3wuIkZG2aWvqs41fUshKhPmMmu4z5KBlDwKooMHOSo19CkZWG7j8uxN08MXHvBDMa0SXCtubyTsEA4Y/z5I7/H0OevR4QPRE/GlovWBKvhXR26F0/RtleHW3dqWyk5kH5alvSQ8mDdPxeDkvNDF0KVCnf5bCtXy/6lMb0GlneigFKw3Uv9BNqRIMonkwb8sKfzmneWYdd8CartUbNR6qjwcstbxobF+MM0Kk1O3YgScRzUvJK5sgzqHYpMEv++r4MYnGOcAguep05QEiH4vx8P4lr4Aq/utlU7S|vid:15901100-9F4F-4349-A5A8-0789A1F710C1
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F681CE4C0F088010D5EC63BFC7|name:redhubiyno|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65gkNT7532CiiWotk99/LhB5WlMehoVWA7cmU5OUiW/PzJlfaktu0GawljYsqOjmPYEFBSdXk2MifvCMkzJjN/dDlwnELgvct2saaC4osk9X64jh5co4EZmpQ8ybpxPZNp+8cSYfihYKeiBEojjyLEIcOKtNGMp2Hgj0GuBxApP/h5aaaomQqs+LUDNUjZ5D9C9o96nRU/jF3zCpMk1ap36bwGmMBBL4HGou0XCQKXB8xYWhzU9S2PErNgulkbVtV3OYv1gVI3IxkiLqncq8f470kkGqnSZSOpHFA4XT+foWVU8V/I41l2a7ZXcMbDghT5JJgaZkXpOuuKkZxth/bIsbHSiIXF/qT6NgR3AoCQkXIoVpagGG2aw14EV/KRS0koFuKkIlPkBWKZ2GMvUrwtVhok/wNUCKqIb9I7/yuLVfwacfEA4TbjGLC1xyY1VCi4YlbyWMa4oNHvGK8IQMsSaN0cJn/UHgOIPe2cNPn+JK|vid:C648F777-D6A2-4244-8288-443653B02EC1
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F519CC03330552D006BDC4146C|name:meohatelox|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6yDi9xZXQSc8Tmqgbsn5etYBdZzsPY3DT3QCG5HvZteHbHqLdqaTZ/RD2BBTVXEbzTlXfPXYrSX2j46dubxkDHm6oR7wMqmSgNCVV/A4F5wS8eAWTbeQH7wd7BNZG3gQLx7E483cMCMw5Y1vZxK1siI2TdcFP50/Sheay8RS/3Qz26ZTc4oz9raC+TyY/64ayWcMWjS8p2X4xYCpGuoNITKaZZQ+7kuydcCMPM3Ke2Wyq0S+WjRijtDAz9UbE7PwKNXUfgCh3xtfmBL2QL8cpvb4HwsyJvGYgMPuDry7upwCoZxsjbe5PuHockZh8VQ+T9LAb47cqOHtb/YKgrmT59O58htyeZ7Wu2rNBTZCrZnkXdEGUsqp6VHpuQVjP0OM5711DKWzIE6psrsgKZ5LzlM+fH5U2aovHgxM9DLws0nCrO4V/Iq79WFFhn5mADH7Y8clSx3wG7MHjIb/boFxM+cAO9ocv/MhtbdECyt3sSZC|vid:0542F439-21F2-4CA6-9631-25044F372D6C
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FA797A300A012B4FEF4EDA17C3|name:typefirdc|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ646BGSidmrWCCHLo6n9egQpLCCIKw5WplS5v/8VmY3oxiX1dnGalYYsVR3EbeVH1jJ8+SHRQtnUCmQdqA5bkGmjcBpLzWaIS6An9hPvqrcV3uKWQQT+N33tWZ1cUlPP7ktvgpCCgHAYSo2FzLhCBDigaiMrk3VV90oVTZ1iWlwsfQg85s9ZbAks3nhYP0YDvAGBcnkCG0mI2CRk5YWGXAgVCAOl0pbwm4jeFTjXhEnZUoK12fvesAUHmk4y4AVbWiYzgNzBQCP67IHuwZn9YTD4YL8mkKzf7qQP3XVcSsB5528hOnh0QstNPTEpM+/l99gQPwVUrjBF4JdwNozfXh99C5o98PDmNhODi6XK2vWJp/iuY48TSS0zCjNB1mJqzNgSIRMWQDfOhDx/nmCUltEMNA7vC+ltDrSNFDipy6P1yVt2DESIPRWh0g9tT1mYMmZUtZ2WBC65HxG3zxFean1Xl7DmlPiSlM/LMwHEYSQFS|vid:C5B2DDF6-D1A2-4974-AEE9-CF688C8450E9
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95DC91960A3703A49EE5EFD64573|name:layoclhsip|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ63wWDrvyp9CJ5SP6rHuDhZxC2Szl7NxyfyodszqvHPuB+79uY6VDfhZ2XM8/t58So4xIff/cf1OEtzqEbMb+pl/4Hczc9TKryH1k4KIxyYyZ8sScBvvfppF6sS6Qs7lENpWiRPenIH2K3xgXP65Y8nv3qaX6x0B/i1GT5pRgfyzrUH7mXhX1V2CymQf6YNa1pks2vekrO/4BeHCIOhcQHdeJ2CB+SgtJ78+fcCPVQa3tDFohVzXApOkpZpUCSphBx8TNJ5n/DKaIPx3S0CI87A1ocpzEoOpyOCvcBjg+hfywL9hrYjumnq9AUIdHsmrrh3LB+zWad8gM7kGSVxWw61FNpkMnFzt5v6mO8bVrIjOidrXFcReou2gWN5lJOioY6oZ1Fjn5Ubs+qoBexf550sc3J4niTIW8Nuh1R6IAyfa3GVcPEdsHhZ5jgLydasVfeBnGJlHbTPDKzsygEuhQGRj5Z6JuwtAZLBb7tcFy/OfA|vid:D03BBA9E-3823-47A1-B7A0-E0A31FCFB892
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95FB9D4E9CE8083502FCAB4EBA68|name:deboarwet|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ6zoUhjFQo4FPfkz007UwCCkn7lS3OWE5r9c4QsEa1LFvZqTcOMVBfvXrZ0rmAG5qOlGjusDB/CX3nTsqQrc4j+26pgEu1nYLHMKdGGe6oT86OjO2aF7E9KTt037QPmQAUMQfE5JlGZOJ/3R3cWk9FeEfmFRbycpnk5XOMKjZ8321dbeRwME4q95CdmkjaOjFg7MSmmpFqqBZvX9itCVxccxQjgFvNLQ96jQ35sReaN5Aafmg1pSgs/JLcpNwCgc8nKhTppeMcKtn/3QONBY61tX7hxlFByo3DkxFLQzomBT/Arh2rYth87Vuz0Vr8vROZ6twGWFII6bvTjPmUrmGyeQF2rH7SoH1Pde32dOSzUt8LIxH4f67ee4l+3/2nMo7k3EQ3vkzSHCkvz5iDWyGIk05O4Z8c72w5NySKut9b3xYFW1hcTnpk1rvTU+Tnea/1OdxsHXuDwWnPP9zBJ0fetYhNX2oWl3uJwV6QWxVhbDX|vid:AC3F70D0-2180-4ED0-A727-094E1BA5687F


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
