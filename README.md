# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_13:04:13_UTC-green)

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

**Latest saved flight:** 2026-08-06 13:04:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 13:04:13 UTC

- **174,034** saved flights
- **56,366** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,034** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,096,649.9 tonnes** estimated CO2 emissions
- **121,544,920 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6905 |
| 2 | SkyWest Airlines | 6370 |
| 3 | EJA | 3452 |
| 4 | IndiGo | 3045 |
| 5 | Southwest Airlines | 2744 |
| 6 | American Airlines | 2732 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2062 |
| 9 | LATAM Airlines | 1610 |
| 10 | Lufthansa | 1576 |
| 11 | AZU | 1539 |
| 12 | WIF | 1458 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1362 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1184 |
| 17 | easyJet | 1183 |
| 18 | EJU | 1064 |
| 19 | QLK | 1063 |
| 20 | Alaska Airlines | 1058 |
| 21 | All Nippon Airways | 1056 |
| 22 | VIV | 957 |
| 23 | Cathay Pacific | 942 |
| 24 | CXK | 924 |
| 25 | GLO | 916 |
| 26 | AEE | 908 |
| 27 | United Airlines | 905 |
| 28 | Air France | 893 |
| 29 | MXY | 880 |
| 30 | JetBlue | 868 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149853 |
| 2 | 🇪🇸 ES | 11134 |
| 3 | 🇧🇷 BR | 9911 |
| 4 | 🇦🇺 AU | 9765 |
| 5 | 🇮🇳 IN | 9557 |
| 6 | 🇨🇦 CA | 9524 |
| 7 | 🇮🇹 IT | 8983 |
| 8 | 🇩🇪 DE | 8623 |
| 9 | 🇬🇧 GB | 8060 |
| 10 | 🇯🇵 JP | 6995 |
| 11 | 🇫🇷 FR | 6901 |
| 12 | 🇨🇴 CO | 6409 |
| 13 | 🇬🇷 GR | 5051 |
| 14 | 🇲🇽 MX | 4978 |
| 15 | 🇨🇭 CH | 4595 |
| 16 | 🇳🇴 NO | 4533 |
| 17 | 🇹🇷 TR | 4269 |
| 18 | 🇲🇾 MY | 3092 |
| 19 | 🇵🇱 PL | 2910 |
| 20 | 🇿🇦 ZA | 2802 |
| 21 | 🇹🇭 TH | 2558 |
| 22 | 🇳🇿 NZ | 2523 |
| 23 | 🇵🇭 PH | 2296 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2184 |
| 26 | 🇲🇦 MA | 1751 |
| 27 | 🇭🇷 HR | 1683 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1566 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2882 |
| 3 | Tokyo International Airport |  | JP | 2185 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2126 |
| 6 | Harry Reid International Airport |  | US | 2085 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1888 |
| 8 | Zurich Airport |  | CH | 1843 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1825 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1573 |
| 14 | Salt Lake City International Airport |  | US | 1562 |
| 15 | Frankfurt am Main International Airport |  | DE | 1539 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1434 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1420 |
| 19 | Capua Airport |  | IT | 1357 |
| 20 | Madrid Barajas International Airport |  | ES | 1356 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1227 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1215 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1181 |
| 26 | Malpensa International Airport |  | IT | 1179 |
| 27 | Kuala Lumpur International Airport |  | MY | 1166 |
| 28 | Bengaluru International Airport |  | IN | 1133 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1080 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1072 |
| 32 | Barcelona International Airport |  | ES | 1028 |
| 33 | Daniel K Inouye International Airport |  | US | 1003 |
| 34 | Seattle-Tacoma International Airport |  | US | 1003 |
| 35 | Calgary International Airport |  | CA | 989 |
| 36 | Reno/Tahoe International Airport |  | US | 987 |
| 37 | Viracopos International Airport |  | BR | 987 |
| 38 | Oslo Gardermoen Airport |  | NO | 968 |
| 39 | Tenerife Norte Airport |  | ES | 962 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 635 | 21m | 244 km | 2,673.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 410 | 24m | 225 km | 1,590.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 395 | 1h 8m | 770 km | 5,247.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 239 | 1h 48m | 1,423 km | 5,865.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 202 | 1h 38m | 1,156 km | 4,029.8 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 26 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 202 | 8m | - | - |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 194 | 24m | 218 km | 730.9 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 189 | 43m | 452 km | 1,473.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-06 05:44 UTC | 2026-08-06 13:04 UTC | 7h 19m |
| N872FA |  | Lewis University Airport (KLOT) | 3IL2 (3IL2) | 2026-08-06 12:34 UTC | 2026-08-06 12:58 UTC | 24m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-06 12:15 UTC | 2026-08-06 12:53 UTC | 37m |
| CDG7608 | CDG | Beijing Capital International Airport (ZBAA) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-06 12:36 UTC | 2026-08-06 12:52 UTC | 15m |
| SAMU86 | SAM | Montendre Marcillac Airport (LFDC) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-08-06 12:33 UTC | 2026-08-06 12:46 UTC | 13m |
| OKDPH | OKD | Letnany Airport (LKLT) | Kolin Airport (LKKO) | 2026-08-06 11:54 UTC | 2026-08-06 12:45 UTC | 50m |
| CPA507 | Cathay Pacific | Kansai International Airport (RJBB) | Zhuhai Airport (ZGSD) | 2026-08-06 09:43 UTC | 2026-08-06 12:44 UTC | 3h 0m |
| N6755W |  | Burnett County Airport (KRZN) | Rush City Regional Airport (KROS) | 2026-08-06 12:14 UTC | 2026-08-06 12:42 UTC | 28m |
| N126ME |  | Immokalee Regional Airport (KIMM) | Naples Municipal Airport (KAPF) | 2026-08-06 12:18 UTC | 2026-08-06 12:41 UTC | 23m |
| HBKKC | HBK | Amlikon Glider Airport (LSPA) | Winterthur Airport (LSPH) | 2026-08-06 11:52 UTC | 2026-08-06 12:41 UTC | 49m |
| RWZ550 | RWZ | Batumi International Airport (UGSB) | Bezymyanka Airfield (UWWG) | 2026-08-06 10:38 UTC | 2026-08-06 12:41 UTC | 2h 2m |
| N805JA |  | Felts Field (KSFF) | Carson Field (MT53) | 2026-08-06 12:10 UTC | 2026-08-06 12:35 UTC | 24m |
| N408RK |  | Hector International Airport (KFAR) | Joe Foss Field (KFSD) | 2026-08-06 11:50 UTC | 2026-08-06 12:32 UTC | 41m |
| N733FF |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-08-06 12:15 UTC | 2026-08-06 12:30 UTC | 14m |
| LOT5TV | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Ostrava Leos Janacek Airport (LKMT) | 2026-08-06 11:47 UTC | 2026-08-06 12:27 UTC | 39m |
| GCM108 | GCM | Lanseria Airport (FALA) | Belfast Aerodrome (FABH) | 2026-08-06 12:07 UTC | 2026-08-06 12:27 UTC | 20m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-06 12:14 UTC | 2026-08-06 12:27 UTC | 12m |
| SKYHWK1 | SKY | Nordholz Airport (ETMN) | Neumagen-Dhron Airport (EDRD) | 2026-08-06 11:44 UTC | 2026-08-06 12:26 UTC | 42m |
| BAW9260 | British Airways | Glasgow International Airport (EGPF) | Glasgow Prestwick Airport (EGPK) | 2026-08-06 11:52 UTC | 2026-08-06 12:19 UTC | 27m |
| GCLXB | GCL | Chichester/Goodwood Airport (EGHR) | Bembridge Airport (EGHJ) | 2026-08-06 12:13 UTC | 2026-08-06 12:19 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
