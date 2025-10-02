---- SC LOGIN JOEY STORE

local accounts = [[
siminhdojr@gmail.com|c9:02:c3:58:45:b7:8c68e39381634325d8f66f1f8ffd5f99:7A5FEE7DFB3D0CB63E13E27292071AD7://+QH0scKwucNsnlJgPkblZcCOhfYz6ciRUwc4IuQ9H1JNojw82wUw6tO95xMovjH3Pf0w5Ea3QgWfCRxszvsvkPH+CeUYWJ7RzZPjXG3lyuaxcrC5m1NNTfJqVOBFyL56HzxkeXq3+X4yzgNU2aTZIUfbb/hZFk26h7vdI+XooDIa11ly1RSfobKiTryBqFHVXsp3spG4u75a+LsbxRv58lWxPPKOnNJm8mgWmGDODnS5sstvXSqbyMJu6vE0pTSnxDwN+i86DO+0y0Ap1LpEG0tcvO3al9WIDWrmFUxzNBeIc+mDzbt0R44YMbZ3l8Lkz6qUhkQzP2NBnKVT6vwwml5YlKv02n2JE5uXLn1Av9aVnXY8G6tswtj4tn3dbg7gXspZXcGitXzLZkbLy/dNWi1Pt8BCKnieCYFoneN+BZS5/7ElfweKzP09E6QA843DeyjpqlTfG8LTnFrfr6bQ==
qnzmgxzacx@gmail.com|26:20:4c:79:57:73:c60dd8059de14e30b4b10ff28adb7977:F7A6E94D8F271BF4DCCFA8CCE54FF3AD://+QH0scKwucNsnlJgPkbuNyjDilJzg2nkLBNH2TDBaZ49AckbYxyn4u32JtugADTyKw/KHDCjpu/XVji/ZHuGoY15vhCEiKSk8mNM9lJMg5Yta2G3S73LvIn3eKC4vyV/NWBr9sIXxXuRStuQeZiGeeN2SRVYidhp7Ma9bPOjy71PtsfWPDW1I0oOVy47OGjdW3+WSnc6oYCtHXq9AMbuWWYjn4yb9RMyGhUNPKjf2z95jbDidj4Xp1kJxcmUWOIyCEEjO1cl/0+MgwqO0h/dYr+3FlYQsD2mevde2c+tBKnEiLZnNrTfqKI2FajvNKBX/kPHgJXyh7CPmi9Uba2Qsu4fs2s5xp69DtlE9fklP4ENcWbvAmb1w/RMf76FUnV7pk8iaoOZ38qKhXAVzsgringJs65GYhSeMPWSzWTji9jYYoGC09aUMzjsoAxoc219BrTxoQ52VIUEk/dxeJ+A==


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
