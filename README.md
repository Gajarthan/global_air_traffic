# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_15:30:00_UTC-green)

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

**Latest saved flight:** 2026-08-12 15:30:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 15:30:00 UTC

- **189,657** saved flights
- **59,936** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,657** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,271,331.2 tonnes** estimated CO2 emissions
- **131,671,374 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7524 |
| 2 | SkyWest Airlines | 6867 |
| 3 | EJA | 3736 |
| 4 | IndiGo | 3302 |
| 5 | Southwest Airlines | 2958 |
| 6 | American Airlines | 2935 |
| 7 | ENY | 2350 |
| 8 | Delta Air Lines | 2225 |
| 9 | LATAM Airlines | 1776 |
| 10 | AZU | 1709 |
| 11 | Lufthansa | 1656 |
| 12 | Vueling | 1574 |
| 13 | WIF | 1574 |
| 14 | LXJ | 1481 |
| 15 | easyJet | 1306 |
| 16 | Swiss International | 1294 |
| 17 | AXM | 1253 |
| 18 | EJU | 1169 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1047 |
| 23 | GLO | 1021 |
| 24 | Air France | 991 |
| 25 | PGT | 977 |
| 26 | AEE | 972 |
| 27 | United Airlines | 972 |
| 28 | CXK | 968 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 941 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161526 |
| 2 | 🇪🇸 ES | 12231 |
| 3 | 🇧🇷 BR | 10899 |
| 4 | 🇦🇺 AU | 10652 |
| 5 | 🇨🇦 CA | 10381 |
| 6 | 🇮🇳 IN | 10351 |
| 7 | 🇮🇹 IT | 9841 |
| 8 | 🇩🇪 DE | 9374 |
| 9 | 🇬🇧 GB | 8833 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7585 |
| 12 | 🇨🇴 CO | 7249 |
| 13 | 🇬🇷 GR | 5555 |
| 14 | 🇲🇽 MX | 5387 |
| 15 | 🇨🇭 CH | 5095 |
| 16 | 🇹🇷 TR | 5040 |
| 17 | 🇳🇴 NO | 4884 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3194 |
| 20 | 🇵🇱 PL | 3141 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2508 |
| 24 | 🇬🇹 GT | 2403 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1937 |
| 27 | 🇲🇦 MA | 1924 |
| 28 | 🇳🇱 NL | 1694 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3930 |
| 2 | Denver International Airport |  | US | 3117 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2338 |
| 5 | Indira Gandhi International Airport |  | IN | 2332 |
| 6 | Harry Reid International Airport |  | US | 2215 |
| 7 | Zurich Airport |  | CH | 2017 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2009 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1959 |
| 10 | La Aurora Airport |  | GT | 1847 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1706 |
| 13 | Salt Lake City International Airport |  | US | 1682 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1623 |
| 16 | Congonhas Airport |  | BR | 1582 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1495 |
| 19 | Capua Airport |  | IT | 1473 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1471 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1400 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1361 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1306 |
| 25 | Charles de Gaulle International Airport |  | FR | 1299 |
| 26 | Charlotte/Douglas International Airport |  | US | 1267 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1222 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1186 |
| 30 | Ninoy Aquino International Airport |  | PH | 1185 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1136 |
| 33 | Viracopos International Airport |  | BR | 1099 |
| 34 | Reno/Tahoe International Airport |  | US | 1094 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1081 |
| 37 | Daniel K Inouye International Airport |  | US | 1065 |
| 38 | Oslo Gardermoen Airport |  | NO | 1060 |
| 39 | Tenerife Norte Airport |  | ES | 1041 |
| 40 | Vitoria/Foronda Airport |  | ES | 1029 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 965 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 693 | 21m | 244 km | 2,918.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 441 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 318 | 27m | 275 km | 1,506.9 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 308 | 14m | 114 km | 604.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 294 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 274 | 22m | 55 km | 260.4 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 272 | 1h 49m | 1,423 km | 6,675.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 253 | 20m | 250 km | 1,092.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 237 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 226 | 19m | 144 km | 562.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 224 | 24m | 218 km | 843.9 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 207 | 1h 48m | 1,304 km | 4,657.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N459MM |  | Cape May County Airport (KWWD) | New Castle Airport (KILG) | 2026-08-12 14:44 UTC | 2026-08-12 15:30 UTC | 45m |
| THA951 | Thai Airways | Copenhagen Kastrup Airport (EKCH) | Gelendzhik Airport (URKG) | 2026-08-12 12:45 UTC | 2026-08-12 15:25 UTC | 2h 40m |
| ASI818 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-12 15:08 UTC | 2026-08-12 15:25 UTC | 17m |
| N88NP |  | South Lakeland Airport (KX49) | Zephyrhills Municipal Airport (KZPH) | 2026-08-12 15:13 UTC | 2026-08-12 15:25 UTC | 11m |
| GKA264 | GKA | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-08-12 15:02 UTC | 2026-08-12 15:24 UTC | 21m |
| LTG8503 | LTG | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-08-12 06:44 UTC | 2026-08-12 15:24 UTC | 8h 39m |
| ENSA87 | ENS | Sitio Sao Jose Airport (SDZZ) | Mirassol Airport (SDMH) | 2026-08-12 15:07 UTC | 2026-08-12 15:24 UTC | 16m |
| TOPCT25 | TOP | Offutt Afb Airport (KOFF) | Mott Municipal Airport (K3P3) | 2026-08-12 14:12 UTC | 2026-08-12 15:21 UTC | 1h 8m |
| BCAT834 | BCA | Newquay Cornwall Airport (EGHQ) | Edinburgh Airport (EGPH) | 2026-08-12 14:05 UTC | 2026-08-12 15:20 UTC | 1h 14m |
| HAWK238 | HAW | Kingsville Nas Airport (KNQI) | Puesta Del Sol Airport (TA44) | 2026-08-12 15:03 UTC | 2026-08-12 15:18 UTC | 14m |
| RGY971 | RGY | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-08-12 14:33 UTC | 2026-08-12 15:16 UTC | 43m |
| AFR93SM | Air France | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-08-12 14:14 UTC | 2026-08-12 15:13 UTC | 58m |
| N106UV |  | Provo Municipal Airport (KPVU) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-12 14:34 UTC | 2026-08-12 15:06 UTC | 31m |
| DSU89 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-08-12 14:19 UTC | 2026-08-12 15:05 UTC | 45m |
| SPGAA | SPG | Jastarnia Airport (EPJA) | Jastarnia Airport (EPJA) | 2026-08-12 15:02 UTC | 2026-08-12 15:02 UTC | 0m |
| N284JA |  | Chester County G O Carlson Airport (KMQS) | York Airport (KTHV) | 2026-08-12 14:32 UTC | 2026-08-12 15:00 UTC | 27m |
| N374BL |  | Market World Airport (FL16) | Winter Haven Regional Airport (KGIF) | 2026-08-12 14:09 UTC | 2026-08-12 14:58 UTC | 49m |
| SLICK92 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-08-12 14:17 UTC | 2026-08-12 14:57 UTC | 40m |
| RTV2N | RTV | Vilar Da Luz Airport (LPVL) | Vila Real Airport (LPVR) | 2026-08-12 13:52 UTC | 2026-08-12 14:57 UTC | 1h 5m |
| N219BH |  | Kissimmee Gateway Airport (KISM) | Stout Airport (FD83) | 2026-08-12 14:39 UTC | 2026-08-12 14:56 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
