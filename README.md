# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_06:04:02_UTC-green)

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

**Latest saved flight:** 2026-08-02 06:04:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 06:04:02 UTC

- **166,033** saved flights
- **54,429** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,033** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,998,122.6 tonnes** estimated CO2 emissions
- **115,833,196 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6623 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2921 |
| 5 | American Airlines | 2623 |
| 6 | Southwest Airlines | 2614 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1985 |
| 9 | LATAM Airlines | 1547 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1455 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1368 |
| 14 | LXJ | 1289 |
| 15 | AXM | 1145 |
| 16 | Swiss International | 1134 |
| 17 | easyJet | 1093 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1016 |
| 20 | QLK | 1016 |
| 21 | All Nippon Airways | 1011 |
| 22 | VIV | 916 |
| 23 | CXK | 886 |
| 24 | Cathay Pacific | 885 |
| 25 | United Airlines | 877 |
| 26 | AEE | 873 |
| 27 | GLO | 869 |
| 28 | MXY | 857 |
| 29 | Air France | 855 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143410 |
| 2 | 🇪🇸 ES | 10599 |
| 3 | 🇧🇷 BR | 9450 |
| 4 | 🇦🇺 AU | 9308 |
| 5 | 🇮🇳 IN | 9162 |
| 6 | 🇨🇦 CA | 9022 |
| 7 | 🇮🇹 IT | 8571 |
| 8 | 🇩🇪 DE | 8292 |
| 9 | 🇬🇧 GB | 7633 |
| 10 | 🇯🇵 JP | 6701 |
| 11 | 🇫🇷 FR | 6566 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4801 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4355 |
| 16 | 🇳🇴 NO | 4343 |
| 17 | 🇹🇷 TR | 3990 |
| 18 | 🇲🇾 MY | 2983 |
| 19 | 🇵🇱 PL | 2809 |
| 20 | 🇿🇦 ZA | 2701 |
| 21 | 🇳🇿 NZ | 2426 |
| 22 | 🇹🇭 TH | 2385 |
| 23 | 🇵🇭 PH | 2194 |
| 24 | 🇬🇹 GT | 2141 |
| 25 | 🇰🇷 KR | 2141 |
| 26 | 🇲🇦 MA | 1671 |
| 27 | 🇭🇷 HR | 1577 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1502 |
| 30 | 🇲🇴 MO | 1415 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3399 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2105 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2031 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1825 |
| 8 | Zurich Airport |  | CH | 1760 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1745 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1502 |
| 14 | Chicago O'Hare International Airport |  | US | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1415 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1307 |
| 20 | Capua Airport |  | IT | 1298 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1173 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1172 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1131 |
| 26 | Kuala Lumpur International Airport |  | MY | 1130 |
| 27 | Malpensa International Airport |  | IT | 1110 |
| 28 | Bengaluru International Airport |  | IN | 1084 |
| 29 | Ninoy Aquino International Airport |  | PH | 1031 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 979 |
| 33 | Daniel K Inouye International Airport |  | US | 970 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 941 |
| 37 | Scottsdale Airport |  | US | 926 |
| 38 | Tenerife Norte Airport |  | ES | 923 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 399 | 24m | 225 km | 1,547.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 378 | 1h 9m | 770 km | 5,021.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 311 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 291 | 1h 7m | 706 km | 3,542.9 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 218 | 20m | 250 km | 941.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 195 | 19m | 144 km | 485.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 179 | 24m | 218 km | 674.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL310 | United Airlines | Washington Dulles International Airport (KIAD) | Dublin Airport (EIDW) | 2026-08-01 23:31 UTC | 2026-08-02 06:04 UTC | 6h 32m |
| LCE | LCE | Kalgoorlie-Boulder Airport (YPKG) | Kalgoorlie-Boulder Airport (YPKG) | 2026-08-02 05:06 UTC | 2026-08-02 05:51 UTC | 44m |
|  |  | Krosno Airport (EPKR) | Radom-Piastrow Glider Airport (EPRP) | 2026-08-02 05:19 UTC | 2026-08-02 05:35 UTC | 15m |
| ZUMTS | ZUM | Grand Central Airport (FAGC) | Grand Central Airport (FAGC) | 2026-08-02 05:04 UTC | 2026-08-02 05:29 UTC | 25m |
| A7GQE |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-08-02 04:38 UTC | 2026-08-02 05:27 UTC | 48m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-08-02 04:30 UTC | 2026-08-02 05:23 UTC | 53m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-08-02 04:54 UTC | 2026-08-02 05:22 UTC | 27m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-08-02 05:11 UTC | 2026-08-02 05:20 UTC | 9m |
| N3NJ |  | Eagles Nest Airport (K31E) | NJ58 (NJ58) | 2026-08-02 05:07 UTC | 2026-08-02 05:19 UTC | 12m |
| THA632 | Thai Airways | Suvarnabhumi Airport (VTBS) | Hsinchu Air Base (RCPO) | 2026-08-02 02:16 UTC | 2026-08-02 05:18 UTC | 3h 2m |
| ROT601A | ROT | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-08-02 04:33 UTC | 2026-08-02 05:18 UTC | 44m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-02 04:33 UTC | 2026-08-02 05:14 UTC | 40m |
| SJX847 | SJX | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-01 23:35 UTC | 2026-08-02 05:13 UTC | 5h 37m |
| JST656 | JST | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 2026-08-02 03:54 UTC | 2026-08-02 05:11 UTC | 1h 16m |
| AWA473 | AWA | VGZR (VGZR) | Paro Airport (VQPR) | 2026-08-02 04:30 UTC | 2026-08-02 05:11 UTC | 40m |
| RYR95YC | Ryanair | Memmingen Allgau Airport (EDJA) | Capua Airport (LIAU) | 2026-08-02 04:06 UTC | 2026-08-02 05:09 UTC | 1h 2m |
| RYR32RL | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Palermo / Bocca Di Falco Airport (LICP) | 2026-08-02 04:18 UTC | 2026-08-02 05:08 UTC | 49m |
| SJX835 | SJX | Kobe Airport (RJBE) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-02 02:54 UTC | 2026-08-02 05:06 UTC | 2h 12m |
| OAL090 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiathos Island National Airport (LGSK) | 2026-08-02 04:44 UTC | 2026-08-02 05:05 UTC | 20m |
| IBS1693 | IBS | Madrid Barajas International Airport (LEMD) | Ibiza Airport (LEIB) | 2026-08-02 04:21 UTC | 2026-08-02 05:05 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
