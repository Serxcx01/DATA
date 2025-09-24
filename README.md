-- SC WIR WINDOWS
--- SC WIR

local input_text = [[
wir_6v6ktndsscf73nh5@gmail.com|VGSFyd+AidAOTdpa3o8xGkCWWXqPo2mrwx2fDl803oii8i9sSpQm6dEXbe8NfHju2ZtJljCMamTvGnDmOvntZ9upTvK5QFfXGQCwo3JqidH0PDtd1BGKxCClyhh9KXeWs/Czw0cllmi0J7xXTlvy6pVnqU65MM7R12euXzZiffLWh6Ioxv3jXIQkdTKFu7ADtEAcv06o75TMP/IvpKwv8+T0LzrAOkpBjx1VJegKt5jIfcfRHYpt5gFFVqNyDuMqwOqF6jHSurjcfsV9Ho646VhIv7/RSCm8ODdDynXhMkVeLLRY5lmE30tqsdUXUR2WcW1nGDTYq6Urm4L5sPW3Y6tjlgnD8VvnkzlTb2Jr423FnkZOWa2UB/4/u+JsVTj6TFP2t2cyW7uvxpzFwEHtutLWmbs7XLIGs46SSKYN/Viv6LIv0lqQUm0MO3iFoChKPIjfwC29sdllgaA352vK8YeQqIeWmwCB3XDwsFWKypmN2Yh2hwHa7dmBvpghsyzl|TZHKNU2K6QRVT2I78VMIEVWL46M2JN6N
wir_rrmidjejuervjgso@gmail.com|8hS/97tatupWgxesdnM6Vt9AGfNq0womr94puvzFVWuiYbzTXMW/2+n9DoQBwZfwsRpJ4LWZVoyMkPqGj1LqUUiHAzU18X6fj7VsoR0o3w9/T/KkJI54qk66BcsKHKi18plpSciLPFi10fscFLkFgDfdwkbZhvKJA1iHCMG+vjSSxRDmFJoZTtzyvBLK9nW4h5jevbZtQdF//RHphS5k1+ZhE1ti3QnqTbE1blG+sYhdO5/J7M0nVedjmGSKO5HZRxz5vrEudmju3AwMjqdeYYkIPySC/vtyov8Yg6XYlKDyQGoUazEdmF3ZMP09GUgBoGIldyzr5un6dNWE2JVpPl7L/TFlwpnbZ9luv6cxXOMxCnCwKlBE7nzi1bC+2fySFCBhhfJJw4Nl1vspNjB0pkYpS4bENIZjK0DYD+9uknQpNBBr+TP95eSKT5Lk88fUPAlR2lQxHpfcPxqdWB30L/uNqY7ZealWNJ7VCBO9BC0dcwSg2dTn6XtnXasAQWAe|89G4YQF24EBD851M6WFFQ5SAGJCIQX52
wir_h0uw1ntdk6zuraku@gmail.com|8hS/97tatupWgxesdnM6Vs/gnTNIGPgAeVGLVaDNLb4VHmNjpCdN/00qh1A98K5Sl7OGDw7MCppHWlwNs6BRvYWRrf0WSpfJjuPtv+1Nr6TC/bQCZwjo87pvdXWd9AzaNSc6kfpzunOnzosyJXajhrrwevAGrYxRwfV/94TxJ4ZMZxDzHdSgVVW8Ku+T0ZDTp9BEw57HB+iiR/o6ic3hjI+zzs2idPhHxJabZCpGZBlJrOVr4EFjikhCk0rfz3TxngrAKgoK6ciewVOKIDESC2EQUf6E+7ScaNMJ55yD/L/e3WxTGq8EoBKsu4+Z3SGjn43AFO4gP7W60eD7I2IIcOcWR7uGkffsMbvtyjyi/T3nxAOHOH3ZgI7UVLn0mWs/uRy0C7RPpJPk2GczfFEj47mIk55R5VPEQg/nknu2DyY3vmNENX7F13G4gDmNkRorkz9P98F9TJ8LWj3gqzjbxAEO3EbMU6O9/CAAVLX5e9ieOuhgkh9kAZfp3MpHbAtc|994RW010UZUBL18KCR50LG7JN7MJ2XJE
wir_sgg78k2hcbugqcay@gmail.com|8hS/97tatupWgxesdnM6VpcCc//QLZ4OuIunKqSxNUZ2eT9BMzCvZZyu5u7xal6j6vp8Y/9FR9R3P3wzr4Nb5vCpM6kwx6tSULuUMFCl7pkGOv4eHgVZgT35wu6ffU6uOMvesWo9qxNDU2RKJ4+wzd8GT4njQ3WGS3/zlYEfOT7qkIE9Gcduh/P5SvMdh2VlxjXORTrs/T/Y5JfgCmRQabJleb529E9Smr/lNQ0wGJch+FM0ICF7KaspN0xgLKUzdeOHQRpZZKRc6rqjBA0mOHiU5P7vJMtAnz3+gPVHr+PpX1ECMI/ubDj1h6z8Wo2l29SFqLHi/8mGJAuTsh3NLnKMfgILdiWFDqiZs5Ui/Nq4wdSalkxWpAUwtoz3NCP4vxcGeJ2s2Gb0l+suMv4cJKCxqo87xrUXVgNPZbWyrvms1BKAuEOOiTNdpXtskHFyCOXK9jTAqGnTp5eRZYI9lWLsUDBgIvX6RzvrvJyknKPSgCsYIqVqjLE2RLwdUSKW|0J125DHNZ5RL44KVLU3F4TLBSYFWPNIQ
wir_05a4y21kbxqxdzoe@gmail.com|8hS/97tatupWgxesdnM6VrJFlhUheDt9REvVF8IT4YOAxcdtMvbq3T93u2E0dXrcpRYuZZlJNOGrqCtwHbdfk6wAMzA4Lcs80Y1c2RtfiQX+56P/R/dzGAxN/3MLo8Bwqu6n61CaFbHIruZi19HmGdD62SmoFjLBgpDMOHYXJMsB2+ksvSfHUBocmuRzc5nhFWJGRrnJhC9gSXltoZKS1a/jM+SWmQAMMHKRMHpPMJjIZ3zBSmrbjwy5NbmyHaHQetTQ7OtU8SICxpwGEhlVYuFywNvQ2FBlQqX7IxUdf2I7aWonlmzQ6zTgFC8s3sNn4b7EtrrgGF0RhaDDQRXjhXzCccfj4k7A93XrYh2e4U+YX9jbL/EZ3etlwVZRC2Qt3qXbIK0h9tH4WwomhXri3UsqFyz44wUXyB5dxTtOPFxu5HK8OCpOH2Clu7jsnLdfhjHuL/Bn6GLli1Y+RKnKFRviiiZca6xAwpZfNqxNU2bA9ZngvITCXxumODWf0tvI|ZXNRSS45BZF540P6COW24G0CJSYW71DA
wir_dbnriit7iigtui75@gmail.com|8hS/97tatupWgxesdnM6VjHDHl/aF3VtHQzEs+87slALqgldPtNZ412aVr9iGN0cfMetKEtlHQdNp2+F6l4CHJePic3/NpZbhBqyCHRA98mGRpyUt0vq1S02G/UNWEQgBs+Shr+X9vODUS1DRq2N1S08H8impUFWf9/pm3QQjSHJfEy8qxTHNOFAEJx1+AibrdVDYZ5h3KHjJygdHA+RhrTiSU7pr/z22Ixi7tohRTJL96klVJTbAjsgdDd4M9EauWATsZV1t76HP2a831Ki3D00NxJvNyQi4VBbJP7TlQ4pXve6C1aEkZThQkLzDCoUPL0xS2V7k5n7npzW04TnL/jijG7vtHarYfL90Spfw6EwSuz1hGXpbvJQrpmuwr04dDvpW1ktn702tE23UuNnP6XunELchgdkknldh4Rw8rcuV0R1e4l2qZ7zzK+cPYQHAzklf3pZ+K+gf4U56eMXY6DTJWJ9fscmL4dauhVsHIGWTZ52qNuPM4fOzvyfsxR3|00W2XVQO55MOLAVN18HB9L7BADXXGCP5
wir_mlakcr58or83ir7k@gmail.com|8hS/97tatupWgxesdnM6VpEltDjzeh8P5kFaar2D9xA+9gRIdPnKU8P1FtEwgtAcZ+T+I4ayPXjoQeTy+Gn1yq4VffrUMjrOeP+ibvlL9h+vgJUngLom2xoNt2chBZFPqfs34Fh1MChG8QngJ/S/DNVqjGuS/LiwyFn4Zxio5xWDqqymE5pcUbFSWQGl5WNV7CeIlVAKxN7RT3WPjuLRum1a9CEMdPs4hSZmV4hqElZH1r7MuJumeJ6nWhpFJyAR8r5J0M1YZE+WbceVPemQp2emsOYNZj8oevGOx6MU87amSYx107IlS6l/zs8QFUCp1ntyuoK/CSKH4NSA68wJ/tioFWFtYuRoDKML1KrzWKFujPDGQjGvNLZB3+MFduwBkhwLjcDzmuygAWeU8GPt/ThO0m7omssH0n7hEe+aCgnCRYzRsYXpKG+tZFkYXqcZ6Jmr7n/fD/fuhyc7QmZfq83wfTEKyCE1X4W8AzXKAfRqDpZFm+TOynNkDWCRrslY|9W3QB56X2P0YPNEVYABQ0RTGU9XBAEFU
wir_kdmdzaodzhyl1yc2@gmail.com|gkXf/ScUxrqjxncvljgLHTCuT9U014la+7g0c7g4jf23aRqdQjicalY1s9BwewGzdIAEZrv+RID+KS4jBEDI6qk2R5be+4bFr+Tpf49KbFwxFZLdnMsnhn9oJ7YftlPsi0uDWG9A4ApLaCZIMs2JoVVwYqPRKHIWnpTI+5wBfhFvdHuKUXwMt8PwEyPZGyrP36MJf9/5E+uQScYFWW5ydjZ7P3QtptAc/yEg3CG+fiUSMTtqdWw9y0/+XCX0nJGcaZmbBwTrrLknsJS6oJS2b1c3rEUe+ejX8KuSmIK4DBtgdKCF6r9KHAVk7uSvRwrySWsllP1aI81R0qxc44jn9Ftb2CmFkLHBr3FK2vSv39b/i32H3aKaRbggagLRJS6cBa83JlrouBZq7GNxDr+/PFbZkwybMWuByfjWuSD1nmL8SeIO4X1QyDeLmDxRqdZRCsm1J1wUA0NCeLcVR2UL+OdLiRAeHNg1jgD+iUHv/0BcNC0lYd8w8XXaoUzqOKvw|8RZ07E7JV6JDNHPOHP4JPDXLZMR4X9MM

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

