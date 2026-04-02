# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_14:26:25_UTC-green)

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

**Latest saved flight:** 2026-04-02 14:26:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 14:26:25 UTC

- **11,002** saved flights
- **6,368** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,002** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **136,359.3 tonnes** estimated CO2 emissions
- **7,904,887 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 435 |
| 3 | IndiGo | 315 |
| 4 | EJA | 215 |
| 5 | American Airlines | 191 |
| 6 | Lufthansa | 181 |
| 7 | Southwest Airlines | 165 |
| 8 | ENY | 139 |
| 9 | AXM | 120 |
| 10 | Vueling | 120 |
| 11 | LATAM Airlines | 113 |
| 12 | All Nippon Airways | 103 |
| 13 | LXJ | 101 |
| 14 | QLK | 99 |
| 15 | WIF | 91 |
| 16 | Delta Air Lines | 86 |
| 17 | Swiss International | 86 |
| 18 | AZU | 79 |
| 19 | AXB | 77 |
| 20 | Japan Airlines | 77 |
| 21 | VIV | 76 |
| 22 | Alaska Airlines | 72 |
| 23 | Cathay Pacific | 68 |
| 24 | EDV | 66 |
| 25 | easyJet | 66 |
| 26 | United Airlines | 66 |
| 27 | EJU | 64 |
| 28 | BRC | 63 |
| 29 | Avianca | 61 |
| 30 | AEE | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8657 |
| 2 | 🇮🇳 IN | 972 |
| 3 | 🇦🇺 AU | 904 |
| 4 | 🇪🇸 ES | 869 |
| 5 | 🇩🇪 DE | 625 |
| 6 | 🇯🇵 JP | 591 |
| 7 | 🇧🇷 BR | 584 |
| 8 | 🇨🇴 CO | 542 |
| 9 | 🇨🇦 CA | 516 |
| 10 | 🇮🇹 IT | 494 |
| 11 | 🇬🇧 GB | 415 |
| 12 | 🇲🇽 MX | 392 |
| 13 | 🇫🇷 FR | 358 |
| 14 | 🇳🇴 NO | 291 |
| 15 | 🇬🇷 GR | 275 |
| 16 | 🇲🇾 MY | 272 |
| 17 | 🇨🇭 CH | 267 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 229 |
| 20 | 🇬🇹 GT | 213 |
| 21 | 🇵🇭 PH | 212 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 183 |
| 24 | 🇵🇱 PL | 147 |
| 25 | 🇹🇭 TH | 146 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇴 MO | 133 |
| 28 | 🇲🇦 MA | 128 |
| 29 | 🇲🇪 ME | 109 |
| 30 | 🇳🇱 NL | 108 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 253 |
| 2 | Tokyo International Airport |  | JP | 213 |
| 3 | Indira Gandhi International Airport |  | IN | 210 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | El Dorado International Airport |  | CO | 182 |
| 6 | Frankfurt am Main International Airport |  | DE | 180 |
| 7 | Harry Reid International Airport |  | US | 152 |
| 8 | Guaymaral Airport |  | CO | 149 |
| 9 | La Aurora Airport |  | GT | 149 |
| 10 | Macau International Airport |  | MO | 133 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 127 |
| 13 | Zurich Airport |  | CH | 127 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 15 | Bengaluru International Airport |  | IN | 107 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 17 | Chicago O'Hare International Airport |  | US | 106 |
| 18 | Kuala Lumpur International Airport |  | MY | 104 |
| 19 | Tenerife Norte Airport |  | ES | 100 |
| 20 | Madrid Barajas International Airport |  | ES | 98 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 96 |
| 22 | Reno/Tahoe International Airport |  | US | 95 |
| 23 | Ninoy Aquino International Airport |  | PH | 95 |
| 24 | Charlotte/Douglas International Airport |  | US | 94 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 91 |
| 26 | Congonhas Airport |  | BR | 87 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 85 |
| 28 | Malpensa International Airport |  | IT | 83 |
| 29 | Daniel K Inouye International Airport |  | US | 82 |
| 30 | Vitoria/Foronda Airport |  | ES | 81 |
| 31 | Pune Airport |  | IN | 78 |
| 32 | Barcelona International Airport |  | ES | 78 |
| 33 | Charles de Gaulle International Airport |  | FR | 77 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 35 | Gimpo International Airport |  | KR | 75 |
| 36 | Salt Lake City International Airport |  | US | 75 |
| 37 | Bodø Airport |  | NO | 74 |
| 38 | Austin-Bergstrom International Airport |  | US | 72 |
| 39 | Seattle-Tacoma International Airport |  | US | 72 |
| 40 | Calgary International Airport |  | CA | 68 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 51 | 14m | 114 km | 100.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 36 | 1h 46m | 1,156 km | 718.2 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 34 | 4m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 32 | 30m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 12 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 28 | 15m | 206 km | 99.5 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 23 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 22 | 1h 57m | 1,304 km | 494.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 16 | 20m | 147 km | 40.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR468 | VAR | Phoenix Goodyear Airport (KGYR) | Glendale Regional Airport (KGEU) | 2026-04-02 14:06 UTC | 2026-04-02 14:26 UTC | 19m |
| KENT25 | KEN | 4TA5 (4TA5) | Wildlife/Stroud Airport (TS80) | 2026-04-02 13:48 UTC | 2026-04-02 14:17 UTC | 28m |
| TEST01 | TES | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-04-02 12:41 UTC | 2026-04-02 14:16 UTC | 1h 35m |
| HBZYJ | HBZ | Megeve Airport (LFHM) | Bex Airport (LSGB) | 2026-04-02 13:50 UTC | 2026-04-02 14:15 UTC | 25m |
| N1625Q |  | Knoxville Downtown Island Airport (KDKX) | Mc Ghee Tyson Airport (KTYS) | 2026-04-02 13:38 UTC | 2026-04-02 14:13 UTC | 35m |
| BRCAT06 | BRC | Roswell Air Center Airport (KROW) | 81NM (81NM) | 2026-04-02 13:22 UTC | 2026-04-02 14:12 UTC | 49m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-02 13:40 UTC | 2026-04-02 14:12 UTC | 32m |
| PRE315 | PRE | Rocky Mountain Metro Airport (KBJC) | Vowers Ranch Airport (WY29) | 2026-04-02 13:35 UTC | 2026-04-02 14:11 UTC | 36m |
| GKINL | GKI | Duxford Airport (EGSU) | Duxford Airport (EGSU) | 2026-04-02 14:02 UTC | 2026-04-02 14:11 UTC | 8m |
| DLH065 | Lufthansa | Dresden Airport (EDDC) | Fulda-Jossa Airport (EDGF) | 2026-04-02 13:24 UTC | 2026-04-02 14:05 UTC | 40m |
| TKJ9SV | TKJ | Sabiha Gokcen International Airport (LTFJ) | Altena-Hegenscheid Airport (EDKD) | 2026-04-02 11:18 UTC | 2026-04-02 14:05 UTC | 2h 47m |
| BRCAT13 | BRC | Roswell Air Center Airport (KROW) | 2 X 4 Ranch Airport (NM47) | 2026-04-02 13:37 UTC | 2026-04-02 14:02 UTC | 25m |
| ERU973 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-02 13:04 UTC | 2026-04-02 14:02 UTC | 57m |
| N520AF |  | Morristown Municipal Airport (KMMU) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-02 12:39 UTC | 2026-04-02 13:56 UTC | 1h 17m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-04-02 13:33 UTC | 2026-04-02 13:54 UTC | 21m |
| NOZ816 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Stockholm-Arlanda Airport (ESSA) | 2026-04-02 13:11 UTC | 2026-04-02 13:53 UTC | 42m |
| FHGTJ | FHG | Aix-en-Provence (BA 114) Airport (LFMA) | Aix-en-Provence (BA 114) Airport (LFMA) | 2026-04-02 13:37 UTC | 2026-04-02 13:52 UTC | 15m |
| CJT918 | CJT | Cincinnati/Northern Kentucky International Airport (KCVG) | Calgary International Airport (CYYC) | 2026-04-02 10:26 UTC | 2026-04-02 13:51 UTC | 3h 25m |
| BRCAT03 | BRC | Jenkins Airport (NM87) | 2 X 4 Ranch Airport (NM47) | 2026-04-02 13:26 UTC | 2026-04-02 13:51 UTC | 25m |
| PHGLD | PHG | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-04-02 12:58 UTC | 2026-04-02 13:50 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
