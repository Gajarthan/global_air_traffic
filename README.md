# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_11:31:12_UTC-green)

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

**Latest saved flight:** 2026-08-16 11:31:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 11:31:12 UTC

- **204,339** saved flights
- **65,339** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,339** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,456,994.1 tonnes** estimated CO2 emissions
- **142,434,438 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8039 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3499 |
| 5 | American Airlines | 3401 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2612 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1837 |
| 11 | Lufthansa | 1741 |
| 12 | Vueling | 1693 |
| 13 | WIF | 1645 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1412 |
| 16 | Swiss International | 1361 |
| 17 | AXM | 1334 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1261 |
| 21 | EJU | 1249 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1119 |
| 24 | GLO | 1095 |
| 25 | Air France | 1089 |
| 26 | PGT | 1089 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1043 |
| 29 | WMT | 1021 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173789 |
| 2 | 🇪🇸 ES | 13064 |
| 3 | 🇧🇷 BR | 11647 |
| 4 | 🇦🇺 AU | 11480 |
| 5 | 🇨🇦 CA | 11281 |
| 6 | 🇮🇳 IN | 10921 |
| 7 | 🇮🇹 IT | 10602 |
| 8 | 🇩🇪 DE | 10107 |
| 9 | 🇬🇧 GB | 9530 |
| 10 | 🇯🇵 JP | 8439 |
| 11 | 🇫🇷 FR | 8092 |
| 12 | 🇨🇴 CO | 8046 |
| 13 | 🇬🇷 GR | 6007 |
| 14 | 🇹🇷 TR | 5744 |
| 15 | 🇲🇽 MX | 5742 |
| 16 | 🇨🇭 CH | 5473 |
| 17 | 🇳🇴 NO | 5096 |
| 18 | 🇲🇾 MY | 3512 |
| 19 | 🇿🇦 ZA | 3418 |
| 20 | 🇵🇱 PL | 3354 |
| 21 | 🇹🇭 TH | 3229 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2723 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2500 |
| 26 | 🇭🇷 HR | 2170 |
| 27 | 🇲🇦 MA | 2052 |
| 28 | 🇳🇱 NL | 1817 |
| 29 | 🇲🇪 ME | 1706 |
| 30 | 🇮🇩 ID | 1678 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2545 |
| 4 | Indira Gandhi International Airport |  | IN | 2479 |
| 5 | Guaymaral Airport |  | CO | 2476 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2136 |
| 8 | Zurich Airport |  | CH | 2126 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1861 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Frankfurt am Main International Airport |  | DE | 1695 |
| 16 | Congonhas Airport |  | BR | 1694 |
| 17 | Madrid Barajas International Airport |  | ES | 1597 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1549 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1405 |
| 25 | Charles de Gaulle International Airport |  | FR | 1396 |
| 26 | Charlotte/Douglas International Airport |  | US | 1391 |
| 27 | Kuala Lumpur International Airport |  | MY | 1302 |
| 28 | Ninoy Aquino International Airport |  | PH | 1290 |
| 29 | Bengaluru International Airport |  | IN | 1270 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1221 |
| 33 | Seattle-Tacoma International Airport |  | US | 1213 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1127 |
| 38 | Vitoria/Foronda Airport |  | ES | 1127 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 498 | 1h 7m | 770 km | 6,615.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 343 | 27m | 275 km | 1,625.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 300 | 44m | 241 km | 1,246.1 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 295 | 1h 49m | 1,423 km | 7,239.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 266 | 21m | 250 km | 1,149.0 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 253 | 24m | 218 km | 953.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 240 | 1h 37m | 1,156 km | 4,787.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 235 | 19m | 144 km | 584.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 231 | 31m | 369 km | 1,470.4 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| S5HPL |  | Ljubljana Joze Pucnik Airport (LJLJ) | Ljubljana Joze Pucnik Airport (LJLJ) | 2026-08-16 11:06 UTC | 2026-08-16 11:31 UTC | 25m |
| CPV369 | CPV | Thiene Airport (LIDH) | Belluno Airport (LIDB) | 2026-08-16 11:03 UTC | 2026-08-16 11:19 UTC | 16m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-16 10:38 UTC | 2026-08-16 11:07 UTC | 29m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-16 10:54 UTC | 2026-08-16 11:07 UTC | 12m |
| SXS9LY | SXS | Vienna International Airport (LOWW) | Karain Airport (LTXE) | 2026-08-16 08:30 UTC | 2026-08-16 11:02 UTC | 2h 31m |
| WIF808 | WIF | Bodø Airport (ENBO) | Leknes Airport (ENLK) | 2026-08-16 10:49 UTC | 2026-08-16 11:00 UTC | 10m |
| HBLKN | HBL | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-16 10:43 UTC | 2026-08-16 10:57 UTC | 13m |
| IGO6393 | IndiGo | Juhu Aerodrome (VAJJ) | Chandigarh Airport (VICG) | 2026-08-16 09:09 UTC | 2026-08-16 10:49 UTC | 1h 40m |
| PH1074 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-16 09:46 UTC | 2026-08-16 10:48 UTC | 1h 1m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-08-16 09:12 UTC | 2026-08-16 10:43 UTC | 1h 30m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 09:52 UTC | 2026-08-16 10:41 UTC | 48m |
| AUA617 | Austrian Airlines | Vienna International Airport (LOWW) | Otocac Airport (LDRO) | 2026-08-16 10:02 UTC | 2026-08-16 10:40 UTC | 38m |
| APG715 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-08-16 10:08 UTC | 2026-08-16 10:35 UTC | 27m |
| WZZ3XL | Wizz Air | Gdańsk Lech Wałęsa Airport (EPGD) | Berane Airport (LYBR) | 2026-08-16 08:54 UTC | 2026-08-16 10:34 UTC | 1h 40m |
| ASL987 | ASL | Belgrade Nikola Tesla Airport (LYBE) | Smolensk North Airport (XUBS) | 2026-08-15 12:32 UTC | 2026-08-16 10:31 UTC | 21h 59m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-16 09:58 UTC | 2026-08-16 10:31 UTC | 32m |
| AIQ3021 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-08-16 09:44 UTC | 2026-08-16 10:29 UTC | 44m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-08-16 09:43 UTC | 2026-08-16 10:29 UTC | 46m |
| HKE694 | HKE | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-08-16 07:41 UTC | 2026-08-16 10:29 UTC | 2h 47m |
| LNX06AR | LNX | Newcastle Airport (EGNT) | RAF Northolt (EGWU) | 2026-08-16 09:42 UTC | 2026-08-16 10:27 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
