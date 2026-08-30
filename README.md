# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_07:05:56_UTC-green)

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

**Latest saved flight:** 2026-08-30 07:05:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-30 07:05:56 UTC

- **241,586** saved flights
- **73,275** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,586** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,908,024.8 tonnes** estimated CO2 emissions
- **168,581,150 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9691 |
| 2 | SkyWest Airlines | 8478 |
| 3 | EJA | 4672 |
| 4 | IndiGo | 4070 |
| 5 | American Airlines | 3891 |
| 6 | Southwest Airlines | 3633 |
| 7 | Delta Air Lines | 3080 |
| 8 | ENY | 2915 |
| 9 | LATAM Airlines | 2315 |
| 10 | AZU | 2243 |
| 11 | Vueling | 2076 |
| 12 | Lufthansa | 1942 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1870 |
| 15 | easyJet | 1685 |
| 16 | Swiss International | 1631 |
| 17 | AXM | 1599 |
| 18 | EJU | 1548 |
| 19 | QLK | 1544 |
| 20 | United Airlines | 1517 |
| 21 | Alaska Airlines | 1444 |
| 22 | All Nippon Airways | 1431 |
| 23 | WMT | 1359 |
| 24 | GLO | 1347 |
| 25 | VIV | 1323 |
| 26 | PGT | 1322 |
| 27 | Air France | 1320 |
| 28 | Wizz Air | 1303 |
| 29 | JetBlue | 1197 |
| 30 | AEE | 1195 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200211 |
| 2 | 🇪🇸 ES | 15531 |
| 3 | 🇧🇷 BR | 14071 |
| 4 | 🇦🇺 AU | 13710 |
| 5 | 🇨🇦 CA | 13444 |
| 6 | 🇮🇹 IT | 13217 |
| 7 | 🇮🇳 IN | 12670 |
| 8 | 🇩🇪 DE | 11922 |
| 9 | 🇬🇧 GB | 11404 |
| 10 | 🇨🇴 CO | 10395 |
| 11 | 🇫🇷 FR | 9733 |
| 12 | 🇯🇵 JP | 9698 |
| 13 | 🇹🇷 TR | 7169 |
| 14 | 🇬🇷 GR | 7117 |
| 15 | 🇲🇽 MX | 6669 |
| 16 | 🇨🇭 CH | 6479 |
| 17 | 🇳🇴 NO | 5950 |
| 18 | 🇹🇭 TH | 4386 |
| 19 | 🇲🇾 MY | 4285 |
| 20 | 🇿🇦 ZA | 4221 |
| 21 | 🇵🇱 PL | 4049 |
| 22 | 🇳🇿 NZ | 3326 |
| 23 | 🇵🇭 PH | 3317 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2854 |
| 26 | 🇭🇷 HR | 2790 |
| 27 | 🇲🇦 MA | 2439 |
| 28 | 🇲🇪 ME | 2255 |
| 29 | 🇳🇱 NL | 2189 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4990 |
| 2 | Denver International Airport |  | US | 3898 |
| 3 | Indira Gandhi International Airport |  | IN | 2950 |
| 4 | Tokyo International Airport |  | JP | 2887 |
| 5 | Guaymaral Airport |  | CO | 2701 |
| 6 | Harry Reid International Airport |  | US | 2568 |
| 7 | Zurich Airport |  | CH | 2536 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2471 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2407 |
| 10 | El Dorado International Airport |  | CO | 2355 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2148 |
| 13 | Salt Lake City International Airport |  | US | 2130 |
| 14 | Congonhas Airport |  | BR | 2056 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2000 |
| 16 | Frankfurt am Main International Airport |  | DE | 1912 |
| 17 | Capua Airport |  | IT | 1906 |
| 18 | Madrid Barajas International Airport |  | ES | 1901 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1814 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1777 |
| 21 | Malpensa International Airport |  | IT | 1730 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1703 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1697 |
| 24 | Charles de Gaulle International Airport |  | FR | 1690 |
| 25 | Macau International Airport |  | MO | 1615 |
| 26 | Ninoy Aquino International Airport |  | PH | 1611 |
| 27 | Charlotte/Douglas International Airport |  | US | 1547 |
| 28 | Kuala Lumpur International Airport |  | MY | 1546 |
| 29 | Barcelona International Airport |  | ES | 1540 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1538 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1458 |
| 32 | Viracopos International Airport |  | BR | 1435 |
| 33 | Don Mueang International Airport |  | TH | 1412 |
| 34 | Seattle-Tacoma International Airport |  | US | 1410 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1404 |
| 37 | Calgary International Airport |  | CA | 1388 |
| 38 | Oslo Gardermoen Airport |  | NO | 1354 |
| 39 | Vancouver International Airport |  | CA | 1337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1321 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1094 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 890 | 21m | 244 km | 3,747.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 615 | 24m | 225 km | 2,385.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 612 | 1h 6m | 770 km | 8,129.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 380 | 1h 50m | 1,423 km | 9,325.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 369 | 44m | 555 km | 3,533.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 350 | 44m | 241 km | 1,453.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 330 | 24m | 218 km | 1,243.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 284 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 272 | 19m | 144 km | 676.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 259 | 1h 50m | 1,304 km | 5,826.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VLJ000P | VLJ | London Stansted Airport (EGSS) | Brussels Airport (EBBR) | 2026-08-30 06:26 UTC | 2026-08-30 07:05 UTC | 39m |
| IGO1253 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-08-30 05:52 UTC | 2026-08-30 07:05 UTC | 1h 12m |
| OUC | OUC | YCVA (YCVA) | YCVA (YCVA) | 2026-08-30 06:38 UTC | 2026-08-30 06:40 UTC | 2m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-30 05:40 UTC | 2026-08-30 06:34 UTC | 54m |
| HDB1 | HDB | Dubai International Airport (OMDB) | Al Minhad Air Base (OMDM) | 2026-08-30 06:05 UTC | 2026-08-30 06:32 UTC | 27m |
| SWR1PM | Swiss International | Stockholm-Arlanda Airport (ESSA) | Zurich Airport (LSZH) | 2026-08-30 04:21 UTC | 2026-08-30 06:32 UTC | 2h 11m |
| CAN14 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-30 06:16 UTC | 2026-08-30 06:28 UTC | 11m |
| XCN81 | XCN | Vey Sheep Ranch Airport (37OR) | Rome State Airport (KREO) | 2026-08-30 05:44 UTC | 2026-08-30 06:25 UTC | 41m |
| VOZ853 | Virgin Australia | Melbourne International Airport (YMML) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-30 05:16 UTC | 2026-08-30 06:19 UTC | 1h 3m |
| SWR47W | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-08-30 05:10 UTC | 2026-08-30 06:15 UTC | 1h 5m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-30 05:33 UTC | 2026-08-30 06:14 UTC | 40m |
| NVP | NVP | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-08-30 05:43 UTC | 2026-08-30 06:12 UTC | 29m |
| RXA6832 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-08-30 05:36 UTC | 2026-08-30 06:11 UTC | 34m |
| 5YSLP |  | Nairobi Wilson Airport (HKNW) | Jomo Kenyatta International Airport (HKJK) | 2026-08-30 05:52 UTC | 2026-08-30 06:11 UTC | 18m |
| RXA6673 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-08-30 05:19 UTC | 2026-08-30 06:11 UTC | 51m |
| SDG234 | SDG | Hindon Airport (VIDX) | Ludhiana Airport (VILD) | 2026-08-30 05:36 UTC | 2026-08-30 06:05 UTC | 29m |
| 5YJMN |  | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-30 05:47 UTC | 2026-08-30 06:05 UTC | 17m |
| CFG8KY | CFG | Frankfurt am Main International Airport (EDDF) | Sinj Glider Airport (LDSS) | 2026-08-30 04:56 UTC | 2026-08-30 06:05 UTC | 1h 9m |
| CEB903 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-30 05:42 UTC | 2026-08-30 06:03 UTC | 21m |
| EWG7KP | EWG | Hamburg Airport (EDDH) | Tortoli' / Arbatax Airport (LIET) | 2026-08-30 04:01 UTC | 2026-08-30 06:02 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
