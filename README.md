# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_19:48:06_UTC-green)

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

**Latest saved flight:** 2026-04-22 19:48:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 19:48:06 UTC

- **48,727** saved flights
- **19,769** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,727** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **583,825.8 tonnes** estimated CO2 emissions
- **33,844,972 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2072 |
| 2 | SkyWest Airlines | 1881 |
| 3 | IndiGo | 1138 |
| 4 | EJA | 841 |
| 5 | American Airlines | 805 |
| 6 | Southwest Airlines | 692 |
| 7 | ENY | 633 |
| 8 | Lufthansa | 550 |
| 9 | Vueling | 487 |
| 10 | AXM | 481 |
| 11 | LATAM Airlines | 476 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 415 |
| 14 | WIF | 402 |
| 15 | Delta Air Lines | 401 |
| 16 | QLK | 386 |
| 17 | LXJ | 373 |
| 18 | Swiss International | 371 |
| 19 | AEE | 331 |
| 20 | Alaska Airlines | 327 |
| 21 | EJU | 318 |
| 22 | easyJet | 312 |
| 23 | VIV | 309 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 277 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 256 |
| 30 | GLO | 246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 38777 |
| 2 | 🇮🇳 IN | 3553 |
| 3 | 🇪🇸 ES | 3534 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2841 |
| 6 | 🇯🇵 JP | 2646 |
| 7 | 🇮🇹 IT | 2639 |
| 8 | 🇩🇪 DE | 2565 |
| 9 | 🇨🇦 CA | 2410 |
| 10 | 🇨🇴 CO | 2273 |
| 11 | 🇬🇧 GB | 2016 |
| 12 | 🇫🇷 FR | 1858 |
| 13 | 🇲🇽 MX | 1515 |
| 14 | 🇬🇷 GR | 1492 |
| 15 | 🇨🇭 CH | 1331 |
| 16 | 🇳🇴 NO | 1284 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 1002 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 872 |
| 21 | 🇹🇷 TR | 858 |
| 22 | 🇵🇭 PH | 843 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 776 |
| 25 | 🇬🇹 GT | 755 |
| 26 | 🇲🇦 MA | 598 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 497 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1144 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 815 |
| 4 | El Dorado International Airport |  | CO | 780 |
| 5 | Indira Gandhi International Airport |  | IN | 752 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 737 |
| 7 | Guaymaral Airport |  | CO | 659 |
| 8 | Harry Reid International Airport |  | US | 635 |
| 9 | Zurich Airport |  | CH | 577 |
| 10 | La Aurora Airport |  | GT | 562 |
| 11 | Frankfurt am Main International Airport |  | DE | 526 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 484 |
| 13 | Chicago O'Hare International Airport |  | US | 483 |
| 14 | Kuala Lumpur International Airport |  | MY | 472 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 462 |
| 16 | Macau International Airport |  | MO | 454 |
| 17 | Madrid Barajas International Airport |  | ES | 440 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 19 | Bengaluru International Airport |  | IN | 430 |
| 20 | Charlotte/Douglas International Airport |  | US | 417 |
| 21 | Congonhas Airport |  | BR | 409 |
| 22 | Tenerife Norte Airport |  | ES | 405 |
| 23 | Malpensa International Airport |  | IT | 404 |
| 24 | Ninoy Aquino International Airport |  | PH | 390 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 373 |
| 26 | Salt Lake City International Airport |  | US | 366 |
| 27 | Daniel K Inouye International Airport |  | US | 362 |
| 28 | Charles de Gaulle International Airport |  | FR | 362 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 355 |
| 30 | Capua Airport |  | IT | 353 |
| 31 | Vitoria/Foronda Airport |  | ES | 334 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 333 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 331 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 324 |
| 36 | O. R. Tambo International Airport |  | ZA | 323 |
| 37 | Barcelona International Airport |  | ES | 321 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Calgary International Airport |  | CA | 291 |
| 40 | Viracopos International Airport |  | BR | 288 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 266 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 188 | 14m | 114 km | 368.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 144 | 21m | 244 km | 606.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 118 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 115 | 26m | 275 km | 544.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 69 | 1h 42m | 1,156 km | 1,376.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 0m | 695 km | 815.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1986H |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-04-22 19:13 UTC | 2026-04-22 19:48 UTC | 34m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-22 19:35 UTC | 2026-04-22 19:46 UTC | 11m |
| N269ME |  | Daniel K Inouye International Airport (PHNL) | PHNP (PHNP) | 2026-04-22 19:34 UTC | 2026-04-22 19:40 UTC | 5m |
| HLE27 | HLE | London City Airport (EGLC) | RAF Northolt (EGWU) | 2026-04-22 19:20 UTC | 2026-04-22 19:37 UTC | 16m |
| N262WJ |  | Aurora Municipal Airport (KARR) | IS94 (IS94) | 2026-04-22 19:24 UTC | 2026-04-22 19:31 UTC | 7m |
| ABF8 | ABF | Liege Airport (EBLG) | Tallinn Airport (EETN) | 2026-04-22 17:10 UTC | 2026-04-22 19:31 UTC | 2h 20m |
| N4888C |  | Dupont/Lapeer Airport (KD95) | Romeo State Airport (KD98) | 2026-04-22 19:07 UTC | 2026-04-22 19:23 UTC | 16m |
| WIF56G | WIF | Bergen Airport Flesland (ENBR) | Gothenburg-Landvetter Airport (ESGG) | 2026-04-22 18:18 UTC | 2026-04-22 19:21 UTC | 1h 3m |
| N525E |  | Phoenix Sky Harbor International Airport (KPHX) | Sedona Airport (KSEZ) | 2026-04-22 19:02 UTC | 2026-04-22 19:21 UTC | 18m |
| CAP5033 | CAP | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-22 18:08 UTC | 2026-04-22 19:20 UTC | 1h 11m |
| N3939S |  | Smyrna Airport (KMQY) | Lebanon Municipal Airport (KM54) | 2026-04-22 19:01 UTC | 2026-04-22 19:18 UTC | 17m |
| EDGE91 | EDG | OK79 (OK79) | Ksa Orchards Airport (OK11) | 2026-04-22 18:43 UTC | 2026-04-22 19:18 UTC | 34m |
| N2776L |  | Auburn University Regional Airport (KAUO) | Lanett Regional Airport (K7A3) | 2026-04-22 19:03 UTC | 2026-04-22 19:16 UTC | 12m |
| N75799 |  | Fort Lauderdale Executive Airport (KFXE) | Witham Field (KSUA) | 2026-04-22 18:20 UTC | 2026-04-22 19:16 UTC | 55m |
| N601RC |  | Indian Hills Airpark (2AZ1) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-22 17:16 UTC | 2026-04-22 19:15 UTC | 1h 58m |
| ERU392 | ERU | Daytona Beach International Airport (KDAB) | Orlando Executive Airport (KORL) | 2026-04-22 18:29 UTC | 2026-04-22 19:12 UTC | 42m |
| N432BL |  | Kent Fort Manor Airport (7MD8) | Lancaster Airport (KLNS) | 2026-04-22 18:27 UTC | 2026-04-22 19:12 UTC | 44m |
| N2147D |  | Fullerton Municipal Airport (KFUL) | AZ86 (AZ86) | 2026-04-22 17:10 UTC | 2026-04-22 19:12 UTC | 2h 2m |
| N954AC |  | Miami Executive Airport (KTMB) | Dade-Collier Training And Transition Airport (KTNT) | 2026-04-22 18:54 UTC | 2026-04-22 19:09 UTC | 14m |
| NEMO05 | NEM | Sarzana / Luni Military Airport (LIQW) | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | 2026-04-22 18:34 UTC | 2026-04-22 19:08 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
