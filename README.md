---- SC AP
local bots = [[
42B271E0E9BEF74326C126308B742245|74EqR3NZgIq1kSH4YIan6Qe2J8vACd1LGFEH66RXZQlkvvRC1CwemlX6HrRnbO7NGeQKh4GZfCQBuFr2fQGrzMB/3uq1U2tKDLYjIVG/pFOKIDclAf98PX6bGszTV7PUs4IGLPHWhwyZdwKCIBnYnRH4EL26ldsmRk4iuBqR2ZFwc6tLEZ2fOPifGfmSpnUQwNqg18xZRQkI82sVH3qXgiJFd4HyGCByEpb+WKlNDViU8i0APQNV8qn9c33aPEYk8a8cMIkdMRBzVLlmdbeJzosiZpIyUUEt3N9YD1gjgXGJH2RrZnPgLNHLbQzHBwqJb2iP/I8U+BjRWu1QuXmIsDt7KRcx4osE1TYgQG1OyyCbaKg+PaoBH5PEv2h1NmHT7yDj5rSskvB+h5cDDQ8aUt2cOfMazPOWmsDtPNf/bJIBLIZwcZQICu4CsP32y8r3e3ZZHU93j3wre2Y0sK6U9AEFtg8IXWpRmuL9yRW79SmCo1rO4amc3SMTPVXmUByf

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
