# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_14:43:30_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-09-20 14:43:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 14:43:30 UTC

- **264,461** saved flights
- **78,023** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,461** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,205,616.6 tonnes** estimated CO2 emissions
- **185,832,848 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10468 |
| 2 | SkyWest Airlines | 9187 |
| 3 | EJA | 5137 |
| 4 | IndiGo | 4448 |
| 5 | American Airlines | 4133 |
| 6 | Southwest Airlines | 3889 |
| 7 | Delta Air Lines | 3293 |
| 8 | ENY | 3115 |
| 9 | LATAM Airlines | 2552 |
| 10 | AZU | 2490 |
| 11 | Vueling | 2221 |
| 12 | WIF | 2134 |
| 13 | LXJ | 2074 |
| 14 | Lufthansa | 2035 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1744 |
| 17 | QLK | 1708 |
| 18 | EJU | 1669 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1622 |
| 21 | Alaska Airlines | 1567 |
| 22 | All Nippon Airways | 1525 |
| 23 | WMT | 1488 |
| 24 | PGT | 1486 |
| 25 | GLO | 1475 |
| 26 | Air France | 1448 |
| 27 | VIV | 1444 |
| 28 | Wizz Air | 1435 |
| 29 | CXK | 1281 |
| 30 | AEE | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219657 |
| 2 | 🇪🇸 ES | 16656 |
| 3 | 🇧🇷 BR | 15490 |
| 4 | 🇦🇺 AU | 15145 |
| 5 | 🇨🇦 CA | 14718 |
| 6 | 🇮🇹 IT | 14395 |
| 7 | 🇮🇳 IN | 14070 |
| 8 | 🇩🇪 DE | 12768 |
| 9 | 🇬🇧 GB | 12272 |
| 10 | 🇨🇴 CO | 12008 |
| 11 | 🇫🇷 FR | 10564 |
| 12 | 🇯🇵 JP | 10226 |
| 13 | 🇹🇷 TR | 8014 |
| 14 | 🇬🇷 GR | 7669 |
| 15 | 🇲🇽 MX | 7272 |
| 16 | 🇨🇭 CH | 7061 |
| 17 | 🇳🇴 NO | 6531 |
| 18 | 🇹🇭 TH | 4749 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4357 |
| 22 | 🇳🇿 NZ | 3678 |
| 23 | 🇵🇭 PH | 3521 |
| 24 | 🇬🇹 GT | 3366 |
| 25 | 🇭🇷 HR | 3017 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2649 |
| 28 | 🇲🇪 ME | 2479 |
| 29 | 🇳🇱 NL | 2375 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5401 |
| 2 | Denver International Airport |  | US | 4277 |
| 3 | Indira Gandhi International Airport |  | IN | 3183 |
| 4 | Tokyo International Airport |  | JP | 3055 |
| 5 | El Dorado International Airport |  | CO | 2814 |
| 6 | Harry Reid International Airport |  | US | 2813 |
| 7 | Guaymaral Airport |  | CO | 2785 |
| 8 | Zurich Airport |  | CH | 2750 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2656 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2559 |
| 11 | La Aurora Airport |  | GT | 2557 |
| 12 | Salt Lake City International Airport |  | US | 2330 |
| 13 | Chicago O'Hare International Airport |  | US | 2270 |
| 14 | Congonhas Airport |  | BR | 2256 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2158 |
| 16 | Capua Airport |  | IT | 2069 |
| 17 | Madrid Barajas International Airport |  | ES | 2042 |
| 18 | Frankfurt am Main International Airport |  | DE | 2018 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2000 |
| 20 | Malpensa International Airport |  | IT | 1911 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1893 |
| 22 | Charles de Gaulle International Airport |  | FR | 1869 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1862 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1838 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1804 |
| 26 | Macau International Airport |  | MO | 1760 |
| 27 | Ninoy Aquino International Airport |  | PH | 1729 |
| 28 | Barcelona International Airport |  | ES | 1652 |
| 29 | Charlotte/Douglas International Airport |  | US | 1647 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1625 |
| 31 | Kuala Lumpur International Airport |  | MY | 1606 |
| 32 | Viracopos International Airport |  | BR | 1605 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1541 |
| 35 | Calgary International Airport |  | CA | 1507 |
| 36 | Don Mueang International Airport |  | TH | 1506 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1488 |
| 39 | Vancouver International Airport |  | CA | 1479 |
| 40 | Antalya International Airport |  | TR | 1418 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 989 | 21m | 244 km | 4,164.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 726 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 432 | 44m | 555 km | 4,136.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 379 | 24m | 218 km | 1,427.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 328 | 26m | 215 km | 1,214.8 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 327 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 286 | 42m | 535 km | 2,641.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 268 | 18m | 14 km | 67.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA689 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-09-20 13:39 UTC | 2026-09-20 14:43 UTC | 1h 3m |
| CXK598 | CXK | Arlington Municipal Airport (KGKY) | Arlington Municipal Airport (KGKY) | 2026-09-20 14:30 UTC | 2026-09-20 14:40 UTC | 10m |
| N967ND |  | Sarasota/Bradenton International Airport (KSRQ) | Albert Whitted Airport (KSPG) | 2026-09-20 14:13 UTC | 2026-09-20 14:40 UTC | 27m |
| CXK284 | CXK | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-20 12:19 UTC | 2026-09-20 14:38 UTC | 2h 18m |
| XBJMV | XBJ | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-09-20 13:56 UTC | 2026-09-20 14:35 UTC | 39m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-09-20 13:52 UTC | 2026-09-20 14:34 UTC | 41m |
| ICV762 | ICV | Chek Lap Kok International Airport (VHHH) | Malpensa International Airport (LIMC) | 2026-09-20 00:41 UTC | 2026-09-20 14:28 UTC | 13h 46m |
| N107MS |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-09-20 14:16 UTC | 2026-09-20 14:27 UTC | 10m |
| BB141 |  | Whiting Field Nas North Airport (KNSE) | Atmore Municipal Airport (K0R1) | 2026-09-20 13:55 UTC | 2026-09-20 14:24 UTC | 29m |
| THY3HJ | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-09-20 07:17 UTC | 2026-09-20 14:23 UTC | 7h 5m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-09-20 14:08 UTC | 2026-09-20 14:19 UTC | 10m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-09-20 06:41 UTC | 2026-09-20 14:18 UTC | 7h 37m |
| N360ES |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-20 13:47 UTC | 2026-09-20 14:15 UTC | 27m |
| N897LP |  | Mesquite Metro Airport (KHQZ) | Mesquite Metro Airport (KHQZ) | 2026-09-20 13:54 UTC | 2026-09-20 14:14 UTC | 20m |
| N831AF |  | Addison Airport (KADS) | Lz Mustang Airport (0TX8) | 2026-09-20 13:50 UTC | 2026-09-20 14:14 UTC | 23m |
| FJHLK | FJH | Tournus Cuisery Airport (LFFX) | Autun-Bellevue Airport (LFQF) | 2026-09-20 13:50 UTC | 2026-09-20 14:11 UTC | 21m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-09-20 13:48 UTC | 2026-09-20 14:10 UTC | 21m |
| VTMTW | VTM | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-20 12:31 UTC | 2026-09-20 14:09 UTC | 1h 38m |
| HB1875 |  | Amlikon Glider Airport (LSPA) | Amlikon Glider Airport (LSPA) | 2026-09-20 13:54 UTC | 2026-09-20 14:09 UTC | 14m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-09-20 13:49 UTC | 2026-09-20 14:08 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
