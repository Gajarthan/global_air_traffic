# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_19:36:40_UTC-green)

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

**Latest saved flight:** 2026-07-31 19:36:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 19:36:40 UTC

- **163,129** saved flights
- **53,745** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,129** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,956,339.2 tonnes** estimated CO2 emissions
- **113,410,969 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6510 |
| 2 | SkyWest Airlines | 5944 |
| 3 | EJA | 3233 |
| 4 | IndiGo | 2859 |
| 5 | American Airlines | 2569 |
| 6 | Southwest Airlines | 2549 |
| 7 | ENY | 2026 |
| 8 | Delta Air Lines | 1942 |
| 9 | Lufthansa | 1530 |
| 10 | LATAM Airlines | 1529 |
| 11 | AZU | 1431 |
| 12 | WIF | 1376 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1268 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1071 |
| 18 | Alaska Airlines | 1010 |
| 19 | QLK | 1003 |
| 20 | EJU | 1001 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 900 |
| 23 | CXK | 875 |
| 24 | United Airlines | 859 |
| 25 | Cathay Pacific | 857 |
| 26 | GLO | 854 |
| 27 | AEE | 851 |
| 28 | Air France | 844 |
| 29 | MXY | 842 |
| 30 | JetBlue | 831 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140921 |
| 2 | 🇪🇸 ES | 10453 |
| 3 | 🇧🇷 BR | 9312 |
| 4 | 🇦🇺 AU | 9202 |
| 5 | 🇮🇳 IN | 8986 |
| 6 | 🇨🇦 CA | 8867 |
| 7 | 🇮🇹 IT | 8392 |
| 8 | 🇩🇪 DE | 8206 |
| 9 | 🇬🇧 GB | 7498 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6458 |
| 12 | 🇨🇴 CO | 5829 |
| 13 | 🇲🇽 MX | 4680 |
| 14 | 🇬🇷 GR | 4678 |
| 15 | 🇳🇴 NO | 4302 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3899 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2771 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2108 |
| 26 | 🇲🇦 MA | 1644 |
| 27 | 🇲🇪 ME | 1534 |
| 28 | 🇭🇷 HR | 1532 |
| 29 | 🇳🇱 NL | 1486 |
| 30 | 🇲🇴 MO | 1364 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3327 |
| 2 | Denver International Airport |  | US | 2708 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2056 |
| 5 | Indira Gandhi International Airport |  | IN | 1997 |
| 6 | Harry Reid International Airport |  | US | 1975 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1793 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1715 |
| 10 | La Aurora Airport |  | GT | 1634 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1515 |
| 12 | El Dorado International Airport |  | CO | 1490 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1475 |
| 15 | Salt Lake City International Airport |  | US | 1467 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1367 |
| 17 | Macau International Airport |  | MO | 1364 |
| 18 | Congonhas Airport |  | BR | 1350 |
| 19 | Madrid Barajas International Airport |  | ES | 1287 |
| 20 | Capua Airport |  | IT | 1279 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1245 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1156 |
| 24 | Charlotte/Douglas International Airport |  | US | 1143 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1113 |
| 27 | Malpensa International Airport |  | IT | 1075 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1001 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 991 |
| 32 | Barcelona International Airport |  | ES | 964 |
| 33 | Daniel K Inouye International Airport |  | US | 957 |
| 34 | Seattle-Tacoma International Airport |  | US | 943 |
| 35 | Calgary International Airport |  | CA | 929 |
| 36 | Viracopos International Airport |  | BR | 926 |
| 37 | Scottsdale Airport |  | US | 913 |
| 38 | Tenerife Norte Airport |  | ES | 912 |
| 39 | Oslo Gardermoen Airport |  | NO | 911 |
| 40 | Reno/Tahoe International Airport |  | US | 894 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 861 | 24m | - | - |
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
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 241 | 22m | 55 km | 229.1 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 237 | 44m | 241 km | 984.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 206 | 20m | 99 km | 352.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 199 | 31m | 49 km | 168.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 195 | 28m | 152 km | 509.6 t |
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
| WNG20B | WNG | Denton Enterprise Airport (KDTO) | Bass Aero Airport (OK17) | 2026-07-31 19:01 UTC | 2026-07-31 19:36 UTC | 35m |
| RAM803L | Royal Air Maroc | London Gatwick Airport (EGKK) | Tit Mellil Airport (GMMT) | 2026-07-31 16:46 UTC | 2026-07-31 19:27 UTC | 2h 40m |
| N6065P |  | Laurence G Hanscom Field (KBED) | Laurence G Hanscom Field (KBED) | 2026-07-31 18:50 UTC | 2026-07-31 19:23 UTC | 33m |
| SH185 |  | Hollandale Municipal Airport (K14M) | Pinebluff Regional/Grider Field (KPBF) | 2026-07-31 18:51 UTC | 2026-07-31 19:23 UTC | 31m |
| UAE9830 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-07-31 12:09 UTC | 2026-07-31 19:22 UTC | 7h 12m |
| LXJ339 | LXJ | Truckee-Tahoe Airport (KTRK) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-31 18:44 UTC | 2026-07-31 19:22 UTC | 37m |
| N984BT |  | Beaver County Airport (KBVI) | Harry Clever Field (KPHD) | 2026-07-31 18:51 UTC | 2026-07-31 19:19 UTC | 27m |
| TESTER23 | TES | Patuxent River Nas (Trapnell Field) Airport (KNHK) | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | 2026-07-31 18:50 UTC | 2026-07-31 19:19 UTC | 28m |
| N7644G |  | OH11 (OH11) | 8OA9 (8OA9) | 2026-07-31 18:06 UTC | 2026-07-31 19:16 UTC | 1h 9m |
| MS2 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-07-31 17:51 UTC | 2026-07-31 19:15 UTC | 1h 24m |
| N271CS |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | Deer Park Airport (KDEW) | 2026-07-31 17:58 UTC | 2026-07-31 19:14 UTC | 1h 16m |
| N809BT |  | Bowman Field (KLOU) | Madison Regional Airport (KIMS) | 2026-07-31 18:21 UTC | 2026-07-31 19:14 UTC | 52m |
| N7261Y |  | Glendale Regional Airport (KGEU) | Montezuma Airport (19AZ) | 2026-07-31 18:42 UTC | 2026-07-31 19:14 UTC | 32m |
| N729GT |  | Bishop International Airport (KFNT) | Gaylord Regional Airport (KGLR) | 2026-07-31 18:39 UTC | 2026-07-31 19:11 UTC | 31m |
| N891JC |  | Roseland Airport (32MD) | MD62 (MD62) | 2026-07-31 19:06 UTC | 2026-07-31 19:10 UTC | 3m |
| OXF4955 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-07-31 18:26 UTC | 2026-07-31 19:08 UTC | 41m |
| N247TC |  | Watsonville Municipal Airport (KWVI) | Truckee-Tahoe Airport (KTRK) | 2026-07-31 18:19 UTC | 2026-07-31 19:08 UTC | 48m |
| N331BR |  | David Wayne Hooks Memorial Airport (KDWH) | Addison Airport (KADS) | 2026-07-31 18:22 UTC | 2026-07-31 19:08 UTC | 45m |
| N7073G |  | Charles M Schulz/Sonoma County Airport (KSTS) | Columbia Airport (KO22) | 2026-07-31 17:46 UTC | 2026-07-31 19:08 UTC | 1h 21m |
| N477XP |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-07-31 17:55 UTC | 2026-07-31 19:03 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
