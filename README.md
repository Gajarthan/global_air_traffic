# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_17:42:35_UTC-green)

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

**Latest saved flight:** 2026-08-05 17:42:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 17:42:35 UTC

- **172,667** saved flights
- **56,058** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **172,667** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,080,402.5 tonnes** estimated CO2 emissions
- **120,603,044 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6854 |
| 2 | SkyWest Airlines | 6310 |
| 3 | EJA | 3433 |
| 4 | IndiGo | 3030 |
| 5 | Southwest Airlines | 2720 |
| 6 | American Airlines | 2713 |
| 7 | ENY | 2150 |
| 8 | Delta Air Lines | 2046 |
| 9 | LATAM Airlines | 1594 |
| 10 | Lufthansa | 1573 |
| 11 | AZU | 1520 |
| 12 | WIF | 1443 |
| 13 | Vueling | 1424 |
| 14 | LXJ | 1349 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1176 |
| 17 | easyJet | 1167 |
| 18 | EJU | 1055 |
| 19 | QLK | 1055 |
| 20 | Alaska Airlines | 1051 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 950 |
| 23 | Cathay Pacific | 933 |
| 24 | CXK | 921 |
| 25 | GLO | 906 |
| 26 | United Airlines | 902 |
| 27 | AEE | 901 |
| 28 | Air France | 888 |
| 29 | MXY | 874 |
| 30 | JetBlue | 864 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 148743 |
| 2 | 🇪🇸 ES | 11063 |
| 3 | 🇧🇷 BR | 9812 |
| 4 | 🇦🇺 AU | 9643 |
| 5 | 🇮🇳 IN | 9499 |
| 6 | 🇨🇦 CA | 9455 |
| 7 | 🇮🇹 IT | 8918 |
| 8 | 🇩🇪 DE | 8576 |
| 9 | 🇬🇧 GB | 7995 |
| 10 | 🇯🇵 JP | 6937 |
| 11 | 🇫🇷 FR | 6855 |
| 12 | 🇨🇴 CO | 6332 |
| 13 | 🇬🇷 GR | 5022 |
| 14 | 🇲🇽 MX | 4942 |
| 15 | 🇨🇭 CH | 4555 |
| 16 | 🇳🇴 NO | 4495 |
| 17 | 🇹🇷 TR | 4230 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2887 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2531 |
| 22 | 🇳🇿 NZ | 2498 |
| 23 | 🇵🇭 PH | 2279 |
| 24 | 🇬🇹 GT | 2212 |
| 25 | 🇰🇷 KR | 2170 |
| 26 | 🇲🇦 MA | 1735 |
| 27 | 🇭🇷 HR | 1668 |
| 28 | 🇲🇪 ME | 1581 |
| 29 | 🇳🇱 NL | 1560 |
| 30 | 🇲🇴 MO | 1491 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3562 |
| 2 | Denver International Airport |  | US | 2854 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2149 |
| 5 | Indira Gandhi International Airport |  | IN | 2114 |
| 6 | Harry Reid International Airport |  | US | 2067 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1880 |
| 8 | Zurich Airport |  | CH | 1826 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1811 |
| 10 | La Aurora Airport |  | GT | 1706 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1592 |
| 12 | El Dorado International Airport |  | CO | 1565 |
| 13 | Chicago O'Hare International Airport |  | US | 1562 |
| 14 | Salt Lake City International Airport |  | US | 1545 |
| 15 | Frankfurt am Main International Airport |  | DE | 1535 |
| 16 | Macau International Airport |  | MO | 1491 |
| 17 | Congonhas Airport |  | BR | 1417 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1412 |
| 19 | Capua Airport |  | IT | 1347 |
| 20 | Madrid Barajas International Airport |  | ES | 1346 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1300 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1212 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1204 |
| 24 | Charlotte/Douglas International Airport |  | US | 1194 |
| 25 | Charles de Gaulle International Airport |  | FR | 1172 |
| 26 | Malpensa International Airport |  | IT | 1165 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Ninoy Aquino International Airport |  | PH | 1073 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1070 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1065 |
| 32 | Barcelona International Airport |  | ES | 1022 |
| 33 | Daniel K Inouye International Airport |  | US | 998 |
| 34 | Seattle-Tacoma International Airport |  | US | 995 |
| 35 | Viracopos International Airport |  | BR | 983 |
| 36 | Calgary International Airport |  | CA | 980 |
| 37 | Reno/Tahoe International Airport |  | US | 971 |
| 38 | Oslo Gardermoen Airport |  | NO | 960 |
| 39 | Tenerife Norte Airport |  | ES | 959 |
| 40 | Scottsdale Airport |  | US | 943 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 890 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 630 | 21m | 244 km | 2,652.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 259 | 44m | 241 km | 1,075.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 258 | 22m | 55 km | 245.2 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 220 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 207 | 50m | 556 km | 1,984.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 206 | 1h 15m | 961 km | 3,414.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 204 | 19m | 144 km | 507.4 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 198 | 1h 38m | 1,156 km | 3,950.0 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 194 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-05 17:29 UTC | 2026-08-05 17:42 UTC | 13m |
| N502BC |  | Eppley Airfield (KOMA) | Joe Foss Field (KFSD) | 2026-08-05 17:09 UTC | 2026-08-05 17:36 UTC | 27m |
| TMN21 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-08-05 08:29 UTC | 2026-08-05 17:35 UTC | 9h 6m |
| N60CM |  | Tyler Pounds Regional Airport (KTYR) | Higgins/Lipscomb County Airport (K1X1) | 2026-08-05 16:45 UTC | 2026-08-05 17:30 UTC | 45m |
| N708CF |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Storm Lake Municipal Airport (KSLB) | 2026-08-05 16:53 UTC | 2026-08-05 17:29 UTC | 36m |
| N451DS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-05 17:05 UTC | 2026-08-05 17:24 UTC | 18m |
|  |  | Tambau Airport (SSET) | Casa Branca Airport (SDKB) | 2026-08-05 17:16 UTC | 2026-08-05 17:24 UTC | 7m |
| NDU84 | NDU | Grand Forks International Airport (KGFK) | 7NA0 (7NA0) | 2026-08-05 16:42 UTC | 2026-08-05 17:23 UTC | 40m |
| N166WC |  | Boundary Bay Airport (CZBB) | Boeing Field/King County International Airport (KBFI) | 2026-08-05 16:56 UTC | 2026-08-05 17:22 UTC | 26m |
| N3262X |  | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-08-05 16:33 UTC | 2026-08-05 17:20 UTC | 46m |
| NWX330 | NWX | Bridgeport Municipal Airport (KXBP) | Bridgeport Municipal Airport (KXBP) | 2026-08-05 16:46 UTC | 2026-08-05 17:19 UTC | 32m |
| N9256C |  | Outlaw Field (KCKV) | Outlaw Field (KCKV) | 2026-08-05 16:24 UTC | 2026-08-05 17:18 UTC | 53m |
| N78603 |  | Beaufort Executive Airport (KARW) | Beaufort Executive Airport (KARW) | 2026-08-05 17:07 UTC | 2026-08-05 17:17 UTC | 9m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | KU77 (KU77) | 2026-08-05 16:55 UTC | 2026-08-05 17:16 UTC | 20m |
| XAZZZ | XAZ | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Chilpancingo Airport (MMCH) | 2026-08-05 16:57 UTC | 2026-08-05 17:16 UTC | 18m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | KU77 (KU77) | 2026-08-05 16:55 UTC | 2026-08-05 17:16 UTC | 20m |
| CGNBJ | CGN | CYKM (CYKM) | Wiarton Airport (CYVV) | 2026-08-05 16:52 UTC | 2026-08-05 17:14 UTC | 22m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-05 16:54 UTC | 2026-08-05 17:10 UTC | 15m |
| N78NA |  | Albuquerque International Sunport Airport (KABQ) | Ohkay Owingeh Airport (KE14) | 2026-08-05 15:54 UTC | 2026-08-05 17:08 UTC | 1h 13m |
| PRD19 | PRD | Lake City Gateway Airport (KLCQ) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-05 16:18 UTC | 2026-08-05 17:06 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
