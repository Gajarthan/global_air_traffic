# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_20:11:08_UTC-green)

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

**Latest saved flight:** 2026-04-24 20:11:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 20:11:08 UTC

- **52,440** saved flights
- **20,960** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,440** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **625,739.0 tonnes** estimated CO2 emissions
- **36,274,723 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2204 |
| 2 | SkyWest Airlines | 1981 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 922 |
| 5 | American Airlines | 842 |
| 6 | Southwest Airlines | 744 |
| 7 | ENY | 664 |
| 8 | Lufthansa | 614 |
| 9 | Vueling | 525 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 500 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 444 |
| 14 | WIF | 437 |
| 15 | Delta Air Lines | 433 |
| 16 | QLK | 412 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 389 |
| 19 | AEE | 354 |
| 20 | Alaska Airlines | 346 |
| 21 | EJU | 332 |
| 22 | VIV | 331 |
| 23 | easyJet | 330 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 273 |
| 28 | JetBlue | 270 |
| 29 | United Airlines | 270 |
| 30 | GLO | 266 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 41793 |
| 2 | 🇪🇸 ES | 3789 |
| 3 | 🇮🇳 IN | 3770 |
| 4 | 🇦🇺 AU | 3570 |
| 5 | 🇧🇷 BR | 3022 |
| 6 | 🇮🇹 IT | 2819 |
| 7 | 🇯🇵 JP | 2809 |
| 8 | 🇩🇪 DE | 2799 |
| 9 | 🇨🇦 CA | 2606 |
| 10 | 🇨🇴 CO | 2414 |
| 11 | 🇬🇧 GB | 2178 |
| 12 | 🇫🇷 FR | 2040 |
| 13 | 🇲🇽 MX | 1614 |
| 14 | 🇬🇷 GR | 1585 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1418 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1087 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 943 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 837 |
| 25 | 🇬🇹 GT | 804 |
| 26 | 🇲🇦 MA | 643 |
| 27 | 🇲🇪 ME | 558 |
| 28 | 🇳🇱 NL | 532 |
| 29 | 🇲🇴 MO | 499 |
| 30 | 🇧🇸 BS | 458 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1200 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 870 |
| 4 | El Dorado International Airport |  | CO | 821 |
| 5 | Indira Gandhi International Airport |  | IN | 805 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 786 |
| 7 | Guaymaral Airport |  | CO | 717 |
| 8 | Harry Reid International Airport |  | US | 674 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 601 |
| 11 | Frankfurt am Main International Airport |  | DE | 601 |
| 12 | Chicago O'Hare International Airport |  | US | 520 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 513 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 501 |
| 15 | Macau International Airport |  | MO | 499 |
| 16 | Kuala Lumpur International Airport |  | MY | 491 |
| 17 | Madrid Barajas International Airport |  | ES | 483 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 438 |
| 21 | Malpensa International Airport |  | IT | 437 |
| 22 | Charlotte/Douglas International Airport |  | US | 431 |
| 23 | Tenerife Norte Airport |  | ES | 415 |
| 24 | Ninoy Aquino International Airport |  | PH | 414 |
| 25 | Charles de Gaulle International Airport |  | FR | 398 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 391 |
| 27 | Salt Lake City International Airport |  | US | 389 |
| 28 | Daniel K Inouye International Airport |  | US | 380 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 368 |
| 31 | Vitoria/Foronda Airport |  | ES | 358 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 354 |
| 33 | Reno/Tahoe International Airport |  | US | 351 |
| 34 | Barcelona International Airport |  | ES | 351 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 348 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 346 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 314 |
| 40 | Viracopos International Airport |  | BR | 308 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 290 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 157 | 21m | 244 km | 661.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 130 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 95 | 20m | 99 km | 162.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 81 | 52m | 556 km | 776.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 74 | 1h 0m | 695 km | 887.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 68 | 12m | 15 km | 17.9 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 53m | 1,304 km | 1,529.8 t |
| 28 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 67 | 13m | - | - |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 67 | 24m | 55 km | 63.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-24 05:54 UTC | 2026-04-24 20:11 UTC | 14h 16m |
| N442TH |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-04-24 18:44 UTC | 2026-04-24 20:03 UTC | 1h 19m |
| N7SG |  | Phoenix Sky Harbor International Airport (KPHX) | Willow Springs Ranch Airport (1AZ8) | 2026-04-24 19:25 UTC | 2026-04-24 19:57 UTC | 32m |
| N102PG |  | Boise Air Trml/Gowen Field (KBOI) | Boeing Field/King County International Airport (KBFI) | 2026-04-24 18:55 UTC | 2026-04-24 19:56 UTC | 1h 0m |
| N48ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-24 19:17 UTC | 2026-04-24 19:56 UTC | 38m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-04-24 19:04 UTC | 2026-04-24 19:56 UTC | 51m |
| BOE242 | BOE | Boeing Field/King County International Airport (KBFI) | Crown Creek Ranch Airport (57WA) | 2026-04-24 18:39 UTC | 2026-04-24 19:55 UTC | 1h 15m |
| HRD44 | HRD | WV76 (WV76) | Lawrence County Airpark (KHTW) | 2026-04-24 19:26 UTC | 2026-04-24 19:51 UTC | 25m |
| N827Z |  | Harry Reid International Airport (KLAS) | Harrisburg International Airport (KMDT) | 2026-04-24 16:03 UTC | 2026-04-24 19:50 UTC | 3h 46m |
| 4438 |  | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 2026-04-24 19:44 UTC | 2026-04-24 19:49 UTC | 4m |
| WIF6Y | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-24 19:36 UTC | 2026-04-24 19:48 UTC | 11m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-24 18:16 UTC | 2026-04-24 19:45 UTC | 1h 28m |
| N95LG |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-24 18:37 UTC | 2026-04-24 19:45 UTC | 1h 8m |
| ATAC41 | ATA | Luke Afb Airport (KLUF) | AZ00 (AZ00) | 2026-04-24 19:15 UTC | 2026-04-24 19:45 UTC | 29m |
| N11PS |  | Quentin Aanenson Field (KLYV) | Brookings Regional Airport (KBKX) | 2026-04-24 19:22 UTC | 2026-04-24 19:43 UTC | 20m |
| N29AV |  | Pompano Beach Airpark (KPMP) | Palm Beach County Park Airport (KLNA) | 2026-04-24 18:58 UTC | 2026-04-24 19:41 UTC | 43m |
| LYM3583 | LYM | Denver International Airport (KDEN) | Geary Ranch Airport (CO65) | 2026-04-24 19:19 UTC | 2026-04-24 19:41 UTC | 22m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-24 18:53 UTC | 2026-04-24 19:40 UTC | 47m |
| N8CB |  | Dekalb-Peachtree Airport (KPDK) | Marion County-Rankin Fite Airport (KHAB) | 2026-04-24 19:08 UTC | 2026-04-24 19:38 UTC | 29m |
| N36GB |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-04-24 19:23 UTC | 2026-04-24 19:37 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
