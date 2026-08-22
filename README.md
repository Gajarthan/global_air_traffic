# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_01:33:36_UTC-green)

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

**Latest saved flight:** 2026-08-22 01:33:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 01:33:36 UTC

- **224,345** saved flights
- **69,987** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,345** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,702,267.4 tonnes** estimated CO2 emissions
- **156,653,180 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8987 |
| 2 | SkyWest Airlines | 7992 |
| 3 | EJA | 4351 |
| 4 | IndiGo | 3783 |
| 5 | American Airlines | 3704 |
| 6 | Southwest Airlines | 3520 |
| 7 | Delta Air Lines | 2877 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2139 |
| 10 | AZU | 2071 |
| 11 | Vueling | 1890 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1776 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1470 |
| 18 | United Airlines | 1416 |
| 19 | QLK | 1409 |
| 20 | EJU | 1405 |
| 21 | Alaska Airlines | 1361 |
| 22 | All Nippon Airways | 1337 |
| 23 | GLO | 1243 |
| 24 | PGT | 1230 |
| 25 | VIV | 1227 |
| 26 | Air France | 1215 |
| 27 | WMT | 1194 |
| 28 | Wizz Air | 1154 |
| 29 | JetBlue | 1126 |
| 30 | AEE | 1117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188513 |
| 2 | 🇪🇸 ES | 14364 |
| 3 | 🇧🇷 BR | 13044 |
| 4 | 🇦🇺 AU | 12685 |
| 5 | 🇨🇦 CA | 12452 |
| 6 | 🇮🇹 IT | 11976 |
| 7 | 🇮🇳 IN | 11797 |
| 8 | 🇩🇪 DE | 11028 |
| 9 | 🇬🇧 GB | 10515 |
| 10 | 🇨🇴 CO | 9249 |
| 11 | 🇯🇵 JP | 9076 |
| 12 | 🇫🇷 FR | 8934 |
| 13 | 🇹🇷 TR | 6539 |
| 14 | 🇬🇷 GR | 6531 |
| 15 | 🇲🇽 MX | 6243 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5561 |
| 18 | 🇲🇾 MY | 3895 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3780 |
| 21 | 🇵🇱 PL | 3717 |
| 22 | 🇳🇿 NZ | 3113 |
| 23 | 🇵🇭 PH | 3038 |
| 24 | 🇬🇹 GT | 2848 |
| 25 | 🇰🇷 KR | 2661 |
| 26 | 🇭🇷 HR | 2503 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇳🇱 NL | 1992 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1911 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4705 |
| 2 | Denver International Airport |  | US | 3666 |
| 3 | Tokyo International Airport |  | JP | 2721 |
| 4 | Indira Gandhi International Airport |  | IN | 2714 |
| 5 | Guaymaral Airport |  | CO | 2628 |
| 6 | Harry Reid International Airport |  | US | 2462 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2268 |
| 10 | La Aurora Airport |  | GT | 2171 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1972 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1925 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1812 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1717 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1675 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1666 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1633 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1578 |
| 24 | Malpensa International Airport |  | IT | 1570 |
| 25 | Charles de Gaulle International Airport |  | FR | 1548 |
| 26 | Charlotte/Douglas International Airport |  | US | 1482 |
| 27 | Ninoy Aquino International Airport |  | PH | 1448 |
| 28 | Kuala Lumpur International Airport |  | MY | 1422 |
| 29 | Barcelona International Airport |  | ES | 1385 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1365 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1331 |
| 33 | Seattle-Tacoma International Airport |  | US | 1325 |
| 34 | Viracopos International Airport |  | BR | 1321 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1277 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Don Mueang International Airport |  | TH | 1242 |
| 39 | Vitoria/Foronda Airport |  | ES | 1240 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 807 | 21m | 244 km | 3,398.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 558 | 1h 7m | 770 km | 7,412.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 542 | 24m | 225 km | 2,102.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 283 | 1h 39m | 1,156 km | 5,645.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 279 | 24m | 218 km | 1,051.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 279 | 19m | 99 km | 477.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 257 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BCD | BCD | YBYL (YBYL) | Gold Coast Airport (YBCG) | 2026-08-22 00:30 UTC | 2026-08-22 01:33 UTC | 1h 2m |
| TKR105 | TKR | Coeur D'Alene Airport (KCOE) | Boundary County Airport (K65S) | 2026-08-22 01:17 UTC | 2026-08-22 01:30 UTC | 12m |
| CGDTF | CGD | Victoria International Airport (CYYJ) | William R Fairchild International Airport (KCLM) | 2026-08-22 01:12 UTC | 2026-08-22 01:29 UTC | 16m |
| N5872H |  | Bradley Lake Hydroelectric Project Airstrip (0AK7) | Bear Cove Farm Airport (46AK) | 2026-08-22 00:00 UTC | 2026-08-22 01:16 UTC | 1h 16m |
| KMI713 | KMI | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-08-22 00:26 UTC | 2026-08-22 01:14 UTC | 48m |
| ASH6334 | ASH | George Bush Intcntl/Houston Airport (KIAH) | Okc Will Rogers International Airport (KOKC) | 2026-08-21 23:56 UTC | 2026-08-22 00:59 UTC | 1h 2m |
| TORA21 | TOR | Flying E Ranch Airport (OK16) | Tulsa International Airport (KTUL) | 2026-08-22 00:26 UTC | 2026-08-22 00:57 UTC | 30m |
| 8L8 |  | Sydney Bankstown Airport (YSBK) | Mudgee Airport (YMDG) | 2026-08-22 00:33 UTC | 2026-08-22 00:57 UTC | 23m |
| N590ML |  | Henderson Executive Airport (KHND) | Harris River Ranch Airport (9CA7) | 2026-08-22 00:05 UTC | 2026-08-22 00:55 UTC | 49m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-22 00:36 UTC | 2026-08-22 00:54 UTC | 18m |
| MLM005 | MLM | Al Maktoum International Airport (OMDW) | Ibiza Airport (LEIB) | 2026-08-21 17:29 UTC | 2026-08-22 00:53 UTC | 7h 23m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-22 00:43 UTC | 2026-08-22 00:50 UTC | 7m |
| RXA6518 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-08-22 00:17 UTC | 2026-08-22 00:50 UTC | 32m |
| CWA924 | CWA | Edmonton International Airport (CYEG) | Swan Hills Airport (CEM5) | 2026-08-22 00:18 UTC | 2026-08-22 00:46 UTC | 28m |
| OXM | OXM | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-22 00:35 UTC | 2026-08-22 00:45 UTC | 10m |
| UAL1855 | United Airlines | Los Angeles International Airport (KLAX) | Newark Liberty International Airport (KEWR) | 2026-08-21 19:27 UTC | 2026-08-22 00:44 UTC | 5h 17m |
| N902F |  | Ontario International Airport (KONT) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-21 23:53 UTC | 2026-08-22 00:43 UTC | 49m |
| CGFVB | CGF | Boundary Bay Airport (CZBB) | Pitt Meadows Airport (CYPK) | 2026-08-21 23:53 UTC | 2026-08-22 00:40 UTC | 47m |
| N85VB |  | Skwentna Airport (PASW) | Merrill Field (PAMR) | 2026-08-22 00:06 UTC | 2026-08-22 00:39 UTC | 32m |
| N96BM |  | 8CA5 (8CA5) | Firebaugh Airport (KF34) | 2026-08-21 23:04 UTC | 2026-08-22 00:37 UTC | 1h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
