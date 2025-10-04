---- SC LOGIN JOEY STORE

local accounts = [[
martinmoralese9357@gmail.com|BC:4A:93:15:3A:16:C4B338C34018BB530F69C8512D8937A9:2D4D753F520B3CCA6DE3C24B9B012E38:Bl4vc4mzkOVMSKLfUvfgWfBcZryQ/kHc+dclvfc/2prekGogRdABf1UB2ZBQxYJgoR0j1wUZx8rmHUxH7ezDPEMSnqRhHBx2qQh+YliNYRNwIfcGoRpXlVkkpDHTYxLXydhhOQHgcc8u1ZUTKmziBhHcOI/j8Q4/EktIAcF4aCX8RPJ1PIIFysR8YVSaZOrc5b2z/Le3vkTjKpJlAJwQyjcLbLqk6ssVVQ7BC1GBXxarmmKGeJd/xW2r5X/eqmuq08qBB3oNvjrOua1AdnQmWZ+glLAIuNPFl7P07xoQhK9sJzM6tRiLtsFvvgbC3Q8eL17oiuGMkmXq536T75A0gq6TI4dz8Fwq34uY+zJAtp1IIgm1JxOv6IAv4glUyxRYUVTtaPm4LslNDBg5uiRbYLzSQRaqhdROAOkeICDQ2LRJ9f5hoSqrt/bs5GUEKn+NzgzoKjABYXwIFG9iFdIRyQ==
ivetteian86@gmail.com|D0:4A:E8:91:D0:74:C4489E3B121E9CDD2C1EB1E01AC853C6:E5FFB63CFAB61B9CB3060831EABDA792:ir4VxN6lCX6IUaOnW1Sbf7J2sgorOQhTm7cDOW+h94XG3s6XiZxyDoCZElZhWbGorMWsWIt+yE4ujLrNIatzvlvN/zeARoiiuW8fM+85EXKK0ZNbt2trVVd+w/HVS3THiN7bxVqRdcexHf3cb3B3GMSoT7b+4aPimLgOhemAc+Ik2IRSPFVy4P1Mutw+B38HGSNlmXLV6w1jNhR9U2Xt9fm4k86n5fSykapVpLOy7NLTOGGivcIc/G1Hp6EbdxaaK8coBefUaH/S26QLb1qzCqigup5hBnoKnLTCjBct9vtGJImf2finloWZ2qDsYAr07oLW+9qEad2MR03FNcucEVRIp9/IgFuMn6ZL/W6132C+4sqTOQlQeoDdggL1JsOIU1d1wcVT9mzgGfVXnSS2r5aeh6SGvPCSH6DGHJCygNAnujyHqmcxYqr50gLW5OWaw+qmM1ifhhmzohAbG59ejw==
leandronikole7@gmail.com|A0:5F:63:D0:35:E2:8CD102AC999ADED09C0196BBE071C8AE:C515A0455DF861F1DE0D238661810B1F:IlX5kmpN/OYxt7ZyecFo6lXP7us54Jhfq8ZgU6OsxIIMrdQz33kQHLe1hRapqTqU++L3Rnp7Vik/UYSKBT1Fq3ifS2i4Qkw6ntxPLpgUD3l86sJgYsdxqsZtIvtpfQ+Dq0o5NEVb9BlwyYCmPLgYPH014f8upcIHR/XSqDju7iBLbnEqrU0C+ej2opnJ9ANBYQEFD5Uc/8swxQML9Ub6Mc9vu8NKhq2hlcvY+otDRsNJ9hcxm3c/KjyJSc+3zEHiDqQyDyb7cscdpdlmHiF2QGqWBP6qnNHu/HZCt4h9nppTndjZR+2jc0PWhCnZ7QEgbDGjQ89azjWg5C9yo5jCMpODprmdF0NFjyr6VNTiwe0/N/eKv7efMvQL+NFcwkkmZ2m6AtzktP9Smu21BQSUGZT4g1PPznlHMsUdfYn011prO+QOgmVVIJD/MGlrdSe/7rbJDVFC6iJiuxG2qlzCaA==
tinasarlashkar455@gmail.com|F0:E5:5D:ED:4A:E0:CE8307F97D047576CCA49B9537CE7819:F72A33C6646208EC5672707A89D89BD6:vzV+dN98LdUXpwo1vqZX/iZhYw53lHDhb7BDVnMRCR1baTL9cvmhtunNN4NJ5W9/emff5Km7uj4eOfl9a0hvKLW8ZPXoDbLpzj1BIsi1jziQ/vNazlImw0FlZcxUwNZ7aGC56OtE3AgQ7l8C5cgtoYFyvIKoyWizNPJKsFJtQ9Im+3x7Nte4GkUrF4GA8ZpnlWBMmkV7AlRUInJvkEMGxjEybUcR6Eq3mYFwrrAGgQjAjyFybEhF7IETmQN0fMXHhJ++3LpFmmbYgufDAFhfcBn8mmvQ4eiPxeCyiqR9ULFbKxAyyuXW6a3ndF/rWT803Jf+wMJPbmUcgXVXN5PxA0O+jMq2RBC9YvOMy4/+fcGK+ij2y4DSM/v9ozO6H95ZpQp0hkW8xz5J9RufkAadzVzIuj8e7goZ8PcM3ehZSY8b6x9ojjVI8BPuQl5fDvVCFYC4Rcl9P4B0RbesS2cj8A==

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
