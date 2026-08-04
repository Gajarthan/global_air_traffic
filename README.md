# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_23:17:01_UTC-green)

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

**Latest saved flight:** 2026-08-04 23:17:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 23:17:01 UTC

- **171,487** saved flights
- **55,800** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,487** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,067,723.8 tonnes** estimated CO2 emissions
- **119,868,047 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6827 |
| 2 | SkyWest Airlines | 6281 |
| 3 | EJA | 3411 |
| 4 | IndiGo | 3005 |
| 5 | Southwest Airlines | 2706 |
| 6 | American Airlines | 2703 |
| 7 | ENY | 2137 |
| 8 | Delta Air Lines | 2040 |
| 9 | LATAM Airlines | 1589 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1513 |
| 12 | WIF | 1433 |
| 13 | Vueling | 1407 |
| 14 | LXJ | 1343 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1167 |
| 17 | easyJet | 1155 |
| 18 | EJU | 1048 |
| 19 | Alaska Airlines | 1047 |
| 20 | QLK | 1045 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 945 |
| 23 | Cathay Pacific | 928 |
| 24 | CXK | 913 |
| 25 | GLO | 901 |
| 26 | United Airlines | 901 |
| 27 | AEE | 893 |
| 28 | Air France | 880 |
| 29 | MXY | 872 |
| 30 | JetBlue | 858 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 147946 |
| 2 | 🇪🇸 ES | 10980 |
| 3 | 🇧🇷 BR | 9763 |
| 4 | 🇦🇺 AU | 9551 |
| 5 | 🇮🇳 IN | 9417 |
| 6 | 🇨🇦 CA | 9370 |
| 7 | 🇮🇹 IT | 8867 |
| 8 | 🇩🇪 DE | 8510 |
| 9 | 🇬🇧 GB | 7944 |
| 10 | 🇯🇵 JP | 6872 |
| 11 | 🇫🇷 FR | 6794 |
| 12 | 🇨🇴 CO | 6255 |
| 13 | 🇬🇷 GR | 4979 |
| 14 | 🇲🇽 MX | 4914 |
| 15 | 🇨🇭 CH | 4500 |
| 16 | 🇳🇴 NO | 4469 |
| 17 | 🇹🇷 TR | 4183 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2876 |
| 20 | 🇿🇦 ZA | 2770 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2475 |
| 23 | 🇵🇭 PH | 2261 |
| 24 | 🇬🇹 GT | 2200 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1726 |
| 27 | 🇭🇷 HR | 1651 |
| 28 | 🇲🇪 ME | 1575 |
| 29 | 🇳🇱 NL | 1555 |
| 30 | 🇲🇴 MO | 1473 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3538 |
| 2 | Denver International Airport |  | US | 2841 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2124 |
| 5 | Indira Gandhi International Airport |  | IN | 2089 |
| 6 | Harry Reid International Airport |  | US | 2057 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1868 |
| 8 | Zurich Airport |  | CH | 1810 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1805 |
| 10 | La Aurora Airport |  | GT | 1698 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1584 |
| 12 | Chicago O'Hare International Airport |  | US | 1559 |
| 13 | El Dorado International Airport |  | CO | 1557 |
| 14 | Salt Lake City International Airport |  | US | 1537 |
| 15 | Frankfurt am Main International Airport |  | DE | 1529 |
| 16 | Macau International Airport |  | MO | 1473 |
| 17 | Congonhas Airport |  | BR | 1407 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1405 |
| 19 | Madrid Barajas International Airport |  | ES | 1342 |
| 20 | Capua Airport |  | IT | 1336 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1294 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1211 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1194 |
| 24 | Charlotte/Douglas International Airport |  | US | 1191 |
| 25 | Charles de Gaulle International Airport |  | FR | 1163 |
| 26 | Malpensa International Airport |  | IT | 1156 |
| 27 | Kuala Lumpur International Airport |  | MY | 1151 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1068 |
| 30 | Ninoy Aquino International Airport |  | PH | 1064 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1057 |
| 32 | Barcelona International Airport |  | ES | 1014 |
| 33 | Daniel K Inouye International Airport |  | US | 995 |
| 34 | Seattle-Tacoma International Airport |  | US | 993 |
| 35 | Viracopos International Airport |  | BR | 977 |
| 36 | Calgary International Airport |  | CA | 970 |
| 37 | Reno/Tahoe International Airport |  | US | 968 |
| 38 | Oslo Gardermoen Airport |  | NO | 954 |
| 39 | Tenerife Norte Airport |  | ES | 952 |
| 40 | Scottsdale Airport |  | US | 942 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 880 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 627 | 21m | 244 km | 2,640.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 256 | 44m | 241 km | 1,063.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 235 | 1h 47m | 1,423 km | 5,767.3 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 218 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 206 | 50m | 556 km | 1,974.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 204 | 1h 15m | 961 km | 3,381.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 199 | 31m | 369 km | 1,266.7 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 194 | 1h 38m | 1,156 km | 3,870.2 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 189 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| URSA10 | URS | Tolovana Hot Springs Airport (83AK) | Ladd Army Air Field (PAFB) | 2026-08-04 22:10 UTC | 2026-08-04 23:17 UTC | 1h 6m |
| N272FG |  | Malone Airport (NJ61) | Sky Manor Airport (KN40) | 2026-08-04 23:14 UTC | 2026-08-04 23:16 UTC | 1m |
| KING39 | KIN | Campbell Army Air Field (Fort Campbell) Airport (KHOP) | Campbell Army Air Field (Fort Campbell) Airport (KHOP) | 2026-08-04 22:48 UTC | 2026-08-04 23:11 UTC | 23m |
| TKR855 | TKR | Thunder Ridge Airpark (UT83) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-04 22:50 UTC | 2026-08-04 23:09 UTC | 19m |
| N400AY |  | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-08-04 22:32 UTC | 2026-08-04 23:04 UTC | 32m |
| N165PW |  | Billy Joe Airport (37CA) | San Bernardino International Airport (KSBD) | 2026-08-04 22:23 UTC | 2026-08-04 23:04 UTC | 41m |
| JUPITER | JUP | Madrid Air Base (SKMA) | German Olano Air Base (SKPQ) | 2026-08-04 22:57 UTC | 2026-08-04 22:57 UTC | 0m |
| N999VP |  | Vogen Airport (IS41) | Vogen Airport (IS41) | 2026-08-04 22:35 UTC | 2026-08-04 22:57 UTC | 21m |
| N375KR |  | Kenora Airport (CYQK) | Eveleth/Virginia Municipal Airport (KEVM) | 2026-08-04 22:32 UTC | 2026-08-04 22:54 UTC | 22m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-04 22:01 UTC | 2026-08-04 22:52 UTC | 51m |
| GLT720 | GLT | Spirit Of St Louis Airport (KSUS) | Easterwood Field (KCLL) | 2026-08-04 21:19 UTC | 2026-08-04 22:51 UTC | 1h 32m |
| N1308T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-04 20:07 UTC | 2026-08-04 22:50 UTC | 2h 42m |
| N989JW |  | Batten International Airport (KRAC) | Cable Union Airport (K3CU) | 2026-08-04 22:09 UTC | 2026-08-04 22:49 UTC | 39m |
| N566KB |  | Georgetown Executive Airport (KGTU) | Calhoun County Airport (K04M) | 2026-08-04 21:29 UTC | 2026-08-04 22:47 UTC | 1h 17m |
| N685DW |  | Orange Municipal Airport (KORE) | Concord Municipal Airport (KCON) | 2026-08-04 22:10 UTC | 2026-08-04 22:47 UTC | 37m |
| TKR138 | TKR | Ephrata Municipal Airport (KEPH) | Anderson Field (KS97) | 2026-08-04 22:34 UTC | 2026-08-04 22:46 UTC | 12m |
| AAL2476 | American Airlines | San Diego International Airport (KSAN) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-04 20:09 UTC | 2026-08-04 22:46 UTC | 2h 36m |
| RYR9438 | Ryanair | Malpensa International Airport (LIMC) | Otocac Airport (LDRO) | 2026-08-04 22:02 UTC | 2026-08-04 22:45 UTC | 43m |
| LR453 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-04 22:12 UTC | 2026-08-04 22:44 UTC | 32m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-04 22:02 UTC | 2026-08-04 22:43 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
