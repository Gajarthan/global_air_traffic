# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_11:21:01_UTC-green)

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

**Latest saved flight:** 2026-04-06 11:21:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 11:21:01 UTC

- **19,755** saved flights
- **9,906** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,755** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **249,350.5 tonnes** estimated CO2 emissions
- **14,455,103 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 818 |
| 3 | IndiGo | 564 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 262 |
| 9 | Vueling | 215 |
| 10 | LATAM Airlines | 209 |
| 11 | AXM | 197 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 175 |
| 14 | LXJ | 171 |
| 15 | QLK | 164 |
| 16 | AZU | 150 |
| 17 | Swiss International | 149 |
| 18 | VIV | 149 |
| 19 | easyJet | 135 |
| 20 | United Airlines | 134 |
| 21 | Alaska Airlines | 132 |
| 22 | Japan Airlines | 132 |
| 23 | Avianca | 130 |
| 24 | EJU | 128 |
| 25 | AEE | 124 |
| 26 | EDV | 118 |
| 27 | WIF | 118 |
| 28 | AXB | 115 |
| 29 | Air France | 110 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15374 |
| 2 | 🇮🇳 IN | 1720 |
| 3 | 🇪🇸 ES | 1596 |
| 4 | 🇦🇺 AU | 1407 |
| 5 | 🇧🇷 BR | 1130 |
| 6 | 🇯🇵 JP | 1082 |
| 7 | 🇨🇴 CO | 1058 |
| 8 | 🇩🇪 DE | 991 |
| 9 | 🇮🇹 IT | 969 |
| 10 | 🇨🇦 CA | 859 |
| 11 | 🇬🇧 GB | 775 |
| 12 | 🇫🇷 FR | 728 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 565 |
| 15 | 🇨🇭 CH | 528 |
| 16 | 🇲🇾 MY | 460 |
| 17 | 🇬🇹 GT | 452 |
| 18 | 🇿🇦 ZA | 441 |
| 19 | 🇳🇿 NZ | 416 |
| 20 | 🇳🇴 NO | 408 |
| 21 | 🇹🇷 TR | 384 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 298 |
| 25 | 🇵🇱 PL | 287 |
| 26 | 🇲🇦 MA | 244 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 214 |
| 29 | 🇲🇪 ME | 209 |
| 30 | 🇲🇴 MO | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 483 |
| 2 | El Dorado International Airport |  | CO | 405 |
| 3 | Tokyo International Airport |  | JP | 373 |
| 4 | Denver International Airport |  | US | 363 |
| 5 | Indira Gandhi International Airport |  | IN | 358 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 266 |
| 8 | Harry Reid International Airport |  | US | 257 |
| 9 | Zurich Airport |  | CH | 243 |
| 10 | Frankfurt am Main International Airport |  | DE | 232 |
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
| 22 | Ninoy Aquino International Airport |  | PH | 172 |
| 23 | Congonhas Airport |  | BR | 168 |
| 24 | Kuala Lumpur International Airport |  | MY | 159 |
| 25 | Salt Lake City International Airport |  | US | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 154 |
| 28 | Malpensa International Airport |  | IT | 151 |
| 29 | Charles de Gaulle International Airport |  | FR | 149 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 147 |
| 31 | Vitoria/Foronda Airport |  | ES | 145 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 139 |
| 35 | O. R. Tambo International Airport |  | ZA | 137 |
| 36 | Pune Airport |  | IN | 134 |
| 37 | Barcelona International Airport |  | ES | 133 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 58 | 1h 27m | 910 km | 910.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 56 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 42 | 23m | 252 km | 182.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 40 | 54m | 546 km | 376.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 37 | 13m | 99 km | 63.4 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 25 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 27 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 34 | 20m | 250 km | 146.9 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 30 | 20m | 147 km | 75.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6042Z |  | Sarasota/Bradenton International Airport (KSRQ) | Venice Municipal Airport (KVNC) | 2026-04-06 11:07 UTC | 2026-04-06 11:21 UTC | 13m |
| AUL508 | AUL | Murmansk Airport (ULMM) | Pushkin Airport (ULLP) | 2026-04-06 09:55 UTC | 2026-04-06 11:01 UTC | 1h 5m |
| AFL1044 | AFL | Sheremetyevo International Airport (UUEE) | Beslan Airport (URMO) | 2026-04-06 08:14 UTC | 2026-04-06 10:57 UTC | 2h 43m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-06 10:39 UTC | 2026-04-06 10:51 UTC | 12m |
| OAL068 | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-06 10:25 UTC | 2026-04-06 10:49 UTC | 23m |
| AWH46A | AWH | Leipzig Halle Airport (EDDP) | Logrono-Agoncillo Airport (LELO) | 2026-04-06 08:43 UTC | 2026-04-06 10:44 UTC | 2h 1m |
| WZZ3606 | Wizz Air | Larnaca International Airport (LCLK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-06 07:39 UTC | 2026-04-06 10:44 UTC | 3h 4m |
| IGO1722 | IndiGo | Chek Lap Kok International Airport (VHHH) | Phonngbyin Airport (VYPB) | 2026-04-06 07:32 UTC | 2026-04-06 10:42 UTC | 3h 10m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-04-06 10:00 UTC | 2026-04-06 10:36 UTC | 36m |
| QAV30E | QAV | John Paul II International Airport Kraków-Balice Airport (EPKK) | Perugia / San Egidio Airport (LIRZ) | 2026-04-06 09:13 UTC | 2026-04-06 10:35 UTC | 1h 21m |
| MEDIC01 | MED | Leeuwarden Air Base (EHLW) | Ameland Airport (EHAL) | 2026-04-06 10:29 UTC | 2026-04-06 10:35 UTC | 5m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-04-06 10:14 UTC | 2026-04-06 10:34 UTC | 20m |
| RYR84TT | Ryanair | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 2026-04-06 09:09 UTC | 2026-04-06 10:34 UTC | 1h 25m |
| AIC6AB | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-06 10:14 UTC | 2026-04-06 10:34 UTC | 19m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-06 09:09 UTC | 2026-04-06 10:32 UTC | 1h 23m |
| DLH1558 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Iasi Airport (LRIA) | 2026-04-06 08:46 UTC | 2026-04-06 10:26 UTC | 1h 40m |
| DLH4PP | Lufthansa | Frankfurt am Main International Airport (EDDF) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-06 07:58 UTC | 2026-04-06 10:26 UTC | 2h 28m |
| ANA373 | All Nippon Airways | Kerama Airport (ROKR) | Saga Airport (RJFS) | 2026-04-06 06:44 UTC | 2026-04-06 10:23 UTC | 3h 39m |
| APG329 | APG | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 2026-04-06 09:49 UTC | 2026-04-06 10:22 UTC | 33m |
| JEC5110 | JEC | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 2026-04-06 10:07 UTC | 2026-04-06 10:21 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
