-- TIME_MALADY dihitung seperti "tick counter"
function clearConsole()
    local b = (getBot and getBot()) or nil
    if not b then
      return false, "no_bot"
    end
    for i = 1, 50 do
        b:getConsole():append("")
    end
end

function findStatus()
    local b = (getBot and getBot()) or nil
    if not b then
      return false, "no_bot"
    end
    for _, con in pairs(b:getConsole().contents) do
        if con:find("Status:") and b.status == BotStatus.online then
            return true
        end
    end
    return false
end

function checkMalady()
    local b = (getBot and getBot()) or nil
    if not b then
      return false, "no_bot"
    end
    if b:isInWorld() and b.status == BotStatus.online then
        clearConsole()
        b:say("/status")
        sleep(700)
        if findStatus() then
            for _, con in pairs(b:getConsole().contents) do
                if con:lower():find("malady:") then
                    maladyName = con:match("Malady:%s*([%S%s]+)%s*!")

                    local hoursMatch = con:match("(%d+) hours?")
                    local minsMatch = con:match("(%d+) mins?")
                    local secsMatch = con:match("(%d+) secs?")

                    maladyHours = tonumber(hoursMatch) or 0
                    maladyMins = tonumber(minsMatch) or 0
                    maladySecs = tonumber(secsMatch) or 0

                    totalSeconds = (maladyHours * 3600) + (maladyMins * 60) + maladySecs

                    print("Malady: " .. (maladyName or "None") .. ". Time Left: " .. maladyHours .. " hours, " .. maladyMins .. " mins, " .. maladySecs .. " secs")
                    return true
                end
            end
        end 
    end
    return false
end

print(checkMalady())
-- print(totalSeconds
