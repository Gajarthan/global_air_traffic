# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_21:38:07_UTC-green)

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

**Latest saved flight:** 2026-08-10 21:38:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 21:38:07 UTC

- **185,296** saved flights
- **58,907** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,296** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,225,197.9 tonnes** estimated CO2 emissions
- **128,996,979 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7352 |
| 2 | SkyWest Airlines | 6755 |
| 3 | EJA | 3667 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2907 |
| 6 | American Airlines | 2890 |
| 7 | ENY | 2307 |
| 8 | Delta Air Lines | 2182 |
| 9 | LATAM Airlines | 1732 |
| 10 | AZU | 1664 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1456 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1235 |
| 18 | EJU | 1145 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1109 |
| 22 | VIV | 1020 |
| 23 | GLO | 993 |
| 24 | AEE | 962 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 946 |
| 29 | United Airlines | 946 |
| 30 | MXY | 921 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158419 |
| 2 | 🇪🇸 ES | 11906 |
| 3 | 🇧🇷 BR | 10639 |
| 4 | 🇦🇺 AU | 10308 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10115 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9149 |
| 9 | 🇬🇧 GB | 8601 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7404 |
| 12 | 🇨🇴 CO | 6989 |
| 13 | 🇬🇷 GR | 5436 |
| 14 | 🇲🇽 MX | 5287 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4861 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3221 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3090 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2631 |
| 23 | 🇵🇭 PH | 2443 |
| 24 | 🇬🇹 GT | 2371 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1875 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3843 |
| 2 | Denver International Airport |  | US | 3065 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2272 |
| 6 | Harry Reid International Airport |  | US | 2167 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1927 |
| 10 | La Aurora Airport |  | GT | 1819 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1689 |
| 12 | El Dorado International Airport |  | CO | 1663 |
| 13 | Salt Lake City International Airport |  | US | 1653 |
| 14 | Chicago O'Hare International Airport |  | US | 1650 |
| 15 | Frankfurt am Main International Airport |  | DE | 1596 |
| 16 | Congonhas Airport |  | BR | 1548 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1382 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1322 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1254 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1160 |
| 30 | Ninoy Aquino International Airport |  | PH | 1152 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1137 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Viracopos International Airport |  | BR | 1066 |
| 34 | Reno/Tahoe International Airport |  | US | 1064 |
| 35 | Seattle-Tacoma International Airport |  | US | 1064 |
| 36 | Calgary International Airport |  | CA | 1053 |
| 37 | Daniel K Inouye International Airport |  | US | 1052 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 680 | 21m | 244 km | 2,863.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 431 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 264 | 8m | - | - |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 227 | 12m | - | - |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 224 | 50m | 556 km | 2,147.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4975F |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-08-10 21:21 UTC | 2026-08-10 21:38 UTC | 17m |
| TKR855 | TKR | K36U (K36U) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-10 21:13 UTC | 2026-08-10 21:28 UTC | 15m |
| BRG594 | BRG | Red Dog Airport (PADG) | Ambler Airport (PAFM) | 2026-08-10 20:40 UTC | 2026-08-10 21:23 UTC | 43m |
| ARCAS20 | ARC | Danaher Airport (7TX0) | Arledge Field (KF56) | 2026-08-10 21:10 UTC | 2026-08-10 21:21 UTC | 11m |
| PNTHR77 | PNT | Middle Wallop Airfield (EGVP) | Upavon Aerodrome (EGDJ) | 2026-08-10 20:50 UTC | 2026-08-10 21:21 UTC | 30m |
| PBR675 | PBR | Victoria International Airport (CYYJ) | Boundary Bay Airport (CZBB) | 2026-08-10 21:04 UTC | 2026-08-10 21:19 UTC | 15m |
| STT5042 | STT | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-10 20:46 UTC | 2026-08-10 21:06 UTC | 20m |
| N1022G |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Truckee-Tahoe Airport (KTRK) | 2026-08-10 20:07 UTC | 2026-08-10 21:03 UTC | 56m |
| UAL327 | United Airlines | San Diego International Airport (KSAN) | Newark Liberty International Airport (KEWR) | 2026-08-10 15:53 UTC | 2026-08-10 20:57 UTC | 5h 4m |
| N985P |  | Cortes Island (Hansen Airfield) Airport (CCI9) | Cortes Island (Hansen Airfield) Airport (CCI9) | 2026-08-10 20:53 UTC | 2026-08-10 20:57 UTC | 3m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-10 20:43 UTC | 2026-08-10 20:56 UTC | 12m |
| HOTT1 | HOT | Nogales International Airport (KOLS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-10 20:20 UTC | 2026-08-10 20:56 UTC | 35m |
| N4451P |  | Space Coast Regional Airport (KTIX) | Ocean Reef Club Airport (07FA) | 2026-08-10 19:00 UTC | 2026-08-10 20:56 UTC | 1h 55m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 20:35 UTC | 2026-08-10 20:54 UTC | 19m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 20:34 UTC | 2026-08-10 20:54 UTC | 20m |
| HK4350 |  | Enrique Olaya Herrera Airport (SKMD) | Amalfi Airport (SKAM) | 2026-08-10 20:40 UTC | 2026-08-10 20:52 UTC | 11m |
| N450PD |  | Coeur D'Alene Airport (KCOE) | Ozzy's Airport (33ID) | 2026-08-10 20:10 UTC | 2026-08-10 20:48 UTC | 37m |
| COUGR07 | COU | Scott Afb/Midamerica St Louis Airport (KBLV) | Yazoo County Airport (K87I) | 2026-08-10 19:52 UTC | 2026-08-10 20:48 UTC | 55m |
| N9531J |  | Mckinney Ntl Airport (KTKI) | Grove Hill Airport (5TX2) | 2026-08-10 20:15 UTC | 2026-08-10 20:46 UTC | 31m |
| BLINR17 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-10 20:36 UTC | 2026-08-10 20:46 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
