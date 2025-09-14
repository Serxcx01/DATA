---- SC AP
local bots = [[
4669E7068F423A7D43CBDBA7AC273DDE|sE6+DTdXMwVKtekKzlxwODbWVKPLBpdJ3NY020wsiPIaKcFFb/ev5jZPA7xqPYgqO9Af/zvoIo92mGN+g6qt0wCyfs7EivY9FrEbn40WG7xsntNkgiUynItKqdudcLa8oVlrxoItUdIKvtiYtMyFmaI0es0eRrLj6ShJtbt6tgaGAgIvbFBteDCMB+KDkcRuL7A402XhmufEJDfkYUFCu/6B6eEHDYAyBEzeIq5fU7DaRINFNflPh/7q3enPN7e7mA+y/QIpSRFZGZqcaiEjd6ol7el7NfBgbR5nuVaXMRg7wovPvIdwFh2zyCDZQvQskNd4G+CiCUkEPGapj7z/hOU+AA7kbxOXeXleiUPlfFeI4OzWKTb8B0dX8zE9YtYSs5CRYogp22uDwypNWomRxmV+I4Z6gBz1hrKAGHVtxA9CUb3aOJGJKJOOTAUQjyGopgwI3E/peYC3razeh8YhgwlDTckByppzDx92hLRnuME3U/Oa1rYy5ITiLYnu2YJm

]]



for line in bots:gmatch("[^\n]+") do
    local rid, ltoken = line:gmatch("([^|]+)|([^|]+)")()
    local dataBot = {
        ["rid"] = rid,
        ["name"] = ltoken,
        ["platform"] = 1,
        ["mac"] = "02:00:00:00:00:00",
        ["wk"] = "NONE0"
    }
    local bot = addBot(dataBot)
    local tutorial = bot.auto_tutorial
    bot:getConsole().enabled = true
    if bot_bypass then
        bot.bypass_logon = true
    end
    tutorial.enabled = true
    tutorial.auto_quest = true
    tutorial.set_as_home = true
    tutorial.set_high_level = true
    tutorial.set_random_skin = false
    tutorial.set_random_profile = true
    bot.dynamic_delay = true

end
