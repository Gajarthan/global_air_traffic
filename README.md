# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_20:38:37_UTC-green)

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

**Latest saved flight:** 2026-05-24 20:38:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 20:38:37 UTC

- **94,262** saved flights
- **33,275** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,262** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,159,872.3 tonnes** estimated CO2 emissions
- **67,238,974 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3984 |
| 2 | SkyWest Airlines | 3504 |
| 3 | IndiGo | 1953 |
| 4 | EJA | 1780 |
| 5 | American Airlines | 1436 |
| 6 | Southwest Airlines | 1369 |
| 7 | ENY | 1169 |
| 8 | Lufthansa | 1136 |
| 9 | Delta Air Lines | 1033 |
| 10 | Vueling | 899 |
| 11 | LATAM Airlines | 848 |
| 12 | AXM | 835 |
| 13 | WIF | 822 |
| 14 | AZU | 751 |
| 15 | LXJ | 711 |
| 16 | Swiss International | 708 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 655 |
| 19 | QLK | 650 |
| 20 | easyJet | 618 |
| 21 | EJU | 607 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 568 |
| 24 | VIV | 559 |
| 25 | Air France | 557 |
| 26 | CXK | 502 |
| 27 | MXY | 499 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77884 |
| 2 | 🇪🇸 ES | 6617 |
| 3 | 🇮🇳 IN | 6169 |
| 4 | 🇦🇺 AU | 5748 |
| 5 | 🇩🇪 DE | 5188 |
| 6 | 🇧🇷 BR | 5174 |
| 7 | 🇮🇹 IT | 5120 |
| 8 | 🇨🇦 CA | 4775 |
| 9 | 🇯🇵 JP | 4524 |
| 10 | 🇬🇧 GB | 4026 |
| 11 | 🇫🇷 FR | 3813 |
| 12 | 🇨🇴 CO | 3264 |
| 13 | 🇲🇽 MX | 2899 |
| 14 | 🇬🇷 GR | 2705 |
| 15 | 🇳🇴 NO | 2627 |
| 16 | 🇨🇭 CH | 2480 |
| 17 | 🇲🇾 MY | 2111 |
| 18 | 🇹🇷 TR | 1742 |
| 19 | 🇿🇦 ZA | 1701 |
| 20 | 🇹🇭 TH | 1595 |
| 21 | 🇳🇿 NZ | 1594 |
| 22 | 🇵🇱 PL | 1549 |
| 23 | 🇰🇷 KR | 1515 |
| 24 | 🇵🇭 PH | 1420 |
| 25 | 🇬🇹 GT | 1414 |
| 26 | 🇲🇦 MA | 1081 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 950 |
| 29 | 🇲🇪 ME | 938 |
| 30 | 🇭🇷 HR | 860 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2045 |
| 2 | Denver International Airport |  | US | 1593 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1343 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1247 |
| 6 | Harry Reid International Airport |  | US | 1208 |
| 7 | Frankfurt am Main International Airport |  | DE | 1152 |
| 8 | Guaymaral Airport |  | CO | 1138 |
| 9 | Zurich Airport |  | CH | 1104 |
| 10 | La Aurora Airport |  | GT | 1081 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1026 |
| 13 | El Dorado International Airport |  | CO | 1026 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 943 |
| 15 | Chicago O'Hare International Airport |  | US | 906 |
| 16 | Madrid Barajas International Airport |  | ES | 841 |
| 17 | Kuala Lumpur International Airport |  | MY | 838 |
| 18 | Salt Lake City International Airport |  | US | 797 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 796 |
| 20 | Capua Airport |  | IT | 785 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 747 |
| 22 | Malpensa International Airport |  | IT | 743 |
| 23 | Charles de Gaulle International Airport |  | FR | 739 |
| 24 | Bengaluru International Airport |  | IN | 739 |
| 25 | Charlotte/Douglas International Airport |  | US | 718 |
| 26 | Congonhas Airport |  | BR | 717 |
| 27 | Daniel K Inouye International Airport |  | US | 676 |
| 28 | Tenerife Norte Airport |  | ES | 672 |
| 29 | Ninoy Aquino International Airport |  | PH | 649 |
| 30 | Barcelona International Airport |  | ES | 634 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 633 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 614 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 605 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 600 |
| 35 | Vitoria/Foronda Airport |  | ES | 587 |
| 36 | Amsterdam Airport Schiphol |  | NL | 586 |
| 37 | Don Mueang International Airport |  | TH | 584 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 560 |
| 40 | O. R. Tambo International Airport |  | ZA | 539 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 467 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 347 | 21m | 244 km | 1,461.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 140 | 27m | 215 km | 518.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 135 | 27m | 152 km | 352.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 122 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 1m | 695 km | 1,450.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 121 | 18m | 144 km | 301.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 117 | 1h 40m | 1,156 km | 2,334.1 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 52m | 1,304 km | 2,542.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-05-24 19:16 UTC | 2026-05-24 20:38 UTC | 1h 22m |
| N407CC |  | Buchanan Field (KCCR) | Byron Airport (KC83) | 2026-05-24 20:07 UTC | 2026-05-24 20:29 UTC | 22m |
| XAPBT | XAP | Del Norte International Airport (MMAN) | Rochester International Airport (KRST) | 2026-05-24 17:44 UTC | 2026-05-24 20:17 UTC | 2h 33m |
| N702KA |  | Mirth Airport (WA22) | Boeing Field/King County International Airport (KBFI) | 2026-05-24 20:02 UTC | 2026-05-24 20:17 UTC | 14m |
| N682AC |  | TE77 (TE77) | Bb Airpark (TE88) | 2026-05-24 20:00 UTC | 2026-05-24 20:06 UTC | 5m |
| N826PA |  | Big Bear City Airport (KL35) | OMU9 (OMU9) | 2026-05-24 15:45 UTC | 2026-05-24 20:05 UTC | 4h 19m |
| N1WG |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-05-24 19:43 UTC | 2026-05-24 19:58 UTC | 14m |
| DLX50 | DLX | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-05-24 19:12 UTC | 2026-05-24 19:58 UTC | 45m |
| N91BT |  | AZ67 (AZ67) | AZ67 (AZ67) | 2026-05-24 19:09 UTC | 2026-05-24 19:57 UTC | 48m |
| N510RM |  | Charleston Afb/International Airport (KCHS) | 8NC3 (8NC3) | 2026-05-24 19:21 UTC | 2026-05-24 19:57 UTC | 35m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-24 19:41 UTC | 2026-05-24 19:54 UTC | 13m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-24 19:09 UTC | 2026-05-24 19:53 UTC | 44m |
| LXJ447 | LXJ | Westchester County Airport (KHPN) | Montréal / St-Hubert Airport (CYHU) | 2026-05-24 18:51 UTC | 2026-05-24 19:52 UTC | 1h 0m |
|  |  | Vancouver International Airport (CYVR) | Port Alberni Airport (CBS8) | 2026-05-24 19:24 UTC | 2026-05-24 19:50 UTC | 25m |
| N320KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-24 19:09 UTC | 2026-05-24 19:50 UTC | 41m |
| RYR8AH | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Corte Airport (LFKT) | 2026-05-24 19:17 UTC | 2026-05-24 19:49 UTC | 32m |
| N127PA |  | 91CL (91CL) | Porter Ranch Airport (68CN) | 2026-05-24 19:22 UTC | 2026-05-24 19:48 UTC | 25m |
| XE1191 |  | Scottsdale Airport (KSDL) | Santa Monica Municipal Airport (KSMO) | 2026-05-24 18:27 UTC | 2026-05-24 19:47 UTC | 1h 20m |
| RYR135R | Ryanair | Eindhoven Airport (EHEH) | Fes Sefrou Airport (GMFU) | 2026-05-24 17:06 UTC | 2026-05-24 19:47 UTC | 2h 40m |
| N5370L |  | Pueblo Memorial Airport (KPUB) | Southeast Colorado Regional Airport (KLAA) | 2026-05-24 19:03 UTC | 2026-05-24 19:46 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
