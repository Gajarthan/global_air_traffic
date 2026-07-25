# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_06:41:38_UTC-green)

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

**Latest saved flight:** 2026-07-25 06:41:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 06:41:38 UTC

- **149,470** saved flights
- **49,813** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,470** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,788,222.2 tonnes** estimated CO2 emissions
- **103,665,056 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6023 |
| 2 | SkyWest Airlines | 5479 |
| 3 | EJA | 2966 |
| 4 | IndiGo | 2672 |
| 5 | American Airlines | 2380 |
| 6 | Southwest Airlines | 2272 |
| 7 | ENY | 1863 |
| 8 | Delta Air Lines | 1763 |
| 9 | Lufthansa | 1458 |
| 10 | LATAM Airlines | 1377 |
| 11 | AZU | 1292 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1259 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1076 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 965 |
| 18 | All Nippon Airways | 946 |
| 19 | Alaska Airlines | 935 |
| 20 | QLK | 930 |
| 21 | EJU | 911 |
| 22 | VIV | 825 |
| 23 | CXK | 799 |
| 24 | AEE | 784 |
| 25 | JetBlue | 781 |
| 26 | Cathay Pacific | 780 |
| 27 | Air France | 779 |
| 28 | MXY | 779 |
| 29 | GLO | 773 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129141 |
| 2 | 🇪🇸 ES | 9624 |
| 3 | 🇦🇺 AU | 8497 |
| 4 | 🇧🇷 BR | 8431 |
| 5 | 🇮🇳 IN | 8403 |
| 6 | 🇨🇦 CA | 8020 |
| 7 | 🇮🇹 IT | 7713 |
| 8 | 🇩🇪 DE | 7626 |
| 9 | 🇬🇧 GB | 6818 |
| 10 | 🇯🇵 JP | 6203 |
| 11 | 🇫🇷 FR | 5904 |
| 12 | 🇨🇴 CO | 5039 |
| 13 | 🇲🇽 MX | 4332 |
| 14 | 🇬🇷 GR | 4226 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3901 |
| 17 | 🇹🇷 TR | 3516 |
| 18 | 🇲🇾 MY | 2801 |
| 19 | 🇵🇱 PL | 2515 |
| 20 | 🇿🇦 ZA | 2412 |
| 21 | 🇳🇿 NZ | 2261 |
| 22 | 🇹🇭 TH | 2179 |
| 23 | 🇰🇷 KR | 2062 |
| 24 | 🇵🇭 PH | 1991 |
| 25 | 🇬🇹 GT | 1949 |
| 26 | 🇲🇦 MA | 1523 |
| 27 | 🇲🇪 ME | 1473 |
| 28 | 🇳🇱 NL | 1380 |
| 29 | 🇭🇷 HR | 1354 |
| 30 | 🇲🇴 MO | 1246 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3080 |
| 2 | Denver International Airport |  | US | 2514 |
| 3 | Tokyo International Airport |  | JP | 1982 |
| 4 | Guaymaral Airport |  | CO | 1866 |
| 5 | Indira Gandhi International Airport |  | IN | 1865 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1674 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1573 |
| 10 | La Aurora Airport |  | GT | 1509 |
| 11 | Frankfurt am Main International Airport |  | DE | 1407 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1343 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1285 |
| 17 | Macau International Airport |  | MO | 1246 |
| 18 | Congonhas Airport |  | BR | 1205 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1186 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1162 |
| 22 | Kuala Lumpur International Airport |  | MY | 1080 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1074 |
| 24 | Charlotte/Douglas International Airport |  | US | 1066 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1050 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1005 |
| 28 | Malpensa International Airport |  | IT | 969 |
| 29 | Ninoy Aquino International Airport |  | PH | 933 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 909 |
| 31 | Barcelona International Airport |  | ES | 899 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 898 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Seattle-Tacoma International Airport |  | US | 860 |
| 35 | Calgary International Airport |  | CA | 854 |
| 36 | Tenerife Norte Airport |  | ES | 852 |
| 37 | Scottsdale Airport |  | US | 849 |
| 38 | Viracopos International Airport |  | BR | 844 |
| 39 | Amsterdam Airport Schiphol |  | NL | 830 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 363 | 24m | 225 km | 1,408.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 348 | 1h 9m | 770 km | 4,622.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 271 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 267 | 27m | 275 km | 1,265.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 200 | 1h 47m | 1,423 km | 4,908.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 184 | 20m | 250 km | 794.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 172 | 44m | 452 km | 1,340.5 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 169 | 1h 1m | 695 km | 2,025.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPMDM | SPM | Gdańsk Lech Wałęsa Airport (EPGD) | Malbork Military Air Base (EPMB) | 2026-07-25 05:58 UTC | 2026-07-25 06:41 UTC | 43m |
| APJ155 | APJ | Kansai International Airport (RJBB) | Ashiya Airport (RJFA) | 2026-07-25 05:59 UTC | 2026-07-25 06:38 UTC | 39m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-07-25 05:52 UTC | 2026-07-25 06:17 UTC | 25m |
| N131HN |  | Skala Airport (PN55) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-07-25 05:59 UTC | 2026-07-25 06:15 UTC | 16m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-25 05:54 UTC | 2026-07-25 06:07 UTC | 12m |
| RYR4LB | Ryanair | Sofia Airport (LBSF) | Elmsett Airport (EGST) | 2026-07-25 02:57 UTC | 2026-07-25 06:04 UTC | 3h 7m |
| N958AL |  | Sky Valley Airstrip (WA68) | Boeing Field/King County International Airport (KBFI) | 2026-07-25 05:36 UTC | 2026-07-25 05:54 UTC | 17m |
| VLG9NM | Vueling | Barcelona International Airport (LEBL) | San Sebastian Airport (LESO) | 2026-07-25 05:13 UTC | 2026-07-25 05:53 UTC | 40m |
| RYR6612 | Ryanair | Madrid Barajas International Airport (LEMD) | Kenitra Airport (GMMY) | 2026-07-25 04:45 UTC | 2026-07-25 05:53 UTC | 1h 8m |
| RYR2778 | Ryanair | Thessaloniki Macedonia International Airport (LGTS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-25 04:03 UTC | 2026-07-25 05:52 UTC | 1h 48m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Losinj Island Airport (LDLO) | 2026-07-25 04:55 UTC | 2026-07-25 05:52 UTC | 56m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-07-25 04:59 UTC | 2026-07-25 05:44 UTC | 45m |
| EWG1T | EWG | Berlin Brandenburg Airport (EDDB) | Visoko Sport Airfield (LQVI) | 2026-07-25 04:27 UTC | 2026-07-25 05:42 UTC | 1h 14m |
| ADO128 | ADO | Hakodate Airport (RJCH) | Matsumoto Airport (RJAF) | 2026-07-25 04:33 UTC | 2026-07-25 05:39 UTC | 1h 5m |
| R1675 |  | Caloundra Airport (YCDR) | Caloundra Airport (YCDR) | 2026-07-25 05:23 UTC | 2026-07-25 05:38 UTC | 15m |
| AEE260 | AEE | Eleftherios Venizelos International Airport (LGAV) | Limnos Airport (LGLM) | 2026-07-25 05:01 UTC | 2026-07-25 05:38 UTC | 37m |
| FD613 |  | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-07-25 04:51 UTC | 2026-07-25 05:37 UTC | 46m |
| IGO7626 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-07-25 04:58 UTC | 2026-07-25 05:37 UTC | 38m |
| ETD80 | Etihad Airways | Malpensa International Airport (LIMC) | OM10 (OM10) | 2026-07-25 00:18 UTC | 2026-07-25 05:36 UTC | 5h 17m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-25 05:08 UTC | 2026-07-25 05:33 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
