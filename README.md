---- SC AP
local bots = [[
106792EBDCECD010D4ADF357C3000DE7|d0gW0x40db7wGdcF2Tq3KTfSAsvSsB7nFoNmm3mJc+xMZEQvv3iisbsevZM6ssXN1aM1UePm5Ztmp8s6yT1t85NLPvBA0462ekTAieZ+o9dZIw0mmUta6o7W5Qtmn13n7sbopWaDJ7LxPcdDGbfbQhw2hFjg60N0ITF9eN6oZTiRlY1CGW/iydA/1KzvO8WCit2R5DQiOftbkwAyXGmMO5I9lJSuOGIm4Ylr3saDT0lrJydXZ4+4AExVOSKuKvG6DRZylgQzqWEcrZAvefIyWMtB249WysppliAuvsgFpFusj0HXLDpUsiJK/JvJh7TddB5R6VLDt6RgT9jEsbPOMk4rXvdF1fPIpSQMVu8JOK1ncokF1T4sHb2u1UtGsBUA1NyoyPTPIatmGybjqJ4M7D/5M6Bp9DQNd10f/Is+e3gzocR1Z09DGkXvdf1XTPYguBlfZdh1IV7v4DLU3ZGfQO43ixQP1Ex/40r5+1a0U27fBlN9gue/rTVMJFdaa/9c
B2EBD68C83E4F5F94A8225C8049BFF55|d0gW0x40db7wGdcF2Tq3KVUzUdNhxsoMCvSoiYUUx/ZFsrri8o30ApVWOxFJ8TghGZwGDlPtewei9PEGWZzZDdLt6ZiLeWIdsvgJYYA+DI/sWjhwG8bCYzkJk2eP5KCkNBZJgyu2ZTp8kqX65Fw87I8jS93tbFMfBKTON0VpcWYSIowwsEIV2mSacXnEFh7W4DA+53gU0LK9klOUYoYuhj8bQ+q/O/f0dFI5JXjdJfHg9rmOgTy66XTB3tnt1BzER1yLxBaX8zXJCxKtraQFf53CA8mK3y6QHQ2LNvFCTZABl21U35VBlE6Dwj5G5VNOQZcISMZNvcqw0Z93ku1YB+tfJuvptvMsR65PJdUtI1pjh7YDcSbWYDAxDkxzfLaHC0YOVEOSrtfz8KzoR0s1lrfKEJedbbbUpOEt+WKpL2eTXnBOxRMfh3zO+oxySUfe5NdZN1BeAX0ZVdw8jDwY+bCDzkJXKUnfzBaJRYoeXGYeaLve62qoHjHKWC9AgpBc
193A72B400BB199B4F8F3E1AE3383308|d0gW0x40db7wGdcF2Tq3KVXq2CbyI3xHENXbQalbHwlgkFWlhOmpDwFUefq11ouflioHrHH6l2J8Ayo6Mzw+e/XX6KGrwXgnCGJ3TjmYwddyKePOuQyxiu3SBrzranbDyy9WyFAukPSk0CasqDN7XpgjVCg82SgoiQWLVIJJQLiY4vH7B9emnGavNUi/zYRLqCUHIAXLWFeQvK9hbKIkY9+Mp4i3dGUYM8CpUli8TLoxxau67iMTM3iHS2T3eV3hKgEUI6OfgCmI72jQPRT9ZvYF5juT/sgCGOR5pGBcza9+/aftQaVD07LTOMWzQYnfZRo//33buKQ4GblyRpXhIWx+PQ7oCA7+FgX5YcFl8mYtFwSRgQctOhAzn/E7/Viy7zbedMxbSvX9cTBSqgXttGy967IaNYh8Y4VBcN1UeFzEPwj1r23/Pes1tCJfRJ36igAJjKHNMaqiH2SRZVcLLIoeE02n3ndWawV6Jzw2hxH9i30zNvPeovtkHNbMLAfb

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
