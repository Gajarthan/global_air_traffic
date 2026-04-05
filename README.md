# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_13:20:19_UTC-green)

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

**Latest saved flight:** 2026-04-05 13:20:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 13:20:19 UTC

- **17,889** saved flights
- **9,204** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,889** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **227,123.1 tonnes** estimated CO2 emissions
- **13,166,556 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 727 |
| 3 | IndiGo | 519 |
| 4 | EJA | 328 |
| 5 | American Airlines | 324 |
| 6 | Lufthansa | 253 |
| 7 | Southwest Airlines | 248 |
| 8 | ENY | 234 |
| 9 | Vueling | 200 |
| 10 | LATAM Airlines | 189 |
| 11 | AXM | 188 |
| 12 | All Nippon Airways | 161 |
| 13 | QLK | 154 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 149 |
| 16 | Swiss International | 134 |
| 17 | AZU | 133 |
| 18 | VIV | 131 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 119 |
| 22 | United Airlines | 117 |
| 23 | Avianca | 115 |
| 24 | AEE | 114 |
| 25 | AXB | 112 |
| 26 | EJU | 111 |
| 27 | EDV | 108 |
| 28 | Cathay Pacific | 104 |
| 29 | WIF | 104 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13947 |
| 2 | 🇮🇳 IN | 1580 |
| 3 | 🇪🇸 ES | 1483 |
| 4 | 🇦🇺 AU | 1308 |
| 5 | 🇧🇷 BR | 1022 |
| 6 | 🇯🇵 JP | 993 |
| 7 | 🇩🇪 DE | 933 |
| 8 | 🇨🇴 CO | 920 |
| 9 | 🇮🇹 IT | 832 |
| 10 | 🇨🇦 CA | 781 |
| 11 | 🇬🇧 GB | 706 |
| 12 | 🇫🇷 FR | 649 |
| 13 | 🇲🇽 MX | 609 |
| 14 | 🇬🇷 GR | 506 |
| 15 | 🇨🇭 CH | 477 |
| 16 | 🇲🇾 MY | 432 |
| 17 | 🇿🇦 ZA | 397 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇵🇭 PH | 350 |
| 20 | 🇳🇴 NO | 348 |
| 21 | 🇬🇹 GT | 341 |
| 22 | 🇹🇷 TR | 339 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 265 |
| 25 | 🇵🇱 PL | 260 |
| 26 | 🇲🇦 MA | 223 |
| 27 | 🇮🇩 ID | 201 |
| 28 | 🇲🇴 MO | 196 |
| 29 | 🇧🇸 BS | 193 |
| 30 | 🇲🇪 ME | 190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 351 |
| 3 | Tokyo International Airport |  | JP | 339 |
| 4 | Indira Gandhi International Airport |  | IN | 330 |
| 5 | Denver International Airport |  | US | 327 |
| 6 | La Aurora Airport |  | GT | 239 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 238 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 224 |
| 10 | Zurich Airport |  | CH | 218 |
| 11 | Macau International Airport |  | MO | 196 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 14 | Guaymaral Airport |  | CO | 183 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 16 | Bengaluru International Airport |  | IN | 175 |
| 17 | Chicago O'Hare International Airport |  | US | 173 |
| 18 | Madrid Barajas International Airport |  | ES | 170 |
| 19 | Charlotte/Douglas International Airport |  | US | 166 |
| 20 | Tenerife Norte Airport |  | ES | 161 |
| 21 | Ninoy Aquino International Airport |  | PH | 160 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 23 | Congonhas Airport |  | BR | 155 |
| 24 | Kuala Lumpur International Airport |  | MY | 153 |
| 25 | Daniel K Inouye International Airport |  | US | 145 |
| 26 | Salt Lake City International Airport |  | US | 143 |
| 27 | Malpensa International Airport |  | IT | 138 |
| 28 | Vitoria/Foronda Airport |  | ES | 138 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 30 | Reno/Tahoe International Airport |  | US | 136 |
| 31 | Charles de Gaulle International Airport |  | FR | 133 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 133 |
| 33 | Miami International Airport |  | US | 124 |
| 34 | Barcelona International Airport |  | ES | 123 |
| 35 | O. R. Tambo International Airport |  | ZA | 121 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 120 |
| 37 | Pune Airport |  | IN | 120 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 39 | Seattle-Tacoma International Airport |  | US | 115 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 112 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 52 | 1h 44m | 1,156 km | 1,037.4 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 47 | 22m | 99 km | 80.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 45 | 28m | 275 km | 213.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 44 | 19m | 165 km | 125.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 35 | 23m | 252 km | 152.0 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 34 | 1h 43m | 1,423 km | 834.4 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 32 | 13m | 99 km | 54.9 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 32 | 11m | 127 km | 70.0 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 28 | 17m | 183 km | 88.3 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 28 | 20m | 250 km | 120.9 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-05 07:07 UTC | 2026-04-05 13:20 UTC | 6h 12m |
| BPX213 | BPX | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-05 13:03 UTC | 2026-04-05 13:18 UTC | 15m |
| LAE2524 | LAE | El Dorado International Airport (SKBO) | Los Angeles International Airport (KLAX) | 2026-04-05 03:07 UTC | 2026-04-05 13:05 UTC | 9h 58m |
| N5333Z |  | Hicks Airfield (KT67) | Bridgeport Municipal Airport (KXBP) | 2026-04-05 12:31 UTC | 2026-04-05 12:58 UTC | 26m |
| TGOZI | TGO | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-05 12:24 UTC | 2026-04-05 12:50 UTC | 25m |
|  |  | Asiago Airport (LIDA) | Trento / Mattarello Airport (LIDT) | 2026-04-05 12:46 UTC | 2026-04-05 12:48 UTC | 2m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-05 12:09 UTC | 2026-04-05 12:46 UTC | 37m |
| KENLEY | KEN | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-04-05 12:41 UTC | 2026-04-05 12:44 UTC | 2m |
| N1910R |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 12:14 UTC | 2026-04-05 12:44 UTC | 29m |
| DLH3LC | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-05 12:08 UTC | 2026-04-05 12:41 UTC | 32m |
| CFL02 | CFL | Hamilton International Airport (NZHN) | Raglan Airfield (NZRA) | 2026-04-05 12:23 UTC | 2026-04-05 12:40 UTC | 17m |
| SAS75G | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Cewice Military Airport (EPCE) | 2026-04-05 12:13 UTC | 2026-04-05 12:40 UTC | 26m |
| RYR38RJ | Ryanair | Luqa Airport (LMML) | Foligno Airport (LIAF) | 2026-04-05 11:20 UTC | 2026-04-05 12:31 UTC | 1h 10m |
| N136M |  | Addison Airport (KADS) | Sulphur Springs Municipal Airport (KSLR) | 2026-04-05 11:49 UTC | 2026-04-05 12:30 UTC | 41m |
| DRAGO67 | DRA | Strasbourg Airport (LFST) | Sarre Union Airport (LFQU) | 2026-04-05 12:09 UTC | 2026-04-05 12:30 UTC | 21m |
| RYR6743 | Ryanair | Ibn Batouta Airport (GMTT) | Angads Airport (GMFO) | 2026-04-05 11:56 UTC | 2026-04-05 12:27 UTC | 31m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-05 12:15 UTC | 2026-04-05 12:27 UTC | 11m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-04-05 11:52 UTC | 2026-04-05 12:24 UTC | 31m |
| EWG4UY | EWG | Dusseldorf International Airport (EDDL) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-05 10:49 UTC | 2026-04-05 12:22 UTC | 1h 33m |
| SWA3263 | Southwest Airlines | Pittsburgh International Airport (KPIT) | St Louis Lambert International Airport (KSTL) | 2026-04-05 10:52 UTC | 2026-04-05 12:21 UTC | 1h 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
