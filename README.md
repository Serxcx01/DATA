---- SC LOGIN JOEY STORE

local accounts = [[
siminhdojr@gmail.com|30:62:38:36:9f:2b:6e4660af445d35b99e3742fae7e85d14:B20A446812EDFAF7B89DAF6CFE7FE527://+QH0scKwucNsnlJgPkblZcCOhfYz6ciRUwc4IuQ9HdxTm+XKWpiamAoO04fVpLmcN4iIHgrrevxzwlSfihz38L5CmqIozzTTPmQBXVCAvTRS+1S7o6AEArPBQmgmKwtiJFeuIHzAshsd+aNMcxZqo80c43UJxGXh0/JvHoQpFfEN2shpaoOmvVFtezzGdyaNZddDeDe5duJkDxcQ5lrY024MPreYxcv9Dbc+p7K0VXymLt5U9PmbYFDi5IQZkaJapRmCWLqhE5fiZfveOl/qkkcOIgWp6mHFThZSp80JebGR/CkuiWCvNRdkth5kF9SY4Q6eSxhzHWumidkuzWvvHaIchMpRtQ+H99H5HltnnvN2yuHIO4rC9prHBGr25C+g0R0qNiZBEzp2YU5n150hmdmQDl9vMMiNraml5RJoKifwSBinj6zd0d43S/j98lM0wMM+AIX7AOZSDT1ibMeQ==
sheltonpilar5@gmail.com|5d:2e:49:67:8d:53:be2a402e170096df98ac19d9eb5ba2fd:1CBEAE10DE641FF5BAAEAFD0E1EAB3C6:4un4UAiUdFbbF5u1tiM+/COOAzyU551uFICSVYIjbS/YscyQlOS6o8+tyyQOZ6kmblfE3biXy4pCy2kVvIlW/LWj7ataHtXu6D08DW0t8lj7xWHtjS/dOU4UQHkd36AdxlV0MYDHrnyma9sC6YK4WyFgi1gTQb1hZTLPmK01TKRGvOTkAkXMCj4P/B8Igf2rD9IsnrY6anDmy0+t2s83WEOjcLKPzt7UVw5e4utLmcQqHtb0sD2b1OyihFIv1KWKZU1vuDgB82jh1fMwaiwAMa8VIQUciNWxoMPnc244K+IJlVXfVroJmE/b6zLsudre/YOKGtBeACcvF0dnb2jl5QZXSXl/j8Zm0JXbaBrUMynelhsclAwG/Fbv+P1ZB2nIk0owC00QJrUUpGlJUQ2CS3qeXiwkzatlQQV9NZqn07bEiXrmCvl1LQfcn8j+wyFom8LTZB8jHvHAhLmq7bftNA==
thicamchau8134@gmail.com|84:ef:34:9e:10:c1:b088c98941a4495364660470ec9d31fe:ADC3C8B9A0DFA580F762FF3AA3B67D99:dlUy33JKvsuFYV936hCS6ox8/YyftRPEhEm9mJgsyndvAqBagySP/BKAtJRpzVwH33JA/ib9k12F8H+oKm9Z6LMYqyyMSZ4HzHn1pIRvA1c3bylSQmm/vyWhlH0XwDYzodtcDK92AaYkO4jxb+6m3Sn2LBkfD2f96a9XRnLFn76tqKn8WXpjvpAKpM56/9asYJ2maG0EyDJ2nYNWfcd7d0GrUwN6UMFCsBvYy974vm/Xl/irCKBWKWp1F+mSojW/WpXEXwaIOoYeCVaBm35x8GXw08awzIptnQCPDugkj455jYPMq0et8md56TJ6NW/Bt1+sJqZYafNmiq+/nnA4oIGA5iFQqEgqHp/bB5FR5yQbX594sEuuOjNLs4QBgkX5SQyOhS8aycAjQCyUTuWQDDnitXB/U/EVEe7w51AJZztZICRuH6IIMLhf54sznoe1zFGb+8cmgyLBDqXzrxN1Cg==
thaihoangvan1198@gmail.com|21:1f:7e:f5:77:f4:4c9287c108c5008dbeb31a59f257cd2e:CBCECC43A8FA6B255D20B4AC85BDBFEA:dlUy33JKvsuFYV936hCS6qdmie2/iOnM69XfrKYIqQPCjxC8qs0EKpPxTXy1A77/UfJ6ycuRViRh7BzpucqjYfzYHW3ZPHYIA0FCD1QT1pPG3n0oKJjYK0r0G8w8KybsOLCYPF9z8VT+/Z4fP/uY+Dj7iMyLZjnEse6R/x4w6yWz8NPZ5UhFy92FRBjoCCiOuXbqorCY0oio1Gcd7hCFJ0QgSTUH0hM2AItDvmUTWAvJon8sEo7ti4hQANmeOnLdYZCon8aFxmrvlhcRoe5Aaf5bQfHExUQZ7MSQEf8YaD/KS67qcGBVvkldS1NRdXxQU0e5f6n6R3J2DI0mkCIQYput4+bqDd9jwk4uo3nM2QTXm3O1ycPa71EMt+iI7cwkfg3o8+EGFFTbL5rP5HDOlkMz8wk/0hCaYlBDmGR7Eh+jsbU8AM4s8XEaS77rFEg8tOAaPU/BDBl1pZji0dLx5g==
rm2808482@gmail.com|bb:c7:e8:5f:6b:12:94424e418b0fff4035fb4f4cc53540a3:A5ED643A8300645C1024FD6DBEF2FC8B:+xUX5CsomK2SdTFaRdt0sbkb9j8SIpwlK8GnzGHdVQM+AqvPywE8hSeTAp0h2JoXEKrA1actlOmYi95Ec4/0NChbPxe6Dn2VFo+hUMEIlyDZ0WhAxoQ7WFdGpiEwNDpUJtnU608drts+8nD8ACiR+/iwyq6usRZ2SCFWdlhq9r9yi/eAty8EFbKtLzby+Nu2pkDfD9AHQHwttmgOyPe16e6kUzHW63IasIS1wiS20sxwRQtva4+Pxi5pob2E7rpOrYHLYNkxe5w7BcQZH8MBpMJE8xfY5XxcoXLOGlRPdL0e9BwjVfmWPFuFo0YK2LfCxJPKZ54ERYdNzItfb0/JOSm+LLtf0lICatXWpBCuH9myc6OhuufG+/E/LKgFE5UBuuPhjqriVuKrFBqL336NqsBkzLafNY/gN43uPn9PpWtzHgMDPRF/YAxHwjbsXIFisPa+8HxYmA+iahN5MwCJjg==
tductri46@gmail.com|7c:87:8b:77:44:26:0376c1dd5c6530c18639da86216065e8:DE56909F7FDE03DABDE48CDD445CF8BD:dlUy33JKvsuFYV936hCS6jHcBOmgMXeK7/846tVbQ+UuI7z6hj8www8iL1AVBqtTofFovEe6//DlDUUqOxrtLT3jxaawokjt7lIv27Bl9jhzmFPR95rEl5hZoAVEBIgwo15WfMEIwhkGE+l1qSdhArBvji3T1u1mmdBKSJJmLHw1Pxz9swDGQqH6vYU3s0WMK8rrhUuOgaQC0pl0bInIRH5Rpm4PdpemweKUrMvgA6vmVFpFQM/pHPFSaNbD/I7hZkXZruZoyooEcTMDjOP2jegGwEmpcOwdaCE3aNBMLFwiISl0m9JjUZCOa4zjR2HtzZuHEyvWrGLymKQmR1ISH3vqaU+Lc8O53G97MjFka57Cgo0mZ6mn7b9w4kv/VVqWHikLO7sVI9U9VBGkR/k2CcxC98Dfl8blcAIszgKytOSpBvzvHn/5uV1AsRpges3ZvcUsnB/cbRebM8P1xmxHTA==
stuartnicolasa748@gmail.com|5c:60:74:b7:00:94:6f255ba32c236952eafc0861fbfbd3d0:3CF1AE2BFBCEDDA680C8BAF05FA7458F:tykd1xHa9Sr9lKPnhkX/vPEgHRxVUtW6C+zKUVXmjRJ30ba18HUDUliJ9icbSmesgSfunnq8nB/p5sKCgj7mftjenJBN2J288+IU/MlSI+QAx9sBxqv9iTnpmIXz15zA8GX7gbzEBpWCjrh0NCqvPRIHWhPiSokvTpERTZzJVzWQOIbPOgR/aMHwwafsf9Cus4sRtnU2P1BwMIzLFv/cw5mnMGGkOpTL/yVYL32Sxjg1+oJOKFxzVEr59AwPj0fShvry1J03Gln2RGO7DrXMpaM8bxNn+5dxGpjZbJgLo8OOPuKZjRyqkpd0jHfyt5e9tZoHzgV5Q0MiFY1KKwdYzZJFz9XiJHCL74DznZqjqABUsTX6REHjPJjAtHLrKVPRFsJnSaROFrbOYErYt3TzYsm0SiUQZ1dnvpoPLZQGUkAt7fTk1/oYyheOR3BJFEDjDr+EKc0aPXmwL3rzdSVa5A==
wk7863707@gmail.com|5f:da:a9:b5:c5:c5:0bd2853455d14b473ec6d4cb55e6852d:FFEDCDDF301171BA77DCED7FEFDE7691:+xUX5CsomK2SdTFaRdt0sSnBN21HsJeHuLwuaE1TlbQZiFI3jbUrPLwIHYMlNymvwHazuLyP3/3V+TsMGRQI0P5xpe/HiDzW1Tqgmy+HGH61KaBHj6VYHXji7H/Q0TDYbev8kj1Rbp2o2hlAMq6/2RgPKaHR8S7Trt1zqT4J8L/h9dhJPMtvLKzg8XhJkvmdutSwI+YuxpgJ8+/1QvoWBsWlOfOkJdxDr+aa3V0pmFJMzaPI+9QhDhD+1gDLGLAscocILTLaSJ2+J1gIxdrYwtZON5RR+I/gGvAl9R6TmhglbtSgI+5K1gcm4Sxtnc7+fp/yNKVIXxwWwKBSUNEZ8KSGE9ROlTfriqW/QATz8i/kVe7oiAoMjtk0E+CjeF/So+gu3CEGE8sl9zgHzfFTAnZ7LxVzNr4oN5g3AQUgkVVdAjw2RRAj1SUfCAQUr1TwqNiYiuXBnwx0DIj+jtYicw==


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
