# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_14:10:03_UTC-green)

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

**Latest saved flight:** 2026-03-30 14:10:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 14:10:03 UTC

- **4,419** saved flights
- **3,134** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,419** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **57,821.3 tonnes** estimated CO2 emissions
- **3,351,959 km** total distance flown
- **889 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 215 |
| 2 | Ryanair | 158 |
| 3 | IndiGo | 119 |
| 4 | EJA | 95 |
| 5 | American Airlines | 85 |
| 6 | Southwest Airlines | 72 |
| 7 | Lufthansa | 66 |
| 8 | ENY | 64 |
| 9 | AXM | 57 |
| 10 | LATAM Airlines | 50 |
| 11 | Vueling | 47 |
| 12 | Delta Air Lines | 43 |
| 13 | All Nippon Airways | 39 |
| 14 | Japan Airlines | 37 |
| 15 | LXJ | 37 |
| 16 | Cathay Pacific | 33 |
| 17 | QLK | 33 |
| 18 | Swiss International | 33 |
| 19 | United Airlines | 33 |
| 20 | VIV | 32 |
| 21 | WIF | 32 |
| 22 | Avianca | 30 |
| 23 | AXB | 30 |
| 24 | AZU | 28 |
| 25 | EDV | 28 |
| 26 | VOE | 26 |
| 27 | Alaska Airlines | 25 |
| 28 | ARE | 23 |
| 29 | MXY | 22 |
| 30 | APG | 21 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3713 |
| 2 | 🇮🇳 IN | 356 |
| 3 | 🇪🇸 ES | 347 |
| 4 | 🇦🇺 AU | 289 |
| 5 | 🇯🇵 JP | 252 |
| 6 | 🇨🇴 CO | 247 |
| 7 | 🇧🇷 BR | 218 |
| 8 | 🇩🇪 DE | 202 |
| 9 | 🇮🇹 IT | 194 |
| 10 | 🇨🇦 CA | 169 |
| 11 | 🇲🇽 MX | 165 |
| 12 | 🇬🇧 GB | 154 |
| 13 | 🇫🇷 FR | 127 |
| 14 | 🇲🇾 MY | 126 |
| 15 | 🇿🇦 ZA | 113 |
| 16 | 🇨🇭 CH | 110 |
| 17 | 🇵🇭 PH | 107 |
| 18 | 🇳🇴 NO | 102 |
| 19 | 🇬🇹 GT | 100 |
| 20 | 🇬🇷 GR | 88 |
| 21 | 🇹🇷 TR | 73 |
| 22 | 🇹🇭 TH | 72 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇮🇩 ID | 58 |
| 25 | 🇲🇴 MO | 58 |
| 26 | 🇵🇱 PL | 53 |
| 27 | 🇰🇷 KR | 52 |
| 28 | 🇲🇦 MA | 50 |
| 29 | 🇧🇸 BS | 47 |
| 30 | 🇫🇮 FI | 45 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 112 |
| 2 | El Dorado International Airport |  | CO | 91 |
| 3 | Tokyo International Airport |  | JP | 85 |
| 4 | Indira Gandhi International Airport |  | IN | 82 |
| 5 | Denver International Airport |  | US | 81 |
| 6 | Frankfurt am Main International Airport |  | DE | 68 |
| 7 | La Aurora Airport |  | GT | 65 |
| 8 | Macau International Airport |  | MO | 58 |
| 9 | Tenerife Norte Airport |  | ES | 56 |
| 10 | Guaymaral Airport |  | CO | 56 |
| 11 | Zurich Airport |  | CH | 54 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 52 |
| 14 | Harry Reid International Airport |  | US | 51 |
| 15 | Ninoy Aquino International Airport |  | PH | 47 |
| 16 | Chicago O'Hare International Airport |  | US | 46 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 18 | Kuala Lumpur International Airport |  | MY | 45 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 42 |
| 20 | Madrid Barajas International Airport |  | ES | 41 |
| 21 | Eleftherios Venizelos International Airport |  | GR | 40 |
| 22 | O. R. Tambo International Airport |  | ZA | 39 |
| 23 | Charlotte/Douglas International Airport |  | US | 38 |
| 24 | Bengaluru International Airport |  | IN | 36 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 36 |
| 26 | Miami International Airport |  | US | 35 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 35 |
| 28 | Vitoria/Foronda Airport |  | ES | 34 |
| 29 | Centennial Airport |  | US | 34 |
| 30 | Reno/Tahoe International Airport |  | US | 33 |
| 31 | Charles de Gaulle International Airport |  | FR | 33 |
| 32 | Los Angeles International Airport |  | US | 32 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 32 |
| 34 | Malpensa International Airport |  | IT | 31 |
| 35 | Amsterdam Airport Schiphol |  | NL | 31 |
| 36 | Salt Lake City International Airport |  | US | 31 |
| 37 | Daniel K Inouye International Airport |  | US | 30 |
| 38 | Tampa International Airport |  | US | 30 |
| 39 | Don Mueang International Airport |  | TH | 29 |
| 40 | VGZR |  |  | 29 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 27 | 14m | 114 km | 53.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 22 | 27m | - | - |
| 4 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 14 | 1h 40m | 1,423 km | 343.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 9 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 11 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 13 | 21m | 165 km | 37.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 12 | 15m | 206 km | 42.7 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 18 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 20 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 21 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 22 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 10 | 8h 13m | 38 km | 6.5 t |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 10 | 4m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 9 | 1h 56m | 1,156 km | 179.5 t |
| 26 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 28 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 8 | 51m | 645 km | 89.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA393 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-30 07:10 UTC | 2026-03-30 14:10 UTC | 6h 59m |
| N32769 |  | Venice Municipal Airport (KVNC) | Venice Municipal Airport (KVNC) | 2026-03-30 13:11 UTC | 2026-03-30 14:06 UTC | 54m |
| N945RF |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-03-30 13:49 UTC | 2026-03-30 14:01 UTC | 11m |
| N87763 |  | Hawks Meadow Airport (07NC) | Sugar Valley Airport (5NC2) | 2026-03-30 13:40 UTC | 2026-03-30 13:55 UTC | 15m |
| PLZ5 | PLZ | Millinocket Municipal Airport (KMLT) | Bangor International Airport (KBGR) | 2026-03-30 13:20 UTC | 2026-03-30 13:49 UTC | 29m |
| N18ZD |  | Fort Morgan Municipal Airport (KFMM) | Moore County Airport (KDUX) | 2026-03-30 12:59 UTC | 2026-03-30 13:42 UTC | 42m |
| N471AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-03-30 13:22 UTC | 2026-03-30 13:38 UTC | 15m |
| N988BZ |  | Princeton Airport (K39N) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-03-30 12:56 UTC | 2026-03-30 13:37 UTC | 40m |
| N262AS |  | St Clair County International Airport (KPHN) | Ann Arbor Municipal Airport (KARB) | 2026-03-30 13:09 UTC | 2026-03-30 13:37 UTC | 27m |
| FIN1TJ | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-03-30 12:51 UTC | 2026-03-30 13:35 UTC | 43m |
| CTN344 | CTN | Busevec Velika Glider Airport (LDZB) | Visoko Sport Airfield (LQVI) | 2026-03-30 13:08 UTC | 2026-03-30 13:34 UTC | 25m |
| EVA159 | EVA Air | Incheon International Airport (RKSI) | Longtan Air Base (RCDI) | 2026-03-30 11:17 UTC | 2026-03-30 13:33 UTC | 2h 15m |
| N901JS |  | Arapahoe Municipal Airport (K37V) | Wilkens Airport (32KS) | 2026-03-30 13:03 UTC | 2026-03-30 13:31 UTC | 27m |
| ERU475 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-03-30 13:11 UTC | 2026-03-30 13:31 UTC | 19m |
| COOL11 | COO | Tularosa Airport (TA31) | Annandale Ranch Airport (2XS7) | 2026-03-30 13:17 UTC | 2026-03-30 13:28 UTC | 11m |
| N3517S |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-03-30 12:39 UTC | 2026-03-30 13:28 UTC | 48m |
| SWA2048 | Southwest Airlines | Dallas Love Field (KDAL) | 5TA4 (5TA4) | 2026-03-30 12:43 UTC | 2026-03-30 13:26 UTC | 42m |
| N720DR |  | Rocky Mountain Metro Airport (KBJC) | Rock & A Hard Place Ranch Airport (WY61) | 2026-03-30 12:38 UTC | 2026-03-30 13:25 UTC | 47m |
| RNGR755 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Whatley Flying Service Airport (8TA1) | 2026-03-30 13:02 UTC | 2026-03-30 13:24 UTC | 22m |
| N3957W |  | Albert Whitted Airport (KSPG) | Zephyrhills Municipal Airport (KZPH) | 2026-03-30 12:58 UTC | 2026-03-30 13:23 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
