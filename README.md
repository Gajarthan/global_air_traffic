# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_03:54:28_UTC-green)

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

**Latest saved flight:** 2026-07-14 03:54:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-14 03:54:28 UTC

- **141,240** saved flights
- **47,450** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,240** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,695,795.6 tonnes** estimated CO2 emissions
- **98,306,992 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5743 |
| 2 | SkyWest Airlines | 5175 |
| 3 | EJA | 2784 |
| 4 | IndiGo | 2583 |
| 5 | American Airlines | 2250 |
| 6 | Southwest Airlines | 2128 |
| 7 | ENY | 1756 |
| 8 | Delta Air Lines | 1675 |
| 9 | Lufthansa | 1429 |
| 10 | LATAM Airlines | 1298 |
| 11 | Vueling | 1216 |
| 12 | AZU | 1214 |
| 13 | WIF | 1210 |
| 14 | LXJ | 1086 |
| 15 | AXM | 1050 |
| 16 | Swiss International | 1005 |
| 17 | easyJet | 922 |
| 18 | All Nippon Airways | 905 |
| 19 | Alaska Airlines | 890 |
| 20 | QLK | 886 |
| 21 | EJU | 869 |
| 22 | VIV | 781 |
| 23 | AEE | 756 |
| 24 | CXK | 756 |
| 25 | Air France | 754 |
| 26 | JetBlue | 750 |
| 27 | United Airlines | 737 |
| 28 | Cathay Pacific | 732 |
| 29 | MXY | 731 |
| 30 | GLO | 721 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121548 |
| 2 | 🇪🇸 ES | 9238 |
| 3 | 🇮🇳 IN | 8087 |
| 4 | 🇦🇺 AU | 8076 |
| 5 | 🇧🇷 BR | 7970 |
| 6 | 🇨🇦 CA | 7436 |
| 7 | 🇮🇹 IT | 7359 |
| 8 | 🇩🇪 DE | 7336 |
| 9 | 🇬🇧 GB | 6439 |
| 10 | 🇯🇵 JP | 5923 |
| 11 | 🇫🇷 FR | 5610 |
| 12 | 🇨🇴 CO | 4489 |
| 13 | 🇲🇽 MX | 4102 |
| 14 | 🇬🇷 GR | 4015 |
| 15 | 🇳🇴 NO | 3785 |
| 16 | 🇨🇭 CH | 3661 |
| 17 | 🇹🇷 TR | 3337 |
| 18 | 🇲🇾 MY | 2739 |
| 19 | 🇵🇱 PL | 2361 |
| 20 | 🇿🇦 ZA | 2308 |
| 21 | 🇳🇿 NZ | 2153 |
| 22 | 🇹🇭 TH | 2112 |
| 23 | 🇰🇷 KR | 2016 |
| 24 | 🇵🇭 PH | 1912 |
| 25 | 🇬🇹 GT | 1865 |
| 26 | 🇲🇦 MA | 1481 |
| 27 | 🇲🇪 ME | 1403 |
| 28 | 🇳🇱 NL | 1328 |
| 29 | 🇭🇷 HR | 1277 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2913 |
| 2 | Denver International Airport |  | US | 2362 |
| 3 | Tokyo International Airport |  | JP | 1916 |
| 4 | Indira Gandhi International Airport |  | IN | 1791 |
| 5 | Harry Reid International Airport |  | US | 1767 |
| 6 | Guaymaral Airport |  | CO | 1717 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1620 |
| 8 | Zurich Airport |  | CH | 1572 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1484 |
| 10 | La Aurora Airport |  | GT | 1442 |
| 11 | Frankfurt am Main International Airport |  | DE | 1379 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1347 |
| 13 | Chicago O'Hare International Airport |  | US | 1328 |
| 14 | Salt Lake City International Airport |  | US | 1263 |
| 15 | El Dorado International Airport |  | CO | 1248 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1227 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1156 |
| 19 | Madrid Barajas International Airport |  | ES | 1142 |
| 20 | Congonhas Airport |  | BR | 1134 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1127 |
| 22 | Kuala Lumpur International Airport |  | MY | 1059 |
| 23 | Charlotte/Douglas International Airport |  | US | 1027 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1020 |
| 25 | Charles de Gaulle International Airport |  | FR | 999 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 982 |
| 27 | Bengaluru International Airport |  | IN | 970 |
| 28 | Malpensa International Airport |  | IT | 915 |
| 29 | Ninoy Aquino International Airport |  | PH | 892 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 864 |
| 31 | Daniel K Inouye International Airport |  | US | 863 |
| 32 | Barcelona International Airport |  | ES | 861 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 833 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 810 |
| 36 | Viracopos International Airport |  | BR | 802 |
| 37 | Seattle-Tacoma International Airport |  | US | 801 |
| 38 | Amsterdam Airport Schiphol |  | NL | 801 |
| 39 | Scottsdale Airport |  | US | 801 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 724 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 513 | 21m | 244 km | 2,160.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 334 | 1h 9m | 770 km | 4,436.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 207 | 22m | 55 km | 196.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 186 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 162 | 1h 1m | 695 km | 1,941.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 161 | 1h 38m | 1,156 km | 3,211.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 158 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFL01 | CFL | Hamilton International Airport (NZHN) | Whakatane Airport (NZWK) | 2026-07-14 03:17 UTC | 2026-07-14 03:54 UTC | 37m |
| CAL107 | CAL | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-14 00:56 UTC | 2026-07-14 03:50 UTC | 2h 54m |
| DAL88 | Delta Air Lines | Chek Lap Kok International Airport (VHHH) | Taipei Songshan Airport (RCSS) | 2026-07-14 02:27 UTC | 2026-07-14 03:50 UTC | 1h 23m |
| IYI | IYI | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-07-14 03:21 UTC | 2026-07-14 03:46 UTC | 24m |
| KXW | KXW | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-14 03:02 UTC | 2026-07-14 03:42 UTC | 39m |
| N4532X |  | Red Wing Regional Airport (KRGK) | Red Wing Regional Airport (KRGK) | 2026-07-14 02:56 UTC | 2026-07-14 03:42 UTC | 46m |
| N137BG |  | Mc Minnville Municipal Airport (KMMV) | Mason City Municipal Airport (KMCW) | 2026-07-14 00:27 UTC | 2026-07-14 03:41 UTC | 3h 13m |
| FFT2582 | FFT | Palm Beach International Airport (KPBI) | Philadelphia International Airport (KPHL) | 2026-07-14 01:32 UTC | 2026-07-14 03:38 UTC | 2h 5m |
| 8L8 |  | Sydney Bankstown Airport (YSBK) | Kelvin Station Airport (YKEL) | 2026-07-14 02:40 UTC | 2026-07-14 03:27 UTC | 47m |
|  |  | Futaysi Airport (OMAF) | Zirku Airport (OMAZ) | 2026-07-14 03:13 UTC | 2026-07-14 03:25 UTC | 12m |
| JBU1318 | JetBlue | John F Kennedy International Airport (KJFK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-14 02:37 UTC | 2026-07-14 03:25 UTC | 47m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-07-14 02:51 UTC | 2026-07-14 03:17 UTC | 26m |
| AAL1927 | American Airlines | George Bush Intcntl/Houston Airport (KIAH) | Philadelphia International Airport (KPHL) | 2026-07-14 00:11 UTC | 2026-07-14 03:13 UTC | 3h 2m |
| SLI995 | SLI | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-14 02:10 UTC | 2026-07-14 03:13 UTC | 1h 2m |
| IGO2121 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-14 00:43 UTC | 2026-07-14 03:10 UTC | 2h 26m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | St. Paul Airport (CEW3) | 2026-07-14 02:46 UTC | 2026-07-14 03:07 UTC | 21m |
| N719KF |  | Old Aerodrome (9CL7) | Sacramento International Airport (KSMF) | 2026-07-14 02:43 UTC | 2026-07-14 03:07 UTC | 24m |
| HOOK25 | HOO | Cottonwood Airport (OK66) | 84OL (84OL) | 2026-07-14 02:25 UTC | 2026-07-14 03:06 UTC | 40m |
| BALL46 | BAL | Good Life Ranch Airport (17OK) | William R Pogue Municipal Airport (KOWP) | 2026-07-14 02:40 UTC | 2026-07-14 03:04 UTC | 24m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-07-14 02:27 UTC | 2026-07-14 03:02 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
