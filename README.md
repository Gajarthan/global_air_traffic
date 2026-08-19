# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_23:36:47_UTC-green)

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

**Latest saved flight:** 2026-08-19 23:36:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 23:36:47 UTC

- **217,756** saved flights
- **68,632** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,756** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,620,274.3 tonnes** estimated CO2 emissions
- **151,899,962 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8713 |
| 2 | SkyWest Airlines | 7798 |
| 3 | EJA | 4242 |
| 4 | IndiGo | 3693 |
| 5 | American Airlines | 3633 |
| 6 | Southwest Airlines | 3460 |
| 7 | Delta Air Lines | 2818 |
| 8 | ENY | 2695 |
| 9 | LATAM Airlines | 2065 |
| 10 | AZU | 1998 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1724 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1382 |
| 19 | EJU | 1355 |
| 20 | QLK | 1348 |
| 21 | Alaska Airlines | 1331 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1193 |
| 24 | GLO | 1187 |
| 25 | PGT | 1178 |
| 26 | Air France | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1109 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1089 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183782 |
| 2 | 🇪🇸 ES | 13942 |
| 3 | 🇧🇷 BR | 12580 |
| 4 | 🇦🇺 AU | 12195 |
| 5 | 🇨🇦 CA | 12012 |
| 6 | 🇮🇹 IT | 11559 |
| 7 | 🇮🇳 IN | 11502 |
| 8 | 🇩🇪 DE | 10765 |
| 9 | 🇬🇧 GB | 10214 |
| 10 | 🇨🇴 CO | 8954 |
| 11 | 🇯🇵 JP | 8872 |
| 12 | 🇫🇷 FR | 8666 |
| 13 | 🇬🇷 GR | 6347 |
| 14 | 🇹🇷 TR | 6257 |
| 15 | 🇲🇽 MX | 6081 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3596 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 3010 |
| 23 | 🇵🇭 PH | 2908 |
| 24 | 🇬🇹 GT | 2763 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4585 |
| 2 | Denver International Airport |  | US | 3561 |
| 3 | Tokyo International Airport |  | JP | 2663 |
| 4 | Indira Gandhi International Airport |  | IN | 2632 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2414 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2103 |
| 11 | El Dorado International Airport |  | CO | 2040 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1923 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1899 |
| 15 | Congonhas Airport |  | BR | 1838 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1614 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1601 |
| 22 | Macau International Airport |  | MO | 1563 |
| 23 | Malpensa International Airport |  | IT | 1534 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1517 |
| 25 | Charles de Gaulle International Airport |  | FR | 1493 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1381 |
| 28 | Kuala Lumpur International Airport |  | MY | 1378 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1330 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1299 |
| 33 | Seattle-Tacoma International Airport |  | US | 1293 |
| 34 | Viracopos International Airport |  | BR | 1276 |
| 35 | Calgary International Airport |  | CA | 1228 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1169 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 777 | 21m | 244 km | 3,271.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 535 | 1h 7m | 770 km | 7,107.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 509 | 24m | 225 km | 1,974.7 t |
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
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OXV | OXV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-19 23:25 UTC | 2026-08-19 23:36 UTC | 11m |
| ADY424 | ADY | Abu Dhabi International Airport (OMAA) | Almaza Air Force Base (HEAZ) | 2026-08-19 20:32 UTC | 2026-08-19 23:30 UTC | 2h 57m |
| LICHEN2 | LIC | 32AK (32AK) | Ladd Army Air Field (PAFB) | 2026-08-19 23:06 UTC | 2026-08-19 23:28 UTC | 21m |
| N43LA |  | Hurst Airport (69PA) | Deck Airport (K9D4) | 2026-08-19 21:54 UTC | 2026-08-19 23:28 UTC | 1h 33m |
| N866SL |  | Zamperini Field (KTOA) | Santa Monica Municipal Airport (KSMO) | 2026-08-19 23:01 UTC | 2026-08-19 23:22 UTC | 21m |
| BLIND63 | BLI | City Of Colorado Springs Municipal Airport (KCOS) | Perry Park Airport (CO93) | 2026-08-19 23:00 UTC | 2026-08-19 23:21 UTC | 21m |
| EURO43 | EUR | Pierce Airport (TE10) | Hawk Ranch Airport (1TX9) | 2026-08-19 22:55 UTC | 2026-08-19 23:19 UTC | 24m |
| TKR103 | TKR | Coeur D'Alene Airport (KCOE) | Coeur D'Alene Airport (KCOE) | 2026-08-19 22:50 UTC | 2026-08-19 23:19 UTC | 28m |
| N703AC |  | Iowa City Municipal Airport (KIOW) | Dubuque Regional Airport (KDBQ) | 2026-08-19 22:36 UTC | 2026-08-19 23:17 UTC | 41m |
| FPP | FPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-19 23:02 UTC | 2026-08-19 23:15 UTC | 12m |
| N2745G |  | Rock Rapids Municipal Airport (KRRQ) | Chan Gurney Municipal Airport (KYKN) | 2026-08-19 22:53 UTC | 2026-08-19 23:15 UTC | 21m |
| ZJI | ZJI | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-08-19 22:27 UTC | 2026-08-19 23:08 UTC | 41m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 22:58 UTC | 2026-08-19 23:05 UTC | 7m |
| N607DB |  | Ryan Aerodrome (7TX7) | Dallas Love Field (KDAL) | 2026-08-19 21:57 UTC | 2026-08-19 23:02 UTC | 1h 4m |
| CFYUL | CFY | Seattle Paine Field International Airport (KPAE) | MT88 (MT88) | 2026-08-19 22:14 UTC | 2026-08-19 23:00 UTC | 45m |
| WSN8 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-08-19 22:19 UTC | 2026-08-19 22:57 UTC | 38m |
| N671PC |  | Las Cruces International Airport (KLRU) | Grant County Airport (KSVC) | 2026-08-19 22:36 UTC | 2026-08-19 22:54 UTC | 17m |
| JANET10 | JAN | China Lake Naws (Armitage Field) Airport (KNID) | Edwards Afb Airport (KEDW) | 2026-08-19 22:40 UTC | 2026-08-19 22:53 UTC | 13m |
| TKR137 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 22:47 UTC | 2026-08-19 22:52 UTC | 5m |
| DAL1254 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-19 21:20 UTC | 2026-08-19 22:50 UTC | 1h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
