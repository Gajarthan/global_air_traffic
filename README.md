# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_20:02:00_UTC-green)

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

**Latest saved flight:** 2026-03-29 20:02:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 20:02:00 UTC

- **3,050** saved flights
- **2,318** unique routes
- **95** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,050** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **40,246.0 tonnes** estimated CO2 emissions
- **2,333,100 km** total distance flown
- **898 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 157 |
| 2 | Ryanair | 107 |
| 3 | IndiGo | 79 |
| 4 | EJA | 68 |
| 5 | American Airlines | 59 |
| 6 | Southwest Airlines | 59 |
| 7 | Lufthansa | 53 |
| 8 | ENY | 51 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 34 |
| 11 | LXJ | 31 |
| 12 | Vueling | 31 |
| 13 | LATAM Airlines | 29 |
| 14 | United Airlines | 28 |
| 15 | VIV | 23 |
| 16 | Avianca | 22 |
| 17 | Cathay Pacific | 21 |
| 18 | Swiss International | 21 |
| 19 | WIF | 21 |
| 20 | All Nippon Airways | 20 |
| 21 | ARE | 19 |
| 22 | AXB | 19 |
| 23 | EDV | 19 |
| 24 | Japan Airlines | 18 |
| 25 | BRC | 17 |
| 26 | VOE | 17 |
| 27 | AEE | 16 |
| 28 | Alaska Airlines | 16 |
| 29 | MXY | 16 |
| 30 | SFR | 16 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2687 |
| 2 | 🇪🇸 ES | 246 |
| 3 | 🇮🇳 IN | 221 |
| 4 | 🇨🇴 CO | 196 |
| 5 | 🇩🇪 DE | 156 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇨🇦 CA | 127 |
| 8 | 🇧🇷 BR | 127 |
| 9 | 🇦🇺 AU | 126 |
| 10 | 🇮🇹 IT | 126 |
| 11 | 🇬🇧 GB | 114 |
| 12 | 🇲🇽 MX | 113 |
| 13 | 🇬🇹 GT | 91 |
| 14 | 🇫🇷 FR | 88 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 72 |
| 18 | 🇳🇴 NO | 67 |
| 19 | 🇬🇷 GR | 64 |
| 20 | 🇵🇭 PH | 63 |
| 21 | 🇹🇷 TR | 46 |
| 22 | 🇹🇭 TH | 45 |
| 23 | 🇵🇱 PL | 42 |
| 24 | 🇧🇸 BS | 40 |
| 25 | 🇫🇮 FI | 38 |
| 26 | 🇮🇩 ID | 37 |
| 27 | 🇲🇦 MA | 35 |
| 28 | 🇲🇴 MO | 32 |
| 29 | 🇳🇱 NL | 28 |
| 30 | 🇰🇷 KR | 26 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 75 |
| 2 | El Dorado International Airport |  | CO | 69 |
| 3 | Denver International Airport |  | US | 61 |
| 4 | La Aurora Airport |  | GT | 58 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 53 |
| 7 | Indira Gandhi International Airport |  | IN | 49 |
| 8 | Tenerife Norte Airport |  | ES | 45 |
| 9 | Tokyo International Airport |  | JP | 44 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 39 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 38 |
| 12 | Harry Reid International Airport |  | US | 38 |
| 13 | Chicago O'Hare International Airport |  | US | 36 |
| 14 | Zurich Airport |  | CH | 36 |
| 15 | Kuala Lumpur International Airport |  | MY | 33 |
| 16 | Macau International Airport |  | MO | 32 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 30 |
| 18 | O. R. Tambo International Airport |  | ZA | 30 |
| 19 | Charlotte/Douglas International Airport |  | US | 29 |
| 20 | Reno/Tahoe International Airport |  | US | 28 |
| 21 | Madrid Barajas International Airport |  | ES | 27 |
| 22 | Vitoria/Foronda Airport |  | ES | 27 |
| 23 | Salt Lake City International Airport |  | US | 27 |
| 24 | Eleftherios Venizelos International Airport |  | GR | 26 |
| 25 | Ninoy Aquino International Airport |  | PH | 26 |
| 26 | Miami International Airport |  | US | 25 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 28 | Charles de Gaulle International Airport |  | FR | 23 |
| 29 | Bengaluru International Airport |  | IN | 23 |
| 30 | Amsterdam Airport Schiphol |  | NL | 23 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 23 |
| 32 | Los Angeles International Airport |  | US | 22 |
| 33 | CO86 |  |  | 22 |
| 34 | Perales Airport |  | CO | 22 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 22 |
| 36 | Centennial Airport |  | US | 22 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 21 |
| 38 | VGZR |  |  | 21 |
| 39 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 21 |
| 40 | Sydney Kingsford Smith International Airport |  | AU | 20 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 22 | 14m | 114 km | 43.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 15 | 26m | 99 km | 25.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 9 | 15m | 206 km | 32.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 12 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 14 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 9 | 30m | 69 km | 10.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 8 | 1h 55m | 1,304 km | 180.0 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 21 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 7 | 12m | - | - |
| 22 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 6 | 2h 1m | 1,156 km | 119.7 t |
| 24 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 28 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 6 | 54m | 630 km | 65.2 t |
| 29 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 30 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 6 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65295 |  | Somerset County Airport (K2G9) | 2PN4 (2PN4) | 2026-03-29 19:49 UTC | 2026-03-29 20:02 UTC | 12m |
| N9259S |  | Greeley-Weld County Airport (KGXY) | Laramie Regional Airport (KLAR) | 2026-03-29 19:19 UTC | 2026-03-29 19:55 UTC | 35m |
| N291ME |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-03-29 19:11 UTC | 2026-03-29 19:54 UTC | 42m |
| TRP1 | TRP | Forest Hill Airport (MD31) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-03-29 19:43 UTC | 2026-03-29 19:53 UTC | 10m |
| N884DM |  | Pella Municipal Airport (KPEA) | Ankeny Regional Airport (KIKV) | 2026-03-29 19:16 UTC | 2026-03-29 19:50 UTC | 34m |
| N104TQ |  | Monterey Regional Airport (KMRY) | Palo Alto Airport (KPAO) | 2026-03-29 19:23 UTC | 2026-03-29 19:47 UTC | 24m |
| FHRIV | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-03-29 19:23 UTC | 2026-03-29 19:47 UTC | 24m |
| NOZ842 | Norwegian Air | Bergen Airport Flesland (ENBR) | Stockholm-Arlanda Airport (ESSA) | 2026-03-29 18:42 UTC | 2026-03-29 19:47 UTC | 1h 4m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-03-29 19:09 UTC | 2026-03-29 19:43 UTC | 34m |
| N198X |  | John Wayne/Orange County Airport (KSNA) | Osborne Airport (8CA0) | 2026-03-29 19:23 UTC | 2026-03-29 19:41 UTC | 17m |
|  |  | Motiti Island Airport (NZOI) | Motiti Island Airport (NZOI) | 2026-03-29 19:39 UTC | 2026-03-29 19:39 UTC | 0m |
| N16NW |  | Pine Ridge Airport (KIEN) | Alliance Municipal Airport (KAIA) | 2026-03-29 19:20 UTC | 2026-03-29 19:36 UTC | 15m |
| CGVUU | CGV | Kelowna Airport (CYLW) | Vernon Airport (CYVK) | 2026-03-29 19:16 UTC | 2026-03-29 19:34 UTC | 18m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-29 18:45 UTC | 2026-03-29 19:33 UTC | 47m |
| EJA549 | EJA | Iron Mountain Ranch Airport (5TE5) | TE08 (TE08) | 2026-03-29 19:03 UTC | 2026-03-29 19:31 UTC | 27m |
| N900D |  | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 2026-03-29 18:38 UTC | 2026-03-29 19:31 UTC | 52m |
| CBC963 | CBC | Oxnard Airport (KOXR) | K36U (K36U) | 2026-03-29 17:20 UTC | 2026-03-29 19:28 UTC | 2h 7m |
| N921RA |  | La Aurora Airport (MGGT) | San Jose Airport (MGSJ) | 2026-03-29 19:15 UTC | 2026-03-29 19:26 UTC | 10m |
| N102UC |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-29 18:16 UTC | 2026-03-29 19:23 UTC | 1h 6m |
| LXJ327 | LXJ | Harry Reid International Airport (KLAS) | Hayward Executive Airport (KHWD) | 2026-03-29 18:18 UTC | 2026-03-29 19:22 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
