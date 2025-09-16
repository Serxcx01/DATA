---- SC AP
local bots = [[
A9EB74D92E3DE41D0F9088DD6B0FB3BC|ubPRTmo9iocimveNAGOQ4O1PKH/bNTNYdhfJdVaB3uZXT2caGpXYcVWHjnfg/CNBk25czv/jNteKI9cq/6YvZNqmBAfDKuHH9LIqqVBT8q5prFzoKpCA6XtGH/+FZVsn13u3z4hRENE/n9FQUzZYD2NcRprSqEqQg+TMgPtbn0b7aoJP1QVESNxMMmkS8z9R05oWApYVk4U+T6wSdEUeGqKEjcfrgsZNx+Pg0snhzxpoWYUQR56yVVP19LBJuhVzqdHLhbW7gkm1IV1BseJtLQSIMxvX9LL/aad8acdVIQ6f6GtRb1V1au38prUQQOVqUE9y2JClZoiP5VR7kE1WtDwehnKr5K/UMyd+YV8ZJSIPQJLvn1P18sn7SQk22+gHYb3t57INyzODDGPdAwvHBYmBMw1T4d+Af2e8wbh9JkEZrjIMA2cP+rKYyKgYwctInpFHD8HBzZ7djLpRke8DwMVaZbafLsKldiLxdcIeAmThlKXUHF5bXkq/Y23v0vrn

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
