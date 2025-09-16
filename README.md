---- SC AP
local bots = [[
A96631B65D717F5C9F6FFD6275C354AC|ubPRTmo9iocimveNAGOQ4E2g6iOSwdjLkDAN1UPaJ7wa5AmF6YdlfVs4VHcUWaXKTWNoXk0U6ODCXENBFD+YT8s3hNj0NQTZwjlBLwZ5jvs+LnVDByEM1EnAn3R+aaz/52vzGbSytg6JL+Iyo4HL4PjI8QtIbRWRAlm3v66e/tAQcQTjuYAAN/NuxONY2uZjXYlApkUo6A0VzCpstRvPA8RNm73TbQRo29/gEkkmz7W6YW41Yvlb/EG0x5ifxiYut/yvpeOKcqM6HZB5k5WkQ6Slcu0gHiT9Soj0WVSlQouDHuDF66GH228+Ot1LRXkXmDIo1mWubLzHc9AKPAuvMFyTXvqKRvonEVeJss1YRyqVRNArQ6jCAn0c5m8oakbhgwTjJ6at+CQ9nvarm3t25Psv9wR+KJCg2sp/2WEKnS9nlLk3QllUqw8oe+BgcxwOyfe5fiX+Q5pY7JUybFosmijlI/FzWmr7iAFRyVZpzkaRMPj8O/0HKvoOpIzV8gL3
1939F93F6C800678576DB787F8F74FA2|ubPRTmo9iocimveNAGOQ4DAM0eQAh2eRvjvY5O4RfEy0zVRpOhdutdhEiqUrJSq4BWfptp0XIBXXMaHoMX1seTyGoyfWrqtU+g6UdqsxjAf13v3HQb4pbVSAKm6HqXJIJWxv/0UcLEJ7ZumRUPLF0i7VSdra3en1HFdE97VxHpjLK9QJtgGO/MZn/uMbh2BMTJZqETXUl49zPoty5RusHL4eQZFt7CeZmu1yRsXE77acuLsMtn39OIL6Y9tDyojjE3GIk8eqpA3rfeRNg7PQb5dwrG3iWSAMhlEzKwpv54RAkfYJC4/MIqQ4SaqfoqPu8g/BbW/CVe89+L41e8g4ZkmKio5dz0zn2YYW+StXmIGMaZNquz2zjzrGIX8mLEEiiOcTF1o0/X+gBVNem4LwjfUD3rZH+336kgBMK/+8L5rFMM53fn8YZoRSOjoHGqzDyX8oFBXV4JfrXYtScUJYJakpUCYEe/g9ZL/Uk1HAjIXFU535lt8A07JwfDkMcGzf
3B886FDFA2902D1F8128001ADE8FE64E|ubPRTmo9iocimveNAGOQ4JMJoOq9eKWNhY8GRB/2igLdVD0wthJXweNZ/+UIuAyfMJhr+rnd3Bp/TB6f5cvwTxqog2U4GuPzfl/pUq+kC2zZNdnTPyyCTehgutkHYWxbakMBEDBGNJD+Z+DYqc2pi9XZe0I/hdnqYH5rBDT17Jus1/Vti1Dan8kHIwB9jy4VXocqaOZKRCBsXT83aUXyGVE6PwroIiibQIzHajkIEgwU3YOduG8lZV7ivlY2MYb3Csniaj+boi2GrC3rOaVc8Wc0GaMv4UcmG9zXvwDFqAhYUEExoNR/VvsO6sIFihq919uuJoTt9mFDqT+kBAAVnjYaypIkw0C6gFP0E3XqHYjZZA7o5qO05PK5OvsgV0SReD3O54DJakJNVwJmwM0McqpDmMi+TwR8hPsa/wvxotuFnXoYb67x3VCB9vOobBeGoIR9Q2h0UVkGiYcEMmxbGGOVUGZzBgstch+x5eCwzFC8oZ/LPNO+PX03RKHZRsiZ
D7B6AA8BEA76289222A355F513ABAC42|ubPRTmo9iocimveNAGOQ4Gm2ZiLUd4KY6vIMlFqmNcAJC8U38XIHve/z7/Bq9nNRrOTwpIfafDo+TVqsRpMgAFsMc0c72NwOm2zJAP59V/A4XIg94LrBzq1hcGHizALeZ+sCzg8cQuaaPDw5VfZ1G9NEpaZ3exOWNYjY9N4ZNajYR1nSjik+NVcsM8ABrn5IAV9IpkNFszPCCBE++cWwhIsJlAI6wKNwE6z8GaYDBY0NAjPyj/yMzsX1ztJG9aWuXDJ3b7VmOb8wd/fSF56vYbaDgBj4IGrPSDJIw8MvzD2inIRMQHDon4fmw5fpXQiChyl6iZuEG/PIFYyAgZAULukL05QK+EIYuV7HAgO3Djgz0kZllL9PoBnWNJJ2snrnwUoxmOSWaK4lBVhKtJwawFMu0uQFUtYp5iZp1J3XQRVKyF4X6JmLD8B+D4ZNLZ2Sl2/Cx03GKJ9PfvnOBfl+gVhfIK4TPBmMPvrFHy7Fd2Zuh/Xkob3FGeTaYkeZ94V6

]]



for line in bots:gmatch("[^\n]+") do
    local rid, ltoken = line:gmatch("([^|]+)|([^|]+)")()
    local dataBot = {
        ["rid"] = rid,
        ["name"] = ltoken,
        ["platform"] = 1,
        ["mac"] = "02:00:00:00:00:00",
        ["wk"] = "NONE0"
    }
    local bot = addBot(dataBot)
    local tutorial = bot.auto_tutorial
    bot:getConsole().enabled = true
    if bot_bypass then
        bot.bypass_logon = true
    end
    tutorial.enabled = true
    tutorial.auto_quest = true
    tutorial.set_as_home = true
    tutorial.set_high_level = true
    tutorial.set_random_skin = false
    tutorial.set_random_profile = true
    bot.dynamic_delay = true

end
