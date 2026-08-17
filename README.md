# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_02:31:15_UTC-green)

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

**Latest saved flight:** 2026-08-17 02:31:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 02:31:15 UTC

- **206,867** saved flights
- **65,920** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,867** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,487,712.4 tonnes** estimated CO2 emissions
- **144,215,214 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8147 |
| 2 | SkyWest Airlines | 7459 |
| 3 | EJA | 4035 |
| 4 | IndiGo | 3524 |
| 5 | American Airlines | 3452 |
| 6 | Southwest Airlines | 3325 |
| 7 | Delta Air Lines | 2663 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1641 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1344 |
| 18 | United Airlines | 1304 |
| 19 | Alaska Airlines | 1283 |
| 20 | QLK | 1269 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1249 |
| 23 | VIV | 1141 |
| 24 | GLO | 1121 |
| 25 | Air France | 1103 |
| 26 | PGT | 1103 |
| 27 | JetBlue | 1061 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175954 |
| 2 | 🇪🇸 ES | 13186 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11565 |
| 5 | 🇨🇦 CA | 11446 |
| 6 | 🇮🇳 IN | 11000 |
| 7 | 🇮🇹 IT | 10768 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9629 |
| 10 | 🇯🇵 JP | 8485 |
| 11 | 🇨🇴 CO | 8240 |
| 12 | 🇫🇷 FR | 8167 |
| 13 | 🇬🇷 GR | 6071 |
| 14 | 🇹🇷 TR | 5861 |
| 15 | 🇲🇽 MX | 5830 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3541 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3404 |
| 21 | 🇹🇭 TH | 3256 |
| 22 | 🇳🇿 NZ | 2865 |
| 23 | 🇵🇭 PH | 2743 |
| 24 | 🇬🇹 GT | 2647 |
| 25 | 🇰🇷 KR | 2515 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2082 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1743 |
| 30 | 🇮🇩 ID | 1695 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4364 |
| 2 | Denver International Airport |  | US | 3392 |
| 3 | Tokyo International Airport |  | JP | 2558 |
| 4 | Guaymaral Airport |  | CO | 2495 |
| 5 | Indira Gandhi International Airport |  | IN | 2495 |
| 6 | Harry Reid International Airport |  | US | 2340 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2152 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2149 |
| 10 | La Aurora Airport |  | GT | 2016 |
| 11 | Chicago O'Hare International Airport |  | US | 1918 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1852 |
| 14 | Salt Lake City International Airport |  | US | 1835 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1577 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1573 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1446 |
| 24 | Malpensa International Airport |  | IT | 1425 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1412 |
| 27 | Kuala Lumpur International Airport |  | MY | 1312 |
| 28 | Ninoy Aquino International Airport |  | PH | 1300 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1277 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1255 |
| 32 | Seattle-Tacoma International Airport |  | US | 1234 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1173 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Daniel K Inouye International Airport |  | US | 1106 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 732 | 21m | 244 km | 3,082.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 503 | 1h 7m | 770 km | 6,682.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 481 | 24m | 225 km | 1,866.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 256 | 19m | 99 km | 438.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 236 | 31m | 369 km | 1,502.2 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N969S |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-17 02:03 UTC | 2026-08-17 02:31 UTC | 28m |
| N73063 |  | Corvallis Municipal Airport (KCVO) | Independence State Airport (K7S5) | 2026-08-17 01:45 UTC | 2026-08-17 02:27 UTC | 41m |
| N1308T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-17 00:04 UTC | 2026-08-17 02:24 UTC | 2h 20m |
| OXG | OXG | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 02:09 UTC | 2026-08-17 02:23 UTC | 13m |
| DXG | DXG | Lilydale Airport (YLIL) | Melbourne Moorabbin Airport (YMMB) | 2026-08-17 02:03 UTC | 2026-08-17 02:16 UTC | 12m |
| CAP440 | CAP | Fullerton Municipal Airport (KFUL) | Riverside Airport (KRAL) | 2026-08-17 01:22 UTC | 2026-08-17 01:55 UTC | 32m |
| N420FJ |  | Monterey Regional Airport (KMRY) | Telluride Regional Airport (KTEX) | 2026-08-16 23:35 UTC | 2026-08-17 01:51 UTC | 2h 16m |
| SUB8902 | SUB | Rickenbacker International Airport (KLCK) | Northeast Philadelphia Airport (KPNE) | 2026-08-17 00:23 UTC | 2026-08-17 01:51 UTC | 1h 27m |
| LJY286 | LJY | Salt Lake City International Airport (KSLC) | Lehigh Valley International Airport (KABE) | 2026-08-16 22:14 UTC | 2026-08-17 01:47 UTC | 3h 32m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-17 00:47 UTC | 2026-08-17 01:45 UTC | 58m |
| XSN82 | XSN | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-08-17 01:09 UTC | 2026-08-17 01:42 UTC | 32m |
| TKR910 | TKR | Rogue Valley International/Medford Airport (KMFR) | Chiloquin State Airport (K2S7) | 2026-08-17 01:31 UTC | 2026-08-17 01:41 UTC | 9m |
| CPA488 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-17 00:21 UTC | 2026-08-17 01:39 UTC | 1h 18m |
| ZMP | ZMP | Perth Jandakot Airport (YPJT) | Perenjori Airport (YPJI) | 2026-08-17 00:35 UTC | 2026-08-17 01:39 UTC | 1h 3m |
| AAY45 | AAY | Harry Reid International Airport (KLAS) | Wabash Municipal Airport (KIWH) | 2026-08-16 22:31 UTC | 2026-08-17 01:37 UTC | 3h 6m |
| VT164QR |  | Faa'a International Airport (NTAA) | Kaukura Airport (NTGK) | 2026-08-17 00:56 UTC | 2026-08-17 01:36 UTC | 39m |
| SGE | SGE | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 01:24 UTC | 2026-08-17 01:36 UTC | 11m |
| QLK1971 | QLK | Brisbane International Airport (YBBN) | Albury Airport (YMAY) | 2026-08-16 23:53 UTC | 2026-08-17 01:35 UTC | 1h 42m |
| WEN3404 | WEN | Edmonton International Airport (CYEG) | Moose Jaw Municipal Airport (CJS4) | 2026-08-17 00:29 UTC | 2026-08-17 01:33 UTC | 1h 4m |
| AAL2602 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Denver International Airport (KDEN) | 2026-08-17 00:12 UTC | 2026-08-17 01:33 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
