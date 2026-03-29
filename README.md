# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_21:40:23_UTC-green)

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

**Latest saved flight:** 2026-03-29 21:40:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 21:40:23 UTC

- **3,333** saved flights
- **2,519** unique routes
- **96** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,333** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **44,070.7 tonnes** estimated CO2 emissions
- **2,554,824 km** total distance flown
- **900 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 183 |
| 2 | Ryanair | 120 |
| 3 | EJA | 81 |
| 4 | IndiGo | 80 |
| 5 | American Airlines | 73 |
| 6 | Southwest Airlines | 63 |
| 7 | ENY | 57 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 37 |
| 11 | Vueling | 36 |
| 12 | LXJ | 35 |
| 13 | LATAM Airlines | 35 |
| 14 | United Airlines | 31 |
| 15 | Avianca | 24 |
| 16 | Cathay Pacific | 24 |
| 17 | VIV | 24 |
| 18 | Swiss International | 22 |
| 19 | WIF | 21 |
| 20 | All Nippon Airways | 20 |
| 21 | ARE | 19 |
| 22 | AXB | 19 |
| 23 | EDV | 19 |
| 24 | Alaska Airlines | 18 |
| 25 | Japan Airlines | 18 |
| 26 | VOE | 18 |
| 27 | AZU | 17 |
| 28 | BRC | 17 |
| 29 | MXY | 17 |
| 30 | AEE | 16 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3043 |
| 2 | 🇪🇸 ES | 267 |
| 3 | 🇮🇳 IN | 223 |
| 4 | 🇨🇴 CO | 205 |
| 5 | 🇩🇪 DE | 157 |
| 6 | 🇧🇷 BR | 153 |
| 7 | 🇨🇦 CA | 142 |
| 8 | 🇦🇺 AU | 136 |
| 9 | 🇯🇵 JP | 134 |
| 10 | 🇮🇹 IT | 133 |
| 11 | 🇲🇽 MX | 127 |
| 12 | 🇬🇧 GB | 119 |
| 13 | 🇬🇹 GT | 96 |
| 14 | 🇫🇷 FR | 91 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 74 |
| 18 | 🇳🇴 NO | 67 |
| 19 | 🇬🇷 GR | 66 |
| 20 | 🇵🇭 PH | 63 |
| 21 | 🇹🇷 TR | 48 |
| 22 | 🇹🇭 TH | 45 |
| 23 | 🇧🇸 BS | 43 |
| 24 | 🇵🇱 PL | 42 |
| 25 | 🇲🇦 MA | 39 |
| 26 | 🇫🇮 FI | 38 |
| 27 | 🇮🇩 ID | 37 |
| 28 | 🇲🇴 MO | 37 |
| 29 | 🇳🇿 NZ | 36 |
| 30 | 🇳🇱 NL | 31 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 93 |
| 2 | Denver International Airport |  | US | 72 |
| 3 | El Dorado International Airport |  | CO | 72 |
| 4 | La Aurora Airport |  | GT | 62 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Indira Gandhi International Airport |  | IN | 50 |
| 8 | Tenerife Norte Airport |  | ES | 48 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 45 |
| 10 | Tokyo International Airport |  | JP | 44 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 43 |
| 12 | Harry Reid International Airport |  | US | 40 |
| 13 | Chicago O'Hare International Airport |  | US | 39 |
| 14 | Zurich Airport |  | CH | 37 |
| 15 | Macau International Airport |  | MO | 37 |
| 16 | Charlotte/Douglas International Airport |  | US | 33 |
| 17 | Kuala Lumpur International Airport |  | MY | 33 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 32 |
| 19 | Miami International Airport |  | US | 31 |
| 20 | O. R. Tambo International Airport |  | ZA | 30 |
| 21 | Reno/Tahoe International Airport |  | US | 29 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 23 | Madrid Barajas International Airport |  | ES | 28 |
| 24 | Salt Lake City International Airport |  | US | 28 |
| 25 | Vitoria/Foronda Airport |  | ES | 27 |
| 26 | Ninoy Aquino International Airport |  | PH | 26 |
| 27 | George Bush Intcntl/Houston Airport |  | US | 26 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 26 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 26 |
| 30 | CO86 |  |  | 25 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 32 | Centennial Airport |  | US | 25 |
| 33 | Los Angeles International Airport |  | US | 24 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 24 |
| 35 | Tampa International Airport |  | US | 24 |
| 36 | Amsterdam Airport Schiphol |  | NL | 24 |
| 37 | Charles de Gaulle International Airport |  | FR | 23 |
| 38 | Bengaluru International Airport |  | IN | 23 |
| 39 | Perales Airport |  | CO | 23 |
| 40 | Seattle-Tacoma International Airport |  | US | 22 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 23 | 14m | 114 km | 45.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 10 | 14m | 206 km | 35.6 t |
| 10 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 10 | 30m | 69 km | 12.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 17 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 8 | 1h 55m | 1,304 km | 180.0 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 21 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 23 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 6 | 1h 49m | - | - |
| 24 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 25 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 26 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 6 | 52m | 645 km | 66.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 6 | 38m | - | - |
| 30 | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 6 | 16h 7m | 12,992 km | 1,344.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9452B |  | New Jerusalem Airport (K1Q4) | New Jerusalem Airport (K1Q4) | 2026-03-29 19:22 UTC | 2026-03-29 21:40 UTC | 2h 17m |
| N23NW |  | Lincoln Airport (KLNK) | 71NE (71NE) | 2026-03-29 19:15 UTC | 2026-03-29 21:37 UTC | 2h 22m |
| N54102 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-03-29 21:09 UTC | 2026-03-29 21:31 UTC | 22m |
| N692DA |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-03-29 21:16 UTC | 2026-03-29 21:27 UTC | 10m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-03-29 20:17 UTC | 2026-03-29 21:25 UTC | 1h 7m |
| N6701R |  | Orlando Apopka Airport (KX04) | Wauchula Municipal Airport (KCHN) | 2026-03-29 20:27 UTC | 2026-03-29 21:25 UTC | 57m |
| N558R |  | Nashville International Airport (KBNA) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-03-29 20:33 UTC | 2026-03-29 21:24 UTC | 51m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-03-29 20:28 UTC | 2026-03-29 21:24 UTC | 56m |
| N603BS |  | Manchester Boston Regional Airport (KMHT) | Laconia Municipal Airport (KLCI) | 2026-03-29 21:05 UTC | 2026-03-29 21:20 UTC | 14m |
| N916BQ |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-03-29 20:25 UTC | 2026-03-29 21:18 UTC | 52m |
| UAE9796 | Emirates | Shaibah Airport (OESB) | Macau International Airport (VMMC) | 2026-03-29 11:41 UTC | 2026-03-29 21:16 UTC | 9h 35m |
| PCJ20 | PCJ | Mc Clellan-Palomar Airport (KCRQ) | Emory Ranch Airport (0CA6) | 2026-03-29 21:00 UTC | 2026-03-29 21:16 UTC | 15m |
| CPA640 | Cathay Pacific | Biratnagar Airport (VNVT) | Macau International Airport (VMMC) | 2026-03-29 18:09 UTC | 2026-03-29 21:11 UTC | 3h 1m |
| TIV740 | TIV | Miami-Opa Locka Executive Airport (KOPF) | The Florida Keys Marathon International Airport (KMTH) | 2026-03-29 20:42 UTC | 2026-03-29 21:03 UTC | 20m |
| UAE9964 | Emirates | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-03-28 21:14 UTC | 2026-03-29 21:02 UTC | 23h 48m |
| WEN3350 | WEN | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-03-29 20:38 UTC | 2026-03-29 21:01 UTC | 23m |
| N71JT |  | Rosenberg Airport (MY80) | Estherville Municipal Airport (KEST) | 2026-03-29 20:40 UTC | 2026-03-29 21:00 UTC | 19m |
| N491JV |  | Daytona Beach International Airport (KDAB) | LA34 (LA34) | 2026-03-29 17:52 UTC | 2026-03-29 20:59 UTC | 3h 7m |
| N123DT |  | Morgan County Airport (K42U) | Morgan County Airport (K42U) | 2026-03-29 20:04 UTC | 2026-03-29 20:58 UTC | 53m |
| N330LD |  | Winnipeg James Armstrong Richardson International Airport (CYWG) | Russell Airport (CJW5) | 2026-03-29 20:25 UTC | 2026-03-29 20:56 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
