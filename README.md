# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_03:21:49_UTC-green)

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

**Latest saved flight:** 2026-07-26 03:21:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 03:21:49 UTC

- **151,567** saved flights
- **50,351** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,567** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,812,728.6 tonnes** estimated CO2 emissions
- **105,085,718 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6112 |
| 2 | SkyWest Airlines | 5554 |
| 3 | EJA | 3000 |
| 4 | IndiGo | 2703 |
| 5 | American Airlines | 2410 |
| 6 | Southwest Airlines | 2310 |
| 7 | ENY | 1895 |
| 8 | Delta Air Lines | 1781 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1404 |
| 11 | AZU | 1317 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1271 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1083 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 987 |
| 18 | All Nippon Airways | 957 |
| 19 | Alaska Airlines | 948 |
| 20 | QLK | 935 |
| 21 | EJU | 928 |
| 22 | VIV | 835 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 795 |
| 26 | JetBlue | 790 |
| 27 | Air France | 788 |
| 28 | GLO | 788 |
| 29 | United Airlines | 783 |
| 30 | Cathay Pacific | 781 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130844 |
| 2 | 🇪🇸 ES | 9789 |
| 3 | 🇧🇷 BR | 8595 |
| 4 | 🇦🇺 AU | 8541 |
| 5 | 🇮🇳 IN | 8503 |
| 6 | 🇨🇦 CA | 8091 |
| 7 | 🇮🇹 IT | 7838 |
| 8 | 🇩🇪 DE | 7758 |
| 9 | 🇬🇧 GB | 6942 |
| 10 | 🇯🇵 JP | 6276 |
| 11 | 🇫🇷 FR | 5990 |
| 12 | 🇨🇴 CO | 5170 |
| 13 | 🇲🇽 MX | 4373 |
| 14 | 🇬🇷 GR | 4299 |
| 15 | 🇳🇴 NO | 4002 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3595 |
| 18 | 🇲🇾 MY | 2823 |
| 19 | 🇵🇱 PL | 2569 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2287 |
| 22 | 🇹🇭 TH | 2199 |
| 23 | 🇰🇷 KR | 2072 |
| 24 | 🇵🇭 PH | 2015 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1544 |
| 27 | 🇲🇪 ME | 1481 |
| 28 | 🇳🇱 NL | 1395 |
| 29 | 🇭🇷 HR | 1386 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3127 |
| 2 | Denver International Airport |  | US | 2547 |
| 3 | Tokyo International Airport |  | JP | 2000 |
| 4 | Guaymaral Airport |  | CO | 1906 |
| 5 | Indira Gandhi International Airport |  | IN | 1885 |
| 6 | Harry Reid International Airport |  | US | 1873 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1695 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1587 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1430 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1420 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | El Dorado International Airport |  | CO | 1368 |
| 15 | Salt Lake City International Airport |  | US | 1365 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1294 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1229 |
| 19 | Madrid Barajas International Airport |  | ES | 1208 |
| 20 | Capua Airport |  | IT | 1205 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1174 |
| 22 | Kuala Lumpur International Airport |  | MY | 1086 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1084 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1069 |
| 26 | Charles de Gaulle International Airport |  | FR | 1039 |
| 27 | Bengaluru International Airport |  | IN | 1017 |
| 28 | Malpensa International Airport |  | IT | 993 |
| 29 | Ninoy Aquino International Airport |  | PH | 944 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 917 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 909 |
| 32 | Barcelona International Airport |  | ES | 906 |
| 33 | Daniel K Inouye International Airport |  | US | 905 |
| 34 | Seattle-Tacoma International Airport |  | US | 875 |
| 35 | Tenerife Norte Airport |  | ES | 872 |
| 36 | Calgary International Airport |  | CA | 862 |
| 37 | Viracopos International Airport |  | BR | 857 |
| 38 | Scottsdale Airport |  | US | 854 |
| 39 | Amsterdam Airport Schiphol |  | NL | 838 |
| 40 | Oslo Gardermoen Airport |  | NO | 830 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 804 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 549 | 21m | 244 km | 2,311.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 366 | 24m | 225 km | 1,419.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 184 | 30m | 49 km | 155.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 171 | 1h 39m | 1,156 km | 3,411.4 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 168 | 51m | 556 km | 1,610.4 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NOE | NOE | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-07-26 03:11 UTC | 2026-07-26 03:21 UTC | 10m |
| N1936T |  | Reading Regional/Carl A Spaatz Field (KRDG) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-26 02:41 UTC | 2026-07-26 03:19 UTC | 37m |
| PGT652 | PGT | Mohammed V International Airport (GMMN) | Kutahya Airport (LTBN) | 2026-07-25 23:14 UTC | 2026-07-26 03:18 UTC | 4h 4m |
| N677F |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-26 02:48 UTC | 2026-07-26 03:17 UTC | 28m |
| SXS6N | SXS | Gaziemir Airport (LTBK) | Sivrihisar Airport (LTAV) | 2026-07-26 02:49 UTC | 2026-07-26 03:17 UTC | 27m |
| THY164 | Turkish Airlines | Istanbul Airport (LTFM) | Cengiz Topel Airport (LTBQ) | 2026-07-26 03:01 UTC | 2026-07-26 03:17 UTC | 15m |
| 01172065 |  | Dimmit County Airport (KCZT) | Hughes Ranch Airport (50XS) | 2026-07-26 01:44 UTC | 2026-07-26 03:06 UTC | 1h 22m |
| N677TX |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-26 02:26 UTC | 2026-07-26 03:02 UTC | 35m |
| AAL3272 | American Airlines | Tampa International Airport (KTPA) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-26 00:51 UTC | 2026-07-26 02:59 UTC | 2h 7m |
| CCPHM | CCP | Comodoro Arturo Merino Benitez International Airport (SCEL) | Contao Airport (SCCK) | 2026-07-26 00:26 UTC | 2026-07-26 02:55 UTC | 2h 28m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-07-26 02:28 UTC | 2026-07-26 02:54 UTC | 26m |
| N999PR |  | K36U (K36U) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-26 01:17 UTC | 2026-07-26 02:53 UTC | 1h 35m |
| RXA6123 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-07-26 02:07 UTC | 2026-07-26 02:51 UTC | 44m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-07-26 02:47 UTC | 2026-07-26 02:51 UTC | 3m |
| LR8154 |  | Brisbane International Airport (YBBN) | Woodville Airport (YWVL) | 2026-07-26 02:01 UTC | 2026-07-26 02:49 UTC | 47m |
|  |  | Yangon International Airport (VYYY) | Taungoo Airport (VYTO) | 2026-07-26 02:09 UTC | 2026-07-26 02:48 UTC | 39m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-07-26 02:31 UTC | 2026-07-26 02:47 UTC | 16m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-07-26 02:34 UTC | 2026-07-26 02:46 UTC | 11m |
| N711SR |  | Salt Lake City International Airport (KSLC) | Wendover Airport (KENV) | 2026-07-26 02:16 UTC | 2026-07-26 02:44 UTC | 27m |
| EOV | EOV | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-07-26 02:35 UTC | 2026-07-26 02:43 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
