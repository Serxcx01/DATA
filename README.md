---- SC LOGIN JOEY STORE

local accounts = [[
martinmoralese9357@gmail.com|CF:81:85:72:9C:A7:65A42D5E550E8A058B2AD7D45D707557:485CC73247CB6CB532C33201327933A8:Bl4vc4mzkOVMSKLfUvfgWfBcZryQ/kHc+dclvfc/2ppyY2xX8iUh6GOr/k4nzPxFKI/NCQ7iw/hxNKuyDOWAmNyuJRPZOa56jCxR+GsDWLlp4bELOXouOVY9uMKNSGCzP+X5KZqlVG8Y4pjhotd4wMhFC088iBUriNElETVlkAbeh8DoyvosYhQ/a2HbI9FtfC6kWIuy/tmtnl786Hwpm95Hq4LUQRmQcV4yO5OJHZcUVhqJG91Fpo/r/z1bqlpS73jSy+cDPIaVML2kzi1+A44KdtM1B4sdBNelHLMRgURGM2PdA3/drEnvJTpfsRONLmvFkvIFlFHyKl/KolcuE4/l/egK9bjxLnmq6Qpgpqv5fIeCUQxkCIR2ne2FkEZxH3L93Iv+QdUS11rXrlqkKkZ/PCvpLEndWsV0a2Tou8SCzlGTX8dl8KLGM8wzsrp3bk2BwBbGZnvUUP6z9utZUw==
ivetteian86@gmail.com|34:2B:17:25:D8:93:BFAE957509444EA9307988C56F632567:8A34B09A0C2A2380DFDF20ECF0565DB3:ir4VxN6lCX6IUaOnW1Sbf7J2sgorOQhTm7cDOW+h94Xgi40hlvwIr8oG84pUIgvO8wAypP/hDZx711ydl3gWlyVQxMjdq9EzRCAXBaLGcR3ot52C2hYPqh1U4zw80WQclpMlnBPhWDc8uZftAGlul2GVdtMJx/C93mFP2+aX+3syS2kHdMB+IqgZ2rCu9+y0UilQ9c/HbqtmXrMtfO2goG28Hzd4uBdGnrObQWWfrFaPXBenI7UqsfjYc456ck1oIaliEixLy9EqJuE4ICzplYlm5SVaL0XI1/6/UqJP3Z5h4LBoqilONCN7RrUU1YR/IQ1XPJv6u7DY3UfUEvkNABUIHP0h5+AjSUP0ofGuO+rRf3C+A5aFcW9aMCB2ev4/2JCa/qs1ZyPib/URBr2oB5vW8UNMIU83ZTvqliwpzKkFQSR/Zp0qy+ltiTIjR+jSlu5RxLkU/4C19TLcoR1BhQ==
leandronikole7@gmail.com|00:59:72:8D:2B:1E:6259ADCDEA8E370C1A0E6E9AAF2620BE:3183C7F9DC17F067D7B9875F345B4EB6:IlX5kmpN/OYxt7ZyecFo6lXP7us54Jhfq8ZgU6OsxIIvILHY3sb8Kh5jmkhvNms1Lu9VdDmLH8k7m7Lwu3xeAei/0QwhT8E7BSTPZ9esnJ/DoYf/PGT9w9i+1xs8+4Dlq7e2tjL6JHJA2nvZgqyJaaP3zxWogXusjFBMyCWOdoF6m7S8egsXWvTiVfqScznRaCBJLwZlfcZJdnXz2Eyc+53ZMduZjifa9IhyaV4caaXMU+h7NeNXNGjelV+D1MiKCB5hxQ2MZ8K9s/sBf2SGSgt2QCeJTs3EMgI3zMBgp+yLJGQz0qme4+k3EaXgun18H0Vx6B3WlLL3d2NduK4xJrp5+91T7IdS8r5ZAEfWT5H6f3jm8AEmCyHE32zRpnchO38XDOfzoedUy5+WSw12GDjLWQkxAgAwbb/3fOY01uSGJF/uWofUlLbnsUBjxxG2DTyzwPvB6N0iGY1Lc4NGKA==
tinasarlashkar455@gmail.com|D5:7C:A7:D2:8F:50:8CC0625FF6E30BF374E4651EB289BE58:3815B241B58735C13210A7A58F583D57:vzV+dN98LdUXpwo1vqZX/iZhYw53lHDhb7BDVnMRCR25yzR+1h/ZgEFafqB/tFZDsWkUDgzBCTTdOnYLXGwuwVFckTo06fwJb5a3ieOwVkki+s9QVBSV9/fzZuSu1dvAzugfllz7hh7jWoUjXxV6Vr9/MP9Nr277hIGMqktkXU8bZr/GGN5al5jc/ywLCa+AQ8o/QHIdIy/OiHBBvozSvNp0BH3ENnC/MoaQpoMxRTsxJc7lyx2yOwiWaqgx7j8e/N7d2NBWBeWvmeaTqyDFqNr9t4p3ysYAtUzzYbIwl6qmCCcrixMKPTA/mYKr553bHPPlevZ/RQmYHZXz7mztTuyYWX9EsTXvRoYQZP2eBnB/4p1Qad54Vg0Mjd0/BwkzTBFmRvAVwXYEUezTwIgv1MIe/dC58NoogRDp0QK9wOlcZA1di2zPQBUnlv0fyZeQbEzxfQ0Kje3Gp8KDVdDOgw==
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
