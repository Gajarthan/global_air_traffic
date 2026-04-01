# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_07:22:15_UTC-green)

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

**Latest saved flight:** 2026-04-01 07:22:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 07:22:15 UTC

- **8,232** saved flights
- **5,126** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,232** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **100,253.4 tonnes** estimated CO2 emissions
- **5,811,792 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 298 |
| 3 | IndiGo | 220 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 134 |
| 7 | Lufthansa | 120 |
| 8 | ENY | 116 |
| 9 | AXM | 93 |
| 10 | Vueling | 91 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | Delta Air Lines | 70 |
| 14 | QLK | 69 |
| 15 | All Nippon Airways | 67 |
| 16 | WIF | 64 |
| 17 | VIV | 59 |
| 18 | AXB | 57 |
| 19 | AZU | 57 |
| 20 | Alaska Airlines | 56 |
| 21 | Swiss International | 56 |
| 22 | Japan Airlines | 55 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | Avianca | 46 |
| 28 | EJU | 45 |
| 29 | JST | 44 |
| 30 | easyJet | 43 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7027 |
| 2 | 🇮🇳 IN | 676 |
| 3 | 🇦🇺 AU | 662 |
| 4 | 🇪🇸 ES | 612 |
| 5 | 🇧🇷 BR | 401 |
| 6 | 🇯🇵 JP | 396 |
| 7 | 🇩🇪 DE | 396 |
| 8 | 🇨🇦 CA | 388 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 356 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 268 |
| 13 | 🇫🇷 FR | 234 |
| 14 | 🇳🇴 NO | 209 |
| 15 | 🇲🇾 MY | 208 |
| 16 | 🇳🇿 NZ | 194 |
| 17 | 🇬🇷 GR | 190 |
| 18 | 🇨🇭 CH | 175 |
| 19 | 🇬🇹 GT | 172 |
| 20 | 🇿🇦 ZA | 163 |
| 21 | 🇵🇭 PH | 160 |
| 22 | 🇹🇷 TR | 142 |
| 23 | 🇰🇷 KR | 119 |
| 24 | 🇮🇩 ID | 102 |
| 25 | 🇹🇭 TH | 100 |
| 26 | 🇲🇦 MA | 94 |
| 27 | 🇵🇱 PL | 94 |
| 28 | 🇲🇴 MO | 85 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Denver International Airport |  | US | 155 |
| 3 | Indira Gandhi International Airport |  | IN | 153 |
| 4 | Tokyo International Airport |  | JP | 142 |
| 5 | El Dorado International Airport |  | CO | 132 |
| 6 | La Aurora Airport |  | GT | 121 |
| 7 | Harry Reid International Airport |  | US | 120 |
| 8 | Frankfurt am Main International Airport |  | DE | 120 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 11 | Zurich Airport |  | CH | 90 |
| 12 | Guaymaral Airport |  | CO | 90 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 89 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 15 | Macau International Airport |  | MO | 85 |
| 16 | Chicago O'Hare International Airport |  | US | 84 |
| 17 | Reno/Tahoe International Airport |  | US | 77 |
| 18 | Kuala Lumpur International Airport |  | MY | 77 |
| 19 | Tenerife Norte Airport |  | ES | 76 |
| 20 | Bengaluru International Airport |  | IN | 74 |
| 21 | Ninoy Aquino International Airport |  | PH | 73 |
| 22 | Madrid Barajas International Airport |  | ES | 73 |
| 23 | Charlotte/Douglas International Airport |  | US | 71 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 25 | Daniel K Inouye International Airport |  | US | 66 |
| 26 | Salt Lake City International Airport |  | US | 64 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 63 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 29 | Malpensa International Airport |  | IT | 62 |
| 30 | Vitoria/Foronda Airport |  | ES | 60 |
| 31 | Pune Airport |  | IN | 59 |
| 32 | Seattle-Tacoma International Airport |  | US | 59 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 34 | Miami International Airport |  | US | 57 |
| 35 | Congonhas Airport |  | BR | 57 |
| 36 | Barcelona International Airport |  | ES | 57 |
| 37 | Bodø Airport |  | NO | 54 |
| 38 | Charles de Gaulle International Airport |  | FR | 53 |
| 39 | Centennial Airport |  | US | 53 |
| 40 | Austin-Bergstrom International Airport |  | US | 52 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 32 | 1h 6m | 706 km | 389.6 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 27 | 31m | - | - |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 26 | 1h 45m | 1,156 km | 518.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 25 | 29m | 304 km | 131.1 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 25 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 23 | 15m | 206 km | 81.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 22 | 20m | 165 km | 62.6 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 20 | 1h 26m | 910 km | 313.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 20 | 30m | 369 km | 127.3 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 18 | 53m | 546 km | 169.5 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 16 | 11m | 127 km | 35.0 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LICHEN3 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-01 07:00 UTC | 2026-04-01 07:22 UTC | 22m |
| N106GR |  | Richards Airport (TA47) | Denton Enterprise Airport (KDTO) | 2026-04-01 07:03 UTC | 2026-04-01 07:08 UTC | 5m |
| IGO239V | IndiGo | Indira Gandhi International Airport (VIDP) | VEDG (VEDG) | 2026-04-01 05:23 UTC | 2026-04-01 06:53 UTC | 1h 30m |
| J910KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-04-01 06:27 UTC | 2026-04-01 06:51 UTC | 24m |
| N510MW |  | Adaminaby Airport (YADI) | Benambra Airport (YBRA) | 2026-04-01 06:32 UTC | 2026-04-01 06:51 UTC | 19m |
| IGO2204 | IndiGo | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-04-01 06:33 UTC | 2026-04-01 06:50 UTC | 16m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-04-01 05:55 UTC | 2026-04-01 06:48 UTC | 53m |
| WIF1X | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-04-01 06:43 UTC | 2026-04-01 06:47 UTC | 4m |
| EJU81TD | EJU | Lyon Saint-Exupery Airport (LFLL) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-04-01 05:35 UTC | 2026-04-01 06:41 UTC | 1h 6m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-01 06:17 UTC | 2026-04-01 06:41 UTC | 24m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-01 05:54 UTC | 2026-04-01 06:41 UTC | 47m |
| VOZ660 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Collector Airport (YCLT) | 2026-04-01 06:12 UTC | 2026-04-01 06:40 UTC | 27m |
| VTFTO | VTF | Salem Airport (VOSM) | Mysore Airport (VOMY) | 2026-04-01 05:59 UTC | 2026-04-01 06:39 UTC | 39m |
| AXM5305 | AXM | Kota Kinabalu International Airport (WBKK) | Seletar Airport (WSSL) | 2026-04-01 04:45 UTC | 2026-04-01 06:39 UTC | 1h 53m |
| ZKIME | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-01 06:25 UTC | 2026-04-01 06:34 UTC | 9m |
| J932KT |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-04-01 06:33 UTC | 2026-04-01 06:34 UTC | 1m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Otocac Airport (LDRO) | 2026-04-01 05:31 UTC | 2026-04-01 06:32 UTC | 1h 1m |
| DLH867 | Lufthansa | Oslo Gardermoen Airport (ENGM) | Frankfurt am Main International Airport (EDDF) | 2026-04-01 04:53 UTC | 2026-04-01 06:32 UTC | 1h 38m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-01 05:10 UTC | 2026-04-01 06:31 UTC | 1h 20m |
| AUR756P | AUR | London Gatwick Airport (EGKK) | Newquay Cornwall Airport (EGHQ) | 2026-04-01 05:49 UTC | 2026-04-01 06:29 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
