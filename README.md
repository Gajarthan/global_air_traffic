# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_15:10:24_UTC-green)

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

**Latest saved flight:** 2026-07-23 15:10:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 15:10:24 UTC

- **145,570** saved flights
- **48,704** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,570** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,743,722.6 tonnes** estimated CO2 emissions
- **101,085,365 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5904 |
| 2 | SkyWest Airlines | 5319 |
| 3 | EJA | 2863 |
| 4 | IndiGo | 2638 |
| 5 | American Airlines | 2323 |
| 6 | Southwest Airlines | 2197 |
| 7 | ENY | 1809 |
| 8 | Delta Air Lines | 1723 |
| 9 | Lufthansa | 1446 |
| 10 | LATAM Airlines | 1342 |
| 11 | AZU | 1255 |
| 12 | Vueling | 1239 |
| 13 | WIF | 1238 |
| 14 | LXJ | 1121 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1032 |
| 17 | easyJet | 943 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 915 |
| 20 | QLK | 913 |
| 21 | EJU | 894 |
| 22 | VIV | 810 |
| 23 | CXK | 783 |
| 24 | AEE | 770 |
| 25 | JetBlue | 766 |
| 26 | Air France | 765 |
| 27 | MXY | 760 |
| 28 | Cathay Pacific | 758 |
| 29 | United Airlines | 756 |
| 30 | GLO | 748 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125353 |
| 2 | 🇪🇸 ES | 9433 |
| 3 | 🇦🇺 AU | 8340 |
| 4 | 🇮🇳 IN | 8261 |
| 5 | 🇧🇷 BR | 8217 |
| 6 | 🇨🇦 CA | 7737 |
| 7 | 🇮🇹 IT | 7577 |
| 8 | 🇩🇪 DE | 7500 |
| 9 | 🇬🇧 GB | 6638 |
| 10 | 🇯🇵 JP | 6094 |
| 11 | 🇫🇷 FR | 5783 |
| 12 | 🇨🇴 CO | 4767 |
| 13 | 🇲🇽 MX | 4239 |
| 14 | 🇬🇷 GR | 4127 |
| 15 | 🇳🇴 NO | 3882 |
| 16 | 🇨🇭 CH | 3798 |
| 17 | 🇹🇷 TR | 3414 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2451 |
| 20 | 🇿🇦 ZA | 2368 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2140 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1891 |
| 26 | 🇲🇦 MA | 1508 |
| 27 | 🇲🇪 ME | 1448 |
| 28 | 🇳🇱 NL | 1358 |
| 29 | 🇭🇷 HR | 1326 |
| 30 | 🇲🇴 MO | 1215 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2999 |
| 2 | Denver International Airport |  | US | 2434 |
| 3 | Tokyo International Airport |  | JP | 1959 |
| 4 | Indira Gandhi International Airport |  | IN | 1831 |
| 5 | Harry Reid International Airport |  | US | 1824 |
| 6 | Guaymaral Airport |  | CO | 1785 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1652 |
| 8 | Zurich Airport |  | CH | 1608 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1525 |
| 10 | La Aurora Airport |  | GT | 1464 |
| 11 | Frankfurt am Main International Airport |  | DE | 1395 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1371 |
| 13 | Chicago O'Hare International Airport |  | US | 1351 |
| 14 | Salt Lake City International Airport |  | US | 1306 |
| 15 | El Dorado International Airport |  | CO | 1298 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1263 |
| 17 | Macau International Airport |  | MO | 1215 |
| 18 | Capua Airport |  | IT | 1182 |
| 19 | Congonhas Airport |  | BR | 1168 |
| 20 | Madrid Barajas International Airport |  | ES | 1161 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1019 |
| 26 | Charles de Gaulle International Airport |  | FR | 1010 |
| 27 | Bengaluru International Airport |  | IN | 988 |
| 28 | Malpensa International Airport |  | IT | 939 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 891 |
| 31 | Barcelona International Airport |  | ES | 882 |
| 32 | Daniel K Inouye International Airport |  | US | 879 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 867 |
| 34 | Tenerife Norte Airport |  | ES | 833 |
| 35 | Seattle-Tacoma International Airport |  | US | 828 |
| 36 | Viracopos International Airport |  | BR | 827 |
| 37 | Calgary International Airport |  | CA | 826 |
| 38 | Scottsdale Airport |  | US | 824 |
| 39 | Amsterdam Airport Schiphol |  | NL | 818 |
| 40 | Oslo Gardermoen Airport |  | NO | 800 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 753 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 528 | 21m | 244 km | 2,223.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 352 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 262 | 26m | 275 km | 1,241.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 260 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 218 | 22m | 55 km | 207.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 194 | 1h 46m | 1,423 km | 4,761.1 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 194 | 44m | 241 km | 805.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N737ZC |  | TS92 (TS92) | Stephenville Clark Regional Airport (KSEP) | 2026-07-23 14:25 UTC | 2026-07-23 15:10 UTC | 45m |
| N904PW |  | Jacksonville Executive At Craig Airport (KCRG) | Lake City Gateway Airport (KLCQ) | 2026-07-23 14:34 UTC | 2026-07-23 15:05 UTC | 30m |
| RNGR820 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-07-23 14:38 UTC | 2026-07-23 15:04 UTC | 26m |
| HB2748 |  | Raron Airport (LSTA) | Megeve Airport (LFHM) | 2026-07-23 13:12 UTC | 2026-07-23 15:03 UTC | 1h 50m |
| CHH408 | CHH | Edinburgh Airport (EGPH) | Ukhta Airport (UUYH) | 2026-07-23 11:25 UTC | 2026-07-23 15:01 UTC | 3h 36m |
| N2054S |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-07-23 14:32 UTC | 2026-07-23 14:58 UTC | 25m |
| PH876 |  | Stendal-Borstel Airport (EDOV) | Stendal-Borstel Airport (EDOV) | 2026-07-23 13:51 UTC | 2026-07-23 14:57 UTC | 1h 6m |
| N5464D |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-23 14:06 UTC | 2026-07-23 14:56 UTC | 50m |
| RAM802L | Royal Air Maroc | Mohammed V International Airport (GMMN) | London Gatwick Airport (EGKK) | 2026-07-23 12:10 UTC | 2026-07-23 14:55 UTC | 2h 45m |
| MILAN76 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-07-23 13:13 UTC | 2026-07-23 14:53 UTC | 1h 39m |
| MSTG87 | MST | Southport Airport (CYPG) | Pilot Butte Airport (CPB5) | 2026-07-23 13:27 UTC | 2026-07-23 14:52 UTC | 1h 25m |
| WVE820 | WVE | Luqa Airport (LMML) | Mitiga Airport (HLLM) | 2026-07-23 14:07 UTC | 2026-07-23 14:52 UTC | 44m |
| N132TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-23 14:35 UTC | 2026-07-23 14:50 UTC | 15m |
| HB2233 |  | Samedan Airport (LSZS) | Muenster Aero Airport (LSPU) | 2026-07-23 12:49 UTC | 2026-07-23 14:47 UTC | 1h 58m |
| N405SP |  | Clermont County Airport (KI69) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-23 14:16 UTC | 2026-07-23 14:47 UTC | 31m |
| SWR4KW | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-07-23 13:46 UTC | 2026-07-23 14:42 UTC | 55m |
| N284BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-07-23 14:41 UTC | 2026-07-23 14:41 UTC | 0m |
| HB3291 |  | Samedan Airport (LSZS) | Muenster Aero Airport (LSPU) | 2026-07-23 12:56 UTC | 2026-07-23 14:40 UTC | 1h 44m |
| ERU64 | ERU | Robin Airport (59AZ) | AZ86 (AZ86) | 2026-07-23 14:37 UTC | 2026-07-23 14:40 UTC | 3m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-07-23 14:16 UTC | 2026-07-23 14:36 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
