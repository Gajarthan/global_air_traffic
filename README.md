# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_17:51:23_UTC-green)

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

**Latest saved flight:** 2026-08-10 17:51:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 17:51:23 UTC

- **184,692** saved flights
- **58,763** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,692** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,218,663.9 tonnes** estimated CO2 emissions
- **128,618,198 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7330 |
| 2 | SkyWest Airlines | 6710 |
| 3 | EJA | 3645 |
| 4 | IndiGo | 3236 |
| 5 | Southwest Airlines | 2896 |
| 6 | American Airlines | 2876 |
| 7 | ENY | 2301 |
| 8 | Delta Air Lines | 2177 |
| 9 | LATAM Airlines | 1727 |
| 10 | AZU | 1656 |
| 11 | Lufthansa | 1626 |
| 12 | WIF | 1529 |
| 13 | Vueling | 1524 |
| 14 | LXJ | 1454 |
| 15 | easyJet | 1268 |
| 16 | Swiss International | 1266 |
| 17 | AXM | 1235 |
| 18 | EJU | 1139 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1105 |
| 22 | VIV | 1015 |
| 23 | GLO | 988 |
| 24 | Air France | 961 |
| 25 | AEE | 960 |
| 26 | CXK | 957 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 943 |
| 29 | United Airlines | 942 |
| 30 | MXY | 917 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157764 |
| 2 | 🇪🇸 ES | 11873 |
| 3 | 🇧🇷 BR | 10598 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10140 |
| 6 | 🇨🇦 CA | 10062 |
| 7 | 🇮🇹 IT | 9541 |
| 8 | 🇩🇪 DE | 9133 |
| 9 | 🇬🇧 GB | 8577 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7391 |
| 12 | 🇨🇴 CO | 6932 |
| 13 | 🇬🇷 GR | 5419 |
| 14 | 🇲🇽 MX | 5270 |
| 15 | 🇨🇭 CH | 4942 |
| 16 | 🇹🇷 TR | 4834 |
| 17 | 🇳🇴 NO | 4752 |
| 18 | 🇲🇾 MY | 3219 |
| 19 | 🇿🇦 ZA | 3104 |
| 20 | 🇵🇱 PL | 3087 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2441 |
| 24 | 🇬🇹 GT | 2364 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1868 |
| 27 | 🇭🇷 HR | 1855 |
| 28 | 🇲🇪 ME | 1667 |
| 29 | 🇳🇱 NL | 1655 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3827 |
| 2 | Denver International Airport |  | US | 3046 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2273 |
| 5 | Guaymaral Airport |  | CO | 2255 |
| 6 | Harry Reid International Airport |  | US | 2159 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1981 |
| 8 | Zurich Airport |  | CH | 1977 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1915 |
| 10 | La Aurora Airport |  | GT | 1813 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1678 |
| 12 | El Dorado International Airport |  | CO | 1655 |
| 13 | Salt Lake City International Airport |  | US | 1645 |
| 14 | Chicago O'Hare International Airport |  | US | 1643 |
| 15 | Frankfurt am Main International Airport |  | DE | 1594 |
| 16 | Congonhas Airport |  | BR | 1537 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 19 | Madrid Barajas International Airport |  | ES | 1451 |
| 20 | Capua Airport |  | IT | 1450 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1377 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1320 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1275 |
| 25 | Charles de Gaulle International Airport |  | FR | 1263 |
| 26 | Charlotte/Douglas International Airport |  | US | 1251 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1153 |
| 30 | Ninoy Aquino International Airport |  | PH | 1151 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1132 |
| 32 | Barcelona International Airport |  | ES | 1094 |
| 33 | Viracopos International Airport |  | BR | 1062 |
| 34 | Seattle-Tacoma International Airport |  | US | 1061 |
| 35 | Reno/Tahoe International Airport |  | US | 1058 |
| 36 | Calgary International Airport |  | CA | 1051 |
| 37 | Daniel K Inouye International Airport |  | US | 1049 |
| 38 | Oslo Gardermoen Airport |  | NO | 1028 |
| 39 | Tenerife Norte Airport |  | ES | 1008 |
| 40 | Vitoria/Foronda Airport |  | ES | 1001 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 930 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 677 | 21m | 244 km | 2,850.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 429 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 310 | 27m | 275 km | 1,469.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 275 | 44m | 241 km | 1,142.3 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 269 | 22m | 55 km | 255.7 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 262 | 8m | - | - |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 261 | 1h 49m | 1,423 km | 6,405.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 226 | 1h 15m | 961 km | 3,746.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 222 | 19m | 144 km | 552.2 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 221 | 50m | 556 km | 2,118.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 218 | 24m | 218 km | 821.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1127 | CXK | Miles Airport (13KY) | Barkley Regional Airport (KPAH) | 2026-08-10 17:09 UTC | 2026-08-10 17:51 UTC | 42m |
| N6544 |  | Winter Haven Regional Airport (KGIF) | Gore Airport (4FL9) | 2026-08-10 17:27 UTC | 2026-08-10 17:46 UTC | 19m |
| N278SP |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-10 16:46 UTC | 2026-08-10 17:39 UTC | 53m |
| N36GV |  | Diamond A Ranch Airport (NM64) | Diamond A Ranch Airport (NM64) | 2026-08-10 17:25 UTC | 2026-08-10 17:38 UTC | 13m |
| TKR855 | TKR | K36U (K36U) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-10 17:21 UTC | 2026-08-10 17:38 UTC | 16m |
| LUZON41 | LUZ | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-08-10 17:02 UTC | 2026-08-10 17:37 UTC | 35m |
| N80484 |  | Montgomery County Airpark (KGAI) | Montgomery County Airpark (KGAI) | 2026-08-10 16:33 UTC | 2026-08-10 17:37 UTC | 1h 3m |
| TKR169 | TKR | Boise Air Trml/Gowen Field (KBOI) | Morgan County Airport (K42U) | 2026-08-10 16:47 UTC | 2026-08-10 17:35 UTC | 47m |
| TKR101 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-10 17:29 UTC | 2026-08-10 17:31 UTC | 2m |
| ELY5142 | ELY | Larnaca International Airport (LCLK) | Ben Gurion International Airport (LLBG) | 2026-08-10 16:42 UTC | 2026-08-10 17:26 UTC | 44m |
| N80619 |  | Airlake Airport (KLVN) | Airlake Airport (KLVN) | 2026-08-10 16:34 UTC | 2026-08-10 17:24 UTC | 50m |
| SH087 |  | Evergreen Regional/Middleton Field (KGZH) | Evergreen Regional/Middleton Field (KGZH) | 2026-08-10 16:56 UTC | 2026-08-10 17:23 UTC | 27m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-10 16:47 UTC | 2026-08-10 17:23 UTC | 36m |
| N528LP |  | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-08-10 16:35 UTC | 2026-08-10 17:22 UTC | 47m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-08-10 16:45 UTC | 2026-08-10 17:22 UTC | 37m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-10 17:02 UTC | 2026-08-10 17:19 UTC | 16m |
| N593FD |  | Thomasville Regional Airport (KTVI) | Booneville/Baldwyn Airport (K8M1) | 2026-08-10 15:58 UTC | 2026-08-10 17:19 UTC | 1h 20m |
| N521RT |  | Knoxville Municipal Airport (KOXV) | Rocky Mountain Metro Airport (KBJC) | 2026-08-10 14:55 UTC | 2026-08-10 17:18 UTC | 2h 22m |
| ARCAS05 | ARC | Kickapoo Downtown Airport (KCWC) | Arledge Field (KF56) | 2026-08-10 17:02 UTC | 2026-08-10 17:14 UTC | 12m |
| N228JJ |  | Toledo Executive Airport (KTDZ) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-10 16:39 UTC | 2026-08-10 17:13 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
