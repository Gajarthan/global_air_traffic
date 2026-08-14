# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_20:44:52_UTC-green)

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

**Latest saved flight:** 2026-08-14 20:44:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 20:44:52 UTC

- **196,659** saved flights
- **61,738** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **196,659** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,348,658.6 tonnes** estimated CO2 emissions
- **136,154,125 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7821 |
| 2 | SkyWest Airlines | 7075 |
| 3 | EJA | 3878 |
| 4 | IndiGo | 3387 |
| 5 | Southwest Airlines | 3048 |
| 6 | American Airlines | 3041 |
| 7 | ENY | 2430 |
| 8 | Delta Air Lines | 2325 |
| 9 | LATAM Airlines | 1842 |
| 10 | AZU | 1777 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1643 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1561 |
| 15 | easyJet | 1353 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1277 |
| 18 | EJU | 1219 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1163 |
| 22 | VIV | 1082 |
| 23 | GLO | 1057 |
| 24 | Air France | 1034 |
| 25 | PGT | 1024 |
| 26 | AEE | 1010 |
| 27 | CXK | 1005 |
| 28 | United Airlines | 1004 |
| 29 | WMT | 985 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167271 |
| 2 | 🇪🇸 ES | 12707 |
| 3 | 🇧🇷 BR | 11294 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10770 |
| 6 | 🇮🇳 IN | 10589 |
| 7 | 🇮🇹 IT | 10249 |
| 8 | 🇩🇪 DE | 9766 |
| 9 | 🇬🇧 GB | 9244 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7838 |
| 12 | 🇨🇴 CO | 7727 |
| 13 | 🇬🇷 GR | 5780 |
| 14 | 🇲🇽 MX | 5562 |
| 15 | 🇹🇷 TR | 5358 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5040 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3246 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2511 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2061 |
| 27 | 🇲🇦 MA | 1991 |
| 28 | 🇳🇱 NL | 1769 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4093 |
| 2 | Denver International Airport |  | US | 3210 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2440 |
| 5 | Indira Gandhi International Airport |  | IN | 2392 |
| 6 | Harry Reid International Airport |  | US | 2260 |
| 7 | Zurich Airport |  | CH | 2079 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2078 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2036 |
| 10 | La Aurora Airport |  | GT | 1925 |
| 11 | El Dorado International Airport |  | CO | 1795 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1758 |
| 13 | Salt Lake City International Airport |  | US | 1747 |
| 14 | Chicago O'Hare International Airport |  | US | 1718 |
| 15 | Frankfurt am Main International Airport |  | DE | 1662 |
| 16 | Congonhas Airport |  | BR | 1644 |
| 17 | Madrid Barajas International Airport |  | ES | 1547 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1505 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1498 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1452 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1413 |
| 23 | Malpensa International Airport |  | IT | 1365 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1303 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1228 |
| 30 | Ninoy Aquino International Airport |  | PH | 1224 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1204 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1143 |
| 34 | Seattle-Tacoma International Airport |  | US | 1127 |
| 35 | Calgary International Airport |  | CA | 1118 |
| 36 | Reno/Tahoe International Airport |  | US | 1113 |
| 37 | Oslo Gardermoen Airport |  | NO | 1109 |
| 38 | Daniel K Inouye International Airport |  | US | 1092 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1076 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 720 | 21m | 244 km | 3,031.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 459 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 345 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 240 | 1h 15m | 961 km | 3,978.1 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 239 | 19m | 99 km | 409.4 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 237 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 232 | 1h 38m | 1,156 km | 4,628.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 214 | 28m | 152 km | 559.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FXC33 | FXC | Laconia Municipal Airport (KLCI) | Wychwood Field (CT48) | 2026-08-14 19:47 UTC | 2026-08-14 20:44 UTC | 57m |
| N76015 |  | Meadows Field (KBFL) | Van Nuys Airport (KVNY) | 2026-08-14 19:40 UTC | 2026-08-14 20:42 UTC | 1h 2m |
| HK5206G |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-14 20:23 UTC | 2026-08-14 20:42 UTC | 18m |
| N973KB |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-08-14 20:11 UTC | 2026-08-14 20:37 UTC | 25m |
| N104LU |  | Boca Raton Airport (KBCT) | Duda Airstrip (FA69) | 2026-08-14 20:08 UTC | 2026-08-14 20:35 UTC | 27m |
| N252CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-14 20:21 UTC | 2026-08-14 20:30 UTC | 9m |
| XSN90 | XSN | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-08-14 19:44 UTC | 2026-08-14 20:29 UTC | 45m |
| TOM7WL | TOM | Palma De Mallorca Airport (LEPA) | London Gatwick Airport (EGKK) | 2026-08-14 18:33 UTC | 2026-08-14 20:27 UTC | 1h 54m |
| TKR181 | TKR | Chico Regional Airport (KCIC) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-14 20:07 UTC | 2026-08-14 20:25 UTC | 18m |
| N733FN |  | Woodford Airpark (20VA) | Woodford Airpark (20VA) | 2026-08-14 20:18 UTC | 2026-08-14 20:24 UTC | 5m |
| TKR103 | TKR | Chico Regional Airport (KCIC) | Hayfork Airport (KF62) | 2026-08-14 20:09 UTC | 2026-08-14 20:23 UTC | 13m |
|  |  | P And R Field (ID26) | Chiloquin State Airport (K2S7) | 2026-08-14 19:30 UTC | 2026-08-14 20:22 UTC | 51m |
| N154LA |  | Centennial Airport (KAPA) | Lake County Airport (KLXV) | 2026-08-14 20:04 UTC | 2026-08-14 20:19 UTC | 15m |
| PAT820 | PAT | Sacramento Mather Airport (KMHR) | Reno/Tahoe International Airport (KRNO) | 2026-08-14 19:47 UTC | 2026-08-14 20:18 UTC | 30m |
| N11TE |  | Destin Executive Airport (KDTS) | Nashville International Airport (KBNA) | 2026-08-14 19:01 UTC | 2026-08-14 20:16 UTC | 1h 14m |
| N1882S |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-14 19:33 UTC | 2026-08-14 20:15 UTC | 42m |
| RPA3616 | Republic Airways | Chicago O'Hare International Airport (KORD) | Harrow Airport (CGL2) | 2026-08-14 19:18 UTC | 2026-08-14 20:15 UTC | 57m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-14 19:25 UTC | 2026-08-14 20:15 UTC | 50m |
| TKR164 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Big Muddy Ranch Airport (2OR1) | 2026-08-14 20:05 UTC | 2026-08-14 20:15 UTC | 9m |
| IGO071 | IndiGo | Indira Gandhi International Airport (VIDP) | Shaibah Airport (OESB) | 2026-08-14 17:01 UTC | 2026-08-14 20:12 UTC | 3h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
