# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_23:38:25_UTC-green)

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

**Latest saved flight:** 2026-04-11 23:38:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 23:38:25 UTC

- **29,881** saved flights
- **13,762** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,881** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **365,066.6 tonnes** estimated CO2 emissions
- **21,163,280 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1228 |
| 2 | Ryanair | 1227 |
| 3 | IndiGo | 767 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 435 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 359 |
| 9 | AXM | 314 |
| 10 | Vueling | 306 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 263 |
| 13 | AZU | 262 |
| 14 | QLK | 254 |
| 15 | Delta Air Lines | 246 |
| 16 | LXJ | 239 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 201 |
| 19 | VIV | 194 |
| 20 | EJU | 193 |
| 21 | easyJet | 193 |
| 22 | Japan Airlines | 190 |
| 23 | WIF | 187 |
| 24 | AEE | 186 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | GLO | 160 |
| 29 | JetBlue | 158 |
| 30 | Air France | 154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23747 |
| 2 | 🇮🇳 IN | 2359 |
| 3 | 🇪🇸 ES | 2212 |
| 4 | 🇦🇺 AU | 2097 |
| 5 | 🇧🇷 BR | 1732 |
| 6 | 🇯🇵 JP | 1613 |
| 7 | 🇮🇹 IT | 1531 |
| 8 | 🇨🇴 CO | 1516 |
| 9 | 🇩🇪 DE | 1495 |
| 10 | 🇨🇦 CA | 1473 |
| 11 | 🇬🇧 GB | 1201 |
| 12 | 🇫🇷 FR | 1098 |
| 13 | 🇲🇽 MX | 967 |
| 14 | 🇬🇷 GR | 845 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 752 |
| 17 | 🇳🇿 NZ | 640 |
| 18 | 🇳🇴 NO | 632 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇬🇹 GT | 551 |
| 21 | 🇵🇭 PH | 551 |
| 22 | 🇹🇷 TR | 541 |
| 23 | 🇹🇭 TH | 533 |
| 24 | 🇰🇷 KR | 504 |
| 25 | 🇵🇱 PL | 450 |
| 26 | 🇲🇦 MA | 373 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 298 |
| 29 | 🇳🇱 NL | 286 |
| 30 | 🇲🇴 MO | 281 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | El Dorado International Airport |  | CO | 540 |
| 3 | Tokyo International Airport |  | JP | 540 |
| 4 | Denver International Airport |  | US | 511 |
| 5 | Indira Gandhi International Airport |  | IN | 493 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 413 |
| 7 | La Aurora Airport |  | GT | 393 |
| 8 | Harry Reid International Airport |  | US | 388 |
| 9 | Guaymaral Airport |  | CO | 359 |
| 10 | Zurich Airport |  | CH | 358 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 12 | Chicago O'Hare International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 302 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 290 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 281 |
| 18 | Charlotte/Douglas International Airport |  | US | 271 |
| 19 | Bengaluru International Airport |  | IN | 268 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Ninoy Aquino International Airport |  | PH | 253 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 239 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 231 |
| 26 | Daniel K Inouye International Airport |  | US | 230 |
| 27 | Salt Lake City International Airport |  | US | 230 |
| 28 | Reno/Tahoe International Airport |  | US | 229 |
| 29 | Charles de Gaulle International Airport |  | FR | 211 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 31 | Capua Airport |  | IT | 205 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 200 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 200 |
| 34 | Miami International Airport |  | US | 200 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 193 |
| 38 | Seattle-Tacoma International Airport |  | US | 190 |
| 39 | Barcelona International Airport |  | ES | 189 |
| 40 | Viracopos International Airport |  | BR | 183 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 125 | 14m | 114 km | 245.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 110 | 24m | 225 km | 426.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 75 | 21m | 99 km | 128.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 57 | 31m | 369 km | 362.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 56 | 52m | 556 km | 536.8 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 46 | 20m | 147 km | 116.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 40 | 55m | 630 km | 434.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AVL120 | AVL | Manassas Regional/Harry P Davis Field (KHEF) | Culpeper Regional Airport (KCJR) | 2026-04-11 23:10 UTC | 2026-04-11 23:38 UTC | 28m |
| N54983 |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-11 22:57 UTC | 2026-04-11 23:32 UTC | 34m |
| N32AW |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-04-11 21:55 UTC | 2026-04-11 23:24 UTC | 1h 29m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-11 20:36 UTC | 2026-04-11 23:23 UTC | 2h 47m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 22:59 UTC | 2026-04-11 23:20 UTC | 21m |
| N93QM |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-04-11 22:43 UTC | 2026-04-11 23:19 UTC | 35m |
| AZG5962 | AZG | Frankfurt-Hahn Airport (EDFH) | Macau International Airport (VMMC) | 2026-04-11 04:58 UTC | 2026-04-11 23:14 UTC | 18h 15m |
| N817FG |  | Williamsport Regional Airport (KIPT) | Lancaster Airport (KLNS) | 2026-04-11 22:12 UTC | 2026-04-11 23:05 UTC | 53m |
| SXS6BM | SXS | Antalya International Airport (LTAI) | Munster Osnabruck Airport (EDDG) | 2026-04-11 19:17 UTC | 2026-04-11 23:00 UTC | 3h 43m |
| R2015 |  | Ballina Byron Gateway Airport (YBNA) | Ballina Byron Gateway Airport (YBNA) | 2026-04-11 22:47 UTC | 2026-04-11 22:59 UTC | 12m |
| N950TT |  | Wheeler Army Air Field (PHHI) | Kawaihapai Airfield (PHDH) | 2026-04-11 22:22 UTC | 2026-04-11 22:57 UTC | 34m |
| EJA347 | EJA | Scottsdale Airport (KSDL) | Henderson Executive Airport (KHND) | 2026-04-11 22:13 UTC | 2026-04-11 22:55 UTC | 41m |
| GEC8462 | GEC | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-11 12:17 UTC | 2026-04-11 22:53 UTC | 10h 36m |
| CGGGQ | CGG | La Ronge (Barber Field) Airport (CYVC) | Regina Beach Airport (CKL9) | 2026-04-11 21:48 UTC | 2026-04-11 22:53 UTC | 1h 5m |
| N757EH |  | Denton Enterprise Airport (KDTO) | Spectre Field (XA07) | 2026-04-11 22:13 UTC | 2026-04-11 22:52 UTC | 38m |
| AAL2753 | American Airlines | Philadelphia International Airport (KPHL) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-11 21:19 UTC | 2026-04-11 22:50 UTC | 1h 30m |
| N4223X |  | Dover Afb Airport (KDOV) | Dover Afb Airport (KDOV) | 2026-04-11 22:47 UTC | 2026-04-11 22:49 UTC | 2m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 22:27 UTC | 2026-04-11 22:49 UTC | 21m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-04-11 22:31 UTC | 2026-04-11 22:49 UTC | 18m |
| ENY4074 | ENY | Dallas-Fort Worth International Airport (KDFW) | Newton Municipal Airport (K61R) | 2026-04-11 22:11 UTC | 2026-04-11 22:48 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
