---- SC LOGIN JOEY STORE

local accounts = [[
qnzmgxzacx@gmail.com|79:17:33:ba:25:41:951fd0a298839530eda81ef4a616969b:0C330CF3F3DF648E6B9832D2CCC72EAE://+QH0scKwucNsnlJgPkbuNyjDilJzg2nkLBNH2TDBb0vnC9d/9Kv8wf+XhpyJj96JAlAMmmhO4IdIVYI25kvDtYeT73Dp+qjOoUpOT6tAocmU5NcCJQOaYLxwrJYuNWrxY81xF6tF/+YoIq2w1oDbkgCfktouZkB3RNSaM3LwDv9t/BSF9Ddrqbuv3ceUVvGZWNs2v6OxkLQ6aturKpj6EW1TS6VpJMG1InhT8h8tFDG8DXnYTXhRUz7jRpVka+HFCFFo7N/AVbjhTIpcOiy3lSBTy49VivZC3WjhJrwsJPbDsHsAbxtCYypbIlIoXJgEU68XhB/qjymAS51yKqyHZNRzy09yPXNMo6IZE3Ka8I4JBI7OKRnJ5fpqGpbwpHIYfPWDEaDJPuhRGc7SxzW6zQzkb65no58oBpRIBWxK+bOxu7paM4gLoHV++SmWYiAdvHvDzWWQog6Xi4SiIYzA==
tinhgiatran728076@gmail.com|a5:20:f3:a4:f6:2d:d94fd10b0da6a0cd176a55050ead680c:A4FF1EAF95B671A7331DEC8462DB03DE:tykd1xHa9Sr9lKPnhkX/vD4elezmrAcKLd1J9WCXwizHUPaWzc2XaomvANVxCRJwElYih1RtXZ6qkG9LaDyssbBTHY0w3k1tLd6DFcG5i774YyrO/jwNmQwAb5K95/qr1FCaPzk5nadC7Enyl4OnUiVMzYqCmXkRkpnK7qjay8dvfumXO7RbiYslCeDE9Xpojzu8kEis479p/PZ94q0OX0QYoMlbZ83Elnv2bAjUurVm8iThmFkkqCxgT0tRRZZPj6sZwwKR2luzGZaKNjm9tOurwsKyRZn1/oaRGGx3GW/IJIbzFyGMUdSkjWe0d1t6BWkD4oS1uI8uEf1CLeQzJwcymlbJ7cgKzGhMWSth5ck3HJiTW1patkm09ZN1o751Xijz58jMiUmG5WS0RyDUJxPLd0/BiofJ/x0aBPLUIJ6k+jFavCpU4h++OdikDicCTvjb7siCWeth3JG7BjzupA==


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
