# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_13:53:56_UTC-green)

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

**Latest saved flight:** 2026-04-24 13:53:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 13:53:56 UTC

- **51,215** saved flights
- **20,502** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **51,215** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **613,336.7 tonnes** estimated CO2 emissions
- **35,555,748 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2163 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1192 |
| 4 | EJA | 879 |
| 5 | American Airlines | 823 |
| 6 | Southwest Airlines | 724 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 598 |
| 9 | Vueling | 515 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 495 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 434 |
| 14 | WIF | 426 |
| 15 | Delta Air Lines | 419 |
| 16 | QLK | 412 |
| 17 | Swiss International | 391 |
| 18 | LXJ | 383 |
| 19 | AEE | 346 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 327 |
| 22 | easyJet | 325 |
| 23 | VIV | 322 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 293 |
| 26 | AXB | 277 |
| 27 | Cathay Pacific | 271 |
| 28 | AIQ | 264 |
| 29 | JetBlue | 264 |
| 30 | United Airlines | 263 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40482 |
| 2 | 🇮🇳 IN | 3750 |
| 3 | 🇪🇸 ES | 3716 |
| 4 | 🇦🇺 AU | 3568 |
| 5 | 🇧🇷 BR | 2952 |
| 6 | 🇯🇵 JP | 2809 |
| 7 | 🇩🇪 DE | 2746 |
| 8 | 🇮🇹 IT | 2740 |
| 9 | 🇨🇦 CA | 2545 |
| 10 | 🇨🇴 CO | 2356 |
| 11 | 🇬🇧 GB | 2131 |
| 12 | 🇫🇷 FR | 1973 |
| 13 | 🇲🇽 MX | 1574 |
| 14 | 🇬🇷 GR | 1555 |
| 15 | 🇨🇭 CH | 1443 |
| 16 | 🇳🇴 NO | 1383 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1062 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 922 |
| 22 | 🇵🇭 PH | 895 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 827 |
| 25 | 🇬🇹 GT | 776 |
| 26 | 🇲🇦 MA | 631 |
| 27 | 🇲🇪 ME | 549 |
| 28 | 🇳🇱 NL | 518 |
| 29 | 🇲🇴 MO | 492 |
| 30 | 🇧🇸 BS | 445 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1177 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 807 |
| 5 | Indira Gandhi International Airport |  | IN | 800 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 769 |
| 7 | Guaymaral Airport |  | CO | 690 |
| 8 | Harry Reid International Airport |  | US | 668 |
| 9 | Zurich Airport |  | CH | 604 |
| 10 | Frankfurt am Main International Airport |  | DE | 582 |
| 11 | La Aurora Airport |  | GT | 578 |
| 12 | Chicago O'Hare International Airport |  | US | 504 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Macau International Airport |  | MO | 492 |
| 15 | Kuala Lumpur International Airport |  | MY | 491 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 17 | Madrid Barajas International Airport |  | ES | 467 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 444 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 424 |
| 22 | Malpensa International Airport |  | IT | 420 |
| 23 | Ninoy Aquino International Airport |  | PH | 413 |
| 24 | Tenerife Norte Airport |  | ES | 410 |
| 25 | Charles de Gaulle International Airport |  | FR | 385 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 384 |
| 27 | Salt Lake City International Airport |  | US | 377 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 376 |
| 29 | Daniel K Inouye International Airport |  | US | 375 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 349 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 346 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 344 |
| 34 | Reno/Tahoe International Airport |  | US | 342 |
| 35 | Barcelona International Airport |  | ES | 342 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 37 | O. R. Tambo International Airport |  | ZA | 340 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 310 |
| 40 | Viracopos International Airport |  | BR | 302 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 279 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 196 | 14m | 114 km | 384.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 154 | 21m | 244 km | 648.5 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 128 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 123 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 119 | 26m | 275 km | 563.9 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 87 | 20m | 250 km | 375.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 84 | 27m | 215 km | 311.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 82 | 20m | 147 km | 207.5 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 78 | 27m | 152 km | 203.8 t |
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
| RPA4368 | Republic Airways | St Louis Lambert International Airport (KSTL) | Jugtown Mountain Airport (2NJ1) | 2026-04-24 11:49 UTC | 2026-04-24 13:53 UTC | 2h 4m |
| SWA168 | Southwest Airlines | Albany International Airport (KALB) | Brandywine Regional Airport (KOQN) | 2026-04-24 12:58 UTC | 2026-04-24 13:53 UTC | 55m |
| N784LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-04-24 12:51 UTC | 2026-04-24 13:53 UTC | 1h 1m |
| N484BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-24 12:16 UTC | 2026-04-24 13:50 UTC | 1h 33m |
| N553XB |  | New York Stewart International Airport (KSWF) | Laguardia Airport (KLGA) | 2026-04-24 13:29 UTC | 2026-04-24 13:47 UTC | 18m |
| WIF66D | WIF | Bodø Airport (ENBO) | Sandnessjoen Airport Stokka (ENST) | 2026-04-24 13:05 UTC | 2026-04-24 13:43 UTC | 38m |
| HBKNS | HBK | Locarno Airport (LSZL) | Lodrino Air Base (LSML) | 2026-04-24 13:25 UTC | 2026-04-24 13:43 UTC | 18m |
| BOXER50 | BOX | Bertani Ranch Airport (23TS) | Sonora Municipal Airport (KSOA) | 2026-04-24 13:32 UTC | 2026-04-24 13:43 UTC | 10m |
| HB2447 |  | Muenster Aero Airport (LSPU) | Ambri Airport (LSPM) | 2026-04-24 13:24 UTC | 2026-04-24 13:40 UTC | 16m |
| RFD9000 | RFD | General Mariano Escobedo International Airport (MMMY) | Plan De Guadalupe International Airport (MMIO) | 2026-04-24 12:50 UTC | 2026-04-24 13:38 UTC | 47m |
| LFA319 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-04-24 13:29 UTC | 2026-04-24 13:36 UTC | 6m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Reichenbach Air Base (LSGR) | 2026-04-24 13:04 UTC | 2026-04-24 13:34 UTC | 30m |
| ERU958 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-24 13:06 UTC | 2026-04-24 13:32 UTC | 25m |
| N26XP |  | Page Field (KFMY) | Southwest Florida International Airport (KRSW) | 2026-04-24 13:17 UTC | 2026-04-24 13:32 UTC | 14m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-24 13:06 UTC | 2026-04-24 13:26 UTC | 20m |
| N7262X |  | Gwinnett County/Briscoe Field (KLZU) | Pickens County Airport (KJZP) | 2026-04-24 12:38 UTC | 2026-04-24 13:23 UTC | 44m |
| CXK568 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-24 11:56 UTC | 2026-04-24 13:22 UTC | 1h 25m |
| N850FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-04-24 12:29 UTC | 2026-04-24 13:21 UTC | 51m |
| SAA063 | SAA | Reitz Airport (FARZ) | Heidelburg Airport (FAHG) | 2026-04-24 12:36 UTC | 2026-04-24 13:20 UTC | 43m |
| N224JA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-24 13:00 UTC | 2026-04-24 13:20 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
