# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_07:46:52_UTC-green)

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

**Latest saved flight:** 2026-03-31 07:46:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 07:46:52 UTC

- **6,146** saved flights
- **4,081** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,146** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **77,328.2 tonnes** estimated CO2 emissions
- **4,482,794 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 221 |
| 3 | IndiGo | 162 |
| 4 | EJA | 129 |
| 5 | American Airlines | 122 |
| 6 | Southwest Airlines | 101 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 89 |
| 9 | LATAM Airlines | 68 |
| 10 | AXM | 64 |
| 11 | Vueling | 60 |
| 12 | LXJ | 57 |
| 13 | Delta Air Lines | 55 |
| 14 | QLK | 54 |
| 15 | All Nippon Airways | 48 |
| 16 | Cathay Pacific | 47 |
| 17 | WIF | 47 |
| 18 | United Airlines | 46 |
| 19 | VIV | 46 |
| 20 | AZU | 43 |
| 21 | Japan Airlines | 42 |
| 22 | Swiss International | 41 |
| 23 | Alaska Airlines | 40 |
| 24 | EDV | 39 |
| 25 | AXB | 38 |
| 26 | Avianca | 37 |
| 27 | MXY | 33 |
| 28 | VOE | 32 |
| 29 | EJU | 31 |
| 30 | JST | 31 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5360 |
| 2 | 🇮🇳 IN | 479 |
| 3 | 🇦🇺 AU | 478 |
| 4 | 🇪🇸 ES | 441 |
| 5 | 🇧🇷 BR | 314 |
| 6 | 🇯🇵 JP | 297 |
| 7 | 🇨🇴 CO | 290 |
| 8 | 🇩🇪 DE | 275 |
| 9 | 🇮🇹 IT | 271 |
| 10 | 🇨🇦 CA | 271 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 188 |
| 13 | 🇫🇷 FR | 177 |
| 14 | 🇳🇴 NO | 153 |
| 15 | 🇲🇾 MY | 142 |
| 16 | 🇬🇹 GT | 132 |
| 17 | 🇨🇭 CH | 130 |
| 18 | 🇵🇭 PH | 128 |
| 19 | 🇬🇷 GR | 127 |
| 20 | 🇿🇦 ZA | 127 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 93 |
| 23 | 🇹🇭 TH | 85 |
| 24 | 🇲🇴 MO | 78 |
| 25 | 🇮🇩 ID | 72 |
| 26 | 🇲🇦 MA | 71 |
| 27 | 🇵🇱 PL | 69 |
| 28 | 🇰🇷 KR | 63 |
| 29 | 🇧🇸 BS | 60 |
| 30 | 🇲🇪 ME | 52 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Indira Gandhi International Airport |  | IN | 108 |
| 4 | El Dorado International Airport |  | CO | 106 |
| 5 | Tokyo International Airport |  | JP | 103 |
| 6 | La Aurora Airport |  | GT | 90 |
| 7 | Frankfurt am Main International Airport |  | DE | 89 |
| 8 | Harry Reid International Airport |  | US | 81 |
| 9 | Macau International Airport |  | MO | 78 |
| 10 | Chicago O'Hare International Airport |  | US | 76 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 73 |
| 13 | Zurich Airport |  | CH | 68 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 15 | Tenerife Norte Airport |  | ES | 65 |
| 16 | Guaymaral Airport |  | CO | 65 |
| 17 | Eleftherios Venizelos International Airport |  | GR | 60 |
| 18 | Reno/Tahoe International Airport |  | US | 58 |
| 19 | Ninoy Aquino International Airport |  | PH | 57 |
| 20 | Bengaluru International Airport |  | IN | 55 |
| 21 | Madrid Barajas International Airport |  | ES | 53 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 23 | Kuala Lumpur International Airport |  | MY | 51 |
| 24 | Charlotte/Douglas International Airport |  | US | 50 |
| 25 | Salt Lake City International Airport |  | US | 49 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 49 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 28 | Malpensa International Airport |  | IT | 47 |
| 29 | Miami International Airport |  | US | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 46 |
| 31 | Congonhas Airport |  | BR | 45 |
| 32 | Seattle-Tacoma International Airport |  | US | 44 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 44 |
| 34 | Daniel K Inouye International Airport |  | US | 43 |
| 35 | Vitoria/Foronda Airport |  | ES | 43 |
| 36 | Centennial Airport |  | US | 43 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 38 | O. R. Tambo International Airport |  | ZA | 42 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 40 | Pune Airport |  | IN | 40 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 26 | 24m | 225 km | 100.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 20 | 1h 7m | 706 km | 243.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 20 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 17 | 1h 41m | 1,423 km | 417.2 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 16 | 1h 49m | 1,156 km | 319.2 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 16 | 4m | - | - |
| 12 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 15 | 21m | 165 km | 42.7 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 14 | 28m | 304 km | 73.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 14 | 29m | 275 km | 66.3 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 14 | 1h 25m | 910 km | 219.7 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 13 | 53m | 546 km | 122.4 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 13 | 1h 10m | 770 km | 172.7 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 24 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 12 | 29m | - | - |
| 25 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 11 | 1h 46m | 1,290 km | 244.8 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 11 | 24m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QAF7 | QAF | Doha International Airport (OTBD) | Shaibah Airport (OESB) | 2026-03-31 07:16 UTC | 2026-03-31 07:46 UTC | 30m |
| SAS755 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-03-31 06:45 UTC | 2026-03-31 07:34 UTC | 48m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-03-31 07:27 UTC | 2026-03-31 07:32 UTC | 5m |
| N41GA |  | Bob Hope Airport (KBUR) | Weed Airport (KO46) | 2026-03-31 05:46 UTC | 2026-03-31 07:31 UTC | 1h 45m |
| FDA133 | FDA | Matsumoto Airport (RJAF) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-03-31 04:12 UTC | 2026-03-31 07:23 UTC | 3h 11m |
| N959UA |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-03-31 06:15 UTC | 2026-03-31 07:22 UTC | 1h 7m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 06:39 UTC | 2026-03-31 07:20 UTC | 41m |
| KZN | KZN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-03-31 06:18 UTC | 2026-03-31 07:20 UTC | 1h 1m |
| YVG | YVG | Perth Jandakot Airport (YPJT) | Dalwallinu Airport (YDWU) | 2026-03-31 06:29 UTC | 2026-03-31 07:18 UTC | 49m |
| SRR6118 | SRR | Munich International Airport (EDDM) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-31 05:12 UTC | 2026-03-31 07:18 UTC | 2h 5m |
| ECODU | ECO | Valencia Airport (LEVC) | Valladolid Airport (LEVD) | 2026-03-31 06:35 UTC | 2026-03-31 07:17 UTC | 41m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-03-31 07:04 UTC | 2026-03-31 07:16 UTC | 12m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 06:48 UTC | 2026-03-31 07:16 UTC | 28m |
| JOKER17 | JOK | Niederstetten Airport (ETHN) | Laupheim Airport (ETHL) | 2026-03-31 06:40 UTC | 2026-03-31 07:15 UTC | 34m |
| SAS98K | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-03-31 05:59 UTC | 2026-03-31 07:14 UTC | 1h 14m |
| LKF | LKF | Perth Jandakot Airport (YPJT) | Dalwallinu Airport (YDWU) | 2026-03-31 06:29 UTC | 2026-03-31 07:13 UTC | 43m |
| N424PE |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-03-31 06:06 UTC | 2026-03-31 07:12 UTC | 1h 6m |
| VTFTO | VTF | Salem Airport (VOSM) | Mysore Airport (VOMY) | 2026-03-31 06:34 UTC | 2026-03-31 07:10 UTC | 36m |
| KAL799T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-03-31 06:41 UTC | 2026-03-31 07:07 UTC | 25m |
| CLX4971 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-03-30 19:58 UTC | 2026-03-31 07:04 UTC | 11h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
