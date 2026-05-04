# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_21:19:12_UTC-green)

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

**Latest saved flight:** 2026-05-04 21:19:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 21:19:12 UTC

- **68,453** saved flights
- **25,696** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,453** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **840,862.2 tonnes** estimated CO2 emissions
- **48,745,633 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2944 |
| 2 | SkyWest Airlines | 2537 |
| 3 | IndiGo | 1581 |
| 4 | EJA | 1231 |
| 5 | American Airlines | 1061 |
| 6 | Southwest Airlines | 964 |
| 7 | Lufthansa | 880 |
| 8 | ENY | 842 |
| 9 | Vueling | 675 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 636 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 579 |
| 14 | Delta Air Lines | 575 |
| 15 | AZU | 555 |
| 16 | Swiss International | 529 |
| 17 | QLK | 523 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 467 |
| 20 | easyJet | 454 |
| 21 | AEE | 451 |
| 22 | EJU | 447 |
| 23 | VIV | 425 |
| 24 | Cathay Pacific | 410 |
| 25 | Air France | 404 |
| 26 | Japan Airlines | 399 |
| 27 | AXB | 387 |
| 28 | CXK | 348 |
| 29 | AIQ | 346 |
| 30 | GLO | 331 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54221 |
| 2 | 🇪🇸 ES | 5020 |
| 3 | 🇮🇳 IN | 4979 |
| 4 | 🇦🇺 AU | 4497 |
| 5 | 🇧🇷 BR | 3845 |
| 6 | 🇩🇪 DE | 3831 |
| 7 | 🇮🇹 IT | 3762 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3363 |
| 10 | 🇬🇧 GB | 2974 |
| 11 | 🇫🇷 FR | 2721 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2172 |
| 14 | 🇬🇷 GR | 2060 |
| 15 | 🇨🇭 CH | 1903 |
| 16 | 🇳🇴 NO | 1871 |
| 17 | 🇲🇾 MY | 1635 |
| 18 | 🇿🇦 ZA | 1371 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1223 |
| 22 | 🇵🇭 PH | 1137 |
| 23 | 🇵🇱 PL | 1125 |
| 24 | 🇬🇹 GT | 1110 |
| 25 | 🇰🇷 KR | 1089 |
| 26 | 🇲🇦 MA | 832 |
| 27 | 🇲🇴 MO | 771 |
| 28 | 🇲🇪 ME | 742 |
| 29 | 🇳🇱 NL | 713 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1508 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1124 |
| 4 | Indira Gandhi International Airport |  | IN | 1042 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1006 |
| 6 | Frankfurt am Main International Airport |  | DE | 881 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Guaymaral Airport |  | CO | 852 |
| 9 | Harry Reid International Airport |  | US | 847 |
| 10 | La Aurora Airport |  | GT | 826 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 771 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 673 |
| 14 | Chicago O'Hare International Airport |  | US | 659 |
| 15 | Kuala Lumpur International Airport |  | MY | 656 |
| 16 | Madrid Barajas International Airport |  | ES | 654 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 609 |
| 18 | Bengaluru International Airport |  | IN | 603 |
| 19 | Malpensa International Airport |  | IT | 599 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 21 | Congonhas Airport |  | BR | 551 |
| 22 | Salt Lake City International Airport |  | US | 546 |
| 23 | Charlotte/Douglas International Airport |  | US | 540 |
| 24 | Tenerife Norte Airport |  | ES | 540 |
| 25 | Charles de Gaulle International Airport |  | FR | 538 |
| 26 | Capua Airport |  | IT | 528 |
| 27 | Ninoy Aquino International Airport |  | PH | 517 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 502 |
| 29 | Daniel K Inouye International Airport |  | US | 498 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 481 |
| 31 | Barcelona International Airport |  | ES | 474 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 463 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 457 |
| 34 | Vitoria/Foronda Airport |  | ES | 455 |
| 35 | O. R. Tambo International Airport |  | ZA | 434 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 427 |
| 38 | Amsterdam Airport Schiphol |  | NL | 420 |
| 39 | Reno/Tahoe International Airport |  | US | 409 |
| 40 | Calgary International Airport |  | CA | 403 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 234 | 21m | 244 km | 985.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 154 | 26m | 275 km | 729.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 130 | 21m | 99 km | 222.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 114 | 27m | 152 km | 297.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 113 | 31m | 369 km | 719.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 96 | 14m | 154 km | 254.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 94 | 1h 2m | 695 km | 1,126.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N20KT |  | T-Bo Field (WI32) | Iowa City Municipal Airport (KIOW) | 2026-05-04 20:00 UTC | 2026-05-04 21:19 UTC | 1h 18m |
| ETH3718 | Ethiopian Airlines | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-05-04 10:30 UTC | 2026-05-04 21:03 UTC | 10h 32m |
| HK259G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-04 20:47 UTC | 2026-05-04 20:59 UTC | 12m |
| BPX290 | BPX | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-05-04 20:38 UTC | 2026-05-04 20:57 UTC | 19m |
| CXK168 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-05-04 20:02 UTC | 2026-05-04 20:53 UTC | 50m |
|  |  | Castroville Municipal Airport (KCVB) | Castroville Municipal Airport (KCVB) | 2026-05-04 20:53 UTC | 2026-05-04 20:53 UTC | 0m |
| WIF1H | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-05-04 20:39 UTC | 2026-05-04 20:50 UTC | 10m |
| N410FC |  | Chicago Executive Airport (KPWK) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-04 20:28 UTC | 2026-05-04 20:50 UTC | 21m |
| N717PK |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-04 20:31 UTC | 2026-05-04 20:48 UTC | 16m |
| N1602M |  | Harford County Airport (K0W3) | Harford County Airport (K0W3) | 2026-05-04 20:47 UTC | 2026-05-04 20:48 UTC | 0m |
| N96TE |  | Stag Air Park (7NC1) | Raleigh-Durham International Airport (KRDU) | 2026-05-04 20:22 UTC | 2026-05-04 20:46 UTC | 23m |
| N37VR |  | Daytona Beach International Airport (KDAB) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-04 19:09 UTC | 2026-05-04 20:45 UTC | 1h 35m |
| N316TS |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-04 20:07 UTC | 2026-05-04 20:44 UTC | 37m |
| BECT75A | BEC | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Dittemore Field (5KS2) | 2026-05-04 18:43 UTC | 2026-05-04 20:43 UTC | 2h 0m |
| UAE34Q | Emirates | Newcastle Airport (EGNT) | Buraimi Airport (OOBR) | 2026-05-04 13:31 UTC | 2026-05-04 20:42 UTC | 7h 10m |
| GPD202 | GPD | New Bedford Regional Airport (KEWB) | Teterboro Airport (KTEB) | 2026-05-04 19:58 UTC | 2026-05-04 20:42 UTC | 44m |
| WMU79 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Brooks Field (KRMY) | 2026-05-04 20:02 UTC | 2026-05-04 20:42 UTC | 39m |
| LXJ345 | LXJ | Louis Armstrong New Orleans International Airport (KMSY) | Rocky Mountain Metro Airport (KBJC) | 2026-05-04 17:36 UTC | 2026-05-04 20:40 UTC | 3h 4m |
| DCM4087 | DCM | Marksville Municipal Airport (KMKV) | Lakefront Airport (KNEW) | 2026-05-04 20:11 UTC | 2026-05-04 20:36 UTC | 25m |
| DLH3EY | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-05-04 19:41 UTC | 2026-05-04 20:35 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
