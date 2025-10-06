
STORAGE_MALADY = "COKANJI|XX1" -- STORAGE|DOOR OR STORAGE
AUTO_MALADY    = true
MALADY_NAME = 2 -- BY INPUT MALADY
--[[ INPUT MALADY
    1 = MOLDY GUTS
    2 = BRAINWORMS
    3 = LUPUS
    4 = ETCO BONES
    5 = FATTY LIVER
]]






function _malady_status()
    -- getBot().malady
    if AUTO_MALADY then
        malady = getBot().auto_malady
        malady.enabled = false
        malady.auto_surgery_station = false
        malady.auto_vial = false
        malady.auto_chicken_feet = false
        malady.auto_grumbleteeth = false
        malady.auto_refresh = true
        malady.storage = STORAGE_MALADY
        malady.vial = MALADY_NAME
    end
end

GATE()
