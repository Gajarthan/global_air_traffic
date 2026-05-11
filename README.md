# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_11:35:43_UTC-green)

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

**Latest saved flight:** 2026-05-11 11:35:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-11 11:35:43 UTC

- **77,772** saved flights
- **28,405** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,772** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **964,304.1 tonnes** estimated CO2 emissions
- **55,901,690 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3349 |
| 2 | SkyWest Airlines | 2886 |
| 3 | IndiGo | 1728 |
| 4 | EJA | 1431 |
| 5 | American Airlines | 1212 |
| 6 | Southwest Airlines | 1140 |
| 7 | Lufthansa | 1019 |
| 8 | ENY | 968 |
| 9 | Delta Air Lines | 840 |
| 10 | Vueling | 746 |
| 11 | AXM | 721 |
| 12 | LATAM Airlines | 710 |
| 13 | WIF | 670 |
| 14 | All Nippon Airways | 627 |
| 15 | AZU | 617 |
| 16 | Swiss International | 597 |
| 17 | QLK | 591 |
| 18 | LXJ | 569 |
| 19 | Alaska Airlines | 548 |
| 20 | easyJet | 521 |
| 21 | EJU | 507 |
| 22 | AEE | 504 |
| 23 | Cathay Pacific | 499 |
| 24 | VIV | 465 |
| 25 | Air France | 458 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 433 |
| 28 | CXK | 397 |
| 29 | MXY | 389 |
| 30 | AIQ | 387 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62752 |
| 2 | 🇪🇸 ES | 5580 |
| 3 | 🇮🇳 IN | 5426 |
| 4 | 🇦🇺 AU | 5035 |
| 5 | 🇩🇪 DE | 4412 |
| 6 | 🇧🇷 BR | 4324 |
| 7 | 🇮🇹 IT | 4299 |
| 8 | 🇯🇵 JP | 4030 |
| 9 | 🇨🇦 CA | 3854 |
| 10 | 🇬🇧 GB | 3355 |
| 11 | 🇫🇷 FR | 3088 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2378 |
| 14 | 🇬🇷 GR | 2302 |
| 15 | 🇳🇴 NO | 2133 |
| 16 | 🇨🇭 CH | 2105 |
| 17 | 🇲🇾 MY | 1808 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇹🇷 TR | 1402 |
| 20 | 🇳🇿 NZ | 1396 |
| 21 | 🇹🇭 TH | 1386 |
| 22 | 🇵🇱 PL | 1297 |
| 23 | 🇵🇭 PH | 1244 |
| 24 | 🇰🇷 KR | 1218 |
| 25 | 🇬🇹 GT | 1207 |
| 26 | 🇲🇦 MA | 920 |
| 27 | 🇲🇴 MO | 913 |
| 28 | 🇲🇪 ME | 833 |
| 29 | 🇳🇱 NL | 813 |
| 30 | 🇭🇷 HR | 678 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1715 |
| 2 | Tokyo International Airport |  | JP | 1354 |
| 3 | Denver International Airport |  | US | 1296 |
| 4 | Indira Gandhi International Airport |  | IN | 1147 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1129 |
| 6 | Frankfurt am Main International Airport |  | DE | 1023 |
| 7 | Harry Reid International Airport |  | US | 965 |
| 8 | Zurich Airport |  | CH | 923 |
| 9 | Macau International Airport |  | MO | 913 |
| 10 | La Aurora Airport |  | GT | 907 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 834 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 781 |
| 15 | Chicago O'Hare International Airport |  | US | 759 |
| 16 | Kuala Lumpur International Airport |  | MY | 726 |
| 17 | Madrid Barajas International Airport |  | ES | 721 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 687 |
| 19 | Malpensa International Airport |  | IT | 676 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 674 |
| 21 | Bengaluru International Airport |  | IN | 672 |
| 22 | Salt Lake City International Airport |  | US | 637 |
| 23 | Capua Airport |  | IT | 619 |
| 24 | Charlotte/Douglas International Airport |  | US | 614 |
| 25 | Charles de Gaulle International Airport |  | FR | 612 |
| 26 | Congonhas Airport |  | BR | 610 |
| 27 | Tenerife Norte Airport |  | ES | 582 |
| 28 | Ninoy Aquino International Airport |  | PH | 566 |
| 29 | Daniel K Inouye International Airport |  | US | 564 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 556 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 527 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 33 | Barcelona International Airport |  | ES | 526 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 508 |
| 35 | Don Mueang International Airport |  | TH | 494 |
| 36 | Vitoria/Foronda Airport |  | ES | 493 |
| 37 | Amsterdam Airport Schiphol |  | NL | 489 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 483 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 461 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 279 | 21m | 244 km | 1,174.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 197 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 185 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 173 | 1h 12m | 770 km | 2,298.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 118 | 27m | 215 km | 437.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 111 | 14m | 154 km | 294.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 110 | 59m | - | - |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 103 | 1h 42m | 1,423 km | 2,527.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 101 | 23m | 55 km | 96.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 97 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N540M |  | Chippewa Valley Regional Airport (KEAU) | Dane County Regional/Truax Field (KMSN) | 2026-05-11 11:09 UTC | 2026-05-11 11:35 UTC | 26m |
| BOX556 | BOX | Bengaluru International Airport (VOBL) | Macau International Airport (VMMC) | 2026-05-11 07:01 UTC | 2026-05-11 11:27 UTC | 4h 26m |
| ELY026 | ELY | Newark Liberty International Airport (KEWR) | LLSD (LLSD) | 2026-05-11 01:44 UTC | 2026-05-11 11:27 UTC | 9h 42m |
| AIC4174 | Air India | San Francisco International Airport (KSFO) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-10 18:57 UTC | 2026-05-11 11:22 UTC | 16h 25m |
| LTA941 | LTA | Indianapolis International Airport (KIND) | Shearer Airport (1IN1) | 2026-05-11 10:34 UTC | 2026-05-11 11:18 UTC | 43m |
| DAL9936 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 09:24 UTC | 2026-05-11 11:12 UTC | 1h 47m |
| AFL1639 | AFL | Izhevsk Airport (USII) | Sheremetyevo International Airport (UUEE) | 2026-05-11 03:48 UTC | 2026-05-11 11:06 UTC | 7h 17m |
| JIV9 | JIV | Gallivare Airport (ESNG) | Hallviken Airport (ESNA) | 2026-05-11 10:28 UTC | 2026-05-11 11:05 UTC | 37m |
| AWH97V | AWH | Hannover Airport (EDDV) | Brussels Airport (EBBR) | 2026-05-11 09:59 UTC | 2026-05-11 11:03 UTC | 1h 4m |
| RDF43 | RDF | LRPV (LRPV) | LRPV (LRPV) | 2026-05-11 10:59 UTC | 2026-05-11 10:59 UTC | 0m |
| WIF808 | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-05-11 10:48 UTC | 2026-05-11 10:59 UTC | 11m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-11 10:44 UTC | 2026-05-11 10:58 UTC | 13m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-05-11 10:10 UTC | 2026-05-11 10:57 UTC | 46m |
| ELY386 | ELY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Herzliya Airport (LLHZ) | 2026-05-11 08:24 UTC | 2026-05-11 10:51 UTC | 2h 27m |
| BARAO60 | BAR | Fazenda Barreiro Grande Airport (SDWN) | Fazenda Araras Airport (SIYF) | 2026-05-11 10:21 UTC | 2026-05-11 10:48 UTC | 27m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-05-11 10:37 UTC | 2026-05-11 10:48 UTC | 10m |
| RYR5SB | Ryanair | Berlin Brandenburg Airport (EDDB) | Otocac Airport (LDRO) | 2026-05-11 09:39 UTC | 2026-05-11 10:46 UTC | 1h 6m |
| DAL170 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 10:25 UTC | 2026-05-11 10:45 UTC | 19m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-11 07:53 UTC | 2026-05-11 10:45 UTC | 2h 51m |
| AMF1570 | AMF | Hoerners Corners Airport (MI10) | Delta County Airport (KESC) | 2026-05-11 09:49 UTC | 2026-05-11 10:41 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
