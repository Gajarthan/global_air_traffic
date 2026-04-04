# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_17:33:12_UTC-green)

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

**Latest saved flight:** 2026-04-04 17:33:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 17:33:12 UTC

- **16,255** saved flights
- **8,645** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,255** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **201,561.1 tonnes** estimated CO2 emissions
- **11,684,700 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 687 |
| 2 | Ryanair | 660 |
| 3 | IndiGo | 474 |
| 4 | EJA | 307 |
| 5 | American Airlines | 289 |
| 6 | Lufthansa | 235 |
| 7 | Southwest Airlines | 231 |
| 8 | ENY | 205 |
| 9 | Vueling | 179 |
| 10 | LATAM Airlines | 173 |
| 11 | AXM | 160 |
| 12 | All Nippon Airways | 141 |
| 13 | LXJ | 138 |
| 14 | QLK | 137 |
| 15 | Delta Air Lines | 132 |
| 16 | AZU | 123 |
| 17 | Swiss International | 123 |
| 18 | VIV | 118 |
| 19 | EJU | 108 |
| 20 | Japan Airlines | 107 |
| 21 | AEE | 105 |
| 22 | Alaska Airlines | 104 |
| 23 | Avianca | 104 |
| 24 | WIF | 102 |
| 25 | AXB | 101 |
| 26 | easyJet | 99 |
| 27 | EDV | 98 |
| 28 | United Airlines | 98 |
| 29 | BRC | 96 |
| 30 | GLO | 94 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12776 |
| 2 | 🇮🇳 IN | 1440 |
| 3 | 🇪🇸 ES | 1338 |
| 4 | 🇦🇺 AU | 1209 |
| 5 | 🇧🇷 BR | 945 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 855 |
| 8 | 🇨🇴 CO | 824 |
| 9 | 🇮🇹 IT | 753 |
| 10 | 🇨🇦 CA | 715 |
| 11 | 🇬🇧 GB | 634 |
| 12 | 🇫🇷 FR | 597 |
| 13 | 🇲🇽 MX | 551 |
| 14 | 🇬🇷 GR | 452 |
| 15 | 🇨🇭 CH | 438 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 368 |
| 18 | 🇿🇦 ZA | 348 |
| 19 | 🇳🇴 NO | 338 |
| 20 | 🇵🇭 PH | 305 |
| 21 | 🇬🇹 GT | 298 |
| 22 | 🇹🇷 TR | 296 |
| 23 | 🇰🇷 KR | 290 |
| 24 | 🇵🇱 PL | 234 |
| 25 | 🇹🇭 TH | 231 |
| 26 | 🇲🇦 MA | 198 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇧🇸 BS | 177 |
| 29 | 🇲🇪 ME | 169 |
| 30 | 🇲🇴 MO | 164 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 380 |
| 2 | El Dorado International Airport |  | CO | 308 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 296 |
| 5 | Denver International Airport |  | US | 290 |
| 6 | Harry Reid International Airport |  | US | 215 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 213 |
| 8 | Frankfurt am Main International Airport |  | DE | 212 |
| 9 | La Aurora Airport |  | GT | 209 |
| 10 | Zurich Airport |  | CH | 198 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Guaymaral Airport |  | CO | 173 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 171 |
| 14 | Macau International Airport |  | MO | 164 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 162 |
| 16 | Bengaluru International Airport |  | IN | 158 |
| 17 | Charlotte/Douglas International Airport |  | US | 151 |
| 18 | Chicago O'Hare International Airport |  | US | 150 |
| 19 | Congonhas Airport |  | BR | 150 |
| 20 | Madrid Barajas International Airport |  | ES | 148 |
| 21 | Tenerife Norte Airport |  | ES | 143 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 142 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 127 |
| 27 | Reno/Tahoe International Airport |  | US | 126 |
| 28 | Salt Lake City International Airport |  | US | 125 |
| 29 | Daniel K Inouye International Airport |  | US | 123 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 123 |
| 31 | Charles de Gaulle International Airport |  | FR | 121 |
| 32 | Vitoria/Foronda Airport |  | ES | 119 |
| 33 | Barcelona International Airport |  | ES | 115 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 110 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 109 |
| 36 | Pune Airport |  | IN | 109 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 105 |
| 38 | Miami International Airport |  | US | 103 |
| 39 | Austin-Bergstrom International Airport |  | US | 103 |
| 40 | Gimpo International Airport |  | KR | 101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 74 | 14m | 114 km | 145.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 66 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 49 | 1h 45m | 1,156 km | 977.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 42 | 26m | 152 km | 109.8 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 41 | 22m | 99 km | 70.2 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 35 | 53m | 556 km | 335.5 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 28 | 59m | 723 km | 349.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 28 | 9m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 24 | 1h 20m | 961 km | 397.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH3P | Lufthansa | Václav Havel Airport (LKPR) | Fulda-Jossa Airport (EDGF) | 2026-04-04 16:50 UTC | 2026-04-04 17:33 UTC | 42m |
| DLH875 | Lufthansa | Bergen Airport Flesland (ENBR) | Gelnhausen Airport (EDFG) | 2026-04-04 15:55 UTC | 2026-04-04 17:33 UTC | 1h 37m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-04 16:44 UTC | 2026-04-04 17:29 UTC | 45m |
| N172AL |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-04 17:03 UTC | 2026-04-04 17:23 UTC | 19m |
| N168Y |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-04 16:09 UTC | 2026-04-04 17:22 UTC | 1h 13m |
| BOX740 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-04 02:50 UTC | 2026-04-04 17:14 UTC | 14h 24m |
| BRCAT16 | BRC | Roswell Air Center Airport (KROW) | Williams Field (TX99) | 2026-04-04 16:50 UTC | 2026-04-04 17:11 UTC | 21m |
| WUK792 | WUK | London Luton Airport (EGGW) | Elbląg Airport (EPEL) | 2026-04-04 15:34 UTC | 2026-04-04 17:08 UTC | 1h 34m |
| N5328Z |  | Bartow Executive Airport (KBOW) | Villa Char Mar Airport (1FA9) | 2026-04-04 16:49 UTC | 2026-04-04 17:08 UTC | 18m |
| SCU12 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-04 17:06 UTC | 2026-04-04 17:06 UTC | 0m |
| BRCAT04 | BRC | Skeen Ranch Airport (82NM) | Skeen Ranch Airport (82NM) | 2026-04-04 16:37 UTC | 2026-04-04 17:05 UTC | 28m |
| RYR6PL | Ryanair | Hamburg Airport (EDDH) | Cewice Military Airport (EPCE) | 2026-04-04 16:24 UTC | 2026-04-04 17:04 UTC | 40m |
| N765KA |  | 61WA (61WA) | Wilding Farm Airport (6WA5) | 2026-04-04 16:56 UTC | 2026-04-04 17:01 UTC | 4m |
| RYR613K | Ryanair | Palma De Mallorca Airport (LEPA) | Malpensa International Airport (LIMC) | 2026-04-04 15:33 UTC | 2026-04-04 16:59 UTC | 1h 26m |
| SAMU38 | SAM | Grenoble Le Versoud Airport (LFLG) | Grenoble Le Versoud Airport (LFLG) | 2026-04-04 16:57 UTC | 2026-04-04 16:59 UTC | 1m |
| N2859W |  | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-04-04 16:01 UTC | 2026-04-04 16:57 UTC | 56m |
| TGABY | TGA | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 16:18 UTC | 2026-04-04 16:55 UTC | 37m |
| N1934J |  | Sussex Airport (KFWN) | Lehigh Valley International Airport (KABE) | 2026-04-04 16:15 UTC | 2026-04-04 16:53 UTC | 38m |
| ETH3784 | Ethiopian Airlines | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-04 04:39 UTC | 2026-04-04 16:52 UTC | 12h 13m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-04-04 16:41 UTC | 2026-04-04 16:52 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
