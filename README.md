# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_03:20:52_UTC-green)

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

**Latest saved flight:** 2026-04-15 03:20:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 03:20:52 UTC

- **35,176** saved flights
- **15,506** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,176** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **429,302.5 tonnes** estimated CO2 emissions
- **24,887,102 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1503 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 871 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 506 |
| 7 | ENY | 469 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 367 |
| 10 | Vueling | 356 |
| 11 | LATAM Airlines | 353 |
| 12 | AZU | 314 |
| 13 | All Nippon Airways | 312 |
| 14 | Delta Air Lines | 299 |
| 15 | QLK | 298 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 265 |
| 18 | WIF | 254 |
| 19 | Alaska Airlines | 236 |
| 20 | AEE | 234 |
| 21 | easyJet | 234 |
| 22 | EJU | 231 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 218 |
| 25 | EDV | 201 |
| 26 | United Airlines | 199 |
| 27 | Air France | 193 |
| 28 | GLO | 192 |
| 29 | JetBlue | 187 |
| 30 | Avianca | 184 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27736 |
| 2 | 🇮🇳 IN | 2665 |
| 3 | 🇪🇸 ES | 2626 |
| 4 | 🇦🇺 AU | 2474 |
| 5 | 🇧🇷 BR | 2079 |
| 6 | 🇯🇵 JP | 1896 |
| 7 | 🇮🇹 IT | 1882 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1726 |
| 11 | 🇬🇧 GB | 1445 |
| 12 | 🇫🇷 FR | 1300 |
| 13 | 🇲🇽 MX | 1131 |
| 14 | 🇬🇷 GR | 1038 |
| 15 | 🇨🇭 CH | 959 |
| 16 | 🇲🇾 MY | 886 |
| 17 | 🇳🇴 NO | 823 |
| 18 | 🇳🇿 NZ | 759 |
| 19 | 🇿🇦 ZA | 726 |
| 20 | 🇵🇭 PH | 667 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 629 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 593 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 441 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 344 |
| 30 | 🇮🇩 ID | 330 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 648 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 510 |
| 7 | Harry Reid International Airport |  | US | 467 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 432 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 13 | Chicago O'Hare International Airport |  | US | 355 |
| 14 | Kuala Lumpur International Airport |  | MY | 341 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 339 |
| 16 | Frankfurt am Main International Airport |  | DE | 334 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Charlotte/Douglas International Airport |  | US | 319 |
| 19 | Madrid Barajas International Airport |  | ES | 318 |
| 20 | Congonhas Airport |  | BR | 309 |
| 21 | Ninoy Aquino International Airport |  | PH | 308 |
| 22 | Bengaluru International Airport |  | IN | 308 |
| 23 | Tenerife Norte Airport |  | ES | 307 |
| 24 | Malpensa International Airport |  | IT | 285 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 280 |
| 26 | Salt Lake City International Airport |  | US | 268 |
| 27 | Daniel K Inouye International Airport |  | US | 267 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 247 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 247 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 234 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 222 |
| 39 | Viracopos International Airport |  | BR | 220 |
| 40 | Miami International Airport |  | US | 219 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 163 | 1h 8m | 706 km | 1,984.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 129 | 24m | 225 km | 500.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 101 | 1h 27m | 910 km | 1,584.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 91 | 19m | 165 km | 258.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 87 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 83 | 21m | 244 km | 349.5 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 74 | 1h 12m | 770 km | 983.0 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 68 | 31m | 369 km | 432.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 64 | 45m | 452 km | 498.8 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 50 | 14m | 154 km | 132.5 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHH489 | CHH | Shenzhen Bao'an International Airport (ZGSZ) | Nida Airport (EYND) | 2026-04-14 11:25 UTC | 2026-04-15 03:20 UTC | 15h 55m |
| 9MSBH |  | Kota Kinabalu International Airport (WBKK) | Labuan Airport (WBKL) | 2026-04-15 02:19 UTC | 2026-04-15 03:08 UTC | 49m |
| EFI | EFI | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-04-15 02:23 UTC | 2026-04-15 03:03 UTC | 39m |
| ZKIDH | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-04-15 01:55 UTC | 2026-04-15 02:59 UTC | 1h 4m |
| BHA701 | BHA | Tribhuvan International Airport (VNKT) | Biratnagar Airport (VNVT) | 2026-04-15 02:28 UTC | 2026-04-15 02:59 UTC | 30m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-15 02:42 UTC | 2026-04-15 02:59 UTC | 16m |
| ZKTAG | ZKT | Flat Point Aerodrome (NZFT) | Hood Airport (NZMS) | 2026-04-15 02:31 UTC | 2026-04-15 02:58 UTC | 26m |
| ROLR4 | ROL | Mount Hotham Airport (YHOT) | Mount Hotham Airport (YHOT) | 2026-04-15 02:41 UTC | 2026-04-15 02:52 UTC | 10m |
| N390EA |  | Watts-Woodland Airport (KO41) | Visalia Municipal Airport (KVIS) | 2026-04-15 01:14 UTC | 2026-04-15 02:49 UTC | 1h 34m |
| N200UW |  | Laramie Regional Airport (KLAR) | Dilts Ranch Airport (WY01) | 2026-04-15 02:13 UTC | 2026-04-15 02:44 UTC | 30m |
| BBC611 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-15 02:07 UTC | 2026-04-15 02:40 UTC | 33m |
| NLQ | NLQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-15 02:21 UTC | 2026-04-15 02:38 UTC | 17m |
| N778SC |  | John C Tune Airport (KJWN) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-04-14 22:40 UTC | 2026-04-15 02:35 UTC | 3h 55m |
|  |  | Gimpo International Airport (RKSS) | RKRS (RKRS) | 2026-04-15 02:27 UTC | 2026-04-15 02:34 UTC | 6m |
| N52654 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-15 02:17 UTC | 2026-04-15 02:30 UTC | 13m |
| SKYFL21 | SKY | Avi Suquilla Airport (KP20) | Blythe Airport (KBLH) | 2026-04-15 01:44 UTC | 2026-04-15 02:30 UTC | 45m |
| AWA411 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-15 01:51 UTC | 2026-04-15 02:25 UTC | 34m |
|  |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-04-15 02:07 UTC | 2026-04-15 02:25 UTC | 18m |
| SLI871 | SLI | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-15 01:45 UTC | 2026-04-15 02:24 UTC | 38m |
| SWA2257 | Southwest Airlines | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-15 01:19 UTC | 2026-04-15 02:23 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
