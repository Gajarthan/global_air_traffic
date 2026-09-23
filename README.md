# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_01:31:24_UTC-green)

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

**Latest saved flight:** 2026-09-23 01:31:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 01:31:24 UTC

- **266,928** saved flights
- **78,488** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **266,928** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,236,895.5 tonnes** estimated CO2 emissions
- **187,646,115 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10539 |
| 2 | SkyWest Airlines | 9290 |
| 3 | EJA | 5192 |
| 4 | IndiGo | 4474 |
| 5 | American Airlines | 4162 |
| 6 | Southwest Airlines | 3930 |
| 7 | Delta Air Lines | 3321 |
| 8 | ENY | 3139 |
| 9 | LATAM Airlines | 2576 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2239 |
| 12 | WIF | 2161 |
| 13 | LXJ | 2095 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1792 |
| 16 | Swiss International | 1758 |
| 17 | QLK | 1722 |
| 18 | EJU | 1684 |
| 19 | AXM | 1670 |
| 20 | United Airlines | 1638 |
| 21 | Alaska Airlines | 1579 |
| 22 | All Nippon Airways | 1538 |
| 23 | PGT | 1504 |
| 24 | WMT | 1498 |
| 25 | GLO | 1491 |
| 26 | Air France | 1467 |
| 27 | VIV | 1461 |
| 28 | Wizz Air | 1450 |
| 29 | CXK | 1299 |
| 30 | AEE | 1285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221954 |
| 2 | 🇪🇸 ES | 16763 |
| 3 | 🇧🇷 BR | 15626 |
| 4 | 🇦🇺 AU | 15324 |
| 5 | 🇨🇦 CA | 14882 |
| 6 | 🇮🇹 IT | 14504 |
| 7 | 🇮🇳 IN | 14153 |
| 8 | 🇩🇪 DE | 12834 |
| 9 | 🇬🇧 GB | 12375 |
| 10 | 🇨🇴 CO | 12188 |
| 11 | 🇫🇷 FR | 10649 |
| 12 | 🇯🇵 JP | 10281 |
| 13 | 🇹🇷 TR | 8084 |
| 14 | 🇬🇷 GR | 7717 |
| 15 | 🇲🇽 MX | 7361 |
| 16 | 🇨🇭 CH | 7114 |
| 17 | 🇳🇴 NO | 6604 |
| 18 | 🇹🇭 TH | 4784 |
| 19 | 🇲🇾 MY | 4502 |
| 20 | 🇿🇦 ZA | 4470 |
| 21 | 🇵🇱 PL | 4382 |
| 22 | 🇳🇿 NZ | 3722 |
| 23 | 🇵🇭 PH | 3543 |
| 24 | 🇬🇹 GT | 3386 |
| 25 | 🇭🇷 HR | 3039 |
| 26 | 🇰🇷 KR | 3024 |
| 27 | 🇲🇦 MA | 2663 |
| 28 | 🇲🇪 ME | 2500 |
| 29 | 🇳🇱 NL | 2387 |
| 30 | 🇮🇩 ID | 2228 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5441 |
| 2 | Denver International Airport |  | US | 4339 |
| 3 | Indira Gandhi International Airport |  | IN | 3203 |
| 4 | Tokyo International Airport |  | JP | 3075 |
| 5 | El Dorado International Airport |  | CO | 2873 |
| 6 | Harry Reid International Airport |  | US | 2855 |
| 7 | Guaymaral Airport |  | CO | 2800 |
| 8 | Zurich Airport |  | CH | 2775 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2677 |
| 10 | La Aurora Airport |  | GT | 2572 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2568 |
| 12 | Salt Lake City International Airport |  | US | 2357 |
| 13 | Chicago O'Hare International Airport |  | US | 2293 |
| 14 | Congonhas Airport |  | BR | 2276 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2181 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2052 |
| 18 | Frankfurt am Main International Airport |  | DE | 2028 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1923 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1904 |
| 22 | Charles de Gaulle International Airport |  | FR | 1894 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1873 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1872 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1812 |
| 26 | Macau International Airport |  | MO | 1776 |
| 27 | Ninoy Aquino International Airport |  | PH | 1739 |
| 28 | Charlotte/Douglas International Airport |  | US | 1666 |
| 29 | Barcelona International Airport |  | ES | 1664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1613 |
| 33 | Seattle-Tacoma International Airport |  | US | 1565 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1562 |
| 35 | Calgary International Airport |  | CA | 1527 |
| 36 | Don Mueang International Airport |  | TH | 1516 |
| 37 | Bengaluru International Airport |  | IN | 1507 |
| 38 | Oslo Gardermoen Airport |  | NO | 1502 |
| 39 | Vancouver International Airport |  | CA | 1497 |
| 40 | Antalya International Airport |  | TR | 1428 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1117 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1000 | 21m | 244 km | 4,210.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 671 | 1h 6m | 770 km | 8,913.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 665 | 24m | 225 km | 2,579.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 594 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 406 | 44m | 241 km | 1,686.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 341 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 337 | 1h 6m | 706 km | 4,103.0 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 334 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 331 | 26m | 215 km | 1,225.9 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 290 | 42m | 535 km | 2,678.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 282 | 18m | 14 km | 70.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N64087 |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-09-23 00:48 UTC | 2026-09-23 01:31 UTC | 42m |
| MVK90 | MVK | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-09-23 01:12 UTC | 2026-09-23 01:29 UTC | 16m |
| ZJU | ZJU | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-09-23 01:03 UTC | 2026-09-23 01:27 UTC | 23m |
| SUMIT81 | SUM | Vantage View Airport (7CO6) | Pueblo Memorial Airport (KPUB) | 2026-09-23 01:09 UTC | 2026-09-23 01:27 UTC | 17m |
| BALL15 | BAL | Cottonwood Airport (OK66) | William R Pogue Municipal Airport (KOWP) | 2026-09-23 01:02 UTC | 2026-09-23 01:23 UTC | 21m |
| VALOR67 | VAL | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-09-23 00:59 UTC | 2026-09-23 01:23 UTC | 24m |
| N350RM |  | Scottsdale Airport (KSDL) | Orlando Executive Airport (KORL) | 2026-09-22 21:38 UTC | 2026-09-23 01:19 UTC | 3h 40m |
| FGVFA | FGV | Moorea Airport (NTTM) | Moorea Airport (NTTM) | 2026-09-23 00:52 UTC | 2026-09-23 01:16 UTC | 23m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-23 00:57 UTC | 2026-09-23 01:15 UTC | 18m |
| R51263 |  | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-09-22 23:42 UTC | 2026-09-23 01:13 UTC | 1h 31m |
| UAL1561 | United Airlines | San Francisco International Airport (KSFO) | San Diego International Airport (KSAN) | 2026-09-23 00:04 UTC | 2026-09-23 01:13 UTC | 1h 8m |
| KCGB521 | KCG | Gimhae International Airport (RKPK) | Gimhae International Airport (RKPK) | 2026-09-23 01:11 UTC | 2026-09-23 01:11 UTC | 0m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-23 00:41 UTC | 2026-09-23 01:11 UTC | 29m |
| GUMP33 | GUM | Anniston Regional Airport (KANB) | Anniston Regional Airport (KANB) | 2026-09-23 00:35 UTC | 2026-09-23 01:10 UTC | 35m |
| LANCE86 | LAN | Dane County Regional/Truax Field (KMSN) | Watertown Municipal Airport (KRYV) | 2026-09-22 23:55 UTC | 2026-09-23 01:10 UTC | 1h 14m |
| N800MK |  | Kansas City Downtown/Wheeler Field (KMKC) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-22 22:09 UTC | 2026-09-23 01:07 UTC | 2h 58m |
| N885G |  | K00V (K00V) | K00V (K00V) | 2026-09-23 00:42 UTC | 2026-09-23 01:07 UTC | 25m |
| SKW4666 | SkyWest Airlines | Casper/Natrona County International Airport (KCPR) | Denver International Airport (KDEN) | 2026-09-23 00:23 UTC | 2026-09-23 01:07 UTC | 43m |
| LS09 |  | CA75 (CA75) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-23 00:48 UTC | 2026-09-23 01:04 UTC | 16m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-23 00:50 UTC | 2026-09-23 01:03 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
