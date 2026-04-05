# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_18:47:31_UTC-green)

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

**Latest saved flight:** 2026-04-05 18:47:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 18:47:31 UTC

- **18,630** saved flights
- **9,478** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,630** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **235,925.1 tonnes** estimated CO2 emissions
- **13,676,815 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 800 |
| 2 | Ryanair | 770 |
| 3 | IndiGo | 538 |
| 4 | American Airlines | 341 |
| 5 | EJA | 335 |
| 6 | Southwest Airlines | 264 |
| 7 | Lufthansa | 256 |
| 8 | ENY | 251 |
| 9 | Vueling | 206 |
| 10 | LATAM Airlines | 197 |
| 11 | AXM | 191 |
| 12 | LXJ | 162 |
| 13 | All Nippon Airways | 161 |
| 14 | Delta Air Lines | 159 |
| 15 | QLK | 154 |
| 16 | AZU | 142 |
| 17 | Swiss International | 140 |
| 18 | VIV | 137 |
| 19 | Alaska Airlines | 124 |
| 20 | Japan Airlines | 124 |
| 21 | easyJet | 123 |
| 22 | Avianca | 122 |
| 23 | EJU | 121 |
| 24 | United Airlines | 121 |
| 25 | AEE | 120 |
| 26 | EDV | 114 |
| 27 | AXB | 113 |
| 28 | WIF | 113 |
| 29 | Cathay Pacific | 105 |
| 30 | Air France | 104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14502 |
| 2 | 🇮🇳 IN | 1635 |
| 3 | 🇪🇸 ES | 1549 |
| 4 | 🇦🇺 AU | 1316 |
| 5 | 🇧🇷 BR | 1077 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 979 |
| 8 | 🇩🇪 DE | 960 |
| 9 | 🇮🇹 IT | 893 |
| 10 | 🇨🇦 CA | 816 |
| 11 | 🇬🇧 GB | 733 |
| 12 | 🇫🇷 FR | 695 |
| 13 | 🇲🇽 MX | 624 |
| 14 | 🇬🇷 GR | 535 |
| 15 | 🇨🇭 CH | 500 |
| 16 | 🇲🇾 MY | 437 |
| 17 | 🇬🇹 GT | 415 |
| 18 | 🇿🇦 ZA | 409 |
| 19 | 🇳🇿 NZ | 396 |
| 20 | 🇳🇴 NO | 377 |
| 21 | 🇹🇷 TR | 359 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 273 |
| 26 | 🇲🇦 MA | 236 |
| 27 | 🇧🇸 BS | 207 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 446 |
| 2 | El Dorado International Airport |  | CO | 371 |
| 3 | Indira Gandhi International Airport |  | IN | 343 |
| 4 | Denver International Airport |  | US | 341 |
| 5 | Tokyo International Airport |  | JP | 340 |
| 6 | La Aurora Airport |  | GT | 289 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 241 |
| 9 | Zurich Airport |  | CH | 229 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Macau International Airport |  | MO | 198 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 198 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 196 |
| 14 | Guaymaral Airport |  | CO | 195 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 16 | Chicago O'Hare International Airport |  | US | 189 |
| 17 | Madrid Barajas International Airport |  | ES | 182 |
| 18 | Bengaluru International Airport |  | IN | 181 |
| 19 | Charlotte/Douglas International Airport |  | US | 177 |
| 20 | Tenerife Norte Airport |  | ES | 172 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 164 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 160 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Salt Lake City International Airport |  | US | 149 |
| 26 | Daniel K Inouye International Airport |  | US | 146 |
| 27 | Vitoria/Foronda Airport |  | ES | 144 |
| 28 | Malpensa International Airport |  | IT | 143 |
| 29 | Reno/Tahoe International Airport |  | US | 143 |
| 30 | Charles de Gaulle International Airport |  | FR | 142 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 139 |
| 33 | Miami International Airport |  | US | 133 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 129 |
| 35 | Barcelona International Airport |  | ES | 129 |
| 36 | Pune Airport |  | IN | 127 |
| 37 | O. R. Tambo International Airport |  | ZA | 126 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 121 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 120 |
| 40 | Seattle-Tacoma International Airport |  | US | 116 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 82 | 14m | 114 km | 160.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 62 | 26m | 152 km | 162.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 58 | 22m | 99 km | 99.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 40 | 1h 54m | 1,304 km | 899.9 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 28 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 31 | 30m | 114 km | 61.1 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N739TW |  | Palo Alto Airport (KPAO) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-05 18:33 UTC | 2026-04-05 18:47 UTC | 14m |
| TGARO | TGA | Copan Ruinas Airport (MHRU) | La Aurora Airport (MGGT) | 2026-04-05 18:12 UTC | 2026-04-05 18:43 UTC | 30m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-05 18:16 UTC | 2026-04-05 18:36 UTC | 19m |
| N92448 |  | Harvey's Acres Airport (OR28) | Newport Municipal Airport (KONP) | 2026-04-05 17:38 UTC | 2026-04-05 18:29 UTC | 50m |
| N677AM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-05 18:07 UTC | 2026-04-05 18:24 UTC | 17m |
| N28641 |  | Salinas Municipal Airport (KSNS) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-05 17:49 UTC | 2026-04-05 18:22 UTC | 32m |
| N3911Q |  | Tampa Executive Airport (KVDF) | Zephyrhills Municipal Airport (KZPH) | 2026-04-05 18:08 UTC | 2026-04-05 18:20 UTC | 11m |
| N17WG |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-05 17:56 UTC | 2026-04-05 18:18 UTC | 22m |
| N5128R |  | Bend Municipal Airport (KBDN) | OG05 (OG05) | 2026-04-05 17:45 UTC | 2026-04-05 18:16 UTC | 30m |
| N38TW |  | Yucca Valley Airport (KL22) | 51CA (51CA) | 2026-04-05 17:48 UTC | 2026-04-05 18:15 UTC | 27m |
| N8398L |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-05 17:59 UTC | 2026-04-05 18:15 UTC | 16m |
| EZY87XA | easyJet | Bristol International Airport (EGGD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-05 16:14 UTC | 2026-04-05 18:14 UTC | 2h 0m |
| TGCYO | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 17:48 UTC | 2026-04-05 18:13 UTC | 24m |
| TGKCS | TGK | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-05 17:43 UTC | 2026-04-05 18:12 UTC | 28m |
| JSX720 | JSX | John Wayne/Orange County Airport (KSNA) | Reno/Tahoe International Airport (KRNO) | 2026-04-05 17:09 UTC | 2026-04-05 18:11 UTC | 1h 1m |
| N47SB |  | Fort Lauderdale/Hollywood International Airport (KFLL) | Orlando Executive Airport (KORL) | 2026-04-05 17:29 UTC | 2026-04-05 18:09 UTC | 39m |
| EJA412 | EJA | Long Beach (Daugherty Field) Airport (KLGB) | Northern Colorado Regional Airport (KFNL) | 2026-04-05 16:05 UTC | 2026-04-05 18:09 UTC | 2h 3m |
| N890MT |  | Mckinney Ntl Airport (KTKI) | Wendover Airport (KENV) | 2026-04-05 15:01 UTC | 2026-04-05 18:08 UTC | 3h 7m |
| NSZ3210 | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-04-05 17:17 UTC | 2026-04-05 18:07 UTC | 50m |
| N106PA |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 17:33 UTC | 2026-04-05 18:05 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
