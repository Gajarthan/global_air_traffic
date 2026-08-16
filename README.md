# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_06:37:59_UTC-green)

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

**Latest saved flight:** 2026-08-16 06:37:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 06:37:59 UTC

- **203,651** saved flights
- **65,200** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,651** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,447,399.7 tonnes** estimated CO2 emissions
- **141,878,245 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7996 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3955 |
| 4 | IndiGo | 3469 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2611 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1836 |
| 11 | Lufthansa | 1724 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1397 |
| 16 | Swiss International | 1352 |
| 17 | AXM | 1318 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1251 |
| 21 | EJU | 1242 |
| 22 | All Nippon Airways | 1236 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | PGT | 1080 |
| 26 | Air France | 1077 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1036 |
| 29 | CXK | 1011 |
| 30 | WMT | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173767 |
| 2 | 🇪🇸 ES | 12993 |
| 3 | 🇧🇷 BR | 11644 |
| 4 | 🇦🇺 AU | 11421 |
| 5 | 🇨🇦 CA | 11274 |
| 6 | 🇮🇳 IN | 10835 |
| 7 | 🇮🇹 IT | 10530 |
| 8 | 🇩🇪 DE | 10020 |
| 9 | 🇬🇧 GB | 9463 |
| 10 | 🇯🇵 JP | 8349 |
| 11 | 🇨🇴 CO | 8044 |
| 12 | 🇫🇷 FR | 8037 |
| 13 | 🇬🇷 GR | 5965 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5680 |
| 16 | 🇨🇭 CH | 5421 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3464 |
| 19 | 🇿🇦 ZA | 3380 |
| 20 | 🇵🇱 PL | 3335 |
| 21 | 🇹🇭 TH | 3194 |
| 22 | 🇳🇿 NZ | 2833 |
| 23 | 🇵🇭 PH | 2693 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2486 |
| 26 | 🇭🇷 HR | 2140 |
| 27 | 🇲🇦 MA | 2038 |
| 28 | 🇳🇱 NL | 1801 |
| 29 | 🇲🇪 ME | 1689 |
| 30 | 🇮🇩 ID | 1665 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2525 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2462 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2125 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2110 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1860 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1826 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1687 |
| 17 | Madrid Barajas International Airport |  | ES | 1586 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Macau International Airport |  | MO | 1541 |
| 21 | Capua Airport |  | IT | 1539 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1430 |
| 24 | Malpensa International Airport |  | IT | 1399 |
| 25 | Charlotte/Douglas International Airport |  | US | 1391 |
| 26 | Charles de Gaulle International Airport |  | FR | 1387 |
| 27 | Kuala Lumpur International Airport |  | MY | 1288 |
| 28 | Ninoy Aquino International Airport |  | PH | 1274 |
| 29 | Bengaluru International Airport |  | IN | 1264 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1231 |
| 32 | Barcelona International Airport |  | ES | 1214 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 492 | 1h 7m | 770 km | 6,535.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 472 | 24m | 225 km | 1,831.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 293 | 1h 49m | 1,423 km | 7,190.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 229 | 31m | 369 km | 1,457.6 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH207 | Lufthansa | Berlin Brandenburg Airport (EDDB) | Frankfurt am Main International Airport (EDDF) | 2026-08-16 05:41 UTC | 2026-08-16 06:37 UTC | 56m |
| MRS0915 | MRS | Ifrane Airport (GMFI) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-16 04:46 UTC | 2026-08-16 06:33 UTC | 1h 47m |
| CRUSH51 | CRU | Grant County International Airport (KMWH) | Hanson Airport (0MT6) | 2026-08-16 05:53 UTC | 2026-08-16 06:32 UTC | 38m |
| BBC388 | BBC | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-16 05:27 UTC | 2026-08-16 06:25 UTC | 58m |
| NVP | NVP | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-16 05:51 UTC | 2026-08-16 06:18 UTC | 27m |
| CHX25 | CHX | Hunsborn Airport (EDKH) | Hunsborn Airport (EDKH) | 2026-08-16 06:04 UTC | 2026-08-16 06:09 UTC | 5m |
| MJO | MJO | Tangalooma Resort Airport (YXTA) | Brisbane International Airport (YBBN) | 2026-08-16 05:49 UTC | 2026-08-16 06:05 UTC | 15m |
| N613PA |  | Indianola Municipal Airport (KIDL) | Cleveland Municipal Airport (KRNV) | 2026-08-16 05:53 UTC | 2026-08-16 06:01 UTC | 7m |
| RGA08 | RGA | Buochs Airport (LSZC) | Kagiswil Airport (LSPG) | 2026-08-16 05:55 UTC | 2026-08-16 06:01 UTC | 6m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-08-16 05:27 UTC | 2026-08-16 06:00 UTC | 33m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Xieng Khouang Airport (VLXK) | 2026-08-16 05:13 UTC | 2026-08-16 06:00 UTC | 47m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | EDVT (EDVT) | 2026-08-16 05:08 UTC | 2026-08-16 05:57 UTC | 49m |
| FJLPR | FJL | Propriano Airport (LFKO) | Figari Sud-Corse Airport (LFKF) | 2026-08-16 05:50 UTC | 2026-08-16 05:56 UTC | 6m |
| WZZ84AY | Wizz Air | Katowice International Airport (EPKT) | Allendorf/Eder Airport (EDFQ) | 2026-08-16 04:16 UTC | 2026-08-16 05:54 UTC | 1h 37m |
| RYR40HE | Ryanair | Torino / Caselle International Airport (LIMF) | Oristano / Fenosu Airport (LIER) | 2026-08-16 04:03 UTC | 2026-08-16 05:53 UTC | 1h 50m |
| RYR57GB | Ryanair | Madrid Barajas International Airport (LEMD) | London Luton Airport (EGGW) | 2026-08-16 03:58 UTC | 2026-08-16 05:53 UTC | 1h 55m |
| DAL8958 | Delta Air Lines | Washington Dulles International Airport (KIAD) | CT32 (CT32) | 2026-08-16 04:41 UTC | 2026-08-16 05:53 UTC | 1h 11m |
| VAR527 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-16 04:57 UTC | 2026-08-16 05:50 UTC | 53m |
| SFR354 | SFR | Lanseria Airport (FALA) | Harrismith Airport (FAHR) | 2026-08-16 04:39 UTC | 2026-08-16 05:50 UTC | 1h 10m |
| ANA536 | All Nippon Airways | Takamatsu Airport (RJOT) | Tateyama Airport (RJTE) | 2026-08-16 04:47 UTC | 2026-08-16 05:50 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
