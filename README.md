local function get_console_safe(b)
  if not b or not b.getConsole then return nil end
  local c = b:getConsole()
  if not c or not c.contents then return nil end
  return c
end

-- Tambah delimiter TANPA clear; simpan id agar tahu start posisi scan
local function mark_delimiter()
  local b = (type(getBot)=="function") and getBot() or nil
  local c = get_console_safe(b)
  if not c then return end
  LAST_DELIM_ID = (LAST_DELIM_ID % 1e9) + 1
  c:append(("---malady-delim:%d---"):format(LAST_DELIM_ID))
  -- cari posisi delimiter di ujung, set LAST_SCAN_IDX
  local N = #c.contents
  LAST_SCAN_IDX = N
end

-- Scan hanya baris baru sejak LAST_SCAN_IDX; return (found, totalSecs, name)
local function scan_malady_since_delim()
  local b = (type(getBot)=="function") and getBot() or nil
  local c = get_console_safe(b)
  if not c then return false, 0, nil end

  local start = math.max(1, LAST_SCAN_IDX)
  local name, total
  for i = start, #c.contents do
    local line = c.contents[i]
    if type(line)=="string" and line:find("[Mm]alady:") then
      local nm = line:match("[Mm]alady:%s*([^!%(%[]+)")
      if nm then nm = nm:gsub("%s+$","") end
      local low  = line:lower()
      local inner = low:match("%(([^)]+)%)") or low
      local h = tonumber(inner:match("(%d+)%s*hour[s]?")) or 0
      local m = tonumber(inner:match("(%d+)%s*min[s]?"))  or 0
      local s = tonumber(inner:match("(%d+)%s*sec[s]?"))  or 0
      name  = nm
      total = h*3600 + m*60 + s
      -- temuan pertama sudah cukup; break cepat
      LAST_SCAN_IDX = i
      return true, total, name
    end
  end
  LAST_SCAN_IDX = #c.contents
  return false, 0, nil
end
scan_malady_since_delim()
