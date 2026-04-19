# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_03:25:41_UTC-green)

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

**Latest saved flight:** 2026-04-19 03:25:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 03:25:41 UTC

- **42,325** saved flights
- **17,793** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,325** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **507,737.7 tonnes** estimated CO2 emissions
- **29,434,068 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1766 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1031 |
| 4 | EJA | 733 |
| 5 | American Airlines | 705 |
| 6 | Southwest Airlines | 598 |
| 7 | ENY | 555 |
| 8 | AXM | 436 |
| 9 | LATAM Airlines | 423 |
| 10 | Vueling | 422 |
| 11 | Lufthansa | 414 |
| 12 | All Nippon Airways | 379 |
| 13 | AZU | 377 |
| 14 | Delta Air Lines | 362 |
| 15 | QLK | 343 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 288 |
| 20 | AEE | 282 |
| 21 | EJU | 277 |
| 22 | easyJet | 272 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 260 |
| 25 | Air France | 236 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 220 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33624 |
| 2 | 🇮🇳 IN | 3157 |
| 3 | 🇪🇸 ES | 3095 |
| 4 | 🇦🇺 AU | 2956 |
| 5 | 🇧🇷 BR | 2541 |
| 6 | 🇯🇵 JP | 2320 |
| 7 | 🇮🇹 IT | 2186 |
| 8 | 🇩🇪 DE | 2128 |
| 9 | 🇨🇦 CA | 2081 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1709 |
| 12 | 🇫🇷 FR | 1620 |
| 13 | 🇲🇽 MX | 1334 |
| 14 | 🇬🇷 GR | 1276 |
| 15 | 🇨🇭 CH | 1178 |
| 16 | 🇲🇾 MY | 1061 |
| 17 | 🇳🇴 NO | 1034 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 862 |
| 20 | 🇵🇭 PH | 764 |
| 21 | 🇹🇭 TH | 745 |
| 22 | 🇹🇷 TR | 733 |
| 23 | 🇬🇹 GT | 707 |
| 24 | 🇰🇷 KR | 704 |
| 25 | 🇵🇱 PL | 664 |
| 26 | 🇲🇦 MA | 522 |
| 27 | 🇳🇱 NL | 432 |
| 28 | 🇲🇪 ME | 429 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 386 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 992 |
| 2 | Tokyo International Airport |  | JP | 793 |
| 3 | Denver International Airport |  | US | 704 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 681 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 632 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 507 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 419 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 397 |
| 16 | Frankfurt am Main International Airport |  | DE | 383 |
| 17 | Madrid Barajas International Airport |  | ES | 379 |
| 18 | Macau International Airport |  | MO | 378 |
| 19 | Bengaluru International Airport |  | IN | 373 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 368 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 355 |
| 24 | Malpensa International Airport |  | IT | 341 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 328 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 315 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 307 |
| 29 | Charles de Gaulle International Airport |  | FR | 306 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 297 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 33 | Reno/Tahoe International Airport |  | US | 293 |
| 34 | O. R. Tambo International Airport |  | ZA | 282 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 282 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 268 |
| 38 | Viracopos International Airport |  | BR | 260 |
| 39 | Calgary International Airport |  | CA | 255 |
| 40 | Seattle-Tacoma International Airport |  | US | 252 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 200 | 1h 7m | 706 km | 2,435.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 153 | 24m | 225 km | 593.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 127 | 28m | 304 km | 665.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 122 | 1h 27m | 910 km | 1,914.5 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 116 | 21m | 244 km | 488.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 113 | 19m | 165 km | 321.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 86 | 44m | 452 km | 670.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 29 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERE | ERE | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-04-19 02:47 UTC | 2026-04-19 03:25 UTC | 38m |
| NIJ | NIJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-19 02:29 UTC | 2026-04-19 03:04 UTC | 35m |
| IOL | IOL | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-04-19 02:55 UTC | 2026-04-19 03:01 UTC | 5m |
| N233LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-19 01:20 UTC | 2026-04-19 02:56 UTC | 1h 36m |
| ATN3369 | ATN | John F Kennedy International Airport (KJFK) | Poplar Grove Airport (KC77) | 2026-04-19 00:41 UTC | 2026-04-19 02:54 UTC | 2h 12m |
| TRA113 | TRA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-04-19 02:24 UTC | 2026-04-19 02:51 UTC | 26m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-19 02:31 UTC | 2026-04-19 02:48 UTC | 16m |
| XUM2593 | XUM | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-19 01:58 UTC | 2026-04-19 02:39 UTC | 40m |
| STA611D | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-04-19 02:19 UTC | 2026-04-19 02:37 UTC | 18m |
| CGVVC | CGV | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-04-19 02:23 UTC | 2026-04-19 02:37 UTC | 13m |
| N273DT |  | Roy Hurd Memorial Airport (KE01) | Rafter P Airport (TA00) | 2026-04-19 01:52 UTC | 2026-04-19 02:37 UTC | 45m |
| N183TS |  | Savannah/Hilton Head International Airport (KSAV) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-19 00:50 UTC | 2026-04-19 02:36 UTC | 1h 45m |
| ASA67 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-04-19 01:18 UTC | 2026-04-19 02:34 UTC | 1h 16m |
| EJA639 | EJA | Los Angeles International Airport (KLAX) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-19 01:41 UTC | 2026-04-19 02:34 UTC | 52m |
| N790A |  | Houma-Terrebonne Airport (KHUM) | 13LS (13LS) | 2026-04-19 02:01 UTC | 2026-04-19 02:30 UTC | 28m |
| IOL | IOL | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-04-19 02:01 UTC | 2026-04-19 02:29 UTC | 27m |
| SKW6248 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Cottonwood Airport (KP52) | 2026-04-19 02:12 UTC | 2026-04-19 02:28 UTC | 15m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-19 02:04 UTC | 2026-04-19 02:28 UTC | 23m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-19 01:58 UTC | 2026-04-19 02:28 UTC | 30m |
| N355CF |  | Stellar Airpark (KP19) | Mesa Gateway Airport (KIWA) | 2026-04-19 02:21 UTC | 2026-04-19 02:27 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
