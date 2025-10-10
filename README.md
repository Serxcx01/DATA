--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D444EDF6F0B4E05F049F50F7AA014|name:wetwwjicy|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjIBaEm9aWiBXQHCW68W5vzG2V4PJL3BXkPoUcyp8/hdRBhCI1AeNF37OcQ0pbOSQLW1tMdmjHFX2GaSwr/Ic8Vk83IADlSvPuexyqaeek452JVfn/BLhcIemP1v8Uo7rtk9KN+ATZ3cugjkb5HPO/diIeSgdUkFJ8/e57cd8rv4+ZnEqrHl5oRxi3C1lAQWqIL+/rpMFNPtLccDchCTQ8w2RhxeaQJkHE0PvKzN7goOYrfS0PME2ysssyP4Sx2tIdfR0Iblgppr7x7xh7nRR1HxSPcnnYR9F5shN3geZ54ewaYWsSNEOCY/xLl41BjvyDBIuXfc55J9qAQmpGDELfPdUrt0JJxUwD4/3OmeDHLcX9/NE0Si8ruWzAeSb3oEONRBmieo8MymiHuj1QwCURulV6k9Ot4iM52TDvO+akSxDqMlHClN49mdcXeJwOlcrcv7LCH+DgL7GygB7vATxzpAHAJK5UazpT1DJWkhY0XDQ|vid:20F44A9E-4E9A-4CD7-939A-B5DE234BD9EB
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4455A410626500876A39AC4AA6B8|name:ynoatmap|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjB/b1rOmBqQ++fB6Q/Zn/47IumbDPYZbqmDaEtK5AhVy7FGlUih5HjI5CP5du6/HrH9sMYEIxfAPceAkv2O3067fL726cqKs9JoolFztnEcUO1a1lDCsSZtBtmEyo/O3MLQeK4a2PhKOOcpVCVqC7hBhELsJ/pbKPGTvokDCgYwMeDkoi8k7Yc4zRVrlZudL7Xg1NRAVnQQxqCvi5wegYF6HCLTVJbh3eS+sHt2g6YkWuolrnY7vq72AfQAbOPFxzyhpHVlLQBhyROLDXXX+jdl/WF47RB+LA+l6rTVSjmYxGbUnjrEBjpk4P5xGIAQp2eVzrTecrG8YZCnQEypy5IGuJ/6eE0qGlsGwDBeHykkOy4DSpYiOGR4HZDa+4JgYq+YrXc1VcXx8Uu8Bef+4Jb7wuTAZPMjGpcCRdDHUi/ZZei8CH+njOvtjcrW6sW3mNQhQ06R1CCUhwoN3Y0QIBTvHJ1FUnLbx/g+EkRglopBG|vid:BDED1A4E-3160-40C1-82B5-5297B3BA751B
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D444BF9E724A901A94E2CBF00192D|name:hardlsaown|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjL2LPdEipnxA3PwfbYx8pJUwJvbJuWdfAFhu06D3BK/Suwwa5Kp7dc7lFKQfq2N9UXserDu8ejAruHQdYudL2mljnZtsJxEwGPOmycWZnAWUHU/tqp95Xl33wADv7C1NvfATMPjplNsLCwuIsfFKvt2LS3RXFe5T4YuF3piEi5+ABIMOQ+EM3I80v6oBumciUn9SRu4t7U/HJnnElFqOOu1JibrEyF2w6YNHP2GjUczq/CbiwGUI280mRL5460q3VyuouMYz0YJqD+WO0KjDTu8JgqyB7o8K8tYsMtCn69RSRZUZPvDWuqU5HgrKxXFRbSI80rrX2WSHFcvGnEHreqjSXqMiXzvI59jIDd7KnpbT17tyyVcq7QQcOXqSdiezg5AWVdhn+R98U2b8Jui9VcRSO4ufnGBBSFors0VJRVUXVeZKmZAgDrjJqOqUX3DZbVq+mhB77QuUoyNYrpNrkPay89cpxsNaoQn06WoKDeg/|vid:62F5A40A-9F33-4229-B165-E4843268E8B6
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023D4450DB19371908EA4CF8E8605ADF|name:aoxspinday|cbits:1536|playerAge:25|token:U+e8XpHTuHQ724UKoGshjKgdxY3k8o9II0HAcWBovXDB3PFb6h2ZLeEEm9x+KlU+XJnjEbkZtX5hMXTwWts+z+fO+O5GbH4vNFfW06q8t7iq1nvDVX3dV2OBXFa7RDRsHLE9Mw/jYDLWvN3rARgYf4kXLPwRLsSrWT/Y05MLE4fmPEwO2cqOzoOLUYbXphQ6Y8vUxJDphYg6Ba9e4jRWN/pYtNkIjJicSTwRiLyrMDXkwsHpYLfR2THtIWIvlbE04SFoCc+XFtJcpdpTj5oadg+uS1cDLyeDJmmZS4YIjY4va9MpScqpJenjaaa2wG2uG8PNQwdd2dBz1rv2yvrqWOI3hZhGQD45Fa6fR4UPpLFIbO8ENdIj2JTj/J/c5eNDqU8XZ+1dHIQyTLXx8NI2uIkiFV8+9Hz1YllUtO2ExbdzABWUz1K1VBS5mm4A9v4ZubAqU3h8UCanG2pMZi2YaIubzpR9A7izP3gtlgddoom8xRLT3bGmzxImr2yhartT|vid:CC668BAE-8F8A-419B-A0CA-07F0A05A4B4F

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
