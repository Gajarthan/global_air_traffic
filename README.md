# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_23:41:52_UTC-green)

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

**Latest saved flight:** 2026-04-01 23:41:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 23:41:52 UTC

- **10,073** saved flights
- **5,999** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,073** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **122,362.3 tonnes** estimated CO2 emissions
- **7,093,464 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 468 |
| 2 | Ryanair | 383 |
| 3 | IndiGo | 264 |
| 4 | EJA | 215 |
| 5 | American Airlines | 186 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 158 |
| 8 | ENY | 139 |
| 9 | Vueling | 106 |
| 10 | LATAM Airlines | 104 |
| 11 | AXM | 103 |
| 12 | LXJ | 98 |
| 13 | Delta Air Lines | 86 |
| 14 | All Nippon Airways | 80 |
| 15 | QLK | 80 |
| 16 | WIF | 80 |
| 17 | Swiss International | 73 |
| 18 | AZU | 71 |
| 19 | VIV | 70 |
| 20 | Alaska Airlines | 65 |
| 21 | EDV | 65 |
| 22 | United Airlines | 65 |
| 23 | AXB | 63 |
| 24 | Avianca | 60 |
| 25 | Japan Airlines | 60 |
| 26 | BRC | 58 |
| 27 | Cathay Pacific | 57 |
| 28 | easyJet | 57 |
| 29 | EJU | 55 |
| 30 | AEE | 51 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8430 |
| 2 | 🇮🇳 IN | 812 |
| 3 | 🇦🇺 AU | 771 |
| 4 | 🇪🇸 ES | 766 |
| 5 | 🇧🇷 BR | 532 |
| 6 | 🇩🇪 DE | 527 |
| 7 | 🇨🇴 CO | 514 |
| 8 | 🇨🇦 CA | 493 |
| 9 | 🇯🇵 JP | 465 |
| 10 | 🇮🇹 IT | 438 |
| 11 | 🇲🇽 MX | 367 |
| 12 | 🇬🇧 GB | 352 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇲🇾 MY | 231 |
| 16 | 🇬🇷 GR | 227 |
| 17 | 🇳🇿 NZ | 226 |
| 18 | 🇨🇭 CH | 225 |
| 19 | 🇬🇹 GT | 209 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 182 |
| 22 | 🇹🇷 TR | 163 |
| 23 | 🇰🇷 KR | 161 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 117 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇴 MO | 101 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 250 |
| 2 | Denver International Airport |  | US | 187 |
| 3 | Indira Gandhi International Airport |  | IN | 179 |
| 4 | El Dorado International Airport |  | CO | 168 |
| 5 | Tokyo International Airport |  | JP | 166 |
| 6 | Frankfurt am Main International Airport |  | DE | 166 |
| 7 | Guaymaral Airport |  | CO | 148 |
| 8 | La Aurora Airport |  | GT | 146 |
| 9 | Harry Reid International Airport |  | US | 140 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 122 |
| 11 | Zurich Airport |  | CH | 113 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 112 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 15 | Chicago O'Hare International Airport |  | US | 105 |
| 16 | Macau International Airport |  | MO | 101 |
| 17 | Charlotte/Douglas International Airport |  | US | 92 |
| 18 | Tenerife Norte Airport |  | ES | 92 |
| 19 | Reno/Tahoe International Airport |  | US | 91 |
| 20 | Madrid Barajas International Airport |  | ES | 91 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 88 |
| 22 | Bengaluru International Airport |  | IN | 87 |
| 23 | Kuala Lumpur International Airport |  | MY | 85 |
| 24 | Ninoy Aquino International Airport |  | PH | 83 |
| 25 | Congonhas Airport |  | BR | 81 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 76 |
| 27 | Salt Lake City International Airport |  | US | 75 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 75 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 30 | Malpensa International Airport |  | IT | 73 |
| 31 | Daniel K Inouye International Airport |  | US | 72 |
| 32 | Vitoria/Foronda Airport |  | ES | 71 |
| 33 | Pune Airport |  | IN | 71 |
| 34 | Seattle-Tacoma International Airport |  | US | 70 |
| 35 | Austin-Bergstrom International Airport |  | US | 69 |
| 36 | Charles de Gaulle International Airport |  | FR | 69 |
| 37 | Barcelona International Airport |  | ES | 69 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 65 |
| 40 | Bodø Airport |  | NO | 65 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 46 | 14m | 114 km | 90.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 36 | 24m | 225 km | 139.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 31 | 30m | 304 km | 162.5 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 31 | 1h 44m | 1,156 km | 618.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 27 | 53m | 556 km | 258.8 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 25 | 15m | 206 km | 88.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 23 | 30m | 369 km | 146.4 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 19 | 1h 55m | 1,304 km | 427.5 t |
| 22 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 15 | 54m | 630 km | 162.9 t |
| 29 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 30 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 15 | 18m | 26 km | 6.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGDLI | CGD | Ottawa / Macdonald-Cartier International Airport (CYOW) | Billy Bishop Toronto City Airport (CYTZ) | 2026-04-01 22:21 UTC | 2026-04-01 23:41 UTC | 1h 20m |
| N2463S |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-01 22:41 UTC | 2026-04-01 23:41 UTC | 1h 0m |
| LOK | LOK | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-04-01 22:54 UTC | 2026-04-01 23:34 UTC | 40m |
| EXV | EXV | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-01 23:11 UTC | 2026-04-01 23:29 UTC | 17m |
| N182HE |  | FL47 (FL47) | Wauchula Municipal Airport (KCHN) | 2026-04-01 22:20 UTC | 2026-04-01 23:27 UTC | 1h 7m |
| FOJ | FOJ | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-04-01 23:05 UTC | 2026-04-01 23:25 UTC | 19m |
| N496MW |  | Gillespie Field (KSEE) | Flying T Ranch Airport (CA76) | 2026-04-01 23:05 UTC | 2026-04-01 23:15 UTC | 10m |
| MJO | MJO | Tangalooma Resort Airport (YXTA) | Tangalooma Resort Airport (YXTA) | 2026-04-01 22:51 UTC | 2026-04-01 23:14 UTC | 23m |
| N420FJ |  | 27CO (27CO) | Telluride Regional Airport (KTEX) | 2026-04-01 22:58 UTC | 2026-04-01 23:12 UTC | 13m |
| WSN1 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-01 22:31 UTC | 2026-04-01 23:12 UTC | 40m |
| N166RD |  | Merle K (Mudhole) Smith Airport (PACV) | Ketchikan International Airport (PAKT) | 2026-04-01 21:54 UTC | 2026-04-01 23:11 UTC | 1h 16m |
| CPA040 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-04-01 18:48 UTC | 2026-04-01 23:10 UTC | 4h 22m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-01 11:31 UTC | 2026-04-01 23:09 UTC | 11h 38m |
| AXM6413 | AXM | Ulu Bernam Airport (WMBF) | Batu Pahat Airport (WMAB) | 2026-04-01 22:41 UTC | 2026-04-01 23:07 UTC | 25m |
| MRNR11 | MRN | RAAF Base Edinburgh (YPED) | Loxton Airport (YLOX) | 2026-04-01 22:48 UTC | 2026-04-01 23:06 UTC | 18m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bombala Airport (YBOM) | 2026-04-01 22:23 UTC | 2026-04-01 23:06 UTC | 42m |
| CXK245 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-01 22:58 UTC | 2026-04-01 23:05 UTC | 7m |
| N661BP |  | Meadows Field (KBFL) | Bishop Airport (KBIH) | 2026-04-01 22:40 UTC | 2026-04-01 23:03 UTC | 22m |
| OXF2477 | OXF | Falcon Field (KFFZ) | Coolidge Municipal Airport (KP08) | 2026-04-01 21:46 UTC | 2026-04-01 23:03 UTC | 1h 16m |
| CSI571 | CSI | Albuquerque International Sunport Airport (KABQ) | Telluride Regional Airport (KTEX) | 2026-04-01 22:31 UTC | 2026-04-01 23:02 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
