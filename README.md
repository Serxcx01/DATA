---- SC LOGIN JOEY STORE

local accounts = [[
siminhdojr@gmail.com|7d:51:29:f9:39:1f:28372bf28e127eb06e722ce187a54ee0:8BDE02EF8CFF13C4A3DF607D13BEFB7B://+QH0scKwucNsnlJgPkblZcCOhfYz6ciRUwc4IuQ9FPeT5J3v/OS85D3CmaEWRoSNNWNbzGqMqaysdvHp6i0LBfZikq+rG+90c/pL3r+jEtZdtYCzCx9cGzIiPUuhL4mUGoguyNMz030ilmx9IF2i8WcArGOe+lJJKNEiFgtJrtwOV6Evbkm2EXBiXlzGXSKSDdsT8ih/m2FU9bAsTy1AanMNBTKvOvPLm+SdJREWUSxW03vCxGL79hG2R3QCmEw5GtAxORS5xHx3ffnWEf11In31w/YLreLyjXOeQa94joPUosEUzGF7zcApuRGxdo6ySf+LlTkfo3dAbTIgL4+bmkOJvlIsoJRwZqVZRrmKM6g1owoqSG82bCzLxFF+tZ1cryufqDSPviMBbdp6nKI1CeNk5RKKMCgQitQdoNHnpwWD/KyCXSldqBeOYoK2DTBeActgtEoCQR7AjhMKfkYg==
qnzmgxzacx@gmail.com|e5:88:ba:27:02:eb:b07404cde5c8ab2d07ba6797303103b6:85269B8E9BFDDFD3E6E6C58B4FA4CEAA://+QH0scKwucNsnlJgPkbuNyjDilJzg2nkLBNH2TDBb1g4Uc24Z8S+GwYdqSpppSVrOFbE4gLez3VIfx83HrRNSFK0Z8eT8X+Yi9mEuvoJKdi6pbzupCCt6bGJHikFdVUEVQeqXATkiTkhdBMod+5PmuYz9UGwbowz/tqfc/LZGCWEng6PxEvmrM6UTDp6fCnt8Hl7z4qbx0YoQlvR9N1YOWXKQB/gsx6Tsu+FaGLpTbFllTyS6HCgUK4uAXxaKCgJ/lSVaqxhpTN/flZJu/P+UkWDbeXS+L/JWRJ9AWKkCF9gsEYWqeqUhqUneL5gXXoSE1d1eJOJlbuwfBfrqhnjvgAENs3Gsm45evfs+wdxOk36srGt9l/Y1F0+kyYI3vOQGjJEcD8Syq6EZRVIE1oiFwacqUwVSUp7iklD0jmntfsUkTKk1G/qRz0CysJW/GN+uiW9OjKP3fcOYHDzqgog==

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
