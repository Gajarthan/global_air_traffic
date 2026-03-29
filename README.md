# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_22:29:13_UTC-green)

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

**Latest saved flight:** 2026-03-29 22:29:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 22:29:13 UTC

- **3,427** saved flights
- **2,575** unique routes
- **98** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,427** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **45,321.0 tonnes** estimated CO2 emissions
- **2,627,303 km** total distance flown
- **903 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 191 |
| 2 | Ryanair | 123 |
| 3 | EJA | 82 |
| 4 | IndiGo | 80 |
| 5 | American Airlines | 75 |
| 6 | Southwest Airlines | 65 |
| 7 | ENY | 58 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 38 |
| 11 | LXJ | 36 |
| 12 | Vueling | 36 |
| 13 | LATAM Airlines | 35 |
| 14 | United Airlines | 31 |
| 15 | VIV | 27 |
| 16 | Cathay Pacific | 26 |
| 17 | Avianca | 25 |
| 18 | EDV | 23 |
| 19 | Swiss International | 22 |
| 20 | WIF | 22 |
| 21 | All Nippon Airways | 20 |
| 22 | ARE | 19 |
| 23 | Alaska Airlines | 19 |
| 24 | AXB | 19 |
| 25 | MXY | 19 |
| 26 | Japan Airlines | 18 |
| 27 | VOE | 18 |
| 28 | AZU | 17 |
| 29 | BRC | 17 |
| 30 | JetBlue | 17 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3150 |
| 2 | 🇪🇸 ES | 271 |
| 3 | 🇮🇳 IN | 224 |
| 4 | 🇨🇴 CO | 209 |
| 5 | 🇩🇪 DE | 157 |
| 6 | 🇧🇷 BR | 155 |
| 7 | 🇦🇺 AU | 154 |
| 8 | 🇨🇦 CA | 146 |
| 9 | 🇲🇽 MX | 138 |
| 10 | 🇮🇹 IT | 136 |
| 11 | 🇯🇵 JP | 134 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇬🇹 GT | 96 |
| 14 | 🇫🇷 FR | 92 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 74 |
| 18 | 🇳🇴 NO | 69 |
| 19 | 🇬🇷 GR | 66 |
| 20 | 🇵🇭 PH | 63 |
| 21 | 🇹🇷 TR | 48 |
| 22 | 🇧🇸 BS | 45 |
| 23 | 🇹🇭 TH | 45 |
| 24 | 🇵🇱 PL | 42 |
| 25 | 🇳🇿 NZ | 40 |
| 26 | 🇲🇦 MA | 39 |
| 27 | 🇲🇴 MO | 39 |
| 28 | 🇫🇮 FI | 38 |
| 29 | 🇮🇩 ID | 37 |
| 30 | 🇳🇱 NL | 32 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 93 |
| 2 | Denver International Airport |  | US | 75 |
| 3 | El Dorado International Airport |  | CO | 74 |
| 4 | La Aurora Airport |  | GT | 62 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Indira Gandhi International Airport |  | IN | 51 |
| 8 | Tenerife Norte Airport |  | ES | 49 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 47 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 46 |
| 11 | Tokyo International Airport |  | JP | 44 |
| 12 | Harry Reid International Airport |  | US | 43 |
| 13 | Chicago O'Hare International Airport |  | US | 42 |
| 14 | Macau International Airport |  | MO | 39 |
| 15 | Zurich Airport |  | CH | 37 |
| 16 | Atizapan De Zaragoza Airport |  | MX | 36 |
| 17 | Charlotte/Douglas International Airport |  | US | 34 |
| 18 | Kuala Lumpur International Airport |  | MY | 33 |
| 19 | Miami International Airport |  | US | 32 |
| 20 | Reno/Tahoe International Airport |  | US | 30 |
| 21 | O. R. Tambo International Airport |  | ZA | 30 |
| 22 | Madrid Barajas International Airport |  | ES | 29 |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 24 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 25 | Salt Lake City International Airport |  | US | 28 |
| 26 | Vitoria/Foronda Airport |  | ES | 27 |
| 27 | George Bush Intcntl/Houston Airport |  | US | 27 |
| 28 | Centennial Airport |  | US | 27 |
| 29 | CO86 |  |  | 26 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 26 |
| 31 | Ninoy Aquino International Airport |  | PH | 26 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 26 |
| 33 | Tampa International Airport |  | US | 25 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 35 | Amsterdam Airport Schiphol |  | NL | 25 |
| 36 | Los Angeles International Airport |  | US | 24 |
| 37 | Charles de Gaulle International Airport |  | FR | 24 |
| 38 | Sydney Kingsford Smith International Airport |  | AU | 24 |
| 39 | Bengaluru International Airport |  | IN | 23 |
| 40 | Perales Airport |  | CO | 23 |

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
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 9 | 1h 55m | 1,304 km | 202.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 17 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 18 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 19 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 7 | 4m | - | - |
| 25 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 6 | 1h 49m | - | - |
| 26 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 28 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 6 | 52m | 645 km | 66.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-03-29 22:00 UTC | 2026-03-29 22:29 UTC | 28m |
| YLH | YLH | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-03-29 21:59 UTC | 2026-03-29 22:28 UTC | 29m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-03-29 10:49 UTC | 2026-03-29 22:19 UTC | 11h 29m |
| N22CH |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-03-29 22:02 UTC | 2026-03-29 22:18 UTC | 16m |
| PE993 |  | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-03-29 21:10 UTC | 2026-03-29 22:17 UTC | 1h 7m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-29 10:46 UTC | 2026-03-29 22:13 UTC | 11h 27m |
| ZJO | ZJO | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-03-29 21:43 UTC | 2026-03-29 22:06 UTC | 23m |
| JUMP3 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-03-29 22:04 UTC | 2026-03-29 22:04 UTC | 0m |
| N530FF |  | KU77 (KU77) | KU77 (KU77) | 2026-03-29 21:33 UTC | 2026-03-29 22:02 UTC | 28m |
| N380VR |  | Greenville Mid-Delta Airport (KGLH) | Indianola Municipal Airport (KIDL) | 2026-03-29 21:49 UTC | 2026-03-29 22:00 UTC | 10m |
| N405SA |  | K5T6 (K5T6) | Luna Landing Airport (NM26) | 2026-03-29 20:59 UTC | 2026-03-29 21:58 UTC | 59m |
| N163BF |  | Schwartz Farms Inc Airport (4FL8) | Albert Whitted Airport (KSPG) | 2026-03-29 21:36 UTC | 2026-03-29 21:57 UTC | 21m |
| N459M |  | Fond Du Lac County Airport (KFLD) | Scottsdale Airport (KSDL) | 2026-03-29 18:39 UTC | 2026-03-29 21:57 UTC | 3h 17m |
| N333PN |  | Baker & Hall Airport (77CL) | 9CL4 (9CL4) | 2026-03-29 21:10 UTC | 2026-03-29 21:55 UTC | 44m |
| N499DL |  | Centennial Airport (KAPA) | Lone Tree Ranch Airport (35CO) | 2026-03-29 21:32 UTC | 2026-03-29 21:53 UTC | 21m |
| N724VB |  | William P Hobby Airport (KHOU) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-03-29 21:02 UTC | 2026-03-29 21:48 UTC | 45m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-29 21:19 UTC | 2026-03-29 21:48 UTC | 28m |
| N71JT |  | Rosenberg Airport (MY80) | Estherville Municipal Airport (KEST) | 2026-03-29 21:12 UTC | 2026-03-29 21:48 UTC | 35m |
| N737JA |  | Watsonville Municipal Airport (KWVI) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-03-29 21:16 UTC | 2026-03-29 21:46 UTC | 29m |
| NJL | NJL | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-03-29 21:21 UTC | 2026-03-29 21:45 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
