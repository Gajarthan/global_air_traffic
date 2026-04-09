# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_07:57:37_UTC-green)

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

**Latest saved flight:** 2026-04-09 07:57:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 07:57:37 UTC

- **24,658** saved flights
- **11,870** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,658** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **305,103.4 tonnes** estimated CO2 emissions
- **17,687,156 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1021 |
| 2 | Ryanair | 1008 |
| 3 | IndiGo | 681 |
| 4 | American Airlines | 448 |
| 5 | EJA | 447 |
| 6 | Southwest Airlines | 354 |
| 7 | ENY | 324 |
| 8 | Lufthansa | 316 |
| 9 | Vueling | 256 |
| 10 | AXM | 253 |
| 11 | LATAM Airlines | 244 |
| 12 | QLK | 228 |
| 13 | All Nippon Airways | 223 |
| 14 | Delta Air Lines | 208 |
| 15 | LXJ | 198 |
| 16 | AZU | 193 |
| 17 | Swiss International | 180 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 166 |
| 20 | VIV | 165 |
| 21 | easyJet | 161 |
| 22 | EJU | 157 |
| 23 | WIF | 154 |
| 24 | AEE | 151 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 145 |
| 27 | EDV | 145 |
| 28 | AXB | 141 |
| 29 | Cathay Pacific | 129 |
| 30 | ANZ | 128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19341 |
| 2 | 🇮🇳 IN | 2082 |
| 3 | 🇦🇺 AU | 1858 |
| 4 | 🇪🇸 ES | 1854 |
| 5 | 🇯🇵 JP | 1387 |
| 6 | 🇧🇷 BR | 1371 |
| 7 | 🇨🇴 CO | 1257 |
| 8 | 🇩🇪 DE | 1256 |
| 9 | 🇮🇹 IT | 1241 |
| 10 | 🇨🇦 CA | 1148 |
| 11 | 🇬🇧 GB | 987 |
| 12 | 🇫🇷 FR | 895 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 692 |
| 15 | 🇨🇭 CH | 678 |
| 16 | 🇲🇾 MY | 601 |
| 17 | 🇳🇿 NZ | 547 |
| 18 | 🇳🇴 NO | 527 |
| 19 | 🇿🇦 ZA | 518 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 474 |
| 22 | 🇵🇭 PH | 472 |
| 23 | 🇰🇷 KR | 439 |
| 24 | 🇹🇭 TH | 405 |
| 25 | 🇵🇱 PL | 361 |
| 26 | 🇲🇦 MA | 297 |
| 27 | 🇮🇩 ID | 253 |
| 28 | 🇧🇸 BS | 251 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇲🇴 MO | 246 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 585 |
| 2 | El Dorado International Airport |  | CO | 467 |
| 3 | Tokyo International Airport |  | JP | 461 |
| 4 | Denver International Airport |  | US | 433 |
| 5 | Indira Gandhi International Airport |  | IN | 432 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 325 |
| 9 | Zurich Airport |  | CH | 294 |
| 10 | Frankfurt am Main International Airport |  | DE | 265 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 255 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 255 |
| 15 | Chicago O'Hare International Airport |  | US | 253 |
| 16 | Macau International Airport |  | MO | 246 |
| 17 | Bengaluru International Airport |  | IN | 231 |
| 18 | Charlotte/Douglas International Airport |  | US | 230 |
| 19 | Ninoy Aquino International Airport |  | PH | 219 |
| 20 | Kuala Lumpur International Airport |  | MY | 219 |
| 21 | Madrid Barajas International Airport |  | ES | 214 |
| 22 | Tenerife Norte Airport |  | ES | 213 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 196 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 193 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 174 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 171 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 162 |
| 35 | O. R. Tambo International Airport |  | ZA | 162 |
| 36 | Seattle-Tacoma International Airport |  | US | 161 |
| 37 | Pune Airport |  | IN | 160 |
| 38 | Barcelona International Airport |  | ES | 159 |
| 39 | Vitoria/Foronda Airport |  | ES | 156 |
| 40 | Calgary International Airport |  | CA | 146 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 116 | 1h 8m | 706 km | 1,412.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 72 | 1h 27m | 910 km | 1,129.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 60 | 19m | 165 km | 170.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 54 | 1h 12m | 770 km | 717.3 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 50 | 27m | 275 km | 236.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 48 | 31m | 369 km | 305.5 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 45 | 45m | 452 km | 350.7 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 42 | 1h 42m | 1,423 km | 1,030.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRU949 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-04-09 07:36 UTC | 2026-04-09 07:57 UTC | 21m |
| THY70 | Turkish Airlines | Sabiha Gokcen International Airport (LTFJ) | Macau International Airport (VMMC) | 2026-04-08 23:05 UTC | 2026-04-09 07:45 UTC | 8h 39m |
| HIPO71 | HIP | Namest Air Base (LKNA) | Namest Air Base (LKNA) | 2026-04-09 07:20 UTC | 2026-04-09 07:37 UTC | 17m |
| YOJ | YOJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-09 06:51 UTC | 2026-04-09 07:35 UTC | 44m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Meiringen Airport (LSMM) | 2026-04-09 07:04 UTC | 2026-04-09 07:34 UTC | 30m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-08 19:48 UTC | 2026-04-09 07:33 UTC | 11h 44m |
| CAL1806 | CAL | Taiwan Taoyuan International Airport (RCTP) | Kaohsiung International Airport (RCKH) | 2026-04-09 06:16 UTC | 2026-04-09 07:33 UTC | 1h 16m |
| N496LG |  | CD82 (CD82) | True Grit South Airport (CO95) | 2026-04-09 07:09 UTC | 2026-04-09 07:22 UTC | 13m |
| SWR59H | Swiss International | Zurich Airport (LSZH) | Dubrovnik Airport (LDDU) | 2026-04-09 05:42 UTC | 2026-04-09 07:20 UTC | 1h 37m |
| RYR71TT | Ryanair | Valencia Airport (LEVC) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-09 04:30 UTC | 2026-04-09 07:19 UTC | 2h 48m |
| HL5247 |  | Gimpo International Airport (RKSS) | G 418 Airport (RK33) | 2026-04-09 06:42 UTC | 2026-04-09 07:17 UTC | 34m |
| BAG12 | BAG | Salzburg Airport (LOWS) | Kalamata Airport (LGKL) | 2026-04-09 04:37 UTC | 2026-04-09 07:15 UTC | 2h 38m |
| RYR70NQ | Ryanair | Thessaloniki Macedonia International Airport (LGTS) | Ercan International Airport (LCEN) | 2026-04-09 05:59 UTC | 2026-04-09 07:15 UTC | 1h 16m |
| ABY537 | ABY | Raxaul Airport (VERL) | Saiq Airport (OOSQ) | 2026-04-09 03:17 UTC | 2026-04-09 07:12 UTC | 3h 54m |
| ANE82BX | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-04-09 06:39 UTC | 2026-04-09 07:09 UTC | 29m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-09 06:57 UTC | 2026-04-09 07:09 UTC | 12m |
| SWR9Q | Swiss International | Zurich Airport (LSZH) | Norvenich Airport (ETNN) | 2026-04-09 06:10 UTC | 2026-04-09 07:07 UTC | 56m |
| AIQ510 | AIQ | Don Mueang International Airport (VTBD) | Mersing Airport (WMAU) | 2026-04-09 05:17 UTC | 2026-04-09 07:05 UTC | 1h 48m |
| RYR5429 | Ryanair | Riga International Airport (EVRA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-09 05:50 UTC | 2026-04-09 07:05 UTC | 1h 15m |
| IGO6097 | IndiGo | Agartala Airport (VEAT) | Barrackpore Air Force Station (VEPI) | 2026-04-09 06:36 UTC | 2026-04-09 07:05 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
