# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_19:47:39_UTC-green)

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

**Latest saved flight:** 2026-07-26 19:47:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 19:47:39 UTC

- **153,014** saved flights
- **50,749** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **153,014** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,830,605.8 tonnes** estimated CO2 emissions
- **106,122,077 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6183 |
| 2 | SkyWest Airlines | 5591 |
| 3 | EJA | 3036 |
| 4 | IndiGo | 2729 |
| 5 | American Airlines | 2425 |
| 6 | Southwest Airlines | 2324 |
| 7 | ENY | 1908 |
| 8 | Delta Air Lines | 1792 |
| 9 | Lufthansa | 1488 |
| 10 | LATAM Airlines | 1419 |
| 11 | AZU | 1330 |
| 12 | WIF | 1289 |
| 13 | Vueling | 1279 |
| 14 | LXJ | 1178 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 999 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 952 |
| 20 | QLK | 941 |
| 21 | EJU | 940 |
| 22 | VIV | 845 |
| 23 | CXK | 817 |
| 24 | AEE | 807 |
| 25 | MXY | 806 |
| 26 | Air France | 797 |
| 27 | GLO | 796 |
| 28 | JetBlue | 794 |
| 29 | United Airlines | 786 |
| 30 | Cathay Pacific | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 131902 |
| 2 | 🇪🇸 ES | 9899 |
| 3 | 🇧🇷 BR | 8689 |
| 4 | 🇦🇺 AU | 8597 |
| 5 | 🇮🇳 IN | 8577 |
| 6 | 🇨🇦 CA | 8162 |
| 7 | 🇮🇹 IT | 7924 |
| 8 | 🇩🇪 DE | 7823 |
| 9 | 🇬🇧 GB | 7018 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6064 |
| 12 | 🇨🇴 CO | 5236 |
| 13 | 🇲🇽 MX | 4419 |
| 14 | 🇬🇷 GR | 4368 |
| 15 | 🇳🇴 NO | 4045 |
| 16 | 🇨🇭 CH | 4023 |
| 17 | 🇹🇷 TR | 3659 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2624 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2221 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1996 |
| 26 | 🇲🇦 MA | 1563 |
| 27 | 🇲🇪 ME | 1494 |
| 28 | 🇭🇷 HR | 1408 |
| 29 | 🇳🇱 NL | 1403 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3153 |
| 2 | Denver International Airport |  | US | 2561 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1922 |
| 5 | Indira Gandhi International Airport |  | IN | 1904 |
| 6 | Harry Reid International Airport |  | US | 1878 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1717 |
| 8 | Zurich Airport |  | CH | 1668 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1598 |
| 10 | La Aurora Airport |  | GT | 1547 |
| 11 | Frankfurt am Main International Airport |  | DE | 1438 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1429 |
| 13 | Chicago O'Hare International Airport |  | US | 1402 |
| 14 | Salt Lake City International Airport |  | US | 1379 |
| 15 | El Dorado International Airport |  | CO | 1379 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1300 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1242 |
| 19 | Madrid Barajas International Airport |  | ES | 1221 |
| 20 | Capua Airport |  | IT | 1213 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1182 |
| 22 | Kuala Lumpur International Airport |  | MY | 1091 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1085 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1081 |
| 26 | Charles de Gaulle International Airport |  | FR | 1050 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1002 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 929 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 915 |
| 32 | Barcelona International Airport |  | ES | 911 |
| 33 | Daniel K Inouye International Airport |  | US | 910 |
| 34 | Tenerife Norte Airport |  | ES | 883 |
| 35 | Seattle-Tacoma International Airport |  | US | 879 |
| 36 | Scottsdale Airport |  | US | 867 |
| 37 | Calgary International Airport |  | CA | 866 |
| 38 | Viracopos International Airport |  | BR | 865 |
| 39 | Amsterdam Airport Schiphol |  | NL | 846 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 840 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 809 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 554 | 21m | 244 km | 2,332.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 372 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 280 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 274 | 27m | 275 km | 1,298.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 207 | 44m | 241 km | 859.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 186 | 30m | 49 km | 157.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 181 | 1h 15m | 961 km | 3,000.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 171 | 51m | 556 km | 1,639.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CCDAL | CCD | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-07-26 19:37 UTC | 2026-07-26 19:47 UTC | 10m |
| N89PT |  | 4AR5 (4AR5) | 4AR5 (4AR5) | 2026-07-26 18:59 UTC | 2026-07-26 19:36 UTC | 36m |
| RAM833B | Royal Air Maroc | Melsbroek Air Base (EBMB) | Tit Mellil Airport (GMMT) | 2026-07-26 16:52 UTC | 2026-07-26 19:31 UTC | 2h 39m |
| N997SE |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-26 17:53 UTC | 2026-07-26 19:31 UTC | 1h 38m |
|  |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-26 19:27 UTC | 2026-07-26 19:29 UTC | 2m |
| N4381L |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-07-26 19:01 UTC | 2026-07-26 19:28 UTC | 27m |
| STW011 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-07-26 16:21 UTC | 2026-07-26 19:25 UTC | 3h 4m |
| N399W |  | Oakland County International Airport (KPTK) | Gaylord Regional Airport (KGLR) | 2026-07-26 18:57 UTC | 2026-07-26 19:25 UTC | 28m |
| N661DS |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-07-26 18:54 UTC | 2026-07-26 19:25 UTC | 30m |
| HLE05 | HLE | Glasgow International Airport (EGPF) | Glasgow Prestwick Airport (EGPK) | 2026-07-26 19:09 UTC | 2026-07-26 19:24 UTC | 15m |
| N734VE |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-26 18:56 UTC | 2026-07-26 19:21 UTC | 24m |
| CYF107 | CYF | Ben Gurion International Airport (LLBG) | Ben Gurion International Airport (LLBG) | 2026-07-26 17:38 UTC | 2026-07-26 19:19 UTC | 1h 40m |
| N452SM |  | Atlanta Regional Falcon Field (KFFC) | Roosevelt Memorial Airport (K5A9) | 2026-07-26 18:57 UTC | 2026-07-26 19:19 UTC | 21m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-26 18:47 UTC | 2026-07-26 19:18 UTC | 31m |
| RAM983 | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Tit Mellil Airport (GMMT) | 2026-07-26 18:30 UTC | 2026-07-26 19:18 UTC | 48m |
| N159FM |  | Chicago Midway International Airport (KMDW) | York Airport (01SC) | 2026-07-26 18:03 UTC | 2026-07-26 19:17 UTC | 1h 13m |
| RAM997 | Royal Air Maroc | Francisco de Sá Carneiro Airport (LPPR) | Mohammed V International Airport (GMMN) | 2026-07-26 18:04 UTC | 2026-07-26 19:14 UTC | 1h 9m |
| EJA405 | EJA | Raleigh-Durham International Airport (KRDU) | Addison Airport (KADS) | 2026-07-26 16:56 UTC | 2026-07-26 19:12 UTC | 2h 16m |
| GRZLY39 | GRZ | Mc Clellan-Palomar Airport (KCRQ) | Walter's Camp Airport (CN98) | 2026-07-26 18:41 UTC | 2026-07-26 19:11 UTC | 30m |
| BYF21 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-07-26 19:02 UTC | 2026-07-26 19:10 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
