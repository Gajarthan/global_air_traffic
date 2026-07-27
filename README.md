# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_03:35:49_UTC-green)

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

**Latest saved flight:** 2026-07-27 03:35:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 03:35:49 UTC

- **154,190** saved flights
- **51,411** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,190** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,847,932.4 tonnes** estimated CO2 emissions
- **107,126,518 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6203 |
| 2 | SkyWest Airlines | 5660 |
| 3 | EJA | 3055 |
| 4 | IndiGo | 2735 |
| 5 | American Airlines | 2466 |
| 6 | Southwest Airlines | 2428 |
| 7 | ENY | 1932 |
| 8 | Delta Air Lines | 1838 |
| 9 | Lufthansa | 1491 |
| 10 | LATAM Airlines | 1434 |
| 11 | AZU | 1341 |
| 12 | WIF | 1290 |
| 13 | Vueling | 1282 |
| 14 | LXJ | 1189 |
| 15 | AXM | 1094 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 1004 |
| 18 | Alaska Airlines | 969 |
| 19 | All Nippon Airways | 963 |
| 20 | QLK | 961 |
| 21 | EJU | 943 |
| 22 | VIV | 849 |
| 23 | United Airlines | 830 |
| 24 | CXK | 820 |
| 25 | MXY | 810 |
| 26 | AEE | 807 |
| 27 | JetBlue | 806 |
| 28 | GLO | 805 |
| 29 | Air France | 798 |
| 30 | Cathay Pacific | 787 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133253 |
| 2 | 🇪🇸 ES | 9922 |
| 3 | 🇧🇷 BR | 8768 |
| 4 | 🇦🇺 AU | 8739 |
| 5 | 🇮🇳 IN | 8599 |
| 6 | 🇨🇦 CA | 8300 |
| 7 | 🇮🇹 IT | 7949 |
| 8 | 🇩🇪 DE | 7833 |
| 9 | 🇬🇧 GB | 7044 |
| 10 | 🇯🇵 JP | 6352 |
| 11 | 🇫🇷 FR | 6078 |
| 12 | 🇨🇴 CO | 5279 |
| 13 | 🇲🇽 MX | 4440 |
| 14 | 🇬🇷 GR | 4381 |
| 15 | 🇳🇴 NO | 4051 |
| 16 | 🇨🇭 CH | 4024 |
| 17 | 🇹🇷 TR | 3675 |
| 18 | 🇲🇾 MY | 2851 |
| 19 | 🇵🇱 PL | 2628 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2226 |
| 23 | 🇰🇷 KR | 2085 |
| 24 | 🇵🇭 PH | 2033 |
| 25 | 🇬🇹 GT | 1999 |
| 26 | 🇲🇦 MA | 1570 |
| 27 | 🇲🇪 ME | 1496 |
| 28 | 🇭🇷 HR | 1410 |
| 29 | 🇳🇱 NL | 1407 |
| 30 | 🇲🇴 MO | 1255 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3175 |
| 2 | Denver International Airport |  | US | 2594 |
| 3 | Tokyo International Airport |  | JP | 2012 |
| 4 | Guaymaral Airport |  | CO | 1928 |
| 5 | Indira Gandhi International Airport |  | IN | 1907 |
| 6 | Harry Reid International Airport |  | US | 1898 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1717 |
| 8 | Zurich Airport |  | CH | 1668 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1616 |
| 10 | La Aurora Airport |  | GT | 1550 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1441 |
| 12 | Frankfurt am Main International Airport |  | DE | 1439 |
| 13 | Chicago O'Hare International Airport |  | US | 1418 |
| 14 | Salt Lake City International Airport |  | US | 1395 |
| 15 | El Dorado International Airport |  | CO | 1389 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1312 |
| 17 | Macau International Airport |  | MO | 1255 |
| 18 | Congonhas Airport |  | BR | 1250 |
| 19 | Madrid Barajas International Airport |  | ES | 1225 |
| 20 | Capua Airport |  | IT | 1215 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1189 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1113 |
| 23 | Charlotte/Douglas International Airport |  | US | 1103 |
| 24 | Kuala Lumpur International Airport |  | MY | 1094 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1093 |
| 26 | Charles de Gaulle International Airport |  | FR | 1053 |
| 27 | Bengaluru International Airport |  | IN | 1028 |
| 28 | Malpensa International Airport |  | IT | 1004 |
| 29 | Ninoy Aquino International Airport |  | PH | 952 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 934 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 32 | Barcelona International Airport |  | ES | 916 |
| 33 | Daniel K Inouye International Airport |  | US | 915 |
| 34 | Seattle-Tacoma International Airport |  | US | 900 |
| 35 | Tenerife Norte Airport |  | ES | 883 |
| 36 | Calgary International Airport |  | CA | 882 |
| 37 | Viracopos International Airport |  | BR | 874 |
| 38 | Scottsdale Airport |  | US | 873 |
| 39 | Amsterdam Airport Schiphol |  | NL | 848 |
| 40 | Oslo Gardermoen Airport |  | NO | 841 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 556 | 21m | 244 km | 2,341.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 282 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 208 | 44m | 241 km | 864.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 179 | 31m | 369 km | 1,139.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N579WA |  | Sierraville Dearwater Airport (KO79) | Napa County Airport (KAPC) | 2026-07-26 22:49 UTC | 2026-07-27 03:35 UTC | 4h 46m |
| N294DL |  | Van Nuys Airport (KVNY) | 88MN (88MN) | 2026-07-27 00:26 UTC | 2026-07-27 03:29 UTC | 3h 2m |
| NVD | NVD | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-07-27 03:13 UTC | 2026-07-27 03:27 UTC | 13m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-07-27 02:52 UTC | 2026-07-27 03:24 UTC | 32m |
| AAY3043 | AAY | Mc Ghee Tyson Airport (KTYS) | Martin Campbell Field (K1A3) | 2026-07-26 23:31 UTC | 2026-07-27 03:22 UTC | 3h 51m |
| ACA486 | Air Canada | Toronto Pearson International Airport (CYYZ) | Cornwall Regional Airport (CYCC) | 2026-07-27 01:44 UTC | 2026-07-27 03:21 UTC | 1h 37m |
| QLK437D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Adaminaby Airport (YADI) | 2026-07-27 02:47 UTC | 2026-07-27 03:21 UTC | 33m |
| SWA1311 | Southwest Airlines | Harry Reid International Airport (KLAS) | TA03 (TA03) | 2026-07-26 21:50 UTC | 2026-07-27 03:20 UTC | 5h 29m |
| SWA3334 | Southwest Airlines | Buckeye Municipal Airport (KBXK) | 02CL (02CL) | 2026-07-27 00:17 UTC | 2026-07-27 03:19 UTC | 3h 2m |
| JSX121 | JSX | Henderson Executive Airport (KHND) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-27 00:28 UTC | 2026-07-27 03:18 UTC | 2h 49m |
| QLK623D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-27 02:32 UTC | 2026-07-27 03:18 UTC | 45m |
| QLK28D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wallabadah Airport (YWBH) | 2026-07-26 23:20 UTC | 2026-07-27 03:17 UTC | 3h 56m |
| SWA1162 | Southwest Airlines | Norman Y Mineta San Jose International Airport (KSJC) | Sacramento International Airport (KSMF) | 2026-07-26 23:48 UTC | 2026-07-27 03:17 UTC | 3h 29m |
| N100BW |  | Talkeetna Airport (PATK) | Mc Kinley Country Airport (81AK) | 2026-07-27 02:35 UTC | 2026-07-27 03:17 UTC | 42m |
| RXA3873 | RXA | Melbourne International Airport (YMML) | Lethbridge Park Airport (YLED) | 2026-07-27 02:41 UTC | 2026-07-27 03:16 UTC | 34m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-27 02:34 UTC | 2026-07-27 03:15 UTC | 40m |
| AAL1192 | American Airlines | Cancun International Airport (MMUN) | VA16 (VA16) | 2026-07-26 21:14 UTC | 2026-07-27 03:14 UTC | 5h 59m |
| FIN100 | Finnair | Chek Lap Kok International Airport (VHHH) | Helsinki Vantaa Airport (EFHK) | 2026-07-26 14:36 UTC | 2026-07-27 03:14 UTC | 12h 37m |
| HKE600 | HKE | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-07-27 00:20 UTC | 2026-07-27 03:13 UTC | 2h 53m |
| RXA6824 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-07-26 22:56 UTC | 2026-07-27 03:12 UTC | 4h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
