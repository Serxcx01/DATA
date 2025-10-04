-- sumber karakter
local LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local DIGITS  = "0123456789"
local BOTH    = LETTERS .. DIGITS

local function random_kata(len, mix)
  local src = mix and BOTH or LETTERS
  local out = {}
  for i = 1, (len or 0) do
    local k = math.random(#src)
    out[i] = src:sub(k, k)
  end
  return table.concat(out)
end

RANDOM_WORLD_AFTER_CHANGE_WORLD = true
JUMLAH_RANDOM_WORLD = 10
function _random_world_list()
  if not RANDOM_WORLD_AFTER_CHANGE_WORLD then return end
  local n = tonumber(JUMLAH_RANDOM_WORLD) or 0
  for _ = 1, math.max(0, n) do
    local wr = random_kata(4, true)
    -- WARP_WORLD(wr) ; sleep(100)
    -- SMART_RECONNECT(wr) ; sleep(100)
    print(wr)
  end
end
