# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_08:46:09_UTC-green)

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

**Latest saved flight:** 2026-08-16 08:46:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 08:46:09 UTC

- **203,969** saved flights
- **65,294** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,969** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,451,182.0 tonnes** estimated CO2 emissions
- **142,097,508 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8019 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3478 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2611 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1837 |
| 11 | Lufthansa | 1738 |
| 12 | Vueling | 1688 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1400 |
| 16 | Swiss International | 1356 |
| 17 | AXM | 1325 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1259 |
| 21 | EJU | 1248 |
| 22 | All Nippon Airways | 1240 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | Air France | 1084 |
| 26 | PGT | 1083 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1041 |
| 29 | WMT | 1015 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173783 |
| 2 | 🇪🇸 ES | 13026 |
| 3 | 🇧🇷 BR | 11646 |
| 4 | 🇦🇺 AU | 11468 |
| 5 | 🇨🇦 CA | 11281 |
| 6 | 🇮🇳 IN | 10864 |
| 7 | 🇮🇹 IT | 10563 |
| 8 | 🇩🇪 DE | 10085 |
| 9 | 🇬🇧 GB | 9477 |
| 10 | 🇯🇵 JP | 8392 |
| 11 | 🇫🇷 FR | 8065 |
| 12 | 🇨🇴 CO | 8046 |
| 13 | 🇬🇷 GR | 5989 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5701 |
| 16 | 🇨🇭 CH | 5450 |
| 17 | 🇳🇴 NO | 5079 |
| 18 | 🇲🇾 MY | 3485 |
| 19 | 🇿🇦 ZA | 3390 |
| 20 | 🇵🇱 PL | 3342 |
| 21 | 🇹🇭 TH | 3209 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2710 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2488 |
| 26 | 🇭🇷 HR | 2151 |
| 27 | 🇲🇦 MA | 2044 |
| 28 | 🇳🇱 NL | 1810 |
| 29 | 🇲🇪 ME | 1696 |
| 30 | 🇮🇩 ID | 1667 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2533 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2468 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2131 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2115 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1861 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1826 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1693 |
| 17 | Madrid Barajas International Airport |  | ES | 1593 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1545 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1435 |
| 24 | Malpensa International Airport |  | IT | 1400 |
| 25 | Charlotte/Douglas International Airport |  | US | 1391 |
| 26 | Charles de Gaulle International Airport |  | FR | 1391 |
| 27 | Kuala Lumpur International Airport |  | MY | 1293 |
| 28 | Ninoy Aquino International Airport |  | PH | 1283 |
| 29 | Bengaluru International Airport |  | IN | 1265 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1219 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1121 |
| 38 | Vitoria/Foronda Airport |  | ES | 1121 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1097 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 494 | 1h 7m | 770 km | 6,562.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 476 | 24m | 225 km | 1,846.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 341 | 27m | 275 km | 1,615.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 293 | 1h 49m | 1,423 km | 7,190.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 252 | 24m | 218 km | 949.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 230 | 31m | 369 km | 1,464.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DESAD | DES | Essen Mulheim Airport (EDLE) | Essen Mulheim Airport (EDLE) | 2026-08-16 08:29 UTC | 2026-08-16 08:46 UTC | 16m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 07:39 UTC | 2026-08-16 08:32 UTC | 52m |
| RGA08 | RGA | Ambri Airport (LSPM) | Lodrino Air Base (LSML) | 2026-08-16 07:59 UTC | 2026-08-16 08:28 UTC | 28m |
| DKEGL | DKE | Kempten-Durach Airport (EDMK) | Hoefen Airport (LOIR) | 2026-08-16 07:45 UTC | 2026-08-16 08:26 UTC | 41m |
| OKHEZ | OKH | Sumperk Airport (LKSU) | Sumperk Airport (LKSU) | 2026-08-16 08:03 UTC | 2026-08-16 08:22 UTC | 19m |
| DFILL | DFI | Marl Loemuhle Airport (EDLM) | Marl Loemuhle Airport (EDLM) | 2026-08-16 07:26 UTC | 2026-08-16 08:08 UTC | 42m |
| LUC6J | LUC | Farnborough Airport (EGLF) | Liverpool John Lennon Airport (EGGP) | 2026-08-16 07:25 UTC | 2026-08-16 08:08 UTC | 43m |
| AWH16S | AWH | Frankfurt am Main International Airport (EDDF) | Hildesheim Airport (EDVM) | 2026-08-16 07:36 UTC | 2026-08-16 08:07 UTC | 31m |
| RYR2PX | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Bristol International Airport (EGGD) | 2026-08-16 05:36 UTC | 2026-08-16 07:58 UTC | 2h 21m |
| HBKNI | HBK | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-16 07:15 UTC | 2026-08-16 07:53 UTC | 37m |
| CSI502 | CSI | Las Cruces International Airport (KLRU) | NM49 (NM49) | 2026-08-16 07:12 UTC | 2026-08-16 07:51 UTC | 38m |
| HBKNN | HBK | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-16 07:19 UTC | 2026-08-16 07:50 UTC | 30m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-16 07:26 UTC | 2026-08-16 07:46 UTC | 20m |
| HBZZX | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-16 06:57 UTC | 2026-08-16 07:44 UTC | 47m |
| HBZVQ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-16 06:56 UTC | 2026-08-16 07:42 UTC | 45m |
| ANA397 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-08-16 07:15 UTC | 2026-08-16 07:41 UTC | 26m |
| CHX29 | CHX | Hamburg Airport (EDDH) | Hamburg-Finkenwerder Airport (EDHI) | 2026-08-16 07:37 UTC | 2026-08-16 07:41 UTC | 4m |
| GAP2045 | GAP | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-16 07:15 UTC | 2026-08-16 07:40 UTC | 25m |
| N733AM |  | Whiteman Airport (KWHP) | San Bernardino International Airport (KSBD) | 2026-08-16 06:55 UTC | 2026-08-16 07:39 UTC | 44m |
| JL3676 |  | Amakusa Airport (RJDA) | Iki Airport (RJDB) | 2026-08-16 07:23 UTC | 2026-08-16 07:37 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
