# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_20:34:06_UTC-green)

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

**Latest saved flight:** 2026-05-18 20:34:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-18 20:34:06 UTC

- **87,588** saved flights
- **31,327** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,588** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,084,205.3 tonnes** estimated CO2 emissions
- **62,852,480 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3753 |
| 2 | SkyWest Airlines | 3248 |
| 3 | IndiGo | 1868 |
| 4 | EJA | 1661 |
| 5 | American Airlines | 1347 |
| 6 | Southwest Airlines | 1278 |
| 7 | Lufthansa | 1102 |
| 8 | ENY | 1089 |
| 9 | Delta Air Lines | 962 |
| 10 | Vueling | 837 |
| 11 | LATAM Airlines | 790 |
| 12 | AXM | 782 |
| 13 | WIF | 749 |
| 14 | AZU | 692 |
| 15 | Swiss International | 675 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 643 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 624 |
| 20 | easyJet | 577 |
| 21 | EJU | 565 |
| 22 | Cathay Pacific | 555 |
| 23 | AEE | 547 |
| 24 | VIV | 527 |
| 25 | Air France | 511 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 460 |
| 28 | AXB | 457 |
| 29 | MXY | 447 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71869 |
| 2 | 🇪🇸 ES | 6215 |
| 3 | 🇮🇳 IN | 5850 |
| 4 | 🇦🇺 AU | 5486 |
| 5 | 🇩🇪 DE | 4867 |
| 6 | 🇮🇹 IT | 4859 |
| 7 | 🇧🇷 BR | 4814 |
| 8 | 🇨🇦 CA | 4374 |
| 9 | 🇯🇵 JP | 4323 |
| 10 | 🇬🇧 GB | 3736 |
| 11 | 🇫🇷 FR | 3499 |
| 12 | 🇨🇴 CO | 2971 |
| 13 | 🇲🇽 MX | 2732 |
| 14 | 🇬🇷 GR | 2546 |
| 15 | 🇳🇴 NO | 2421 |
| 16 | 🇨🇭 CH | 2317 |
| 17 | 🇲🇾 MY | 1965 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1591 |
| 20 | 🇳🇿 NZ | 1519 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1455 |
| 23 | 🇰🇷 KR | 1360 |
| 24 | 🇵🇭 PH | 1354 |
| 25 | 🇬🇹 GT | 1323 |
| 26 | 🇲🇦 MA | 1016 |
| 27 | 🇲🇴 MO | 1016 |
| 28 | 🇲🇪 ME | 907 |
| 29 | 🇳🇱 NL | 892 |
| 30 | 🇭🇷 HR | 788 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1928 |
| 2 | Denver International Airport |  | US | 1467 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1258 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1208 |
| 6 | Harry Reid International Airport |  | US | 1114 |
| 7 | Frankfurt am Main International Airport |  | DE | 1113 |
| 8 | Zurich Airport |  | CH | 1044 |
| 9 | Macau International Airport |  | MO | 1016 |
| 10 | Guaymaral Airport |  | CO | 1009 |
| 11 | La Aurora Airport |  | GT | 1004 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 973 |
| 13 | El Dorado International Airport |  | CO | 949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 887 |
| 15 | Chicago O'Hare International Airport |  | US | 846 |
| 16 | Madrid Barajas International Airport |  | ES | 796 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 754 |
| 19 | Capua Airport |  | IT | 742 |
| 20 | Salt Lake City International Airport |  | US | 731 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 22 | Malpensa International Airport |  | IT | 716 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 680 |
| 25 | Charlotte/Douglas International Airport |  | US | 679 |
| 26 | Congonhas Airport |  | BR | 673 |
| 27 | Daniel K Inouye International Airport |  | US | 643 |
| 28 | Tenerife Norte Airport |  | ES | 641 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 591 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 582 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 562 |
| 35 | Vitoria/Foronda Airport |  | ES | 559 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 552 |
| 37 | Amsterdam Airport Schiphol |  | NL | 546 |
| 38 | Don Mueang International Airport |  | TH | 545 |
| 39 | Calgary International Airport |  | CA | 517 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 414 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 327 | 21m | 244 km | 1,376.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 225 | 14m | 114 km | 441.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 223 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 127 | 20m | 147 km | 321.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 113 | 18m | 144 km | 281.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| URSA32 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-18 20:22 UTC | 2026-05-18 20:34 UTC | 11m |
| VIV7060 | VIV | Cancun International Airport (MMUN) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-05-18 18:44 UTC | 2026-05-18 20:29 UTC | 1h 44m |
| N247EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-18 17:36 UTC | 2026-05-18 20:24 UTC | 2h 48m |
| BPX252 | BPX | Cobb County International/Mccollum Field (KRYY) | Cartersville Airport (KVPC) | 2026-05-18 19:37 UTC | 2026-05-18 20:22 UTC | 45m |
| JEDI43 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Hattiesburg Bobby L Chain Municipal Airport (KHBG) | 2026-05-18 19:46 UTC | 2026-05-18 20:20 UTC | 34m |
| KEN46 | KEN | Seattle Paine Field International Airport (KPAE) | William R Fairchild International Airport (KCLM) | 2026-05-18 19:39 UTC | 2026-05-18 20:18 UTC | 39m |
| EDGE91 | EDG | Jones Farm Field (OK12) | Perkins Airport (5OK8) | 2026-05-18 19:41 UTC | 2026-05-18 20:15 UTC | 34m |
| N63681 |  | Mckinney Ntl Airport (KTKI) | 31TS (31TS) | 2026-05-18 18:45 UTC | 2026-05-18 20:14 UTC | 1h 29m |
| R21236 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-18 19:05 UTC | 2026-05-18 20:14 UTC | 1h 8m |
| XBMHJ | XBM | General Mariano Matamoros Airport (MMCB) | Chilpancingo Airport (MMCH) | 2026-05-18 19:47 UTC | 2026-05-18 20:09 UTC | 21m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-18 19:45 UTC | 2026-05-18 20:06 UTC | 20m |
| PAIN11 | PAI | Flying E Ranch Airport (OK16) | Henderson Farm Airport (35OL) | 2026-05-18 19:38 UTC | 2026-05-18 20:06 UTC | 27m |
| N604SG |  | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-05-18 19:23 UTC | 2026-05-18 20:05 UTC | 41m |
| LFA316 | LFA | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-05-18 19:27 UTC | 2026-05-18 20:04 UTC | 36m |
| N197BL |  | San Marcos Regional Airport (KHYI) | 52TE (52TE) | 2026-05-18 19:26 UTC | 2026-05-18 19:58 UTC | 31m |
| KYOTE048 | KYO | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-05-18 19:38 UTC | 2026-05-18 19:56 UTC | 17m |
| SWR8YP | Swiss International | Belgrade Nikola Tesla Airport (LYBE) | Zurich Airport (LSZH) | 2026-05-18 18:21 UTC | 2026-05-18 19:54 UTC | 1h 32m |
| PJC94 | PJC | Tulsa International Airport (KTUL) | Gail Ballard Airport (SN63) | 2026-05-18 19:21 UTC | 2026-05-18 19:51 UTC | 30m |
| CTF273 | CTF | Phoenix Deer Valley Airport (KDVT) | Austin-Bergstrom International Airport (KAUS) | 2026-05-18 17:34 UTC | 2026-05-18 19:48 UTC | 2h 14m |
| N48JA |  | De Kalb Taylor Municipal Airport (KDKB) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-18 19:44 UTC | 2026-05-18 19:44 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
