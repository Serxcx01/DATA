---- SC LOGIN JOEY STORE

local accounts = [[
norikoandrew914@gmail.com|87:a3:3b:5e:be:47:bb959e0f2abf937ced3c1747f7e1b9e0:D0EF6B5E32B9ED6FD9FBA948FE6A2BF4:80UptFvonl9/irzirSAn4hNCfIGbVyCVu4o9uC8+VWPK6DFAI5WaEl9fvVIyEsSGSHBV5jiTFh0ERPOiFdB5OcDlxfPdsMlHZaeD1udUBHRvEsbj2osnjYL4nCHAzZvQJbPr1j8owCiD+ZYzHtCrWxH+0wtR2TW0r2qClCh+9P5gAEmvBDstv2AISreKXs7lMjTL75MeC+nQ6poo456ydfkzT5449sRITmSOvGDROr9Qj8/e4SCJsVKNDELU5Td+4SVEjL9a6DIMKcwkuNziEWtyIV6bKFMf6NTZLeDq08P5/aVhDyg+fVscyqPiRKpzjl8y0aFUQbOM/mq9C/pKaPbkQuRyR0zYScyqJyD6AIWfAXfZlEYGt8FG8Xxu4tabOldStyBc/nGa/GfwzIiZDDvqzU7/FIqIoHbyTIf4YpKy9LTUGTEdO65AVQjqmKLm5bn2leex86idN1TJE11RsA==
thaoducbui938068@gmail.com|04:2b:b2:93:2e:07:7d997133932808bfe8221d786a581cc1:EF3AB7D74ACEEB1C5ADF8B42875CE362:80UptFvonl9/irzirSAn4jh8LNv9TOKe/DqG2qoa9GUmA+zJq8bn1BRq4l8gcqpdqz621ZO6CvcUJg3UpOqh0s4dRpIP6zmrhqhfh/2rbB099fREp2SQYsePekbMK10rM/mlIQ1VwLYJEJ62fwXhALKjp/uaUg+anEpxQzywp1zFwDbrkKSWkCPKUgY1MYeq0GvetX07E9SrStcEPhbOrqovdaJuxp1JiGq1VJuUwZy6nx8HwfSE2k0cNYlWgp0PRoPKkZgeRkBiIWoCaWmznEKCdsdIr2o+Bq00XqR+H2jNheegXXoGPC2d4294unoPBFy8XOgV1PevxCaMRmLxQWuKcU84B1Gxp6zysH8LPZ7tQX8PQt3ywnOPVObf16OawhAZ4Z1PUq9oOatLDG8/A6kilvoR7x1J8OpufCzOQ3RrbeCZuRxk/oTAUHiiCIzTpIBj5g9aikRnOOLOf2jKgg==
tamthidoknw@gmail.com|e3:93:0f:19:57:8d:d3ea180d73a61e7dbb1016f49d836a72:79704B71ADCAF4A968707AC7AD271CCE:80UptFvonl9/irzirSAn4n2jSyz7aQfA5oyEE0ZgyAmHkyQ4UTZjFPiAkUp8qdLbcFFcwo6M26edtJZBHrRB8HnFUkGIalQX6hbU70q+15IZKcTcZkP1GPbD5CUrCvCqqLoAA3N9W1QiRdakS9Qokb3l1j76z+Mbp5jwt5KTaMcz+y1dGU5mY16WqaMKPi5sTcKm5QXCe1jT5/fbRunl88dYQIg8QABYrYqFyQ+oJ1+0kRyB+OP0Evo0XUHS1b3ZxBbBcQK/foA14qhQ8gRwbUm+9X1xVDiNXeuQErqWImmHrkKfISd+lLzoSF3upqfqnSnxHIqB20aGXTsiKqluiQqG27Ac2ml2igRQIfDFYDmZu8u6SKvGRmDTwpFRl+7eb6zYYzs0Iz8Id3z60Vj7dUdFhj1ZMYDQZEyG70rASNfY4ik0c+dfMKTuoaxI7AeQJMWmRdrHJLNoVewCemPPYA==
truongtuanngouqg@gmail.com|54:02:03:f7:67:34:0ef1b22b092df14362c2b47006d79d72:ACBDAE8BCCCAEAACB2F7858E1CC3F8CC:k+Phd3JdhNRCfzOUYs4NjTyKJ7QjjqxZFFGPYiCLVKgqzmTdurmqCaqDfjYo6hLA9cil/fwjIzH8n5MByDnX5K3dkA8BRfzF7Y/kFmUor8oe7yKrSOB4jnlGz30KyVJlQcp7Wmlg40D4YfsJ4U7FfIAJ6BRKP1aJSIWncKGyVif8KaZFsrrB3ue5sE+he0PxF96nvtkb3cR0AWfymLC3z0Df5YNLoJgavPvk8/VV/q07An6dCPqWNLtnzMerIXZOkDvrUmqnhiTGY9kn2WwEsbpXPiHuybU2zxC3f/i6C3NNP0p2AjNzvEWJNuDB8Y3JySbWgscuzH2eHFhvc6rM/JLGC2HlcWy0fsDTWlPRpeIvYfKA4+zwps/bBU/v5NyskiBYdhw8acDC/RgC2/h6R0VqHv+UEQJ/prSMXV+SVTk9ZlSySDR1g1nZ3lUJAYuV7HJ4qdShzIye0LMbYkQK3Q==

]]

use_bypass =  false
for account in accounts:gmatch("[^\n]+") do
    local email, sisa = account:match("([^|]+)|(.+)")

    if email and sisa then
        local mac, rid, wk, ltoken = sisa:match("([^|]+):([^|]+):([^|]+):(.+)")
        if mac and rid and wk and ltoken then
            print(mac,rid,wk,ltoken)
            local details = {
                ["name"] = ltoken,
                ["rid"] = rid,
                ["mac"] = mac,
                ["wk"] = wk,
                ["platform"] = 0,
            }
            local bot = addBot(details)
            bot:getConsole().enabled = true
            bot.bypass_logon = use_bypass
            bot.auto_ban = true
        
            local tutorial = bot.auto_tutorial
            tutorial.enabled = true
            tutorial.auto_quest = true
            tutorial.set_as_home = true
            tutorial.set_high_level = true
            tutorial.set_random_skin = false
            tutorial.set_random_profile = false
        
            sleep(3)
        end
    else
        local mac, rid, wk, ltoken = sisa:match("([^|]+):([^|]+):([^|]+):(.+)")
        if mac and rid and wk and ltoken then
            local details = {
                ["name"] = ltoken,
                ["rid"] = rid,
                ["mac"] = mac,
                ["wk"] = wk,
                ["platform"] = 0,
            }
            local bot = addBot(details)
            bot:getConsole().enabled = true
            bot.bypass_logon = use_bypass
            bot.auto_ban = true
        
            local tutorial = bot.auto_tutorial
            tutorial.enabled = true
            tutorial.auto_quest = true
            tutorial.set_as_home = true
            tutorial.set_high_level = true
            tutorial.set_random_skin = false
            tutorial.set_random_profile = false
        
            sleep(3)
        end
    end
end
