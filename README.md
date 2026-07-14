# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_00:40:38_UTC-green)

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

**Latest saved flight:** 2026-07-14 00:40:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-14 00:40:38 UTC

- **141,138** saved flights
- **47,427** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,138** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,694,566.1 tonnes** estimated CO2 emissions
- **98,235,719 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5743 |
| 2 | SkyWest Airlines | 5174 |
| 3 | EJA | 2782 |
| 4 | IndiGo | 2576 |
| 5 | American Airlines | 2248 |
| 6 | Southwest Airlines | 2128 |
| 7 | ENY | 1756 |
| 8 | Delta Air Lines | 1673 |
| 9 | Lufthansa | 1429 |
| 10 | LATAM Airlines | 1298 |
| 11 | Vueling | 1216 |
| 12 | AZU | 1214 |
| 13 | WIF | 1210 |
| 14 | LXJ | 1086 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 1005 |
| 17 | easyJet | 922 |
| 18 | All Nippon Airways | 901 |
| 19 | Alaska Airlines | 890 |
| 20 | QLK | 884 |
| 21 | EJU | 869 |
| 22 | VIV | 780 |
| 23 | AEE | 756 |
| 24 | CXK | 756 |
| 25 | Air France | 754 |
| 26 | JetBlue | 749 |
| 27 | United Airlines | 737 |
| 28 | Cathay Pacific | 732 |
| 29 | MXY | 731 |
| 30 | GLO | 721 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121469 |
| 2 | 🇪🇸 ES | 9238 |
| 3 | 🇮🇳 IN | 8070 |
| 4 | 🇦🇺 AU | 8049 |
| 5 | 🇧🇷 BR | 7970 |
| 6 | 🇨🇦 CA | 7430 |
| 7 | 🇮🇹 IT | 7359 |
| 8 | 🇩🇪 DE | 7334 |
| 9 | 🇬🇧 GB | 6438 |
| 10 | 🇯🇵 JP | 5912 |
| 11 | 🇫🇷 FR | 5610 |
| 12 | 🇨🇴 CO | 4485 |
| 13 | 🇲🇽 MX | 4098 |
| 14 | 🇬🇷 GR | 4015 |
| 15 | 🇳🇴 NO | 3785 |
| 16 | 🇨🇭 CH | 3661 |
| 17 | 🇹🇷 TR | 3332 |
| 18 | 🇲🇾 MY | 2732 |
| 19 | 🇵🇱 PL | 2359 |
| 20 | 🇿🇦 ZA | 2308 |
| 21 | 🇳🇿 NZ | 2148 |
| 22 | 🇹🇭 TH | 2110 |
| 23 | 🇰🇷 KR | 2016 |
| 24 | 🇵🇭 PH | 1912 |
| 25 | 🇬🇹 GT | 1863 |
| 26 | 🇲🇦 MA | 1481 |
| 27 | 🇲🇪 ME | 1403 |
| 28 | 🇳🇱 NL | 1328 |
| 29 | 🇭🇷 HR | 1277 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2912 |
| 2 | Denver International Airport |  | US | 2362 |
| 3 | Tokyo International Airport |  | JP | 1913 |
| 4 | Indira Gandhi International Airport |  | IN | 1788 |
| 5 | Harry Reid International Airport |  | US | 1766 |
| 6 | Guaymaral Airport |  | CO | 1715 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1620 |
| 8 | Zurich Airport |  | CH | 1572 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1484 |
| 10 | La Aurora Airport |  | GT | 1441 |
| 11 | Frankfurt am Main International Airport |  | DE | 1379 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1347 |
| 13 | Chicago O'Hare International Airport |  | US | 1328 |
| 14 | Salt Lake City International Airport |  | US | 1263 |
| 15 | El Dorado International Airport |  | CO | 1247 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1225 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1156 |
| 19 | Madrid Barajas International Airport |  | ES | 1142 |
| 20 | Congonhas Airport |  | BR | 1134 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1126 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1027 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1014 |
| 25 | Charles de Gaulle International Airport |  | FR | 999 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 982 |
| 27 | Bengaluru International Airport |  | IN | 967 |
| 28 | Malpensa International Airport |  | IT | 915 |
| 29 | Ninoy Aquino International Airport |  | PH | 892 |
| 30 | Daniel K Inouye International Airport |  | US | 863 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 862 |
| 32 | Barcelona International Airport |  | ES | 861 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 831 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 810 |
| 36 | Viracopos International Airport |  | BR | 802 |
| 37 | Seattle-Tacoma International Airport |  | US | 801 |
| 38 | Amsterdam Airport Schiphol |  | NL | 801 |
| 39 | Scottsdale Airport |  | US | 800 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 723 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 513 | 21m | 244 km | 2,160.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
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
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 188 | 20m | 99 km | 322.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 186 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 160 | 1h 38m | 1,156 km | 3,191.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 158 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N115 |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-14 00:14 UTC | 2026-07-14 00:40 UTC | 26m |
| EVA891 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Chek Lap Kok International Airport (VHHH) | 2026-07-13 23:26 UTC | 2026-07-14 00:34 UTC | 1h 8m |
|  |  | 14CO (14CO) | 14CO (14CO) | 2026-07-14 00:17 UTC | 2026-07-14 00:30 UTC | 12m |
| BRW101 | BRW | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-07-13 23:45 UTC | 2026-07-14 00:27 UTC | 41m |
| N79BE |  | MT88 (MT88) | Troy Airport (K57S) | 2026-07-14 00:07 UTC | 2026-07-14 00:24 UTC | 17m |
| CFCAU | CFC | Abbotsford Airport (CYXX) | Chilliwack Airport (CYCW) | 2026-07-13 23:51 UTC | 2026-07-14 00:24 UTC | 33m |
| N520SC |  | Kalamazoo/Battle Creek International Airport (KAZO) | Zinck Airport (90ME) | 2026-07-13 22:46 UTC | 2026-07-14 00:23 UTC | 1h 37m |
| CGRDW | CGR | Fountains Airport (ID60) | Calgary / Springbank Airport (CYBW) | 2026-07-13 22:45 UTC | 2026-07-14 00:20 UTC | 1h 35m |
| JBU1782 | JetBlue | Duke Field,(Eglin Af Aux Nr 3) Airport (KEGI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-13 21:03 UTC | 2026-07-14 00:13 UTC | 3h 10m |
| N112EE |  | Plains Airport (KS34) | Art Sutcliffe Field (CAJ3) | 2026-07-13 23:37 UTC | 2026-07-14 00:12 UTC | 35m |
| JIA5209 | JIA | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-13 13:00 UTC | 2026-07-14 00:12 UTC | 11h 11m |
| N59KX |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-14 00:10 UTC | 2026-07-14 00:10 UTC | 0m |
| N73753 |  | Waukegan Ntl Airport (KUGN) | Waukegan Ntl Airport (KUGN) | 2026-07-13 23:55 UTC | 2026-07-14 00:09 UTC | 14m |
| YGZ | YGZ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-13 23:38 UTC | 2026-07-14 00:06 UTC | 28m |
| MRA633 | MRA | Durant Regional/Eaker Field (KDUA) | Mc Alester Regional Airport (KMLC) | 2026-07-13 23:38 UTC | 2026-07-14 00:03 UTC | 25m |
| VULCN91 | VUL | Tlc Airport (OK71) | Double H Ranch Airport (OK40) | 2026-07-13 23:51 UTC | 2026-07-14 00:02 UTC | 11m |
| JIA5394 | JIA | Louisville Muhammad Ali International Airport (KSDF) | Philadelphia International Airport (KPHL) | 2026-07-13 22:26 UTC | 2026-07-13 23:58 UTC | 1h 32m |
| SKW4327 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Simko Field (1ID9) | 2026-07-13 23:35 UTC | 2026-07-13 23:58 UTC | 22m |
| PDT6043 | PDT | Charlotte/Douglas International Airport (KCLT) | Fairfield County Airport (KFDW) | 2026-07-13 23:42 UTC | 2026-07-13 23:57 UTC | 14m |
| N5721T |  | Boeing Field/King County International Airport (KBFI) | Leisureland Airpark (WA96) | 2026-07-13 22:59 UTC | 2026-07-13 23:55 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
