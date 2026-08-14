# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_22:16:31_UTC-green)

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

**Latest saved flight:** 2026-08-14 22:16:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 22:16:31 UTC

- **196,916** saved flights
- **61,805** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **196,916** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,351,540.2 tonnes** estimated CO2 emissions
- **136,321,170 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7834 |
| 2 | SkyWest Airlines | 7090 |
| 3 | EJA | 3884 |
| 4 | IndiGo | 3387 |
| 5 | Southwest Airlines | 3052 |
| 6 | American Airlines | 3047 |
| 7 | ENY | 2434 |
| 8 | Delta Air Lines | 2327 |
| 9 | LATAM Airlines | 1845 |
| 10 | AZU | 1782 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1565 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1277 |
| 18 | EJU | 1222 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1165 |
| 22 | VIV | 1085 |
| 23 | GLO | 1063 |
| 24 | Air France | 1034 |
| 25 | PGT | 1025 |
| 26 | AEE | 1010 |
| 27 | CXK | 1005 |
| 28 | United Airlines | 1005 |
| 29 | WMT | 986 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167540 |
| 2 | 🇪🇸 ES | 12716 |
| 3 | 🇧🇷 BR | 11329 |
| 4 | 🇦🇺 AU | 11013 |
| 5 | 🇨🇦 CA | 10790 |
| 6 | 🇮🇳 IN | 10589 |
| 7 | 🇮🇹 IT | 10266 |
| 8 | 🇩🇪 DE | 9769 |
| 9 | 🇬🇧 GB | 9251 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7843 |
| 12 | 🇨🇴 CO | 7762 |
| 13 | 🇬🇷 GR | 5782 |
| 14 | 🇲🇽 MX | 5572 |
| 15 | 🇹🇷 TR | 5367 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5041 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3251 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2743 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2518 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4101 |
| 2 | Denver International Airport |  | US | 3211 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2442 |
| 5 | Indira Gandhi International Airport |  | IN | 2392 |
| 6 | Harry Reid International Airport |  | US | 2262 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2079 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2039 |
| 10 | La Aurora Airport |  | GT | 1930 |
| 11 | El Dorado International Airport |  | CO | 1802 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1761 |
| 13 | Salt Lake City International Airport |  | US | 1752 |
| 14 | Chicago O'Hare International Airport |  | US | 1725 |
| 15 | Frankfurt am Main International Airport |  | DE | 1663 |
| 16 | Congonhas Airport |  | BR | 1653 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1505 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1502 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1452 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1417 |
| 23 | Malpensa International Airport |  | IT | 1368 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1304 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1229 |
| 30 | Ninoy Aquino International Airport |  | PH | 1224 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1206 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1145 |
| 34 | Seattle-Tacoma International Airport |  | US | 1129 |
| 35 | Calgary International Airport |  | CA | 1120 |
| 36 | Reno/Tahoe International Airport |  | US | 1114 |
| 37 | Oslo Gardermoen Airport |  | NO | 1110 |
| 38 | Daniel K Inouye International Airport |  | US | 1093 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 721 | 21m | 244 km | 3,035.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 460 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 351 | 8m | - | - |
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
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 240 | 19m | 99 km | 411.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 232 | 1h 38m | 1,156 km | 4,628.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-14 22:03 UTC | 2026-08-14 22:16 UTC | 13m |
| N76SJ |  | Santa Barbara Municipal Airport (KSBA) | Santa Barbara Municipal Airport (KSBA) | 2026-08-14 21:49 UTC | 2026-08-14 22:16 UTC | 27m |
| N6QT |  | Skwentna Airport (PASW) | Merrill Field (PAMR) | 2026-08-14 21:42 UTC | 2026-08-14 22:14 UTC | 31m |
| MAFFS4 | MAF | Lonnie Pool Field/Weaverville Airport (KO54) | Redding Regional Airport (KRDD) | 2026-08-14 22:00 UTC | 2026-08-14 22:10 UTC | 10m |
| N916SY |  | Long Beach (Daugherty Field) Airport (KLGB) | Scottsdale Airport (KSDL) | 2026-08-14 20:06 UTC | 2026-08-14 22:10 UTC | 2h 4m |
| N85JA |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-08-14 21:46 UTC | 2026-08-14 22:01 UTC | 14m |
| HK3522 |  | Matecana International Airport (SKPE) | Guaymaral Airport (SKGY) | 2026-08-14 20:53 UTC | 2026-08-14 21:52 UTC | 59m |
| N711WK |  | Olbia / Costa Smeralda Airport (LIEO) | Bangor International Airport (KBGR) | 2026-08-14 14:14 UTC | 2026-08-14 21:52 UTC | 7h 37m |
| TKR160 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Big Muddy Ranch Airport (2OR1) | 2026-08-14 21:40 UTC | 2026-08-14 21:51 UTC | 10m |
| N63UD |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-08-14 20:55 UTC | 2026-08-14 21:50 UTC | 54m |
| FXC44 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Laguardia Airport (KLGA) | 2026-08-14 21:30 UTC | 2026-08-14 21:50 UTC | 20m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-14 21:34 UTC | 2026-08-14 21:49 UTC | 15m |
| DICEY92 | DIC | 4XA5 (4XA5) | Pleasant Valley Airport (07OK) | 2026-08-14 21:11 UTC | 2026-08-14 21:48 UTC | 37m |
| N213PF |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-14 20:23 UTC | 2026-08-14 21:48 UTC | 1h 25m |
| PRVNZ | PRV | Fazenda Santa Rita de Cassia Airport (SWEZ) | Fazenda Guanabara Airport (SWGZ) | 2026-08-14 21:34 UTC | 2026-08-14 21:48 UTC | 14m |
| N73671 |  | Tracy Municipal Airport (KTCY) | Lodi Airport (K1O3) | 2026-08-14 21:27 UTC | 2026-08-14 21:47 UTC | 20m |
| N500JR |  | Jacqueline Cochran Regional Airport (KTRM) | Glendale Regional Airport (KGEU) | 2026-08-14 20:45 UTC | 2026-08-14 21:46 UTC | 1h 0m |
| N215DA |  | Dallas Love Field (KDAL) | Harris River Ranch Airport (9CA7) | 2026-08-14 19:05 UTC | 2026-08-14 21:46 UTC | 2h 40m |
| TKK183 | TKK | Roberts Field/Redmond Municipal Airport (KRDM) | Big Muddy Ranch Airport (2OR1) | 2026-08-14 21:34 UTC | 2026-08-14 21:44 UTC | 9m |
| N454RM |  | Roberts Field/Redmond Municipal Airport (KRDM) | OG12 (OG12) | 2026-08-14 21:34 UTC | 2026-08-14 21:41 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
