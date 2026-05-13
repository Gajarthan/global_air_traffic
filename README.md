# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_23:37:11_UTC-green)

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

**Latest saved flight:** 2026-05-13 23:37:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 23:37:11 UTC

- **81,105** saved flights
- **29,440** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,105** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **999,454.7 tonnes** estimated CO2 emissions
- **57,939,405 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3477 |
| 2 | SkyWest Airlines | 3019 |
| 3 | IndiGo | 1777 |
| 4 | EJA | 1520 |
| 5 | American Airlines | 1252 |
| 6 | Southwest Airlines | 1186 |
| 7 | Lufthansa | 1055 |
| 8 | ENY | 1019 |
| 9 | Delta Air Lines | 892 |
| 10 | Vueling | 771 |
| 11 | LATAM Airlines | 741 |
| 12 | AXM | 734 |
| 13 | WIF | 702 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 640 |
| 16 | Swiss International | 630 |
| 17 | QLK | 598 |
| 18 | LXJ | 592 |
| 19 | Alaska Airlines | 572 |
| 20 | easyJet | 538 |
| 21 | EJU | 521 |
| 22 | AEE | 517 |
| 23 | Cathay Pacific | 509 |
| 24 | VIV | 483 |
| 25 | Air France | 476 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 439 |
| 28 | CXK | 423 |
| 29 | United Airlines | 402 |
| 30 | MXY | 401 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66171 |
| 2 | 🇪🇸 ES | 5760 |
| 3 | 🇮🇳 IN | 5559 |
| 4 | 🇦🇺 AU | 5177 |
| 5 | 🇩🇪 DE | 4568 |
| 6 | 🇧🇷 BR | 4486 |
| 7 | 🇮🇹 IT | 4481 |
| 8 | 🇯🇵 JP | 4125 |
| 9 | 🇨🇦 CA | 4040 |
| 10 | 🇬🇧 GB | 3472 |
| 11 | 🇫🇷 FR | 3219 |
| 12 | 🇨🇴 CO | 2721 |
| 13 | 🇲🇽 MX | 2453 |
| 14 | 🇬🇷 GR | 2368 |
| 15 | 🇳🇴 NO | 2259 |
| 16 | 🇨🇭 CH | 2183 |
| 17 | 🇲🇾 MY | 1840 |
| 18 | 🇿🇦 ZA | 1530 |
| 19 | 🇹🇷 TR | 1446 |
| 20 | 🇳🇿 NZ | 1420 |
| 21 | 🇹🇭 TH | 1419 |
| 22 | 🇵🇱 PL | 1350 |
| 23 | 🇵🇭 PH | 1276 |
| 24 | 🇬🇹 GT | 1240 |
| 25 | 🇰🇷 KR | 1237 |
| 26 | 🇲🇦 MA | 949 |
| 27 | 🇲🇴 MO | 934 |
| 28 | 🇲🇪 ME | 867 |
| 29 | 🇳🇱 NL | 837 |
| 30 | 🇭🇷 HR | 717 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1784 |
| 2 | Tokyo International Airport |  | JP | 1384 |
| 3 | Denver International Airport |  | US | 1366 |
| 4 | Indira Gandhi International Airport |  | IN | 1178 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1159 |
| 6 | Frankfurt am Main International Airport |  | DE | 1065 |
| 7 | Harry Reid International Airport |  | US | 1007 |
| 8 | Zurich Airport |  | CH | 967 |
| 9 | La Aurora Airport |  | GT | 937 |
| 10 | Macau International Airport |  | MO | 934 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 918 |
| 12 | Guaymaral Airport |  | CO | 913 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 820 |
| 15 | Chicago O'Hare International Airport |  | US | 790 |
| 16 | Madrid Barajas International Airport |  | ES | 742 |
| 17 | Kuala Lumpur International Airport |  | MY | 736 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 710 |
| 19 | Malpensa International Airport |  | IT | 689 |
| 20 | Bengaluru International Airport |  | IN | 683 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 681 |
| 22 | Salt Lake City International Airport |  | US | 672 |
| 23 | Capua Airport |  | IT | 660 |
| 24 | Charlotte/Douglas International Airport |  | US | 634 |
| 25 | Charles de Gaulle International Airport |  | FR | 633 |
| 26 | Congonhas Airport |  | BR | 632 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Daniel K Inouye International Airport |  | US | 587 |
| 29 | Ninoy Aquino International Airport |  | PH | 583 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 579 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 544 |
| 32 | Barcelona International Airport |  | ES | 542 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 541 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 526 |
| 35 | Vitoria/Foronda Airport |  | ES | 513 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 510 |
| 37 | Don Mueang International Airport |  | TH | 508 |
| 38 | Amsterdam Airport Schiphol |  | NL | 506 |
| 39 | O. R. Tambo International Airport |  | ZA | 486 |
| 40 | Calgary International Airport |  | CA | 480 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 291 | 21m | 244 km | 1,225.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 232 | 24m | 225 km | 900.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 216 | 1h 27m | 910 km | 3,389.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 208 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 192 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 185 | 19m | 165 km | 526.2 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 183 | 1h 11m | 770 km | 2,431.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 127 | 31m | 369 km | 808.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 118 | 20m | 147 km | 298.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 108 | 57m | 493 km | 918.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 101 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N333AQ |  | Agua Dulce Airport (KL70) | Santa Monica Municipal Airport (KSMO) | 2026-05-13 23:16 UTC | 2026-05-13 23:37 UTC | 20m |
| TROY314 | TRO | North Island Nas (Halsey Field) Airport (KNZY) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-13 22:03 UTC | 2026-05-13 23:32 UTC | 1h 29m |
| UAL2852 | United Airlines | Miami International Airport (KMIA) | Denver International Airport (KDEN) | 2026-05-13 19:32 UTC | 2026-05-13 23:28 UTC | 3h 56m |
| N54FB |  | Des Moines International Airport (KDSM) | Colonel James Jabara Airport (KAAO) | 2026-05-13 22:38 UTC | 2026-05-13 23:25 UTC | 46m |
| N163MD |  | Fort Worth Meacham International Airport (KFTW) | Austin-Bergstrom International Airport (KAUS) | 2026-05-13 22:50 UTC | 2026-05-13 23:20 UTC | 30m |
| TKR219 | TKR | Saskatoon John G. Diefenbaker International Airport (CYXE) | Corman Air Park (CJN5) | 2026-05-13 21:03 UTC | 2026-05-13 23:20 UTC | 2h 16m |
| JRT545 | JRT | Burke Lakefront Airport (KBKL) | Braxton County Airport (K48I) | 2026-05-13 22:45 UTC | 2026-05-13 23:13 UTC | 27m |
| N575SD |  | Menominee Regional Airport (KMNM) | Clintonville Municipal Airport (KCLI) | 2026-05-13 22:39 UTC | 2026-05-13 23:13 UTC | 33m |
| N144AL |  | Fort Worth Meacham International Airport (KFTW) | Valley Vista Airport (6CA5) | 2026-05-13 20:28 UTC | 2026-05-13 23:13 UTC | 2h 45m |
| R20060 |  | Brown Field Municipal Airport (KSDM) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-13 23:01 UTC | 2026-05-13 23:11 UTC | 10m |
| N9702C |  | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | 2026-05-13 22:41 UTC | 2026-05-13 22:58 UTC | 17m |
| N327CH |  | Frasca Field (KC16) | Frasca Field (KC16) | 2026-05-13 22:51 UTC | 2026-05-13 22:54 UTC | 2m |
| N83NC |  | Washington Dulles International Airport (KIAD) | Wallace-Pender Airport (KACZ) | 2026-05-13 21:59 UTC | 2026-05-13 22:51 UTC | 51m |
| SIS918 | SIS | Camarillo Airport (KCMA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-13 22:03 UTC | 2026-05-13 22:51 UTC | 48m |
| SWA2544 | Southwest Airlines | Harry Reid International Airport (KLAS) | AL40 (AL40) | 2026-05-13 19:50 UTC | 2026-05-13 22:50 UTC | 2h 59m |
| N40ER |  | Savannah/Hilton Head International Airport (KSAV) | Swaids Field (2GA2) | 2026-05-13 22:32 UTC | 2026-05-13 22:49 UTC | 16m |
| ZFQ | ZFQ | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-05-13 22:26 UTC | 2026-05-13 22:49 UTC | 22m |
| TAM3964 | LATAM Airlines | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-05-13 22:05 UTC | 2026-05-13 22:48 UTC | 43m |
| N7071G |  | TX09 (TX09) | Gillespie County Airport (KT82) | 2026-05-13 22:10 UTC | 2026-05-13 22:48 UTC | 37m |
| N342T |  | City Of Colorado Springs Municipal Airport (KCOS) | 97CO (97CO) | 2026-05-13 22:32 UTC | 2026-05-13 22:47 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
