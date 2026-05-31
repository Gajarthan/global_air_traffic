# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_22:27:14_UTC-green)

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

**Latest saved flight:** 2026-05-31 22:27:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 22:27:14 UTC

- **99,918** saved flights
- **35,523** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **99,918** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,224,281.2 tonnes** estimated CO2 emissions
- **70,972,826 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4147 |
| 2 | SkyWest Airlines | 3738 |
| 3 | IndiGo | 2021 |
| 4 | EJA | 1905 |
| 5 | American Airlines | 1620 |
| 6 | Southwest Airlines | 1509 |
| 7 | ENY | 1241 |
| 8 | Lufthansa | 1175 |
| 9 | Delta Air Lines | 1172 |
| 10 | Vueling | 938 |
| 11 | LATAM Airlines | 887 |
| 12 | WIF | 876 |
| 13 | AXM | 858 |
| 14 | AZU | 805 |
| 15 | LXJ | 758 |
| 16 | Swiss International | 731 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 697 |
| 19 | QLK | 674 |
| 20 | easyJet | 654 |
| 21 | EJU | 630 |
| 22 | Cathay Pacific | 596 |
| 23 | AEE | 588 |
| 24 | Air France | 580 |
| 25 | VIV | 578 |
| 26 | United Airlines | 560 |
| 27 | CXK | 540 |
| 28 | MXY | 534 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 495 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83614 |
| 2 | 🇪🇸 ES | 6955 |
| 3 | 🇮🇳 IN | 6379 |
| 4 | 🇦🇺 AU | 5998 |
| 5 | 🇧🇷 BR | 5468 |
| 6 | 🇩🇪 DE | 5434 |
| 7 | 🇮🇹 IT | 5344 |
| 8 | 🇨🇦 CA | 5123 |
| 9 | 🇯🇵 JP | 4637 |
| 10 | 🇬🇧 GB | 4261 |
| 11 | 🇫🇷 FR | 4007 |
| 12 | 🇨🇴 CO | 3479 |
| 13 | 🇲🇽 MX | 3036 |
| 14 | 🇬🇷 GR | 2864 |
| 15 | 🇳🇴 NO | 2777 |
| 16 | 🇨🇭 CH | 2586 |
| 17 | 🇲🇾 MY | 2185 |
| 18 | 🇹🇷 TR | 1901 |
| 19 | 🇿🇦 ZA | 1751 |
| 20 | 🇳🇿 NZ | 1669 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇵🇱 PL | 1605 |
| 23 | 🇰🇷 KR | 1601 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1123 |
| 27 | 🇲🇴 MO | 1057 |
| 28 | 🇳🇱 NL | 1002 |
| 29 | 🇲🇪 ME | 959 |
| 30 | 🇭🇷 HR | 888 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2182 |
| 2 | Denver International Airport |  | US | 1712 |
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1388 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1292 |
| 6 | Harry Reid International Airport |  | US | 1275 |
| 7 | Guaymaral Airport |  | CO | 1255 |
| 8 | Frankfurt am Main International Airport |  | DE | 1179 |
| 9 | Zurich Airport |  | CH | 1149 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1077 |
| 12 | El Dorado International Airport |  | CO | 1069 |
| 13 | Macau International Airport |  | MO | 1057 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1015 |
| 15 | Chicago O'Hare International Airport |  | US | 1000 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 863 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 861 |
| 19 | Salt Lake City International Airport |  | US | 846 |
| 20 | Capua Airport |  | IT | 827 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 776 |
| 23 | Charles de Gaulle International Airport |  | FR | 769 |
| 24 | Malpensa International Airport |  | IT | 765 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 760 |
| 27 | Daniel K Inouye International Airport |  | US | 692 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 662 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 654 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 651 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 637 |
| 34 | Amsterdam Airport Schiphol |  | NL | 618 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 585 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |
| 40 | Seattle-Tacoma International Airport |  | US | 571 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 517 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 362 | 21m | 244 km | 1,524.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 255 | 14m | 114 km | 500.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 131 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 129 | 18m | 144 km | 320.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 126 | 1h 39m | 1,156 km | 2,513.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-31 21:38 UTC | 2026-05-31 22:27 UTC | 48m |
| N729EL |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-05-31 21:51 UTC | 2026-05-31 22:25 UTC | 34m |
| N41TE |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-05-31 21:48 UTC | 2026-05-31 22:23 UTC | 35m |
| ES800 |  | Chico Regional Airport (KCIC) | Mc Clellan Airfield (KMCC) | 2026-05-31 21:40 UTC | 2026-05-31 22:21 UTC | 40m |
| AIZ991 | AIZ | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-31 21:58 UTC | 2026-05-31 22:20 UTC | 22m |
| UAE118 | Emirates | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-05-31 21:00 UTC | 2026-05-31 22:18 UTC | 1h 18m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-31 17:46 UTC | 2026-05-31 22:18 UTC | 4h 31m |
| N34EF |  | Princeton Airport (K39N) | Lancaster Airport (KLNS) | 2026-05-31 21:40 UTC | 2026-05-31 22:18 UTC | 37m |
| AUA71RD | Austrian Airlines | Vienna International Airport (LOWW) | Visoko Sport Airfield (LQVI) | 2026-05-31 21:42 UTC | 2026-05-31 22:16 UTC | 34m |
| N75274 |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-05-31 21:36 UTC | 2026-05-31 22:16 UTC | 39m |
| CLX7956 | CLX | Gia Lam Air Base (VVGL) | Macau International Airport (VMMC) | 2026-05-31 21:14 UTC | 2026-05-31 22:15 UTC | 1h 0m |
| N259DC |  | Chico Regional Airport (KCIC) | Napa County Airport (KAPC) | 2026-05-31 21:44 UTC | 2026-05-31 22:06 UTC | 22m |
| UAL1411 | United Airlines | Portland International Airport (KPDX) | Denver International Airport (KDEN) | 2026-05-31 19:56 UTC | 2026-05-31 22:05 UTC | 2h 9m |
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-05-31 21:48 UTC | 2026-05-31 21:58 UTC | 9m |
| N34HF |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-05-31 21:25 UTC | 2026-05-31 21:56 UTC | 30m |
| N628SR |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | San Carlos Airport (KSQL) | 2026-05-31 20:38 UTC | 2026-05-31 21:56 UTC | 1h 18m |
| PGT398 | PGT | Sabiha Gokcen International Airport (LTFJ) | Pskov Airport (ULOO) | 2026-05-31 19:17 UTC | 2026-05-31 21:55 UTC | 2h 37m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-31 17:33 UTC | 2026-05-31 21:55 UTC | 4h 21m |
| N726AP |  | Mount Airy/Surry County Airport (KMWK) | Mount Airy/Surry County Airport (KMWK) | 2026-05-31 21:38 UTC | 2026-05-31 21:55 UTC | 16m |
| GEC8290 | GEC | Frankfurt am Main International Airport (EDDF) | HE12 (HE12) | 2026-05-31 18:35 UTC | 2026-05-31 21:50 UTC | 3h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
