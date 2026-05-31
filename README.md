# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_17:43:42_UTC-green)

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

**Latest saved flight:** 2026-05-31 17:43:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 17:43:42 UTC

- **99,429** saved flights
- **35,371** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **99,429** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,218,453.6 tonnes** estimated CO2 emissions
- **70,634,993 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4131 |
| 2 | SkyWest Airlines | 3706 |
| 3 | IndiGo | 2020 |
| 4 | EJA | 1883 |
| 5 | American Airlines | 1604 |
| 6 | Southwest Airlines | 1501 |
| 7 | ENY | 1231 |
| 8 | Lufthansa | 1173 |
| 9 | Delta Air Lines | 1166 |
| 10 | Vueling | 934 |
| 11 | LATAM Airlines | 882 |
| 12 | WIF | 873 |
| 13 | AXM | 858 |
| 14 | AZU | 802 |
| 15 | LXJ | 750 |
| 16 | Swiss International | 731 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 695 |
| 19 | QLK | 674 |
| 20 | easyJet | 649 |
| 21 | EJU | 629 |
| 22 | Cathay Pacific | 593 |
| 23 | AEE | 588 |
| 24 | Air France | 579 |
| 25 | VIV | 578 |
| 26 | United Airlines | 557 |
| 27 | CXK | 533 |
| 28 | MXY | 530 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 494 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83002 |
| 2 | 🇪🇸 ES | 6928 |
| 3 | 🇮🇳 IN | 6372 |
| 4 | 🇦🇺 AU | 5992 |
| 5 | 🇧🇷 BR | 5442 |
| 6 | 🇩🇪 DE | 5422 |
| 7 | 🇮🇹 IT | 5331 |
| 8 | 🇨🇦 CA | 5090 |
| 9 | 🇯🇵 JP | 4637 |
| 10 | 🇬🇧 GB | 4242 |
| 11 | 🇫🇷 FR | 3997 |
| 12 | 🇨🇴 CO | 3459 |
| 13 | 🇲🇽 MX | 3030 |
| 14 | 🇬🇷 GR | 2854 |
| 15 | 🇳🇴 NO | 2772 |
| 16 | 🇨🇭 CH | 2584 |
| 17 | 🇲🇾 MY | 2185 |
| 18 | 🇹🇷 TR | 1890 |
| 19 | 🇿🇦 ZA | 1751 |
| 20 | 🇳🇿 NZ | 1667 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇰🇷 KR | 1601 |
| 23 | 🇵🇱 PL | 1599 |
| 24 | 🇬🇹 GT | 1482 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1117 |
| 27 | 🇲🇴 MO | 1051 |
| 28 | 🇳🇱 NL | 999 |
| 29 | 🇲🇪 ME | 957 |
| 30 | 🇭🇷 HR | 885 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2163 |
| 2 | Denver International Airport |  | US | 1694 |
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1384 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1290 |
| 6 | Harry Reid International Airport |  | US | 1269 |
| 7 | Guaymaral Airport |  | CO | 1248 |
| 8 | Frankfurt am Main International Airport |  | DE | 1178 |
| 9 | Zurich Airport |  | CH | 1147 |
| 10 | La Aurora Airport |  | GT | 1139 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1071 |
| 12 | El Dorado International Airport |  | CO | 1064 |
| 13 | Macau International Airport |  | MO | 1051 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1006 |
| 15 | Chicago O'Hare International Airport |  | US | 994 |
| 16 | Madrid Barajas International Airport |  | ES | 873 |
| 17 | Kuala Lumpur International Airport |  | MY | 863 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 856 |
| 19 | Salt Lake City International Airport |  | US | 842 |
| 20 | Capua Airport |  | IT | 823 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 770 |
| 23 | Charles de Gaulle International Airport |  | FR | 768 |
| 24 | Malpensa International Airport |  | IT | 765 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 754 |
| 27 | Tenerife Norte Airport |  | ES | 691 |
| 28 | Daniel K Inouye International Airport |  | US | 690 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 660 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 654 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 649 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 633 |
| 34 | Amsterdam Airport Schiphol |  | NL | 616 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 583 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | Seattle-Tacoma International Airport |  | US | 565 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 516 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 267 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 254 | 14m | 114 km | 498.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 148 | 27m | 215 km | 548.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 130 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 128 | 18m | 144 km | 318.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5447L |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-05-31 17:20 UTC | 2026-05-31 17:43 UTC | 23m |
| N119PT |  | Strietelmeier Flying Field (91IN) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-31 17:07 UTC | 2026-05-31 17:38 UTC | 31m |
| N67487 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-31 17:07 UTC | 2026-05-31 17:36 UTC | 29m |
| N690MF |  | Garrett Ranch Airport (77XS) | Garrett Ranch Airport (77XS) | 2026-05-31 17:24 UTC | 2026-05-31 17:36 UTC | 11m |
| N4841Y |  | Ambrosich Field (4CO7) | Kelly Air Park (CO15) | 2026-05-31 17:13 UTC | 2026-05-31 17:30 UTC | 17m |
| ERU23 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 00AZ (00AZ) | 2026-05-31 17:13 UTC | 2026-05-31 17:27 UTC | 14m |
| N421ER |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-05-31 16:31 UTC | 2026-05-31 17:26 UTC | 55m |
| N7718A |  | Ogden-Hinckley Airport (KOGD) | Logan-Cache Airport (KLGU) | 2026-05-31 17:06 UTC | 2026-05-31 17:24 UTC | 17m |
| N215VB |  | Skypark Airport (KBTF) | Logan-Cache Airport (KLGU) | 2026-05-31 16:48 UTC | 2026-05-31 17:23 UTC | 35m |
| 2JSEG |  | Santa Fe Regional Airport (KSAF) | Central Colorado Regional Airport (KAEJ) | 2026-05-31 16:40 UTC | 2026-05-31 17:23 UTC | 43m |
| JBU1380 | JetBlue | Fort Lauderdale/Hollywood International Airport (KFLL) | La Aurora Airport (MGGT) | 2026-05-31 15:05 UTC | 2026-05-31 17:23 UTC | 2h 17m |
| N894SA |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-31 15:40 UTC | 2026-05-31 17:23 UTC | 1h 43m |
| N47354 |  | Sanctuary Ranch Airport (7TS4) | Vance Field (TE76) | 2026-05-31 16:51 UTC | 2026-05-31 17:22 UTC | 30m |
| N201LC |  | San Gabriel Valley Airport (KEMT) | Big Bear City Airport (KL35) | 2026-05-31 16:53 UTC | 2026-05-31 17:21 UTC | 28m |
| N583M |  | Lago Vista Tx/Rusty Allen Airport (KRYW) | Taylor Municipal Airport (KT74) | 2026-05-31 17:04 UTC | 2026-05-31 17:21 UTC | 16m |
| N711EM |  | J P Reilly Airport (59PA) | Lancaster Airport (KLNS) | 2026-05-31 16:48 UTC | 2026-05-31 17:18 UTC | 30m |
| N1998C |  | Provo Municipal Airport (KPVU) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-31 15:47 UTC | 2026-05-31 17:14 UTC | 1h 27m |
| 345 |  | Be'er Sheva (Teyman) Airport (LLBS) | Be'er Sheva (Teyman) Airport (LLBS) | 2026-05-31 17:09 UTC | 2026-05-31 17:12 UTC | 2m |
| N7210L |  | Sacramento Mather Airport (KMHR) | Truckee-Tahoe Airport (KTRK) | 2026-05-31 16:42 UTC | 2026-05-31 17:08 UTC | 26m |
| N4174B |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-31 16:53 UTC | 2026-05-31 17:08 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
