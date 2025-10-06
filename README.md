--- SC LOGIN ANDRE

local accounts = [[
lidarui341@gmail.com|8B:AF:9C:DC:F6:43:C801ED6707FDEDA4025046EB8B06F9C2:E787A62FE4CB4B40A81FDCCAFA22D2B6:HKwlXYN449mKtfRcvfcobz0zpBuLTWjZhod08KJIovw0XPIlFRcHlWMmMP\/hufK0MsECmgiblH0Ri\/+twkbB7bW5k2Tm7YvuzP01MOb0t8bu1Zs6YX5Vsx97HvxX8wYusgcQ0mo2dJStkg5zFMAqIke7JmqoLJQvxaz3qsOch+Y3vzkpEm7eiChXLz0iku+Jysw+r3t4PClm48nJYD+uXKwd1o71XLxK3jNsTgjkPeu\/wsKZ2+65fhzyzqcQOdahrPuskkp7uOSb1iQ4r\/Yt0iEint6ti+5ooLsYqHQDt2fqdaxgUjYtj70uKjG51v736NiKPqmcaY8BDJx2yWawpgeefSBlp+ZlxbVBAl42L6VG4LWHgLt3h4bZCZoD3xPEYZWen2Doi6yFieYw22x8p4mO2OdDKXeNPE1KK3KtHsSyrjB+8+shmFmoRno69HC1aI1UAAGsh+t+gXuQkJ5Z8A==


]]


for account in accounts:gmatch("[^\n]+") do
    local email, mac, rid, wk, ltoken = account:match("([^|]+)|([^|]+):([^|]+):([^|]+):(.+)")
    if mac and rid and wk and ltoken then
        local details = {
            ["display"] = email,
            ["secret"] = email,
            ["name"] = ltoken, 
            ["rid"] = rid,
            ["mac"] = mac,
            ["wk"] = wk,
            ["platform"] = 0,
        }

        local bot = addBot(details)
        sleep(100)
        -- local bot = addBot(details, "", "", "", Platform.android)
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
    end
end
