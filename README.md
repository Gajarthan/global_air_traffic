# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_01:26:31_UTC-green)

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

**Latest saved flight:** 2026-06-17 01:26:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 01:26:31 UTC

- **112,658** saved flights
- **39,207** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,658** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,374,627.8 tonnes** estimated CO2 emissions
- **79,688,569 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4633 |
| 2 | SkyWest Airlines | 4204 |
| 3 | EJA | 2189 |
| 4 | IndiGo | 2188 |
| 5 | American Airlines | 1781 |
| 6 | Southwest Airlines | 1682 |
| 7 | ENY | 1409 |
| 8 | Delta Air Lines | 1335 |
| 9 | Lufthansa | 1263 |
| 10 | Vueling | 1029 |
| 11 | LATAM Airlines | 993 |
| 12 | WIF | 992 |
| 13 | AXM | 942 |
| 14 | AZU | 937 |
| 15 | LXJ | 861 |
| 16 | Swiss International | 804 |
| 17 | All Nippon Airways | 782 |
| 18 | Alaska Airlines | 762 |
| 19 | QLK | 738 |
| 20 | easyJet | 726 |
| 21 | EJU | 712 |
| 22 | Cathay Pacific | 664 |
| 23 | AEE | 632 |
| 24 | Air France | 626 |
| 25 | United Airlines | 626 |
| 26 | VIV | 626 |
| 27 | MXY | 598 |
| 28 | CXK | 594 |
| 29 | GLO | 555 |
| 30 | AXB | 552 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95053 |
| 2 | 🇪🇸 ES | 7708 |
| 3 | 🇮🇳 IN | 6902 |
| 4 | 🇦🇺 AU | 6692 |
| 5 | 🇧🇷 BR | 6235 |
| 6 | 🇮🇹 IT | 6037 |
| 7 | 🇩🇪 DE | 6007 |
| 8 | 🇨🇦 CA | 5923 |
| 9 | 🇯🇵 JP | 5080 |
| 10 | 🇬🇧 GB | 4853 |
| 11 | 🇫🇷 FR | 4481 |
| 12 | 🇨🇴 CO | 3812 |
| 13 | 🇲🇽 MX | 3330 |
| 14 | 🇬🇷 GR | 3192 |
| 15 | 🇳🇴 NO | 3105 |
| 16 | 🇨🇭 CH | 2879 |
| 17 | 🇲🇾 MY | 2436 |
| 18 | 🇹🇷 TR | 2250 |
| 19 | 🇿🇦 ZA | 1911 |
| 20 | 🇰🇷 KR | 1855 |
| 21 | 🇳🇿 NZ | 1852 |
| 22 | 🇹🇭 TH | 1840 |
| 23 | 🇵🇱 PL | 1836 |
| 24 | 🇵🇭 PH | 1639 |
| 25 | 🇬🇹 GT | 1610 |
| 26 | 🇲🇦 MA | 1236 |
| 27 | 🇲🇴 MO | 1159 |
| 28 | 🇲🇪 ME | 1102 |
| 29 | 🇳🇱 NL | 1092 |
| 30 | 🇭🇷 HR | 977 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2407 |
| 2 | Denver International Airport |  | US | 1909 |
| 3 | Tokyo International Airport |  | JP | 1685 |
| 4 | Indira Gandhi International Airport |  | IN | 1502 |
| 5 | Harry Reid International Airport |  | US | 1415 |
| 6 | Guaymaral Airport |  | CO | 1413 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1387 |
| 8 | Zurich Airport |  | CH | 1264 |
| 9 | La Aurora Airport |  | GT | 1240 |
| 10 | Frankfurt am Main International Airport |  | DE | 1232 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1213 |
| 12 | Macau International Airport |  | MO | 1159 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1132 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 976 |
| 17 | Madrid Barajas International Airport |  | ES | 975 |
| 18 | Salt Lake City International Airport |  | US | 954 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 947 |
| 20 | Kuala Lumpur International Airport |  | MY | 944 |
| 21 | Charlotte/Douglas International Airport |  | US | 873 |
| 22 | Congonhas Airport |  | BR | 867 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 844 |
| 24 | Charles de Gaulle International Airport |  | FR | 838 |
| 25 | Bengaluru International Airport |  | IN | 835 |
| 26 | Malpensa International Airport |  | IT | 814 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 784 |
| 28 | Ninoy Aquino International Airport |  | PH | 756 |
| 29 | Daniel K Inouye International Airport |  | US | 743 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 740 |
| 31 | Tenerife Norte Airport |  | ES | 738 |
| 32 | Barcelona International Airport |  | ES | 732 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 713 |
| 34 | Amsterdam Airport Schiphol |  | NL | 672 |
| 35 | Don Mueang International Airport |  | TH | 670 |
| 36 | Vitoria/Foronda Airport |  | ES | 667 |
| 37 | Calgary International Airport |  | CA | 666 |
| 38 | Seattle-Tacoma International Airport |  | US | 651 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 648 |
| 40 | Viracopos International Airport |  | BR | 641 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 586 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 410 | 21m | 244 km | 1,726.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 299 | 24m | 225 km | 1,160.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 274 | 1h 25m | 910 km | 4,299.7 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 267 | 1h 10m | 770 km | 3,546.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 225 | 26m | 275 km | 1,066.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 154 | 27m | 152 km | 402.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 149 | 44m | 452 km | 1,161.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 143 | 44m | 241 km | 594.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 135 | 1h 1m | 695 km | 1,618.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 125 | 24m | 223 km | 480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-06-17 00:54 UTC | 2026-06-17 01:26 UTC | 32m |
| N232LA |  | Compton/Woodley Airport (KCPM) | Los Alamitos Army Air Field (KSLI) | 2026-06-17 00:26 UTC | 2026-06-17 01:25 UTC | 58m |
| LBQ799 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | PN21 (PN21) | 2026-06-17 00:54 UTC | 2026-06-17 01:15 UTC | 21m |
| N271B |  | South St Paul Municipal/Richard E Fleming Field (KSGS) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-06-17 00:28 UTC | 2026-06-17 01:08 UTC | 40m |
| AXEL10 | AXE | Oldham County Airport (KE52) | Provo Municipal Airport (KPVU) | 2026-06-16 23:39 UTC | 2026-06-17 01:07 UTC | 1h 28m |
| KING67 | KIN | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-06-17 00:50 UTC | 2026-06-17 01:07 UTC | 16m |
| ZEUS31 | ZEU | Raleigh-Durham International Airport (KRDU) | Harnett Regional Jetport Airport (KHRJ) | 2026-06-17 00:47 UTC | 2026-06-17 01:05 UTC | 18m |
| N305SA |  | Polecat Aerodrome (SC67) | Williamsburg Regional Airport (KCKI) | 2026-06-17 00:42 UTC | 2026-06-17 01:04 UTC | 22m |
| N650MC |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-06-17 00:27 UTC | 2026-06-17 01:04 UTC | 37m |
| N1022G |  | Phoenix Sky Harbor International Airport (KPHX) | NV13 (NV13) | 2026-06-16 23:38 UTC | 2026-06-17 01:04 UTC | 1h 25m |
| EWF | EWF | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-16 23:20 UTC | 2026-06-17 01:01 UTC | 1h 41m |
| N902NA |  | La Porte Municipal Airport (KT41) | Center Municipal Airport (KF17) | 2026-06-17 00:40 UTC | 2026-06-17 01:00 UTC | 20m |
| JBU1096 | JetBlue | Hartsfield/Jackson Atlanta International Airport (KATL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-16 23:04 UTC | 2026-06-17 00:59 UTC | 1h 55m |
| JBU398 | JetBlue | Seattle-Tacoma International Airport (KSEA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-16 20:28 UTC | 2026-06-17 00:55 UTC | 4h 27m |
| RVJ275 | RVJ | North Palm Beach County General Aviation Airport (KF45) | John F Kennedy International Airport (KJFK) | 2026-06-16 22:34 UTC | 2026-06-17 00:52 UTC | 2h 17m |
| N49BT |  | Eppley Airfield (KOMA) | Richton-Perry County Airport (KM59) | 2026-06-16 22:27 UTC | 2026-06-17 00:49 UTC | 2h 22m |
| CHP21 | CHP | Auburn Municipal Airport (KAUN) | Sacramento International Airport (KSMF) | 2026-06-17 00:34 UTC | 2026-06-17 00:47 UTC | 13m |
| N424KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-17 00:20 UTC | 2026-06-17 00:45 UTC | 25m |
| N96626 |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-06-16 23:52 UTC | 2026-06-17 00:43 UTC | 51m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-16 23:59 UTC | 2026-06-17 00:42 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
