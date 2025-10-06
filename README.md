STORAGE_MALADY = "COKANJI|XX1"   -- "WORLD|DOOR" atau cukup "WORLD"
AUTO_MALADY    = true
MALADY_NAME    = 2               -- 1=Moldy Guts, 2=Brainworms, 3=Lupus, 4=Ecto-Bones, 5=Fatty Liver


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


function _malady_status(status_take)
    malady = getBot().auto_malady
    malady.enabled = AUTO_MALADY
    malady.auto_surgery_station = false
    malady.auto_vial = status_take
    malady.auto_chicken_feet = false
    malady.auto_grumbleteeth = false
    malady.auto_refresh = true
    malady.storage = STORAGE_MALADY
    malady.vial = MALADY_NAME
end

-- function untill_malady()
--     status_malady = getBot().malady
--     if status_malady == 0 then
--         for i =1,#Malady do
--             local split_data_malady = {}
--             for w in Malady[i]:gmatch("([^|]+)") do 
--                 table.insert(split_data_malady, w) 
--             end
--             if status_malady == split_data_malady[1] then
--                 return false
--             end
--         end
--         return true
--     else
--         return false
--     end
-- end

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

-- function check_malady_now()
--     if untill_malady() then
--         while untill_malady() do
--             sleep(2000)
--             _malady_status(true)
--         end
--     end
--     _malady_status(false)
-- end

if untill_malady() then
    print("malady")
else
    print("no malady")
end
