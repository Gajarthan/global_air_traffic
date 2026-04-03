# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_08:08:01_UTC-green)

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

**Latest saved flight:** 2026-04-03 08:08:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 08:08:01 UTC

- **12,836** saved flights
- **7,237** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,836** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **159,580.2 tonnes** estimated CO2 emissions
- **9,251,027 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 487 |
| 3 | IndiGo | 349 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 199 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 134 |
| 10 | LATAM Airlines | 130 |
| 11 | AXM | 129 |
| 12 | QLK | 120 |
| 13 | LXJ | 117 |
| 14 | All Nippon Airways | 114 |
| 15 | Delta Air Lines | 101 |
| 16 | Swiss International | 97 |
| 17 | AZU | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Cathay Pacific | 85 |
| 22 | United Airlines | 84 |
| 23 | AXB | 83 |
| 24 | Japan Airlines | 83 |
| 25 | EDV | 78 |
| 26 | easyJet | 77 |
| 27 | EJU | 75 |
| 28 | ANZ | 72 |
| 29 | BRC | 72 |
| 30 | Avianca | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10352 |
| 2 | 🇮🇳 IN | 1080 |
| 3 | 🇦🇺 AU | 1059 |
| 4 | 🇪🇸 ES | 974 |
| 5 | 🇧🇷 BR | 711 |
| 6 | 🇩🇪 DE | 685 |
| 7 | 🇯🇵 JP | 668 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 605 |
| 10 | 🇮🇹 IT | 573 |
| 11 | 🇬🇧 GB | 474 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 406 |
| 14 | 🇳🇿 NZ | 321 |
| 15 | 🇬🇷 GR | 319 |
| 16 | 🇨🇭 CH | 314 |
| 17 | 🇳🇴 NO | 301 |
| 18 | 🇲🇾 MY | 292 |
| 19 | 🇵🇭 PH | 256 |
| 20 | 🇿🇦 ZA | 245 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇹🇷 TR | 226 |
| 23 | 🇰🇷 KR | 225 |
| 24 | 🇵🇱 PL | 177 |
| 25 | 🇹🇭 TH | 168 |
| 26 | 🇮🇩 ID | 157 |
| 27 | 🇲🇴 MO | 154 |
| 28 | 🇲🇦 MA | 147 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 234 |
| 3 | Denver International Airport |  | US | 233 |
| 4 | Indira Gandhi International Airport |  | IN | 231 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 187 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Sydney Kingsford Smith International Airport |  | AU | 157 |
| 10 | Macau International Airport |  | MO | 154 |
| 11 | Zurich Airport |  | CH | 154 |
| 12 | Guaymaral Airport |  | CO | 153 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 145 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Chicago O'Hare International Airport |  | US | 123 |
| 17 | Bengaluru International Airport |  | IN | 120 |
| 18 | Ninoy Aquino International Airport |  | PH | 116 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 20 | Charlotte/Douglas International Airport |  | US | 112 |
| 21 | Madrid Barajas International Airport |  | ES | 111 |
| 22 | Congonhas Airport |  | BR | 109 |
| 23 | Kuala Lumpur International Airport |  | MY | 108 |
| 24 | Tenerife Norte Airport |  | ES | 106 |
| 25 | Salt Lake City International Airport |  | US | 98 |
| 26 | Daniel K Inouye International Airport |  | US | 97 |
| 27 | Reno/Tahoe International Airport |  | US | 97 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 97 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 30 | Vitoria/Foronda Airport |  | ES | 93 |
| 31 | Malpensa International Airport |  | IT | 92 |
| 32 | Barcelona International Airport |  | ES | 91 |
| 33 | Charles de Gaulle International Airport |  | FR | 88 |
| 34 | Pune Airport |  | IN | 86 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 36 | Austin-Bergstrom International Airport |  | US | 85 |
| 37 | Seattle-Tacoma International Airport |  | US | 85 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Gimpo International Airport |  | KR | 81 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 55 | 1h 7m | 706 km | 669.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 43 | 29m | 304 km | 225.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 39 | 1h 46m | 1,156 km | 778.0 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 39 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 33 | 1h 26m | 910 km | 517.8 t |
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
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 21 | 1h 0m | 723 km | 261.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 20 | 20m | 147 km | 50.6 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 20 | 44m | 452 km | 155.9 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-04-03 07:53 UTC | 2026-04-03 08:08 UTC | 14m |
| ZKIWG | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-03 07:50 UTC | 2026-04-03 08:01 UTC | 10m |
| KLM99F | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Durham Tees Valley Airport (EGNV) | 2026-04-03 06:38 UTC | 2026-04-03 07:43 UTC | 1h 5m |
| ZSMPC | ZSM | Wonderboom Airport (FAWB) | Dunnottar Airport (FADR) | 2026-04-03 07:17 UTC | 2026-04-03 07:41 UTC | 23m |
| N53AR |  | Ted Stevens Anchorage International Airport (PANC) | Ralph M Calhoun Memorial Airport (PATA) | 2026-04-03 06:43 UTC | 2026-04-03 07:40 UTC | 57m |
|  |  | Mayerhofen Airport (LOKM) | Ossiacher See Airport (LOKF) | 2026-04-03 07:33 UTC | 2026-04-03 07:33 UTC | 0m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-03 07:17 UTC | 2026-04-03 07:29 UTC | 11m |
| MB55G |  | Perth International Airport (YPPH) | Rothsay Mine Airport (YROT) | 2026-04-03 06:45 UTC | 2026-04-03 07:28 UTC | 42m |
| URSA20 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-03 07:04 UTC | 2026-04-03 07:20 UTC | 15m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Megeve Airport (LFHM) | 2026-04-03 07:01 UTC | 2026-04-03 07:16 UTC | 15m |
| N55169 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-04-03 06:10 UTC | 2026-04-03 07:15 UTC | 1h 5m |
| RYR518E | Ryanair | Baneasa International Airport (LRBS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-03 05:56 UTC | 2026-04-03 07:13 UTC | 1h 17m |
| CWA935 | CWA | Edmonton / Gartner Airport (CFQ7) | Vermilion Airport (CYVG) | 2026-04-03 06:53 UTC | 2026-04-03 07:12 UTC | 18m |
| AM260 |  | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-04-03 06:26 UTC | 2026-04-03 07:11 UTC | 45m |
| AAR8707 | AAR | Gimpo International Airport (RKSS) | Kunsan Air Base (RKJK) | 2026-04-03 06:50 UTC | 2026-04-03 07:11 UTC | 21m |
| SEJ2448 | SEJ | Indira Gandhi International Airport (VIDP) | Lokpriya Gopinath Bordoloi International Airport (VEGT) | 2026-04-03 04:32 UTC | 2026-04-03 07:10 UTC | 2h 38m |
| IGO502 | IndiGo | Tirupati Airport (VOTP) | Pune Airport (VAPO) | 2026-04-03 06:02 UTC | 2026-04-03 07:09 UTC | 1h 6m |
| EZS91JX | EZS | Mollis Airport (LSZM) | Decimomannu Airport (LIED) | 2026-04-03 05:50 UTC | 2026-04-03 07:08 UTC | 1h 17m |
| DLH3PK | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-04-03 06:07 UTC | 2026-04-03 07:07 UTC | 1h 0m |
| CJT620 | CJT | John C. Munro Hamilton International Airport (CYHM) | Chipman Airport (CCS4) | 2026-04-03 05:50 UTC | 2026-04-03 07:07 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
