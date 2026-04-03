# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_14:50:52_UTC-green)

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

**Latest saved flight:** 2026-04-03 14:50:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 14:50:52 UTC

- **13,390** saved flights
- **7,454** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,390** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **166,336.5 tonnes** estimated CO2 emissions
- **9,642,698 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 560 |
| 2 | Ryanair | 514 |
| 3 | IndiGo | 387 |
| 4 | EJA | 256 |
| 5 | American Airlines | 238 |
| 6 | Lufthansa | 205 |
| 7 | Southwest Airlines | 191 |
| 8 | ENY | 167 |
| 9 | Vueling | 142 |
| 10 | AXM | 141 |
| 11 | LATAM Airlines | 136 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 103 |
| 16 | Swiss International | 103 |
| 17 | AZU | 102 |
| 18 | VIV | 97 |
| 19 | WIF | 97 |
| 20 | Japan Airlines | 88 |
| 21 | Alaska Airlines | 87 |
| 22 | AXB | 87 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 83 |
| 26 | EJU | 82 |
| 27 | EDV | 79 |
| 28 | AEE | 78 |
| 29 | BRC | 74 |
| 30 | GLO | 73 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10507 |
| 2 | 🇮🇳 IN | 1185 |
| 3 | 🇦🇺 AU | 1078 |
| 4 | 🇪🇸 ES | 1024 |
| 5 | 🇧🇷 BR | 763 |
| 6 | 🇯🇵 JP | 722 |
| 7 | 🇩🇪 DE | 722 |
| 8 | 🇨🇴 CO | 631 |
| 9 | 🇨🇦 CA | 613 |
| 10 | 🇮🇹 IT | 594 |
| 11 | 🇬🇧 GB | 515 |
| 12 | 🇲🇽 MX | 471 |
| 13 | 🇫🇷 FR | 464 |
| 14 | 🇬🇷 GR | 360 |
| 15 | 🇨🇭 CH | 351 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 317 |
| 18 | 🇳🇴 NO | 310 |
| 19 | 🇿🇦 ZA | 283 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇬🇹 GT | 245 |
| 22 | 🇹🇷 TR | 244 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 187 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇮🇩 ID | 166 |
| 27 | 🇲🇦 MA | 162 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇲🇪 ME | 140 |
| 30 | 🇳🇱 NL | 134 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 318 |
| 2 | Tokyo International Airport |  | JP | 253 |
| 3 | Indira Gandhi International Airport |  | IN | 251 |
| 4 | Denver International Airport |  | US | 234 |
| 5 | El Dorado International Airport |  | CO | 222 |
| 6 | Frankfurt am Main International Airport |  | DE | 194 |
| 7 | Harry Reid International Airport |  | US | 182 |
| 8 | La Aurora Airport |  | GT | 169 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 165 |
| 10 | Zurich Airport |  | CH | 162 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 154 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Bengaluru International Airport |  | IN | 132 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 127 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 121 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 118 |
| 20 | Congonhas Airport |  | BR | 118 |
| 21 | Madrid Barajas International Airport |  | ES | 117 |
| 22 | Kuala Lumpur International Airport |  | MY | 116 |
| 23 | Charlotte/Douglas International Airport |  | US | 114 |
| 24 | Tenerife Norte Airport |  | ES | 108 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 107 |
| 26 | Vitoria/Foronda Airport |  | ES | 102 |
| 27 | Charles de Gaulle International Airport |  | FR | 98 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 98 |
| 29 | Salt Lake City International Airport |  | US | 98 |
| 30 | Daniel K Inouye International Airport |  | US | 97 |
| 31 | Reno/Tahoe International Airport |  | US | 97 |
| 32 | Malpensa International Airport |  | IT | 96 |
| 33 | Barcelona International Airport |  | ES | 93 |
| 34 | Pune Airport |  | IN | 91 |
| 35 | Gimpo International Airport |  | KR | 86 |
| 36 | Seattle-Tacoma International Airport |  | US | 86 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 38 | Austin-Bergstrom International Airport |  | US | 85 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 80 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 62 | 14m | 114 km | 121.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 41 | 1h 45m | 1,156 km | 817.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 35 | 22m | 99 km | 60.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 31 | 28m | 275 km | 146.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 28 | 1h 55m | 1,304 km | 629.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 19 | 20m | 250 km | 82.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TTW606 | TTW | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-04-03 08:47 UTC | 2026-04-03 14:50 UTC | 6h 3m |
| FHVYC | FHV | Malaga Airport (LEMG) | Melsbroek Air Base (EBMB) | 2026-04-03 12:00 UTC | 2026-04-03 14:47 UTC | 2h 46m |
| N2157H |  | Glendale Regional Airport (KGEU) | Coolidge Municipal Airport (KP08) | 2026-04-03 14:07 UTC | 2026-04-03 14:46 UTC | 39m |
| CAL5225 | CAL | Ted Stevens Anchorage International Airport (PANC) | Taiwan Taoyuan International Airport (RCTP) | 2026-04-03 04:56 UTC | 2026-04-03 14:45 UTC | 9h 48m |
| TTW203 | TTW | Narita International Airport (RJAA) | Longtan Air Base (RCDI) | 2026-04-03 11:27 UTC | 2026-04-03 14:42 UTC | 3h 14m |
| HBPKG | HBP | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-04-03 14:16 UTC | 2026-04-03 14:39 UTC | 22m |
| N691RM |  | Pribram Airport (LKPM) | St. Johann In Tirol Airport (LOIJ) | 2026-04-03 13:14 UTC | 2026-04-03 14:38 UTC | 1h 24m |
| NL851D |  | Kissimmee Gateway Airport (KISM) | Bartow Executive Airport (KBOW) | 2026-04-03 14:17 UTC | 2026-04-03 14:38 UTC | 20m |
| N216DA |  | Charleston Afb/International Airport (KCHS) | Berkeley County Airport (KMKS) | 2026-04-03 14:10 UTC | 2026-04-03 14:33 UTC | 23m |
| SHINR81 | SHI | Flysooner Field (OK50) | Enix Airport (OK51) | 2026-04-03 13:53 UTC | 2026-04-03 14:31 UTC | 37m |
| IGREI | IGR | Torino / Aeritalia Airport (LIMA) | Torino / Aeritalia Airport (LIMA) | 2026-04-03 13:59 UTC | 2026-04-03 14:31 UTC | 32m |
| VEGA21 | VEG | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-04-03 14:02 UTC | 2026-04-03 14:30 UTC | 28m |
| SCA43 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-03 14:17 UTC | 2026-04-03 14:29 UTC | 11m |
| AXLE11 | AXL | Enix Airport (OK51) | Flying E Ranch Airport (OK16) | 2026-04-03 13:59 UTC | 2026-04-03 14:29 UTC | 29m |
| BOMR723 | BOM | XS10 (XS10) | Kalt Ranch Airport (9TE5) | 2026-04-03 14:15 UTC | 2026-04-03 14:27 UTC | 12m |
| CXK543 | CXK | Mesa Gateway Airport (KIWA) | Mesa Gateway Airport (KIWA) | 2026-04-03 13:10 UTC | 2026-04-03 14:27 UTC | 1h 17m |
| YLERA | YLE | S. Darius and S. Girenas Airport (EYKS) | S. Darius and S. Girenas Airport (EYKS) | 2026-04-03 14:16 UTC | 2026-04-03 14:17 UTC | 0m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-03 14:06 UTC | 2026-04-03 14:16 UTC | 9m |
| SHARP41 | SHA | 75OK (75OK) | Flying E Ranch Airport (OK16) | 2026-04-03 13:44 UTC | 2026-04-03 14:11 UTC | 27m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-03 13:57 UTC | 2026-04-03 14:11 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
