# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_23:05:00_UTC-green)

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

**Latest saved flight:** 2026-09-19 23:05:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 23:05:00 UTC

- **264,039** saved flights
- **77,955** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,039** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,199,711.7 tonnes** estimated CO2 emissions
- **185,490,532 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10444 |
| 2 | SkyWest Airlines | 9180 |
| 3 | EJA | 5135 |
| 4 | IndiGo | 4437 |
| 5 | American Airlines | 4132 |
| 6 | Southwest Airlines | 3885 |
| 7 | Delta Air Lines | 3290 |
| 8 | ENY | 3112 |
| 9 | LATAM Airlines | 2551 |
| 10 | AZU | 2485 |
| 11 | Vueling | 2216 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2070 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1742 |
| 17 | QLK | 1703 |
| 18 | EJU | 1665 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1619 |
| 21 | Alaska Airlines | 1564 |
| 22 | All Nippon Airways | 1522 |
| 23 | PGT | 1486 |
| 24 | WMT | 1484 |
| 25 | GLO | 1471 |
| 26 | Air France | 1445 |
| 27 | VIV | 1442 |
| 28 | Wizz Air | 1431 |
| 29 | CXK | 1279 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219423 |
| 2 | 🇪🇸 ES | 16634 |
| 3 | 🇧🇷 BR | 15468 |
| 4 | 🇦🇺 AU | 15111 |
| 5 | 🇨🇦 CA | 14704 |
| 6 | 🇮🇹 IT | 14357 |
| 7 | 🇮🇳 IN | 14019 |
| 8 | 🇩🇪 DE | 12749 |
| 9 | 🇬🇧 GB | 12252 |
| 10 | 🇨🇴 CO | 11987 |
| 11 | 🇫🇷 FR | 10549 |
| 12 | 🇯🇵 JP | 10208 |
| 13 | 🇹🇷 TR | 7999 |
| 14 | 🇬🇷 GR | 7657 |
| 15 | 🇲🇽 MX | 7265 |
| 16 | 🇨🇭 CH | 7048 |
| 17 | 🇳🇴 NO | 6516 |
| 18 | 🇹🇭 TH | 4732 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4350 |
| 22 | 🇳🇿 NZ | 3660 |
| 23 | 🇵🇭 PH | 3509 |
| 24 | 🇬🇹 GT | 3364 |
| 25 | 🇭🇷 HR | 3010 |
| 26 | 🇰🇷 KR | 2992 |
| 27 | 🇲🇦 MA | 2645 |
| 28 | 🇲🇪 ME | 2474 |
| 29 | 🇳🇱 NL | 2366 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5397 |
| 2 | Denver International Airport |  | US | 4273 |
| 3 | Indira Gandhi International Airport |  | IN | 3169 |
| 4 | Tokyo International Airport |  | JP | 3048 |
| 5 | El Dorado International Airport |  | CO | 2809 |
| 6 | Harry Reid International Airport |  | US | 2809 |
| 7 | Guaymaral Airport |  | CO | 2785 |
| 8 | Zurich Airport |  | CH | 2747 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2654 |
| 10 | La Aurora Airport |  | GT | 2556 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2555 |
| 12 | Salt Lake City International Airport |  | US | 2326 |
| 13 | Chicago O'Hare International Airport |  | US | 2268 |
| 14 | Congonhas Airport |  | BR | 2255 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2157 |
| 16 | Capua Airport |  | IT | 2065 |
| 17 | Madrid Barajas International Airport |  | ES | 2039 |
| 18 | Frankfurt am Main International Airport |  | DE | 2015 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1996 |
| 20 | Malpensa International Airport |  | IT | 1902 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1891 |
| 22 | Charles de Gaulle International Airport |  | FR | 1864 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1858 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1836 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1803 |
| 26 | Macau International Airport |  | MO | 1758 |
| 27 | Ninoy Aquino International Airport |  | PH | 1723 |
| 28 | Barcelona International Airport |  | ES | 1647 |
| 29 | Charlotte/Douglas International Airport |  | US | 1646 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1623 |
| 31 | Viracopos International Airport |  | BR | 1603 |
| 32 | Kuala Lumpur International Airport |  | MY | 1603 |
| 33 | Seattle-Tacoma International Airport |  | US | 1551 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1540 |
| 35 | Calgary International Airport |  | CA | 1507 |
| 36 | Don Mueang International Airport |  | TH | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1498 |
| 38 | Oslo Gardermoen Airport |  | NO | 1486 |
| 39 | Vancouver International Airport |  | CA | 1478 |
| 40 | Antalya International Airport |  | TR | 1414 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 987 | 21m | 244 km | 4,156.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 725 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 663 | 1h 6m | 770 km | 8,807.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 657 | 24m | 225 km | 2,548.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 417 | 1h 50m | 1,423 km | 10,233.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 377 | 24m | 218 km | 1,420.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 337 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 283 | 42m | 535 km | 2,613.7 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 266 | 18m | 14 km | 66.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-09-19 22:16 UTC | 2026-09-19 23:05 UTC | 48m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-09-19 11:34 UTC | 2026-09-19 23:04 UTC | 11h 30m |
| N23DD |  | Van Nuys Airport (KVNY) | Santa Monica Municipal Airport (KSMO) | 2026-09-19 22:45 UTC | 2026-09-19 23:03 UTC | 17m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-09-19 12:08 UTC | 2026-09-19 22:50 UTC | 10h 41m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-19 18:22 UTC | 2026-09-19 22:46 UTC | 4h 23m |
| N973JH |  | Madras Municipal Airport (KS33) | Greenleaf Air Ranch Airport (ID90) | 2026-09-19 21:55 UTC | 2026-09-19 22:41 UTC | 45m |
| N2206B |  | Sky Manor Airport (KN40) | Aeroflex/Andover Airport (K12N) | 2026-09-19 22:24 UTC | 2026-09-19 22:41 UTC | 16m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-09-19 12:01 UTC | 2026-09-19 22:40 UTC | 10h 38m |
| N80807 |  | Denton Enterprise Airport (KDTO) | TA08 (TA08) | 2026-09-19 21:50 UTC | 2026-09-19 22:37 UTC | 46m |
| EJA434 | EJA | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-09-19 22:30 UTC | 2026-09-19 22:36 UTC | 6m |
| FDX169 | FDX | Singapore Changi International Airport (WSSS) | Chek Lap Kok International Airport (VHHH) | 2026-09-19 19:12 UTC | 2026-09-19 22:35 UTC | 3h 23m |
| N828SC |  | Scappoose Airport (KSPB) | Scappoose Airport (KSPB) | 2026-09-19 22:05 UTC | 2026-09-19 22:35 UTC | 30m |
| SGA2552 | SGA | Sharjah International Airport (OMSJ) | Chek Lap Kok International Airport (VHHH) | 2026-09-19 10:14 UTC | 2026-09-19 22:29 UTC | 12h 14m |
| N33395 |  | 80WA (80WA) | Arlington Municipal Airport (KAWO) | 2026-09-19 22:05 UTC | 2026-09-19 22:26 UTC | 20m |
| HK5084 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-09-19 22:20 UTC | 2026-09-19 22:24 UTC | 4m |
| N229LJ |  | Northwest Arkansas Ntl Airport (KXNA) | Petit Jean Park Airport (KMPJ) | 2026-09-19 22:06 UTC | 2026-09-19 22:22 UTC | 16m |
| XE1194 |  | Santa Monica Municipal Airport (KSMO) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-19 21:09 UTC | 2026-09-19 22:22 UTC | 1h 13m |
| N8584V |  | Olympia Regional Airport (KOLM) | Olympia Regional Airport (KOLM) | 2026-09-19 22:08 UTC | 2026-09-19 22:21 UTC | 12m |
| N64087 |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-09-19 21:37 UTC | 2026-09-19 22:19 UTC | 41m |
| N544SW |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-19 20:45 UTC | 2026-09-19 22:18 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
