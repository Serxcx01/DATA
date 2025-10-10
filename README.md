local tokens = [[
mac:02:00:00:00:00:00|wk:NONE0|platform:1|rid:023E95F1C83AA04A01005AE2EF0B375A|name:icydewkabn|cbits:1536|playerAge:25|token:3sIBYx38skHwW52TbCaJ65nkwTjaPqSk0DNgoAND5w7R4VvNvl/IPChVqZFddc1WNdpCTMgvfvrdH01FQcBLCFIk2zwvWCDSol3WSWobA4PKRaoZq9u6ntZVCYdjAXQeMfIEiJnqmcnGVaahfi46p2xy+hybRJBdXnZ0zUa1JtHkUxh9hQpIOfGQpkNHfe53kH7OLOTjpPKhB4VzSJc2k5AN18LpTXOzq/axa2QwwRxcO+7I8LBfdWi6PVVUu2SvE639EBjdyNflgWmaBOTZyHF8JzGJJG2KsSkQ41I9LWzGJUbGXlf5CA57ulyNBgze3QMl8cHC2w8Ag78TiSQcw2O4y9fhifmeQ9N928NygMHzXFtWZ1H/nXbaoR1OKprV4cCE1hyTLSyqIVAYXp3/T/Is9SYce14/wNqvVFegKEDdaXHFda0VM6RXnqglEfXbN1iwRXMkZoynP0B6Uld4UZ/SN9e4WdVWwtJi0UHsWSPmwGgl8xw0gWgp6HilgleD|vid:24C059E7-7CC8-4833-874D-660A4AE312AC

]]

local useProxy = false
local connectBot = true

local function parseTokenLine(line)
    local bot = {}
    
    for key_value in line:gmatch("[^|]+") do
        local key, value = key_value:match("([^:]+):(.+)")
        if key and value then
            bot[key] = value
        end
    end
    
    return bot
end

local function configureAndAddBot(bot)
    if not bot.token then
        return
    end

    bot.connect = connectBot

    if type(calculateBackpackCost) == "function" then
        if useProxy then
            bot.proxy = "auto"
        end
        bot.type = TOKEN
    else
        bot.name = bot.token
        bot.platform = tonumber(bot.platform)
    end

    for key, value in pairs(bot) do
        print(key .. ": " .. tostring(value))
    end

    if addBot(bot) then
        print("Bot has been added: " .. (bot.name or "Unknown"))
    end
end

for line in tokens:gmatch("[^\r\n]+") do
    local bot = parseTokenLine(line)
    configureAndAddBot(bot)
end
