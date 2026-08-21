# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_19:30:28_UTC-green)

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

**Latest saved flight:** 2026-08-21 19:30:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 19:30:28 UTC

- **223,471** saved flights
- **69,793** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **223,471** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,690,905.0 tonnes** estimated CO2 emissions
- **155,994,495 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8960 |
| 2 | SkyWest Airlines | 7934 |
| 3 | EJA | 4326 |
| 4 | IndiGo | 3780 |
| 5 | American Airlines | 3689 |
| 6 | Southwest Airlines | 3503 |
| 7 | Delta Air Lines | 2868 |
| 8 | ENY | 2745 |
| 9 | LATAM Airlines | 2124 |
| 10 | AZU | 2055 |
| 11 | Vueling | 1885 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1786 |
| 14 | LXJ | 1761 |
| 15 | easyJet | 1546 |
| 16 | Swiss International | 1486 |
| 17 | AXM | 1467 |
| 18 | QLK | 1405 |
| 19 | EJU | 1400 |
| 20 | United Airlines | 1400 |
| 21 | Alaska Airlines | 1356 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1228 |
| 24 | PGT | 1224 |
| 25 | VIV | 1215 |
| 26 | Air France | 1213 |
| 27 | WMT | 1190 |
| 28 | Wizz Air | 1150 |
| 29 | JetBlue | 1121 |
| 30 | AEE | 1115 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 187629 |
| 2 | 🇪🇸 ES | 14333 |
| 3 | 🇧🇷 BR | 12945 |
| 4 | 🇦🇺 AU | 12655 |
| 5 | 🇨🇦 CA | 12353 |
| 6 | 🇮🇹 IT | 11923 |
| 7 | 🇮🇳 IN | 11791 |
| 8 | 🇩🇪 DE | 11021 |
| 9 | 🇬🇧 GB | 10488 |
| 10 | 🇨🇴 CO | 9215 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8920 |
| 13 | 🇬🇷 GR | 6519 |
| 14 | 🇹🇷 TR | 6502 |
| 15 | 🇲🇽 MX | 6195 |
| 16 | 🇨🇭 CH | 5881 |
| 17 | 🇳🇴 NO | 5555 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3710 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2829 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2493 |
| 27 | 🇲🇦 MA | 2252 |
| 28 | 🇳🇱 NL | 1987 |
| 29 | 🇲🇪 ME | 1985 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4681 |
| 2 | Denver International Airport |  | US | 3638 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2712 |
| 5 | Guaymaral Airport |  | CO | 2625 |
| 6 | Harry Reid International Airport |  | US | 2451 |
| 7 | Zurich Airport |  | CH | 2314 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2289 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2265 |
| 10 | La Aurora Airport |  | GT | 2157 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2040 |
| 13 | Salt Lake City International Airport |  | US | 1961 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1918 |
| 15 | Congonhas Airport |  | BR | 1896 |
| 16 | Frankfurt am Main International Airport |  | DE | 1809 |
| 17 | Madrid Barajas International Airport |  | ES | 1751 |
| 18 | Capua Airport |  | IT | 1709 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1669 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1648 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1627 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1566 |
| 25 | Charles de Gaulle International Airport |  | FR | 1545 |
| 26 | Charlotte/Douglas International Airport |  | US | 1478 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1379 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1355 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1319 |
| 33 | Seattle-Tacoma International Airport |  | US | 1317 |
| 34 | Viracopos International Airport |  | BR | 1311 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1288 |
| 36 | Calgary International Airport |  | CA | 1264 |
| 37 | Oslo Gardermoen Airport |  | NO | 1247 |
| 38 | Don Mueang International Airport |  | TH | 1239 |
| 39 | Vitoria/Foronda Airport |  | ES | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1204 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1071 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 805 | 21m | 244 km | 3,389.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 521 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 506 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 376 | 27m | 275 km | 1,781.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 282 | 1h 39m | 1,156 km | 5,625.8 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 275 | 19m | 99 km | 471.1 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 263 | 1h 14m | 961 km | 4,359.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 254 | 19m | 144 km | 631.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 237 | 28m | 152 km | 619.4 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6338F |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-21 18:57 UTC | 2026-08-21 19:30 UTC | 33m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-21 19:12 UTC | 2026-08-21 19:29 UTC | 17m |
| N8083L |  | Hermitage Airport (45CN) | Buchanan Field (KCCR) | 2026-08-21 18:41 UTC | 2026-08-21 19:27 UTC | 46m |
| N286NW |  | Waco Regional Airport (KACT) | KF48 (KF48) | 2026-08-21 17:37 UTC | 2026-08-21 19:22 UTC | 1h 45m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-21 18:58 UTC | 2026-08-21 19:19 UTC | 21m |
| N406EH |  | Cedar Crest Field (1TN0) | John C Tune Airport (KJWN) | 2026-08-21 19:05 UTC | 2026-08-21 19:19 UTC | 13m |
| N4174B |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-21 18:51 UTC | 2026-08-21 19:16 UTC | 24m |
| CXK1105 | CXK | Trenton Mercer Airport (KTTN) | Trenton-Robbinsville Airport (KN87) | 2026-08-21 18:27 UTC | 2026-08-21 19:15 UTC | 47m |
| N2373M |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-21 18:30 UTC | 2026-08-21 19:08 UTC | 37m |
| N546CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-21 17:46 UTC | 2026-08-21 19:07 UTC | 1h 21m |
| N4174L |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-08-21 17:44 UTC | 2026-08-21 19:06 UTC | 1h 22m |
| N800HX |  | Flying G Ranch Airport (86GA) | Flying G Ranch Airport (86GA) | 2026-08-21 19:01 UTC | 2026-08-21 19:04 UTC | 2m |
| SCU43 | SCU | Tulsa Riverside Airport (KRVS) | Haskell Airport (K2K9) | 2026-08-21 18:49 UTC | 2026-08-21 19:01 UTC | 12m |
| UAE9846 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-21 11:53 UTC | 2026-08-21 19:01 UTC | 7h 8m |
| N242BS |  | Triangle North Executive Airport (KLHZ) | Twin County Airport (KHLX) | 2026-08-21 18:29 UTC | 2026-08-21 18:58 UTC | 29m |
| N914LD |  | John Wayne/Orange County Airport (KSNA) | Scottsdale Airport (KSDL) | 2026-08-21 18:04 UTC | 2026-08-21 18:57 UTC | 53m |
| N247TC |  | Watsonville Municipal Airport (KWVI) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 18:09 UTC | 2026-08-21 18:57 UTC | 48m |
| SCU26 | SCU | Tulsa Riverside Airport (KRVS) | Haskell Airport (K2K9) | 2026-08-21 18:29 UTC | 2026-08-21 18:57 UTC | 28m |
| CXK168 | CXK | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-08-21 18:04 UTC | 2026-08-21 18:57 UTC | 52m |
| N6635D |  | Fillmore County Airport (KFKA) | Fillmore County Airport (KFKA) | 2026-08-21 18:55 UTC | 2026-08-21 18:56 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
