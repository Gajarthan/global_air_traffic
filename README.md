# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_18:40:42_UTC-green)

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

**Latest saved flight:** 2026-08-17 18:40:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 18:40:42 UTC

- **209,487** saved flights
- **66,745** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,487** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,519,064.6 tonnes** estimated CO2 emissions
- **146,032,732 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8296 |
| 2 | SkyWest Airlines | 7519 |
| 3 | EJA | 4078 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3502 |
| 6 | Southwest Airlines | 3369 |
| 7 | Delta Air Lines | 2707 |
| 8 | ENY | 2610 |
| 9 | LATAM Airlines | 1974 |
| 10 | AZU | 1895 |
| 11 | Lufthansa | 1767 |
| 12 | Vueling | 1745 |
| 13 | WIF | 1687 |
| 14 | LXJ | 1653 |
| 15 | easyJet | 1454 |
| 16 | Swiss International | 1401 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1324 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1288 |
| 21 | EJU | 1281 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1151 |
| 24 | GLO | 1133 |
| 25 | Air France | 1131 |
| 26 | PGT | 1122 |
| 27 | JetBlue | 1071 |
| 28 | AEE | 1067 |
| 29 | WMT | 1061 |
| 30 | Wizz Air | 1038 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177492 |
| 2 | 🇪🇸 ES | 13411 |
| 3 | 🇧🇷 BR | 12019 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11558 |
| 6 | 🇮🇳 IN | 11153 |
| 7 | 🇮🇹 IT | 10963 |
| 8 | 🇩🇪 DE | 10357 |
| 9 | 🇬🇧 GB | 9782 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8351 |
| 12 | 🇫🇷 FR | 8331 |
| 13 | 🇬🇷 GR | 6163 |
| 14 | 🇹🇷 TR | 5962 |
| 15 | 🇲🇽 MX | 5880 |
| 16 | 🇨🇭 CH | 5576 |
| 17 | 🇳🇴 NO | 5229 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3516 |
| 20 | 🇵🇱 PL | 3462 |
| 21 | 🇹🇭 TH | 3353 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2694 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2253 |
| 27 | 🇲🇦 MA | 2116 |
| 28 | 🇳🇱 NL | 1870 |
| 29 | 🇲🇪 ME | 1780 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4398 |
| 2 | Denver International Airport |  | US | 3410 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2538 |
| 5 | Guaymaral Airport |  | CO | 2515 |
| 6 | Harry Reid International Airport |  | US | 2356 |
| 7 | Zurich Airport |  | CH | 2186 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2178 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2168 |
| 10 | La Aurora Airport |  | GT | 2049 |
| 11 | Chicago O'Hare International Airport |  | US | 1940 |
| 12 | El Dorado International Airport |  | CO | 1911 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1865 |
| 14 | Salt Lake City International Airport |  | US | 1849 |
| 15 | Congonhas Airport |  | BR | 1748 |
| 16 | Frankfurt am Main International Airport |  | DE | 1721 |
| 17 | Madrid Barajas International Airport |  | ES | 1640 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1590 |
| 20 | Capua Airport |  | IT | 1580 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1527 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1451 |
| 25 | Charles de Gaulle International Airport |  | FR | 1442 |
| 26 | Charlotte/Douglas International Airport |  | US | 1420 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1294 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1269 |
| 32 | Barcelona International Airport |  | ES | 1256 |
| 33 | Seattle-Tacoma International Airport |  | US | 1242 |
| 34 | Viracopos International Airport |  | BR | 1215 |
| 35 | Calgary International Airport |  | CA | 1182 |
| 36 | Oslo Gardermoen Airport |  | NO | 1160 |
| 37 | Vitoria/Foronda Airport |  | ES | 1155 |
| 38 | Reno/Tahoe International Airport |  | US | 1147 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1131 |
| 40 | Don Mueang International Airport |  | TH | 1113 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1033 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 477 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 414 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 307 | 44m | 241 km | 1,275.2 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 240 | 19m | 144 km | 597.0 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TALON41 | TAL | James H Easom Field (KM23) | Magee Municipal Airport (K17M) | 2026-08-17 18:22 UTC | 2026-08-17 18:40 UTC | 18m |
| N66HC |  | Renton Municipal Airport (KRNT) | Newport Municipal Airport (KONP) | 2026-08-17 17:03 UTC | 2026-08-17 18:36 UTC | 1h 33m |
| ITY602 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | John F Kennedy International Airport (KJFK) | 2026-08-17 09:30 UTC | 2026-08-17 18:34 UTC | 9h 3m |
| SCU28 | SCU | Jirik Field (OL23) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-17 18:09 UTC | 2026-08-17 18:32 UTC | 22m |
| N3386E |  | Borrego Valley Airport (KL08) | Hemet-Ryan Airport (KHMT) | 2026-08-17 17:58 UTC | 2026-08-17 18:29 UTC | 31m |
| CGLCP | CGL | Vancouver International Airport (CYVR) | Sechelt-Gibsons Airport (CAP3) | 2026-08-17 18:07 UTC | 2026-08-17 18:26 UTC | 19m |
| MVK88 | MVK | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-08-17 17:57 UTC | 2026-08-17 18:21 UTC | 24m |
| EZY93AR | easyJet | London Gatwick Airport (EGKK) | Zemunik Airport (LDZD) | 2026-08-17 16:38 UTC | 2026-08-17 18:21 UTC | 1h 43m |
| DFARO | DFA | Nevers-Fourchambault Airport (LFQG) | Nevers-Fourchambault Airport (LFQG) | 2026-08-17 17:50 UTC | 2026-08-17 18:19 UTC | 28m |
| N828CF |  | Shawano Municipal Airport (KEZS) | Shawano Municipal Airport (KEZS) | 2026-08-17 18:03 UTC | 2026-08-17 18:18 UTC | 15m |
| MFO500T | MFO | El Gora Airport (HEGR) | El Gora Airport (HEGR) | 2026-08-17 18:06 UTC | 2026-08-17 18:18 UTC | 11m |
| TRP6 | TRP | Pokety Airport (3MD8) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-08-17 17:57 UTC | 2026-08-17 18:15 UTC | 17m |
| N420FP |  | Flagstaff Pulliam Airport (KFLG) | Flagstaff Pulliam Airport (KFLG) | 2026-08-17 18:03 UTC | 2026-08-17 18:11 UTC | 8m |
| N36456 |  | Beverly Regional Airport (KBVY) | Beverly Regional Airport (KBVY) | 2026-08-17 17:27 UTC | 2026-08-17 18:11 UTC | 44m |
| N919G |  | Des Moines International Airport (KDSM) | Clark County Airport (K8D7) | 2026-08-17 17:25 UTC | 2026-08-17 18:10 UTC | 44m |
| PBR675 | PBR | Victoria International Airport (CYYJ) | Port Mcneill Airport (CAT5) | 2026-08-17 17:18 UTC | 2026-08-17 18:09 UTC | 50m |
| LXJ418 | LXJ | Sacramento Mather Airport (KMHR) | Zamperini Field (KTOA) | 2026-08-17 17:05 UTC | 2026-08-17 18:09 UTC | 1h 3m |
| UAL3866 | United Airlines | Washington Dulles International Airport (KIAD) | Washington Dulles International Airport (KIAD) | 2026-08-17 16:34 UTC | 2026-08-17 18:07 UTC | 1h 32m |
| N571ND |  | Destin Executive Airport (KDTS) | Destin Executive Airport (KDTS) | 2026-08-17 17:51 UTC | 2026-08-17 18:06 UTC | 15m |
| N411DD |  | Bridgeport/Sikorsky Airport (KBDR) | Bridgeport/Sikorsky Airport (KBDR) | 2026-08-17 18:06 UTC | 2026-08-17 18:06 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
