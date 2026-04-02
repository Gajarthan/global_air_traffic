# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_06:24:31_UTC-green)

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

**Latest saved flight:** 2026-04-02 06:24:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 06:24:31 UTC

- **10,306** saved flights
- **6,075** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,306** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **125,997.3 tonnes** estimated CO2 emissions
- **7,304,191 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 387 |
| 3 | IndiGo | 272 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | AXM | 109 |
| 10 | LATAM Airlines | 106 |
| 11 | Vueling | 106 |
| 12 | LXJ | 100 |
| 13 | All Nippon Airways | 89 |
| 14 | QLK | 89 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 80 |
| 17 | Swiss International | 73 |
| 18 | Alaska Airlines | 72 |
| 19 | VIV | 72 |
| 20 | AZU | 71 |
| 21 | Japan Airlines | 68 |
| 22 | AXB | 66 |
| 23 | EDV | 66 |
| 24 | United Airlines | 65 |
| 25 | Cathay Pacific | 63 |
| 26 | Avianca | 60 |
| 27 | BRC | 58 |
| 28 | easyJet | 57 |
| 29 | ANZ | 55 |
| 30 | EJU | 55 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8538 |
| 2 | 🇦🇺 AU | 851 |
| 3 | 🇮🇳 IN | 833 |
| 4 | 🇪🇸 ES | 767 |
| 5 | 🇧🇷 BR | 540 |
| 6 | 🇩🇪 DE | 535 |
| 7 | 🇨🇴 CO | 524 |
| 8 | 🇯🇵 JP | 516 |
| 9 | 🇨🇦 CA | 508 |
| 10 | 🇮🇹 IT | 443 |
| 11 | 🇲🇽 MX | 377 |
| 12 | 🇬🇧 GB | 355 |
| 13 | 🇫🇷 FR | 302 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇳🇿 NZ | 257 |
| 16 | 🇲🇾 MY | 245 |
| 17 | 🇬🇷 GR | 236 |
| 18 | 🇨🇭 CH | 225 |
| 19 | 🇬🇹 GT | 209 |
| 20 | 🇿🇦 ZA | 205 |
| 21 | 🇵🇭 PH | 198 |
| 22 | 🇰🇷 KR | 173 |
| 23 | 🇹🇷 TR | 163 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 127 |
| 26 | 🇹🇭 TH | 119 |
| 27 | 🇲🇦 MA | 117 |
| 28 | 🇲🇴 MO | 114 |
| 29 | 🇲🇪 ME | 99 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Denver International Airport |  | US | 189 |
| 3 | Tokyo International Airport |  | JP | 185 |
| 4 | Indira Gandhi International Airport |  | IN | 185 |
| 5 | El Dorado International Airport |  | CO | 173 |
| 6 | Frankfurt am Main International Airport |  | DE | 166 |
| 7 | Harry Reid International Airport |  | US | 148 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 125 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 124 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 114 |
| 13 | Macau International Airport |  | MO | 114 |
| 14 | Zurich Airport |  | CH | 113 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Reno/Tahoe International Airport |  | US | 95 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 92 |
| 19 | Charlotte/Douglas International Airport |  | US | 92 |
| 20 | Tenerife Norte Airport |  | ES | 92 |
| 21 | Madrid Barajas International Airport |  | ES | 91 |
| 22 | Kuala Lumpur International Airport |  | MY | 91 |
| 23 | Ninoy Aquino International Airport |  | PH | 89 |
| 24 | Bengaluru International Airport |  | IN | 89 |
| 25 | Daniel K Inouye International Airport |  | US | 81 |
| 26 | Congonhas Airport |  | BR | 81 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 79 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 76 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 30 | Salt Lake City International Airport |  | US | 75 |
| 31 | Malpensa International Airport |  | IT | 74 |
| 32 | Austin-Bergstrom International Airport |  | US | 72 |
| 33 | Seattle-Tacoma International Airport |  | US | 72 |
| 34 | Vitoria/Foronda Airport |  | ES | 71 |
| 35 | Pune Airport |  | IN | 71 |
| 36 | Charles de Gaulle International Airport |  | FR | 69 |
| 37 | Barcelona International Airport |  | ES | 69 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | Calgary International Airport |  | CA | 67 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 65 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 45 | 1h 7m | 706 km | 547.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 38 | 24m | 225 km | 147.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 31 | 30m | 304 km | 162.5 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 31 | 1h 44m | 1,156 km | 618.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 28 | 20m | 165 km | 79.6 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 26 | 1h 26m | 910 km | 408.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 24 | 30m | 369 km | 152.8 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 21 | 53m | 546 km | 197.7 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 20 | 1h 10m | 770 km | 265.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 20 | 1h 55m | 1,304 km | 449.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 18 | 11m | 127 km | 39.4 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 16 | 32m | - | - |
| 27 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 16 | 18m | 26 km | 7.2 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 15 | 1h 17m | 924 km | 239.2 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 15 | 17m | 183 km | 47.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSN6040 | China Southern | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-04-01 18:44 UTC | 2026-04-02 06:24 UTC | 11h 40m |
| FOE | FOE | Gold Coast Airport (YBCG) | Sunshine Coast Airport (YBMC) | 2026-04-02 05:37 UTC | 2026-04-02 06:22 UTC | 45m |
| FKT | FKT | Caboolture Airport (YCAB) | Sunshine Coast Airport (YBMC) | 2026-04-02 05:55 UTC | 2026-04-02 06:12 UTC | 16m |
| COLT62 | COL | Nagoya Airport (RJNA) | Ojika Airport (RJDO) | 2026-04-02 04:56 UTC | 2026-04-02 06:05 UTC | 1h 8m |
| SWA1934 | Southwest Airlines | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-04-02 04:53 UTC | 2026-04-02 05:48 UTC | 55m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-04-02 04:49 UTC | 2026-04-02 05:44 UTC | 54m |
| BEL5BN | Brussels Airlines | Melsbroek Air Base (EBMB) | Malpensa International Airport (LIMC) | 2026-04-02 04:31 UTC | 2026-04-02 05:43 UTC | 1h 11m |
| L2B |  | Melbourne Essendon Airport (YMEN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-02 04:42 UTC | 2026-04-02 05:42 UTC | 1h 0m |
| EWG56R | EWG | Stuttgart Airport (EDDS) | Hamburg Airport (EDDH) | 2026-04-02 04:45 UTC | 2026-04-02 05:39 UTC | 54m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-02 05:13 UTC | 2026-04-02 05:39 UTC | 25m |
| CWA927 | CWA | Red Deer Regional Airport (CYQF) | Hardisty Airport (CEA5) | 2026-04-02 05:13 UTC | 2026-04-02 05:36 UTC | 22m |
| LKF | LKF | Perth Jandakot Airport (YPJT) | Perenjori Airport (YPJI) | 2026-04-02 04:37 UTC | 2026-04-02 05:34 UTC | 56m |
| CEB1111 | CEB | Diosdado Macapagal International Airport (RPLC) | Wasig Airport (RPVL) | 2026-04-02 05:04 UTC | 2026-04-02 05:33 UTC | 29m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-01 17:50 UTC | 2026-04-02 05:28 UTC | 11h 38m |
| JAL2765 | Japan Airlines | Okadama Airport (RJCO) | Tokachi Airport (RJCT) | 2026-04-02 05:11 UTC | 2026-04-02 05:27 UTC | 15m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-01 15:06 UTC | 2026-04-02 05:26 UTC | 14h 19m |
| CPA937 | Cathay Pacific | Macau International Airport (VMMC) | Chek Lap Kok International Airport (VHHH) | 2026-04-02 05:19 UTC | 2026-04-02 05:25 UTC | 5m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-02 04:14 UTC | 2026-04-02 05:24 UTC | 1h 10m |
| KAL399T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-02 04:58 UTC | 2026-04-02 05:23 UTC | 25m |
| ANZ856M | ANZ | Christchurch International Airport (NZCH) | Lake Station Airport (NZLE) | 2026-04-02 04:52 UTC | 2026-04-02 05:21 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
