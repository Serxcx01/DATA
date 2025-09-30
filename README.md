---- SC LOGIN JOEY STORE

local accounts = [[
sgrtghth@gmail.com|05:c6:be:5f:45:85:905cc0e172bc6852c6093db64af10aa9:BA3FFE1B2F4FAD342AE45CC2B5E9E2EF:tykd1xHa9Sr9lKPnhkX/vImiSyIrvZ74b+lKm3z55otBDTJVUsTxYTEDgmelZStQr2gjL4/sfg1aAJpFe1/jDyVRyME42hbvVGEnk9b45AaKwTZc85VfNh8pGxNav5PS8Le7lkzli3ygXHHRMiGwazKotVB7DszxfBYLUlyX0XqmzaZtLDRF+O4BHXpBq2pA86rul2eEAE9vB09e5OJuk5jhxKzNoXUQhI4Pr60Xs3okHyxlokxycsMlYVCn6T4DQl8UZdE0VIJb5z+6quxGCzCBocF3rMpyKsz9V8I5qA2+pjL0ePUrJfevNluYCDNRCTeAdSx/zgrcAWvDgcsH3eUZvAifyNP5BNymbbRgggWY1v8x38cM4ZEt6fPTbgAtcNN6BAsnVoEGrZgpEQqbBctSZqgdU6pENmruSWGmtjPTiqVhhkkqMwigP4Hrt3QEHeFAzW6zjTcJ7Pvcleigqw==


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
