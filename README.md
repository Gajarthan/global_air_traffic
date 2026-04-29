# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_21:59:05_UTC-green)

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

**Latest saved flight:** 2026-04-29 21:59:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 21:59:05 UTC

- **59,714** saved flights
- **23,119** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,714** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **725,632.9 tonnes** estimated CO2 emissions
- **42,065,673 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2547 |
| 2 | SkyWest Airlines | 2240 |
| 3 | IndiGo | 1362 |
| 4 | EJA | 1073 |
| 5 | American Airlines | 936 |
| 6 | Southwest Airlines | 848 |
| 7 | Lufthansa | 759 |
| 8 | ENY | 742 |
| 9 | Vueling | 597 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 569 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 501 |
| 14 | Delta Air Lines | 498 |
| 15 | AZU | 489 |
| 16 | Swiss International | 473 |
| 17 | QLK | 464 |
| 18 | LXJ | 425 |
| 19 | Alaska Airlines | 409 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 376 |
| 24 | Air France | 353 |
| 25 | Cathay Pacific | 350 |
| 26 | Japan Airlines | 346 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 300 |
| 30 | United Airlines | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47304 |
| 2 | 🇪🇸 ES | 4336 |
| 3 | 🇮🇳 IN | 4312 |
| 4 | 🇦🇺 AU | 4046 |
| 5 | 🇧🇷 BR | 3379 |
| 6 | 🇩🇪 DE | 3311 |
| 7 | 🇮🇹 IT | 3289 |
| 8 | 🇯🇵 JP | 3227 |
| 9 | 🇨🇦 CA | 2960 |
| 10 | 🇨🇴 CO | 2611 |
| 11 | 🇬🇧 GB | 2523 |
| 12 | 🇫🇷 FR | 2366 |
| 13 | 🇲🇽 MX | 1871 |
| 14 | 🇬🇷 GR | 1784 |
| 15 | 🇨🇭 CH | 1664 |
| 16 | 🇳🇴 NO | 1637 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1114 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1073 |
| 22 | 🇵🇭 PH | 1003 |
| 23 | 🇵🇱 PL | 969 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 869 |
| 26 | 🇲🇦 MA | 748 |
| 27 | 🇲🇪 ME | 651 |
| 28 | 🇲🇴 MO | 644 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1333 |
| 2 | Tokyo International Airport |  | JP | 1096 |
| 3 | Denver International Airport |  | US | 999 |
| 4 | Indira Gandhi International Airport |  | IN | 907 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 879 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 807 |
| 8 | Harry Reid International Airport |  | US | 758 |
| 9 | Frankfurt am Main International Airport |  | DE | 749 |
| 10 | Zurich Airport |  | CH | 720 |
| 11 | La Aurora Airport |  | GT | 655 |
| 12 | Macau International Airport |  | MO | 644 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 591 |
| 14 | Chicago O'Hare International Airport |  | US | 567 |
| 15 | Kuala Lumpur International Airport |  | MY | 555 |
| 16 | Madrid Barajas International Airport |  | ES | 554 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 551 |
| 18 | Malpensa International Airport |  | IT | 520 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 487 |
| 22 | Charlotte/Douglas International Airport |  | US | 475 |
| 23 | Charles de Gaulle International Airport |  | FR | 466 |
| 24 | Capua Airport |  | IT | 466 |
| 25 | Salt Lake City International Airport |  | US | 464 |
| 26 | Tenerife Norte Airport |  | ES | 463 |
| 27 | Ninoy Aquino International Airport |  | PH | 460 |
| 28 | Daniel K Inouye International Airport |  | US | 449 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 431 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 431 |
| 31 | Barcelona International Airport |  | ES | 409 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 401 |
| 33 | Vitoria/Foronda Airport |  | ES | 399 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 394 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 382 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 381 |
| 38 | Amsterdam Airport Schiphol |  | NL | 368 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 355 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 200 | 21m | 244 km | 842.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 168 | 28m | 304 km | 880.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 142 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 126 | 1h 12m | 770 km | 1,673.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 99 | 31m | 369 km | 630.2 t |
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
| N950G |  | Fort Worth Meacham International Airport (KFTW) | Okc Will Rogers International Airport (KOKC) | 2026-04-29 21:08 UTC | 2026-04-29 21:59 UTC | 50m |
| N306SB |  | San Bernardino International Airport (KSBD) | Big Bear City Airport (KL35) | 2026-04-29 21:41 UTC | 2026-04-29 21:58 UTC | 17m |
| ABD4601 | ABD | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-29 10:39 UTC | 2026-04-29 21:57 UTC | 11h 17m |
| N54466 |  | Somerset Airport (KSMQ) | Lehigh Valley International Airport (KABE) | 2026-04-29 21:35 UTC | 2026-04-29 21:57 UTC | 21m |
| N4871V |  | Willows/Glenn County Airport (KWLW) | Tracy Municipal Airport (KTCY) | 2026-04-29 20:51 UTC | 2026-04-29 21:55 UTC | 1h 4m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-29 17:38 UTC | 2026-04-29 21:55 UTC | 4h 16m |
| N700MM |  | Roberts Field (KRDM) | Mahogany Mtn Airport (1JY2) | 2026-04-29 21:29 UTC | 2026-04-29 21:49 UTC | 20m |
| N6294Y |  | Fairbanks International Airport (PAFA) | Nenana Municipal Airport (PANN) | 2026-04-29 21:00 UTC | 2026-04-29 21:48 UTC | 48m |
| N858TW |  | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-04-29 21:35 UTC | 2026-04-29 21:47 UTC | 12m |
| CPA234 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-28 17:09 UTC | 2026-04-29 21:46 UTC | 28h 36m |
| ZJI | ZJI | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-29 21:21 UTC | 2026-04-29 21:44 UTC | 22m |
| TORA81 | TOR | Enid Woodring Regional Airport (KWDG) | Good Life Ranch Airport (17OK) | 2026-04-29 21:22 UTC | 2026-04-29 21:43 UTC | 20m |
| FHY727 | FHY | Antalya International Airport (LTAI) | Izgrev Airport (LBWV) | 2026-04-29 20:38 UTC | 2026-04-29 21:42 UTC | 1h 4m |
| HKE235 | HKE | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-29 14:41 UTC | 2026-04-29 21:42 UTC | 7h 0m |
| ERU816 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-29 21:20 UTC | 2026-04-29 21:41 UTC | 21m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-29 10:46 UTC | 2026-04-29 21:38 UTC | 10h 52m |
| CPA085 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-29 07:14 UTC | 2026-04-29 21:37 UTC | 14h 22m |
| N690LA |  | Charleston Executive Airport (KJZI) | Nashville International Airport (KBNA) | 2026-04-29 20:14 UTC | 2026-04-29 21:34 UTC | 1h 20m |
| N239CH |  | Aurora State Airport (KUAO) | Mc Minnville Municipal Airport (KMMV) | 2026-04-29 21:21 UTC | 2026-04-29 21:34 UTC | 12m |
| N73929 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-29 21:11 UTC | 2026-04-29 21:33 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
