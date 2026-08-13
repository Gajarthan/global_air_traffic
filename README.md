# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_15:59:17_UTC-green)

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

**Latest saved flight:** 2026-08-13 15:59:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 15:59:17 UTC

- **192,572** saved flights
- **60,623** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **192,572** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,302,556.2 tonnes** estimated CO2 emissions
- **133,481,517 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7660 |
| 2 | SkyWest Airlines | 6944 |
| 3 | EJA | 3789 |
| 4 | IndiGo | 3338 |
| 5 | Southwest Airlines | 3001 |
| 6 | American Airlines | 2977 |
| 7 | ENY | 2382 |
| 8 | Delta Air Lines | 2270 |
| 9 | LATAM Airlines | 1809 |
| 10 | AZU | 1738 |
| 11 | Lufthansa | 1670 |
| 12 | Vueling | 1603 |
| 13 | WIF | 1595 |
| 14 | LXJ | 1514 |
| 15 | easyJet | 1327 |
| 16 | Swiss International | 1310 |
| 17 | AXM | 1258 |
| 18 | EJU | 1188 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1058 |
| 23 | GLO | 1035 |
| 24 | Air France | 1006 |
| 25 | PGT | 996 |
| 26 | AEE | 986 |
| 27 | CXK | 985 |
| 28 | United Airlines | 980 |
| 29 | WMT | 958 |
| 30 | Wizz Air | 957 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163810 |
| 2 | 🇪🇸 ES | 12423 |
| 3 | 🇧🇷 BR | 11068 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10545 |
| 6 | 🇮🇳 IN | 10453 |
| 7 | 🇮🇹 IT | 10019 |
| 8 | 🇩🇪 DE | 9538 |
| 9 | 🇬🇧 GB | 9013 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7702 |
| 12 | 🇨🇴 CO | 7442 |
| 13 | 🇬🇷 GR | 5635 |
| 14 | 🇲🇽 MX | 5438 |
| 15 | 🇨🇭 CH | 5189 |
| 16 | 🇹🇷 TR | 5176 |
| 17 | 🇳🇴 NO | 4946 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3258 |
| 20 | 🇵🇱 PL | 3181 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2443 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 1992 |
| 27 | 🇲🇦 MA | 1955 |
| 28 | 🇳🇱 NL | 1730 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3991 |
| 2 | Denver International Airport |  | US | 3149 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2384 |
| 5 | Indira Gandhi International Airport |  | IN | 2356 |
| 6 | Harry Reid International Airport |  | US | 2236 |
| 7 | Zurich Airport |  | CH | 2043 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2037 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1989 |
| 10 | La Aurora Airport |  | GT | 1877 |
| 11 | El Dorado International Airport |  | CO | 1746 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1732 |
| 13 | Salt Lake City International Airport |  | US | 1712 |
| 14 | Chicago O'Hare International Airport |  | US | 1684 |
| 15 | Frankfurt am Main International Airport |  | DE | 1634 |
| 16 | Congonhas Airport |  | BR | 1610 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1518 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1485 |
| 20 | Capua Airport |  | IT | 1484 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1419 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1383 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1330 |
| 25 | Charles de Gaulle International Airport |  | FR | 1321 |
| 26 | Charlotte/Douglas International Airport |  | US | 1280 |
| 27 | Bengaluru International Airport |  | IN | 1235 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1201 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1179 |
| 32 | Barcelona International Airport |  | ES | 1151 |
| 33 | Viracopos International Airport |  | BR | 1118 |
| 34 | Seattle-Tacoma International Airport |  | US | 1106 |
| 35 | Calgary International Airport |  | CA | 1100 |
| 36 | Reno/Tahoe International Airport |  | US | 1099 |
| 37 | Oslo Gardermoen Airport |  | NO | 1082 |
| 38 | Daniel K Inouye International Airport |  | US | 1079 |
| 39 | Tenerife Norte Airport |  | ES | 1057 |
| 40 | Vitoria/Foronda Airport |  | ES | 1052 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 985 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 707 | 21m | 244 km | 2,977.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 449 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 324 | 27m | 275 km | 1,535.3 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 311 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 287 | 44m | 241 km | 1,192.1 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 277 | 1h 49m | 1,423 km | 6,798.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 241 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 239 | 27m | 215 km | 885.2 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 235 | 19m | 99 km | 402.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 234 | 24m | 218 km | 881.6 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 209 | 28m | 152 km | 546.2 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU820 | ERU | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-08-13 15:44 UTC | 2026-08-13 15:59 UTC | 15m |
| N54466 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-08-13 15:22 UTC | 2026-08-13 15:52 UTC | 29m |
| N44413 |  | General Dick Stout Field (K1L8) | General Dick Stout Field (K1L8) | 2026-08-13 15:39 UTC | 2026-08-13 15:51 UTC | 12m |
| SPECK21 | SPE | Enix Airport (OK51) | Sopwith Ldg Airport (OK56) | 2026-08-13 15:37 UTC | 2026-08-13 15:50 UTC | 13m |
| HBSEW | HBS | Speck-Fehraltorf Airport (LSZK) | Speck-Fehraltorf Airport (LSZK) | 2026-08-13 15:05 UTC | 2026-08-13 15:50 UTC | 44m |
| CITT85 | CIT | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Kingman/Clyde Cessna Field (K9K8) | 2026-08-13 14:54 UTC | 2026-08-13 15:50 UTC | 55m |
| N1950F |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-13 15:26 UTC | 2026-08-13 15:49 UTC | 22m |
| SUBUO | SUB | HE13 (HE13) | HE13 (HE13) | 2026-08-13 15:21 UTC | 2026-08-13 15:48 UTC | 26m |
| OXF3274 | OXF | Falcon Field (KFFZ) | Phoenix Goodyear Airport (KGYR) | 2026-08-13 14:22 UTC | 2026-08-13 15:47 UTC | 1h 24m |
| N2068A |  | Stockton Metro Airport (KSCK) | Stockton Metro Airport (KSCK) | 2026-08-13 14:41 UTC | 2026-08-13 15:46 UTC | 1h 5m |
| SLICK92 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-08-13 15:26 UTC | 2026-08-13 15:46 UTC | 20m |
| N576JA |  | Savannah/Hilton Head International Airport (KSAV) | Wabash Municipal Airport (KIWH) | 2026-08-13 14:09 UTC | 2026-08-13 15:45 UTC | 1h 35m |
| DHTOC | DHT | Reichelsheim Airport (EDFB) | Reichelsheim Airport (EDFB) | 2026-08-13 14:42 UTC | 2026-08-13 15:42 UTC | 1h 0m |
| HBKLR | HBK | Lommis Airfield (LSZT) | Bad Ragaz Airport (LSZE) | 2026-08-13 13:36 UTC | 2026-08-13 15:40 UTC | 2h 3m |
| N384VR |  | Barkley Regional Airport (KPAH) | Barkley Regional Airport (KPAH) | 2026-08-13 15:21 UTC | 2026-08-13 15:35 UTC | 14m |
| N284V |  | Fort Worth Spinks Airport (KFWS) | Waco Regional Airport (KACT) | 2026-08-13 14:42 UTC | 2026-08-13 15:34 UTC | 51m |
| N381SB |  | Eveleigh Farms Airport (3KS4) | Leach Airport (K1V8) | 2026-08-13 14:47 UTC | 2026-08-13 15:32 UTC | 44m |
| N779AM |  | Montgomery-Gibbs Executive Airport (KMYF) | Osborne Airport (8CA0) | 2026-08-13 15:06 UTC | 2026-08-13 15:30 UTC | 23m |
| CONGO63 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-08-13 13:20 UTC | 2026-08-13 15:29 UTC | 2h 8m |
| EAI86W | EAI | Dublin Airport (EIDW) | Bristol International Airport (EGGD) | 2026-08-13 14:11 UTC | 2026-08-13 15:25 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
