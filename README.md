# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_18:59:56_UTC-green)

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

**Latest saved flight:** 2026-09-14 18:59:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-14 18:59:56 UTC

- **258,583** saved flights
- **76,857** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,583** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,130,196.8 tonnes** estimated CO2 emissions
- **181,460,681 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10261 |
| 2 | SkyWest Airlines | 9009 |
| 3 | EJA | 5019 |
| 4 | IndiGo | 4340 |
| 5 | American Airlines | 4081 |
| 6 | Southwest Airlines | 3804 |
| 7 | Delta Air Lines | 3236 |
| 8 | ENY | 3066 |
| 9 | LATAM Airlines | 2487 |
| 10 | AZU | 2425 |
| 11 | Vueling | 2188 |
| 12 | WIF | 2076 |
| 13 | LXJ | 2022 |
| 14 | Lufthansa | 2018 |
| 15 | easyJet | 1762 |
| 16 | Swiss International | 1727 |
| 17 | QLK | 1666 |
| 18 | AXM | 1647 |
| 19 | EJU | 1641 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1534 |
| 22 | All Nippon Airways | 1498 |
| 23 | WMT | 1462 |
| 24 | GLO | 1441 |
| 25 | PGT | 1437 |
| 26 | Air France | 1414 |
| 27 | VIV | 1414 |
| 28 | Wizz Air | 1409 |
| 29 | AEE | 1250 |
| 30 | JetBlue | 1250 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214663 |
| 2 | 🇪🇸 ES | 16397 |
| 3 | 🇧🇷 BR | 15116 |
| 4 | 🇦🇺 AU | 14734 |
| 5 | 🇨🇦 CA | 14389 |
| 6 | 🇮🇹 IT | 14093 |
| 7 | 🇮🇳 IN | 13639 |
| 8 | 🇩🇪 DE | 12583 |
| 9 | 🇬🇧 GB | 12047 |
| 10 | 🇨🇴 CO | 11606 |
| 11 | 🇫🇷 FR | 10394 |
| 12 | 🇯🇵 JP | 10068 |
| 13 | 🇹🇷 TR | 7793 |
| 14 | 🇬🇷 GR | 7532 |
| 15 | 🇲🇽 MX | 7124 |
| 16 | 🇨🇭 CH | 6941 |
| 17 | 🇳🇴 NO | 6389 |
| 18 | 🇹🇭 TH | 4647 |
| 19 | 🇲🇾 MY | 4432 |
| 20 | 🇿🇦 ZA | 4392 |
| 21 | 🇵🇱 PL | 4283 |
| 22 | 🇳🇿 NZ | 3571 |
| 23 | 🇵🇭 PH | 3474 |
| 24 | 🇬🇹 GT | 3266 |
| 25 | 🇭🇷 HR | 2965 |
| 26 | 🇰🇷 KR | 2955 |
| 27 | 🇲🇦 MA | 2596 |
| 28 | 🇲🇪 ME | 2436 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5304 |
| 2 | Denver International Airport |  | US | 4181 |
| 3 | Indira Gandhi International Airport |  | IN | 3123 |
| 4 | Tokyo International Airport |  | JP | 3003 |
| 5 | Guaymaral Airport |  | CO | 2766 |
| 6 | Harry Reid International Airport |  | US | 2745 |
| 7 | Zurich Airport |  | CH | 2713 |
| 8 | El Dorado International Airport |  | CO | 2702 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2608 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2523 |
| 11 | La Aurora Airport |  | GT | 2481 |
| 12 | Salt Lake City International Airport |  | US | 2280 |
| 13 | Chicago O'Hare International Airport |  | US | 2248 |
| 14 | Congonhas Airport |  | BR | 2214 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2116 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1992 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1944 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1864 |
| 21 | Malpensa International Airport |  | IT | 1860 |
| 22 | Charles de Gaulle International Airport |  | FR | 1822 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1819 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1787 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1754 |
| 26 | Macau International Airport |  | MO | 1712 |
| 27 | Ninoy Aquino International Airport |  | PH | 1702 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1617 |
| 30 | Kuala Lumpur International Airport |  | MY | 1594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1586 |
| 32 | Viracopos International Airport |  | BR | 1562 |
| 33 | Seattle-Tacoma International Airport |  | US | 1517 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1508 |
| 35 | Don Mueang International Airport |  | TH | 1486 |
| 36 | Calgary International Airport |  | CA | 1480 |
| 37 | Bengaluru International Airport |  | IN | 1469 |
| 38 | Oslo Gardermoen Airport |  | NO | 1458 |
| 39 | Vancouver International Airport |  | CA | 1450 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 964 | 21m | 244 km | 4,059.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 696 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 577 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 392 | 44m | 241 km | 1,628.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 364 | 24m | 218 km | 1,371.3 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 321 | 19m | 99 km | 549.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 315 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 310 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 277 | 1h 50m | 1,304 km | 6,231.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 274 | 42m | 535 km | 2,530.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N733JT |  | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Ocean City Municipal Airport (KOXB) | 2026-09-14 18:26 UTC | 2026-09-14 18:59 UTC | 33m |
| N465FA |  | Capital City Airport (KCXY) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-14 18:28 UTC | 2026-09-14 18:59 UTC | 30m |
| QAF6 | QAF | Paris-Orly Airport (LFPO) | Al Khawr Airport (OTBK) | 2026-09-14 12:55 UTC | 2026-09-14 18:58 UTC | 6h 3m |
| RENO71 | REN | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-09-14 18:20 UTC | 2026-09-14 18:58 UTC | 38m |
| N141FA |  | Fullerton Municipal Airport (KFUL) | Mc Conville Airstrip (CA42) | 2026-09-14 18:32 UTC | 2026-09-14 18:50 UTC | 18m |
| TGCYO | TGC | La Aurora Airport (MGGT) | La Estanzuela Airport (MHLZ) | 2026-09-14 18:22 UTC | 2026-09-14 18:49 UTC | 26m |
| N724FL |  | Joliet Regional Airport (KJOT) | 89LL (89LL) | 2026-09-14 17:59 UTC | 2026-09-14 18:46 UTC | 46m |
| N3676L |  | Montgomery-Gibbs Executive Airport (KMYF) | CA84 (CA84) | 2026-09-14 18:36 UTC | 2026-09-14 18:44 UTC | 7m |
| N9939Z |  | King Salmon Airport (PAKN) | King Salmon Airport (PAKN) | 2026-09-14 18:24 UTC | 2026-09-14 18:40 UTC | 16m |
| BRG661 | BRG | Point Hope Airport (PAPO) | Kivalina Airport (PAVL) | 2026-09-14 18:12 UTC | 2026-09-14 18:36 UTC | 24m |
| PLF110 | PLF | Warsaw Chopin Airport (EPWA) | Stuttgart Airport (EDDS) | 2026-09-14 17:01 UTC | 2026-09-14 18:34 UTC | 1h 33m |
| N212HF |  | Des Moines International Airport (KDSM) | Flying Cloud Airport (KFCM) | 2026-09-14 17:44 UTC | 2026-09-14 18:33 UTC | 49m |
| WIF6Y | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-14 18:23 UTC | 2026-09-14 18:33 UTC | 10m |
| N787MM |  | Salt Lake City International Airport (KSLC) | Harry Reid International Airport (KLAS) | 2026-09-14 17:30 UTC | 2026-09-14 18:31 UTC | 1h 1m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-09-14 17:48 UTC | 2026-09-14 18:30 UTC | 42m |
| N3049Q |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-14 18:06 UTC | 2026-09-14 18:29 UTC | 23m |
| GOLEM31 | GOL | 75OK (75OK) | Nelson High Point Airport (8OK7) | 2026-09-14 18:15 UTC | 2026-09-14 18:28 UTC | 13m |
| N355HG |  | Midland Airpark (KMDD) | 81NM (81NM) | 2026-09-14 17:54 UTC | 2026-09-14 18:28 UTC | 33m |
| N946MM |  | Charlotte/Douglas International Airport (KCLT) | Orlando Executive Airport (KORL) | 2026-09-14 17:14 UTC | 2026-09-14 18:27 UTC | 1h 13m |
| N911SF |  | Redding Regional Airport (KRDD) | Hayfork Airport (KF62) | 2026-09-14 18:04 UTC | 2026-09-14 18:26 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
