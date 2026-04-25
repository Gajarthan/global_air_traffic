# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_23:36:18_UTC-green)

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

**Latest saved flight:** 2026-04-25 23:36:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 23:36:18 UTC

- **54,504** saved flights
- **21,562** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,504** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **656,333.4 tonnes** estimated CO2 emissions
- **38,048,312 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2297 |
| 2 | SkyWest Airlines | 2068 |
| 3 | IndiGo | 1229 |
| 4 | EJA | 967 |
| 5 | American Airlines | 878 |
| 6 | Southwest Airlines | 778 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 642 |
| 9 | Vueling | 547 |
| 10 | LATAM Airlines | 526 |
| 11 | AXM | 522 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | Swiss International | 419 |
| 17 | QLK | 416 |
| 18 | LXJ | 397 |
| 19 | AEE | 362 |
| 20 | Alaska Airlines | 361 |
| 21 | VIV | 351 |
| 22 | EJU | 349 |
| 23 | easyJet | 349 |
| 24 | Air France | 313 |
| 25 | Japan Airlines | 313 |
| 26 | Cathay Pacific | 304 |
| 27 | AXB | 286 |
| 28 | GLO | 279 |
| 29 | JetBlue | 278 |
| 30 | AIQ | 277 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43569 |
| 2 | 🇪🇸 ES | 3952 |
| 3 | 🇮🇳 IN | 3869 |
| 4 | 🇦🇺 AU | 3631 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2945 |
| 7 | 🇩🇪 DE | 2909 |
| 8 | 🇯🇵 JP | 2891 |
| 9 | 🇨🇦 CA | 2713 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2282 |
| 12 | 🇫🇷 FR | 2124 |
| 13 | 🇲🇽 MX | 1713 |
| 14 | 🇬🇷 GR | 1624 |
| 15 | 🇨🇭 CH | 1537 |
| 16 | 🇳🇴 NO | 1455 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1023 |
| 20 | 🇹🇷 TR | 982 |
| 21 | 🇹🇭 TH | 975 |
| 22 | 🇵🇭 PH | 922 |
| 23 | 🇰🇷 KR | 875 |
| 24 | 🇵🇱 PL | 873 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 685 |
| 27 | 🇲🇪 ME | 589 |
| 28 | 🇳🇱 NL | 553 |
| 29 | 🇲🇴 MO | 547 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1247 |
| 2 | Tokyo International Airport |  | JP | 981 |
| 3 | Denver International Airport |  | US | 909 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 823 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 801 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 702 |
| 9 | Zurich Airport |  | CH | 646 |
| 10 | Frankfurt am Main International Airport |  | DE | 628 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 547 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 541 |
| 14 | Chicago O'Hare International Airport |  | US | 533 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 504 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 473 |
| 19 | Malpensa International Airport |  | IT | 468 |
| 20 | Bengaluru International Airport |  | IN | 461 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 426 |
| 25 | Salt Lake City International Airport |  | US | 413 |
| 26 | Charles de Gaulle International Airport |  | FR | 413 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Capua Airport |  | IT | 398 |
| 29 | Daniel K Inouye International Airport |  | US | 397 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 386 |
| 31 | Vitoria/Foronda Airport |  | ES | 372 |
| 32 | Barcelona International Airport |  | ES | 369 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 364 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 358 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 247 | 1h 7m | 706 km | 3,007.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 176 | 24m | 225 km | 682.8 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 169 | 21m | 244 km | 711.6 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 126 | 26m | 275 km | 597.1 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 93 | 31m | 369 km | 592.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-25 21:45 UTC | 2026-04-25 23:36 UTC | 1h 50m |
| OAI | OAI | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-25 23:14 UTC | 2026-04-25 23:35 UTC | 20m |
| CFBXH | CFB | Fort St. John Airport (CYXJ) | Fort St. John Airport (CYXJ) | 2026-04-25 22:53 UTC | 2026-04-25 23:19 UTC | 26m |
| N3312G |  | Dogs Run Free Airport (WA76) | Green Acres Airport (6WA3) | 2026-04-25 22:00 UTC | 2026-04-25 23:17 UTC | 1h 16m |
| IGO454H | IndiGo | Juhu Aerodrome (VAJJ) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-25 21:12 UTC | 2026-04-25 23:12 UTC | 2h 0m |
| N316PW |  | Boulder Creek Airstrip (44ID) | KU42 (KU42) | 2026-04-25 22:10 UTC | 2026-04-25 23:11 UTC | 1h 0m |
| BOE116 | BOE | Seattle Paine Field International Airport (KPAE) | Slinkard Airfield (WN31) | 2026-04-25 20:10 UTC | 2026-04-25 23:09 UTC | 2h 58m |
| FHY743 | FHY | Antalya International Airport (LTAI) | Deblin Military Air Base (EPDE) | 2026-04-25 20:35 UTC | 2026-04-25 23:04 UTC | 2h 29m |
| DHK011 | DHK | East Midlands Airport (EGNX) | Macau International Airport (VMMC) | 2026-04-25 11:38 UTC | 2026-04-25 23:01 UTC | 11h 23m |
| N225RH |  | Del Norte International Airport (MMAN) | Plan De Guadalupe International Airport (MMIO) | 2026-04-25 22:43 UTC | 2026-04-25 22:56 UTC | 12m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-04-25 11:26 UTC | 2026-04-25 22:55 UTC | 11h 29m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-04-25 12:03 UTC | 2026-04-25 22:50 UTC | 10h 46m |
| N158PT |  | Miami Executive Airport (KTMB) | Tampa Executive Airport (KVDF) | 2026-04-25 20:38 UTC | 2026-04-25 22:49 UTC | 2h 11m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-04-25 11:49 UTC | 2026-04-25 22:47 UTC | 10h 58m |
| FDX5124 | FDX | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-04-25 21:48 UTC | 2026-04-25 22:46 UTC | 58m |
| SKW6381 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-25 21:08 UTC | 2026-04-25 22:45 UTC | 1h 36m |
| N715ML |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-04-25 21:55 UTC | 2026-04-25 22:44 UTC | 48m |
| CXK416 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-04-25 22:24 UTC | 2026-04-25 22:43 UTC | 18m |
| SNJ91 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-25 21:34 UTC | 2026-04-25 22:42 UTC | 1h 7m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-25 12:06 UTC | 2026-04-25 22:41 UTC | 10h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
