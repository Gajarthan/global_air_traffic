# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_16:21:08_UTC-green)

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

**Latest saved flight:** 2026-08-15 16:21:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 16:21:08 UTC

- **198,972** saved flights
- **62,181** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,972** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,376,239.9 tonnes** estimated CO2 emissions
- **137,753,039 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7916 |
| 2 | SkyWest Airlines | 7121 |
| 3 | EJA | 3903 |
| 4 | IndiGo | 3442 |
| 5 | Southwest Airlines | 3075 |
| 6 | American Airlines | 3057 |
| 7 | ENY | 2455 |
| 8 | Delta Air Lines | 2354 |
| 9 | LATAM Airlines | 1875 |
| 10 | AZU | 1808 |
| 11 | Lufthansa | 1702 |
| 12 | Vueling | 1671 |
| 13 | WIF | 1639 |
| 14 | LXJ | 1576 |
| 15 | easyJet | 1367 |
| 16 | Swiss International | 1346 |
| 17 | AXM | 1307 |
| 18 | EJU | 1231 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1096 |
| 23 | GLO | 1082 |
| 24 | Air France | 1053 |
| 25 | PGT | 1048 |
| 26 | AEE | 1025 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1007 |
| 29 | WMT | 1005 |
| 30 | Wizz Air | 985 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168573 |
| 2 | 🇪🇸 ES | 12856 |
| 3 | 🇧🇷 BR | 11489 |
| 4 | 🇦🇺 AU | 11146 |
| 5 | 🇨🇦 CA | 10867 |
| 6 | 🇮🇳 IN | 10754 |
| 7 | 🇮🇹 IT | 10427 |
| 8 | 🇩🇪 DE | 9878 |
| 9 | 🇬🇧 GB | 9355 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7931 |
| 12 | 🇨🇴 CO | 7873 |
| 13 | 🇬🇷 GR | 5872 |
| 14 | 🇲🇽 MX | 5617 |
| 15 | 🇹🇷 TR | 5503 |
| 16 | 🇨🇭 CH | 5399 |
| 17 | 🇳🇴 NO | 5073 |
| 18 | 🇲🇾 MY | 3427 |
| 19 | 🇿🇦 ZA | 3364 |
| 20 | 🇵🇱 PL | 3292 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2546 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2111 |
| 27 | 🇲🇦 MA | 2015 |
| 28 | 🇳🇱 NL | 1791 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4130 |
| 2 | Denver International Airport |  | US | 3228 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2456 |
| 5 | Indira Gandhi International Airport |  | IN | 2438 |
| 6 | Harry Reid International Airport |  | US | 2270 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2105 |
| 8 | Zurich Airport |  | CH | 2105 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2057 |
| 10 | La Aurora Airport |  | GT | 1950 |
| 11 | El Dorado International Airport |  | CO | 1828 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1767 |
| 13 | Salt Lake City International Airport |  | US | 1765 |
| 14 | Chicago O'Hare International Airport |  | US | 1739 |
| 15 | Congonhas Airport |  | BR | 1682 |
| 16 | Frankfurt am Main International Airport |  | DE | 1676 |
| 17 | Madrid Barajas International Airport |  | ES | 1567 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1522 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1511 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1461 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1438 |
| 23 | Malpensa International Airport |  | IT | 1385 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 25 | Charles de Gaulle International Airport |  | FR | 1368 |
| 26 | Charlotte/Douglas International Airport |  | US | 1311 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1241 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1198 |
| 33 | Viracopos International Airport |  | BR | 1162 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1118 |
| 37 | Reno/Tahoe International Airport |  | US | 1117 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1099 |
| 40 | Tenerife Norte Airport |  | ES | 1090 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1012 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 363 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 336 | 27m | 275 km | 1,592.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 291 | 1h 49m | 1,423 km | 7,141.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 284 | 22m | 55 km | 269.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 242 | 1h 15m | 961 km | 4,011.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 237 | 1h 38m | 1,156 km | 4,728.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 215 | 1h 3m | 695 km | 2,577.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5721T |  | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-15 15:41 UTC | 2026-08-15 16:21 UTC | 39m |
| FHDSA | FHD | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-08-15 16:00 UTC | 2026-08-15 16:19 UTC | 19m |
| N252JM |  | North Perry Airport (KHWO) | Fort Lauderdale Executive Airport (KFXE) | 2026-08-15 15:41 UTC | 2026-08-15 16:16 UTC | 35m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-15 15:36 UTC | 2026-08-15 16:08 UTC | 31m |
| N474LE |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-08-15 15:22 UTC | 2026-08-15 15:58 UTC | 36m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-08-15 15:42 UTC | 2026-08-15 15:56 UTC | 14m |
| N327LX |  | Boire Field (KASH) | Westover Arb/Metro Airport (KCEF) | 2026-08-15 15:33 UTC | 2026-08-15 15:54 UTC | 20m |
| N447EA |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-08-15 15:52 UTC | 2026-08-15 15:52 UTC | 0m |
| OXF3867 | OXF | Cottonwood Airport (KP52) | Pleasant Valley Airstrip (24AZ) | 2026-08-15 14:55 UTC | 2026-08-15 15:50 UTC | 55m |
| N5229H |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-08-15 15:19 UTC | 2026-08-15 15:45 UTC | 25m |
| N8687N |  | Glendale Regional Airport (KGEU) | Massey Farm Airport (AZ34) | 2026-08-15 14:56 UTC | 2026-08-15 15:44 UTC | 48m |
| LXJ524 | LXJ | Dallas Love Field (KDAL) | Cisco Municipal Airport (K3F2) | 2026-08-15 15:20 UTC | 2026-08-15 15:44 UTC | 24m |
| AAL3301 | American Airlines | ME66 (ME66) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-15 12:20 UTC | 2026-08-15 15:42 UTC | 3h 22m |
| N895CA |  | Mesa Gateway Airport (KIWA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-15 15:26 UTC | 2026-08-15 15:42 UTC | 16m |
| N64364 |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-15 15:25 UTC | 2026-08-15 15:42 UTC | 16m |
| N714ER |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-15 15:24 UTC | 2026-08-15 15:40 UTC | 15m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-15 14:48 UTC | 2026-08-15 15:39 UTC | 51m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-15 14:53 UTC | 2026-08-15 15:37 UTC | 44m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-15 15:13 UTC | 2026-08-15 15:35 UTC | 22m |
| AIZ1843 | AIZ | Ben Gurion International Airport (LLBG) | Yotvata Airfield (LLYT) | 2026-08-15 15:08 UTC | 2026-08-15 15:35 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
