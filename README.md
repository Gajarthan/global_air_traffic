# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_18:02:43_UTC-green)

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

**Latest saved flight:** 2026-09-10 18:02:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 18:02:43 UTC

- **253,883** saved flights
- **75,918** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **253,883** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,060,782.2 tonnes** estimated CO2 emissions
- **177,436,649 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10137 |
| 2 | SkyWest Airlines | 8848 |
| 3 | EJA | 4899 |
| 4 | IndiGo | 4252 |
| 5 | American Airlines | 4033 |
| 6 | Southwest Airlines | 3751 |
| 7 | Delta Air Lines | 3194 |
| 8 | ENY | 3029 |
| 9 | LATAM Airlines | 2444 |
| 10 | AZU | 2362 |
| 11 | Vueling | 2160 |
| 12 | WIF | 2035 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1987 |
| 15 | easyJet | 1735 |
| 16 | Swiss International | 1704 |
| 17 | QLK | 1636 |
| 18 | AXM | 1633 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1579 |
| 21 | Alaska Airlines | 1512 |
| 22 | All Nippon Airways | 1481 |
| 23 | WMT | 1436 |
| 24 | GLO | 1411 |
| 25 | PGT | 1396 |
| 26 | VIV | 1387 |
| 27 | Air France | 1383 |
| 28 | Wizz Air | 1382 |
| 29 | JetBlue | 1238 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210702 |
| 2 | 🇪🇸 ES | 16194 |
| 3 | 🇧🇷 BR | 14811 |
| 4 | 🇦🇺 AU | 14471 |
| 5 | 🇨🇦 CA | 14133 |
| 6 | 🇮🇹 IT | 13899 |
| 7 | 🇮🇳 IN | 13312 |
| 8 | 🇩🇪 DE | 12429 |
| 9 | 🇬🇧 GB | 11869 |
| 10 | 🇨🇴 CO | 11243 |
| 11 | 🇫🇷 FR | 10210 |
| 12 | 🇯🇵 JP | 9949 |
| 13 | 🇹🇷 TR | 7603 |
| 14 | 🇬🇷 GR | 7428 |
| 15 | 🇲🇽 MX | 6995 |
| 16 | 🇨🇭 CH | 6828 |
| 17 | 🇳🇴 NO | 6298 |
| 18 | 🇹🇭 TH | 4563 |
| 19 | 🇲🇾 MY | 4394 |
| 20 | 🇿🇦 ZA | 4339 |
| 21 | 🇵🇱 PL | 4220 |
| 22 | 🇳🇿 NZ | 3470 |
| 23 | 🇵🇭 PH | 3432 |
| 24 | 🇬🇹 GT | 3154 |
| 25 | 🇰🇷 KR | 2921 |
| 26 | 🇭🇷 HR | 2913 |
| 27 | 🇲🇦 MA | 2561 |
| 28 | 🇲🇪 ME | 2386 |
| 29 | 🇳🇱 NL | 2286 |
| 30 | 🇮🇩 ID | 2169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5223 |
| 2 | Denver International Airport |  | US | 4100 |
| 3 | Indira Gandhi International Airport |  | IN | 3078 |
| 4 | Tokyo International Airport |  | JP | 2967 |
| 5 | Guaymaral Airport |  | CO | 2748 |
| 6 | Harry Reid International Airport |  | US | 2692 |
| 7 | Zurich Airport |  | CH | 2658 |
| 8 | El Dorado International Airport |  | CO | 2599 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2568 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2495 |
| 11 | La Aurora Airport |  | GT | 2407 |
| 12 | Salt Lake City International Airport |  | US | 2239 |
| 13 | Chicago O'Hare International Airport |  | US | 2213 |
| 14 | Congonhas Airport |  | BR | 2176 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2079 |
| 16 | Capua Airport |  | IT | 2004 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1965 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1900 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1844 |
| 21 | Malpensa International Airport |  | IT | 1823 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1782 |
| 23 | Charles de Gaulle International Airport |  | FR | 1780 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1766 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1701 |
| 26 | Ninoy Aquino International Airport |  | PH | 1678 |
| 27 | Macau International Airport |  | MO | 1674 |
| 28 | Barcelona International Airport |  | ES | 1598 |
| 29 | Charlotte/Douglas International Airport |  | US | 1597 |
| 30 | Kuala Lumpur International Airport |  | MY | 1583 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1558 |
| 32 | Viracopos International Airport |  | BR | 1516 |
| 33 | Seattle-Tacoma International Airport |  | US | 1493 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1470 |
| 35 | Calgary International Airport |  | CA | 1463 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1447 |
| 38 | Oslo Gardermoen Airport |  | NO | 1435 |
| 39 | Vancouver International Airport |  | CA | 1423 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1371 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 943 | 21m | 244 km | 3,970.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 678 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 637 | 1h 6m | 770 km | 8,462.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 569 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 404 | 1h 50m | 1,423 km | 9,914.8 t |
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
| N731KS |  | Bartow Executive Airport (KBOW) | Wauchula Municipal Airport (KCHN) | 2026-09-10 17:46 UTC | 2026-09-10 18:02 UTC | 15m |
| N17DM |  | Monterey Bay Academy Airport (CA66) | Half Moon Bay Airport (KHAF) | 2026-09-10 17:35 UTC | 2026-09-10 18:01 UTC | 25m |
| KING41 | KIN | Patrick Space Force Base Airport (KCOF) | Patrick Space Force Base Airport (KCOF) | 2026-09-10 16:47 UTC | 2026-09-10 17:59 UTC | 1h 11m |
| N698JA |  | San Carlos Airport (KSQL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-10 17:41 UTC | 2026-09-10 17:59 UTC | 17m |
| PAT489 | PAT | Nervino Airport (KO02) | Sacramento Mather Airport (KMHR) | 2026-09-10 16:51 UTC | 2026-09-10 17:54 UTC | 1h 2m |
| N510KA |  | Van Nuys Airport (KVNY) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-09-10 17:40 UTC | 2026-09-10 17:51 UTC | 10m |
| XATSR | XAT | El Lencero Airport (MMJA) | Atizapan De Zaragoza Airport (MMJC) | 2026-09-10 16:48 UTC | 2026-09-10 17:50 UTC | 1h 1m |
| DHC99 | DHC | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-09-10 17:14 UTC | 2026-09-10 17:46 UTC | 32m |
| PERRIS2 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-09-10 14:09 UTC | 2026-09-10 17:46 UTC | 3h 37m |
| N521CL |  | Lake City Gateway Airport (KLCQ) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-10 16:56 UTC | 2026-09-10 17:45 UTC | 48m |
| FDB39K | flydubai | Dubai International Airport (OMDB) | Queen Alia International Airport (OJAI) | 2026-09-10 15:02 UTC | 2026-09-10 17:44 UTC | 2h 41m |
| BRG661 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-09-10 17:12 UTC | 2026-09-10 17:43 UTC | 31m |
| N9187C |  | Schaumburg Regional Airport (K06C) | 0IL8 (0IL8) | 2026-09-10 17:14 UTC | 2026-09-10 17:43 UTC | 28m |
| AIC4218 | Air India | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-10 15:16 UTC | 2026-09-10 17:39 UTC | 2h 22m |
| N91JA |  | 43NC (43NC) | Boonville Airport (26NC) | 2026-09-10 16:54 UTC | 2026-09-10 17:32 UTC | 38m |
| HK5436G |  | Santa Ana Airport (SKGO) | Santa Ana Airport (SKGO) | 2026-09-10 17:23 UTC | 2026-09-10 17:32 UTC | 9m |
| N279WB |  | Chumchal Farms Airport (71TA) | Castle Lakes Airport (CD32) | 2026-09-10 16:18 UTC | 2026-09-10 17:29 UTC | 1h 11m |
| N92AG |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-09-10 16:17 UTC | 2026-09-10 17:29 UTC | 1h 12m |
| LVZZH | LVZ | Gualeguaychu Airport (SAAG) | Gualeguaychu Airport (SAAG) | 2026-09-10 17:11 UTC | 2026-09-10 17:27 UTC | 15m |
| SAS366 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-09-10 16:46 UTC | 2026-09-10 17:27 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
