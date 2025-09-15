---- SC AP
local bots = [[
2AB0B1EAC63570792BA54837C0D3B710|74EqR3NZgIq1kSH4YIan6aRaW2LFn5bJb0vdQplSljDiQacYWvq6K0i7ex1nlnC2QPdqQEuNOocondgrQKuhGFLXsCIiEV9Wwkl5CbD3YtMrJlGGRXgbIX6k5BBXlliWTF+EBY3Q/pBwGeV/hL1vE5ff+fhQyVwEYysp4EHHO1QmUsCeGvdIbr491IoIe8CacgujGD3Av9srINT6pwBSEY8HW4y6bDJXgVNbEvhd7sX84pr0Ie0TMaKviqMdvUOSzs72BE2WcZ4YsJsZnlGjK/oqcKziXGggCMryMv2ptIeWpsb4mVvLbdUIlRujQlXicSSFeXE/qSscXLYfEZwqwvqLLEvbw1yUFxEW+OcepaxEtQ6z0T6FkM/2D5QfTIuG2I39P/wli/RGhAdA/rnigDu+Uw6pGfyzeo4yhOc0ZK7q98aihRKrN+dNjXczgkuzW60KEqj43aUEQBbMUT7R+3OcYSUx5foqqcxNbXBjMHMgj9nNtFR5s9q4G7FRSooU
E26EA3D312D3A091BEEB09D7FEFACACB|74EqR3NZgIq1kSH4YIan6flqfVIprvgAQvi5mkZzqbDFLFWFDP0q5FwZK2QthQE3hkT4kKO6rIc6IIXK7+AHAdE2h/t+RJMPW1Q0ykizuz+VKoXF1vAgl9Wgw7On0WvjGOn5eNkP6Rw+Qj1YWBddTRNSN4yzwqhTl1DZ987phVnBZ9ix0MaGhBUCf5kPXH7/TFp8VETzrd8C3m+63mP39deIBFbh4V8Q8T7+W6Hgug80Jv7QcSDFo2rHjLJFg6ztWuDcesElWfntqetsIZTSPPerNhUdPutFfBhXx0TlCk/o1WJGopKQ+VFdRKbDfxohXQoMJzFDtiqDNMSFZE7VcFcVRv/qMfVQNU61p2hBApsM4xVKP+SImwbKFlvo6ZaS8aJXWuGVrlg/xlbKjzPuS3QBwyonVTe8KmPUJh4nzYVFJaZaPopMgGrwCWEsCN4/vsqMGvaP/LCFB2hGOwAw8DfgdDj1XFUZfj6lKhQ1jmxjRbNMLsTHS3QIXrOwEdDe

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
