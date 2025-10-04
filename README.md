---- SC LOGIN JOEY STORE

local accounts = [[
siminhdojr@gmail.com|54:17:dc:1b:83:5c:c1bb4ecab50a24786e32b2c97216def5:1D8EF9CAEEDCFB6AB952FB564FD864B3://+QH0scKwucNsnlJgPkblZcCOhfYz6ciRUwc4IuQ9HjGo+kD5FT99KEti+bFv7VucpjVxbF+qtjJx1qBsYwPXT/SjffVS6GBXbbImrdzDxVLkzAS+kiC4RgE6Wrw3OqVb3fd9bjb2fO8i26m5G5umukMpR7dq4ip4eG2+b2JWSbJFNcpCqx2bLpV9RJbOVVZlxDv+7qfTQwUfRS3AxfARP1DDaBneB4sIsh1W9fPKq3QwFehdCWG6p6K+CJokTrUBJWNbV/oc/IYBTp1pT2s+pgYmDGGlk/0yqXyGP9jDgis1uapX9i1cEbrTuSeLoPEA3zgEGqftB+MxOiZPoXlIiGngZcrVNszcpBA59m767wN57imwG8o/ejNwfXBbjVaqxH8XBbyDHt2y/Od6K+dzafhLN0K5Pe6VE8aX5d/xqPlK0rtbKDPhBH2u+CkevzmrDq+4nI6izyCHKxSB08IA==
stuartnicolasa748@gmail.com|3c:c5:46:2e:84:6a:692c3f51fb797fbd51bb023b086fcecb:82E5F9B18C118C3CD0679C49DC7EEFEC:tykd1xHa9Sr9lKPnhkX/vPEgHRxVUtW6C+zKUVXmjRI5NnwtcPBbrMEJG/KVLnccMqgG7ZEO8G7ELgSkL/JBXZ8W5ml0alVJ4m6dYMMraEGSP+/FF20V6AMbhsJrkRcEtcHXzOcWGNkYw5BINoJQfAwGTagiIsj3cJHy36cG4nBKs1H1HhobH3/80LYi+AWUoZULxZ8+DCKsIOq5Vco2+2h7Ny7TQBmMju03fbirkQ/wMYtHX8+QW8TTB3C/VOApF+2nMujliM54sRoJmTa4FqwH55rU6zWyoxG3Fo4/MQ8v0KBXiH9Pp5dJF9RKEaTwoE5xk/qz0XYDHvTPXTJKwShVI9wz5Eb6URGGYJ7iu8jvhbmIBLvCFbAgkQVuBZ/UMK6l5K/XjxOiDdz16xDS+PaETaOPfyDGYpmhZLlIZrqEIIrBf2QKJZ/RHwvWaO7Ud3JpLQR4AWZor7TjTXsxfQ==

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
