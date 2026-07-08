# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_23:46:30_UTC-green)

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

**Latest saved flight:** 2026-07-07 23:46:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 23:46:30 UTC

- **132,621** saved flights
- **44,999** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,621** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,596,939.6 tonnes** estimated CO2 emissions
- **92,576,206 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5390 |
| 2 | SkyWest Airlines | 4906 |
| 3 | EJA | 2605 |
| 4 | IndiGo | 2470 |
| 5 | American Airlines | 2072 |
| 6 | Southwest Airlines | 2000 |
| 7 | ENY | 1669 |
| 8 | Delta Air Lines | 1589 |
| 9 | Lufthansa | 1379 |
| 10 | LATAM Airlines | 1223 |
| 11 | Vueling | 1163 |
| 12 | WIF | 1155 |
| 13 | AZU | 1126 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 941 |
| 17 | All Nippon Airways | 868 |
| 18 | easyJet | 846 |
| 19 | Alaska Airlines | 843 |
| 20 | QLK | 828 |
| 21 | EJU | 817 |
| 22 | VIV | 732 |
| 23 | AEE | 719 |
| 24 | Air France | 718 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 712 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 695 |
| 29 | MXY | 687 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113770 |
| 2 | 🇪🇸 ES | 8813 |
| 3 | 🇮🇳 IN | 7741 |
| 4 | 🇦🇺 AU | 7632 |
| 5 | 🇧🇷 BR | 7487 |
| 6 | 🇨🇦 CA | 7016 |
| 7 | 🇩🇪 DE | 6933 |
| 8 | 🇮🇹 IT | 6914 |
| 9 | 🇬🇧 GB | 5919 |
| 10 | 🇯🇵 JP | 5685 |
| 11 | 🇫🇷 FR | 5269 |
| 12 | 🇨🇴 CO | 4167 |
| 13 | 🇲🇽 MX | 3873 |
| 14 | 🇬🇷 GR | 3792 |
| 15 | 🇳🇴 NO | 3589 |
| 16 | 🇨🇭 CH | 3426 |
| 17 | 🇹🇷 TR | 2953 |
| 18 | 🇲🇾 MY | 2634 |
| 19 | 🇵🇱 PL | 2186 |
| 20 | 🇿🇦 ZA | 2181 |
| 21 | 🇳🇿 NZ | 2091 |
| 22 | 🇹🇭 TH | 2040 |
| 23 | 🇰🇷 KR | 1970 |
| 24 | 🇵🇭 PH | 1819 |
| 25 | 🇬🇹 GT | 1804 |
| 26 | 🇲🇦 MA | 1406 |
| 27 | 🇲🇪 ME | 1315 |
| 28 | 🇳🇱 NL | 1248 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1168 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2771 |
| 2 | Denver International Airport |  | US | 2249 |
| 3 | Tokyo International Airport |  | JP | 1865 |
| 4 | Indira Gandhi International Airport |  | IN | 1713 |
| 5 | Harry Reid International Airport |  | US | 1647 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1556 |
| 8 | Zurich Airport |  | CH | 1475 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1412 |
| 10 | La Aurora Airport |  | GT | 1394 |
| 11 | Frankfurt am Main International Airport |  | DE | 1336 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1278 |
| 13 | Chicago O'Hare International Airport |  | US | 1275 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1184 |
| 16 | Salt Lake City International Airport |  | US | 1180 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1144 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1087 |
| 19 | Madrid Barajas International Airport |  | ES | 1085 |
| 20 | Capua Airport |  | IT | 1083 |
| 21 | Congonhas Airport |  | BR | 1061 |
| 22 | Kuala Lumpur International Airport |  | MY | 1023 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 961 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 933 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 911 |
| 28 | Malpensa International Airport |  | IT | 881 |
| 29 | Ninoy Aquino International Airport |  | PH | 844 |
| 30 | Daniel K Inouye International Airport |  | US | 827 |
| 31 | Barcelona International Airport |  | ES | 817 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 810 |
| 33 | Tenerife Norte Airport |  | ES | 797 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 781 |
| 35 | Calgary International Airport |  | CA | 774 |
| 36 | Seattle-Tacoma International Airport |  | US | 764 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Viracopos International Airport |  | BR | 756 |
| 39 | Vitoria/Foronda Airport |  | ES | 755 |
| 40 | Amsterdam Airport Schiphol |  | NL | 750 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 480 | 21m | 244 km | 2,021.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 330 | 24m | 225 km | 1,280.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 183 | 20m | 99 km | 313.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 178 | 1h 46m | 1,423 km | 4,368.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFR72 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-07-07 22:12 UTC | 2026-07-07 23:46 UTC | 1h 34m |
| TKR133 | TKR | Redding Regional Airport (KRDD) | Fall River Mills Airport (KO89) | 2026-07-07 23:32 UTC | 2026-07-07 23:45 UTC | 12m |
| E82 |  | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-07 22:55 UTC | 2026-07-07 23:37 UTC | 41m |
| TKR104 | TKR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-07 23:07 UTC | 2026-07-07 23:31 UTC | 24m |
| HAWK258 | HAW | Kingsville Nas Airport (KNQI) | TE63 (TE63) | 2026-07-07 23:08 UTC | 2026-07-07 23:31 UTC | 22m |
| ES809 |  | Sacramento Mather Airport (KMHR) | Sacramento Executive Airport (KSAC) | 2026-07-07 22:08 UTC | 2026-07-07 23:31 UTC | 1h 22m |
| N172HG |  | Lewis University Airport (KLOT) | Neiner Airport (19LL) | 2026-07-07 22:59 UTC | 2026-07-07 23:29 UTC | 30m |
| ARCAT55 | ARC | Gillespie Field (KSEE) | Apple Valley Airport (KAPV) | 2026-07-07 23:00 UTC | 2026-07-07 23:25 UTC | 24m |
| CAP774 | CAP | Hagerstown Regional/Richard A Henson Field (KHGR) | Green Landings Airport (WV22) | 2026-07-07 23:18 UTC | 2026-07-07 23:24 UTC | 6m |
| N404PH |  | Hank Sasser/Breakaway Airport (40XS) | Bud Dryden Airport (TX05) | 2026-07-07 23:13 UTC | 2026-07-07 23:23 UTC | 9m |
| TKR131 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-07 22:48 UTC | 2026-07-07 23:22 UTC | 33m |
| N532LW |  | Truckee-Tahoe Airport (KTRK) | Robin Airport (59AZ) | 2026-07-07 22:02 UTC | 2026-07-07 23:20 UTC | 1h 18m |
| BURNY17 | BUR | 29TA (29TA) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-07-07 23:03 UTC | 2026-07-07 23:20 UTC | 16m |
| N3544W |  | 03IN (03IN) | Frankfort Clinton County Regional Airport (KFKR) | 2026-07-07 23:03 UTC | 2026-07-07 23:18 UTC | 15m |
| PWA62 | PWA | Napa County Airport (KAPC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-07 22:55 UTC | 2026-07-07 23:18 UTC | 22m |
| N58BN |  | Animas Air Park (K00C) | True Grit South Airport (CO95) | 2026-07-07 22:54 UTC | 2026-07-07 23:16 UTC | 21m |
| TKR41 | TKR | CD82 (CD82) | Animas Air Park (K00C) | 2026-07-07 22:50 UTC | 2026-07-07 23:15 UTC | 24m |
| WMT726 | WMT | Malmo Sturup Airport (ESMS) | Cemovsko Polje Airport (LYPO) | 2026-07-07 21:29 UTC | 2026-07-07 23:13 UTC | 1h 43m |
| N18MG |  | Rosaschi Air Park (KN59) | Dayton Valley Airpark (KA34) | 2026-07-07 22:55 UTC | 2026-07-07 23:11 UTC | 16m |
| FD471 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-07-07 22:40 UTC | 2026-07-07 23:09 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
