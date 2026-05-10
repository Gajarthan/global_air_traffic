# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_21:19:06_UTC-green)

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

**Latest saved flight:** 2026-05-10 21:19:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 21:19:06 UTC

- **77,657** saved flights
- **28,376** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,657** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **962,690.0 tonnes** estimated CO2 emissions
- **55,808,114 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3337 |
| 2 | SkyWest Airlines | 2886 |
| 3 | IndiGo | 1724 |
| 4 | EJA | 1431 |
| 5 | American Airlines | 1212 |
| 6 | Southwest Airlines | 1140 |
| 7 | Lufthansa | 1015 |
| 8 | ENY | 968 |
| 9 | Delta Air Lines | 836 |
| 10 | Vueling | 743 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 710 |
| 13 | WIF | 667 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 617 |
| 16 | QLK | 591 |
| 17 | Swiss International | 591 |
| 18 | LXJ | 569 |
| 19 | Alaska Airlines | 548 |
| 20 | easyJet | 521 |
| 21 | EJU | 506 |
| 22 | AEE | 504 |
| 23 | Cathay Pacific | 499 |
| 24 | VIV | 465 |
| 25 | Air France | 457 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 431 |
| 28 | CXK | 397 |
| 29 | MXY | 389 |
| 30 | AIQ | 386 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62726 |
| 2 | 🇪🇸 ES | 5568 |
| 3 | 🇮🇳 IN | 5409 |
| 4 | 🇦🇺 AU | 5032 |
| 5 | 🇩🇪 DE | 4397 |
| 6 | 🇧🇷 BR | 4321 |
| 7 | 🇮🇹 IT | 4287 |
| 8 | 🇯🇵 JP | 4019 |
| 9 | 🇨🇦 CA | 3852 |
| 10 | 🇬🇧 GB | 3346 |
| 11 | 🇫🇷 FR | 3082 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2378 |
| 14 | 🇬🇷 GR | 2298 |
| 15 | 🇳🇴 NO | 2128 |
| 16 | 🇨🇭 CH | 2096 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇹🇷 TR | 1395 |
| 20 | 🇳🇿 NZ | 1395 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1294 |
| 23 | 🇵🇭 PH | 1242 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1207 |
| 26 | 🇲🇦 MA | 916 |
| 27 | 🇲🇴 MO | 912 |
| 28 | 🇲🇪 ME | 827 |
| 29 | 🇳🇱 NL | 810 |
| 30 | 🇭🇷 HR | 675 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1715 |
| 2 | Tokyo International Airport |  | JP | 1350 |
| 3 | Denver International Airport |  | US | 1296 |
| 4 | Indira Gandhi International Airport |  | IN | 1144 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1128 |
| 6 | Frankfurt am Main International Airport |  | DE | 1019 |
| 7 | Harry Reid International Airport |  | US | 964 |
| 8 | Zurich Airport |  | CH | 915 |
| 9 | Macau International Airport |  | MO | 912 |
| 10 | La Aurora Airport |  | GT | 907 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 826 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 781 |
| 15 | Chicago O'Hare International Airport |  | US | 759 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 721 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 687 |
| 19 | Malpensa International Airport |  | IT | 676 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 673 |
| 21 | Bengaluru International Airport |  | IN | 670 |
| 22 | Salt Lake City International Airport |  | US | 637 |
| 23 | Capua Airport |  | IT | 618 |
| 24 | Charlotte/Douglas International Airport |  | US | 614 |
| 25 | Charles de Gaulle International Airport |  | FR | 611 |
| 26 | Congonhas Airport |  | BR | 610 |
| 27 | Tenerife Norte Airport |  | ES | 581 |
| 28 | Ninoy Aquino International Airport |  | PH | 565 |
| 29 | Daniel K Inouye International Airport |  | US | 563 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 555 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 527 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 33 | Barcelona International Airport |  | ES | 525 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 506 |
| 35 | Vitoria/Foronda Airport |  | ES | 493 |
| 36 | Don Mueang International Airport |  | TH | 490 |
| 37 | Amsterdam Airport Schiphol |  | NL | 488 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 483 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 461 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 278 | 21m | 244 km | 1,170.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 197 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 184 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 118 | 27m | 215 km | 437.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 106 | 1h 0m | - | - |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 103 | 1h 42m | 1,423 km | 2,527.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 101 | 23m | 55 km | 96.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 96 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N474LE |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-05-10 20:24 UTC | 2026-05-10 21:19 UTC | 54m |
| N1873H |  | Lewis University Airport (KLOT) | South Haven Area Regional Airport (KLWA) | 2026-05-10 20:20 UTC | 2026-05-10 21:14 UTC | 54m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-10 21:00 UTC | 2026-05-10 21:13 UTC | 12m |
| DAL2819 | Delta Air Lines | Charlotte/Douglas International Airport (KCLT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 18:51 UTC | 2026-05-10 21:07 UTC | 2h 16m |
| N402AA |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-10 20:46 UTC | 2026-05-10 21:06 UTC | 19m |
| FIRE2 | FIR | Van Nuys Airport (KVNY) | Bob Hope Airport (KBUR) | 2026-05-10 20:45 UTC | 2026-05-10 21:04 UTC | 18m |
| ASI541 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-05-10 19:50 UTC | 2026-05-10 20:55 UTC | 1h 4m |
| N874BU |  | 6FD7 (6FD7) | Peter O Knight Airport (KTPF) | 2026-05-10 20:35 UTC | 2026-05-10 20:50 UTC | 14m |
| EJA671 | EJA | Westchester County Airport (KHPN) | Lehigh Valley International Airport (KABE) | 2026-05-10 20:21 UTC | 2026-05-10 20:50 UTC | 28m |
| N956RW |  | Georgetown Executive Airport (KGTU) | Gillespie County Airport (KT82) | 2026-05-10 20:02 UTC | 2026-05-10 20:49 UTC | 46m |
| CPA064 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-10 09:38 UTC | 2026-05-10 20:47 UTC | 11h 9m |
| OXF6250 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-05-10 19:24 UTC | 2026-05-10 20:47 UTC | 1h 22m |
| N104QT |  | Los Angeles International Airport (KLAX) | Westwater Airport (UT42) | 2026-05-10 19:28 UTC | 2026-05-10 20:47 UTC | 1h 18m |
| N1382F |  | Washington County Airport (KAFJ) | Washington County Airport (KAFJ) | 2026-05-10 19:15 UTC | 2026-05-10 20:45 UTC | 1h 29m |
| N497P |  | Purdue University Airport (KLAF) | Songer Airport (IN55) | 2026-05-10 20:32 UTC | 2026-05-10 20:44 UTC | 12m |
| AAL2381 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 18:27 UTC | 2026-05-10 20:43 UTC | 2h 15m |
| DAL2113 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 20:23 UTC | 2026-05-10 20:39 UTC | 15m |
| N81EB |  | Columbia Metro Airport (KCAE) | Walker County/Bevill Field (KJFX) | 2026-05-10 19:27 UTC | 2026-05-10 20:35 UTC | 1h 8m |
| N18MG |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-05-10 19:43 UTC | 2026-05-10 20:35 UTC | 51m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-10 20:09 UTC | 2026-05-10 20:34 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
