# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_13:48:05_UTC-green)

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

**Latest saved flight:** 2026-08-21 13:48:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 13:48:05 UTC

- **222,159** saved flights
- **69,509** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,159** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,675,426.8 tonnes** estimated CO2 emissions
- **155,097,204 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8910 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4290 |
| 4 | IndiGo | 3772 |
| 5 | American Airlines | 3671 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2112 |
| 10 | AZU | 2037 |
| 11 | Vueling | 1872 |
| 12 | Lufthansa | 1839 |
| 13 | WIF | 1780 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1538 |
| 16 | Swiss International | 1478 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1391 |
| 20 | EJU | 1390 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | PGT | 1218 |
| 24 | GLO | 1213 |
| 25 | VIV | 1206 |
| 26 | Air France | 1205 |
| 27 | WMT | 1184 |
| 28 | Wizz Air | 1140 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1109 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186402 |
| 2 | 🇪🇸 ES | 14240 |
| 3 | 🇧🇷 BR | 12831 |
| 4 | 🇦🇺 AU | 12651 |
| 5 | 🇨🇦 CA | 12256 |
| 6 | 🇮🇹 IT | 11837 |
| 7 | 🇮🇳 IN | 11766 |
| 8 | 🇩🇪 DE | 10970 |
| 9 | 🇬🇧 GB | 10427 |
| 10 | 🇨🇴 CO | 9129 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8859 |
| 13 | 🇬🇷 GR | 6490 |
| 14 | 🇹🇷 TR | 6446 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5859 |
| 17 | 🇳🇴 NO | 5535 |
| 18 | 🇲🇾 MY | 3884 |
| 19 | 🇿🇦 ZA | 3825 |
| 20 | 🇹🇭 TH | 3765 |
| 21 | 🇵🇱 PL | 3688 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3016 |
| 24 | 🇬🇹 GT | 2796 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2479 |
| 27 | 🇲🇦 MA | 2237 |
| 28 | 🇲🇪 ME | 1976 |
| 29 | 🇳🇱 NL | 1972 |
| 30 | 🇮🇩 ID | 1906 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3616 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2703 |
| 5 | Guaymaral Airport |  | CO | 2612 |
| 6 | Harry Reid International Airport |  | US | 2444 |
| 7 | Zurich Airport |  | CH | 2303 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2256 |
| 10 | La Aurora Airport |  | GT | 2130 |
| 11 | El Dorado International Airport |  | CO | 2077 |
| 12 | Chicago O'Hare International Airport |  | US | 2026 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1873 |
| 16 | Frankfurt am Main International Airport |  | DE | 1804 |
| 17 | Madrid Barajas International Airport |  | ES | 1739 |
| 18 | Capua Airport |  | IT | 1697 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1638 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1556 |
| 25 | Charles de Gaulle International Airport |  | FR | 1531 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1436 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1368 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1332 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1302 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1243 |
| 37 | Oslo Gardermoen Airport |  | NO | 1239 |
| 38 | Don Mueang International Airport |  | TH | 1238 |
| 39 | Vitoria/Foronda Airport |  | ES | 1233 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1193 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1067 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 801 | 21m | 244 km | 3,372.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 501 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 374 | 27m | 275 km | 1,772.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 330 | 1h 50m | 1,423 km | 8,098.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 295 | 21m | 250 km | 1,274.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 280 | 1h 39m | 1,156 km | 5,585.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 277 | 24m | 218 km | 1,043.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 274 | 27m | 215 km | 1,014.8 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 273 | 44m | 555 km | 2,614.1 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 233 | 28m | 152 km | 608.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1115M |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-21 13:23 UTC | 2026-08-21 13:48 UTC | 24m |
| IGO1161 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-08-21 12:35 UTC | 2026-08-21 13:46 UTC | 1h 11m |
| DLH3F | Lufthansa | Charles de Gaulle International Airport (LFPG) | Frankfurt am Main International Airport (EDDF) | 2026-08-21 12:43 UTC | 2026-08-21 13:36 UTC | 52m |
| N264FA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-08-21 12:32 UTC | 2026-08-21 13:33 UTC | 1h 0m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-21 06:43 UTC | 2026-08-21 13:29 UTC | 6h 46m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-21 05:56 UTC | 2026-08-21 13:28 UTC | 7h 31m |
| N43813 |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-21 13:20 UTC | 2026-08-21 13:25 UTC | 5m |
| N55BF |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-21 12:43 UTC | 2026-08-21 13:21 UTC | 37m |
| CGJDU | CGJ | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Montréal (Mirabel) Airport (CYMX) | 2026-08-21 13:01 UTC | 2026-08-21 13:16 UTC | 14m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-21 12:52 UTC | 2026-08-21 13:15 UTC | 23m |
| N544CM |  | Dry Pen Airport (16CO) | Telluride Regional Airport (KTEX) | 2026-08-21 13:00 UTC | 2026-08-21 13:14 UTC | 13m |
| MEDX528 | MED | Napoli / Capodichino International Airport (LIRN) | Salerno / Pontecagnano Airport (LIRI) | 2026-08-21 12:19 UTC | 2026-08-21 13:13 UTC | 53m |
| N1491T |  | Rapids Airway Airport (04MI) | Mason Jewett Field (KTEW) | 2026-08-21 13:09 UTC | 2026-08-21 13:12 UTC | 3m |
| N841DS |  | Columbus Airport (KCSG) | Lovell Field (KCHA) | 2026-08-21 11:54 UTC | 2026-08-21 13:12 UTC | 1h 17m |
| N20MA |  | Fort Smith Regional Airport (KFSM) | 0AR1 (0AR1) | 2026-08-21 12:56 UTC | 2026-08-21 13:12 UTC | 15m |
| N17NA |  | Northampton Airport (K7B2) | Northampton Airport (K7B2) | 2026-08-21 12:57 UTC | 2026-08-21 13:06 UTC | 9m |
| N6018K |  | Atlanta Regional Falcon Field (KFFC) | K4A7 (K4A7) | 2026-08-21 12:47 UTC | 2026-08-21 13:03 UTC | 15m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-21 12:33 UTC | 2026-08-21 13:02 UTC | 29m |
| N98FF |  | KFTG (KFTG) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-21 12:15 UTC | 2026-08-21 13:02 UTC | 46m |
| AZU4530 | AZU | Viracopos International Airport (SBKP) | Pederneiras Airport (SSOI) | 2026-08-21 12:30 UTC | 2026-08-21 13:01 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
