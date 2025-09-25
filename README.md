---- SC LOGIN JOEY STORE

local accounts = [[
taduyhung3853@gmail.com|2d:57:ff:68:84:f2:31699b4aac62fbf1b407fc13c38273bb:FC049E0BEA65F95D1D6BF944E2E83A0A:uDfwPsjwqFPHSjsILVho0BxrL9gGXwLe0U5dyLHbA/EsvI9OgTLirn0oeqW5Y5mQT/xJ9nM0beJuqsuHbYiytsj0AjcbeQccdsEC/cBEmswlHuCuaie+nGGudPi5zGFR/gzIfc7u6UxqmyXkupTAQwPKKH8mBg6PYXwlV9KUT/X8isE6lPEXsFjRT0GW/Dm9PTNFVBayzgsuJVtjf2LCmfLUWg8tenG4Ysl/fEnRSAeorMzA4yS5cXQn3DPWtprvlWgGFgvWpnHQMeln1RlfPMRp4h55Xi6rRNuYFu2Vm7qdOzR8jJlXQYa2aHKxktrOgocVA5Tl9gZKIXJc5naUhwIj6LWdSQhG1CgxsVQSF/8WbSoRamSI/usAOkmgHTtIndlGMhlia0t81KAE/pIWDyHxh1Bb6bCjwc4afpPOmTUWeeSOO/swaJc9nXxAsK413u3gHCtuuGEupEEXRZPmbA==

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
