# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_15:48:34_UTC-green)

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

**Latest saved flight:** 2026-08-11 15:48:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 15:48:34 UTC

- **187,077** saved flights
- **59,316** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,077** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,244,353.1 tonnes** estimated CO2 emissions
- **130,107,425 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7433 |
| 2 | SkyWest Airlines | 6788 |
| 3 | EJA | 3681 |
| 4 | IndiGo | 3269 |
| 5 | Southwest Airlines | 2929 |
| 6 | American Airlines | 2907 |
| 7 | ENY | 2324 |
| 8 | Delta Air Lines | 2203 |
| 9 | LATAM Airlines | 1753 |
| 10 | AZU | 1682 |
| 11 | Lufthansa | 1642 |
| 12 | WIF | 1550 |
| 13 | Vueling | 1546 |
| 14 | LXJ | 1463 |
| 15 | easyJet | 1286 |
| 16 | Swiss International | 1279 |
| 17 | AXM | 1247 |
| 18 | EJU | 1155 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1029 |
| 23 | GLO | 1002 |
| 24 | Air France | 971 |
| 25 | AEE | 967 |
| 26 | CXK | 961 |
| 27 | PGT | 960 |
| 28 | United Airlines | 953 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 930 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159493 |
| 2 | 🇪🇸 ES | 12048 |
| 3 | 🇧🇷 BR | 10739 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10243 |
| 6 | 🇨🇦 CA | 10210 |
| 7 | 🇮🇹 IT | 9697 |
| 8 | 🇩🇪 DE | 9273 |
| 9 | 🇬🇧 GB | 8706 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7490 |
| 12 | 🇨🇴 CO | 7070 |
| 13 | 🇬🇷 GR | 5491 |
| 14 | 🇲🇽 MX | 5327 |
| 15 | 🇨🇭 CH | 5021 |
| 16 | 🇹🇷 TR | 4936 |
| 17 | 🇳🇴 NO | 4817 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3148 |
| 20 | 🇵🇱 PL | 3106 |
| 21 | 🇹🇭 TH | 2892 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2381 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1904 |
| 27 | 🇭🇷 HR | 1897 |
| 28 | 🇲🇪 ME | 1678 |
| 29 | 🇳🇱 NL | 1674 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3875 |
| 2 | Denver International Airport |  | US | 3072 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2304 |
| 5 | Guaymaral Airport |  | CO | 2288 |
| 6 | Harry Reid International Airport |  | US | 2188 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1994 |
| 8 | Zurich Airport |  | CH | 1994 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1938 |
| 10 | La Aurora Airport |  | GT | 1828 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1697 |
| 12 | El Dorado International Airport |  | CO | 1680 |
| 13 | Salt Lake City International Airport |  | US | 1663 |
| 14 | Chicago O'Hare International Airport |  | US | 1654 |
| 15 | Frankfurt am Main International Airport |  | DE | 1611 |
| 16 | Congonhas Airport |  | BR | 1562 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1476 |
| 19 | Capua Airport |  | IT | 1460 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1456 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1392 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1341 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1290 |
| 25 | Charles de Gaulle International Airport |  | FR | 1277 |
| 26 | Charlotte/Douglas International Airport |  | US | 1258 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1209 |
| 29 | Ninoy Aquino International Airport |  | PH | 1169 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1168 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1145 |
| 32 | Barcelona International Airport |  | ES | 1114 |
| 33 | Viracopos International Airport |  | BR | 1077 |
| 34 | Seattle-Tacoma International Airport |  | US | 1074 |
| 35 | Reno/Tahoe International Airport |  | US | 1073 |
| 36 | Calgary International Airport |  | CA | 1061 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1047 |
| 39 | Tenerife Norte Airport |  | ES | 1024 |
| 40 | Vitoria/Foronda Airport |  | ES | 1015 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 943 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 435 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 329 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 315 | 27m | 275 km | 1,492.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 303 | 14m | 114 km | 594.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 281 | 44m | 241 km | 1,167.2 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 271 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 233 | 27m | 215 km | 862.9 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 224 | 1h 38m | 1,156 km | 4,468.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 220 | 24m | 218 km | 828.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GAGE44 | GAG | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-08-11 15:04 UTC | 2026-08-11 15:48 UTC | 44m |
| N9643Q |  | Bend Municipal Airport (KBDN) | Bend Municipal Airport (KBDN) | 2026-08-11 14:54 UTC | 2026-08-11 15:46 UTC | 51m |
| DMFSS | DMF | Ampfing-Waldkraiburg Airport (EDNA) | Ampfing-Waldkraiburg Airport (EDNA) | 2026-08-11 15:04 UTC | 2026-08-11 15:42 UTC | 37m |
| AAL2425 | American Airlines | Big Bear City Airport (KL35) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-11 13:13 UTC | 2026-08-11 15:42 UTC | 2h 29m |
| N275CV |  | Jacksonville Executive At Craig Airport (KCRG) | Palatka Municipal/Lt Kay Larkin Field (K28J) | 2026-08-11 14:46 UTC | 2026-08-11 15:38 UTC | 51m |
| N1227T |  | Rush City Regional Airport (KROS) | Rush City Regional Airport (KROS) | 2026-08-11 15:09 UTC | 2026-08-11 15:33 UTC | 24m |
| N555UJ |  | K68J (K68J) | Thomasville Regional Airport (KTVI) | 2026-08-11 15:18 UTC | 2026-08-11 15:32 UTC | 13m |
| N955JA |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Hope Airport (KBUR) | 2026-08-11 14:19 UTC | 2026-08-11 15:30 UTC | 1h 11m |
| N138MH |  | Maryland Airport (K2W5) | St Mary's County Regional Airport (K2W6) | 2026-08-11 14:25 UTC | 2026-08-11 15:28 UTC | 1h 3m |
| N63ES |  | Chino Airport (KCNO) | Lakeside Airport (MT03) | 2026-08-11 13:19 UTC | 2026-08-11 15:27 UTC | 2h 7m |
| SRA511 | SRA | Madeira Airport (LPMA) | Madeira Airport (LPMA) | 2026-08-11 14:56 UTC | 2026-08-11 15:25 UTC | 29m |
| N3383T |  | Blue Ridge Skyport Airport (57GA) | Pratermill Flight Park Airport (GA72) | 2026-08-11 15:05 UTC | 2026-08-11 15:24 UTC | 19m |
| SHADY05 | SHA | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-11 15:09 UTC | 2026-08-11 15:24 UTC | 15m |
| D5864 |  | Albstadt-Degerfeld Airport (EDSA) | Grabenstetten Airport (EDSG) | 2026-08-11 13:38 UTC | 2026-08-11 15:24 UTC | 1h 46m |
| CARGO41 | CAR | Hidden Springs Airpark (36AL) | Dothan Regional Airport (KDHN) | 2026-08-11 14:58 UTC | 2026-08-11 15:24 UTC | 25m |
| R51267 |  | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-08-11 13:30 UTC | 2026-08-11 15:23 UTC | 1h 53m |
| CFWKQ | CFW | Thunder Bay Airport (CYQT) | Atikokan Municipal Airport (CYIB) | 2026-08-11 15:03 UTC | 2026-08-11 15:21 UTC | 18m |
| TUTOR895 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-11 14:46 UTC | 2026-08-11 15:18 UTC | 32m |
| BOMR832 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Corpus Christi Nas (Truax Field) Airport (KNGP) | 2026-08-11 14:52 UTC | 2026-08-11 15:18 UTC | 26m |
| N911XF |  | Baton Rouge Metro, Ryan Field (KBTR) | LA42 (LA42) | 2026-08-11 15:15 UTC | 2026-08-11 15:17 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
