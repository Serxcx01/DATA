---- SC LOGIN JOEY STORE

local accounts = [[
taduyhung3853@gmail.com|e6:ce:f2:60:4e:57:2fc309250649d3b5caf6ffd2659303a6:ED90AA48A34FB808A7D930B3D3B6ADEB:uDfwPsjwqFPHSjsILVho0BxrL9gGXwLe0U5dyLHbA/FSFzgA1gRYsjeF8xRQ4QeW64BB1xSSSkYo9rgkYDA/IFv37Y2k+w67tjw/iexX+EyUUQTT15K6s7R20Lf5Dy/C6xNw1H7luauf96QQwHbUWLE3ZReCw3VwWhNB8t5rVSc34LFHbQdgiXy1niW/Tr90vLEajaaj+G0+GTw3nV3H5vSpEkA5gmsarAzJNQajwwRheUGzjlaSJdHhxsjStSJNJmSAFKlxVUDkr/LO36j5GEKWO2qqgusuh+bp7pJqjS6c14cYBgF2oanGegMxwokZSL/MwieQpOXPUvqSH7MXI1/c3HdSNquoiq/HKsCmWtYaZkP7VN69OiKD2YsSsCxNzKmSWQO9z7CxKF2DeQTO2aEHEtbNTtIeCCRbLvj9xz+kQvPvUckTK0FgqZk+UNsGzFI4GdFrhYzx1eYJmDjiXw==

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
