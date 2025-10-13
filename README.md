function clearConsole()
    local b = (getBot and getBot()) or nil
    if not b then
      return false, "no_bot"
    end
    for i = 1, 50 do
        b:getConsole():append("")
    end
end


clearConsole()
