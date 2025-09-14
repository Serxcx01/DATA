---- SC AP
local bots = [[
73B148742BFCDE4EF217184D2D88E7AA|sE6+DTdXMwVKtekKzlxwOJqzqv6gR58koCgBg3GMYvaIX9SQrBXX4j4Nf/Wht2kazV48vjPEy21cIfr/qnk41qjAS6zPJbSVekjyC6sQnNewSa9cnQ+dI3afe/8tbwf8Ph/XO0g9SDhsezpOum41Xy5HneUa/q5GvQTHSrMFw/ROFW7bEjc+T7r6BWv+uO55lg+zzPgNCIfBOlUDKIx8jVnliFjBOIa/T4HTdwpbRd0hmW6XppQhQid6cmsdHP9LCBHvLZ/uB2fgSGY33a2N8lP2BbPl2Pjq96Q4MUymYeMduucDJDKzrkPNx/hZVDp9aB+ZFvV4VLq38VbOaHHqkaGnF5h50eeum4eKlUzkgvFIvewYkifop+9q+zK7BD6OEODQCbf7bQ3p22d4o+JSFszNrJKER7bgRoBru9oFAEXshm+xcb3XD5Qf8ujtP9/+/Q82y8Yf5W/AF1SF00ZJatC2OyVWVqn3e6s+4C3Z7bsYfyEvQGDir9sOc5o0idjW
420DBB7A225693C20AB7FD30567C1E7D|sE6+DTdXMwVKtekKzlxwOBDLjXHbxr4Ww9op6lk0LtAUJVCOz2XnxhITl8Dpee/vk2bo3K8EA9q/uYRJTfY7nYqncsv4KFPhRDl2Tsz2VyvegCwWt7lgMT5yOwhgLn0sjJIG9cT4L/7tVceuIUKSunpg3XIy5/QyEQLiEaRoornkhr68eOTPRtSJ9MbHq2bWb0x5AFRpNZu01BnWu1tc+7GfDi/pmpRDOb5LexoHFGwQqw2eqtUI8j7IFaeIUZHY33FqYRlNreDSO+gme1u/QEDltMquKz57g6BRxw+BPpirwzy1pCMtdTLjHhYyKZTRxBzmWPnoM543Z9b353TouanwjaDns2dePr/XOtG3pVH0M4YcRmKtUNXdAuZZDHishP1R/AZUqG1UXCQSUlT1Ik51sUNaiTQSePzCB2XGAWh/WJXm98aHoEoI8BwoXZAsQC/oM21Yk9a6ohxGg/yvZ8pFsI6tvynOGs3Va+yql+RbKeMtFxZ3eLAJ3tZK1Fd3
0DE08CED19E1A413ECD713B3C148F7AD|sE6+DTdXMwVKtekKzlxwOLiAryIv3koiasiFvJKryhEav0FfIIcX1JH9eak7mvAAb8fzZjy0R1lrfgh4G7CsQQe1TjBRGmCM+iLLErcFoak8bHdoAROBbkfwT9Kr92cd2ZXIETp/dCeACOveWAbreM2h3UncELZPWLjVFzT2yUAOZl7ndnz1V9bJoWjWXfCk90pnFg7JxlckAkO85ql+eYM9kPt6XwI5+k+VQ7FEhtQd6i7xKzdRYIhOOJUUpzY3vi2K9uVy4xRdJWY9Hz9HrWmv2f7CycerYDWxV1VJbQkpJUYO3Lod2ay7eILubZmyfGWGT1808XE9krucCDYKfVafFzsrnkIY+AuDiJSjEJzSY+ztEb7GvbIUX3a0X9jhwITmhMdpV0m6VGeZm4tXoBtJ30bXbFxAIW/7gvLjFKM6tUtRsJH8ba9KdtSKu/4RUZ1XSbg0e2WKsU8gWVMo1lyIyfLY5ATNhr+SLYpBYASaH9hTNSJbGp3wjd1hNiG6

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
