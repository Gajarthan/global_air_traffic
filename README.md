# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_23:00:25_UTC-green)

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

**Latest saved flight:** 2026-04-29 23:00:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 23:00:25 UTC

- **59,809** saved flights
- **23,149** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,809** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **727,206.0 tonnes** estimated CO2 emissions
- **42,156,867 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2548 |
| 2 | SkyWest Airlines | 2246 |
| 3 | IndiGo | 1362 |
| 4 | EJA | 1077 |
| 5 | American Airlines | 940 |
| 6 | Southwest Airlines | 849 |
| 7 | Lufthansa | 759 |
| 8 | ENY | 745 |
| 9 | Vueling | 597 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 569 |
| 12 | All Nippon Airways | 527 |
| 13 | Delta Air Lines | 501 |
| 14 | WIF | 501 |
| 15 | AZU | 490 |
| 16 | Swiss International | 473 |
| 17 | QLK | 466 |
| 18 | LXJ | 426 |
| 19 | Alaska Airlines | 410 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 376 |
| 24 | Cathay Pacific | 354 |
| 25 | Air France | 353 |
| 26 | Japan Airlines | 346 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 300 |
| 30 | CXK | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47429 |
| 2 | 🇪🇸 ES | 4338 |
| 3 | 🇮🇳 IN | 4313 |
| 4 | 🇦🇺 AU | 4054 |
| 5 | 🇧🇷 BR | 3384 |
| 6 | 🇩🇪 DE | 3312 |
| 7 | 🇮🇹 IT | 3289 |
| 8 | 🇯🇵 JP | 3229 |
| 9 | 🇨🇦 CA | 2968 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2524 |
| 12 | 🇫🇷 FR | 2366 |
| 13 | 🇲🇽 MX | 1874 |
| 14 | 🇬🇷 GR | 1784 |
| 15 | 🇨🇭 CH | 1665 |
| 16 | 🇳🇴 NO | 1637 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1114 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1073 |
| 22 | 🇵🇭 PH | 1009 |
| 23 | 🇵🇱 PL | 969 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 871 |
| 26 | 🇲🇦 MA | 749 |
| 27 | 🇲🇪 ME | 652 |
| 28 | 🇲🇴 MO | 648 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1334 |
| 2 | Tokyo International Airport |  | JP | 1097 |
| 3 | Denver International Airport |  | US | 1002 |
| 4 | Indira Gandhi International Airport |  | IN | 908 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 879 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 759 |
| 9 | Frankfurt am Main International Airport |  | DE | 750 |
| 10 | Zurich Airport |  | CH | 721 |
| 11 | La Aurora Airport |  | GT | 656 |
| 12 | Macau International Airport |  | MO | 648 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 593 |
| 14 | Chicago O'Hare International Airport |  | US | 570 |
| 15 | Madrid Barajas International Airport |  | ES | 555 |
| 16 | Kuala Lumpur International Airport |  | MY | 555 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 553 |
| 18 | Malpensa International Airport |  | IT | 520 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 520 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 487 |
| 22 | Charlotte/Douglas International Airport |  | US | 476 |
| 23 | Charles de Gaulle International Airport |  | FR | 466 |
| 24 | Capua Airport |  | IT | 466 |
| 25 | Salt Lake City International Airport |  | US | 465 |
| 26 | Tenerife Norte Airport |  | ES | 463 |
| 27 | Ninoy Aquino International Airport |  | PH | 462 |
| 28 | Daniel K Inouye International Airport |  | US | 450 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 431 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 431 |
| 31 | Barcelona International Airport |  | ES | 409 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 33 | Vitoria/Foronda Airport |  | ES | 399 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 394 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 382 |
| 38 | Amsterdam Airport Schiphol |  | NL | 368 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 201 | 21m | 244 km | 846.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 168 | 28m | 304 km | 880.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 142 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 127 | 1h 12m | 770 km | 1,687.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 101 | 31m | 369 km | 642.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 90 | 20m | 147 km | 227.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 89 | 28m | 152 km | 232.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 83 | 1h 43m | 1,156 km | 1,655.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 1m | 695 km | 994.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 78 | 1h 43m | 1,423 km | 1,914.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 76 | 1h 19m | 961 km | 1,259.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EVIL67 | EVI | Enid Woodring Regional Airport (KWDG) | Gilstrap Field (55OK) | 2026-04-29 22:22 UTC | 2026-04-29 23:00 UTC | 37m |
| URSA98 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-29 19:49 UTC | 2026-04-29 22:59 UTC | 3h 9m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-29 12:10 UTC | 2026-04-29 22:53 UTC | 10h 43m |
| UAE9840 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-29 16:11 UTC | 2026-04-29 22:43 UTC | 6h 32m |
| N640TC |  | KU42 (KU42) | KU42 (KU42) | 2026-04-29 21:48 UTC | 2026-04-29 22:37 UTC | 49m |
| N982MR |  | Crete Municipal Airport (KCEK) | Crete Municipal Airport (KCEK) | 2026-04-29 22:27 UTC | 2026-04-29 22:37 UTC | 9m |
| BALL19 | BAL | Enid Woodring Regional Airport (KWDG) | Tulsa Riverside Airport (KRVS) | 2026-04-29 22:14 UTC | 2026-04-29 22:36 UTC | 22m |
| N76FF |  | Rocky Mountain Metro Airport (KBJC) | Northern Colorado Regional Airport (KFNL) | 2026-04-29 22:10 UTC | 2026-04-29 22:35 UTC | 24m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-04-29 10:54 UTC | 2026-04-29 22:33 UTC | 11h 39m |
| N63FB |  | San Antonio International Airport (KSAT) | Upton County Airport (KE48) | 2026-04-29 21:25 UTC | 2026-04-29 22:33 UTC | 1h 7m |
| CGDGO | CGD | Montréal / St-Hubert Airport (CYHU) | Thetford Mines Airport (CSM3) | 2026-04-29 22:09 UTC | 2026-04-29 22:28 UTC | 19m |
| WOLF72 | WOL | Okc Will Rogers International Airport (KOKC) | Winslow-Lindbergh Regional Airport (KINW) | 2026-04-29 20:31 UTC | 2026-04-29 22:26 UTC | 1h 55m |
| HOBBY45 | HOB | 12XS (12XS) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-29 21:14 UTC | 2026-04-29 22:20 UTC | 1h 5m |
| WC402 |  | Fernando Air Base (RPUL) | Fernando Air Base (RPUL) | 2026-04-29 21:49 UTC | 2026-04-29 22:20 UTC | 31m |
| N8850P |  | Denton Enterprise Airport (KDTO) | 69XA (69XA) | 2026-04-29 21:50 UTC | 2026-04-29 22:19 UTC | 29m |
| SKW1003 | SkyWest Airlines | Tucson International Airport (KTUS) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-04-29 21:32 UTC | 2026-04-29 22:16 UTC | 44m |
| PCJ20 | PCJ | Moffett Federal Airfield (KNUQ) | Santa Monica Municipal Airport (KSMO) | 2026-04-29 21:21 UTC | 2026-04-29 22:16 UTC | 55m |
| N643SA |  | Addison Airport (KADS) | Dreamland Airport (XA48) | 2026-04-29 21:50 UTC | 2026-04-29 22:15 UTC | 25m |
| JEC5452 | JEC | Guaymaral Airport (SKGY) | Gustavo Rojas Pinilla International Airport (SKSP) | 2026-04-29 16:59 UTC | 2026-04-29 22:15 UTC | 5h 15m |
| AM324 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-04-29 21:55 UTC | 2026-04-29 22:14 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
