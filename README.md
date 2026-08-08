# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_23:00:48_UTC-green)

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

**Latest saved flight:** 2026-08-08 23:00:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 23:00:48 UTC

- **179,894** saved flights
- **57,666** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,894** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,162,522.9 tonnes** estimated CO2 emissions
- **125,363,644 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7126 |
| 2 | SkyWest Airlines | 6573 |
| 3 | EJA | 3546 |
| 4 | IndiGo | 3144 |
| 5 | Southwest Airlines | 2836 |
| 6 | American Airlines | 2812 |
| 7 | ENY | 2245 |
| 8 | Delta Air Lines | 2137 |
| 9 | LATAM Airlines | 1678 |
| 10 | AZU | 1611 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1487 |
| 14 | LXJ | 1406 |
| 15 | easyJet | 1228 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1211 |
| 18 | EJU | 1094 |
| 19 | QLK | 1093 |
| 20 | Alaska Airlines | 1091 |
| 21 | All Nippon Airways | 1088 |
| 22 | VIV | 993 |
| 23 | GLO | 963 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 936 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 903 |
| 30 | PGT | 895 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154383 |
| 2 | 🇪🇸 ES | 11553 |
| 3 | 🇧🇷 BR | 10334 |
| 4 | 🇦🇺 AU | 10075 |
| 5 | 🇮🇳 IN | 9857 |
| 6 | 🇨🇦 CA | 9828 |
| 7 | 🇮🇹 IT | 9283 |
| 8 | 🇩🇪 DE | 8894 |
| 9 | 🇬🇧 GB | 8305 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7152 |
| 12 | 🇨🇴 CO | 6701 |
| 13 | 🇬🇷 GR | 5242 |
| 14 | 🇲🇽 MX | 5152 |
| 15 | 🇨🇭 CH | 4789 |
| 16 | 🇳🇴 NO | 4645 |
| 17 | 🇹🇷 TR | 4579 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2366 |
| 24 | 🇬🇹 GT | 2292 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1816 |
| 27 | 🇭🇷 HR | 1792 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3724 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2222 |
| 5 | Indira Gandhi International Airport |  | IN | 2195 |
| 6 | Harry Reid International Airport |  | US | 2122 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1934 |
| 8 | Zurich Airport |  | CH | 1909 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1875 |
| 10 | La Aurora Airport |  | GT | 1761 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1646 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | El Dorado International Airport |  | CO | 1611 |
| 14 | Salt Lake City International Airport |  | US | 1610 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1498 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Madrid Barajas International Airport |  | ES | 1409 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1347 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1283 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1239 |
| 25 | Charlotte/Douglas International Airport |  | US | 1223 |
| 26 | Charles de Gaulle International Airport |  | FR | 1215 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1120 |
| 30 | Ninoy Aquino International Airport |  | PH | 1113 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1104 |
| 32 | Barcelona International Airport |  | ES | 1072 |
| 33 | Seattle-Tacoma International Airport |  | US | 1038 |
| 34 | Viracopos International Airport |  | BR | 1035 |
| 35 | Daniel K Inouye International Airport |  | US | 1033 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1028 |
| 38 | Oslo Gardermoen Airport |  | NO | 997 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 663 | 21m | 244 km | 2,791.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 217 | 1h 15m | 961 km | 3,596.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 215 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 207 | 31m | 369 km | 1,317.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 196 | 1h 2m | 695 km | 2,349.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-08 22:44 UTC | 2026-08-08 23:00 UTC | 16m |
| N51XP |  | Cricket Field (4WA2) | Chehalis-Centralia Airport (KCLS) | 2026-08-08 22:19 UTC | 2026-08-08 22:54 UTC | 34m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-08 22:31 UTC | 2026-08-08 22:48 UTC | 16m |
| 051465 |  | Longbell Ranch Airport (2CL3) | Redding Regional Airport (KRDD) | 2026-08-08 22:34 UTC | 2026-08-08 22:45 UTC | 11m |
| EJA330 | EJA | Centennial Airport (KAPA) | Mc Alester Regional Airport (KMLC) | 2026-08-08 21:17 UTC | 2026-08-08 22:43 UTC | 1h 25m |
| N6479G |  | Jeremiah Denton Airport (K4R9) | St Elmo Airport (K2R5) | 2026-08-08 22:14 UTC | 2026-08-08 22:40 UTC | 25m |
| N446BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-08 19:35 UTC | 2026-08-08 22:38 UTC | 3h 3m |
| SKW5846 | SkyWest Airlines | Hilltop Airport (98TE) | K9U4 (K9U4) | 2026-08-08 20:48 UTC | 2026-08-08 22:34 UTC | 1h 45m |
| BYF41 | BYF | San Carlos Airport (KSQL) | Hayward Executive Airport (KHWD) | 2026-08-08 21:30 UTC | 2026-08-08 22:31 UTC | 1h 1m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-08 22:24 UTC | 2026-08-08 22:31 UTC | 7m |
| TKR181 | TKR | Chico Regional Airport (KCIC) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-08 22:09 UTC | 2026-08-08 22:27 UTC | 18m |
| N874EB |  | Rogue Valley International/Medford Airport (KMFR) | Tracy Ranch Airport (ID88) | 2026-08-08 17:40 UTC | 2026-08-08 22:23 UTC | 4h 43m |
| PRDRV | PRD | Santos Dumont Airport (SBRJ) | Santos Dumont Airport (SBRJ) | 2026-08-08 22:18 UTC | 2026-08-08 22:22 UTC | 4m |
| N122KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-08 21:48 UTC | 2026-08-08 22:19 UTC | 30m |
| N636KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-08 21:46 UTC | 2026-08-08 22:17 UTC | 31m |
| N491LG |  | Tall Timber Airport (CD28) | Athanasiou Valley Airport (CO07) | 2026-08-08 21:59 UTC | 2026-08-08 22:17 UTC | 18m |
| AM320 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-08-08 21:51 UTC | 2026-08-08 22:16 UTC | 25m |
| N5383D |  | Santa Monica Municipal Airport (KSMO) | Whiteman Airport (KWHP) | 2026-08-08 20:53 UTC | 2026-08-08 22:16 UTC | 1h 22m |
| N929KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-08 21:44 UTC | 2026-08-08 22:15 UTC | 31m |
| N66MD |  | Westchester County Airport (KHPN) | Telluride Regional Airport (KTEX) | 2026-08-08 18:26 UTC | 2026-08-08 22:15 UTC | 3h 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
