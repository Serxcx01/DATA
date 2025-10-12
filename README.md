function findHomeWorld(variant, netid)
  if variant:get(0):getString() == "OnRequestWorldSelectMenu"
      and variant:get(1):getString():find("Your Worlds") then
    local text = variant:get(1):getString()
    local lines = {}
    for line in text:gmatch("[^\r\n]+") do table.insert(lines, line) end
    for i, value in ipairs(lines) do
      if i == 3 then
        local kalimat = lines[3]
        local nilai = kalimat:match("|([a-zA-Z0-9%s]+)|")
        if nilai then nilai = nilai:gsub("%s", ""); worldTutor = nilai; print("Tutorial World: " .. worldTutor) end
      end
    end
  end
end

function checkTutor()
  local bot=getBot and getBot()
  while bot:isInWorld() do bot:leaveWorld(); sleep(3000) end
  worldTutor = ""; noHomeWorld = false
  print("Checking Tutorial/Home World")
  addEvent(Event.variantlist, findHomeWorld)
  for _ = 1, 3 do
    local w = (bot and bot.getWorld and bot:getWorld() and bot:getWorld().name) or ""
    if worldTutor == "" and (w:upper() == "EXIT") then
      bot:sendPacket(3, "action|world_button\nname|_16"); listenEvents(5)
    end
  end
  if worldTutor == "" then printCrit("Doesn't Have Tutorial/Home World!"); callNotif("Doesn't Have Tutorial/Home World!", true); noHomeWorld = true end
  sleep(100); removeEvent(Event.variantlist)
end

print(checkTutor())
