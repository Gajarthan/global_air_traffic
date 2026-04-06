# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_10:42:17_UTC-green)

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

**Latest saved flight:** 2026-04-06 10:42:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 10:42:17 UTC

- **19,685** saved flights
- **9,882** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,685** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **248,369.4 tonnes** estimated CO2 emissions
- **14,398,225 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 814 |
| 3 | IndiGo | 560 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 258 |
| 9 | Vueling | 214 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 196 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 173 |
| 14 | LXJ | 171 |
| 15 | QLK | 164 |
| 16 | AZU | 150 |
| 17 | VIV | 149 |
| 18 | Swiss International | 148 |
| 19 | United Airlines | 134 |
| 20 | Alaska Airlines | 132 |
| 21 | easyJet | 132 |
| 22 | Japan Airlines | 132 |
| 23 | Avianca | 130 |
| 24 | EJU | 126 |
| 25 | AEE | 124 |
| 26 | EDV | 118 |
| 27 | WIF | 118 |
| 28 | AXB | 115 |
| 29 | Air France | 109 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15367 |
| 2 | 🇮🇳 IN | 1710 |
| 3 | 🇪🇸 ES | 1592 |
| 4 | 🇦🇺 AU | 1407 |
| 5 | 🇧🇷 BR | 1126 |
| 6 | 🇯🇵 JP | 1072 |
| 7 | 🇨🇴 CO | 1056 |
| 8 | 🇩🇪 DE | 984 |
| 9 | 🇮🇹 IT | 955 |
| 10 | 🇨🇦 CA | 857 |
| 11 | 🇬🇧 GB | 767 |
| 12 | 🇫🇷 FR | 719 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 559 |
| 15 | 🇨🇭 CH | 526 |
| 16 | 🇲🇾 MY | 458 |
| 17 | 🇬🇹 GT | 452 |
| 18 | 🇿🇦 ZA | 437 |
| 19 | 🇳🇿 NZ | 416 |
| 20 | 🇳🇴 NO | 406 |
| 21 | 🇹🇷 TR | 380 |
| 22 | 🇵🇭 PH | 378 |
| 23 | 🇰🇷 KR | 348 |
| 24 | 🇹🇭 TH | 298 |
| 25 | 🇵🇱 PL | 285 |
| 26 | 🇲🇦 MA | 243 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 211 |
| 29 | 🇲🇪 ME | 205 |
| 30 | 🇲🇴 MO | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 483 |
| 2 | El Dorado International Airport |  | CO | 404 |
| 3 | Tokyo International Airport |  | JP | 369 |
| 4 | Denver International Airport |  | US | 363 |
| 5 | Indira Gandhi International Airport |  | IN | 356 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 262 |
| 8 | Harry Reid International Airport |  | US | 256 |
| 9 | Zurich Airport |  | CH | 242 |
| 10 | Frankfurt am Main International Airport |  | DE | 229 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 216 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 13 | Chicago O'Hare International Airport |  | US | 210 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 15 | Guaymaral Airport |  | CO | 201 |
| 16 | Macau International Airport |  | MO | 199 |
| 17 | Bengaluru International Airport |  | IN | 193 |
| 18 | Charlotte/Douglas International Airport |  | US | 190 |
| 19 | Madrid Barajas International Airport |  | ES | 187 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 179 |
| 21 | Tenerife Norte Airport |  | ES | 178 |
| 22 | Ninoy Aquino International Airport |  | PH | 171 |
| 23 | Congonhas Airport |  | BR | 167 |
| 24 | Kuala Lumpur International Airport |  | MY | 159 |
| 25 | Salt Lake City International Airport |  | US | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 153 |
| 28 | Malpensa International Airport |  | IT | 151 |
| 29 | Charles de Gaulle International Airport |  | FR | 148 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 147 |
| 31 | Vitoria/Foronda Airport |  | ES | 145 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 137 |
| 35 | O. R. Tambo International Airport |  | ZA | 136 |
| 36 | Pune Airport |  | IN | 133 |
| 37 | Barcelona International Airport |  | ES | 132 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 94 | 1h 8m | 706 km | 1,144.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 68 | 28m | 304 km | 356.5 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 58 | 1h 27m | 910 km | 910.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 56 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 42 | 23m | 252 km | 182.4 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 42 | 1h 12m | 770 km | 557.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 40 | 54m | 546 km | 376.6 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 25 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 27 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 34 | 20m | 250 km | 146.9 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1722 | IndiGo | Chek Lap Kok International Airport (VHHH) | Phonngbyin Airport (VYPB) | 2026-04-06 07:32 UTC | 2026-04-06 10:42 UTC | 3h 10m |
| MAI274 | MAI | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-04-06 10:03 UTC | 2026-04-06 10:14 UTC | 10m |
| UAL871 | United Airlines | San Francisco International Airport (KSFO) | Longtan Air Base (RCDI) | 2026-04-05 21:19 UTC | 2026-04-06 10:13 UTC | 12h 54m |
| JST573 | JST | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-04-06 07:58 UTC | 2026-04-06 10:10 UTC | 2h 12m |
| IGO176 | IndiGo | Indira Gandhi International Airport (VIDP) | Bengaluru International Airport (VOBL) | 2026-04-06 07:57 UTC | 2026-04-06 10:06 UTC | 2h 8m |
| GRVBH | GRV | Sleap Airport (EGCV) | Sleap Airport (EGCV) | 2026-04-06 09:53 UTC | 2026-04-06 10:05 UTC | 11m |
| RLB833 | RLB | Diosdado Macapagal International Airport (RPLC) | Wasig Airport (RPVL) | 2026-04-06 09:02 UTC | 2026-04-06 09:50 UTC | 48m |
| AUA362M | Austrian Airlines | Charles de Gaulle International Airport (LFPG) | Vienna International Airport (LOWW) | 2026-04-06 08:14 UTC | 2026-04-06 09:50 UTC | 1h 35m |
| RYR2WH | Ryanair | Toulouse-Blagnac Airport (LFBO) | Ifrane Airport (GMFI) | 2026-04-06 08:15 UTC | 2026-04-06 09:46 UTC | 1h 31m |
| C17 |  | Timmersdorf Airport (LOGT) | Graz Airport (LOWG) | 2026-04-06 09:22 UTC | 2026-04-06 09:46 UTC | 23m |
| N104AE |  | Stanton Airport (KI50) | Blue Grass Airport (KLEX) | 2026-04-06 09:25 UTC | 2026-04-06 09:43 UTC | 18m |
| N90RT |  | Shreveport Regional Airport (KSHV) | Leesville Airport (KL39) | 2026-04-06 09:23 UTC | 2026-04-06 09:41 UTC | 18m |
| IGO273W | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lengpui Airport (VELP) | 2026-04-06 08:59 UTC | 2026-04-06 09:34 UTC | 34m |
|  |  | Bergen Airport Flesland (ENBR) | Kristiansund Airport Kvernberget (ENKB) | 2026-04-06 08:49 UTC | 2026-04-06 09:33 UTC | 43m |
| DLH1JH | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-04-06 08:31 UTC | 2026-04-06 09:32 UTC | 1h 0m |
| 83C |  | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-06 08:56 UTC | 2026-04-06 09:31 UTC | 35m |
| JAL669 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-06 08:15 UTC | 2026-04-06 09:31 UTC | 1h 15m |
| SWR2WX | Swiss International | Copenhagen Kastrup Airport (EKCH) | Zurich Airport (LSZH) | 2026-04-06 08:09 UTC | 2026-04-06 09:30 UTC | 1h 21m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-06 08:59 UTC | 2026-04-06 09:29 UTC | 30m |
| RYR4125 | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Capua Airport (LIAU) | 2026-04-06 08:24 UTC | 2026-04-06 09:29 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
