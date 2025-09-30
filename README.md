storageWorld = "FENCEPAPA1"
bot = getBot()
function round(n)
    return n % 1 > 0.5 and math.ceil(n) or math.floor(n)
end

function faceSide2()
    local packet = GameUpdatePacket.new()
    packet.type = 0
    packet.flags = 32
    bot:sendRaw(packet)
end

function warp(world)
    cok = 0
    nuked = false
    while getBot().world ~= world:upper() and not nuked do
        bot:warp(world or ""):upper()
        sleep(5000)
        if cok == 7 then
            nuked = true
        else
            cok = cok + 1
        end
    end
end

function take(id)
    warp(storageWorld)
    sleep(100)
    for _,obj in pairs(getObjects()) do
        if obj.id == id then
            findPath(round(obj.x/32),math.floor(obj.y/32))
            sleep(1000)
            collect(2)
            sleep(1000)
            if findItem(id) > 0 then
                break  
            end
        end
    end
    if bot:getInventory():getItemCount(id) > 1 then
      faceSide2()
      sleep(100)
      bot:drop(id,bot:getInventory():getItemCount(id) - 1)
      sleep(500)
      bot:leaveWorld()
    end
end

take(226)
