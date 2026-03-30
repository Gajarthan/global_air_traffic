# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_20:17:21_UTC-green)

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

**Latest saved flight:** 2026-03-30 20:17:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 20:17:21 UTC

- **5,325** saved flights
- **3,666** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,325** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **67,558.8 tonnes** estimated CO2 emissions
- **3,916,454 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 271 |
| 2 | Ryanair | 203 |
| 3 | IndiGo | 136 |
| 4 | EJA | 119 |
| 5 | American Airlines | 104 |
| 6 | Southwest Airlines | 87 |
| 7 | ENY | 83 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 59 |
| 10 | AXM | 58 |
| 11 | LXJ | 53 |
| 12 | Vueling | 53 |
| 13 | Delta Air Lines | 50 |
| 14 | WIF | 42 |
| 15 | VIV | 40 |
| 16 | All Nippon Airways | 39 |
| 17 | United Airlines | 39 |
| 18 | Swiss International | 38 |
| 19 | Japan Airlines | 37 |
| 20 | Cathay Pacific | 36 |
| 21 | AZU | 35 |
| 22 | AXB | 34 |
| 23 | Avianca | 33 |
| 24 | EDV | 33 |
| 25 | QLK | 33 |
| 26 | Alaska Airlines | 31 |
| 27 | VOE | 31 |
| 28 | EJU | 30 |
| 29 | Air France | 27 |
| 30 | MXY | 27 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4671 |
| 2 | 🇮🇳 IN | 408 |
| 3 | 🇪🇸 ES | 399 |
| 4 | 🇦🇺 AU | 293 |
| 5 | 🇧🇷 BR | 271 |
| 6 | 🇨🇴 CO | 268 |
| 7 | 🇮🇹 IT | 255 |
| 8 | 🇯🇵 JP | 252 |
| 9 | 🇩🇪 DE | 240 |
| 10 | 🇨🇦 CA | 218 |
| 11 | 🇲🇽 MX | 190 |
| 12 | 🇬🇧 GB | 180 |
| 13 | 🇫🇷 FR | 169 |
| 14 | 🇳🇴 NO | 141 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇨🇭 CH | 124 |
| 17 | 🇿🇦 ZA | 123 |
| 18 | 🇬🇹 GT | 121 |
| 19 | 🇬🇷 GR | 115 |
| 20 | 🇵🇭 PH | 109 |
| 21 | 🇹🇷 TR | 86 |
| 22 | 🇹🇭 TH | 73 |
| 23 | 🇳🇿 NZ | 67 |
| 24 | 🇲🇦 MA | 65 |
| 25 | 🇵🇱 PL | 64 |
| 26 | 🇲🇴 MO | 62 |
| 27 | 🇮🇩 ID | 58 |
| 28 | 🇧🇸 BS | 57 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 49 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 138 |
| 2 | Denver International Airport |  | US | 102 |
| 3 | El Dorado International Airport |  | CO | 97 |
| 4 | Indira Gandhi International Airport |  | IN | 92 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 83 |
| 7 | Frankfurt am Main International Airport |  | DE | 79 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 68 |
| 9 | Zurich Airport |  | CH | 65 |
| 10 | Guaymaral Airport |  | CO | 63 |
| 11 | Chicago O'Hare International Airport |  | US | 62 |
| 12 | Tenerife Norte Airport |  | ES | 62 |
| 13 | Macau International Airport |  | MO | 62 |
| 14 | Harry Reid International Airport |  | US | 60 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 60 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 53 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 50 |
| 18 | Madrid Barajas International Airport |  | ES | 48 |
| 19 | Ninoy Aquino International Airport |  | PH | 48 |
| 20 | Reno/Tahoe International Airport |  | US | 47 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 22 | Kuala Lumpur International Airport |  | MY | 46 |
| 23 | Charlotte/Douglas International Airport |  | US | 45 |
| 24 | Bengaluru International Airport |  | IN | 45 |
| 25 | Miami International Airport |  | US | 43 |
| 26 | Charles de Gaulle International Airport |  | FR | 43 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 43 |
| 28 | Salt Lake City International Airport |  | US | 42 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 42 |
| 30 | O. R. Tambo International Airport |  | ZA | 42 |
| 31 | Malpensa International Airport |  | IT | 41 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 40 |
| 33 | Vitoria/Foronda Airport |  | ES | 38 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 35 | Centennial Airport |  | US | 38 |
| 36 | Los Angeles International Airport |  | US | 37 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 37 |
| 38 | Austin-Bergstrom International Airport |  | US | 36 |
| 39 | Amsterdam Airport Schiphol |  | NL | 36 |
| 40 | Congonhas Airport |  | BR | 36 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 14 | 1h 51m | 1,156 km | 279.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 13 | 15m | 206 km | 46.2 t |
| 12 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 14 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 16 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 13 | 4m | - | - |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 18 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 12 | 29m | 69 km | 14.3 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 11 | 1h 56m | 1,304 km | 247.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 9 | 1h 3m | 723 km | 112.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-03-30 05:54 UTC | 2026-03-30 20:17 UTC | 14h 22m |
| N8273A |  | Burlington/Alamance Regional Airport (KBUY) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-03-30 19:33 UTC | 2026-03-30 20:16 UTC | 43m |
| ASA867 | Alaska Airlines | Salt Lake City International Airport (KSLC) | Daniel K Inouye International Airport (PHNL) | 2026-03-30 13:30 UTC | 2026-03-30 20:12 UTC | 6h 42m |
| N984AA |  | San Marcos Regional Airport (KHYI) | Lockhart Municipal Airport (K50R) | 2026-03-30 19:22 UTC | 2026-03-30 20:04 UTC | 42m |
| N9258N |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-03-30 19:04 UTC | 2026-03-30 20:04 UTC | 1h 0m |
| HKC9496 | HKC | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-03-30 07:52 UTC | 2026-03-30 20:02 UTC | 12h 9m |
| CPA3485 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-03-30 05:27 UTC | 2026-03-30 20:01 UTC | 14h 34m |
| N54VM |  | Richmond Executive/Chesterfield County Airport (KFCI) | Witham Field (KSUA) | 2026-03-30 18:15 UTC | 2026-03-30 20:00 UTC | 1h 44m |
| N759UL |  | MY03 (MY03) | MY03 (MY03) | 2026-03-30 19:46 UTC | 2026-03-30 19:57 UTC | 10m |
| RYR94CC | Ryanair | Manchester Airport (EGCC) | Cewice Military Airport (EPCE) | 2026-03-30 18:10 UTC | 2026-03-30 19:51 UTC | 1h 41m |
| N291CB |  | Riverside Airport (KRAL) | Cable Airport (KCCB) | 2026-03-30 19:38 UTC | 2026-03-30 19:49 UTC | 11m |
| N578CF |  | Henderson Executive Airport (KHND) | Wendover Airport (KENV) | 2026-03-30 18:49 UTC | 2026-03-30 19:49 UTC | 1h 0m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-03-30 19:33 UTC | 2026-03-30 19:46 UTC | 12m |
| N716AT |  | Red Dog Airport (PADG) | Bob Baker Memorial Airport (PAIK) | 2026-03-30 19:14 UTC | 2026-03-30 19:46 UTC | 31m |
| 8M2 |  | Cessnock Airport (YCNK) | Walcha Airport (YWCH) | 2026-03-30 19:24 UTC | 2026-03-30 19:45 UTC | 21m |
| N9140Q |  | Crystal Airport (KMIC) | Redwood Falls Municipal Airport (KRWF) | 2026-03-30 19:10 UTC | 2026-03-30 19:44 UTC | 34m |
| N139PS |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-03-30 19:14 UTC | 2026-03-30 19:41 UTC | 27m |
| N546ND |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-03-30 18:51 UTC | 2026-03-30 19:39 UTC | 48m |
| LXJ323 | LXJ | Harry Reid International Airport (KLAS) | Addison Airport (KADS) | 2026-03-30 17:25 UTC | 2026-03-30 19:38 UTC | 2h 13m |
| JZA7985 | JZA | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-03-30 18:38 UTC | 2026-03-30 19:38 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
