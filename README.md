----------------------------------------------------------------
-- MULTI WORLD HARVEST + DROP SNAKE (ANTI-SKIP 2 TILE)
-- + TXT JOB QUEUE (worlds.txt / inprogress.txt / done.txt)
-- + WORK-STEALING ("stale" only) / ASSIST_MODE ("always" / "stale")
-- + SMART MULTI-BOT ASSIGNMENT (AUTO SLOT & AUTO TOTAL_BOTS) [opsional RR/CHUNK]
-- + WARP TAHAN BANTING (NUKED + PUBLIC + BAD_DOOR + SAFE TILE) + LOGGING
-- + GUARD: ANTI-STUCK respawn WHITE DOOR (fg==6)
-- + DROP SNAKE SMART (kanan→atas, fallback kiri, stance walkable, tepi kanan aman)
-- + TAKE_MAGNI: keep exactly 1; sisanya drop ke storage; no double-wear
----------------------------------------------------------------

-------------------- BASE PATH (Windows Desktop) --------------------
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/JOB-ANDRE/"):gsub("[/\\]?$", "/")

local function _ensure_dir(p)
  local is_windows = package.config:sub(1,1) == "\\"
  if is_windows then os.execute(('if not exist "%s" mkdir "%s"'):format(p, p))
  else os.execute(('mkdir -p "%s"'):format(p)) end
end
local function _pjoin(base, name) return (base or "") .. (name or "") end


_ensure_dir(extraFilePath)

-------------------- CONFIG --------------------
USE_TXT_QUEUE = true   -- pakai worlds.txt queue

-- >>> Assist mode <<<
ASSIST_MODE         = tostring(ASSIST_MODE or "always"):lower()  -- "stale" / "always"
ASSIST_HELPER_LIMIT = math.max(1, tonumber(ASSIST_HELPER_LIMIT or 1) or 1)  -- max helper per world (exclude owner)
STEAL_HELP          = (STEAL_HELP ~= false)  -- default true; set false untuk mematikan steal
STALE_SEC           = tonumber(STALE_SEC or 30*60) or (30*60)
LOOP_MODE           = false
DELAY_EXE           = 1000

-- Delay/harvest
USE_MAGNI     = false
DELAY_HARVEST = 170

-- Storage MAGNI (opsional)
STORAGE_MAGNI, DOOR_MAGNI = "", "" -- lokasi kacamata (10158)


-- Storage CAKE (final/idle drop tanpa ambang)
STORAGE_CAKE, DOOR_CAKE = "AFILPEPPER1", "XX1"
cakeList  = {1058,1094,1096,
1098,1100,1102,1104,1106,1108,1110,1112,1114,1116,
1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,
1138,1140,1142,1144,1146,1148,1150,1152,1154,1156,
1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,
1178,1180,1182,1184,1186,1188,1190,1192,1194,1196,
1198,1200,10158}

-- Ambang drop snake (by tile/stack) ---
local TILE_CAP, STACK_CAP = 3000, 20


-------------------- RNG (seed) --------------------
ROTATE_SEED  = ROTATE_SEED or 12345

-- File queue/log di Desktop
JOB_FILES = {
  worlds     = _pjoin(extraFilePath, "worlds.txt"),
  inprogress = _pjoin(extraFilePath, "inprogress.txt"),
  done       = _pjoin(extraFilePath, "done.txt"),
}
FAIL_LOG_FILE    = _pjoin(extraFilePath, "warp_fail.log")
SUCCESS_LOG_FILE = _pjoin(extraFilePath, "success.log")
local function _touch(path) local f=io.open(path, "a"); if f then f:close() end end
_touch(JOB_FILES.worlds); _touch(JOB_FILES.inprogress); _touch(JOB_FILES.done)

-- === WORLD LOCK (per-world) ===
local LOCKS_DIR = _pjoin(extraFilePath, "locks/")
_ensure_dir(LOCKS_DIR)

local function _lock_path(world) return LOCKS_DIR .. (world or ""):upper() .. ".lock" end
local function _is_windows() return package.config:sub(1,1) == "\\" end

local function _acquire_world_lock(world, timeout_ms)
  timeout_ms = timeout_ms or 1500
  local path = _lock_path(world)
  local deadline = os.time() + math.ceil(timeout_ms/1000)
  while os.time() < deadline do
    local cmd = _is_windows()
      and ('cmd /c mkdir "%s" 2>nul'):format(path)
      or  ('mkdir "%s" 2>/dev/null'):format(path)
    local ok = os.execute(cmd)
    if ok then return path end
    if sleep then sleep(30) end
  end
  return nil
end

local function _release_world_lock(lock_path)
  if not lock_path then return end
  local cmd = _is_windows()
    and ('cmd /c rmdir "%s" 2>nul'):format(lock_path)
    or  ('rmdir "%s" 2>/dev/null'):format(lock_path)
  os.execute(cmd)
end

-------------------- UTIL TXT --------------------
local function _read_lines(path)
  local t, f = {}, io.open(path, "r")
  if f then for ln in f:lines() do table.insert(t, ln) end f:close() end
  return t
end
local function _write_lines(path, rows)
  local f = io.open(path, "w")
  if not f then return end
  for _,ln in ipairs(rows or {}) do f:write(ln, "\n") end
  f:close()
end
local function _now() return os.time() end

local function _append_done(world) local f=io.open(JOB_FILES.done,"a"); if f then f:write((world or "").."\n"); f:close() end end

local function _world_has_job(world)
  world=(world or ""):upper()
  for _,ln in ipairs(_read_lines(JOB_FILES.worlds)) do
    local w=ln:match("^([^|]+)")
    if w and (w:upper()==world) then return true end
  end
  return false
end

local function _update_heartbeat(world, who)
  world=(world or ""):upper(); who=who or WORKER_ID
  local rows = _read_lines(JOB_FILES.inprogress)
  local out  = {}
  local replaced = false
  local now = _now()
  for _,ln in ipairs(rows) do
    local w, wh, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and wh and ts and w:upper()==world and wh==who then
      table.insert(out, string.format("%s|%s|%d", world, who, now))
      replaced = true
    else
      table.insert(out, ln)
    end
  end
  if not replaced then table.insert(out, string.format("%s|%s|%d", world, who, now)) end
  _write_lines(JOB_FILES.inprogress, out)
end

local function _cleanup_stale_inprogress(world)
  world=(world or ""):upper()
  local rows = _read_lines(JOB_FILES.inprogress)
  local out  = {}
  for _, ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if w and w:upper()~=world then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress, out)
end

local function _uncommit_self(world)
  world = (world or ""):upper()
  local rows = _read_lines(JOB_FILES.inprogress)
  local out  = {}
  for _, ln in ipairs(rows) do
    local w, who = ln:match("^([^|]+)|([^|]+)|")
    if not (w and who and w:upper()==world and who==WORKER_ID) then
      table.insert(out, ln)
    end
  end
  _write_lines(JOB_FILES.inprogress, out)
end

-- === count unique workers (owner + helpers) ===
local function _count_unique_workers(world)
  world = (world or ""):upper()
  if world == "" then return 0 end
  local rows = _read_lines(JOB_FILES.inprogress)
  local S = {}
  for _, ln in ipairs(rows) do
    local w, who = ln:match("^([^|]+)|([^|]+)|")
    if w and who and (w:upper() == world) then S[who] = true end
  end
  local n = 0; for _ in pairs(S) do n = n + 1 end
  return n
end

-- === commit helper dengan world-lock + rollback ===
local function _try_commit_helper(world)
  world = (world or ""):upper()
  if world == "" then return false end

  local lk = _acquire_world_lock(world, 1500)
  if not lk then return false end
  local ok = false

  -- optional: bersihkan sisa baris lama milik kita (anti-duplikat)
  do
    local rows, out = _read_lines(JOB_FILES.inprogress), {}
    for _, ln in ipairs(rows) do
      local w, who = ln:match("^([^|]+)|([^|]+)|")
      if not (w and who and w:upper()==world and who==WORKER_ID) then
        table.insert(out, ln)
      end
    end
    if #out ~= #rows then _write_lines(JOB_FILES.inprogress, out) end
  end

  -- 1) append claim helper
  local fh = io.open(JOB_FILES.inprogress, "a")
  if not fh then
    _release_world_lock(lk)
    return false
  end
  fh:write(string.format("%s|%s|%d\n", world, WORKER_ID, _now()))
  fh:close()

  if sleep and math and math.random then sleep(math.random(40,80)) end

  -- 2) re-check setelah append
  local total = _count_unique_workers(world)   -- owner + helpers
  local helpers_now = math.max(0, total - 1)   -- exclude owner
  if helpers_now > (ASSIST_HELPER_LIMIT or 1) then
    -- 3) rollback: hapus baris kita
    local rows, out = _read_lines(JOB_FILES.inprogress), {}
    for _, ln in ipairs(rows) do
      local w, who = ln:match("^([^|]+)|([^|]+)|")
      if not (w and who and w:upper()==world and who==WORKER_ID) then
        table.insert(out, ln)
      end
    end
    _write_lines(JOB_FILES.inprogress, out)
    ok = false
  else
    ok = true
  end

  _release_world_lock(lk)
  return ok
end

-------------------- QUEUE HELPERS (sebagian fungsi lain milikmu tetap) --------------------
-- (Di bawah ini diasumsikan semua fungsi lain (HARVEST_UNTIL_EMPTY, MARK_DONE, RECONCILE_QUEUE, dll.)
-- sudah ada di file asli dan tidak diubah.)

local function SPEC_FOR_WORLD(W)
  local worlds=_read_lines(JOB_FILES.worlds)
  for _,ln in ipairs(worlds) do local w,d,bid,sw,sd=_parse_world_line(ln); if w and w==(W or ""):upper() then return w,d,bid,sw,sd end end
  return nil
end

local function FIND_OWN_INPROGRESS()
  local rows=_read_lines(JOB_FILES.inprogress); local bestW,bestTS=nil,-1
  for _,ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who==WORKER_ID then local t=tonumber(ts) or 0; if t>bestTS then bestTS,bestW=t,(w or ""):upper() end end
  end
  return bestW
end

local function UNCLAIM(world)
  world=(world or ""):upper(); if world=="" then return end
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w,who=ln:match("^([^|]+)|([^|]+)|"); if not (w and who and w:upper()==world and who==WORKER_ID) then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress,out)
end

local function CLAIM_NEXT_JOB()
  local rows=_read_lines(JOB_FILES.worlds)
  for _,ln in ipairs(rows) do
    local W,D,BID,SW,SD=_parse_world_line(ln)
    if W then
      local now=_now(); _update_heartbeat(W, WORKER_ID)
      return ln
    end
  end
  return nil
end

local function QUEUE_STATS()
  local w=_read_lines(JOB_FILES.worlds)
  local p=_read_lines(JOB_FILES.inprogress)
  local d=_read_lines(JOB_FILES.done)
  local setW, setP, setD = {}, {}, {}
  for _,ln in ipairs(w) do local ww=ln:match("^([^|]+)"); if ww then setW[(ww or ""):upper()] = true end end
  for _,ln in ipairs(p) do local ww=ln:match("^([^|]+)"); if ww then setP[(ww or ""):upper()] = true end end
  for _,ln in ipairs(d) do local ww=ln:match("^([^|]+)"); if ww then setD[(ww or ""):upper()] = true end end
  local total, inprog, done = 0,0,0
  for _ in pairs(setW) do total=total+1 end
  for _ in pairs(setP) do inprog=inprog+1 end
  for _ in pairs(setD) do done=done+1 end
  local unclaimed = math.max(0, total - inprog - done)
  return {total=total, inprogress=inprog, done=done, unclaimed=unclaimed}
end

local function _parse_world_line(ln)
  if not ln then return nil end
  local w,d,bid,sw,sd = ln:match("^([^|]+)|([^|]*)|BID=(%d+)|([^|]*)|([^|]*)$")
  if not w then w = ln:match("^([^|]+)") end
  return (w or ""):upper(), d, tonumber(bid or 0), sw, sd
end

local function MARK_DONE(world)
  world=(world or ""):upper(); if world=="" then return end
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if not (w and w:upper()==world) then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress,out); _append_done(world)
end

local function PICK_ASSIST_WORLD(mode)
  local prog = _read_lines(JOB_FILES.inprogress)
  if #prog == 0 then return nil, false end

  -- kandidat milik orang lain yang paling lama (umur heartbeat tertua)
  local best, best_age, best_owner = nil, -1, nil
  local now = _now()

  for _, ln in ipairs(prog) do
    local ww, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if ww and who and ts and who ~= WORKER_ID then
      local age = now - tonumber(ts)
      if age > best_age then
        best, best_age, best_owner = (ww or ""):upper(), age, who
      end
    end
  end
  if not best then return nil, false end

  -- jika world sudah tidak ada di worlds.txt → bersihkan & skip
  if not _world_has_job(best) then
    _cleanup_stale_inprogress(best)
    return nil, false
  end

  -- hormati limit helper (owner + helpers, exclude owner)
  local total_workers = _count_unique_workers(best)         -- owner + helpers
  local helpers_now   = math.max(0, total_workers - 1)      -- exclude owner
  if helpers_now >= (ASSIST_HELPER_LIMIT or 1) then
    -- slot helper penuh → skip
    return nil, false
  end

  -- mode "stale": hanya eligible kalau sudah melewati STALE_SEC & STEAL_HELP aktif
  if tostring(mode or ""):lower() == "stale" then
    if best_age >= (STALE_SEC or 1800) and (STEAL_HELP ~= false) then
      return best, true  -- sinyal: boleh steal
    else
      return nil, false
    end
  end

  -- mode "always": bantu tanpa steal (owner tetap)
  return best, false
end


function RUN_FROM_TXT_QUEUE()
  -- helper kecil: commit dengan anti-race kalau tersedia
  local function _commit_ok(world)
    if type(_try_commit_helper) == "function" then
      return _try_commit_helper(world)
    else
      -- fallback: setidaknya heartbeat dulu
      _update_heartbeat(world, WORKER_ID)
      return true
    end
  end

  -- Auto-resume by SLOT
  local resumeW = FIND_OWN_INPROGRESS()
  if resumeW then
    local W, D, BID, SW, SD = SPEC_FOR_WORLD(resumeW)
    if W and BID then
      ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
      print(string.format("[RESUME] %s lanjut %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
      local hb = function(world) _update_heartbeat(world, WORKER_ID) end
      _update_heartbeat(W, WORKER_ID)
      HARVEST_UNTIL_EMPTY(W, D, SW, SD, { ITEM_BLOCK_ID, ITEM_SEED_ID }, hb)
      MARK_DONE(W); RECONCILE_QUEUE()
      print(string.format("[RESUME] %s selesai %s", WORKER_ID, W))
    else
      print(string.format("[RESUME] Spec %s tidak ditemukan; unclaim.", tostring(resumeW)))
      UNCLAIM(resumeW)
    end
  end

  while true do
    -- Klaim baru
    local job = CLAIM_NEXT_JOB()
    if job then
      local W, D, BID, SW, SD = _parse_world_line(job)
      if W and BID then
        ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
        print(string.format("[JOB] %s klaim %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
        local hb = function(world) _update_heartbeat(world, WORKER_ID) end
        _update_heartbeat(W, WORKER_ID)
        HARVEST_UNTIL_EMPTY(W, D, SW, SD, { ITEM_BLOCK_ID, ITEM_SEED_ID }, hb)
        MARK_DONE(W); RECONCILE_QUEUE()
        print(string.format("[JOB] %s selesai %s", WORKER_ID, W))
      end

    else
      -- Tidak ada yang bisa diklaim
      local qs = QUEUE_STATS()

      -- Gating: kalau "stale", TUNGGU sampai unclaimed==0; kalau "always", langsung boleh assist
      if ASSIST_MODE ~= "always" and qs.unclaimed > 0 then
        print(string.format("[QUEUE] Masih ada %d world belum diklaim. Menunggu...", qs.unclaimed))
        sleep(800)
      else
        -- 1x panggil, jangan duplikat
        local assistW, stolen = PICK_ASSIST_WORLD(ASSIST_MODE)

        -- Guard: skip kalau world sudah tidak punya job
        if assistW and not _world_has_job(assistW) then
          _cleanup_stale_inprogress(assistW)
          assistW = nil
        end

        if assistW then
          -- Steal flow: kosongkan dulu semua inprogress world tsb
          if stolen then
            _cleanup_stale_inprogress(assistW)
          end

          -- Commit helper anti-race (append → recheck → rollback jika penuh)
          if not _commit_ok(assistW) then
            -- slot helper penuh saat commit → cari kandidat lagi
            assistW = nil
          end
        end

        if assistW then
          print(string.format("[HELP] %s bantu %s (mode=%s%s)",
            WORKER_ID, assistW, ASSIST_MODE, stolen and " +steal" or ""))

          -- Cari spesifikasi world dari worlds.txt
          local worlds = _read_lines(JOB_FILES.worlds)
          for _, ln in ipairs(worlds) do
            local W, D, BID, SW, SD = _parse_world_line(ln)
            if W == assistW then
              ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID + 1
              local hb = function(world) _update_heartbeat(world, WORKER_ID) end
              _update_heartbeat(W, WORKER_ID)

              HARVEST_UNTIL_EMPTY(W, D, SW, SD, { ITEM_BLOCK_ID, ITEM_SEED_ID }, hb)

              -- MARK_DONE hanya jika kita owner (steal pada mode "stale")
              local rows = _read_lines(JOB_FILES.inprogress)
              local owner_now = nil
              for _, ll in ipairs(rows) do
                local ww, who = ll:match("^([^|]+)|([^|]+)|")
                if ww and ww:upper() == W then owner_now = who; break end
              end
              if owner_now == WORKER_ID then
                MARK_DONE(W); RECONCILE_QUEUE()
                print(string.format("[HELP] %s menutup %s", WORKER_ID, W))
              end
              break
            end
          end

        else
          -- Tidak ada aktif sama sekali
          local qs2 = QUEUE_STATS()
          if LOOP_MODE then
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job aktif (total=%d, inprog=%d, done=%d). Menunggu...",
              qs2.total, qs2.inprogress, qs2.done))

            -- idle actions opsional
            if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
              pcall(function()
                DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, { tile_cap = 3000, stack_cap = 20 })
              end)
            end

            local b = getBot and getBot() or nil
            if b and b.leaveWorld then b:leaveWorld() end
            sleep(1000)
            if b then b.auto_reconnect = true end

            -- stagger ringan
            sleep(DELAY_EXE * (index or 1))

          else
            RECONCILE_QUEUE()
            print(string.format("[QUEUE] Tidak ada job aktif (total=%d, inprog=%d, done=%d). LOOP_MODE=false -> exit.",
              qs2.total, qs2.inprogress, qs2.done))
            break
          end
        end
      end
    end

    sleep(350)
  end
  -- Final cleanup
  if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
    pcall(function()
      DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList,
        {tile_cap=3000, stack_cap=20})
    end)
  end
  local b=getBot and getBot() or nil
  if b and b.leaveWorld then b:leaveWorld() end
  sleep(900)
  if b then b.auto_reconnect = true end
end


-------------------- MAIN --------------------
sleep( DELAY_EXE * ( index - ( 1 - 1 ) ) )
do
  ASSIGN_MODE=(ASSIGN_MODE or "rr"):lower():gsub("%s+",""); if ASSIGN_MODE~="rr" and ASSIGN_MODE~="chunk" then ASSIGN_MODE="rr" end
  print(string.format("[CONFIG] SLOT=%d | WORKER_ID=%s | USE_TXT_QUEUE=%s | ASSIST_MODE=%s | ASSIGN_MODE=%s | ASSIST_HELPER_LIMIT=%d",
    MY_SLOT, WORKER_ID, tostring(USE_TXT_QUEUE), ASSIST_MODE, ASSIGN_MODE, ASSIST_HELPER_LIMIT))

  if USE_TXT_QUEUE then
    RUN_FROM_TXT_QUEUE()
  else
    local myList=build_worlds_for_bot(LIST_WORLD, MY_SLOT, TOTAL_BOTS, FARM_PER_BOT, ASSIGN_MODE)
    print(string.format("[CHECK] I am slot %d of %d (mode=%s)", MY_SLOT, TOTAL_BOTS, ASSIGN_MODE))
    if #myList==0 then print(string.format("[ASSIGN] Slot %d tidak kebagian world.",MY_SLOT)); return end
    print("[WARP] PUBLIC")
    warp_safely("PUBLIC","",true)
    for _,ln in ipairs(myList) do
      local W,D,BID,SW,SD=_parse_world_line(ln)
      if W and BID then
        ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
        local hb=function(world) _update_heartbeat(world, WORKER_ID) end
        print(string.format("[RUN] %s -> %s|%s (BID=%d)",WORKER_ID,W,(D or ""),BID))
        _update_heartbeat(W, WORKER_ID)
        HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID},hb)
        MARK_DONE(W)
        RECONCILE_QUEUE()
      end
      sleep(350)
    end
  end
end
