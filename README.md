# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_05:15:00_UTC-green)

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

**Latest saved flight:** 2026-08-13 05:15:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 05:15:00 UTC

- **191,417** saved flights
- **60,379** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,417** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,289,958.9 tonnes** estimated CO2 emissions
- **132,751,238 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7581 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3317 |
| 5 | Southwest Airlines | 2993 |
| 6 | American Airlines | 2973 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2254 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1661 |
| 12 | WIF | 1585 |
| 13 | Vueling | 1584 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1257 |
| 18 | EJU | 1179 |
| 19 | QLK | 1178 |
| 20 | All Nippon Airways | 1157 |
| 21 | Alaska Airlines | 1141 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 995 |
| 25 | PGT | 990 |
| 26 | CXK | 983 |
| 27 | AEE | 977 |
| 28 | United Airlines | 977 |
| 29 | WMT | 949 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163345 |
| 2 | 🇪🇸 ES | 12303 |
| 3 | 🇧🇷 BR | 11014 |
| 4 | 🇦🇺 AU | 10734 |
| 5 | 🇨🇦 CA | 10507 |
| 6 | 🇮🇳 IN | 10383 |
| 7 | 🇮🇹 IT | 9920 |
| 8 | 🇩🇪 DE | 9446 |
| 9 | 🇬🇧 GB | 8897 |
| 10 | 🇯🇵 JP | 7806 |
| 11 | 🇫🇷 FR | 7634 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5584 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5107 |
| 17 | 🇳🇴 NO | 4916 |
| 18 | 🇲🇾 MY | 3287 |
| 19 | 🇿🇦 ZA | 3214 |
| 20 | 🇵🇱 PL | 3158 |
| 21 | 🇹🇭 TH | 2952 |
| 22 | 🇳🇿 NZ | 2706 |
| 23 | 🇵🇭 PH | 2523 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2338 |
| 26 | 🇭🇷 HR | 1964 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1705 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇮🇩 ID | 1535 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3141 |
| 3 | Tokyo International Airport |  | JP | 2406 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2339 |
| 6 | Harry Reid International Airport |  | US | 2228 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2020 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1709 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1482 |
| 20 | Capua Airport |  | IT | 1481 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1415 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1335 |
| 24 | Malpensa International Airport |  | IT | 1319 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1277 |
| 27 | Kuala Lumpur International Airport |  | MY | 1230 |
| 28 | Bengaluru International Airport |  | IN | 1226 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 30 | Ninoy Aquino International Airport |  | PH | 1192 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1176 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1103 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1076 |
| 38 | Oslo Gardermoen Airport |  | NO | 1069 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 704 | 21m | 244 km | 2,964.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 464 | 1h 7m | 770 km | 6,163.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 443 | 24m | 225 km | 1,718.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 229 | 24m | 218 km | 862.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R20576 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-13 03:54 UTC | 2026-08-13 05:15 UTC | 1h 20m |
| JBU387 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Taos Regional Airport (KSKX) | 2026-08-13 01:02 UTC | 2026-08-13 05:05 UTC | 4h 3m |
| N907KC |  | Fullerton Municipal Airport (KFUL) | Meadows Field (KBFL) | 2026-08-13 03:29 UTC | 2026-08-13 05:03 UTC | 1h 34m |
| LBQ790 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Worcester Regional Airport (KORH) | 2026-08-13 04:01 UTC | 2026-08-13 05:01 UTC | 59m |
| FR140 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-13 04:44 UTC | 2026-08-13 04:57 UTC | 12m |
| N546MT |  | Kingman/Clyde Cessna Field (K9K8) | Cessna Acft Field (KCEA) | 2026-08-13 04:33 UTC | 2026-08-13 04:54 UTC | 21m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-13 04:40 UTC | 2026-08-13 04:52 UTC | 12m |
| VSV5333 | VSV | Phitsanulok Airport (VTPP) | Naypyidaw Airport (VYEL) | 2026-08-13 04:18 UTC | 2026-08-13 04:51 UTC | 33m |
| SFJ47 | SFJ | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-13 03:35 UTC | 2026-08-13 04:48 UTC | 1h 12m |
| PAL426 | Philippine Airlines | Ninoy Aquino International Airport (RPLL) | Iki Airport (RJDB) | 2026-08-13 01:48 UTC | 2026-08-13 04:45 UTC | 2h 57m |
| A6FHE |  | Zirku Airport (OMAZ) | Das Island Airport (OMAS) | 2026-08-13 04:31 UTC | 2026-08-13 04:40 UTC | 8m |
| N797GM |  | CA40 (CA40) | Lake Tahoe Airport (KTVL) | 2026-08-13 04:01 UTC | 2026-08-13 04:39 UTC | 37m |
| KAL2015 | Korean Air | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-08-13 01:34 UTC | 2026-08-13 04:37 UTC | 3h 3m |
| AEE352 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-13 04:16 UTC | 2026-08-13 04:37 UTC | 20m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-13 04:21 UTC | 2026-08-13 04:35 UTC | 13m |
| DAL1340 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Wilcox Airport (1MT9) | 2026-08-13 03:40 UTC | 2026-08-13 04:31 UTC | 51m |
| AIZ801 | AIZ | Ben Gurion International Airport (LLBG) | Yotvata Airfield (LLYT) | 2026-08-13 04:02 UTC | 2026-08-13 04:25 UTC | 22m |
| PGT52FR | PGT | Sabiha Gokcen International Airport (LTFJ) | Antalya International Airport (LTAI) | 2026-08-13 03:31 UTC | 2026-08-13 04:24 UTC | 52m |
| VT512 |  | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-08-13 03:32 UTC | 2026-08-13 04:23 UTC | 50m |
| QLK861D | QLK | Brisbane International Airport (YBBN) | Bunyan Airfield (YBUY) | 2026-08-13 02:26 UTC | 2026-08-13 04:19 UTC | 1h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
