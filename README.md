# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_03:18:21_UTC-green)

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

**Latest saved flight:** 2026-07-30 03:18:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 03:18:21 UTC

- **159,759** saved flights
- **52,882** unique routes
- **137** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,759** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,917,374.3 tonnes** estimated CO2 emissions
- **111,152,135 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6402 |
| 2 | SkyWest Airlines | 5837 |
| 3 | EJA | 3175 |
| 4 | IndiGo | 2808 |
| 5 | American Airlines | 2529 |
| 6 | Southwest Airlines | 2511 |
| 7 | ENY | 1994 |
| 8 | Delta Air Lines | 1902 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1502 |
| 11 | AZU | 1409 |
| 12 | WIF | 1351 |
| 13 | Vueling | 1336 |
| 14 | LXJ | 1233 |
| 15 | AXM | 1115 |
| 16 | Swiss International | 1098 |
| 17 | easyJet | 1044 |
| 18 | Alaska Airlines | 1000 |
| 19 | All Nippon Airways | 987 |
| 20 | QLK | 987 |
| 21 | EJU | 976 |
| 22 | VIV | 877 |
| 23 | CXK | 847 |
| 24 | United Airlines | 845 |
| 25 | GLO | 842 |
| 26 | Cathay Pacific | 841 |
| 27 | AEE | 838 |
| 28 | MXY | 832 |
| 29 | Air France | 829 |
| 30 | JetBlue | 820 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138038 |
| 2 | 🇪🇸 ES | 10243 |
| 3 | 🇧🇷 BR | 9148 |
| 4 | 🇦🇺 AU | 9012 |
| 5 | 🇮🇳 IN | 8836 |
| 6 | 🇨🇦 CA | 8693 |
| 7 | 🇮🇹 IT | 8243 |
| 8 | 🇩🇪 DE | 8070 |
| 9 | 🇬🇧 GB | 7312 |
| 10 | 🇯🇵 JP | 6501 |
| 11 | 🇫🇷 FR | 6303 |
| 12 | 🇨🇴 CO | 5636 |
| 13 | 🇲🇽 MX | 4589 |
| 14 | 🇬🇷 GR | 4572 |
| 15 | 🇳🇴 NO | 4223 |
| 16 | 🇨🇭 CH | 4169 |
| 17 | 🇹🇷 TR | 3804 |
| 18 | 🇲🇾 MY | 2899 |
| 19 | 🇵🇱 PL | 2710 |
| 20 | 🇿🇦 ZA | 2573 |
| 21 | 🇳🇿 NZ | 2356 |
| 22 | 🇹🇭 TH | 2278 |
| 23 | 🇵🇭 PH | 2104 |
| 24 | 🇰🇷 KR | 2104 |
| 25 | 🇬🇹 GT | 2039 |
| 26 | 🇲🇦 MA | 1620 |
| 27 | 🇲🇪 ME | 1524 |
| 28 | 🇭🇷 HR | 1480 |
| 29 | 🇳🇱 NL | 1459 |
| 30 | 🇲🇴 MO | 1327 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3270 |
| 2 | Denver International Airport |  | US | 2662 |
| 3 | Tokyo International Airport |  | JP | 2055 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1967 |
| 6 | Harry Reid International Airport |  | US | 1948 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1768 |
| 8 | Zurich Airport |  | CH | 1705 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1682 |
| 10 | La Aurora Airport |  | GT | 1582 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1492 |
| 12 | El Dorado International Airport |  | CO | 1465 |
| 13 | Frankfurt am Main International Airport |  | DE | 1464 |
| 14 | Chicago O'Hare International Airport |  | US | 1448 |
| 15 | Salt Lake City International Airport |  | US | 1437 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1335 |
| 17 | Congonhas Airport |  | BR | 1327 |
| 18 | Macau International Airport |  | MO | 1327 |
| 19 | Madrid Barajas International Airport |  | ES | 1264 |
| 20 | Capua Airport |  | IT | 1257 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1229 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1139 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1137 |
| 24 | Charlotte/Douglas International Airport |  | US | 1122 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Bengaluru International Airport |  | IN | 1055 |
| 28 | Malpensa International Airport |  | IT | 1054 |
| 29 | Ninoy Aquino International Airport |  | PH | 986 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 974 |
| 32 | Barcelona International Airport |  | ES | 953 |
| 33 | Daniel K Inouye International Airport |  | US | 943 |
| 34 | Seattle-Tacoma International Airport |  | US | 934 |
| 35 | Calgary International Airport |  | CA | 921 |
| 36 | Viracopos International Airport |  | BR | 915 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 877 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 582 | 21m | 244 km | 2,450.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 381 | 24m | 225 km | 1,478.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 367 | 1h 9m | 770 km | 4,875.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 177 | 1h 1m | 695 km | 2,121.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSN3714 | China Southern | Quanzhou Airport (ZSQZ) | Guangzhou Baiyun International Airport (ZGGG) | 2026-07-30 02:18 UTC | 2026-07-30 03:18 UTC | 59m |
| N914UF |  | Holk Field At Foley Municipal Airport (K5R4) | Holk Field At Foley Municipal Airport (K5R4) | 2026-07-30 02:55 UTC | 2026-07-30 03:12 UTC | 16m |
| N3744Y |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Sacramento Executive Airport (KSAC) | 2026-07-30 02:21 UTC | 2026-07-30 03:09 UTC | 47m |
| PAT300 | PAT | Truckee-Tahoe Airport (KTRK) | Sacramento Mather Airport (KMHR) | 2026-07-30 01:04 UTC | 2026-07-30 03:05 UTC | 2h 0m |
| N854H |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | Regan Ranch Airport (6ID1) | 2026-07-30 02:43 UTC | 2026-07-30 03:02 UTC | 18m |
| AM317 |  | Melbourne Essendon Airport (YMEN) | Kyabram Airport (YKYB) | 2026-07-30 02:38 UTC | 2026-07-30 02:59 UTC | 20m |
| ETD870 | Etihad Airways | Al Bateen Executive Airport (OMAD) | Macau International Airport (VMMC) | 2026-07-29 19:43 UTC | 2026-07-30 02:58 UTC | 7h 15m |
| BCS21G | BCS | Leipzig Halle Airport (EDDP) | Amsterdam Airport Schiphol (EHAM) | 2026-07-30 01:53 UTC | 2026-07-30 02:54 UTC | 1h 1m |
| CCA103 | Air China | Tianjin Binhai International Airport (ZBTJ) | Zhuhai Airport (ZGSD) | 2026-07-30 00:23 UTC | 2026-07-30 02:52 UTC | 2h 29m |
| PJC35 | PJC | Cuyahoga County Airport (KCGF) | Teterboro Airport (KTEB) | 2026-07-30 01:51 UTC | 2026-07-30 02:52 UTC | 1h 1m |
| LBQ792 | LBQ | Syracuse Hancock International Airport (KSYR) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-30 02:33 UTC | 2026-07-30 02:51 UTC | 18m |
| SFJ45 | SFJ | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-07-30 01:39 UTC | 2026-07-30 02:51 UTC | 1h 12m |
| TKR132 | TKR | WA15 (WA15) | Anderson Field (KS97) | 2026-07-30 02:41 UTC | 2026-07-30 02:51 UTC | 10m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-07-30 01:20 UTC | 2026-07-30 02:50 UTC | 1h 29m |
| N65619 |  | Long Beach (Daugherty Field) Airport (KLGB) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-30 01:15 UTC | 2026-07-30 02:50 UTC | 1h 34m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-07-30 00:13 UTC | 2026-07-30 02:49 UTC | 2h 36m |
| N280WA |  | John Wayne/Orange County Airport (KSNA) | Scottsdale Airport (KSDL) | 2026-07-30 01:54 UTC | 2026-07-30 02:46 UTC | 51m |
| FSCN200 | FSC | Sydney Bankstown Airport (YSBK) | Cudal Airport (YCUA) | 2026-07-30 02:18 UTC | 2026-07-30 02:42 UTC | 24m |
|  |  | Southern Illinois Airport (KMDH) | Southern Illinois Airport (KMDH) | 2026-07-30 02:39 UTC | 2026-07-30 02:40 UTC | 0m |
| N912MN |  | Joe Foss Field (KFSD) | Parkston Municipal Airport (K8V3) | 2026-07-30 02:19 UTC | 2026-07-30 02:38 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
