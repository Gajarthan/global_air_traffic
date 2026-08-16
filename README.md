# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_17:18:48_UTC-green)

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

**Latest saved flight:** 2026-08-16 17:18:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 17:18:48 UTC

- **205,343** saved flights
- **65,541** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,343** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,468,422.1 tonnes** estimated CO2 emissions
- **143,096,934 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8091 |
| 2 | SkyWest Airlines | 7371 |
| 3 | EJA | 3972 |
| 4 | IndiGo | 3518 |
| 5 | American Airlines | 3410 |
| 6 | Southwest Airlines | 3310 |
| 7 | Delta Air Lines | 2627 |
| 8 | ENY | 2558 |
| 9 | LATAM Airlines | 1927 |
| 10 | AZU | 1856 |
| 11 | Lufthansa | 1746 |
| 12 | Vueling | 1700 |
| 13 | WIF | 1655 |
| 14 | LXJ | 1615 |
| 15 | easyJet | 1419 |
| 16 | Swiss International | 1372 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1294 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1259 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1127 |
| 24 | GLO | 1106 |
| 25 | Air France | 1099 |
| 26 | PGT | 1095 |
| 27 | AEE | 1051 |
| 28 | JetBlue | 1051 |
| 29 | WMT | 1034 |
| 30 | CXK | 1014 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174381 |
| 2 | 🇪🇸 ES | 13134 |
| 3 | 🇧🇷 BR | 11749 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11321 |
| 6 | 🇮🇳 IN | 10978 |
| 7 | 🇮🇹 IT | 10701 |
| 8 | 🇩🇪 DE | 10169 |
| 9 | 🇬🇧 GB | 9585 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8141 |
| 12 | 🇨🇴 CO | 8114 |
| 13 | 🇬🇷 GR | 6054 |
| 14 | 🇹🇷 TR | 5810 |
| 15 | 🇲🇽 MX | 5761 |
| 16 | 🇨🇭 CH | 5499 |
| 17 | 🇳🇴 NO | 5125 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3452 |
| 20 | 🇵🇱 PL | 3389 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2584 |
| 25 | 🇰🇷 KR | 2504 |
| 26 | 🇭🇷 HR | 2197 |
| 27 | 🇲🇦 MA | 2069 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1724 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4307 |
| 2 | Denver International Airport |  | US | 3348 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2489 |
| 5 | Guaymaral Airport |  | CO | 2486 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2148 |
| 8 | Zurich Airport |  | CH | 2145 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2129 |
| 10 | La Aurora Airport |  | GT | 1975 |
| 11 | Chicago O'Hare International Airport |  | US | 1905 |
| 12 | El Dorado International Airport |  | CO | 1870 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1830 |
| 14 | Salt Lake City International Airport |  | US | 1814 |
| 15 | Congonhas Airport |  | BR | 1713 |
| 16 | Frankfurt am Main International Airport |  | DE | 1704 |
| 17 | Madrid Barajas International Airport |  | ES | 1611 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1568 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1560 |
| 20 | Capua Airport |  | IT | 1557 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1485 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1408 |
| 26 | Charlotte/Douglas International Airport |  | US | 1396 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1275 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1261 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1233 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1217 |
| 34 | Viracopos International Airport |  | BR | 1189 |
| 35 | Calgary International Airport |  | CA | 1160 |
| 36 | Reno/Tahoe International Airport |  | US | 1138 |
| 37 | Oslo Gardermoen Airport |  | NO | 1135 |
| 38 | Vitoria/Foronda Airport |  | ES | 1133 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1023 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 467 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 391 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 256 | 24m | 218 km | 964.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 247 | 19m | 99 km | 423.1 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 241 | 1h 37m | 1,156 km | 4,807.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 218 | 28m | 152 km | 569.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 17:02 UTC | 2026-08-16 17:18 UTC | 16m |
| EIN68R | Aer Lingus | Geneva Cointrin International Airport (LSGG) | Dublin Airport (EIDW) | 2026-08-16 15:19 UTC | 2026-08-16 17:12 UTC | 1h 53m |
| N4736Y |  | Cy Nunnally Memorial Airport (KD73) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 16:53 UTC | 2026-08-16 17:11 UTC | 18m |
| RFS713 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-16 16:25 UTC | 2026-08-16 17:06 UTC | 41m |
| CCDBA | CCD | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-08-16 16:54 UTC | 2026-08-16 17:06 UTC | 11m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-08-16 16:54 UTC | 2026-08-16 17:05 UTC | 11m |
| TGSZC | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-16 16:52 UTC | 2026-08-16 17:02 UTC | 9m |
| N2182H |  | University Airport (KEDU) | San Carlos Airport (KSQL) | 2026-08-16 16:16 UTC | 2026-08-16 17:01 UTC | 44m |
| N2593G |  | Shreveport Downtown Airport (KDTN) | LS90 (LS90) | 2026-08-16 14:25 UTC | 2026-08-16 17:00 UTC | 2h 35m |
| N579BJ |  | Santa Barbara Municipal Airport (KSBA) | Truckee-Tahoe Airport (KTRK) | 2026-08-16 16:05 UTC | 2026-08-16 16:55 UTC | 49m |
|  |  | Asheville Regional Airport (KAVL) | 4NC6 (4NC6) | 2026-08-16 16:52 UTC | 2026-08-16 16:53 UTC | 1m |
| N4102B |  | Reno/Tahoe International Airport (KRNO) | Yerington Municipal Airport (KO43) | 2026-08-16 16:29 UTC | 2026-08-16 16:53 UTC | 24m |
| N478CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 16:20 UTC | 2026-08-16 16:53 UTC | 32m |
| EDV4989 | EDV | Laguardia Airport (KLGA) | Northwest Florida Beaches International Airport (KECP) | 2026-08-16 14:41 UTC | 2026-08-16 16:52 UTC | 2h 10m |
| FDB1BM | flydubai | Sarajevo International Airport (LQSA) | Abumusa Island Airport (OIBA) | 2026-08-16 12:02 UTC | 2026-08-16 16:46 UTC | 4h 44m |
| N330V |  | Kintail Farm Airport (GA00) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 16:33 UTC | 2026-08-16 16:45 UTC | 12m |
| PRDBR | PRD | Campo de Marte Airport (SBMT) | Ubatuba Airport (SDUB) | 2026-08-16 16:21 UTC | 2026-08-16 16:43 UTC | 22m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-16 16:24 UTC | 2026-08-16 16:42 UTC | 17m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-16 15:26 UTC | 2026-08-16 16:39 UTC | 1h 13m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 16:24 UTC | 2026-08-16 16:39 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
