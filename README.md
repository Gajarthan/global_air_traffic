# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_21:52:34_UTC-green)

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

**Latest saved flight:** 2026-08-12 21:52:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 21:52:34 UTC

- **190,881** saved flights
- **60,246** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,881** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,284,881.4 tonnes** estimated CO2 emissions
- **132,456,892 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7576 |
| 2 | SkyWest Airlines | 6913 |
| 3 | EJA | 3773 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2983 |
| 6 | American Airlines | 2964 |
| 7 | ENY | 2365 |
| 8 | Delta Air Lines | 2243 |
| 9 | LATAM Airlines | 1790 |
| 10 | AZU | 1726 |
| 11 | Lufthansa | 1661 |
| 12 | WIF | 1584 |
| 13 | Vueling | 1583 |
| 14 | LXJ | 1497 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1179 |
| 19 | QLK | 1169 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1138 |
| 22 | VIV | 1052 |
| 23 | GLO | 1031 |
| 24 | Air France | 995 |
| 25 | PGT | 987 |
| 26 | CXK | 980 |
| 27 | United Airlines | 976 |
| 28 | AEE | 975 |
| 29 | WMT | 948 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162761 |
| 2 | 🇪🇸 ES | 12301 |
| 3 | 🇧🇷 BR | 10989 |
| 4 | 🇦🇺 AU | 10666 |
| 5 | 🇨🇦 CA | 10468 |
| 6 | 🇮🇳 IN | 10369 |
| 7 | 🇮🇹 IT | 9912 |
| 8 | 🇩🇪 DE | 9441 |
| 9 | 🇬🇧 GB | 8894 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7633 |
| 12 | 🇨🇴 CO | 7354 |
| 13 | 🇬🇷 GR | 5579 |
| 14 | 🇲🇽 MX | 5409 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5093 |
| 17 | 🇳🇴 NO | 4912 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3212 |
| 20 | 🇵🇱 PL | 3156 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2414 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1962 |
| 27 | 🇲🇦 MA | 1934 |
| 28 | 🇳🇱 NL | 1704 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3964 |
| 2 | Denver International Airport |  | US | 3134 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2225 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2018 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1978 |
| 10 | La Aurora Airport |  | GT | 1856 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1728 |
| 12 | El Dorado International Airport |  | CO | 1725 |
| 13 | Salt Lake City International Airport |  | US | 1697 |
| 14 | Chicago O'Hare International Airport |  | US | 1670 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1598 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | Capua Airport |  | IT | 1480 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1479 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1407 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1370 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1317 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1276 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1225 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1193 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1170 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1110 |
| 34 | Seattle-Tacoma International Airport |  | US | 1099 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1089 |
| 37 | Daniel K Inouye International Airport |  | US | 1071 |
| 38 | Oslo Gardermoen Airport |  | NO | 1067 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 699 | 21m | 244 km | 2,943.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 444 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 303 | 8m | - | - |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N871AE |  | Humphreys County Airport (K0M5) | John C Tune Airport (KJWN) | 2026-08-12 21:30 UTC | 2026-08-12 21:52 UTC | 21m |
| N3427M |  | Charles M Schulz/Sonoma County Airport (KSTS) | Hayward Executive Airport (KHWD) | 2026-08-12 20:56 UTC | 2026-08-12 21:49 UTC | 53m |
| N229MT |  | Stellar Airpark (KP19) | Casa Grande Municipal Airport (KCGZ) | 2026-08-12 21:31 UTC | 2026-08-12 21:47 UTC | 15m |
| N3956M |  | Waterbury-Oxford Airport (KOXC) | Mile Creek Airport (5CT7) | 2026-08-12 21:21 UTC | 2026-08-12 21:46 UTC | 24m |
| CFR652 | CFR | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-08-12 21:17 UTC | 2026-08-12 21:43 UTC | 25m |
| N93124 |  | Tacoma Narrows Airport (KTIW) | Tacoma Narrows Airport (KTIW) | 2026-08-12 21:25 UTC | 2026-08-12 21:41 UTC | 16m |
| UAE29N | Emirates | Dubai International Airport (OMDB) | Cairo International Airport (HECA) | 2026-08-12 18:21 UTC | 2026-08-12 21:40 UTC | 3h 19m |
| N8054S |  | Dream Team Airport (GA50) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-12 21:05 UTC | 2026-08-12 21:40 UTC | 35m |
| CXK237 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-08-12 20:31 UTC | 2026-08-12 21:35 UTC | 1h 3m |
| N32MK |  | Fort Lauderdale/Hollywood International Airport (KFLL) | Southern Oaks Airport (GE35) | 2026-08-12 18:56 UTC | 2026-08-12 21:33 UTC | 2h 37m |
| TSC377 | TSC | Amsterdam Airport Schiphol (EHAM) | Toronto Pearson International Airport (CYYZ) | 2026-08-12 13:37 UTC | 2026-08-12 21:32 UTC | 7h 54m |
| N46WY |  | Fort Lauderdale/Hollywood International Airport (KFLL) | Austin-Bergstrom International Airport (KAUS) | 2026-08-12 19:15 UTC | 2026-08-12 21:32 UTC | 2h 17m |
| BAW858V | British Airways | London Heathrow Airport (EGLL) | Kulmbach Airport (EDQK) | 2026-08-12 20:00 UTC | 2026-08-12 21:32 UTC | 1h 31m |
| BAW94DL | British Airways | London Heathrow Airport (EGLL) | Dinkelsbuhl-Sinbronn Airport (EDND) | 2026-08-12 20:03 UTC | 2026-08-12 21:32 UTC | 1h 28m |
| DLH4KW | Lufthansa | Frankfurt am Main International Airport (EDDF) | Seedorf Airport (EDXS) | 2026-08-12 20:33 UTC | 2026-08-12 21:32 UTC | 58m |
| DLH4T | Lufthansa | Munich International Airport (EDDM) | Karlovy Vary International Airport (LKKV) | 2026-08-12 20:44 UTC | 2026-08-12 21:32 UTC | 47m |
| EWG49BE | EWG | Beirut Rafic Hariri International Airport (OLBA) | Allstedt Airport (EDBT) | 2026-08-12 17:33 UTC | 2026-08-12 21:32 UTC | 3h 58m |
| EWG53G | EWG | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Meinerzhagen Airport (EDKZ) | 2026-08-12 19:57 UTC | 2026-08-12 21:32 UTC | 1h 34m |
| FHY1361 | FHY | Antalya International Airport (LTAI) | Hunsborn Airport (EDKH) | 2026-08-12 17:52 UTC | 2026-08-12 21:32 UTC | 3h 39m |
| SWT2SO | SWT | Sofia Airport (LBSF) | Ober-Morlen Airport (EDFP) | 2026-08-12 17:58 UTC | 2026-08-12 21:32 UTC | 3h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
