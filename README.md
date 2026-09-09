# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_15:11:16_UTC-green)

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

**Latest saved flight:** 2026-09-09 15:11:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 15:11:16 UTC

- **252,590** saved flights
- **75,639** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,590** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,043,246.8 tonnes** estimated CO2 emissions
- **176,420,105 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10099 |
| 2 | SkyWest Airlines | 8814 |
| 3 | EJA | 4877 |
| 4 | IndiGo | 4234 |
| 5 | American Airlines | 4025 |
| 6 | Southwest Airlines | 3736 |
| 7 | Delta Air Lines | 3190 |
| 8 | ENY | 3012 |
| 9 | LATAM Airlines | 2429 |
| 10 | AZU | 2347 |
| 11 | Vueling | 2147 |
| 12 | WIF | 2023 |
| 13 | Lufthansa | 1993 |
| 14 | LXJ | 1969 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1699 |
| 17 | AXM | 1630 |
| 18 | QLK | 1622 |
| 19 | EJU | 1618 |
| 20 | United Airlines | 1573 |
| 21 | Alaska Airlines | 1505 |
| 22 | All Nippon Airways | 1478 |
| 23 | WMT | 1433 |
| 24 | GLO | 1401 |
| 25 | PGT | 1386 |
| 26 | VIV | 1381 |
| 27 | Air France | 1378 |
| 28 | Wizz Air | 1375 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209542 |
| 2 | 🇪🇸 ES | 16119 |
| 3 | 🇧🇷 BR | 14721 |
| 4 | 🇦🇺 AU | 14381 |
| 5 | 🇨🇦 CA | 14032 |
| 6 | 🇮🇹 IT | 13832 |
| 7 | 🇮🇳 IN | 13237 |
| 8 | 🇩🇪 DE | 12381 |
| 9 | 🇬🇧 GB | 11823 |
| 10 | 🇨🇴 CO | 11155 |
| 11 | 🇫🇷 FR | 10164 |
| 12 | 🇯🇵 JP | 9922 |
| 13 | 🇹🇷 TR | 7553 |
| 14 | 🇬🇷 GR | 7405 |
| 15 | 🇲🇽 MX | 6962 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6251 |
| 18 | 🇹🇭 TH | 4548 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4209 |
| 22 | 🇳🇿 NZ | 3450 |
| 23 | 🇵🇭 PH | 3427 |
| 24 | 🇬🇹 GT | 3143 |
| 25 | 🇰🇷 KR | 2914 |
| 26 | 🇭🇷 HR | 2904 |
| 27 | 🇲🇦 MA | 2552 |
| 28 | 🇲🇪 ME | 2376 |
| 29 | 🇳🇱 NL | 2277 |
| 30 | 🇮🇩 ID | 2162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5204 |
| 2 | Denver International Airport |  | US | 4081 |
| 3 | Indira Gandhi International Airport |  | IN | 3066 |
| 4 | Tokyo International Airport |  | JP | 2960 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2681 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2579 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2557 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2397 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2201 |
| 14 | Congonhas Airport |  | BR | 2159 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2075 |
| 16 | Capua Airport |  | IT | 1993 |
| 17 | Madrid Barajas International Airport |  | ES | 1983 |
| 18 | Frankfurt am Main International Airport |  | DE | 1963 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1890 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1835 |
| 21 | Malpensa International Airport |  | IT | 1814 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1772 |
| 23 | Charles de Gaulle International Airport |  | FR | 1772 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1759 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1680 |
| 26 | Ninoy Aquino International Airport |  | PH | 1674 |
| 27 | Macau International Airport |  | MO | 1667 |
| 28 | Barcelona International Airport |  | ES | 1591 |
| 29 | Charlotte/Douglas International Airport |  | US | 1590 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1551 |
| 32 | Viracopos International Airport |  | BR | 1507 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1464 |
| 35 | Don Mueang International Airport |  | TH | 1456 |
| 36 | Calgary International Airport |  | CA | 1455 |
| 37 | Bengaluru International Airport |  | IN | 1443 |
| 38 | Oslo Gardermoen Airport |  | NO | 1424 |
| 39 | Vancouver International Airport |  | CA | 1412 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1365 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 937 | 21m | 244 km | 3,945.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 672 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 634 | 1h 6m | 770 km | 8,422.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 378 | 44m | 241 km | 1,570.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 372 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 306 | 19m | 99 km | 524.2 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 273 | 1h 50m | 1,304 km | 6,141.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CRK453 | CRK | Wuzhou Xijiang Airport (ZGWZ) | Macau International Airport (VMMC) | 2026-09-09 14:46 UTC | 2026-09-09 15:11 UTC | 24m |
| N819KS |  | Witham Field (KSUA) | Witham Field (KSUA) | 2026-09-09 14:00 UTC | 2026-09-09 15:08 UTC | 1h 8m |
| N777ZA |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-09-09 13:41 UTC | 2026-09-09 15:06 UTC | 1h 24m |
| THY6264 | Turkish Airlines | Queen Alia International Airport (OJAI) | Zhuhai Airport (ZGSD) | 2026-09-09 05:36 UTC | 2026-09-09 15:03 UTC | 9h 27m |
| GFA064 | Gulf Air | Bahrain International Airport (OBBI) | Pune Airport (VAPO) | 2026-09-09 11:48 UTC | 2026-09-09 15:00 UTC | 3h 12m |
| DUKE25 | DUK | Wiesbaden Army Airfield (ETOU) | Stuttgart Airport (EDDS) | 2026-09-09 14:25 UTC | 2026-09-09 14:57 UTC | 31m |
|  |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-09-09 14:42 UTC | 2026-09-09 14:54 UTC | 11m |
| N488UV |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-09-09 14:11 UTC | 2026-09-09 14:53 UTC | 41m |
| IGO6283 | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-09 13:48 UTC | 2026-09-09 14:53 UTC | 1h 4m |
| JANET09 | JAN | Harry Reid International Airport (KLAS) | 11CL (11CL) | 2026-09-09 14:17 UTC | 2026-09-09 14:51 UTC | 34m |
| ELY011 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-09-09 14:29 UTC | 2026-09-09 14:50 UTC | 21m |
| AIC9BS | Air India | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-09 13:44 UTC | 2026-09-09 14:50 UTC | 1h 5m |
| BOX502 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-09-09 04:08 UTC | 2026-09-09 14:49 UTC | 10h 40m |
| N2369X |  | Pompano Beach Airpark (KPMP) | Fort Lauderdale Executive Airport (KFXE) | 2026-09-09 14:23 UTC | 2026-09-09 14:47 UTC | 24m |
| IGO1602 | IndiGo | Soekarno-Hatta International Airport (WIII) | Pune Airport (VAPO) | 2026-09-09 09:22 UTC | 2026-09-09 14:46 UTC | 5h 23m |
| CGTBF | CGT | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-09-09 14:17 UTC | 2026-09-09 14:45 UTC | 28m |
| BOMR735 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-09-09 14:16 UTC | 2026-09-09 14:43 UTC | 26m |
| DAL2828 | Delta Air Lines | Chicago O'Hare International Airport (KORD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-09 12:55 UTC | 2026-09-09 14:42 UTC | 1h 47m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-09-09 14:11 UTC | 2026-09-09 14:42 UTC | 31m |
| N6026Z |  | KFTG (KFTG) | 68CO (68CO) | 2026-09-09 14:02 UTC | 2026-09-09 14:40 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
