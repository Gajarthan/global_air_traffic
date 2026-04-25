# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_20:38:56_UTC-green)

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

**Latest saved flight:** 2026-04-25 20:38:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 20:38:56 UTC

- **54,256** saved flights
- **21,496** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,256** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **651,110.0 tonnes** estimated CO2 emissions
- **37,745,505 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2291 |
| 2 | SkyWest Airlines | 2049 |
| 3 | IndiGo | 1228 |
| 4 | EJA | 963 |
| 5 | American Airlines | 873 |
| 6 | Southwest Airlines | 772 |
| 7 | ENY | 684 |
| 8 | Lufthansa | 642 |
| 9 | Vueling | 547 |
| 10 | AXM | 522 |
| 11 | LATAM Airlines | 522 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 461 |
| 14 | Delta Air Lines | 449 |
| 15 | WIF | 448 |
| 16 | Swiss International | 419 |
| 17 | QLK | 416 |
| 18 | LXJ | 397 |
| 19 | AEE | 362 |
| 20 | Alaska Airlines | 356 |
| 21 | EJU | 348 |
| 22 | easyJet | 348 |
| 23 | VIV | 347 |
| 24 | Air France | 313 |
| 25 | Japan Airlines | 313 |
| 26 | Cathay Pacific | 288 |
| 27 | AXB | 286 |
| 28 | AIQ | 277 |
| 29 | GLO | 277 |
| 30 | JetBlue | 277 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43262 |
| 2 | 🇪🇸 ES | 3946 |
| 3 | 🇮🇳 IN | 3864 |
| 4 | 🇦🇺 AU | 3625 |
| 5 | 🇧🇷 BR | 3145 |
| 6 | 🇮🇹 IT | 2934 |
| 7 | 🇩🇪 DE | 2904 |
| 8 | 🇯🇵 JP | 2889 |
| 9 | 🇨🇦 CA | 2696 |
| 10 | 🇨🇴 CO | 2471 |
| 11 | 🇬🇧 GB | 2274 |
| 12 | 🇫🇷 FR | 2119 |
| 13 | 🇲🇽 MX | 1697 |
| 14 | 🇬🇷 GR | 1624 |
| 15 | 🇨🇭 CH | 1535 |
| 16 | 🇳🇴 NO | 1455 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1019 |
| 20 | 🇹🇷 TR | 979 |
| 21 | 🇹🇭 TH | 975 |
| 22 | 🇵🇭 PH | 918 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 872 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 682 |
| 27 | 🇲🇪 ME | 588 |
| 28 | 🇳🇱 NL | 552 |
| 29 | 🇲🇴 MO | 533 |
| 30 | 🇧🇸 BS | 471 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1235 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 901 |
| 4 | El Dorado International Airport |  | CO | 837 |
| 5 | Indira Gandhi International Airport |  | IN | 822 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 801 |
| 7 | Guaymaral Airport |  | CO | 743 |
| 8 | Harry Reid International Airport |  | US | 700 |
| 9 | Zurich Airport |  | CH | 645 |
| 10 | Frankfurt am Main International Airport |  | DE | 626 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 536 |
| 13 | Macau International Airport |  | MO | 533 |
| 14 | Chicago O'Hare International Airport |  | US | 531 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 514 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 504 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 472 |
| 19 | Malpensa International Airport |  | IT | 465 |
| 20 | Bengaluru International Airport |  | IN | 461 |
| 21 | Congonhas Airport |  | BR | 452 |
| 22 | Charlotte/Douglas International Airport |  | US | 444 |
| 23 | Tenerife Norte Airport |  | ES | 434 |
| 24 | Ninoy Aquino International Airport |  | PH | 424 |
| 25 | Salt Lake City International Airport |  | US | 411 |
| 26 | Charles de Gaulle International Airport |  | FR | 411 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 405 |
| 28 | Capua Airport |  | IT | 398 |
| 29 | Daniel K Inouye International Airport |  | US | 392 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 385 |
| 31 | Vitoria/Foronda Airport |  | ES | 372 |
| 32 | Barcelona International Airport |  | ES | 367 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 364 |
| 34 | Reno/Tahoe International Airport |  | US | 363 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 358 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 358 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 324 |
| 40 | Viracopos International Airport |  | BR | 320 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 301 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 166 | 21m | 244 km | 699.0 t |
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
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 73 | 1h 53m | 1,304 km | 1,642.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 72 | 23m | 55 km | 68.4 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 70 | 1h 19m | 961 km | 1,160.3 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TMN125 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-04-25 11:43 UTC | 2026-04-25 20:38 UTC | 8h 55m |
| CPA865 | Cathay Pacific | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-04-25 07:49 UTC | 2026-04-25 20:36 UTC | 12h 47m |
| HKC6652 | HKC | VGZR (VGZR) | Zhuhai Airport (ZGSD) | 2026-04-25 15:31 UTC | 2026-04-25 20:28 UTC | 4h 57m |
| HKC9484 | HKC | Istanbul Hezarfen Airfield (LTBW) | Zhuhai Airport (ZGSD) | 2026-04-25 08:53 UTC | 2026-04-25 20:24 UTC | 11h 31m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-25 20:12 UTC | 2026-04-25 20:23 UTC | 11m |
| TKR184 | TKR | Lake City Gateway Airport (KLCQ) | Cuyler Field (FD27) | 2026-04-25 19:45 UTC | 2026-04-25 20:21 UTC | 35m |
| N23VB |  | Redstone Ranch Airport (TS76) | Gillespie County Airport (KT82) | 2026-04-25 20:08 UTC | 2026-04-25 20:21 UTC | 12m |
| N1293E |  | Airglades Airport (K2IS) | Airglades Airport (K2IS) | 2026-04-25 19:44 UTC | 2026-04-25 20:21 UTC | 36m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 20:02 UTC | 2026-04-25 20:17 UTC | 15m |
| N68750 |  | Bob Walberg Field (IL36) | Watertown Municipal Airport (KRYV) | 2026-04-25 19:35 UTC | 2026-04-25 20:16 UTC | 40m |
| N112UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-04-25 19:58 UTC | 2026-04-25 20:14 UTC | 16m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-04-25 05:45 UTC | 2026-04-25 20:10 UTC | 14h 25m |
| N172KJ |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-25 19:48 UTC | 2026-04-25 20:04 UTC | 15m |
| N114UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-04-25 19:49 UTC | 2026-04-25 20:03 UTC | 13m |
| LVX666 | LVX | Mariano Moreno Airport (SADJ) | Mariano Moreno Airport (SADJ) | 2026-04-25 20:02 UTC | 2026-04-25 20:02 UTC | 0m |
| N25430 |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-04-25 19:51 UTC | 2026-04-25 20:02 UTC | 10m |
| N850UW |  | 1WI9 (1WI9) | Dane County Regional/Truax Field (KMSN) | 2026-04-25 19:49 UTC | 2026-04-25 20:01 UTC | 12m |
| N940QS |  | Fort Lauderdale Executive Airport (KFXE) | Miami Executive Airport (KTMB) | 2026-04-25 13:59 UTC | 2026-04-25 19:58 UTC | 5h 59m |
| N220BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-25 19:10 UTC | 2026-04-25 19:54 UTC | 44m |
| N592CL |  | Harry Reid International Airport (KLAS) | Dry Pen Airport (16CO) | 2026-04-25 18:59 UTC | 2026-04-25 19:53 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
