# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_19:49:30_UTC-green)

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

**Latest saved flight:** 2026-04-19 19:49:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 19:49:30 UTC

- **43,855** saved flights
- **18,272** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,855** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **527,311.1 tonnes** estimated CO2 emissions
- **30,568,756 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1856 |
| 2 | SkyWest Airlines | 1701 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 752 |
| 5 | American Airlines | 720 |
| 6 | Southwest Airlines | 621 |
| 7 | ENY | 569 |
| 8 | AXM | 446 |
| 9 | Lufthansa | 438 |
| 10 | Vueling | 438 |
| 11 | LATAM Airlines | 435 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 385 |
| 14 | Delta Air Lines | 374 |
| 15 | QLK | 354 |
| 16 | LXJ | 345 |
| 17 | WIF | 344 |
| 18 | Swiss International | 337 |
| 19 | AEE | 299 |
| 20 | Alaska Airlines | 294 |
| 21 | EJU | 291 |
| 22 | easyJet | 281 |
| 23 | VIV | 278 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | United Airlines | 236 |
| 27 | AXB | 232 |
| 28 | GLO | 230 |
| 29 | JetBlue | 230 |
| 30 | EDV | 223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34608 |
| 2 | 🇮🇳 IN | 3299 |
| 3 | 🇪🇸 ES | 3241 |
| 4 | 🇦🇺 AU | 3034 |
| 5 | 🇧🇷 BR | 2618 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2330 |
| 8 | 🇩🇪 DE | 2233 |
| 9 | 🇨🇦 CA | 2132 |
| 10 | 🇨🇴 CO | 2023 |
| 11 | 🇬🇧 GB | 1781 |
| 12 | 🇫🇷 FR | 1679 |
| 13 | 🇲🇽 MX | 1364 |
| 14 | 🇬🇷 GR | 1354 |
| 15 | 🇨🇭 CH | 1202 |
| 16 | 🇳🇴 NO | 1093 |
| 17 | 🇲🇾 MY | 1090 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 792 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 776 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 722 |
| 25 | 🇵🇱 PL | 701 |
| 26 | 🇲🇦 MA | 546 |
| 27 | 🇲🇪 ME | 462 |
| 28 | 🇳🇱 NL | 449 |
| 29 | 🇧🇸 BS | 407 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1023 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 725 |
| 4 | Indira Gandhi International Airport |  | IN | 710 |
| 5 | El Dorado International Airport |  | CO | 706 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 674 |
| 7 | Harry Reid International Airport |  | US | 559 |
| 8 | Guaymaral Airport |  | CO | 553 |
| 9 | La Aurora Airport |  | GT | 533 |
| 10 | Zurich Airport |  | CH | 526 |
| 11 | Chicago O'Hare International Airport |  | US | 432 |
| 12 | Kuala Lumpur International Airport |  | MY | 432 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 430 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 424 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Bengaluru International Airport |  | IN | 392 |
| 19 | Madrid Barajas International Airport |  | ES | 390 |
| 20 | Tenerife Norte Airport |  | ES | 388 |
| 21 | Charlotte/Douglas International Airport |  | US | 379 |
| 22 | Congonhas Airport |  | BR | 375 |
| 23 | Ninoy Aquino International Airport |  | PH | 367 |
| 24 | Malpensa International Airport |  | IT | 365 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 333 |
| 26 | Salt Lake City International Airport |  | US | 333 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Charles de Gaulle International Airport |  | FR | 324 |
| 29 | Daniel K Inouye International Airport |  | US | 323 |
| 30 | Reno/Tahoe International Airport |  | US | 306 |
| 31 | Vitoria/Foronda Airport |  | ES | 305 |
| 32 | Capua Airport |  | IT | 303 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 303 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 282 |
| 38 | Viracopos International Airport |  | BR | 267 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 262 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 223 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 166 | 14m | 114 km | 325.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 121 | 21m | 244 km | 509.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 108 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 101 | 26m | 275 km | 478.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 90 | 20m | 99 km | 154.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 52m | 1,304 km | 1,372.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-19 18:59 UTC | 2026-04-19 19:49 UTC | 50m |
| AFL1247 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-19 15:06 UTC | 2026-04-19 19:48 UTC | 4h 41m |
| N716AT |  | Ralph Wien Memorial Airport (PAOT) | Robert/Bob/Curtis Memorial Airport (PFNO) | 2026-04-19 19:28 UTC | 2026-04-19 19:45 UTC | 16m |
| BOBCT25 | BOB | Pensacola International Airport (KPNS) | MS27 (MS27) | 2026-04-19 19:27 UTC | 2026-04-19 19:42 UTC | 15m |
| VIV2034 | VIV | Cancun International Airport (MMUN) | Plan De Guadalupe International Airport (MMIO) | 2026-04-19 17:19 UTC | 2026-04-19 19:38 UTC | 2h 19m |
| N811DK |  | Zamperini Field (KTOA) | Riverside Airport (KRAL) | 2026-04-19 19:06 UTC | 2026-04-19 19:37 UTC | 31m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-19 19:17 UTC | 2026-04-19 19:30 UTC | 13m |
| CGEAI | CGE | Rocky Mountain House Airport (CYRM) | Rocky Mountain House Airport (CYRM) | 2026-04-19 19:12 UTC | 2026-04-19 19:25 UTC | 13m |
| N202LS |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-19 19:13 UTC | 2026-04-19 19:23 UTC | 10m |
| N52331 |  | Albert Whitted Airport (KSPG) | Albert Whitted Airport (KSPG) | 2026-04-19 18:46 UTC | 2026-04-19 19:16 UTC | 29m |
| N9285H |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-19 18:25 UTC | 2026-04-19 19:16 UTC | 50m |
| N7516Z |  | Byron Airport (KC83) | Byron Airport (KC83) | 2026-04-19 19:13 UTC | 2026-04-19 19:15 UTC | 2m |
| N5633R |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-19 18:39 UTC | 2026-04-19 19:15 UTC | 36m |
| N302AZ |  | Orlando Sanford International Airport (KSFB) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-19 18:36 UTC | 2026-04-19 19:15 UTC | 38m |
| N649SP |  | Dane County Regional/Truax Field (KMSN) | Washington Dulles International Airport (KIAD) | 2026-04-19 17:51 UTC | 2026-04-19 19:14 UTC | 1h 22m |
| N581RS |  | St Simons Island Airport (KSSI) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-19 18:27 UTC | 2026-04-19 19:13 UTC | 46m |
| N723BG |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-19 18:59 UTC | 2026-04-19 19:13 UTC | 14m |
| N355PC |  | Bay Minette Municipal Airport (K1R8) | Russell County Airport (KK24) | 2026-04-19 17:46 UTC | 2026-04-19 19:12 UTC | 1h 26m |
| CFLOE | CFL | Edmonton / Cooking Lake Airport (CEZ3) | Tofield Airport (CEV7) | 2026-04-19 18:58 UTC | 2026-04-19 19:12 UTC | 14m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-04-19 18:46 UTC | 2026-04-19 19:12 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
