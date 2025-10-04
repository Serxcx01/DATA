-- sumber karakter
local LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local DIGITS  = "0123456789"
local BOTH    = LETTERS .. DIGITS

function Zeerandomlist(zee, w)
  local src = w and BOTH or LETTERS
  local out = {}
  for i = 1, zee do
    local k = math.random(#src)
    out[i] = src:sub(k, k)
  end
  return table.concat(out) -- sudah uppercase dari sumber
end

print(Zeerandomlist(4, true))
