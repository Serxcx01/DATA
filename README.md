---- SC LOGIN JOEY STORE

local accounts = [[
sergioxenia4@gmail.com|8b:5e:35:85:b1:0f:a71c0425d652dfd60d2c9ae12993f12f:F6DDDCB0A9EB7D4375CDBC3AE1D1FFFD://+QH0scKwucNsnlJgPkbg4P6YP+FniCYrI25q0n4uIkr+iO8AkxVOgwt4hqUYCMI5uPlKnm7u7OzHMDDx1lnQfeXaQowfiPeCeWIwFDcwqCyNBf4OMF9ob5SkkGMX/3Ulklt30fv6D6ej0bO0xX2dxMRo102BhhBrv+3fKSpJ9ZaztjW5oP6k5KL1UOqxFGKvLMIiKYYbWreQkgnoI3gzxjdMx1S32zzaQl4SEfBWuuKC3dMTKRwNTy/oG8KBcB21MkSkTEIo+UVek6NfIibrso4zx4qyfC7gws1kFl6/Lq90rPVoN0NyI53MZwro08o6eYEqmqWgaeMc+StdAaxbOrU7LeX7h6P8Sj6VBesd9mWaKSl5mYrZdtMLRE4ZCjIN3sIbUfljRi+DkkWJWRkNju/SPVnSt+XRDrReqQIH+mNqMvVIDRlPxBzMIe2iCgDVXWSMc1La4JlU/s/0O5tg==
tytjdudgdhfdghj@gmail.com|4d:73:c7:dd:bc:3c:02af50a36a7175701ac19b5e4fb0bb4b:DAF078D0FE41F7DF9EC09A32204BACDD://+QH0scKwucNsnlJgPkbi4riMmoA/TUNadSBYrN5CZVLQCNSjR6IfIllFFn2b4wx6RIia4TFHIRKU8cQQsSaf3iVj5NXiiIE02SIw/POfaiFHOWYTxDZf3UsWbR5cYiA3iy3n9vMqFfGctxYwnGwr8ubKsQC0T+AFFqyjspauOtN1eHp0JINV5JULRXvEBZUgLfLrI1UcC6u88D/HS9eRBFe1VInvD1+CG/akKTs63ADCyNJkBBfs7NuS6CMleZvIQx75kGmyahoiJae64HHoKE/eKUS5rjr0DWHyxN3zXvf3L66eXuWCGHtEdkwIwycP2NKuHRz0y/4noacX8FZL4vWoy7fhqwXkqw/QRSvk+WAABqZHcljRPZV+byenmyaWe0mM09guEFe60BUWXlJlxuFXvsvD8bj014vFA7ov7shLGhw9pOec3Kg4yfKP7OSyOrbOWyIQTaNygd2PD9zw==
rcrdeionyontwsr587@gmail.com|d3:2c:52:8a:b6:17:1d0832c2df13c876ae6d56d1b1a03e55:F8B3FADE3DA48A8AAA0FFE34E4042744://+QH0scKwucNsnlJgPkbgPAesTncRzCDUoa/m44FoLtfX5Xt/2hywG8jOFLXCROOEzeS9lD2/rNhIUOJXSF0SJeIaTftf3umz02yNfSBMJSIjJoo4TQJZpBICKTLFLgw4mScrObhm+0O8effVrTtnzmip7LV68SAZwTfbCtmy5F94J/YNn/GzcgDVpZqYyN9BXPEtmAYmVaZYtNynShN2PlpXzcSFLz4zWVjTj7JPvQMGd9V2HmfvYqXJcFTUBCWIu4GBT6ruEl/XZEjq47nMPzfg0IqE3f2YqRQ9elAmSgI+lprPVpySpVLRkCDESOSi3+ULg31GgcG0h0hawEuIVi3NN8A2CMTVSwhBY1iMhDOClh61aZQd5LngU5/01v97LtZpYI8pPZeHNAeDs370isxHlJQHkytuaZ/hnvof7CudeaGwlhB9fR6j09G/ZuSORVrpP1zypOOp/8/hFshQ==

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
