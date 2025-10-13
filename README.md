local MALADY_CODES = {
  [1]  = "Torn Punching Muscle",
  [2]  = "Gem Cuts",
  [3]  = "Chicken Feet",
  [4]  = "Grumbleteeth",
  [5]  = "Broken Heart",
  [6]  = "Chaos Infection",
  [7]  = "Moldy Guts",
  [8]  = "Brainworms",
  [9]  = "Lupus",
  [10] = "Ecto-Bones",
  [11] = "Fatty Liver"
}

function untill_malady()
    local b = getBot and getBot() or nil
    local m = b.malady
    if m == 0 then
        if m == MALADY_CODES[m] then 
            return false
        end
        return true
    end
    return false
end

print(untill_malady())
