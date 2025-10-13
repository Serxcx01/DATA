function findStatus()
    local bot = (getBot and getBot()) or nil
    if not bot or not bot.getConsole then return false end
    local console = bot:getConsole()
    if not console or not console.contents then return false end
    for _, con in pairs(console.contents) do
        if type(con) == "string" and con:find("Status:") and (bot.status == BotStatus.online or bot.status == 1) then
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
                        -- Ambil nama malady
                        local name = con:match("[Mm]alady:%s*([^!%(\n\r]+)")
                        if not name then
                            name = con:match("[Mm]alady:%s*(.-)%.") -- fallback kalau formatnya pakai titik
                        end
                        if name then name = name:gsub("%s+$", "") end

                        -- Ambil bagian waktu di dalam tanda kurung (lebih akurat)
                        local time_part = con:match("%(([^%)]+)%)") or ""

                        -- Tangkap jam, menit, detik (support hour/hours/hr/min/mins/sec/secs)
                        local h = tonumber(time_part:match("(%d+)%s*hour[s]?")) or
                                  tonumber(time_part:match("(%d+)%s*hr[s]?")) or 0
                        local m = tonumber(time_part:match("(%d+)%s*min[s]?")) or
                                  tonumber(time_part:match("(%d+)%s*minute[s]?")) or 0
                        local s = tonumber(time_part:match("(%d+)%s*sec[s]?")) or
                                  tonumber(time_part:match("(%d+)%s*second[s]?")) or 0

                        local total = h * 3600 + m * 60 + s

                        maladyName, maladyHours, maladyMins, maladySecs, totalSeconds =
                            name, h, m, s, total

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
