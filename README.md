# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_14:47:44_UTC-green)

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

**Latest saved flight:** 2026-09-10 14:47:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 14:47:44 UTC

- **253,657** saved flights
- **75,866** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **253,657** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,058,006.2 tonnes** estimated CO2 emissions
- **177,275,720 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10134 |
| 2 | SkyWest Airlines | 8843 |
| 3 | EJA | 4894 |
| 4 | IndiGo | 4249 |
| 5 | American Airlines | 4031 |
| 6 | Southwest Airlines | 3747 |
| 7 | Delta Air Lines | 3193 |
| 8 | ENY | 3025 |
| 9 | LATAM Airlines | 2444 |
| 10 | AZU | 2361 |
| 11 | Vueling | 2158 |
| 12 | WIF | 2033 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1981 |
| 15 | easyJet | 1734 |
| 16 | Swiss International | 1702 |
| 17 | QLK | 1636 |
| 18 | AXM | 1633 |
| 19 | EJU | 1623 |
| 20 | United Airlines | 1578 |
| 21 | Alaska Airlines | 1511 |
| 22 | All Nippon Airways | 1481 |
| 23 | WMT | 1436 |
| 24 | GLO | 1410 |
| 25 | PGT | 1396 |
| 26 | VIV | 1386 |
| 27 | Air France | 1383 |
| 28 | Wizz Air | 1382 |
| 29 | JetBlue | 1237 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210469 |
| 2 | 🇪🇸 ES | 16173 |
| 3 | 🇧🇷 BR | 14807 |
| 4 | 🇦🇺 AU | 14471 |
| 5 | 🇨🇦 CA | 14115 |
| 6 | 🇮🇹 IT | 13891 |
| 7 | 🇮🇳 IN | 13302 |
| 8 | 🇩🇪 DE | 12417 |
| 9 | 🇬🇧 GB | 11859 |
| 10 | 🇨🇴 CO | 11227 |
| 11 | 🇫🇷 FR | 10199 |
| 12 | 🇯🇵 JP | 9949 |
| 13 | 🇹🇷 TR | 7596 |
| 14 | 🇬🇷 GR | 7425 |
| 15 | 🇲🇽 MX | 6983 |
| 16 | 🇨🇭 CH | 6823 |
| 17 | 🇳🇴 NO | 6288 |
| 18 | 🇹🇭 TH | 4563 |
| 19 | 🇲🇾 MY | 4394 |
| 20 | 🇿🇦 ZA | 4335 |
| 21 | 🇵🇱 PL | 4218 |
| 22 | 🇳🇿 NZ | 3470 |
| 23 | 🇵🇭 PH | 3432 |
| 24 | 🇬🇹 GT | 3152 |
| 25 | 🇰🇷 KR | 2921 |
| 26 | 🇭🇷 HR | 2912 |
| 27 | 🇲🇦 MA | 2558 |
| 28 | 🇲🇪 ME | 2384 |
| 29 | 🇳🇱 NL | 2285 |
| 30 | 🇮🇩 ID | 2169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5220 |
| 2 | Denver International Airport |  | US | 4096 |
| 3 | Indira Gandhi International Airport |  | IN | 3076 |
| 4 | Tokyo International Airport |  | JP | 2967 |
| 5 | Guaymaral Airport |  | CO | 2748 |
| 6 | Harry Reid International Airport |  | US | 2691 |
| 7 | Zurich Airport |  | CH | 2654 |
| 8 | El Dorado International Airport |  | CO | 2595 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2565 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2495 |
| 11 | La Aurora Airport |  | GT | 2405 |
| 12 | Salt Lake City International Airport |  | US | 2237 |
| 13 | Chicago O'Hare International Airport |  | US | 2211 |
| 14 | Congonhas Airport |  | BR | 2174 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2078 |
| 16 | Capua Airport |  | IT | 2000 |
| 17 | Madrid Barajas International Airport |  | ES | 1987 |
| 18 | Frankfurt am Main International Airport |  | DE | 1964 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1900 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1842 |
| 21 | Malpensa International Airport |  | IT | 1823 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1782 |
| 23 | Charles de Gaulle International Airport |  | FR | 1780 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1764 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1697 |
| 26 | Ninoy Aquino International Airport |  | PH | 1678 |
| 27 | Macau International Airport |  | MO | 1674 |
| 28 | Barcelona International Airport |  | ES | 1597 |
| 29 | Charlotte/Douglas International Airport |  | US | 1593 |
| 30 | Kuala Lumpur International Airport |  | MY | 1583 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1516 |
| 33 | Seattle-Tacoma International Airport |  | US | 1493 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1470 |
| 35 | Calgary International Airport |  | CA | 1461 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1447 |
| 38 | Oslo Gardermoen Airport |  | NO | 1433 |
| 39 | Vancouver International Airport |  | CA | 1421 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1370 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 941 | 21m | 244 km | 3,962.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 677 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 637 | 1h 6m | 770 km | 8,462.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 568 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 402 | 44m | 555 km | 3,849.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 382 | 44m | 241 km | 1,586.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 373 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 354 | 24m | 218 km | 1,333.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 338 | 23m | 55 km | 321.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 307 | 19m | 99 km | 525.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 303 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 297 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 291 | 1h 14m | 961 km | 4,823.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 264 | 41m | 535 km | 2,438.2 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7166R |  | KM33 (KM33) | KM33 (KM33) | 2026-09-10 13:58 UTC | 2026-09-10 14:47 UTC | 49m |
| CPA337 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-09-10 12:10 UTC | 2026-09-10 14:44 UTC | 2h 34m |
| CHZ255 | CHZ | Al Maktoum International Airport (OMDW) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-10 12:06 UTC | 2026-09-10 14:41 UTC | 2h 34m |
| TVS1DZ | TVS | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-09-10 13:22 UTC | 2026-09-10 14:38 UTC | 1h 15m |
|  |  | Dothan Regional Airport (KDHN) | Coates Airport (79GA) | 2026-09-10 13:51 UTC | 2026-09-10 14:26 UTC | 35m |
| QTR8400 | Qatar Airways | Doha International Airport (OTBD) | Zhuhai Airport (ZGSD) | 2026-09-10 06:48 UTC | 2026-09-10 14:24 UTC | 7h 35m |
| N619LF |  | Dawson Municipal Airport (K16J) | Dawson Municipal Airport (K16J) | 2026-09-10 14:02 UTC | 2026-09-10 14:21 UTC | 18m |
| FGJFI | FGJ | Pau Pyrenees Airport (LFBP) | Pau Pyrenees Airport (LFBP) | 2026-09-10 14:08 UTC | 2026-09-10 14:21 UTC | 13m |
| SVA986 | Saudia | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-09-09 18:35 UTC | 2026-09-10 14:19 UTC | 19h 43m |
| YV3025 |  | San Roque Airport (SVOL) | Upata Airport (SVUP) | 2026-09-10 13:47 UTC | 2026-09-10 14:19 UTC | 31m |
| ARCAS21 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-09-10 13:59 UTC | 2026-09-10 14:18 UTC | 18m |
| THY99D | Turkish Airlines | Miami International Airport (KMIA) | Istanbul Airport (LTFM) | 2026-09-10 03:33 UTC | 2026-09-10 14:17 UTC | 10h 43m |
| BPX201 | BPX | Daytona Beach International Airport (KDAB) | 46FD (46FD) | 2026-09-10 13:42 UTC | 2026-09-10 14:14 UTC | 32m |
| N1323X |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-09-10 13:54 UTC | 2026-09-10 14:14 UTC | 19m |
| SKYVAN5 | SKY | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-09-10 13:55 UTC | 2026-09-10 14:12 UTC | 17m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-10 13:57 UTC | 2026-09-10 14:12 UTC | 14m |
| N772FG |  | Trenton Mercer Airport (KTTN) | Hammonton Municipal Airport (KN81) | 2026-09-10 12:53 UTC | 2026-09-10 14:12 UTC | 1h 19m |
| PKSCJ | PKS | Semplak Airport (WIAJ) | Halim Perdanakusuma International Airport (WIHH) | 2026-09-10 12:44 UTC | 2026-09-10 14:12 UTC | 1h 27m |
| WIF3LA | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-10 13:27 UTC | 2026-09-10 14:11 UTC | 44m |
| N218LG |  | Whitewater Mesa Ranch Airport (NM55) | Milbank Municipal Airport (K1D1) | 2026-09-10 10:53 UTC | 2026-09-10 14:10 UTC | 3h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
