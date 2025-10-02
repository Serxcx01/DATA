bot = getBot()

function checkMalady()
    if bot:isInWorld() and bot.status == BotStatus.online then
        clearConsole()
        sleep(100)
        bot:say("/status")
        sleep(700)

        if findStatus() then
            for _, con in pairs(bot:getConsole().contents) do
                if con:lower():find("malady:") then
                    maladyName = con:match("Malady:%s*([%S%s]+)%s*!")

                    local hoursMatch = con:match("(%d+) hours?")
                    local minsMatch = con:match("(%d+) mins?")
                    local secsMatch = con:match("(%d+) secs?")

                    maladyHours = tonumber(hoursMatch) or 0
                    maladyMins = tonumber(minsMatch) or 0
                    maladySecs = tonumber(secsMatch) or 0

                    totalSeconds = (maladyHours * 3600) + (maladyMins * 60) + maladySecs

                    printLog("Malady: " .. (maladyName or "None") .. ". Time Left: " .. maladyHours .. " hours, " .. maladyMins .. " mins, " .. maladySecs .. " secs")
                    return true
                end
            end
        end 
    end
    return false
end
print("############")
print(checkMalady())
