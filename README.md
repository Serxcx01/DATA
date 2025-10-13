--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF22DD5087A00151E075B3477FA1|name:mixwinoqfn|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtIXUFS4pawHEsKXddt9EKF8SOVVtQeXqSmYSGHhOKh8axcZelK4tPujJT2F/XLkkbBZZt7XJLO6rZRRDVirTLvvnEuVonOQ/JQc4wgRip4LxTH+sV7E/cIl3yD7wjy3ZlNi1h0FFfhPZnCEvi+mYgvbuGefJBG88gyPXlwHHe89PYKdlNQUW8dxBeyAPjL5gQ4vwB7VRdwlgHFe/AHt6mjzRY30osh/NADe2lLte23UyPvFWSo/aX2/Owsj6eAxNiqHr1emV5dFJ/MIq1IGTIHBdXwhGGQb28cnPqHewkBox8UYWS7ayt5sTsDuWdI6WX4mucVmL6cwcZ0Vf+IBuiq7CPIdAAQFhjx6mTvtOO0Qd8x0BrJE7SKltAe6aX1xSkprlH6eQztXxEdjZuzZTNlQ8mjiNRGwY1CxMDEtnHg6Q0KaqB9NcewlL28++uPFqgTuGCBpd5OQjXYgobMWrBFtmyge3Sgc/pLH/KRwDt78g|vid:8291D983-B026-4E1B-9C7F-D887B5413AC1
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF27D8C1FCD903BBF167A2B83C78|name:ckamisscow|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtOyNfVkbbKpUL3FFRM0s2uaK3iWN8CsjQVWYM4Syyl9C4ieTocXKCahaRAFkjlbiJfXlgi5DZ3Y7vxbFaIh86foaqVn1ZG+ys7AQlbJHShze5IfGD4Uo3fFZLQSSxsIXg4j4ATqtyh+YeEkcZe9H2CK5TVsa+iY2ILYz6c90eRSBC3ClE9sRtrL6ioR8pbLYJk5/qmFTWvL5ZrDa6266GQlJwO9xZAgKPrkryVheRlVjYbx7uQlw5uq1UVivixGdD/cctnLTivX/neB86c7CoZWjCIh722zile6YQCI4LZiPmUEsBBU7P/IOVeSpa6W4Epyn4ZshcBnasVi9POwWKtpReUkJkNpy4v4DKDlnhgOp+22LSB98u3gD7YJSJvhF1THnpj99AU9zVrb0v88L3J9hlMOGCtOiZYeQLG7ohW0W9rfuLanFilfXLbGdcTWWtqoBFu7MjHhdDx3tBdTNlfyb7c0TVxYqPBjjUCE8nBc2|vid:44C9678F-7343-463F-A211-45AC5219141A
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF112CAC72180837F34C1E3EB20A|name:burneffly|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtHXN+izVmRPwKqFm+eMghrY+9wd8odJVr+VwRfG6XSN7k5jtmd2ipLGiojAGIikVGSJVtsDFZfT48lwiGPQozkNo5SM2kPcTe6sOuK45yVur+pALJ7pKYj/bBHUTcrqlQCSVZeFAwBDOd9L+4L7nN9gmCOYjEdUYrKC/TXmWFtrHQSeonJSjUUuMdmso6KgFZAZGjrXbVh8d+Yw8KDK1Bu2zNcyBA8vBALViQjKS8umHjkkKGMx6KclGRF+Qsa5EURJhHARahn0qy7MaGYBczPd9qZvlX4P3o+q+by6xVvB9XauutqcxKehjzSjQIELqr1k5UxUsuKQH5BPOhsQ8ZFTPRiFvjvrls8Nh0zoSeQ4JrdKOWojrlhnNI6+4DX5GrkDiN46G2CFHHAzw7uQ+pV8daDZjEs83ghxLDwFdpkNZVkxtgFwlOp1fFArk+FPsHFMDByuV+I2XdKgX7SHh8e7ETlRSSKZmr0VGOUFWrIS/|vid:D84E0E28-E7BC-44B1-8BF3-2C5ED96124FE
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF235D14ECBB0533020D18CE2687|name:csfoolbig|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtEVxG+1x5/YfCgQQ09qq3k/NVw7H2n+Id6gZshGqHBER5kpctRavfm9sPI7qdqRYyCHYIrsmItpJzy2Zjd7NinvpQkBSasSzMSn/Xw3alnWiFlANl4hwpbBbR1HWU6j8V+/nUBla5BZpFlccmhhD21sGmLHel9BADtuQFNe2vyGF2bdQmNOUlVibF9zFMriOcEv/SNFLh42cfpBzjG7gBMOPNvZcNCMxhdI4ETiR7JeUNGsx0c/hFIpHiRrlQwPX8bqX8pCf9R4a4DgPmTw1h7ZNX6ig8ZnHmOayjieTSKtWT6eNl50+W41F5lOf+2VFgfrmfAXMHvz5UEhJ8nrmOSrF8cy4kvufK8kLOkDX4Xzz+ZMG9vZgmvSvMQ5T53JsBZ5H3Zh1nrRADWKxgWgt+65o6EuByMYaPFE3LSFSUzwSaK1QD0pDX5qRfSgmDFj4BJjF0lPPvAa5NLk+SgYgLJbh0SqiCjcTtsUIImUJMWa8|vid:88FEA80F-D959-43E3-BAFA-0C52050C9BDE
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF2187A9480E0AB2F09BA1FF54F6|name:addgliblay|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtKjkTGa1NdoBQrDeG7xN++ev3pjt0mSrApaeCIKvC1KZh3SD9hcU7+rr6XQ0BKgC/qe0sceoyFVQMqQ/vDqNpzCCb29i1p5UVwsjdrdvWhB2xE4uuC3UX+3aRF9BwnbD+FV4N9q7kZj+sFG+a/z0fKHgyuo57SlydI1LQDy2wDjCHoDIWaoc7SW0Ks/0mwso69J6oM9lG8QN4PrvF81ucsBaj6DBBLn6HEa2UubMNFKTXy1Gwb7ZoCwzyTsSgxZCIo4o+xyQ84DOOZZfA0JUdTvlAlD4ypT/FOtCK4xkXdzs6yoC0riZehd5M+NyIuDY8pULyTL4NgniZBHFX3ps0NgPwc85DIED410gYPGtOmp+kyjz9qLnVOuaHXcyM2qpjQlQ4eQnKHdZ8gzH2EdTHMmSwSrzuJfoam/Fm3G+R53xlqbLxCzgl+aXAP030do63d4XIfSBe5tAN1c6TOHMWyW2NtGGgzwP+DTv4C5Z//r0|vid:EFADA78A-1A6A-4538-A44F-2102B6D2346C
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF2981A80BFC03BFB33345611BC0|name:waitdigfve|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtACPeg3yL5GtVIQ5u4YyFpNuhPmVtUxKXf4V2+9gBs36njSnaLfdxLizZe6seyXyHGpV0G0PefO/WQ1t7yjMdpun3bt7rNbQlorvgOT90EhzVXaLGC1yza7XtcaNmckb5RYnzjeMoZkI/FM/bM1odxUZ8TzSijeWfBBWxwuZTxce6EiaKnFj7KI7KhSDLPhMqvDznO0+kkqz6ShZJaS+XTRvWdR7sHPAuXdzPC7NXJCxe7N/rhh3svJQ2MeuEYlKAGA2xZw4ilUYIY+3Y3JoNSGkb9jo5cFp+pUPlebd5N+q8Jiwkbd7RgieROGr6RFXvnYYPDAsj7bt0M9Xia2dBMsbw0ASQ5j1Gmyi6e64vDGTW508SG9p8ocTZ4Nyr8cKV2pnfiID3cF5M/VPQXXge7qLZBerjBZQ2QK33+IO3LIWARB1uFBVSzZPtXs6ntQAk8jBIgrqw9bOJ44at7TsU5Vm8nVlBV1I+gEZhqImd5ny|vid:4C67B17C-6239-4AFE-A567-17AA3F44CFEA
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF264998C37B027E01FA4E0A96DA|name:gunjrwet|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtL0btfIvRgpWQ5uFDFQlJ1NQkm0rERmoHmTdjrPbZ8hfg6uSpeQAjsoMxzVJ8R7WLQuXbHMt4rDYWih7WtyNQEbaZHd7Z3lLPOKyPb/L4DRyzOQTbYxqkUmH9DB1O52qfEbYm/80ms/CH7t9a4Q552KwLbr/AAMGrhQb8AM5Yup/b10FGqG91L+u7KbgVOMwkdsNIBgw+9vx1dncLorxK4HkCL3ZFx5GYm7GywJj3WjWAsM+2aHnx03KkPVVC+34tfhE3Vfyf8AzXg70Damm+iJ2pszUrSzBXFSV+4p+TZC5/mfh7ydpPqDpSnDt85oaQQLj0UWs1juGOI8fVCjoCsQfM8bLfMnFNWdmt7yWzaFvwNNzTj3wAuIcYA71JxerkKqv+g3E6IcCtJAhHLzT8+kK7qm2v58rXV+dTKoBDJM1nmX8p57KkY9G1orTcWPnYP+aPRR/gQpgbR2/p4WVq/DB90Dbb9UlOkRsCVJYiUxA|vid:924F9C86-62EF-4396-82FB-C251EE231F6E
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023FAF267DCE3BF0073767CDD3B8967E|name:funcyaaim|cbits:1536|playerAge:25|token:TEthYA4Dg/3Yy5XL4GGrtB378gEiW2VFvwIo/lj2g2uOveJ4VFrz/WVnMFNPVNcZfadjtceLcCVBJzlaxfwDVxPjcye0CGHNsuBKpxiCQnL++ZFzo79D9BP22gv1XGrKhDArfUCJ6nM7fi3XiV8Sx0BXhPU7RzdxAD4Ma8Su3Rd/drs03v+7RhRv8DDa4nc5psQYw9ftX98Iy+bBb+ZRBJlUayweaYBnNdvdayHZpFO9hiPJZ2HkXPZYrPUum21ry1GXzp5kwcv+97DKhAtAqGIR+LExpINJy2DgIXRYq2verss8ytM25+D8UBjqtLRDIxwjBiFKjKLtebK+JxNyUOFM7GM4mL2SBUxsnM/Aoo0M6oxt/0o+fP/bZRLHtJAu/66PL4wiVZvls6UHkRZ1MR32vIPU/Br/rclUGkS3UaCvdO9zfrBYeDGME5i8Ga/PPvvSkRYn77qzUctxVvFEUNqeWwozScwFEd1ExGS2NP80txxzvNru2rsOvKiy1YQy|vid:FA81DB4C-4E61-4868-8417-42174F3A84EB

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
