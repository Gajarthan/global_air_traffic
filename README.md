# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_00:57:52_UTC-green)

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

**Latest saved flight:** 2026-07-07 00:57:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 00:57:52 UTC

- **131,682** saved flights
- **44,728** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,682** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,588,399.5 tonnes** estimated CO2 emissions
- **92,081,128 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5353 |
| 2 | SkyWest Airlines | 4886 |
| 3 | EJA | 2584 |
| 4 | IndiGo | 2458 |
| 5 | American Airlines | 2053 |
| 6 | Southwest Airlines | 1984 |
| 7 | ENY | 1657 |
| 8 | Delta Air Lines | 1580 |
| 9 | Lufthansa | 1370 |
| 10 | LATAM Airlines | 1208 |
| 11 | Vueling | 1159 |
| 12 | WIF | 1147 |
| 13 | AZU | 1119 |
| 14 | LXJ | 1017 |
| 15 | AXM | 1014 |
| 16 | Swiss International | 921 |
| 17 | All Nippon Airways | 865 |
| 18 | easyJet | 843 |
| 19 | Alaska Airlines | 842 |
| 20 | QLK | 825 |
| 21 | EJU | 812 |
| 22 | VIV | 730 |
| 23 | AEE | 716 |
| 24 | Cathay Pacific | 716 |
| 25 | Air France | 714 |
| 26 | CXK | 707 |
| 27 | United Airlines | 702 |
| 28 | JetBlue | 691 |
| 29 | MXY | 686 |
| 30 | GLO | 676 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112942 |
| 2 | 🇪🇸 ES | 8772 |
| 3 | 🇮🇳 IN | 7706 |
| 4 | 🇦🇺 AU | 7599 |
| 5 | 🇧🇷 BR | 7421 |
| 6 | 🇨🇦 CA | 6962 |
| 7 | 🇩🇪 DE | 6879 |
| 8 | 🇮🇹 IT | 6857 |
| 9 | 🇬🇧 GB | 5873 |
| 10 | 🇯🇵 JP | 5669 |
| 11 | 🇫🇷 FR | 5230 |
| 12 | 🇨🇴 CO | 4129 |
| 13 | 🇲🇽 MX | 3846 |
| 14 | 🇬🇷 GR | 3764 |
| 15 | 🇳🇴 NO | 3563 |
| 16 | 🇨🇭 CH | 3382 |
| 17 | 🇹🇷 TR | 2933 |
| 18 | 🇲🇾 MY | 2628 |
| 19 | 🇿🇦 ZA | 2171 |
| 20 | 🇵🇱 PL | 2159 |
| 21 | 🇳🇿 NZ | 2090 |
| 22 | 🇹🇭 TH | 2034 |
| 23 | 🇰🇷 KR | 1967 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1788 |
| 26 | 🇲🇦 MA | 1400 |
| 27 | 🇲🇪 ME | 1301 |
| 28 | 🇳🇱 NL | 1232 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1155 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2755 |
| 2 | Denver International Airport |  | US | 2245 |
| 3 | Tokyo International Airport |  | JP | 1861 |
| 4 | Indira Gandhi International Airport |  | IN | 1701 |
| 5 | Harry Reid International Airport |  | US | 1641 |
| 6 | Guaymaral Airport |  | CO | 1595 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1551 |
| 8 | Zurich Airport |  | CH | 1450 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1405 |
| 10 | La Aurora Airport |  | GT | 1382 |
| 11 | Frankfurt am Main International Airport |  | DE | 1327 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1269 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1179 |
| 16 | Salt Lake City International Airport |  | US | 1175 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1135 |
| 18 | Madrid Barajas International Airport |  | ES | 1084 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1080 |
| 20 | Capua Airport |  | IT | 1077 |
| 21 | Congonhas Airport |  | BR | 1048 |
| 22 | Kuala Lumpur International Airport |  | MY | 1020 |
| 23 | Charlotte/Douglas International Airport |  | US | 979 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 956 |
| 25 | Charles de Gaulle International Airport |  | FR | 952 |
| 26 | Bengaluru International Airport |  | IN | 931 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 901 |
| 28 | Malpensa International Airport |  | IT | 880 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 824 |
| 31 | Barcelona International Airport |  | ES | 815 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 808 |
| 33 | Tenerife Norte Airport |  | ES | 793 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 775 |
| 35 | Calgary International Airport |  | CA | 769 |
| 36 | Seattle-Tacoma International Airport |  | US | 759 |
| 37 | Vitoria/Foronda Airport |  | ES | 754 |
| 38 | Viracopos International Airport |  | BR | 753 |
| 39 | Scottsdale Airport |  | US | 753 |
| 40 | Amsterdam Airport Schiphol |  | NL | 744 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 668 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 477 | 21m | 244 km | 2,008.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 329 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 319 | 1h 10m | 770 km | 4,237.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 282 | 14m | 114 km | 553.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 249 | 26m | 275 km | 1,179.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 192 | 22m | 55 km | 182.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 183 | 26m | 215 km | 677.8 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 180 | 20m | 99 km | 308.3 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 173 | 1h 46m | 1,423 km | 4,245.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 159 | 30m | 49 km | 134.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N74426 |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-07-07 00:09 UTC | 2026-07-07 00:57 UTC | 48m |
| AIC215 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-07-06 23:23 UTC | 2026-07-07 00:46 UTC | 1h 22m |
| S31 |  | Gaziemir Airport (LTBK) | Gaziemir Airport (LTBK) | 2026-07-07 00:00 UTC | 2026-07-07 00:46 UTC | 45m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-07-07 00:25 UTC | 2026-07-07 00:41 UTC | 15m |
| N8257G |  | Ramona Airport (KRNM) | San Bernardino International Airport (KSBD) | 2026-07-06 23:51 UTC | 2026-07-07 00:39 UTC | 48m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-06 23:39 UTC | 2026-07-07 00:38 UTC | 58m |
| CGARX | CGA | Winters Aire Park Airport (CFY4) | Winters Aire Park Airport (CFY4) | 2026-07-06 19:56 UTC | 2026-07-07 00:35 UTC | 4h 38m |
| TKR104 | TKR | Mesa Gateway Airport (KIWA) | San Bernardino International Airport (KSBD) | 2026-07-06 22:54 UTC | 2026-07-07 00:28 UTC | 1h 34m |
| N711FP |  | Easterwood Field (KCLL) | Addington Field (4TX8) | 2026-07-06 23:49 UTC | 2026-07-07 00:28 UTC | 38m |
| N9939Z |  | King Salmon Airport (PAKN) | King Salmon Airport (PAKN) | 2026-07-07 00:11 UTC | 2026-07-07 00:24 UTC | 13m |
| N9685G |  | Waukesha County Airport (KUES) | Lawrence J Timmerman Airport (KMWC) | 2026-07-06 23:49 UTC | 2026-07-07 00:23 UTC | 33m |
| N52168 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-07-06 22:43 UTC | 2026-07-07 00:22 UTC | 1h 39m |
| MRA633 | MRA | Durant Regional/Eaker Field (KDUA) | Mc Alester Regional Airport (KMLC) | 2026-07-06 23:55 UTC | 2026-07-07 00:19 UTC | 24m |
| N600CK |  | Madrid Barajas International Airport (LEMD) | Ibiza Airport (LEIB) | 2026-07-06 23:26 UTC | 2026-07-07 00:19 UTC | 52m |
| N532LB |  | Scottsdale Airport (KSDL) | Flagstaff Pulliam Airport (KFLG) | 2026-07-06 23:35 UTC | 2026-07-07 00:15 UTC | 39m |
| T73 |  | Ramona Airport (KRNM) | Ramona Airport (KRNM) | 2026-07-06 23:52 UTC | 2026-07-07 00:14 UTC | 21m |
| CKS464 | CKS | Ted Stevens Anchorage International Airport (PANC) | Yokota Air Base (RJTY) | 2026-07-06 17:44 UTC | 2026-07-07 00:13 UTC | 6h 29m |
| RAVN33 | RAV | Newcastle Airport (YWLM) | Bathurst Airport (YBTH) | 2026-07-06 23:48 UTC | 2026-07-07 00:13 UTC | 25m |
| FD627 |  | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-07-06 23:30 UTC | 2026-07-07 00:13 UTC | 42m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-06 23:29 UTC | 2026-07-07 00:10 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
