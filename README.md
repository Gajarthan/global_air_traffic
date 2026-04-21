# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_15:48:58_UTC-green)

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

**Latest saved flight:** 2026-04-21 15:48:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 15:48:58 UTC

- **46,920** saved flights
- **19,206** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,920** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **564,302.1 tonnes** estimated CO2 emissions
- **32,713,167 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1998 |
| 2 | SkyWest Airlines | 1804 |
| 3 | IndiGo | 1106 |
| 4 | EJA | 804 |
| 5 | American Airlines | 773 |
| 6 | Southwest Airlines | 671 |
| 7 | ENY | 608 |
| 8 | Lufthansa | 505 |
| 9 | Vueling | 475 |
| 10 | AXM | 469 |
| 11 | LATAM Airlines | 464 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 399 |
| 14 | Delta Air Lines | 390 |
| 15 | QLK | 376 |
| 16 | WIF | 376 |
| 17 | LXJ | 363 |
| 18 | Swiss International | 360 |
| 19 | AEE | 321 |
| 20 | Alaska Airlines | 318 |
| 21 | EJU | 313 |
| 22 | VIV | 300 |
| 23 | easyJet | 299 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 250 |
| 27 | JetBlue | 250 |
| 28 | AXB | 248 |
| 29 | United Airlines | 246 |
| 30 | GLO | 238 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37175 |
| 2 | 🇮🇳 IN | 3439 |
| 3 | 🇪🇸 ES | 3428 |
| 4 | 🇦🇺 AU | 3235 |
| 5 | 🇧🇷 BR | 2746 |
| 6 | 🇯🇵 JP | 2569 |
| 7 | 🇮🇹 IT | 2555 |
| 8 | 🇩🇪 DE | 2441 |
| 9 | 🇨🇦 CA | 2284 |
| 10 | 🇨🇴 CO | 2182 |
| 11 | 🇬🇧 GB | 1920 |
| 12 | 🇫🇷 FR | 1795 |
| 13 | 🇲🇽 MX | 1453 |
| 14 | 🇬🇷 GR | 1438 |
| 15 | 🇨🇭 CH | 1291 |
| 16 | 🇳🇴 NO | 1201 |
| 17 | 🇲🇾 MY | 1146 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 911 |
| 20 | 🇹🇭 TH | 846 |
| 21 | 🇵🇭 PH | 833 |
| 22 | 🇹🇷 TR | 827 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 743 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 584 |
| 27 | 🇲🇪 ME | 499 |
| 28 | 🇳🇱 NL | 482 |
| 29 | 🇲🇴 MO | 441 |
| 30 | 🇧🇸 BS | 421 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1100 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 777 |
| 4 | El Dorado International Airport |  | CO | 761 |
| 5 | Indira Gandhi International Airport |  | IN | 736 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 712 |
| 7 | Guaymaral Airport |  | CO | 604 |
| 8 | Harry Reid International Airport |  | US | 604 |
| 9 | Zurich Airport |  | CH | 556 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 477 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 13 | Chicago O'Hare International Airport |  | US | 459 |
| 14 | Kuala Lumpur International Airport |  | MY | 459 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 448 |
| 16 | Macau International Airport |  | MO | 441 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 418 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 402 |
| 21 | Malpensa International Airport |  | IT | 400 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 392 |
| 24 | Ninoy Aquino International Airport |  | PH | 385 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 356 |
| 26 | Daniel K Inouye International Airport |  | US | 349 |
| 27 | Charles de Gaulle International Airport |  | FR | 349 |
| 28 | Salt Lake City International Airport |  | US | 348 |
| 29 | Capua Airport |  | IT | 348 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 344 |
| 31 | Reno/Tahoe International Airport |  | US | 323 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 323 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 319 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | O. R. Tambo International Airport |  | ZA | 313 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 37 | Barcelona International Airport |  | ES | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 280 |
| 40 | Viracopos International Airport |  | BR | 279 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 242 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 178 | 14m | 114 km | 349.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 137 | 21m | 244 km | 576.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 75 | 52m | 556 km | 718.9 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 0m | 695 km | 779.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N727DC |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Clearwater Executive Airport (KCLW) | 2026-04-21 15:04 UTC | 2026-04-21 15:48 UTC | 44m |
| N682EE |  | Melbourne Orlando International Airport (KMLB) | Melbourne Orlando International Airport (KMLB) | 2026-04-21 15:08 UTC | 2026-04-21 15:45 UTC | 37m |
| CGEFZ | CGE | Oshawa Airport (CYOO) | CSD7 (CSD7) | 2026-04-21 15:06 UTC | 2026-04-21 15:43 UTC | 37m |
| N203VS |  | Edwards Af Aux North Base Airport (K9L2) | Lone Pine/Death Valley Airport (KO26) | 2026-04-21 15:08 UTC | 2026-04-21 15:43 UTC | 34m |
| N827EC |  | Tucson International Airport (KTUS) | AZ74 (AZ74) | 2026-04-21 15:15 UTC | 2026-04-21 15:41 UTC | 26m |
| N9477L |  | West Georgia Regional/O V Gray Field (KCTJ) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-04-21 14:59 UTC | 2026-04-21 15:40 UTC | 40m |
| BOMR841 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-04-21 15:20 UTC | 2026-04-21 15:37 UTC | 16m |
| N130HB |  | Ohio State University Airport (KOSU) | Ohio State University Airport (KOSU) | 2026-04-21 14:02 UTC | 2026-04-21 15:29 UTC | 1h 27m |
| TOM513 | TOM | Antalya International Airport (LTAI) | Manchester Airport (EGCC) | 2026-04-21 10:57 UTC | 2026-04-21 15:29 UTC | 4h 31m |
| N415AM |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-04-21 14:40 UTC | 2026-04-21 15:29 UTC | 48m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-21 14:05 UTC | 2026-04-21 15:24 UTC | 1h 18m |
| N64023 |  | 84OL (84OL) | Tulsa International Airport (KTUL) | 2026-04-21 15:01 UTC | 2026-04-21 15:23 UTC | 21m |
| HAGAR70 | HAG | Dover Afb Airport (KDOV) | Ass-Pirin Acres Airport (VT11) | 2026-04-21 14:02 UTC | 2026-04-21 15:14 UTC | 1h 12m |
| N9157A |  | Montgomery-Gibbs Executive Airport (KMYF) | CL35 (CL35) | 2026-04-21 14:05 UTC | 2026-04-21 15:14 UTC | 1h 9m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-21 15:02 UTC | 2026-04-21 15:14 UTC | 11m |
| DESRT159 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-21 14:57 UTC | 2026-04-21 15:08 UTC | 11m |
| N153PC |  | Ryan Field (KRYN) | Pinal Airpark (KMZJ) | 2026-04-21 14:54 UTC | 2026-04-21 15:06 UTC | 12m |
| N712PA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-21 14:44 UTC | 2026-04-21 15:04 UTC | 20m |
| BB129 |  | Thomas Farms Airport (85FL) | Evergreen Regional/Middleton Field (KGZH) | 2026-04-21 14:42 UTC | 2026-04-21 15:04 UTC | 21m |
| 4XHPM |  | LL59 (LL59) | LL59 (LL59) | 2026-04-21 14:57 UTC | 2026-04-21 15:03 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
