# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_22:39:22_UTC-green)

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

**Latest saved flight:** 2026-08-19 22:39:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 22:39:22 UTC

- **217,639** saved flights
- **68,605** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,639** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,619,130.5 tonnes** estimated CO2 emissions
- **151,833,650 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8713 |
| 2 | SkyWest Airlines | 7794 |
| 3 | EJA | 4241 |
| 4 | IndiGo | 3692 |
| 5 | American Airlines | 3632 |
| 6 | Southwest Airlines | 3455 |
| 7 | Delta Air Lines | 2813 |
| 8 | ENY | 2691 |
| 9 | LATAM Airlines | 2060 |
| 10 | AZU | 1994 |
| 11 | Vueling | 1826 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1722 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1380 |
| 19 | EJU | 1354 |
| 20 | QLK | 1348 |
| 21 | Alaska Airlines | 1330 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1193 |
| 24 | GLO | 1186 |
| 25 | PGT | 1178 |
| 26 | Air France | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1109 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183648 |
| 2 | 🇪🇸 ES | 13940 |
| 3 | 🇧🇷 BR | 12560 |
| 4 | 🇦🇺 AU | 12181 |
| 5 | 🇨🇦 CA | 12001 |
| 6 | 🇮🇹 IT | 11558 |
| 7 | 🇮🇳 IN | 11498 |
| 8 | 🇩🇪 DE | 10765 |
| 9 | 🇬🇧 GB | 10213 |
| 10 | 🇨🇴 CO | 8949 |
| 11 | 🇯🇵 JP | 8872 |
| 12 | 🇫🇷 FR | 8665 |
| 13 | 🇬🇷 GR | 6345 |
| 14 | 🇹🇷 TR | 6256 |
| 15 | 🇲🇽 MX | 6078 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3595 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 3004 |
| 23 | 🇵🇭 PH | 2904 |
| 24 | 🇬🇹 GT | 2763 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1908 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4578 |
| 2 | Denver International Airport |  | US | 3559 |
| 3 | Tokyo International Airport |  | JP | 2663 |
| 4 | Indira Gandhi International Airport |  | IN | 2631 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2410 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2241 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2211 |
| 10 | La Aurora Airport |  | GT | 2103 |
| 11 | El Dorado International Airport |  | CO | 2039 |
| 12 | Chicago O'Hare International Airport |  | US | 2005 |
| 13 | Salt Lake City International Airport |  | US | 1922 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1898 |
| 15 | Congonhas Airport |  | BR | 1835 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1642 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1613 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1597 |
| 22 | Macau International Airport |  | MO | 1563 |
| 23 | Malpensa International Airport |  | IT | 1534 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1517 |
| 25 | Charles de Gaulle International Airport |  | FR | 1493 |
| 26 | Charlotte/Douglas International Airport |  | US | 1461 |
| 27 | Ninoy Aquino International Airport |  | PH | 1379 |
| 28 | Kuala Lumpur International Airport |  | MY | 1378 |
| 29 | Barcelona International Airport |  | ES | 1332 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1329 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1298 |
| 33 | Seattle-Tacoma International Airport |  | US | 1290 |
| 34 | Viracopos International Airport |  | BR | 1273 |
| 35 | Calgary International Airport |  | CA | 1226 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 776 | 21m | 244 km | 3,267.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 535 | 1h 7m | 770 km | 7,107.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 492 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 256 | 31m | 369 km | 1,629.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 235 | 1h 49m | 1,304 km | 5,286.9 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1242U |  | Dupage Airport (KDPA) | Lake In The Hills Airport (K3CK) | 2026-08-19 22:06 UTC | 2026-08-19 22:39 UTC | 32m |
| N81493 |  | Batten International Airport (KRAC) | Batten International Airport (KRAC) | 2026-08-19 22:01 UTC | 2026-08-19 22:36 UTC | 34m |
| TKR103 | TKR | Coeur D'Alene Airport (KCOE) | Coeur D'Alene Airport (KCOE) | 2026-08-19 22:06 UTC | 2026-08-19 22:35 UTC | 29m |
| UPS5334 | UPS | Dallas-Fort Worth International Airport (KDFW) | The Florida Keys Marathon International Airport (KMTH) | 2026-08-19 20:16 UTC | 2026-08-19 22:34 UTC | 2h 17m |
| AAL1310 | American Airlines | Denver International Airport (KDEN) | The Florida Keys Marathon International Airport (KMTH) | 2026-08-19 19:03 UTC | 2026-08-19 22:32 UTC | 3h 28m |
| N239FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-08-19 22:14 UTC | 2026-08-19 22:31 UTC | 17m |
| HKC9458 | HKC | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-19 17:34 UTC | 2026-08-19 22:31 UTC | 4h 57m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-08-19 11:02 UTC | 2026-08-19 22:30 UTC | 11h 28m |
| TRTGA31 | TRT | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-19 22:05 UTC | 2026-08-19 22:29 UTC | 23m |
| N926SJ |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-19 22:01 UTC | 2026-08-19 22:27 UTC | 26m |
| N5254D |  | Flying Cloud Airport (KFCM) | Boyceville Municipal Airport (K3T3) | 2026-08-19 21:42 UTC | 2026-08-19 22:26 UTC | 43m |
| ENY3961 | ENY | Pensacola International Airport (KPNS) | Tavernaero Park Airport (FA81) | 2026-08-19 21:05 UTC | 2026-08-19 22:23 UTC | 1h 18m |
| N345GB |  | Lenhardt Airpark (K7S9) | Iron Crown Airport (22OR) | 2026-08-19 22:19 UTC | 2026-08-19 22:23 UTC | 4m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-08-19 12:04 UTC | 2026-08-19 22:23 UTC | 10h 18m |
| AAL1167 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Tavernaero Park Airport (FA81) | 2026-08-19 19:54 UTC | 2026-08-19 22:23 UTC | 2h 28m |
| N454NC |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-19 17:03 UTC | 2026-08-19 22:22 UTC | 5h 18m |
| BOE447 | BOE | Boeing Field/King County International Airport (KBFI) | Franz Ranch Airport (33WA) | 2026-08-19 21:08 UTC | 2026-08-19 22:21 UTC | 1h 12m |
| N739ZH |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-08-19 22:18 UTC | 2026-08-19 22:21 UTC | 2m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-19 17:40 UTC | 2026-08-19 22:18 UTC | 4h 37m |
| UAL592 | United Airlines | Indianapolis International Airport (KIND) | Chicago O'Hare International Airport (KORD) | 2026-08-19 20:50 UTC | 2026-08-19 22:18 UTC | 1h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
