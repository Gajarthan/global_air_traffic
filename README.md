# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_13:46:46_UTC-green)

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

**Latest saved flight:** 2026-07-18 13:46:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-18 13:46:46 UTC

- **142,367** saved flights
- **47,752** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,367** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,708,107.1 tonnes** estimated CO2 emissions
- **99,020,700 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5796 |
| 2 | SkyWest Airlines | 5193 |
| 3 | EJA | 2799 |
| 4 | IndiGo | 2599 |
| 5 | American Airlines | 2272 |
| 6 | Southwest Airlines | 2143 |
| 7 | ENY | 1760 |
| 8 | Delta Air Lines | 1683 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1310 |
| 11 | Vueling | 1224 |
| 12 | AZU | 1223 |
| 13 | WIF | 1219 |
| 14 | LXJ | 1094 |
| 15 | AXM | 1055 |
| 16 | Swiss International | 1014 |
| 17 | easyJet | 927 |
| 18 | All Nippon Airways | 913 |
| 19 | Alaska Airlines | 896 |
| 20 | QLK | 894 |
| 21 | EJU | 878 |
| 22 | VIV | 791 |
| 23 | AEE | 762 |
| 24 | CXK | 762 |
| 25 | Air France | 759 |
| 26 | JetBlue | 759 |
| 27 | United Airlines | 741 |
| 28 | MXY | 738 |
| 29 | Cathay Pacific | 735 |
| 30 | GLO | 729 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122338 |
| 2 | 🇪🇸 ES | 9295 |
| 3 | 🇦🇺 AU | 8153 |
| 4 | 🇮🇳 IN | 8141 |
| 5 | 🇧🇷 BR | 8036 |
| 6 | 🇨🇦 CA | 7488 |
| 7 | 🇮🇹 IT | 7430 |
| 8 | 🇩🇪 DE | 7388 |
| 9 | 🇬🇧 GB | 6520 |
| 10 | 🇯🇵 JP | 5972 |
| 11 | 🇫🇷 FR | 5667 |
| 12 | 🇨🇴 CO | 4557 |
| 13 | 🇲🇽 MX | 4127 |
| 14 | 🇬🇷 GR | 4057 |
| 15 | 🇳🇴 NO | 3817 |
| 16 | 🇨🇭 CH | 3688 |
| 17 | 🇹🇷 TR | 3370 |
| 18 | 🇲🇾 MY | 2751 |
| 19 | 🇵🇱 PL | 2396 |
| 20 | 🇿🇦 ZA | 2326 |
| 21 | 🇳🇿 NZ | 2182 |
| 22 | 🇹🇭 TH | 2127 |
| 23 | 🇰🇷 KR | 2027 |
| 24 | 🇵🇭 PH | 1928 |
| 25 | 🇬🇹 GT | 1870 |
| 26 | 🇲🇦 MA | 1490 |
| 27 | 🇲🇪 ME | 1411 |
| 28 | 🇳🇱 NL | 1344 |
| 29 | 🇭🇷 HR | 1298 |
| 30 | 🇲🇴 MO | 1192 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2925 |
| 2 | Denver International Airport |  | US | 2378 |
| 3 | Tokyo International Airport |  | JP | 1928 |
| 4 | Indira Gandhi International Airport |  | IN | 1804 |
| 5 | Harry Reid International Airport |  | US | 1786 |
| 6 | Guaymaral Airport |  | CO | 1736 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1634 |
| 8 | Zurich Airport |  | CH | 1585 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1490 |
| 10 | La Aurora Airport |  | GT | 1446 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1349 |
| 13 | Chicago O'Hare International Airport |  | US | 1330 |
| 14 | Salt Lake City International Airport |  | US | 1271 |
| 15 | El Dorado International Airport |  | CO | 1260 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1254 |
| 17 | Macau International Airport |  | MO | 1192 |
| 18 | Capua Airport |  | IT | 1166 |
| 19 | Madrid Barajas International Airport |  | ES | 1146 |
| 20 | Congonhas Airport |  | BR | 1143 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1129 |
| 22 | Kuala Lumpur International Airport |  | MY | 1062 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1028 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 993 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 921 |
| 29 | Ninoy Aquino International Airport |  | PH | 900 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 872 |
| 31 | Daniel K Inouye International Airport |  | US | 868 |
| 32 | Barcelona International Airport |  | ES | 868 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 840 |
| 34 | Tenerife Norte Airport |  | ES | 824 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Seattle-Tacoma International Airport |  | US | 807 |
| 37 | Amsterdam Airport Schiphol |  | NL | 807 |
| 38 | Viracopos International Airport |  | BR | 806 |
| 39 | Scottsdale Airport |  | US | 803 |
| 40 | Vitoria/Foronda Airport |  | ES | 784 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 731 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 518 | 21m | 244 km | 2,181.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 338 | 1h 9m | 770 km | 4,490.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 210 | 22m | 55 km | 199.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 178 | 28m | 152 km | 465.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 164 | 1h 16m | 961 km | 2,718.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 159 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1039 | CXK | Smyrna Airport (KMQY) | Smyrna Airport (KMQY) | 2026-07-18 13:34 UTC | 2026-07-18 13:46 UTC | 12m |
| N97FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-07-18 12:38 UTC | 2026-07-18 13:42 UTC | 1h 3m |
| SYH3831 | SYH | Millinocket Municipal Airport (KMLT) | Laurence G Hanscom Field (KBED) | 2026-07-18 12:03 UTC | 2026-07-18 13:42 UTC | 1h 38m |
| N756PA |  | Orlando Executive Airport (KORL) | Fort Lauderdale/Hollywood International Airport (KFLL) | 2026-07-18 11:53 UTC | 2026-07-18 13:41 UTC | 1h 47m |
| GFBPS | GFB | EG32 (EG32) | EG32 (EG32) | 2026-07-18 11:19 UTC | 2026-07-18 13:41 UTC | 2h 21m |
| HAT3301 | HAT | Malpensa International Airport (LIMC) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-18 12:48 UTC | 2026-07-18 13:36 UTC | 48m |
| N59CW |  | Kissimmee Gateway Airport (KISM) | Winter Haven Regional Airport (KGIF) | 2026-07-18 12:05 UTC | 2026-07-18 13:30 UTC | 1h 25m |
| JIA5209 | JIA | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-18 12:35 UTC | 2026-07-18 13:27 UTC | 51m |
| N909MA |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-18 12:57 UTC | 2026-07-18 13:25 UTC | 27m |
| N715GC |  | Sulphur Springs Municipal Airport (KSLR) | 81NM (81NM) | 2026-07-18 11:24 UTC | 2026-07-18 13:24 UTC | 1h 59m |
| FGJBC | FGJ | Quiberon Airport (LFEQ) | Quiberon Airport (LFEQ) | 2026-07-18 12:36 UTC | 2026-07-18 13:24 UTC | 48m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-07-18 12:09 UTC | 2026-07-18 13:21 UTC | 1h 12m |
| CGBGA | CGB | Bridgewater / Dayspring Airpark (CDY6) | Bridgewater / Dayspring Airpark (CDY6) | 2026-07-18 12:57 UTC | 2026-07-18 13:18 UTC | 21m |
| N132JS |  | Mesquite Airport (K67L) | Mesquite Airport (K67L) | 2026-07-18 13:11 UTC | 2026-07-18 13:18 UTC | 7m |
| YRGVB | YRG | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-07-18 12:27 UTC | 2026-07-18 13:16 UTC | 48m |
| TOG923 | TOG | Cecil Ranch Airport (37CN) | NV13 (NV13) | 2026-07-18 12:44 UTC | 2026-07-18 13:15 UTC | 30m |
| TIBBI | TIB | Tobias Bolanos International Airport (MRPV) | Tobias Bolanos International Airport (MRPV) | 2026-07-18 13:01 UTC | 2026-07-18 13:14 UTC | 12m |
| A6FTS |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-07-18 13:11 UTC | 2026-07-18 13:12 UTC | 1m |
| N670LF |  | Felts Field (KSFF) | Lazy F Ranch Airport (99OR) | 2026-07-18 12:29 UTC | 2026-07-18 13:08 UTC | 39m |
| N377KH |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-07-18 12:50 UTC | 2026-07-18 13:08 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
