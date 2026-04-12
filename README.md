# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_20:51:43_UTC-green)

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

**Latest saved flight:** 2026-04-12 20:51:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 20:51:43 UTC

- **31,342** saved flights
- **14,241** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,342** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **384,850.5 tonnes** estimated CO2 emissions
- **22,310,176 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1311 |
| 2 | SkyWest Airlines | 1273 |
| 3 | IndiGo | 804 |
| 4 | American Airlines | 546 |
| 5 | EJA | 546 |
| 6 | Southwest Airlines | 456 |
| 7 | ENY | 425 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 335 |
| 10 | Vueling | 320 |
| 11 | LATAM Airlines | 318 |
| 12 | All Nippon Airways | 287 |
| 13 | AZU | 276 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 258 |
| 16 | LXJ | 245 |
| 17 | Swiss International | 233 |
| 18 | easyJet | 210 |
| 19 | Alaska Airlines | 209 |
| 20 | WIF | 206 |
| 21 | EJU | 204 |
| 22 | VIV | 201 |
| 23 | AEE | 197 |
| 24 | Japan Airlines | 197 |
| 25 | United Airlines | 184 |
| 26 | EDV | 183 |
| 27 | Avianca | 170 |
| 28 | GLO | 170 |
| 29 | Air France | 169 |
| 30 | JetBlue | 167 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24698 |
| 2 | 🇮🇳 IN | 2468 |
| 3 | 🇪🇸 ES | 2337 |
| 4 | 🇦🇺 AU | 2173 |
| 5 | 🇧🇷 BR | 1853 |
| 6 | 🇯🇵 JP | 1713 |
| 7 | 🇮🇹 IT | 1643 |
| 8 | 🇩🇪 DE | 1592 |
| 9 | 🇨🇴 CO | 1580 |
| 10 | 🇨🇦 CA | 1508 |
| 11 | 🇬🇧 GB | 1271 |
| 12 | 🇫🇷 FR | 1157 |
| 13 | 🇲🇽 MX | 1001 |
| 14 | 🇬🇷 GR | 892 |
| 15 | 🇨🇭 CH | 879 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 695 |
| 18 | 🇳🇿 NZ | 667 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 580 |
| 21 | 🇹🇷 TR | 577 |
| 22 | 🇵🇭 PH | 575 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 477 |
| 26 | 🇲🇦 MA | 403 |
| 27 | 🇧🇸 BS | 330 |
| 28 | 🇲🇪 ME | 312 |
| 29 | 🇳🇱 NL | 300 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 754 |
| 2 | Tokyo International Airport |  | JP | 576 |
| 3 | El Dorado International Airport |  | CO | 561 |
| 4 | Denver International Airport |  | US | 530 |
| 5 | Indira Gandhi International Airport |  | IN | 520 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 437 |
| 7 | La Aurora Airport |  | GT | 419 |
| 8 | Harry Reid International Airport |  | US | 407 |
| 9 | Zurich Airport |  | CH | 386 |
| 10 | Guaymaral Airport |  | CO | 384 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 325 |
| 12 | Chicago O'Hare International Airport |  | US | 323 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 321 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 292 |
| 18 | Charlotte/Douglas International Airport |  | US | 283 |
| 19 | Tenerife Norte Airport |  | ES | 282 |
| 20 | Bengaluru International Airport |  | IN | 281 |
| 21 | Madrid Barajas International Airport |  | ES | 280 |
| 22 | Congonhas Airport |  | BR | 270 |
| 23 | Ninoy Aquino International Airport |  | PH | 264 |
| 24 | Malpensa International Airport |  | IT | 253 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 240 |
| 26 | Reno/Tahoe International Airport |  | US | 239 |
| 27 | Daniel K Inouye International Airport |  | US | 238 |
| 28 | Salt Lake City International Airport |  | US | 238 |
| 29 | Charles de Gaulle International Airport |  | FR | 229 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 226 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 216 |
| 32 | Capua Airport |  | IT | 216 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 211 |
| 35 | Miami International Airport |  | US | 210 |
| 36 | O. R. Tambo International Airport |  | ZA | 209 |
| 37 | Vitoria/Foronda Airport |  | ES | 207 |
| 38 | Seattle-Tacoma International Airport |  | US | 197 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 149 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 132 | 14m | 114 km | 258.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 74 | 9m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 71 | 27m | 152 km | 185.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 67 | 27m | 275 km | 317.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 60 | 21m | 244 km | 252.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
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
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 44 | 16m | 162 km | 123.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N576JA |  | Frederick Municipal Airport (KFDK) | II14 (II14) | 2026-04-12 19:28 UTC | 2026-04-12 20:51 UTC | 1h 22m |
| SAVER20 | SAV | Bodø Airport (ENBO) | Sandnessjoen Airport Stokka (ENST) | 2026-04-12 19:59 UTC | 2026-04-12 20:50 UTC | 51m |
| UAE9836 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-12 14:28 UTC | 2026-04-12 20:50 UTC | 6h 22m |
| CFYUL | CFY | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-04-12 20:29 UTC | 2026-04-12 20:50 UTC | 21m |
| RYR9KJ | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-04-12 19:19 UTC | 2026-04-12 20:46 UTC | 1h 27m |
| WCP253 | WCP | Treasure Coast International Airport (KFPR) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-12 17:45 UTC | 2026-04-12 20:45 UTC | 2h 59m |
| OCN3HT | OCN | Frankfurt am Main International Airport (EDDF) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 11:05 UTC | 2026-04-12 20:45 UTC | 9h 39m |
| N380PK |  | Naples Municipal Airport (KAPF) | Koenig Airport (8CO8) | 2026-04-12 16:52 UTC | 2026-04-12 20:43 UTC | 3h 50m |
| N904CH |  | Livingston County/Spencer J Hardy Airport (KOZW) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-04-12 20:41 UTC | 2026-04-12 20:42 UTC | 0m |
| N606SG |  | Palm Beach International Airport (KPBI) | Southwest Georgia Regional Airport (KABY) | 2026-04-12 19:38 UTC | 2026-04-12 20:39 UTC | 1h 1m |
| N563FL |  | Boss Airport (08KY) | Duff Airport (44KY) | 2026-04-12 20:13 UTC | 2026-04-12 20:39 UTC | 25m |
| N379VM |  | Georgetown Executive Airport (KGTU) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-04-12 19:09 UTC | 2026-04-12 20:37 UTC | 1h 28m |
| N300LX |  | Phoenix Deer Valley Airport (KDVT) | 2AZ7 (2AZ7) | 2026-04-12 20:23 UTC | 2026-04-12 20:30 UTC | 7m |
| N732LA |  | Cherry Hill Airport (40IN) | Lancaster Airport (KLNS) | 2026-04-12 17:58 UTC | 2026-04-12 20:30 UTC | 2h 31m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-12 19:30 UTC | 2026-04-12 20:25 UTC | 55m |
| N493LG |  | CO54 (CO54) | 7CO1 (7CO1) | 2026-04-12 20:01 UTC | 2026-04-12 20:24 UTC | 23m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-12 20:02 UTC | 2026-04-12 20:24 UTC | 21m |
| CPA085 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-12 05:10 UTC | 2026-04-12 20:23 UTC | 15h 12m |
| DLH2KK | Lufthansa | Frankfurt am Main International Airport (EDDF) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 20:22 UTC | 2026-04-12 20:22 UTC | 0m |
| WSN1 | WSN | Phoenix Sky Harbor International Airport (KPHX) | Greenlee County Airport (KCFT) | 2026-04-12 19:46 UTC | 2026-04-12 20:22 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
