# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_17:15:38_UTC-green)

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

**Latest saved flight:** 2026-03-31 17:15:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 17:15:38 UTC

- **6,992** saved flights
- **4,526** unique routes
- **106** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,992** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **87,983.6 tonnes** estimated CO2 emissions
- **5,100,500 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 324 |
| 2 | Ryanair | 268 |
| 3 | IndiGo | 194 |
| 4 | EJA | 139 |
| 5 | American Airlines | 130 |
| 6 | Lufthansa | 112 |
| 7 | Southwest Airlines | 107 |
| 8 | ENY | 97 |
| 9 | AXM | 78 |
| 10 | LATAM Airlines | 73 |
| 11 | Vueling | 72 |
| 12 | LXJ | 61 |
| 13 | Delta Air Lines | 59 |
| 14 | WIF | 58 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 50 |
| 19 | VIV | 50 |
| 20 | Cathay Pacific | 47 |
| 21 | Japan Airlines | 47 |
| 22 | United Airlines | 47 |
| 23 | AZU | 45 |
| 24 | EDV | 43 |
| 25 | Alaska Airlines | 42 |
| 26 | Avianca | 41 |
| 27 | AEE | 38 |
| 28 | EJU | 38 |
| 29 | Air India | 37 |
| 30 | BRC | 37 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5848 |
| 2 | 🇮🇳 IN | 591 |
| 3 | 🇪🇸 ES | 534 |
| 4 | 🇦🇺 AU | 508 |
| 5 | 🇩🇪 DE | 368 |
| 6 | 🇧🇷 BR | 346 |
| 7 | 🇯🇵 JP | 338 |
| 8 | 🇨🇴 CO | 327 |
| 9 | 🇮🇹 IT | 317 |
| 10 | 🇨🇦 CA | 292 |
| 11 | 🇲🇽 MX | 244 |
| 12 | 🇬🇧 GB | 243 |
| 13 | 🇫🇷 FR | 217 |
| 14 | 🇳🇴 NO | 190 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 170 |
| 17 | 🇨🇭 CH | 167 |
| 18 | 🇿🇦 ZA | 159 |
| 19 | 🇬🇹 GT | 148 |
| 20 | 🇵🇭 PH | 132 |
| 21 | 🇹🇷 TR | 122 |
| 22 | 🇳🇿 NZ | 122 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇮🇩 ID | 89 |
| 25 | 🇲🇦 MA | 89 |
| 26 | 🇵🇱 PL | 86 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇳🇱 NL | 68 |
| 30 | 🇲🇪 ME | 67 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 170 |
| 2 | Indira Gandhi International Airport |  | IN | 135 |
| 3 | Denver International Airport |  | US | 128 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 116 |
| 6 | Frankfurt am Main International Airport |  | DE | 111 |
| 7 | La Aurora Airport |  | GT | 102 |
| 8 | Harry Reid International Airport |  | US | 93 |
| 9 | Zurich Airport |  | CH | 87 |
| 10 | Macau International Airport |  | MO | 81 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 80 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 79 |
| 13 | Guaymaral Airport |  | CO | 79 |
| 14 | Chicago O'Hare International Airport |  | US | 78 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 75 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 17 | Tenerife Norte Airport |  | ES | 70 |
| 18 | Kuala Lumpur International Airport |  | MY | 65 |
| 19 | Madrid Barajas International Airport |  | ES | 64 |
| 20 | Bengaluru International Airport |  | IN | 64 |
| 21 | Reno/Tahoe International Airport |  | US | 63 |
| 22 | Ninoy Aquino International Airport |  | PH | 59 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 59 |
| 24 | Vitoria/Foronda Airport |  | ES | 54 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 26 | Malpensa International Airport |  | IT | 53 |
| 27 | Charlotte/Douglas International Airport |  | US | 53 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 53 |
| 29 | Charles de Gaulle International Airport |  | FR | 52 |
| 30 | Daniel K Inouye International Airport |  | US | 51 |
| 31 | Salt Lake City International Airport |  | US | 51 |
| 32 | Congonhas Airport |  | BR | 51 |
| 33 | Miami International Airport |  | US | 50 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 50 |
| 35 | Seattle-Tacoma International Airport |  | US | 47 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 47 |
| 37 | Pune Airport |  | IN | 46 |
| 38 | O. R. Tambo International Airport |  | ZA | 46 |
| 39 | Amsterdam Airport Schiphol |  | NL | 45 |
| 40 | Centennial Airport |  | US | 44 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 32 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 23 | 26m | 152 km | 60.1 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 20 | 1h 47m | 1,156 km | 399.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 20 | 4m | - | - |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 20 | 24m | 99 km | 34.3 t |
| 12 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 18 | 15m | 206 km | 64.0 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 18 | 28m | 275 km | 85.3 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 16 | 51m | 556 km | 153.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 21 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 13 | 22m | - | - |
| 27 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 13 | 8m | - | - |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N309HG |  | Space Coast Regional Airport (KTIX) | Bartow Executive Airport (KBOW) | 2026-03-31 16:40 UTC | 2026-03-31 17:15 UTC | 35m |
| SKW4338 | SkyWest Airlines | Detroit Metro Wayne County Airport (KDTW) | K8M8 (K8M8) | 2026-03-31 16:32 UTC | 2026-03-31 17:02 UTC | 30m |
| JEDI18 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Hawthorn Pines Airport (6AL6) | 2026-03-31 16:40 UTC | 2026-03-31 17:02 UTC | 21m |
| DUSTY10 | DUS | Grafenwohr Army Air Field (ETIC) | Vilseck Army Air Field (ETOI) | 2026-03-31 16:30 UTC | 2026-03-31 16:57 UTC | 27m |
| N111MP |  | KFTG (KFTG) | 68CO (68CO) | 2026-03-31 16:47 UTC | 2026-03-31 16:56 UTC | 8m |
| N176TA |  | Daniel K Inouye International Airport (PHNL) | Daniel K Inouye International Airport (PHNL) | 2026-03-31 16:54 UTC | 2026-03-31 16:54 UTC | 0m |
| N541LC |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-03-31 16:51 UTC | 2026-03-31 16:54 UTC | 2m |
| TZP2 | TZP | Narita International Airport (RJAA) | Wheeler Army Air Field (PHHI) | 2026-03-31 10:37 UTC | 2026-03-31 16:54 UTC | 6h 16m |
| UPS32 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Kawaihapai Airfield (PHDH) | 2026-03-31 08:19 UTC | 2026-03-31 16:54 UTC | 8h 34m |
| BRCAT20 | BRC | Roswell Air Center Airport (KROW) | Portales Municipal Airport (KPRZ) | 2026-03-31 16:39 UTC | 2026-03-31 16:54 UTC | 14m |
| N8274Q |  | Eagle Soaring Airport (1CD4) | Mesa 1 Airport (81CO) | 2026-03-31 16:22 UTC | 2026-03-31 16:53 UTC | 30m |
| BB165 |  | Chilton County Airport (K02A) | South Alabama Regional At Bill Benton Field (K79J) | 2026-03-31 16:22 UTC | 2026-03-31 16:50 UTC | 28m |
| N13232 |  | Westfield-Barnes Regional Airport (KBAF) | Hadley Airport (03MA) | 2026-03-31 16:36 UTC | 2026-03-31 16:50 UTC | 13m |
| GCONL | GCO | Fife Airport (EGPJ) | Cumbernauld Airport (EGPG) | 2026-03-31 16:32 UTC | 2026-03-31 16:48 UTC | 16m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-03-31 16:04 UTC | 2026-03-31 16:48 UTC | 43m |
| HOOK76 | HOO | Flysooner Field (OK50) | Barcus Field (95OK) | 2026-03-31 16:20 UTC | 2026-03-31 16:47 UTC | 27m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-31 16:31 UTC | 2026-03-31 16:45 UTC | 14m |
| SLOW69 | SLO | Enix Airport (OK51) | Tulsa International Airport (KTUL) | 2026-03-31 16:08 UTC | 2026-03-31 16:44 UTC | 35m |
| BOE977 | BOE | Boeing Field/King County International Airport (KBFI) | Quincy Flying Service Airport (WA74) | 2026-03-31 16:20 UTC | 2026-03-31 16:41 UTC | 21m |
| N852MA |  | Daniel K Inouye International Airport (PHNL) | Daniel K Inouye International Airport (PHNL) | 2026-03-31 16:19 UTC | 2026-03-31 16:40 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
