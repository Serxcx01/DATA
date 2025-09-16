---- SC AP
local bots = [[
540B7E5F7B543CBB89E904CCED252EA7|d0gW0x40db7wGdcF2Tq3Ka6XESw82jXbpS0ejHjmZRG+vxH/Vp5WvXWofbypX1Nrh5ak45Z+JYABA5tmFmU//RzK/WtBDuByp04lNChmVMTDqjmp/uHojBnJYVP4IlRCubkKeKZ5EmWm6od7rLTdWJu+8Z9/PXe/eqDn1TRHkpRpZZaZSdA2v9kZDdZITU9ld1Oh8vFUn59AMjJZLmFWyhyArGCmajQuezxHULcPWoMTjuZivzOpB62G04jHftn1h96iN5lP2k4FwZlV0Jg56pjSF8MdYCu9XxVA/mkYggW5BwllxLblykYlBtd5Ucwztm76Fudu6mujbHF1eAdd1aWl7itN5XIXlU6AnMMwAMYbBCVXxtBe7GhzsWDSUinzRq9GfLOwJxFE1CT01CoW6fwmdUd2s9dGEybIOwLmDDz/apu8AX4HhQcv520r1RXAcwPxBq7zGy5yCG8oq3rdcFrymGz9vwmGPGUJftUWAL0Q4yJybOl7T/xQTqIR92nG
ED4D1EF92FE4BDC9C4F2C991914F29BB|d0gW0x40db7wGdcF2Tq3KYYNZBSMODgL4cJck+ufRNR56r4WibYpa5rD7ijf2st8uYg42fSWi8EtgZMZMTsXYrEN0luA6ZwVpMqK/JOxP60GLjPmMtkgppfM7H8CUhkKVzqE/vgzv43qrLKftHkpO+lLT9gKGikwmw92GSaMInZqWWGBhQ0NlYWhC7wpPGg2OzxhFn2DH8n5SYQ76q0hTP+3qMqCfqc4hLEgUynNTXCkPxJvwlHynu6ticuf86xEl6Pm12xnOWTChh+MuEY1EOaFmJ7dzAd9Disfev8OTGxO3zpPhTUwMqIaBvDcUS9jixd2eWmQdoDdTOZbsTYhkwof55+pBUCzpgvEPpeTV2tfFB+6ZjfIWnb1R/J//eknqTobEw57f6QuwsQ1uIScyttT2IA3g3fgRya/o7aZbfGwI7nxryYMZcAfZbyojFLnpFOSjwpY9t+dI3+rY1pFIV1U67JFxFOldulEKrxokrGZyB1PsV7bYmW6m7frYGB1

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
