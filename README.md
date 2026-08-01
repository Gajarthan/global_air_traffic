# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_23:48:20_UTC-green)

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

**Latest saved flight:** 2026-07-31 23:48:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 23:48:20 UTC

- **163,731** saved flights
- **53,915** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,731** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,965,312.8 tonnes** estimated CO2 emissions
- **113,931,175 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6537 |
| 2 | SkyWest Airlines | 5981 |
| 3 | EJA | 3254 |
| 4 | IndiGo | 2861 |
| 5 | American Airlines | 2589 |
| 6 | Southwest Airlines | 2570 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1956 |
| 9 | LATAM Airlines | 1532 |
| 10 | Lufthansa | 1530 |
| 11 | AZU | 1437 |
| 12 | WIF | 1378 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1132 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1072 |
| 18 | Alaska Airlines | 1014 |
| 19 | QLK | 1004 |
| 20 | EJU | 1002 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 902 |
| 23 | CXK | 878 |
| 24 | Cathay Pacific | 868 |
| 25 | United Airlines | 863 |
| 26 | GLO | 857 |
| 27 | AEE | 853 |
| 28 | MXY | 846 |
| 29 | Air France | 844 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141667 |
| 2 | 🇪🇸 ES | 10474 |
| 3 | 🇧🇷 BR | 9345 |
| 4 | 🇦🇺 AU | 9212 |
| 5 | 🇮🇳 IN | 8993 |
| 6 | 🇨🇦 CA | 8926 |
| 7 | 🇮🇹 IT | 8428 |
| 8 | 🇩🇪 DE | 8209 |
| 9 | 🇬🇧 GB | 7513 |
| 10 | 🇯🇵 JP | 6595 |
| 11 | 🇫🇷 FR | 6464 |
| 12 | 🇨🇴 CO | 5861 |
| 13 | 🇲🇽 MX | 4695 |
| 14 | 🇬🇷 GR | 4691 |
| 15 | 🇳🇴 NO | 4308 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3909 |
| 18 | 🇲🇾 MY | 2940 |
| 19 | 🇵🇱 PL | 2773 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2391 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2138 |
| 24 | 🇰🇷 KR | 2120 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1651 |
| 27 | 🇲🇪 ME | 1537 |
| 28 | 🇭🇷 HR | 1537 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1379 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3350 |
| 2 | Denver International Airport |  | US | 2729 |
| 3 | Tokyo International Airport |  | JP | 2078 |
| 4 | Guaymaral Airport |  | CO | 2061 |
| 5 | Indira Gandhi International Airport |  | IN | 1998 |
| 6 | Harry Reid International Airport |  | US | 1985 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1797 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1522 |
| 12 | El Dorado International Airport |  | CO | 1502 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1474 |
| 16 | Macau International Airport |  | MO | 1379 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1377 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1293 |
| 20 | Capua Airport |  | IT | 1281 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1251 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1159 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1158 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1115 |
| 27 | Malpensa International Airport |  | IT | 1082 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 30 | Ninoy Aquino International Airport |  | PH | 1004 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1003 |
| 32 | Barcelona International Airport |  | ES | 967 |
| 33 | Daniel K Inouye International Airport |  | US | 958 |
| 34 | Seattle-Tacoma International Airport |  | US | 950 |
| 35 | Calgary International Airport |  | CA | 935 |
| 36 | Viracopos International Airport |  | BR | 929 |
| 37 | Scottsdale Airport |  | US | 917 |
| 38 | Tenerife Norte Airport |  | ES | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 901 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 596 | 21m | 244 km | 2,509.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 389 | 24m | 225 km | 1,509.1 t |
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
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 201 | 31m | 49 km | 169.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZJI | ZJI | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-07-31 23:20 UTC | 2026-07-31 23:48 UTC | 27m |
| TRP2 | TRP | Joint Base Andrews Airport (KADW) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-31 23:15 UTC | 2026-07-31 23:45 UTC | 29m |
| N403JS |  | Kaunas International Airport (EYKA) | Luqa Airport (LMML) | 2026-07-31 20:44 UTC | 2026-07-31 23:45 UTC | 3h 0m |
| CFUDF | CFU | Beiseker Airport (CFV2) | Beiseker Airport (CFV2) | 2026-07-31 22:41 UTC | 2026-07-31 23:39 UTC | 58m |
| N536SH |  | Coal Field (64KY) | Coal Field (64KY) | 2026-07-31 19:41 UTC | 2026-07-31 23:23 UTC | 3h 42m |
| TKR41 | TKR | CD82 (CD82) | Animas Air Park (K00C) | 2026-07-31 22:57 UTC | 2026-07-31 23:22 UTC | 25m |
| N626GM |  | Napa County Airport (KAPC) | Napa County Airport (KAPC) | 2026-07-31 23:01 UTC | 2026-07-31 23:21 UTC | 19m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-07-31 22:53 UTC | 2026-07-31 23:19 UTC | 26m |
| SCU34 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-07-31 23:17 UTC | 2026-07-31 23:19 UTC | 1m |
| N79333 |  | Tracy Municipal Airport (KTCY) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-31 23:00 UTC | 2026-07-31 23:18 UTC | 17m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-31 22:04 UTC | 2026-07-31 23:16 UTC | 1h 12m |
| N972CC |  | Wadsworth Municipal Airport (K3G3) | Lockeridge Airport (OI58) | 2026-07-31 23:01 UTC | 2026-07-31 23:12 UTC | 10m |
| PDT5814 | PDT | Charlotte/Douglas International Airport (KCLT) | Logan County Airport (K6L4) | 2026-07-31 22:35 UTC | 2026-07-31 23:07 UTC | 32m |
| ZMV | ZMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-07-31 22:49 UTC | 2026-07-31 23:03 UTC | 14m |
| TAM3964 | LATAM Airlines | Congonhas Airport (SBSP) | Catanduva Airport (SDCD) | 2026-07-31 22:25 UTC | 2026-07-31 23:01 UTC | 35m |
| RYR4QJ | Ryanair | Paris Beauvais Tille Airport (LFOB) | Malpensa International Airport (LIMC) | 2026-07-31 21:57 UTC | 2026-07-31 23:00 UTC | 1h 2m |
| N400AL |  | Buckhorn Airport (7MO5) | Mc Elroy Airfield (K20V) | 2026-07-31 21:22 UTC | 2026-07-31 22:59 UTC | 1h 36m |
| UAL2171 | United Airlines | Chicago O'Hare International Airport (KORD) | Newark Liberty International Airport (KEWR) | 2026-07-31 21:23 UTC | 2026-07-31 22:58 UTC | 1h 35m |
| EZY32FP | easyJet | Glasgow International Airport (EGPF) | Birmingham International Airport (EGBB) | 2026-07-31 22:09 UTC | 2026-07-31 22:57 UTC | 47m |
| AXM6413 | AXM | Penang International Airport (WMKP) | Batu Pahat Airport (WMAB) | 2026-07-31 22:19 UTC | 2026-07-31 22:57 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
