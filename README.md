# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_20:18:37_UTC-green)

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

**Latest saved flight:** 2026-04-01 20:18:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 20:18:37 UTC

- **9,613** saved flights
- **5,772** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,613** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **115,777.6 tonnes** estimated CO2 emissions
- **6,711,744 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 436 |
| 2 | Ryanair | 371 |
| 3 | IndiGo | 263 |
| 4 | EJA | 198 |
| 5 | American Airlines | 175 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 146 |
| 8 | ENY | 134 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 93 |
| 12 | LXJ | 89 |
| 13 | All Nippon Airways | 80 |
| 14 | WIF | 79 |
| 15 | Delta Air Lines | 74 |
| 16 | Swiss International | 72 |
| 17 | QLK | 70 |
| 18 | AZU | 66 |
| 19 | VIV | 66 |
| 20 | AXB | 63 |
| 21 | Alaska Airlines | 60 |
| 22 | Japan Airlines | 60 |
| 23 | EDV | 59 |
| 24 | United Airlines | 59 |
| 25 | BRC | 58 |
| 26 | EJU | 55 |
| 27 | easyJet | 54 |
| 28 | Avianca | 52 |
| 29 | AEE | 50 |
| 30 | Cathay Pacific | 49 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7949 |
| 2 | 🇮🇳 IN | 806 |
| 3 | 🇪🇸 ES | 757 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 524 |
| 6 | 🇧🇷 BR | 484 |
| 7 | 🇨🇴 CO | 470 |
| 8 | 🇨🇦 CA | 465 |
| 9 | 🇯🇵 JP | 463 |
| 10 | 🇮🇹 IT | 430 |
| 11 | 🇬🇧 GB | 344 |
| 12 | 🇲🇽 MX | 338 |
| 13 | 🇫🇷 FR | 298 |
| 14 | 🇳🇴 NO | 259 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 226 |
| 17 | 🇨🇭 CH | 224 |
| 18 | 🇿🇦 ZA | 203 |
| 19 | 🇳🇿 NZ | 201 |
| 20 | 🇬🇹 GT | 198 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇹🇷 TR | 159 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 127 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 114 |
| 27 | 🇹🇭 TH | 113 |
| 28 | 🇲🇪 ME | 94 |
| 29 | 🇧🇸 BS | 93 |
| 30 | 🇲🇴 MO | 93 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 231 |
| 2 | Indira Gandhi International Airport |  | IN | 177 |
| 3 | Denver International Airport |  | US | 170 |
| 4 | Tokyo International Airport |  | JP | 166 |
| 5 | Frankfurt am Main International Airport |  | DE | 166 |
| 6 | El Dorado International Airport |  | CO | 152 |
| 7 | La Aurora Airport |  | GT | 140 |
| 8 | Guaymaral Airport |  | CO | 137 |
| 9 | Harry Reid International Airport |  | US | 131 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 114 |
| 11 | Zurich Airport |  | CH | 112 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Chicago O'Hare International Airport |  | US | 101 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 96 |
| 16 | Macau International Airport |  | MO | 93 |
| 17 | Tenerife Norte Airport |  | ES | 91 |
| 18 | Madrid Barajas International Airport |  | ES | 89 |
| 19 | Bengaluru International Airport |  | IN | 87 |
| 20 | Charlotte/Douglas International Airport |  | US | 86 |
| 21 | Reno/Tahoe International Airport |  | US | 86 |
| 22 | Kuala Lumpur International Airport |  | MY | 85 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 81 |
| 24 | Ninoy Aquino International Airport |  | PH | 78 |
| 25 | Malpensa International Airport |  | IT | 73 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 73 |
| 27 | Congonhas Airport |  | BR | 72 |
| 28 | Vitoria/Foronda Airport |  | ES | 71 |
| 29 | Pune Airport |  | IN | 70 |
| 30 | Daniel K Inouye International Airport |  | US | 69 |
| 31 | Salt Lake City International Airport |  | US | 69 |
| 32 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 69 |
| 33 | Barcelona International Airport |  | ES | 68 |
| 34 | Charles de Gaulle International Airport |  | FR | 67 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 67 |
| 36 | Seattle-Tacoma International Airport |  | US | 65 |
| 37 | Miami International Airport |  | US | 63 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 63 |
| 39 | Bodø Airport |  | NO | 63 |
| 40 | Austin-Bergstrom International Airport |  | US | 61 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 55 | 28m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 44 | 14m | 114 km | 86.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 29 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 27 | 22m | 99 km | 46.2 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 25 | 15m | 206 km | 88.9 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 24 | 52m | 556 km | 230.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
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
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 14 | 13m | 99 km | 24.0 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG621 | BRG | Shungnak Airport (PAGH) | Ambler Airport (PAFM) | 2026-04-01 20:08 UTC | 2026-04-01 20:18 UTC | 10m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-01 20:05 UTC | 2026-04-01 20:18 UTC | 12m |
| ANA968 | All Nippon Airways | Nagasaki Airport (RJFU) | Tokyo International Airport (RJTT) | 2026-04-01 19:05 UTC | 2026-04-01 20:17 UTC | 1h 11m |
| QTR8762 | Qatar Airways | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-01 07:27 UTC | 2026-04-01 20:07 UTC | 12h 39m |
| LSXX | LSX | Lake Wohlford Resort Airport (8CL1) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 19:31 UTC | 2026-04-01 20:04 UTC | 32m |
| KPO47 | KPO | Marco Island Executive Airport (KMKY) | Toronto Pearson International Airport (CYYZ) | 2026-04-01 17:06 UTC | 2026-04-01 19:56 UTC | 2h 50m |
| N916LF |  | Patrick Leahy Burlington International Airport (KBTV) | Secret Spot Airport (3NK5) | 2026-04-01 19:38 UTC | 2026-04-01 19:53 UTC | 14m |
| OXF2087 | OXF | Falcon Field (KFFZ) | Marana Regional Airport (KAVQ) | 2026-04-01 18:44 UTC | 2026-04-01 19:51 UTC | 1h 6m |
| N1727L |  | Mckinney Ntl Airport (KTKI) | J Ranch Airport (41TX) | 2026-04-01 19:26 UTC | 2026-04-01 19:49 UTC | 22m |
| N976CT |  | Newnan Coweta County Airport (KCCO) | 7GE5 (7GE5) | 2026-04-01 19:34 UTC | 2026-04-01 19:46 UTC | 12m |
| N605WM |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-01 19:15 UTC | 2026-04-01 19:45 UTC | 29m |
| C6565 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-04-01 19:43 UTC | 2026-04-01 19:44 UTC | 0m |
| CGDFN | CGD | Thunder Bay Airport (CYQT) | Thunder Bay Airport (CYQT) | 2026-04-01 18:43 UTC | 2026-04-01 19:43 UTC | 1h 0m |
| N65903 |  | Tacoma Narrows Airport (KTIW) | Boeing Field/King County International Airport (KBFI) | 2026-04-01 18:28 UTC | 2026-04-01 19:42 UTC | 1h 13m |
| EJM5 | EJM | Ziggy's Airport (0ID1) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-01 18:07 UTC | 2026-04-01 19:42 UTC | 1h 34m |
| RYR5605 | Ryanair | Lamezia Terme Airport (LICA) | Saarbrucken Airport (EDDR) | 2026-04-01 17:35 UTC | 2026-04-01 19:36 UTC | 2h 1m |
| N530SE |  | Georgetown Executive Airport (KGTU) | Chaney San Francisco Ranch Airport (92TE) | 2026-04-01 18:51 UTC | 2026-04-01 19:36 UTC | 44m |
| N715WM |  | Cobb County International/Mccollum Field (KRYY) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-04-01 19:20 UTC | 2026-04-01 19:33 UTC | 12m |
| CTN632 | CTN | Zagreb Airport (LDZA) | Sepurine Training Base (LD57) | 2026-04-01 19:10 UTC | 2026-04-01 19:33 UTC | 22m |
| EJA477 | EJA | John Wayne/Orange County Airport (KSNA) | Austin-Bergstrom International Airport (KAUS) | 2026-04-01 17:08 UTC | 2026-04-01 19:28 UTC | 2h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
