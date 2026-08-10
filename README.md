# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_13:49:50_UTC-green)

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

**Latest saved flight:** 2026-08-10 13:49:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 13:49:50 UTC

- **184,000** saved flights
- **58,598** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,000** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,211,529.5 tonnes** estimated CO2 emissions
- **128,204,607 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7300 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3630 |
| 4 | IndiGo | 3226 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2869 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1721 |
| 10 | AZU | 1651 |
| 11 | Lufthansa | 1625 |
| 12 | WIF | 1524 |
| 13 | Vueling | 1519 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1263 |
| 16 | Swiss International | 1263 |
| 17 | AXM | 1235 |
| 18 | QLK | 1135 |
| 19 | EJU | 1131 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1013 |
| 23 | GLO | 985 |
| 24 | AEE | 957 |
| 25 | CXK | 954 |
| 26 | Air France | 953 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 941 |
| 29 | PGT | 938 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157109 |
| 2 | 🇪🇸 ES | 11830 |
| 3 | 🇧🇷 BR | 10559 |
| 4 | 🇦🇺 AU | 10304 |
| 5 | 🇮🇳 IN | 10111 |
| 6 | 🇨🇦 CA | 10002 |
| 7 | 🇮🇹 IT | 9512 |
| 8 | 🇩🇪 DE | 9113 |
| 9 | 🇬🇧 GB | 8539 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7352 |
| 12 | 🇨🇴 CO | 6878 |
| 13 | 🇬🇷 GR | 5397 |
| 14 | 🇲🇽 MX | 5249 |
| 15 | 🇨🇭 CH | 4928 |
| 16 | 🇹🇷 TR | 4805 |
| 17 | 🇳🇴 NO | 4738 |
| 18 | 🇲🇾 MY | 3219 |
| 19 | 🇿🇦 ZA | 3080 |
| 20 | 🇵🇱 PL | 3079 |
| 21 | 🇹🇭 TH | 2856 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2435 |
| 24 | 🇬🇹 GT | 2356 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1858 |
| 27 | 🇭🇷 HR | 1846 |
| 28 | 🇲🇪 ME | 1663 |
| 29 | 🇳🇱 NL | 1650 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2266 |
| 5 | Guaymaral Airport |  | CO | 2239 |
| 6 | Harry Reid International Airport |  | US | 2153 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1974 |
| 8 | Zurich Airport |  | CH | 1972 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1807 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1647 |
| 13 | Salt Lake City International Airport |  | US | 1639 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1589 |
| 16 | Congonhas Airport |  | BR | 1531 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 19 | Madrid Barajas International Airport |  | ES | 1447 |
| 20 | Capua Airport |  | IT | 1439 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1317 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1273 |
| 25 | Charles de Gaulle International Airport |  | FR | 1254 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1197 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1149 |
| 30 | Ninoy Aquino International Airport |  | PH | 1148 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1089 |
| 33 | Viracopos International Airport |  | BR | 1059 |
| 34 | Seattle-Tacoma International Airport |  | US | 1057 |
| 35 | Reno/Tahoe International Airport |  | US | 1050 |
| 36 | Daniel K Inouye International Airport |  | US | 1047 |
| 37 | Calgary International Airport |  | CA | 1047 |
| 38 | Oslo Gardermoen Airport |  | NO | 1023 |
| 39 | Tenerife Norte Airport |  | ES | 1004 |
| 40 | Vitoria/Foronda Airport |  | ES | 996 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 923 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 675 | 21m | 244 km | 2,842.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 309 | 27m | 275 km | 1,464.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 273 | 44m | 241 km | 1,134.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 256 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 227 | 19m | 99 km | 388.8 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 221 | 19m | 144 km | 549.7 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 218 | 1h 38m | 1,156 km | 4,349.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 217 | 24m | 218 km | 817.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 214 | 31m | 369 km | 1,362.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASI96 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-10 13:30 UTC | 2026-08-10 13:49 UTC | 19m |
| N560RW |  | Wings Field (KLOM) | KNHZ (KNHZ) | 2026-08-10 12:52 UTC | 2026-08-10 13:48 UTC | 56m |
| N798JS |  | Provo Municipal Airport (KPVU) | Logan-Cache Airport (KLGU) | 2026-08-10 13:18 UTC | 2026-08-10 13:40 UTC | 22m |
| NH32 |  | 1VA9 (1VA9) | 1VA9 (1VA9) | 2026-08-10 13:08 UTC | 2026-08-10 13:38 UTC | 30m |
| GHOST11 | GHO | OL09 (OL09) | Ksa Orchards Airport (OK11) | 2026-08-10 13:12 UTC | 2026-08-10 13:36 UTC | 24m |
| N22467 |  | Gastonia Municipal Airport (KAKH) | Gastonia Municipal Airport (KAKH) | 2026-08-10 12:52 UTC | 2026-08-10 13:36 UTC | 43m |
| HBKZG | HBK | Les Eplatures Airport (LSGC) | Bern Belp Airport (LSZB) | 2026-08-10 13:15 UTC | 2026-08-10 13:36 UTC | 21m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Pompano Beach Airpark (KPMP) | 2026-08-10 12:41 UTC | 2026-08-10 13:33 UTC | 52m |
| PA |  | Ptuj Airport (LJPT) | Ptuj Airport (LJPT) | 2026-08-10 13:16 UTC | 2026-08-10 13:32 UTC | 16m |
| N41VU |  | Barrow County Airport (KWDR) | Southern Oaks Airport (GE35) | 2026-08-10 12:58 UTC | 2026-08-10 13:27 UTC | 29m |
| N199RN |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-08-10 13:24 UTC | 2026-08-10 13:27 UTC | 2m |
| JEDDA02 | JED | Lewis Private Airport (4TE2) | J R Ranch Airport (15TA) | 2026-08-10 13:13 UTC | 2026-08-10 13:26 UTC | 12m |
| VWA108 | VWA | Falcon Field (KFFZ) | Ak-Chin Regional Airport (KA39) | 2026-08-10 12:43 UTC | 2026-08-10 13:22 UTC | 38m |
| RTY592 | RTY | Northern Colorado Regional Airport (KFNL) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-10 12:43 UTC | 2026-08-10 13:21 UTC | 38m |
| N20AW |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-10 12:44 UTC | 2026-08-10 13:18 UTC | 33m |
| D6666 |  | Laucha Airport (EDBL) | Laucha Airport (EDBL) | 2026-08-10 12:56 UTC | 2026-08-10 13:17 UTC | 20m |
| AWH57T | AWH | Palma De Mallorca Airport (LEPA) | Hamburg Airport (EDDH) | 2026-08-10 10:52 UTC | 2026-08-10 13:14 UTC | 2h 22m |
| N426CA |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-10 12:31 UTC | 2026-08-10 13:14 UTC | 43m |
| N346BA |  | Flying Cloud Airport (KFCM) | Minnesuing Airport (WI31) | 2026-08-10 12:41 UTC | 2026-08-10 13:13 UTC | 32m |
| T342 |  | Dubendorf Airport (LSMD) | Meiringen Airport (LSMM) | 2026-08-10 11:32 UTC | 2026-08-10 13:11 UTC | 1h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
