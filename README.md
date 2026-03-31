# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_08:47:39_UTC-green)

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

**Latest saved flight:** 2026-03-31 08:47:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 08:47:39 UTC

- **6,229** saved flights
- **4,124** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,229** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **78,644.3 tonnes** estimated CO2 emissions
- **4,559,091 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 226 |
| 3 | IndiGo | 163 |
| 4 | EJA | 129 |
| 5 | American Airlines | 122 |
| 6 | Southwest Airlines | 101 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 92 |
| 9 | LATAM Airlines | 68 |
| 10 | AXM | 67 |
| 11 | Vueling | 61 |
| 12 | LXJ | 57 |
| 13 | QLK | 56 |
| 14 | Delta Air Lines | 55 |
| 15 | All Nippon Airways | 50 |
| 16 | Cathay Pacific | 47 |
| 17 | WIF | 47 |
| 18 | United Airlines | 46 |
| 19 | VIV | 46 |
| 20 | Japan Airlines | 44 |
| 21 | AZU | 43 |
| 22 | Swiss International | 43 |
| 23 | AXB | 41 |
| 24 | Alaska Airlines | 40 |
| 25 | EDV | 39 |
| 26 | Avianca | 37 |
| 27 | VOE | 34 |
| 28 | EJU | 33 |
| 29 | MXY | 33 |
| 30 | JST | 32 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5364 |
| 2 | 🇮🇳 IN | 492 |
| 3 | 🇦🇺 AU | 490 |
| 4 | 🇪🇸 ES | 457 |
| 5 | 🇧🇷 BR | 314 |
| 6 | 🇯🇵 JP | 307 |
| 7 | 🇨🇴 CO | 290 |
| 8 | 🇩🇪 DE | 285 |
| 9 | 🇮🇹 IT | 277 |
| 10 | 🇨🇦 CA | 271 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 195 |
| 13 | 🇫🇷 FR | 182 |
| 14 | 🇳🇴 NO | 154 |
| 15 | 🇲🇾 MY | 150 |
| 16 | 🇨🇭 CH | 142 |
| 17 | 🇬🇷 GR | 134 |
| 18 | 🇬🇹 GT | 132 |
| 19 | 🇵🇭 PH | 129 |
| 20 | 🇿🇦 ZA | 127 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 95 |
| 23 | 🇹🇭 TH | 87 |
| 24 | 🇮🇩 ID | 79 |
| 25 | 🇲🇴 MO | 79 |
| 26 | 🇲🇦 MA | 75 |
| 27 | 🇵🇱 PL | 72 |
| 28 | 🇰🇷 KR | 68 |
| 29 | 🇧🇸 BS | 60 |
| 30 | 🇲🇪 ME | 58 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Indira Gandhi International Airport |  | IN | 112 |
| 4 | Tokyo International Airport |  | JP | 108 |
| 5 | El Dorado International Airport |  | CO | 106 |
| 6 | Frankfurt am Main International Airport |  | DE | 92 |
| 7 | La Aurora Airport |  | GT | 90 |
| 8 | Harry Reid International Airport |  | US | 81 |
| 9 | Macau International Airport |  | MO | 79 |
| 10 | Chicago O'Hare International Airport |  | US | 76 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 13 | Zurich Airport |  | CH | 72 |
| 14 | Tenerife Norte Airport |  | ES | 67 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 16 | Guaymaral Airport |  | CO | 65 |
| 17 | Eleftherios Venizelos International Airport |  | GR | 62 |
| 18 | Reno/Tahoe International Airport |  | US | 58 |
| 19 | Ninoy Aquino International Airport |  | PH | 58 |
| 20 | Madrid Barajas International Airport |  | ES | 56 |
| 21 | Bengaluru International Airport |  | IN | 56 |
| 22 | Kuala Lumpur International Airport |  | MY | 53 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 24 | Charlotte/Douglas International Airport |  | US | 50 |
| 25 | Salt Lake City International Airport |  | US | 49 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 49 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 28 | Malpensa International Airport |  | IT | 47 |
| 29 | Charles de Gaulle International Airport |  | FR | 47 |
| 30 | Miami International Airport |  | US | 46 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 45 |
| 32 | Congonhas Airport |  | BR | 45 |
| 33 | Vitoria/Foronda Airport |  | ES | 44 |
| 34 | Seattle-Tacoma International Airport |  | US | 44 |
| 35 | Daniel K Inouye International Airport |  | US | 43 |
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
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 22 | 1h 7m | 706 km | 267.9 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 20 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 18 | 1h 41m | 1,423 km | 441.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 16 | 28m | 304 km | 83.9 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 16 | 1h 49m | 1,156 km | 319.2 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 16 | 21m | 165 km | 45.5 t |
| 13 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 16 | 4m | - | - |
| 14 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 14 | 29m | 275 km | 66.3 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 14 | 1h 25m | 910 km | 219.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 13 | 1h 10m | 770 km | 172.7 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 12 | 1h 46m | 1,290 km | 267.0 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 12 | 29m | - | - |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 12 | 23m | - | - |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAR702 | AAR | Ninoy Aquino International Airport (RPLL) | A 511 Airport (RKSG) | 2026-03-31 05:36 UTC | 2026-03-31 08:47 UTC | 3h 10m |
| QAF5 | QAF | Doha International Airport (OTBD) | Shaibah Airport (OESB) | 2026-03-31 08:07 UTC | 2026-03-31 08:40 UTC | 32m |
| OHPBL | OHP | Lausanne-la Blecherette Airport (LSGL) | Bern Belp Airport (LSZB) | 2026-03-31 08:02 UTC | 2026-03-31 08:35 UTC | 32m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 07:50 UTC | 2026-03-31 08:25 UTC | 35m |
| YGW | YGW | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 07:54 UTC | 2026-03-31 08:23 UTC | 29m |
| CFE3271 | CFE | Madrid Barajas International Airport (LEMD) | London City Airport (EGLC) | 2026-03-31 06:22 UTC | 2026-03-31 08:21 UTC | 1h 59m |
| VOE67LC | VOE | Malaga Airport (LEMG) | La Morgal Airport (LEMR) | 2026-03-31 07:01 UTC | 2026-03-31 08:14 UTC | 1h 12m |
| DRAGO741 | DRA | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Megeve Airport (LFHM) | 2026-03-31 08:01 UTC | 2026-03-31 08:13 UTC | 12m |
| RGA01 | RGA | Zurich Airport (LSZH) | Dubendorf Airport (LSMD) | 2026-03-31 08:04 UTC | 2026-03-31 08:08 UTC | 3m |
| DHK011 | DHK | East Midlands Airport (EGNX) | Macau International Airport (VMMC) | 2026-03-30 20:30 UTC | 2026-03-31 08:01 UTC | 11h 30m |
| VOE9EF | VOE | Malaga Airport (LEMG) | Bilbao Airport (LEBB) | 2026-03-31 06:48 UTC | 2026-03-31 07:59 UTC | 1h 11m |
| AXM6037 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-31 07:41 UTC | 2026-03-31 07:59 UTC | 18m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Lutong Airport (WMLU) | 2026-03-31 07:26 UTC | 2026-03-31 07:56 UTC | 29m |
| RYR50GF | Ryanair | Valencia Airport (LEVC) | Ifrane Airport (GMFI) | 2026-03-31 07:06 UTC | 2026-03-31 07:54 UTC | 48m |
| NOZ1950 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Zemunik Airport (LDZD) | 2026-03-31 05:47 UTC | 2026-03-31 07:53 UTC | 2h 5m |
| QLK1527 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-03-31 07:03 UTC | 2026-03-31 07:52 UTC | 49m |
| EZS1287 | EZS | Mollis Airport (LSZM) | Isparta Airport (LTBM) | 2026-03-31 05:08 UTC | 2026-03-31 07:51 UTC | 2h 42m |
| QLK1581 | QLK | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 2026-03-31 06:28 UTC | 2026-03-31 07:49 UTC | 1h 21m |
| URSA20 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-03-31 06:48 UTC | 2026-03-31 07:48 UTC | 1h 0m |
| LICHEN8 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-03-31 06:38 UTC | 2026-03-31 07:47 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
