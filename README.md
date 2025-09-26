---- SC LOGIN JOEY STORE

local accounts = [[
tductri46@gmail.com|4c:de:e3:17:56:5c:7a567fe2528fc58b26e64dafbdee0a79:7EFEBDD44B1EFD6F9E0B0B46BCD9B31A:dlUy33JKvsuFYV936hCS6jHcBOmgMXeK7/846tVbQ+XoT5gjWORP0rVU+77fECZbBDN/inKAFBD2pw/EBcwthnmEYhztu+n9jWQHtctgLOap2SHJ3SVSRhPFmHUFcGcTIZldy0gzeahBPkNtRP8ElYaceRNyvT450dGddqqWVvlMfmUOJmySZveGcg1QlUTBziYlIkrGPbsgrIiLYZgwJK4TbVj7ZaZHLgSTr2NNPxT7Ym7E+wLTKjzb0FN7b1tZE+T8qkhZBw/KzDaHaVjVc5l8ifhjVnW/OVhXH63hICbv11hybsnmrsfsr+74igI25EAW1YKZ8rWpTG60VNVoTPFIv35yFJ3OngyoepraaV4gQBf3dy+NbZ4We6kiXbESsNdGEM/FC8vqVzImJkN6/4cyhezf5Ug1HL4TCu8wuK/t/QwQxnuorU5S9yh3banAegwR6mawSWtmI82KBZYMWw==
thaihoangvan1198@gmail.com|0a:d4:04:4c:9a:bf:09f1cf25cb2f92321f58b7d85a92161a:5C28A6D8AB98E13B9BB70483D8203D3E:dlUy33JKvsuFYV936hCS6qdmie2/iOnM69XfrKYIqQMq8g1uExE7guTHvZpSGMYqTM8uC8gL5E281nUeeAplqXZXIZgHqSe239H0J0Foai3DtEe9nwV2ZVlnXcv61ghIa/GIzLO3jwgDt4ILyM+lir2PdejUkALI6Lq89nPeuPtEdoCsLjE7cDtWdBI0SBGKra8HzYakhotvbcCdJNQ5wXoYEk+aNbpLD84Uh5JQpF+TEAPRPiTzjlZCXdiMrsQiMmRlZ3nWioHd/09zByLeF5aIXVMUie/my5e51mBo9mrNB2H4WTNStCCADbjKBAa484mCjC7bkbGKPGQkAg9WVcRQfeFfuaJF+Riu2h9OKAGd9gt9C1VaOPuKyDELiUos62aJOckwDbkqY5n0V+kdd10F419wBr9jNaoqorgHT0PcwHFTnCSIx0zIol7q4M6wKjdUYFvXBv7S0zV4iwCIPg==
thicamchau8134@gmail.com|d3:99:68:4b:a0:71:0edfa02ab578a46d0063a77e0db33281:3B5CDBCD69834DAED1013202C19C67AD:dlUy33JKvsuFYV936hCS6ox8/YyftRPEhEm9mJgsyndmpP/Key5Vmfd6A7KMXKTqJIgwqX3J/xaGqtEYYDYeZpkulUjubFGg6LwIZcEOKK+J0+RK570pj0vUKHOtqa9Z3hi32vh0PJMYDCa2sepIA2t+U1z03aqYSZy+Ujy2UVIv1nk97JbKBje52mAmwt5Z73t6U2v15dz45mF5liIS7pKOGwESCNjfSp17TaMwZWndgIa7AT0tmlNl4IMW/T00C/zWDLjky57BiT7NHcufHxjqj0Xpv0z0RCbdEh44vSyz1V+149Tlu3NN9lIyHcBeObeDnH4YSEDeAI5x5o3Be5pIzWN+iu5ntQrJezjqBakotzAM92jY8Fi0fBTEuj3C8/2JRbN4QsIZATcryIwXmnfDFFJEqhv/z7i89maK3v5t3gLjrvf10ZwLBbR7+1HbyC3ckO5EproJNMtdowBhLg==

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
