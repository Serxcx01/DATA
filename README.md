---- SC AP
local bots = [[
87B74C972E0ACC175380238C40C7FD8B|64X0C4yyB8Pj8j325mQfdQujXl2R74+Y3TPLUzoqsYcvlZcuQ/Ku6pY+ee2DN+IwHqrSSa66OtCiHRqSiw2V6pydR3qHpkRLsuvwn5Zwtj4nyfS7rcuFwTUMYWdnVrlWl7IRFZuhX8kKQ1NTOlOwdefgV/J4qGgUGy6ZEUXI8zlX+dr/yTPWG5e5VWWO0gKJB11hK4RdnPk0unSt85pRZygxWo3lmq4CzxG1pzWc3inpR8SlS6CQFyl6l/rbPIl8IpS/eLWsfJVyFQbOrS5aOPS+s5jgb3m5Pp7HVr0/kH06i88Hg+rdDC/Y7ttZM/Eb8UMyzQPb60Wz5bdQ5pxtPRfBAa5HxqR9A8S3JKqIdok52cSq/h/UGGJqbkYnZ6xt5nwolAN3YGrBg1bqba5vAaWPvdEF2AGuRx4WMyBwNeK0JxpzAvGyv47NTSYhrtTKSuR8J2I05d0McLPkjjFV1PicH/jPezpjT75USgIFyB3IahL5VqPnLk/xLQLmRyyl
39A2B8C760C0B8E8C02B63E5CE92AA0B|64X0C4yyB8Pj8j325mQfdXQlNBlGqtuyYrqvTIt6UCKnS7bdgbDn3KuBVmK4MvvNxC1ZZtLvueWeQxSbz/npbbdLiQY5Sn1CmOdp4ojSQ497sn8goa8MAGCkEkvKvmi2tGI3zx2S946oWyNhh521vHM4YMAFbVrvqbh7LnDvKYhVlTn+/k1dEnxJ3p5BzBUup/nQORjTL1cHoPJuPD99jEUpeEZGXWawJwWVtt5O9L2P1p97htZPiKPtBmu/FvjwF4JP/t0dKpe/A+/JKbydVkGTQqsstlVUKL8SevMyLhqkUmCcLzwnAJvPsGB3Ozn4Kt+l9I8mobGszXCq2cmMccGYOFUl/uW9NxdyAl26q1maL8RCipipGKchSUB0wiBL8MVW7/6nXFpuiOM5EwbrZ4PfANESPcDxseJfCp82cVT6Jkj4qnHRTSwAc5dAWN9Cf3gmw8ZYQEMBz1VRk24QhR9Fg4zNeFknsCcEjlWtIb1s95blhUuFnTNCu/k6rgxK
6B1C24ABB66940EA1175AB75B658CC52|64X0C4yyB8Pj8j325mQfda9OHStfjZD/llM2yH6ipZevM0W32EDtAWhnDYDRI3AR1B3c+YQQCTRioY1L4UeRlXDPIA1RREFhk3WGkt+WW+4C+DEhTw8i21AzRR2+g5DWNbSxZWa4kvDS8C1y0OQRVsXh1j8wK4X+KxnkxRJPph0xbddNXGf7r0Kq/YVqsUtMMOxSZSEOjFouikmAQMzwZ3Xn0KdU/bwv4T3eXrOegi0/U8hSj/oRXFdeiuDkepaVWDGXsN/fmoiYX396idRzGau1CVS/A5gbh+iFAUrvqdK/BNo9XSsNsZIiC5qwMSOpOkCc+9wJ8QoCKaiAs0GXeNb0Ih+7n25bek9Es5maoqDfxzQF5iCfkeAVj7zIaIiIqOfouDHFUnbGLNte0astftZZsp3EDoycjFkx+VkCfEfbqqGiISOGpHaFEdlFb+/itroxQgsXO/0kDym4afR0PO1hDxyKrFV0mxUaIsFhv5j71BcJ3gBfj91q/Ab1i1R2
381F14107BF407B2025DA822A84270A4|64X0C4yyB8Pj8j325mQfdbNafjlDyaePFAuJO5iLu8Bpmvn81j2AyEPWsu22Kj3+k+IJXilXJMZbjTYzzA5BpHBAOoWs0DuMG/IgxzqwTOAVZHk2jkBm6lTJKuPM7J9701eZxpvb6BRieAiBd9cpv8b0a0s3zng9Knvk7reKUqkrX9tGbzsItN/gZZP7GRlv0OP0BoMXn5d46faa0ovY1nM6rX4KJ3bqCyom3AiSKbyCmj5QDg0m0WESoxbe2RYq6B0V8KEsz0xt0qiblTEr472d0HrIquoKzQlJnCFCfxkyK3PzsGTl6J3JYUNwClQEtqHmKtBJQU04xXENoYAZDb8KMsAE4Z4oyJGe7ubxS7D9Z5uHN3Mix3tsnKD42tSFyhUiQEDzqXafDLy/xPk9aR9LkMKyKxlmzhAiMG2Dk38rPRA/AOtmdMpAqHXaTyYgWSP7Q/Sw9wE1hkIuvWHF4Zuf29IhlLQODvMhpAhZKF0S4pbPSupZ46rGO9tyLgoa

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
