---- SC AP
local bots = [[
6381E7127EB9032A94D3FFC6CCAA9F16|BEMNEMJre8Q8syPw6oX7+9SQQni0F1kerUOzcUmUS8moligj8jZg0mldYS0moUQx3oRZbMsLXNW7kNcx0n6atcjva0VphtOcxv7nWY0KIuuAoWD8dm8yGL6gFlUK7g2YOSUtvvOG5LCC3gZXfM0XpIfKSBNY8mL5ggOgotTVuBcqXl5IqWDf3DH1bLWZTf7EXcB2MtCO499vyPs6ZBS/aomLoX4uRyETRHfWfaiN8WC+G8EN/6I9QOCKv5p2QNwDDHT2JVxgUwPyjUeUOf9P7Z3dC9RddcdcE4pFFmAFOEVUPrz92NXX39/4z9r9LKNweUC4w8//L7YJCHDSxmWF/0FGS9e8s4EbHip+iThJ2w8qfpfOT/pAodUUfieY7HdTgm6+YYyXEv06058kLoF2K8n1/80GJw6GthjjxQbMF0pfrgRLORSvkR60M7PMMxqgKE06pgLxCTS7k8O8mq8pL8e1jxOuArU+UsQ+JeWj+p3Kmbplk9gT9l6qaI1SWfVY
21912E237A06F24838BE4F712E9D1382|BEMNEMJre8Q8syPw6oX7++BvEyAMvEs0Fj7CuoVwTFdmwKoKwVFTitj7c+wtAcOKHMjSUD6rVuyz/7gDkGBMpMu7gC0xAOek4LhnEYSnwDQZ7/LkVTbLS/ddPKrM1Eeknqv2ki0DspE6GAH1+4tGovVc3M5uLVG31EBErWZGXS7fHEZbJXm200RCtlDE4eUuG9++j5b7A7ZdsQ9BUuren9hv8KEdrMu5OOXp5WQs0NaMabIdsetfjmgjUqniezYxUXdq6P3/KHa1en38vPagCuEjslyCSYX8SDeg57jCU93KjxvflDe/hQP7rpN6eZZgumoCmcDp4/2D06/vm1Pu4LqTIllzUM1n/8vC+jYKpwVeR+qRRS6UalltoR6ATZk2D0c7updsPfVttXu6gJDodXaj5PUmu1VQqWUNxNsep+fTVGOqhb3svRxMN5GL85xA0BAwrKuD4cxrm7b6ukdpzBxEpOJgoNHnX9dVZYzRxYONsGVX8E5QwiaSTiliH2Ya
BB4D1E3D5CACDB33E30755B3F4139D55|BEMNEMJre8Q8syPw6oX7++Wz7VRI0jMQ9YUyJyfByzTcZlQLPt696f6zhbecQsSu6JMtqS6/oObGyjjZGfZk/ewwMSA9wSAugR6wNE5WfOnEXsHTSV+Rimw8RzM1iZa/mrIzodhIRCHa8hO/fdBarLFOsHU9Wk79tBEhO6TEdI9swLrVXL+nIc7Szb1yZLq7D4l/vMmBuQMjfPKw0sl64zKLto4hdRaztnO1aHURp+Uhacl5c7jhoLOLIhQ9Ae8J82reInkKeapSdBlhYcHU316dE89vD+qCK93NekG8T9/VN3zQNbHs44TeQvAPGRSfIHoSw/bWLkk/FXphRzsYAtxImwCE5hYE6guPYMP26Sk4ePVNlnuWiFg0S7A2OLGrjpLqxaVQR8gysyc3bhnV7Ddccb4gWX05d7FTHGnV65OY6j7lNAttQ70lgvMNZB7wtlLvCI8gVbNnKdaDy5sVm0F37I5S8YAR9+wZwoG2I7KKxzyCVJ2fi74L4FVGSkeR
FACF0F03C2CA52E6E2F09966978D1261|BEMNEMJre8Q8syPw6oX7+wooFlud3Ri0dVC0vhQKQ2lhOO9jJ9yYKKkRmQCRObFp0OwopV17kVFuxUWQbHjRapl+Wca7YMVqWNkpunh4fe8e44Nnt6AW2CYUUbwQP8Y+lsrpE1F2t+1VnL9nxC7xVpfwV1kMlP9b0hLpWJ3rsqpmH3DDWqQqg8yjaNe9uyETkSIu8gyrSYOKJboMZKqZR1ePhfYW5gEU3IM80vI6M+puSqTkPJYjGOUHTlKZbUVEQg8Xggu7gBEFx07/NEe6tmzzcBMTB3VZkrFBEgmEtyTPtI3gC7mQHdc21OF97jo8Ft+xL7KbRXsi02KtADkt79pyHOn/r/s9s7X61gYuFQayS3B7qpG5KXW7FJY0uz71XougouCSL5JKs+zt7gMnzQbXkJAGySpeRfxnkl6QBsAOeZ2PSoA3wbUPSSxt8dWb/q1GD5xfdrLcvRSVC5YTYgUIewGfjh2qOvgogG83k1VGevh8+5rWZfsFebiaTJxf
36A37A31A52474CE7D17ADCB025939A4|BEMNEMJre8Q8syPw6oX7+8MY5cbx1T5yya/ftRqaTyWAljA6TIJeZH5woqDYlJk8f6cREEFuXB9SxUkWkNKr5AyD66IDYpXRWVR9m/8624wJhn3iqgce3ffkCLRQhjgbC3YP2VkUD8xK+nu/SWmdaq8mUXoJT4jUD+3aYv7rwj4T/EVgcyywo3gMtZ6rRC62XM4KNUnqPQ3PBXjlOjepajljKPUP526L5Tx94xecP5SVQi0MU55UoBKgDeXfpjg/HoDEeyF+H77vCE0fJiDF8m2H7LyqTOHd6novT3/nSaU1BdiV+81KsdwdOcDzl+YdD28ynfnXG/m33NKKvT2Mka75xSRAv76KzdIAt41Oh/FkB64BlizqgsV9pMCR8NAJicHc48ieJit0gM7SBiW1mZhZ9PuuO1De6q1GCtBHX5ieN4gH9+8hBh4j/LGaujA5n4o/2Sd9PQcqNIOy8lQ2TRe7gbWNKg8Pl7Q5uhjYKyo8zDSvSBud7BdPJzD9p7OB
EB8306403262493258678D8889D32977|BEMNEMJre8Q8syPw6oX7+w2ZWjCakWWdOvhCiB56nBL83e2PexaE/koMQFDJUj9jAcSxWJnc26jtwSLm+/DnODbDR/DSLTtX1KEr0WYdw93o46IMrIOOZxPSJjLi2sd6J7tVX50tCj75zLiQyF2vucG+ocZuJvx/mEsi1IA/h7+c+vDYkpOVlZU3BvP/J/MJiQWeE7PCltpwYSMEGCXbh3RDl+5F8FxcBg+9yiPmHq2TvZ8VWD9yLcUKSOm1pmp/75VvhPNEwhE7iBHQi65f7J4opCenCegPWzK2qU079d0c+Um0kQrwBBhBKrOX+tXZqXY6dfzrOaa2LbuNSmS51RRoEOafdqIEB7lh4xipz5+nGevtsWha1hg1VUHsDcij+cvbNf0IkEngkB38+e1zoJVq3n/eOz5rTlzVMlj5DfCyUN+axWQ1ANdCAEtWKjt2DrbHz49bOSl861GrMwrvhV3dBpRExM1cteHYUFshurNX7yarjavbYqECvBdJVtPI

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
