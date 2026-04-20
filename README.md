# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_03:17:12_UTC-green)

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

**Latest saved flight:** 2026-04-20 03:17:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 03:17:12 UTC

- **44,478** saved flights
- **18,474** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,478** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **535,695.0 tonnes** estimated CO2 emissions
- **31,054,780 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1868 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1073 |
| 4 | EJA | 778 |
| 5 | American Airlines | 739 |
| 6 | Southwest Airlines | 638 |
| 7 | ENY | 584 |
| 8 | AXM | 447 |
| 9 | Vueling | 445 |
| 10 | LATAM Airlines | 444 |
| 11 | Lufthansa | 438 |
| 12 | All Nippon Airways | 401 |
| 13 | AZU | 388 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 360 |
| 16 | LXJ | 354 |
| 17 | WIF | 344 |
| 18 | Swiss International | 339 |
| 19 | Alaska Airlines | 306 |
| 20 | AEE | 301 |
| 21 | EJU | 291 |
| 22 | VIV | 285 |
| 23 | easyJet | 284 |
| 24 | Japan Airlines | 271 |
| 25 | Air France | 250 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 237 |
| 28 | GLO | 233 |
| 29 | AXB | 232 |
| 30 | Cathay Pacific | 226 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35369 |
| 2 | 🇮🇳 IN | 3307 |
| 3 | 🇪🇸 ES | 3261 |
| 4 | 🇦🇺 AU | 3070 |
| 5 | 🇧🇷 BR | 2658 |
| 6 | 🇯🇵 JP | 2435 |
| 7 | 🇮🇹 IT | 2347 |
| 8 | 🇩🇪 DE | 2241 |
| 9 | 🇨🇦 CA | 2175 |
| 10 | 🇨🇴 CO | 2057 |
| 11 | 🇬🇧 GB | 1796 |
| 12 | 🇫🇷 FR | 1684 |
| 13 | 🇲🇽 MX | 1396 |
| 14 | 🇬🇷 GR | 1360 |
| 15 | 🇨🇭 CH | 1204 |
| 16 | 🇳🇴 NO | 1095 |
| 17 | 🇲🇾 MY | 1094 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 889 |
| 20 | 🇵🇭 PH | 798 |
| 21 | 🇹🇭 TH | 784 |
| 22 | 🇹🇷 TR | 783 |
| 23 | 🇬🇹 GT | 733 |
| 24 | 🇰🇷 KR | 730 |
| 25 | 🇵🇱 PL | 702 |
| 26 | 🇲🇦 MA | 551 |
| 27 | 🇲🇪 ME | 467 |
| 28 | 🇳🇱 NL | 452 |
| 29 | 🇧🇸 BS | 411 |
| 30 | 🇲🇴 MO | 409 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1049 |
| 2 | Tokyo International Airport |  | JP | 832 |
| 3 | Denver International Airport |  | US | 749 |
| 4 | El Dorado International Airport |  | CO | 719 |
| 5 | Indira Gandhi International Airport |  | IN | 712 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 676 |
| 7 | Harry Reid International Airport |  | US | 574 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 528 |
| 11 | Chicago O'Hare International Airport |  | US | 442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 13 | Kuala Lumpur International Airport |  | MY | 434 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 412 |
| 17 | Macau International Airport |  | MO | 409 |
| 18 | Madrid Barajas International Airport |  | ES | 394 |
| 19 | Bengaluru International Airport |  | IN | 393 |
| 20 | Tenerife Norte Airport |  | ES | 390 |
| 21 | Charlotte/Douglas International Airport |  | US | 387 |
| 22 | Congonhas Airport |  | BR | 381 |
| 23 | Malpensa International Airport |  | IT | 373 |
| 24 | Ninoy Aquino International Airport |  | PH | 369 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Daniel K Inouye International Airport |  | US | 330 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 329 |
| 29 | Charles de Gaulle International Airport |  | FR | 325 |
| 30 | Reno/Tahoe International Airport |  | US | 311 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 309 |
| 32 | Vitoria/Foronda Airport |  | ES | 307 |
| 33 | Capua Airport |  | IT | 305 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 302 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 287 |
| 38 | Calgary International Airport |  | CA | 273 |
| 39 | Viracopos International Airport |  | BR | 270 |
| 40 | Seattle-Tacoma International Airport |  | US | 265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 207 | 1h 7m | 706 km | 2,520.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 125 | 21m | 244 km | 526.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 119 | 19m | 165 km | 338.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 118 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 92 | 44m | 452 km | 717.0 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 63 | 13m | 99 km | 108.0 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZJX | ZJX | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-20 02:55 UTC | 2026-04-20 03:17 UTC | 22m |
| USC240 | USC | Portland International Airport (KPDX) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-20 01:43 UTC | 2026-04-20 03:09 UTC | 1h 25m |
| N120FM |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-20 02:24 UTC | 2026-04-20 03:09 UTC | 44m |
| SWA1799 | Southwest Airlines | Bob Hope Airport (KBUR) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-20 02:18 UTC | 2026-04-20 03:07 UTC | 49m |
| N229LJ |  | Eppley Airfield (KOMA) | Naylor Field (19AR) | 2026-04-20 02:11 UTC | 2026-04-20 03:04 UTC | 52m |
| N357EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-20 01:56 UTC | 2026-04-20 02:59 UTC | 1h 3m |
| PXT150 | PXT | Scottsdale Airport (KSDL) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-20 01:22 UTC | 2026-04-20 02:59 UTC | 1h 37m |
| MUST | MUS | Yarram Airport (YYRM) | Yarram Airport (YYRM) | 2026-04-20 02:55 UTC | 2026-04-20 02:57 UTC | 2m |
| N340MJ |  | Abraham Ranch Airport (7CA1) | Gray Butte Field (04CA) | 2026-04-20 02:40 UTC | 2026-04-20 02:56 UTC | 16m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-20 02:22 UTC | 2026-04-20 02:55 UTC | 33m |
| STA621D | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-04-20 02:33 UTC | 2026-04-20 02:52 UTC | 19m |
| JBU2077 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Harry Reid International Airport (KLAS) | 2026-04-19 21:33 UTC | 2026-04-20 02:47 UTC | 5h 13m |
| AWQ178 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-04-20 02:29 UTC | 2026-04-20 02:44 UTC | 15m |
| SRQ6129 | SRQ | Diosdado Macapagal International Airport (RPLC) | Bulan Airport (RPUU) | 2026-04-20 02:00 UTC | 2026-04-20 02:43 UTC | 42m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-20 02:06 UTC | 2026-04-20 02:36 UTC | 30m |
|  |  | Ardmore Airport (NZAR) | Ardmore Airport (NZAR) | 2026-04-20 02:35 UTC | 2026-04-20 02:36 UTC | 0m |
| HL5248 |  | Gimpo International Airport (RKSS) | G 419 Airport (RK48) | 2026-04-20 02:10 UTC | 2026-04-20 02:35 UTC | 25m |
| ANA1262 | All Nippon Airways | New Chitose Airport (RJCC) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-04-20 01:16 UTC | 2026-04-20 02:35 UTC | 1h 19m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-04-20 02:06 UTC | 2026-04-20 02:30 UTC | 24m |
| NKS361 | NKS | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-04-20 01:39 UTC | 2026-04-20 02:30 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
