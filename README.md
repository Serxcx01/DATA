bot = getBot()

function findHomeWorld(variant, netid)
    if variant:get(0):getString() == "OnRequestWorldSelectMenu" and variant:get(1):getString():find("Your Worlds") then
        local text = variant:get(1):getString()
        local lines = {}
        for line in text:gmatch("[^\r\n]+") do
            table.insert(lines, line)
        end
        for i, value in ipairs(lines) do
            if i == 3 then
                kalimat = lines[3]
                local nilai = kalimat:match("|([a-zA-Z0-9%s]+)|"):gsub("|", ""):gsub("%s", "")
                worldTutor = nilai
                printLog("Tutorial World: "..worldTutor)
            end
        end
    end
end

function checkTutor()
    while bot:isInWorld() do
        bot:leaveWorld()
        sleep(3000)
    end

    worldTutor = ""
    noHomeWorld = false
    printLog("Checking Tutorial/Home World")

    addEvent(Event.variantlist, findHomeWorld)
    for i = 1, 3 do
        if worldTutor == "" and bot:getWorld().name:upper() == "EXIT" then
            bot:sendPacket(3,"action|world_button\nname|_16")
            listenEvents(5)
        end
    end

    if worldTutor == "" then
        printCrit("Doesn't Have Tutorial/Home World!")
        callNotif("Doesn't Have Tutorial/Home World!", true)
        noHomeWorld = true
    end
    
    sleep(100)
    removeEvent(Event.variantlist)
end

checkTutor()
