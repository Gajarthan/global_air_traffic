# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_19:17:39_UTC-green)

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

**Latest saved flight:** 2026-04-02 19:17:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 19:17:39 UTC

- **11,806** saved flights
- **6,775** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,806** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **145,807.9 tonnes** estimated CO2 emissions
- **8,452,630 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 500 |
| 2 | Ryanair | 471 |
| 3 | IndiGo | 328 |
| 4 | EJA | 229 |
| 5 | American Airlines | 211 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 177 |
| 8 | ENY | 148 |
| 9 | Vueling | 128 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 119 |
| 12 | LXJ | 111 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | WIF | 95 |
| 16 | Swiss International | 94 |
| 17 | Delta Air Lines | 91 |
| 18 | AZU | 87 |
| 19 | VIV | 83 |
| 20 | AXB | 80 |
| 21 | Japan Airlines | 77 |
| 22 | Alaska Airlines | 76 |
| 23 | easyJet | 73 |
| 24 | EDV | 72 |
| 25 | EJU | 72 |
| 26 | BRC | 70 |
| 27 | Cathay Pacific | 70 |
| 28 | United Airlines | 69 |
| 29 | Avianca | 68 |
| 30 | GLO | 64 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9427 |
| 2 | 🇮🇳 IN | 1013 |
| 3 | 🇪🇸 ES | 941 |
| 4 | 🇦🇺 AU | 904 |
| 5 | 🇩🇪 DE | 663 |
| 6 | 🇧🇷 BR | 650 |
| 7 | 🇯🇵 JP | 595 |
| 8 | 🇨🇴 CO | 583 |
| 9 | 🇨🇦 CA | 548 |
| 10 | 🇮🇹 IT | 544 |
| 11 | 🇬🇧 GB | 453 |
| 12 | 🇲🇽 MX | 418 |
| 13 | 🇫🇷 FR | 396 |
| 14 | 🇬🇷 GR | 301 |
| 15 | 🇳🇴 NO | 300 |
| 16 | 🇨🇭 CH | 292 |
| 17 | 🇲🇾 MY | 272 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 226 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇹🇷 TR | 207 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 171 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇦 MA | 141 |
| 28 | 🇲🇴 MO | 135 |
| 29 | 🇳🇱 NL | 120 |
| 30 | 🇲🇪 ME | 118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 276 |
| 2 | Indira Gandhi International Airport |  | IN | 218 |
| 3 | Tokyo International Airport |  | JP | 213 |
| 4 | Denver International Airport |  | US | 203 |
| 5 | El Dorado International Airport |  | CO | 199 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 162 |
| 8 | La Aurora Airport |  | GT | 158 |
| 9 | Guaymaral Airport |  | CO | 152 |
| 10 | Zurich Airport |  | CH | 145 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 12 | Macau International Airport |  | MO | 135 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 132 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 118 |
| 16 | Bengaluru International Airport |  | IN | 114 |
| 17 | Chicago O'Hare International Airport |  | US | 113 |
| 18 | Charlotte/Douglas International Airport |  | US | 106 |
| 19 | Madrid Barajas International Airport |  | ES | 106 |
| 20 | Tenerife Norte Airport |  | ES | 105 |
| 21 | Kuala Lumpur International Airport |  | MY | 104 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 103 |
| 23 | Congonhas Airport |  | BR | 100 |
| 24 | Ninoy Aquino International Airport |  | PH | 97 |
| 25 | Reno/Tahoe International Airport |  | US | 96 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Vitoria/Foronda Airport |  | ES | 90 |
| 28 | Malpensa International Airport |  | IT | 89 |
| 29 | Daniel K Inouye International Airport |  | US | 87 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 87 |
| 31 | Charles de Gaulle International Airport |  | FR | 86 |
| 32 | Barcelona International Airport |  | ES | 84 |
| 33 | Pune Airport |  | IN | 80 |
| 34 | Salt Lake City International Airport |  | US | 80 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 79 |
| 36 | Bodø Airport |  | NO | 78 |
| 37 | Austin-Bergstrom International Airport |  | US | 77 |
| 38 | Gimpo International Airport |  | KR | 75 |
| 39 | Seattle-Tacoma International Airport |  | US | 75 |
| 40 | Amsterdam Airport Schiphol |  | NL | 74 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 56 | 14m | 114 km | 109.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 37 | 1h 46m | 1,156 km | 738.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 30 | 15m | 206 km | 106.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 23 | 1h 57m | 1,304 km | 517.4 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 19 | 13m | 99 km | 32.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2135K |  | Indianapolis Executive Airport (KTYQ) | Monroe County Airport (KBMG) | 2026-04-02 18:22 UTC | 2026-04-02 19:17 UTC | 55m |
| GLO1555 | GLO | Pinto Martins International Airport (SBFZ) | Professor Urbano Ernesto Stumpf Airport (SBSJ) | 2026-04-02 15:59 UTC | 2026-04-02 19:13 UTC | 3h 13m |
| N665M |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-02 18:39 UTC | 2026-04-02 19:12 UTC | 32m |
| N680WA |  | Santa Monica Municipal Airport (KSMO) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-02 18:39 UTC | 2026-04-02 19:05 UTC | 26m |
| R08463 |  | Whetstone Airport (11AZ) | Tombstone Municipal Airport (KP29) | 2026-04-02 18:45 UTC | 2026-04-02 19:03 UTC | 18m |
| N253EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-02 18:15 UTC | 2026-04-02 19:03 UTC | 47m |
| FLC81 | FLC | Battle Creek Executive At Kellogg Field (KBTL) | James M Cox Dayton International Airport (KDAY) | 2026-04-02 17:42 UTC | 2026-04-02 19:02 UTC | 1h 20m |
| N129SW |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-02 18:45 UTC | 2026-04-02 19:01 UTC | 16m |
| AEA66ZQ | AEA | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-02 18:10 UTC | 2026-04-02 18:59 UTC | 49m |
| N493LG |  | Usaf Academy Davis Airfield (KAFF) | Desiderata Ranch Airport (30CO) | 2026-04-02 18:42 UTC | 2026-04-02 18:58 UTC | 16m |
| PONY01 | PON | Davis Monthan Afb Airport (KDMA) | Davis Monthan Afb Airport (KDMA) | 2026-04-02 18:23 UTC | 2026-04-02 18:53 UTC | 29m |
| BRG661 | BRG | Point Hope Airport (PAPO) | Kivalina Airport (PAVL) | 2026-04-02 18:26 UTC | 2026-04-02 18:52 UTC | 26m |
| MNB178 | MNB | Ataturk International Airport (LTBA) | Zhuhai Airport (ZGSD) | 2026-04-02 06:29 UTC | 2026-04-02 18:48 UTC | 12h 19m |
| AEE278 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-02 18:22 UTC | 2026-04-02 18:48 UTC | 25m |
| VLG16GL | Vueling | Sevilla Airport (LEZL) | Paris-Orly Airport (LFPO) | 2026-04-02 16:32 UTC | 2026-04-02 18:45 UTC | 2h 12m |
| N222CF |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-02 17:47 UTC | 2026-04-02 18:42 UTC | 55m |
| ERU884 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-02 18:22 UTC | 2026-04-02 18:42 UTC | 20m |
| SCU54 | SCU | Cherokee Ranch Airport (OK25) | Gregg Airport (7OK1) | 2026-04-02 18:32 UTC | 2026-04-02 18:40 UTC | 7m |
| LXJ309 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | Santa Monica Municipal Airport (KSMO) | 2026-04-02 17:50 UTC | 2026-04-02 18:40 UTC | 49m |
| VT146CZ |  | Faa'a International Airport (NTAA) | Arutua Airport (NTGU) | 2026-04-02 17:43 UTC | 2026-04-02 18:38 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
