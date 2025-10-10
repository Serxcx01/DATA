bot = getBot()

function say(od)
    bot:say(od)
end

function Kegiatan(od)
    bot.custom_status = od
end

function StatusBot(detail)
    local OdStatus = {
        [BotStatus.online] = "online",
        [BotStatus.wrong_password] = "wrong",
        [BotStatus.account_banned] = "acc banned",
        [BotStatus.account_suspended] = "acc banned",
        [BotStatus.location_banned] = "ip banned",
        [BotStatus.too_many_login] = "too many",
        [BotStatus.version_update] = "update version",
        [BotStatus.maintenance] = "maintenance",
        [BotStatus.advanced_account_protection] = "AAP",
        [BotStatus.http_block] = "HTTP Block",
        [BotStatus.mod_entered ] = "Mod Entered",
        [BotStatus.changing_subserver ] = "Subserver",
        [BotStatus.bad_gateway] = "Bad Gateway",
        [BotStatus.server_issue] = "Server Issue",
        [BotStatus.retrieving_token] = "Retrieving Token",
        [BotStatus.logon_fail] = "Login Fail",
        [BotStatus.error_connecting] = "Ercon",
        [BotStatus.banwave_detected] = "Banwave",
    }

    local erS
    if detail then
        erS = OdStatus[detail.status]
    else
        erS = OdStatus[bot.status]
    end
    
    if not erS then
        erS = "offline"
    end
    return erS
end

function StatusGoogle(detail)
    local OdGoogle = {
        [GoogleStatus.idle] = "Idle",
        [GoogleStatus.processing] = "Processing",
        [GoogleStatus.init_error] = "Init Error",
        [GoogleStatus.invalid_credentials] = "Inv Credentials",
        [GoogleStatus.account_disabled] = "Acc Disabled",
        [GoogleStatus.captcha_required] = "Captcha Required",
        [GoogleStatus.phone_required] = "Phone Required",
        [GoogleStatus.recovery_required] = "Recovery Required",
        [GoogleStatus.couldnt_verify] = "Couldnt Verify",
        [GoogleStatus.unknown_url] = "Unknown URL"
    }

    local erG
    if detail then
        erG = OdGoogle[detail.google_status]
    else
        erG = OdGoogle[bot.google_status]
    end
    
    if not erG then
        erG = "Idle"
    end
    return erG
end

function StatusAllBot()
    local act = 0
    local nonact = 0
    local ban = 0
    local chapc = 0
    local iner = 0
    local permata = 0
    local obt_permata = 0

    for _, erBot in pairs(getBots()) do
        local statusb = StatusBot(erBot)
        local statusg = StatusGoogle(erBot)
        permata = permata + erBot.gem_count
        obt_permata = obt_permata + erBot.obtained_gem_count

        if statusb == "online" then
            act = act + 1
        elseif statusb ~= "online" and statusb ~= "acc banned" then
            nonact = nonact + 1
        elseif statusb == "acc banned" then
            ban = ban + 1
        end

        if statusg == "Captcha Required" or statusg == "Couldnt Verify" then
            chapc = chapc + 1
        elseif statusg == "Init Error" then
            iner = iner + 1
        end
    end

    return act, nonact, ban, permata, obt_permata, chapc, iner
end

function GetMaladyName()
    local maladies = {
        [0] = "Healthy",
        [1] = "Torn Punching Muscle",
        [2] = "Gem Cuts",
        [3] = "Chicken Feet",
        [4] = "Grumbleteeth",
        [5] = "Broken Heart",
        [6] = "Chaos Infection",
        [7] = "Moldy Guts",
        [8] = "Brainworms",
        [9] = "Lupus",
        [10] = "Ecto-Bones",
        [11] = "Fatty Liver"
    }

    local maladyName = maladies[bot.malady]

    if not maladyName then
        maladyName = "Healthy"
    end

    return maladyName
end

function OdBot()
    if not GuestAkun then
        erine = bot.name
    else
        if not erine then
            if bot:isInWorld() then
                erine = getLocal().name
            else
                erine = bot.name
            end
        else
            if not string.match(erine, "_%d+") then
                if bot:isInWorld() then
                    erine = getLocal().name
                else
                    erine = bot.name
                end
            end
        end
    end

    return {
        world = bot:getWorld().name,
        name = erine,
        x = bot.x,
        y = bot.y,
        level = bot.level,
        status = StatusBot(),
        gems = bot.gem_count,
        items = bot:getInventory().itemcount,
        slots = bot:getInventory().slotcount,
    }
end

function getPlayers()
    world = bot:getWorld()
    local orang = {}
    for _,ppl in pairs(world:getPlayers()) do
        table.insert(orang, { name = ppl.name, userid = ppl.userid, netid = ppl.netid, country = ppl.country, x = math.floor(ppl.posx / 32), y = math.floor(ppl.posy / 32)})
    end
    return orang
end

function wear(id)
    bot:wear(id)
end

function unwear(id)
    bot:unwear(id)
end

function getPing()
    return bot:getPing()
end

function findItem(id)
    if id == 112 then
        return OdBot().gems
    end
    item = bot:getInventory():findItem(id)
    if item == nil then
        return 0
    else
        return item
    end
end

function findClothes(id)
    return bot:getInventory():getItem(id).isActive
end

function collect(erin)
    bot:collect(erin, 100)
end

function formatUang(nilai)
    local formatted = tostring(nilai)    
    local result = formatted:reverse():gsub("(%d%d%d)", "%1."):reverse()
    
    if result:sub(1, 1) == "." then
        result = result:sub(2)
    end
    
    return result
end

function findPath(x,y)
    bot:findPath(x,y)
end

function wrench(x, y)
    bot:wrench(bot.x + x, bot.y + y)
end

function punch(x, y)
    bot:hit(bot.x + x, bot.y + y)
end

function place(id, x, y)
    bot:place(bot.x + x, bot.y + y, id)
end

function sendPacket(typ, pkt)
    bot:sendPacket(typ, pkt)
end

function drop(id, count)
    if count then
        bot:drop(id, count)
    else
        bot:drop(id, findItem(id))
    end
end

function trash(id, count)
    if count then
        bot:trash(id, count)
    else
        bot:trash(id, findItem(id))
    end
end

function convertMS(ms)
    return ms / 1000
end

CollectInterval = CollectInterval or 200
ObjectCollectDelay = ObjectCollectDelay or 100

function collectSet(erin, jarak)
    bot:setInterval(Action.collect, convertMS(CollectInterval))
    bot.object_collect_delay = ObjectCollectDelay
    bot.collect_range = jarak
    bot.auto_collect = erin
end

function disconnect()
    bot:disconnect()
end

function connect()
    bot:connect()
end

function getTile(x, y)
    if not bot:isInWorld() or x < 0 or x > 99 or y < 0 or y > 53 then
        return {
            fg = 9999,
            bg = 9999,
            flags = 0,
            ready = false,
            access = 0,
        }
    end

    local world = bot:getWorld()
    local tile = world:getTile(x, y)

    if not tile then
        return {
            fg = 9999,
            bg = 9999,
            flags = 0,
            ready = false,
            access = 0,
        }
    end

    return {
        fg = tile.fg or 0,
        bg = tile.bg or 0,
        flags = tile.flags or 0,
        ready = tile.canHarvest and tile:canHarvest() or false,
        access = world.hasAccess and world:hasAccess(x, y) or 0,
    }
end

function getInventory()
    local tas = {}
    for _,bag in pairs(bot:getInventory():getItems()) do
        table.insert(tas, { id = bag.id, count = bag.count})
    end
    return tas
end

function getTiles()
    world = bot:getWorld()
    local tiles = {}
    for _,tile in pairs(world:getTiles()) do
        if bot:isInWorld() then
            table.insert(tiles, { x = tile.x, y = tile.y, fg = tile.fg, bg = tile.bg, ready = tile:canHarvest(), flags = tile.flags})
        end
    end
    return tiles
end

function getObjects()
    world = bot:getWorld()
    local object = {}
    for _,obj in pairs(world:getObjects()) do
        table.insert(object, { x = obj.x, y = obj.y, id = obj.id, oid = obj.oid, count = obj.count, flags = obj.flags})
    end
    return object
end

function getClothes()
    local items = {}
    for _, item in pairs(getBot():getInventory():getItems()) do
        if getInfo(item.id).clothing_type > 0 then
            table.insert(items, { id = item.id, name = getInfo(item.id).name, type = getInfo(item.id).clothing_type})
        end
    end
    return items
end

function GetNameID(id)
    local info = getInfo(tonumber(id))
    if info and info.name then
        return info.name
    end
    return "Unknown Item - "..id
end

function ItemName(id)
    local IconItem = {
        [2382] = "<:2382:1296875147411591261>",
        [2292] = "<:2292:1296883683873001502>",
        [2294] = "<:2294:1296883814706184242>",
        [2296] = "<:2296:1296883678403756098>",
        [2298] = "<:2298:1296883676260597760>",
        [2300] = "<:2300:1296883674020581376>",
        [2308] = "<:2308:1296883671537815576>",
        [2310] = "<:2310:1296883668937216040>",
        [2312] = "<:2312:1296883666638868581>",
        [2314] = "<:2314:1296883664122155050>",
        [2316] = "<:2316:1296883657008480266>",
        [2320] = "<:2320:1296883654785634304>",
        [2322] = "<:2322:1296883652491214920>",
        [2324] = "<:2324:1296883650612170795>",
        [2326] = "<:2326:1296883648842301452>",
        [2328] = "<:2328:1296883646778576978>",
        [2332] = "<:2332:1296883644643807232>",
        [2334] = "<:2334:1296883642488066229>",
        [2336] = "<:2336:1296883640382263306>",
        [2338] = "<:2338:1296883638100557844>",
        [2340] = "<:2340:1296883636112592926>",
        [5706] = "<:5706:1296885688154984579>"
    }
    if IconItem[id] then
        return IconItem[id]
    end
    return "[" .. GetNameID(id) .. "]"
end

function warp(Dunia, Kunci)
    CurrentWorld = OdBot().world:upper()
    if CurrentWorld ~= Dunia:upper() and CurrentWorld ~= "EXIT" then
        bot:leaveWorld()
        sleep(2000)
    end
    if Kunci then
        bot:warp(Dunia.."|"..Kunci)
    else
        bot:warp(Dunia)
    end
end

function buy(pek)
    sendPacket(2, "action|buy\nitem|"..pek)
end

function Upgrades()
    sendPacket(2, "action|buy\nitem|upgrade_backpack")
end

Server_Ohdear = "http://47.251.174.22"