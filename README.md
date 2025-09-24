-- SC WIR WINDOWS
--- SC WIR

local input_text = [[
wir_ibbt95fmglt2narz@gmail.com|gkXf/ScUxrqjxncvljgLHYmZx9X8z0dSl3rVb9zJs36F2ZisgvX9hcqFZh92eDXKaWu6AUh8QryT51I5IUISuHgMOd3qYx20bMRAxqsNhPyCUIXdUEdVsh2/oSswgnnjfh4Xy5o8xr71sN3Qfjl3MUdsmCjiRNbXYz9FhiDhGZ+2gp7RGQ01Epbg2CSw4GNtTpo1tzj8vXFVjS8w2WTzzrNq0Dc4z7bSPzrw9tDtP7w0iKWHoGf7JGhXSsQ1rYT6uAjfLm+KFz7euDpExxIQG39oqr2PDThZxWn/p058D5/anm/uJ7cvVvGn8DRlAu6D3HKfz0S7Zsxqt+z6O+opO21KIIpPvtQ/K/TE1Hruyx/f0XofI/ZNUXR+6uA9MR1g7BLgooi8ybu2JJ83yvsnNgPqUYLMAXsiOR/QpAu2HTsotkwS7uk0bu4w2clyrOqbGqp6DUUuwUaEqeeIj/QanlHDA6KMaQ3OZxgh108k/kgNO7hgpMg38RldXEsSr4lg|MFHP6WGXITBNKNE6RF6MZAGQL5YMLE8V
wir_rvf780ss5rre7nfm@gmail.com|8hS/97tatupWgxesdnM6VtYqMHEvK9QvlDAZc2BOWvbKVGN749cTQMBpDC5ztWSjQ/JRJ7DUh/yI6ygGLw2k824/asedfj7sHKKltcybrwCIaWrX0RIUklvjGgkzmlBF4ytvIrAMSlN2dGBNmrCg5zyRis5C7MM9Fl99crkk3bZigg/muqHjr6eCegGw+twq/U/+3TB5y25C3J7OloiZg5KVJX/2OElu7Ap/5bm6ndRVUrbeqBZHGt69HJHSDzHXkli9YJUVJT29fA9UJgg8XDz2Cx04v06pGj0GDe9CXnAsOVJrN2M9NT6+tOQPyN9dRop/GZlHobJKxjZ4khPznF/nll8mgmzCGzExUjbRzlifO7KAYEH89dBWCbQNxcPHDJgqEPhN2K4bzB5jGE1WLTqnyqo2fV0IryALeG48Drbk0MrFEPZFINRk5dSYFp2FKADJzZaPGOOgGLAjhnhlKrX0uoPElZcwozFWVwmYGOIo2Y4Z0kfKgVcEIIcMZoWN|TSIOYY97F0O8JICAW9WXH0V7GC2LPQCC
wir_b8c7nvsdsao1yo7k@gmail.com|8hS/97tatupWgxesdnM6VrUHq+dT07LyWH+5/KNJmtvUyW7AaNHn5SJ34mb4idiykFLTmJEjSvl6TfyTInuPFYCc7MjCEfGYTPEuw8GSjqzyOGUllhzpEH+OavS2GwTA/1KIAKGWf5hv9QvxIhkBO9y5DpWag1YADD1VzKJF4FLuPakACbA3oWIuCVAEuDaJTsFpWb/9g6K1BolDd1c4R92VkqtmMYVwk9DirTi+M3VPYebhd9Vr05/06hrXUs0HiLGuu7dHH8w0QuS3rB4kfN+PWMXTqBxDEtCs4APlUGZfEf0Y4Wh51m6h5zFCkXJ3LqKyCS6/2qHTlCSYP7D9kCt4LnDNtl7UosiMfBwAUs91Mefy4UyQ3fBBEBfisWJgGK69O9/5hdoVHLhXTc/3Oyc4HZpeVwR8c6vys9hTEpnCpT7JtRZpNXdVPkJMyI2pADA8kc3cs06CoCXwbsO1B1Knl7EXWAiDYsQkw20wt3ODNDMYSA8eaN0yn1zM+4TJ|FFSTOEA0QQN89YCHROAVPD2F21X081OK
wir_qw8q4cu87xe82nxk@gmail.com|8hS/97tatupWgxesdnM6VsalDf2YxrCMchM8NLxqWkDZnWe8a3x0ocEu+1UAVWDwOQaS6UqDsdvUz9fuiDhU/89BF6LJo2weE5hj4JCbhLJAZjGoSIvAbdZg6uA2hdYx2mjnWtA0a1hrqMSJ21QsMUNXwqi33MYrvGVdNUIh9Ed9s7W7RXq0SXPIYc983lXDn+edI85eDMY5uKfTEppI/RmMy14xT40JJXyZXrzfHcuS+bQM3ZXRhzF2f0prsOLrskKfYoaeKy3mTAZDUlv2hmi/Mfj4s2WYdOo5qMmaTGN4bxEE53NuR1R9uEX/Z4ZGoN2/m58F5inS/upkRiE9eCapy+px05k15m7FgTP9XRHSDm51yGAFUSvQkO3M9qL9NBb3xNbSnTGFgWGQZNxMa2fcHXb6iNzHie7ehWtb4FKLtpRy7tixOd6VPKNrn0Dn+aK5jJX+QCY9l+xsuixCEY5nVeScAGodKFQByqWDsqQRcO7ZKLLz9jRQATaufKZd|CVYZFZ3NVCXRJI7KKUN3ZEHR38KID7R8
wir_c0zcsm816sqq3a99@gmail.com|8hS/97tatupWgxesdnM6VigEO9BBzZ41V3Oeobv8t2qCu1N7aXaFsJD3FyHiX2qlTgbiPP2NwI1dou4QrkqKDGu3hNzSbZACrPU+ubQvgQQhDHgfrYmwVA6EvkP+KaJfaiwqrddKQOl7HoWN6YHuM1BqI+/Vs8JIKpw9HLeGTjNv3pzaKtbC7de34NpESzgl6+r+a7KNahpzgECLyL9eZJIttG7JLZ/eSeeE44bw2dFeIN992s9fRs2GYh1gzdq0DdZNsWbLAqdSNJ9GK8A4Zz9S18Cn7zwodSKdbJFxh2E0Hae4E8Dyo8Rzj+2rDuo6BWxdkWzJhWe9HgoXw6nNlCNIS5PxWdEABkVv2z0/QDD2eg6Whrf2pzb1FfLLxbsKI3B3cM0AQ5rxFPJhLrEVHrDQsCIcOzTf75pgFazRGE70TtuQoC0gEmfATPlwPIPKWwLbjnfrSO7arp9e57fbgS5aASVuStg7/m5A44XniCURuPCiK2LssDUe+x5v7P7A|T2XOD9YWJCCSUABRPCB1E4AJS4UK0ZI9
wir_6ee01n5y1se7oqbk@gmail.com|gkXf/ScUxrqjxncvljgLHTi7DlRQ1FPuRZnPF//VLL7uzaqwLAP9Ko1vMaoIIt0NNHnSHUYo5ZjQhll5kj1Uj1/vDM+C2XhHamNBvN8bOA8iVO5S7zj+DkcACwi79s3nFs2s4qjNEY+cmAJhFlNrwTpVJLMUpebu9+2pclOShwilSOSv1svuvcy01qaITo9zxhpAe1E2pIvPskVAFD8taOLzs3PBIg4ceLc8fhCOfOY+7I70SsKN/ObBmLGb0H7ZEv7M8eLQ1xVc0l6hA6k0/MNL/wjt7vqLZCV0q5a6WqTZw8xn9NGVIltuxI91Fbp9DSdt/4Lgfkx4/2VqcfaOmgF7UtFCuKFpSbuUU4KihpHOJ0Q5VIBW4myOsdeydnCvv5KjlXL64V+nSGRpuerDJrsCtN4wvnW1aXM808MesGHO7PfetPNDZZmnucycmrZcPnUk9VTd4mVP7TNGl06isHpXVdKU/Plq3VbGdHscGJXRS0sUBE/QZSK+vFBUHFB8|JUMOLQD6YTUTE2O5ELB1M197T30ZKB34
wir_81bt0mpizzvmne1y@gmail.com|8hS/97tatupWgxesdnM6Vn3tIPjRw/mgJ9gVeQxS8yg6arO38odT2eJrRPihXKlMPTax5BcZmdUw1t99321c8u+K0xODj8GdBKHAI55A40RBvu6hKlJiOiTLnBMep/PbpRVZw7WZ6/NtI6kxzXwKHOxG6Ntscpbr3AB107d2TgI7uua/XM1pfKII/RdLphSqysKVbWt8bGo6kudJsfQ0wAGYSZa3Xf2KxFOeoFurPviEiX22YLKo016bjRJ9qBXvnnsaXjZcjwcYv2IINmCN8B5JwwmzlQiddUD0Wvfl9vY2Sa/ukUgZ504zpQ9N0eCBefEcz4PsXD0cnog6jipz57rF2ZzK4lE+PBMzszcLtNa7Xkw6alzP2YYmKF5x8OB8oVtnrs7cmSF22lkvOQZHxwxNWQJV+yWXItqwQGoaZbnH+ufBfWix+n/oKUliSI+zMJdggZ9n3HYxHmC76Jtuzmbh4iYXOG4mAFRSwikDB9AdLzYLHEndpPYsN5RVaEZp|3EOUZ4PZX1BGWKDIX5DJWSPBGR2PBJCQ
wir_ldhowm5segyhuffy@gmail.com|8hS/97tatupWgxesdnM6Vqwb+zFR6zAQdJUPPwR6iIdo546COVHb5dWrig2ZMw4gS2+3iYiA7PWp37eR+BkvpmysIXicbFi23AteO0wpnRV2lj8aVDyGLN9Yj6ag3f78AL+yn4GLF4veP42jG/UKjepbKTyewTY66RvXe1LX9G2Of1tJedDqwy+h1OPxW/47NXzUkilWOJqlXe1BOj4WkncoYNNvJw28cmMhc/WYFPIoOyc9okfS8y7cTbBPy0wrpfSFBt3TkpDv8ebQtoAtw/UPCv1fO6WF+MFG9Mj4EmDenKMjfDimpEzdXyGXDQcfXyccl3BEGj/VgWqMhRtLF7TCNKV9MBpP4m+h3c95TYLY/19tUDYvDB8SHIQVs4lWSDYzVpIh54kiF3Dx72jl3ecBhByAufQPsvrepBBKSwhHDoihd19YGELW2Su9ne39ukawhZL7Lbhe+g9Ww/H3Mcx8UsAF+zlS1EqZ/SpLErl2EKOIuxXDoN6JqxEpqmOZ|TWZYLPWJ2YBMN7L9EMBTY9GH564YLN0B

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

