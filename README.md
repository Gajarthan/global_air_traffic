# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_10:02:10_UTC-green)

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

**Latest saved flight:** 2026-04-03 10:02:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 10:02:10 UTC

- **12,988** saved flights
- **7,293** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,988** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **161,510.7 tonnes** estimated CO2 emissions
- **9,362,939 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 493 |
| 3 | IndiGo | 362 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 203 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 135 |
| 10 | AXM | 134 |
| 11 | LATAM Airlines | 130 |
| 12 | QLK | 122 |
| 13 | All Nippon Airways | 120 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 102 |
| 16 | Swiss International | 100 |
| 17 | WIF | 97 |
| 18 | AZU | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Cathay Pacific | 85 |
| 22 | Japan Airlines | 85 |
| 23 | AXB | 84 |
| 24 | United Airlines | 84 |
| 25 | EDV | 78 |
| 26 | easyJet | 78 |
| 27 | EJU | 76 |
| 28 | ANZ | 72 |
| 29 | BRC | 72 |
| 30 | Avianca | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10360 |
| 2 | 🇮🇳 IN | 1117 |
| 3 | 🇦🇺 AU | 1072 |
| 4 | 🇪🇸 ES | 985 |
| 5 | 🇧🇷 BR | 713 |
| 6 | 🇩🇪 DE | 698 |
| 7 | 🇯🇵 JP | 696 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 605 |
| 10 | 🇮🇹 IT | 577 |
| 11 | 🇬🇧 GB | 487 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 429 |
| 14 | 🇨🇭 CH | 329 |
| 15 | 🇬🇷 GR | 328 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇳🇴 NO | 305 |
| 18 | 🇲🇾 MY | 300 |
| 19 | 🇵🇭 PH | 260 |
| 20 | 🇿🇦 ZA | 259 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇹🇷 TR | 233 |
| 23 | 🇰🇷 KR | 233 |
| 24 | 🇵🇱 PL | 180 |
| 25 | 🇹🇭 TH | 171 |
| 26 | 🇮🇩 ID | 162 |
| 27 | 🇲🇴 MO | 155 |
| 28 | 🇲🇦 MA | 153 |
| 29 | 🇲🇪 ME | 130 |
| 30 | 🇧🇸 BS | 128 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 242 |
| 3 | Indira Gandhi International Airport |  | IN | 239 |
| 4 | Denver International Airport |  | US | 233 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 192 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 10 | Zurich Airport |  | CH | 158 |
| 11 | Macau International Airport |  | MO | 155 |
| 12 | Guaymaral Airport |  | CO | 153 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 149 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Bengaluru International Airport |  | IN | 125 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 118 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 20 | Madrid Barajas International Airport |  | ES | 113 |
| 21 | Charlotte/Douglas International Airport |  | US | 112 |
| 22 | Kuala Lumpur International Airport |  | MY | 109 |
| 23 | Congonhas Airport |  | BR | 109 |
| 24 | Tenerife Norte Airport |  | ES | 107 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 100 |
| 26 | Salt Lake City International Airport |  | US | 98 |
| 27 | Daniel K Inouye International Airport |  | US | 97 |
| 28 | Reno/Tahoe International Airport |  | US | 97 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 30 | Vitoria/Foronda Airport |  | ES | 94 |
| 31 | Malpensa International Airport |  | IT | 93 |
| 32 | Charles de Gaulle International Airport |  | FR | 92 |
| 33 | Barcelona International Airport |  | ES | 91 |
| 34 | Pune Airport |  | IN | 88 |
| 35 | Seattle-Tacoma International Airport |  | US | 86 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 37 | Austin-Bergstrom International Airport |  | US | 85 |
| 38 | Gimpo International Airport |  | KR | 84 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 58 | 1h 7m | 706 km | 706.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 45 | 29m | 304 km | 235.9 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 40 | 1h 46m | 1,156 km | 798.0 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 34 | 1h 26m | 910 km | 533.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 30 | 28m | 275 km | 142.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 30 | 53m | 546 km | 282.5 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 28 | 30m | 369 km | 178.2 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 25 | 1h 10m | 770 km | 332.1 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 23 | 23m | 252 km | 99.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 22 | 20m | 147 km | 55.7 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 21 | 44m | 452 km | 163.7 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKIME | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-03 09:43 UTC | 2026-04-03 10:02 UTC | 18m |
| SYERSTON | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-04-03 09:43 UTC | 2026-04-03 10:00 UTC | 17m |
| CLX4324 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-04-02 17:39 UTC | 2026-04-03 09:47 UTC | 16h 7m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-03 09:32 UTC | 2026-04-03 09:42 UTC | 10m |
| QFA81D | Qantas | Sydney Kingsford Smith International Airport (YSSY) | Changi Air Base (WSAC) | 2026-04-03 01:53 UTC | 2026-04-03 09:36 UTC | 7h 42m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-04-03 09:27 UTC | 2026-04-03 09:35 UTC | 7m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-04-03 09:01 UTC | 2026-04-03 09:35 UTC | 33m |
| NAK317 | NAK | Paray Le Monial Airport (LFGN) | Lyon-Bron Airport (LFLY) | 2026-04-03 08:56 UTC | 2026-04-03 09:31 UTC | 34m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-03 09:04 UTC | 2026-04-03 09:28 UTC | 24m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-04-03 08:51 UTC | 2026-04-03 09:27 UTC | 36m |
| NHZ25 | NHZ | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-04-03 08:34 UTC | 2026-04-03 09:26 UTC | 52m |
| OEFBW | OEF | Zell Am See Airport (LOWZ) | Zell Am See Airport (LOWZ) | 2026-04-03 09:04 UTC | 2026-04-03 09:24 UTC | 20m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-04-03 08:58 UTC | 2026-04-03 09:23 UTC | 24m |
| MAC265W | MAC | Mohammed V International Airport (GMMN) | Dittingen Airport (LSPD) | 2026-04-03 06:06 UTC | 2026-04-03 09:21 UTC | 3h 14m |
| ZSFON | ZSF | Rand Airport (FAGM) | Rooiberg Airport (FARO) | 2026-04-03 08:56 UTC | 2026-04-03 09:21 UTC | 25m |
| KAL799T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-03 08:57 UTC | 2026-04-03 09:20 UTC | 22m |
| SWR2GE | Swiss International | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-04-03 08:29 UTC | 2026-04-03 09:19 UTC | 50m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Ålesund Airport (ENAL) | 2026-04-03 08:49 UTC | 2026-04-03 09:19 UTC | 30m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-03 08:27 UTC | 2026-04-03 09:18 UTC | 51m |
| FHBTI | FHB | Toussus-le-Noble Airport (LFPN) | Etampes Mondesir Airport (LFOX) | 2026-04-03 08:22 UTC | 2026-04-03 09:18 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
