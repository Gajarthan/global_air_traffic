# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_00:55:47_UTC-green)

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

**Latest saved flight:** 2026-09-10 00:55:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 00:55:47 UTC

- **253,277** saved flights
- **75,795** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **253,277** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,051,829.7 tonnes** estimated CO2 emissions
- **176,917,665 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10123 |
| 2 | SkyWest Airlines | 8841 |
| 3 | EJA | 4892 |
| 4 | IndiGo | 4237 |
| 5 | American Airlines | 4031 |
| 6 | Southwest Airlines | 3746 |
| 7 | Delta Air Lines | 3193 |
| 8 | ENY | 3024 |
| 9 | LATAM Airlines | 2439 |
| 10 | AZU | 2355 |
| 11 | Vueling | 2155 |
| 12 | WIF | 2026 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1980 |
| 15 | easyJet | 1732 |
| 16 | Swiss International | 1699 |
| 17 | QLK | 1631 |
| 18 | AXM | 1630 |
| 19 | EJU | 1620 |
| 20 | United Airlines | 1576 |
| 21 | Alaska Airlines | 1510 |
| 22 | All Nippon Airways | 1479 |
| 23 | WMT | 1433 |
| 24 | GLO | 1408 |
| 25 | PGT | 1392 |
| 26 | VIV | 1385 |
| 27 | Air France | 1379 |
| 28 | Wizz Air | 1379 |
| 29 | JetBlue | 1237 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210298 |
| 2 | 🇪🇸 ES | 16153 |
| 3 | 🇧🇷 BR | 14775 |
| 4 | 🇦🇺 AU | 14433 |
| 5 | 🇨🇦 CA | 14095 |
| 6 | 🇮🇹 IT | 13865 |
| 7 | 🇮🇳 IN | 13256 |
| 8 | 🇩🇪 DE | 12395 |
| 9 | 🇬🇧 GB | 11838 |
| 10 | 🇨🇴 CO | 11212 |
| 11 | 🇫🇷 FR | 10175 |
| 12 | 🇯🇵 JP | 9926 |
| 13 | 🇹🇷 TR | 7574 |
| 14 | 🇬🇷 GR | 7410 |
| 15 | 🇲🇽 MX | 6981 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6260 |
| 18 | 🇹🇭 TH | 4549 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4213 |
| 22 | 🇳🇿 NZ | 3467 |
| 23 | 🇵🇭 PH | 3430 |
| 24 | 🇬🇹 GT | 3148 |
| 25 | 🇰🇷 KR | 2916 |
| 26 | 🇭🇷 HR | 2907 |
| 27 | 🇲🇦 MA | 2556 |
| 28 | 🇲🇪 ME | 2381 |
| 29 | 🇳🇱 NL | 2282 |
| 30 | 🇮🇩 ID | 2164 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5217 |
| 2 | Denver International Airport |  | US | 4093 |
| 3 | Indira Gandhi International Airport |  | IN | 3072 |
| 4 | Tokyo International Airport |  | JP | 2962 |
| 5 | Guaymaral Airport |  | CO | 2747 |
| 6 | Harry Reid International Airport |  | US | 2690 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2592 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2565 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2401 |
| 12 | Salt Lake City International Airport |  | US | 2236 |
| 13 | Chicago O'Hare International Airport |  | US | 2211 |
| 14 | Congonhas Airport |  | BR | 2169 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2078 |
| 16 | Capua Airport |  | IT | 1997 |
| 17 | Madrid Barajas International Airport |  | ES | 1987 |
| 18 | Frankfurt am Main International Airport |  | DE | 1964 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1897 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1841 |
| 21 | Malpensa International Airport |  | IT | 1821 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1778 |
| 23 | Charles de Gaulle International Airport |  | FR | 1774 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1764 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1694 |
| 26 | Ninoy Aquino International Airport |  | PH | 1677 |
| 27 | Macau International Airport |  | MO | 1671 |
| 28 | Barcelona International Airport |  | ES | 1594 |
| 29 | Charlotte/Douglas International Airport |  | US | 1593 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1512 |
| 33 | Seattle-Tacoma International Airport |  | US | 1493 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1468 |
| 35 | Calgary International Airport |  | CA | 1461 |
| 36 | Don Mueang International Airport |  | TH | 1456 |
| 37 | Bengaluru International Airport |  | IN | 1443 |
| 38 | Oslo Gardermoen Airport |  | NO | 1428 |
| 39 | Vancouver International Airport |  | CA | 1419 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 940 | 21m | 244 km | 3,958.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 676 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 635 | 1h 6m | 770 km | 8,435.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 566 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 380 | 44m | 241 km | 1,578.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 372 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 338 | 23m | 55 km | 321.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 312 | 26m | 215 km | 1,155.5 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 307 | 19m | 99 km | 525.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 303 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 290 | 1h 14m | 961 km | 4,806.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N99725 |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-09-10 00:36 UTC | 2026-09-10 00:55 UTC | 19m |
| PCM7703 | PCM | Visalia Municipal Airport (KVIS) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-09 23:43 UTC | 2026-09-10 00:51 UTC | 1h 7m |
| N83480 |  | Sandridge Airpark Inc Airport (OK94) | Sandridge Airpark Inc Airport (OK94) | 2026-09-10 00:45 UTC | 2026-09-10 00:49 UTC | 4m |
| N53FJ |  | Midland International Air And Space Port Airport (KMAF) | Austin Executive Airport (KEDC) | 2026-09-10 00:06 UTC | 2026-09-10 00:49 UTC | 42m |
| N42BG |  | Bend Municipal Airport (KBDN) | Palo Alto Airport (KPAO) | 2026-09-09 22:59 UTC | 2026-09-10 00:48 UTC | 1h 49m |
|  |  | 93FD (93FD) | 93FD (93FD) | 2026-09-10 00:47 UTC | 2026-09-10 00:47 UTC | 0m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-09-10 00:23 UTC | 2026-09-10 00:46 UTC | 23m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-09-09 20:07 UTC | 2026-09-10 00:45 UTC | 4h 37m |
| SND3 | SND | Corowa Airport (YCOR) | Corowa Airport (YCOR) | 2026-09-10 00:33 UTC | 2026-09-10 00:44 UTC | 11m |
| N830GS |  | Harry Reid International Airport (KLAS) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-09 23:57 UTC | 2026-09-10 00:38 UTC | 40m |
| N10EH |  | Salt Lake City International Airport (KSLC) | Rock & A Hard Place Ranch Airport (WY61) | 2026-09-09 23:53 UTC | 2026-09-10 00:34 UTC | 41m |
| UAE441 | Emirates | Adelaide International Airport (YPAD) | Fujairah International Airport (OMFJ) | 2026-09-09 12:36 UTC | 2026-09-10 00:34 UTC | 11h 58m |
| AVA007 | Avianca | Miami International Airport (KMIA) | El Dorado International Airport (SKBO) | 2026-09-09 21:19 UTC | 2026-09-10 00:32 UTC | 3h 12m |
| N251GM |  | John Wayne/Orange County Airport (KSNA) | 5XS2 (5XS2) | 2026-09-09 22:18 UTC | 2026-09-10 00:30 UTC | 2h 12m |
| VHJKM | VHJ | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-09-09 23:29 UTC | 2026-09-10 00:30 UTC | 1h 0m |
| N950TT |  | Wheeler Army Air Field (PHHI) | Kawaihapai Airfield (PHDH) | 2026-09-10 00:19 UTC | 2026-09-10 00:30 UTC | 10m |
| N778SC |  | Church's Landing Airport (1MU8) | Chiriaco Summit Airport (KL77) | 2026-09-09 21:46 UTC | 2026-09-10 00:29 UTC | 2h 43m |
| ZKNAL | ZKN | Motueka Airport (NZMK) | Motueka Airport (NZMK) | 2026-09-10 00:06 UTC | 2026-09-10 00:28 UTC | 21m |
| N585EC |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-09-10 00:10 UTC | 2026-09-10 00:26 UTC | 15m |
| N907KW |  | Healy River Airport (PAHV) | Nugget Bench Airport (33AK) | 2026-09-09 23:33 UTC | 2026-09-10 00:25 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
