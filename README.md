----------------------------------------------------------------
-- MULTI WORLD HARVEST + DROP SNAKE + TXT QUEUE (WORK-STEALING)
-- - Worker ID berbasis SLOT (tahan ganti akun saat ban)
-- - Reclaim/Takeover job stale (owner ke-ban/berhenti)
-- - ASSIST_MODE="always": bantu semua job in-progress saat
--   unclaimed = 0 (owner langsung direassign ke kita)
-- - Warp tahan banting + smart drop
----------------------------------------------------------------

-------------------- PATH KE FOLDER QUEUE ----------------------
-- ganti sesuai lokasi folder job kamu
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/JOB-ANDRE/"):gsub("[/\\]?$", "/")

local function _ensure_dir(p)
  local is_windows = package.config:sub(1,1) == "\\"
  if is_windows then os.execute(('if not exist "%s" mkdir "%s"'):format(p,p))
  else os.execute(('mkdir -p "%s"'):format(p)) end
end
local function _pjoin(base,name) return (base or "") .. (name or "") end
_ensure_dir(extraFilePath)

-------------------- KONFIG UTAMA ------------------------------
USE_TXT_QUEUE = true
ASSIST_MODE   = ASSIST_MODE or "always"   -- "stale" | "always"
STEAL_HELP    = true
STALE_SEC     = 30*60                     -- 30 menit
SMART_DELAY   = false

-- storage drop “cake” (opsional). kosongkan jika tak dipakai
STORAGE_CAKE, DOOR_CAKE = "HVKKLL", "XX1"
cakeList = {1058,1094,1096,1098,1828,3870,7058,10134,10136,10138,10140,10142,10146,10150,10164,10228,11286}

-- storage magni (opsional)
USE_MAGNI = true
STORAGE_MAGNI, DOOR_MAGNI = "HVKKLL", "XX2"        -- world | door kacamata 10158

-- file queue/log
JOB_FILES = {
  worlds     = _pjoin(extraFilePath,"worlds.txt"),
  inprogress = _pjoin(extraFilePath,"inprogress.txt"),
  done       = _pjoin(extraFilePath,"done.txt"),
}
FAIL_LOG_FILE    = _pjoin(extraFilePath,"warp_fail.log")
SUCCESS_LOG_FILE = _pjoin(extraFilePath,"warp_success.log")
local function _touch(p) local f=io.open(p,"a"); if f then f:close() end end
_touch(JOB_FILES.worlds); _touch(JOB_FILES.inprogress); _touch(JOB_FILES.done)

-------------------- HELPERS: BOT/STATUS/DELAY -----------------
function STATUS_BOT_NEW()
  local b = getBot and getBot() or nil
  local s = b and b.status or nil
  local Status = "Unknown"
  if     (s==BotStatus.online)  or (s==1) then Status="online"
  elseif (s==BotStatus.offline) or (s==0) then Status="offline"
  elseif s==BotStatus.wrong_password              then Status="Wrong Password"
  elseif s==BotStatus.account_banned              then Status="Banned"
  elseif s==BotStatus.location_banned             then Status="Location Banned"
  elseif s==BotStatus.version_update              then Status="Version Update"
  elseif s==BotStatus.advanced_account_protection then Status="Advanced Account Protection"
  elseif s==BotStatus.server_overload             then Status="Server Overload"
  elseif s==BotStatus.too_many_login              then Status="Too Many Login"
  elseif s==BotStatus.maintenance                 then Status="Maintenance"
  elseif s==BotStatus.http_block                  then Status="Http Block"
  elseif s==BotStatus.captcha_requested           then Status="Captcha Requested"
  elseif s==BotStatus.error_connecting            then Status="Error Connecting"
  elseif s==BotStatus.high_ping                   then Status="High Ping"
  elseif s==BotStatus.logon_fail                  then Status="Logon Fail"
  else Status=tostring(s or "nil") end

  local world_name = ""
  if b and b.getWorld then local w=b:getWorld(); if w and w.name then world_name=(w.name or ""):upper() end end
  local inv = (b and b.getInventory and b:getInventory()) or nil
  return {world=world_name,name=(b and b.name) or "",level=(b and b.level) or 0,
          status=Status,gems=(b and b.gem_count) or 0,slots=(inv and inv.slotcount) or 0}
end

function UPDATE_DELAY_BY_PING()
  if not SMART_DELAY then return end
  local b = getBot and getBot() or nil
  local P = (b and b.getPing and b:getPing()) or 0; if P==0 then P=200 end
  if P<=150 then return end
  DELAY_RECONNECT = math.max(20000, P*200)
  DELAY_BAD_SERVER= math.max(120000,P*600)
  DELAY_PNB       = P
  DELAY_PLACE     = math.floor(P*0.7)
  DELAY_WARP      = math.max(5000, P*30)
  DELAY_TRASH     = math.max(100, math.floor(P*0.5))
end

DELAY_RECONNECT,DELAY_BAD_SERVER,DELAY_PNB,DELAY_PLACE,DELAY_WARP,DELAY_TRASH =
  20000, 120000, 175, 115, 7000, 100
DELAY_HARVEST = 170

-------------------- WORLD/BOT SMALL UTILS ---------------------
local function _my_xy()
  local b=getBot and getBot() or nil
  local w=b and b.getWorld and b:getWorld() or nil
  local me=w and w.getLocal and w:getLocal() or nil
  if not me then return 0,0 end
  return math.floor(me.posx/32), math.floor(me.posy/32)
end
local function _world_size()
  local b=getBot and getBot() or nil
  local w=b and b.getWorld and b:getWorld() or nil
  local wx = (w and w.width  and (w.width-1)) or 99
  local wy = (w and w.height and (w.height-1)) or 23
  return wx, wy
end

-------------------- QUEUE FILE UTILS -------------------------
local function _read_lines(path)
  local t, f = {}, io.open(path,"r"); if not f then return t end
  for line in f:lines() do
    line=line:gsub("\r",""):gsub("\n","")
    if line~="" and not line:match("^%s*;") then table.insert(t,line) end
  end
  f:close(); return t
end
local function _write_lines(path,lines)
  local f=io.open(path,"w"); if not f then return false end
  for _,ln in ipairs(lines or {}) do f:write(ln.."\n") end
  f:close(); return true
end
local function _append_line(path,line)
  local f=io.open(path,"a"); if not f then return false end
  f:write(line.."\n"); f:close(); return true
end

-------------------- WORKER ID BERBASIS SLOT -------------------
local function WORKER_ID()
  local b=getBot and getBot() or nil
  if b and b.slot then return "SLOT-"..tostring(b.slot) end
  local num = b and b.name and tonumber((b.name or ""):match("(%d+)$") or "")
  return "SLOT-"..tostring(num or 1)
end

-------------------- QUEUE PARSER & STATS ----------------------
local function _parse_world_line(s)
  local farmW,farmD,bid,storeW,storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW then return nil end
  return farmW:upper(), (farmD or ""), tonumber(bid),(storeW or ""):upper(),(storeD or "")
end
local function _set_of_worlds(lines)
  local S={}; for _,ln in ipairs(lines) do local w=ln:match("^([^|]+)"); if w then S[w:upper()]=true end end; return S
end
local function QUEUE_STATS()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog  =_read_lines(JOB_FILES.inprogress)
  local done  =_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog),_set_of_worlds(done)
  local total,unclaimed,inprog,ndone=0,0,0,0
  for _,ln in ipairs(worlds) do
    local W=(ln:match("^([^|]+)") or ""):upper()
    if W~="" then
      total=total+1
      local isp=S_prog[W] and true or false
      local isd=S_done[W] and true or false
      if (not isp) and (not isd) then unclaimed=unclaimed+1 end
      if isp then inprog=inprog+1 end
      if isd then ndone=ndone+1 end
    end
  end
  return {total=total, unclaimed=unclaimed, inprogress=inprog, done=ndone}
end

-------------------- CLAIM / DONE / HEARTBEAT ------------------
local function _now() return os.time() end
local function _norm_ts(ts) local n=tonumber(ts) or 0; if n>1e12 then n=math.floor(n/1000) end; return n end

local function _update_heartbeat(world, who)
  world=(world or ""):upper(); who=who or WORKER_ID()
  local now=_now()
  local rows=_read_lines(JOB_FILES.inprogress)
  local out, touched={}, false
  for _, ln in ipairs(rows) do
    local w, worker, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and worker and ts then
      if w:upper()==world and worker==who then
        table.insert(out, string.format("%s|%s|%d", w, worker, now)); touched=true
      else table.insert(out, ln) end
    end
  end
  if not touched then table.insert(out, string.format("%s|%s|%d", world, who, now)) end
  _write_lines(JOB_FILES.inprogress, out)
end

local function CLAIM_NEXT_JOB()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog  =_read_lines(JOB_FILES.inprogress)
  local done  =_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog),_set_of_worlds(done)
  for _, ln in ipairs(worlds) do
    local W=ln:match("^([^|]+)"); if W then
      if (not S_prog[W:upper()]) and (not S_done[W:upper()]) then
        _append_line(JOB_FILES.inprogress, string.format("%s|%s|%d", W:upper(), WORKER_ID(), _now()))
        return ln
      end
    end
  end
  return nil
end

local function MARK_DONE(world)
  world=(world or ""):upper()
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _, ln in ipairs(rows) do
    local w=ln:match("^([^|]+)")
    if w and w:upper()~=world then table.insert(out, ln) end
  end
  _write_lines(JOB_FILES.inprogress, out)
  _append_line(JOB_FILES.done, string.format("%s|%s|%d", world, WORKER_ID(), _now()))
end

local function SPEC_FOR_WORLD(W)
  local worlds=_read_lines(JOB_FILES.worlds)
  for _, ln in ipairs(worlds) do
    local w,d,bid,sw,sd=_parse_world_line(ln)
    if w and w==(W or ""):upper() then return w,d,bid,sw,sd end
  end
  return nil
end

local function FIND_OWN_INPROGRESS()
  local rows=_read_lines(JOB_FILES.inprogress)
  local bestW,bestTS=nil,-1
  for _, ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who==WORKER_ID() then
      local t=_norm_ts(ts); if t>bestTS then bestTS, bestW=t,(w or ""):upper() end
    end
  end
  return bestW
end

-------------------- RECLAIM STALE (takeover cepat) -----------
local function RECLAIM_STALE_JOBS(mode)
  mode = mode or "takeover"
  local now=os.time()
  local rows=_read_lines(JOB_FILES.inprogress)
  local out, changed = {}, false
  for _, ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts then
      local age = now - _norm_ts(ts)
      if age >= (STALE_SEC or 1800) then
        if mode=="takeover" then
          table.insert(out, string.format("%s|%s|%d",(w or ""):upper(), WORKER_ID(), now))
        else
          -- "unclaim": drop baris ini
        end
        changed=true
      else
        table.insert(out, ln)
      end
    end
  end
  if changed then _write_lines(JOB_FILES.inprogress, out) end
  return changed
end

-------------------- PICK ASSIST (stale/always) ----------------
local function PICK_ASSIST_WORLD(allow_nonstale)
  local prog=_read_lines(JOB_FILES.inprogress)
  if #prog==0 then return nil end
  local best,best_age,now=nil,-1,os.time()
  for _, ln in ipairs(prog) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who~=WORKER_ID() then
      local age = now - _norm_ts(ts)
      if allow_nonstale then
        if age>best_age then best,best_age=(w or ""):upper(), age end
      else
        if age>=(STALE_SEC or 1800) and age>best_age then best,best_age=(w or ""):upper(), age end
      end
    end
  end
  if not best then return nil end
  -- reassign owner ke kita
  local rows=_read_lines(JOB_FILES.inprogress)
  local out={}
  for _, ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and (w or ""):upper()==best then
      table.insert(out, string.format("%s|%s|%d", (w or ""):upper(), WORKER_ID(), now))
    else table.insert(out, ln) end
  end
  _write_lines(JOB_FILES.inprogress, out)
  return best
end

-------------------- WARP / GUARD (ringkas) --------------------
local function _current_world_upper()
  local b=getBot and getBot() or nil
  local w=b and b.world or ""
  if (not w or w=="") and b and b.getWorld then local ww=b:getWorld(); if ww and ww.name then w=ww.name end end
  return (w or ""):upper()
end

local function _current_tile_fg()
  local b=getBot and getBot() or nil; if not(b and b.getWorld) then return -1 end
  local w=b:getWorld(); local me=w and w:getLocal() or nil; if not me then return -1 end
  local tx,ty=math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
  local t=w:getTile(tx,ty); return t and t.fg or -1
end

local function _current_tile_fg_safe(polls,wait_ms)
  polls=polls or 12; wait_ms=wait_ms or 120
  for _=1,polls do local fg=_current_tile_fg(); if fg and fg>=0 then return fg end; sleep(wait_ms) end
  return -1
end

MAX_WARP_RETRY, MAX_DOOR_RETRY, MAX_RECOLL_CYCLES = 10, 5, 2
function WARP_WORLD(WORLD, DOOR)
  WORLD=(WORLD or ""):upper(); if WORLD=="" then return false end
  local tryDoor=(DOOR or "")~=""
  local function _warp_once()
    local b=getBot and getBot() or nil
    if not b or not b.warp then return false end
    if tryDoor then b:warp(WORLD.."|"..DOOR) else b:warp(WORLD) end
    sleep(DELAY_WARP); return _current_world_upper()==WORLD
  end
  if _current_world_upper()==WORLD then
    local fg=_current_tile_fg_safe(5,80); if (not tryDoor) or (fg~=6) then return true end
  end
  local ok=false
  for _=1,MAX_WARP_RETRY do if _warp_once() then ok=true; break end end
  if not ok then return false end
  if tryDoor then
    local fg=_current_tile_fg_safe(12,120)
    if fg==6 then
      for _=1,MAX_DOOR_RETRY do if _warp_once() then fg=_current_tile_fg_safe(6,100); if fg~=6 then break end end end
      if fg==6 then return false end
    end
  end
  return true
end

-------------------- DROP SNAKE (smart) -----------------------
local _OBJ_CACHE={grid={},last_refresh=0}
local function _grid_key(x,y) return tostring(x).."|"..tostring(y) end
local function _rebuild_obj_grid()
  _OBJ_CACHE.grid={}
  local b=getBot and getBot() or nil; if not (b and b.getWorld) then return end
  local w=b:getWorld(); local objs=(w.getObjects and w:getObjects()) or {}
  for _,o in pairs(objs) do
    local ox,oy=math.floor((o.x+16)/32), math.floor(o.y/32)
    local k=_grid_key(ox,oy); local g=_OBJ_CACHE.grid[k]
    if not g then g={total=0,stacks=0}; _OBJ_CACHE.grid[k]=g end
    g.total=g.total+(o.count or 0); g.stacks=g.stacks+1
  end
  _OBJ_CACHE.last_refresh=os.time()
end
local function _maybe_refresh_obj_grid() if (os.time()-(_OBJ_CACHE.last_refresh or 0))>=3 then _rebuild_obj_grid() end end
local function _countOnTile(tx,ty) _maybe_refresh_obj_grid(); local g=_OBJ_CACHE.grid[_grid_key(tx,ty)]; if g then return g.total,g.stacks end; return 0,0 end
local FULL_CACHE,BAD_CACHE={},{}
local function _key(x,y) return x..":"..y end
local function mark_full(x,y) FULL_CACHE[_key(x,y)]=true end
local function mark_bad (x,y) BAD_CACHE [_key(x,y)]=true end
local function is_full_or_bad(x,y) return FULL_CACHE[_key(x,y)] or BAD_CACHE[_key(x,y)] end
local function reset_caches() FULL_CACHE={}; BAD_CACHE={} end

local function _walkable(tx,ty)
  local b=getBot and getBot() or nil; if not b or not b.getWorld then return false end
  local w=b:getWorld()
  if tx<0 or ty<0 then return false end
  local wx,wy=_world_size()
  if tx>wx or ty>wy then return false end
  local t=w:getTile(tx,ty)
  if not t then return false end
  return (t.fg==0) and (t.bg==0 or true) -- fg 0 = kosong
end

local function _nextDropTileSnake(startX,startY,cursor,max_cols,max_rows,world_width,tile_cap,stack_cap)
  local MAX_STACK=tile_cap or 3000
  local MAX_SLOTS=stack_cap or 20
  max_cols=max_cols or 40
  max_rows=max_rows or 8
  world_width=world_width or 199

  local cx,cy=cursor.x,cursor.y
  local tried_rows=0
  local start_col=startX+1

  while tried_rows<max_rows do
    if cx<0 then cx=0 end
    if cx>world_width then cx=world_width end

    if (not is_full_or_bad(cx,cy)) and _walkable(cx-1,cy) then
      local total,stacks=_countOnTile(cx,cy)
      if (total<MAX_STACK) and (stacks<MAX_SLOTS) then
        cursor.x,cursor.y=cx,cy
        return cx,cy,cursor
      else mark_full(cx,cy) end
    else
      if not _walkable(cx-1,cy) then mark_bad(cx,cy) end
    end

    cx=cx+1
    if cx>=startX+1+max_cols then
      tried_rows=tried_rows+1
      cy=cy-1
      cx=start_col
    end
  end
  return nil,nil,cursor
end

local function _gotoExact(world,door,tx,ty,path_try,step_ms)
  local b=getBot and getBot() or nil; if not b then return false end
  path_try=path_try or 10; step_ms=step_ms or 700
  for _=1,path_try do
    local mx,my=_my_xy(); if mx==tx and my==ty then return true end
    b:findPath(tx,ty); sleep(step_ms)
    -- guard stuck white door
    if _current_tile_fg_safe(2,60)==6 then
      if not WARP_WORLD(world,door) then return false end
    end
  end
  return false
end

function DROP_ITEMS_SNAKE(WORLD,DOOR,ITEMS,opts)
  local b=getBot and getBot() or nil; if not b or type(ITEMS)~="table" then return end
  opts=opts or {}
  local CHUNK=opts.chunk or 400
  local STEP_MS=opts.step_ms or 700
  local PATH_TRY=opts.path_try or 10
  local TILE_CAP=opts.tile_cap or 4000
  local STACK_CAP=opts.stack_cap or 20
  local RETRIES_TL=opts.tile_retries or 2

  reset_caches()
  WARP_WORLD(WORLD,DOOR); sleep(150)

  local sx,sy=_my_xy()
  local wx,wy=_world_size()
  local start_col=math.min(sx+1, wx); if start_col<0 then start_col=0 end
  local start_row=math.max(0, math.min(sy, wy))
  local cursor={x=start_col, y=start_row}

  for _,ITEM in pairs(ITEMS) do
    local have=b:getInventory():getItemCount(ITEM)
    while have>0 do
      ::seek_slot::
      local candX,candY; candX,candY,cursor=_nextDropTileSnake(sx,sy,cursor,(wx-start_col+1), (start_row+1), wx, TILE_CAP, STACK_CAP)
      if not candX then print("[DROP] Tidak ketemu slot kosong."); return end
      local stanceX,stanceY=candX-1,candY
      if stanceX<0 or (not _walkable(stanceX,stanceY)) then mark_bad(candX,candY); cursor.x=candX+1; goto seek_slot end
      if not _gotoExact(WORLD,DOOR,stanceX,stanceY,PATH_TRY,STEP_MS) then mark_bad(candX,candY); cursor.x=candX+1; goto seek_slot end

      local total,stacks=_countOnTile(candX,candY)
      if (total>=TILE_CAP) or (stacks>=STACK_CAP) then mark_full(candX,candY); cursor.x=candX+1; goto seek_slot end

      local cap=math.max(0,TILE_CAP-total)
      local drop_try=math.min(have,CHUNK,cap)
      if drop_try<=0 then mark_full(candX,candY); cursor.x=candX+1; goto seek_slot end

      local attempts_here=0
      while drop_try>0 and have>0 do
        attempts_here=attempts_here+1
        local before=b:getInventory():getItemCount(ITEM)
        b:drop(tostring(ITEM),drop_try)
        sleep(STEP_MS)
        local after=b:getInventory():getItemCount(ITEM)
        if after<before then
          have=after
          local t2,s2=_countOnTile(candX,candY)
          if (t2>=TILE_CAP) or (s2>=STACK_CAP) then mark_full(candX,candY); cursor.x=candX+1; break end
          local sisa=TILE_CAP-t2; if sisa<=0 then mark_full(candX,candY); cursor.x=candX+1; break end
          drop_try=math.min(have,CHUNK,sisa); attempts_here=0
        else
          if attempts_here>=RETRIES_TL then mark_bad(candX,candY); cursor.x=candX+1; goto seek_slot end
          drop_try=math.max(1,math.floor(drop_try/2))
        end
      end
    end
  end
end

-------------------- HARVEST (ringkas) ------------------------
ITEM_BLOCK_ID = 4584
ITEM_SEED_ID  = ITEM_BLOCK_ID + 1

local function _get_tiles()
  return (type(getTilesSafe)=="function" and getTilesSafe())
      or (type(getTiles)=="function" and getTiles())
      or {}
end
local function has_harvestables()
  local b=getBot and getBot() or nil; if not(b and b.getWorld) then return false end
  local w=b:getWorld()
  for _,t in pairs(_get_tiles()) do local tt=w:getTile(t.x,t.y); if tt and tt.fg==ITEM_SEED_ID and tt:canHarvest() then return true end end
  return false
end
local function checkitemfarm(farmList)
  local inv=getBot():getInventory()
  for _,it in pairs(farmList) do if inv:getItemCount(it)>=190 then return true end end
  return false
end
function HARVEST_UNTIL_EMPTY(FARM_WORLD,FARM_DOOR,STORAGE_WORLD,STORAGE_DOOR,farmList,on_tick)
  local b=getBot and getBot() or nil; if not b then return end
  WARP_WORLD(FARM_WORLD,FARM_DOOR)
  while true do
    if on_tick then pcall(on_tick,FARM_WORLD) end
    local did=false
    local w=b:getWorld()
    for _,t in ipairs(_get_tiles()) do
      local tile=w:getTile(t.x,t.y)
      if tile and tile.fg==ITEM_SEED_ID and tile:canHarvest() then
        b:findPath(t.x,t.y); sleep(150)
        local cnt=0
        while true do
          local cur=w:getTile(t.x,t.y)
          if not(cur and cur.fg==ITEM_SEED_ID and cur:canHarvest()) then break end
          b:hit(t.x,t.y); sleep(DELAY_HARVEST)
          cnt=cnt+1; if cnt>=100 then break end
        end
        did=true
        if checkitemfarm(farmList) then break end
      end
    end
    if checkitemfarm(farmList) then
      DROP_ITEMS_SNAKE(STORAGE_WORLD,STORAGE_DOOR,farmList,{tile_cap=3000,stack_cap=20})
    end
    if (not did) and (not checkitemfarm(farmList)) then
      if not has_harvestables() then break end
    end
  end
end

-------------------- MAIN QUEUE LOOP --------------------------
local function RUN_FROM_TXT_QUEUE()
  -- takeover cepat job stale (owner mati/ban)
  RECLAIM_STALE_JOBS("takeover")

  -- resume jika kita tercatat sebagai owner
  local resumeW = FIND_OWN_INPROGRESS()
  if resumeW then
    local W,D,BID,SW,SD = SPEC_FOR_WORLD(resumeW)
    if W and BID then
      ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
      print(("[RESUME] %s -> %s|%s (BID=%d)"):format(WORKER_ID(),W,D,BID))
      local hb=function(world) _update_heartbeat(world, WORKER_ID()) end
      _update_heartbeat(W, WORKER_ID())
      HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID},hb)
      MARK_DONE(W)
    end
  end

  while true do
    -- 1) klaim job baru
    local job = CLAIM_NEXT_JOB()
    if job then
      local W,D,BID,SW,SD=_parse_world_line(job)
      if W and BID then
        ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
        print(("[JOB] %s klaim %s|%s (BID=%d)"):format(WORKER_ID(),W,D,BID))
        local hb=function(world) _update_heartbeat(world, WORKER_ID()) end
        _update_heartbeat(W, WORKER_ID())
        HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID},hb)
        MARK_DONE(W)
        print(("[JOB] %s selesai %s"):format(WORKER_ID(),W))
      end

    else
      -- 2) tidak ada unclaimed -> assist
      local qs=QUEUE_STATS()
      if qs.unclaimed>0 then
        print(("[QUEUE] Masih ada %d unclaimed. Menunggu..."):format(qs.unclaimed))
        sleep(1000)
      else
        local allow_nonstale=(ASSIST_MODE=="always")
        local assistW=PICK_ASSIST_WORLD(allow_nonstale)
        if assistW then
          print(("[HELP] %s bantu %s (%s)"):format(WORKER_ID(),assistW, allow_nonstale and "always" or "stale"))
          for _,ln in ipairs(_read_lines(JOB_FILES.worlds)) do
            local W,D,BID,SW,SD=_parse_world_line(ln)
            if W and W:upper()==assistW then
              ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
              local hb=function(world) _update_heartbeat(world, WORKER_ID()) end
              _update_heartbeat(W, WORKER_ID())
              HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID},hb)
              MARK_DONE(W)
              print(("[HELP] %s menutup %s"):format(WORKER_ID(),W))
              break
            end
          end
        else
          print("[QUEUE] Tidak ada job maupun assist. Selesai.")
          break
        end
      end
    end

    sleep(400)
  end

  -- final cleanup (opsional)
  if (STORAGE_CAKE or "")~="" then
    local b=getBot and getBot() or nil
    local inv=b and b.getInventory and b:getInventory()
    local has=false
    if inv then for _,id in pairs(cakeList or {}) do if inv:getItemCount(id)>0 then has=true; break end end end
    if has then pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE,DOOR_CAKE,cakeList,{tile_cap=3000,stack_cap=20}) end) end
  end
  local b=getBot and getBot() or nil
  if b and b.leaveWorld then b:leaveWorld() end
  sleep(800)
  if b then b.auto_reconnect=true end
end

-------------------- ENTRYPOINT -------------------------------
do
  print(string.format("[CONFIG] USE_TXT_QUEUE=%s | ASSIST_MODE=%s | STALE_SEC=%ds",
    tostring(USE_TXT_QUEUE), tostring(ASSIST_MODE), STALE_SEC))
  if USE_TXT_QUEUE then
    RUN_FROM_TXT_QUEUE()
  else
    print("[INFO] Mode RR/CHUNK tidak diaktifkan di build ini.")
  end
end
