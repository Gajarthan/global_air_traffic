# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_12:38:31_UTC-green)

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

**Latest saved flight:** 2026-04-21 12:38:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 12:38:31 UTC

- **46,583** saved flights
- **19,106** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,583** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **561,402.1 tonnes** estimated CO2 emissions
- **32,545,047 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1981 |
| 2 | SkyWest Airlines | 1799 |
| 3 | IndiGo | 1102 |
| 4 | EJA | 800 |
| 5 | American Airlines | 770 |
| 6 | Southwest Airlines | 670 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 492 |
| 9 | Vueling | 473 |
| 10 | AXM | 468 |
| 11 | LATAM Airlines | 461 |
| 12 | All Nippon Airways | 421 |
| 13 | AZU | 397 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 376 |
| 16 | WIF | 368 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 357 |
| 19 | Alaska Airlines | 318 |
| 20 | AEE | 317 |
| 21 | EJU | 312 |
| 22 | VIV | 298 |
| 23 | easyJet | 297 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 265 |
| 26 | Cathay Pacific | 249 |
| 27 | JetBlue | 249 |
| 28 | United Airlines | 246 |
| 29 | AXB | 245 |
| 30 | GLO | 237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36912 |
| 2 | 🇮🇳 IN | 3425 |
| 3 | 🇪🇸 ES | 3414 |
| 4 | 🇦🇺 AU | 3229 |
| 5 | 🇧🇷 BR | 2722 |
| 6 | 🇯🇵 JP | 2566 |
| 7 | 🇮🇹 IT | 2527 |
| 8 | 🇩🇪 DE | 2406 |
| 9 | 🇨🇦 CA | 2270 |
| 10 | 🇨🇴 CO | 2144 |
| 11 | 🇬🇧 GB | 1909 |
| 12 | 🇫🇷 FR | 1771 |
| 13 | 🇲🇽 MX | 1445 |
| 14 | 🇬🇷 GR | 1421 |
| 15 | 🇨🇭 CH | 1282 |
| 16 | 🇳🇴 NO | 1172 |
| 17 | 🇲🇾 MY | 1142 |
| 18 | 🇿🇦 ZA | 968 |
| 19 | 🇳🇿 NZ | 911 |
| 20 | 🇹🇭 TH | 844 |
| 21 | 🇵🇭 PH | 831 |
| 22 | 🇹🇷 TR | 822 |
| 23 | 🇰🇷 KR | 771 |
| 24 | 🇵🇱 PL | 739 |
| 25 | 🇬🇹 GT | 737 |
| 26 | 🇲🇦 MA | 579 |
| 27 | 🇲🇪 ME | 495 |
| 28 | 🇳🇱 NL | 477 |
| 29 | 🇲🇴 MO | 437 |
| 30 | 🇧🇸 BS | 420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1096 |
| 2 | Tokyo International Airport |  | JP | 873 |
| 3 | Denver International Airport |  | US | 775 |
| 4 | El Dorado International Airport |  | CO | 751 |
| 5 | Indira Gandhi International Airport |  | IN | 736 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 706 |
| 7 | Harry Reid International Airport |  | US | 602 |
| 8 | Guaymaral Airport |  | CO | 584 |
| 9 | Zurich Airport |  | CH | 551 |
| 10 | La Aurora Airport |  | GT | 545 |
| 11 | Frankfurt am Main International Airport |  | DE | 464 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 13 | Chicago O'Hare International Airport |  | US | 459 |
| 14 | Kuala Lumpur International Airport |  | MY | 457 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 447 |
| 16 | Macau International Airport |  | MO | 437 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 417 |
| 19 | Bengaluru International Airport |  | IN | 411 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 399 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 389 |
| 24 | Ninoy Aquino International Airport |  | PH | 384 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 355 |
| 26 | Daniel K Inouye International Airport |  | US | 347 |
| 27 | Salt Lake City International Airport |  | US | 346 |
| 28 | Charles de Gaulle International Airport |  | FR | 345 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 344 |
| 30 | Capua Airport |  | IT | 342 |
| 31 | Reno/Tahoe International Airport |  | US | 322 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 321 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 319 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 36 | O. R. Tambo International Airport |  | ZA | 311 |
| 37 | Barcelona International Airport |  | ES | 309 |
| 38 | Don Mueang International Airport |  | TH | 284 |
| 39 | Calgary International Airport |  | CA | 280 |
| 40 | Viracopos International Airport |  | BR | 277 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 176 | 14m | 114 km | 345.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 135 | 21m | 244 km | 568.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 124 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 124 | 19m | 165 km | 352.7 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 111 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 70 | 13m | 99 km | 120.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N445B |  | Doylestown Airport (KDYL) | Deck Airport (K9D4) | 2026-04-21 12:01 UTC | 2026-04-21 12:38 UTC | 36m |
| CGSCR | CGS | Peterborough Airport (CYPQ) | CME2 (CME2) | 2026-04-21 12:14 UTC | 2026-04-21 12:29 UTC | 14m |
| N374BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-21 11:50 UTC | 2026-04-21 12:26 UTC | 35m |
| N491LP |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-21 10:52 UTC | 2026-04-21 12:09 UTC | 1h 17m |
| N75270 |  | Republic Airport (KFRG) | Meriden Markham Municipal Airport (KMMK) | 2026-04-21 11:24 UTC | 2026-04-21 12:05 UTC | 41m |
| N604D |  | Richmond International Airport (KRIC) | Norfolk International Airport (KORF) | 2026-04-21 11:43 UTC | 2026-04-21 12:00 UTC | 16m |
| OARIX3 | OAR | La Axarquia-Leoni Benabu Airport (LEAX) | La Axarquia-Leoni Benabu Airport (LEAX) | 2026-04-21 11:01 UTC | 2026-04-21 11:58 UTC | 57m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-21 11:49 UTC | 2026-04-21 11:56 UTC | 7m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Hausen am Albis Airport (LSZN) | 2026-04-21 11:34 UTC | 2026-04-21 11:56 UTC | 21m |
| EWG6100 | EWG | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-04-21 11:09 UTC | 2026-04-21 11:51 UTC | 41m |
| HB3500 |  | Ambri Airport (LSPM) | Muenster Aero Airport (LSPU) | 2026-04-21 11:06 UTC | 2026-04-21 11:49 UTC | 43m |
| HB2512 |  | Samedan Airport (LSZS) | Samedan Airport (LSZS) | 2026-04-21 10:33 UTC | 2026-04-21 11:49 UTC | 1h 15m |
| SAS2892 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-21 10:45 UTC | 2026-04-21 11:48 UTC | 1h 2m |
| LLR723 | LLR | Shillong Airport (VEBI) | Rupsi India Airport (VERU) | 2026-04-21 11:18 UTC | 2026-04-21 11:47 UTC | 29m |
| N15TC |  | Springdale Municipal Airport (KASG) | Danville Municipal Airport (K32A) | 2026-04-21 11:27 UTC | 2026-04-21 11:46 UTC | 19m |
| RYR8LC | Ryanair | Warsaw Modlin Airport (EPMO) | Bari / Palese International Airport (LIBD) | 2026-04-21 09:51 UTC | 2026-04-21 11:44 UTC | 1h 52m |
| HKS39 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-04-21 11:23 UTC | 2026-04-21 11:43 UTC | 19m |
| N41FA |  | Lakeland Linder International Airport (KLAL) | Bartow Executive Airport (KBOW) | 2026-04-21 11:32 UTC | 2026-04-21 11:43 UTC | 10m |
| RYR5909 | Ryanair | Nimes-Arles-Camargue Airport (LFTW) | Taza Airport (GMFZ) | 2026-04-21 09:51 UTC | 2026-04-21 11:43 UTC | 1h 51m |
| SAS4546 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-04-21 10:07 UTC | 2026-04-21 11:41 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
