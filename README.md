---========================== [[[ OHDEAR SCRIPT ]]] ==========================---

--------=========== BUYER SETTINGS ===========--------
DiscordID = "867849626072907776"    -- Put Your User Discord Here! (Ex : 4226705284830330)
Token = "qUMIBu3MuexO"              -- Put Your Token Here!

---===== FOLDER SETTINGS [NONTON SHOWCASE BIAR LEBIH PAHAM] =====---
worldPath = "C:/Users/Administrator/Desktop/ANDRE/List-World/"        -- Untuk Mengambil World Farm, Secondary Farm, Plant, Storage Pack, Seed, Special Item
extraFilePath = "C:/Users/Administrator/Desktop/ANDRE/Extra-File/"    -- Untuk Me-load Script yang diperlukan
PnbWorldPath = "C:/Users/Administrator/Desktop/ANDRE/List-PNB/"       -- Untuk Mengambil / Menyimpan World PNB Other Semua Bot
jsonPath = "C:/Users/Administrator/Desktop/ANDRE/JSON/"               -- Untuk Me-load/Save JSON File [NEW]

--------=========== MALADY SETTINGS ===========-------- 
AutoCure = true             -- If true, bot will automatically cure from Torn/Gem Malady
TalkTooMuch = false         -- If true, auto find Greemble / Chicken Maladies [Only Work if AutoCure true]
Custom_Malady = "All"       -- Choose Malady: Grumble / Chicken / All [it means Grumble+Chicken]
idVial = 8542               -- ID Item to use Vilevial, Bot will take vial Items on WorldTools
maladyTimeout = true        -- Apabila true, botnya akan menunggu sampai Malady Expired habis [10 Menit Kebawah]
MaxBotSurg = 3              -- Max Bot in World Surg/Station
SurgPrice = 3               -- How much price for Auto Surg Machine [Put High Price]
MinMaladyDuration = 300     -- Minimum Duration for Waiting Malady Expired [Make sure maladyTimeout is true]

--------=========== BOT SETTINGS ===========--------
JedaExe = 7000              -- Delay after Running Script > (Index Bot * Ms)
HW_Exit = true              -- If true, Bot will afk in EXIT when Hardwarp else afk with offline
JedaHW = 5                  -- Hard warp rest in X Minutes when Hardwarp
NewUpdate = true            -- If your bot does not require a minimum level requirement for farming!
Leveling = true            -- If true, bot will leveling with Secondary Farm else Leveling by Harvesting Main Farm
MoveRange = 7               -- Maximum Range for each findpath
MoveInterval = 120          -- Interval for each findpath
CollectInterval = 0         -- Interval for Auto Collect
ObjectCollectDelay = 0      -- Object Delay for Auto Collect
TargetLevel = 125           -- Bot Will Terminated when reached X level
SpamText = false            -- If true, bot will saying random text every harvesting, pnb, etc.
IgnoreGems = false          -- Bot will ignoring gems on farm World (Only Work for Soil Rotation)
IgnoreGems_PTHT = false     -- Bot will ignoring gems while Planting / Harvesting
TimeRelogBotMatung = 5     -- Bot will auto reconnect when AFK during X minutes
nextrandom = false          -- If true, Bot will join random world after each rotation
storagerandom = false       -- If true, Bot will join random world after drop pack/seed
delayrandomworld = 15000    -- Delay Warp
randomworld = {
    "BUYPARTYBOX", "SELLPARTYBOX"
}                               -- List of world to joining random world
WhiteList = {
    "Hamumu"
}                           -- Bot Didn't Banning Whitelist Name while doing PNB!

--------=========== PNB SETTINGS ===========--------
PutJammer = false            -- Bot will automatically buying Signal Jammer and Auto Place in PNB World
SetLevelWorld = 120         -- Bot will automatically set world level in PNB World
DurasiWorldPNB = 100        -- Auto Change PNB World when Limit Duration
TilePNB = 3                 -- (1 - 5)
nLettPNB = 12               -- How Much Letter Name for PNB World
PNBinFarm = true           -- PNB didalam Farm
CoordPNB = {
    x = 16,
    y = 1
}                           -- CUSTOM COORD PNB [BERLAKU UNTUK PNB IN FARM]

--------=========== MAIN FARM SETTINGS ===========--------
StopLooping = false         -- if True, bot will stopped after all Farm finished [NEW]
SeedID = 4585               -- Put your Seed ID Here
MainMinimumLevel = 12       -- Bot will leveling until reach X MainMinimumLevel [make sure NewUpdate is true] [NEW]
SisaTree = 3                -- Bot will next world if X Ready Harvest Tree or less 
PerBotWorldCount = 8       -- Farm each bot | it means every bot get 2 farming world
BersihkanFloat = true       -- Bot will take floating farmable in farm world
BotStart = {
    1,
    1,
}                           -- Write down the numbers from which world you want to start
JmlPenyusup = 3             -- Maximum Stranger in Farm, bot will do action if Random Ppl Entered the Farm
Exit = true                 -- If true, Bot Will Leave World for X Seconds [delaykabur]
delaykabur = 30000          -- How long bot waiting before go back to farm

--------=========== SECONDARY FARM SETTINGS ===========--------
SecondaryMinimumLevel = 7   -- Bot will Harvesting Secondary Farm until reach X SecondaryMinimumLevel [make sure NewUpdate and Leveling is true] [NEW]
MaxBotInFarm = 1            -- Limit Bot per Farm [Secondary Farm]
SecondarySeedID = 955       -- IDItem Seed for Leveling Bot

--------=========== TOOLS SETTINGS ===========--------
TakePickaxe = true              -- Bot will take pickaxe before farming and after leveling
PadamkanApi = false              -- If your farm get burn, the bot will take the firehose at WorldTools and then put out the fire
KillGhost = false               -- MEMBUTUHKAN NEUTRON POWER GLOVE [DROP KE WORLDTOOLS]

--------=========== EXTRA SETTINGS ===========--------
UrlToEditData = ""    -- You can set config without re-exe in this link! use http or https!
ControlViaDC = false                             -- Bot will be offline when u sending (!od off) in Insert Token Channel 
RestSchedule = false                            -- Istirahat Terjadwal
JadwalOff = {
    "04.20 - 10.00"
    -- "12.45 - 15.25",
    -- "01.15 - 02.45",
    -- "06.55 - 08.00"
}                                                 -- Masukkan Jam dan Menit On Offnya 
Rest_Settings = {
    enable = false,                              -- Bot will Resting if true
    interval = 120,                             -- Every 120 Minutes [2 Hours] the Bot will enter Rest Mode [Disconnect]
    rest = 10                                    -- The bot will rest for 5 minutes
}
AutoG4G = true                                  -- Auto Claim G4G apabila Poinnya mencukupi [Akan di cek secara berkala setiap membeli pack]
JedaBanwave = 10                                -- Apabila Status Bot berubah Menjadi "Banwave Detected", botnya akan Berhenti sejenak selama x Menit
Mods_List = {}--{"caitriona", "hamumu", "seth"}     -- Bot akan otomatis Offline selama Salah satu mods dari List masih Online
ModEntered = true                               -- If Status Mod Entered, All Bots will Disconnect              
JedaModEntered = 5                              -- Rest X Minutes if Mod Entered
MaxPlayerOnline = 100000 --80000                         -- Bot Will Disconnect if Players Online Reach X MaxPlayersOnline [Make it false or 0 if u dont needed]

--------=========== WEBHOOK SETTINGS ===========--------
SimplePinghook = true                                       -- If true, No more embeds on PingHook
UTC_Time = 7                                                -- Put your Timezone here
PingHook = "https://discord.com/api/webhooks/1383503120738287666/hb-dbsvaiYxY7QTORxxdkJyL7vwdef0x5JeLs8lgXv6A-7RsJfao6kqm_aAQkTuHc39V"       -- WebhookUrl for disconnected info, important, etc.
NukedHook = "https://discord.com/api/webhooks/1383503224476008498/NU9ZZFnwfMyntPRZPtBJ5GZ4wSTeWdYl8bL6O8ttXSacN8knIqgC5HxfbuhJRM-gaNo3"             -- WebhookUrl for Nuked Farm
WebhookPlant = "https://discord.com/api/webhooks/"          -- URL Webhook for Planting Info
AllBotHook = "https://discord.com/api/webhooks/1383502607892615201/oM00mS6eKWheOLuvSSe0fZb-z1_NtcsfpDAvTDllUiyPwtFrV1Dm6Tv7Vnn_2hyGa9Ce"            -- URL Webhook for All Bots Info
HookIDBot = "1383511692260020361"                                       -- id Message Webhook Info

PackHook = "https://discord.com/api/webhooks/1383503282261200988/xe1o8p0ST4ktasNtvUxVHf0Sd96Mg3VPhUS3IBjDnlNZTXrBSc81h9kRIlXFyCtq6ape"
HookIDPack = "1383503491074490472"
SeedHook = "https://discord.com/api/webhooks/1383503282261200988/xe1o8p0ST4ktasNtvUxVHf0Sd96Mg3VPhUS3IBjDnlNZTXrBSc81h9kRIlXFyCtq6ape"
HookIDSeed = "1383503604404584500"
SpecHook = "https://discord.com/api/webhooks/1383503538407080060/7T6kiScnCGI9iP6u8cFiBYMimiXAkjHfPGVUzalBP604d3euAVZ2L2Xpf7Nx28Lf4pl1"
HookIDSpec = "1383503830003486832"
ToolsHook = "https://discord.com/api/webhooks/1383503368328183840/X1mXO84TG7t9cKWgAhTButwx25wXMLgAEVTYWCklHWGV9_kcqdeKrCIjN4sFg1lELY63"
HookIDTools = "1383503752710848562"

--------=========== SEED SETTINGS ===========--------
setoran = 100                -- minimum seeds so that the bot drops the seeds into storage
AcuanSeed = 3               -- Target ID Foreground or Background for Drop Main Farm Seed
DropSecondarySeed = true    -- Bot will drop profitan secondary farm seeds into storage
AcuanSecondarySeed = 15     -- Target ID Foreground or Background for Drop Secondary Farm Seed
LanjutPlant = false         -- If true, Bot will planting profit seeds in (Plant.txt) else drop seed in storage

--------=========== PACK SETTINGS ===========--------
autobuypack = true              -- Automatically buying a pack
-- hargapack = 20000               -- Pack Price
-- MinGems = 20000             -- Minimum Gems for Buying Pack
-- namapack = "world_lock_10_pack" -- Pack Name
-- MinItemPack = 10                -- Bot will dropping the pack when he have X MinItemPack or more
-- iditempack = {242}              -- Put all your id item pack in here
hargapack = 1000               -- Pack Price
MinGems = 10000             -- Minimum Gems for Buying Pack
namapack = "ssp_10_pack" -- Pack Name
MinItemPack = 100                -- Bot will dropping the pack when he have X MinItemPack or more
iditempack = {5706}              -- Put all your id item pack in here
-- namapack = "summer_pack"
-- MinItemPack = 1
-- iditempack = {830,834,836,11044}
maxbuy = 10                      -- Bot will try to buying X times if have more gems
ID_AcuanDrop_Pack = 3           -- ID Foreground or Background for Drop Pack
-- ssp:ssp_10_pack:1000:5706
--------=========== EVENT SETTINGS ===========--------
SpecialItem = {}                -- Put all your id item special in here
minSpec = 30                    -- Bot will dropping the item when he have X minSpec or more
ID_AcuanDrop_Spec = 3           -- ID Foreground or Background for Drop Special Item

--------=========== EMOTICON SETTINGS ===========--------
Emoji = {
    Online = "<a:Onlen:1206807819370758204>",   -- Emoji for online status
    Offline = "<a:Oflen:1206807838996045844>",  -- Emoji for offline status
    Banned = "<a:warning:1270653635641999443>", -- Emoji for banned status
    Pack = "<:packcrate:1156971687062032394>",  -- Emoji for seed item
    Spec = "<a:arrow1:1346186032000929882>",    -- Emoji for Special Item
    Tools = "<:gpick:1091356094749757471>",     -- Emoji for Tools Hook
    Gems = "<:gems:1089014830561759345>",       -- Emoji for PNB/gem display
} -- [NEW]

--------=========== MORE SETTINGS ===========--------
DynamicDelay = true             -- Dynamic Delay for High Ping
DelayRecon = 20000              -- Interval Reconnecting
DelayBadServer = 120000         -- Interval Reconnecting if Server Issue / Bad Gateway
delayht = 150                   -- Interval Harvesting
delayplant = 150                -- Interval Planting
delaypnb = 175                  -- Interval Punch
delayplace = 115                -- Interval Place
delayworld = 5000               -- Interval Warping World
delaydrop = 1000                -- Interval Droping Item
delaytrash = 100                -- Interval Trashing Item
targettrash = 100               -- Auto trashing item when reach X target
target_block = 190              -- Bot Will doing pnb when reach X block
target_seed = 1                 -- Bot Will doing planting when reach X seed
DontTrash = {}                  -- Extra Whitelist item, bot doesn't trash ur item here. Include pick, pack, farmable, etc.
AbaikanTile = {12, 886}         -- Bot will ignoring tile while doing planting

--------=========== ENCRYPT SETTINGS ===========--------
extraFilePath = (extraFilePath or "C:/Users/Administrator/Desktop/Extra-File/"):gsub("[/\\]?$", "/")
extraFilePaths = extraFilePath .. "?.lua" -- [NEW]

function dofileCustom(fileName) -- [NEW]
    local filePath = extraFilePaths:gsub("?", fileName)  -- Ganti ? dengan nama file
    dofile(filePath)
end

dofileCustom("Main-Script") -- [NEW]
