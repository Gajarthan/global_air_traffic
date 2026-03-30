# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_15:35:51_UTC-green)

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

**Latest saved flight:** 2026-03-30 15:35:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 15:35:51 UTC

- **4,583** saved flights
- **3,246** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,583** saved routes in the archive
- **1h 18m** average flight duration

### Carbon Footprint Estimate

- **59,201.2 tonnes** estimated CO2 emissions
- **3,431,954 km** total distance flown
- **880 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 218 |
| 2 | Ryanair | 170 |
| 3 | IndiGo | 123 |
| 4 | EJA | 96 |
| 5 | American Airlines | 85 |
| 6 | Southwest Airlines | 73 |
| 7 | Lufthansa | 72 |
| 8 | ENY | 67 |
| 9 | AXM | 58 |
| 10 | LATAM Airlines | 51 |
| 11 | Vueling | 49 |
| 12 | Delta Air Lines | 43 |
| 13 | All Nippon Airways | 39 |
| 14 | LXJ | 38 |
| 15 | Japan Airlines | 37 |
| 16 | WIF | 35 |
| 17 | Cathay Pacific | 34 |
| 18 | Swiss International | 34 |
| 19 | QLK | 33 |
| 20 | United Airlines | 33 |
| 21 | Avianca | 32 |
| 22 | VIV | 32 |
| 23 | AXB | 30 |
| 24 | AZU | 30 |
| 25 | EDV | 28 |
| 26 | VOE | 27 |
| 27 | Alaska Airlines | 25 |
| 28 | ARE | 23 |
| 29 | EJU | 23 |
| 30 | BRC | 22 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3846 |
| 2 | 🇮🇳 IN | 367 |
| 3 | 🇪🇸 ES | 362 |
| 4 | 🇦🇺 AU | 289 |
| 5 | 🇨🇴 CO | 257 |
| 6 | 🇯🇵 JP | 252 |
| 7 | 🇧🇷 BR | 228 |
| 8 | 🇩🇪 DE | 215 |
| 9 | 🇮🇹 IT | 208 |
| 10 | 🇨🇦 CA | 182 |
| 11 | 🇲🇽 MX | 165 |
| 12 | 🇬🇧 GB | 157 |
| 13 | 🇫🇷 FR | 138 |
| 14 | 🇲🇾 MY | 128 |
| 15 | 🇿🇦 ZA | 117 |
| 16 | 🇨🇭 CH | 112 |
| 17 | 🇳🇴 NO | 111 |
| 18 | 🇵🇭 PH | 107 |
| 19 | 🇬🇹 GT | 101 |
| 20 | 🇬🇷 GR | 96 |
| 21 | 🇹🇷 TR | 75 |
| 22 | 🇹🇭 TH | 72 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇲🇴 MO | 59 |
| 25 | 🇮🇩 ID | 58 |
| 26 | 🇵🇱 PL | 58 |
| 27 | 🇲🇦 MA | 54 |
| 28 | 🇰🇷 KR | 52 |
| 29 | 🇧🇸 BS | 49 |
| 30 | 🇫🇮 FI | 46 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 116 |
| 2 | El Dorado International Airport |  | CO | 95 |
| 3 | Tokyo International Airport |  | JP | 85 |
| 4 | Indira Gandhi International Airport |  | IN | 84 |
| 5 | Denver International Airport |  | US | 81 |
| 6 | Frankfurt am Main International Airport |  | DE | 71 |
| 7 | La Aurora Airport |  | GT | 66 |
| 8 | Macau International Airport |  | MO | 59 |
| 9 | Tenerife Norte Airport |  | ES | 58 |
| 10 | Guaymaral Airport |  | CO | 58 |
| 11 | Zurich Airport |  | CH | 55 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 53 |
| 13 | Harry Reid International Airport |  | US | 52 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 52 |
| 15 | Chicago O'Hare International Airport |  | US | 47 |
| 16 | Ninoy Aquino International Airport |  | PH | 47 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 18 | Kuala Lumpur International Airport |  | MY | 46 |
| 19 | Eleftherios Venizelos International Airport |  | GR | 43 |
| 20 | Madrid Barajas International Airport |  | ES | 43 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 42 |
| 22 | O. R. Tambo International Airport |  | ZA | 40 |
| 23 | Charlotte/Douglas International Airport |  | US | 38 |
| 24 | Bengaluru International Airport |  | IN | 37 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 37 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 37 |
| 27 | Miami International Airport |  | US | 35 |
| 28 | Vitoria/Foronda Airport |  | ES | 35 |
| 29 | Reno/Tahoe International Airport |  | US | 34 |
| 30 | Amsterdam Airport Schiphol |  | NL | 34 |
| 31 | Charles de Gaulle International Airport |  | FR | 34 |
| 32 | Centennial Airport |  | US | 34 |
| 33 | Malpensa International Airport |  | IT | 33 |
| 34 | Los Angeles International Airport |  | US | 32 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 32 |
| 36 | Salt Lake City International Airport |  | US | 31 |
| 37 | Daniel K Inouye International Airport |  | US | 30 |
| 38 | Tampa International Airport |  | US | 30 |
| 39 | Austin-Bergstrom International Airport |  | US | 30 |
| 40 | VGZR |  |  | 30 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 23 | 28m | - | - |
| 4 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 15 | 25m | 152 km | 39.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 14 | 1h 40m | 1,423 km | 343.6 t |
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
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 11 | 4m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 10 | 1h 56m | 1,156 km | 199.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 26 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 9 | 52m | 136 km | 21.1 t |
| 29 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 8 | 51m | 645 km | 89.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9088D |  | Le Sueur Municipal Airport (K12Y) | Flying Cloud Airport (KFCM) | 2026-03-30 15:18 UTC | 2026-03-30 15:35 UTC | 17m |
| N154RV |  | K00V (K00V) | Limon Municipal Airport (KLIC) | 2026-03-30 15:04 UTC | 2026-03-30 15:18 UTC | 13m |
| N37PZ |  | Swains Creek Airport (UT00) | Henderson Executive Airport (KHND) | 2026-03-30 14:43 UTC | 2026-03-30 15:14 UTC | 30m |
| EWG24Y | EWG | Cologne Bonn Airport (EDDK) | Palma De Mallorca Airport (LEPA) | 2026-03-30 13:19 UTC | 2026-03-30 15:12 UTC | 1h 53m |
| SHIV91 | SHI | Dunbar Ranch Airport (0XS8) | 6TA4 (6TA4) | 2026-03-30 14:53 UTC | 2026-03-30 15:12 UTC | 18m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-03-30 15:00 UTC | 2026-03-30 15:11 UTC | 11m |
| IGO257M | IndiGo | Juhu Aerodrome (VAJJ) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-30 12:53 UTC | 2026-03-30 15:09 UTC | 2h 15m |
| CHX80 | CHX | Weiden in der Oberpfalz Airport (EDQW) | Schmidgaden Airport (EDPQ) | 2026-03-30 15:00 UTC | 2026-03-30 15:06 UTC | 5m |
| NIT256 | NIT | Heart Of Georgia Regional Airport (KEZM) | W H 'Bud' Barron Airport (KDBN) | 2026-03-30 14:35 UTC | 2026-03-30 15:04 UTC | 29m |
| N247CL |  | Newnan Coweta County Airport (KCCO) | Newnan Coweta County Airport (KCCO) | 2026-03-30 14:55 UTC | 2026-03-30 15:03 UTC | 8m |
| TEK644 | TEK | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-03-30 14:37 UTC | 2026-03-30 15:00 UTC | 23m |
| C2709 |  | St Pete-Clearwater International Airport (KPIE) | Hilton Head Airport (KHXD) | 2026-03-30 13:41 UTC | 2026-03-30 15:00 UTC | 1h 18m |
| N357EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-30 14:07 UTC | 2026-03-30 14:58 UTC | 51m |
| TOPCT92 | TOP | Offutt Afb Airport (KOFF) | SD41 (SD41) | 2026-03-30 13:55 UTC | 2026-03-30 14:57 UTC | 1h 2m |
| N1774V |  | Denton Enterprise Airport (KDTO) | Flying T Ranch Airport (41TS) | 2026-03-30 13:16 UTC | 2026-03-30 14:56 UTC | 1h 39m |
| N7040Q |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-03-30 14:38 UTC | 2026-03-30 14:54 UTC | 16m |
| REECMRJ | REE | Valencia Airport (LEVC) | Valencia Airport (LEVC) | 2026-03-30 14:30 UTC | 2026-03-30 14:53 UTC | 22m |
| ACR63 | ACR | Cuatro Vientos Airport (LECU) | E. Castellanos-Villacastin Airport (LEEV) | 2026-03-30 14:21 UTC | 2026-03-30 14:50 UTC | 29m |
| AVR4872 | AVR | El Dorado International Airport (SKBO) | Alberto Lleras Camargo Airport (SKSO) | 2026-03-30 14:35 UTC | 2026-03-30 14:50 UTC | 15m |
| LXJ428 | LXJ | Tulsa International Airport (KTUL) | Rocky Mountain Metro Airport (KBJC) | 2026-03-30 13:17 UTC | 2026-03-30 14:49 UTC | 1h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
