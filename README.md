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

local function current_malady_code()
  -- Asumsi getBot().malady mengembalikan integer: 0 = sehat, >0 = kode
  local b = getBot and getBot() or nil
  if not b then return 0 end
  local code = tonumber(b.malady) or 0
  return code
end

local function current_malady_name()
  local code = current_malady_code()
  return MALADY_CODES[code], code
end

function check_malady_now()
    if AUTO_MALADY then
        _malady_status(false)
        local name, code = current_malady_name()
        if code == 0 then
            print("Malady Status : Notfound")
        end

        if untill_malady() then
            while untill_malady() do
                sleep(2000)
                _malady_status(true)
            end
        end
        _malady_status(false)
    end
end

print(current_malady_name())
