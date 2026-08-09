# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_22:28:37_UTC-green)

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

**Latest saved flight:** 2026-08-09 22:28:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 22:28:37 UTC

- **182,860** saved flights
- **58,374** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,860** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,198,136.3 tonnes** estimated CO2 emissions
- **127,428,193 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7260 |
| 2 | SkyWest Airlines | 6657 |
| 3 | EJA | 3618 |
| 4 | IndiGo | 3195 |
| 5 | Southwest Airlines | 2868 |
| 6 | American Airlines | 2857 |
| 7 | ENY | 2280 |
| 8 | Delta Air Lines | 2167 |
| 9 | LATAM Airlines | 1711 |
| 10 | AZU | 1640 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1508 |
| 14 | LXJ | 1445 |
| 15 | easyJet | 1254 |
| 16 | Swiss International | 1252 |
| 17 | AXM | 1226 |
| 18 | EJU | 1124 |
| 19 | QLK | 1117 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1099 |
| 22 | VIV | 1006 |
| 23 | GLO | 982 |
| 24 | AEE | 954 |
| 25 | CXK | 953 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 925 |
| 30 | MXY | 914 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156529 |
| 2 | 🇪🇸 ES | 11750 |
| 3 | 🇧🇷 BR | 10510 |
| 4 | 🇦🇺 AU | 10205 |
| 5 | 🇮🇳 IN | 10009 |
| 6 | 🇨🇦 CA | 9957 |
| 7 | 🇮🇹 IT | 9470 |
| 8 | 🇩🇪 DE | 9053 |
| 9 | 🇬🇧 GB | 8479 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7283 |
| 12 | 🇨🇴 CO | 6848 |
| 13 | 🇬🇷 GR | 5361 |
| 14 | 🇲🇽 MX | 5226 |
| 15 | 🇨🇭 CH | 4879 |
| 16 | 🇹🇷 TR | 4747 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3064 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2412 |
| 24 | 🇬🇹 GT | 2345 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1850 |
| 27 | 🇭🇷 HR | 1827 |
| 28 | 🇲🇪 ME | 1651 |
| 29 | 🇳🇱 NL | 1643 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3792 |
| 2 | Denver International Airport |  | US | 3024 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2142 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1962 |
| 8 | Zurich Airport |  | CH | 1953 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1902 |
| 10 | La Aurora Airport |  | GT | 1799 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1668 |
| 12 | El Dorado International Airport |  | CO | 1642 |
| 13 | Chicago O'Hare International Airport |  | US | 1635 |
| 14 | Salt Lake City International Airport |  | US | 1634 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1525 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1447 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1434 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1367 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1309 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1265 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1242 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1142 |
| 30 | Ninoy Aquino International Airport |  | PH | 1136 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1119 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Viracopos International Airport |  | BR | 1051 |
| 34 | Seattle-Tacoma International Airport |  | US | 1051 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1043 |
| 37 | Calgary International Airport |  | CA | 1041 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 999 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 671 | 21m | 244 km | 2,825.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 425 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 253 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 225 | 19m | 99 km | 385.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 223 | 1h 15m | 961 km | 3,696.3 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 222 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 199 | 1h 1m | 695 km | 2,385.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N115GK |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-09 21:59 UTC | 2026-08-09 22:28 UTC | 29m |
| N1018B |  | Johnson Airport (3AK4) | Johnson Airport (3AK4) | 2026-08-09 21:53 UTC | 2026-08-09 22:25 UTC | 32m |
| N294NG |  | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-09 22:06 UTC | 2026-08-09 22:24 UTC | 17m |
| EJA906 | EJA | Vancouver International Airport (CYVR) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-09 18:05 UTC | 2026-08-09 22:23 UTC | 4h 17m |
| BNL304 | BNL | Istanbul Airport (LTFM) | Benina International Airport (HLLB) | 2026-08-09 20:38 UTC | 2026-08-09 22:22 UTC | 1h 44m |
| XAEKT | XAE | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-08-09 22:09 UTC | 2026-08-09 22:22 UTC | 12m |
| N19333 |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-08-09 21:36 UTC | 2026-08-09 22:13 UTC | 37m |
| N198AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-09 19:21 UTC | 2026-08-09 22:11 UTC | 2h 49m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-09 21:54 UTC | 2026-08-09 22:06 UTC | 12m |
| N914WB |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-09 21:38 UTC | 2026-08-09 22:03 UTC | 24m |
| N7244E |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-09 21:45 UTC | 2026-08-09 22:02 UTC | 17m |
| FTO382 | FTO | Westmoreland Airport (49NY) | John F Kennedy International Airport (KJFK) | 2026-08-09 21:26 UTC | 2026-08-09 22:01 UTC | 34m |
| N405CM |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-09 21:45 UTC | 2026-08-09 22:00 UTC | 15m |
| N821MV |  | Fort Worth Meacham International Airport (KFTW) | Telluride Regional Airport (KTEX) | 2026-08-09 20:23 UTC | 2026-08-09 21:59 UTC | 1h 36m |
| N383TA |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-09 21:20 UTC | 2026-08-09 21:56 UTC | 35m |
| N1314T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-09 19:17 UTC | 2026-08-09 21:53 UTC | 2h 35m |
| N877PM |  | Austin Executive Airport (KEDC) | Southland Field (KUXL) | 2026-08-09 21:04 UTC | 2026-08-09 21:52 UTC | 47m |
| N901ST |  | Rochelle Municipal/Koritz Field (KRPJ) | Rochelle Municipal/Koritz Field (KRPJ) | 2026-08-09 21:11 UTC | 2026-08-09 21:50 UTC | 39m |
| N255DW |  | Billy Joe Airport (37CA) | Yolo Ranch Airport (33AZ) | 2026-08-09 20:50 UTC | 2026-08-09 21:50 UTC | 1h 0m |
| CFG4105 | CFG | Frankfurt am Main International Airport (EDDF) | HE42 (HE42) | 2026-08-09 18:23 UTC | 2026-08-09 21:45 UTC | 3h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
