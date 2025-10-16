--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABE67E5B079083FDF28477597B6|name:wabeanbox|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZMSW8T0at9zoM1N08SqhBbTJKYIkrPlyKM1lUz775rmkqNEv+RlxT8GWHKFujHVcR7taLv3a7L7SSqAxv19okO9DNE9WdInvumDg9bsGSGFTYcS5bXFsc2pRcCHheFx3ipmTzK5x28kN26PsZPHmohNJ5FWszArN41CCD/0zlTqHlbrLx1+USYae+BpZJoJ6RX27Qcun2tS+xg/LsJbeyRuvPR8x5SAo5W6dGdNpKjw891VJsNXjWIui+bnfgdq2lIzThP9LzabRhqEgci1nWiPxiiOayphpeKAbjM3GXfGf6hfLRx1tdFHRpLdAzGNv7P4kRlKV49tCgnmk/SH3n7wofM6BIF+uP5RJkE3YrNb+Nwmj4MFre+beFwbLzGVJC3R94PuR5eWWewT0TaCBMrY+tTFJnMSV08DCnyGfeltYHbjYqKAg7aOA5SG7BGlQFv8YkaD+cxiv/JzeuWeXJKEspOVYKVPrYb7j13Llttm8|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABC56CA6DCD08EB0A8D836D77A0|name:slowedwet|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZKYaNGoayjOE8Fk5DF4xTTcPoBLZZow4zsQixOPtl0ps364Os4/ohm6S2OuzfUhITKdT9WadIu89HuFoHWgYD+yZiXtxYkoSn4X2GFRrSby2ouW0YD0a6U0xJH1t6+IMjzTCFCB+UMVddg5h+ffYfm3iTZ8CWRoVIVfbpisqFCnrtXHuKZKWYbxFxZqEYV8q8ZJDiNo5MFfGiK80aknpn5I0zY2a4pCuBnouDqYxxK7RKNAiRwVJEnLfRr7ly/4PxJbclmKGPgxg7tAVzypHEN2ucyF7R3ZlyM/md+CBWXTzDxGtTUKw1Cw6cIaCrsXh2pMY/H8oflcenuXTnHAZDpihrBzWCz1bdn02WGjvIEqr3YSzeyk336zzhGq5B4FIU8R/pfpiBlkTmaTSBg2VVIiC/R4nsnuCTipc64XWwp/H4PRNMyswuH5zXybvyOg+IMhDph0QlhtH4wGrvEexLJa+JihdPVik0Rd7520EZm9Z|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC1D948AE2C08E48D0D95659920|name:dmlniceshy|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZJPUrxLzxZFzsyGrXlPf7GdfZKiu8cKBTHhRJXkCteKC0YKe2X2n5V0kbphD2MFxiHZuXQRQFP21PLbd5X7euzzaFrNyo8v36Lv4h8A8Nlj3EqfsZL1TrZHbh7NZw+DUIdm+G3o91PkF0rGbZ4l1Sh7M2FRaEEend5PDRjiz4li3Gg3JmIyz5MbChBHdpPy9z9O+GcdXK8qz7qiKtGD8fhoIhErRO/BgSO85oEngKM/15WhWFZCe8JPTdevjnbCukiyUsCWxJfQUxGi538B2dAO5RFWV8wnYcKLPcu7yinwoAPnWi3kbBYf/ntLf8NbsZcA2anTdxh4lZndbOjBb5mpveSEMb+NtzrqSxipsUiAChpL4B8P1mwvuFdVU8wajZcx2HQnWS5sFlnp4kiU8QKLkRVuJu6iZ8ONoMxIASr/8cZ1DXIiIerxxq7FUG1XnFu7pMYJfnXtBYoFKvTLIpV4wbpeAMDJHn4cOST959oB1|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABD62D3413C07BE6D41A1C96691|name:nbtgskycod|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZFpdMD8oZZn8eJCuooaBSmgaxt1J9FDJ0wpNdQWrRVOVwUeMmt2AeYIDGmrCyvtUy4TE0vx5Js+W5h0KMZf2jU2bzhXw5g84M57NwdMSMg4x2dWqEpqVpWcTqkuNlPPyLzQtJwOoMTs7sxwRYCgyTmEZhX2DudN/lk+uacPZbEs/MbxH9pwM2vm716bP0p3Ab/9KHGcPos2YBgK/nchXzF/Gs9uwJkZoVy1UzjrwDHsFTvMJmvZByNEpJ1c8OmM+juMXzUhpFHTkUTpvykWzYPYTnnenQDo4ChBbqak5oAye0BimUWIFbI9gIzBzmae1qZ/Wd5eDODRTP3XGVjue7V7N9qQnJetwKCLiSBTvsmbp0b8TxKecsCvjXhBZTfyWbJpGBMdoqdiACdRCaEGeeIcoRYBz1do+QTvFICmxXdAS+gUUe3K4+0pr34t2vp3p/qE6pTTrUwFjV6PUDjUIQalgx03O9eNHFD0X9I17vLsg|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC00563B5EE09A03B36C2BAECC9|name:ovalgfdry|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZISh0a7468XlxdyoooNv3Q96yFrCdfdoTClsoBjfib22qJIw7cXMHxwrxOexzjwm+5pDtSUVN6UibniQm8Nkc0fzzksPIvkbf6ZqkgOZQPRrGzshHMVpVkc1fDiimNCRz4nmSrQl3FAAZ36/n4VrGKRTtoQUYF1UWdY/mY5YcwUcvehwwjU94xjdSqWcu836d4rupcEYfEcnsgjJ5vlO8zwjkXG5kqs4AqMf+CQzOPnwGVK57iShN3BLmYBnGkXfcTLs0ti/rlyQvTK3HrL1X3yzG9yNUtm6pUwf5ZMKJTUcfkHxSdVYNeQkqVE6/P2yHBSYE0ZjeeLMqcmni682O67lo9DH3W8+G+lksOC648VmxB8CMWWmDDRRLIqh88R4/LvAgvQyZVziBCXPe3aIirl2h4XoCYrPWLz4BdAPlg9LI1f2ojI88JBMzdVd/4Dvf+Jv4msXx22zR85dE3OP2Bph5elu8s/l27mzU1jSecL1|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABE63C2A7BC067B7E5B1731277E|name:qbklateset|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZB7zKdAkp7Ywxqj+gXBKoJ0yJgMjM9kFhUS8piNOZyrFF0/nKZ3anj+KwSe4TN2HpX1upteUM8NMAoQuQHM8afXUgOPo+N1QypRPL7t1Yre0N3kb/9CoCxfAyw6eJ3ImZAmM09CeQFNNswWGsnBJbcDdouuPMCbcq10AH8RidzMp/63RxwV2hSduUQH4SwXQEpScX6SrZ1IznYgoo+zSYkAOmvz3UuSivtLDh7GJPI7AWH6afFtJZyEpDgEAmWD7kvG7/SVH4QtmBXFiOkPHv61/NPVVV+xk5H88iiLoMvva6t4n2/teJp6WgwM/xedEr7ApDzx26riH/2MzG2dQi7xNR5SAP6TgFupkz4dFXS/2poz5H7op0H7p8VzN8ZL6TNIAhW/28ehdWytv08nE2FL6Lduo2/2tvWpzoeW0f7jvqr5WM0M0WPAQfhXNxLmb4bBabM+1swWjpKCgXwi2B78LrE7SUShzXryhApu/FTBb|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC1ED8BF5070530EFA8B116A7FE|name:ngripejet|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZL2lU/HguIoVz24+JXcX7cHEgOFxXUb2HgGxqTZT4Or6OyLT9hkDTKHqyb5gH0G/zRIUaYnVPEXJAzF0wH9kMhVurNs5RaEt5DYEbXWviUHwAA62fHNTjzj+dvLZ1lC3MHKdlakj/7C4os4oQ0SJqBsp0KiyGqgw7JKcdhQaBFjuugbKa0B74IX8IhMinu8S7/9sgJbWlJIazsRAt7e4qfoeNoigV5mUjKCwr9dLVq4Wayvvzv/mFmSdl5kypcaNyLNBx2kgMKzGjCPF7F9goekKzuJIxEdTuEQAMGbjBMESVBv1VKT0hJzEgg7Nx3oO6OlgmqtqpxRTAExErAAup0hv0dreVo0543VU6B2xwOz5dUqsJohaIv+D0vwX3z5CWLauwm/87bdKZfOLLtNxp+ZYZMInlJE51/ta+edWqzYc9EdVW7RZjZOGm3YLGXy9ApuBax0YKhm+MyZrp1AUXIPIL1E9BcliTeVk1VQybvP5|vid:
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ABC4248AA630273AFB0DF4B522C|name:workspyabf|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZI4FEJasxwvtrY3sJxwlp19JD7pUKITqBpSA06hqm12khqGRQQNKdyV9EGbgYUJa2ByQ88KMh7BBTj/W2/jBPfUXDKM7pNwf62FcD53ymBE5sPiN/sPn+L7Ezs0ZDim5XZRBMFURsjbO9XFzJvERhBp8A/kyiNjz278+DmQOmOSv+rtRdyKL5HiFK2GC1J1UgEYXUWZ43+ifgH8ePD2Xr6StxbbNCd4K81/tkqFBUpxLYNtnVGCj6DC0xjpprZ/t1+NPqaTAmyoI0yUnVouB2nv2rVy3wDBM0Z+DBLBmGe4sNhpIaWWzYSQHDFxo/+3jrpK8kOJYAgu4jzwieeH9g2dVNIMrVICicle7CI0fJGLEMd4IlPRvSP0wXOkWfGe6diuKa+So9gxumPtm2hgKGh8EOU2gte1KYRKg6Kzl7j0YDTSn/k+rQcCkdFBFfhRyndH84f4WwC+UBwrtvLOiSfQWGnOHRt3jikTTZXrZC51E|vid:

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
