# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_21:40:53_UTC-green)

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

**Latest saved flight:** 2026-08-13 21:40:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 21:40:53 UTC

- **193,701** saved flights
- **60,940** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **193,701** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,315,601.5 tonnes** estimated CO2 emissions
- **134,237,767 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7707 |
| 2 | SkyWest Airlines | 7002 |
| 3 | EJA | 3819 |
| 4 | IndiGo | 3345 |
| 5 | Southwest Airlines | 3013 |
| 6 | American Airlines | 3002 |
| 7 | ENY | 2399 |
| 8 | Delta Air Lines | 2287 |
| 9 | LATAM Airlines | 1817 |
| 10 | AZU | 1747 |
| 11 | Lufthansa | 1673 |
| 12 | Vueling | 1613 |
| 13 | WIF | 1603 |
| 14 | LXJ | 1534 |
| 15 | easyJet | 1337 |
| 16 | Swiss International | 1315 |
| 17 | AXM | 1258 |
| 18 | EJU | 1193 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1149 |
| 22 | VIV | 1064 |
| 23 | GLO | 1042 |
| 24 | Air France | 1011 |
| 25 | PGT | 1007 |
| 26 | AEE | 991 |
| 27 | United Airlines | 990 |
| 28 | CXK | 989 |
| 29 | WMT | 964 |
| 30 | Wizz Air | 962 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 164987 |
| 2 | 🇪🇸 ES | 12503 |
| 3 | 🇧🇷 BR | 11139 |
| 4 | 🇦🇺 AU | 10812 |
| 5 | 🇨🇦 CA | 10610 |
| 6 | 🇮🇳 IN | 10471 |
| 7 | 🇮🇹 IT | 10076 |
| 8 | 🇩🇪 DE | 9584 |
| 9 | 🇬🇧 GB | 9066 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7731 |
| 12 | 🇨🇴 CO | 7530 |
| 13 | 🇬🇷 GR | 5672 |
| 14 | 🇲🇽 MX | 5481 |
| 15 | 🇹🇷 TR | 5223 |
| 16 | 🇨🇭 CH | 5208 |
| 17 | 🇳🇴 NO | 4963 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3190 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2712 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2465 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 2009 |
| 27 | 🇲🇦 MA | 1970 |
| 28 | 🇳🇱 NL | 1742 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4028 |
| 2 | Denver International Airport |  | US | 3178 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2410 |
| 5 | Indira Gandhi International Airport |  | IN | 2359 |
| 6 | Harry Reid International Airport |  | US | 2243 |
| 7 | Zurich Airport |  | CH | 2054 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2046 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2007 |
| 10 | La Aurora Airport |  | GT | 1895 |
| 11 | El Dorado International Airport |  | CO | 1762 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1741 |
| 13 | Salt Lake City International Airport |  | US | 1729 |
| 14 | Chicago O'Hare International Airport |  | US | 1697 |
| 15 | Frankfurt am Main International Airport |  | DE | 1639 |
| 16 | Congonhas Airport |  | BR | 1623 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1527 |
| 19 | Capua Airport |  | IT | 1492 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1489 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1431 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1388 |
| 23 | Malpensa International Airport |  | IT | 1343 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1343 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1290 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1207 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1185 |
| 32 | Barcelona International Airport |  | ES | 1159 |
| 33 | Viracopos International Airport |  | BR | 1126 |
| 34 | Seattle-Tacoma International Airport |  | US | 1111 |
| 35 | Calgary International Airport |  | CA | 1108 |
| 36 | Reno/Tahoe International Airport |  | US | 1103 |
| 37 | Oslo Gardermoen Airport |  | NO | 1087 |
| 38 | Daniel K Inouye International Airport |  | US | 1082 |
| 39 | Tenerife Norte Airport |  | ES | 1066 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 710 | 21m | 244 km | 2,989.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 454 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 318 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 289 | 44m | 241 km | 1,200.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 242 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 238 | 24m | 218 km | 896.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 228 | 1h 38m | 1,156 km | 4,548.5 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 209 | 1h 48m | 1,304 km | 4,702.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7913U |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-08-13 21:03 UTC | 2026-08-13 21:40 UTC | 37m |
| N533ME |  | Allegheny County Airport (KAGC) | Allegheny County Airport (KAGC) | 2026-08-13 21:28 UTC | 2026-08-13 21:39 UTC | 11m |
| TEX01 | TEX | RNZAF Base Ohakea (NZOH) | RNZAF Base Ohakea (NZOH) | 2026-08-13 21:09 UTC | 2026-08-13 21:37 UTC | 27m |
| BULET47 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-13 21:10 UTC | 2026-08-13 21:27 UTC | 17m |
| CMF1200 | CMF | Dekalb-Peachtree Airport (KPDK) | Southwest Georgia Regional Airport (KABY) | 2026-08-13 20:11 UTC | 2026-08-13 21:25 UTC | 1h 13m |
| N808W |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-08-13 21:07 UTC | 2026-08-13 21:18 UTC | 11m |
| N417Q |  | Buffalo Niagara International Airport (KBUF) | Battle Lake Municipal Airport (00MN) | 2026-08-13 18:38 UTC | 2026-08-13 21:10 UTC | 2h 32m |
| SKW6086 | SkyWest Airlines | Tucson International Airport (KTUS) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-08-13 20:29 UTC | 2026-08-13 21:09 UTC | 39m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-08-13 20:32 UTC | 2026-08-13 21:06 UTC | 34m |
| XSR326 | XSR | Raleigh-Durham International Airport (KRDU) | 3PA4 (3PA4) | 2026-08-13 19:58 UTC | 2026-08-13 21:05 UTC | 1h 7m |
| AVL119 | AVL | Washington Manassas/Harry P Davis Field (KHEF) | Culpeper Regional Airport (KCJR) | 2026-08-13 20:07 UTC | 2026-08-13 21:05 UTC | 57m |
| N6227 |  | Austin Executive Airport (KEDC) | Bud Dryden Airport (TX05) | 2026-08-13 20:40 UTC | 2026-08-13 21:04 UTC | 24m |
| N2472U |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-13 20:37 UTC | 2026-08-13 21:01 UTC | 23m |
| N504PS |  | La Porte Municipal Airport (KPPO) | Bessemer Ntl Airport (KEKY) | 2026-08-13 19:34 UTC | 2026-08-13 21:00 UTC | 1h 26m |
| HK5298G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-13 20:27 UTC | 2026-08-13 20:57 UTC | 29m |
| N733GL |  | Cincinnati West Airport (KI67) | Miami University Airport (KOXD) | 2026-08-13 20:37 UTC | 2026-08-13 20:57 UTC | 20m |
| AAL133 | American Airlines | Dublin Airport (EIDW) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-13 11:59 UTC | 2026-08-13 20:55 UTC | 8h 56m |
| MSC652 | MSC | Eleftherios Venizelos International Airport (LGAV) | HE12 (HE12) | 2026-08-13 19:35 UTC | 2026-08-13 20:55 UTC | 1h 20m |
| N733KG |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-08-13 20:28 UTC | 2026-08-13 20:54 UTC | 25m |
| N650MP |  | Washington Manassas/Harry P Davis Field (KHEF) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-13 18:55 UTC | 2026-08-13 20:53 UTC | 1h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
