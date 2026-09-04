# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_19:05:33_UTC-green)

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

**Latest saved flight:** 2026-09-04 19:05:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 19:05:33 UTC

- **247,441** saved flights
- **74,594** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,441** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,975,963.7 tonnes** estimated CO2 emissions
- **172,519,635 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9920 |
| 2 | SkyWest Airlines | 8644 |
| 3 | EJA | 4774 |
| 4 | IndiGo | 4134 |
| 5 | American Airlines | 3969 |
| 6 | Southwest Airlines | 3687 |
| 7 | Delta Air Lines | 3141 |
| 8 | ENY | 2959 |
| 9 | LATAM Airlines | 2388 |
| 10 | AZU | 2302 |
| 11 | Vueling | 2117 |
| 12 | WIF | 1982 |
| 13 | Lufthansa | 1970 |
| 14 | LXJ | 1922 |
| 15 | easyJet | 1713 |
| 16 | Swiss International | 1660 |
| 17 | AXM | 1619 |
| 18 | EJU | 1590 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1553 |
| 21 | Alaska Airlines | 1477 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1397 |
| 24 | GLO | 1381 |
| 25 | VIV | 1360 |
| 26 | PGT | 1354 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1336 |
| 29 | JetBlue | 1221 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205186 |
| 2 | 🇪🇸 ES | 15863 |
| 3 | 🇧🇷 BR | 14466 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13753 |
| 6 | 🇮🇹 IT | 13555 |
| 7 | 🇮🇳 IN | 12897 |
| 8 | 🇩🇪 DE | 12175 |
| 9 | 🇬🇧 GB | 11634 |
| 10 | 🇨🇴 CO | 10785 |
| 11 | 🇫🇷 FR | 9975 |
| 12 | 🇯🇵 JP | 9788 |
| 13 | 🇹🇷 TR | 7361 |
| 14 | 🇬🇷 GR | 7282 |
| 15 | 🇲🇽 MX | 6837 |
| 16 | 🇨🇭 CH | 6669 |
| 17 | 🇳🇴 NO | 6143 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4345 |
| 20 | 🇿🇦 ZA | 4281 |
| 21 | 🇵🇱 PL | 4142 |
| 22 | 🇳🇿 NZ | 3378 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3092 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2841 |
| 27 | 🇲🇦 MA | 2504 |
| 28 | 🇲🇪 ME | 2311 |
| 29 | 🇳🇱 NL | 2233 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5093 |
| 2 | Denver International Airport |  | US | 3998 |
| 3 | Indira Gandhi International Airport |  | IN | 3015 |
| 4 | Tokyo International Airport |  | JP | 2920 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2638 |
| 7 | Zurich Airport |  | CH | 2590 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2517 |
| 9 | El Dorado International Airport |  | CO | 2466 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2458 |
| 11 | La Aurora Airport |  | GT | 2353 |
| 12 | Salt Lake City International Airport |  | US | 2192 |
| 13 | Chicago O'Hare International Airport |  | US | 2170 |
| 14 | Congonhas Airport |  | BR | 2125 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2040 |
| 16 | Capua Airport |  | IT | 1947 |
| 17 | Frankfurt am Main International Airport |  | DE | 1941 |
| 18 | Madrid Barajas International Airport |  | ES | 1940 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1861 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1809 |
| 21 | Malpensa International Airport |  | IT | 1775 |
| 22 | Charles de Gaulle International Airport |  | FR | 1738 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1727 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1633 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1622 |
| 28 | Charlotte/Douglas International Airport |  | US | 1570 |
| 29 | Barcelona International Airport |  | ES | 1567 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1512 |
| 32 | Viracopos International Airport |  | BR | 1475 |
| 33 | Seattle-Tacoma International Airport |  | US | 1454 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1440 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Bengaluru International Airport |  | IN | 1426 |
| 37 | Calgary International Airport |  | CA | 1423 |
| 38 | Oslo Gardermoen Airport |  | NO | 1394 |
| 39 | Vancouver International Airport |  | CA | 1381 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1345 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 919 | 21m | 244 km | 3,869.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 652 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 620 | 1h 6m | 770 km | 8,236.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 394 | 1h 50m | 1,423 km | 9,669.4 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 366 | 44m | 241 km | 1,520.3 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 345 | 24m | 218 km | 1,299.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 269 | 1h 50m | 1,304 km | 6,051.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 254 | 28m | 152 km | 663.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9158D |  | A Paul Vance Fredericktown Regional Airport (KH88) | Lee C Fine Memorial Airport (KAIZ) | 2026-09-04 18:21 UTC | 2026-09-04 19:05 UTC | 43m |
| TRP1 | TRP | Martin State Airport (KMTN) | Harford County Airport (K0W3) | 2026-09-04 18:38 UTC | 2026-09-04 19:04 UTC | 26m |
| N123SL |  | Raleigh-Durham International Airport (KRDU) | MD99 (MD99) | 2026-09-04 17:57 UTC | 2026-09-04 19:03 UTC | 1h 5m |
| CXK126 | CXK | Double Eagle Ii Airport (KAEG) | Socorro Municipal Airport (KONM) | 2026-09-04 18:22 UTC | 2026-09-04 19:01 UTC | 38m |
| N991AK |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-09-04 18:20 UTC | 2026-09-04 19:00 UTC | 39m |
| REH001 | REH | Sutter County Airport (KO52) | Sacramento Executive Airport (KSAC) | 2026-09-04 18:39 UTC | 2026-09-04 18:59 UTC | 19m |
| N950PC |  | Fort Lauderdale Executive Airport (KFXE) | Orlando Executive Airport (KORL) | 2026-09-04 12:40 UTC | 2026-09-04 18:55 UTC | 6h 14m |
| GRYDR49 | GRY | Frederick Douglass/Greater Rochester International Airport (KROC) | Dansville Municipal Airport (KDSV) | 2026-09-04 18:12 UTC | 2026-09-04 18:53 UTC | 40m |
| N6069F |  | Morristown Municipal Airport (KMMU) | Blairstown Airport (K1N7) | 2026-09-04 17:51 UTC | 2026-09-04 18:51 UTC | 59m |
| PROFC | PRO | SBEC (SBEC) | SBEC (SBEC) | 2026-09-04 18:49 UTC | 2026-09-04 18:49 UTC | 0m |
| PREFX | PRE | SBEC (SBEC) | SBEC (SBEC) | 2026-09-04 18:45 UTC | 2026-09-04 18:46 UTC | 0m |
| SKYVAN5 | SKY | Sarita Airport (37AZ) | Coolidge Municipal Airport (KP08) | 2026-09-04 18:32 UTC | 2026-09-04 18:44 UTC | 11m |
| EFY7836 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-04 18:09 UTC | 2026-09-04 18:40 UTC | 30m |
| N856FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-04 17:52 UTC | 2026-09-04 18:39 UTC | 46m |
| N34029 |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-09-04 17:11 UTC | 2026-09-04 18:37 UTC | 1h 26m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-09-04 18:20 UTC | 2026-09-04 18:37 UTC | 16m |
| N947SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-09-04 18:34 UTC | 2026-09-04 18:35 UTC | 0m |
| N8269L |  | Springdale Municipal Airport (KASG) | Huntsville Municipal Airport (KH34) | 2026-09-04 18:05 UTC | 2026-09-04 18:35 UTC | 30m |
| TGCOB | TGC | MHLE (MHLE) | San Jose Airport (MGSJ) | 2026-09-04 18:00 UTC | 2026-09-04 18:32 UTC | 31m |
| GLO2165 | GLO | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Ministro Victor Konder International Airport (SBNF) | 2026-09-04 17:13 UTC | 2026-09-04 18:31 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
