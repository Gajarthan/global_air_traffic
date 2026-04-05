# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_23:37:28_UTC-green)

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

**Latest saved flight:** 2026-04-05 23:37:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 23:37:28 UTC

- **19,293** saved flights
- **9,765** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,293** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **243,648.3 tonnes** estimated CO2 emissions
- **14,124,537 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 851 |
| 2 | Ryanair | 789 |
| 3 | IndiGo | 541 |
| 4 | American Airlines | 373 |
| 5 | EJA | 363 |
| 6 | Southwest Airlines | 280 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 256 |
| 9 | Vueling | 210 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 176 |
| 13 | LXJ | 169 |
| 14 | All Nippon Airways | 161 |
| 15 | QLK | 157 |
| 16 | AZU | 149 |
| 17 | VIV | 147 |
| 18 | Swiss International | 142 |
| 19 | Alaska Airlines | 131 |
| 20 | United Airlines | 131 |
| 21 | Avianca | 130 |
| 22 | easyJet | 124 |
| 23 | Japan Airlines | 124 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | EDV | 118 |
| 27 | WIF | 116 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15257 |
| 2 | 🇮🇳 IN | 1641 |
| 3 | 🇪🇸 ES | 1569 |
| 4 | 🇦🇺 AU | 1336 |
| 5 | 🇧🇷 BR | 1124 |
| 6 | 🇨🇴 CO | 1048 |
| 7 | 🇯🇵 JP | 1002 |
| 8 | 🇩🇪 DE | 966 |
| 9 | 🇮🇹 IT | 908 |
| 10 | 🇨🇦 CA | 853 |
| 11 | 🇬🇧 GB | 744 |
| 12 | 🇫🇷 FR | 700 |
| 13 | 🇲🇽 MX | 675 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 505 |
| 16 | 🇬🇹 GT | 452 |
| 17 | 🇲🇾 MY | 441 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 408 |
| 20 | 🇳🇴 NO | 391 |
| 21 | 🇹🇷 TR | 369 |
| 22 | 🇵🇭 PH | 362 |
| 23 | 🇰🇷 KR | 329 |
| 24 | 🇵🇱 PL | 278 |
| 25 | 🇹🇭 TH | 274 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 477 |
| 2 | El Dorado International Airport |  | CO | 400 |
| 3 | Denver International Airport |  | US | 359 |
| 4 | Indira Gandhi International Airport |  | IN | 343 |
| 5 | Tokyo International Airport |  | JP | 342 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 253 |
| 9 | Zurich Airport |  | CH | 233 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 215 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 210 |
| 13 | Chicago O'Hare International Airport |  | US | 209 |
| 14 | Guaymaral Airport |  | CO | 200 |
| 15 | Macau International Airport |  | MO | 198 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 194 |
| 17 | Charlotte/Douglas International Airport |  | US | 190 |
| 18 | Madrid Barajas International Airport |  | ES | 184 |
| 19 | Bengaluru International Airport |  | IN | 183 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 177 |
| 21 | Tenerife Norte Airport |  | ES | 174 |
| 22 | Congonhas Airport |  | BR | 167 |
| 23 | Ninoy Aquino International Airport |  | PH | 165 |
| 24 | Salt Lake City International Airport |  | US | 157 |
| 25 | Kuala Lumpur International Airport |  | MY | 155 |
| 26 | Daniel K Inouye International Airport |  | US | 153 |
| 27 | Reno/Tahoe International Airport |  | US | 152 |
| 28 | Malpensa International Airport |  | IT | 146 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 31 | Charles de Gaulle International Airport |  | FR | 143 |
| 32 | Miami International Airport |  | US | 140 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 131 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 130 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 130 |
| 37 | Barcelona International Airport |  | ES | 130 |
| 38 | Pune Airport |  | IN | 129 |
| 39 | O. R. Tambo International Airport |  | ZA | 127 |
| 40 | Seattle-Tacoma International Airport |  | US | 125 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 88 | 14m | 114 km | 172.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 86 | 1h 8m | 706 km | 1,047.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 70 | 24m | 225 km | 271.6 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 41 | 1h 12m | 770 km | 544.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 34 | 58m | 723 km | 423.9 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N361ME |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-04-05 23:23 UTC | 2026-04-05 23:37 UTC | 13m |
| N315NG |  | Phoenix Goodyear Airport (KGYR) | Shiprock Airstrip (K5V5) | 2026-04-05 22:16 UTC | 2026-04-05 23:31 UTC | 1h 15m |
| ZKPDZ | ZKP | Glenorchy Airport (NZGY) | Queenstown International Airport (NZQN) | 2026-04-05 22:35 UTC | 2026-04-05 23:17 UTC | 41m |
| OAI | OAI | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-05 22:57 UTC | 2026-04-05 23:16 UTC | 19m |
| HL5247 |  | Gimpo International Airport (RKSS) | G 419 Airport (RK48) | 2026-04-05 22:44 UTC | 2026-04-05 23:11 UTC | 27m |
| N8351L |  | Tulsa Riverside Airport (KRVS) | Gregg Airport (7OK1) | 2026-04-05 22:48 UTC | 2026-04-05 23:11 UTC | 23m |
| FFT1081 | FFT | Washington Dulles International Airport (KIAD) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-04-05 21:50 UTC | 2026-04-05 23:10 UTC | 1h 19m |
| DAL554 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-04-05 19:07 UTC | 2026-04-05 23:08 UTC | 4h 0m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-05 22:59 UTC | 2026-04-05 23:07 UTC | 7m |
| SXS8SD | SXS | Antalya International Airport (LTAI) | Lublin Radwiec Airport (EPLR) | 2026-04-05 20:31 UTC | 2026-04-05 23:03 UTC | 2h 31m |
| N694DA |  | 3WI1 (3WI1) | 3WI1 (3WI1) | 2026-04-05 22:43 UTC | 2026-04-05 23:01 UTC | 17m |
| N67AF |  | Nashville International Airport (KBNA) | Austin-Bergstrom International Airport (KAUS) | 2026-04-05 20:51 UTC | 2026-04-05 22:58 UTC | 2h 6m |
| N560WR |  | Lubbock Executive Airpark (KF82) | 81NM (81NM) | 2026-04-05 22:26 UTC | 2026-04-05 22:56 UTC | 29m |
| SKW6064 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Ida Grove Municipal Airport (KIDG) | 2026-04-05 21:52 UTC | 2026-04-05 22:55 UTC | 1h 3m |
| 00000000 |  | San Diego International Airport (KSAN) | Jacqueline Cochran Regional Airport (KTRM) | 2026-04-05 22:36 UTC | 2026-04-05 22:54 UTC | 18m |
| EJA878 | EJA | Van Nuys Airport (KVNY) | San Francisco International Airport (KSFO) | 2026-04-05 21:55 UTC | 2026-04-05 22:52 UTC | 57m |
| AAL2627 | American Airlines | Chicago O'Hare International Airport (KORD) | South Haven Area Regional Airport (KLWA) | 2026-04-05 22:24 UTC | 2026-04-05 22:51 UTC | 26m |
| ENY3581 | ENY | Chicago O'Hare International Airport (KORD) | West Bend Municipal Airport (KETB) | 2026-04-05 22:17 UTC | 2026-04-05 22:51 UTC | 33m |
| SWA1269 | Southwest Airlines | Denver International Airport (KDEN) | Paddock Field (41WI) | 2026-04-05 21:00 UTC | 2026-04-05 22:51 UTC | 1h 51m |
| USC102 | USC | Addison Airport (KADS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-05 20:37 UTC | 2026-04-05 22:50 UTC | 2h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
