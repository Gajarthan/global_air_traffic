# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_18:37:01_UTC-green)

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

**Latest saved flight:** 2026-09-09 18:37:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 18:37:01 UTC

- **252,784** saved flights
- **75,679** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,784** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,045,837.8 tonnes** estimated CO2 emissions
- **176,570,306 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10109 |
| 2 | SkyWest Airlines | 8818 |
| 3 | EJA | 4883 |
| 4 | IndiGo | 4237 |
| 5 | American Airlines | 4028 |
| 6 | Southwest Airlines | 3738 |
| 7 | Delta Air Lines | 3190 |
| 8 | ENY | 3017 |
| 9 | LATAM Airlines | 2431 |
| 10 | AZU | 2348 |
| 11 | Vueling | 2151 |
| 12 | WIF | 2025 |
| 13 | Lufthansa | 1994 |
| 14 | LXJ | 1971 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1699 |
| 17 | AXM | 1630 |
| 18 | QLK | 1622 |
| 19 | EJU | 1619 |
| 20 | United Airlines | 1573 |
| 21 | Alaska Airlines | 1507 |
| 22 | All Nippon Airways | 1478 |
| 23 | WMT | 1433 |
| 24 | GLO | 1404 |
| 25 | PGT | 1389 |
| 26 | VIV | 1382 |
| 27 | Air France | 1379 |
| 28 | Wizz Air | 1378 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209738 |
| 2 | 🇪🇸 ES | 16135 |
| 3 | 🇧🇷 BR | 14733 |
| 4 | 🇦🇺 AU | 14381 |
| 5 | 🇨🇦 CA | 14043 |
| 6 | 🇮🇹 IT | 13847 |
| 7 | 🇮🇳 IN | 13249 |
| 8 | 🇩🇪 DE | 12386 |
| 9 | 🇬🇧 GB | 11830 |
| 10 | 🇨🇴 CO | 11167 |
| 11 | 🇫🇷 FR | 10170 |
| 12 | 🇯🇵 JP | 9922 |
| 13 | 🇹🇷 TR | 7564 |
| 14 | 🇬🇷 GR | 7409 |
| 15 | 🇲🇽 MX | 6970 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6255 |
| 18 | 🇹🇭 TH | 4548 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4211 |
| 22 | 🇳🇿 NZ | 3450 |
| 23 | 🇵🇭 PH | 3427 |
| 24 | 🇬🇹 GT | 3146 |
| 25 | 🇰🇷 KR | 2914 |
| 26 | 🇭🇷 HR | 2906 |
| 27 | 🇲🇦 MA | 2553 |
| 28 | 🇲🇪 ME | 2378 |
| 29 | 🇳🇱 NL | 2279 |
| 30 | 🇮🇩 ID | 2162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5209 |
| 2 | Denver International Airport |  | US | 4081 |
| 3 | Indira Gandhi International Airport |  | IN | 3068 |
| 4 | Tokyo International Airport |  | JP | 2960 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2682 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2582 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2559 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2400 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2204 |
| 14 | Congonhas Airport |  | BR | 2161 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2075 |
| 16 | Capua Airport |  | IT | 1995 |
| 17 | Madrid Barajas International Airport |  | ES | 1986 |
| 18 | Frankfurt am Main International Airport |  | DE | 1963 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1891 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1837 |
| 21 | Malpensa International Airport |  | IT | 1817 |
| 22 | Charles de Gaulle International Airport |  | FR | 1773 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1772 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1760 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1684 |
| 26 | Ninoy Aquino International Airport |  | PH | 1674 |
| 27 | Macau International Airport |  | MO | 1667 |
| 28 | Charlotte/Douglas International Airport |  | US | 1591 |
| 29 | Barcelona International Airport |  | ES | 1591 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1508 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1464 |
| 35 | Calgary International Airport |  | CA | 1457 |
| 36 | Don Mueang International Airport |  | TH | 1456 |
| 37 | Bengaluru International Airport |  | IN | 1443 |
| 38 | Oslo Gardermoen Airport |  | NO | 1425 |
| 39 | Vancouver International Airport |  | CA | 1415 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 939 | 21m | 244 km | 3,953.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 673 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 634 | 1h 6m | 770 km | 8,422.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 566 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 379 | 44m | 241 km | 1,574.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 372 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 312 | 26m | 215 km | 1,155.5 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 306 | 19m | 99 km | 524.2 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N51NW |  | Boise Air Trml/Gowen Field (KBOI) | Sundog Airport (99UT) | 2026-09-09 16:22 UTC | 2026-09-09 18:37 UTC | 2h 14m |
| N725LV |  | Henderson Executive Airport (KHND) | Jean Airport (K0L7) | 2026-09-09 18:07 UTC | 2026-09-09 18:33 UTC | 25m |
| LS21 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-09 17:05 UTC | 2026-09-09 18:23 UTC | 1h 17m |
| N34737 |  | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-09-09 18:12 UTC | 2026-09-09 18:21 UTC | 9m |
| BOX722 | BOX | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-09 13:46 UTC | 2026-09-09 18:20 UTC | 4h 33m |
| ROKT71 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-09-09 17:59 UTC | 2026-09-09 18:19 UTC | 19m |
| N1374U |  | Chesapeake Regional Airport (KCPK) | Chesapeake Regional Airport (KCPK) | 2026-09-09 17:38 UTC | 2026-09-09 18:18 UTC | 39m |
| N96LS |  | Sky Ranch At Carefree Airport (18AZ) | Montezuma Airport (19AZ) | 2026-09-09 18:01 UTC | 2026-09-09 18:17 UTC | 16m |
| N172LK |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-09 17:45 UTC | 2026-09-09 18:17 UTC | 31m |
| ARCAS34 | ARC | 4TA5 (4TA5) | 54TS (54TS) | 2026-09-09 18:03 UTC | 2026-09-09 18:15 UTC | 12m |
| KLM877 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 10:15 UTC | 2026-09-09 18:13 UTC | 7h 57m |
| N2893E |  | Reno/Tahoe International Airport (KRNO) | Rolling Thunder Airport (NV96) | 2026-09-09 17:37 UTC | 2026-09-09 18:13 UTC | 36m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Ted Stevens Anchorage International Airport (PANC) | 2026-09-09 17:48 UTC | 2026-09-09 18:13 UTC | 24m |
| N513XX |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | NM71 (NM71) | 2026-09-09 17:30 UTC | 2026-09-09 18:10 UTC | 40m |
| DLH766 | Lufthansa | Munich International Airport (EDDM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 10:45 UTC | 2026-09-09 18:06 UTC | 7h 20m |
| SEJ9601 | SEJ | Nariya Airport (OENR) | Pune Airport (VAPO) | 2026-09-09 14:51 UTC | 2026-09-09 18:04 UTC | 3h 12m |
| KRAKEN | KRA | Comodoro Arturo Merino Benitez International Airport (SCEL) | Chicureo Airport (SCHC) | 2026-09-09 16:17 UTC | 2026-09-09 18:03 UTC | 1h 45m |
| SAS1444 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Gothenburg-Landvetter Airport (ESGG) | 2026-09-09 17:28 UTC | 2026-09-09 17:57 UTC | 28m |
| BAW139 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 09:23 UTC | 2026-09-09 17:56 UTC | 8h 33m |
| AIC4218 | Air India | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-09 15:17 UTC | 2026-09-09 17:56 UTC | 2h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
