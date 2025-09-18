--- SC LOGIN WUTWUT

local data = [[
toantrang503@gmail.com|B4:C1:1B:DA:D0:8D|71CE7E2AECA3018F56430D3D8DEA91BF|B0EBA1BD2DA0D20379FCE4231567D481|/D6PJ0AO24dTWAUbOQYH78s1mHTA2EydmCgzp5w0wabk5KFlrqulig5Tv6T7HK+LuLMlPTNmFIdkhzIOKVe8EVjzsgEBjslgDMbK56U16QlbN2dfECxDdC4eI2WD7iT+7uYjpqPKcU0lyIRGdKT1tmNFlKr0GowqKMdZ/HrHCqUttavaG1AvaqYLki5FfWre2Mempk9nz44ww9sqHpnZiHHGNfPh9vLHfOtKECGNZ+vUb+N4ArCU5XPsObO/0WQjIQbsh5I5Pzw+XS/kjV8w5xxjEYIlJVn78y/i5PG61zS1pkgw694NeYfBw2acnaNolN2LoWLwH92CSDZZ686Vet8cDc4k4PURey1svvbSDoIcq+3qWIXUxS6/VBEYuxhbz39iBjkNhguo662GEK9da9UoDfUbXjR8K1pLtSkuZ0QBWlP6paWUNkjKYARX/b8Pkc2J6rMtxrEfllY6ERdTCQ==
truongkhang9717g@gmail.com|52:A7:73:BD:89:74|DD6BA7838859E3CFFAAF827EC8B3C096|32DA9EE0C6F0DC76360AB653E82FC316|ZFj32sBpJIAHXwiM/cIVOmufST9ejnb9nRbzSbT88m7dqHVMWJ70P0jCTloZClYgyrZdtuta3CqIhB8Hb6+GID/bOeB3FXxMh9N8zZXMhTATouk8qFI6rOpoHpakcv+LQPrC8Agsg1aqrkhLtd+4p3iCVLYH+rVQ7rpyyY7evT7xMtkz93f8epssPizVONzDj0+AemlZIsLfQLKIWcdJRJTyPmqREEOQiab6ew0ZAmYBOm2NLGC9c4Ztc2DTmMqo2XUOfs449QNylEmKL7FwHHElqptoiHkEPrGrFZZ+jCVpxyilwvdvBympPbfDY4IS1zXNnKiNFgKvsvvCdVuEzeMscUkRxD5Xol5TFA6g8rTfm/HbLULE660tdeRK2kGfk3QpBIZrdr4e2uvLQSFy3fBtZC+m13+8EUBgoObfkC0aMSfdmoiJClewge9PxWQkoeINXoum8Skz7fdyub2pEQ==
]]

bot_bypass = false

for line in string.gmatch(data, "([^\n]+)") do
    local mail, mac, rid, wk, ltoken = string.match(line, "([^|]+)|([^|]+)|([^|]+)|([^|]+)|([^|]+)")
    if mail and mac and rid and wk and ltoken then
        local details = {
            ["display"] = mail,
            ["secret"] = mail,
            ["name"] = ltoken,
            ["mac"] = mac,
            ["rid"] = rid,
            ["wk"] = wk,
            ["platform"] = 2
        }
        local bot = addBot(details)
        local tutorial = bot.auto_tutorial
        bot:getConsole().enabled = true
        if bot_bypass then
            bot.bypass_logon = true
        end
        tutorial.enabled = true
        tutorial.auto_quest = true
        tutorial.set_as_home = true
        tutorial.set_high_level = true
        tutorial.set_random_skin = true
        tutorial.set_random_profile = true
        bot.dynamic_delay = true
    else
        print("Gagal parsing data: " .. line)
    end
end
