---- SC AP
local bots = [[
7ABF7AF38ECF84C4132167115BEACBDF|FhBZgsGS678WdJF/HjzsulLM3R+yWjRWBldl1PKqhNcyQO4khj7P6O0PF5kK4S1EgaJiVlmlX1cz4npOGPE5DEmM82y+O6DKBfHiHN3jGm5EbQdphkhzqbo8BUuHziMcSMYUK695Y+WHt201vzR7VdSSD8hAIMlbU37M3lVhhcXHISP+X0tcg6NhZgA8WqBKNqSsHktAJXCRKRNpcqyP2ccGZg1Pcc/E4eDYPaxjvhy3fjCaKBarQMGC7wl7/7xioXDqdE1Fh4xr+nTMCI741a4WJgMFlMJaI1lgkLcIQJFy+TasArZvcdGS5bjL+3mkvqlTBA7XpCC8nKPU3J8fnNIz0UpUDgGH3lDWQR6kouapFJjB/+Guwhgee+go/zsH8HpYe+Gc3d0/5cw5YL6WGfShLjiZO5vIJ0IZH9DI6h5CRTn46XYLmehvXYHVRo7/uArmd3HxywCzBQ7GRt6LzcjQFQ51KJso/z2uCzLvM1JS/stWaRN/5oyb90CJUmdO
ED548E21F0C6D4369789A7F96D33BC04|FhBZgsGS678WdJF/HjzsuolQArXVvQp/wLeGzEYbKsVoH+V8Gh8uNKPCC1gtkCoxKuCUksTyBlkdO5AS88sbv70Pmh6v9w2zfKeCqIbrh7wAD10SO2MxSkeGoy3+O8MFPddvaaunB0xMx8NY3hve7wdw8EOkUgfOz4dWiv8I0ILD1wzVtntzlwdg4e9VFvMI7vDEw5yXd6desXAiMlpZOTCvUWQT19aGTYdT3KgnieRS+yHx1+PsfZf40j2hHm2DLPO6l4fUFw78WsoH5F+FX1c/JNHT0+IBw50QVT6XBXR7mPSTbg005sTmpc5Ez/KVQ30MLLMJu8JPyOT7JQrSo96gaAcn3J2iDM+sDm4z51bVE4BnwWrqHIt0Zg1Hq7BiLtVFPt2biGmNXl5zlIJ0IKKbwE11QazkMvnqzz1C13ucFHpjFPgpLLK5rxIh1nKGqNEajaRn4qM/Mkp9N3G2qZb4GHJ76jMI4fVc/djiQFf1GDCI9sgCn1Kc7Wrtfw/4
E4358551A9193C0DA946796244F02DF1|wtxoz+FRHXYhtgw4iVXj13KKD9i4hA8zdLk+VgUCfBiO2yXml5zAkUhZZ0m/EZRctCplu50e9ezXwoGoO3CMK6KJrtiAlEtYsODet6cgJqT72CYJS+mDOQUU8SXP10Y1ugePX058mK4Lw5cVYWAqRQ0XVC7KWQ4WE77q03llSdMnH79uIBiJwiLEbZQUP23ks2w9WtOpfEUSTPNSEd8FWb5eKNOdMyCmfAH+1p98UArOU4ctBDhlmsq254CjxnYgvzimCyyNonjn24z5SqxHeVIM8gfT2ePQfAycseHclxEO72xv7wxNnM8Y78LNW67yWUUzuVpVAfRG4IJRPX7StsRYOTi7OsT2byaQE2R0oiByKwShL+YlOIpaqUVLNXbtlpaFbjxPM9gDTcS1C6G7tjn9zWRyxTHgTeX16RXol2abSY90x2Il5A+tOLTmZeeWv40/A/v7KSLXAP/AUSY6Zuaxw3XhnXpiyPp2MVHQjv2PcIAO9xJMfFVxnPH17MIQ

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
