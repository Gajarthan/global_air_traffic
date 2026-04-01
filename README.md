# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_10:33:25_UTC-green)

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

**Latest saved flight:** 2026-04-01 10:33:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 10:33:25 UTC

- **8,499** saved flights
- **5,238** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,499** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **103,565.5 tonnes** estimated CO2 emissions
- **6,003,795 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 319 |
| 3 | IndiGo | 241 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Lufthansa | 138 |
| 7 | Southwest Airlines | 134 |
| 8 | ENY | 116 |
| 9 | AXM | 100 |
| 10 | Vueling | 94 |
| 11 | LATAM Airlines | 82 |
| 12 | All Nippon Airways | 76 |
| 13 | LXJ | 73 |
| 14 | Delta Air Lines | 71 |
| 15 | QLK | 70 |
| 16 | Swiss International | 65 |
| 17 | WIF | 64 |
| 18 | AXB | 60 |
| 19 | VIV | 59 |
| 20 | AZU | 58 |
| 21 | Japan Airlines | 58 |
| 22 | Alaska Airlines | 56 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | EJU | 48 |
| 28 | easyJet | 48 |
| 29 | Avianca | 46 |
| 30 | JST | 46 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7048 |
| 2 | 🇮🇳 IN | 738 |
| 3 | 🇦🇺 AU | 689 |
| 4 | 🇪🇸 ES | 650 |
| 5 | 🇩🇪 DE | 446 |
| 6 | 🇯🇵 JP | 442 |
| 7 | 🇧🇷 BR | 407 |
| 8 | 🇨🇦 CA | 393 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 377 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 288 |
| 13 | 🇫🇷 FR | 249 |
| 14 | 🇲🇾 MY | 223 |
| 15 | 🇳🇴 NO | 214 |
| 16 | 🇬🇷 GR | 201 |
| 17 | 🇨🇭 CH | 197 |
| 18 | 🇳🇿 NZ | 197 |
| 19 | 🇿🇦 ZA | 173 |
| 20 | 🇬🇹 GT | 172 |
| 21 | 🇵🇭 PH | 162 |
| 22 | 🇰🇷 KR | 151 |
| 23 | 🇹🇷 TR | 145 |
| 24 | 🇮🇩 ID | 114 |
| 25 | 🇹🇭 TH | 109 |
| 26 | 🇵🇱 PL | 99 |
| 27 | 🇲🇦 MA | 98 |
| 28 | 🇲🇴 MO | 87 |
| 29 | 🇳🇱 NL | 79 |
| 30 | 🇲🇪 ME | 78 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Indira Gandhi International Airport |  | IN | 164 |
| 3 | Tokyo International Airport |  | JP | 158 |
| 4 | Denver International Airport |  | US | 155 |
| 5 | Frankfurt am Main International Airport |  | DE | 138 |
| 6 | El Dorado International Airport |  | CO | 132 |
| 7 | La Aurora Airport |  | GT | 121 |
| 8 | Harry Reid International Airport |  | US | 120 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 108 |
| 10 | Zurich Airport |  | CH | 100 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 93 |
| 13 | Guaymaral Airport |  | CO | 90 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 15 | Macau International Airport |  | MO | 87 |
| 16 | Chicago O'Hare International Airport |  | US | 84 |
| 17 | Kuala Lumpur International Airport |  | MY | 82 |
| 18 | Tenerife Norte Airport |  | ES | 81 |
| 19 | Bengaluru International Airport |  | IN | 79 |
| 20 | Reno/Tahoe International Airport |  | US | 77 |
| 21 | Madrid Barajas International Airport |  | ES | 74 |
| 22 | Ninoy Aquino International Airport |  | PH | 73 |
| 23 | Charlotte/Douglas International Airport |  | US | 71 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 70 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 26 | Malpensa International Airport |  | IT | 67 |
| 27 | Daniel K Inouye International Airport |  | US | 66 |
| 28 | Salt Lake City International Airport |  | US | 64 |
| 29 | Pune Airport |  | IN | 63 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 31 | Vitoria/Foronda Airport |  | ES | 62 |
| 32 | Seattle-Tacoma International Airport |  | US | 60 |
| 33 | Barcelona International Airport |  | ES | 60 |
| 34 | Charles de Gaulle International Airport |  | FR | 59 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 36 | Congonhas Airport |  | BR | 58 |
| 37 | Miami International Airport |  | US | 57 |
| 38 | Gimpo International Airport |  | KR | 57 |
| 39 | Bodø Airport |  | NO | 54 |
| 40 | Austin-Bergstrom International Airport |  | US | 53 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 38 | 1h 7m | 706 km | 462.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 28 | 1h 44m | 1,156 km | 558.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 27 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 25 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 24 | 20m | 165 km | 68.3 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 23 | 15m | 206 km | 81.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 21 | 1h 26m | 910 km | 329.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 20 | 30m | 369 km | 127.3 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 18 | 53m | 546 km | 169.5 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 17 | 1h 0m | 723 km | 211.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 13 | 35m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR6848 | Ryanair | Copenhagen Kastrup Airport (EKCH) | Oksywie Military Air Base (EPOK) | 2026-04-01 09:57 UTC | 2026-04-01 10:33 UTC | 35m |
| GFD4 | GFD | Hohn Airport (ETNH) | Wunstorf Airport (ETNW) | 2026-04-01 08:19 UTC | 2026-04-01 10:27 UTC | 2h 7m |
| SEH05O | SEH | Diagoras Airport (LGRP) | Leros Airport (LGLE) | 2026-04-01 10:01 UTC | 2026-04-01 10:24 UTC | 23m |
| PSBUR | PSB | Fazenda Santa Adelina Airport (SSIY) | Ubatuba Airport (SDUB) | 2026-04-01 09:24 UTC | 2026-04-01 10:21 UTC | 57m |
| IGO7126 | IndiGo | Tiruchirapally Civil Airport Airport (VOTR) | Mysore Airport (VOMY) | 2026-04-01 03:30 UTC | 2026-04-01 10:19 UTC | 6h 49m |
| DHK877 | DHK | Leipzig Halle Airport (EDDP) | John F Kennedy International Airport (KJFK) | 2026-04-01 01:30 UTC | 2026-04-01 10:13 UTC | 8h 43m |
| ZXP01 | ZXP | Texel Airport (EHTX) | Texel Airport (EHTX) | 2026-04-01 10:10 UTC | 2026-04-01 10:10 UTC | 0m |
| SUI784 | SUI | Emmen Airport (LSME) | Raron Airport (LSTA) | 2026-04-01 09:45 UTC | 2026-04-01 10:08 UTC | 23m |
| SWR2TM | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-04-01 09:22 UTC | 2026-04-01 10:04 UTC | 42m |
| WMT7GM | WMT | Glasgow International Airport (EGPF) | Malpensa International Airport (LIMC) | 2026-04-01 07:49 UTC | 2026-04-01 10:03 UTC | 2h 14m |
| SWR92T | Swiss International | Palermo / Punta Raisi Airport (LICJ) | Zurich Airport (LSZH) | 2026-04-01 08:19 UTC | 2026-04-01 10:02 UTC | 1h 43m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-01 09:42 UTC | 2026-04-01 10:02 UTC | 20m |
| HTY107 | HTY | Gibraltar Airport (LXGB) | Gibraltar Airport (LXGB) | 2026-04-01 09:54 UTC | 2026-04-01 10:02 UTC | 8m |
| KLM1498 | KLM Royal Dutch | Barcelona International Airport (LEBL) | Rotterdam Airport (EHRD) | 2026-04-01 07:43 UTC | 2026-04-01 10:02 UTC | 2h 19m |
| TRA24M | TRA | Alicante International Airport (LEAL) | Seppe Airport (EHSE) | 2026-04-01 07:20 UTC | 2026-04-01 10:02 UTC | 2h 41m |
| VJC946 | VJC | Incheon International Airport (RKSI) | Kaohsiung International Airport (RCKH) | 2026-04-01 02:09 UTC | 2026-04-01 10:02 UTC | 7h 52m |
| CCM55VN | CCM | Bastia-Poretta Airport (LFKB) | Paris-Orly Airport (LFPO) | 2026-04-01 08:38 UTC | 2026-04-01 10:01 UTC | 1h 23m |
| PBD839 | PBD | Sheremetyevo International Airport (UUEE) | Isparta Airport (LTBM) | 2026-04-01 05:32 UTC | 2026-04-01 10:00 UTC | 4h 28m |
| MRL01F | MRL | San Javier Airport (LELC) | Ontur Airport (LEOT) | 2026-04-01 09:29 UTC | 2026-04-01 09:59 UTC | 29m |
| DLH77Y | Lufthansa | Nice-Cote d'Azur Airport (LFMN) | Frankfurt am Main International Airport (EDDF) | 2026-04-01 08:42 UTC | 2026-04-01 09:58 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
