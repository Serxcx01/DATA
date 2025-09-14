-- Script BY ZCScript [DONT REMOVE AND RESELL]
worldList = {
"FQZMSFAFXO|RITASLAYER1",
"OCLSRIFJQL|RITASLAYER1",
"GZWSFKPEPW|RITASLAYER1",
"HNMPFJTXQT|RITASLAYER1",
"TMZNZVAPFV|RITASLAYER1",
"JCKIPLAZFI|RITASLAYER1",
"YQNHGXDBKE|RITASLAYER1",
"TYRLPEKV|RITASLAYER1",
"FTKRNKRREE|RITASLAYER1",
"TMCAYABK|RITASLAYER1",
"AEDOCPKUOG|RITASLAYER1",
"JJUUGTNFZC|RITASLAYER1",
"PMUQTJHSNP|RITASLAYER1",
"FVHBWAIKMG|RITASLAYER1",
"XJFCWYPAEX|RITASLAYER1",
"QWRCBHAE|RITASLAYER1",
"XEHCVPJSTG|RITASLAYER1",
"DZEKOKHRNS|RITASLAYER1",
"IFUTFSYZ|RITASLAYER1",
"ROHRTHQXKG|RITASLAYER1",
"RRUUWKOBJU|RITASLAYER1",
"DPPOWWWR|RITASLAYER1",
"CCKZFYDL|RITASLAYER1",
"XLKKXNHG|RITASLAYER1",
"CZFGXLOAWI|RITASLAYER1",
"YKGFEUUJKW|RITASLAYER1",
"JGHHUIKFRZ|RITASLAYER1",
"KHAZUWEOTG|RITASLAYER1",
"JYUZSERMOO|RITASLAYER1",
"UYRJACUE|RITASLAYER1",
"KZUZBXBYEM|RITASLAYER1",
"OSVDOLNENN|RITASLAYER1",
"RDJKHEBUKG|RITASLAYER1",
"AGKHLUJP|RITASLAYER1",
"YNFICDMNHJ|RITASLAYER1",
"GIJQPKVB|RITASLAYER1",
"LLSRNOPKLT|RITASLAYER1",
"FODJVUBXIQ|RITASLAYER1",
"CGMBHWZJCW|RITASLAYER1",
"TTLIMKKY|RITASLAYER1",
"OVVGFWBE|RITASLAYER1",
"SWWPZYALEU|RITASLAYER1",
"VRROEOJM|RITASLAYER1",
"JCAJKYBV|RITASLAYER1",
"MGKHRJCX|RITASLAYER1",
"QYPPPSCN|RITASLAYER1",
"ARYQWNXP|RITASLAYER1",
"IJSGVXKF|RITASLAYER1",
"ZTPPTFZS|RITASLAYER1",
"JSEOMXPZ|RITASLAYER1",
"SFMEMIPK|RITASLAYER1",
"KTKUAJWU|RITASLAYER1",
"QZVDTZGZ|RITASLAYER1",
"CPYOWRSB|RITASLAYER1",
"CDAGBNVC|RITASLAYER1",
"CAHHVNNN|RITASLAYER1",
"XHJHAEVY|RITASLAYER1",
"ALOOFIGB|RITASLAYER1",
"AVILCSLV|RITASLAYER1",
"DOPTJHPZ|RITASLAYER1",
"PHAWEYDD|RITASLAYER1",
"DBGKKISO|RITASLAYER1",
"TXKKEXJKRY|RITASLAYER1",
"WEIBWHAMKK|RITASLAYER1",
"IXGUWVIAAH|RITASLAYER1",
"RZPAKQFF|RITASLAYER1",
"PDDXRYAT|RITASLAYER1",
"UVBXSCJEAE|RITASLAYER1",
"VSAJSYVVFQ|RITASLAYER1",
"NIIEHWHHYU|RITASLAYER1",
"NQMNEVEBQP|RITASLAYER1",
"NLHSARMFAX|RITASLAYER1",
"DGMUGHGO|RITASLAYER1",
"YVCWXAGUPR|RITASLAYER1",
"LJLAVBTP|RITASLAYER1",
"CSKSTOGZHM|RITASLAYER1",
"BBUYKUONKI|RITASLAYER1",
"MDAPFJHJED|RITASLAYER1",
"WUBMFPORWF|RITASLAYER1",
"LMHRUAIZ|RITASLAYER1",
"UERFGBGZ|RITASLAYER1",
"EIIJGOPS|RITASLAYER1",
"HMLAVHLYER|RITASLAYER1",
"TPXTYCXMAH|RITASLAYER1",
"OCELLUFOBV|RITASLAYER1",
"IUDXRJPDYZ|RITASLAYER1",
"DQWBIPSQTJ|RITASLAYER1",
"CGKTVCZIVO|RITASLAYER1",
"UEWMNKNYJA|RITASLAYER1",
"CYQXXLKW|RITASLAYER1",
"NPLCWCHZMM|RITASLAYER1",
"WKVHUPZGIE|RITASLAYER1",
"XEQECMNF|RITASLAYER1",
"XDLLRJLAWD|RITASLAYER1",
"HYRQCEUP|RITASLAYER1",
"ACUHQLKP|RITASLAYER1",
"RPBRDLJY|RITASLAYER1",
"VGJNPTCK|RITASLAYER1",
}
doorEdit = "UTHIS01"

fileSuccesChange = "success.txt"
fileFailChange = "fail.txt"

delayWarp = 8500
delayHardWarp = 60000
delayReconnect = 15000
------------------------------------------------------------------------------------------------------------------------------------------------
client = getBot()
client_world = client:getWorld()

isLocked = false
successEdit = false

client.auto_reconnect = false 

function splitString(str, special)
    local rows = {}
    delimiter = special
    for row in str:gmatch("[^"..delimiter.."]+") do
        table.insert(rows, row)
    end
    return rows
end

addEvent(Event.variantlist, function(variant, netid)
    if variant:get(0):getString() == "OnConsoleMessage" then
        message = variant:get(1):getString()
        if message:find("That world is inaccessible") then 
            nuked = true
        end
        unlistenEvents()
    elseif variant:get(0):getString() == "OnDialogRequest" then
        local message = variant:get(1):getString()
        if message:find("end_dialog|door_edit") then
            if message:find("add_text_input|door_id|ID|"..doorEdit.."|") then successEdit = true else client:sendPacket(2, string.format("action|dialog_return\ndialog_name|door_edit\ntilex|%d|\ntiley|%d|\ndoor_name|ZCScript\ndoor_target|\ndoor_id|"..doorEdit , message:match("tilex|(%d+)"), message:match("tiley|(%d+)"))) end
        end
        unlistenEvents()
    end
end)

function join(world, id)
    local door, hw = 0, 0
    local check = (id and id ~= "") and true or false
    if client_world.name ~= world then 
        while client_world.name ~= world and not nuked do 
            if check then client:warp(world..'|'..id) else client:warp(world) end 
            listenEvents(math.floor(delayWarp/1000))
            if hw >= 4 then 
                if client_world.name ~= world then 
                    client:disconnect()
                    sleep(delayHardWarp)
                end 
                reconnect()
                hw = 0 
            else hw = hw + 1 end 
            reconnect()
        end 
    end 
    if check and not nuked then 
        while client_world:getTile(client.x, client.y).fg == 6 and not nuked and not wrongId do 
            client:warp(world..'|'..id)
            listenEvents(math.floor(delayWarp/1000))
            if door >= 6 then
                if client_world:getTile(client.x, client.y).fg == 6 then
                    wrongId = true 
                end 
                door = 0 
            else door = door + 1 end 
            reconnect()
        end 
    end 
end

function reconnect(world, id)
    if client.status ~= BotStatus.online then 
        while client.status ~= BotStatus.online do 
            client:connect()
            sleep(delayReconnect)
            if client.status == BotStatus.account_banned then 
                print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Your account got banned!")
                client:stopScript()
            end
            if client.status == BotStatus.online then 
                if world ~= "" and world then 
                    if id ~= "" and id then 
                        join(world, id)
                    else 
                        join(world)
                    end 
                end 
            end 
        end 
        print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Success reconnecting!")
    end 
end

function changeDoor(world, id)
    if client_world:hasAccess(client.x, client.y) > 0 then 
        while getInfo(client_world:getTile(client.x, client.y).fg).action_type == 2 and not successEdit do
            client:wrench(client.x, client.y)
            listenEvents(5)
            reconnect(world, id)
        end
        successEdit = false 
    else 
        isLocked = true 
        return false 
    end 
end

i = 1
while i <= #worldList do 
    world, doors = splitString(worldList[i], "|")[1], splitString(worldList[i], "|")[2]
    join(world, doors)
    if not nuked and not wrongId then 
        changeDoor(world, doors)
        if not isLocked then
            append(fileSuccesChange, world.."|"..doors)
            print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Success changing id "..world.." !")
        else
            append(fileFailChange, world.."|"..doors.."|LOCKED")
            print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Failed changing id in "..world.." because bot doesn't have access!")
            isLocked = false
        end
    elseif nuked then
        nuked = false 
        append(fileFailChange, world.."|"..doors.."|NUKED")
        print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Failed to join world because "..world.." got nuked!")
    elseif wrongId then
        wrongId = false
        append(fileFailChange, world.."|"..doors.."|WRONG")
        print("[ZCScript] [CHANGE DOOR] ["..client.name:upper().."] Failed to join world because "..world.." have wrong id!")
    end 
    if i <= #worldList then
        i = i + 1
    end 
    sleep(100)
end
