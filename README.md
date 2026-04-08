# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_20:42:38_UTC-green)

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

**Latest saved flight:** 2026-04-08 20:42:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 20:42:38 UTC

- **23,918** saved flights
- **11,605** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,918** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **295,853.9 tonnes** estimated CO2 emissions
- **17,150,952 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 994 |
| 2 | SkyWest Airlines | 993 |
| 3 | IndiGo | 665 |
| 4 | American Airlines | 435 |
| 5 | EJA | 435 |
| 6 | Southwest Airlines | 339 |
| 7 | ENY | 311 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 249 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 236 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 203 |
| 15 | LXJ | 194 |
| 16 | AZU | 188 |
| 17 | Swiss International | 174 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 161 |
| 21 | easyJet | 160 |
| 22 | EJU | 155 |
| 23 | AEE | 150 |
| 24 | WIF | 150 |
| 25 | United Airlines | 148 |
| 26 | Avianca | 142 |
| 27 | EDV | 139 |
| 28 | AXB | 138 |
| 29 | Air France | 125 |
| 30 | JetBlue | 122 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18689 |
| 2 | 🇮🇳 IN | 2027 |
| 3 | 🇪🇸 ES | 1828 |
| 4 | 🇦🇺 AU | 1750 |
| 5 | 🇯🇵 JP | 1349 |
| 6 | 🇧🇷 BR | 1329 |
| 7 | 🇩🇪 DE | 1225 |
| 8 | 🇮🇹 IT | 1224 |
| 9 | 🇨🇴 CO | 1222 |
| 10 | 🇨🇦 CA | 1084 |
| 11 | 🇬🇧 GB | 978 |
| 12 | 🇫🇷 FR | 887 |
| 13 | 🇲🇽 MX | 772 |
| 14 | 🇬🇷 GR | 688 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇿🇦 ZA | 516 |
| 18 | 🇳🇴 NO | 513 |
| 19 | 🇳🇿 NZ | 503 |
| 20 | 🇬🇹 GT | 476 |
| 21 | 🇹🇷 TR | 462 |
| 22 | 🇵🇭 PH | 449 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 390 |
| 25 | 🇵🇱 PL | 354 |
| 26 | 🇲🇦 MA | 292 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇲🇪 ME | 249 |
| 29 | 🇧🇸 BS | 248 |
| 30 | 🇳🇱 NL | 239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 565 |
| 2 | El Dorado International Airport |  | CO | 453 |
| 3 | Tokyo International Airport |  | JP | 448 |
| 4 | Denver International Airport |  | US | 417 |
| 5 | Indira Gandhi International Airport |  | IN | 417 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 335 |
| 7 | La Aurora Airport |  | GT | 328 |
| 8 | Harry Reid International Airport |  | US | 313 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Guaymaral Airport |  | CO | 253 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 249 |
| 13 | Chicago O'Hare International Airport |  | US | 248 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 247 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 16 | Macau International Airport |  | MO | 228 |
| 17 | Bengaluru International Airport |  | IN | 227 |
| 18 | Charlotte/Douglas International Airport |  | US | 222 |
| 19 | Kuala Lumpur International Airport |  | MY | 211 |
| 20 | Madrid Barajas International Airport |  | ES | 210 |
| 21 | Tenerife Norte Airport |  | ES | 209 |
| 22 | Ninoy Aquino International Airport |  | PH | 207 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 194 |
| 25 | Congonhas Airport |  | BR | 191 |
| 26 | Salt Lake City International Airport |  | US | 187 |
| 27 | Daniel K Inouye International Airport |  | US | 181 |
| 28 | Reno/Tahoe International Airport |  | US | 179 |
| 29 | Charles de Gaulle International Airport |  | FR | 174 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 165 |
| 32 | O. R. Tambo International Airport |  | ZA | 161 |
| 33 | Miami International Airport |  | US | 160 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 159 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 158 |
| 36 | Pune Airport |  | IN | 157 |
| 37 | Vitoria/Foronda Airport |  | ES | 154 |
| 38 | Barcelona International Airport |  | ES | 154 |
| 39 | Seattle-Tacoma International Airport |  | US | 151 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 141 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 98 | 14m | 114 km | 192.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 93 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 66 | 1h 42m | 1,156 km | 1,316.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 46 | 52m | 556 km | 440.9 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 41 | 1h 43m | 1,423 km | 1,006.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N365PC |  | Sanctuary Ranch Airport (7TS4) | Decatur Municipal Airport (KLUD) | 2026-04-08 20:32 UTC | 2026-04-08 20:42 UTC | 10m |
| N778TP |  | Richmond Executive/Chesterfield County Airport (KFCI) | Tri Cities Executive/Dinwiddie County Airport (KPTB) | 2026-04-08 19:38 UTC | 2026-04-08 20:40 UTC | 1h 1m |
| N721JD |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-04-08 19:38 UTC | 2026-04-08 20:39 UTC | 1h 1m |
| SLH386 | SLH | Washington Dulles International Airport (KIAD) | Lincoln Airport (KLNK) | 2026-04-08 18:05 UTC | 2026-04-08 20:39 UTC | 2h 34m |
| URSA10 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-08 19:37 UTC | 2026-04-08 20:38 UTC | 1h 1m |
| RANGR41 | RAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-04-08 20:12 UTC | 2026-04-08 20:38 UTC | 25m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-04-08 05:46 UTC | 2026-04-08 20:31 UTC | 14h 44m |
| ICAREZ8 | ICA | Landivisiau Air Base (LFRJ) | Landivisiau Air Base (LFRJ) | 2026-04-08 19:41 UTC | 2026-04-08 20:29 UTC | 48m |
| N143PM |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-04-08 19:35 UTC | 2026-04-08 20:29 UTC | 53m |
| N469FA |  | Allentown Queen City Municipal Airport (KXLL) | Allentown Queen City Municipal Airport (KXLL) | 2026-04-08 19:43 UTC | 2026-04-08 20:23 UTC | 39m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-08 20:06 UTC | 2026-04-08 20:20 UTC | 13m |
| WZZ3357 | Wizz Air | Tallinn Airport (EETN) | Warsaw Chopin Airport (EPWA) | 2026-04-08 19:39 UTC | 2026-04-08 20:19 UTC | 40m |
| N733JT |  | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Ocean City Municipal Airport (KOXB) | 2026-04-08 19:58 UTC | 2026-04-08 20:13 UTC | 15m |
| C2002 |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Upolu Airport (PHUP) | 2026-04-08 19:38 UTC | 2026-04-08 20:13 UTC | 34m |
| N5962P |  | Caldwell Executive Airport (KEUL) | High Valley Airport (ID35) | 2026-04-08 19:52 UTC | 2026-04-08 20:11 UTC | 19m |
| N714TA |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-04-08 19:53 UTC | 2026-04-08 20:09 UTC | 16m |
|  |  | Concord-Padgett Regional Airport (KJQF) | Concord-Padgett Regional Airport (KJQF) | 2026-04-08 20:06 UTC | 2026-04-08 20:09 UTC | 2m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-08 08:49 UTC | 2026-04-08 20:07 UTC | 11h 18m |
| EJA680 | EJA | Boise Air Trml/Gowen Field (KBOI) | Colonel James Jabara Airport (KAAO) | 2026-04-08 17:59 UTC | 2026-04-08 20:07 UTC | 2h 8m |
| N603DW |  | Dubuque Regional Airport (KDBQ) | James G Whiting Memorial Field (KMEY) | 2026-04-08 19:17 UTC | 2026-04-08 20:04 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
