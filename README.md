# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_18:15:17_UTC-green)

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

**Latest saved flight:** 2026-03-31 18:15:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 18:15:17 UTC

- **7,149** saved flights
- **4,620** unique routes
- **106** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,149** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **89,469.3 tonnes** estimated CO2 emissions
- **5,186,625 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 331 |
| 2 | Ryanair | 273 |
| 3 | IndiGo | 196 |
| 4 | EJA | 144 |
| 5 | American Airlines | 132 |
| 6 | Lufthansa | 112 |
| 7 | Southwest Airlines | 111 |
| 8 | ENY | 100 |
| 9 | AXM | 78 |
| 10 | LATAM Airlines | 73 |
| 11 | Vueling | 72 |
| 12 | LXJ | 63 |
| 13 | Delta Air Lines | 61 |
| 14 | WIF | 58 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 50 |
| 19 | VIV | 50 |
| 20 | Cathay Pacific | 47 |
| 21 | Japan Airlines | 47 |
| 22 | United Airlines | 47 |
| 23 | EDV | 46 |
| 24 | AZU | 45 |
| 25 | Alaska Airlines | 44 |
| 26 | Avianca | 42 |
| 27 | AEE | 39 |
| 28 | BRC | 39 |
| 29 | EJU | 39 |
| 30 | easyJet | 39 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6033 |
| 2 | 🇮🇳 IN | 595 |
| 3 | 🇪🇸 ES | 545 |
| 4 | 🇦🇺 AU | 508 |
| 5 | 🇩🇪 DE | 370 |
| 6 | 🇧🇷 BR | 352 |
| 7 | 🇯🇵 JP | 338 |
| 8 | 🇨🇴 CO | 331 |
| 9 | 🇮🇹 IT | 322 |
| 10 | 🇨🇦 CA | 314 |
| 11 | 🇲🇽 MX | 252 |
| 12 | 🇬🇧 GB | 249 |
| 13 | 🇫🇷 FR | 221 |
| 14 | 🇳🇴 NO | 193 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 173 |
| 17 | 🇨🇭 CH | 167 |
| 18 | 🇿🇦 ZA | 161 |
| 19 | 🇬🇹 GT | 153 |
| 20 | 🇵🇭 PH | 132 |
| 21 | 🇹🇷 TR | 125 |
| 22 | 🇳🇿 NZ | 122 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇲🇦 MA | 91 |
| 25 | 🇮🇩 ID | 89 |
| 26 | 🇵🇱 PL | 88 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 69 |
| 30 | 🇳🇱 NL | 68 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 175 |
| 2 | Indira Gandhi International Airport |  | IN | 135 |
| 3 | Denver International Airport |  | US | 129 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 117 |
| 6 | Frankfurt am Main International Airport |  | DE | 111 |
| 7 | La Aurora Airport |  | GT | 106 |
| 8 | Harry Reid International Airport |  | US | 94 |
| 9 | Zurich Airport |  | CH | 87 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 81 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 81 |
| 12 | Macau International Airport |  | MO | 81 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 80 |
| 14 | Guaymaral Airport |  | CO | 80 |
| 15 | Chicago O'Hare International Airport |  | US | 79 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 17 | Tenerife Norte Airport |  | ES | 71 |
| 18 | Madrid Barajas International Airport |  | ES | 66 |
| 19 | Reno/Tahoe International Airport |  | US | 65 |
| 20 | Bengaluru International Airport |  | IN | 65 |
| 21 | Kuala Lumpur International Airport |  | MY | 65 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 62 |
| 23 | Ninoy Aquino International Airport |  | PH | 59 |
| 24 | Charlotte/Douglas International Airport |  | US | 57 |
| 25 | Malpensa International Airport |  | IT | 55 |
| 26 | Daniel K Inouye International Airport |  | US | 54 |
| 27 | Vitoria/Foronda Airport |  | ES | 54 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 53 |
| 30 | Miami International Airport |  | US | 52 |
| 31 | Charles de Gaulle International Airport |  | FR | 52 |
| 32 | Salt Lake City International Airport |  | US | 52 |
| 33 | Congonhas Airport |  | BR | 52 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 52 |
| 35 | Pune Airport |  | IN | 47 |
| 36 | Seattle-Tacoma International Airport |  | US | 47 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 47 |
| 38 | O. R. Tambo International Airport |  | ZA | 47 |
| 39 | Barcelona International Airport |  | ES | 46 |
| 40 | Amsterdam Airport Schiphol |  | NL | 45 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 32 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 24 | 26m | 152 km | 62.7 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 21 | 24m | 99 km | 36.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 20 | 1h 47m | 1,156 km | 399.0 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 19 | 15m | 206 km | 67.5 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 18 | 28m | 275 km | 85.3 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 16 | 51m | 556 km | 153.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 21 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 14 | 8m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 13 | 22m | - | - |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 12 | 1h 1m | 723 km | 149.6 t |
| 29 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 12 | 54m | 630 km | 130.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEVIL33 | DEV | Hughes Ranch Airport (50XS) | Maverick County Memorial International Airport (K5T9) | 2026-03-31 18:04 UTC | 2026-03-31 18:15 UTC | 10m |
| BOMR730 | BOM | Green Lake Ranch Airport (69TX) | San Jose Island Airport (XS67) | 2026-03-31 17:44 UTC | 2026-03-31 18:10 UTC | 25m |
| N365PC |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-03-31 17:05 UTC | 2026-03-31 18:02 UTC | 57m |
| BURNY31 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-03-31 17:41 UTC | 2026-03-31 18:01 UTC | 19m |
| EVANS11 | EVA Air | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-03-31 17:05 UTC | 2026-03-31 18:01 UTC | 55m |
| N3459R |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-03-31 17:46 UTC | 2026-03-31 18:01 UTC | 14m |
| N380LA |  | Bridgeport Municipal Airport (KXBP) | Richards Airport (TA47) | 2026-03-31 17:10 UTC | 2026-03-31 18:00 UTC | 49m |
| N939SP |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-03-31 17:41 UTC | 2026-03-31 17:58 UTC | 16m |
| GPD202 | GPD | Norfolk International Airport (KORF) | Lehigh Valley International Airport (KABE) | 2026-03-31 16:58 UTC | 2026-03-31 17:57 UTC | 58m |
| LXJ600 | LXJ | Moffett Federal Airfield (KNUQ) | San Francisco International Airport (KSFO) | 2026-03-31 17:40 UTC | 2026-03-31 17:57 UTC | 16m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-03-31 17:08 UTC | 2026-03-31 17:55 UTC | 47m |
| ARCAS24 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-03-31 17:39 UTC | 2026-03-31 17:54 UTC | 14m |
| BRG650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-03-31 17:27 UTC | 2026-03-31 17:54 UTC | 26m |
| CXK1144 | CXK | Smyrna Airport (KMQY) | Cedar Crest Field (1TN0) | 2026-03-31 17:08 UTC | 2026-03-31 17:51 UTC | 42m |
| CGMJT | CGM | North Battleford Airport (CYQW) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-03-31 17:23 UTC | 2026-03-31 17:51 UTC | 27m |
| N510PA |  | Fall City Airport (1WA6) | Fall City Airport (1WA6) | 2026-03-31 17:14 UTC | 2026-03-31 17:49 UTC | 35m |
| N485BL |  | Johnston Regional Airport (KJNX) | Rondo Airport (NC76) | 2026-03-31 17:12 UTC | 2026-03-31 17:46 UTC | 34m |
| N7433G |  | Northwest Alabama Regional Airport (KMSL) | Wilson Creek Airport (0AL9) | 2026-03-31 17:20 UTC | 2026-03-31 17:46 UTC | 25m |
| N4405T |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-03-31 17:29 UTC | 2026-03-31 17:42 UTC | 12m |
| N641MC |  | Houma-Terrebonne Airport (KHUM) | Hesler/Noble Field (KLUL) | 2026-03-31 17:08 UTC | 2026-03-31 17:41 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
