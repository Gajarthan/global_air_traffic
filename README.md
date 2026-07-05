# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_14:32:33_UTC-green)

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

**Latest saved flight:** 2026-07-05 14:32:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 14:32:33 UTC

- **129,575** saved flights
- **44,073** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,575** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,564,459.2 tonnes** estimated CO2 emissions
- **90,693,290 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5270 |
| 2 | SkyWest Airlines | 4798 |
| 3 | EJA | 2532 |
| 4 | IndiGo | 2436 |
| 5 | American Airlines | 1999 |
| 6 | Southwest Airlines | 1948 |
| 7 | ENY | 1623 |
| 8 | Delta Air Lines | 1552 |
| 9 | Lufthansa | 1364 |
| 10 | LATAM Airlines | 1177 |
| 11 | Vueling | 1152 |
| 12 | WIF | 1134 |
| 13 | AZU | 1103 |
| 14 | AXM | 1009 |
| 15 | LXJ | 1000 |
| 16 | Swiss International | 902 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 835 |
| 19 | easyJet | 829 |
| 20 | QLK | 816 |
| 21 | EJU | 803 |
| 22 | VIV | 718 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 707 |
| 25 | Air France | 703 |
| 26 | CXK | 695 |
| 27 | United Airlines | 690 |
| 28 | MXY | 677 |
| 29 | JetBlue | 673 |
| 30 | GLO | 659 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110790 |
| 2 | 🇪🇸 ES | 8645 |
| 3 | 🇮🇳 IN | 7636 |
| 4 | 🇦🇺 AU | 7519 |
| 5 | 🇧🇷 BR | 7273 |
| 6 | 🇨🇦 CA | 6831 |
| 7 | 🇩🇪 DE | 6815 |
| 8 | 🇮🇹 IT | 6778 |
| 9 | 🇬🇧 GB | 5759 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5157 |
| 12 | 🇨🇴 CO | 4092 |
| 13 | 🇲🇽 MX | 3782 |
| 14 | 🇬🇷 GR | 3696 |
| 15 | 🇳🇴 NO | 3524 |
| 16 | 🇨🇭 CH | 3325 |
| 17 | 🇹🇷 TR | 2833 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2153 |
| 20 | 🇵🇱 PL | 2126 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2012 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1387 |
| 27 | 🇲🇪 ME | 1287 |
| 28 | 🇳🇱 NL | 1216 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1133 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2699 |
| 2 | Denver International Airport |  | US | 2201 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1685 |
| 5 | Harry Reid International Airport |  | US | 1612 |
| 6 | Guaymaral Airport |  | CO | 1579 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1536 |
| 8 | Zurich Airport |  | CH | 1425 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1378 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1319 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1241 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1152 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1086 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1066 |
| 20 | Madrid Barajas International Airport |  | ES | 1064 |
| 21 | Congonhas Airport |  | BR | 1025 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 939 |
| 26 | Bengaluru International Airport |  | IN | 924 |
| 27 | Malpensa International Airport |  | IT | 878 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 874 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 816 |
| 31 | Barcelona International Airport |  | ES | 806 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 793 |
| 33 | Tenerife Norte Airport |  | ES | 784 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 754 |
| 36 | Vitoria/Foronda Airport |  | ES | 749 |
| 37 | Seattle-Tacoma International Airport |  | US | 747 |
| 38 | Scottsdale Airport |  | US | 744 |
| 39 | Viracopos International Airport |  | BR | 743 |
| 40 | Amsterdam Airport Schiphol |  | NL | 733 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 662 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 469 | 21m | 244 km | 1,974.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 239 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 181 | 44m | 241 km | 751.8 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 159 | 18m | 144 km | 395.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 148 | 54m | 136 km | 347.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N842EB |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-07-05 13:47 UTC | 2026-07-05 14:32 UTC | 44m |
| RPA5674 | Republic Airways | Cleveland-Hopkins International Airport (KCLE) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-05 13:13 UTC | 2026-07-05 14:31 UTC | 1h 17m |
| NXC255 | NXC | Southwest Florida International Airport (KRSW) | Heaven's Landing Airport (GE99) | 2026-07-05 12:45 UTC | 2026-07-05 14:28 UTC | 1h 43m |
| CAP1904 | CAP | Plymouth Municipal Airport (KPYM) | Southbridge Municipal Airport (K3B0) | 2026-07-05 13:48 UTC | 2026-07-05 14:27 UTC | 39m |
|  |  | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-07-05 14:07 UTC | 2026-07-05 14:25 UTC | 18m |
| N66HT |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-07-05 14:04 UTC | 2026-07-05 14:25 UTC | 20m |
| VOE9TN | VOE | Nantes Atlantique Airport (LFRS) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-05 13:09 UTC | 2026-07-05 14:24 UTC | 1h 14m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-05 13:49 UTC | 2026-07-05 14:22 UTC | 32m |
| N8273A |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-07-05 13:31 UTC | 2026-07-05 14:21 UTC | 50m |
| SCANER1 | SCA | Rolph Airport (CPH2) | Rolph Airport (CPH2) | 2026-07-05 13:20 UTC | 2026-07-05 14:15 UTC | 54m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-07-05 13:51 UTC | 2026-07-05 14:11 UTC | 19m |
| RNA202 | RNA | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-07-05 12:02 UTC | 2026-07-05 14:11 UTC | 2h 8m |
| IGO746L | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-07-05 13:09 UTC | 2026-07-05 14:06 UTC | 56m |
| N806JA |  | Port Colborne Airport (CPE5) | Port Colborne Airport (CPE5) | 2026-07-05 12:37 UTC | 2026-07-05 13:58 UTC | 1h 20m |
| N502PS |  | Charlo Airport (CYCL) | Bangor International Airport (KBGR) | 2026-07-05 13:13 UTC | 2026-07-05 13:58 UTC | 44m |
| CFBSX | CFB | Brampton Airport (CNC3) | Emsdale Airport (CNA4) | 2026-07-05 13:01 UTC | 2026-07-05 13:58 UTC | 56m |
| DFROH | DFR | Casale Monferrato Airport (LILM) | Casale Monferrato Airport (LILM) | 2026-07-05 11:49 UTC | 2026-07-05 13:57 UTC | 2h 8m |
| N8263W |  | Prescott Regional/Ernest A Love Field (KPRC) | Montezuma Airport (19AZ) | 2026-07-05 13:36 UTC | 2026-07-05 13:55 UTC | 18m |
| HB2471 |  | Fricktal-Schupfart Airport (LSZI) | Muenster Aero Airport (LSPU) | 2026-07-05 10:11 UTC | 2026-07-05 13:55 UTC | 3h 43m |
| N95021 |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-07-05 13:53 UTC | 2026-07-05 13:54 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
