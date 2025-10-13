--- SC LOGIN ANDRE (versi diperbaiki & fleksibel)

local accounts = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC4C55FD8590971FD6F75947D53|name:rolagguy|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZFl1VhLLTb8YCzdgbUN4tr3exFsfSUYdit8e7v09u900JIJ4Ir5J0JkM6aso1D45rFLMpnDaS5sKeTx0CxgbMgr1/ngfF/d7Wnnv1KBgVyJRx7MuXoRF06tpEN/ku1H8jEG/psQ+QDT+vTjAp9h2IMIhHoeIjMQjKoJp72eG3695Mip7gQaB2jrhUXOE8Gtfj0A5nY+RNHRrZZiWaf8nnhKpH7O/gVz78NTxRMpxJIjclZxSxlcHJCz2pgktWPQONNmYqael5ZIamHJ+amu4/IELkJWpkgJsVxiNmijaBKosgNtCX6aWg+7M21fVo816OHYY1SqBIclMAVXEndqxhJbeolNL/DerJgqJRUHg2XeQbrWYaD/4F1ifFP8r8GTwNQvVuu6LD+1ThggCXfqTaFT/FLxq+soJI/UEaUc0OzWmUw+QpMQh/rvgp2P136V/zbzUsdOBkAe6ETqzvlOuCjomStyiuhVaE2NigtCoH6Tu|vid:A351B9B9-179E-4982-9836-B1247B13FE40
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC9B716827507D91A56990F34BC|name:wirynewwh|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZAs/KRsT6ZBGow6YN77LeXzHqlTNt9lVXV81Sfnnod2Fya3sN2o79+8dZV/Pl30mHq3HnGcO4idxHVe0fJUm9N5pEabV4l4+uamm1tOos9gocQs6rPFeglnNBOehqQqAPg1Y14UOPTFog65gXQ5kKrAoK1HuQwvZ9x3Mrtxj4gc6i/GwQEljarioDqBlPTU9fU04JxRJRHlfOQY1v2zBFmblq3Zmy/7UHKlvPKGZOWnsOK/0SuNwDWT9XlTARruXJlSqu2XFoQKSaWuy9x3rIckccfBWPkdmXC6zh5idvcHyp5X+z9uWpD8iSfrJHlwftQei2vcPTHmxacNmodVmj7VyBAXQvo5yhnUKid7AEV1RmqS5xyhSOoez7LZOUuktFcss6PUi2i0kOF8ompL7pcjuG6DCkx0HgVGI/fs4DOa7hrIRuWqTINg/mkevPgb47GfAPB3NmB2A9FPl1NKLtAcT9z3S0FJ5jESmK3myDB0b|vid:822E955F-4BD9-4AC0-8640-0FAABD4A53BA
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC77A325F7C0BD968A29E3563AD|name:baywetonz|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZMTRnBcQDCp7fAv+TTHTZgh4s8kQ7ZW76HghfHQfigSm69YPJOr/JnFllC3v7ia0US5pE1XZVAHW2SVboQfzl9sJwrEvbNaiXrVA0by1TwzvA0MYb5AVbQjbNgyNcK+r+K1jBxnT4aKqx5luEq/hcmPwV3yvpApjrDtF4l3cShN7ZcRSJxtkmd9pqvh/2N20qSjJotHgbUrSWlZQN0a8CiavPsrez7oj9BfWHGk+lyRhjYxvfLF8zjfOkRcTIspB4ZnFzSMakwNwoZ+fnK2MGKBdfnJNoGU9qr7zKD1jytfszEvWf9cyShhMFl5uKRTYivpY3HY2KPrQ3pRL+Te/eLpF3pR74bVpuotCKgkNPQNVlLmih+UWLz6lxat8yGI+asXHbpzYGp7k6CHxCfUYCRp14u4bntiWqUH7w/oby/8YpgqNrDDMs3PpjKLILw3f2wp+YNbEIASYzsv4xlTgFHdKyt+dpaRoWM0UtLRlp6zW|vid:EDC30AAB-E045-4AC3-9731-CD96663C02FD
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC7C86E30760518F215E17A8F15|name:zincsadred|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZMk75AKach5DNEtniwfZgCZBj+5LO2zrJgdTWaowRZjFDPsTwbwjF/l4CafD6V6OasZTK9nFqY+1hxO6Vyx3/UtRLUyXRdsnlphnP8d7lgIEm8h0aaCjSeJtreQpGBjO298EU0RzvRYNSNt/zi9wMvjursKF3ltpeeIr/N2nnmOokOA1Z8NSFFpUAJ+hgVejPVCmZh6CbhW6rVeMDLCKIz0eSLQuuDtVDRnguqFY5gz3+re9xcmITeusDvEZy88z8dmm1i71qBTSkPDc20h4RVHioLA2QJHWBbyXeDYnmt+9oOJUebHX3NuD0NJgXw58Sz3QbHqpXt5XnW232QNts/447CUlnh1DBb5R6UHFwJSER87hnxsxCYoCZ14RZG6oizYtZfJUy8UIQVtNYyZCZmh2Avo8VsN3eGvns2qBBH13yHkXyEfSutgfXj1kXLAFCW01lS8P6Gsji2My0skYFwX9+oo5DaQgYqVhqQDD27LD|vid:AD2B15AF-EBC8-4168-BA07-587AC403BE24
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ACC4EB94C500A98E344267930C6|name:avebigman|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZN4zk70WU4NS1l8ChtkYPqVsaYBbA/a0TsiI8APyXjjVLuODiqdWrAz06FKLG7C/jrVn4sqhCZ7KN2yt1aRr2LPf96kwF+lR/+AxYm1rxJuXCFQMnInov72YGE+4c3k8fI5p7ysyjWWNSGc/W01DHbnNM2gD3Bxg5kH383buLqFMbH1LA2IxJoVoUzIideCPFr6v0WnGKDbvyKyZHDK5c4rOM3hfHPE7O/vbRHj5N7YM+SX3x6bsdrQoxbhozY/PeXBbweCvS+jqz8Et3A3o1Wg2/GZBdbfKSwsG/rWURAHErgbXDEP3/RGb2UMbu0G1mE8Bb5f0BrLHYZXWgb2kZbTpfx9ezF/vytS7qHF9LZIheB5LKRqWC1f85N6/SDM3g+I35JPMJEt9q5+1xd10t6TXNh+rc2k9T+kaJRKNf4vLXbuz1EEsFBSZHEXPwAp6cWGkAY5hj4uiHElMF3DBl9ogeoc9y8bS/airlohUPiU9|vid:27A8DEFC-C555-4B7C-A9E7-397BFE83FFAF
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412ACA619579EA0B10DFD6E6FE0912|name:nailcpwtap|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZCA345CI5nHcBLg2nfvg9BqfwezXG2PWXfsynyfYROXTRJwIKokFD8Xi7n4mJk0cP5ZchcMJdxXmalyCgNG45Y4XnVtSRktOzWJtRJQvTYrr2vpQy5oiWip8FgxzUdg0EK0SAOJxvBQt2YEl7Dy77+AwBmwUi6vo6LFR2ItPix0/SfQG+EM4vmZXGSqpd2ysdaNwFiF7etsgXZZ0EyKwx96laHCEuJmp6utDxjHPZy/QSujTK9RP7Ye7j3XDv9A/d3BRoIH2zvUew2ZKD0K12aps5Cg+U4J6zFk8FJki9fJ4sNCVKd+jnbRe4kCVKcbjfKq+3skqc5lO6rjw1zJnk27f/4a3utQ7dPGSSUn0vUNgKZyd8btqvbUaVyQSfDrYqVwUD6CJ8Y/Kl4Hu7OW7A4cMXjSeK7mOECxeCZ0WcUkUm6rmYIUqv/XydbWoDPrMpyph4kMSPQYWC6sUlosIPloBPfKUU5jCFDKsqiuYTLZo|vid:00FC2B98-8A95-4919-A15D-10BE33220AF0
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC670F92DA1021D1FA78DE9CEDE|name:castzippr|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZOUdTJhM5aJbUgsoDP1ijvhyFhKLJrw1KD3sHg/P3pMIlbWmvhpmhOdUz6NllsqOEmgufSqOI718tjH4Yx51eR8GtAzXojfpPqrfuFoO0TO7JFizhcpymoQoNgC8//p64tqfHipG4lDBkqQVDxRwkEYN9/dL8AHf91qP78PVYZYlXVtzL+fkFqdRXVopvzqU7aYZm1Bb+B4OOwznj9HZmlJHTOossKrwODHfv4vANbNR6VHALrHY9X52DcY+6CMdZGjZr3V1xfDCc1RKYrxdWDWv8KzLCq9NclkTUSfnXK8rruqkUh/uOaP5LSty8JozTK1kHlM5ScqZg9cGnvqsDwLPVdd40HnyloI53pHMiw3BLdT1z3l6l5m41G+4jx1Q1Y+nJifgjrzrgvW0piLb9+Jqmv8EEdxa6bb5VT092yfxqx6Ci4s6fQLtI2jPsn5HgHnTnV7LSRrh9xeG0//WdSA0+0WB4hQVHR1c6jHzgSDi|vid:7CBAEE5B-00D7-4164-8AE9-C85ED1462728
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:02412AC563A0264F02BBC5AF96E94EF1|name:yplcampwry|cbits:1536|playerAge:25|token:yi0QwIJvcHmEaSzqI1wSZLus0F6uVKdead4SGsyXtNAw6zHmW1zMZ4OJ/WeosRdb1sjj2SkX98+H6bPSHqqbUzbzjJKiLmRkUky24+uICur2CQVVo+3gAKtKix/svWTs1DbBaSBWzCh2v+Ghq+2Ovjwg4t7zWEavosGnfNAuyWX6EoVFz+aYUWF0XY0W17AMZ5UUB/jVKb5Vg3dJR75hNXIma8wfcYDXWXLMxgb471fTn7IPUm+Tkx+/B6fuBGvge/1VKKHngFenTS9kprn7my0N+fsVw3Xh++7VNl7uugAj9plMQ/pxB4DJRtvjiM3/YAscv+icVb/AAT6OGjDwaocNpSFEE2eRzjuFgO8nt+Du8zIOnt5NLTjj4jvEVJJTNrSR4J6vVNhTvvuVcfW/8eM4WwZb9NEL7uZaNYYYDhlzP+qlsMtlvL14CyLyJCh7DSTn4AdvJ62ZOftG7MDnbIEZVQU2lGo/rzVDlhhce1qzt+vwPumXvTOyDLoSGvcb|vid:459D1D4C-7BBC-498A-87EE-7D1252B96CC8

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
