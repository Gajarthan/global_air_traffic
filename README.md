# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_19:52:43_UTC-green)

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

**Latest saved flight:** 2026-08-11 19:52:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 19:52:43 UTC

- **187,822** saved flights
- **59,508** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,822** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,252,560.4 tonnes** estimated CO2 emissions
- **130,583,209 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7466 |
| 2 | SkyWest Airlines | 6824 |
| 3 | EJA | 3704 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2937 |
| 6 | American Airlines | 2923 |
| 7 | ENY | 2330 |
| 8 | Delta Air Lines | 2210 |
| 9 | LATAM Airlines | 1757 |
| 10 | AZU | 1690 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1558 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1469 |
| 15 | easyJet | 1296 |
| 16 | Swiss International | 1281 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1119 |
| 22 | VIV | 1038 |
| 23 | GLO | 1009 |
| 24 | Air France | 977 |
| 25 | AEE | 969 |
| 26 | CXK | 965 |
| 27 | PGT | 964 |
| 28 | United Airlines | 955 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 934 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160252 |
| 2 | 🇪🇸 ES | 12108 |
| 3 | 🇧🇷 BR | 10784 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10266 |
| 6 | 🇨🇦 CA | 10253 |
| 7 | 🇮🇹 IT | 9745 |
| 8 | 🇩🇪 DE | 9293 |
| 9 | 🇬🇧 GB | 8739 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7515 |
| 12 | 🇨🇴 CO | 7118 |
| 13 | 🇬🇷 GR | 5514 |
| 14 | 🇲🇽 MX | 5353 |
| 15 | 🇨🇭 CH | 5031 |
| 16 | 🇹🇷 TR | 4972 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3115 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2390 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1910 |
| 27 | 🇭🇷 HR | 1906 |
| 28 | 🇲🇪 ME | 1682 |
| 29 | 🇳🇱 NL | 1676 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3897 |
| 2 | Denver International Airport |  | US | 3091 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2304 |
| 6 | Harry Reid International Airport |  | US | 2197 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 8 | Zurich Airport |  | CH | 1999 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1945 |
| 10 | La Aurora Airport |  | GT | 1837 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1706 |
| 12 | El Dorado International Airport |  | CO | 1686 |
| 13 | Salt Lake City International Airport |  | US | 1674 |
| 14 | Chicago O'Hare International Airport |  | US | 1655 |
| 15 | Frankfurt am Main International Airport |  | DE | 1613 |
| 16 | Congonhas Airport |  | BR | 1569 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1481 |
| 19 | Capua Airport |  | IT | 1468 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1460 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1396 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1344 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1294 |
| 25 | Charles de Gaulle International Airport |  | FR | 1283 |
| 26 | Charlotte/Douglas International Airport |  | US | 1262 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1176 |
| 30 | Ninoy Aquino International Airport |  | PH | 1169 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1151 |
| 32 | Barcelona International Airport |  | ES | 1123 |
| 33 | Viracopos International Airport |  | BR | 1082 |
| 34 | Reno/Tahoe International Airport |  | US | 1080 |
| 35 | Seattle-Tacoma International Airport |  | US | 1078 |
| 36 | Calgary International Airport |  | CA | 1065 |
| 37 | Daniel K Inouye International Airport |  | US | 1059 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1031 |
| 40 | Vitoria/Foronda Airport |  | ES | 1018 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 950 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 687 | 21m | 244 km | 2,892.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 438 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 315 | 27m | 275 km | 1,492.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 304 | 14m | 114 km | 596.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 278 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 229 | 1h 15m | 961 km | 3,795.8 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 229 | 50m | 556 km | 2,195.2 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 203 | 1h 49m | 1,304 km | 4,567.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N22TE |  | 3WA9 (3WA9) | Condon State Pauling Field (K3S9) | 2026-08-11 17:15 UTC | 2026-08-11 19:52 UTC | 2h 37m |
| N608FM |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-08-11 19:26 UTC | 2026-08-11 19:42 UTC | 15m |
| BOMR832 | BOM | Easterwood Field (KCLL) | Gritz Field (XS46) | 2026-08-11 18:49 UTC | 2026-08-11 19:42 UTC | 53m |
| GFD50 | GFD | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-08-11 18:41 UTC | 2026-08-11 19:40 UTC | 59m |
| ALAMO20 | ALA | Cross-B Airport (24XA) | Easterwood Field (KCLL) | 2026-08-11 18:41 UTC | 2026-08-11 19:37 UTC | 56m |
| JBU2020 | JetBlue | Fort Lauderdale/Hollywood International Airport (KFLL) | Worcester Regional Airport (KORH) | 2026-08-11 16:59 UTC | 2026-08-11 19:36 UTC | 2h 37m |
| N257CT |  | Mahlon Sweet Field (KEUG) | Mahlon Sweet Field (KEUG) | 2026-08-11 18:37 UTC | 2026-08-11 19:34 UTC | 57m |
| CFR89 | CFR | Nevada County Airport (KGOO) | Truckee-Tahoe Airport (KTRK) | 2026-08-11 19:23 UTC | 2026-08-11 19:33 UTC | 10m |
| CFR88 | CFR | Nevada County Airport (KGOO) | Truckee-Tahoe Airport (KTRK) | 2026-08-11 19:22 UTC | 2026-08-11 19:33 UTC | 10m |
| N56578 |  | Somerset Airport (KSMQ) | Lehigh Valley International Airport (KABE) | 2026-08-11 18:41 UTC | 2026-08-11 19:31 UTC | 50m |
| N326AK |  | Delaware Coastal Airport (KGED) | Delaware Coastal Airport (KGED) | 2026-08-11 18:59 UTC | 2026-08-11 19:30 UTC | 31m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Solberg/Hunterdon Airport (KN51) | 2026-08-11 18:51 UTC | 2026-08-11 19:28 UTC | 37m |
| N28JA |  | Lakewood Airport (KN12) | Lakewood Airport (KN12) | 2026-08-11 19:18 UTC | 2026-08-11 19:23 UTC | 4m |
| CXK253 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-08-11 18:03 UTC | 2026-08-11 19:22 UTC | 1h 19m |
| N140SX |  | Carson City Airport (KCXP) | Gnoss Field (KDVO) | 2026-08-11 18:47 UTC | 2026-08-11 19:19 UTC | 31m |
| WLDLD27 | WLD | Centennial Airport (KAPA) | Castle Lakes Airport (CD32) | 2026-08-11 17:55 UTC | 2026-08-11 19:18 UTC | 1h 22m |
| EJA803 | EJA | Laurence G Hanscom Field (KBED) | Bulljump Airport (11MA) | 2026-08-11 18:53 UTC | 2026-08-11 19:18 UTC | 24m |
| N4431R |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-11 18:47 UTC | 2026-08-11 19:17 UTC | 30m |
|  |  | Whidbey Island Nas (Ault Field) Airport (KNUW) | Mineral County Airport (K9S4) | 2026-08-11 18:26 UTC | 2026-08-11 19:17 UTC | 50m |
| N406M |  | Iliamna Airport (PAIL) | Soldotna Airport (PASX) | 2026-08-11 18:32 UTC | 2026-08-11 19:15 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
