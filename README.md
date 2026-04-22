# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_18:32:01_UTC-green)

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

**Latest saved flight:** 2026-04-22 18:32:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 18:32:01 UTC

- **48,563** saved flights
- **19,712** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,563** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **582,206.1 tonnes** estimated CO2 emissions
- **33,751,080 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2062 |
| 2 | SkyWest Airlines | 1870 |
| 3 | IndiGo | 1138 |
| 4 | EJA | 838 |
| 5 | American Airlines | 802 |
| 6 | Southwest Airlines | 690 |
| 7 | ENY | 629 |
| 8 | Lufthansa | 546 |
| 9 | Vueling | 486 |
| 10 | AXM | 481 |
| 11 | LATAM Airlines | 474 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 415 |
| 14 | Delta Air Lines | 400 |
| 15 | WIF | 399 |
| 16 | QLK | 386 |
| 17 | LXJ | 372 |
| 18 | Swiss International | 369 |
| 19 | AEE | 331 |
| 20 | Alaska Airlines | 326 |
| 21 | EJU | 318 |
| 22 | easyJet | 310 |
| 23 | VIV | 308 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 277 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | JetBlue | 256 |
| 29 | United Airlines | 252 |
| 30 | GLO | 246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 38588 |
| 2 | 🇮🇳 IN | 3553 |
| 3 | 🇪🇸 ES | 3524 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2835 |
| 6 | 🇯🇵 JP | 2646 |
| 7 | 🇮🇹 IT | 2627 |
| 8 | 🇩🇪 DE | 2553 |
| 9 | 🇨🇦 CA | 2404 |
| 10 | 🇨🇴 CO | 2265 |
| 11 | 🇬🇧 GB | 2010 |
| 12 | 🇫🇷 FR | 1856 |
| 13 | 🇲🇽 MX | 1506 |
| 14 | 🇬🇷 GR | 1492 |
| 15 | 🇨🇭 CH | 1327 |
| 16 | 🇳🇴 NO | 1278 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 1002 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 872 |
| 21 | 🇹🇷 TR | 856 |
| 22 | 🇵🇭 PH | 843 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 772 |
| 25 | 🇬🇹 GT | 753 |
| 26 | 🇲🇦 MA | 595 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 496 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 436 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1135 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 807 |
| 4 | El Dorado International Airport |  | CO | 778 |
| 5 | Indira Gandhi International Airport |  | IN | 752 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 737 |
| 7 | Guaymaral Airport |  | CO | 655 |
| 8 | Harry Reid International Airport |  | US | 630 |
| 9 | Zurich Airport |  | CH | 575 |
| 10 | La Aurora Airport |  | GT | 560 |
| 11 | Frankfurt am Main International Airport |  | DE | 520 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 480 |
| 13 | Chicago O'Hare International Airport |  | US | 480 |
| 14 | Kuala Lumpur International Airport |  | MY | 472 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 462 |
| 16 | Macau International Airport |  | MO | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 437 |
| 19 | Bengaluru International Airport |  | IN | 430 |
| 20 | Charlotte/Douglas International Airport |  | US | 416 |
| 21 | Congonhas Airport |  | BR | 408 |
| 22 | Tenerife Norte Airport |  | ES | 404 |
| 23 | Malpensa International Airport |  | IT | 403 |
| 24 | Ninoy Aquino International Airport |  | PH | 390 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 372 |
| 26 | Salt Lake City International Airport |  | US | 364 |
| 27 | Charles de Gaulle International Airport |  | FR | 362 |
| 28 | Daniel K Inouye International Airport |  | US | 360 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 355 |
| 30 | Capua Airport |  | IT | 352 |
| 31 | Vitoria/Foronda Airport |  | ES | 332 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 332 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 330 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | O. R. Tambo International Airport |  | ZA | 323 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 322 |
| 37 | Barcelona International Airport |  | ES | 320 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Calgary International Airport |  | CA | 291 |
| 40 | Viracopos International Airport |  | BR | 288 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 264 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 186 | 14m | 114 km | 364.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 143 | 21m | 244 km | 602.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 117 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 113 | 26m | 275 km | 535.5 t |
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
| EIS91 | EIS | Vilnius International Airport (EYVI) | EYIG (EYIG) | 2026-04-22 17:46 UTC | 2026-04-22 18:32 UTC | 45m |
| STOOGE1 | STO | Randolph Afb Airport (KRND) | Squirrel Creek Ranch Airport (4TE9) | 2026-04-22 18:18 UTC | 2026-04-22 18:31 UTC | 12m |
| N311ZZ |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-22 18:02 UTC | 2026-04-22 18:29 UTC | 27m |
| CXK1037 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-22 17:18 UTC | 2026-04-22 18:26 UTC | 1h 8m |
| MNL08 | MNL | Sierraville Dearwater Airport (KO79) | Palo Alto Airport (KPAO) | 2026-04-22 17:37 UTC | 2026-04-22 18:24 UTC | 46m |
| N6896H |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-22 18:03 UTC | 2026-04-22 18:20 UTC | 17m |
| N475LP |  | Glendale Regional Airport (KGEU) | 99AZ (99AZ) | 2026-04-22 17:09 UTC | 2026-04-22 18:15 UTC | 1h 6m |
| N449BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-22 17:36 UTC | 2026-04-22 18:14 UTC | 37m |
| N825US |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-04-22 17:54 UTC | 2026-04-22 18:10 UTC | 16m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-04-22 17:19 UTC | 2026-04-22 18:10 UTC | 50m |
| N428DR |  | Deer Park Airport (KDEW) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-22 16:29 UTC | 2026-04-22 18:07 UTC | 1h 37m |
| N285BL |  | Winter Haven Regional Airport (KGIF) | Market World Airport (FL16) | 2026-04-22 17:43 UTC | 2026-04-22 18:02 UTC | 19m |
| N199VJ |  | Witham Field (KSUA) | Twin City Airport (K5J9) | 2026-04-22 16:18 UTC | 2026-04-22 18:02 UTC | 1h 43m |
| N437PS |  | Williams Field (5MI7) | Jackson County/Reynolds Field (KJXN) | 2026-04-22 17:47 UTC | 2026-04-22 18:01 UTC | 13m |
| N904TF |  | Northwest Arkansas Ntl Airport (KXNA) | Landers Loop Airport (AR89) | 2026-04-22 17:46 UTC | 2026-04-22 18:00 UTC | 13m |
| N799TH |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-22 17:44 UTC | 2026-04-22 17:57 UTC | 13m |
| JEDDA73 | JED | Pilots Landing Airport (81TE) | Kimble County Airport (KJCT) | 2026-04-22 17:43 UTC | 2026-04-22 17:57 UTC | 14m |
| CFR80 | CFR | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-04-22 17:46 UTC | 2026-04-22 17:55 UTC | 8m |
| FLC78 | FLC | Eppley Airfield (KOMA) | X1 Ranch Airport (8NE5) | 2026-04-22 17:24 UTC | 2026-04-22 17:54 UTC | 29m |
| R72225 |  | Nashville International Airport (KBNA) | Nashville International Airport (KBNA) | 2026-04-22 17:36 UTC | 2026-04-22 17:53 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
