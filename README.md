# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_00:59:49_UTC-green)

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

**Latest saved flight:** 2026-07-25 00:59:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 00:59:49 UTC

- **149,299** saved flights
- **49,783** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,299** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,785,576.1 tonnes** estimated CO2 emissions
- **103,511,656 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6015 |
| 2 | SkyWest Airlines | 5478 |
| 3 | EJA | 2964 |
| 4 | IndiGo | 2666 |
| 5 | American Airlines | 2379 |
| 6 | Southwest Airlines | 2267 |
| 7 | ENY | 1862 |
| 8 | Delta Air Lines | 1762 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1377 |
| 11 | AZU | 1289 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1258 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1073 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 965 |
| 18 | All Nippon Airways | 942 |
| 19 | Alaska Airlines | 935 |
| 20 | QLK | 927 |
| 21 | EJU | 910 |
| 22 | VIV | 824 |
| 23 | CXK | 799 |
| 24 | AEE | 781 |
| 25 | JetBlue | 781 |
| 26 | Cathay Pacific | 780 |
| 27 | Air France | 779 |
| 28 | MXY | 779 |
| 29 | GLO | 772 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129071 |
| 2 | 🇪🇸 ES | 9616 |
| 3 | 🇦🇺 AU | 8476 |
| 4 | 🇧🇷 BR | 8423 |
| 5 | 🇮🇳 IN | 8375 |
| 6 | 🇨🇦 CA | 8020 |
| 7 | 🇮🇹 IT | 7704 |
| 8 | 🇩🇪 DE | 7616 |
| 9 | 🇬🇧 GB | 6815 |
| 10 | 🇯🇵 JP | 6177 |
| 11 | 🇫🇷 FR | 5904 |
| 12 | 🇨🇴 CO | 5036 |
| 13 | 🇲🇽 MX | 4329 |
| 14 | 🇬🇷 GR | 4214 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3511 |
| 18 | 🇲🇾 MY | 2795 |
| 19 | 🇵🇱 PL | 2512 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2256 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2059 |
| 24 | 🇵🇭 PH | 1984 |
| 25 | 🇬🇹 GT | 1947 |
| 26 | 🇲🇦 MA | 1522 |
| 27 | 🇲🇪 ME | 1471 |
| 28 | 🇳🇱 NL | 1380 |
| 29 | 🇭🇷 HR | 1353 |
| 30 | 🇲🇴 MO | 1243 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3077 |
| 2 | Denver International Airport |  | US | 2514 |
| 3 | Tokyo International Airport |  | JP | 1978 |
| 4 | Guaymaral Airport |  | CO | 1866 |
| 5 | Indira Gandhi International Airport |  | IN | 1860 |
| 6 | Harry Reid International Airport |  | US | 1854 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1669 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1572 |
| 10 | La Aurora Airport |  | GT | 1508 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 12 | Frankfurt am Main International Airport |  | DE | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1342 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1284 |
| 17 | Macau International Airport |  | MO | 1243 |
| 18 | Congonhas Airport |  | BR | 1205 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1182 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1161 |
| 22 | Kuala Lumpur International Airport |  | MY | 1077 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1070 |
| 24 | Charlotte/Douglas International Airport |  | US | 1066 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1049 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1002 |
| 28 | Malpensa International Airport |  | IT | 964 |
| 29 | Ninoy Aquino International Airport |  | PH | 929 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 909 |
| 31 | Barcelona International Airport |  | ES | 898 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 896 |
| 33 | Daniel K Inouye International Airport |  | US | 896 |
| 34 | Seattle-Tacoma International Airport |  | US | 860 |
| 35 | Calgary International Airport |  | CA | 854 |
| 36 | Tenerife Norte Airport |  | ES | 852 |
| 37 | Scottsdale Airport |  | US | 849 |
| 38 | Viracopos International Airport |  | BR | 841 |
| 39 | Amsterdam Airport Schiphol |  | NL | 830 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 542 | 21m | 244 km | 2,282.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 347 | 1h 9m | 770 km | 4,609.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 266 | 27m | 275 km | 1,260.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 196 | 20m | 99 km | 335.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 183 | 20m | 250 km | 790.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 171 | 44m | 452 km | 1,332.7 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 169 | 1h 1m | 695 km | 2,025.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-25 00:42 UTC | 2026-07-25 00:59 UTC | 17m |
| N309PF |  | Pekin Municipal Airport (KC15) | Weishaupt Airport (9IL6) | 2026-07-25 00:40 UTC | 2026-07-25 00:54 UTC | 13m |
| LFA312 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Executive Airport (KORL) | 2026-07-24 23:38 UTC | 2026-07-25 00:50 UTC | 1h 11m |
| BRG605 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-07-25 00:26 UTC | 2026-07-25 00:50 UTC | 23m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-07-25 00:28 UTC | 2026-07-25 00:45 UTC | 16m |
| N23VJ |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-24 23:32 UTC | 2026-07-25 00:43 UTC | 1h 11m |
| EJA601 | EJA | Martha's Vineyard Airport (KMVY) | Lincoln Airport (KLNK) | 2026-07-24 21:13 UTC | 2026-07-25 00:41 UTC | 3h 28m |
| N7499C |  | Portland-Hillsboro Airport (KHIO) | WN80 (WN80) | 2026-07-25 00:18 UTC | 2026-07-25 00:40 UTC | 22m |
| N44LX |  | Gallinger Airport (51WI) | With Wings And A Halo Airport (0WI7) | 2026-07-25 00:24 UTC | 2026-07-25 00:39 UTC | 14m |
| LOT45 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Toronto Pearson International Airport (CYYZ) | 2026-07-24 15:59 UTC | 2026-07-25 00:38 UTC | 8h 39m |
| XSN73 | XSN | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-24 23:57 UTC | 2026-07-25 00:33 UTC | 36m |
| N667JD |  | Raleigh-Durham International Airport (KRDU) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-24 19:44 UTC | 2026-07-25 00:30 UTC | 4h 45m |
| N95RZ |  | Aerodrome Les Noyers Airport (50OH) | 00OH (00OH) | 2026-07-25 00:02 UTC | 2026-07-25 00:29 UTC | 27m |
| N531HC |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-25 00:20 UTC | 2026-07-25 00:25 UTC | 4m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-25 00:15 UTC | 2026-07-25 00:24 UTC | 8m |
| N491LG |  | Tall Timber Airport (CD28) | Tall Timber Airport (CD28) | 2026-07-24 23:42 UTC | 2026-07-25 00:21 UTC | 39m |
| N659SP |  | Northwest Florida Beaches International Airport (KECP) | Northwest Florida Beaches International Airport (KECP) | 2026-07-24 23:39 UTC | 2026-07-25 00:21 UTC | 42m |
| N558LM |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-07-24 23:38 UTC | 2026-07-25 00:16 UTC | 37m |
| RPC8694 | RPC | Plaridel Airport (RPUX) | Plaridel Airport (RPUX) | 2026-07-24 23:55 UTC | 2026-07-25 00:14 UTC | 18m |
| SKW3897 | SkyWest Airlines | Seattle-Tacoma International Airport (KSEA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-24 22:09 UTC | 2026-07-25 00:13 UTC | 2h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
