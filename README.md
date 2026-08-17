# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_08:31:07_UTC-green)

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

**Latest saved flight:** 2026-08-17 08:31:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 08:31:07 UTC

- **207,396** saved flights
- **65,993** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,396** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,494,032.4 tonnes** estimated CO2 emissions
- **144,581,586 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8181 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3544 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2666 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1755 |
| 12 | Vueling | 1718 |
| 13 | WIF | 1667 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1432 |
| 16 | Swiss International | 1380 |
| 17 | AXM | 1355 |
| 18 | United Airlines | 1304 |
| 19 | QLK | 1291 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1265 |
| 22 | All Nippon Airways | 1260 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | PGT | 1107 |
| 26 | Air France | 1105 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1057 |
| 29 | WMT | 1046 |
| 30 | Wizz Air | 1020 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176059 |
| 2 | 🇪🇸 ES | 13226 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11708 |
| 5 | 🇨🇦 CA | 11459 |
| 6 | 🇮🇳 IN | 11047 |
| 7 | 🇮🇹 IT | 10818 |
| 8 | 🇩🇪 DE | 10239 |
| 9 | 🇬🇧 GB | 9639 |
| 10 | 🇯🇵 JP | 8588 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8190 |
| 13 | 🇬🇷 GR | 6096 |
| 14 | 🇹🇷 TR | 5876 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5530 |
| 17 | 🇳🇴 NO | 5163 |
| 18 | 🇲🇾 MY | 3569 |
| 19 | 🇿🇦 ZA | 3460 |
| 20 | 🇵🇱 PL | 3414 |
| 21 | 🇹🇭 TH | 3303 |
| 22 | 🇳🇿 NZ | 2888 |
| 23 | 🇵🇭 PH | 2763 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2530 |
| 26 | 🇭🇷 HR | 2218 |
| 27 | 🇲🇦 MA | 2086 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1751 |
| 30 | 🇮🇩 ID | 1714 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2583 |
| 4 | Indira Gandhi International Airport |  | IN | 2508 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2162 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2158 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1920 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1856 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1710 |
| 17 | Madrid Barajas International Airport |  | ES | 1625 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1572 |
| 21 | Macau International Airport |  | MO | 1543 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1465 |
| 24 | Malpensa International Airport |  | IT | 1435 |
| 25 | Charles de Gaulle International Airport |  | FR | 1417 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1319 |
| 28 | Ninoy Aquino International Airport |  | PH | 1309 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1281 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1236 |
| 33 | Barcelona International Airport |  | ES | 1236 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Oslo Gardermoen Airport |  | NO | 1144 |
| 37 | Reno/Tahoe International Airport |  | US | 1143 |
| 38 | Vitoria/Foronda Airport |  | ES | 1139 |
| 39 | Daniel K Inouye International Airport |  | US | 1110 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 509 | 1h 7m | 770 km | 6,761.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 485 | 24m | 225 km | 1,881.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 346 | 27m | 275 km | 1,639.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 343 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 304 | 44m | 241 km | 1,262.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 300 | 1h 49m | 1,423 km | 7,362.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 258 | 24m | 218 km | 972.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 252 | 27m | 215 km | 933.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 245 | 1h 37m | 1,156 km | 4,887.7 t |
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
| WPF | WPF | Perth Jandakot Airport (YPJT) | Busselton Regional Airport (YBLN) | 2026-08-17 07:52 UTC | 2026-08-17 08:31 UTC | 38m |
| SBI3034 | SBI | Antalya International Airport (LTAI) | Tunoshna Airport (UUDL) | 2026-08-16 12:31 UTC | 2026-08-17 08:28 UTC | 19h 56m |
| PSDN19 | PSD | Garden Island (Military) Airport (YGAD) | Garden Island (Military) Airport (YGAD) | 2026-08-17 07:33 UTC | 2026-08-17 08:27 UTC | 53m |
| SUI005 | SUI | Lugano Airport (LSZA) | Bern Belp Airport (LSZB) | 2026-08-17 07:53 UTC | 2026-08-17 08:20 UTC | 27m |
| IAM3181 | IAM | Ciampino Airport (LIRA) | Gioia Del Colle Airport (LIBV) | 2026-08-17 07:48 UTC | 2026-08-17 08:19 UTC | 31m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-08-17 07:55 UTC | 2026-08-17 08:11 UTC | 16m |
| SUNDOG1 | SUN | Nordholz Airport (ETMN) | Heubach Airport (EDTH) | 2026-08-17 07:24 UTC | 2026-08-17 08:09 UTC | 45m |
|  |  | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-17 07:14 UTC | 2026-08-17 08:06 UTC | 52m |
| AM320 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-08-17 07:44 UTC | 2026-08-17 08:05 UTC | 21m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-08-17 07:44 UTC | 2026-08-17 08:02 UTC | 17m |
| EZY41VP | easyJet | Isle of Man Airport (EGNS) | Liverpool John Lennon Airport (EGGP) | 2026-08-17 07:37 UTC | 2026-08-17 08:00 UTC | 23m |
| FHNDE | FHN | Bernay St Martin Airport (LFPD) | Rouen Airport (LFOP) | 2026-08-17 07:47 UTC | 2026-08-17 07:58 UTC | 11m |
| TVS68J | TVS | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-08-17 07:29 UTC | 2026-08-17 07:56 UTC | 26m |
| ZSNSA | ZSN | Wonderboom Airport (FAWB) | Carltonville Airport (FACR) | 2026-08-17 07:32 UTC | 2026-08-17 07:55 UTC | 22m |
| RYR80AY | Ryanair | Paris Beauvais Tille Airport (LFOB) | Poznań-Ławica Airport (EPPO) | 2026-08-17 06:25 UTC | 2026-08-17 07:55 UTC | 1h 29m |
| WMT3662 | WMT | Bergamo / Orio Al Serio Airport (LIME) | Sibiu International Airport (LRSB) | 2026-08-17 06:32 UTC | 2026-08-17 07:53 UTC | 1h 21m |
| IHEBZ | IHE | Bolzano Airport (LIPB) | Bolzano Airport (LIPB) | 2026-08-17 07:47 UTC | 2026-08-17 07:53 UTC | 5m |
| IAM3180 | IAM | Ciampino Airport (LIRA) | Gioia Del Colle Airport (LIBV) | 2026-08-17 07:23 UTC | 2026-08-17 07:52 UTC | 28m |
| IBE0671 | Iberia | Madrid Barajas International Airport (LEMD) | Malpensa International Airport (LIMC) | 2026-08-17 05:57 UTC | 2026-08-17 07:50 UTC | 1h 53m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-08-17 06:39 UTC | 2026-08-17 07:48 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
