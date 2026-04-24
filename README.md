# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_11:01:54_UTC-green)

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

**Latest saved flight:** 2026-04-24 11:01:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 11:01:54 UTC

- **50,983** saved flights
- **20,436** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,983** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **610,262.1 tonnes** estimated CO2 emissions
- **35,377,514 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2148 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1189 |
| 4 | EJA | 878 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 723 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 592 |
| 9 | Vueling | 510 |
| 10 | AXM | 504 |
| 11 | LATAM Airlines | 494 |
| 12 | All Nippon Airways | 464 |
| 13 | AZU | 432 |
| 14 | WIF | 420 |
| 15 | Delta Air Lines | 419 |
| 16 | QLK | 412 |
| 17 | Swiss International | 388 |
| 18 | LXJ | 382 |
| 19 | AEE | 345 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 326 |
| 22 | VIV | 322 |
| 23 | easyJet | 320 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 290 |
| 26 | AXB | 274 |
| 27 | Cathay Pacific | 269 |
| 28 | JetBlue | 263 |
| 29 | United Airlines | 263 |
| 30 | AIQ | 261 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40392 |
| 2 | 🇮🇳 IN | 3732 |
| 3 | 🇪🇸 ES | 3687 |
| 4 | 🇦🇺 AU | 3566 |
| 5 | 🇧🇷 BR | 2942 |
| 6 | 🇯🇵 JP | 2803 |
| 7 | 🇮🇹 IT | 2728 |
| 8 | 🇩🇪 DE | 2721 |
| 9 | 🇨🇦 CA | 2543 |
| 10 | 🇨🇴 CO | 2347 |
| 11 | 🇬🇧 GB | 2107 |
| 12 | 🇫🇷 FR | 1956 |
| 13 | 🇲🇽 MX | 1571 |
| 14 | 🇬🇷 GR | 1548 |
| 15 | 🇨🇭 CH | 1407 |
| 16 | 🇳🇴 NO | 1371 |
| 17 | 🇲🇾 MY | 1230 |
| 18 | 🇿🇦 ZA | 1050 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 936 |
| 21 | 🇹🇷 TR | 909 |
| 22 | 🇵🇭 PH | 889 |
| 23 | 🇰🇷 KR | 855 |
| 24 | 🇵🇱 PL | 819 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 626 |
| 27 | 🇲🇪 ME | 546 |
| 28 | 🇳🇱 NL | 514 |
| 29 | 🇲🇴 MO | 485 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 953 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 803 |
| 5 | Indira Gandhi International Airport |  | IN | 796 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 765 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 667 |
| 9 | Zurich Airport |  | CH | 598 |
| 10 | Frankfurt am Main International Airport |  | DE | 575 |
| 11 | La Aurora Airport |  | GT | 574 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Kuala Lumpur International Airport |  | MY | 489 |
| 15 | Macau International Airport |  | MO | 485 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 18 | Madrid Barajas International Airport |  | ES | 464 |
| 19 | Bengaluru International Airport |  | IN | 443 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 422 |
| 22 | Malpensa International Airport |  | IT | 418 |
| 23 | Ninoy Aquino International Airport |  | PH | 410 |
| 24 | Tenerife Norte Airport |  | ES | 410 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Charles de Gaulle International Airport |  | FR | 382 |
| 27 | Salt Lake City International Airport |  | US | 377 |
| 28 | Daniel K Inouye International Airport |  | US | 374 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 374 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 32 | Vitoria/Foronda Airport |  | ES | 345 |
| 33 | Reno/Tahoe International Airport |  | US | 342 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 341 |
| 36 | Barcelona International Airport |  | ES | 338 |
| 37 | O. R. Tambo International Airport |  | ZA | 337 |
| 38 | Don Mueang International Airport |  | TH | 317 |
| 39 | Calgary International Airport |  | CA | 309 |
| 40 | Viracopos International Airport |  | BR | 300 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 194 | 14m | 114 km | 380.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 153 | 21m | 244 km | 644.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 128 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 118 | 26m | 275 km | 559.2 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 104 | 44m | 452 km | 810.5 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 91 | 1h 12m | 770 km | 1,208.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 87 | 31m | 369 km | 553.8 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 87 | 20m | 250 km | 375.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 83 | 26m | 215 km | 307.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 81 | 20m | 147 km | 205.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-24 10:25 UTC | 2026-04-24 11:01 UTC | 36m |
| ETP08 | ETP | MoD Boscombe Down Airport (EGDM) | MoD Boscombe Down Airport (EGDM) | 2026-04-24 10:01 UTC | 2026-04-24 10:57 UTC | 56m |
| TCADA | TCA | Milas Bodrum International Airport (LTFE) | Ataturk International Airport (LTBA) | 2026-04-24 10:04 UTC | 2026-04-24 10:48 UTC | 44m |
| LIFTR06 | LIF | Hof-Plauen Airport (EDQM) | Oberpfaffenhofen Airport (EDMO) | 2026-04-24 09:59 UTC | 2026-04-24 10:43 UTC | 44m |
| UAU953 | UAU | MoD Boscombe Down Airport (EGDM) | MoD Boscombe Down Airport (EGDM) | 2026-04-24 10:10 UTC | 2026-04-24 10:37 UTC | 27m |
| 4XHSC |  | LL59 (LL59) | Tel Nov Air Base (LLEK) | 2026-04-24 10:32 UTC | 2026-04-24 10:37 UTC | 5m |
| SKQ78 | SKQ | Burlington/Alamance Regional Airport (KBUY) | West Virginia International Yeager Airport (KCRW) | 2026-04-24 09:52 UTC | 2026-04-24 10:36 UTC | 44m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-04-23 20:13 UTC | 2026-04-24 10:35 UTC | 14h 22m |
| SAS338 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-24 09:45 UTC | 2026-04-24 10:26 UTC | 41m |
| 494LG |  | Simonson Field (80CO) | 14CO (14CO) | 2026-04-24 10:05 UTC | 2026-04-24 10:22 UTC | 16m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-24 09:29 UTC | 2026-04-24 10:21 UTC | 51m |
| FHSBB | FHS | Grenoble-Isere Airport (LFLS) | Fontenay Le Comte Airport (LFFK) | 2026-04-24 08:52 UTC | 2026-04-24 10:08 UTC | 1h 16m |
| VLG83CM | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-04-24 09:10 UTC | 2026-04-24 10:06 UTC | 55m |
| KLM50W | KLM Royal Dutch | London City Airport (EGLC) | Amsterdam Airport Schiphol (EHAM) | 2026-04-24 09:23 UTC | 2026-04-24 10:05 UTC | 41m |
| NOK104 | NOK | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-04-24 09:12 UTC | 2026-04-24 10:02 UTC | 49m |
| CHX29 | CHX | Hamburg Airport (EDDH) | Luneburg Airport (EDHG) | 2026-04-24 09:50 UTC | 2026-04-24 10:02 UTC | 12m |
| IGO394 | IndiGo | Agartala Airport (VEAT) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-24 08:55 UTC | 2026-04-24 09:59 UTC | 1h 3m |
| FIH30 | FIH | Tampere-Pirkkala Airport (EFTP) | Tampere-Pirkkala Airport (EFTP) | 2026-04-24 09:48 UTC | 2026-04-24 09:58 UTC | 10m |
| EXS1RG | EXS | Glasgow International Airport (EGPF) | Isparta Airport (LTBM) | 2026-04-24 05:50 UTC | 2026-04-24 09:55 UTC | 4h 5m |
| SWR75L | Swiss International | Dublin Airport (EIDW) | Zurich Airport (LSZH) | 2026-04-24 08:07 UTC | 2026-04-24 09:55 UTC | 1h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
