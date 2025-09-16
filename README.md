---- SC AP
local bots = [[
DF0D3EE7A068AC9AB12CB8F41C38F920|d0gW0x40db7wGdcF2Tq3KfaZ10IzbwR9Q5LSkHIwWp4NzAJOBDV3zEhYNk0zZlZA/0U9PrPzVvdagvTN10Tjdpn8Nclsjq5XEsfb7rSDieM8Q7tgY1rb+bIrUnDCQzS5NSsIgwmKKq9rXn0TBi2sLeeQJpzwibFexQUftyfZzSb61LHggxPCHth6Uql42TJoluWXxdp+/kZxFgP0F8C1FaXjh/KAjneU4/V2B93Ln8v4oiUp4/e14hsJn3oS39VY/qfUOE9v4FaIVeetxuNRWVSewvHV26Roxcv7D8z6roWevY2cuGz3LOtlZlIQ+17u8fmEw3geJZaajQ/di5HFwWYoA/HK+PcYSt/dWvwDDexv6SqZTeGGc3Zwb0GKaFCFPb43yN9YbJlTPC2L/iMZxRsCdlLaGl3uSKoKSEZ30YLrUpjjCpApWXQn62mkWDRq9co1zHvmX7lleDTkPowFHB2jxBCZYqtDCLQMtYijoM68uZ1MA+jLkegvITjU3PFZ

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
