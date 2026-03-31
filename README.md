# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_15:04:57_UTC-green)

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

**Latest saved flight:** 2026-03-31 15:04:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 15:04:57 UTC

- **6,706** saved flights
- **4,371** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,706** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **84,786.0 tonnes** estimated CO2 emissions
- **4,915,132 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 313 |
| 2 | Ryanair | 256 |
| 3 | IndiGo | 186 |
| 4 | EJA | 136 |
| 5 | American Airlines | 124 |
| 6 | Lufthansa | 107 |
| 7 | Southwest Airlines | 101 |
| 8 | ENY | 93 |
| 9 | AXM | 78 |
| 10 | LATAM Airlines | 72 |
| 11 | Vueling | 68 |
| 12 | LXJ | 58 |
| 13 | All Nippon Airways | 57 |
| 14 | Delta Air Lines | 57 |
| 15 | QLK | 56 |
| 16 | WIF | 54 |
| 17 | Swiss International | 52 |
| 18 | VIV | 49 |
| 19 | AXB | 48 |
| 20 | Cathay Pacific | 47 |
| 21 | Japan Airlines | 47 |
| 22 | United Airlines | 47 |
| 23 | AZU | 45 |
| 24 | EDV | 41 |
| 25 | Alaska Airlines | 40 |
| 26 | Avianca | 40 |
| 27 | EJU | 37 |
| 28 | AEE | 35 |
| 29 | easyJet | 35 |
| 30 | VOE | 35 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5576 |
| 2 | 🇮🇳 IN | 565 |
| 3 | 🇪🇸 ES | 509 |
| 4 | 🇦🇺 AU | 508 |
| 5 | 🇩🇪 DE | 343 |
| 6 | 🇯🇵 JP | 337 |
| 7 | 🇧🇷 BR | 333 |
| 8 | 🇨🇴 CO | 313 |
| 9 | 🇮🇹 IT | 308 |
| 10 | 🇨🇦 CA | 281 |
| 11 | 🇲🇽 MX | 236 |
| 12 | 🇬🇧 GB | 230 |
| 13 | 🇫🇷 FR | 208 |
| 14 | 🇳🇴 NO | 178 |
| 15 | 🇲🇾 MY | 176 |
| 16 | 🇨🇭 CH | 163 |
| 17 | 🇿🇦 ZA | 159 |
| 18 | 🇬🇷 GR | 158 |
| 19 | 🇬🇹 GT | 136 |
| 20 | 🇵🇭 PH | 132 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 110 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇮🇩 ID | 89 |
| 25 | 🇲🇦 MA | 83 |
| 26 | 🇵🇱 PL | 83 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇳🇱 NL | 66 |
| 30 | 🇲🇪 ME | 66 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 166 |
| 2 | Indira Gandhi International Airport |  | IN | 129 |
| 3 | Denver International Airport |  | US | 124 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 116 |
| 6 | Frankfurt am Main International Airport |  | DE | 107 |
| 7 | La Aurora Airport |  | GT | 92 |
| 8 | Zurich Airport |  | CH | 84 |
| 9 | Harry Reid International Airport |  | US | 83 |
| 10 | Macau International Airport |  | MO | 81 |
| 11 | Chicago O'Hare International Airport |  | US | 77 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 75 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 72 |
| 16 | Guaymaral Airport |  | CO | 69 |
| 17 | Tenerife Norte Airport |  | ES | 68 |
| 18 | Kuala Lumpur International Airport |  | MY | 64 |
| 19 | Madrid Barajas International Airport |  | ES | 62 |
| 20 | Bengaluru International Airport |  | IN | 62 |
| 21 | Reno/Tahoe International Airport |  | US | 59 |
| 22 | Ninoy Aquino International Airport |  | PH | 59 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 55 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 53 |
| 25 | Malpensa International Airport |  | IT | 52 |
| 26 | Charlotte/Douglas International Airport |  | US | 51 |
| 27 | Charles de Gaulle International Airport |  | FR | 51 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 51 |
| 29 | Vitoria/Foronda Airport |  | ES | 50 |
| 30 | Salt Lake City International Airport |  | US | 49 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 32 | Miami International Airport |  | US | 46 |
| 33 | Congonhas Airport |  | BR | 46 |
| 34 | O. R. Tambo International Airport |  | ZA | 46 |
| 35 | Amsterdam Airport Schiphol |  | NL | 45 |
| 36 | Pune Airport |  | IN | 45 |
| 37 | Daniel K Inouye International Airport |  | US | 44 |
| 38 | Seattle-Tacoma International Airport |  | US | 44 |
| 39 | Centennial Airport |  | US | 43 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 42 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 27 | 26m | - | - |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 20 | 24m | 99 km | 34.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 19 | 1h 48m | 1,156 km | 379.0 t |
| 11 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 19 | 1h 42m | 1,423 km | 466.3 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 18 | 5m | - | - |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 17 | 15m | 206 km | 60.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 17 | 29m | 275 km | 80.6 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 20 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
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
| N916BQ |  | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-03-31 14:08 UTC | 2026-03-31 15:04 UTC | 56m |
| HTY252 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-03-31 14:38 UTC | 2026-03-31 15:03 UTC | 24m |
| N709LU |  | New London Airport (KW90) | Brookneal/Campbell County Airport (K0V4) | 2026-03-31 14:35 UTC | 2026-03-31 15:00 UTC | 24m |
| TGRIO | TGR | San Jose Airport (MGSJ) | La Aurora Airport (MGGT) | 2026-03-31 14:48 UTC | 2026-03-31 14:59 UTC | 10m |
| N4381L |  | Trenton-Robbinsville Airport (KN87) | Princeton Airport (K39N) | 2026-03-31 14:38 UTC | 2026-03-31 14:59 UTC | 20m |
| DESRT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-03-31 14:46 UTC | 2026-03-31 14:57 UTC | 10m |
| CXK219 | CXK | Greenville Downtown Airport (KGMU) | Pickens County Airport (KLQK) | 2026-03-31 14:39 UTC | 2026-03-31 14:55 UTC | 15m |
| N8VB |  | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-03-31 14:06 UTC | 2026-03-31 14:53 UTC | 47m |
| IBE04GH | Iberia | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-03-31 14:02 UTC | 2026-03-31 14:52 UTC | 50m |
| BOMR710 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-03-31 13:56 UTC | 2026-03-31 14:51 UTC | 55m |
| LLN103 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | 69XA (69XA) | 2026-03-31 14:03 UTC | 2026-03-31 14:50 UTC | 46m |
| IGO257M | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-31 12:43 UTC | 2026-03-31 14:45 UTC | 2h 2m |
| ERU944 | ERU | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-03-31 14:30 UTC | 2026-03-31 14:42 UTC | 11m |
| BOMR730 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-03-31 14:14 UTC | 2026-03-31 14:40 UTC | 26m |
| AWH124 | AWH | Hannover Airport (EDDV) | Hannover Airport (EDDV) | 2026-03-31 13:41 UTC | 2026-03-31 14:37 UTC | 56m |
| N414EP |  | Bellingham International Airport (KBLI) | Boeing Field/King County International Airport (KBFI) | 2026-03-31 14:06 UTC | 2026-03-31 14:37 UTC | 31m |
| UPS7845 | UPS | Fort Lauderdale/Hollywood International Airport (KFLL) | Dallas-Fort Worth International Airport (KDFW) | 2026-03-31 11:51 UTC | 2026-03-31 14:36 UTC | 2h 45m |
| N265BL |  | North Fork Valley Airport (K7V2) | CD97 (CD97) | 2026-03-31 14:23 UTC | 2026-03-31 14:36 UTC | 13m |
| N3049D |  | Clermont County Airport (KI69) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-03-31 14:27 UTC | 2026-03-31 14:31 UTC | 3m |
| DESRT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-03-31 14:19 UTC | 2026-03-31 14:31 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
