# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_10:46:20_UTC-green)

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

**Latest saved flight:** 2026-08-17 10:46:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 10:46:20 UTC

- **207,632** saved flights
- **66,033** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,632** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,497,239.8 tonnes** estimated CO2 emissions
- **144,767,527 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8193 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3553 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2667 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1876 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1723 |
| 13 | WIF | 1670 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1434 |
| 16 | Swiss International | 1381 |
| 17 | AXM | 1359 |
| 18 | United Airlines | 1306 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1267 |
| 22 | All Nippon Airways | 1263 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | Air France | 1112 |
| 26 | PGT | 1111 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1060 |
| 29 | WMT | 1051 |
| 30 | Wizz Air | 1023 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176068 |
| 2 | 🇪🇸 ES | 13251 |
| 3 | 🇧🇷 BR | 11883 |
| 4 | 🇦🇺 AU | 11728 |
| 5 | 🇨🇦 CA | 11463 |
| 6 | 🇮🇳 IN | 11076 |
| 7 | 🇮🇹 IT | 10838 |
| 8 | 🇩🇪 DE | 10258 |
| 9 | 🇬🇧 GB | 9663 |
| 10 | 🇯🇵 JP | 8613 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8218 |
| 13 | 🇬🇷 GR | 6111 |
| 14 | 🇹🇷 TR | 5893 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5537 |
| 17 | 🇳🇴 NO | 5172 |
| 18 | 🇲🇾 MY | 3583 |
| 19 | 🇿🇦 ZA | 3482 |
| 20 | 🇵🇱 PL | 3417 |
| 21 | 🇹🇭 TH | 3324 |
| 22 | 🇳🇿 NZ | 2890 |
| 23 | 🇵🇭 PH | 2765 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2536 |
| 26 | 🇭🇷 HR | 2224 |
| 27 | 🇲🇦 MA | 2091 |
| 28 | 🇳🇱 NL | 1846 |
| 29 | 🇲🇪 ME | 1759 |
| 30 | 🇮🇩 ID | 1721 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2591 |
| 4 | Indira Gandhi International Airport |  | IN | 2518 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2165 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2163 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1921 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1856 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1712 |
| 17 | Madrid Barajas International Airport |  | ES | 1627 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1572 |
| 21 | Macau International Airport |  | MO | 1544 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1466 |
| 24 | Malpensa International Airport |  | IT | 1437 |
| 25 | Charles de Gaulle International Airport |  | FR | 1424 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1324 |
| 28 | Ninoy Aquino International Airport |  | PH | 1310 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1283 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1238 |
| 33 | Barcelona International Airport |  | ES | 1237 |
| 34 | Viracopos International Airport |  | BR | 1203 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Oslo Gardermoen Airport |  | NO | 1148 |
| 37 | Vitoria/Foronda Airport |  | ES | 1144 |
| 38 | Reno/Tahoe International Airport |  | US | 1143 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1113 |
| 40 | Daniel K Inouye International Airport |  | US | 1110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 511 | 1h 7m | 770 km | 6,788.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 346 | 27m | 275 km | 1,639.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 302 | 1h 49m | 1,423 km | 7,411.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 261 | 24m | 218 km | 983.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 253 | 27m | 215 km | 937.0 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 246 | 1h 37m | 1,156 km | 4,907.6 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EIN952 | Aer Lingus | Seattle-Tacoma International Airport (KSEA) | Dublin Airport (EIDW) | 2026-08-17 02:21 UTC | 2026-08-17 10:46 UTC | 8h 25m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-17 10:06 UTC | 2026-08-17 10:34 UTC | 28m |
| OKACL | OKA | Hodkovice Nad Mohelkou Airport (LKHD) | Nove Mesto Airport (LKNM) | 2026-08-17 09:55 UTC | 2026-08-17 10:34 UTC | 38m |
|  |  | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-17 10:23 UTC | 2026-08-17 10:24 UTC | 0m |
| UAL698 | United Airlines | San Francisco International Airport (KSFO) | Newark Liberty International Airport (KEWR) | 2026-08-17 05:37 UTC | 2026-08-17 10:17 UTC | 4h 39m |
| FHNTS | FHN | Nantes Atlantique Airport (LFRS) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-17 09:34 UTC | 2026-08-17 10:12 UTC | 37m |
| EFC18J | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 09:58 UTC | 2026-08-17 10:11 UTC | 12m |
| UBA208 | UBA | Tachileik Airport (VYTL) | Heho Airport (VYHH) | 2026-08-17 09:13 UTC | 2026-08-17 10:10 UTC | 57m |
| CGBHY | CGB | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-17 08:48 UTC | 2026-08-17 10:09 UTC | 1h 20m |
| N200TG |  | Americana Airport (SDAI) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-08-17 09:23 UTC | 2026-08-17 10:00 UTC | 37m |
| FD258 |  | Woodvale Airport (YWOV) | Pyramid Hill Airport (YPYD) | 2026-08-17 09:50 UTC | 2026-08-17 10:00 UTC | 10m |
| THY3160 | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-17 07:03 UTC | 2026-08-17 09:57 UTC | 2h 53m |
| NATO01 | NAT | Geilenkirchen Airport (ETNG) | Rendsburg-Schachtholm Airport (EDXR) | 2026-08-17 09:00 UTC | 2026-08-17 09:54 UTC | 54m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-17 08:27 UTC | 2026-08-17 09:52 UTC | 1h 25m |
| WZZ1797 | Wizz Air | Dortmund Airport (EDLW) | Trstenik Airport (LYTR) | 2026-08-17 08:09 UTC | 2026-08-17 09:51 UTC | 1h 42m |
| EFC74L | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 09:36 UTC | 2026-08-17 09:49 UTC | 13m |
| VLG9FT | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-08-17 08:55 UTC | 2026-08-17 09:49 UTC | 53m |
| RYR2WH | Ryanair | Toulouse-Blagnac Airport (LFBO) | Ifrane Airport (GMFI) | 2026-08-17 08:16 UTC | 2026-08-17 09:48 UTC | 1h 32m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | Sacheon Air Base (RKPS) | 2026-08-17 09:02 UTC | 2026-08-17 09:47 UTC | 45m |
| GGYTO | GGY | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-08-17 09:27 UTC | 2026-08-17 09:47 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
