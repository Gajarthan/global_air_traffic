# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_07:07:10_UTC-green)

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

**Latest saved flight:** 2026-08-26 07:07:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 07:07:10 UTC

- **237,654** saved flights
- **72,404** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **237,654** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,862,232.7 tonnes** estimated CO2 emissions
- **165,926,535 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9510 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4002 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3033 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2283 |
| 10 | AZU | 2216 |
| 11 | Vueling | 2031 |
| 12 | Lufthansa | 1923 |
| 13 | WIF | 1885 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1590 |
| 17 | AXM | 1588 |
| 18 | QLK | 1522 |
| 19 | EJU | 1521 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1416 |
| 23 | GLO | 1329 |
| 24 | WMT | 1326 |
| 25 | VIV | 1312 |
| 26 | PGT | 1297 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1269 |
| 29 | JetBlue | 1180 |
| 30 | AEE | 1177 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197416 |
| 2 | 🇪🇸 ES | 15227 |
| 3 | 🇧🇷 BR | 13885 |
| 4 | 🇦🇺 AU | 13521 |
| 5 | 🇨🇦 CA | 13173 |
| 6 | 🇮🇹 IT | 12948 |
| 7 | 🇮🇳 IN | 12477 |
| 8 | 🇩🇪 DE | 11681 |
| 9 | 🇬🇧 GB | 11182 |
| 10 | 🇨🇴 CO | 10123 |
| 11 | 🇯🇵 JP | 9615 |
| 12 | 🇫🇷 FR | 9507 |
| 13 | 🇹🇷 TR | 7053 |
| 14 | 🇬🇷 GR | 6991 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6336 |
| 17 | 🇳🇴 NO | 5869 |
| 18 | 🇹🇭 TH | 4274 |
| 19 | 🇲🇾 MY | 4253 |
| 20 | 🇿🇦 ZA | 4157 |
| 21 | 🇵🇱 PL | 3946 |
| 22 | 🇳🇿 NZ | 3290 |
| 23 | 🇵🇭 PH | 3279 |
| 24 | 🇬🇹 GT | 2978 |
| 25 | 🇰🇷 KR | 2803 |
| 26 | 🇭🇷 HR | 2737 |
| 27 | 🇲🇦 MA | 2396 |
| 28 | 🇲🇪 ME | 2209 |
| 29 | 🇳🇱 NL | 2127 |
| 30 | 🇮🇩 ID | 2078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2900 |
| 4 | Tokyo International Airport |  | JP | 2864 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2480 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2374 |
| 10 | El Dorado International Airport |  | CO | 2277 |
| 11 | La Aurora Airport |  | GT | 2269 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1882 |
| 17 | Capua Airport |  | IT | 1869 |
| 18 | Madrid Barajas International Airport |  | ES | 1862 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1794 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1751 |
| 21 | Malpensa International Airport |  | IT | 1704 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1675 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1588 |
| 27 | Kuala Lumpur International Airport |  | MY | 1537 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1501 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1418 |
| 33 | Seattle-Tacoma International Airport |  | US | 1392 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 35 | Bengaluru International Airport |  | IN | 1390 |
| 36 | Don Mueang International Airport |  | TH | 1382 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1302 |
| 40 | O. R. Tambo International Airport |  | ZA | 1292 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 876 | 21m | 244 km | 3,688.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 607 | 24m | 225 km | 2,354.9 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 604 | 1h 6m | 770 km | 8,023.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 392 | 27m | 275 km | 1,857.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 370 | 1h 50m | 1,423 km | 9,080.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 363 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 352 | 44m | 555 km | 3,370.6 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 336 | 21m | 250 km | 1,451.3 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 320 | 1h 7m | 706 km | 3,896.0 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 319 | 24m | 218 km | 1,201.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 316 | 1h 40m | 1,156 km | 6,304.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 291 | 27m | 215 km | 1,077.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 275 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N487LP |  | AZ00 (AZ00) | Glendale Regional Airport (KGEU) | 2026-08-26 06:01 UTC | 2026-08-26 07:07 UTC | 1h 5m |
| ZSDCA | ZSD | Cape Town International Airport (FACT) | Morningside Farm Airport (FAMS) | 2026-08-26 05:23 UTC | 2026-08-26 06:56 UTC | 1h 33m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-25 19:43 UTC | 2026-08-26 06:56 UTC | 11h 13m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-26 00:10 UTC | 2026-08-26 06:54 UTC | 6h 43m |
| EQE902 | EQE | Juhu Aerodrome (VAJJ) | Cairo International Airport (HECA) | 2026-08-26 01:35 UTC | 2026-08-26 06:53 UTC | 5h 17m |
| QTR818 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-25 23:14 UTC | 2026-08-26 06:50 UTC | 7h 36m |
| N302TP |  | 84OL (84OL) | Tulsa Riverside Airport (KRVS) | 2026-08-26 06:14 UTC | 2026-08-26 06:43 UTC | 29m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-26 05:45 UTC | 2026-08-26 06:40 UTC | 54m |
| DIWAW | DIW | Oulu Airport (EFOU) | EFML (EFML) | 2026-08-26 06:21 UTC | 2026-08-26 06:32 UTC | 11m |
| KLM887 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-08-25 19:38 UTC | 2026-08-26 06:32 UTC | 10h 53m |
| HL1272 |  | RKTA (RKTA) | Daegu Airport (RKTN) | 2026-08-26 05:11 UTC | 2026-08-26 06:30 UTC | 1h 19m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-08-25 19:56 UTC | 2026-08-26 06:30 UTC | 10h 33m |
| FD571 |  | Adelaide International Airport (YPAD) | Blinman Airport (YBLM) | 2026-08-26 05:21 UTC | 2026-08-26 06:28 UTC | 1h 7m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Aosta Airport (LIMW) | 2026-08-26 05:42 UTC | 2026-08-26 06:24 UTC | 42m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-08-25 18:47 UTC | 2026-08-26 06:23 UTC | 11h 35m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-26 05:47 UTC | 2026-08-26 06:23 UTC | 35m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-08-26 05:37 UTC | 2026-08-26 06:22 UTC | 45m |
| N541LM |  | Ted Stevens Anchorage International Airport (PANC) | AK04 (AK04) | 2026-08-26 05:51 UTC | 2026-08-26 06:21 UTC | 29m |
| BOX592 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-25 11:14 UTC | 2026-08-26 06:16 UTC | 19h 2m |
| EZS12XR | EZS | Geneva Cointrin International Airport (LSGG) | Pristina International Airport (BKPR) | 2026-08-26 04:36 UTC | 2026-08-26 06:15 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
