# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_22:32:20_UTC-green)

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

**Latest saved flight:** 2026-09-11 22:32:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 22:32:20 UTC

- **255,506** saved flights
- **76,271** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,506** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,084,434.9 tonnes** estimated CO2 emissions
- **178,807,818 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10181 |
| 2 | SkyWest Airlines | 8903 |
| 3 | EJA | 4937 |
| 4 | IndiGo | 4273 |
| 5 | American Airlines | 4052 |
| 6 | Southwest Airlines | 3763 |
| 7 | Delta Air Lines | 3201 |
| 8 | ENY | 3036 |
| 9 | LATAM Airlines | 2462 |
| 10 | AZU | 2380 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2053 |
| 13 | Lufthansa | 2000 |
| 14 | LXJ | 1996 |
| 15 | easyJet | 1740 |
| 16 | Swiss International | 1711 |
| 17 | QLK | 1647 |
| 18 | AXM | 1638 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1585 |
| 21 | Alaska Airlines | 1517 |
| 22 | All Nippon Airways | 1489 |
| 23 | WMT | 1444 |
| 24 | GLO | 1423 |
| 25 | PGT | 1406 |
| 26 | VIV | 1397 |
| 27 | Air France | 1395 |
| 28 | Wizz Air | 1389 |
| 29 | JetBlue | 1243 |
| 30 | TKR | 1241 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212196 |
| 2 | 🇪🇸 ES | 16253 |
| 3 | 🇧🇷 BR | 14919 |
| 4 | 🇦🇺 AU | 14565 |
| 5 | 🇨🇦 CA | 14230 |
| 6 | 🇮🇹 IT | 13964 |
| 7 | 🇮🇳 IN | 13388 |
| 8 | 🇩🇪 DE | 12470 |
| 9 | 🇬🇧 GB | 11929 |
| 10 | 🇨🇴 CO | 11377 |
| 11 | 🇫🇷 FR | 10261 |
| 12 | 🇯🇵 JP | 9982 |
| 13 | 🇹🇷 TR | 7652 |
| 14 | 🇬🇷 GR | 7456 |
| 15 | 🇲🇽 MX | 7050 |
| 16 | 🇨🇭 CH | 6853 |
| 17 | 🇳🇴 NO | 6339 |
| 18 | 🇹🇭 TH | 4590 |
| 19 | 🇲🇾 MY | 4405 |
| 20 | 🇿🇦 ZA | 4354 |
| 21 | 🇵🇱 PL | 4234 |
| 22 | 🇳🇿 NZ | 3523 |
| 23 | 🇵🇭 PH | 3441 |
| 24 | 🇬🇹 GT | 3206 |
| 25 | 🇰🇷 KR | 2931 |
| 26 | 🇭🇷 HR | 2925 |
| 27 | 🇲🇦 MA | 2575 |
| 28 | 🇲🇪 ME | 2401 |
| 29 | 🇳🇱 NL | 2299 |
| 30 | 🇮🇩 ID | 2175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5241 |
| 2 | Denver International Airport |  | US | 4127 |
| 3 | Indira Gandhi International Airport |  | IN | 3087 |
| 4 | Tokyo International Airport |  | JP | 2980 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2705 |
| 7 | Zurich Airport |  | CH | 2674 |
| 8 | El Dorado International Airport |  | CO | 2629 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2579 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2501 |
| 11 | La Aurora Airport |  | GT | 2441 |
| 12 | Salt Lake City International Airport |  | US | 2251 |
| 13 | Chicago O'Hare International Airport |  | US | 2226 |
| 14 | Congonhas Airport |  | BR | 2190 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2089 |
| 16 | Capua Airport |  | IT | 2013 |
| 17 | Madrid Barajas International Airport |  | ES | 1995 |
| 18 | Frankfurt am Main International Airport |  | DE | 1974 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1916 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1849 |
| 21 | Malpensa International Airport |  | IT | 1837 |
| 22 | Charles de Gaulle International Airport |  | FR | 1799 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1792 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1777 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1722 |
| 26 | Macau International Airport |  | MO | 1692 |
| 27 | Ninoy Aquino International Airport |  | PH | 1682 |
| 28 | Barcelona International Airport |  | ES | 1606 |
| 29 | Charlotte/Douglas International Airport |  | US | 1602 |
| 30 | Kuala Lumpur International Airport |  | MY | 1586 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1570 |
| 32 | Viracopos International Airport |  | BR | 1528 |
| 33 | Seattle-Tacoma International Airport |  | US | 1499 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1485 |
| 35 | Calgary International Airport |  | CA | 1470 |
| 36 | Don Mueang International Airport |  | TH | 1469 |
| 37 | Bengaluru International Airport |  | IN | 1451 |
| 38 | Oslo Gardermoen Airport |  | NO | 1445 |
| 39 | Vancouver International Airport |  | CA | 1432 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1379 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 948 | 21m | 244 km | 3,991.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 684 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 640 | 1h 6m | 770 km | 8,501.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 408 | 44m | 555 km | 3,906.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 386 | 44m | 241 km | 1,603.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 356 | 24m | 218 km | 1,341.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 340 | 23m | 55 km | 323.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 313 | 19m | 99 km | 536.1 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 308 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 303 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 264 | 28m | 152 km | 689.9 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N907SE |  | Dubuque Regional Airport (KDBQ) | Dupage Airport (KDPA) | 2026-09-11 21:16 UTC | 2026-09-11 22:32 UTC | 1h 15m |
| CXK549 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-09-11 21:11 UTC | 2026-09-11 22:28 UTC | 1h 16m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-09-11 10:34 UTC | 2026-09-11 22:27 UTC | 11h 53m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-11 17:53 UTC | 2026-09-11 22:27 UTC | 4h 33m |
| N717AF |  | Byron Airport (KC83) | Mineta San Jose International Airport (KSJC) | 2026-09-11 21:45 UTC | 2026-09-11 22:25 UTC | 40m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-09-11 10:29 UTC | 2026-09-11 22:21 UTC | 11h 52m |
| TRON51 | TRO | Davis Monthan Afb Airport (KDMA) | Davis Monthan Afb Airport (KDMA) | 2026-09-11 19:30 UTC | 2026-09-11 22:19 UTC | 2h 48m |
| N70JV |  | Centennial Airport (KAPA) | Haxtun Municipal Airport (K17V) | 2026-09-11 21:51 UTC | 2026-09-11 22:17 UTC | 25m |
| BCS694 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-09-11 17:03 UTC | 2026-09-11 22:17 UTC | 5h 13m |
| CHP14 | CHP | CA53 (CA53) | Bodad Airport (CA11) | 2026-09-11 21:38 UTC | 2026-09-11 22:14 UTC | 36m |
| N8922V |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-09-11 21:47 UTC | 2026-09-11 22:07 UTC | 20m |
| RNGR740 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Fainting Goat Airport (87TX) | 2026-09-11 21:29 UTC | 2026-09-11 22:04 UTC | 34m |
| EFY7838 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-11 21:29 UTC | 2026-09-11 22:03 UTC | 33m |
| N1432E |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-11 21:43 UTC | 2026-09-11 22:02 UTC | 18m |
| ASP836 | ASP | Halifax Robert L. Stanfield International Airport (CYHZ) | Toronto Pearson International Airport (CYYZ) | 2026-09-11 20:02 UTC | 2026-09-11 22:02 UTC | 1h 59m |
| PSC581 | PSC | Montréal / St-Hubert Airport (CYHU) | St-Ferdinand Airport (CSH5) | 2026-09-11 21:32 UTC | 2026-09-11 21:59 UTC | 27m |
| TGCCC | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-09-11 21:38 UTC | 2026-09-11 21:58 UTC | 19m |
| EURO22 | EUR | Huntsville International-Carl T Jones Field (KHSV) | Western Carolina Regional Airport (KRHP) | 2026-09-11 21:33 UTC | 2026-09-11 21:56 UTC | 23m |
| N282LS |  | Albuquerque International Sunport Airport (KABQ) | Rafter P Airport (TA00) | 2026-09-11 20:33 UTC | 2026-09-11 21:55 UTC | 1h 22m |
| GIZMO11 | GIZ | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-09-11 21:16 UTC | 2026-09-11 21:55 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
