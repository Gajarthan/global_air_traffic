# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_19:51:29_UTC-green)

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

**Latest saved flight:** 2026-09-03 19:51:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 19:51:29 UTC

- **246,264** saved flights
- **74,347** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,264** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,963,702.8 tonnes** estimated CO2 emissions
- **171,808,856 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9873 |
| 2 | SkyWest Airlines | 8608 |
| 3 | EJA | 4748 |
| 4 | IndiGo | 4122 |
| 5 | American Airlines | 3955 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3128 |
| 8 | ENY | 2947 |
| 9 | LATAM Airlines | 2371 |
| 10 | AZU | 2288 |
| 11 | Vueling | 2110 |
| 12 | WIF | 1975 |
| 13 | Lufthansa | 1968 |
| 14 | LXJ | 1908 |
| 15 | easyJet | 1709 |
| 16 | Swiss International | 1658 |
| 17 | AXM | 1616 |
| 18 | EJU | 1587 |
| 19 | QLK | 1577 |
| 20 | United Airlines | 1551 |
| 21 | Alaska Airlines | 1469 |
| 22 | All Nippon Airways | 1448 |
| 23 | WMT | 1387 |
| 24 | GLO | 1373 |
| 25 | PGT | 1350 |
| 26 | VIV | 1350 |
| 27 | Air France | 1346 |
| 28 | Wizz Air | 1334 |
| 29 | AEE | 1214 |
| 30 | JetBlue | 1214 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204083 |
| 2 | 🇪🇸 ES | 15805 |
| 3 | 🇧🇷 BR | 14373 |
| 4 | 🇦🇺 AU | 13991 |
| 5 | 🇨🇦 CA | 13700 |
| 6 | 🇮🇹 IT | 13494 |
| 7 | 🇮🇳 IN | 12853 |
| 8 | 🇩🇪 DE | 12139 |
| 9 | 🇬🇧 GB | 11597 |
| 10 | 🇨🇴 CO | 10700 |
| 11 | 🇫🇷 FR | 9942 |
| 12 | 🇯🇵 JP | 9773 |
| 13 | 🇹🇷 TR | 7314 |
| 14 | 🇬🇷 GR | 7263 |
| 15 | 🇲🇽 MX | 6796 |
| 16 | 🇨🇭 CH | 6629 |
| 17 | 🇳🇴 NO | 6120 |
| 18 | 🇹🇭 TH | 4446 |
| 19 | 🇲🇾 MY | 4329 |
| 20 | 🇿🇦 ZA | 4275 |
| 21 | 🇵🇱 PL | 4131 |
| 22 | 🇳🇿 NZ | 3370 |
| 23 | 🇵🇭 PH | 3364 |
| 24 | 🇬🇹 GT | 3081 |
| 25 | 🇰🇷 KR | 2878 |
| 26 | 🇭🇷 HR | 2833 |
| 27 | 🇲🇦 MA | 2489 |
| 28 | 🇲🇪 ME | 2302 |
| 29 | 🇳🇱 NL | 2228 |
| 30 | 🇮🇩 ID | 2142 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5068 |
| 2 | Denver International Airport |  | US | 3977 |
| 3 | Indira Gandhi International Airport |  | IN | 3001 |
| 4 | Tokyo International Airport |  | JP | 2914 |
| 5 | Guaymaral Airport |  | CO | 2721 |
| 6 | Harry Reid International Airport |  | US | 2620 |
| 7 | Zurich Airport |  | CH | 2585 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2509 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2453 |
| 10 | El Dorado International Airport |  | CO | 2442 |
| 11 | La Aurora Airport |  | GT | 2344 |
| 12 | Salt Lake City International Airport |  | US | 2183 |
| 13 | Chicago O'Hare International Airport |  | US | 2165 |
| 14 | Congonhas Airport |  | BR | 2110 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2031 |
| 16 | Capua Airport |  | IT | 1940 |
| 17 | Frankfurt am Main International Airport |  | DE | 1938 |
| 18 | Madrid Barajas International Airport |  | ES | 1930 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1852 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1805 |
| 21 | Malpensa International Airport |  | IT | 1764 |
| 22 | Charles de Gaulle International Airport |  | FR | 1732 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1725 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 25 | Ninoy Aquino International Airport |  | PH | 1637 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1600 |
| 28 | Charlotte/Douglas International Airport |  | US | 1567 |
| 29 | Barcelona International Airport |  | ES | 1563 |
| 30 | Kuala Lumpur International Airport |  | MY | 1560 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1500 |
| 32 | Viracopos International Airport |  | BR | 1462 |
| 33 | Seattle-Tacoma International Airport |  | US | 1446 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1429 |
| 35 | Don Mueang International Airport |  | TH | 1428 |
| 36 | Bengaluru International Airport |  | IN | 1424 |
| 37 | Calgary International Airport |  | CA | 1419 |
| 38 | Oslo Gardermoen Airport |  | NO | 1389 |
| 39 | Vancouver International Airport |  | CA | 1373 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1343 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 911 | 21m | 244 km | 3,836.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 643 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 552 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 406 | 27m | 275 km | 1,923.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 390 | 1h 50m | 1,423 km | 9,571.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 364 | 44m | 241 km | 1,512.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 343 | 24m | 218 km | 1,292.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 329 | 22m | 55 km | 312.7 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 305 | 26m | 215 km | 1,129.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 304 | 19m | 99 km | 520.7 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 284 | 1h 14m | 961 km | 4,707.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 279 | 19m | 144 km | 694.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 266 | 1h 50m | 1,304 km | 5,984.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N550AJ |  | Capital City Airport (KCXY) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-09-03 19:16 UTC | 2026-09-03 19:51 UTC | 34m |
| QTR23V | Qatar Airways | Cairo International Airport (HECA) | Doha International Airport (OTBD) | 2026-09-03 17:31 UTC | 2026-09-03 19:50 UTC | 2h 19m |
| IGO28F | IndiGo | Bengaluru International Airport (VOBL) | Arzanah Airport (OMAR) | 2026-09-03 16:17 UTC | 2026-09-03 19:47 UTC | 3h 29m |
| N99DQ |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-09-03 19:31 UTC | 2026-09-03 19:45 UTC | 13m |
| TRP7 | TRP | Chesapeake Ranch Airport (MD50) | Joint Base Andrews Airport (KADW) | 2026-09-03 19:25 UTC | 2026-09-03 19:41 UTC | 16m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-03 19:22 UTC | 2026-09-03 19:40 UTC | 17m |
| N733HH |  | Linden Airport (KLDJ) | Central Jersey Regional Airport (K47N) | 2026-09-03 18:22 UTC | 2026-09-03 19:39 UTC | 1h 16m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-03 17:07 UTC | 2026-09-03 19:38 UTC | 2h 31m |
| N554CN |  | Wiley Post Airport (KPWA) | Mc Alester Regional Airport (KMLC) | 2026-09-03 19:16 UTC | 2026-09-03 19:38 UTC | 22m |
| N528SV |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-09-03 19:05 UTC | 2026-09-03 19:37 UTC | 32m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-03 19:01 UTC | 2026-09-03 19:37 UTC | 35m |
| N772FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-03 18:41 UTC | 2026-09-03 19:35 UTC | 53m |
| LS00 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-03 18:16 UTC | 2026-09-03 19:32 UTC | 1h 16m |
| N998RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-09-03 18:55 UTC | 2026-09-03 19:32 UTC | 37m |
| LFA328 | LFA | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-09-03 19:15 UTC | 2026-09-03 19:28 UTC | 12m |
| FD534 |  | Port Augusta Airport (YPAG) | Port Pirie Airport (YPIR) | 2026-09-03 19:07 UTC | 2026-09-03 19:25 UTC | 18m |
| DHC99 | DHC | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-09-03 18:50 UTC | 2026-09-03 19:24 UTC | 33m |
| N469DM |  | Rochester International Airport (KRST) | C A Moore Airport (K19M) | 2026-09-03 17:54 UTC | 2026-09-03 19:24 UTC | 1h 29m |
| N18HM |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-09-03 19:00 UTC | 2026-09-03 19:22 UTC | 22m |
| NOZ842 | Norwegian Air | Bergen Airport Flesland (ENBR) | Stockholm-Arlanda Airport (ESSA) | 2026-09-03 18:22 UTC | 2026-09-03 19:22 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
