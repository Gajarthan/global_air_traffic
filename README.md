# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_20:37:36_UTC-green)

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

**Latest saved flight:** 2026-07-31 20:37:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 20:37:36 UTC

- **163,316** saved flights
- **53,799** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,316** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,958,952.9 tonnes** estimated CO2 emissions
- **113,562,488 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6520 |
| 2 | SkyWest Airlines | 5956 |
| 3 | EJA | 3243 |
| 4 | IndiGo | 2860 |
| 5 | American Airlines | 2575 |
| 6 | Southwest Airlines | 2555 |
| 7 | ENY | 2030 |
| 8 | Delta Air Lines | 1945 |
| 9 | Lufthansa | 1530 |
| 10 | LATAM Airlines | 1529 |
| 11 | AZU | 1432 |
| 12 | WIF | 1377 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1270 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1071 |
| 18 | Alaska Airlines | 1011 |
| 19 | QLK | 1003 |
| 20 | EJU | 1001 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 900 |
| 23 | CXK | 878 |
| 24 | United Airlines | 860 |
| 25 | Cathay Pacific | 859 |
| 26 | GLO | 854 |
| 27 | AEE | 852 |
| 28 | Air France | 844 |
| 29 | MXY | 843 |
| 30 | JetBlue | 831 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141135 |
| 2 | 🇪🇸 ES | 10461 |
| 3 | 🇧🇷 BR | 9322 |
| 4 | 🇦🇺 AU | 9202 |
| 5 | 🇮🇳 IN | 8988 |
| 6 | 🇨🇦 CA | 8893 |
| 7 | 🇮🇹 IT | 8404 |
| 8 | 🇩🇪 DE | 8207 |
| 9 | 🇬🇧 GB | 7506 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6461 |
| 12 | 🇨🇴 CO | 5841 |
| 13 | 🇲🇽 MX | 4686 |
| 14 | 🇬🇷 GR | 4683 |
| 15 | 🇳🇴 NO | 4304 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3905 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2772 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2385 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2113 |
| 26 | 🇲🇦 MA | 1648 |
| 27 | 🇲🇪 ME | 1535 |
| 28 | 🇭🇷 HR | 1533 |
| 29 | 🇳🇱 NL | 1486 |
| 30 | 🇲🇴 MO | 1367 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3333 |
| 2 | Denver International Airport |  | US | 2717 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2060 |
| 5 | Indira Gandhi International Airport |  | IN | 1997 |
| 6 | Harry Reid International Airport |  | US | 1977 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1795 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1718 |
| 10 | La Aurora Airport |  | GT | 1637 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1518 |
| 12 | El Dorado International Airport |  | CO | 1495 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1478 |
| 15 | Salt Lake City International Airport |  | US | 1470 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1368 |
| 17 | Macau International Airport |  | MO | 1367 |
| 18 | Congonhas Airport |  | BR | 1350 |
| 19 | Madrid Barajas International Airport |  | ES | 1289 |
| 20 | Capua Airport |  | IT | 1280 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1247 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1156 |
| 24 | Charlotte/Douglas International Airport |  | US | 1145 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1114 |
| 27 | Malpensa International Airport |  | IT | 1077 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1001 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 994 |
| 32 | Barcelona International Airport |  | ES | 965 |
| 33 | Daniel K Inouye International Airport |  | US | 957 |
| 34 | Seattle-Tacoma International Airport |  | US | 944 |
| 35 | Calgary International Airport |  | CA | 931 |
| 36 | Viracopos International Airport |  | BR | 927 |
| 37 | Tenerife Norte Airport |  | ES | 913 |
| 38 | Scottsdale Airport |  | US | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 896 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 595 | 21m | 244 km | 2,505.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 243 | 22m | 55 km | 231.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 208 | 20m | 99 km | 356.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 200 | 30m | 49 km | 169.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 194 | 1h 15m | 961 km | 3,215.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 175 | 1h 49m | 1,304 km | 3,937.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3772M |  | Ionia County Airport (KY70) | Minikey Airport (MI13) | 2026-07-31 19:58 UTC | 2026-07-31 20:37 UTC | 38m |
| AAL1564 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 15:59 UTC | 2026-07-31 20:28 UTC | 4h 29m |
| N334AM |  | Yosemite Hidden Lake Ranch Airport (0CL0) | Truckee-Tahoe Airport (KTRK) | 2026-07-31 19:54 UTC | 2026-07-31 20:26 UTC | 31m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-31 20:07 UTC | 2026-07-31 20:25 UTC | 17m |
| N565HT |  | Newport State Airport (KUUU) | Laguardia Airport (KLGA) | 2026-07-31 19:28 UTC | 2026-07-31 20:24 UTC | 55m |
| N278DS |  | Gilbert Airport (73PA) | Lancaster Airport (KLNS) | 2026-07-31 19:46 UTC | 2026-07-31 20:14 UTC | 27m |
| N507RP |  | Jim Hamilton L B Owens Airport (KCUB) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-31 18:52 UTC | 2026-07-31 20:13 UTC | 1h 21m |
| N816RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-31 19:58 UTC | 2026-07-31 20:09 UTC | 10m |
| YS999P |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-07-31 19:41 UTC | 2026-07-31 20:07 UTC | 25m |
| N768SP |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-07-31 19:17 UTC | 2026-07-31 20:06 UTC | 49m |
| N17WG |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-31 19:40 UTC | 2026-07-31 20:05 UTC | 25m |
| CFCEI | CFC | Québec City Jean Lesage International Airport (CYQB) | Montmagny Airport (CSE5) | 2026-07-31 19:35 UTC | 2026-07-31 20:04 UTC | 29m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-07-31 09:02 UTC | 2026-07-31 20:04 UTC | 11h 1m |
|  |  | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | 2026-07-31 20:03 UTC | 2026-07-31 20:03 UTC | 0m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-07-31 06:00 UTC | 2026-07-31 20:03 UTC | 14h 2m |
| N316SA |  | Baton Rouge Metro, Ryan Field (KBTR) | AL54 (AL54) | 2026-07-31 19:10 UTC | 2026-07-31 20:02 UTC | 51m |
| RYR6TV | Ryanair | L'Aquila / Preturo Airport (LIAP) | Alghero / Fertilia Airport (LIEA) | 2026-07-31 19:13 UTC | 2026-07-31 20:00 UTC | 46m |
| CXK678 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-07-31 18:57 UTC | 2026-07-31 19:56 UTC | 58m |
| N636KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-31 19:07 UTC | 2026-07-31 19:56 UTC | 48m |
| PHX594 | PHX | Kitchener / Waterloo Airport (CYKF) | Englehart (Dave's Field) (CDF3) | 2026-07-31 18:48 UTC | 2026-07-31 19:55 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
