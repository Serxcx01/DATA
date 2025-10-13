function findStatus()
    local bot = (getBot and getBot()) or nil
    for _, con in pairs(bot:getConsole().contents) do
        if con:find("Status:") and bot.status == BotStatus.online then
            return true
        end
    end
    return false
end


function checkMalady()
    local b = (getBot and getBot()) or nil
    if b and b.isInWorld and b:isInWorld() and (b.status == BotStatus.online or b.status == 1) then
        if b.say then b:say("/status") end
        sleep(700)

        if type(findStatus)=="function" and findStatus() and b.getConsole then
            local conso = b:getConsole()
            if conso and conso.contents then
                for _, con in pairs(conso.contents) do
                    if type(con)=="string" and con:lower():find("malady:") then
                        local name = con:match("[Mm]alady:%s*([^!]+)")
                        if name then name = name:gsub("%s+$","") end

                        -- cari hanya di bagian dalam tanda kurung
                        local time_part = con:match("%(([%d%sa-zA-Z,]+)%)") or ""
                        local h = tonumber(time_part:match("(%d+)%s*hour")) or 0
                        local m = tonumber(time_part:match("(%d+)%s*min")) or 0
                        local s = tonumber(time_part:match("(%d+)%s*sec")) or 0

                        local total = h * 3600 + m * 60 + s
                        print(("Malady: %s. Time Left: %d hours, %d mins, %d secs")
                            :format(name or "None", h, m, s))
                        return true, total, name
                    end
                end
            end
        end
    end
    return false, nil, nil
end

print(checkMalady())
