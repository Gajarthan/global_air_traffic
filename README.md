# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_16:03:20_UTC-green)

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

**Latest saved flight:** 2026-04-19 16:03:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 16:03:20 UTC

- **43,279** saved flights
- **18,077** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,279** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **521,015.7 tonnes** estimated CO2 emissions
- **30,203,810 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1823 |
| 2 | SkyWest Airlines | 1661 |
| 3 | IndiGo | 1069 |
| 4 | EJA | 737 |
| 5 | American Airlines | 708 |
| 6 | Southwest Airlines | 601 |
| 7 | ENY | 561 |
| 8 | AXM | 446 |
| 9 | Lufthansa | 434 |
| 10 | LATAM Airlines | 434 |
| 11 | Vueling | 432 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 382 |
| 14 | Delta Air Lines | 366 |
| 15 | QLK | 354 |
| 16 | LXJ | 338 |
| 17 | Swiss International | 337 |
| 18 | WIF | 336 |
| 19 | AEE | 293 |
| 20 | Alaska Airlines | 290 |
| 21 | EJU | 286 |
| 22 | easyJet | 278 |
| 23 | VIV | 272 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 246 |
| 26 | AXB | 231 |
| 27 | United Airlines | 230 |
| 28 | JetBlue | 229 |
| 29 | GLO | 226 |
| 30 | AIQ | 222 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33977 |
| 2 | 🇮🇳 IN | 3291 |
| 3 | 🇪🇸 ES | 3197 |
| 4 | 🇦🇺 AU | 3031 |
| 5 | 🇧🇷 BR | 2590 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2277 |
| 8 | 🇩🇪 DE | 2205 |
| 9 | 🇨🇦 CA | 2092 |
| 10 | 🇨🇴 CO | 2002 |
| 11 | 🇬🇧 GB | 1762 |
| 12 | 🇫🇷 FR | 1666 |
| 13 | 🇲🇽 MX | 1340 |
| 14 | 🇬🇷 GR | 1333 |
| 15 | 🇨🇭 CH | 1200 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1070 |
| 18 | 🇿🇦 ZA | 911 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 765 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 713 |
| 25 | 🇵🇱 PL | 694 |
| 26 | 🇲🇦 MA | 539 |
| 27 | 🇲🇪 ME | 454 |
| 28 | 🇳🇱 NL | 446 |
| 29 | 🇧🇸 BS | 400 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1000 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 708 |
| 4 | Indira Gandhi International Airport |  | IN | 708 |
| 5 | El Dorado International Airport |  | CO | 701 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 663 |
| 7 | Harry Reid International Airport |  | US | 549 |
| 8 | Guaymaral Airport |  | CO | 541 |
| 9 | La Aurora Airport |  | GT | 526 |
| 10 | Zurich Airport |  | CH | 524 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 417 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 414 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 405 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Bengaluru International Airport |  | IN | 390 |
| 19 | Madrid Barajas International Airport |  | ES | 389 |
| 20 | Tenerife Norte Airport |  | ES | 379 |
| 21 | Charlotte/Douglas International Airport |  | US | 373 |
| 22 | Congonhas Airport |  | BR | 372 |
| 23 | Ninoy Aquino International Airport |  | PH | 366 |
| 24 | Malpensa International Airport |  | IT | 357 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 27 | Salt Lake City International Airport |  | US | 327 |
| 28 | Charles de Gaulle International Airport |  | FR | 321 |
| 29 | Daniel K Inouye International Airport |  | US | 320 |
| 30 | Vitoria/Foronda Airport |  | ES | 302 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 302 |
| 32 | Reno/Tahoe International Airport |  | US | 297 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 295 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 294 |
| 35 | O. R. Tambo International Airport |  | ZA | 292 |
| 36 | Capua Airport |  | IT | 292 |
| 37 | Barcelona International Airport |  | ES | 280 |
| 38 | Viracopos International Airport |  | BR | 265 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 218 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 164 | 14m | 114 km | 321.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 119 | 21m | 244 km | 501.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 107 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 101 | 26m | 275 km | 478.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 71 | 20m | 147 km | 179.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 70 | 52m | 556 km | 671.0 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 66 | 26m | 215 km | 244.4 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 61 | 13m | 99 km | 104.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 61 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 59 | 1h 21m | 961 km | 978.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGSGP | CGS | Bantry Aerodrome (EIBN) | Bantry Aerodrome (EIBN) | 2026-04-19 15:05 UTC | 2026-04-19 16:03 UTC | 57m |
| DICEY92 | DIC | 0TS2 (0TS2) | Neuwirth Airstrip (71OK) | 2026-04-19 15:03 UTC | 2026-04-19 16:00 UTC | 56m |
| N564CH |  | Flying Cloud Airport (KFCM) | St Augustine Airport (KSGJ) | 2026-04-19 13:32 UTC | 2026-04-19 15:59 UTC | 2h 27m |
| FFL436 | FFL | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-04-19 15:52 UTC | 2026-04-19 15:56 UTC | 3m |
| N131PA |  | Addison Airport (KADS) | Magee Airport (42TX) | 2026-04-19 14:59 UTC | 2026-04-19 15:56 UTC | 56m |
| N6395B |  | North Fork Valley Airport (K7V2) | Telluride Regional Airport (KTEX) | 2026-04-19 15:14 UTC | 2026-04-19 15:54 UTC | 39m |
| N830CA |  | North Las Vegas Airport (KVGT) | Henderson Executive Airport (KHND) | 2026-04-19 15:42 UTC | 2026-04-19 15:54 UTC | 11m |
| N308AB |  | Cincinnati Municipal/Lunken Field (KLUK) | Julian Carroll Airport (KJKL) | 2026-04-19 15:21 UTC | 2026-04-19 15:51 UTC | 30m |
| N54240 |  | Tucson International Airport (KTUS) | Eric Marcus Municipal Airport (KP01) | 2026-04-19 14:25 UTC | 2026-04-19 15:51 UTC | 1h 25m |
| N110GN |  | Askey Field (9TN5) | Tampa Executive Airport (KVDF) | 2026-04-19 13:43 UTC | 2026-04-19 15:48 UTC | 2h 5m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-19 15:27 UTC | 2026-04-19 15:43 UTC | 16m |
| N408ZW |  | Hidden Valley Airpark (5TX0) | Dreamland Airport (XA48) | 2026-04-19 15:26 UTC | 2026-04-19 15:40 UTC | 13m |
| SXS8BU | SXS | Stuttgart Airport (EDDS) | Kaklic Airport (LTFA) | 2026-04-19 13:23 UTC | 2026-04-19 15:38 UTC | 2h 14m |
| N739PS |  | Shiprock Airstrip (K5V5) | Blanding Municipal Airport (KBDG) | 2026-04-19 15:02 UTC | 2026-04-19 15:36 UTC | 33m |
| N626LA |  | Joe Foss Field (KFSD) | Danville Municipal Airport (K32A) | 2026-04-19 14:20 UTC | 2026-04-19 15:35 UTC | 1h 15m |
| N85WC |  | Yuba County Airport (KMYV) | Sacramento Executive Airport (KSAC) | 2026-04-19 15:20 UTC | 2026-04-19 15:35 UTC | 15m |
| N995CE |  | Oakland County International Airport (KPTK) | Conway-Horry County Airport (KHYW) | 2026-04-19 14:10 UTC | 2026-04-19 15:34 UTC | 1h 24m |
| TRF1 | TRF | Addison Airport (KADS) | Indianhead Ranch Airport (1TS9) | 2026-04-19 15:13 UTC | 2026-04-19 15:32 UTC | 18m |
| SD1 |  | Tri-County Aerodrome (48TX) | 52TA (52TA) | 2026-04-19 14:32 UTC | 2026-04-19 15:32 UTC | 59m |
| N164AS |  | Skywest Inc Airport (K7T7) | Midland International Air And Space Port Airport (KMAF) | 2026-04-19 15:19 UTC | 2026-04-19 15:30 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
