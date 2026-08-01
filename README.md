# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_22:49:04_UTC-green)

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

**Latest saved flight:** 2026-08-01 22:49:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 22:49:04 UTC

- **165,754** saved flights
- **54,381** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,754** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,994,020.5 tonnes** estimated CO2 emissions
- **115,595,391 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6614 |
| 2 | SkyWest Airlines | 6051 |
| 3 | EJA | 3292 |
| 4 | IndiGo | 2912 |
| 5 | American Airlines | 2618 |
| 6 | Southwest Airlines | 2609 |
| 7 | ENY | 2065 |
| 8 | Delta Air Lines | 1980 |
| 9 | LATAM Airlines | 1546 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1453 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1368 |
| 14 | LXJ | 1288 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1134 |
| 17 | easyJet | 1093 |
| 18 | Alaska Airlines | 1023 |
| 19 | EJU | 1016 |
| 20 | QLK | 1012 |
| 21 | All Nippon Airways | 1009 |
| 22 | VIV | 914 |
| 23 | CXK | 886 |
| 24 | Cathay Pacific | 880 |
| 25 | United Airlines | 876 |
| 26 | AEE | 872 |
| 27 | GLO | 868 |
| 28 | Air France | 855 |
| 29 | MXY | 855 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143225 |
| 2 | 🇪🇸 ES | 10595 |
| 3 | 🇧🇷 BR | 9442 |
| 4 | 🇦🇺 AU | 9262 |
| 5 | 🇮🇳 IN | 9137 |
| 6 | 🇨🇦 CA | 9008 |
| 7 | 🇮🇹 IT | 8560 |
| 8 | 🇩🇪 DE | 8286 |
| 9 | 🇬🇧 GB | 7630 |
| 10 | 🇯🇵 JP | 6662 |
| 11 | 🇫🇷 FR | 6565 |
| 12 | 🇨🇴 CO | 5973 |
| 13 | 🇬🇷 GR | 4788 |
| 14 | 🇲🇽 MX | 4749 |
| 15 | 🇨🇭 CH | 4355 |
| 16 | 🇳🇴 NO | 4343 |
| 17 | 🇹🇷 TR | 3986 |
| 18 | 🇲🇾 MY | 2968 |
| 19 | 🇵🇱 PL | 2806 |
| 20 | 🇿🇦 ZA | 2695 |
| 21 | 🇳🇿 NZ | 2412 |
| 22 | 🇹🇭 TH | 2369 |
| 23 | 🇵🇭 PH | 2175 |
| 24 | 🇬🇹 GT | 2141 |
| 25 | 🇰🇷 KR | 2133 |
| 26 | 🇲🇦 MA | 1668 |
| 27 | 🇭🇷 HR | 1574 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1502 |
| 30 | 🇲🇴 MO | 1407 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3393 |
| 2 | Denver International Airport |  | US | 2761 |
| 3 | Tokyo International Airport |  | JP | 2096 |
| 4 | Guaymaral Airport |  | CO | 2081 |
| 5 | Indira Gandhi International Airport |  | IN | 2025 |
| 6 | Harry Reid International Airport |  | US | 2003 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1820 |
| 8 | Zurich Airport |  | CH | 1760 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1741 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1537 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Chicago O'Hare International Airport |  | US | 1499 |
| 14 | Frankfurt am Main International Airport |  | DE | 1499 |
| 15 | Salt Lake City International Airport |  | US | 1486 |
| 16 | Macau International Airport |  | MO | 1407 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1384 |
| 18 | Congonhas Airport |  | BR | 1369 |
| 19 | Madrid Barajas International Airport |  | ES | 1306 |
| 20 | Capua Airport |  | IT | 1296 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1263 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1172 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1164 |
| 24 | Charlotte/Douglas International Airport |  | US | 1161 |
| 25 | Charles de Gaulle International Airport |  | FR | 1131 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1108 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1023 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1020 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1016 |
| 32 | Barcelona International Airport |  | ES | 979 |
| 33 | Daniel K Inouye International Airport |  | US | 966 |
| 34 | Seattle-Tacoma International Airport |  | US | 963 |
| 35 | Calgary International Airport |  | CA | 943 |
| 36 | Viracopos International Airport |  | BR | 940 |
| 37 | Scottsdale Airport |  | US | 926 |
| 38 | Tenerife Norte Airport |  | ES | 923 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 915 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 604 | 21m | 244 km | 2,543.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 378 | 1h 9m | 770 km | 5,021.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 228 | 1h 47m | 1,423 km | 5,595.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 217 | 20m | 250 km | 937.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 208 | 31m | 49 km | 175.8 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 195 | 19m | 144 km | 485.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 178 | 24m | 218 km | 670.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RNGR721 | RNG | Calhoun County Airport (KPKV) | Gritz Field (XS46) | 2026-08-01 22:35 UTC | 2026-08-01 22:49 UTC | 13m |
| N311VA |  | Portsmouth International At Pease Airport (KPSM) | Salmon Falls Airport (ME61) | 2026-08-01 22:13 UTC | 2026-08-01 22:46 UTC | 33m |
| THY170 | Turkish Airlines | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-08-01 13:21 UTC | 2026-08-01 22:41 UTC | 9h 19m |
| N5415F |  | Houston Executive Airport (KTME) | Houston Executive Airport (KTME) | 2026-08-01 22:03 UTC | 2026-08-01 22:25 UTC | 22m |
| BRG590 | BRG | Selawik Airport (PASK) | Ambler Airport (PAFM) | 2026-08-01 21:42 UTC | 2026-08-01 22:23 UTC | 40m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-01 22:13 UTC | 2026-08-01 22:23 UTC | 10m |
| FILL31 | FIL | Wiley Post Airport (KPWA) | Sopwith Ldg Airport (OK56) | 2026-08-01 21:24 UTC | 2026-08-01 22:19 UTC | 55m |
| AAL836 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Chicago O'Hare International Airport (KORD) | 2026-08-01 20:14 UTC | 2026-08-01 22:18 UTC | 2h 3m |
| N727KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-01 21:41 UTC | 2026-08-01 22:12 UTC | 30m |
| N747V |  | Boulder Municipal Airport (KBDU) | Cedar Creek Ranch Airport (96WY) | 2026-08-01 16:12 UTC | 2026-08-01 22:12 UTC | 5h 59m |
| N18MG |  | Bryant Field (KO57) | Bryant Field (KO57) | 2026-08-01 21:31 UTC | 2026-08-01 22:10 UTC | 39m |
| MAFFS4 | MAF | Boise Air Trml/Gowen Field (KBOI) | Payette Municipal Airport (KS75) | 2026-08-01 21:58 UTC | 2026-08-01 22:10 UTC | 11m |
| N310WJ |  | Oasis Airpark (1ID4) | Coyote Run Airport (0ID3) | 2026-08-01 21:42 UTC | 2026-08-01 22:08 UTC | 26m |
| AEE6002 | AEE | Eleftherios Venizelos International Airport (LGAV) | Chania International Airport (LGSA) | 2026-08-01 21:39 UTC | 2026-08-01 22:08 UTC | 28m |
| ZKTET | ZKT | Ashburton Aerodrome (NZAS) | Rangiora Airfield (NZRT) | 2026-08-01 21:35 UTC | 2026-08-01 22:07 UTC | 32m |
| N85SG |  | Northwest Florida Beaches International Airport (KECP) | Boone County Airport (KHRO) | 2026-08-01 20:25 UTC | 2026-08-01 22:05 UTC | 1h 39m |
| N80945 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-01 21:23 UTC | 2026-08-01 22:04 UTC | 40m |
| N510PR |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-01 21:27 UTC | 2026-08-01 21:59 UTC | 32m |
| N21QU |  | Morgan County Airport (K42U) | Morgan County Airport (K42U) | 2026-08-01 20:27 UTC | 2026-08-01 21:58 UTC | 1h 30m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-08-01 11:15 UTC | 2026-08-01 21:57 UTC | 10h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
