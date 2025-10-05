
STORAGE_MALADY = "xx"
DOOR_MALADY = STORAGE_MALADY


function checkMalady()
    local b = (getBot and getBot()) or nil
    if b and b.isInWorld and b:isInWorld() and (b.status == BotStatus.online or b.status == 1) then
        if b.say then b:say("/status") end
        sleep(700)

        if type(findStatus)=="function" and findStatus() and b.getConsole then
            local conso = b:getConsole()
            if conso and conso.contents then
                for _, con in pairs(conso.contents) do
                    if type(con)=="string" and con:lower():find("malady:") then
                        local name = con:match("[Mm]alady:%s*([^!]+)")
                        if name then name = name:gsub("%s+$","") end

                        local h = tonumber(con:match("(%d+)%s*hours?")) or 0
                        local m = tonumber(con:match("(%d+)%s*mins?"))  or 0
                        local s = tonumber(con:match("(%d+)%s*secs?"))  or 0
                        local total = h * 3600 + m * 60 + s

                        maladyName, maladyHours, maladyMins, maladySecs, totalSeconds =
                            name, h, m, s, total

                        print(("Malady: %s. Time Left: %d hours, %d mins, %d secs")
                            :format(name or "None", h, m, s))
                        return true, total, name
                    end
                end
            end
        end
    end
    return false, nil, nil
end

function ensureMalady(threshold_min, opts)
    opts = opts or {}
    local minutes     = tonumber(threshold_min or 5) or 5
    local THRESH_SECS = math.floor(minutes * 60)

        -- pastikan tidak di EXIT (dan refresh w setelah hop)
    if hop_until_leave_exit then pcall(hop_until_leave_exit, 10) end
    local b = (getBot and getBot()) or nil
    local w = b and b:getWorld() or nil
    local wname = (w and w.name) and tostring(w.name):upper() or ""
    if wname == "" or wname == "EXIT" then
        return false, "not_in_world"
    end

    if (not STORAGE_MALADY) or STORAGE_MALADY == "" then
        return false, "storage_not_set"
    end
    local useW, useD = STORAGE_MALADY, (DOOR_MALADY or "")
    local status_malady, total_secs, name_malady = checkMalady()         -- sumber /status
    local ttl_secs = tonumber(total_secs or 0) or 0


    if status_malady and ttl_secs > THRESH_SECS then
        print(("[MALADY] %s (%02dh %02dm %02ds) ~%ds > %d → skip.")
            :format(name_malady or "Unknown",
                    tonumber(maladyHours or 0),
                    tonumber(maladyMins  or 0),
                    tonumber(maladySecs  or 0),
                    ttl_secs, THRESH_SECS))
        return false, "malady_still_long"
    end

    -- helper format detik -> H:M:S
    local function fmt_hms(secs)
        secs = math.max(0, tonumber(secs or 0))
        local h = math.floor(secs / 3600)
        local m = math.floor((secs % 3600) / 60)
        local s = secs % 60
        return string.format("%02dh %02dm %02ds", h, m, s)
    end

    -- Asumsi: sudah ada status_malady (bool), ttl_secs (detik), THRESH_SECS (detik), minutes (ambang menit)
    -- ===== ensureMalady() (loop nunggu) =====
    if status_malady then
        if ttl_secs <= THRESH_SECS then
            print(("[MALADY] %s sisa %s (≤ %d menit) → nunggu selesai...")
            :format(name_malady or "Unknown", fmt_hms(ttl_secs), minutes))

            local recheck_every = 5
            local last_check = os.time()

            while ttl_secs > 0 do
            -- TIDUR 1s supaya countdown realtime + CPU aman
            sleep(1000)

            -- recheck tiap beberapa detik agar adaptif
            if os.time() - last_check >= recheck_every then
                last_check = os.time()
                local ok, new_secs, new_name = checkMalady()
                if ok then
                ttl_secs = tonumber(new_secs or 0) or 0
                name_malady = new_name or name_malady
                else
                -- fallback: kurangi sesuai interval recheck
                ttl_secs = math.max(0, ttl_secs - recheck_every)
                end
            else
                -- kurangi 1s untuk siklus ini
                ttl_secs = math.max(0, ttl_secs - 1)
            end
            end

            print("\n[MALADY] Selesai (0s). Lanjut.")
        else
            print(("[MALADY] %s sisa %s (> %d menit) → skip nunggu.")
            :format(name_malady or "Unknown", fmt_hms(ttl_secs), minutes))
            return false, "malady_too_long"
        end
    else
    print("[MALADY] Tidak terdeteksi malady → lanjut.")
    end

    if not status_malady then
        print("take malady ajoyed")
    end
end

ensureMalady(5)
