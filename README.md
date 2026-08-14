# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_17:23:44_UTC-green)

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

**Latest saved flight:** 2026-08-14 17:23:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 17:23:44 UTC

- **195,914** saved flights
- **61,556** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,914** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,339,506.4 tonnes** estimated CO2 emissions
- **135,623,561 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7793 |
| 2 | SkyWest Airlines | 7032 |
| 3 | EJA | 3856 |
| 4 | IndiGo | 3381 |
| 5 | Southwest Airlines | 3039 |
| 6 | American Airlines | 3024 |
| 7 | ENY | 2418 |
| 8 | Delta Air Lines | 2310 |
| 9 | LATAM Airlines | 1836 |
| 10 | AZU | 1764 |
| 11 | Lufthansa | 1694 |
| 12 | Vueling | 1635 |
| 13 | WIF | 1623 |
| 14 | LXJ | 1550 |
| 15 | easyJet | 1348 |
| 16 | Swiss International | 1325 |
| 17 | AXM | 1277 |
| 18 | EJU | 1211 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1076 |
| 23 | GLO | 1055 |
| 24 | Air France | 1034 |
| 25 | PGT | 1019 |
| 26 | AEE | 1007 |
| 27 | CXK | 1001 |
| 28 | United Airlines | 997 |
| 29 | WMT | 981 |
| 30 | Wizz Air | 969 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 166481 |
| 2 | 🇪🇸 ES | 12657 |
| 3 | 🇧🇷 BR | 11247 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10707 |
| 6 | 🇮🇳 IN | 10577 |
| 7 | 🇮🇹 IT | 10201 |
| 8 | 🇩🇪 DE | 9744 |
| 9 | 🇬🇧 GB | 9216 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7822 |
| 12 | 🇨🇴 CO | 7651 |
| 13 | 🇬🇷 GR | 5764 |
| 14 | 🇲🇽 MX | 5533 |
| 15 | 🇹🇷 TR | 5323 |
| 16 | 🇨🇭 CH | 5307 |
| 17 | 🇳🇴 NO | 5028 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3237 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2492 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2046 |
| 27 | 🇲🇦 MA | 1985 |
| 28 | 🇳🇱 NL | 1766 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4069 |
| 2 | Denver International Airport |  | US | 3192 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2429 |
| 5 | Indira Gandhi International Airport |  | IN | 2387 |
| 6 | Harry Reid International Airport |  | US | 2255 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2073 |
| 8 | Zurich Airport |  | CH | 2072 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2024 |
| 10 | La Aurora Airport |  | GT | 1913 |
| 11 | El Dorado International Airport |  | CO | 1786 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1747 |
| 13 | Salt Lake City International Airport |  | US | 1739 |
| 14 | Chicago O'Hare International Airport |  | US | 1707 |
| 15 | Frankfurt am Main International Airport |  | DE | 1660 |
| 16 | Congonhas Airport |  | BR | 1638 |
| 17 | Madrid Barajas International Airport |  | ES | 1544 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1499 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1496 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1442 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1407 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1356 |
| 25 | Charles de Gaulle International Airport |  | FR | 1349 |
| 26 | Charlotte/Douglas International Airport |  | US | 1298 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1243 |
| 29 | Ninoy Aquino International Airport |  | PH | 1224 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1221 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1198 |
| 32 | Barcelona International Airport |  | ES | 1177 |
| 33 | Viracopos International Airport |  | BR | 1136 |
| 34 | Seattle-Tacoma International Airport |  | US | 1123 |
| 35 | Calgary International Airport |  | CA | 1113 |
| 36 | Reno/Tahoe International Airport |  | US | 1109 |
| 37 | Oslo Gardermoen Airport |  | NO | 1106 |
| 38 | Daniel K Inouye International Airport |  | US | 1088 |
| 39 | Vitoria/Foronda Airport |  | ES | 1077 |
| 40 | Tenerife Norte Airport |  | ES | 1071 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1003 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 716 | 21m | 244 km | 3,014.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 457 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 7 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 331 | 8m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 294 | 44m | 241 km | 1,221.2 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 282 | 1h 49m | 1,423 km | 6,920.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 279 | 22m | 55 km | 265.2 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 238 | 1h 15m | 961 km | 3,945.0 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 237 | 19m | 99 km | 406.0 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 231 | 1h 38m | 1,156 km | 4,608.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 230 | 19m | 144 km | 572.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 213 | 28m | 152 km | 556.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EPI187 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | St Augustine Airport (KSGJ) | 2026-08-14 16:39 UTC | 2026-08-14 17:23 UTC | 43m |
| N708LA |  | Northeast Philadelphia Airport (KPNE) | Wings Field (KLOM) | 2026-08-14 16:55 UTC | 2026-08-14 17:23 UTC | 28m |
| N71286 |  | Princeton Airport (K39N) | Ocean County Airport (KMJX) | 2026-08-14 16:39 UTC | 2026-08-14 17:19 UTC | 40m |
| N998RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-14 16:47 UTC | 2026-08-14 17:17 UTC | 29m |
| N929CH |  | Centennial Airport (KAPA) | Metrogro Farm Airport (CO25) | 2026-08-14 16:53 UTC | 2026-08-14 17:12 UTC | 18m |
| N4347R |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-14 16:38 UTC | 2026-08-14 17:11 UTC | 33m |
| DAH3017 | DAH | Istanbul Airport (LTFM) | Houari Boumediene Airport (DAAG) | 2026-08-14 14:08 UTC | 2026-08-14 17:06 UTC | 2h 58m |
| RN096 |  | Chilton County Airport (K02A) | South Alabama Regional At Bill Benton Field (K79J) | 2026-08-14 16:40 UTC | 2026-08-14 17:06 UTC | 26m |
| N415AE |  | Majors Airport (KGVT) | 01TE (01TE) | 2026-08-14 16:37 UTC | 2026-08-14 17:03 UTC | 25m |
| HLE27 | HLE | London Biggin Hill Airport (EGKB) | London City Airport (EGLC) | 2026-08-14 16:54 UTC | 2026-08-14 17:00 UTC | 6m |
|  |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-14 16:59 UTC | 2026-08-14 16:59 UTC | 0m |
| ABY625 | ABY | Cairo International Airport (HECA) | Sirri Island Airport (OIBS) | 2026-08-14 14:12 UTC | 2026-08-14 16:57 UTC | 2h 45m |
| N168Y |  | Modesto City-County-Harry Sham Field (KMOD) | Tracy Municipal Airport (KTCY) | 2026-08-14 16:40 UTC | 2026-08-14 16:56 UTC | 15m |
| SAS221 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Kristiansand Airport (ENCN) | 2026-08-14 16:17 UTC | 2026-08-14 16:56 UTC | 39m |
| ASY679 | ASY | Eglin Aux Field 6 Airport (FL34) | Hurlburt Field (KHRT) | 2026-08-14 16:40 UTC | 2026-08-14 16:56 UTC | 15m |
| N118RF |  | Sacramento Mather Airport (KMHR) | Amedee Army Air Field (KAHC) | 2026-08-14 16:08 UTC | 2026-08-14 16:55 UTC | 47m |
| N566FF |  | Glenwood Municipal Airport (KGHW) | 59NE (59NE) | 2026-08-14 15:46 UTC | 2026-08-14 16:53 UTC | 1h 6m |
| OMBHG | OMB | Zilina Airport (LZZI) | Zilina Airport (LZZI) | 2026-08-14 16:23 UTC | 2026-08-14 16:52 UTC | 29m |
| MAO3 | MAO | Albert Lea Municipal Airport (KAEL) | Mankato Regional Airport (KMKT) | 2026-08-14 16:37 UTC | 2026-08-14 16:52 UTC | 15m |
| N441UC |  | Martha's Vineyard Airport (KMVY) | 97NY (97NY) | 2026-08-14 16:04 UTC | 2026-08-14 16:52 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
