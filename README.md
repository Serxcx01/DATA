---- SC LOGIN JOEY STORE

local accounts = [[
reytrrtygfhf@gmail.com|c9:50:63:48:ca:30:605409c037441216aed0db7099309298:9D79108A9CD67EE907B3B0EDED9EABF4:+xUX5CsomK2SdTFaRdt0sVeQQcWziZbFV8099VaO0aY1YjmYITwGphLw553mU/7em/3yacR45YwRwLiRn5Z4deT4H8obyZ4mMnDEchnI1MAuxKXl3JRlRI3XhiITxdlJnkYWE3QcnxuM1V8QRC5amr/DAjzH5Dp3pyPnl/Izq8C0PB0jWB4eJPaoQXcqq7lVueAHkCWWhJZtHYrQliRf+YZ2Klq3hsZjxgCqt6DSH5sQvMV5nBBPvD0Ibskl1Hw+llQZy59LqK5hbgFuSb4NbfdjIW5kVv49U7yf56xpLKvtUGL4jHZsmTEHJ22/Iyl4hR2b2NNQ8d8Iqc76wud5yIhew89a3G/MGg6sakyl9gYVnKNEYgmpkgBvAjYQ0+IAZTDhukKbZLaWXeK/5Y2zL8rnq2qRLAfbgFtb/EnZc35IsI4RaPV3txdK1IAFuGlpSwt8dcbyS32iYfZ0gONVEQ==
rm2808482@gmail.com|b8:18:20:e3:11:93:ab911aec3f91dec414c736d9d37673b5:4D0D83A4C5768634AC28C30BD5E04B84:+xUX5CsomK2SdTFaRdt0sbkb9j8SIpwlK8GnzGHdVQMuzK5glXUB5m75hXXVIOaNeP/mnQUT5oIzbPI9hCgy5E/miiMUtxA0eSSJO1K/nDfL4R8twSbbPD1kWmyub51ilHazpyQmx5YzPyJ7aZwp73/CNxKcBdOUT5LDd33T4vkLeZFPIJLrQzKMOm/r2EJa3Zsd6yRPrE0jcu97Aa9+JhWqHnhC1q9DJhzpcYSElkRMzSNqxkSMMQjf8YCJRN5dVazbqGh9F0qdfyc6iEwRSYEe7sUDAQmDtTbSsc0ywqoJu7ciR2D3a1nAUxa8QNHa7hilkKdKhh3ZfUGBrbedt+ocnNZa3EaOhUJTsuW7UzjiOggTwGXU9mN1/ZvqnGHYX0SRFidPRCn9Z1xvr3zMrWwU7/LHzQbtYDE3+fI37a6R2rLIormBERS9JjZWkTBByGNO9T7gyfCHlBY3bNKQfw==
wk7863707@gmail.com|ae:f1:c5:3a:11:c4:86485e02783588814a7c8f6a03ef4c8b:FF9ABE603CE1ED7BACBBFC2C3416BF27:+xUX5CsomK2SdTFaRdt0sSnBN21HsJeHuLwuaE1TlbQIPlHArVvrOQLJ/q73HUpMR5YYgSSGoTT0H2eripBcyGNupYBIaoURAi0R6o+ZR+qoZ0rGb4rJS/B2wEvRGjZBAfsqbuy9MDqzZsjeCqAfGo91sWoffkJx164M+cjq82sI3RDunNv7i0/snlUCaDi2nToV7eASprGGf0kNKpelCkQ3QEBAdTVGYjnnlOR7uPu1TCOf+brNYfI7ynTFjDlNkBNc1wRBo4TxFzpGnfAtlaMXZJkcNXFx37pfaATW3YUg5V1iUxINRMsgSYJWe57Cjq95Yh8AokhtNZ8qaBVaU1jML8rTjC10wsQRDQR8uftXGpTBUKrQ+0mRhemozRzl5WzNDdVPfgI4j2hGldrVIe0pC4/d1euPyLNk0rXJLDk0kGxu4SfqxvJ8xIkdntFqdQFkh9keAxHiXm/2PtvP7w==
ratantatababu7788@gmail.com|9c:ec:72:35:f3:df:b928fdb16647c4a00316d0e5f28c3030:28CB8ECBE12F02E5AA7B6D2EC2FCBCCF:+xUX5CsomK2SdTFaRdt0sRbPxA1407WASsu7fXCwr+gzLZ0pMaTLk9zehaPaEOnS/aDAZXCv4eJJagfnxYdX4SOPsoTHzW+AJs9br4b3sVY+J8XA0zJpKUVhbjdZSxY2kNQxPXq/8N7Yk7n3TwyF1SkK/ieznLUD3XqxgmcmlTUnTIrpKUPX/f0dPf3hwgtn32UY8BsImtrGr76Rsg8IqI9dI/OGYb4Y8YPhuPmNeqsgu2LbiH+YYMlUMmNm0/teZLW2jAnVh57QVcPBZEEPNtLDVRnb3IRRMAUPX/qnUTO4gOPZSY7w95sqaufxyWNNR4bTc6StSDTmlPtq+75llCSuXXazjaWI8Baw7j7qWpUkDar0lzSS/UeKFylzpsvyWIy+fXRbD6vVSOL+tqoW6fzrlvSfYnRokJ8dP03JbmTonOcK/L//NSK0bcfoIBuY9DgUFFWRX9OsCsYjKQc2Zg==


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
