# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_06:23:45_UTC-green)

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

**Latest saved flight:** 2026-04-26 06:23:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 06:23:45 UTC

- **54,732** saved flights
- **21,620** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,732** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **659,354.1 tonnes** estimated CO2 emissions
- **38,223,426 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2304 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1236 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 647 |
| 9 | Vueling | 549 |
| 10 | AXM | 528 |
| 11 | LATAM Airlines | 526 |
| 12 | All Nippon Airways | 484 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | QLK | 422 |
| 17 | Swiss International | 420 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 363 |
| 21 | VIV | 352 |
| 22 | EJU | 349 |
| 23 | easyJet | 349 |
| 24 | Japan Airlines | 318 |
| 25 | Air France | 313 |
| 26 | Cathay Pacific | 308 |
| 27 | AXB | 288 |
| 28 | AIQ | 280 |
| 29 | JetBlue | 280 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43670 |
| 2 | 🇪🇸 ES | 3961 |
| 3 | 🇮🇳 IN | 3896 |
| 4 | 🇦🇺 AU | 3696 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2953 |
| 7 | 🇯🇵 JP | 2936 |
| 8 | 🇩🇪 DE | 2929 |
| 9 | 🇨🇦 CA | 2721 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2283 |
| 12 | 🇫🇷 FR | 2126 |
| 13 | 🇲🇽 MX | 1720 |
| 14 | 🇬🇷 GR | 1626 |
| 15 | 🇨🇭 CH | 1538 |
| 16 | 🇳🇴 NO | 1456 |
| 17 | 🇲🇾 MY | 1283 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1037 |
| 20 | 🇹🇷 TR | 990 |
| 21 | 🇹🇭 TH | 983 |
| 22 | 🇵🇭 PH | 934 |
| 23 | 🇰🇷 KR | 882 |
| 24 | 🇵🇱 PL | 875 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 686 |
| 27 | 🇲🇪 ME | 591 |
| 28 | 🇳🇱 NL | 555 |
| 29 | 🇲🇴 MO | 554 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1247 |
| 2 | Tokyo International Airport |  | JP | 998 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 825 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 802 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 703 |
| 9 | Zurich Airport |  | CH | 647 |
| 10 | Frankfurt am Main International Airport |  | DE | 631 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 554 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 511 |
| 17 | Madrid Barajas International Airport |  | ES | 505 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 486 |
| 19 | Malpensa International Airport |  | IT | 469 |
| 20 | Bengaluru International Airport |  | IN | 465 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 431 |
| 25 | Salt Lake City International Airport |  | US | 415 |
| 26 | Charles de Gaulle International Airport |  | FR | 414 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 400 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 389 |
| 31 | Vitoria/Foronda Airport |  | ES | 374 |
| 32 | Barcelona International Airport |  | ES | 371 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 359 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 336 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 248 | 1h 7m | 706 km | 3,019.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 178 | 24m | 225 km | 690.6 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 158 | 1h 27m | 910 km | 2,479.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 132 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 127 | 26m | 275 km | 601.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 103 | 1h 11m | 770 km | 1,368.3 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 94 | 31m | 369 km | 598.3 t |
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
| THY7MV | Turkish Airlines | Antalya International Airport (LTAI) | Sabiha Gokcen International Airport (LTFJ) | 2026-04-26 05:38 UTC | 2026-04-26 06:23 UTC | 45m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Ein Yahav Airfield (LLEY) | 2026-04-26 05:52 UTC | 2026-04-26 06:10 UTC | 17m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-26 05:40 UTC | 2026-04-26 06:03 UTC | 23m |
| EWG4QK | EWG | Dusseldorf International Airport (EDDL) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-26 04:34 UTC | 2026-04-26 06:02 UTC | 1h 28m |
| QLK42D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-26 05:35 UTC | 2026-04-26 06:01 UTC | 25m |
| RYR5XE | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-04-26 05:01 UTC | 2026-04-26 06:00 UTC | 59m |
| CWA927 | CWA | Edmonton International Airport (CYEG) | Provost Airport (CEH6) | 2026-04-26 05:28 UTC | 2026-04-26 05:57 UTC | 29m |
| N398GF |  | Ted Stevens Anchorage International Airport (PANC) | AK04 (AK04) | 2026-04-26 05:26 UTC | 2026-04-26 05:55 UTC | 28m |
| SNJ35 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-26 04:11 UTC | 2026-04-26 05:54 UTC | 1h 42m |
| BBC601 | BBC | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-04-26 05:30 UTC | 2026-04-26 05:49 UTC | 18m |
| N874BU |  | Peter O Knight Airport (KTPF) | Wimauma Air Park (FD77) | 2026-04-26 05:31 UTC | 2026-04-26 05:48 UTC | 17m |
| AWQ180 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-04-26 05:32 UTC | 2026-04-26 05:45 UTC | 13m |
| VOE2032 | VOE | Lyon Saint-Exupery Airport (LFLL) | Sinj Glider Airport (LDSS) | 2026-04-26 04:32 UTC | 2026-04-26 05:43 UTC | 1h 11m |
| EWG8ET | EWG | Dusseldorf International Airport (EDDL) | Zemunik Airport (LDZD) | 2026-04-26 04:22 UTC | 2026-04-26 05:41 UTC | 1h 19m |
| AM261 |  | Sydney Kingsford Smith International Airport (YSSY) | Coonabarabran Airport (YCBB) | 2026-04-26 04:59 UTC | 2026-04-26 05:41 UTC | 42m |
| IGO36DC | IndiGo | Bengaluru International Airport (VOBL) | Coimbatore International Airport (VOCB) | 2026-04-26 05:17 UTC | 2026-04-26 05:40 UTC | 22m |
| VTFTO | VTF | Salem Airport (VOSM) | Mysore Airport (VOMY) | 2026-04-26 04:51 UTC | 2026-04-26 05:39 UTC | 48m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-04-26 04:42 UTC | 2026-04-26 05:38 UTC | 56m |
| AWA473 | AWA | VGZR (VGZR) | Balurghat Airport (VEBG) | 2026-04-26 04:48 UTC | 2026-04-26 05:38 UTC | 50m |
| AM295 |  | Sydney Kingsford Smith International Airport (YSSY) | Grenfell Airport (YGNF) | 2026-04-26 05:00 UTC | 2026-04-26 05:38 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
