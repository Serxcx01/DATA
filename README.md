----------------------------------------------------------------
-- FULL HARVEST SCRIPT (PATCHED)
-- - Safe warp/reconnect (anti "|" world)
-- - HARVEST_PASS 5-tile centered (left2, center, right2) zig-zag
-- - TAKE_MAGNI cooldown only after consecutive failures; logs by STORAGE
-- - DROP_ITEMS_SNAKE improved capacity check and stance
-- - All reconnect/guard calls accept explicit world/door, with safe fallbacks
-- - hasAccess(x,y) is global (no b:)
----------------------------------------------------------------

-------------------- CONFIG (user-adjustable) --------------------
USE_TXT_QUEUE = (USE_TXT_QUEUE ~= false)
ASSIST_MODE          = (ASSIST_MODE or "always")
ASSIST_MODE          = tostring(ASSIST_MODE):lower()
ASSIST_HELPER_LIMIT  = ASSIST_HELPER_LIMIT or 2
STEAL_HELP           = (STEAL_HELP ~= false)
STALE_SEC            = STALE_SEC or 30 * 60
LOOP_MODE            = LOOP_MODE or false

USE_MAGNI     = USE_MAGNI or false
DELAY_HARVEST = DELAY_HARVEST or 170

-- Storage MAGNI (optional)
STORAGE_MAGNI = (STORAGE_MAGNI or "")
DOOR_MAGNI    = (DOOR_MAGNI or "")

-- Storage CAKE (final/idle drop)
STORAGE_CAKE  = (STORAGE_CAKE or "Lgridbun5")
DOOR_CAKE     = (DOOR_CAKE or "Devi")
cakeList  = cakeList or {1058,1094,1096,1098,1828,3870,7058,10134,10136,10138,10140,10142,10146,10150,10164,10228,11286}
cekepremium = cekepremium or {1828}
MAX_CAKE_PREMIUM = MAX_CAKE_PREMIUM or 2

-- Item IDs (default; may be overridden per world)
ITEM_BLOCK_ID = ITEM_BLOCK_ID or 4584
ITEM_SEED_ID  = ITEM_SEED_ID  or (ITEM_BLOCK_ID + 1)

-- Harvest window (must be odd); default 5 => offsets -2..+2
TILE_WINDOW  = tonumber(TILE_WINDOW or 5)
local HALF_W = math.floor((TILE_WINDOW - 1) / 2)
local OFFSETS_CENTER = {}
for m = -HALF_W, HALF_W do table.insert(OFFSETS_CENTER, m) end
local TILE_STEP  = TILE_WINDOW

-- Drop snake limits
WORLD_MAX_X, WORLD_MAX_Y = 99, 23

-------------------- SAFE STATE & HELPERS --------------------
LAST_GOOD_WORLD, LAST_GOOD_DOOR = LAST_GOOD_WORLD, LAST_GOOD_DOOR

local function _norm(s) return tostring(s or ""):upper() end
local function _nz(s)  return (s ~= nil and s ~= "") and s or nil end

local function SET_LAST_TARGET(world, door)
  local w = _nz(_norm(world)); if not w then return false end
  LAST_GOOD_WORLD = w
  if door ~= nil then LAST_GOOD_DOOR = _nz(_norm(door)) or LAST_GOOD_DOOR end
  return true
end

function WARP_WORLD_SAFE(world, door)
  local w = _nz(_norm(world)); if not w then return false end
  if _nz(door) then
    if WARP_WORLD then WARP_WORLD(w, door) else getBot():warp(w.."|".._norm(door)) end
  else
    if WARP_WORLD then WARP_WORLD(w) else getBot():warp(w) end
  end
  SET_LAST_TARGET(w, door)
  return true
end

function SMART_RECONNECT_SAFE(world, door, tx, ty)
  local w = _nz(_norm(world)) or LAST_GOOD_WORLD
  if not w then return false end
  local d = _nz(_norm(door)) or LAST_GOOD_DOOR
  if SMART_RECONNECT then
    if tx and ty then SMART_RECONNECT(w, d, tx, ty) else SMART_RECONNECT(w, d) end
  else
    local b = getBot and getBot() or nil
    if b and (not b:isInWorld(w)) then
      if d then b:warp(w.."|"..d) else b:warp(w) end
    end
  end
  return true
end

function GUARD_DOOR_STUCK_SAFE(world, door)
  local w = _nz(_norm(world)) or LAST_GOOD_WORLD
  if not w then return false end
  local d = _nz(_norm(door)) or LAST_GOOD_DOOR
  if GUARD_DOOR_STUCK then GUARD_DOOR_STUCK(w, d) end
  return true
end

-------------------- SAFE GETTERS --------------------
SAFE_ONLY = (SAFE_ONLY ~= false)

local function _get_tiles()
  if SAFE_ONLY then
    return (type(getTilesSafe)=="function" and getTilesSafe()) or {}
  else
    return (type(getTilesSafe)=="function" and getTilesSafe())
        or (type(getTiles)=="function" and getTiles())
        or {}
  end
end

local function _get_objects()
  if SAFE_ONLY then
    return (type(getObjectsSafe)=="function" and getObjectsSafe()) or {}
  else
    return (type(getObjectsSafe)=="function" and getObjectsSafe())
        or (type(getObjects)=="function" and getObjects())
        or {}
  end
end

local function _world()
  local b = getBot and getBot() or nil
  return b and b.getWorld and b:getWorld() or nil
end
local function _local_xy()
  local w = _world(); local me = w and w.getLocal and w:getLocal() or nil
  if not me then return nil,nil end
  return math.floor((me.posx or 0)/32), math.floor((me.posy or 0)/32)
end

function ZEE_COLLECT(state)
  local b=getBot and getBot() or nil; if not b then return end
  if state then b.auto_collect=true; b.ignore_gems=true; b.collect_range=3; b.object_collect_delay=200
  else b.auto_collect=false end
end

function faceSide2()
  local b=getBot and getBot() or bot; if not b then return end
  local packet=GameUpdatePacket.new(); packet.type=0; packet.flags=32; b:sendRaw(packet)
end

-------------------- DROP SNAKE SUPPORT --------------------
local _OBJ_CACHE = { grid={}, last_refresh=0 }
local function _grid_key(x,y) return tostring(x).."|"..tostring(y) end
local function _rebuild_obj_grid()
  _OBJ_CACHE.grid={}
  local w=_world(); if not w then return end
  local objs=(w.getObjects and w:getObjects()) or {}
  for _,o in pairs(objs) do
    local ox=math.floor((o.x+16)/32); local oy=math.floor(o.y/32)
    local k=_grid_key(ox,oy); local g=_OBJ_CACHE.grid[k]
    if not g then g={total=0,stacks=0}; _OBJ_CACHE.grid[k]=g end
    g.total=g.total+(o.count or 0); g.stacks=g.stacks+1
  end
  _OBJ_CACHE.last_refresh=os.time()
end
local function _maybe_refresh_obj_grid() if (os.time()-(_OBJ_CACHE.last_refresh or 0))>=3 then _rebuild_obj_grid() end end
local function _countOnTile(tx,ty) _maybe_refresh_obj_grid(); local g=_OBJ_CACHE.grid[tostring(tx).."|"..tostring(ty)]; if g then return g.total,g.stacks end; return 0,0 end

local function REFRESH_WORLD_BOUNDS()
  local w=_world(); if not w then return end
  local wx=(w.width and (w.width-1)) or WORLD_MAX_X
  local wy=(w.height and (w.height-1)) or WORLD_MAX_Y
  WORLD_MAX_X, WORLD_MAX_Y = wx, wy
end

local function _is_in_bounds(x,y) return x>=0 and x<=WORLD_MAX_X and y>=0 and y<=WORLD_MAX_Y end
local function _is_walkable(tx,ty)
  local w=_world(); local t=w and w:getTile(tx,ty) or nil
  return (t~=nil) and ((t.fg or 0)==0)
end

local FULL_CACHE, BAD_CACHE = {}, {}
local function _key(x,y) return x..":"..y end
local function mark_full(x,y) FULL_CACHE[_key(x,y)]=true end
local function mark_bad (x,y) BAD_CACHE [_key(x,y)]=true end
local function is_full_or_bad(x,y) return FULL_CACHE[_key(x,y)] or BAD_CACHE[_key(x,y)] end
local function reset_caches() FULL_CACHE={}; BAD_CACHE={} end

local function _nextDropTileSnake_auto(sx,sy,cursor,tile_cap,stack_cap)
  local function _probe_slot(cx,cy)
    if not _is_in_bounds(cx,cy) then return false end
    local w=_world(); if not w then return false end
    local t=w:getTile(cx,cy); if not t or (t.fg or 0)~=0 then mark_bad(cx,cy); return false end
    local stanceX, stanceY = cx-1, cy
    if stanceX < 0 or (not _is_in_bounds(stanceX,stanceY)) or (not _is_walkable(stanceX,stanceY)) then
      mark_bad(cx,cy); return false
    end
    if is_full_or_bad(cx,cy) then return false end
    local total,stacks=_countOnTile(cx,cy)
    if (total >= (tile_cap or 4000)) or (stacks >= (stack_cap or 20)) then mark_full(cx,cy); return false end
    return true
  end

  local function _scan_row_right(start_x, cy, tile_cap, stack_cap)
    local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
    while cx<=WORLD_MAX_X do if _probe_slot(cx,cy) then return cx,cy end; cx=cx+1 end
    return nil,nil
  end
  local function _scan_row_left(start_x, cy, tile_cap, stack_cap)
    local cx=math.max(0, math.min(start_x, WORLD_MAX_X))
    while cx>=0 do if _probe_slot(cx,cy) then return cx,cy end; cx=cx-1 end
    return nil,nil
  end

  local start_col=sx+1; if start_col>WORLD_MAX_X then start_col=WORLD_MAX_X end; if start_col<0 then start_col=0 end
  local curx=cursor.x or start_col; local cury=math.max(0, math.min(cursor.y or sy, WORLD_MAX_Y))

  do -- Pass 1: kanan → atas
    local y=cury; local first_row=true
    while y>=0 do
      local row_start= first_row and math.max(curx,start_col) or start_col
      local rx,ry=_scan_row_right(row_start,y,tile_cap,stack_cap)
      if rx then cursor.x, cursor.y = rx, ry; return rx, ry, cursor end
      y=y-1; first_row=false
    end
  end
  do -- Pass 2: fallback kiri ←
    local y=cury; local first_row=true
    while y>=0 do
      local row_start_left= first_row and (math.min(curx,WORLD_MAX_X)-1) or (start_col-1)
      if row_start_left>WORLD_MAX_X then row_start_left=WORLD_MAX_X end
      if row_start_left<0 then row_start_left=start_col-1 end
      local lx,ly=_scan_row_left(row_start_left,y,tile_cap,stack_cap)
      if lx then cursor.x, cursor.y = lx, ly; return lx, ly, cursor end
      y=y-1; first_row=false
    end
  end
  return nil,nil,cursor
end

local function _meTile()
  local x,y = _local_xy()
  return x or 0, y or 0
end

local function _gotoExact(world, door, tx, ty, path_try, step_ms)
  local b = getBot and getBot() or nil; if not b then return false end
  path_try = path_try or 10
  step_ms  = step_ms  or 700
  local last_mx, last_my = nil, nil
  local stale_ticks = 0
  local backoff     = 0
  for _ = 1, path_try do
    local mx, my = _meTile()
    if mx == tx and my == ty then return true end
    b:findPath(tx, ty)
    sleep(step_ms + backoff)
    SMART_RECONNECT_SAFE(world, door)
    local cmx, cmy = _meTile()
    if (cmx == (last_mx or mx)) and (cmy == (last_my or my)) then
      stale_ticks = stale_ticks + 1
      if stale_ticks >= 3 then
        if backoff < 600 then backoff = math.min(600, (backoff == 0) and 150 or math.floor(backoff * 2)) end
        sleep(120)
        if stale_ticks >= 6 then return false end
      end
    else
      stale_ticks = 0
      backoff = 0
    end
    last_mx, last_my = cmx, cmy
  end
  return false
end

-------------------- CAKE --------------------
local function includesNumber(t,n) for _,num in pairs(t or {}) do if num==n then return true end end; return false end
function checkCake()
  local bot = getBot and getBot() or nil; if not (bot and bot.getInventory) then return false end
  local inv = bot:getInventory()
  for _, id in pairs(cakeList or {}) do
    local isPremium = includesNumber(cekepremium or {}, id)
    local need = isPremium and MAX_CAKE_PREMIUM or 120
    if inv:getItemCount(id) >= need then return true end
  end
  return false
end
local __next_cake_drop_at_ms, __cake_cooldown_ms = 0, 4000
local function __now_ms() return (os.time() or 0)*1000 end
local function _maybe_drop_cake()
  if not (type(checkCake)=="function" and checkCake()) then return end
  local t=__now_ms(); if t<__next_cake_drop_at_ms then return end
  DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList)
  __next_cake_drop_at_ms = t + __cake_cooldown_ms
end

-------------------- DROP_ITEMS_SNAKE --------------------
function DROP_ITEMS_SNAKE(WORLD, DOOR, ITEMS, opts)
  local b = getBot and getBot() or nil
  if not b or type(ITEMS) ~= "table" then return end

  opts = opts or {}
  local CHUNK      = opts.chunk or 400
  local STEP_MS    = opts.step_ms or 700
  local PATH_TRY   = opts.path_try or 10
  local TILE_CAP   = opts.tile_cap or 4000
  local STACK_CAP  = opts.stack_cap or 20
  local RETRIES_TL = opts.tile_retries or 2
  local HARD_LIMIT = 150

  local function _poll_inv_drop_ok(item_id, before)
    for _ = 1, 4 do
      sleep(math.max(120, math.floor(STEP_MS/4)))
      local now = b:getInventory():getItemCount(item_id)
      if now < before then return true, now end
    end
    return false, b:getInventory():getItemCount(item_id)
  end

  reset_caches(); ZEE_COLLECT(false)
  WARP_WORLD_SAFE(WORLD, DOOR); sleep(150); SMART_RECONNECT_SAFE(WORLD, DOOR)
  REFRESH_WORLD_BOUNDS()

  local sx, sy = _meTile()
  local start_col = math.min((sx or 0) + 1, WORLD_MAX_X); if start_col < 0 then start_col = 0 end
  local start_row = math.max(0, math.min(sy or 0, WORLD_MAX_Y))
  local cursor    = { x = start_col, y = start_row }

  for _, ITEM in pairs(ITEMS) do
    local have = b:getInventory():getItemCount(ITEM)
    local hard_attempts = 0
    while have > 0 do
      ::seek_slot::
      if hard_attempts > HARD_LIMIT then
        print("[DROP] hard-limit tercapai, cari tile lain ", ITEM)
        hard_attempts = 0
      end
      local candX, candY
      candX, candY, cursor = _nextDropTileSnake_auto(sx or 0, sy or 0, cursor, TILE_CAP, STACK_CAP)
      if not candX then
        print("[DROP] Area penuh/habis jangkauan.")
        return
      end
      local stanceX, stanceY = candX - 1, candY
      if (stanceX < 0) or (not _is_in_bounds(stanceX, stanceY)) or (not _is_walkable(stanceX, stanceY)) then
        mark_bad(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end
      if not _gotoExact(WORLD, DOOR, stanceX, stanceY, PATH_TRY, STEP_MS) then
        mark_bad(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      faceSide2()
      local total, stacks = _countOnTile(candX, candY)
      if (total >= TILE_CAP) or (stacks >= STACK_CAP) then
        mark_full(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      local cap = math.max(0, TILE_CAP - total)
      local drop_try = math.min(have, CHUNK, cap)
      if drop_try <= 0 then
        mark_full(candX, candY)
        cursor.x = math.min(candX + 1, WORLD_MAX_X)
        goto seek_slot
      end

      local attempts_here = 0
      while drop_try > 0 and have > 0 do
        attempts_here  = attempts_here + 1
        hard_attempts  = hard_attempts + 1

        local before = b:getInventory():getItemCount(ITEM)
        b:drop(ITEM, drop_try)

        sleep(STEP_MS)
        SMART_RECONNECT_SAFE(WORLD, DOOR)

        local ok, after = _poll_inv_drop_ok(ITEM, before)
        if ok then
          have = after
          attempts_here = 0
          local t2, s2 = _countOnTile(candX, candY)
          if (t2 >= TILE_CAP) or (s2 >= STACK_CAP) then
            mark_full(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            break
          end
          local sisa = TILE_CAP - t2
          if sisa <= 0 then
            mark_full(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            break
          end
          drop_try = math.min(have, CHUNK, sisa)
        else
          if attempts_here >= RETRIES_TL then
            mark_bad(candX, candY)
            cursor.x = math.min(candX + 1, WORLD_MAX_X)
            goto seek_slot
          end
          drop_try = math.max(1, math.floor(drop_try / 2))
        end

        if hard_attempts > HARD_LIMIT then
          mark_bad(candX, candY)
          cursor.x = math.min(candX + 1, WORLD_MAX_X)
          goto seek_slot
        end
      end
    end
  end
end

-------------------- MAGNI: keep exactly 1 (cooldown after fails) --------------------
MAGNI_COOLDOWN       = MAGNI_COOLDOWN or {}
MAGNI_COOLDOWN_MIN   = tonumber(MAGNI_COOLDOWN_MIN or 10)
MAGNI_FAILS          = MAGNI_FAILS or {}
MAGNI_FAILS_MAX_TRY  = tonumber(MAGNI_FAILS_MAX_TRY or 3)

local function _world_key(w) return tostring(w or ""):upper() end
local function _set_cd(w, add_min)
  local mins = tonumber(add_min ~= nil and add_min or MAGNI_COOLDOWN_MIN) or 0
  if mins > 0 then MAGNI_COOLDOWN[_world_key(w)] = os.time() + mins*60 end
end
local function _inc_fail(w) local k=_world_key(w); MAGNI_FAILS[k]=(MAGNI_FAILS[k] or 0)+1; return MAGNI_FAILS[k] end
local function _reset_fail(w) MAGNI_FAILS[_world_key(w)] = 0 end

local function _ensure_single_item_in_storage(item_id, keep, storageW, storageD, opts)
  local b=getBot and getBot() or nil; if not b then return end
  keep=keep or 1; opts=opts or {}
  local CHUNK=opts.chunk or 400; local STEP_MS=opts.step_ms or 700; local PATH_TRY=opts.path_try or 10
  local TILE_CAP=opts.tile_cap or 4000; local STACK_CAP=opts.stack_cap or 20; local RETRIES_TL=opts.tile_retries or 2
  local inv=b:getInventory(); local have=inv:getItemCount(item_id)
  if have<=keep then return end
  if (storageW or "")~="" then WARP_WORLD_SAFE(storageW,storageD); sleep(150); SMART_RECONNECT_SAFE(storageW,storageD) end
  reset_caches(); ZEE_COLLECT(false)
  local mx,my=_local_xy(); local sx,sy= (mx or 1), (my or 1)
  local cursor={x=math.min(sx+1,WORLD_MAX_X), y=math.max(0, math.min(sy, WORLD_MAX_Y))}
  local extras=have-keep
  while extras>0 do
    ::seek_slot::
    local candX,candY; candX,candY,cursor=_nextDropTileSnake_auto(sx,sy,cursor,TILE_CAP,STACK_CAP)
    if not candX then print("[MAGNI] Storage area penuh/jangkauan habis."); return end
    local stanceX,stanceY=candX-1,candY
    if (stanceX<0) or (not _is_in_bounds(stanceX,stanceY)) or (not _is_walkable(stanceX,stanceY)) then
      mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot
    end
    if not _gotoExact(storageW,storageD,stanceX,stanceY,PATH_TRY,STEP_MS) then
      mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot
    end
    faceSide2()
    local total,stacks=_countOnTile(candX,candY)
    if (total>=TILE_CAP) or (stacks>=STACK_CAP) then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
    local cap=math.max(0,TILE_CAP-total); local drop_try=math.min(extras,CHUNK,cap); if drop_try<=0 then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
    local attempts_here=0
    while drop_try>0 and extras>0 do
      attempts_here=attempts_here+1
      local before=inv:getItemCount(item_id)
      b:drop(item_id, drop_try)
      sleep(STEP_MS); SMART_RECONNECT_SAFE(storageW,storageD)
      local after=inv:getItemCount(item_id)
      if after<before then
        local dropped=before-after; extras=math.max(0, extras-dropped)
        local t2,s2=_countOnTile(candX,candY)
        if (t2>=TILE_CAP) or (s2>=STACK_CAP) then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); break end
        local sisa_cap=TILE_CAP-t2; if sisa_cap<=0 then mark_full(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); break end
        drop_try=math.min(extras,CHUNK,sisa_cap); attempts_here=0
      else
        if attempts_here>=RETRIES_TL then mark_bad(candX,candY); cursor.x=math.min(candX+1,WORLD_MAX_X); goto seek_slot end
        drop_try=math.max(1, math.floor(drop_try/2))
      end
    end
  end
end

function TAKE_MAGNI(WORLD, DOOR)
  local b=getBot and getBot() or nil; if not b or not USE_MAGNI then return false end
  local TARGET_ID=10158; local inv=b:getInventory()
  local now=os.time()
  local CD_WORLD = ((STORAGE_MAGNI or "") ~= "") and STORAGE_MAGNI or WORLD
  local CDKEY    = _world_key(CD_WORLD)

  do
    local cd_until = MAGNI_COOLDOWN[CDKEY]
    if cd_until and now < cd_until then
      local sisa = cd_until - now
      print(string.format("[TAKE_MAGNI] Cooldown aktif %s (%ds)", CD_WORLD, sisa))
      return false
    end
  end

  do
    local have=inv:getItemCount(TARGET_ID)
    if have>1 then
      local storageW,storageD=STORAGE_MAGNI,DOOR_MAGNI
      if (storageW or "")=="" then storageW,storageD=WORLD,DOOR end
      _ensure_single_item_in_storage(TARGET_ID,1,storageW,storageD,
        {chunk=200,step_ms=600,path_try=10,tile_cap=4000,stack_cap=20,tile_retries=2})
      if inv:getItemCount(TARGET_ID)>0 then b:wear(TARGET_ID); sleep(250) end
      return true
    end
  end

  local function _try_take_at(w,d)
    if (w or "")=="" then return false end
    WARP_WORLD_SAFE(w,d); sleep(250)
    SMART_RECONNECT_SAFE(w,d)
    txafterwarp, tyafterwarp = (getBot() and getBot().x or nil), (getBot() and getBot().y or nil)

    local MAX_ROUNDS, WAIT_MS = 10, 1200
    local got=false
    ZEE_COLLECT(true)
    local ok, err = pcall(function()
      for _=1,MAX_ROUNDS do
        if inv:getItemCount(TARGET_ID)>0 then got=true; break end
        local objs=_get_objects()
        local ww=_world(); local me=ww and ww:getLocal() or nil
        local best,bestd2=nil,1e18
        for _,o in pairs(objs) do
          if o.id==TARGET_ID then
            local txo,tyo=math.floor(o.x/32),math.floor(o.y/32)
            if me then
              local mx,my=math.floor(me.posx/32),math.floor(me.posy/32)
              local d2=(txo-mx)*(txo-mx)+(tyo-my)*(tyo-my)
              if d2<bestd2 then best,bestd2=o,d2 end
            else best,bestd2=o,0 end
          end
        end
        if best then
          local tx,ty=math.floor(best.x/32),math.floor(best.y/32)
          SMART_RECONNECT_SAFE(w,d,tx,ty); getBot():findPath(tx,ty); sleep(WAIT_MS)
        else
          SMART_RECONNECT_SAFE(w,d); sleep(WAIT_MS)
        end
      end
    end)
    ZEE_COLLECT(false)
    return got or (inv:getItemCount(TARGET_ID)>0)
  end

  local got = inv:getItemCount(TARGET_ID) > 0
  if not got then
    got = _try_take_at(STORAGE_MAGNI, DOOR_MAGNI) or _try_take_at(WORLD, DOOR)
  end

  do
    local storageW,storageD=STORAGE_MAGNI,DOOR_MAGNI
    if (storageW or "")=="" then storageW,storageD=WORLD,DOOR end
    if txafterwarp and tyafterwarp then
      getBot():findPath(txafterwarp, tyafterwarp); sleep(400); faceSide2()
    end
    _ensure_single_item_in_storage(10158,1,storageW,storageD,
      {chunk=200,step_ms=600,path_try=10,tile_cap=4000,stack_cap=20,tile_retries=2})
  end

  if inv:getItemCount(10158)>0 then
    getBot():wear(10158); sleep(250)
    _reset_fail(CD_WORLD)
    return true
  else
    local fails = _inc_fail(CD_WORLD)
    print(string.format("[TAKE_MAGNI] Gagal #%d di %s", fails, CD_WORLD))
    if fails >= (MAGNI_FAILS_MAX_TRY or 3) then
      _set_cd(CD_WORLD)
      print(string.format("[TAKE_MAGNI] Set cooldown %s (%d menit) setelah %d gagal.",
        CD_WORLD, MAGNI_COOLDOWN_MIN or 10, fails))
      _reset_fail(CD_WORLD)
    end
    return false
  end
end

-------------------- HARVEST (5-tile centered) --------------------
local function _sorted_rows_and_bounds()
  local rows_map, bounds = {}, {}
  local w = _world()
  for _, t in pairs(_get_tiles()) do
    local tile = w:getTile(t.x, t.y)
    if tile and tile.fg == ITEM_SEED_ID and tile:canHarvest() and hasAccess(t.x, t.y) > 0 then
      rows_map[t.y] = true
      local bd = bounds[t.y]
      if not bd then
        bounds[t.y] = {min_x = t.x, max_x = t.x}
      else
        if t.x < bd.min_x then bd.min_x = t.x end
        if t.x > bd.max_x then bd.max_x = t.x end
      end
    end
  end
  local rows = {}
  for y,_ in pairs(rows_map) do table.insert(rows, y) end
  table.sort(rows)
  return rows, bounds
end

local function _at_tile(x, y)
  local mx,my = _local_xy()
  return mx and my and (mx==x and my==y)
end

local function _valid_seed_tile(x, y)
  local w = _world(); local t = w and w:getTile(x, y) or nil
  return t and t.fg == ITEM_SEED_ID and t:canHarvest() and hasAccess(x, y) > 0
end

function HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
  local b = getBot and getBot() or nil; if not b then return false end

  if USE_MAGNI then
    local inv = b:getInventory(); local have = inv:getItemCount(10158); local called = false
    if have == 0 then
      if (STORAGE_MAGNI or "") ~= "" then TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI); called = true end
      if inv:getItemCount(10158) == 0 then TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called = true end
    elseif have > 1 then TAKE_MAGNI(FARM_WORLD, FARM_DOOR); called = true end
    if (not called) and inv:getItemCount(10158) > 0 then b:wear(10158); sleep(200) end
  end

  WARP_WORLD_SAFE(FARM_WORLD, FARM_DOOR)
  ZEE_COLLECT(true); sleep(120); SMART_RECONNECT_SAFE(FARM_WORLD, FARM_DOOR)

  local w = _world(); if not w then ZEE_COLLECT(false); return false end
  local worldW = (w.getWidth and w:getWidth()) or 200
  local did_any = false

  local rows, bounds = _sorted_rows_and_bounds()

  for i, y in ipairs(rows) do
    _maybe_drop_cake()
    SMART_RECONNECT_SAFE(FARM_WORLD, FARM_DOOR)

    local bd = bounds[y]
    if bd then
      local minA = bd.min_x + HALF_W
      local maxA = bd.max_x - HALF_W
      if minA > maxA then minA, maxA = bd.min_x, bd.max_x end

      local forward   = (i % 2 == 1)
      local direction = forward and 1 or -1
      local x_start   = forward and minA or maxA
      local x_end     = forward and maxA or minA
      local anchor    = x_start

      local step = ((maxA - minA + 1) < TILE_WINDOW) and 1 or TILE_STEP

      while true do
        if forward and anchor > x_end then break end
        if (not forward) and anchor < x_end then break end

        local tries = 0
        while tries < 6 and not _at_tile(anchor, y) do
          b:findPath(anchor, y)
          SMART_RECONNECT_SAFE(FARM_WORLD, FARM_DOOR)
          GUARD_DOOR_STUCK_SAFE(FARM_WORLD, FARM_DOOR)
          tries = tries + 1; sleep(80)
        end

        if _at_tile(anchor, y) then
          for _, m in ipairs(OFFSETS_CENTER) do
            local hx = anchor + m
            if hx >= 0 and hx < worldW then
              local hit_cnt = 0
              while _valid_seed_tile(hx, y) and _at_tile(anchor, y) do
                b:hit(hx, y)
                sleep(DELAY_HARVEST)
                SMART_RECONNECT_SAFE(FARM_WORLD, FARM_DOOR)
                GUARD_DOOR_STUCK_SAFE(FARM_WORLD, FARM_DOOR)
                hit_cnt = hit_cnt + 1
                if hit_cnt >= 100 then
                  print(string.format("[HARVEST_PASS] Stop 100 hits (%d,%d)", hx, y))
                  break
                end
              end
            end
          end
          did_any = true
        end

        _maybe_drop_cake()
        if checkitemfarm and checkitemfarm(farmListActive) then ZEE_COLLECT(false); return did_any end

        anchor = anchor + (direction * step)
      end
    end
  end

  _maybe_drop_cake()
  ZEE_COLLECT(false)
  return did_any
end

function has_harvestables()
  local w=_world(); if not w then return false end
  for _,t in pairs(_get_tiles()) do local tt=w:getTile(t.x,t.y); if tt and tt.fg==ITEM_SEED_ID and tt:canHarvest() then return true end end
  return false
end

local function checkitemfarm(farmList)
  local inv=getBot():getInventory()
  for _,item in pairs(farmList) do if inv:getItemCount(item)>=190 then return true end end
  return false
end
local function has_any_item_farm(farmList)
  local inv=getBot():getInventory()
  for _,item in pairs(farmList) do if inv:getItemCount(item)>0 then return true end end
  return false
end

function DROP_FARM_ITEMS(STORAGE_WORLD, STORAGE_DOOR, farmListActive)
  if has_any_item_farm(farmListActive) then
    DROP_ITEMS_SNAKE(STORAGE_WORLD, STORAGE_DOOR, farmListActive, {tile_cap=3000, stack_cap=20})
  end
end

function HARVEST_UNTIL_EMPTY(FARM_WORLD, FARM_DOOR, STORAGE_WORLD, STORAGE_DOOR, farmListActive, on_tick)
  local ok = WARP_WORLD_SAFE(FARM_WORLD, FARM_DOOR)
  if not ok then print("[HARVEST] Gagal warp ke:", FARM_WORLD); return end
  local t0=os.time()
  while true do
    if on_tick then pcall(on_tick, FARM_WORLD) end
    local did=HARVEST_PASS(FARM_WORLD, FARM_DOOR, farmListActive)
    if on_tick then pcall(on_tick, FARM_WORLD) end
    if checkitemfarm and checkitemfarm(farmListActive) then
      DROP_ITEMS_SNAKE(STORAGE_WORLD, STORAGE_DOOR, farmListActive, {tile_cap=3000, stack_cap=20})
      _maybe_drop_cake()
    end
    if (not did) and (not checkitemfarm(farmListActive)) then
      if not has_harvestables() then print("[HARVEST] Selesai world:", FARM_WORLD); break end
    end
  end
  DROP_FARM_ITEMS(STORAGE_WORLD, STORAGE_DOOR, farmListActive)
  ZEE_COLLECT(false)
  print(string.format("[HARVEST] %s selesai dalam %ds", tostring(FARM_WORLD), os.time()-t0))
end

-------------------- RR/CHUNK MODE --------------------
local function _parse_world_entry(s)
  local farmW,farmD,idstr,storeW,storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW or not idstr then return nil end
  return (farmW or ""):upper(), (farmD or ""), tonumber(idstr), (storeW or ""):upper(), (storeD or "")
end

function RUN_MULTI_HARVEST(list_world)
  if USE_MAGNI then TAKE_MAGNI(STORAGE_MAGNI, DOOR_MAGNI) end
  local old_block,old_seed=ITEM_BLOCK_ID, ITEM_SEED_ID
  local specs={}
  for idx,entry in ipairs(list_world or {}) do
    local W,D,BID,SW,SD=_parse_world_entry(entry)
    if W and BID then
      ITEM_BLOCK_ID=BID; ITEM_SEED_ID=BID+1
      local perworld={ITEM_BLOCK_ID, ITEM_SEED_ID}
      print(("[MULTI] %d) %s|%s BLOCK=%d SEED=%d -> %s|%s"):format(idx,W,D,ITEM_BLOCK_ID,ITEM_SEED_ID,SW,SD))
      local ok,reason=warp_ok_and_public(W,D)
      if not ok then print(("⏭ Skip %s (%s)"):format(W, tostring(reason))); goto cont end
      specs[#specs+1]={storageW=SW, storageD=SD, farmItems=perworld}
      HARVEST_UNTIL_EMPTY(W,D,SW,SD,perworld)
      ::cont::
    else print("[MULTI] Entry invalid: "..tostring(entry)) end
  end
  ITEM_BLOCK_ID,ITEM_SEED_ID=old_block,old_seed
  print("[MULTI] Final drop per-world...")
  for _,sp in ipairs(specs) do DROP_ITEMS_SNAKE(sp.storageW, sp.storageD, sp.farmItems, {tile_cap=3000, stack_cap=20}) end
  if (STORAGE_CAKE or "")~="" and has_any_cake() then pcall(function() DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList, {tile_cap=3000, stack_cap=20}) end) end
  local b=getBot and getBot() or nil; if b and b.leaveWorld then b:leaveWorld() end; sleep(900); if b then b.auto_reconnect=true end
  print("[MULTI] Done.")
end

-------------------- TXT QUEUE (assist: "stale" / "always") --------------------
local function _read_lines(path)
  local t, f={}, io.open(path,"r"); if not f then return t end
  for line in f:lines() do line=line:gsub("\r",""):gsub("\n",""); if line~="" and not line:match("^%s*;") then table.insert(t,line) end end
  f:close(); return t
end
local function _write_lines(path, lines) local f=io.open(path,"w"); if not f then return false end; for _,ln in ipairs(lines or {}) do f:write(ln.."\n") end; f:close(); return true end
local function _append_line(path,line) local f=io.open(path,"a"); if not f then return false end; f:write(line.."\n"); f:close(); return true end
local function _now() return os.time() end

local function _parse_world_line(s)
  local farmW,farmD,bid,storeW,storeD = s:match("^([^|]+)|([^|]*)|(%d+)|([^|]*)|([^|]*)$")
  if not farmW then return nil end
  return farmW:upper(), (farmD or ""), tonumber(bid), (storeW or ""):upper(), (storeD or "")
end
local function _set_of_worlds(lines) local S={}; for _,ln in ipairs(lines) do local w=ln:match("^([^|]+)"); if w then S[w:upper()]=true end end; return S end

local function _update_heartbeat(world, who_slot)
  world=(world or ""):upper(); who_slot=who_slot or WORKER_ID
  local now=_now(); local rows=_read_lines(JOB_FILES.inprogress); local out,touched={},false
  for _,ln in ipairs(rows) do
    local w,who,ts=ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts then
      if w:upper()==world and who==who_slot then table.insert(out, string.format("%s|%s|%d", w, who_slot, now)); touched=true
      else table.insert(out, ln) end
    end
  end
  if not touched then table.insert(out, string.format("%s|%s|%d", world, who_slot, now)) end
  _write_lines(JOB_FILES.inprogress, out)
end

local function CLAIM_NEXT_JOB()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog=_read_lines(JOB_FILES.inprogress)
  local done=_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog), _set_of_worlds(done)
  for _,ln in ipairs(worlds) do
    local W=ln:match("^([^|]+)")
    if W and (not S_prog[W:upper()]) and (not S_done[W:upper()]) then
      _append_line(JOB_FILES.inprogress, string.format("%s|%s|%d", W:upper(), WORKER_ID, _now()))
      return ln
    end
  end
  return nil
end

local function MARK_DONE(world)
  world=(world or ""):upper()
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if w and w:upper()~=world then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress, out)
  _append_line(JOB_FILES.done, string.format("%s|%s|%d", world, WORKER_ID, _now()))
end

local function QUEUE_STATS()
  local worlds=_read_lines(JOB_FILES.worlds)
  local prog=_read_lines(JOB_FILES.inprogress)
  local done=_read_lines(JOB_FILES.done)
  local S_prog,S_done=_set_of_worlds(prog), _set_of_worlds(done)
  local total,unclaimed,inprog,ndone=0,0,0,0
  for _,ln in ipairs(worlds) do
    local W=(ln:match("^([^|]+)") or ""):upper()
    if W~="" then
      total=total+1
      local is_prog=S_prog[W] and true or false
      local is_done=S_done[W] and true or false
      if (not is_prog) and (not is_done) then unclaimed=unclaimed+1 end
      if is_prog then inprog=inprog+1 end
      if is_done then ndone=ndone+1 end
    end
  end
  return {total=total, unclaimed=unclaimed, inprogress=inprog, done=ndone}
end

-- PICK_ASSIST_WORLD dengan mode:
--  - "stale": pilih inprogress milik orang lain yang macet >= STALE_SEC dan STEAL owner -> bisa MARK_DONE
--  - "always": pilih inprogress milik orang lain (terlama), TANPA steal -> tidak MARK_DONE

-- Hitung jumlah WORKER_ID unik yang terdaftar untuk sebuah world di inprogress.txt
local function _count_unique_workers(world)
  world = (world or ""):upper()
  if world == "" then return 0 end
  local rows = _read_lines(JOB_FILES.inprogress)
  local S = {}
  for _, ln in ipairs(rows) do
    local w, who = ln:match("^([^|]+)|([^|]+)|")
    if w and who and (w:upper() == world) then S[who] = true end
  end
  local n = 0
  for _ in pairs(S) do n = n + 1 end
  return n
end

-- Cek apakah world masih punya job (masih ada di worlds.txt)
local function _world_has_job(world)
  world = (world or ""):upper()
  if world == "" then return false end
  local rows = _read_lines(JOB_FILES.worlds)
  for _, ln in ipairs(rows) do
    local W = ln:match("^([^|]+)")
    if W and W:upper() == world then return true end
  end
  return false
end

-- Bersihkan semua entry inprogress untuk world tertentu (owner/helpers yang nyangkut)
local function _cleanup_stale_inprogress(world)
  world = (world or ""):upper()
  if world == "" then return end
  local rows = _read_lines(JOB_FILES.inprogress)
  local out = {}
  for _, ln in ipairs(rows) do
    local W = ln:match("^([^|]+)")
    if not (W and W:upper() == world) then
      table.insert(out, ln)
    end
  end
  _write_lines(JOB_FILES.inprogress, out)
end


-- PICK_ASSIST_WORLD dengan limit helper & cleanup zombie
local function PICK_ASSIST_WORLD(mode)
  local prog = _read_lines(JOB_FILES.inprogress)
  if #prog == 0 then return nil, false end

  -- pilih world kandidat milik orang lain (terlama heartbeat)
  local best, best_age, best_owner = nil, -1, nil
  local now = _now()
  for _, ln in ipairs(prog) do
    local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
    if w and who and ts and who ~= WORKER_ID then
      local age = now - tonumber(ts)
      if age > best_age then
        best, best_age, best_owner = w:upper(), age, who
      end
    end
  end
  if not best then return nil, false end

  -- jika world ini sudah tidak ada di worlds.txt → cleanup & skip
  if not _world_has_job(best) then
    _cleanup_stale_inprogress(best)
    return nil, false
  end

  if mode == "stale" then
    -- seperti semula: bantu hanya jika macet >= STALE_SEC dan boleh steal
    if best_age < (STALE_SEC or 90) or not STEAL_HELP then
      return nil, false
    end

    -- steal owner → set owner jadi kita di inprogress
    local rows = _read_lines(JOB_FILES.inprogress)
    local out, stolen = {}, false
    for _, ln in ipairs(rows) do
      local w, who, ts = ln:match("^([^|]+)|([^|]+)|(%d+)$")
      if w and who and ts and w:upper() == best then
        table.insert(out, string.format("%s|%s|%d", w:upper(), WORKER_ID, _now()))
        stolen = true
      else
        table.insert(out, ln)
      end
    end
    if stolen then _write_lines(JOB_FILES.inprogress, out) end
    return best, true
  else
    -- mode "always": bantu tanpa steal, tapi hormati limit helper
    local total_workers = _count_unique_workers(best)   -- owner + helpers
    local helpers_now   = math.max(0, total_workers - 1)
    if helpers_now >= (ASSIST_HELPER_LIMIT or 0) then
      return nil, false   -- sudah penuh helper untuk world ini
    end
    return best, false
  end
end


local function RECONCILE_QUEUE()
  local worlds=_read_lines(JOB_FILES.worlds)
  local done=_read_lines(JOB_FILES.done); local S_done=_set_of_worlds(done)
  local out={}
  for _,ln in ipairs(worlds) do local W=ln:match("^([^|]+)") or ""; if W~="" and (not S_done[W:upper()]) then table.insert(out, ln) end end
  _write_lines(JOB_FILES.worlds, out)
end

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
  world=(world or ""):upper()
  local rows=_read_lines(JOB_FILES.inprogress); local out={}
  for _,ln in ipairs(rows) do local w=ln:match("^([^|]+)"); if w and w:upper()~=world then table.insert(out,ln) end end
  _write_lines(JOB_FILES.inprogress, out)
end

function RUN_FROM_TXT_QUEUE()
  -- Auto-resume by SLOT
  local resumeW = FIND_OWN_INPROGRESS()
  if resumeW then
    local W,D,BID,SW,SD = SPEC_FOR_WORLD(resumeW)
    if W and BID then
      ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
      print(string.format("[RESUME] %s lanjut %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
      local hb = function(world) _update_heartbeat(world, WORKER_ID) end
      _update_heartbeat(W, WORKER_ID)
      HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)
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
      local W,D,BID,SW,SD = _parse_world_line(job)
      if W and BID then
        ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
        print(string.format("[JOB] %s klaim %s|%s (BID=%d)", WORKER_ID, W, (D or ""), BID))
        local hb = function(world) _update_heartbeat(world, WORKER_ID) end
        _update_heartbeat(W, WORKER_ID)
        HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)
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
        local assistW, stolen = PICK_ASSIST_WORLD(ASSIST_MODE)

        -- >>> NEW GUARD: anti-spam & limit helper
        if assistW then
          -- skip kalau world sudah tidak punya job
          if not _world_has_job(assistW) then
            _cleanup_stale_inprogress(assistW)
            assistW = nil
          else
            -- re-check limit helper
            if ASSIST_MODE == "always" then
              local total_workers = _count_unique_workers(assistW)
              local helpers_now   = math.max(0, total_workers - 1)
              if helpers_now >= (ASSIST_HELPER_LIMIT or 0) then
                assistW = nil
              end
            end
          end
        end
        -- <<< END NEW

        if assistW then
          print(string.format("[HELP] %s bantu %s (mode=%s%s)",
            WORKER_ID, assistW, ASSIST_MODE, stolen and " +steal" or ""))
          local worlds = _read_lines(JOB_FILES.worlds)
          for _,ln in ipairs(worlds) do
            local W,D,BID,SW,SD = _parse_world_line(ln)
            if W == assistW then
              ITEM_BLOCK_ID = BID; ITEM_SEED_ID = BID+1
              local hb = function(world) _update_heartbeat(world, WORKER_ID) end
              _update_heartbeat(W, WORKER_ID)
              HARVEST_UNTIL_EMPTY(W,D,SW,SD,{ITEM_BLOCK_ID,ITEM_SEED_ID}, hb)

              -- MARK_DONE hanya jika owner pindah ke kita (steal pada mode "stale")
              local rows = _read_lines(JOB_FILES.inprogress); local owner_now = nil
              for _,ll in ipairs(rows) do
                local ww,who = ll:match("^([^|]+)|([^|]+)|")
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
            -- idle actions
            if (STORAGE_CAKE or "") ~= "" and has_any_cake() then
              pcall(function()
                DROP_ITEMS_SNAKE(STORAGE_CAKE, DOOR_CAKE, cakeList,
                  {tile_cap=3000, stack_cap=20})
              end)
            end
            local b=getBot and getBot() or nil
            if b and b.leaveWorld then b:leaveWorld() end
            sleep(1000)
            if b then b.auto_reconnect = true end
            sleep(1200)
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
do
  ASSIGN_MODE=(ASSIGN_MODE or "rr"):lower():gsub("%s+",""); if ASSIGN_MODE~="rr" and ASSIGN_MODE~="chunk" then ASSIGN_MODE="rr" end
  print(string.format("[CONFIG] SLOT=%d | WORKER_ID=%s | USE_TXT_QUEUE=%s | ASSIST_MODE=%s | ASSIGN_MODE=%s",
    MY_SLOT, WORKER_ID, tostring(USE_TXT_QUEUE), ASSIST_MODE, ASSIGN_MODE))

  if USE_TXT_QUEUE then
    RUN_FROM_TXT_QUEUE()
  else
    local myList=build_worlds_for_bot(LIST_WORLD, MY_SLOT, TOTAL_BOTS, FARM_PER_BOT, ASSIGN_MODE)
    print(string.format("[CHECK] I am slot %d of %d (mode=%s)", MY_SLOT, TOTAL_BOTS, ASSIGN_MODE))
    if #myList==0 then print(string.format("[ASSIGN] SLOT %d tidak mendapat world. Cek TOTAL_BOTS/ASSIGN_MODE/ROTATE_LIST.", MY_SLOT))
    else
      print("[CHECK] Worlds assigned to me:"); for i,w in ipairs(myList) do print(string.format("  %02d) %s", i,w)) end
      RUN_MULTI_HARVEST(myList)
    end
  end
end

