# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_23:31:48_UTC-green)

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

**Latest saved flight:** 2026-03-29 23:31:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 23:31:48 UTC

- **3,585** saved flights
- **2,669** unique routes
- **99** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,585** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **47,028.6 tonnes** estimated CO2 emissions
- **2,726,294 km** total distance flown
- **897 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 202 |
| 2 | Ryanair | 124 |
| 3 | EJA | 88 |
| 4 | American Airlines | 81 |
| 5 | IndiGo | 80 |
| 6 | Southwest Airlines | 68 |
| 7 | ENY | 62 |
| 8 | Lufthansa | 53 |
| 9 | Delta Air Lines | 39 |
| 10 | LATAM Airlines | 39 |
| 11 | AXM | 38 |
| 12 | LXJ | 37 |
| 13 | Vueling | 36 |
| 14 | United Airlines | 32 |
| 15 | Cathay Pacific | 27 |
| 16 | VIV | 27 |
| 17 | Avianca | 26 |
| 18 | EDV | 25 |
| 19 | Swiss International | 22 |
| 20 | WIF | 22 |
| 21 | Alaska Airlines | 21 |
| 22 | QLK | 21 |
| 23 | All Nippon Airways | 20 |
| 24 | ARE | 20 |
| 25 | AXB | 19 |
| 26 | AZU | 19 |
| 27 | MXY | 19 |
| 28 | Japan Airlines | 18 |
| 29 | JIA | 18 |
| 30 | VOE | 18 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3336 |
| 2 | 🇪🇸 ES | 272 |
| 3 | 🇮🇳 IN | 224 |
| 4 | 🇨🇴 CO | 219 |
| 5 | 🇦🇺 AU | 187 |
| 6 | 🇧🇷 BR | 171 |
| 7 | 🇨🇦 CA | 161 |
| 8 | 🇩🇪 DE | 157 |
| 9 | 🇲🇽 MX | 148 |
| 10 | 🇮🇹 IT | 136 |
| 11 | 🇯🇵 JP | 134 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇬🇹 GT | 98 |
| 14 | 🇫🇷 FR | 93 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 74 |
| 18 | 🇵🇭 PH | 71 |
| 19 | 🇳🇴 NO | 69 |
| 20 | 🇬🇷 GR | 66 |
| 21 | 🇹🇷 TR | 48 |
| 22 | 🇧🇸 BS | 46 |
| 23 | 🇹🇭 TH | 45 |
| 24 | 🇳🇿 NZ | 43 |
| 25 | 🇵🇱 PL | 42 |
| 26 | 🇲🇴 MO | 40 |
| 27 | 🇲🇦 MA | 39 |
| 28 | 🇫🇮 FI | 38 |
| 29 | 🇮🇩 ID | 37 |
| 30 | 🇳🇱 NL | 32 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 102 |
| 2 | Denver International Airport |  | US | 79 |
| 3 | El Dorado International Airport |  | CO | 79 |
| 4 | La Aurora Airport |  | GT | 64 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Indira Gandhi International Airport |  | IN | 51 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 50 |
| 9 | Tenerife Norte Airport |  | ES | 49 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 48 |
| 11 | Harry Reid International Airport |  | US | 46 |
| 12 | Chicago O'Hare International Airport |  | US | 45 |
| 13 | Tokyo International Airport |  | JP | 44 |
| 14 | Macau International Airport |  | MO | 40 |
| 15 | Charlotte/Douglas International Airport |  | US | 38 |
| 16 | Zurich Airport |  | CH | 37 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 37 |
| 18 | Reno/Tahoe International Airport |  | US | 33 |
| 19 | Miami International Airport |  | US | 33 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 33 |
| 21 | Kuala Lumpur International Airport |  | MY | 33 |
| 22 | Ninoy Aquino International Airport |  | PH | 30 |
| 23 | O. R. Tambo International Airport |  | ZA | 30 |
| 24 | Madrid Barajas International Airport |  | ES | 29 |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 26 | Salt Lake City International Airport |  | US | 29 |
| 27 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 28 |
| 29 | Centennial Airport |  | US | 28 |
| 30 | Los Angeles International Airport |  | US | 27 |
| 31 | CO86 |  |  | 27 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 27 |
| 33 | Tampa International Airport |  | US | 27 |
| 34 | Vitoria/Foronda Airport |  | ES | 27 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 27 |
| 36 | Charles de Gaulle International Airport |  | FR | 25 |
| 37 | Perales Airport |  | CO | 25 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 39 | Amsterdam Airport Schiphol |  | NL | 25 |
| 40 | Austin-Bergstrom International Airport |  | US | 24 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 25 | 14m | 114 km | 49.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 15 | 23m | 225 km | 58.2 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 10 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 11 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 12 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 17 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 18 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 19 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 7 | 29m | 369 km | 44.6 t |
| 23 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 7 | 18m | 183 km | 22.1 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 25 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 7 | 8h 38m | 38 km | 4.6 t |
| 26 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 7 | 54m | 630 km | 76.0 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 28 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 7 | 4m | - | - |
| 29 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 6 | 1h 49m | - | - |
| 30 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG682 | BRG | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-03-29 23:16 UTC | 2026-03-29 23:31 UTC | 15m |
| N628SR |  | North Las Vegas Airport (KVGT) | Palo Alto Airport (KPAO) | 2026-03-29 22:01 UTC | 2026-03-29 23:31 UTC | 1h 30m |
| N724TT |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Santa Monica Municipal Airport (KSMO) | 2026-03-29 23:06 UTC | 2026-03-29 23:26 UTC | 19m |
| EXV | EXV | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-03-29 23:00 UTC | 2026-03-29 23:18 UTC | 17m |
| N808MT |  | Mc Alester Regional Airport (KMLC) | Mc Alester Regional Airport (KMLC) | 2026-03-29 23:07 UTC | 2026-03-29 23:17 UTC | 10m |
| KOJ | KOJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-29 22:38 UTC | 2026-03-29 23:14 UTC | 36m |
| CYO711 | CYO | Witham Field (KSUA) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-03-29 21:32 UTC | 2026-03-29 23:14 UTC | 1h 41m |
| N2221K |  | Rob Airport (95TS) | 69XA (69XA) | 2026-03-29 22:59 UTC | 2026-03-29 23:13 UTC | 13m |
| N269DD |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-03-29 23:02 UTC | 2026-03-29 23:12 UTC | 10m |
| TWY429 | TWY | Austin-Bergstrom International Airport (KAUS) | San Francisco International Airport (KSFO) | 2026-03-29 20:13 UTC | 2026-03-29 23:09 UTC | 2h 56m |
| JUMP3 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-03-29 22:56 UTC | 2026-03-29 23:08 UTC | 11m |
| VT585 |  | Faa'a International Airport (NTAA) | Kaukura Airport (NTGK) | 2026-03-29 22:17 UTC | 2026-03-29 23:06 UTC | 49m |
| PE993 |  | Cooma Snowy Mountains Airport (YCOM) | Cooma Snowy Mountains Airport (YCOM) | 2026-03-29 22:58 UTC | 2026-03-29 23:02 UTC | 3m |
| CFKSF | CFK | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-03-29 21:46 UTC | 2026-03-29 23:01 UTC | 1h 15m |
| N913JT |  | Dunlap Airpark (3TN4) | Tompkinsville/Monroe County Airport (KTZV) | 2026-03-29 22:39 UTC | 2026-03-29 23:00 UTC | 20m |
| CHILD1 | CHI | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-03-29 22:49 UTC | 2026-03-29 22:59 UTC | 10m |
| GTW184 | GTW | Spirit Of St Louis Airport (KSUS) | Z M Jack Stell Field (KCRT) | 2026-03-29 22:00 UTC | 2026-03-29 22:58 UTC | 58m |
| N713DH |  | Ocala International-Jim Taylor Field (KOCF) | James H Easom Field (KM23) | 2026-03-29 21:58 UTC | 2026-03-29 22:56 UTC | 58m |
| EJA907 | EJA | William P Hobby Airport (KHOU) | Napa County Airport (KAPC) | 2026-03-29 18:55 UTC | 2026-03-29 22:56 UTC | 4h 0m |
| CGPCN | CGP | Vancouver International Airport (CYVR) | Grand Forks Airport (CZGF) | 2026-03-29 22:10 UTC | 2026-03-29 22:53 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
