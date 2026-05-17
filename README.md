# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_18:32:27_UTC-green)

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

**Latest saved flight:** 2026-05-17 18:32:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 18:32:27 UTC

- **86,564** saved flights
- **31,004** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,564** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,071,200.2 tonnes** estimated CO2 emissions
- **62,098,560 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3713 |
| 2 | SkyWest Airlines | 3194 |
| 3 | IndiGo | 1866 |
| 4 | EJA | 1625 |
| 5 | American Airlines | 1323 |
| 6 | Southwest Airlines | 1258 |
| 7 | Lufthansa | 1097 |
| 8 | ENY | 1071 |
| 9 | Delta Air Lines | 945 |
| 10 | Vueling | 825 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 780 |
| 13 | WIF | 739 |
| 14 | AZU | 677 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 666 |
| 17 | LXJ | 636 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 574 |
| 21 | EJU | 557 |
| 22 | Cathay Pacific | 550 |
| 23 | AEE | 542 |
| 24 | VIV | 517 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 457 |
| 28 | AXB | 455 |
| 29 | MXY | 433 |
| 30 | AIQ | 426 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70752 |
| 2 | 🇪🇸 ES | 6146 |
| 3 | 🇮🇳 IN | 5834 |
| 4 | 🇦🇺 AU | 5477 |
| 5 | 🇩🇪 DE | 4838 |
| 6 | 🇮🇹 IT | 4800 |
| 7 | 🇧🇷 BR | 4745 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4299 |
| 10 | 🇬🇧 GB | 3712 |
| 11 | 🇫🇷 FR | 3470 |
| 12 | 🇨🇴 CO | 2919 |
| 13 | 🇲🇽 MX | 2667 |
| 14 | 🇬🇷 GR | 2523 |
| 15 | 🇳🇴 NO | 2391 |
| 16 | 🇨🇭 CH | 2308 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1570 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1502 |
| 22 | 🇵🇱 PL | 1440 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1301 |
| 26 | 🇲🇦 MA | 1007 |
| 27 | 🇲🇴 MO | 1007 |
| 28 | 🇲🇪 ME | 902 |
| 29 | 🇳🇱 NL | 885 |
| 30 | 🇭🇷 HR | 780 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1888 |
| 2 | Denver International Airport |  | US | 1449 |
| 3 | Tokyo International Airport |  | JP | 1443 |
| 4 | Indira Gandhi International Airport |  | IN | 1252 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1202 |
| 6 | Frankfurt am Main International Airport |  | DE | 1110 |
| 7 | Harry Reid International Airport |  | US | 1096 |
| 8 | Zurich Airport |  | CH | 1037 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | Guaymaral Airport |  | CO | 989 |
| 11 | La Aurora Airport |  | GT | 988 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 956 |
| 13 | El Dorado International Airport |  | CO | 934 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 871 |
| 15 | Chicago O'Hare International Airport |  | US | 835 |
| 16 | Madrid Barajas International Airport |  | ES | 789 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 744 |
| 19 | Capua Airport |  | IT | 727 |
| 20 | Salt Lake City International Airport |  | US | 720 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 22 | Malpensa International Airport |  | IT | 712 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 677 |
| 25 | Charlotte/Douglas International Airport |  | US | 669 |
| 26 | Congonhas Airport |  | BR | 665 |
| 27 | Tenerife Norte Airport |  | ES | 638 |
| 28 | Daniel K Inouye International Airport |  | US | 632 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 587 |
| 32 | Barcelona International Airport |  | ES | 580 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 576 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 557 |
| 35 | Vitoria/Foronda Airport |  | ES | 554 |
| 36 | Don Mueang International Airport |  | TH | 544 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 543 |
| 38 | Amsterdam Airport Schiphol |  | NL | 540 |
| 39 | O. R. Tambo International Airport |  | ZA | 510 |
| 40 | Calgary International Airport |  | CA | 508 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 321 | 21m | 244 km | 1,351.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 222 | 14m | 114 km | 435.4 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 221 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 130 | 27m | 152 km | 339.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 110 | 18m | 144 km | 273.6 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 109 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 105 | 1h 52m | 1,304 km | 2,362.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2871T |  | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-05-17 18:20 UTC | 2026-05-17 18:32 UTC | 12m |
| N54947 |  | Maryland Airport (K2W5) | Maryland Airport (K2W5) | 2026-05-17 17:55 UTC | 2026-05-17 18:20 UTC | 25m |
| N53176 |  | John Wayne/Orange County Airport (KSNA) | John Wayne/Orange County Airport (KSNA) | 2026-05-17 17:56 UTC | 2026-05-17 18:18 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-17 17:55 UTC | 2026-05-17 18:14 UTC | 18m |
| AXB2391 | AXB | Juhu Aerodrome (VAJJ) | Sardar Vallabhbhai Patel International Airport (VAAH) | 2026-05-17 17:31 UTC | 2026-05-17 18:10 UTC | 39m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-17 17:54 UTC | 2026-05-17 18:09 UTC | 14m |
| GCSIX | GCS | Perth/Scone Airport (EGPT) | Beverley/Linley Hill Airport (EGNY) | 2026-05-17 16:40 UTC | 2026-05-17 18:07 UTC | 1h 27m |
| WLDLD28 | WLD | Centennial Airport (KAPA) | Boise City Airport (K17K) | 2026-05-17 17:05 UTC | 2026-05-17 18:06 UTC | 1h 0m |
| N1453U |  | Suffolk Executive Airport (KSFQ) | Currituck County Regional Airport (KONX) | 2026-05-17 17:41 UTC | 2026-05-17 18:03 UTC | 22m |
| PRO4860 | PRO | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Bathurst Airport (CZBF) | 2026-05-17 16:41 UTC | 2026-05-17 18:02 UTC | 1h 21m |
| QTR9C | Qatar Airways | Munich International Airport (EDDM) | Queen Alia International Airport (OJAI) | 2026-05-17 15:28 UTC | 2026-05-17 18:00 UTC | 2h 32m |
| CGWOK | CGW | Boundary Bay Airport (CZBB) | Fort Langley Airport (CBQ2) | 2026-05-17 17:28 UTC | 2026-05-17 18:00 UTC | 31m |
| N577LF |  | Barnwell Regional Airport (KBNL) | Daniel Field (KDNL) | 2026-05-17 17:31 UTC | 2026-05-17 17:59 UTC | 27m |
| QTR5G | Qatar Airways | Frankfurt am Main International Airport (EDDF) | Amman-Marka International Airport (OJAM) | 2026-05-17 15:10 UTC | 2026-05-17 17:59 UTC | 2h 49m |
| UAE6RM | Emirates | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-05-17 16:54 UTC | 2026-05-17 17:58 UTC | 1h 4m |
| N407DV |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-05-17 17:53 UTC | 2026-05-17 17:56 UTC | 3m |
| CPA3348 | Cathay Pacific | Soekarno-Hatta International Airport (WIII) | Zhuhai Airport (ZGSD) | 2026-05-17 09:46 UTC | 2026-05-17 17:53 UTC | 8h 6m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-17 17:11 UTC | 2026-05-17 17:51 UTC | 40m |
| SCA77 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-05-17 17:44 UTC | 2026-05-17 17:51 UTC | 7m |
| N1122T |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-05-17 17:39 UTC | 2026-05-17 17:49 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
