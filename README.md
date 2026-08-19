# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_09:58:15_UTC-green)

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

**Latest saved flight:** 2026-08-19 09:58:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 09:58:15 UTC

- **214,873** saved flights
- **67,821** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,873** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,584,114.8 tonnes** estimated CO2 emissions
- **149,803,756 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8538 |
| 2 | SkyWest Airlines | 7695 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3672 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2767 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2028 |
| 10 | AZU | 1962 |
| 11 | Vueling | 1804 |
| 12 | Lufthansa | 1789 |
| 13 | WIF | 1721 |
| 14 | LXJ | 1694 |
| 15 | easyJet | 1487 |
| 16 | Swiss International | 1431 |
| 17 | AXM | 1410 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1346 |
| 20 | EJU | 1328 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1303 |
| 23 | VIV | 1183 |
| 24 | GLO | 1163 |
| 25 | PGT | 1161 |
| 26 | Air France | 1159 |
| 27 | WMT | 1114 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1081 |
| 30 | Wizz Air | 1074 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181406 |
| 2 | 🇪🇸 ES | 13743 |
| 3 | 🇧🇷 BR | 12344 |
| 4 | 🇦🇺 AU | 12149 |
| 5 | 🇨🇦 CA | 11857 |
| 6 | 🇮🇳 IN | 11429 |
| 7 | 🇮🇹 IT | 11340 |
| 8 | 🇩🇪 DE | 10592 |
| 9 | 🇬🇧 GB | 10010 |
| 10 | 🇯🇵 JP | 8857 |
| 11 | 🇨🇴 CO | 8745 |
| 12 | 🇫🇷 FR | 8536 |
| 13 | 🇬🇷 GR | 6295 |
| 14 | 🇹🇷 TR | 6154 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5688 |
| 17 | 🇳🇴 NO | 5334 |
| 18 | 🇲🇾 MY | 3728 |
| 19 | 🇿🇦 ZA | 3636 |
| 20 | 🇵🇱 PL | 3536 |
| 21 | 🇹🇭 TH | 3494 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2888 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2605 |
| 26 | 🇭🇷 HR | 2343 |
| 27 | 🇲🇦 MA | 2161 |
| 28 | 🇳🇱 NL | 1911 |
| 29 | 🇲🇪 ME | 1860 |
| 30 | 🇮🇩 ID | 1802 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4513 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2658 |
| 4 | Indira Gandhi International Airport |  | IN | 2611 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2395 |
| 7 | Zurich Airport |  | CH | 2230 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2204 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1749 |
| 17 | Madrid Barajas International Airport |  | ES | 1674 |
| 18 | Capua Airport |  | IT | 1628 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1574 |
| 22 | Macau International Airport |  | MO | 1561 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1515 |
| 24 | Malpensa International Airport |  | IT | 1505 |
| 25 | Charles de Gaulle International Airport |  | FR | 1478 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1373 |
| 28 | Ninoy Aquino International Airport |  | PH | 1371 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1313 |
| 31 | Bengaluru International Airport |  | IN | 1311 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1254 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1190 |
| 37 | Vitoria/Foronda Airport |  | ES | 1187 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1156 |
| 40 | Don Mueang International Airport |  | TH | 1155 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 533 | 1h 7m | 770 km | 7,080.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 356 | 27m | 275 km | 1,686.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 315 | 1h 49m | 1,423 km | 7,730.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 314 | 44m | 241 km | 1,304.3 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 268 | 1h 38m | 1,156 km | 5,346.5 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 267 | 19m | 99 km | 457.4 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 263 | 27m | 215 km | 974.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 253 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 250 | 31m | 369 km | 1,591.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 227 | 44m | 555 km | 2,173.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJU69WF | EJU | Mikonos Airport (LGMK) | Malpensa International Airport (LIMC) | 2026-08-19 07:33 UTC | 2026-08-19 09:58 UTC | 2h 25m |
| UPS474 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Montréal (Mirabel) Airport (CYMX) | 2026-08-19 08:20 UTC | 2026-08-19 09:51 UTC | 1h 31m |
| KAL2027 | Korean Air | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-19 07:50 UTC | 2026-08-19 09:51 UTC | 2h 0m |
| GFRGP | GFR | Coventry Airport (EGBE) | Elstree Airfield (EGTR) | 2026-08-19 09:24 UTC | 2026-08-19 09:49 UTC | 25m |
| CAL5175 | CAL | San Francisco International Airport (KSFO) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-18 21:27 UTC | 2026-08-19 09:48 UTC | 12h 21m |
| BOREAL9 | BOR | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-19 09:00 UTC | 2026-08-19 09:47 UTC | 47m |
| CAN11 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-19 09:13 UTC | 2026-08-19 09:44 UTC | 30m |
| STW171 | STW | Cardak Airport (LTAY) | Smolensk North Airport (XUBS) | 2026-08-19 06:40 UTC | 2026-08-19 09:41 UTC | 3h 1m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-19 08:08 UTC | 2026-08-19 09:38 UTC | 1h 29m |
| EMC8T | EMC | London Biggin Hill Airport (EGKB) | Lydd Airport (EGMD) | 2026-08-19 08:48 UTC | 2026-08-19 09:37 UTC | 48m |
| TUTOR18 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-19 09:14 UTC | 2026-08-19 09:36 UTC | 22m |
| CSHIX | CSH | Casarrubios Del Monte Airport (LEMT) | Cuatro Vientos Airport (LECU) | 2026-08-19 09:19 UTC | 2026-08-19 09:36 UTC | 17m |
| THY6238 | Turkish Airlines | Tbilisi International Airport (UGTB) | Zhuhai Airport (ZGSD) | 2026-08-19 01:27 UTC | 2026-08-19 09:35 UTC | 8h 8m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-08-19 08:19 UTC | 2026-08-19 09:34 UTC | 1h 15m |
| VMY | VMY | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-08-19 09:10 UTC | 2026-08-19 09:32 UTC | 22m |
| DFARO | DFA | Nevers-Fourchambault Airport (LFQG) | Nevers-Fourchambault Airport (LFQG) | 2026-08-19 08:51 UTC | 2026-08-19 09:26 UTC | 35m |
| EFC74D | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-19 09:10 UTC | 2026-08-19 09:25 UTC | 14m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-08-19 09:00 UTC | 2026-08-19 09:22 UTC | 22m |
| CAN21 | CAN | Trieste / Ronchi Dei Legionari (LIPQ) | Notsch Im Gailtal Airport (LOKN) | 2026-08-19 09:03 UTC | 2026-08-19 09:21 UTC | 18m |
| TTW215 | TTW | Okayama Airport (RJOB) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-19 07:12 UTC | 2026-08-19 09:14 UTC | 2h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
