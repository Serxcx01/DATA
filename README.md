---- SC LOGIN JOEY STORE

local accounts = [[
qn3971006@gmail.com|db:5d:26:1b:6b:e4:c18c2819473cd1b56cf86a2e8f7874bc:66B3FB8A5C18DFD61B9AE052F90A34D1:kJcx2nNfhE+JJXx9wVhC9jufZ6/sVspOPe5stAZdkP7SQmtSByMahsQk0L0NLPcZxUiWmfd4IuGGbjQ5UJGuTQ+ZIrMb2rEsTNTgGPzwOFFE0jH8C/c7BArdlx9yoXIPakXK+XiZXCO7ExIhruGHfHaamqX6zwJcdoE1fF7iQSE2Heyl+AXEmLmSQuUeG6bzdhc2RGOybwDpLlZW6ITcHZM1bKx/Jj0oJG+ctenHKlppnX8HxYj142XElzNhTKT1/DqX42GkIDsfdMpAatVsaYl7M3ibTzYKk1DInDEpjjSkc8arS0/P08i1y6Yp9sjJ9zlDHTpdOKehw27bmZeTVE1YFKmfW7QePUt6Xj7xdiaVADRRhMiIhEQW0JKHbCw1yatVyRH3Pzb9+okD92s/kP5qSYmBAcDQKDRc/5qTgW8b5uLz+fAmbJMEY4KRS5ibM5xiOUozWXOj4FDN/hRSSg==
quanghuukiet7139@gmail.com|a6:a9:68:89:c3:f5:dd7f3a0c0a8ac26498b63fb35a7d1491:9A4FDA55CDFDA2AD8CF7F2FFCB9B300B:kJcx2nNfhE+JJXx9wVhC9kCI4UfYpUtgLP17hKtoWPXgwaP4UNc1gfZwoac6lDhZGXaUPN9O8SOJWOmmkHEodaI7nwK+YNWdCdC8MJgulYakfINQMbDJrU+4l2iYhrMlA1naeQGi+7EkN0arD5W3+q8uEC86vKgUURV1w+jemXmnThPYwbdhVBrPfRLU4B+9aIyoPG8leCq99LkatvPiYw0Ix+lliCU5ATM1W74WnZWZi7SbmHzzBrtxZp39fQqQbmNVr5ZB/znkrvQgXrUDQHvOBC5QWC5ElniaAXqJ+WQcaYwChuC4XWHhQgWg2P/REPZzgSQUtuvmikTQNsjr7K+aZAuSyJRrHvFwp9tEHg/PCl4ylXDNDSOrxhyE5OTEmFAmApm5iaKCtxhO0UkzmAn28bG0vkHsEB0ERj/cQx8QmEL+s2MgnzLuH1X4PV+SkUzY8Y+u74KckbSJCiV6jA==
phucduct739@gmail.com|86:f7:05:3a:6b:e7:2306356aa033ed54e8f896369980fd5b:09AE8FF8D5210BEA804FA8D173E4B291:kJcx2nNfhE+JJXx9wVhC9jBQgDYSzRK/xFRkPLlWmWfwN6NroJ/zILI3ZWRd+B4MVSiHhY/gMtVUOQVm2/dVdFjkRJ/ne6PmSbViTJX182IkCrWKM+cg6+qG6tia45sf1//b8JkP+1GD/hnGFuNJDxJR9MSdwzvcDokD/o9kfv+xZmclNvlqh/7e+NVztMqxHdMpGkk9Qum4FmS5HQVy/2t9nbAVWQQ9etCMCxnO/v031+erR+IS6RbR+ZKRuMDSyDLDQ/gG2Byr3qTi9FjYT3qOGdXwa6H4/LVwxDW2FJapTtlEwLxsi0nRfjrFMektXOjUHpiRaY8nwGg4nsx42gbQmsMWLQoRSMtJ4zHkOjs/71T7rF8G3uteb4s60b9ScGNTpdWoUphpUu8EjnUccAioHMEQjSra2aDptZrsu6cHX22e27/21k9dPZrn95QDy3mUlddPdnYIL1OtccBZ2A==

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
