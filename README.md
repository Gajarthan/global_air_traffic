# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_15:31:12_UTC-green)

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

**Latest saved flight:** 2026-07-25 15:31:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 15:31:12 UTC

- **150,226** saved flights
- **49,999** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,226** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,797,748.7 tonnes** estimated CO2 emissions
- **104,217,315 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6059 |
| 2 | SkyWest Airlines | 5481 |
| 3 | EJA | 2971 |
| 4 | IndiGo | 2685 |
| 5 | American Airlines | 2384 |
| 6 | Southwest Airlines | 2274 |
| 7 | ENY | 1867 |
| 8 | Delta Air Lines | 1767 |
| 9 | Lufthansa | 1473 |
| 10 | LATAM Airlines | 1384 |
| 11 | AZU | 1302 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1267 |
| 14 | LXJ | 1156 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1060 |
| 17 | easyJet | 974 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 917 |
| 22 | VIV | 831 |
| 23 | CXK | 808 |
| 24 | AEE | 792 |
| 25 | MXY | 784 |
| 26 | JetBlue | 783 |
| 27 | Air France | 782 |
| 28 | Cathay Pacific | 781 |
| 29 | GLO | 780 |
| 30 | United Airlines | 772 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129439 |
| 2 | 🇪🇸 ES | 9710 |
| 3 | 🇦🇺 AU | 8505 |
| 4 | 🇧🇷 BR | 8493 |
| 5 | 🇮🇳 IN | 8456 |
| 6 | 🇨🇦 CA | 8036 |
| 7 | 🇮🇹 IT | 7767 |
| 8 | 🇩🇪 DE | 7708 |
| 9 | 🇬🇧 GB | 6883 |
| 10 | 🇯🇵 JP | 6247 |
| 11 | 🇫🇷 FR | 5950 |
| 12 | 🇨🇴 CO | 5073 |
| 13 | 🇲🇽 MX | 4345 |
| 14 | 🇬🇷 GR | 4274 |
| 15 | 🇳🇴 NO | 3997 |
| 16 | 🇨🇭 CH | 3960 |
| 17 | 🇹🇷 TR | 3554 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2554 |
| 20 | 🇿🇦 ZA | 2452 |
| 21 | 🇳🇿 NZ | 2265 |
| 22 | 🇹🇭 TH | 2192 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1959 |
| 26 | 🇲🇦 MA | 1527 |
| 27 | 🇲🇪 ME | 1479 |
| 28 | 🇳🇱 NL | 1387 |
| 29 | 🇭🇷 HR | 1368 |
| 30 | 🇲🇴 MO | 1248 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3086 |
| 2 | Denver International Airport |  | US | 2516 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Indira Gandhi International Airport |  | IN | 1875 |
| 5 | Guaymaral Airport |  | CO | 1874 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1690 |
| 8 | Zurich Airport |  | CH | 1643 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1575 |
| 10 | La Aurora Airport |  | GT | 1517 |
| 11 | Frankfurt am Main International Airport |  | DE | 1420 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1406 |
| 13 | Chicago O'Hare International Airport |  | US | 1384 |
| 14 | Salt Lake City International Airport |  | US | 1349 |
| 15 | El Dorado International Airport |  | CO | 1349 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1287 |
| 17 | Macau International Airport |  | MO | 1248 |
| 18 | Congonhas Airport |  | BR | 1215 |
| 19 | Madrid Barajas International Airport |  | ES | 1196 |
| 20 | Capua Airport |  | IT | 1193 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1163 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1067 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1054 |
| 26 | Charles de Gaulle International Airport |  | FR | 1032 |
| 27 | Bengaluru International Airport |  | IN | 1009 |
| 28 | Malpensa International Airport |  | IT | 981 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 912 |
| 31 | Barcelona International Airport |  | ES | 902 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 899 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Tenerife Norte Airport |  | ES | 862 |
| 35 | Seattle-Tacoma International Airport |  | US | 861 |
| 36 | Calgary International Airport |  | CA | 855 |
| 37 | Viracopos International Airport |  | BR | 851 |
| 38 | Scottsdale Airport |  | US | 851 |
| 39 | Amsterdam Airport Schiphol |  | NL | 834 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 791 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 365 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 276 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 268 | 27m | 275 km | 1,269.9 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 224 | 22m | 55 km | 212.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 201 | 1h 47m | 1,423 km | 4,932.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 187 | 20m | 250 km | 807.7 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 177 | 1h 16m | 961 km | 2,933.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N280JB |  | Martens Airport (4MO8) | Mc Donnell Airport (03MU) | 2026-07-25 15:08 UTC | 2026-07-25 15:31 UTC | 22m |
| N358EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-25 14:13 UTC | 2026-07-25 15:25 UTC | 1h 12m |
| N3584S |  | Shafter-Minter Field (KMIT) | Meadows Field (KBFL) | 2026-07-25 14:54 UTC | 2026-07-25 15:25 UTC | 30m |
| DHTAF | DHT | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-07-25 15:13 UTC | 2026-07-25 15:22 UTC | 8m |
| N121UC |  | Pfeiffer Field (2OH7) | Clermont County Airport (KI69) | 2026-07-25 15:11 UTC | 2026-07-25 15:20 UTC | 9m |
| N731M |  | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-07-25 14:47 UTC | 2026-07-25 15:16 UTC | 28m |
| ECNKX | ECN | Castellón De La Plana Airport (LECN) | Castellón De La Plana Airport (LECN) | 2026-07-25 15:00 UTC | 2026-07-25 15:15 UTC | 15m |
| AFL801 | AFL | Antalya International Airport (LTAI) | Beslan Airport (URMO) | 2026-07-25 07:37 UTC | 2026-07-25 15:14 UTC | 7h 37m |
| N687CW |  | Ocean Reef Club Airport (07FA) | Miami Executive Airport (KTMB) | 2026-07-25 14:55 UTC | 2026-07-25 15:14 UTC | 18m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-07-25 15:00 UTC | 2026-07-25 15:13 UTC | 13m |
| N3855G |  | Lexington Airfield (TE75) | Lexington Airfield (TE75) | 2026-07-25 14:48 UTC | 2026-07-25 15:10 UTC | 21m |
| A6FNG |  | Fujairah International Airport (OMFJ) | Ras Al Khaimah International Airport (OMRK) | 2026-07-25 14:23 UTC | 2026-07-25 15:09 UTC | 45m |
| N466LP |  | Double Eagle Ii Airport (KAEG) | NM74 (NM74) | 2026-07-25 14:52 UTC | 2026-07-25 15:05 UTC | 13m |
| CXK160 | CXK | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-25 14:46 UTC | 2026-07-25 15:05 UTC | 19m |
| N906WD |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-07-25 14:46 UTC | 2026-07-25 15:04 UTC | 17m |
| N58FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-07-25 13:37 UTC | 2026-07-25 15:03 UTC | 1h 25m |
| VET430 | VET | Frederick Municipal Airport (KFDK) | Williamsport Airpark (SC86) | 2026-07-25 13:58 UTC | 2026-07-25 15:03 UTC | 1h 5m |
| HBKNL | HBK | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-07-25 14:54 UTC | 2026-07-25 15:01 UTC | 6m |
| N4117H |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-25 14:34 UTC | 2026-07-25 15:00 UTC | 25m |
| N993CB |  | Sacramento International Airport (KSMF) | Buchanan Field (KCCR) | 2026-07-25 14:42 UTC | 2026-07-25 14:58 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
