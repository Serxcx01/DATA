--- SC LOGIN WUTWUT

local data = [[
khoicao736@gmail.com|00:35:63:06:69:6F|3487F3B03586E6D9030EF91D27D50082|CB21B4567F57E800082DAA63845C3E7D|gmxpkScDukvSammPdCQm7wmt4aJLIunjpNv4xVJGAwwUTCh8jB9dwKHicI+ZNmBx789h1T92XDQK62Uyye39KKf6jm7Fn1HbhC90CxTfTmrjAe/nrQ7SwB6zoS6U5P5q1G59Km7Zbsd++BiitwEzO0h9IIroKQRbPthXCT3JDYB3A13uZMZBTCOBKhtHTkIRdbhjZoxzMgL7mGpv70ueiDjlmS6taqos5AkdauHg/GdcQg93BNcfdmaG+09bCTk0s1QreKTXe9OllSXtpaH46BuKRP/zvR6rhy3yZOqlPT6VXRGZH/pajvp6FlBAKgJ96Rmxc4jHEP4qvZgIDhlVJYa01b9tfr3uqlrYUPojmKAytQInUSEQvycgBnWBb/HBnA3O8daFpwxiUk5/beUAWiqq5R+SRywCYk0Q3GxWn2GJurEGXCApQBC91JU2wRWgCgGujYRsebrOOu9RBWoJ4g==
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
