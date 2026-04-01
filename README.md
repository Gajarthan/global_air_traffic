# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_00:57:13_UTC-green)

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

**Latest saved flight:** 2026-04-01 00:57:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 00:57:13 UTC

- **7,977** saved flights
- **5,042** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,977** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **97,424.2 tonnes** estimated CO2 emissions
- **5,647,781 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 389 |
| 2 | Ryanair | 293 |
| 3 | IndiGo | 203 |
| 4 | EJA | 171 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 133 |
| 7 | ENY | 116 |
| 8 | Lufthansa | 115 |
| 9 | Vueling | 82 |
| 10 | AXM | 81 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | Delta Air Lines | 70 |
| 14 | All Nippon Airways | 63 |
| 15 | QLK | 62 |
| 16 | VIV | 59 |
| 17 | WIF | 59 |
| 18 | AZU | 56 |
| 19 | Swiss International | 55 |
| 20 | United Airlines | 54 |
| 21 | Alaska Airlines | 53 |
| 22 | EDV | 53 |
| 23 | AXB | 52 |
| 24 | Japan Airlines | 49 |
| 25 | BRC | 48 |
| 26 | Cathay Pacific | 47 |
| 27 | Avianca | 46 |
| 28 | easyJet | 43 |
| 29 | EJU | 42 |
| 30 | JST | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6952 |
| 2 | 🇮🇳 IN | 614 |
| 3 | 🇦🇺 AU | 589 |
| 4 | 🇪🇸 ES | 586 |
| 5 | 🇧🇷 BR | 398 |
| 6 | 🇩🇪 DE | 382 |
| 7 | 🇨🇦 CA | 381 |
| 8 | 🇨🇴 CO | 376 |
| 9 | 🇯🇵 JP | 366 |
| 10 | 🇮🇹 IT | 346 |
| 11 | 🇲🇽 MX | 294 |
| 12 | 🇬🇧 GB | 266 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 198 |
| 15 | 🇲🇾 MY | 182 |
| 16 | 🇳🇿 NZ | 178 |
| 17 | 🇬🇷 GR | 176 |
| 18 | 🇬🇹 GT | 171 |
| 19 | 🇨🇭 CH | 168 |
| 20 | 🇿🇦 ZA | 161 |
| 21 | 🇵🇭 PH | 144 |
| 22 | 🇹🇷 TR | 138 |
| 23 | 🇹🇭 TH | 95 |
| 24 | 🇲🇦 MA | 94 |
| 25 | 🇵🇱 PL | 94 |
| 26 | 🇮🇩 ID | 92 |
| 27 | 🇰🇷 KR | 91 |
| 28 | 🇲🇴 MO | 82 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 199 |
| 2 | Denver International Airport |  | US | 154 |
| 3 | Indira Gandhi International Airport |  | IN | 139 |
| 4 | Tokyo International Airport |  | JP | 130 |
| 5 | El Dorado International Airport |  | CO | 130 |
| 6 | La Aurora Airport |  | GT | 120 |
| 7 | Harry Reid International Airport |  | US | 117 |
| 8 | Frankfurt am Main International Airport |  | DE | 115 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Guaymaral Airport |  | CO | 90 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 12 | Zurich Airport |  | CH | 88 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 85 |
| 14 | Chicago O'Hare International Airport |  | US | 84 |
| 15 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 16 | Macau International Airport |  | MO | 82 |
| 17 | Reno/Tahoe International Airport |  | US | 76 |
| 18 | Tenerife Norte Airport |  | ES | 75 |
| 19 | Charlotte/Douglas International Airport |  | US | 70 |
| 20 | Madrid Barajas International Airport |  | ES | 70 |
| 21 | Bengaluru International Airport |  | IN | 68 |
| 22 | Kuala Lumpur International Airport |  | MY | 67 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 66 |
| 24 | Ninoy Aquino International Airport |  | PH | 65 |
| 25 | Salt Lake City International Airport |  | US | 64 |
| 26 | Daniel K Inouye International Airport |  | US | 63 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 28 | Malpensa International Airport |  | IT | 59 |
| 29 | Vitoria/Foronda Airport |  | ES | 59 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 31 | Seattle-Tacoma International Airport |  | US | 58 |
| 32 | Miami International Airport |  | US | 57 |
| 33 | Pune Airport |  | IN | 57 |
| 34 | Congonhas Airport |  | BR | 57 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 36 | Charles de Gaulle International Airport |  | FR | 52 |
| 37 | Centennial Airport |  | US | 52 |
| 38 | Barcelona International Airport |  | ES | 51 |
| 39 | Austin-Bergstrom International Airport |  | US | 50 |
| 40 | Vancouver International Airport |  | CA | 50 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 35 | 14m | 114 km | 68.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 30 | 24m | 225 km | 116.4 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 29 | 1h 6m | 706 km | 353.1 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 24 | 1h 46m | 1,156 km | 478.8 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 21 | 15m | 206 km | 74.7 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 20 | 29m | 304 km | 104.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 19 | 52m | 556 km | 182.1 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 17 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 17 | 1h 25m | 910 km | 266.8 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 17 | 1h 10m | 770 km | 225.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 17 | 30m | 369 km | 108.2 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 16 | 53m | 546 km | 150.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 14 | 11m | 127 km | 30.6 t |
| 26 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VALOR67 | VAL | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-04-01 00:20 UTC | 2026-04-01 00:57 UTC | 36m |
| R51270 |  | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-03-31 23:53 UTC | 2026-04-01 00:54 UTC | 1h 1m |
| BRG652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-01 00:27 UTC | 2026-04-01 00:53 UTC | 26m |
| N924S |  | William P Hobby Airport (KHOU) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-01 00:03 UTC | 2026-04-01 00:44 UTC | 41m |
| N53977 |  | Bradley Lake Hydroelectric Project Airstrip (0AK7) | Soldotna Airport (PASX) | 2026-04-01 00:24 UTC | 2026-04-01 00:41 UTC | 16m |
| FYC | FYC | Wilton Airport (YWIO) | Wilton Airport (YWIO) | 2026-03-31 23:34 UTC | 2026-04-01 00:35 UTC | 1h 0m |
| TRP7 | TRP | Chesapeake Ranch Airport (MD50) | Joint Base Andrews Airport (KADW) | 2026-04-01 00:09 UTC | 2026-04-01 00:35 UTC | 25m |
| N289CS |  | Page Field (KFMY) | Winter Haven Regional Airport (KGIF) | 2026-03-31 23:40 UTC | 2026-04-01 00:33 UTC | 52m |
| URSA05 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-01 00:13 UTC | 2026-04-01 00:30 UTC | 16m |
| YHU | YHU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 23:51 UTC | 2026-04-01 00:30 UTC | 38m |
| N189DT |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-03-31 20:25 UTC | 2026-04-01 00:24 UTC | 3h 58m |
| WAH | WAH | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-04-01 00:09 UTC | 2026-04-01 00:23 UTC | 14m |
| ZFO | ZFO | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 23:40 UTC | 2026-04-01 00:21 UTC | 40m |
| N479BW |  | Charlotte/Monroe Executive Airport (KEQY) | Mitchell Field (17NC) | 2026-03-31 23:44 UTC | 2026-04-01 00:21 UTC | 36m |
| ASP864 | ASP | Palm Springs International Airport (KPSP) | Vancouver International Airport (CYVR) | 2026-03-31 21:46 UTC | 2026-04-01 00:15 UTC | 2h 28m |
| AXM433 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-03-31 23:44 UTC | 2026-04-01 00:06 UTC | 22m |
| GJS4415 | GJS | Chicago O'Hare International Airport (KORD) | 1PS4 (1PS4) | 2026-03-31 23:01 UTC | 2026-04-01 00:05 UTC | 1h 4m |
| LR453 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-03-31 23:29 UTC | 2026-04-01 00:05 UTC | 35m |
| 8RK |  | Melbourne Essendon Airport (YMEN) | Melbourne Essendon Airport (YMEN) | 2026-03-31 23:34 UTC | 2026-04-01 00:04 UTC | 30m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-03-31 23:35 UTC | 2026-04-01 00:04 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
