# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_19:47:39_UTC-green)

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

**Latest saved flight:** 2026-04-12 19:47:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 19:47:39 UTC

- **31,135** saved flights
- **14,149** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,135** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **382,135.7 tonnes** estimated CO2 emissions
- **22,152,796 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1300 |
| 2 | SkyWest Airlines | 1262 |
| 3 | IndiGo | 804 |
| 4 | American Airlines | 537 |
| 5 | EJA | 537 |
| 6 | Southwest Airlines | 449 |
| 7 | ENY | 422 |
| 8 | Lufthansa | 369 |
| 9 | AXM | 335 |
| 10 | Vueling | 318 |
| 11 | LATAM Airlines | 311 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 273 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 257 |
| 16 | LXJ | 243 |
| 17 | Swiss International | 231 |
| 18 | easyJet | 208 |
| 19 | Alaska Airlines | 207 |
| 20 | WIF | 206 |
| 21 | EJU | 204 |
| 22 | VIV | 201 |
| 23 | Japan Airlines | 197 |
| 24 | AEE | 196 |
| 25 | United Airlines | 183 |
| 26 | EDV | 182 |
| 27 | Air France | 169 |
| 28 | Avianca | 169 |
| 29 | GLO | 167 |
| 30 | JetBlue | 165 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24495 |
| 2 | 🇮🇳 IN | 2468 |
| 3 | 🇪🇸 ES | 2322 |
| 4 | 🇦🇺 AU | 2173 |
| 5 | 🇧🇷 BR | 1823 |
| 6 | 🇯🇵 JP | 1711 |
| 7 | 🇮🇹 IT | 1631 |
| 8 | 🇩🇪 DE | 1566 |
| 9 | 🇨🇴 CO | 1559 |
| 10 | 🇨🇦 CA | 1499 |
| 11 | 🇬🇧 GB | 1264 |
| 12 | 🇫🇷 FR | 1154 |
| 13 | 🇲🇽 MX | 998 |
| 14 | 🇬🇷 GR | 891 |
| 15 | 🇨🇭 CH | 874 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 691 |
| 18 | 🇳🇿 NZ | 667 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 576 |
| 21 | 🇵🇭 PH | 575 |
| 22 | 🇹🇷 TR | 571 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 476 |
| 26 | 🇲🇦 MA | 402 |
| 27 | 🇧🇸 BS | 329 |
| 28 | 🇲🇪 ME | 311 |
| 29 | 🇳🇱 NL | 297 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 745 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 552 |
| 4 | Denver International Airport |  | US | 523 |
| 5 | Indira Gandhi International Airport |  | IN | 520 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 436 |
| 7 | La Aurora Airport |  | GT | 415 |
| 8 | Harry Reid International Airport |  | US | 403 |
| 9 | Zurich Airport |  | CH | 381 |
| 10 | Guaymaral Airport |  | CO | 379 |
| 11 | Chicago O'Hare International Airport |  | US | 321 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 320 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 320 |
| 14 | Frankfurt am Main International Airport |  | DE | 314 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 290 |
| 18 | Bengaluru International Airport |  | IN | 281 |
| 19 | Charlotte/Douglas International Airport |  | US | 280 |
| 20 | Tenerife Norte Airport |  | ES | 278 |
| 21 | Madrid Barajas International Airport |  | ES | 277 |
| 22 | Congonhas Airport |  | BR | 265 |
| 23 | Ninoy Aquino International Airport |  | PH | 264 |
| 24 | Malpensa International Airport |  | IT | 251 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 239 |
| 26 | Reno/Tahoe International Airport |  | US | 237 |
| 27 | Salt Lake City International Airport |  | US | 237 |
| 28 | Daniel K Inouye International Airport |  | US | 236 |
| 29 | Charles de Gaulle International Airport |  | FR | 229 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 222 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 216 |
| 32 | Capua Airport |  | IT | 216 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 34 | O. R. Tambo International Airport |  | ZA | 209 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 209 |
| 36 | Miami International Airport |  | US | 208 |
| 37 | Vitoria/Foronda Airport |  | ES | 206 |
| 38 | Seattle-Tacoma International Airport |  | US | 197 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 148 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 129 | 14m | 114 km | 253.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 72 | 9m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 71 | 27m | 152 km | 185.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 66 | 27m | 275 km | 312.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 59 | 21m | 244 km | 248.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LHX1U | LHX | London Heathrow Airport (EGLL) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 18:43 UTC | 2026-04-12 19:47 UTC | 1h 3m |
| QXE2276 | QXE | Edmonton International Airport (CYEG) | Seattle-Tacoma International Airport (KSEA) | 2026-04-12 18:17 UTC | 2026-04-12 19:38 UTC | 1h 20m |
| ASA735 | Alaska Airlines | Harry Reid International Airport (KLAS) | Seattle-Tacoma International Airport (KSEA) | 2026-04-12 17:32 UTC | 2026-04-12 19:36 UTC | 2h 4m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-04-12 19:16 UTC | 2026-04-12 19:33 UTC | 16m |
| EVA065 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Chanmyathazi Airport (VYCZ) | 2026-04-12 16:03 UTC | 2026-04-12 19:32 UTC | 3h 28m |
| N670CP |  | Westchester County Airport (KHPN) | Lehigh Valley International Airport (KABE) | 2026-04-12 18:54 UTC | 2026-04-12 19:24 UTC | 30m |
| N11937 |  | Waterbury-Oxford Airport (KOXC) | Tweed/New Haven Airport (KHVN) | 2026-04-12 19:09 UTC | 2026-04-12 19:24 UTC | 14m |
| N203BH |  | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-12 18:29 UTC | 2026-04-12 19:20 UTC | 51m |
| N5522S |  | Addison Airport (KADS) | Denton Enterprise Airport (KDTO) | 2026-04-12 18:30 UTC | 2026-04-12 19:19 UTC | 49m |
| N123JK |  | Springfield-Branson Ntl Airport (KSGF) | Rocky Mountain Metro Airport (KBJC) | 2026-04-12 17:32 UTC | 2026-04-12 19:09 UTC | 1h 36m |
| N604LB |  | Sky Acres Airport (VT25) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-12 17:00 UTC | 2026-04-12 19:07 UTC | 2h 6m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-04-12 18:50 UTC | 2026-04-12 19:05 UTC | 14m |
| N560BE |  | Humann Private Airstrip (ND85) | Myers Field (KCNB) | 2026-04-12 18:36 UTC | 2026-04-12 19:02 UTC | 26m |
| ERY277 | ERY | Burke Lakefront Airport (KBKL) | Washington Dulles International Airport (KIAD) | 2026-04-12 18:09 UTC | 2026-04-12 19:01 UTC | 51m |
| SKW5310 | SkyWest Airlines | Denver International Airport (KDEN) | Ohkay Owingeh Airport (KE14) | 2026-04-12 18:19 UTC | 2026-04-12 18:59 UTC | 39m |
| RYR151B | Ryanair | Stockholm-Arlanda Airport (ESSA) | Paderborn Lippstadt Airport (EDLP) | 2026-04-12 17:09 UTC | 2026-04-12 18:59 UTC | 1h 50m |
| 3023 |  | PA23 (PA23) | 0PA4 (0PA4) | 2026-04-12 18:37 UTC | 2026-04-12 18:59 UTC | 22m |
| N440BV |  | Fort Worth Meacham International Airport (KFTW) | Howard County Airport (KM77) | 2026-04-12 18:18 UTC | 2026-04-12 18:57 UTC | 38m |
| NJE869L | NJE | Stockholm-Bromma Airport (ESSB) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-12 15:51 UTC | 2026-04-12 18:55 UTC | 3h 4m |
| N703RK |  | Jacksonville International Airport (KJAX) | Mores Island Airport (MYA0) | 2026-04-12 18:11 UTC | 2026-04-12 18:53 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
