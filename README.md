# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_05:11:37_UTC-green)

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

**Latest saved flight:** 2026-04-05 05:11:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 05:11:37 UTC

- **17,265** saved flights
- **9,022** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,265** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **216,491.1 tonnes** estimated CO2 emissions
- **12,550,208 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 768 |
| 2 | Ryanair | 689 |
| 3 | IndiGo | 491 |
| 4 | EJA | 328 |
| 5 | American Airlines | 319 |
| 6 | Southwest Airlines | 247 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 234 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 166 |
| 12 | Delta Air Lines | 150 |
| 13 | LXJ | 149 |
| 14 | All Nippon Airways | 145 |
| 15 | QLK | 142 |
| 16 | VIV | 131 |
| 17 | AZU | 130 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 120 |
| 20 | United Airlines | 116 |
| 21 | Avianca | 113 |
| 22 | Japan Airlines | 110 |
| 23 | EJU | 109 |
| 24 | EDV | 108 |
| 25 | AEE | 107 |
| 26 | easyJet | 107 |
| 27 | AXB | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | GLO | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13864 |
| 2 | 🇮🇳 IN | 1495 |
| 3 | 🇪🇸 ES | 1400 |
| 4 | 🇦🇺 AU | 1240 |
| 5 | 🇧🇷 BR | 998 |
| 6 | 🇨🇴 CO | 905 |
| 7 | 🇯🇵 JP | 898 |
| 8 | 🇩🇪 DE | 874 |
| 9 | 🇮🇹 IT | 788 |
| 10 | 🇨🇦 CA | 777 |
| 11 | 🇬🇧 GB | 663 |
| 12 | 🇫🇷 FR | 610 |
| 13 | 🇲🇽 MX | 605 |
| 14 | 🇬🇷 GR | 467 |
| 15 | 🇨🇭 CH | 445 |
| 16 | 🇳🇿 NZ | 388 |
| 17 | 🇲🇾 MY | 381 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 337 |
| 21 | 🇵🇭 PH | 330 |
| 22 | 🇹🇷 TR | 310 |
| 23 | 🇰🇷 KR | 299 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 237 |
| 26 | 🇲🇦 MA | 210 |
| 27 | 🇧🇸 BS | 191 |
| 28 | 🇮🇩 ID | 182 |
| 29 | 🇲🇴 MO | 180 |
| 30 | 🇲🇪 ME | 173 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 418 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Denver International Airport |  | US | 326 |
| 4 | Indira Gandhi International Airport |  | IN | 311 |
| 5 | Tokyo International Airport |  | JP | 308 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 231 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 218 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 204 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 188 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 13 | Guaymaral Airport |  | CO | 182 |
| 14 | Macau International Airport |  | MO | 180 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 180 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 165 |
| 18 | Charlotte/Douglas International Airport |  | US | 163 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 156 |
| 20 | Madrid Barajas International Airport |  | ES | 156 |
| 21 | Congonhas Airport |  | BR | 154 |
| 22 | Ninoy Aquino International Airport |  | PH | 150 |
| 23 | Tenerife Norte Airport |  | ES | 150 |
| 24 | Salt Lake City International Airport |  | US | 142 |
| 25 | Daniel K Inouye International Airport |  | US | 141 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 137 |
| 27 | Kuala Lumpur International Airport |  | MY | 136 |
| 28 | Reno/Tahoe International Airport |  | US | 135 |
| 29 | Malpensa International Airport |  | IT | 133 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 122 |
| 34 | Barcelona International Airport |  | ES | 120 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 38 | Seattle-Tacoma International Airport |  | US | 112 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 76 | 1h 8m | 706 km | 925.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 63 | 24m | 225 km | 244.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 58 | 29m | 304 km | 304.1 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 50 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 48 | 1h 27m | 910 km | 753.2 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 47 | 16m | 206 km | 167.1 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 39 | 19m | 165 km | 110.9 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 36 | 1h 11m | 770 km | 478.2 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 32 | 53m | 546 km | 301.3 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 29 | 46m | 452 km | 226.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N478KN |  | Seattle Paine Field International Airport (KPAE) | Boeing Field/King County International Airport (KBFI) | 2026-04-05 04:40 UTC | 2026-04-05 05:11 UTC | 31m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-05 00:50 UTC | 2026-04-05 05:07 UTC | 4h 16m |
| JCO655 | JCO | Indira Gandhi International Airport (VIDP) | Glasgow International Airport (EGPF) | 2026-04-04 19:35 UTC | 2026-04-05 04:58 UTC | 9h 23m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-04 14:08 UTC | 2026-04-05 04:45 UTC | 14h 36m |
| LT612 |  | Ensenada Airport (MMES) | Ensenada Airport (MMES) | 2026-04-05 03:09 UTC | 2026-04-05 04:33 UTC | 1h 24m |
| WJA2133 | WJA | Cancun International Airport (MMUN) | Toronto Pearson International Airport (CYYZ) | 2026-04-05 01:05 UTC | 2026-04-05 04:27 UTC | 3h 22m |
| GTI8154 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-04 17:17 UTC | 2026-04-05 04:25 UTC | 11h 8m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-05 03:51 UTC | 2026-04-05 04:25 UTC | 33m |
| CMD3 | CMD | Auburn Municipal Airport (KAUN) | Lake Tahoe Airport (KTVL) | 2026-04-05 04:03 UTC | 2026-04-05 04:22 UTC | 19m |
| AEE270 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-05 03:51 UTC | 2026-04-05 04:21 UTC | 30m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Sariang Airport (VTCS) | 2026-04-05 03:52 UTC | 2026-04-05 04:20 UTC | 27m |
| FIN9KC | Finnair | Helsinki Vantaa Airport (EFHK) | Khrabrovo Airport (UMKK) | 2026-04-05 03:55 UTC | 2026-04-05 04:17 UTC | 21m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-05 04:03 UTC | 2026-04-05 04:16 UTC | 13m |
| IGO564E | IndiGo | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-04-05 03:53 UTC | 2026-04-05 04:09 UTC | 16m |
| VAR466 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-05 04:01 UTC | 2026-04-05 04:08 UTC | 6m |
| ACA223 | Air Canada | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-04-05 02:55 UTC | 2026-04-05 04:08 UTC | 1h 12m |
| FDA353 | FDA | Gifu Airport (RJNG) | Yamagata Airport (RJSC) | 2026-04-05 03:24 UTC | 2026-04-05 04:04 UTC | 39m |
| KAL1815 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-05 03:36 UTC | 2026-04-05 04:03 UTC | 26m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-04-05 02:23 UTC | 2026-04-05 04:02 UTC | 1h 38m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 03:42 UTC | 2026-04-05 04:00 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
