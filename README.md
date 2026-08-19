# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_15:55:45_UTC-green)

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

**Latest saved flight:** 2026-08-19 15:55:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 15:55:45 UTC

- **216,217** saved flights
- **68,300** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,217** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,601,293.2 tonnes** estimated CO2 emissions
- **150,799,607 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8647 |
| 2 | SkyWest Airlines | 7712 |
| 3 | EJA | 4196 |
| 4 | IndiGo | 3685 |
| 5 | American Airlines | 3599 |
| 6 | Southwest Airlines | 3437 |
| 7 | Delta Air Lines | 2793 |
| 8 | ENY | 2667 |
| 9 | LATAM Airlines | 2046 |
| 10 | AZU | 1974 |
| 11 | Vueling | 1818 |
| 12 | Lufthansa | 1810 |
| 13 | WIF | 1728 |
| 14 | LXJ | 1700 |
| 15 | easyJet | 1501 |
| 16 | Swiss International | 1443 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1367 |
| 19 | EJU | 1348 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1185 |
| 24 | PGT | 1174 |
| 25 | Air France | 1172 |
| 26 | GLO | 1171 |
| 27 | WMT | 1129 |
| 28 | JetBlue | 1102 |
| 29 | Wizz Air | 1100 |
| 30 | AEE | 1086 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182105 |
| 2 | 🇪🇸 ES | 13889 |
| 3 | 🇧🇷 BR | 12440 |
| 4 | 🇦🇺 AU | 12167 |
| 5 | 🇨🇦 CA | 11901 |
| 6 | 🇮🇳 IN | 11475 |
| 7 | 🇮🇹 IT | 11462 |
| 8 | 🇩🇪 DE | 10729 |
| 9 | 🇬🇧 GB | 10152 |
| 10 | 🇯🇵 JP | 8869 |
| 11 | 🇨🇴 CO | 8833 |
| 12 | 🇫🇷 FR | 8641 |
| 13 | 🇬🇷 GR | 6330 |
| 14 | 🇹🇷 TR | 6214 |
| 15 | 🇲🇽 MX | 6035 |
| 16 | 🇨🇭 CH | 5753 |
| 17 | 🇳🇴 NO | 5377 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3673 |
| 20 | 🇵🇱 PL | 3580 |
| 21 | 🇹🇭 TH | 3537 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2745 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2368 |
| 27 | 🇲🇦 MA | 2176 |
| 28 | 🇳🇱 NL | 1932 |
| 29 | 🇲🇪 ME | 1882 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4528 |
| 2 | Denver International Airport |  | US | 3512 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2620 |
| 5 | Guaymaral Airport |  | CO | 2579 |
| 6 | Harry Reid International Airport |  | US | 2402 |
| 7 | Zurich Airport |  | CH | 2249 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2216 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2208 |
| 10 | La Aurora Airport |  | GT | 2086 |
| 11 | El Dorado International Airport |  | CO | 2016 |
| 12 | Chicago O'Hare International Airport |  | US | 1985 |
| 13 | Salt Lake City International Airport |  | US | 1902 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1891 |
| 15 | Congonhas Airport |  | BR | 1812 |
| 16 | Frankfurt am Main International Airport |  | DE | 1769 |
| 17 | Madrid Barajas International Airport |  | ES | 1695 |
| 18 | Capua Airport |  | IT | 1644 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1628 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1610 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1589 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1518 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1486 |
| 26 | Charlotte/Douglas International Airport |  | US | 1450 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1327 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1320 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1290 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1261 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1199 |
| 37 | Vitoria/Foronda Airport |  | ES | 1195 |
| 38 | Amsterdam Airport Schiphol |  | NL | 1168 |
| 39 | Don Mueang International Airport |  | TH | 1167 |
| 40 | Reno/Tahoe International Airport |  | US | 1164 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1055 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 770 | 21m | 244 km | 3,242.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 485 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 468 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 361 | 27m | 275 km | 1,710.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 284 | 21m | 250 km | 1,226.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 264 | 27m | 215 km | 977.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 255 | 1h 14m | 961 km | 4,226.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N40798 |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-08-19 14:59 UTC | 2026-08-19 15:55 UTC | 56m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-19 15:38 UTC | 2026-08-19 15:53 UTC | 14m |
| N105FA |  | Pennridge Airport (KCKZ) | Trenton Mercer Airport (KTTN) | 2026-08-19 15:32 UTC | 2026-08-19 15:50 UTC | 17m |
| DOC42 | DOC | Trondheim Airport Vaernes (ENVA) | Trondheim Airport Vaernes (ENVA) | 2026-08-19 15:29 UTC | 2026-08-19 15:48 UTC | 19m |
| N733JM |  | Cortez Municipal Airport (KCEZ) | Telluride Regional Airport (KTEX) | 2026-08-19 15:11 UTC | 2026-08-19 15:44 UTC | 33m |
| N321CT |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-19 14:47 UTC | 2026-08-19 15:42 UTC | 54m |
| TUTOR983 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-19 15:12 UTC | 2026-08-19 15:41 UTC | 28m |
| N3547L |  | Boulder Municipal Airport (KBDU) | Boulder Municipal Airport (KBDU) | 2026-08-19 15:06 UTC | 2026-08-19 15:40 UTC | 34m |
| N449KC |  | Laconia Municipal Airport (KLCI) | Lehigh Valley International Airport (KABE) | 2026-08-19 14:21 UTC | 2026-08-19 15:39 UTC | 1h 17m |
| TUTOR18 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-19 15:15 UTC | 2026-08-19 15:38 UTC | 23m |
| TAUNT21 | TAU | Enid Woodring Regional Airport (KWDG) | Flying E Ranch Airport (OK16) | 2026-08-19 15:23 UTC | 2026-08-19 15:37 UTC | 14m |
| N541S |  | John C Tune Airport (KJWN) | Savannah-Hardin County Airport (KSNH) | 2026-08-19 15:19 UTC | 2026-08-19 15:35 UTC | 16m |
| N5254D |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-08-19 15:14 UTC | 2026-08-19 15:35 UTC | 21m |
| N583CA |  | Dallas Executive Airport (KRBD) | Lancaster Regional Airport (KLNC) | 2026-08-19 14:32 UTC | 2026-08-19 15:34 UTC | 1h 2m |
| N7365S |  | Chico Regional Airport (KCIC) | Willows/Glenn County Airport (KWLW) | 2026-08-19 15:03 UTC | 2026-08-19 15:33 UTC | 30m |
| CGTEP | CGT | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-19 15:18 UTC | 2026-08-19 15:32 UTC | 14m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-19 15:08 UTC | 2026-08-19 15:31 UTC | 23m |
| FD478 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-19 14:54 UTC | 2026-08-19 15:28 UTC | 34m |
| N464TA |  | Laurence G Hanscom Field (KBED) | Lebanon Municipal Airport (KLEB) | 2026-08-19 14:35 UTC | 2026-08-19 15:28 UTC | 53m |
| FIRE02 | FIR | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-19 15:18 UTC | 2026-08-19 15:27 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
