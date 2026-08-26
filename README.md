# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_23:12:02_UTC-green)

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

**Latest saved flight:** 2026-08-26 23:12:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 23:12:02 UTC

- **239,641** saved flights
- **72,838** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **239,641** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,887,228.0 tonnes** estimated CO2 emissions
- **167,375,538 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9622 |
| 2 | SkyWest Airlines | 8415 |
| 3 | EJA | 4638 |
| 4 | IndiGo | 4038 |
| 5 | American Airlines | 3873 |
| 6 | Southwest Airlines | 3616 |
| 7 | Delta Air Lines | 3053 |
| 8 | ENY | 2896 |
| 9 | LATAM Airlines | 2298 |
| 10 | AZU | 2231 |
| 11 | Vueling | 2061 |
| 12 | Lufthansa | 1935 |
| 13 | WIF | 1901 |
| 14 | LXJ | 1860 |
| 15 | easyJet | 1669 |
| 16 | Swiss International | 1611 |
| 17 | AXM | 1591 |
| 18 | EJU | 1536 |
| 19 | QLK | 1528 |
| 20 | United Airlines | 1512 |
| 21 | Alaska Airlines | 1432 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1348 |
| 24 | GLO | 1336 |
| 25 | VIV | 1316 |
| 26 | Air France | 1310 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1284 |
| 29 | JetBlue | 1189 |
| 30 | AEE | 1188 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 198611 |
| 2 | 🇪🇸 ES | 15411 |
| 3 | 🇧🇷 BR | 13978 |
| 4 | 🇦🇺 AU | 13585 |
| 5 | 🇨🇦 CA | 13310 |
| 6 | 🇮🇹 IT | 13109 |
| 7 | 🇮🇳 IN | 12578 |
| 8 | 🇩🇪 DE | 11837 |
| 9 | 🇬🇧 GB | 11318 |
| 10 | 🇨🇴 CO | 10248 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9652 |
| 13 | 🇹🇷 TR | 7116 |
| 14 | 🇬🇷 GR | 7061 |
| 15 | 🇲🇽 MX | 6625 |
| 16 | 🇨🇭 CH | 6427 |
| 17 | 🇳🇴 NO | 5925 |
| 18 | 🇹🇭 TH | 4338 |
| 19 | 🇲🇾 MY | 4264 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 3986 |
| 22 | 🇵🇭 PH | 3294 |
| 23 | 🇳🇿 NZ | 3293 |
| 24 | 🇬🇹 GT | 3004 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2771 |
| 27 | 🇲🇦 MA | 2426 |
| 28 | 🇲🇪 ME | 2244 |
| 29 | 🇳🇱 NL | 2172 |
| 30 | 🇮🇩 ID | 2103 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4955 |
| 2 | Denver International Airport |  | US | 3867 |
| 3 | Indira Gandhi International Airport |  | IN | 2927 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2546 |
| 7 | Zurich Airport |  | CH | 2510 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2456 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2393 |
| 10 | El Dorado International Airport |  | CO | 2312 |
| 11 | La Aurora Airport |  | GT | 2292 |
| 12 | Chicago O'Hare International Airport |  | US | 2141 |
| 13 | Salt Lake City International Airport |  | US | 2106 |
| 14 | Congonhas Airport |  | BR | 2039 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1995 |
| 16 | Frankfurt am Main International Airport |  | DE | 1898 |
| 17 | Capua Airport |  | IT | 1891 |
| 18 | Madrid Barajas International Airport |  | ES | 1881 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1806 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1764 |
| 21 | Malpensa International Airport |  | IT | 1719 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1691 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1676 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1598 |
| 27 | Kuala Lumpur International Airport |  | MY | 1541 |
| 28 | Charlotte/Douglas International Airport |  | US | 1537 |
| 29 | Barcelona International Airport |  | ES | 1525 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1516 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1449 |
| 32 | Viracopos International Airport |  | BR | 1429 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1400 |
| 35 | Seattle-Tacoma International Airport |  | US | 1395 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1393 |
| 37 | Calgary International Airport |  | CA | 1375 |
| 38 | Oslo Gardermoen Airport |  | NO | 1345 |
| 39 | Vancouver International Airport |  | CA | 1315 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 881 | 21m | 244 km | 3,709.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 613 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 541 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 396 | 27m | 275 km | 1,876.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 375 | 1h 50m | 1,423 km | 9,203.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 347 | 44m | 241 km | 1,441.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 326 | 24m | 218 km | 1,228.2 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 319 | 22m | 55 km | 303.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 257 | 1h 50m | 1,304 km | 5,781.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LOST56 | LOS | Los Alamitos Army Air Field (KSLI) | Lake Tahoe Airport (KTVL) | 2026-08-26 22:06 UTC | 2026-08-26 23:12 UTC | 1h 5m |
| N585M |  | Spirit Of St Louis Airport (KSUS) | Des Moines International Airport (KDSM) | 2026-08-26 22:31 UTC | 2026-08-26 23:09 UTC | 38m |
| N5276P |  | Palo Alto Airport (KPAO) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-26 22:26 UTC | 2026-08-26 23:09 UTC | 42m |
| N651KC |  | John Wayne/Orange County Airport (KSNA) | John Wayne/Orange County Airport (KSNA) | 2026-08-26 22:30 UTC | 2026-08-26 23:04 UTC | 34m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-26 22:41 UTC | 2026-08-26 22:57 UTC | 16m |
| N326PA |  | Kansas City International Airport (KMCI) | Plattsmouth Municipal/Douglas V Duey Field (KPMV) | 2026-08-26 22:24 UTC | 2026-08-26 22:56 UTC | 32m |
| GH70 |  | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-26 22:28 UTC | 2026-08-26 22:56 UTC | 28m |
| RFS735 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-26 22:36 UTC | 2026-08-26 22:55 UTC | 19m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Grand Junction Regional Airport (KGJT) | 2026-08-26 22:00 UTC | 2026-08-26 22:55 UTC | 55m |
| N636EM |  | Dupage Airport (KDPA) | IS80 (IS80) | 2026-08-26 22:06 UTC | 2026-08-26 22:52 UTC | 45m |
| SFE2 | SFE | XS89 (XS89) | Bud Dryden Airport (TX05) | 2026-08-26 22:24 UTC | 2026-08-26 22:51 UTC | 27m |
| AER930 | AER | King Salmon Airport (PAKN) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-26 21:49 UTC | 2026-08-26 22:50 UTC | 1h 1m |
| N825AV |  | Meadows Field (KBFL) | Palm Springs International Airport (KPSP) | 2026-08-26 22:20 UTC | 2026-08-26 22:49 UTC | 29m |
| OXF9864 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-08-26 22:15 UTC | 2026-08-26 22:45 UTC | 29m |
| N26CF |  | Johnson Airport (3AK4) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-26 22:10 UTC | 2026-08-26 22:44 UTC | 33m |
| TKR914 | TKR | Mc Clellan Airfield (KMCC) | Fallon Nas (Van Voorhis Field) Airport (KNFL) | 2026-08-26 22:20 UTC | 2026-08-26 22:44 UTC | 23m |
| SNAP07 | SNA | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Swift Current Airport (CYYN) | 2026-08-26 22:22 UTC | 2026-08-26 22:42 UTC | 20m |
| N619FB |  | North Las Vegas Airport (KVGT) | Henderson Executive Airport (KHND) | 2026-08-26 22:30 UTC | 2026-08-26 22:42 UTC | 12m |
| BOX724 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-26 06:49 UTC | 2026-08-26 22:39 UTC | 15h 49m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-08-26 11:02 UTC | 2026-08-26 22:35 UTC | 11h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
