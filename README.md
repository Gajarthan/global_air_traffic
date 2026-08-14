# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_16:37:02_UTC-green)

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

**Latest saved flight:** 2026-08-14 16:37:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 16:37:02 UTC

- **195,715** saved flights
- **61,507** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,715** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,337,584.2 tonnes** estimated CO2 emissions
- **135,512,126 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7785 |
| 2 | SkyWest Airlines | 7028 |
| 3 | EJA | 3850 |
| 4 | IndiGo | 3376 |
| 5 | Southwest Airlines | 3035 |
| 6 | American Airlines | 3023 |
| 7 | ENY | 2416 |
| 8 | Delta Air Lines | 2306 |
| 9 | LATAM Airlines | 1836 |
| 10 | AZU | 1763 |
| 11 | Lufthansa | 1692 |
| 12 | Vueling | 1633 |
| 13 | WIF | 1621 |
| 14 | LXJ | 1550 |
| 15 | easyJet | 1348 |
| 16 | Swiss International | 1324 |
| 17 | AXM | 1277 |
| 18 | EJU | 1210 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1075 |
| 23 | GLO | 1054 |
| 24 | Air France | 1028 |
| 25 | PGT | 1019 |
| 26 | AEE | 1005 |
| 27 | CXK | 998 |
| 28 | United Airlines | 996 |
| 29 | WMT | 980 |
| 30 | Wizz Air | 968 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 166284 |
| 2 | 🇪🇸 ES | 12642 |
| 3 | 🇧🇷 BR | 11243 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10697 |
| 6 | 🇮🇳 IN | 10565 |
| 7 | 🇮🇹 IT | 10191 |
| 8 | 🇩🇪 DE | 9737 |
| 9 | 🇬🇧 GB | 9210 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7810 |
| 12 | 🇨🇴 CO | 7639 |
| 13 | 🇬🇷 GR | 5755 |
| 14 | 🇲🇽 MX | 5523 |
| 15 | 🇹🇷 TR | 5311 |
| 16 | 🇨🇭 CH | 5306 |
| 17 | 🇳🇴 NO | 5021 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3316 |
| 20 | 🇵🇱 PL | 3235 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2485 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2043 |
| 27 | 🇲🇦 MA | 1983 |
| 28 | 🇳🇱 NL | 1764 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4064 |
| 2 | Denver International Airport |  | US | 3189 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2429 |
| 5 | Indira Gandhi International Airport |  | IN | 2385 |
| 6 | Harry Reid International Airport |  | US | 2254 |
| 7 | Zurich Airport |  | CH | 2071 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2070 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2023 |
| 10 | La Aurora Airport |  | GT | 1909 |
| 11 | El Dorado International Airport |  | CO | 1785 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1738 |
| 14 | Chicago O'Hare International Airport |  | US | 1707 |
| 15 | Frankfurt am Main International Airport |  | DE | 1658 |
| 16 | Congonhas Airport |  | BR | 1636 |
| 17 | Madrid Barajas International Airport |  | ES | 1543 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1497 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1496 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1440 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1407 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1356 |
| 25 | Charles de Gaulle International Airport |  | FR | 1343 |
| 26 | Charlotte/Douglas International Airport |  | US | 1296 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1243 |
| 29 | Ninoy Aquino International Airport |  | PH | 1224 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1218 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1198 |
| 32 | Barcelona International Airport |  | ES | 1176 |
| 33 | Viracopos International Airport |  | BR | 1136 |
| 34 | Seattle-Tacoma International Airport |  | US | 1122 |
| 35 | Calgary International Airport |  | CA | 1113 |
| 36 | Reno/Tahoe International Airport |  | US | 1107 |
| 37 | Oslo Gardermoen Airport |  | NO | 1104 |
| 38 | Daniel K Inouye International Airport |  | US | 1088 |
| 39 | Vitoria/Foronda Airport |  | ES | 1074 |
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
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 327 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 294 | 44m | 241 km | 1,221.2 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 282 | 1h 49m | 1,423 km | 6,920.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 278 | 22m | 55 km | 264.2 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 244 | 26m | 215 km | 903.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 238 | 1h 15m | 961 km | 3,945.0 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 237 | 19m | 99 km | 406.0 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 231 | 1h 38m | 1,156 km | 4,608.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 213 | 28m | 152 km | 556.6 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 212 | 1h 3m | 695 km | 2,541.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-14 15:54 UTC | 2026-08-14 16:37 UTC | 42m |
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-14 14:19 UTC | 2026-08-14 16:26 UTC | 2h 7m |
| RGA10 | RGA | Reichenbach Air Base (LSGR) | Meiringen Airport (LSMM) | 2026-08-14 15:44 UTC | 2026-08-14 16:26 UTC | 42m |
| N208W |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-08-14 16:01 UTC | 2026-08-14 16:25 UTC | 23m |
| N13DA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-14 15:46 UTC | 2026-08-14 16:22 UTC | 36m |
| LNX06AR | LNX | Aberdeen Dyce Airport (EGPD) | Newcastle Airport (EGNT) | 2026-08-14 15:51 UTC | 2026-08-14 16:22 UTC | 31m |
| CXK372 | CXK | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-08-14 15:23 UTC | 2026-08-14 16:22 UTC | 58m |
| HK4472 |  | Enrique Olaya Herrera Airport (SKMD) | Guaymaral Airport (SKGY) | 2026-08-14 15:20 UTC | 2026-08-14 16:19 UTC | 59m |
| N423LL |  | Herr Brothers Airport (NJ95) | Jugtown Mountain Airport (2NJ1) | 2026-08-14 15:56 UTC | 2026-08-14 16:17 UTC | 21m |
| EGE93 | EGE | Danbury Municipal Airport (KDXR) | 2NK7 (2NK7) | 2026-08-14 15:57 UTC | 2026-08-14 16:16 UTC | 19m |
| LFA324 | LFA | Vero Beach Regional Airport (KVRB) | Space Coast Regional Airport (KTIX) | 2026-08-14 15:34 UTC | 2026-08-14 16:09 UTC | 35m |
| N3038N |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-14 15:22 UTC | 2026-08-14 16:07 UTC | 44m |
| N3641R |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-08-14 15:10 UTC | 2026-08-14 16:06 UTC | 56m |
| N464RB |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-14 15:47 UTC | 2026-08-14 16:06 UTC | 18m |
| N353KM |  | San Luis Obispo County Regional Airport (KSBP) | Truckee-Tahoe Airport (KTRK) | 2026-08-14 15:09 UTC | 2026-08-14 16:06 UTC | 57m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-14 15:52 UTC | 2026-08-14 16:06 UTC | 14m |
| ZSTGI | ZST | Wonderboom Airport (FAWB) | Wonderboom Airport (FAWB) | 2026-08-14 16:02 UTC | 2026-08-14 16:03 UTC | 0m |
| CGTEP | CGT | Brampton Airport (CNC3) | Billy Bishop Toronto City Airport (CYTZ) | 2026-08-14 15:37 UTC | 2026-08-14 16:02 UTC | 25m |
| CGHAP | CGH | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-08-14 15:34 UTC | 2026-08-14 16:01 UTC | 27m |
| N1MY |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-14 15:39 UTC | 2026-08-14 16:00 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
