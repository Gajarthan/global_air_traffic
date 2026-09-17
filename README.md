# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_12:02:04_UTC-green)

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

**Latest saved flight:** 2026-09-17 12:02:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 12:02:04 UTC

- **261,116** saved flights
- **77,356** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **261,116** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,162,799.8 tonnes** estimated CO2 emissions
- **183,350,714 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10338 |
| 2 | SkyWest Airlines | 9091 |
| 3 | EJA | 5059 |
| 4 | IndiGo | 4382 |
| 5 | American Airlines | 4103 |
| 6 | Southwest Airlines | 3837 |
| 7 | Delta Air Lines | 3262 |
| 8 | ENY | 3085 |
| 9 | LATAM Airlines | 2518 |
| 10 | AZU | 2451 |
| 11 | Vueling | 2200 |
| 12 | WIF | 2100 |
| 13 | LXJ | 2039 |
| 14 | Lufthansa | 2026 |
| 15 | easyJet | 1769 |
| 16 | Swiss International | 1734 |
| 17 | QLK | 1688 |
| 18 | AXM | 1650 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1550 |
| 22 | All Nippon Airways | 1515 |
| 23 | WMT | 1471 |
| 24 | PGT | 1457 |
| 25 | GLO | 1455 |
| 26 | Air France | 1431 |
| 27 | VIV | 1429 |
| 28 | Wizz Air | 1418 |
| 29 | TKR | 1274 |
| 30 | AEE | 1262 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216809 |
| 2 | 🇪🇸 ES | 16510 |
| 3 | 🇧🇷 BR | 15279 |
| 4 | 🇦🇺 AU | 14967 |
| 5 | 🇨🇦 CA | 14547 |
| 6 | 🇮🇹 IT | 14206 |
| 7 | 🇮🇳 IN | 13819 |
| 8 | 🇩🇪 DE | 12655 |
| 9 | 🇬🇧 GB | 12138 |
| 10 | 🇨🇴 CO | 11753 |
| 11 | 🇫🇷 FR | 10456 |
| 12 | 🇯🇵 JP | 10152 |
| 13 | 🇹🇷 TR | 7889 |
| 14 | 🇬🇷 GR | 7580 |
| 15 | 🇲🇽 MX | 7187 |
| 16 | 🇨🇭 CH | 6992 |
| 17 | 🇳🇴 NO | 6441 |
| 18 | 🇹🇭 TH | 4684 |
| 19 | 🇲🇾 MY | 4447 |
| 20 | 🇿🇦 ZA | 4416 |
| 21 | 🇵🇱 PL | 4312 |
| 22 | 🇳🇿 NZ | 3621 |
| 23 | 🇵🇭 PH | 3494 |
| 24 | 🇬🇹 GT | 3330 |
| 25 | 🇭🇷 HR | 2985 |
| 26 | 🇰🇷 KR | 2980 |
| 27 | 🇲🇦 MA | 2614 |
| 28 | 🇲🇪 ME | 2459 |
| 29 | 🇳🇱 NL | 2334 |
| 30 | 🇮🇩 ID | 2207 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5348 |
| 2 | Denver International Airport |  | US | 4220 |
| 3 | Indira Gandhi International Airport |  | IN | 3145 |
| 4 | Tokyo International Airport |  | JP | 3030 |
| 5 | Harry Reid International Airport |  | US | 2775 |
| 6 | Guaymaral Airport |  | CO | 2774 |
| 7 | El Dorado International Airport |  | CO | 2742 |
| 8 | Zurich Airport |  | CH | 2728 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2627 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2536 |
| 11 | La Aurora Airport |  | GT | 2527 |
| 12 | Salt Lake City International Airport |  | US | 2303 |
| 13 | Chicago O'Hare International Airport |  | US | 2260 |
| 14 | Congonhas Airport |  | BR | 2229 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2130 |
| 16 | Capua Airport |  | IT | 2037 |
| 17 | Madrid Barajas International Airport |  | ES | 2022 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1969 |
| 20 | Malpensa International Airport |  | IT | 1879 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1875 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1843 |
| 23 | Charles de Gaulle International Airport |  | FR | 1843 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1781 |
| 26 | Macau International Airport |  | MO | 1732 |
| 27 | Ninoy Aquino International Airport |  | PH | 1714 |
| 28 | Barcelona International Airport |  | ES | 1630 |
| 29 | Charlotte/Douglas International Airport |  | US | 1627 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1604 |
| 31 | Kuala Lumpur International Airport |  | MY | 1596 |
| 32 | Viracopos International Airport |  | BR | 1583 |
| 33 | Seattle-Tacoma International Airport |  | US | 1530 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1520 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1492 |
| 37 | Bengaluru International Airport |  | IN | 1482 |
| 38 | Oslo Gardermoen Airport |  | NO | 1469 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1401 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1111 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 974 | 21m | 244 km | 4,101.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 656 | 1h 6m | 770 km | 8,714.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 653 | 24m | 225 km | 2,533.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 585 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 422 | 27m | 275 km | 1,999.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 398 | 44m | 241 km | 1,653.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 368 | 24m | 218 km | 1,386.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 318 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 301 | 1h 14m | 961 km | 4,989.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 300 | 19m | 144 km | 746.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 282 | 1h 50m | 1,304 km | 6,344.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AKJ1150 | AKJ | Bengaluru International Airport (VOBL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 10:50 UTC | 2026-09-17 12:02 UTC | 1h 12m |
| UAE502 | Emirates | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 09:31 UTC | 2026-09-17 12:00 UTC | 2h 29m |
| AIC4UZ | Air India | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-17 10:32 UTC | 2026-09-17 11:58 UTC | 1h 26m |
| FNG200 | FNG | Helsinki Vantaa Airport (EFHK) | EFHF (EFHF) | 2026-09-17 11:47 UTC | 2026-09-17 11:58 UTC | 10m |
|  |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Lynchburg Regional/Preston Glenn Field (KLYH) | 2026-09-17 11:37 UTC | 2026-09-17 11:50 UTC | 12m |
| IGO5031 | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-17 10:41 UTC | 2026-09-17 11:47 UTC | 1h 5m |
| EMC8 | EMC | Manchester Airport (EGCC) | Blackpool International Airport (EGNH) | 2026-09-17 10:22 UTC | 2026-09-17 11:45 UTC | 1h 22m |
| AIC6VA | Air India | Bhuj Airport (VABJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 10:46 UTC | 2026-09-17 11:44 UTC | 57m |
| PPBBI | PPB | Campo de Marte Airport (SBMT) | Nascimento I Airport (SDNI) | 2026-09-17 11:32 UTC | 2026-09-17 11:35 UTC | 3m |
| PSBER | PSB | Americana Airport (SDAI) | Americana Airport (SDAI) | 2026-09-17 11:21 UTC | 2026-09-17 11:32 UTC | 11m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-09-17 11:13 UTC | 2026-09-17 11:27 UTC | 14m |
| IGO674 | IndiGo | Cochin International Airport (VOCI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 09:56 UTC | 2026-09-17 11:26 UTC | 1h 29m |
| JANET55 | JAN | Harry Reid International Airport (KLAS) | Tonopah Test Range (KTNX) | 2026-09-17 11:02 UTC | 2026-09-17 11:24 UTC | 21m |
| AM319 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-09-17 10:57 UTC | 2026-09-17 11:16 UTC | 19m |
| HBZZX | HBZ | Muenster Aero Airport (LSPU) | Meiringen Airport (LSMM) | 2026-09-17 11:11 UTC | 2026-09-17 11:16 UTC | 4m |
| TPON30 | TPO | Cazaux (BA 120) Air Base (LFBC) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-09-17 11:04 UTC | 2026-09-17 11:14 UTC | 10m |
| N12EC |  | Tango 7 Airport (9AR4) | Yazoo County Airport (K87I) | 2026-09-17 10:51 UTC | 2026-09-17 11:10 UTC | 18m |
| DEFGR | DEF | Leutkirch-Unterzeil Airport (EDNL) | Mengen-Hohentengen Airport (EDTM) | 2026-09-17 10:49 UTC | 2026-09-17 11:08 UTC | 19m |
| RYR71JD | Ryanair | Nantes Atlantique Airport (LFRS) | Saiss Airport (GMFF) | 2026-09-17 09:17 UTC | 2026-09-17 11:05 UTC | 1h 48m |
| TONIC1 | TON | Nordholz Airport (ETMN) | Nordholz-Spieka Airport (EDXN) | 2026-09-17 11:03 UTC | 2026-09-17 11:05 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
