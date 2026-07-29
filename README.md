# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_23:00:52_UTC-green)

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

**Latest saved flight:** 2026-07-29 23:00:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 23:00:52 UTC

- **159,527** saved flights
- **52,811** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,527** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,914,493.2 tonnes** estimated CO2 emissions
- **110,985,116 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6402 |
| 2 | SkyWest Airlines | 5833 |
| 3 | EJA | 3173 |
| 4 | IndiGo | 2803 |
| 5 | American Airlines | 2528 |
| 6 | Southwest Airlines | 2505 |
| 7 | ENY | 1989 |
| 8 | Delta Air Lines | 1895 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1499 |
| 11 | AZU | 1409 |
| 12 | WIF | 1351 |
| 13 | Vueling | 1335 |
| 14 | LXJ | 1230 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1098 |
| 17 | easyJet | 1044 |
| 18 | Alaska Airlines | 999 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 976 |
| 22 | VIV | 875 |
| 23 | CXK | 847 |
| 24 | United Airlines | 844 |
| 25 | Cathay Pacific | 841 |
| 26 | GLO | 840 |
| 27 | AEE | 837 |
| 28 | MXY | 831 |
| 29 | Air France | 829 |
| 30 | JetBlue | 818 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 137793 |
| 2 | 🇪🇸 ES | 10241 |
| 3 | 🇧🇷 BR | 9138 |
| 4 | 🇦🇺 AU | 8967 |
| 5 | 🇮🇳 IN | 8818 |
| 6 | 🇨🇦 CA | 8668 |
| 7 | 🇮🇹 IT | 8243 |
| 8 | 🇩🇪 DE | 8068 |
| 9 | 🇬🇧 GB | 7312 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6303 |
| 12 | 🇨🇴 CO | 5632 |
| 13 | 🇲🇽 MX | 4584 |
| 14 | 🇬🇷 GR | 4571 |
| 15 | 🇳🇴 NO | 4223 |
| 16 | 🇨🇭 CH | 4169 |
| 17 | 🇹🇷 TR | 3802 |
| 18 | 🇲🇾 MY | 2894 |
| 19 | 🇵🇱 PL | 2710 |
| 20 | 🇿🇦 ZA | 2573 |
| 21 | 🇳🇿 NZ | 2351 |
| 22 | 🇹🇭 TH | 2276 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2095 |
| 25 | 🇬🇹 GT | 2038 |
| 26 | 🇲🇦 MA | 1620 |
| 27 | 🇲🇪 ME | 1524 |
| 28 | 🇭🇷 HR | 1480 |
| 29 | 🇳🇱 NL | 1458 |
| 30 | 🇲🇴 MO | 1322 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3264 |
| 2 | Denver International Airport |  | US | 2655 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1966 |
| 6 | Harry Reid International Airport |  | US | 1945 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1767 |
| 8 | Zurich Airport |  | CH | 1705 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1679 |
| 10 | La Aurora Airport |  | GT | 1581 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1488 |
| 12 | El Dorado International Airport |  | CO | 1464 |
| 13 | Frankfurt am Main International Airport |  | DE | 1464 |
| 14 | Chicago O'Hare International Airport |  | US | 1446 |
| 15 | Salt Lake City International Airport |  | US | 1435 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1333 |
| 17 | Congonhas Airport |  | BR | 1324 |
| 18 | Macau International Airport |  | MO | 1322 |
| 19 | Madrid Barajas International Airport |  | ES | 1264 |
| 20 | Capua Airport |  | IT | 1257 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1227 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1138 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1136 |
| 24 | Charlotte/Douglas International Airport |  | US | 1122 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Malpensa International Airport |  | IT | 1054 |
| 28 | Bengaluru International Airport |  | IN | 1050 |
| 29 | Ninoy Aquino International Airport |  | PH | 983 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 974 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 971 |
| 32 | Barcelona International Airport |  | ES | 952 |
| 33 | Daniel K Inouye International Airport |  | US | 940 |
| 34 | Seattle-Tacoma International Airport |  | US | 932 |
| 35 | Calgary International Airport |  | CA | 917 |
| 36 | Viracopos International Airport |  | BR | 915 |
| 37 | Scottsdale Airport |  | US | 903 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 876 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 579 | 21m | 244 km | 2,438.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 181 | 50m | 556 km | 1,735.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR15 | TKR | Othello Municipal Airport (KS70) | King's Airport (9OR4) | 2026-07-29 22:50 UTC | 2026-07-29 23:00 UTC | 10m |
| CAP4532 | CAP | Richmond Executive/Chesterfield County Airport (KFCI) | Tri Cities Executive/Dinwiddie County Airport (KPTB) | 2026-07-29 22:38 UTC | 2026-07-29 22:58 UTC | 19m |
| N462SP |  | KL38 (KL38) | KL38 (KL38) | 2026-07-29 22:35 UTC | 2026-07-29 22:51 UTC | 16m |
| N30381 |  | Joseph A Hardy Connellsville Airport (KVVS) | 2PN4 (2PN4) | 2026-07-29 22:23 UTC | 2026-07-29 22:49 UTC | 25m |
| N6379J |  | Grove City Airport (K29D) | Nelson's Run Airport (39PN) | 2026-07-29 22:29 UTC | 2026-07-29 22:48 UTC | 19m |
| TKJ3TQ | TKJ | Sivas Airport (LTAR) | Tbilisi International Airport (UGTB) | 2026-07-29 21:51 UTC | 2026-07-29 22:47 UTC | 56m |
| N677F |  | Rocky Mountain Metro Airport (KBJC) | Big Muddy Ranch Airport (2OR1) | 2026-07-29 19:59 UTC | 2026-07-29 22:43 UTC | 2h 43m |
| N137HS |  | IL31 (IL31) | IS43 (IS43) | 2026-07-29 22:07 UTC | 2026-07-29 22:41 UTC | 33m |
| CFCAU | CFC | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-07-29 22:22 UTC | 2026-07-29 22:40 UTC | 18m |
| N967BY |  | Miami-Opa Locka Executive Airport (KOPF) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-07-29 21:06 UTC | 2026-07-29 22:36 UTC | 1h 29m |
| DHXFI | DHX | Halle-Oppin Airport (EDAQ) | Halle-Oppin Airport (EDAQ) | 2026-07-29 21:05 UTC | 2026-07-29 22:36 UTC | 1h 30m |
| CXK654 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-07-29 21:11 UTC | 2026-07-29 22:36 UTC | 1h 24m |
| CHP24 | CHP | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-07-29 22:14 UTC | 2026-07-29 22:33 UTC | 19m |
| YTG | YTG | Toowoomba Wellcamp Airport (YBWW) | Pittsworth Airport (YPWH) | 2026-07-29 22:20 UTC | 2026-07-29 22:31 UTC | 11m |
| N324SC |  | KU77 (KU77) | Canyon Airport (ID04) | 2026-07-29 22:01 UTC | 2026-07-29 22:30 UTC | 28m |
| R21233 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-29 21:18 UTC | 2026-07-29 22:29 UTC | 1h 10m |
| N342ND |  | Sarasota/Bradenton International Airport (KSRQ) | Venice Municipal Airport (KVNC) | 2026-07-29 22:10 UTC | 2026-07-29 22:27 UTC | 16m |
| ORO1042 | ORO | Barcelona International Airport (LEBL) | Ibiza Airport (LEIB) | 2026-07-29 21:57 UTC | 2026-07-29 22:27 UTC | 30m |
| N65GH |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-07-29 21:19 UTC | 2026-07-29 22:23 UTC | 1h 4m |
| N30EA |  | Skydive Chicago Airport (K8N2) | Skydive Chicago Airport (K8N2) | 2026-07-29 22:04 UTC | 2026-07-29 22:21 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
