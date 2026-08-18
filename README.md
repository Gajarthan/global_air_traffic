# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_21:46:29_UTC-green)

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

**Latest saved flight:** 2026-08-18 21:46:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 21:46:29 UTC

- **213,618** saved flights
- **67,574** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,618** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,569,006.8 tonnes** estimated CO2 emissions
- **148,927,930 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8480 |
| 2 | SkyWest Airlines | 7673 |
| 3 | EJA | 4168 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3572 |
| 6 | Southwest Airlines | 3417 |
| 7 | Delta Air Lines | 2752 |
| 8 | ENY | 2652 |
| 9 | LATAM Airlines | 2012 |
| 10 | AZU | 1951 |
| 11 | Vueling | 1789 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1686 |
| 15 | easyJet | 1482 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1358 |
| 19 | QLK | 1320 |
| 20 | EJU | 1315 |
| 21 | Alaska Airlines | 1310 |
| 22 | All Nippon Airways | 1287 |
| 23 | VIV | 1177 |
| 24 | GLO | 1159 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1088 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180636 |
| 2 | 🇪🇸 ES | 13677 |
| 3 | 🇧🇷 BR | 12282 |
| 4 | 🇦🇺 AU | 11966 |
| 5 | 🇨🇦 CA | 11805 |
| 6 | 🇮🇳 IN | 11356 |
| 7 | 🇮🇹 IT | 11262 |
| 8 | 🇩🇪 DE | 10536 |
| 9 | 🇬🇧 GB | 9963 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8674 |
| 12 | 🇫🇷 FR | 8485 |
| 13 | 🇬🇷 GR | 6261 |
| 14 | 🇹🇷 TR | 6126 |
| 15 | 🇲🇽 MX | 5988 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3676 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2947 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2728 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2152 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1848 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4496 |
| 2 | Denver International Airport |  | US | 3499 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2559 |
| 6 | Harry Reid International Airport |  | US | 2387 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2202 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2074 |
| 11 | El Dorado International Airport |  | CO | 1974 |
| 12 | Chicago O'Hare International Airport |  | US | 1974 |
| 13 | Salt Lake City International Airport |  | US | 1890 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1886 |
| 15 | Congonhas Airport |  | BR | 1790 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1616 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1612 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1604 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1561 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Malpensa International Airport |  | IT | 1491 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 25 | Charles de Gaulle International Airport |  | FR | 1472 |
| 26 | Charlotte/Douglas International Airport |  | US | 1439 |
| 27 | Kuala Lumpur International Airport |  | MY | 1357 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1316 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1301 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1285 |
| 33 | Seattle-Tacoma International Airport |  | US | 1267 |
| 34 | Viracopos International Airport |  | BR | 1247 |
| 35 | Calgary International Airport |  | CA | 1211 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1159 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1046 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 759 | 21m | 244 km | 3,195.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 482 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 455 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 266 | 19m | 99 km | 455.6 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 240 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 229 | 1h 49m | 1,304 km | 5,151.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N160WP |  | Atlanta Regional Falcon Field (KFFC) | Thomaston-Upson County Airport (KOPN) | 2026-08-18 21:22 UTC | 2026-08-18 21:46 UTC | 23m |
| N798BP |  | Sky River Ranch Airport (WA78) | Sky River Ranch Airport (WA78) | 2026-08-18 20:28 UTC | 2026-08-18 21:44 UTC | 1h 15m |
| N26BQ |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-18 21:20 UTC | 2026-08-18 21:43 UTC | 22m |
| SXS5VF | SXS | Dublin Airport (EIDW) | Kaklic Airport (LTFA) | 2026-08-18 18:28 UTC | 2026-08-18 21:43 UTC | 3h 14m |
| N402MT |  | Detroit Metro Wayne County Airport (KDTW) | Auburn University Regional Airport (KAUO) | 2026-08-18 20:00 UTC | 2026-08-18 21:41 UTC | 1h 41m |
| N5469K |  | K3M3 (K3M3) | Flying G Ranch Airport (86GA) | 2026-08-18 21:29 UTC | 2026-08-18 21:39 UTC | 10m |
| SHED61 | SHE | TA29 (TA29) | Four Square Ranch Airport (3TA0) | 2026-08-18 21:25 UTC | 2026-08-18 21:37 UTC | 11m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-08-18 10:29 UTC | 2026-08-18 21:33 UTC | 11h 3m |
| N810DA |  | David Wayne Hooks Memorial Airport (KDWH) | Huntsville Municipal Airport (KUTS) | 2026-08-18 20:59 UTC | 2026-08-18 21:33 UTC | 33m |
| N172YA |  | Somerset Airport (KSMQ) | Central Jersey Regional Airport (K47N) | 2026-08-18 20:55 UTC | 2026-08-18 21:28 UTC | 32m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-18 21:22 UTC | 2026-08-18 21:27 UTC | 4m |
| URSA10 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-18 20:28 UTC | 2026-08-18 21:25 UTC | 57m |
| N294NG |  | Ziggy's Airport (0ID1) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-18 19:24 UTC | 2026-08-18 21:23 UTC | 1h 59m |
| LXJ437 | LXJ | Los Angeles International Airport (KLAX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-18 20:32 UTC | 2026-08-18 21:18 UTC | 45m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-18 19:24 UTC | 2026-08-18 21:18 UTC | 1h 54m |
| SAMU13 | SAM | Avignon-Caumont Airport (LFMV) | Marseille Provence Airport (LFML) | 2026-08-18 20:56 UTC | 2026-08-18 21:18 UTC | 21m |
| URSA19 | URS | Ladd Army Air Field (PAFB) | Gold King Creek Airport (PAAN) | 2026-08-18 20:11 UTC | 2026-08-18 21:16 UTC | 1h 5m |
| N90422 |  | Seattle Paine Field International Airport (KPAE) | Boeing Field/King County International Airport (KBFI) | 2026-08-18 21:06 UTC | 2026-08-18 21:14 UTC | 7m |
| N8454H |  | Monmouth Executive Airport (KBLM) | Old Bridge Airport (K3N6) | 2026-08-18 21:00 UTC | 2026-08-18 21:12 UTC | 12m |
| CKS221 | CKS | East Midlands Airport (EGNX) | Zhuhai Airport (ZGSD) | 2026-08-18 09:51 UTC | 2026-08-18 21:10 UTC | 11h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
