---- SC LOGIN JOEY STORE

local accounts = [[
taduyhung3853@gmail.com|d6:d1:ea:55:2a:4b:600fc000447f1fbf6904a7e86e478afe:F17CCE2D2EB4CBD4E539ACDDDCC63B6A:NKbBpi4L8jrwtAlyyWMST2i+N/F5df3lhYyjeVUFBJVKD8mXYIDcNdjmc3HNMafhf959ak2oB+aMhkqb2ft4qH2elb+I+vkblRjoTW7eQeQfEvfS7G6EL8qPNiS8sD0t1+fSE31z2yX4RSQIFEqe8LG+BLSg2TyqIb2J+f6LuG6ezZMIolor+sgqgp5wemdFNtCrpkJzZ7GM+GIqzM+aBehZ98lNtCEFTHxYsWrMTI4pVwrLwOJwskvTQEwvu3uHbMfBgaiiy9it88ledx5FrFDKcZ1OEjZvvtZRccd+3WSWBF6IZcon2rHcNXgShs3KLdkMwB4ZlFNBgSzlUim4gzL/EtwI3tkCbGJpHm6u6CKw9+WW29y6z7n3UtiLyVbPDkGXRt830YMmOxHUNVZuTiq6Mf3Xn1mu9tnbcGsV6KjXPSn5nC4Wf72NvXa2H6lEWlvPTgBQHwQT5kHVslPZbA==
quynhthuly27@gmail.com|fa:8b:51:e8:29:93:1b2fd171418ac7bb8d11b4765cc4f0cf:BFBFC0BBD24ED0A0DEDA3DAB7BA1BF52:jabAM2pUZjv/irD6ljCbGrYmVOTm3eUqlGSF0nXNQusq+J/Ya3lBboKTiQCL7izwO5AAq4hxFH+27nibuA1uupE9IdgjI14cM3CudHPdOcGJ5HTK7l+yR+Eb7BrSyJPx9FQwBzrOsBjCQtVAgAxErynu418vEdnaSki0CAfN9yLYPvcNocxLaUl9tfMsUldBMOYYRoX2cuBVmtJH4a8tzRs043Yn0D56z54I/92jEb1qIugMBkNor9nNoq4DjcqHYqIhw4BKKBuPSaoAENf8s8MV+RJ1DgdF+8qUaX/3pPVeRyzsiu6osO3wisMtdhcLjXgEUUNbBvWZwDueyCxNkj9eGsLM9ZQmumL3LYN/NqvIcEYo/aKBtBQ8vfUR0QC3E5d7Du+MTJr7cD7hs5837uOVfrQ9FUG88cnmiqRZosbcth+1vTaavN2/TrpFNHYfMC3qocfQEEcU5ke0z+k4Qg==
takieuoanh4371@gmail.com|99:fc:bb:06:d0:07:b5cb550663070edd7d651fd65dd1e677:C8134BD65DBFA1C1CD4E996FAEB450E5:NKbBpi4L8jrwtAlyyWMST3l3/cBHjDE4WN1IBXtau0ex0UPQutazbm1alnVVdq0i6xCnMyEFxFWDskmtCrTbWBkD2orjkLDQeKKXlAwZyxG05C9nt47m8XEeGsEdFYVIxiDlD6zoPlIcNyXt/cZLwhYrWod/9pZC8N5CEVV2BIZOxRczYP6Az9I/03EyWh0PTdNJoGQD+rnpAmVRxZBzWVIRHtfDHc1MpX+KTrP3jGi98uSMPOgFoDEv/qzOVxJfNlSM450ssSu6lanB14x7Ej1yTac2wCSlzO3JGhAyPLUrwKeQBYFGb+SCHNkzhinAa77FnCsklrQAdTVLFuJuKy8OhuPcPoyBtBiNA4QTtmsBvO8O7Vg4GcT9wpJfCl3LoYHDNBcgDZkmghk1/NJN7wVi2TfxCcdmgtay3INRX/qrWlr8qNCjQJoyXqYGN6mcjbsjyxKmS5rjTaF5EYtsfg==

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
