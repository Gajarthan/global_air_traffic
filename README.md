# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_10:37:19_UTC-green)

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

**Latest saved flight:** 2026-05-05 10:37:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 10:37:19 UTC

- **68,995** saved flights
- **25,839** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,995** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **848,671.3 tonnes** estimated CO2 emissions
- **49,198,338 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2961 |
| 2 | SkyWest Airlines | 2557 |
| 3 | IndiGo | 1594 |
| 4 | EJA | 1242 |
| 5 | American Airlines | 1071 |
| 6 | Southwest Airlines | 978 |
| 7 | Lufthansa | 890 |
| 8 | ENY | 851 |
| 9 | Vueling | 675 |
| 10 | AXM | 663 |
| 11 | LATAM Airlines | 640 |
| 12 | WIF | 584 |
| 13 | All Nippon Airways | 583 |
| 14 | Delta Air Lines | 580 |
| 15 | AZU | 559 |
| 16 | QLK | 533 |
| 17 | Swiss International | 533 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 473 |
| 20 | easyJet | 460 |
| 21 | AEE | 452 |
| 22 | EJU | 448 |
| 23 | VIV | 430 |
| 24 | Cathay Pacific | 416 |
| 25 | Japan Airlines | 409 |
| 26 | Air France | 407 |
| 27 | AXB | 388 |
| 28 | AIQ | 350 |
| 29 | CXK | 348 |
| 30 | MXY | 337 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54646 |
| 2 | 🇪🇸 ES | 5037 |
| 3 | 🇮🇳 IN | 5012 |
| 4 | 🇦🇺 AU | 4587 |
| 5 | 🇩🇪 DE | 3867 |
| 6 | 🇧🇷 BR | 3864 |
| 7 | 🇮🇹 IT | 3776 |
| 8 | 🇯🇵 JP | 3717 |
| 9 | 🇨🇦 CA | 3400 |
| 10 | 🇬🇧 GB | 2995 |
| 11 | 🇫🇷 FR | 2728 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2193 |
| 14 | 🇬🇷 GR | 2070 |
| 15 | 🇨🇭 CH | 1910 |
| 16 | 🇳🇴 NO | 1882 |
| 17 | 🇲🇾 MY | 1652 |
| 18 | 🇿🇦 ZA | 1381 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1254 |
| 21 | 🇹🇷 TR | 1237 |
| 22 | 🇵🇭 PH | 1154 |
| 23 | 🇵🇱 PL | 1133 |
| 24 | 🇬🇹 GT | 1113 |
| 25 | 🇰🇷 KR | 1107 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 785 |
| 28 | 🇲🇪 ME | 747 |
| 29 | 🇳🇱 NL | 721 |
| 30 | 🇮🇩 ID | 587 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1524 |
| 2 | Tokyo International Airport |  | JP | 1254 |
| 3 | Denver International Airport |  | US | 1131 |
| 4 | Indira Gandhi International Airport |  | IN | 1048 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1011 |
| 6 | Frankfurt am Main International Airport |  | DE | 884 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 859 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 828 |
| 11 | Zurich Airport |  | CH | 818 |
| 12 | Macau International Airport |  | MO | 785 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 681 |
| 14 | Kuala Lumpur International Airport |  | MY | 662 |
| 15 | Chicago O'Hare International Airport |  | US | 660 |
| 16 | Madrid Barajas International Airport |  | ES | 655 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 617 |
| 18 | Bengaluru International Airport |  | IN | 605 |
| 19 | Malpensa International Airport |  | IT | 602 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 600 |
| 21 | Salt Lake City International Airport |  | US | 552 |
| 22 | Congonhas Airport |  | BR | 552 |
| 23 | Charlotte/Douglas International Airport |  | US | 543 |
| 24 | Charles de Gaulle International Airport |  | FR | 543 |
| 25 | Tenerife Norte Airport |  | ES | 542 |
| 26 | Capua Airport |  | IT | 529 |
| 27 | Ninoy Aquino International Airport |  | PH | 525 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 509 |
| 29 | Daniel K Inouye International Airport |  | US | 502 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 487 |
| 31 | Barcelona International Airport |  | ES | 478 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 460 |
| 34 | Vitoria/Foronda Airport |  | ES | 456 |
| 35 | Don Mueang International Airport |  | TH | 440 |
| 36 | O. R. Tambo International Airport |  | ZA | 437 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 430 |
| 38 | Amsterdam Airport Schiphol |  | NL | 425 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 408 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 236 | 21m | 244 km | 993.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 167 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 155 | 26m | 275 km | 734.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 131 | 21m | 99 km | 224.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 127 | 44m | 452 km | 989.8 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 116 | 31m | 369 km | 738.4 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 109 | 20m | 250 km | 470.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 106 | 27m | 215 km | 392.6 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 98 | 14m | 154 km | 259.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| REV61T | REV | East Midlands Airport (EGNX) | Liverpool John Lennon Airport (EGGP) | 2026-05-05 09:46 UTC | 2026-05-05 10:37 UTC | 51m |
| TAP028 | TAP Air Portugal | Lisbon Portela Airport (LPPT) | Lisbon Portela Airport (LPPT) | 2026-05-04 17:10 UTC | 2026-05-05 10:33 UTC | 17h 22m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-05-05 09:45 UTC | 2026-05-05 10:28 UTC | 42m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-05-05 09:00 UTC | 2026-05-05 10:01 UTC | 1h 1m |
| EZY9 | easyJet | London Gatwick Airport (EGKK) | Durham Tees Valley Airport (EGNV) | 2026-05-05 08:20 UTC | 2026-05-05 10:00 UTC | 1h 40m |
| KAYI0004 | KAY | Tekirdag Corlu Airport (LTBU) | Sinop Airport (LTCM) | 2026-05-05 07:28 UTC | 2026-05-05 09:58 UTC | 2h 30m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Kauhajoki Airport (EFKJ) | 2026-05-05 09:13 UTC | 2026-05-05 09:57 UTC | 44m |
| RYR91KF | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Valencia Airport (LEVC) | 2026-05-05 07:57 UTC | 2026-05-05 09:51 UTC | 1h 53m |
| RYR418Z | Ryanair | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-05-05 09:15 UTC | 2026-05-05 09:44 UTC | 28m |
| AFR256 | Air France | Charles de Gaulle International Airport (LFPG) | Tanjung Balai Airport (WIBT) | 2026-05-04 21:43 UTC | 2026-05-05 09:41 UTC | 11h 58m |
| SKYHWK1 | SKY | Nordholz Airport (ETMN) | Juist Airport (EDWJ) | 2026-05-05 09:30 UTC | 2026-05-05 09:41 UTC | 10m |
| RYR17MN | Ryanair | Malaga Airport (LEMG) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-05 06:33 UTC | 2026-05-05 09:40 UTC | 3h 7m |
| AUR100T | AUR | Jersey Airport (EGJJ) | Jersey Airport (EGJJ) | 2026-05-05 08:08 UTC | 2026-05-05 09:40 UTC | 1h 32m |
| LSI145 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-04 22:32 UTC | 2026-05-05 09:39 UTC | 11h 6m |
| NAY27XK | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-05-05 09:27 UTC | 2026-05-05 09:37 UTC | 10m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-05-05 07:35 UTC | 2026-05-05 09:36 UTC | 2h 1m |
| ZAM29 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-05 09:26 UTC | 2026-05-05 09:36 UTC | 10m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-05 08:30 UTC | 2026-05-05 09:36 UTC | 1h 5m |
| SEH011 | SEH | Astypalaia Airport (LGPL) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-05 08:51 UTC | 2026-05-05 09:35 UTC | 44m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-05-05 09:14 UTC | 2026-05-05 09:35 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
