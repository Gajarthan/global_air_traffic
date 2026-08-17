# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_19:12:13_UTC-green)

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

**Latest saved flight:** 2026-08-17 19:12:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 19:12:13 UTC

- **209,616** saved flights
- **66,769** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,616** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,520,600.1 tonnes** estimated CO2 emissions
- **146,121,747 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8301 |
| 2 | SkyWest Airlines | 7527 |
| 3 | EJA | 4084 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3502 |
| 6 | Southwest Airlines | 3370 |
| 7 | Delta Air Lines | 2712 |
| 8 | ENY | 2614 |
| 9 | LATAM Airlines | 1975 |
| 10 | AZU | 1898 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1745 |
| 13 | WIF | 1690 |
| 14 | LXJ | 1654 |
| 15 | easyJet | 1455 |
| 16 | Swiss International | 1402 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1324 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1290 |
| 21 | EJU | 1282 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1153 |
| 24 | GLO | 1134 |
| 25 | Air France | 1133 |
| 26 | PGT | 1122 |
| 27 | JetBlue | 1071 |
| 28 | AEE | 1068 |
| 29 | WMT | 1062 |
| 30 | Wizz Air | 1039 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177601 |
| 2 | 🇪🇸 ES | 13420 |
| 3 | 🇧🇷 BR | 12031 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11567 |
| 6 | 🇮🇳 IN | 11154 |
| 7 | 🇮🇹 IT | 10969 |
| 8 | 🇩🇪 DE | 10364 |
| 9 | 🇬🇧 GB | 9788 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8367 |
| 12 | 🇫🇷 FR | 8337 |
| 13 | 🇬🇷 GR | 6168 |
| 14 | 🇹🇷 TR | 5967 |
| 15 | 🇲🇽 MX | 5887 |
| 16 | 🇨🇭 CH | 5580 |
| 17 | 🇳🇴 NO | 5234 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3516 |
| 20 | 🇵🇱 PL | 3464 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2694 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2253 |
| 27 | 🇲🇦 MA | 2117 |
| 28 | 🇳🇱 NL | 1871 |
| 29 | 🇲🇪 ME | 1782 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4403 |
| 2 | Denver International Airport |  | US | 3413 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2538 |
| 5 | Guaymaral Airport |  | CO | 2519 |
| 6 | Harry Reid International Airport |  | US | 2358 |
| 7 | Zurich Airport |  | CH | 2188 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2180 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2169 |
| 10 | La Aurora Airport |  | GT | 2049 |
| 11 | Chicago O'Hare International Airport |  | US | 1943 |
| 12 | El Dorado International Airport |  | CO | 1911 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1869 |
| 14 | Salt Lake City International Airport |  | US | 1854 |
| 15 | Congonhas Airport |  | BR | 1750 |
| 16 | Frankfurt am Main International Airport |  | DE | 1721 |
| 17 | Madrid Barajas International Airport |  | ES | 1641 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1591 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 20 | Capua Airport |  | IT | 1581 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1528 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1451 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1420 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1295 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1269 |
| 32 | Barcelona International Airport |  | ES | 1256 |
| 33 | Seattle-Tacoma International Airport |  | US | 1243 |
| 34 | Viracopos International Airport |  | BR | 1217 |
| 35 | Calgary International Airport |  | CA | 1184 |
| 36 | Oslo Gardermoen Airport |  | NO | 1160 |
| 37 | Vitoria/Foronda Airport |  | ES | 1155 |
| 38 | Reno/Tahoe International Airport |  | US | 1148 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1132 |
| 40 | Don Mueang International Airport |  | TH | 1114 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1035 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 738 | 21m | 244 km | 3,107.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 477 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 418 | 8m | - | - |
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
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
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
| N503WA |  | Three Rivers Municipal/Dr Haines Airport (KHAI) | Kirsch Municipal Airport (KIRS) | 2026-08-17 18:33 UTC | 2026-08-17 19:12 UTC | 38m |
| N40057 |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-17 18:31 UTC | 2026-08-17 19:11 UTC | 39m |
| NDU80T | NDU | Knutson Airport (4ND1) | Hillsboro Municipal Airport (K3H4) | 2026-08-17 18:30 UTC | 2026-08-17 19:06 UTC | 36m |
| ES809 |  | Livermore Municipal Airport (KLVK) | Sacramento Executive Airport (KSAC) | 2026-08-17 18:33 UTC | 2026-08-17 19:03 UTC | 29m |
| NIT239 | NIT | Heart Of Georgia Regional Airport (KEZM) | Cauley's Airstrip (3GA8) | 2026-08-17 18:45 UTC | 2026-08-17 19:01 UTC | 15m |
| N950RF |  | Provo Municipal Airport (KPVU) | Mineral Canyon Strip (UT75) | 2026-08-17 15:01 UTC | 2026-08-17 18:59 UTC | 3h 57m |
| N9979B |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-08-17 18:32 UTC | 2026-08-17 18:58 UTC | 25m |
|  |  | Daniels Field Llc Airport (OR78) | Daniels Field Llc Airport (OR78) | 2026-08-17 18:49 UTC | 2026-08-17 18:58 UTC | 8m |
| BOE38F | BOE | Boeing Field/King County International Airport (KBFI) | Pangborn Memorial Airport (KEAT) | 2026-08-17 18:33 UTC | 2026-08-17 18:56 UTC | 23m |
| N365KS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-17 18:33 UTC | 2026-08-17 18:53 UTC | 20m |
| N78PT |  | Reno/Tahoe International Airport (KRNO) | NV13 (NV13) | 2026-08-17 18:39 UTC | 2026-08-17 18:52 UTC | 13m |
| GIZMO11 | GIZ | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-17 18:31 UTC | 2026-08-17 18:48 UTC | 16m |
| LXJ418 | LXJ | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-08-17 18:29 UTC | 2026-08-17 18:45 UTC | 15m |
| FIRE01 | FIR | Ovar Airport (LPOV) | Lousa Private Airport (LPLZ) | 2026-08-17 17:40 UTC | 2026-08-17 18:44 UTC | 1h 3m |
| WIF6Y | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-17 18:30 UTC | 2026-08-17 18:41 UTC | 11m |
| TALON41 | TAL | James H Easom Field (KM23) | Magee Municipal Airport (K17M) | 2026-08-17 18:22 UTC | 2026-08-17 18:40 UTC | 18m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-17 18:23 UTC | 2026-08-17 18:39 UTC | 15m |
| N340ES |  | Akron-Canton Regional Airport (KCAK) | Harry Clever Field (KPHD) | 2026-08-17 18:26 UTC | 2026-08-17 18:38 UTC | 12m |
| N66HC |  | Renton Municipal Airport (KRNT) | Newport Municipal Airport (KONP) | 2026-08-17 17:03 UTC | 2026-08-17 18:36 UTC | 1h 33m |
| ITY602 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | John F Kennedy International Airport (KJFK) | 2026-08-17 09:30 UTC | 2026-08-17 18:34 UTC | 9h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
