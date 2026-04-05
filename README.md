# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_20:02:18_UTC-green)

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

**Latest saved flight:** 2026-04-05 20:02:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 20:02:18 UTC

- **18,830** saved flights
- **9,567** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,830** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **238,531.2 tonnes** estimated CO2 emissions
- **13,827,895 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 820 |
| 2 | Ryanair | 778 |
| 3 | IndiGo | 538 |
| 4 | American Airlines | 352 |
| 5 | EJA | 341 |
| 6 | Southwest Airlines | 268 |
| 7 | Lufthansa | 256 |
| 8 | ENY | 254 |
| 9 | Vueling | 207 |
| 10 | LATAM Airlines | 199 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 162 |
| 13 | LXJ | 162 |
| 14 | All Nippon Airways | 161 |
| 15 | QLK | 154 |
| 16 | AZU | 145 |
| 17 | Swiss International | 141 |
| 18 | VIV | 141 |
| 19 | United Airlines | 127 |
| 20 | Alaska Airlines | 125 |
| 21 | easyJet | 124 |
| 22 | Japan Airlines | 124 |
| 23 | Avianca | 123 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | EDV | 115 |
| 27 | WIF | 115 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14717 |
| 2 | 🇮🇳 IN | 1635 |
| 3 | 🇪🇸 ES | 1559 |
| 4 | 🇦🇺 AU | 1316 |
| 5 | 🇧🇷 BR | 1090 |
| 6 | 🇨🇴 CO | 1000 |
| 7 | 🇯🇵 JP | 994 |
| 8 | 🇩🇪 DE | 964 |
| 9 | 🇮🇹 IT | 900 |
| 10 | 🇨🇦 CA | 824 |
| 11 | 🇬🇧 GB | 743 |
| 12 | 🇫🇷 FR | 698 |
| 13 | 🇲🇽 MX | 636 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 504 |
| 16 | 🇲🇾 MY | 439 |
| 17 | 🇬🇹 GT | 428 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 396 |
| 20 | 🇳🇴 NO | 383 |
| 21 | 🇹🇷 TR | 363 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇵🇱 PL | 275 |
| 25 | 🇹🇭 TH | 273 |
| 26 | 🇲🇦 MA | 238 |
| 27 | 🇧🇸 BS | 211 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 453 |
| 2 | El Dorado International Airport |  | CO | 380 |
| 3 | Denver International Airport |  | US | 348 |
| 4 | Indira Gandhi International Airport |  | IN | 343 |
| 5 | Tokyo International Airport |  | JP | 340 |
| 6 | La Aurora Airport |  | GT | 297 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 246 |
| 9 | Zurich Airport |  | CH | 232 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 204 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 199 |
| 13 | Macau International Airport |  | MO | 198 |
| 14 | Chicago O'Hare International Airport |  | US | 197 |
| 15 | Guaymaral Airport |  | CO | 197 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 17 | Madrid Barajas International Airport |  | ES | 183 |
| 18 | Charlotte/Douglas International Airport |  | US | 182 |
| 19 | Bengaluru International Airport |  | IN | 181 |
| 20 | Tenerife Norte Airport |  | ES | 174 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 168 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 161 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Salt Lake City International Airport |  | US | 152 |
| 26 | Reno/Tahoe International Airport |  | US | 148 |
| 27 | Daniel K Inouye International Airport |  | US | 147 |
| 28 | Malpensa International Airport |  | IT | 144 |
| 29 | Vitoria/Foronda Airport |  | ES | 144 |
| 30 | Charles de Gaulle International Airport |  | FR | 143 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 140 |
| 33 | Miami International Airport |  | US | 134 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 130 |
| 35 | Barcelona International Airport |  | ES | 129 |
| 36 | Pune Airport |  | IN | 127 |
| 37 | O. R. Tambo International Airport |  | ZA | 127 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 125 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 123 |
| 40 | Seattle-Tacoma International Airport |  | US | 118 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 84 | 14m | 114 km | 164.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 60 | 22m | 99 km | 102.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 51 | 16m | 206 km | 181.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 42 | 1h 53m | 1,304 km | 944.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 37 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 33 | 30m | 114 km | 65.0 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG2650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-05 19:34 UTC | 2026-04-05 20:02 UTC | 27m |
| N3717R |  | CL36 (CL36) | Charles M Schulz/Sonoma County Airport (KSTS) | 2026-04-05 18:35 UTC | 2026-04-05 19:56 UTC | 1h 21m |
| N294B |  | Butler Memorial Airport (KBUM) | Johnson County Executive Airport (KOJC) | 2026-04-05 19:33 UTC | 2026-04-05 19:51 UTC | 18m |
| AFR25LD | Air France | Charles de Gaulle International Airport (LFPG) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-04-05 18:34 UTC | 2026-04-05 19:48 UTC | 1h 13m |
| AFL836 | AFL | Koltsovo Airport (USSS) | Sheremetyevo International Airport (UUEE) | 2026-04-03 16:53 UTC | 2026-04-05 19:38 UTC | 50h 44m |
| EJA348 | EJA | Greenbrier Valley Airport (KLWB) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-05 18:35 UTC | 2026-04-05 19:37 UTC | 1h 1m |
| N1910R |  | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-04-05 18:58 UTC | 2026-04-05 19:34 UTC | 35m |
| N396FS |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 19:10 UTC | 2026-04-05 19:33 UTC | 23m |
| TGARO | TGA | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-05 18:53 UTC | 2026-04-05 19:28 UTC | 34m |
| N719PJ |  | David Jay Perry Airport (K1K4) | 11OK (11OK) | 2026-04-05 19:20 UTC | 2026-04-05 19:26 UTC | 6m |
| N469RB |  | Chicago Midway International Airport (KMDW) | Frank Field (VA52) | 2026-04-05 18:09 UTC | 2026-04-05 19:20 UTC | 1h 11m |
| N2BA |  | Tangerine Airport (FL97) | Tangerine Airport (FL97) | 2026-04-05 19:12 UTC | 2026-04-05 19:20 UTC | 8m |
| RYR80NW | Ryanair | London Luton Airport (EGGW) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-05 17:24 UTC | 2026-04-05 19:17 UTC | 1h 53m |
| N423FP |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-05 18:43 UTC | 2026-04-05 19:15 UTC | 32m |
| LET7207 | LET | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Del Norte International Airport (MMAN) | 2026-04-05 14:39 UTC | 2026-04-05 19:13 UTC | 4h 34m |
| AAY3019 | AAY | Sarasota/Bradenton International Airport (KSRQ) | Akron-Canton Regional Airport (KCAK) | 2026-04-05 17:08 UTC | 2026-04-05 19:13 UTC | 2h 5m |
| EJA707 | EJA | Rocky Mountain Metro Airport (KBJC) | Morning Shadows Ranch Airport (CD69) | 2026-04-05 18:47 UTC | 2026-04-05 19:12 UTC | 24m |
| TGPWO | TGP | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-05 18:46 UTC | 2026-04-05 19:11 UTC | 25m |
| N801GW |  | North Las Vegas Airport (KVGT) | Big Bear City Airport (KL35) | 2026-04-05 18:20 UTC | 2026-04-05 19:10 UTC | 50m |
| SKW5986 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Root Field (82VA) | 2026-04-05 17:59 UTC | 2026-04-05 19:07 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
