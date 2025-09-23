--- SC LOGIN ANDRE

local accounts = [[
lidarui341@gmail.com|AA:77:DF:C8:3A:A0:A8FA30D0E77DD41961536D3ACB66417B:3A97175F52ADAB3C2E986399917070B4:WgVhUkRg0qNhT6pY1HrfmxCdSoH4p4xuoCTo31i3TFmvjadd9VVpgmFT\/mPEArXfMXj\/hpq3EccNrio\/gu\/rMlTaLruPqDDCvpWIxSx7vc6\/5KV4qTIPIIlGVJ9arLS0YFO+qhwwHtxYMyBEBhOM5ziFBFQ8qsOyfo74GpybuB2D5NbpO\/14lC+yDg1TMGmj8qRi9uJoL\/wbFGZqR6kSrExi494WhLU1kC3KMr6ravtmcrzGNQaIxw\/qrY\/CPVeMpkI6Eb0PGELIfpUUTBX\/46S8S4jk86wEcUAZFeJ2mXg0xjxjspP0Pv1gpFFWZ1zoFQG\/+hi8BT3UBzcuU6AQE19xWUl+QuHHATSrQt6Rj4kFxftXf0NFjqV5SPHzO5DtbuaVYN5TexDLkVCw7yDEXv40cLVYKDmZlgk7hBMvk4Ye1R1Gf8rwnu+hzZKB13BNmO894A44Btykv7L4V3kBlQ==


]]
-- lidarui341@gmail.com|95:90:7D:69:3A:9E:FE95BB0A92FE871C300C70C8723B8AA1:32AAFFAF9431C48CA92BA31664B088A6:WgVhUkRg0qNhT6pY1HrfmxCdSoH4p4xuoCTo31i3TFkdGomdNgJcldClC2TT4OxS4C2bNcgLA7C\/HHPKccTNTxrpeBV2bDYXaZ96QWv11XGWWjE2dCbUoHarp6B2WKJgDPwRsA7N7BOkoFsHQJqojGamflHO9iceQo\/eJDb4S5YIEhNxZGxwS9po7ZYa1X50I+SRllt9JzEYJnQET38RNVcdj3Q0ZtYlwWPjpAfD++\/Llckw411\/8MSm9XztOuqL7ZtlXDcztcY0QzebQ\/UV6mO38KQnlACeTs4KkeTlxwT0\/obV2\/Y1lVmBnbIkegjHXuPo4UCmS0c5lblLj\/4P4ZwVm8mjFzDU3p9Oss9qHRmNH4uMRu8RdiojYRO9rjQgoXCk1Co8SIFVBZFtRZ\/r1gRy7+zI6rJjxgViUnwO3CLem3ZhFG3c6lVgOOLcH1Rz3rJVbnTxD0oU++QcrRtOIg==

-- lidarui341@gmail.com|0B:03:98:B1:AF:E4:8E6A5B8347E27B4609D3D931CF0453A5:ACC10FCC54991C73AEAC6462BC9F71B0:WgVhUkRg0qNhT6pY1HrfmxCdSoH4p4xuoCTo31i3TFn66QJdYB7i26Fo9Sm9L0l6kgz1P1eGlEFoMFNo3bGhBiZk7cUQ3m7Sjvmn0LeVWZ4CifetuxELDzhi7KS1vPvK8uTep11NfE3xnIsdT4FSvT4nGvfrt7Gb1cKuaIQ9i82EM/U1rsdFaplcuYvcpwKYXRbnjKGj5fz0MJEiSwDQPenHD5dJOshw102YcBrEabJaxZASMSklyYOh0uwTY5Nz4B3ohP0l0gFJe8sce7i+ZyXeZ69KkMUaWlMn3rDnioKg/YiO4UDA5wh52LloGzzh51LRYZPrPczte2THK0I5HFSjk+cTzO6iwmODZXxzU1gMa9YZH80OP6j2dhML/DsF9djlBTXDurohbWuDyChj6DxoC30OkZ0GkAgFsQygtXMd3V06b/r1H6CDtl7Fq5B2eJx2n+lasmddZwq3b1AfuQ==
-- local email, mac, rid, wk, ltoken = account:match("([^|]+)|([^|]+):([^|]+):([^|]+):(.+)")


-- andresaputra011105@gmail.com|1D:34:B4:69:87:DC:AD2AAD5D775861EE8D75E8D7E4BBC296:F0790D608BBDEBD2F0FCDF92FC1FEA99:P19SRdj1keCwEZTRAWRWFGRK2ukec65oBAu1oem\/tfrHonfqB+sZFNWXt\/REu3qBbdwC8vytfd0OzHzxnJpYPmxu85v6Fv2EzVscjiWaiztkqQLEMCYjAfwlQ3YCNDvux\/xfcgOQr85PF8lbsbE2yy2ab3+L4WjiN69BbHBapizhS++o2UI4vLojftkCB\/s6Pxqe0+MYzocfGKdFXBZvv94shwl\/\/QUmHA3pt0jpA5TOhtrx6yoplczapTggwgJsNjKyJSZD1+4r3DiNy7z6zmGQ\/Mrn+djM7BXpSGItu4V2ME\/cg6BFJOWaX+uTQLyLjOQmhS0HzD3X+diz1CD2PwwEkKgVolqB+7Weo0wFTF7zdEWtBod\/81PardAoBxIWh2pYwBd5fONyUGMnssIigzCHAIayK0tkWjaICjshAgxTQqgaBe2o\/XYZdG6eH\/huemODSLMUHVVKXeB8HWwcRA==








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
