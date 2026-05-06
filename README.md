# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_08:54:17_UTC-green)

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

**Latest saved flight:** 2026-05-06 08:54:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 08:54:17 UTC

- **70,335** saved flights
- **26,208** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,335** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **867,612.5 tonnes** estimated CO2 emissions
- **50,296,375 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3024 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1609 |
| 4 | EJA | 1282 |
| 5 | American Airlines | 1096 |
| 6 | Southwest Airlines | 1018 |
| 7 | Lufthansa | 904 |
| 8 | ENY | 876 |
| 9 | Vueling | 692 |
| 10 | AXM | 678 |
| 11 | LATAM Airlines | 656 |
| 12 | WIF | 599 |
| 13 | Delta Air Lines | 594 |
| 14 | All Nippon Airways | 590 |
| 15 | AZU | 570 |
| 16 | QLK | 547 |
| 17 | Swiss International | 543 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 494 |
| 20 | easyJet | 472 |
| 21 | EJU | 454 |
| 22 | AEE | 453 |
| 23 | VIV | 441 |
| 24 | Cathay Pacific | 431 |
| 25 | Japan Airlines | 419 |
| 26 | Air France | 413 |
| 27 | AXB | 392 |
| 28 | AIQ | 358 |
| 29 | CXK | 349 |
| 30 | GLO | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55894 |
| 2 | 🇪🇸 ES | 5133 |
| 3 | 🇮🇳 IN | 5064 |
| 4 | 🇦🇺 AU | 4704 |
| 5 | 🇧🇷 BR | 3957 |
| 6 | 🇩🇪 DE | 3917 |
| 7 | 🇮🇹 IT | 3847 |
| 8 | 🇯🇵 JP | 3764 |
| 9 | 🇨🇦 CA | 3471 |
| 10 | 🇬🇧 GB | 3050 |
| 11 | 🇫🇷 FR | 2780 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2228 |
| 14 | 🇬🇷 GR | 2095 |
| 15 | 🇨🇭 CH | 1929 |
| 16 | 🇳🇴 NO | 1920 |
| 17 | 🇲🇾 MY | 1687 |
| 18 | 🇿🇦 ZA | 1394 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1282 |
| 21 | 🇹🇷 TR | 1265 |
| 22 | 🇵🇭 PH | 1168 |
| 23 | 🇵🇱 PL | 1154 |
| 24 | 🇬🇹 GT | 1129 |
| 25 | 🇰🇷 KR | 1127 |
| 26 | 🇲🇦 MA | 845 |
| 27 | 🇲🇴 MO | 815 |
| 28 | 🇲🇪 ME | 757 |
| 29 | 🇳🇱 NL | 731 |
| 30 | 🇮🇩 ID | 596 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1570 |
| 2 | Tokyo International Airport |  | JP | 1269 |
| 3 | Denver International Airport |  | US | 1167 |
| 4 | Indira Gandhi International Airport |  | IN | 1064 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1025 |
| 6 | Frankfurt am Main International Airport |  | DE | 902 |
| 7 | Harry Reid International Airport |  | US | 879 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 839 |
| 11 | Zurich Airport |  | CH | 832 |
| 12 | Macau International Airport |  | MO | 815 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 703 |
| 14 | Kuala Lumpur International Airport |  | MY | 676 |
| 15 | Chicago O'Hare International Airport |  | US | 675 |
| 16 | Madrid Barajas International Airport |  | ES | 671 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 19 | Malpensa International Airport |  | IT | 610 |
| 20 | Bengaluru International Airport |  | IN | 610 |
| 21 | Salt Lake City International Airport |  | US | 569 |
| 22 | Congonhas Airport |  | BR | 562 |
| 23 | Charlotte/Douglas International Airport |  | US | 555 |
| 24 | Charles de Gaulle International Airport |  | FR | 552 |
| 25 | Capua Airport |  | IT | 547 |
| 26 | Tenerife Norte Airport |  | ES | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 530 |
| 28 | Daniel K Inouye International Airport |  | US | 516 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 513 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 495 |
| 31 | Barcelona International Airport |  | ES | 488 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 477 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 466 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 443 |
| 37 | O. R. Tambo International Airport |  | ZA | 439 |
| 38 | Amsterdam Airport Schiphol |  | NL | 433 |
| 39 | Reno/Tahoe International Airport |  | US | 416 |
| 40 | Calgary International Airport |  | CA | 416 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 244 | 21m | 244 km | 1,027.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 199 | 28m | 304 km | 1,043.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 196 | 1h 27m | 910 km | 3,075.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 175 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 173 | 20m | 165 km | 492.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 158 | 26m | 275 km | 748.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 106 | 20m | 147 km | 268.2 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 100 | 14m | 154 km | 265.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 97 | 1h 2m | 695 km | 1,162.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CLX4162 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-05 21:46 UTC | 2026-05-06 08:54 UTC | 11h 7m |
| SVI1101 | SVI | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-05-05 11:47 UTC | 2026-05-06 08:44 UTC | 20h 56m |
| LPR41 | LPR | Warsaw Chopin Airport (EPWA) | Copernicus Wrocław Airport (EPWR) | 2026-05-06 08:07 UTC | 2026-05-06 08:41 UTC | 34m |
| NSZ3LZ | NSZ | Alicante International Airport (LEAL) | Stockholm-Arlanda Airport (ESSA) | 2026-05-06 04:58 UTC | 2026-05-06 08:36 UTC | 3h 37m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-06 01:16 UTC | 2026-05-06 08:34 UTC | 7h 18m |
| BKBD06 | BKB | Khok Kathiam Airport (VTBL) | Khok Kathiam Airport (VTBL) | 2026-05-06 08:01 UTC | 2026-05-06 08:23 UTC | 22m |
| ARK401A | ARK | Sabadell Airport (LELL) | Girona Airport (LEGE) | 2026-05-06 07:58 UTC | 2026-05-06 08:20 UTC | 21m |
| RYR8SL | Ryanair | Grazzanise Airport (LIRM) | Bergamo / Orio Al Serio Airport (LIME) | 2026-05-06 07:16 UTC | 2026-05-06 08:14 UTC | 58m |
| RYR74SB | Ryanair | Kaunas International Airport (EYKA) | Telsiai Airport (EYTL) | 2026-05-06 07:55 UTC | 2026-05-06 08:11 UTC | 16m |
| RYR29FF | Ryanair | Frankfurt-Hahn Airport (EDFH) | Otocac Airport (LDRO) | 2026-05-06 06:56 UTC | 2026-05-06 08:09 UTC | 1h 12m |
| 00000223 |  | Moi Air Base (HKRE) | Nairobi Wilson Airport (HKNW) | 2026-05-06 08:03 UTC | 2026-05-06 08:08 UTC | 4m |
| RYR22EY | Ryanair | Faro Airport (LPFR) | London Luton Airport (EGGW) | 2026-05-06 05:43 UTC | 2026-05-06 08:07 UTC | 2h 24m |
| VOE3269 | VOE | Sevilla Airport (LEZL) | Bilbao Airport (LEBB) | 2026-05-06 07:08 UTC | 2026-05-06 08:07 UTC | 58m |
| VOZ1224 | Virgin Australia | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 2026-05-06 06:47 UTC | 2026-05-06 08:01 UTC | 1h 13m |
| DLH9MT | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-05-06 07:25 UTC | 2026-05-06 07:58 UTC | 32m |
| AUA733 | Austrian Airlines | Vienna International Airport (LOWW) | Niksic Airport (LYNK) | 2026-05-06 07:09 UTC | 2026-05-06 07:57 UTC | 48m |
| RYR93QL | Ryanair | Brussels South Charleroi Airport (EBCI) | Ampuriabrava Airport (LEAP) | 2026-05-06 06:38 UTC | 2026-05-06 07:57 UTC | 1h 19m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-05-06 07:30 UTC | 2026-05-06 07:56 UTC | 26m |
| AFL1946 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-05-05 23:15 UTC | 2026-05-06 07:54 UTC | 8h 38m |
| JAL3114 | Japan Airlines | New Chitose Airport (RJCC) | Chubu Centrair International Airport (RJGG) | 2026-05-06 06:26 UTC | 2026-05-06 07:51 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
