# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_15:34:25_UTC-green)

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

**Latest saved flight:** 2026-08-14 15:34:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 15:34:25 UTC

- **195,529** saved flights
- **61,463** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,529** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,336,104.0 tonnes** estimated CO2 emissions
- **135,426,317 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7779 |
| 2 | SkyWest Airlines | 7021 |
| 3 | EJA | 3842 |
| 4 | IndiGo | 3373 |
| 5 | Southwest Airlines | 3034 |
| 6 | American Airlines | 3019 |
| 7 | ENY | 2412 |
| 8 | Delta Air Lines | 2302 |
| 9 | LATAM Airlines | 1833 |
| 10 | AZU | 1762 |
| 11 | Lufthansa | 1692 |
| 12 | Vueling | 1632 |
| 13 | WIF | 1619 |
| 14 | LXJ | 1548 |
| 15 | easyJet | 1348 |
| 16 | Swiss International | 1324 |
| 17 | AXM | 1277 |
| 18 | EJU | 1210 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1074 |
| 23 | GLO | 1053 |
| 24 | Air France | 1028 |
| 25 | PGT | 1017 |
| 26 | AEE | 1004 |
| 27 | United Airlines | 996 |
| 28 | CXK | 995 |
| 29 | WMT | 980 |
| 30 | Wizz Air | 968 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 166112 |
| 2 | 🇪🇸 ES | 12630 |
| 3 | 🇧🇷 BR | 11231 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10681 |
| 6 | 🇮🇳 IN | 10557 |
| 7 | 🇮🇹 IT | 10178 |
| 8 | 🇩🇪 DE | 9728 |
| 9 | 🇬🇧 GB | 9207 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7808 |
| 12 | 🇨🇴 CO | 7618 |
| 13 | 🇬🇷 GR | 5750 |
| 14 | 🇲🇽 MX | 5519 |
| 15 | 🇹🇷 TR | 5307 |
| 16 | 🇨🇭 CH | 5300 |
| 17 | 🇳🇴 NO | 5017 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3308 |
| 20 | 🇵🇱 PL | 3232 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2476 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2038 |
| 27 | 🇲🇦 MA | 1983 |
| 28 | 🇳🇱 NL | 1764 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4059 |
| 2 | Denver International Airport |  | US | 3187 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2422 |
| 5 | Indira Gandhi International Airport |  | IN | 2383 |
| 6 | Harry Reid International Airport |  | US | 2254 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2069 |
| 8 | Zurich Airport |  | CH | 2069 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2019 |
| 10 | La Aurora Airport |  | GT | 1902 |
| 11 | El Dorado International Airport |  | CO | 1781 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1738 |
| 14 | Chicago O'Hare International Airport |  | US | 1704 |
| 15 | Frankfurt am Main International Airport |  | DE | 1657 |
| 16 | Congonhas Airport |  | BR | 1633 |
| 17 | Madrid Barajas International Airport |  | ES | 1541 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1497 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1495 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1438 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1406 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1354 |
| 25 | Charles de Gaulle International Airport |  | FR | 1342 |
| 26 | Charlotte/Douglas International Airport |  | US | 1296 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1242 |
| 29 | Ninoy Aquino International Airport |  | PH | 1224 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1218 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1175 |
| 33 | Viracopos International Airport |  | BR | 1135 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1113 |
| 36 | Reno/Tahoe International Airport |  | US | 1107 |
| 37 | Oslo Gardermoen Airport |  | NO | 1103 |
| 38 | Daniel K Inouye International Airport |  | US | 1087 |
| 39 | Vitoria/Foronda Airport |  | ES | 1073 |
| 40 | Tenerife Norte Airport |  | ES | 1071 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1000 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 715 | 21m | 244 km | 3,010.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 326 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 293 | 44m | 241 km | 1,217.1 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 281 | 1h 49m | 1,423 km | 6,896.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 278 | 22m | 55 km | 264.2 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 243 | 27m | 215 km | 900.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 241 | 24m | 218 km | 907.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 230 | 1h 38m | 1,156 km | 4,588.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 212 | 1h 3m | 695 km | 2,541.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6697D |  | Pickens County Airport (KJZP) | Pickens County Airport (KJZP) | 2026-08-14 15:09 UTC | 2026-08-14 15:34 UTC | 25m |
| GRZLY05 | GRZ | Brussels Airport (EBBR) | Melsbroek Air Base (EBMB) | 2026-08-14 13:47 UTC | 2026-08-14 15:31 UTC | 1h 44m |
| CXK520 | CXK | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-08-14 15:13 UTC | 2026-08-14 15:30 UTC | 16m |
| CAP4227 | CAP | Easterwood Field (KCLL) | Easterwood Field (KCLL) | 2026-08-14 15:02 UTC | 2026-08-14 15:30 UTC | 28m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-14 15:09 UTC | 2026-08-14 15:26 UTC | 17m |
| N48ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-14 15:09 UTC | 2026-08-14 15:25 UTC | 16m |
| UFX63 | UFX | Humberside Airport (EGNJ) | Blackpool International Airport (EGNH) | 2026-08-14 13:39 UTC | 2026-08-14 15:22 UTC | 1h 43m |
| DLH2PP | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-08-14 14:47 UTC | 2026-08-14 15:21 UTC | 33m |
| N888UH |  | Scottsdale Airport (KSDL) | Phoenix Deer Valley Airport (KDVT) | 2026-08-14 15:09 UTC | 2026-08-14 15:21 UTC | 11m |
| GPD828 | GPD | Teterboro Airport (KTEB) | Lehigh Valley International Airport (KABE) | 2026-08-14 14:53 UTC | 2026-08-14 15:19 UTC | 26m |
| WING57 | WIN | Ozark/Blackwell Field (K71J) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-14 14:10 UTC | 2026-08-14 15:18 UTC | 1h 7m |
| N4745L |  | Easton/Newnam Field (KESN) | Msm Airport (PS50) | 2026-08-14 13:26 UTC | 2026-08-14 15:15 UTC | 1h 49m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-14 14:52 UTC | 2026-08-14 15:14 UTC | 22m |
| HB2100 |  | Muenster Aero Airport (LSPU) | Samedan Airport (LSZS) | 2026-08-14 13:14 UTC | 2026-08-14 15:10 UTC | 1h 55m |
| N423BB |  | Aurora State Airport (KUAO) | Pangborn Memorial Airport (KEAT) | 2026-08-14 14:39 UTC | 2026-08-14 15:09 UTC | 30m |
| N116UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-14 14:38 UTC | 2026-08-14 15:08 UTC | 29m |
| N1910R |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-14 14:36 UTC | 2026-08-14 15:07 UTC | 31m |
| TGJAK | TGJ | La Retama Southwest Airport (MM17) | Hughes Ranch Airport (50XS) | 2026-08-14 13:28 UTC | 2026-08-14 15:06 UTC | 1h 38m |
| CXK437 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Santa Barbara Municipal Airport (KSBA) | 2026-08-14 14:13 UTC | 2026-08-14 15:06 UTC | 53m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-14 14:43 UTC | 2026-08-14 15:03 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
