---- SC LOGIN JOEY STORE

local accounts = [[
taduyhung3853@gmail.com|68:e5:76:33:83:2f:f285a78faa2e100f27c8a907749502e1:F718B020FFEFF340B95AC093B2C510CC:uDfwPsjwqFPHSjsILVho0BxrL9gGXwLe0U5dyLHbA/G7zPy1J6eRLBHtIrs0sXhS09/8fL+SvcFFYs/CNnrqStb0ZfA/P9yGySfQvqlnM+NgZdtlPp8bzaRhBxUcO2Z1ucJNov6L83AyJi+XnxUzoly44JU/r2YlKvsdfAD43x4nGIw9rqfNnMapYgX3allkqcxgSC+C730johiY70fdDAP+GdQIwENjQ4i2ncxecjHGYR/IRrGXJTqpnawx1a7Luzv00AEBMKNdUava2C0fE4cxGT048pogrb9Cq4eJqkfiL0LAmD+LMq042pv68CjeIYv9wwb8n9I8qt50FjRfwPsFdVHBoG+H+1gtHmV/wl/L7ibK5cOgmrvQtYJIfgL0s4Av8YDEShuif1R9rxCqpmoH8T+hr+LeaDunCTjYqV+9ak1CVyRXkvpaAXnRxaxW1oO2z3zEmoaSZqQizkkHcA==


]]

use_bypass =  false
for account in accounts:gmatch("[^\n]+") do
    local email, sisa = account:match("([^|]+)|(.+)")

    if email and sisa then
        local mac, rid, wk, ltoken = sisa:match("([^|]+):([^|]+):([^|]+):(.+)")
        if mac and rid and wk and ltoken then
            print(mac,rid,wk,ltoken)
            local details = {
                ["name"] = ltoken,
                ["rid"] = rid,
                ["mac"] = mac,
                ["wk"] = wk,
                ["platform"] = 0,
            }
            local bot = addBot(details)
            bot:getConsole().enabled = true
            bot.bypass_logon = use_bypass
            bot.auto_ban = true
        
            local tutorial = bot.auto_tutorial
            tutorial.enabled = true
            tutorial.auto_quest = true
            tutorial.set_as_home = true
            tutorial.set_high_level = true
            tutorial.set_random_skin = false
            tutorial.set_random_profile = false
        
            sleep(3)
        end
    else
        local mac, rid, wk, ltoken = sisa:match("([^|]+):([^|]+):([^|]+):(.+)")
        if mac and rid and wk and ltoken then
            local details = {
                ["name"] = ltoken,
                ["rid"] = rid,
                ["mac"] = mac,
                ["wk"] = wk,
                ["platform"] = 0,
            }
            local bot = addBot(details)
            bot:getConsole().enabled = true
            bot.bypass_logon = use_bypass
            bot.auto_ban = true
        
            local tutorial = bot.auto_tutorial
            tutorial.enabled = true
            tutorial.auto_quest = true
            tutorial.set_as_home = true
            tutorial.set_high_level = true
            tutorial.set_random_skin = false
            tutorial.set_random_profile = false
        
            sleep(3)
        end
    end
end
