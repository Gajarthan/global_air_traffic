# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_19:40:30_UTC-green)

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

**Latest saved flight:** 2026-05-20 19:40:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-20 19:40:30 UTC

- **89,369** saved flights
- **31,885** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,369** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,106,028.9 tonnes** estimated CO2 emissions
- **64,117,619 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3838 |
| 2 | SkyWest Airlines | 3317 |
| 3 | IndiGo | 1887 |
| 4 | EJA | 1689 |
| 5 | American Airlines | 1365 |
| 6 | Southwest Airlines | 1296 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1100 |
| 9 | Delta Air Lines | 978 |
| 10 | Vueling | 853 |
| 11 | LATAM Airlines | 804 |
| 12 | AXM | 790 |
| 13 | WIF | 776 |
| 14 | AZU | 710 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 671 |
| 17 | LXJ | 662 |
| 18 | Alaska Airlines | 634 |
| 19 | QLK | 632 |
| 20 | easyJet | 589 |
| 21 | EJU | 576 |
| 22 | Cathay Pacific | 574 |
| 23 | AEE | 552 |
| 24 | VIV | 535 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 468 |
| 28 | AXB | 459 |
| 29 | MXY | 455 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73498 |
| 2 | 🇪🇸 ES | 6346 |
| 3 | 🇮🇳 IN | 5916 |
| 4 | 🇦🇺 AU | 5553 |
| 5 | 🇩🇪 DE | 4955 |
| 6 | 🇮🇹 IT | 4954 |
| 7 | 🇧🇷 BR | 4907 |
| 8 | 🇨🇦 CA | 4477 |
| 9 | 🇯🇵 JP | 4367 |
| 10 | 🇬🇧 GB | 3818 |
| 11 | 🇫🇷 FR | 3591 |
| 12 | 🇨🇴 CO | 3069 |
| 13 | 🇲🇽 MX | 2772 |
| 14 | 🇬🇷 GR | 2582 |
| 15 | 🇳🇴 NO | 2487 |
| 16 | 🇨🇭 CH | 2355 |
| 17 | 🇲🇾 MY | 1984 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1627 |
| 20 | 🇳🇿 NZ | 1536 |
| 21 | 🇹🇭 TH | 1523 |
| 22 | 🇵🇱 PL | 1480 |
| 23 | 🇰🇷 KR | 1384 |
| 24 | 🇵🇭 PH | 1368 |
| 25 | 🇬🇹 GT | 1337 |
| 26 | 🇲🇦 MA | 1031 |
| 27 | 🇲🇴 MO | 1031 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 906 |
| 30 | 🇭🇷 HR | 808 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1951 |
| 2 | Denver International Airport |  | US | 1499 |
| 3 | Tokyo International Airport |  | JP | 1456 |
| 4 | Indira Gandhi International Airport |  | IN | 1279 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1216 |
| 6 | Harry Reid International Airport |  | US | 1138 |
| 7 | Frankfurt am Main International Airport |  | DE | 1125 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1048 |
| 10 | Macau International Airport |  | MO | 1031 |
| 11 | La Aurora Airport |  | GT | 1017 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 987 |
| 13 | El Dorado International Airport |  | CO | 975 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 910 |
| 15 | Chicago O'Hare International Airport |  | US | 863 |
| 16 | Madrid Barajas International Airport |  | ES | 813 |
| 17 | Kuala Lumpur International Airport |  | MY | 786 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 767 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 750 |
| 21 | Malpensa International Airport |  | IT | 727 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 723 |
| 23 | Bengaluru International Airport |  | IN | 712 |
| 24 | Charles de Gaulle International Airport |  | FR | 697 |
| 25 | Congonhas Airport |  | BR | 688 |
| 26 | Charlotte/Douglas International Airport |  | US | 686 |
| 27 | Daniel K Inouye International Airport |  | US | 655 |
| 28 | Tenerife Norte Airport |  | ES | 653 |
| 29 | Ninoy Aquino International Airport |  | PH | 628 |
| 30 | Barcelona International Airport |  | ES | 602 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 599 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 588 |
| 34 | Vitoria/Foronda Airport |  | ES | 568 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 565 |
| 37 | Amsterdam Airport Schiphol |  | NL | 556 |
| 38 | Don Mueang International Airport |  | TH | 555 |
| 39 | Calgary International Airport |  | CA | 531 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 333 | 21m | 244 km | 1,402.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 244 | 24m | 225 km | 946.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 233 | 14m | 114 km | 457.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 228 | 28m | 304 km | 1,195.2 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 228 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 204 | 1h 10m | 770 km | 2,710.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 185 | 26m | 275 km | 876.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 129 | 23m | 55 km | 122.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 126 | 14m | 154 km | 333.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GASTN61 | GAS | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-05-20 19:02 UTC | 2026-05-20 19:40 UTC | 38m |
| WIRE31 | WIR | 75OK (75OK) | Sopwith Ldg Airport (OK56) | 2026-05-20 19:04 UTC | 2026-05-20 19:31 UTC | 26m |
| CREEP31 | CRE | Cottonwood Airport (OK66) | Kegelman Af Aux Field (KCKA) | 2026-05-20 19:15 UTC | 2026-05-20 19:31 UTC | 16m |
| SHINR81 | SHI | Good Life Ranch Airport (17OK) | Good Life Ranch Airport (17OK) | 2026-05-20 18:54 UTC | 2026-05-20 19:30 UTC | 36m |
| N36AE |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-05-20 19:15 UTC | 2026-05-20 19:23 UTC | 8m |
| GFY164 | GFY | Scappoose Airport (KSPB) | 52OR (52OR) | 2026-05-20 18:26 UTC | 2026-05-20 19:19 UTC | 52m |
| N234ZG |  | K55J (K55J) | K55J (K55J) | 2026-05-20 19:16 UTC | 2026-05-20 19:17 UTC | 1m |
| N512UT |  | Austin Executive Airport (KEDC) | Austin Executive Airport (KEDC) | 2026-05-20 18:41 UTC | 2026-05-20 19:15 UTC | 34m |
| N6782H |  | Galt Field (K10C) | Galt Field (K10C) | 2026-05-20 18:26 UTC | 2026-05-20 19:15 UTC | 49m |
| CGMPQ | CGM | CFB Greenwood (CYZX) | Montréal / St-Hubert Airport (CYHU) | 2026-05-20 15:29 UTC | 2026-05-20 19:14 UTC | 3h 45m |
| JIA5490 | JIA | Dallas-Fort Worth International Airport (KDFW) | 9LS9 (9LS9) | 2026-05-20 18:27 UTC | 2026-05-20 19:12 UTC | 44m |
| N7017R |  | Auburn University Regional Airport (KAUO) | Lanett Regional Airport (K7A3) | 2026-05-20 18:44 UTC | 2026-05-20 19:10 UTC | 25m |
| N24BQ |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-20 18:58 UTC | 2026-05-20 19:09 UTC | 11m |
| N9968F |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-20 18:55 UTC | 2026-05-20 19:07 UTC | 11m |
| N5QD |  | 0PA0 (0PA0) | Gunden Airport (PS54) | 2026-05-20 19:06 UTC | 2026-05-20 19:07 UTC | 1m |
| VEGA21 | VEG | Flying E Ranch Airport (OK16) | Flying E Ranch Airport (OK16) | 2026-05-20 18:32 UTC | 2026-05-20 19:05 UTC | 33m |
| TGFYL | TGF | La Aurora Airport (MGGT) | El Palmer Airport (MSSA) | 2026-05-20 18:45 UTC | 2026-05-20 19:03 UTC | 18m |
| BNOB | BNO | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-05-20 18:45 UTC | 2026-05-20 19:02 UTC | 16m |
| N669FG |  | Sky Manor Airport (KN40) | Sky Manor Airport (KN40) | 2026-05-20 18:59 UTC | 2026-05-20 19:00 UTC | 1m |
| N35731 |  | Moore County Airport (KSOP) | Moore County Airport (KSOP) | 2026-05-20 18:31 UTC | 2026-05-20 18:58 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
