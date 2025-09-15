---- SC AP
local bots = [[
2D10FEBBFB0B457EB886BEE50588E148|64X0C4yyB8Pj8j325mQfdWZJVCrafqB5hHcUCer6lGGwrk3SAXQiruhAMicr1N+BJSArOACcVi3TSgBsJE8jybkjMzjrD+kjqFwsHZTOqu01Ld1XR85hmZ8vLEOahU7rH6BqLJX9NB5f677fJ+ei1F0D95tKiBmMgG4CODlONLu+MeHqQQSJw16UmjxLCrtYZjxuykIU2EbmekdrrFP9H4dE3L0c8e8okNhjuDfyWF3zhBYAGpG4rWLEyNbwaqtOupfH8cmr97dp5wH9y7ZqemC+r5+oO5t8yJNbF3bDnmwFDclJrsvxYZGjcD8vh8WaG5HglRTeuRpFkXqFNSmFREkkSj6p+WGsKDKXNjuxKmsHaqPD0QSZJODAAKYw917VAh5VwlSD2LKQcg0/xCCJuDYPknpjPeeD85lJnB5Lbo9iSxNQDRAhslZZ6gf6dFE3W9C/UYdeSsjve0wh8H1BwVNeTm6UUABc+kPXD8xzwkAk0fuVkCaq+kf/qe6m3ul7
FDC1C714F01493CF7C73B0327EAAD543|64X0C4yyB8Pj8j325mQfdamGHVIMj/FjYcYvbyBehVjvQkzIQKHcBUgs193Wgq8zwhmbCDVsI4E65vWDCMiTBihDV2NHytca9ayeOJZKol2hWjiL+NUKcVhY4WNvF644SeOdY4JjpY0vr3tjxFqi8BuNF2jIWV+mALtf98rnXthWirhsJUvLewud2FrhXvIG0Dr7ue/9tPC20uMkJDx81zXaXKg+ocAlntou1JQARc6GVG/2EGbRo8Mqxg0c7xTOGu8FTxTGf+fYbRCmpGmVMVxLhx0jjXYE3O4f20LuAmzFXfcnWwGYtghayQ1Hkrw9zWmihGAMJl4WR3CHWRp81AWjv8GYJespegQ1zMEorbAOGSUpD7sC7Cj+K9f8T07SJ1O/2hrAXR946KkrH2fCO1e78ycd7El8IRZF6s5x9AuNtKrRWBHXSN+aKIEulT+6R9t5deVoj1/a5+iOvmFI3an9dzCEtzCG+wf57W3xvuaAboFIgcoHEhyUsyOuWlj6
BBC9A106A0E9211FD0F18847D57CC397|64X0C4yyB8Pj8j325mQfdYFJk9ENsVkOHNMNJuujM9BoWLO65C8sACYL2ioTgIAkEp69LCyWGosUQ09S3Z0FQFxd4vAVBgbjCkqzI28tBsUt8c4J3sPbLc1lbTLELKCUcVKqncv0Zdbxxeob6kKzyYAO4CefJE+LpQ4tEi4UT0WMIowCMUxFF15HyIYAceN4hPw6v0m7B76sGuYIZyuhaXyU8HxtRKNJzNoFf96r2RAA+xXCFTw5LTEhA+QjzfpJ+pF0GQbF5ss6muoZL1U8XIn0c4GsBQFAnWD8FI6N2qRWxUafnW61AcvP9fnMTCK9LvYth/fLUcx9cSRZWzd1GzgaBoFC6/gR482Txq9KhEMcP/AQWgt7rJJh4rz+EfSYLCki1Z1yGc2bP1fVhux4rR55VPaJdUb6AOh0ofvGI8vcM0Y8fKJTepz+CZ3ycf7NQ8ujps+ooXiFLdY5c04TmguysLxqLriJKogNMR4/cy1hXzKAGOOZjEOfkeJlhh76
50DA723216E2C2E16DAA5328D70F6F42|64X0C4yyB8Pj8j325mQfdeaLyqYdZB9gk8Ifqu9bBEXwh/gJuDhBDYsU6D1wqLM+exbq6VtKEAEHgkqk224lLrJ7TRwQveedDMmz8ryNbL/kWl+4J+W6hYcbV8SGZHk8xPBy0ScEJ1mb1eBejPybU95iTbYQEklyC+Etlu06rJDwsWhZiQQuj4h0JZRsmnG8Fo7pkkDiuzSzq+enDIY+chlWtZd+Fdc6YEzePMqgcECiOooFGxH6HSYMMHWEQbKiL1GKwtPRiv9tYXSShB6RZZlmQLvzLz5xIMFrYfpnbiap9EaQZNJwjTZydjBK5dHUFeP9cVmoKv/Y7KWlD/YEZ54r/OhhDNoN76Ze7frqxKlk7DE7ZWP0Oq4C9zX2rw8O+dIr29X+uFIEdLTmaqkPWMO6A95BvbvMdnggmBs8GyWYg2mBeNa2XIBnHwUD/DQKKY5bgscy+qCUAhsuH+GkpF3MvLlNsoWj/7oC7zFtPORIEXobBgzqoGIags26c8lg
71CA8D0F8AA0E865CABE2D40410EB8E8|64X0C4yyB8Pj8j325mQfdXoMrX3RV42oI/KAita1HbMnX2wTNEMnQTzBlBW1WRlxV1G9Ovl/J5Xuoo9sOpfdhsXgPCUCx7fFOHp6QrI5gG6w67qW+LfAYG9egXCTjlK+J+E4KLVeh3e1BF+ilgKp2DlfSxGYbn0rJwLl2eV8eDFcv3nzwx2fPm2FmcG+AQw+jHSCKSxNtc3z805yB3axBZurgyZIZwluMViIYwUfqfeh8MkwfXbHkaCsjxHLPsG0t8VbCrHxO4Mecbri9/7tD4voaH5kUWjKU24CrJ2xTxwXm56hJ3yfdmqyS+9+gEJ0J1sGpI0wPpCLwybZRt+riDMdBfaVZBHfNkeN3GX9eth/A+OqFVBWQMxJaZ30SIynL6oxDGWgy5yH0G7mKInWPnLayyT7V93Ph77dOusJ63/5U4cyWigNBHjSna7NudALwWc99ORhSDUcSZzjMh1213eYBJRL1xgj4OlVRH9ktbSkGl3X9u3RGxVtFR5375vn
04985F57ECC39FFA12E65698A8097AF5|64X0C4yyB8Pj8j325mQfdTOI0dyETSB2EyhZeSIssorCwRwKNIFKRXf08Wbsy/S1qhhZld57HGtx47udD2PPgHtviiu36KNn+mah55QFAX+v8+1jgvyYHNJ3GG2L94PJLUm/wMbayiVxSY1BoPmZQP4/f905luQOohO8tvgeU3z0mEmafou6uVawf//Qkv+dEEfPowEXGXvxOY35azJep+ezceJ5ug3XmIoIjsPVORVqwEWLLHT8MZDHYCvGg1/EnwZSGoavnabynnNmpNvyarz/ijLYkKAqg2tomYTS0eSletlMic25bZOOi3MFidYFFEqxWGPT3O2B0sWr77k92dwN7R1qM4FpD9W+nGhHCdtEQsjNu4B7iLQHS1zf54RkOIJbxSLzfRxAQFC821qMf/NSbnYP8pZ0yyNgG/zgSI8AoraLzm1V19dRx+Vge6VTVv9LDniGhJFeDL3tfxX5tPx8sKx9lAEBWI6ojGjWrYRnCXo09XUopN426NiZzM46

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
