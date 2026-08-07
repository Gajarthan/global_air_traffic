# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_23:22:52_UTC-green)

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

**Latest saved flight:** 2026-08-07 23:22:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 23:22:52 UTC

- **177,032** saved flights
- **57,042** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,032** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,128,144.6 tonnes** estimated CO2 emissions
- **123,370,703 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7015 |
| 2 | SkyWest Airlines | 6484 |
| 3 | EJA | 3503 |
| 4 | IndiGo | 3094 |
| 5 | Southwest Airlines | 2793 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2210 |
| 8 | Delta Air Lines | 2094 |
| 9 | LATAM Airlines | 1641 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1580 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1394 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1200 |
| 17 | AXM | 1196 |
| 18 | EJU | 1082 |
| 19 | QLK | 1082 |
| 20 | Alaska Airlines | 1071 |
| 21 | All Nippon Airways | 1069 |
| 22 | VIV | 975 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 939 |
| 25 | GLO | 936 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 892 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152357 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10122 |
| 4 | 🇦🇺 AU | 9963 |
| 5 | 🇮🇳 IN | 9700 |
| 6 | 🇨🇦 CA | 9696 |
| 7 | 🇮🇹 IT | 9143 |
| 8 | 🇩🇪 DE | 8740 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7079 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6516 |
| 13 | 🇬🇷 GR | 5150 |
| 14 | 🇲🇽 MX | 5069 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4392 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2938 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2624 |
| 22 | 🇳🇿 NZ | 2563 |
| 23 | 🇵🇭 PH | 2334 |
| 24 | 🇬🇹 GT | 2264 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1741 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3669 |
| 2 | Denver International Airport |  | US | 2941 |
| 3 | Tokyo International Airport |  | JP | 2210 |
| 4 | Guaymaral Airport |  | CO | 2176 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2108 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1914 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1852 |
| 10 | La Aurora Airport |  | GT | 1742 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1626 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1583 |
| 14 | El Dorado International Airport |  | CO | 1582 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1470 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1426 |
| 19 | Capua Airport |  | IT | 1383 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1321 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1248 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1236 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1098 |
| 30 | Ninoy Aquino International Airport |  | PH | 1098 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1094 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1021 |
| 34 | Daniel K Inouye International Airport |  | US | 1016 |
| 35 | Viracopos International Airport |  | BR | 1015 |
| 36 | Reno/Tahoe International Airport |  | US | 1010 |
| 37 | Calgary International Airport |  | CA | 1008 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 646 | 21m | 244 km | 2,720.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 415 | 24m | 225 km | 1,610.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 407 | 1h 8m | 770 km | 5,406.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 222 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 193 | 1h 2m | 695 km | 2,313.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N316EP |  | Long Beach (Daugherty Field) Airport (KLGB) | Camarillo Airport (KCMA) | 2026-08-07 22:34 UTC | 2026-08-07 23:22 UTC | 48m |
| N1314T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-07 20:28 UTC | 2026-08-07 23:21 UTC | 2h 52m |
| N916HT |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-07 22:36 UTC | 2026-08-07 23:14 UTC | 38m |
| ADY424 | ADY | Abu Dhabi International Airport (OMAA) | Hulwan (HE15) | 2026-08-07 20:17 UTC | 2026-08-07 23:11 UTC | 2h 54m |
| N215BN |  | Bellefontaine Regional Airport (KEDJ) | Bellefontaine Regional Airport (KEDJ) | 2026-08-07 22:35 UTC | 2026-08-07 23:11 UTC | 36m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-07 22:20 UTC | 2026-08-07 23:10 UTC | 49m |
| N451LF |  | Piper Canyon Airport (9WA4) | 07OR (07OR) | 2026-08-07 22:15 UTC | 2026-08-07 22:59 UTC | 43m |
| CARBN21 | CAR | Spring Ranch Airport (3TA6) | Real County Airport (K49R) | 2026-08-07 22:38 UTC | 2026-08-07 22:55 UTC | 16m |
| AAL1163 | American Airlines | San Francisco International Airport (KSFO) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-07 19:58 UTC | 2026-08-07 22:53 UTC | 2h 54m |
| TKR137 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-07 22:45 UTC | 2026-08-07 22:52 UTC | 7m |
| ZSO | ZSO | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-08-07 22:15 UTC | 2026-08-07 22:52 UTC | 37m |
| N7425G |  | Fullerton Municipal Airport (KFUL) | Santa Monica Municipal Airport (KSMO) | 2026-08-07 22:29 UTC | 2026-08-07 22:52 UTC | 22m |
| N299RB |  | Robert S Kerr Airport (KRKR) | Danville Municipal Airport (K32A) | 2026-08-07 22:31 UTC | 2026-08-07 22:51 UTC | 20m |
| TKR102 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-07 22:40 UTC | 2026-08-07 22:48 UTC | 8m |
| BNOB | BNO | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-08-07 22:14 UTC | 2026-08-07 22:47 UTC | 33m |
| N912BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-08-07 22:45 UTC | 2026-08-07 22:45 UTC | 0m |
| N190SW |  | Houma-Terrebonne Airport (KHUM) | Gulf Shores International/Jack Edwards Field (KJKA) | 2026-08-07 22:14 UTC | 2026-08-07 22:44 UTC | 30m |
| N851MB |  | Lemons Private Strip (CO10) | Greeley-Weld County Airport (KGXY) | 2026-08-07 22:05 UTC | 2026-08-07 22:40 UTC | 35m |
| LXJ325 | LXJ | Heiner Airport (WY60) | Aztec Municipal Airport (KN19) | 2026-08-07 21:53 UTC | 2026-08-07 22:40 UTC | 47m |
| WCC33 | WCC | John Wayne/Orange County Airport (KSNA) | Bishop Airport (KBIH) | 2026-08-07 21:43 UTC | 2026-08-07 22:39 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
