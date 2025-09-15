--- SC LOGIN ANDRE

local accounts = [[
joykillme662@gmail.com|D2:E4:C8:D9:3F:0F:A9D0D403852635A062F0FC3E7007383F:7B5FBF49B6F0A8FC435DACC917F6D7E9:n8UC27cBpu1WedJRy8\/A8TcRbMFl6lroLEbqGBEHNDvRmOXDlm1ngr\/uTZ2o50EcqV4x4IgM8\/EKkzSdr5q05nA2AApU7phJ0KDYkO26aIsrkOmB7WQq0ma5yo48D\/UFcPfqmIjqMS5eB+pUEqg9+FCLsPJwtwMCJDB9qoUsnqRA9HfkhCuj08A4zM7cmqDtf+fXclMqFHALUJzOMBykxeTujBxFemwn9ksDAYBWGVQFLZgBPKFny+gQFa4SHKlq5jsCnV8x+noEbX66ugaYAnG9d5AxgpO5xCog1xb4eckO2HNJIkZwqqG58c7Ho3NDJT5BYk5RfcZyLuYJCnWtU\/MqzYz9O7XB7UkGEvv2uPNZ0\/l+0QjFxJqWwkJkLs9nRYEiRW0mxgZAp8lC5u2iwy5Tptjy4g4FcRSBG+OISXL0YPIj9byhtFBqJvkVVzLKge6td7fnxD8jla63\/t13SQ==

]]

-- lidarui341@gmail.com|0B:03:98:B1:AF:E4:8E6A5B8347E27B4609D3D931CF0453A5:ACC10FCC54991C73AEAC6462BC9F71B0:WgVhUkRg0qNhT6pY1HrfmxCdSoH4p4xuoCTo31i3TFn66QJdYB7i26Fo9Sm9L0l6kgz1P1eGlEFoMFNo3bGhBiZk7cUQ3m7Sjvmn0LeVWZ4CifetuxELDzhi7KS1vPvK8uTep11NfE3xnIsdT4FSvT4nGvfrt7Gb1cKuaIQ9i82EM/U1rsdFaplcuYvcpwKYXRbnjKGj5fz0MJEiSwDQPenHD5dJOshw102YcBrEabJaxZASMSklyYOh0uwTY5Nz4B3ohP0l0gFJe8sce7i+ZyXeZ69KkMUaWlMn3rDnioKg/YiO4UDA5wh52LloGzzh51LRYZPrPczte2THK0I5HFSjk+cTzO6iwmODZXxzU1gMa9YZH80OP6j2dhML/DsF9djlBTXDurohbWuDyChj6DxoC30OkZ0GkAgFsQygtXMd3V06b/r1H6CDtl7Fq5B2eJx2n+lasmddZwq3b1AfuQ==
-- local email, mac, rid, wk, ltoken = account:match("([^|]+)|([^|]+):([^|]+):([^|]+):(.+)")










worldBFG = "YXIS"
bot_bypass = false


function zeeBot(bot)
    -- local bot = getBot()  -- Mengambil getBot() satu kali untuk menghindari pemanggilan berulang
    local Status
    if bot.status == BotStatus.online and bot.status == 1 then
        Status = "online"
    elseif bot.status == BotStatus.offline and bot.status ~= 1 then
        Status = "offline"
    elseif bot.status == BotStatus.wrong_password then
        Status = "Wrong Password"
    elseif bot.status == BotStatus.account_banned then
        Status = "Banned"
    elseif bot.status == BotStatus.location_banned then
        Status = "Location Banned"
    elseif bot.status == BotStatus.version_update then
        Status = "Version Update"
    elseif bot.status == BotStatus.advanced_account_protection then
        Status = "Advanced Account Protection"
    elseif bot.status == BotStatus.server_overload then
        Status = "Server Overload"
    elseif bot.status == BotStatus.too_many_login then
        Status = "Too Many Login"
    elseif bot.status == BotStatus.maintenance then
        Status = "Maintenance"
    elseif bot.status == BotStatus.http_block then
        Status = "Http Block"
    elseif bot.status == BotStatus.captcha_requested then
        Status = "Captcha Requested"
    elseif bot.status == BotStatus.error_connecting then
        Status = "Error Connecting"
    end

    return {
        world = bot:getWorld().name,
        name = bot.name,
        level = bot.level,
        status = Status,
        gems = bot.gem_count,
        slots = bot:getInventory().slotcount,
        getdoor = getTile(bot.x, bot.y).fg == 6,
    }
end

function warpnow(world, bot)
    warp_time = 0
    while bot:getWorld().name ~= world do
        while bot.status ~= BotStatus.online and bot.status ~= 1 do
            bot:connect()
            sleep(10000)
        end
        bot:warp(string.upper(world))
        sleep(7000)
        warp_time = warp_time + 1
        if warp_time >= 5 then
            sleep(8000)
        end
    end
end

function take_remote(bot)
    ex = math.floor(bot:getWorld():getLocal().posx/32) + 0
    ye = math.floor(bot:getWorld():getLocal().posy/32) - 1
    bot:wrench(ex,ye)
    sleep(3000)
    bot:sendPacket(2,"action|dialog_return\ndialog_name|itemsucker\ntilex|"..(ex).."|\ntiley|"..(ye).."|\nbuttonClicked|getplantationdevice")
    sleep(3000)
end



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
        -- sleep(3)
        -- while true do
        --     if bot.level >= 6 then
        --         warpnow(worldBFG, bot)
        --         tile_skip = 0
        --         get_tile_world = bot:getWorld()
        --         for _,tile in pairs(get_tile_world:getTilesSafe()) do
        --             tile_skip = tile_skip + 1
        --             if tile_skip >= 4 then
        --                 if bot:getWorld():getTile(tile.x, tile.y).fg == 5638 then
        --                     bot:findPath(tile.x,tile.y + 1)
        --                     sleep(1000)
        --                     take_remote(bot)
        --                     sleep(100)
        --                 end
        --             end
        --         end
        --         bot:leaveWorld()
        --         break
        --     end
        -- end
    end
end
