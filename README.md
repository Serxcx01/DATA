


function GATE()
    -- getBot().malady
    malady = getBot().auto_malady
    malady.enabled = false
    malady.auto_surgery_station = false
    malady.auto_vial = false
    malady.auto_chicken_feet = false
    malady.auto_grumbleteeth = false
    malady.auto_refresh = true
    malady.storage = "COKANJI|XX1"
    malady.vial = 8 -- Chaos Infection (By Menu Order)
end

GATE()
