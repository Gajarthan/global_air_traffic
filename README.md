# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_22:47:31_UTC-green)

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

**Latest saved flight:** 2026-08-25 22:47:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 22:47:31 UTC

- **236,935** saved flights
- **72,296** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,935** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,853,369.1 tonnes** estimated CO2 emissions
- **165,412,703 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9501 |
| 2 | SkyWest Airlines | 8383 |
| 3 | EJA | 4606 |
| 4 | IndiGo | 3986 |
| 5 | American Airlines | 3852 |
| 6 | Southwest Airlines | 3612 |
| 7 | Delta Air Lines | 3023 |
| 8 | ENY | 2876 |
| 9 | LATAM Airlines | 2274 |
| 10 | AZU | 2213 |
| 11 | Vueling | 2028 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1850 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1588 |
| 17 | AXM | 1576 |
| 18 | EJU | 1520 |
| 19 | QLK | 1502 |
| 20 | United Airlines | 1502 |
| 21 | Alaska Airlines | 1423 |
| 22 | All Nippon Airways | 1401 |
| 23 | GLO | 1325 |
| 24 | WMT | 1324 |
| 25 | VIV | 1308 |
| 26 | PGT | 1291 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1268 |
| 29 | JetBlue | 1178 |
| 30 | AEE | 1175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196978 |
| 2 | 🇪🇸 ES | 15215 |
| 3 | 🇧🇷 BR | 13853 |
| 4 | 🇦🇺 AU | 13356 |
| 5 | 🇨🇦 CA | 13120 |
| 6 | 🇮🇹 IT | 12930 |
| 7 | 🇮🇳 IN | 12423 |
| 8 | 🇩🇪 DE | 11661 |
| 9 | 🇬🇧 GB | 11176 |
| 10 | 🇨🇴 CO | 10077 |
| 11 | 🇯🇵 JP | 9548 |
| 12 | 🇫🇷 FR | 9503 |
| 13 | 🇹🇷 TR | 7032 |
| 14 | 🇬🇷 GR | 6979 |
| 15 | 🇲🇽 MX | 6585 |
| 16 | 🇨🇭 CH | 6322 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇲🇾 MY | 4225 |
| 19 | 🇹🇭 TH | 4219 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3944 |
| 22 | 🇳🇿 NZ | 3261 |
| 23 | 🇵🇭 PH | 3245 |
| 24 | 🇬🇹 GT | 2972 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2734 |
| 27 | 🇲🇦 MA | 2396 |
| 28 | 🇲🇪 ME | 2203 |
| 29 | 🇳🇱 NL | 2125 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4923 |
| 2 | Denver International Airport |  | US | 3846 |
| 3 | Indira Gandhi International Airport |  | IN | 2885 |
| 4 | Tokyo International Airport |  | JP | 2844 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2533 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2431 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2369 |
| 10 | La Aurora Airport |  | GT | 2266 |
| 11 | El Dorado International Airport |  | CO | 2260 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2091 |
| 14 | Congonhas Airport |  | BR | 2019 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1984 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1864 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1787 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1750 |
| 21 | Malpensa International Airport |  | IT | 1699 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1679 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1650 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1569 |
| 27 | Charlotte/Douglas International Airport |  | US | 1527 |
| 28 | Kuala Lumpur International Airport |  | MY | 1526 |
| 29 | Barcelona International Airport |  | ES | 1499 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1491 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1437 |
| 32 | Viracopos International Airport |  | BR | 1416 |
| 33 | Seattle-Tacoma International Airport |  | US | 1389 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1388 |
| 35 | Bengaluru International Airport |  | IN | 1384 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1356 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1295 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 869 | 21m | 244 km | 3,659.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 599 | 1h 6m | 770 km | 7,957.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 391 | 27m | 275 km | 1,852.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 318 | 24m | 218 km | 1,198.0 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 315 | 1h 40m | 1,156 km | 6,284.1 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 315 | 22m | 55 km | 299.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 295 | 19m | 99 km | 505.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 254 | 1h 50m | 1,304 km | 5,714.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N23AT |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Hayward Executive Airport (KHWD) | 2026-08-25 22:23 UTC | 2026-08-25 22:47 UTC | 24m |
| N267FG |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-08-25 22:32 UTC | 2026-08-25 22:46 UTC | 14m |
| CFR72 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-08-25 20:19 UTC | 2026-08-25 22:42 UTC | 2h 23m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-25 22:24 UTC | 2026-08-25 22:36 UTC | 12m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-25 15:25 UTC | 2026-08-25 22:31 UTC | 7h 6m |
| N250WG |  | Mount Hawley Auxiliary Airport (K3MY) | 3SC7 (3SC7) | 2026-08-25 20:15 UTC | 2026-08-25 22:29 UTC | 2h 14m |
| N133MC |  | Gerald R Ford International Airport (KGRR) | Mason County Airport (KLDM) | 2026-08-25 21:46 UTC | 2026-08-25 22:26 UTC | 40m |
| RAIDR47 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Mammoth Yosemite Airport (KMMH) | 2026-08-25 21:26 UTC | 2026-08-25 22:26 UTC | 59m |
| N406M |  | Merrill Field (PAMR) | Mc Grath Airport (PAMC) | 2026-08-25 20:55 UTC | 2026-08-25 22:25 UTC | 1h 29m |
| XAPAZ | XAP | Charleston Afb/International Airport (KCHS) | Laredo International Airport (KLRD) | 2026-08-25 19:58 UTC | 2026-08-25 22:23 UTC | 2h 25m |
| CPA696 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-08-25 17:09 UTC | 2026-08-25 22:22 UTC | 5h 12m |
| NCJ12 | NCJ | Joe Foss Field (KFSD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-25 21:39 UTC | 2026-08-25 22:22 UTC | 42m |
| N713PM |  | 5MS2 (5MS2) | 5MS2 (5MS2) | 2026-08-25 21:01 UTC | 2026-08-25 22:21 UTC | 1h 19m |
| N262WJ |  | Aurora Municipal Airport (KARR) | 2LL1 (2LL1) | 2026-08-25 22:12 UTC | 2026-08-25 22:20 UTC | 7m |
| N403AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-25 21:44 UTC | 2026-08-25 22:19 UTC | 35m |
| LOT7YE | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Tallinn Airport (EETN) | 2026-08-25 21:19 UTC | 2026-08-25 22:17 UTC | 58m |
| N125MG |  | Roberts Field/Redmond Municipal Airport (KRDM) | Dry Creek Airpark (OG21) | 2026-08-25 21:46 UTC | 2026-08-25 22:15 UTC | 28m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-08-25 11:14 UTC | 2026-08-25 22:13 UTC | 10h 59m |
| N813AM |  | Litchfield Municipal Airport (K3LF) | 1IL1 (1IL1) | 2026-08-25 21:54 UTC | 2026-08-25 22:11 UTC | 16m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-25 21:47 UTC | 2026-08-25 22:11 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
