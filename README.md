# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_16:06:08_UTC-green)

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

**Latest saved flight:** 2026-03-31 16:06:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 16:06:08 UTC

- **6,828** saved flights
- **4,444** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,828** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **86,057.4 tonnes** estimated CO2 emissions
- **4,988,833 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 315 |
| 2 | Ryanair | 264 |
| 3 | IndiGo | 191 |
| 4 | EJA | 136 |
| 5 | American Airlines | 125 |
| 6 | Lufthansa | 110 |
| 7 | Southwest Airlines | 102 |
| 8 | ENY | 95 |
| 9 | AXM | 78 |
| 10 | LATAM Airlines | 73 |
| 11 | Vueling | 70 |
| 12 | LXJ | 60 |
| 13 | All Nippon Airways | 57 |
| 14 | Delta Air Lines | 57 |
| 15 | QLK | 56 |
| 16 | Swiss International | 55 |
| 17 | WIF | 55 |
| 18 | AXB | 50 |
| 19 | VIV | 49 |
| 20 | Cathay Pacific | 47 |
| 21 | Japan Airlines | 47 |
| 22 | United Airlines | 47 |
| 23 | AZU | 45 |
| 24 | EDV | 42 |
| 25 | Alaska Airlines | 40 |
| 26 | Avianca | 40 |
| 27 | EJU | 37 |
| 28 | VOE | 36 |
| 29 | AEE | 35 |
| 30 | easyJet | 35 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5673 |
| 2 | 🇮🇳 IN | 578 |
| 3 | 🇪🇸 ES | 524 |
| 4 | 🇦🇺 AU | 508 |
| 5 | 🇩🇪 DE | 360 |
| 6 | 🇧🇷 BR | 342 |
| 7 | 🇯🇵 JP | 337 |
| 8 | 🇨🇴 CO | 319 |
| 9 | 🇮🇹 IT | 312 |
| 10 | 🇨🇦 CA | 284 |
| 11 | 🇲🇽 MX | 238 |
| 12 | 🇬🇧 GB | 236 |
| 13 | 🇫🇷 FR | 213 |
| 14 | 🇳🇴 NO | 182 |
| 15 | 🇲🇾 MY | 176 |
| 16 | 🇨🇭 CH | 167 |
| 17 | 🇬🇷 GR | 162 |
| 18 | 🇿🇦 ZA | 159 |
| 19 | 🇬🇹 GT | 139 |
| 20 | 🇵🇭 PH | 132 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 118 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇮🇩 ID | 89 |
| 25 | 🇲🇦 MA | 87 |
| 26 | 🇵🇱 PL | 84 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇲🇪 ME | 67 |
| 30 | 🇳🇱 NL | 66 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 167 |
| 2 | Indira Gandhi International Airport |  | IN | 132 |
| 3 | Denver International Airport |  | US | 125 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 116 |
| 6 | Frankfurt am Main International Airport |  | DE | 110 |
| 7 | La Aurora Airport |  | GT | 95 |
| 8 | Zurich Airport |  | CH | 87 |
| 9 | Harry Reid International Airport |  | US | 85 |
| 10 | Macau International Airport |  | MO | 81 |
| 11 | Chicago O'Hare International Airport |  | US | 77 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 75 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 74 |
| 16 | Guaymaral Airport |  | CO | 73 |
| 17 | Tenerife Norte Airport |  | ES | 68 |
| 18 | Madrid Barajas International Airport |  | ES | 64 |
| 19 | Kuala Lumpur International Airport |  | MY | 64 |
| 20 | Bengaluru International Airport |  | IN | 63 |
| 21 | Reno/Tahoe International Airport |  | US | 61 |
| 22 | Ninoy Aquino International Airport |  | PH | 59 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 57 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 25 | Malpensa International Airport |  | IT | 53 |
| 26 | Charlotte/Douglas International Airport |  | US | 53 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 53 |
| 28 | Vitoria/Foronda Airport |  | ES | 52 |
| 29 | Charles de Gaulle International Airport |  | FR | 51 |
| 30 | Salt Lake City International Airport |  | US | 49 |
| 31 | Congonhas Airport |  | BR | 49 |
| 32 | Miami International Airport |  | US | 48 |
| 33 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 34 | O. R. Tambo International Airport |  | ZA | 46 |
| 35 | Amsterdam Airport Schiphol |  | NL | 45 |
| 36 | Pune Airport |  | IN | 45 |
| 37 | Daniel K Inouye International Airport |  | US | 44 |
| 38 | Seattle-Tacoma International Airport |  | US | 44 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 44 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 43 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 29 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 22 | 26m | 152 km | 57.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 20 | 24m | 99 km | 34.3 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 19 | 1h 48m | 1,156 km | 379.0 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 19 | 5m | - | - |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 18 | 28m | 275 km | 85.3 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 17 | 15m | 206 km | 60.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 15 | 51m | 556 km | 143.8 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 21 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 25 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 12 | 23m | - | - |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N204EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-03-31 15:23 UTC | 2026-03-31 16:06 UTC | 43m |
| N3466K |  | Flying J Airport (86TX) | Kestrel Airpark (K1T7) | 2026-03-31 15:44 UTC | 2026-03-31 16:05 UTC | 21m |
| TCF648 | TCF | FL56 (FL56) | Palm Beach International Airport (KPBI) | 2026-03-31 15:24 UTC | 2026-03-31 16:04 UTC | 39m |
| AEA57CN | AEA | Madrid Barajas International Airport (LEMD) | Frankfurt am Main International Airport (EDDF) | 2026-03-31 13:46 UTC | 2026-03-31 16:03 UTC | 2h 17m |
| N733GV |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-03-31 15:47 UTC | 2026-03-31 16:02 UTC | 15m |
| HOOK52 | HOO | 75OK (75OK) | Double W Airport (3OK7) | 2026-03-31 15:40 UTC | 2026-03-31 16:02 UTC | 22m |
| HAWK201 | HAW | Kingsville Nas Airport (KNQI) | Seven C's Ranch Airport (0XA4) | 2026-03-31 15:37 UTC | 2026-03-31 15:53 UTC | 16m |
| CGSGH | CGS | Avery County/Morrison Field (K7A8) | Avery County/Morrison Field (K7A8) | 2026-03-31 15:34 UTC | 2026-03-31 15:52 UTC | 17m |
| N4381L |  | Princeton Airport (K39N) | Sky Manor Airport (KN40) | 2026-03-31 15:09 UTC | 2026-03-31 15:51 UTC | 42m |
| N486CB |  | Chino Airport (KCNO) | Riverside Airport (KRAL) | 2026-03-31 15:35 UTC | 2026-03-31 15:49 UTC | 13m |
| V8MHB |  | Hamburg Airport (EDDH) | Hamburg Airport (EDDH) | 2026-03-31 12:43 UTC | 2026-03-31 15:48 UTC | 3h 5m |
| VLG3YP | Vueling | Barcelona International Airport (LEBL) | Son Bonet Airport (LESB) | 2026-03-31 15:26 UTC | 2026-03-31 15:48 UTC | 21m |
| RNGR744 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-03-31 15:02 UTC | 2026-03-31 15:43 UTC | 40m |
| N208LN |  | Five Oaks Estate Airport (FD03) | Evergreen Regional/Middleton Field (KGZH) | 2026-03-31 15:10 UTC | 2026-03-31 15:36 UTC | 26m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-03-31 15:26 UTC | 2026-03-31 15:27 UTC | 0m |
| OOH89 | OOH | Amougies Airport (EBAM) | Amougies Airport (EBAM) | 2026-03-31 15:22 UTC | 2026-03-31 15:26 UTC | 3m |
| FHLID | FHL | Muchamiel Airport (LEMU) | Alcantarilla Airport (LERI) | 2026-03-31 10:55 UTC | 2026-03-31 15:25 UTC | 4h 30m |
| TEAM41 | TEA | Mc Guire Field (Joint Base Mc Guire Dix Lakehurst) Airport (KWRI) | Columbiana County Airport (K02G) | 2026-03-31 14:24 UTC | 2026-03-31 15:25 UTC | 1h 1m |
| FHY246 | FHY | Frankfurt am Main International Airport (EDDF) | Karain Airport (LTXE) | 2026-03-31 12:29 UTC | 2026-03-31 15:21 UTC | 2h 52m |
| DEHUL | DEH | Oberschleisheim Airfield (EDNX) | Augsburg Airport (EDMA) | 2026-03-31 14:46 UTC | 2026-03-31 15:21 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
