# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_11:39:27_UTC-green)

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

**Latest saved flight:** 2026-04-01 11:39:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 11:39:27 UTC

- **8,592** saved flights
- **5,277** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,592** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **104,832.8 tonnes** estimated CO2 emissions
- **6,077,261 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 330 |
| 3 | IndiGo | 247 |
| 4 | EJA | 175 |
| 5 | American Airlines | 154 |
| 6 | Lufthansa | 145 |
| 7 | Southwest Airlines | 134 |
| 8 | ENY | 116 |
| 9 | AXM | 102 |
| 10 | Vueling | 95 |
| 11 | LATAM Airlines | 84 |
| 12 | All Nippon Airways | 78 |
| 13 | LXJ | 73 |
| 14 | Delta Air Lines | 72 |
| 15 | QLK | 70 |
| 16 | WIF | 66 |
| 17 | Swiss International | 65 |
| 18 | AXB | 60 |
| 19 | Japan Airlines | 60 |
| 20 | AZU | 59 |
| 21 | VIV | 59 |
| 22 | Alaska Airlines | 56 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | easyJet | 50 |
| 26 | BRC | 49 |
| 27 | Cathay Pacific | 48 |
| 28 | EJU | 48 |
| 29 | Avianca | 47 |
| 30 | JST | 46 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7061 |
| 2 | 🇮🇳 IN | 754 |
| 3 | 🇦🇺 AU | 691 |
| 4 | 🇪🇸 ES | 669 |
| 5 | 🇩🇪 DE | 461 |
| 6 | 🇯🇵 JP | 455 |
| 7 | 🇧🇷 BR | 417 |
| 8 | 🇨🇦 CA | 395 |
| 9 | 🇮🇹 IT | 385 |
| 10 | 🇨🇴 CO | 382 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 302 |
| 13 | 🇫🇷 FR | 250 |
| 14 | 🇲🇾 MY | 228 |
| 15 | 🇳🇴 NO | 218 |
| 16 | 🇬🇷 GR | 203 |
| 17 | 🇨🇭 CH | 202 |
| 18 | 🇳🇿 NZ | 197 |
| 19 | 🇿🇦 ZA | 183 |
| 20 | 🇬🇹 GT | 172 |
| 21 | 🇵🇭 PH | 166 |
| 22 | 🇰🇷 KR | 156 |
| 23 | 🇹🇷 TR | 147 |
| 24 | 🇮🇩 ID | 117 |
| 25 | 🇹🇭 TH | 110 |
| 26 | 🇵🇱 PL | 101 |
| 27 | 🇲🇦 MA | 98 |
| 28 | 🇲🇴 MO | 88 |
| 29 | 🇳🇱 NL | 79 |
| 30 | 🇲🇪 ME | 79 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Indira Gandhi International Airport |  | IN | 166 |
| 3 | Tokyo International Airport |  | JP | 163 |
| 4 | Denver International Airport |  | US | 155 |
| 5 | Frankfurt am Main International Airport |  | DE | 145 |
| 6 | El Dorado International Airport |  | CO | 133 |
| 7 | Harry Reid International Airport |  | US | 121 |
| 8 | La Aurora Airport |  | GT | 121 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 108 |
| 10 | Zurich Airport |  | CH | 101 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 94 |
| 13 | Guaymaral Airport |  | CO | 90 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 89 |
| 15 | Macau International Airport |  | MO | 88 |
| 16 | Tenerife Norte Airport |  | ES | 85 |
| 17 | Chicago O'Hare International Airport |  | US | 84 |
| 18 | Kuala Lumpur International Airport |  | MY | 84 |
| 19 | Bengaluru International Airport |  | IN | 80 |
| 20 | Reno/Tahoe International Airport |  | US | 77 |
| 21 | Madrid Barajas International Airport |  | ES | 77 |
| 22 | Ninoy Aquino International Airport |  | PH | 75 |
| 23 | Charlotte/Douglas International Airport |  | US | 72 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 71 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 26 | Malpensa International Airport |  | IT | 67 |
| 27 | Daniel K Inouye International Airport |  | US | 66 |
| 28 | Pune Airport |  | IN | 64 |
| 29 | Salt Lake City International Airport |  | US | 64 |
| 30 | Vitoria/Foronda Airport |  | ES | 63 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 32 | Congonhas Airport |  | BR | 61 |
| 33 | Barcelona International Airport |  | ES | 61 |
| 34 | Charles de Gaulle International Airport |  | FR | 60 |
| 35 | Seattle-Tacoma International Airport |  | US | 60 |
| 36 | Gimpo International Airport |  | KR | 59 |
| 37 | Miami International Airport |  | US | 58 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 39 | Bodø Airport |  | NO | 56 |
| 40 | Austin-Bergstrom International Airport |  | US | 53 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 28 | 1h 44m | 1,156 km | 558.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 28 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 26 | 4m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 23 | 15m | 206 km | 81.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 22 | 1h 26m | 910 km | 345.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 17 | 1h 0m | 723 km | 211.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 25 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 28 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 14 | 34m | 431 km | 104.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL1269 | Delta Air Lines | Philadelphia International Airport (KPHL) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-04-01 10:05 UTC | 2026-04-01 11:39 UTC | 1h 33m |
| LCO1503 | LCO | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-04-01 02:53 UTC | 2026-04-01 11:32 UTC | 8h 39m |
| EJA326 | EJA | Dallas Love Field (KDAL) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-01 10:13 UTC | 2026-04-01 11:15 UTC | 1h 2m |
| FNG8 | FNG | Turku Airport (EFTU) | Kymi Airport (EFKY) | 2026-04-01 10:20 UTC | 2026-04-01 11:13 UTC | 52m |
| ERU885 | ERU | Daytona Beach International Airport (KDAB) | Earle Airpark (13FA) | 2026-04-01 10:17 UTC | 2026-04-01 11:07 UTC | 50m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-01 10:05 UTC | 2026-04-01 11:03 UTC | 57m |
| EZY9 | easyJet | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-04-01 10:06 UTC | 2026-04-01 11:00 UTC | 54m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Catanduva Airport (SDCD) | 2026-04-01 10:20 UTC | 2026-04-01 10:57 UTC | 36m |
| JAL377 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-01 09:40 UTC | 2026-04-01 10:56 UTC | 1h 15m |
| IGO6393 | IndiGo | Juhu Aerodrome (VAJJ) | Kalka Airport (VI71) | 2026-04-01 09:19 UTC | 2026-04-01 10:56 UTC | 1h 36m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-04-01 09:50 UTC | 2026-04-01 10:52 UTC | 1h 2m |
| DMDGD | DMD | Eggenfelden Airport (EDME) | Eggenfelden Airport (EDME) | 2026-04-01 10:38 UTC | 2026-04-01 10:51 UTC | 12m |
| UNI135 | UNI | Cologne Bonn Airport (EDDK) | Hoefen Airport (LOIR) | 2026-04-01 10:08 UTC | 2026-04-01 10:50 UTC | 41m |
| WIF808 | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-04-01 10:44 UTC | 2026-04-01 10:49 UTC | 5m |
| RYR9UM | Ryanair | Vilnius International Airport (EYVI) | Lauf-Lillinghof Airport (EDQI) | 2026-04-01 09:07 UTC | 2026-04-01 10:48 UTC | 1h 40m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-01 10:16 UTC | 2026-04-01 10:48 UTC | 32m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-04-01 10:38 UTC | 2026-04-01 10:48 UTC | 9m |
| AIC4EP | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-04-01 10:29 UTC | 2026-04-01 10:47 UTC | 17m |
| LOT3LD | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Berane Airport (LYBR) | 2026-04-01 09:16 UTC | 2026-04-01 10:45 UTC | 1h 28m |
| ZSRAF | ZSR | Rand Airport (FAGM) | Vrede Airport (FAVD) | 2026-04-01 10:21 UTC | 2026-04-01 10:45 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
