# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_23:03:24_UTC-green)

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

**Latest saved flight:** 2026-09-09 23:03:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 23:03:24 UTC

- **253,140** saved flights
- **75,773** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **253,140** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,050,366.5 tonnes** estimated CO2 emissions
- **176,832,840 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10123 |
| 2 | SkyWest Airlines | 8834 |
| 3 | EJA | 4890 |
| 4 | IndiGo | 4237 |
| 5 | American Airlines | 4031 |
| 6 | Southwest Airlines | 3743 |
| 7 | Delta Air Lines | 3192 |
| 8 | ENY | 3019 |
| 9 | LATAM Airlines | 2438 |
| 10 | AZU | 2355 |
| 11 | Vueling | 2155 |
| 12 | WIF | 2026 |
| 13 | Lufthansa | 1994 |
| 14 | LXJ | 1978 |
| 15 | easyJet | 1732 |
| 16 | Swiss International | 1699 |
| 17 | AXM | 1630 |
| 18 | QLK | 1624 |
| 19 | EJU | 1620 |
| 20 | United Airlines | 1576 |
| 21 | Alaska Airlines | 1508 |
| 22 | All Nippon Airways | 1478 |
| 23 | WMT | 1433 |
| 24 | GLO | 1408 |
| 25 | PGT | 1391 |
| 26 | VIV | 1382 |
| 27 | Air France | 1379 |
| 28 | Wizz Air | 1379 |
| 29 | JetBlue | 1236 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210142 |
| 2 | 🇪🇸 ES | 16153 |
| 3 | 🇧🇷 BR | 14771 |
| 4 | 🇦🇺 AU | 14397 |
| 5 | 🇨🇦 CA | 14080 |
| 6 | 🇮🇹 IT | 13865 |
| 7 | 🇮🇳 IN | 13255 |
| 8 | 🇩🇪 DE | 12393 |
| 9 | 🇬🇧 GB | 11837 |
| 10 | 🇨🇴 CO | 11203 |
| 11 | 🇫🇷 FR | 10175 |
| 12 | 🇯🇵 JP | 9922 |
| 13 | 🇹🇷 TR | 7572 |
| 14 | 🇬🇷 GR | 7410 |
| 15 | 🇲🇽 MX | 6975 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6260 |
| 18 | 🇹🇭 TH | 4549 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4213 |
| 22 | 🇳🇿 NZ | 3460 |
| 23 | 🇵🇭 PH | 3429 |
| 24 | 🇬🇹 GT | 3146 |
| 25 | 🇰🇷 KR | 2914 |
| 26 | 🇭🇷 HR | 2907 |
| 27 | 🇲🇦 MA | 2556 |
| 28 | 🇲🇪 ME | 2380 |
| 29 | 🇳🇱 NL | 2282 |
| 30 | 🇮🇩 ID | 2162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5213 |
| 2 | Denver International Airport |  | US | 4090 |
| 3 | Indira Gandhi International Airport |  | IN | 3071 |
| 4 | Tokyo International Airport |  | JP | 2960 |
| 5 | Guaymaral Airport |  | CO | 2747 |
| 6 | Harry Reid International Airport |  | US | 2687 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2590 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2565 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2400 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2208 |
| 14 | Congonhas Airport |  | BR | 2167 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2076 |
| 16 | Capua Airport |  | IT | 1997 |
| 17 | Madrid Barajas International Airport |  | ES | 1987 |
| 18 | Frankfurt am Main International Airport |  | DE | 1963 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1897 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1841 |
| 21 | Malpensa International Airport |  | IT | 1821 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1774 |
| 23 | Charles de Gaulle International Airport |  | FR | 1774 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1761 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1694 |
| 26 | Ninoy Aquino International Airport |  | PH | 1676 |
| 27 | Macau International Airport |  | MO | 1670 |
| 28 | Barcelona International Airport |  | ES | 1594 |
| 29 | Charlotte/Douglas International Airport |  | US | 1593 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1512 |
| 33 | Seattle-Tacoma International Airport |  | US | 1492 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1464 |
| 35 | Calgary International Airport |  | CA | 1459 |
| 36 | Don Mueang International Airport |  | TH | 1456 |
| 37 | Bengaluru International Airport |  | IN | 1443 |
| 38 | Oslo Gardermoen Airport |  | NO | 1428 |
| 39 | Vancouver International Airport |  | CA | 1417 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 939 | 21m | 244 km | 3,953.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 676 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 634 | 1h 6m | 770 km | 8,422.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 566 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 380 | 44m | 241 km | 1,578.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 372 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 338 | 23m | 55 km | 321.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 312 | 26m | 215 km | 1,155.5 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 306 | 19m | 99 km | 524.2 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 302 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 290 | 1h 14m | 961 km | 4,806.9 t |
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
| CFKAL | CFK | Winnipeg / St. Andrews Airport (CYAV) | Thunder Bay Airport (CYQT) | 2026-09-09 21:09 UTC | 2026-09-09 23:03 UTC | 1h 54m |
| N215TS |  | Talachulitna River Airport (1AK6) | Falcon Lake Strip (0AK9) | 2026-09-09 22:35 UTC | 2026-09-09 23:00 UTC | 25m |
| N94SF |  | Tyler Pounds Regional Airport (KTYR) | Austin-Bergstrom International Airport (KAUS) | 2026-09-09 22:27 UTC | 2026-09-09 23:00 UTC | 33m |
| N90422 |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-09-09 22:23 UTC | 2026-09-09 22:59 UTC | 36m |
| N62BN |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-09-09 22:38 UTC | 2026-09-09 22:55 UTC | 17m |
| N98AG |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-09-09 22:24 UTC | 2026-09-09 22:48 UTC | 23m |
| GMN94 | GMN | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-09-09 21:49 UTC | 2026-09-09 22:48 UTC | 58m |
| ZDS | ZDS | Sydney Bankstown Airport (YSBK) | Young Airport (YYNG) | 2026-09-09 21:57 UTC | 2026-09-09 22:48 UTC | 50m |
| LS21 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-09 21:18 UTC | 2026-09-09 22:44 UTC | 1h 26m |
| N503RP |  | Baton Rouge Metro, Ryan Field (KBTR) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-09 20:29 UTC | 2026-09-09 22:43 UTC | 2h 14m |
| STT208 | STT | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-09-09 22:00 UTC | 2026-09-09 22:43 UTC | 42m |
| LS31 |  | John Nichol's Field (0CL3) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-09 22:30 UTC | 2026-09-09 22:42 UTC | 12m |
| ARCAS46 | ARC | 4TA5 (4TA5) | K14F (K14F) | 2026-09-09 22:19 UTC | 2026-09-09 22:40 UTC | 21m |
| OXF8186 | OXF | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-09-09 21:17 UTC | 2026-09-09 22:40 UTC | 1h 22m |
| GRYHK11 | GRY | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-09-09 22:21 UTC | 2026-09-09 22:38 UTC | 17m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-09-09 10:59 UTC | 2026-09-09 22:36 UTC | 11h 37m |
| N930TD |  | Smith Field (8NE3) | Rocky Mountain Metro Airport (KBJC) | 2026-09-09 21:53 UTC | 2026-09-09 22:33 UTC | 40m |
| LXJ444 | LXJ | San Francisco International Airport (KSFO) | San Francisco International Airport (KSFO) | 2026-09-09 22:33 UTC | 2026-09-09 22:33 UTC | 0m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-09-09 17:44 UTC | 2026-09-09 22:28 UTC | 4h 44m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-09 17:47 UTC | 2026-09-09 22:27 UTC | 4h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
