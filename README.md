# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_16:54:27_UTC-green)

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

**Latest saved flight:** 2026-05-09 16:54:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 16:54:27 UTC

- **75,662** saved flights
- **27,841** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,662** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **933,339.2 tonnes** estimated CO2 emissions
- **54,106,620 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3237 |
| 2 | SkyWest Airlines | 2799 |
| 3 | IndiGo | 1696 |
| 4 | EJA | 1391 |
| 5 | American Airlines | 1172 |
| 6 | Southwest Airlines | 1100 |
| 7 | Lufthansa | 987 |
| 8 | ENY | 944 |
| 9 | Vueling | 730 |
| 10 | Delta Air Lines | 729 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 700 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 606 |
| 16 | QLK | 579 |
| 17 | Swiss International | 576 |
| 18 | LXJ | 555 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 499 |
| 21 | AEE | 488 |
| 22 | EJU | 484 |
| 23 | Cathay Pacific | 476 |
| 24 | VIV | 457 |
| 25 | Japan Airlines | 443 |
| 26 | Air France | 441 |
| 27 | AXB | 419 |
| 28 | CXK | 390 |
| 29 | AIQ | 377 |
| 30 | MXY | 366 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60886 |
| 2 | 🇪🇸 ES | 5421 |
| 3 | 🇮🇳 IN | 5315 |
| 4 | 🇦🇺 AU | 4954 |
| 5 | 🇩🇪 DE | 4270 |
| 6 | 🇧🇷 BR | 4236 |
| 7 | 🇮🇹 IT | 4137 |
| 8 | 🇯🇵 JP | 3959 |
| 9 | 🇨🇦 CA | 3770 |
| 10 | 🇬🇧 GB | 3251 |
| 11 | 🇫🇷 FR | 3004 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2337 |
| 14 | 🇬🇷 GR | 2233 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2062 |
| 17 | 🇲🇾 MY | 1772 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1366 |
| 20 | 🇹🇷 TR | 1360 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1269 |
| 23 | 🇵🇭 PH | 1216 |
| 24 | 🇬🇹 GT | 1195 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 892 |
| 27 | 🇲🇴 MO | 879 |
| 28 | 🇲🇪 ME | 804 |
| 29 | 🇳🇱 NL | 792 |
| 30 | 🇭🇷 HR | 641 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1669 |
| 2 | Tokyo International Airport |  | JP | 1329 |
| 3 | Denver International Airport |  | US | 1265 |
| 4 | Indira Gandhi International Airport |  | IN | 1116 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1096 |
| 6 | Frankfurt am Main International Airport |  | DE | 985 |
| 7 | Harry Reid International Airport |  | US | 936 |
| 8 | La Aurora Airport |  | GT | 896 |
| 9 | Zurich Airport |  | CH | 892 |
| 10 | Guaymaral Airport |  | CO | 890 |
| 11 | El Dorado International Airport |  | CO | 879 |
| 12 | Macau International Airport |  | MO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 756 |
| 14 | Chicago O'Hare International Airport |  | US | 735 |
| 15 | Kuala Lumpur International Airport |  | MY | 712 |
| 16 | Madrid Barajas International Airport |  | ES | 705 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 669 |
| 18 | Bengaluru International Airport |  | IN | 660 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 651 |
| 20 | Malpensa International Airport |  | IT | 649 |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 636 |
| 22 | Salt Lake City International Airport |  | US | 618 |
| 23 | Congonhas Airport |  | BR | 599 |
| 24 | Charlotte/Douglas International Airport |  | US | 593 |
| 25 | Charles de Gaulle International Airport |  | FR | 589 |
| 26 | Capua Airport |  | IT | 586 |
| 27 | Tenerife Norte Airport |  | ES | 563 |
| 28 | Daniel K Inouye International Airport |  | US | 551 |
| 29 | Ninoy Aquino International Airport |  | PH | 551 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 541 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 520 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 506 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 501 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Don Mueang International Airport |  | TH | 475 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 475 |
| 38 | Amsterdam Airport Schiphol |  | NL | 474 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 449 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 268 | 21m | 244 km | 1,128.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 194 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 113 | 20m | 147 km | 286.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 94 | 1h 19m | 961 km | 1,558.1 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 94 | 52m | 556 km | 901.1 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SKW4329 | SkyWest Airlines | Grand Forks Afb Airport (KRDR) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 16:03 UTC | 2026-05-09 16:54 UTC | 51m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-09 16:32 UTC | 2026-05-09 16:48 UTC | 16m |
| BCS673 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-05-08 22:43 UTC | 2026-05-09 16:48 UTC | 18h 4m |
| AEZ7817 | AEZ | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Olbia / Costa Smeralda Airport (LIEO) | 2026-05-09 16:17 UTC | 2026-05-09 16:47 UTC | 29m |
| DAL2090 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 14:31 UTC | 2026-05-09 16:45 UTC | 2h 14m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-09 16:28 UTC | 2026-05-09 16:43 UTC | 15m |
| N327TM |  | Henderson Executive Airport (KHND) | Lake Havasu City Airport (KHII) | 2026-05-09 15:44 UTC | 2026-05-09 16:43 UTC | 58m |
| N265PS |  | Orlando Executive Airport (KORL) | Leesburg International Airport (KLEE) | 2026-05-09 16:07 UTC | 2026-05-09 16:37 UTC | 29m |
| N851CB |  | Beech Factory Airport (KBEC) | El Dorado/Capt Jack Thomas Memorial Airport (KEQA) | 2026-05-09 16:07 UTC | 2026-05-09 16:37 UTC | 30m |
| N7651F |  | Aero Valley Airport (K52F) | Denton Enterprise Airport (KDTO) | 2026-05-09 15:26 UTC | 2026-05-09 16:35 UTC | 1h 8m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 16:08 UTC | 2026-05-09 16:32 UTC | 24m |
| N199SP |  | Chicago Executive Airport (KPWK) | Lake In The Hills Airport (K3CK) | 2026-05-09 16:13 UTC | 2026-05-09 16:32 UTC | 18m |
| CFMYB | CFM | Kitchener / Waterloo Airport (CYKF) | Billy Bishop Toronto City Airport (CYTZ) | 2026-05-09 16:13 UTC | 2026-05-09 16:32 UTC | 18m |
| EJA511 | EJA | Charleston Executive Airport (KJZI) | Rocky Mountain Metro Airport (KBJC) | 2026-05-09 12:32 UTC | 2026-05-09 16:31 UTC | 3h 58m |
| N3026W |  | MN85 (MN85) | Crystal Airport (KMIC) | 2026-05-09 16:09 UTC | 2026-05-09 16:30 UTC | 20m |
| DAL2178 | Delta Air Lines | San Francisco International Airport (KSFO) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 13:21 UTC | 2026-05-09 16:29 UTC | 3h 8m |
| N4377G |  | Madera Municipal Airport (KMAE) | Sacramento Executive Airport (KSAC) | 2026-05-09 15:49 UTC | 2026-05-09 16:29 UTC | 40m |
| DAL2847 | Delta Air Lines | Cleveland-Hopkins International Airport (KCLE) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 14:44 UTC | 2026-05-09 16:28 UTC | 1h 44m |
| DAL161 | Delta Air Lines | Amsterdam Airport Schiphol (EHAM) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 08:18 UTC | 2026-05-09 16:26 UTC | 8h 7m |
| N896PA |  | North Texas Regional/Perrin Field (KGYI) | Pierce Airport (TE10) | 2026-05-09 15:13 UTC | 2026-05-09 16:26 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
