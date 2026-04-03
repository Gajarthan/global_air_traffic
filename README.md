# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_19:48:31_UTC-green)

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

**Latest saved flight:** 2026-04-03 19:48:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 19:48:31 UTC

- **14,232** saved flights
- **7,843** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,232** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **176,136.1 tonnes** estimated CO2 emissions
- **10,210,786 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 615 |
| 2 | Ryanair | 543 |
| 3 | IndiGo | 403 |
| 4 | EJA | 284 |
| 5 | American Airlines | 264 |
| 6 | Lufthansa | 210 |
| 7 | Southwest Airlines | 205 |
| 8 | ENY | 186 |
| 9 | Vueling | 154 |
| 10 | LATAM Airlines | 147 |
| 11 | AXM | 142 |
| 12 | LXJ | 126 |
| 13 | All Nippon Airways | 123 |
| 14 | QLK | 123 |
| 15 | AZU | 114 |
| 16 | Delta Air Lines | 113 |
| 17 | Swiss International | 109 |
| 18 | VIV | 103 |
| 19 | WIF | 97 |
| 20 | Alaska Airlines | 91 |
| 21 | United Airlines | 91 |
| 22 | AXB | 89 |
| 23 | easyJet | 89 |
| 24 | Japan Airlines | 89 |
| 25 | AEE | 87 |
| 26 | EDV | 87 |
| 27 | EJU | 87 |
| 28 | Cathay Pacific | 85 |
| 29 | GLO | 83 |
| 30 | BRC | 81 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11414 |
| 2 | 🇮🇳 IN | 1227 |
| 3 | 🇪🇸 ES | 1098 |
| 4 | 🇦🇺 AU | 1082 |
| 5 | 🇧🇷 BR | 834 |
| 6 | 🇩🇪 DE | 755 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 681 |
| 9 | 🇨🇦 CA | 653 |
| 10 | 🇮🇹 IT | 621 |
| 11 | 🇬🇧 GB | 548 |
| 12 | 🇫🇷 FR | 499 |
| 13 | 🇲🇽 MX | 494 |
| 14 | 🇬🇷 GR | 386 |
| 15 | 🇨🇭 CH | 372 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 265 |
| 21 | 🇵🇭 PH | 265 |
| 22 | 🇬🇹 GT | 261 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 198 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 171 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 154 |
| 30 | 🇲🇪 ME | 148 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 350 |
| 2 | Indira Gandhi International Airport |  | IN | 260 |
| 3 | Denver International Airport |  | US | 253 |
| 4 | Tokyo International Airport |  | JP | 253 |
| 5 | El Dorado International Airport |  | CO | 246 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 193 |
| 8 | La Aurora Airport |  | GT | 182 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 179 |
| 10 | Zurich Airport |  | CH | 173 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 158 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 155 |
| 15 | Bengaluru International Airport |  | IN | 140 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 139 |
| 17 | Chicago O'Hare International Airport |  | US | 136 |
| 18 | Congonhas Airport |  | BR | 131 |
| 19 | Charlotte/Douglas International Airport |  | US | 130 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 125 |
| 21 | Madrid Barajas International Airport |  | ES | 125 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 114 |
| 25 | Vitoria/Foronda Airport |  | ES | 111 |
| 26 | Salt Lake City International Airport |  | US | 111 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 28 | Reno/Tahoe International Airport |  | US | 107 |
| 29 | Charles de Gaulle International Airport |  | FR | 104 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 104 |
| 31 | Daniel K Inouye International Airport |  | US | 103 |
| 32 | Malpensa International Airport |  | IT | 102 |
| 33 | Pune Airport |  | IN | 98 |
| 34 | Barcelona International Airport |  | ES | 96 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 95 |
| 36 | Austin-Bergstrom International Airport |  | US | 94 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 92 |
| 38 | Seattle-Tacoma International Airport |  | US | 91 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 88 |
| 40 | Miami International Airport |  | US | 88 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 66 | 14m | 114 km | 129.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 36 | 22m | 99 km | 61.7 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 34 | 26m | 152 km | 88.9 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 31 | 53m | 556 km | 297.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 30 | 1h 55m | 1,304 km | 674.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 19 | 30m | 213 km | 69.8 t |
| 30 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SCU20 | SCU | Double W Airport (3OK7) | Tulsa International Airport (KTUL) | 2026-04-03 18:57 UTC | 2026-04-03 19:48 UTC | 50m |
| N432R |  | Long Beach (Daugherty Field) Airport (KLGB) | French Valley Airport (KF70) | 2026-04-03 18:57 UTC | 2026-04-03 19:47 UTC | 49m |
| N532AN |  | Long Beach (Daugherty Field) Airport (KLGB) | Compton/Woodley Airport (KCPM) | 2026-04-03 18:38 UTC | 2026-04-03 19:45 UTC | 1h 6m |
| PDU66 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-03 19:02 UTC | 2026-04-03 19:43 UTC | 40m |
| N650TP |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-04-03 19:14 UTC | 2026-04-03 19:34 UTC | 19m |
| SCA29 | SCA | Scottsdale Airport (KSDL) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 18:35 UTC | 2026-04-03 19:30 UTC | 54m |
| N19646 |  | Dekalb-Peachtree Airport (KPDK) | Dekalb-Peachtree Airport (KPDK) | 2026-04-03 19:10 UTC | 2026-04-03 19:30 UTC | 19m |
| JPR12 | JPR | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-03 18:49 UTC | 2026-04-03 19:27 UTC | 37m |
| N128SH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-03 19:06 UTC | 2026-04-03 19:25 UTC | 18m |
| WAH | WAH | Beluga Airport (PABG) | Kenai Municipal Airport (PAEN) | 2026-04-03 19:07 UTC | 2026-04-03 19:22 UTC | 15m |
| N4120R |  | 36AZ (36AZ) | 36AZ (36AZ) | 2026-04-03 19:15 UTC | 2026-04-03 19:16 UTC | 1m |
| CFR78 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-04-03 18:25 UTC | 2026-04-03 19:16 UTC | 51m |
| SCU38 | SCU | Double W Airport (3OK7) | Double W Airport (3OK7) | 2026-04-03 19:07 UTC | 2026-04-03 19:16 UTC | 9m |
| SCU54 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Tulsa International Airport (KTUL) | 2026-04-03 18:48 UTC | 2026-04-03 19:16 UTC | 27m |
| N729JF |  | Philip Billard Municipal Airport (KTOP) | Ness City Municipal Airport (K48K) | 2026-04-03 18:37 UTC | 2026-04-03 19:09 UTC | 32m |
| N222JS |  | Gerald R Ford International Airport (KGRR) | Miami Executive Airport (KTMB) | 2026-04-03 16:28 UTC | 2026-04-03 19:08 UTC | 2h 39m |
| N484BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-03 18:45 UTC | 2026-04-03 19:06 UTC | 20m |
| N994SD |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-04-03 19:03 UTC | 2026-04-03 19:06 UTC | 2m |
| N5691R |  | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-04-03 18:32 UTC | 2026-04-03 19:06 UTC | 33m |
| N500TD |  | OG08 (OG08) | OG08 (OG08) | 2026-04-03 18:46 UTC | 2026-04-03 18:59 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
