# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_03:27:45_UTC-green)

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

**Latest saved flight:** 2026-08-26 03:27:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 03:27:45 UTC

- **237,348** saved flights
- **72,372** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **237,348** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,857,440.5 tonnes** estimated CO2 emissions
- **165,648,724 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9501 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 3992 |
| 5 | American Airlines | 3854 |
| 6 | Southwest Airlines | 3612 |
| 7 | Delta Air Lines | 3033 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2282 |
| 10 | AZU | 2216 |
| 11 | Vueling | 2028 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1588 |
| 17 | AXM | 1580 |
| 18 | EJU | 1520 |
| 19 | QLK | 1513 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1425 |
| 22 | All Nippon Airways | 1408 |
| 23 | GLO | 1329 |
| 24 | WMT | 1324 |
| 25 | VIV | 1311 |
| 26 | PGT | 1295 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1268 |
| 29 | JetBlue | 1180 |
| 30 | AEE | 1175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197330 |
| 2 | 🇪🇸 ES | 15216 |
| 3 | 🇧🇷 BR | 13883 |
| 4 | 🇦🇺 AU | 13447 |
| 5 | 🇨🇦 CA | 13164 |
| 6 | 🇮🇹 IT | 12930 |
| 7 | 🇮🇳 IN | 12444 |
| 8 | 🇩🇪 DE | 11664 |
| 9 | 🇬🇧 GB | 11178 |
| 10 | 🇨🇴 CO | 10116 |
| 11 | 🇯🇵 JP | 9585 |
| 12 | 🇫🇷 FR | 9503 |
| 13 | 🇹🇷 TR | 7043 |
| 14 | 🇬🇷 GR | 6979 |
| 15 | 🇲🇽 MX | 6598 |
| 16 | 🇨🇭 CH | 6322 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇲🇾 MY | 4236 |
| 19 | 🇹🇭 TH | 4233 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3945 |
| 22 | 🇳🇿 NZ | 3280 |
| 23 | 🇵🇭 PH | 3261 |
| 24 | 🇬🇹 GT | 2974 |
| 25 | 🇰🇷 KR | 2780 |
| 26 | 🇭🇷 HR | 2734 |
| 27 | 🇲🇦 MA | 2396 |
| 28 | 🇲🇪 ME | 2205 |
| 29 | 🇳🇱 NL | 2125 |
| 30 | 🇮🇩 ID | 2067 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2889 |
| 4 | Tokyo International Airport |  | JP | 2855 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2369 |
| 10 | El Dorado International Airport |  | CO | 2274 |
| 11 | La Aurora Airport |  | GT | 2267 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1864 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1793 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1751 |
| 21 | Malpensa International Airport |  | IT | 1699 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1665 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1578 |
| 27 | Kuala Lumpur International Airport |  | MY | 1531 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1499 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1441 |
| 32 | Viracopos International Airport |  | BR | 1418 |
| 33 | Seattle-Tacoma International Airport |  | US | 1391 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 35 | Bengaluru International Airport |  | IN | 1385 |
| 36 | Don Mueang International Airport |  | TH | 1369 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1301 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 871 | 21m | 244 km | 3,667.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 601 | 1h 6m | 770 km | 7,983.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 601 | 24m | 225 km | 2,331.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 391 | 27m | 275 km | 1,852.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 344 | 44m | 555 km | 3,294.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 319 | 1h 7m | 706 km | 3,883.8 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 318 | 24m | 218 km | 1,198.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 317 | 22m | 55 km | 301.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 316 | 1h 40m | 1,156 km | 6,304.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 295 | 19m | 99 km | 505.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N40798 |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-08-26 02:43 UTC | 2026-08-26 03:27 UTC | 43m |
| ZKJMP | ZKJ | RNZAF Base Auckland-Whenuapai (NZWP) | RNZAF Base Auckland-Whenuapai (NZWP) | 2026-08-26 03:03 UTC | 2026-08-26 03:25 UTC | 21m |
| BC706 |  | North Island Nas (Halsey Field) Airport (KNZY) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-08-26 01:48 UTC | 2026-08-26 03:13 UTC | 1h 25m |
| N27SJ |  | Purdue University Airport (KLAF) | Lehigh Valley International Airport (KABE) | 2026-08-25 23:59 UTC | 2026-08-26 03:12 UTC | 3h 12m |
| HSDZT | HSD | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-08-26 02:55 UTC | 2026-08-26 03:11 UTC | 16m |
| N853AA |  | Palm Beach County Park Airport (KLNA) | Miami Executive Airport (KTMB) | 2026-08-26 02:20 UTC | 2026-08-26 03:09 UTC | 48m |
| N786WM |  | Merrill Field (PAMR) | Donlin Creek Airport (PFCR) | 2026-08-26 01:30 UTC | 2026-08-26 02:57 UTC | 1h 27m |
| N107UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-26 02:31 UTC | 2026-08-26 02:49 UTC | 18m |
| KYOTE50 | KYO | Sky Ranch At Carefree Airport (18AZ) | Sky Ranch At Carefree Airport (18AZ) | 2026-08-26 02:31 UTC | 2026-08-26 02:46 UTC | 15m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-08-26 02:12 UTC | 2026-08-26 02:44 UTC | 31m |
| CKS270 | CKS | Narita International Airport (RJAA) | Zhuhai Airport (ZGSD) | 2026-08-25 22:53 UTC | 2026-08-26 02:35 UTC | 3h 42m |
| CFSUG | CFS | CRK2 (CRK2) | Whitecourt Airport (CYZU) | 2026-08-26 02:06 UTC | 2026-08-26 02:35 UTC | 28m |
| AXM462 | AXM | Kuala Lumpur International Airport (WMKK) | Bentayan Airport (WIPY) | 2026-08-26 01:40 UTC | 2026-08-26 02:34 UTC | 54m |
| ZKFII | ZKF | Motiti Island Airport (NZOI) | Motiti Island Airport (NZOI) | 2026-08-26 02:33 UTC | 2026-08-26 02:33 UTC | 0m |
| KYOTE49 | KYO | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-26 02:29 UTC | 2026-08-26 02:30 UTC | 1m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-26 01:58 UTC | 2026-08-26 02:28 UTC | 30m |
| CEB907 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-26 02:05 UTC | 2026-08-26 02:27 UTC | 21m |
| MAS1268 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-08-26 02:15 UTC | 2026-08-26 02:26 UTC | 10m |
| AIC1HN | Air India | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-08-26 00:44 UTC | 2026-08-26 02:25 UTC | 1h 41m |
| AWA411 | AWA | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-08-26 01:58 UTC | 2026-08-26 02:25 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
