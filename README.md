# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_21:09:32_UTC-green)

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

**Latest saved flight:** 2026-08-12 21:09:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 21:09:32 UTC

- **190,750** saved flights
- **60,200** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,750** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,283,193.5 tonnes** estimated CO2 emissions
- **132,359,044 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7572 |
| 2 | SkyWest Airlines | 6908 |
| 3 | EJA | 3769 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2979 |
| 6 | American Airlines | 2963 |
| 7 | ENY | 2362 |
| 8 | Delta Air Lines | 2242 |
| 9 | LATAM Airlines | 1789 |
| 10 | AZU | 1724 |
| 11 | Lufthansa | 1659 |
| 12 | WIF | 1584 |
| 13 | Vueling | 1583 |
| 14 | LXJ | 1495 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1179 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1136 |
| 22 | VIV | 1051 |
| 23 | GLO | 1030 |
| 24 | Air France | 994 |
| 25 | PGT | 987 |
| 26 | CXK | 977 |
| 27 | AEE | 975 |
| 28 | United Airlines | 975 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162621 |
| 2 | 🇪🇸 ES | 12299 |
| 3 | 🇧🇷 BR | 10981 |
| 4 | 🇦🇺 AU | 10662 |
| 5 | 🇨🇦 CA | 10453 |
| 6 | 🇮🇳 IN | 10368 |
| 7 | 🇮🇹 IT | 9907 |
| 8 | 🇩🇪 DE | 9427 |
| 9 | 🇬🇧 GB | 8892 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7631 |
| 12 | 🇨🇴 CO | 7336 |
| 13 | 🇬🇷 GR | 5577 |
| 14 | 🇲🇽 MX | 5406 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5090 |
| 17 | 🇳🇴 NO | 4912 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3211 |
| 20 | 🇵🇱 PL | 3155 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2414 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1960 |
| 27 | 🇲🇦 MA | 1932 |
| 28 | 🇳🇱 NL | 1703 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3960 |
| 2 | Denver International Airport |  | US | 3133 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2361 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2225 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2017 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1976 |
| 10 | La Aurora Airport |  | GT | 1856 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1727 |
| 12 | El Dorado International Airport |  | CO | 1723 |
| 13 | Salt Lake City International Airport |  | US | 1695 |
| 14 | Chicago O'Hare International Airport |  | US | 1669 |
| 15 | Frankfurt am Main International Airport |  | DE | 1626 |
| 16 | Congonhas Airport |  | BR | 1597 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | Capua Airport |  | IT | 1480 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1478 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1406 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1369 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1316 |
| 25 | Charles de Gaulle International Airport |  | FR | 1305 |
| 26 | Charlotte/Douglas International Airport |  | US | 1275 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1192 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1170 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1108 |
| 34 | Reno/Tahoe International Airport |  | US | 1097 |
| 35 | Seattle-Tacoma International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1088 |
| 37 | Daniel K Inouye International Airport |  | US | 1070 |
| 38 | Oslo Gardermoen Airport |  | NO | 1067 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 975 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 698 | 21m | 244 km | 2,939.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 444 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 301 | 8m | - | - |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 233 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 232 | 1h 15m | 961 km | 3,845.5 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 227 | 19m | 144 km | 564.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N362LU |  | Lewis University Airport (KLOT) | 89LL (89LL) | 2026-08-12 20:31 UTC | 2026-08-12 21:09 UTC | 38m |
| N734BN |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-12 20:28 UTC | 2026-08-12 21:08 UTC | 40m |
| N49024 |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-08-12 20:01 UTC | 2026-08-12 21:04 UTC | 1h 3m |
| N24RP |  | Gillespie Field (KSEE) | Borrego Air Ranch Airport (58CL) | 2026-08-12 20:25 UTC | 2026-08-12 21:02 UTC | 36m |
| N789PF |  | Wilkes-Barre Wyoming Valley Airport (KWBW) | Lancaster Airport (KLNS) | 2026-08-12 20:15 UTC | 2026-08-12 21:01 UTC | 45m |
| LXJ444 | LXJ | Moffett Federal Airfield (KNUQ) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-12 19:01 UTC | 2026-08-12 20:58 UTC | 1h 56m |
| DINOCO1 | DIN | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | 0WN9 (0WN9) | 2026-08-12 17:43 UTC | 2026-08-12 20:57 UTC | 3h 14m |
| CFR652 | CFR | Porterville Municipal Airport (KPTV) | 6CL4 (6CL4) | 2026-08-12 20:11 UTC | 2026-08-12 20:52 UTC | 40m |
| COBRA74 | COB | 91CL (91CL) | Edwards Af Aux North Base Airport (K9L2) | 2026-08-12 20:39 UTC | 2026-08-12 20:50 UTC | 11m |
| N38987 |  | Newport State Airport (KUUU) | Newport State Airport (KUUU) | 2026-08-12 20:22 UTC | 2026-08-12 20:48 UTC | 25m |
| LS19 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-12 19:39 UTC | 2026-08-12 20:44 UTC | 1h 4m |
| VAR476 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-12 20:12 UTC | 2026-08-12 20:43 UTC | 31m |
| N682MA |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-12 20:26 UTC | 2026-08-12 20:42 UTC | 16m |
| SFY200 | SFY | Vero Beach Regional Airport (KVRB) | Indian River Aerodrome (FL74) | 2026-08-12 19:39 UTC | 2026-08-12 20:42 UTC | 1h 3m |
| THY7LA | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-12 18:23 UTC | 2026-08-12 20:42 UTC | 2h 19m |
| BCS4620 | BCS | Stuttgart Airport (EDDS) | Cologne Bonn Airport (EDDK) | 2026-08-12 19:52 UTC | 2026-08-12 20:39 UTC | 47m |
| KLM59F | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Lager Hammelburg Airport (EDFJ) | 2026-08-12 19:49 UTC | 2026-08-12 20:39 UTC | 50m |
| HAWK247 | HAW | Kingsville Nas Airport (KNQI) | 59TS (59TS) | 2026-08-12 20:29 UTC | 2026-08-12 20:39 UTC | 10m |
| N216BG |  | Destin Executive Airport (KDTS) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-12 19:46 UTC | 2026-08-12 20:37 UTC | 50m |
| TKR167 | TKR | Paradise Skypark Airport (CA92) | Nervino Airport (KO02) | 2026-08-12 20:24 UTC | 2026-08-12 20:36 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
