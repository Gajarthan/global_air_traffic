# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_00:46:11_UTC-green)

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

**Latest saved flight:** 2026-04-18 00:46:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 00:46:11 UTC

- **40,423** saved flights
- **17,243** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,423** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **486,804.2 tonnes** estimated CO2 emissions
- **28,220,532 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1692 |
| 2 | SkyWest Airlines | 1589 |
| 3 | IndiGo | 978 |
| 4 | EJA | 711 |
| 5 | American Airlines | 679 |
| 6 | Southwest Airlines | 569 |
| 7 | ENY | 523 |
| 8 | AXM | 414 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 398 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 360 |
| 13 | All Nippon Airways | 356 |
| 14 | Delta Air Lines | 346 |
| 15 | QLK | 332 |
| 16 | LXJ | 324 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 271 |
| 20 | AEE | 267 |
| 21 | easyJet | 264 |
| 22 | EJU | 262 |
| 23 | VIV | 262 |
| 24 | Japan Airlines | 241 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | Cathay Pacific | 205 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32182 |
| 2 | 🇮🇳 IN | 2984 |
| 3 | 🇪🇸 ES | 2980 |
| 4 | 🇦🇺 AU | 2825 |
| 5 | 🇧🇷 BR | 2402 |
| 6 | 🇯🇵 JP | 2161 |
| 7 | 🇮🇹 IT | 2099 |
| 8 | 🇩🇪 DE | 2018 |
| 9 | 🇨🇦 CA | 2008 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1641 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1281 |
| 14 | 🇬🇷 GR | 1204 |
| 15 | 🇨🇭 CH | 1100 |
| 16 | 🇲🇾 MY | 1005 |
| 17 | 🇳🇴 NO | 1005 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 823 |
| 20 | 🇵🇭 PH | 726 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 706 |
| 23 | 🇬🇹 GT | 688 |
| 24 | 🇰🇷 KR | 647 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 497 |
| 27 | 🇳🇱 NL | 405 |
| 28 | 🇲🇪 ME | 402 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 369 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 736 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 676 |
| 5 | Indira Gandhi International Airport |  | IN | 642 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 600 |
| 7 | Harry Reid International Airport |  | US | 522 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 508 |
| 10 | Zurich Airport |  | CH | 485 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 399 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 13 | Kuala Lumpur International Airport |  | MY | 395 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 385 |
| 16 | Macau International Airport |  | MO | 369 |
| 17 | Madrid Barajas International Airport |  | ES | 364 |
| 18 | Charlotte/Douglas International Airport |  | US | 358 |
| 19 | Tenerife Norte Airport |  | ES | 358 |
| 20 | Congonhas Airport |  | BR | 353 |
| 21 | Frankfurt am Main International Airport |  | DE | 351 |
| 22 | Bengaluru International Airport |  | IN | 348 |
| 23 | Ninoy Aquino International Airport |  | PH | 337 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 318 |
| 26 | Salt Lake City International Airport |  | US | 312 |
| 27 | Daniel K Inouye International Airport |  | US | 301 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 278 |
| 32 | Reno/Tahoe International Airport |  | US | 276 |
| 33 | Vitoria/Foronda Airport |  | ES | 276 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Calgary International Airport |  | CA | 247 |
| 39 | Viracopos International Airport |  | BR | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 184 | 1h 8m | 706 km | 2,240.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 142 | 24m | 225 km | 550.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 112 | 1h 27m | 910 km | 1,757.5 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 106 | 21m | 244 km | 446.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 80 | 44m | 452 km | 623.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 73 | 31m | 369 km | 464.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 64 | 52m | 556 km | 613.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N35597 |  | David Wayne Hooks Memorial Airport (KDWH) | Navasota Municipal Airport (K60R) | 2026-04-17 23:45 UTC | 2026-04-18 00:46 UTC | 1h 0m |
| RN184 |  | Stennis International Airport (KHSA) | Shade Tree Field (MS82) | 2026-04-18 00:25 UTC | 2026-04-18 00:37 UTC | 12m |
| PFT103 | PFT | Los Angeles International Airport (KLAX) | Henderson Executive Airport (KHND) | 2026-04-17 23:49 UTC | 2026-04-18 00:37 UTC | 48m |
| UUQ | UUQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-18 00:12 UTC | 2026-04-18 00:36 UTC | 24m |
| N2376G |  | Norman Grier Field (KS36) | Enumclaw Airport (WA77) | 2026-04-18 00:26 UTC | 2026-04-18 00:34 UTC | 7m |
| N3NJ |  | Hammonton Municipal Airport (KN81) | Trenton Mercer Airport (KTTN) | 2026-04-17 23:23 UTC | 2026-04-18 00:20 UTC | 57m |
| BULET56 | BUL | CA84 (CA84) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-18 00:08 UTC | 2026-04-18 00:20 UTC | 12m |
| TKR180 | TKR | Spokane International Airport (KGEG) | Spokane International Airport (KGEG) | 2026-04-17 23:47 UTC | 2026-04-18 00:19 UTC | 31m |
| HL5121 |  | Gimpo International Airport (RKSS) | G 712 Airport (RK60) | 2026-04-17 22:30 UTC | 2026-04-18 00:17 UTC | 1h 47m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-17 23:35 UTC | 2026-04-18 00:13 UTC | 37m |
| T73 |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-04-17 23:36 UTC | 2026-04-18 00:12 UTC | 36m |
| CFR85 | CFR | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-04-17 23:49 UTC | 2026-04-18 00:11 UTC | 22m |
| CFR70 | CFR | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-04-17 23:48 UTC | 2026-04-18 00:10 UTC | 21m |
| NLQ | NLQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-17 23:33 UTC | 2026-04-18 00:05 UTC | 31m |
| UUD | UUD | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-17 23:08 UTC | 2026-04-18 00:03 UTC | 54m |
| HR615 |  | Kadena Air Base (RODN) | Kadena Air Base (RODN) | 2026-04-17 23:57 UTC | 2026-04-18 00:02 UTC | 5m |
| N2065M |  | South Lakeland Airport (KX49) | South Lakeland Airport (KX49) | 2026-04-17 23:48 UTC | 2026-04-17 23:59 UTC | 11m |
| VOZ1851 | Virgin Australia | Perth International Airport (YPPH) | Kalgoorlie-Boulder Airport (YPKG) | 2026-04-17 23:08 UTC | 2026-04-17 23:58 UTC | 49m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-04-17 23:12 UTC | 2026-04-17 23:58 UTC | 45m |
| N402ER |  | AZ86 (AZ86) | AZ86 (AZ86) | 2026-04-17 23:53 UTC | 2026-04-17 23:57 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
