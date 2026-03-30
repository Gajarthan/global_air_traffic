# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_22:37:23_UTC-green)

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

**Latest saved flight:** 2026-03-30 22:37:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 22:37:23 UTC

- **5,649** saved flights
- **3,849** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,649** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **71,649.0 tonnes** estimated CO2 emissions
- **4,153,567 km** total distance flown
- **875 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 298 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 139 |
| 4 | EJA | 124 |
| 5 | American Airlines | 116 |
| 6 | Southwest Airlines | 93 |
| 7 | ENY | 89 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 63 |
| 10 | AXM | 58 |
| 11 | LXJ | 55 |
| 12 | Vueling | 54 |
| 13 | Delta Air Lines | 52 |
| 14 | Cathay Pacific | 44 |
| 15 | United Airlines | 44 |
| 16 | VIV | 44 |
| 17 | WIF | 43 |
| 18 | All Nippon Airways | 39 |
| 19 | AZU | 38 |
| 20 | Swiss International | 38 |
| 21 | Japan Airlines | 37 |
| 22 | EDV | 36 |
| 23 | Alaska Airlines | 35 |
| 24 | Avianca | 35 |
| 25 | AXB | 34 |
| 26 | QLK | 34 |
| 27 | VOE | 31 |
| 28 | EJU | 30 |
| 29 | MXY | 30 |
| 30 | BRC | 28 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5050 |
| 2 | 🇮🇳 IN | 418 |
| 3 | 🇪🇸 ES | 407 |
| 4 | 🇦🇺 AU | 315 |
| 5 | 🇧🇷 BR | 294 |
| 6 | 🇨🇴 CO | 280 |
| 7 | 🇮🇹 IT | 263 |
| 8 | 🇯🇵 JP | 254 |
| 9 | 🇨🇦 CA | 246 |
| 10 | 🇩🇪 DE | 242 |
| 11 | 🇲🇽 MX | 213 |
| 12 | 🇬🇧 GB | 184 |
| 13 | 🇫🇷 FR | 170 |
| 14 | 🇳🇴 NO | 143 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇨🇭 CH | 124 |
| 17 | 🇿🇦 ZA | 123 |
| 18 | 🇬🇹 GT | 122 |
| 19 | 🇬🇷 GR | 117 |
| 20 | 🇵🇭 PH | 109 |
| 21 | 🇹🇷 TR | 91 |
| 22 | 🇳🇿 NZ | 91 |
| 23 | 🇹🇭 TH | 73 |
| 24 | 🇲🇴 MO | 72 |
| 25 | 🇲🇦 MA | 67 |
| 26 | 🇵🇱 PL | 65 |
| 27 | 🇧🇸 BS | 60 |
| 28 | 🇮🇩 ID | 58 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 157 |
| 2 | Denver International Airport |  | US | 118 |
| 3 | El Dorado International Airport |  | CO | 101 |
| 4 | Indira Gandhi International Airport |  | IN | 95 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 84 |
| 7 | Frankfurt am Main International Airport |  | DE | 80 |
| 8 | Macau International Airport |  | MO | 72 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 71 |
| 10 | Chicago O'Hare International Airport |  | US | 68 |
| 11 | Harry Reid International Airport |  | US | 67 |
| 12 | Zurich Airport |  | CH | 65 |
| 13 | Guaymaral Airport |  | CO | 65 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 63 |
| 15 | Tenerife Norte Airport |  | ES | 62 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 51 |
| 18 | Reno/Tahoe International Airport |  | US | 50 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 49 |
| 20 | Madrid Barajas International Airport |  | ES | 48 |
| 21 | Ninoy Aquino International Airport |  | PH | 48 |
| 22 | Charlotte/Douglas International Airport |  | US | 47 |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 47 |
| 24 | Malpensa International Airport |  | IT | 46 |
| 25 | Miami International Airport |  | US | 46 |
| 26 | Bengaluru International Airport |  | IN | 46 |
| 27 | Salt Lake City International Airport |  | US | 46 |
| 28 | Kuala Lumpur International Airport |  | MY | 46 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 45 |
| 30 | Charles de Gaulle International Airport |  | FR | 44 |
| 31 | Congonhas Airport |  | BR | 42 |
| 32 | O. R. Tambo International Airport |  | ZA | 42 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 41 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 35 | Centennial Airport |  | US | 41 |
| 36 | Seattle-Tacoma International Airport |  | US | 39 |
| 37 | Los Angeles International Airport |  | US | 38 |
| 38 | Austin-Bergstrom International Airport |  | US | 38 |
| 39 | Vitoria/Foronda Airport |  | ES | 38 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |

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
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 15 | 15m | 206 km | 53.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 14 | 1h 51m | 1,156 km | 279.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 14 | 4m | - | - |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 18 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 11 | 1h 56m | 1,304 km | 247.5 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 10 | 1h 2m | 723 km | 124.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTZ | YTZ | Caboolture Airport (YCAB) | Sunshine Coast Airport (YBMC) | 2026-03-30 22:22 UTC | 2026-03-30 22:37 UTC | 14m |
| N690RA |  | San Bernardino International Airport (KSBD) | Ontario International Airport (KONT) | 2026-03-30 21:46 UTC | 2026-03-30 22:35 UTC | 48m |
| N1096W |  | Nut Tree Airport (KVCB) | Palo Alto Airport (KPAO) | 2026-03-30 22:09 UTC | 2026-03-30 22:35 UTC | 25m |
| URSA98 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-03-30 20:26 UTC | 2026-03-30 22:35 UTC | 2h 8m |
| N460CA |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-03-30 22:08 UTC | 2026-03-30 22:34 UTC | 26m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-03-30 11:28 UTC | 2026-03-30 22:34 UTC | 11h 5m |
| N768SP |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-03-30 22:17 UTC | 2026-03-30 22:30 UTC | 13m |
| ZJF | ZJF | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 22:07 UTC | 2026-03-30 22:30 UTC | 22m |
| N26WR |  | Santa Ynez/Kunkle Field (KIZA) | Santa Monica Municipal Airport (KSMO) | 2026-03-30 22:02 UTC | 2026-03-30 22:27 UTC | 25m |
| SCU5 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-03-30 22:03 UTC | 2026-03-30 22:22 UTC | 19m |
| HOOK62 | HOO | Northwest Arkansas Ntl Airport (KXNA) | Tulsa International Airport (KTUL) | 2026-03-30 21:56 UTC | 2026-03-30 22:20 UTC | 24m |
| N731ND |  | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-03-30 21:54 UTC | 2026-03-30 22:19 UTC | 25m |
| N13312 |  | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-03-30 21:06 UTC | 2026-03-30 22:19 UTC | 1h 12m |
| N155JW |  | Sanctuary Ranch Airport (7TS4) | Addington Field (4TX8) | 2026-03-30 21:28 UTC | 2026-03-30 22:17 UTC | 48m |
| N641AT |  | Merrill Field (PAMR) | PAFW (PAFW) | 2026-03-30 21:32 UTC | 2026-03-30 22:13 UTC | 40m |
| N3974X |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-03-30 20:41 UTC | 2026-03-30 22:13 UTC | 1h 32m |
| CPA014 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-03-30 11:27 UTC | 2026-03-30 22:12 UTC | 10h 44m |
| CFLDK | CFL | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-03-30 21:54 UTC | 2026-03-30 22:10 UTC | 16m |
| CPA044 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-03-30 17:36 UTC | 2026-03-30 22:10 UTC | 4h 34m |
| N159AH |  | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Redstone Army Air Field (KHUA) | 2026-03-30 22:01 UTC | 2026-03-30 22:09 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
