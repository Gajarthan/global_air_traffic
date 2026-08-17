# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_01:24:29_UTC-green)

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

**Latest saved flight:** 2026-08-17 01:24:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 01:24:29 UTC

- **206,776** saved flights
- **65,906** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,776** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,486,664.9 tonnes** estimated CO2 emissions
- **144,154,487 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8147 |
| 2 | SkyWest Airlines | 7458 |
| 3 | EJA | 4034 |
| 4 | IndiGo | 3523 |
| 5 | American Airlines | 3449 |
| 6 | Southwest Airlines | 3325 |
| 7 | Delta Air Lines | 2661 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1874 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1641 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1341 |
| 18 | United Airlines | 1304 |
| 19 | Alaska Airlines | 1282 |
| 20 | QLK | 1267 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1247 |
| 23 | VIV | 1139 |
| 24 | GLO | 1121 |
| 25 | Air France | 1103 |
| 26 | PGT | 1102 |
| 27 | JetBlue | 1061 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175892 |
| 2 | 🇪🇸 ES | 13186 |
| 3 | 🇧🇷 BR | 11875 |
| 4 | 🇦🇺 AU | 11542 |
| 5 | 🇨🇦 CA | 11440 |
| 6 | 🇮🇳 IN | 10996 |
| 7 | 🇮🇹 IT | 10768 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9628 |
| 10 | 🇯🇵 JP | 8469 |
| 11 | 🇨🇴 CO | 8236 |
| 12 | 🇫🇷 FR | 8167 |
| 13 | 🇬🇷 GR | 6071 |
| 14 | 🇹🇷 TR | 5859 |
| 15 | 🇲🇽 MX | 5822 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3533 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3404 |
| 21 | 🇹🇭 TH | 3249 |
| 22 | 🇳🇿 NZ | 2862 |
| 23 | 🇵🇭 PH | 2741 |
| 24 | 🇬🇹 GT | 2645 |
| 25 | 🇰🇷 KR | 2510 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2082 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1743 |
| 30 | 🇮🇩 ID | 1688 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4364 |
| 2 | Denver International Airport |  | US | 3390 |
| 3 | Tokyo International Airport |  | JP | 2554 |
| 4 | Indira Gandhi International Airport |  | IN | 2495 |
| 5 | Guaymaral Airport |  | CO | 2494 |
| 6 | Harry Reid International Airport |  | US | 2338 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2152 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2149 |
| 10 | La Aurora Airport |  | GT | 2015 |
| 11 | Chicago O'Hare International Airport |  | US | 1918 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1849 |
| 14 | Salt Lake City International Airport |  | US | 1833 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1577 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1573 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1445 |
| 24 | Malpensa International Airport |  | IT | 1425 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1412 |
| 27 | Kuala Lumpur International Airport |  | MY | 1311 |
| 28 | Ninoy Aquino International Airport |  | PH | 1299 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1282 |
| 30 | Bengaluru International Airport |  | IN | 1276 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1252 |
| 32 | Seattle-Tacoma International Airport |  | US | 1233 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1201 |
| 35 | Calgary International Airport |  | CA | 1173 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Daniel K Inouye International Airport |  | US | 1105 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 731 | 21m | 244 km | 3,078.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 502 | 1h 7m | 770 km | 6,668.7 t |
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
| N9385L |  | North Perry Airport (KHWO) | Belle Glade State Municipal Airport (KX10) | 2026-08-17 00:50 UTC | 2026-08-17 01:24 UTC | 34m |
| N947AF |  | Addison Airport (KADS) | Grove Hill Airport (5TX2) | 2026-08-17 00:47 UTC | 2026-08-17 01:15 UTC | 28m |
| PPD | PPD | Gold Coast Airport (YBCG) | Tamworth Airport (YSTW) | 2026-08-17 00:13 UTC | 2026-08-17 01:14 UTC | 1h 0m |
| N859HW |  | Frederick W Smith International/Memphis Airport (KMEM) | Jonesboro Municipal Airport (KJBR) | 2026-08-17 00:44 UTC | 2026-08-17 01:12 UTC | 27m |
| ZHH | ZHH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-17 00:51 UTC | 2026-08-17 01:11 UTC | 19m |
| YHX | YHX | Warrnambool Airport (YWBL) | Warrnambool Airport (YWBL) | 2026-08-17 00:48 UTC | 2026-08-17 01:00 UTC | 11m |
| HK4907 |  | Rafael Nunez International Airport (SKCG) | Jose Maria Cordova International Airport (SKRG) | 2026-08-17 00:15 UTC | 2026-08-17 00:59 UTC | 43m |
| N1065U |  | Sandridge Airpark Inc Airport (OK94) | 84OL (84OL) | 2026-08-17 00:54 UTC | 2026-08-17 00:58 UTC | 4m |
| EJA816 | EJA | Dallas-Fort Worth International Airport (KDFW) | Moffett Federal Airfield (KNUQ) | 2026-08-16 21:46 UTC | 2026-08-17 00:56 UTC | 3h 9m |
| GPD388 | GPD | Westchester County Airport (KHPN) | Wings Field (KLOM) | 2026-08-17 00:23 UTC | 2026-08-17 00:54 UTC | 31m |
| N738EP |  | Auburn Municipal Airport (KS50) | Wishkah River Ranch Airport (94WA) | 2026-08-17 00:08 UTC | 2026-08-17 00:54 UTC | 45m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-17 00:33 UTC | 2026-08-17 00:47 UTC | 13m |
| N142EB |  | Mc Gregor Executive Airport (KPWG) | 81NM (81NM) | 2026-08-16 23:11 UTC | 2026-08-17 00:45 UTC | 1h 34m |
| EPI783 | EPI | Tucson International Airport (KTUS) | 31AZ (31AZ) | 2026-08-17 00:14 UTC | 2026-08-17 00:45 UTC | 30m |
| EJA430 | EJA | Monterey Regional Airport (KMRY) | Flying M & M Ranch Airport (0CO6) | 2026-08-16 23:09 UTC | 2026-08-17 00:41 UTC | 1h 32m |
| FWA5 | FWA | Flagstaff Pulliam Airport (KFLG) | Flagstaff Pulliam Airport (KFLG) | 2026-08-17 00:17 UTC | 2026-08-17 00:41 UTC | 23m |
| RFS706 | RFS | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-08-16 23:42 UTC | 2026-08-17 00:38 UTC | 56m |
| N361ML |  | Long Beach (Daugherty Field) Airport (KLGB) | Henderson Executive Airport (KHND) | 2026-08-16 23:44 UTC | 2026-08-17 00:37 UTC | 53m |
| PE993 |  | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-16 23:52 UTC | 2026-08-17 00:36 UTC | 44m |
| CATS12 | CAT | Osan Air Base (RKSO) | G 301 Airport (RKRG) | 2026-08-17 00:23 UTC | 2026-08-17 00:36 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
