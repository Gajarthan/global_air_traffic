# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_17:24:32_UTC-green)

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

**Latest saved flight:** 2026-03-30 17:24:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 17:24:32 UTC

- **4,904** saved flights
- **3,433** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,904** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **62,434.7 tonnes** estimated CO2 emissions
- **3,619,404 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 237 |
| 2 | Ryanair | 181 |
| 3 | IndiGo | 133 |
| 4 | EJA | 105 |
| 5 | American Airlines | 89 |
| 6 | Southwest Airlines | 77 |
| 7 | Lufthansa | 74 |
| 8 | ENY | 73 |
| 9 | AXM | 58 |
| 10 | LATAM Airlines | 55 |
| 11 | Vueling | 52 |
| 12 | LXJ | 49 |
| 13 | Delta Air Lines | 44 |
| 14 | WIF | 40 |
| 15 | All Nippon Airways | 39 |
| 16 | Japan Airlines | 37 |
| 17 | Swiss International | 36 |
| 18 | VIV | 35 |
| 19 | Cathay Pacific | 34 |
| 20 | QLK | 33 |
| 21 | United Airlines | 33 |
| 22 | Avianca | 32 |
| 23 | AXB | 32 |
| 24 | AZU | 31 |
| 25 | EDV | 29 |
| 26 | EJU | 28 |
| 27 | VOE | 28 |
| 28 | Air France | 27 |
| 29 | Alaska Airlines | 26 |
| 30 | MXY | 26 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4168 |
| 2 | 🇮🇳 IN | 397 |
| 3 | 🇪🇸 ES | 378 |
| 4 | 🇦🇺 AU | 291 |
| 5 | 🇨🇴 CO | 263 |
| 6 | 🇯🇵 JP | 252 |
| 7 | 🇧🇷 BR | 242 |
| 8 | 🇮🇹 IT | 233 |
| 9 | 🇩🇪 DE | 226 |
| 10 | 🇨🇦 CA | 197 |
| 11 | 🇲🇽 MX | 176 |
| 12 | 🇬🇧 GB | 168 |
| 13 | 🇫🇷 FR | 157 |
| 14 | 🇲🇾 MY | 128 |
| 15 | 🇳🇴 NO | 127 |
| 16 | 🇿🇦 ZA | 123 |
| 17 | 🇨🇭 CH | 119 |
| 18 | 🇬🇹 GT | 116 |
| 19 | 🇵🇭 PH | 109 |
| 20 | 🇬🇷 GR | 105 |
| 21 | 🇹🇷 TR | 82 |
| 22 | 🇹🇭 TH | 72 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇵🇱 PL | 60 |
| 25 | 🇲🇦 MA | 59 |
| 26 | 🇲🇴 MO | 59 |
| 27 | 🇮🇩 ID | 58 |
| 28 | 🇧🇸 BS | 52 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇫🇮 FI | 47 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 125 |
| 2 | El Dorado International Airport |  | CO | 96 |
| 3 | Denver International Airport |  | US | 89 |
| 4 | Indira Gandhi International Airport |  | IN | 89 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 79 |
| 7 | Frankfurt am Main International Airport |  | DE | 72 |
| 8 | Zurich Airport |  | CH | 61 |
| 9 | Guaymaral Airport |  | CO | 60 |
| 10 | Macau International Airport |  | MO | 59 |
| 11 | Tenerife Norte Airport |  | ES | 58 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 56 |
| 13 | Harry Reid International Airport |  | US | 54 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 53 |
| 15 | Chicago O'Hare International Airport |  | US | 52 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 48 |
| 17 | Ninoy Aquino International Airport |  | PH | 48 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 19 | Kuala Lumpur International Airport |  | MY | 46 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 46 |
| 21 | Madrid Barajas International Airport |  | ES | 43 |
| 22 | Charles de Gaulle International Airport |  | FR | 43 |
| 23 | Bengaluru International Airport |  | IN | 43 |
| 24 | O. R. Tambo International Airport |  | ZA | 42 |
| 25 | Charlotte/Douglas International Airport |  | US | 40 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 40 |
| 27 | Miami International Airport |  | US | 38 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 29 | Reno/Tahoe International Airport |  | US | 37 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 36 |
| 31 | Vitoria/Foronda Airport |  | ES | 36 |
| 32 | Amsterdam Airport Schiphol |  | NL | 36 |
| 33 | Malpensa International Airport |  | IT | 36 |
| 34 | Centennial Airport |  | US | 36 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 35 |
| 36 | Los Angeles International Airport |  | US | 33 |
| 37 | Austin-Bergstrom International Airport |  | US | 33 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 33 |
| 39 | Congonhas Airport |  | BR | 33 |
| 40 | Salt Lake City International Airport |  | US | 33 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 24 | 28m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 20 | 27m | 152 km | 52.3 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 12 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 12 | 15m | 206 km | 42.7 t |
| 15 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 12 | 4m | - | - |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 11 | 29m | 275 km | 52.1 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 11 | 1h 55m | 1,156 km | 219.4 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 23 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N759UL |  | New Ulm Municipal Airport (KULM) | New Ulm Municipal Airport (KULM) | 2026-03-30 16:52 UTC | 2026-03-30 17:24 UTC | 32m |
| C6587 |  | Port Angeles Cgas Airport (KNOW) | Lawson Airpark (WN21) | 2026-03-30 16:42 UTC | 2026-03-30 17:23 UTC | 40m |
| DSU57 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-03-30 16:44 UTC | 2026-03-30 17:22 UTC | 37m |
| RIPPER1 | RIP | Ksa Orchards Airport (OK11) | Ksa Orchards Airport (OK11) | 2026-03-30 17:04 UTC | 2026-03-30 17:22 UTC | 17m |
| N479BC |  | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-03-30 16:52 UTC | 2026-03-30 17:20 UTC | 28m |
| CHH490 | CHH | Staroselye Airport (UUBK) | Sharypovo Airport (UNKO) | 2026-03-30 14:26 UTC | 2026-03-30 17:13 UTC | 2h 46m |
| ENRGY14 | ENR | Nellis Afb Airport (KLSV) | Nellis Afb Airport (KLSV) | 2026-03-30 16:21 UTC | 2026-03-30 17:12 UTC | 50m |
| BLZR213 | BLZ | Orange Grove Nalf Airport (KNOG) | TE63 (TE63) | 2026-03-30 16:52 UTC | 2026-03-30 17:09 UTC | 17m |
| N156U |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-03-30 16:35 UTC | 2026-03-30 17:09 UTC | 34m |
| EJA641 | EJA | 19TE (19TE) | Yampa Valley Airport (KHDN) | 2026-03-30 14:58 UTC | 2026-03-30 17:08 UTC | 2h 9m |
| N9725Q |  | Sky Acres Airport (K44N) | 0NK8 (0NK8) | 2026-03-30 16:51 UTC | 2026-03-30 17:07 UTC | 16m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-03-30 16:44 UTC | 2026-03-30 17:07 UTC | 22m |
| N733ES |  | Denton Enterprise Airport (KDTO) | Richards Airport (TA47) | 2026-03-30 16:53 UTC | 2026-03-30 17:06 UTC | 12m |
| TGCCC | TGC | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-03-30 16:27 UTC | 2026-03-30 16:58 UTC | 30m |
| N216CH |  | Valdez Pioneer Field (PAVD) | Valdez Pioneer Field (PAVD) | 2026-03-30 16:56 UTC | 2026-03-30 16:57 UTC | 0m |
| LFA334 | LFA | Orlando Sanford International Airport (KSFB) | Flying Dutchman Ranch Airport (FD29) | 2026-03-30 16:25 UTC | 2026-03-30 16:55 UTC | 30m |
| N270PM |  | K4R4 (K4R4) | K4R4 (K4R4) | 2026-03-30 16:51 UTC | 2026-03-30 16:55 UTC | 3m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-03-30 16:15 UTC | 2026-03-30 16:53 UTC | 38m |
| N172UZ |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-03-30 15:58 UTC | 2026-03-30 16:53 UTC | 55m |
| WMU92 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Claucherty Airport (MI35) | 2026-03-30 16:22 UTC | 2026-03-30 16:51 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
