# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_21:40:01_UTC-green)

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

**Latest saved flight:** 2026-08-05 21:40:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 21:40:01 UTC

- **173,245** saved flights
- **56,200** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,245** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,087,452.8 tonnes** estimated CO2 emissions
- **121,011,758 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6881 |
| 2 | SkyWest Airlines | 6348 |
| 3 | EJA | 3446 |
| 4 | IndiGo | 3031 |
| 5 | Southwest Airlines | 2734 |
| 6 | American Airlines | 2728 |
| 7 | ENY | 2157 |
| 8 | Delta Air Lines | 2055 |
| 9 | LATAM Airlines | 1600 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1529 |
| 12 | WIF | 1448 |
| 13 | Vueling | 1428 |
| 14 | LXJ | 1357 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1175 |
| 18 | EJU | 1057 |
| 19 | Alaska Airlines | 1055 |
| 20 | QLK | 1055 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 952 |
| 23 | Cathay Pacific | 936 |
| 24 | CXK | 924 |
| 25 | GLO | 910 |
| 26 | United Airlines | 904 |
| 27 | AEE | 902 |
| 28 | Air France | 888 |
| 29 | MXY | 878 |
| 30 | JetBlue | 866 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149391 |
| 2 | 🇪🇸 ES | 11087 |
| 3 | 🇧🇷 BR | 9857 |
| 4 | 🇦🇺 AU | 9647 |
| 5 | 🇮🇳 IN | 9507 |
| 6 | 🇨🇦 CA | 9490 |
| 7 | 🇮🇹 IT | 8945 |
| 8 | 🇩🇪 DE | 8583 |
| 9 | 🇬🇧 GB | 8023 |
| 10 | 🇯🇵 JP | 6937 |
| 11 | 🇫🇷 FR | 6862 |
| 12 | 🇨🇴 CO | 6382 |
| 13 | 🇬🇷 GR | 5029 |
| 14 | 🇲🇽 MX | 4959 |
| 15 | 🇨🇭 CH | 4563 |
| 16 | 🇳🇴 NO | 4507 |
| 17 | 🇹🇷 TR | 4247 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2895 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2532 |
| 22 | 🇳🇿 NZ | 2500 |
| 23 | 🇵🇭 PH | 2280 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2170 |
| 26 | 🇲🇦 MA | 1740 |
| 27 | 🇭🇷 HR | 1673 |
| 28 | 🇲🇪 ME | 1586 |
| 29 | 🇳🇱 NL | 1564 |
| 30 | 🇲🇴 MO | 1496 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3578 |
| 2 | Denver International Airport |  | US | 2874 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2118 |
| 6 | Harry Reid International Airport |  | US | 2074 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1882 |
| 8 | Zurich Airport |  | CH | 1831 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1821 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1599 |
| 12 | El Dorado International Airport |  | CO | 1574 |
| 13 | Chicago O'Hare International Airport |  | US | 1569 |
| 14 | Salt Lake City International Airport |  | US | 1556 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1496 |
| 17 | Congonhas Airport |  | BR | 1424 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1417 |
| 19 | Capua Airport |  | IT | 1351 |
| 20 | Madrid Barajas International Airport |  | ES | 1349 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1301 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1217 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1204 |
| 24 | Charlotte/Douglas International Airport |  | US | 1198 |
| 25 | Charles de Gaulle International Airport |  | FR | 1174 |
| 26 | Malpensa International Airport |  | IT | 1173 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1076 |
| 30 | Ninoy Aquino International Airport |  | PH | 1074 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1068 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Daniel K Inouye International Airport |  | US | 1000 |
| 34 | Seattle-Tacoma International Airport |  | US | 1000 |
| 35 | Viracopos International Airport |  | BR | 984 |
| 36 | Reno/Tahoe International Airport |  | US | 983 |
| 37 | Calgary International Airport |  | CA | 983 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 944 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 632 | 21m | 244 km | 2,661.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 260 | 22m | 55 km | 247.1 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 200 | 1h 38m | 1,156 km | 3,989.9 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 198 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N26WR |  | Salinas Municipal Airport (KSNS) | Santa Monica Municipal Airport (KSMO) | 2026-08-05 20:37 UTC | 2026-08-05 21:40 UTC | 1h 2m |
| N59FG |  | French Valley Airport (KF70) | Gray Butte Field (04CA) | 2026-08-05 21:08 UTC | 2026-08-05 21:37 UTC | 28m |
| N187SD |  | W H 'Bud' Barron Airport (KDBN) | W H 'Bud' Barron Airport (KDBN) | 2026-08-05 21:17 UTC | 2026-08-05 21:36 UTC | 19m |
| N21866 |  | Oakland San Francisco Bay Airport (KOAK) | Livermore Municipal Airport (KLVK) | 2026-08-05 21:15 UTC | 2026-08-05 21:29 UTC | 13m |
| N222ND |  | Laurence G Hanscom Field (KBED) | Laurence G Hanscom Field (KBED) | 2026-08-05 21:22 UTC | 2026-08-05 21:29 UTC | 6m |
| N545AM |  | Grimes Field (KI74) | Ohio Air Spray Airport (1OH1) | 2026-08-05 21:04 UTC | 2026-08-05 21:25 UTC | 21m |
| N39JK |  | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-08-05 19:56 UTC | 2026-08-05 21:22 UTC | 1h 25m |
| TKR136 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-05 21:11 UTC | 2026-08-05 21:20 UTC | 9m |
| N409KC |  | Meadows Field (KBFL) | Zamora Airport (97CA) | 2026-08-05 19:47 UTC | 2026-08-05 21:19 UTC | 1h 31m |
| TKR160 | TKR | Coeur D'Alene Airport (KCOE) | 0ID5 (0ID5) | 2026-08-05 20:22 UTC | 2026-08-05 21:15 UTC | 53m |
| N1242N |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-05 20:44 UTC | 2026-08-05 21:13 UTC | 29m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-08-05 17:38 UTC | 2026-08-05 21:12 UTC | 3h 34m |
| N818HF |  | San Antonio International Airport (KSAT) | Addison Airport (KADS) | 2026-08-05 20:29 UTC | 2026-08-05 21:11 UTC | 42m |
| N7274L |  | Cleveland Regional Jetport Airport (KRZR) | St Pete-Clearwater International Airport (KPIE) | 2026-08-05 19:11 UTC | 2026-08-05 21:11 UTC | 2h 0m |
| TEXGLD | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-08-05 20:52 UTC | 2026-08-05 21:09 UTC | 16m |
| N153PM |  | Ryan Aerodrome (7TX7) | 5TA6 (5TA6) | 2026-08-05 20:48 UTC | 2026-08-05 21:07 UTC | 18m |
| XSR331 | XSR | Kansas City Downtown/Wheeler Field (KMKC) | Telluride Regional Airport (KTEX) | 2026-08-05 19:07 UTC | 2026-08-05 21:03 UTC | 1h 55m |
| N9685G |  | Waukesha County Airport (KUES) | Watertown Municipal Airport (KRYV) | 2026-08-05 19:41 UTC | 2026-08-05 21:03 UTC | 1h 21m |
| PRPEN | PRP | Lajinha Airport (SNLH) | Eurico de Aguiar Salles Airport (SBVT) | 2026-08-05 20:43 UTC | 2026-08-05 21:02 UTC | 18m |
| N956HC |  | Joe Foss Field (KFSD) | Walden-Jackson County Airport (K33V) | 2026-08-05 19:37 UTC | 2026-08-05 20:59 UTC | 1h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
