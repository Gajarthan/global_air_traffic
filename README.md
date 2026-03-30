# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_16:23:52_UTC-green)

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

**Latest saved flight:** 2026-03-30 16:23:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 16:23:52 UTC

- **4,735** saved flights
- **3,333** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,735** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **60,634.5 tonnes** estimated CO2 emissions
- **3,515,043 km** total distance flown
- **874 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 229 |
| 2 | Ryanair | 175 |
| 3 | IndiGo | 129 |
| 4 | EJA | 97 |
| 5 | American Airlines | 87 |
| 6 | Southwest Airlines | 74 |
| 7 | Lufthansa | 72 |
| 8 | ENY | 70 |
| 9 | AXM | 58 |
| 10 | LATAM Airlines | 54 |
| 11 | Vueling | 49 |
| 12 | Delta Air Lines | 44 |
| 13 | LXJ | 44 |
| 14 | All Nippon Airways | 39 |
| 15 | WIF | 39 |
| 16 | Japan Airlines | 37 |
| 17 | Swiss International | 36 |
| 18 | Cathay Pacific | 34 |
| 19 | QLK | 33 |
| 20 | United Airlines | 33 |
| 21 | VIV | 33 |
| 22 | Avianca | 32 |
| 23 | AXB | 31 |
| 24 | AZU | 31 |
| 25 | EDV | 29 |
| 26 | VOE | 28 |
| 27 | EJU | 27 |
| 28 | Alaska Airlines | 25 |
| 29 | MXY | 25 |
| 30 | ARE | 24 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3993 |
| 2 | 🇮🇳 IN | 383 |
| 3 | 🇪🇸 ES | 370 |
| 4 | 🇦🇺 AU | 289 |
| 5 | 🇨🇴 CO | 263 |
| 6 | 🇯🇵 JP | 252 |
| 7 | 🇧🇷 BR | 240 |
| 8 | 🇩🇪 DE | 219 |
| 9 | 🇮🇹 IT | 218 |
| 10 | 🇨🇦 CA | 185 |
| 11 | 🇲🇽 MX | 168 |
| 12 | 🇬🇧 GB | 160 |
| 13 | 🇫🇷 FR | 144 |
| 14 | 🇲🇾 MY | 128 |
| 15 | 🇿🇦 ZA | 123 |
| 16 | 🇳🇴 NO | 121 |
| 17 | 🇨🇭 CH | 117 |
| 18 | 🇵🇭 PH | 109 |
| 19 | 🇬🇹 GT | 107 |
| 20 | 🇬🇷 GR | 101 |
| 21 | 🇹🇷 TR | 80 |
| 22 | 🇹🇭 TH | 72 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇲🇴 MO | 59 |
| 25 | 🇵🇱 PL | 59 |
| 26 | 🇮🇩 ID | 58 |
| 27 | 🇲🇦 MA | 54 |
| 28 | 🇰🇷 KR | 52 |
| 29 | 🇧🇸 BS | 50 |
| 30 | 🇫🇮 FI | 47 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 121 |
| 2 | El Dorado International Airport |  | CO | 96 |
| 3 | Denver International Airport |  | US | 87 |
| 4 | Indira Gandhi International Airport |  | IN | 86 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | Frankfurt am Main International Airport |  | DE | 71 |
| 7 | La Aurora Airport |  | GT | 71 |
| 8 | Guaymaral Airport |  | CO | 60 |
| 9 | Macau International Airport |  | MO | 59 |
| 10 | Zurich Airport |  | CH | 59 |
| 11 | Tenerife Norte Airport |  | ES | 58 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 53 |
| 13 | Harry Reid International Airport |  | US | 53 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 52 |
| 15 | Chicago O'Hare International Airport |  | US | 49 |
| 16 | Ninoy Aquino International Airport |  | PH | 48 |
| 17 | Eleftherios Venizelos International Airport |  | GR | 46 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 19 | Kuala Lumpur International Airport |  | MY | 46 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 44 |
| 21 | Madrid Barajas International Airport |  | ES | 43 |
| 22 | O. R. Tambo International Airport |  | ZA | 42 |
| 23 | Bengaluru International Airport |  | IN | 40 |
| 24 | Charlotte/Douglas International Airport |  | US | 39 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 39 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 27 | Miami International Airport |  | US | 36 |
| 28 | Charles de Gaulle International Airport |  | FR | 36 |
| 29 | Centennial Airport |  | US | 36 |
| 30 | Vitoria/Foronda Airport |  | ES | 35 |
| 31 | Amsterdam Airport Schiphol |  | NL | 35 |
| 32 | Malpensa International Airport |  | IT | 35 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 34 |
| 34 | Reno/Tahoe International Airport |  | US | 34 |
| 35 | Congonhas Airport |  | BR | 33 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 33 |
| 37 | Los Angeles International Airport |  | US | 32 |
| 38 | Tampa International Airport |  | US | 32 |
| 39 | Austin-Bergstrom International Airport |  | US | 31 |
| 40 | Salt Lake City International Airport |  | US | 31 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 24 | 28m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 4 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 17 | 26m | 152 km | 44.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 12 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 12 | 15m | 206 km | 42.7 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 11 | 29m | 275 km | 52.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 19 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 21 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 23 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 11 | 4m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 10 | 1h 56m | 1,156 km | 199.5 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 10 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 30 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 8 | 51m | 645 km | 89.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AXLE11 | AXL | 75OK (75OK) | OK49 (OK49) | 2026-03-30 16:06 UTC | 2026-03-30 16:23 UTC | 17m |
| NSZ8MV | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-03-30 15:19 UTC | 2026-03-30 16:12 UTC | 53m |
| CCA772 | Air China | Shenzhen Bao'an International Airport (ZGSZ) | Sharypovo Airport (UNKO) | 2026-03-29 16:39 UTC | 2026-03-30 16:12 UTC | 23h 32m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-03-30 15:57 UTC | 2026-03-30 16:11 UTC | 14m |
| AUB1787 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-03-30 15:58 UTC | 2026-03-30 16:11 UTC | 12m |
| G20630 |  | St Paul Downtown Holman Field (KSTP) | St Paul Downtown Holman Field (KSTP) | 2026-03-30 16:10 UTC | 2026-03-30 16:11 UTC | 0m |
| PGT4AQ | PGT | Gaziemir Airport (LTBK) | Ataturk International Airport (LTBA) | 2026-03-30 15:43 UTC | 2026-03-30 16:10 UTC | 26m |
| FHLID | FHL | Ontur Airport (LEOT) | Alhama De Murcia Airport (LELH) | 2026-03-30 15:54 UTC | 2026-03-30 16:08 UTC | 13m |
| N863BW |  | Lakeland Linder International Airport (KLAL) | Bartow Executive Airport (KBOW) | 2026-03-30 15:34 UTC | 2026-03-30 16:07 UTC | 32m |
| SPIN222 | SPI | Kingsville Nas Airport (KNQI) | Kleberg County Airport (KIKG) | 2026-03-30 15:43 UTC | 2026-03-30 16:06 UTC | 22m |
| N77ZA |  | Centennial Airport (KAPA) | Telluride Regional Airport (KTEX) | 2026-03-30 15:04 UTC | 2026-03-30 16:02 UTC | 58m |
| G20908 |  | 7PS4 (7PS4) | PS35 (PS35) | 2026-03-30 15:51 UTC | 2026-03-30 16:02 UTC | 10m |
| NDU82 | NDU | Central Valley Aviation Airport (NA81) | Deck Airport (5ND9) | 2026-03-30 15:28 UTC | 2026-03-30 16:02 UTC | 34m |
| N54GB |  | Carson City Airport (KCXP) | Minden-Tahoe Airport (KMEV) | 2026-03-30 15:55 UTC | 2026-03-30 16:01 UTC | 5m |
| N5336K |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-03-30 15:26 UTC | 2026-03-30 15:59 UTC | 32m |
| OXF6514 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-03-30 15:07 UTC | 2026-03-30 15:57 UTC | 50m |
| N496SP |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-03-30 14:54 UTC | 2026-03-30 15:57 UTC | 1h 2m |
| LXJ435 | LXJ | Teterboro Airport (KTEB) | Miami Executive Airport (KTMB) | 2026-03-30 13:23 UTC | 2026-03-30 15:56 UTC | 2h 32m |
| SGE67 | SGE | Kenneth Copeland Airport (K4T2) | Kenneth Copeland Airport (K4T2) | 2026-03-30 15:51 UTC | 2026-03-30 15:55 UTC | 3m |
| C6516 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-03-30 15:34 UTC | 2026-03-30 15:51 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
