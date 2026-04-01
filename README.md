# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_19:33:19_UTC-green)

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

**Latest saved flight:** 2026-04-01 19:33:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 19:33:19 UTC

- **9,495** saved flights
- **5,710** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,495** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **114,207.3 tonnes** estimated CO2 emissions
- **6,620,713 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 428 |
| 2 | Ryanair | 362 |
| 3 | IndiGo | 263 |
| 4 | EJA | 195 |
| 5 | American Airlines | 169 |
| 6 | Lufthansa | 163 |
| 7 | Southwest Airlines | 143 |
| 8 | ENY | 130 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 92 |
| 12 | LXJ | 87 |
| 13 | All Nippon Airways | 79 |
| 14 | WIF | 78 |
| 15 | Delta Air Lines | 74 |
| 16 | Swiss International | 72 |
| 17 | QLK | 70 |
| 18 | AZU | 66 |
| 19 | VIV | 66 |
| 20 | AXB | 63 |
| 21 | Japan Airlines | 60 |
| 22 | EDV | 59 |
| 23 | Alaska Airlines | 58 |
| 24 | BRC | 58 |
| 25 | United Airlines | 58 |
| 26 | EJU | 54 |
| 27 | easyJet | 53 |
| 28 | Avianca | 52 |
| 29 | AEE | 50 |
| 30 | Cathay Pacific | 49 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7816 |
| 2 | 🇮🇳 IN | 806 |
| 3 | 🇪🇸 ES | 747 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 521 |
| 6 | 🇧🇷 BR | 480 |
| 7 | 🇯🇵 JP | 461 |
| 8 | 🇨🇴 CO | 460 |
| 9 | 🇨🇦 CA | 458 |
| 10 | 🇮🇹 IT | 425 |
| 11 | 🇬🇧 GB | 341 |
| 12 | 🇲🇽 MX | 335 |
| 13 | 🇫🇷 FR | 294 |
| 14 | 🇳🇴 NO | 257 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 226 |
| 17 | 🇨🇭 CH | 222 |
| 18 | 🇿🇦 ZA | 203 |
| 19 | 🇳🇿 NZ | 199 |
| 20 | 🇬🇹 GT | 196 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇹🇷 TR | 158 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 125 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇹🇭 TH | 113 |
| 27 | 🇲🇦 MA | 111 |
| 28 | 🇧🇸 BS | 92 |
| 29 | 🇲🇴 MO | 92 |
| 30 | 🇲🇪 ME | 92 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 225 |
| 2 | Indira Gandhi International Airport |  | IN | 177 |
| 3 | Denver International Airport |  | US | 167 |
| 4 | Tokyo International Airport |  | JP | 165 |
| 5 | Frankfurt am Main International Airport |  | DE | 165 |
| 6 | El Dorado International Airport |  | CO | 148 |
| 7 | La Aurora Airport |  | GT | 139 |
| 8 | Guaymaral Airport |  | CO | 133 |
| 9 | Harry Reid International Airport |  | US | 128 |
| 10 | Zurich Airport |  | CH | 112 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 111 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Chicago O'Hare International Airport |  | US | 99 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 96 |
| 16 | Macau International Airport |  | MO | 92 |
| 17 | Tenerife Norte Airport |  | ES | 91 |
| 18 | Bengaluru International Airport |  | IN | 87 |
| 19 | Reno/Tahoe International Airport |  | US | 86 |
| 20 | Kuala Lumpur International Airport |  | MY | 85 |
| 21 | Charlotte/Douglas International Airport |  | US | 83 |
| 22 | Madrid Barajas International Airport |  | ES | 83 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 81 |
| 24 | Ninoy Aquino International Airport |  | PH | 78 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 73 |
| 26 | Malpensa International Airport |  | IT | 72 |
| 27 | Vitoria/Foronda Airport |  | ES | 70 |
| 28 | Pune Airport |  | IN | 70 |
| 29 | Congonhas Airport |  | BR | 70 |
| 30 | Salt Lake City International Airport |  | US | 69 |
| 31 | Daniel K Inouye International Airport |  | US | 68 |
| 32 | Barcelona International Airport |  | ES | 68 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 67 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 67 |
| 35 | Charles de Gaulle International Airport |  | FR | 66 |
| 36 | Seattle-Tacoma International Airport |  | US | 64 |
| 37 | Miami International Airport |  | US | 63 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 61 |
| 39 | Bodø Airport |  | NO | 61 |
| 40 | Gimpo International Airport |  | KR | 60 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 54 | 28m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 43 | 14m | 114 km | 84.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 28 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 26 | 23m | 99 km | 44.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 24 | 52m | 556 km | 230.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 17 | 1h 56m | 1,304 km | 382.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 14 | 54m | 630 km | 152.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N715WM |  | Cobb County International/Mccollum Field (KRYY) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-04-01 19:20 UTC | 2026-04-01 19:33 UTC | 12m |
| RN110 |  | Triple B Airpark (FL81) | Evergreen Regional/Middleton Field (KGZH) | 2026-04-01 19:00 UTC | 2026-04-01 19:28 UTC | 28m |
| N38AM |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-04-01 18:45 UTC | 2026-04-01 19:19 UTC | 34m |
| N2FT |  | Flying Cloud Airport (KFCM) | Van Normans Airport (2MN6) | 2026-04-01 18:27 UTC | 2026-04-01 19:17 UTC | 49m |
| N445BL |  | Winter Haven Regional Airport (KGIF) | Market World Airport (FL16) | 2026-04-01 19:12 UTC | 2026-04-01 19:14 UTC | 2m |
| RN190 |  | Stennis International Airport (KHSA) | Shade Tree Field (MS82) | 2026-04-01 19:06 UTC | 2026-04-01 19:13 UTC | 7m |
| MAGOO65 | MAG | Dunbar Ranch Airport (0XS8) | 6TA4 (6TA4) | 2026-04-01 18:49 UTC | 2026-04-01 19:08 UTC | 19m |
| N448VA |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-01 18:07 UTC | 2026-04-01 19:08 UTC | 1h 0m |
| N404SP |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Boerne Stage Airfield (K5C1) | 2026-04-01 18:19 UTC | 2026-04-01 19:03 UTC | 44m |
| N2138W |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-04-01 18:11 UTC | 2026-04-01 19:01 UTC | 49m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-01 18:33 UTC | 2026-04-01 19:01 UTC | 27m |
| N15206 |  | Skyhaven Airport (KDAW) | Perrotti Skyranch Airfield (09ME) | 2026-04-01 18:54 UTC | 2026-04-01 18:57 UTC | 3m |
| VIV7345 | VIV | Francisco Sarabia International Airport (MMTC) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-01 17:53 UTC | 2026-04-01 18:53 UTC | 1h 0m |
| N404DC |  | Cy Nunnally Memorial Airport (KD73) | Cy Nunnally Memorial Airport (KD73) | 2026-04-01 18:50 UTC | 2026-04-01 18:51 UTC | 1m |
| N558LM |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-01 17:48 UTC | 2026-04-01 18:50 UTC | 1h 2m |
| SKW5088 | SkyWest Airlines | George Bush Intcntl/Houston Airport (KIAH) | Thigpen Field (K00M) | 2026-04-01 17:55 UTC | 2026-04-01 18:47 UTC | 52m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-01 18:15 UTC | 2026-04-01 18:46 UTC | 31m |
| N164S |  | Felts Field (KSFF) | Rice Ranch Airport (2WA6) | 2026-04-01 18:20 UTC | 2026-04-01 18:46 UTC | 26m |
| BRCAT05 | BRC | Roswell Air Center Airport (KROW) | 2 X 4 Ranch Airport (NM47) | 2026-04-01 18:22 UTC | 2026-04-01 18:46 UTC | 24m |
| RHODY11 | RHO | Newport State Airport (KUUU) | Westover Arb/Metro Airport (KCEF) | 2026-04-01 18:14 UTC | 2026-04-01 18:45 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
