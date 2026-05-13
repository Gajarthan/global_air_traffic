# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_17:56:06_UTC-green)

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

**Latest saved flight:** 2026-05-13 17:56:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 17:56:06 UTC

- **80,491** saved flights
- **29,228** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **80,491** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **991,954.7 tonnes** estimated CO2 emissions
- **57,504,617 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3457 |
| 2 | SkyWest Airlines | 2985 |
| 3 | IndiGo | 1776 |
| 4 | EJA | 1496 |
| 5 | American Airlines | 1243 |
| 6 | Southwest Airlines | 1175 |
| 7 | Lufthansa | 1053 |
| 8 | ENY | 1001 |
| 9 | Delta Air Lines | 880 |
| 10 | Vueling | 769 |
| 11 | AXM | 734 |
| 12 | LATAM Airlines | 731 |
| 13 | WIF | 698 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 631 |
| 16 | Swiss International | 627 |
| 17 | QLK | 596 |
| 18 | LXJ | 586 |
| 19 | Alaska Airlines | 564 |
| 20 | easyJet | 535 |
| 21 | EJU | 519 |
| 22 | AEE | 516 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 478 |
| 25 | Air France | 476 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 438 |
| 28 | CXK | 421 |
| 29 | AIQ | 399 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 65409 |
| 2 | 🇪🇸 ES | 5734 |
| 3 | 🇮🇳 IN | 5552 |
| 4 | 🇦🇺 AU | 5145 |
| 5 | 🇩🇪 DE | 4552 |
| 6 | 🇮🇹 IT | 4461 |
| 7 | 🇧🇷 BR | 4442 |
| 8 | 🇯🇵 JP | 4123 |
| 9 | 🇨🇦 CA | 4003 |
| 10 | 🇬🇧 GB | 3455 |
| 11 | 🇫🇷 FR | 3206 |
| 12 | 🇨🇴 CO | 2718 |
| 13 | 🇲🇽 MX | 2425 |
| 14 | 🇬🇷 GR | 2364 |
| 15 | 🇳🇴 NO | 2249 |
| 16 | 🇨🇭 CH | 2180 |
| 17 | 🇲🇾 MY | 1840 |
| 18 | 🇿🇦 ZA | 1530 |
| 19 | 🇹🇷 TR | 1446 |
| 20 | 🇹🇭 TH | 1419 |
| 21 | 🇳🇿 NZ | 1414 |
| 22 | 🇵🇱 PL | 1345 |
| 23 | 🇵🇭 PH | 1268 |
| 24 | 🇰🇷 KR | 1235 |
| 25 | 🇬🇹 GT | 1229 |
| 26 | 🇲🇦 MA | 945 |
| 27 | 🇲🇴 MO | 928 |
| 28 | 🇲🇪 ME | 861 |
| 29 | 🇳🇱 NL | 834 |
| 30 | 🇭🇷 HR | 710 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1759 |
| 2 | Tokyo International Airport |  | JP | 1383 |
| 3 | Denver International Airport |  | US | 1345 |
| 4 | Indira Gandhi International Airport |  | IN | 1175 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1157 |
| 6 | Frankfurt am Main International Airport |  | DE | 1061 |
| 7 | Harry Reid International Airport |  | US | 993 |
| 8 | Zurich Airport |  | CH | 965 |
| 9 | Macau International Airport |  | MO | 928 |
| 10 | La Aurora Airport |  | GT | 927 |
| 11 | Guaymaral Airport |  | CO | 910 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 906 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 811 |
| 15 | Chicago O'Hare International Airport |  | US | 784 |
| 16 | Madrid Barajas International Airport |  | ES | 737 |
| 17 | Kuala Lumpur International Airport |  | MY | 736 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 707 |
| 19 | Malpensa International Airport |  | IT | 688 |
| 20 | Bengaluru International Airport |  | IN | 682 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 22 | Salt Lake City International Airport |  | US | 662 |
| 23 | Capua Airport |  | IT | 657 |
| 24 | Charlotte/Douglas International Airport |  | US | 631 |
| 25 | Charles de Gaulle International Airport |  | FR | 631 |
| 26 | Congonhas Airport |  | BR | 627 |
| 27 | Tenerife Norte Airport |  | ES | 598 |
| 28 | Daniel K Inouye International Airport |  | US | 582 |
| 29 | Ninoy Aquino International Airport |  | PH | 579 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 579 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 541 |
| 32 | Barcelona International Airport |  | ES | 540 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 534 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 525 |
| 35 | Vitoria/Foronda Airport |  | ES | 511 |
| 36 | Don Mueang International Airport |  | TH | 508 |
| 37 | Amsterdam Airport Schiphol |  | NL | 505 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 501 |
| 39 | O. R. Tambo International Airport |  | ZA | 486 |
| 40 | Calgary International Airport |  | CA | 473 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 379 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 289 | 21m | 244 km | 1,216.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 216 | 1h 27m | 910 km | 3,389.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 205 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 192 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 185 | 19m | 165 km | 526.2 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 182 | 1h 11m | 770 km | 2,417.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 118 | 20m | 147 km | 298.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 108 | 1h 2m | 695 km | 1,294.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 108 | 57m | 493 km | 918.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 102 | 18m | 144 km | 253.7 t |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL965 | United Airlines | Capua Airport (LIAU) | Newark Liberty International Airport (KEWR) | 2026-05-13 08:19 UTC | 2026-05-13 17:56 UTC | 9h 36m |
| TRF560 | TRF | 19TE (19TE) | Cleveland Municipal Airport (K6R3) | 2026-05-13 17:16 UTC | 2026-05-13 17:52 UTC | 35m |
| PGT1580 | PGT | Antalya International Airport (LTAI) | Nida Airport (EYND) | 2026-05-13 15:17 UTC | 2026-05-13 17:48 UTC | 2h 30m |
| MSR712 | EgyptAir | Rayak Air Base (OLRA) | HE32 (HE32) | 2026-05-13 17:01 UTC | 2026-05-13 17:47 UTC | 46m |
| NJE801A | NJE | Évora Airport (LPEV) | Zurich Airport (LSZH) | 2026-05-13 15:11 UTC | 2026-05-13 17:43 UTC | 2h 32m |
| N6539H |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-05-13 17:24 UTC | 2026-05-13 17:43 UTC | 18m |
| N7669G |  | Dupage Airport (KDPA) | IS63 (IS63) | 2026-05-13 17:22 UTC | 2026-05-13 17:42 UTC | 19m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-13 17:21 UTC | 2026-05-13 17:34 UTC | 13m |
| OKNGX | OKN | Warsaw Chopin Airport (EPWA) | Poznań-Ławica Airport (EPPO) | 2026-05-13 16:43 UTC | 2026-05-13 17:30 UTC | 46m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-13 16:28 UTC | 2026-05-13 17:29 UTC | 1h 1m |
| SEH051 | SEH | Samos Airport (LGSM) | Diagoras Airport (LGRP) | 2026-05-13 16:58 UTC | 2026-05-13 17:28 UTC | 30m |
| N353MV |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-05-13 16:57 UTC | 2026-05-13 17:19 UTC | 21m |
| NIT287 | NIT | Macon Downtown Airport (KMAC) | Macon Downtown Airport (KMAC) | 2026-05-13 16:54 UTC | 2026-05-13 17:18 UTC | 23m |
| ABP811 | ABP | M. R. Stefanik Airport (LZIB) | Raron Airport (LSTA) | 2026-05-13 16:03 UTC | 2026-05-13 17:15 UTC | 1h 12m |
| TOM5HT | TOM | Diagoras Airport (LGRP) | London Gatwick Airport (EGKK) | 2026-05-13 13:10 UTC | 2026-05-13 17:15 UTC | 4h 5m |
| GIZMO51 | GIZ | Vance Afb Airport (KEND) | Lariat Ranch Airport (OK42) | 2026-05-13 16:52 UTC | 2026-05-13 17:15 UTC | 22m |
| FIN317 | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-05-13 16:30 UTC | 2026-05-13 17:13 UTC | 43m |
| N3292U |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Ferros Ranch-Aero Airport (0MO0) | 2026-05-13 16:51 UTC | 2026-05-13 17:12 UTC | 21m |
| EJA567 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-05-13 16:39 UTC | 2026-05-13 17:11 UTC | 31m |
| N171AA |  | Portland-Hillsboro Airport (KHIO) | Nelson Ranch Airport (19OR) | 2026-05-13 16:54 UTC | 2026-05-13 17:11 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
