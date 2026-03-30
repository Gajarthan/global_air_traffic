# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_12:24:21_UTC-green)

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

**Latest saved flight:** 2026-03-30 12:24:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 12:24:21 UTC

- **4,276** saved flights
- **3,042** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,276** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **56,615.6 tonnes** estimated CO2 emissions
- **3,282,062 km** total distance flown
- **898 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 158 |
| 3 | IndiGo | 114 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 71 |
| 7 | Lufthansa | 64 |
| 8 | ENY | 63 |
| 9 | AXM | 56 |
| 10 | Vueling | 46 |
| 11 | LATAM Airlines | 43 |
| 12 | Delta Air Lines | 42 |
| 13 | All Nippon Airways | 39 |
| 14 | Japan Airlines | 37 |
| 15 | LXJ | 37 |
| 16 | QLK | 33 |
| 17 | United Airlines | 33 |
| 18 | Cathay Pacific | 32 |
| 19 | VIV | 32 |
| 20 | Swiss International | 31 |
| 21 | AXB | 30 |
| 22 | Avianca | 29 |
| 23 | EDV | 27 |
| 24 | WIF | 27 |
| 25 | Alaska Airlines | 25 |
| 26 | AZU | 24 |
| 27 | VOE | 23 |
| 28 | ARE | 21 |
| 29 | MXY | 21 |
| 30 | Wizz Air | 21 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3607 |
| 2 | 🇮🇳 IN | 345 |
| 3 | 🇪🇸 ES | 328 |
| 4 | 🇦🇺 AU | 287 |
| 5 | 🇯🇵 JP | 252 |
| 6 | 🇨🇴 CO | 239 |
| 7 | 🇩🇪 DE | 197 |
| 8 | 🇧🇷 BR | 197 |
| 9 | 🇮🇹 IT | 189 |
| 10 | 🇨🇦 CA | 167 |
| 11 | 🇲🇽 MX | 163 |
| 12 | 🇬🇧 GB | 147 |
| 13 | 🇲🇾 MY | 123 |
| 14 | 🇫🇷 FR | 121 |
| 15 | 🇿🇦 ZA | 111 |
| 16 | 🇵🇭 PH | 105 |
| 17 | 🇨🇭 CH | 99 |
| 18 | 🇬🇹 GT | 98 |
| 19 | 🇳🇴 NO | 90 |
| 20 | 🇬🇷 GR | 85 |
| 21 | 🇹🇷 TR | 70 |
| 22 | 🇹🇭 TH | 65 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇲🇴 MO | 57 |
| 25 | 🇮🇩 ID | 55 |
| 26 | 🇵🇱 PL | 53 |
| 27 | 🇰🇷 KR | 51 |
| 28 | 🇲🇦 MA | 49 |
| 29 | 🇧🇸 BS | 46 |
| 30 | 🇫🇮 FI | 42 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 88 |
| 3 | Tokyo International Airport |  | JP | 85 |
| 4 | Denver International Airport |  | US | 81 |
| 5 | Indira Gandhi International Airport |  | IN | 79 |
| 6 | Frankfurt am Main International Airport |  | DE | 66 |
| 7 | La Aurora Airport |  | GT | 64 |
| 8 | Macau International Airport |  | MO | 57 |
| 9 | Tenerife Norte Airport |  | ES | 54 |
| 10 | Guaymaral Airport |  | CO | 54 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 51 |
| 13 | Zurich Airport |  | CH | 51 |
| 14 | Harry Reid International Airport |  | US | 49 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 16 | Ninoy Aquino International Airport |  | PH | 46 |
| 17 | Chicago O'Hare International Airport |  | US | 45 |
| 18 | Kuala Lumpur International Airport |  | MY | 45 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 42 |
| 20 | Madrid Barajas International Airport |  | ES | 39 |
| 21 | Eleftherios Venizelos International Airport |  | GR | 38 |
| 22 | Charlotte/Douglas International Airport |  | US | 38 |
| 23 | O. R. Tambo International Airport |  | ZA | 38 |
| 24 | Bengaluru International Airport |  | IN | 35 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 34 |
| 26 | Reno/Tahoe International Airport |  | US | 33 |
| 27 | Miami International Airport |  | US | 33 |
| 28 | Vitoria/Foronda Airport |  | ES | 33 |
| 29 | Los Angeles International Airport |  | US | 32 |
| 30 | Charles de Gaulle International Airport |  | FR | 32 |
| 31 | Centennial Airport |  | US | 32 |
| 32 | Amsterdam Airport Schiphol |  | NL | 31 |
| 33 | Salt Lake City International Airport |  | US | 31 |
| 34 | Daniel K Inouye International Airport |  | US | 30 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 30 |
| 36 | Malpensa International Airport |  | IT | 30 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 29 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 39 | CO86 |  |  | 28 |
| 40 | Tampa International Airport |  | US | 28 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 27 | 14m | 114 km | 53.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 17 | 30m | - | - |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 14 | 1h 40m | 1,423 km | 343.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 9 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 11 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 13 | 21m | 165 km | 37.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 12 | 15m | 206 km | 42.7 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 19 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 20 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 10 | 4m | - | - |
| 24 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |
| 25 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 9 | 8h 21m | 38 km | 5.9 t |
| 26 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 8 | 1h 58m | 1,156 km | 159.6 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 29 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-03-30 12:09 UTC | 2026-03-30 12:24 UTC | 14m |
| CHH758 | CHH | Charles de Gaulle International Airport (LFPG) | Smolensk North Airport (XUBS) | 2026-03-30 09:50 UTC | 2026-03-30 12:21 UTC | 2h 31m |
| GPD433 | GPD | General Edward Lawrence Logan International Airport (KBOS) | Teterboro Airport (KTEB) | 2026-03-30 11:25 UTC | 2026-03-30 12:15 UTC | 50m |
| N773SD |  | Joe Foss Field (KFSD) | Brookings Regional Airport (KBKX) | 2026-03-30 11:56 UTC | 2026-03-30 12:12 UTC | 15m |
| TJT35DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-03-30 10:42 UTC | 2026-03-30 12:06 UTC | 1h 24m |
| N441WF |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Las Animas - Bent County Airport (K7V9) | 2026-03-30 11:41 UTC | 2026-03-30 12:04 UTC | 23m |
| N490LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-03-30 10:43 UTC | 2026-03-30 12:03 UTC | 1h 19m |
| N97HL |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-03-30 11:37 UTC | 2026-03-30 12:01 UTC | 24m |
| N495LP |  | K00V (K00V) | Lone Tree Ranch Airport (35CO) | 2026-03-30 11:33 UTC | 2026-03-30 11:58 UTC | 25m |
| AJD19ST | AJD | Paris-Le Bourget Airport (LFPB) | Rotterdam Airport (EHRD) | 2026-03-30 11:07 UTC | 2026-03-30 11:56 UTC | 48m |
| IOS512N | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-03-30 11:19 UTC | 2026-03-30 11:53 UTC | 33m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-03-30 10:51 UTC | 2026-03-30 11:50 UTC | 59m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-03-30 07:33 UTC | 2026-03-30 11:49 UTC | 4h 15m |
|  |  | Wauchula Municipal Airport (KCHN) | Wauchula Municipal Airport (KCHN) | 2026-03-30 11:46 UTC | 2026-03-30 11:47 UTC | 0m |
| FRA30 | FRA | RAF Northolt (EGWU) | Cranfield Airport (EGTC) | 2026-03-30 10:19 UTC | 2026-03-30 11:47 UTC | 1h 27m |
| THY8UZ | Turkish Airlines | Ataturk International Airport (LTBA) | Adana Airport (LTAF) | 2026-03-30 10:48 UTC | 2026-03-30 11:47 UTC | 58m |
| CPA331 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-30 04:33 UTC | 2026-03-30 11:44 UTC | 7h 10m |
| IAM1482 | IAM | Pratica Di Mare Airport (LIRE) | Brindisi / Casale Airport (LIBR) | 2026-03-30 10:47 UTC | 2026-03-30 11:42 UTC | 54m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | 7CO1 (7CO1) | 2026-03-30 11:16 UTC | 2026-03-30 11:38 UTC | 21m |
| RYR19SR | Ryanair | Brussels South Charleroi Airport (EBCI) | Niksic Airport (LYNK) | 2026-03-30 09:54 UTC | 2026-03-30 11:36 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
