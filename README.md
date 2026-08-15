# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_17:45:52_UTC-green)

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

**Latest saved flight:** 2026-08-15 17:45:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 17:45:52 UTC

- **199,303** saved flights
- **62,252** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,380,370.5 tonnes** estimated CO2 emissions
- **137,992,491 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7932 |
| 2 | SkyWest Airlines | 7138 |
| 3 | EJA | 3911 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3082 |
| 6 | American Airlines | 3061 |
| 7 | ENY | 2456 |
| 8 | Delta Air Lines | 2357 |
| 9 | LATAM Airlines | 1875 |
| 10 | AZU | 1812 |
| 11 | Lufthansa | 1704 |
| 12 | Vueling | 1676 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1581 |
| 15 | easyJet | 1367 |
| 16 | Swiss International | 1346 |
| 17 | AXM | 1308 |
| 18 | EJU | 1234 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1100 |
| 23 | GLO | 1085 |
| 24 | Air France | 1057 |
| 25 | PGT | 1051 |
| 26 | AEE | 1028 |
| 27 | United Airlines | 1010 |
| 28 | CXK | 1009 |
| 29 | WMT | 1006 |
| 30 | Wizz Air | 986 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168864 |
| 2 | 🇪🇸 ES | 12880 |
| 3 | 🇧🇷 BR | 11502 |
| 4 | 🇦🇺 AU | 11148 |
| 5 | 🇨🇦 CA | 10893 |
| 6 | 🇮🇳 IN | 10763 |
| 7 | 🇮🇹 IT | 10458 |
| 8 | 🇩🇪 DE | 9896 |
| 9 | 🇬🇧 GB | 9361 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7945 |
| 12 | 🇨🇴 CO | 7913 |
| 13 | 🇬🇷 GR | 5883 |
| 14 | 🇲🇽 MX | 5627 |
| 15 | 🇹🇷 TR | 5520 |
| 16 | 🇨🇭 CH | 5404 |
| 17 | 🇳🇴 NO | 5075 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3297 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2547 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2118 |
| 27 | 🇲🇦 MA | 2021 |
| 28 | 🇳🇱 NL | 1793 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4143 |
| 2 | Denver International Airport |  | US | 3233 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2461 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2271 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2108 |
| 8 | Zurich Airport |  | CH | 2107 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2061 |
| 10 | La Aurora Airport |  | GT | 1951 |
| 11 | El Dorado International Airport |  | CO | 1836 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1769 |
| 13 | Salt Lake City International Airport |  | US | 1767 |
| 14 | Chicago O'Hare International Airport |  | US | 1744 |
| 15 | Congonhas Airport |  | BR | 1685 |
| 16 | Frankfurt am Main International Airport |  | DE | 1679 |
| 17 | Madrid Barajas International Airport |  | ES | 1568 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1529 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1513 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1463 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1439 |
| 23 | Malpensa International Airport |  | IT | 1391 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1382 |
| 25 | Charles de Gaulle International Airport |  | FR | 1372 |
| 26 | Charlotte/Douglas International Airport |  | US | 1315 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1244 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1216 |
| 32 | Barcelona International Airport |  | ES | 1200 |
| 33 | Viracopos International Airport |  | BR | 1163 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1129 |
| 36 | Reno/Tahoe International Airport |  | US | 1121 |
| 37 | Oslo Gardermoen Airport |  | NO | 1119 |
| 38 | Vitoria/Foronda Airport |  | ES | 1105 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1093 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1014 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 370 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 336 | 27m | 275 km | 1,592.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 284 | 22m | 55 km | 269.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 243 | 1h 14m | 961 km | 4,027.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N248LK |  | Appleton International Airport (KATW) | Dane County Regional/Truax Field (KMSN) | 2026-08-15 17:10 UTC | 2026-08-15 17:45 UTC | 35m |
| RPA5695 | Republic Airways | General Edward Lawrence Logan International Airport (KBOS) | Easley Acres Airport (33NC) | 2026-08-15 16:05 UTC | 2026-08-15 17:39 UTC | 1h 33m |
| AAL1459 | American Airlines | Chicago O'Hare International Airport (KORD) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-15 15:52 UTC | 2026-08-15 17:39 UTC | 1h 46m |
| N5713R |  | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-15 17:13 UTC | 2026-08-15 17:37 UTC | 23m |
| N187ND |  | TX81 (TX81) | Rowland R Airfield (23TA) | 2026-08-15 16:56 UTC | 2026-08-15 17:36 UTC | 39m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-15 16:59 UTC | 2026-08-15 17:36 UTC | 36m |
| N5QD |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-08-15 17:30 UTC | 2026-08-15 17:33 UTC | 3m |
| N360MC |  | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-08-15 16:57 UTC | 2026-08-15 17:25 UTC | 28m |
| DEUBH | DEU | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-08-15 16:50 UTC | 2026-08-15 17:23 UTC | 32m |
| N352HP |  | Salt Lake City International Airport (KSLC) | Provo Municipal Airport (KPVU) | 2026-08-15 17:07 UTC | 2026-08-15 17:23 UTC | 15m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Crystal Lakes Airport (25CO) | 2026-08-15 16:57 UTC | 2026-08-15 17:20 UTC | 23m |
| N21272 |  | Ryan Field (KRYN) | Ryan Field (KRYN) | 2026-08-15 16:47 UTC | 2026-08-15 17:18 UTC | 30m |
| N135RF |  | Daulton Airport (77CA) | Lee Vining Airport (KO24) | 2026-08-15 15:26 UTC | 2026-08-15 17:18 UTC | 1h 51m |
| N524BB |  | Smith Reynolds Airport (KINT) | Flying Cloud Airport (KFCM) | 2026-08-15 15:02 UTC | 2026-08-15 17:16 UTC | 2h 14m |
| CXK1073 | CXK | Shepard Strip (07ID) | Logan-Cache Airport (KLGU) | 2026-08-15 16:37 UTC | 2026-08-15 17:16 UTC | 38m |
| WIF9007 | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-15 16:29 UTC | 2026-08-15 17:16 UTC | 46m |
| RAM694T | Royal Air Maroc | Nador International Airport (GMMW) | Frankfurt am Main International Airport (EDDF) | 2026-08-15 14:29 UTC | 2026-08-15 17:15 UTC | 2h 46m |
| CFG3HU | CFG | Palma De Mallorca Airport (LEPA) | Frankfurt am Main International Airport (EDDF) | 2026-08-15 15:21 UTC | 2026-08-15 17:15 UTC | 1h 54m |
| CFLTV | CFL | Cornwall Regional Airport (CYCC) | Cornwall Regional Airport (CYCC) | 2026-08-15 16:37 UTC | 2026-08-15 17:15 UTC | 38m |
| FGD561 | FGD | Abbotsford Airport (CYXX) | Hope Airport (CYHE) | 2026-08-15 17:00 UTC | 2026-08-15 17:15 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
