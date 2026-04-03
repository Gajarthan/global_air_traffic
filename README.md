# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_02:41:15_UTC-green)

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

**Latest saved flight:** 2026-04-03 02:41:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 02:41:15 UTC

- **12,567** saved flights
- **7,161** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,567** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **156,788.6 tonnes** estimated CO2 emissions
- **9,089,193 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 482 |
| 3 | IndiGo | 332 |
| 4 | EJA | 254 |
| 5 | American Airlines | 233 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 131 |
| 10 | LATAM Airlines | 127 |
| 11 | AXM | 122 |
| 12 | LXJ | 117 |
| 13 | QLK | 112 |
| 14 | All Nippon Airways | 106 |
| 15 | Delta Air Lines | 99 |
| 16 | AZU | 95 |
| 17 | Swiss International | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Cathay Pacific | 85 |
| 21 | Alaska Airlines | 84 |
| 22 | United Airlines | 84 |
| 23 | AXB | 81 |
| 24 | EDV | 78 |
| 25 | easyJet | 77 |
| 26 | Japan Airlines | 77 |
| 27 | EJU | 73 |
| 28 | BRC | 72 |
| 29 | Avianca | 71 |
| 30 | GLO | 70 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10295 |
| 2 | 🇮🇳 IN | 1034 |
| 3 | 🇦🇺 AU | 977 |
| 4 | 🇪🇸 ES | 956 |
| 5 | 🇧🇷 BR | 705 |
| 6 | 🇩🇪 DE | 674 |
| 7 | 🇨🇴 CO | 617 |
| 8 | 🇯🇵 JP | 612 |
| 9 | 🇨🇦 CA | 599 |
| 10 | 🇮🇹 IT | 558 |
| 11 | 🇬🇧 GB | 468 |
| 12 | 🇲🇽 MX | 460 |
| 13 | 🇫🇷 FR | 399 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 297 |
| 17 | 🇳🇿 NZ | 297 |
| 18 | 🇲🇾 MY | 278 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 234 |
| 21 | 🇵🇭 PH | 230 |
| 22 | 🇹🇷 TR | 216 |
| 23 | 🇰🇷 KR | 209 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 155 |
| 26 | 🇲🇴 MO | 154 |
| 27 | 🇮🇩 ID | 151 |
| 28 | 🇲🇦 MA | 145 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 122 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 312 |
| 2 | Denver International Airport |  | US | 232 |
| 3 | Indira Gandhi International Airport |  | IN | 222 |
| 4 | Tokyo International Airport |  | JP | 218 |
| 5 | El Dorado International Airport |  | CO | 215 |
| 6 | Frankfurt am Main International Airport |  | DE | 185 |
| 7 | Harry Reid International Airport |  | US | 176 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Macau International Airport |  | MO | 154 |
| 10 | Guaymaral Airport |  | CO | 153 |
| 11 | Zurich Airport |  | CH | 148 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 146 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 144 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Chicago O'Hare International Airport |  | US | 123 |
| 17 | Bengaluru International Airport |  | IN | 116 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 113 |
| 19 | Charlotte/Douglas International Airport |  | US | 112 |
| 20 | Congonhas Airport |  | BR | 109 |
| 21 | Madrid Barajas International Airport |  | ES | 108 |
| 22 | Tenerife Norte Airport |  | ES | 106 |
| 23 | Kuala Lumpur International Airport |  | MY | 105 |
| 24 | Ninoy Aquino International Airport |  | PH | 104 |
| 25 | Reno/Tahoe International Airport |  | US | 97 |
| 26 | Salt Lake City International Airport |  | US | 96 |
| 27 | Daniel K Inouye International Airport |  | US | 93 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 93 |
| 29 | Vitoria/Foronda Airport |  | ES | 92 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 31 | Malpensa International Airport |  | IT | 91 |
| 32 | Barcelona International Airport |  | ES | 88 |
| 33 | Charles de Gaulle International Airport |  | FR | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 35 | Austin-Bergstrom International Airport |  | US | 84 |
| 36 | Pune Airport |  | IN | 84 |
| 37 | Seattle-Tacoma International Airport |  | US | 84 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Miami International Airport |  | US | 79 |
| 40 | Bodø Airport |  | NO | 78 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 43 | 24m | 225 km | 166.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 41 | 29m | 304 km | 214.9 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 35 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 30 | 1h 26m | 910 km | 470.8 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 27 | 53m | 546 km | 254.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 27 | 30m | 369 km | 171.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 23 | 1h 10m | 770 km | 305.5 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 22 | 23m | 252 km | 95.5 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 21 | 1h 0m | 723 km | 261.8 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 20 | 13m | 99 km | 34.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 18 | 44m | 452 km | 140.3 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 18 | 8h 30m | 38 km | 11.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWA738 | Southwest Airlines | Oakland San Francisco Bay Airport (KOAK) | Bermuda Dunes Airport (KUDD) | 2026-04-03 01:45 UTC | 2026-04-03 02:41 UTC | 56m |
| UAL8247 | United Airlines | Chicago O'Hare International Airport (KORD) | Denver International Airport (KDEN) | 2026-04-03 00:13 UTC | 2026-04-03 02:37 UTC | 2h 23m |
| AWA411 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-03 01:53 UTC | 2026-04-03 02:34 UTC | 41m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-03 02:08 UTC | 2026-04-03 02:34 UTC | 26m |
| N967BY |  | Charleston Executive Airport (KJZI) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-03 01:13 UTC | 2026-04-03 02:22 UTC | 1h 9m |
| SNJ33 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-03 00:47 UTC | 2026-04-03 02:16 UTC | 1h 29m |
| CXK609 | CXK | Hayward Executive Airport (KHWD) | Buchanan Field (KCCR) | 2026-04-03 01:59 UTC | 2026-04-03 02:14 UTC | 14m |
| N400SL |  | Portland International Airport (KPDX) | Cable Creek Ranch Airport (96OR) | 2026-04-03 01:31 UTC | 2026-04-03 02:12 UTC | 40m |
| BBC491 | BBC | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-04-03 01:21 UTC | 2026-04-03 02:11 UTC | 49m |
| EJA864 | EJA | Van Nuys Airport (KVNY) | OR73 (OR73) | 2026-04-03 00:43 UTC | 2026-04-03 02:09 UTC | 1h 25m |
| SCA17 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-03 01:38 UTC | 2026-04-03 02:07 UTC | 29m |
| N317KC |  | Merrill Field (PAMR) | Perryville Airport (PAPE) | 2026-04-03 00:12 UTC | 2026-04-03 02:07 UTC | 1h 55m |
| SHADO79 | SHA | Albuquerque International Sunport Airport (KABQ) | Cannon Afb Airport (KCVS) | 2026-04-02 22:04 UTC | 2026-04-03 02:07 UTC | 4h 2m |
| VIV7435 | VIV | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-03 01:24 UTC | 2026-04-03 02:06 UTC | 42m |
| SWA2723 | Southwest Airlines | San Diego International Airport (KSAN) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-03 00:19 UTC | 2026-04-03 02:04 UTC | 1h 45m |
| SWA580 | Southwest Airlines | Harry Reid International Airport (KLAS) | Carson City Airport (KCXP) | 2026-04-03 01:14 UTC | 2026-04-03 02:04 UTC | 49m |
| N741SM |  | Harry Reid International Airport (KLAS) | North Las Vegas Airport (KVGT) | 2026-04-03 01:45 UTC | 2026-04-03 02:04 UTC | 19m |
| QLK623D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-03 01:28 UTC | 2026-04-03 02:02 UTC | 34m |
| MTNGBLUE | MTN | Kamphaeng Saen Airport (VTBK) | Photharam Airport (VTPR) | 2026-04-03 01:36 UTC | 2026-04-03 02:02 UTC | 25m |
| CEB196 | CEB | Ninoy Aquino International Airport (RPLL) | Loakan Airport (RPUB) | 2026-04-03 01:40 UTC | 2026-04-03 02:01 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
