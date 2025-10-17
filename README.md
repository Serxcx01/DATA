-- Util aman ambil console
local function get_console_safe(b)
  if not b or not b.getConsole then return nil end
  local c = b:getConsole()
  if not c or not c.contents then return nil end
  return c
end

-- "Clear" console dengan cara aman (fallback kalau nggak ada API clear)
function clearConsole()
  local b = (type(getBot)=="function") and getBot() or nil
  if not b then return false, "no_bot" end

  local c = get_console_safe(b)
  if not c then return false, "no_console" end

  -- kalau ada method clear, pakai itu; kalau tidak, push delimiter 1x
  if c.clear then
    pcall(function() c:clear() end)
  else
    c:append("--- status-delimiter ---")
  end
  return true
end

-- Cari baris yang memuat "Status:" dengan guard lengkap
function findStatus()
  local b = (type(getBot)=="function") and getBot() or nil
  if not b or not (b.status == BotStatus.online or b.status == 1) then
    return false
  end
  local c = get_console_safe(b)
  if not c then return false end

  for _, line in pairs(c.contents) do
    if type(line)=="string" and line:find("Status:") then
      return true
    end
  end
  return false
end

-- Parser waktu yang fleksibel (hour(s)/min(s)/sec(s), case-insensitive)
local function parse_time_triplet(s)
  s = (s or ""):lower()
  -- ambil isi dalam kurung kalau ada; kalau tidak, pakai string penuh
  local inner = s:match("%(([^)]+)%)") or s
  local h = tonumber(inner:match("(%d+)%s*hour[s]?")) or 0
  local m = tonumber(inner:match("(%d+)%s*min[s]?"))  or 0
  local sec = tonumber(inner:match("(%d+)%s*sec[s]?")) or 0
  return h, m, sec
end

-- Cek malady (true, totalSecs, name) atau (false, 0, nil)
function checkMalady()
  local b = (type(getBot)=="function") and getBot() or nil
  if not b or not b.isInWorld or not b:isInWorld()
     or not (b.status == BotStatus.online or b.status == 1) then
    return false, 0, nil
  end

  -- bersihkan / delimiter supaya baris baru gampang dibedakan
  clearConsole()
  sleep(200)

  if b.say then b:say("/status") end

  -- beri waktu log masuk (1–1.5s biasanya cukup)
  sleep(1200)

  if type(findStatus)=="function" and findStatus() then
    local c = get_console_safe(b)
    if not c then return false, 0, nil end

    for _, line in pairs(c.contents) do
      if type(line)=="string" and line:lower():find("malady:") then
        local name = line:match("[Mm]alady:%s*([^!%(%[]+)")
        if name then name = name:gsub("%s+$","") end

        local h, m, s = parse_time_triplet(line)
        local total = h*3600 + m*60 + s

        print(("Malady: %s. Time Left: %d hours, %d mins, %d secs")
          :format(name or "None", h, m, s))

        return true, total, name
      end
    end
  end

  return false, 0, nil
end


checkMalady()
