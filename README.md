-- SC WIR WINDOWS
--- SC WIR

local input_text = [[
wir_tn4urq0jyycgq228@gmail.com|8hS/97tatupWgxesdnM6VictdXuBsPmrJhoNu4wQ4NAwOXIB3ixgqHuDWKIwuAzdaGdX18EkwY8ctQtZEwQFprOrINwtAB2BA5SUYQmLI25F8yRYQlYdBFZcw/QiubBRrRn51cTInPn3X435b9gPulMbDFsHdQRTPEJEMEZNEUlDAd4JKcZNweEO0bDpvtJWSv2rV/0kNAu9TftKqrjnGL00mKKL3k/bjiSZZmF+nrbXJ8NOltHpeiSrRbArUIMx5CwCijew22UTIMHalqeMzdxKRzQfuqJk0mLhADURab2tjb/bG3ks57tWUGG5e7y5WtmnhYRW7B7lKJOsG5BpK2fEB9s7dsmlRx4lHEBYMku/vK9AdD1Anq1wpuE0GidxNULDZFiVIKrbtcokPocwtfHaz2jO5qonosP4AiqIJbXnB4doKvwBuh6/KzQVOLLesXCLcI0s9c5X6H5OPD2X7tchh6E5qypKQCi7qvY8+CoftW0pCrEHxG9nz8h/6Ee0|XA7UAT852OTZPAY91JNFHY0CKJNGFG0C
wir_shkbpbylwjfkzl0g@gmail.com|8hS/97tatupWgxesdnM6VkVnzg1KgDj19O2VZxoTZXlRoJ/M7KiE4OdbG55BsjFvN5XQ1P1xCbt2z9QNK82iAN/Gadqeu2yfoQkHXFF1AhW1nuafnWXN5AadhvHDWaumyTcFCXg3wT0wXLt2iTA5gqOuWo1IvxzZis3G6f1J1iUjMysHGKn8umEiUopHN5W6Su4zr2OlL6Z0069gWafRrNOyB1e2mwKTAxGTIrS5W8P/wjOvyA5Stxzt95E8HDmnJSUekJn+1LrMMNa5minvFmNiDqZ7eaFBO+7tpxmUFwLU70MHLiQn7w1triUHT010xBbz3PWoGOe+37f6GSV2U53eHB6EaALoTe1fsd5LHAXuLtNGvwOdpB6L4PwJ/6PzQplOyieczGoYht2X7xdscodr3JfcKU+ChBa3koJx/W9Rtp0r71dHoXucFpGV1kgnfG4A8CzzGycb1mm6K0lFipCGrzXD8bzhudtSuHNEF1oWnbgRIzp/nT0HK1sSV60l|N7XUJS1679I26HKV3EKPW81T1G7MAPU5
wir_x2s8qjkj5nq1s3pt@gmail.com|8hS/97tatupWgxesdnM6Vnn7Kqd6tcg/6h+fnUg1cXWyI/yZ5DinLUslr/Vn6CKM5x9qVye6e4oIdaZW8Bj2aS19p9aE1JbjiPDhtjLTGtV5N7S9qriO3hsImQTwGJvkIUDMuY7FRQ1wSGD3qQkRxjKomTS+yK3I4I75xW0Y2vo+SIw0WazSyDVBaXOtSamuUwG/BLHKEDtstE59bMpVl34S6I7svkx/1+Ycc3SMhYwm4pvDtAmpZShrsMBIiySAFRTmCsjoXmk5gy5pFPYOvgrNTH7bzab99+Odcg5vqn52g+ekeUP7NWhYcPohoHifZxyZZLISvfP3TFSLag7h8OmUhQtQWDij+4e+te9tk5OYXRewWg6t0bUoD3oS3aveE6TrptQAmkY9bsorO7UVrK3Auo6L+ESVtRrsj4CyJTjA4CFEKv4YQ/jJG/2UBV1p1zTobtQvgWYUwTNaUKcppTFbfOLwD3d3xA+Va99crDgDnEkCOFWna+axn1Xbck/c|9SSICDXLL35VRF8L5UAN14ZNFZZQ88QV
wir_rec68uehruag1hoi@gmail.com|8hS/97tatupWgxesdnM6VmejY6gVHu8Y6r8OhvdM/nddlSQkYZqO/BtUMiJHxVaxnMNeRGmWuFoo8doVaZG3fZjirY39/y3YQ3j6CSZ8gNm6/1suw+7b7qhq81x1Iz90Y7CxPfYfnTlOPrsob9Y2pCR2Fd/Ic0NJvoqi6PcmmnP8Dg330w16Pvi4fyoho19XpK9/T7Y4qUO6eoADJDN1R2ZJiw6flZWroswGbhVaVvyGUJXlyjG9ywm8n4YeWCBvXzk+RfCNhhC9w0n9tbKuah8v09rJVpvWepSNLfmLGSt5MSqZK7OiU/NkrTT+NYXvgH88XkP6Z1/adAnk83wXdlCqc7edRkir9Pg5vDnPr5sfirXq3Agsi/hlRmG7WcepT9UowKpywhp8TkSp2J1qdFRdl8Fvxqzc3c7e7KV3dCDLGv2SX0X6OqZWtPrLK8bTspWFY+QwUZlU9mP8YXdUlgkKYpQaC2PvdO6pKD9QkWsy6enAhXfwYeuJVvzKnCs0|6Z9G7UUHQYFPB8X95HPF90U20DO5ZIJC

]]



for line in string.gmatch(input_text, "([^\r\n]+)") do
    local email, token, rid = line:match("([^|]+)|([^|]+)|([^|]+)")
    local information = {
        ["display"] = email,
        ["secret"] = email,
        ["name"] = token,
        ["rid"] = rid,
        ["mac"] = "02:00:00:00:00:00",
        ["wk"] = "NONE0",
        ["platform"] = 1,
    }

    local bot = addBot(information)
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


-- for line in string.gmatch(input_text, "([^\r\n]+)") do
--     local email, token, rid = line:match("([^|]+)|([^|]+)|([^|]+)")
--     local information = {
--         ["display"] = email,
--         ["secret"] = email,
--         ["name"] = token,
--         ["rid"] = rid,
--         ["mac"] = "02:00:00:00:00:00",
--         ["wk"] = "NONE0",
--         ["platform"] = 1,
--     }

--     local bot = addBot(information)
--     local tutorial = bot.auto_tutorial
--     bot:getConsole().enabled = true
--     if bot_bypass then
--         bot.bypass_logon = true
--     end
--     tutorial.enabled = true
--     tutorial.auto_quest = true
--     tutorial.set_as_home = true
--     tutorial.set_high_level = true
--     tutorial.set_random_skin = false
--     tutorial.set_random_profile = true
--     bot.dynamic_delay = true
-- end

