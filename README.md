---- SC AP
local bots = [[
EE74B60700D0BECFE08941C7E57CAD36|5piYbFYxmieb8d+DUjUVDOO16vPQEL9z8/y6W05OzUc+fS8Kj5vXxV+zLQZ5YL4db7NR08XM4oXo9V7OHfEDC2yElwcZAwXfVdWrsjbU/Y99zK1FNEQfxLKcJNI/A7M7VOMap/OH7NeywHtseuUbVMj8MpEu7vTNaiwPLeWFNmvllGDDS8o5NANpSeIVZ+05C8I6S2Cfta9yMfA8u/J0EAdYwNeoFQENSAgmA7aMUZ8bfbRLS13ayIGhtLAPX7WkNVlUZ249yJMD5RRz1xD/D0oeuq4TBDBSJ+RTG+QghbTrm+ZrlANuwKV9AkrI/GCeo11wpgyF7taouvzq1ibL+EslV2pqVlF7UKaz2Ic50OfGSoQLRw9sArNfWH1JFX7T7mNxWZqEEndZHtwAlCW/Fso+7XdNEps6U9XN6E1VXhHplriZmNZMcOf/HgJcaeMueA9KmbgDw2X4e/6Sw/IR2mzz62Ep0XOziDa5MDVFW6/6j8S+AqBeetP+MuDjwR54
C522472017E40DB6F96557374398757C|5piYbFYxmieb8d+DUjUVDHqK3IttJtfjCMJo2K4ZQgDijaMzA5JEXTraZxYEqRNY52L35tUt8YTMPo7I479bbqQaQrnE9hwXTB/DP+3gEBTHYfZRJViO0VjHnVAXpevbjS5Z5wQhX4mJ1KKt6fOnWEyjalzDRqcVnJ40seh+WOZ6IndFWBLtCYJgpWKLV37s80CWKbziPKnytq5Iyf4di3SvBWE80LjP4Fhyf0eC0KI7qmqBBTCeY8mzfxMlXD/8Qf3lc+Of6jiXSVq5KLXWi534Hx5EfYrV/Ohpz6O3wqNj27En2ZrplWaCHa9FQGyHqBLZT9P53s9w/Pn450GPvYacZ5NA9MYeRAs+CozZnrRcc0txCvqHsD4UqN8nrWgcupfAje9FjiKAxoToUh79oVk7en36YImIDKVqm3X/ry+s2PBGT+OmofCm2M6x07vznrBbuwn+H2DIH+9zroQHvQMS4Bp9OsC3QTdiRC1L2PVcQ4e3xqxUi430v1cCwxla
E2C71E4A33F5E7BD7092BD7A162A13C3|5piYbFYxmieb8d+DUjUVDMkebdaGhntt5NLtp9wUwPS1X62MlHqr/fhT47+9eiuUg7ztCD+UeSRskE1pJ7h4vExP9hRnmZMWyBvBGtzHY1yA6yVHQQ6F9QUKttzji0ioXTqiQOOW/Almx+wjof2byAeIrPl056Z4AsJXnqgVIet1tEbxWeJX95LmC6SjowiHDxHbY2vFf5s2Rn+nDWKvtAvPeI0NezM9pKjfm5Nu7pqYbvspg7t0JXiJTU4fadi58PnDTt7hdAMTqwUdnlyKV4DK8F6gAWH+2wleD6OqN8ZRn7tUHHTFJShWTJ4Ji6KwUuUIJdCBe6vGSqZJecV56uPZ3P5J9XGocQiUWhGHkyDlj/22Pee7Ss+YyJKsfEuPjuild1XnjMFDJy8P8MjxTuFG2+y+QGnaciZltpI5wXTyFI3EfBtHZT/XdeTuMpIkB5TI/0u8sxYuofos8wTkU/Ac340edEWydfMX3i+6BjISIxmHAa/M4RAkkdACiXzI
CD2FD75B25EAD7E2508B48DE0B437463|5piYbFYxmieb8d+DUjUVDMnGa+LLKITlzDU1H7UYzfEgJsj/rEtFdvIZjvKJDuIVNXJxf5SaPxAZ/El1ACd19fp4JcTFYd4vmve6unJ9alHkjj1p/8ZEB7YPW/72Md+W8hJ3AyIlybzau4CWkgN6ZigSmOJ7saWe+Yu+UBLGQd8pcMhTGJMUSodNrwaUHU9+YWU5JVN2qvCwZYp1r/rRoj1h8rqnjlv+GwGTbqAfDBVM4Y6t1bRk3+kYKOmjKBCkNtRHiUAKddTZvi+JLAazNWvx/LIXV53lqeZaL94MPFMvWIQQdvco49dX9cP3FCJpfshYxZHyzoiS7zBsoKvpA7+nYa+N6eHbCDEfHB6EuwgG39+/nsqkS8sJdtTaBm++9Pb2b2SVCRmFKTeznby5v7P+boqZTCyY6eqOI8sRfB0eXGyzgiwrc099lJvC0LapARlbTEotE3rofIxSPbMTqyWOW0mnXRD7z6KTvOL6EPi8/KBibJ4ItrnNV1orLcpu



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
