# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_22:05:22_UTC-green)

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

**Latest saved flight:** 2026-04-23 22:05:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 22:05:22 UTC

- **50,321** saved flights
- **20,260** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,321** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **599,962.5 tonnes** estimated CO2 emissions
- **34,780,434 km** total distance flown
- **831 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2129 |
| 2 | SkyWest Airlines | 1928 |
| 3 | IndiGo | 1169 |
| 4 | EJA | 868 |
| 5 | American Airlines | 817 |
| 6 | Southwest Airlines | 712 |
| 7 | ENY | 644 |
| 8 | Lufthansa | 580 |
| 9 | Vueling | 502 |
| 10 | AXM | 495 |
| 11 | LATAM Airlines | 488 |
| 12 | All Nippon Airways | 455 |
| 13 | AZU | 427 |
| 14 | WIF | 417 |
| 15 | Delta Air Lines | 414 |
| 16 | QLK | 406 |
| 17 | LXJ | 379 |
| 18 | Swiss International | 376 |
| 19 | AEE | 343 |
| 20 | Alaska Airlines | 333 |
| 21 | EJU | 325 |
| 22 | VIV | 319 |
| 23 | easyJet | 317 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 284 |
| 26 | AXB | 268 |
| 27 | JetBlue | 263 |
| 28 | United Airlines | 262 |
| 29 | Cathay Pacific | 259 |
| 30 | AIQ | 256 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40044 |
| 2 | 🇮🇳 IN | 3668 |
| 3 | 🇪🇸 ES | 3634 |
| 4 | 🇦🇺 AU | 3477 |
| 5 | 🇧🇷 BR | 2916 |
| 6 | 🇯🇵 JP | 2742 |
| 7 | 🇮🇹 IT | 2697 |
| 8 | 🇩🇪 DE | 2678 |
| 9 | 🇨🇦 CA | 2498 |
| 10 | 🇨🇴 CO | 2334 |
| 11 | 🇬🇧 GB | 2067 |
| 12 | 🇫🇷 FR | 1927 |
| 13 | 🇲🇽 MX | 1551 |
| 14 | 🇬🇷 GR | 1530 |
| 15 | 🇨🇭 CH | 1383 |
| 16 | 🇳🇴 NO | 1348 |
| 17 | 🇲🇾 MY | 1207 |
| 18 | 🇿🇦 ZA | 1038 |
| 19 | 🇳🇿 NZ | 962 |
| 20 | 🇹🇭 TH | 914 |
| 21 | 🇹🇷 TR | 888 |
| 22 | 🇵🇭 PH | 872 |
| 23 | 🇰🇷 KR | 827 |
| 24 | 🇵🇱 PL | 811 |
| 25 | 🇬🇹 GT | 769 |
| 26 | 🇲🇦 MA | 621 |
| 27 | 🇲🇪 ME | 536 |
| 28 | 🇳🇱 NL | 507 |
| 29 | 🇲🇴 MO | 461 |
| 30 | 🇧🇸 BS | 443 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1165 |
| 2 | Tokyo International Airport |  | JP | 930 |
| 3 | Denver International Airport |  | US | 835 |
| 4 | El Dorado International Airport |  | CO | 797 |
| 5 | Indira Gandhi International Airport |  | IN | 785 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 756 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 655 |
| 9 | Zurich Airport |  | CH | 586 |
| 10 | La Aurora Airport |  | GT | 572 |
| 11 | Frankfurt am Main International Airport |  | DE | 559 |
| 12 | Chicago O'Hare International Airport |  | US | 498 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 492 |
| 14 | Kuala Lumpur International Airport |  | MY | 482 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 478 |
| 16 | Macau International Airport |  | MO | 461 |
| 17 | Madrid Barajas International Airport |  | ES | 457 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 19 | Bengaluru International Airport |  | IN | 438 |
| 20 | Charlotte/Douglas International Airport |  | US | 421 |
| 21 | Congonhas Airport |  | BR | 417 |
| 22 | Malpensa International Airport |  | IT | 412 |
| 23 | Tenerife Norte Airport |  | ES | 408 |
| 24 | Ninoy Aquino International Airport |  | PH | 402 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 380 |
| 26 | Salt Lake City International Airport |  | US | 376 |
| 27 | Charles de Gaulle International Airport |  | FR | 375 |
| 28 | Daniel K Inouye International Airport |  | US | 371 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 344 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 341 |
| 33 | Vitoria/Foronda Airport |  | ES | 340 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 337 |
| 35 | Reno/Tahoe International Airport |  | US | 336 |
| 36 | Barcelona International Airport |  | ES | 333 |
| 37 | O. R. Tambo International Airport |  | ZA | 332 |
| 38 | Don Mueang International Airport |  | TH | 311 |
| 39 | Calgary International Airport |  | CA | 304 |
| 40 | Viracopos International Airport |  | BR | 296 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 235 | 1h 7m | 706 km | 2,861.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 192 | 14m | 114 km | 376.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 151 | 21m | 244 km | 635.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 149 | 28m | 304 km | 781.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 121 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 103 | 44m | 452 km | 802.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 86 | 20m | 250 km | 371.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 79 | 52m | 556 km | 757.3 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 71 | 1h 0m | 695 km | 851.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N63PF |  | Fort Lauderdale Executive Airport (KFXE) | Punta Gorda Airport (KPGD) | 2026-04-23 21:06 UTC | 2026-04-23 22:05 UTC | 58m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-04-23 21:53 UTC | 2026-04-23 22:05 UTC | 11m |
| N9968F |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-23 21:01 UTC | 2026-04-23 22:00 UTC | 59m |
| N8502V |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-23 21:12 UTC | 2026-04-23 21:59 UTC | 47m |
| OZN915 | OZN | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-04-23 21:44 UTC | 2026-04-23 21:57 UTC | 13m |
| DCM6432 | DCM | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Auburn University Regional Airport (KAUO) | 2026-04-23 21:17 UTC | 2026-04-23 21:56 UTC | 38m |
| N576SP |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-04-23 21:10 UTC | 2026-04-23 21:54 UTC | 44m |
| BYF31 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-04-23 21:48 UTC | 2026-04-23 21:54 UTC | 6m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-04-23 21:35 UTC | 2026-04-23 21:52 UTC | 16m |
| N5374K |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-23 20:56 UTC | 2026-04-23 21:50 UTC | 54m |
| CRK081 | CRK | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-04-23 08:31 UTC | 2026-04-23 21:45 UTC | 13h 14m |
| SAS45T | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Parnu Airport (EEPU) | 2026-04-23 21:04 UTC | 2026-04-23 21:44 UTC | 39m |
| JDW824 | JDW | RAF Brize Norton (EGVN) | RAF Abingdon (EGUD) | 2026-04-23 19:52 UTC | 2026-04-23 21:44 UTC | 1h 52m |
| N92983 |  | Anson County/Jeff Cloud Field (KAFP) | Polecat Aerodrome (SC67) | 2026-04-23 21:15 UTC | 2026-04-23 21:44 UTC | 28m |
| N875MH |  | Echo Bay Airport (K0L9) | Harry Reid International Airport (KLAS) | 2026-04-23 21:23 UTC | 2026-04-23 21:42 UTC | 18m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-23 17:20 UTC | 2026-04-23 21:42 UTC | 4h 21m |
| N511HS |  | Door County Cherryland Airport (KSUE) | Allen Parish Airport (KACP) | 2026-04-23 19:28 UTC | 2026-04-23 21:40 UTC | 2h 12m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-04-23 21:17 UTC | 2026-04-23 21:37 UTC | 19m |
| N781LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Brookneal/Campbell County Airport (K0V4) | 2026-04-23 20:52 UTC | 2026-04-23 21:34 UTC | 42m |
| TEK63 | TEK | Chester County G O Carlson Airport (KMQS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-23 20:24 UTC | 2026-04-23 21:33 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
