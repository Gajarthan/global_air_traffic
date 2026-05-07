# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_17:59:41_UTC-green)

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

**Latest saved flight:** 2026-05-07 17:59:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 17:59:41 UTC

- **72,266** saved flights
- **26,829** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,266** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **890,210.9 tonnes** estimated CO2 emissions
- **51,606,427 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3114 |
| 2 | SkyWest Airlines | 2690 |
| 3 | IndiGo | 1637 |
| 4 | EJA | 1328 |
| 5 | American Airlines | 1133 |
| 6 | Southwest Airlines | 1051 |
| 7 | Lufthansa | 926 |
| 8 | ENY | 909 |
| 9 | Vueling | 707 |
| 10 | AXM | 688 |
| 11 | LATAM Airlines | 671 |
| 12 | WIF | 618 |
| 13 | Delta Air Lines | 604 |
| 14 | All Nippon Airways | 599 |
| 15 | AZU | 581 |
| 16 | Swiss International | 555 |
| 17 | QLK | 554 |
| 18 | LXJ | 525 |
| 19 | Alaska Airlines | 508 |
| 20 | easyJet | 479 |
| 21 | EJU | 466 |
| 22 | AEE | 465 |
| 23 | Cathay Pacific | 448 |
| 24 | VIV | 447 |
| 25 | Japan Airlines | 426 |
| 26 | Air France | 422 |
| 27 | AXB | 401 |
| 28 | CXK | 362 |
| 29 | AIQ | 359 |
| 30 | GLO | 346 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57818 |
| 2 | 🇪🇸 ES | 5238 |
| 3 | 🇮🇳 IN | 5137 |
| 4 | 🇦🇺 AU | 4799 |
| 5 | 🇧🇷 BR | 4047 |
| 6 | 🇩🇪 DE | 4015 |
| 7 | 🇮🇹 IT | 3961 |
| 8 | 🇯🇵 JP | 3829 |
| 9 | 🇨🇦 CA | 3600 |
| 10 | 🇬🇧 GB | 3110 |
| 11 | 🇫🇷 FR | 2847 |
| 12 | 🇨🇴 CO | 2677 |
| 13 | 🇲🇽 MX | 2276 |
| 14 | 🇬🇷 GR | 2145 |
| 15 | 🇳🇴 NO | 2004 |
| 16 | 🇨🇭 CH | 1967 |
| 17 | 🇲🇾 MY | 1715 |
| 18 | 🇿🇦 ZA | 1426 |
| 19 | 🇳🇿 NZ | 1320 |
| 20 | 🇹🇷 TR | 1300 |
| 21 | 🇹🇭 TH | 1294 |
| 22 | 🇵🇱 PL | 1204 |
| 23 | 🇵🇭 PH | 1174 |
| 24 | 🇬🇹 GT | 1146 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 859 |
| 27 | 🇲🇴 MO | 842 |
| 28 | 🇲🇪 ME | 771 |
| 29 | 🇳🇱 NL | 750 |
| 30 | 🇧🇸 BS | 608 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1612 |
| 2 | Tokyo International Airport |  | JP | 1287 |
| 3 | Denver International Airport |  | US | 1205 |
| 4 | Indira Gandhi International Airport |  | IN | 1083 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1049 |
| 6 | Frankfurt am Main International Airport |  | DE | 920 |
| 7 | Harry Reid International Airport |  | US | 902 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 872 |
| 10 | Zurich Airport |  | CH | 857 |
| 11 | La Aurora Airport |  | GT | 853 |
| 12 | Macau International Airport |  | MO | 842 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 727 |
| 14 | Chicago O'Hare International Airport |  | US | 703 |
| 15 | Kuala Lumpur International Airport |  | MY | 689 |
| 16 | Madrid Barajas International Airport |  | ES | 680 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 643 |
| 18 | Malpensa International Airport |  | IT | 629 |
| 19 | Bengaluru International Airport |  | IN | 626 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 21 | Salt Lake City International Airport |  | US | 587 |
| 22 | Capua Airport |  | IT | 572 |
| 23 | Congonhas Airport |  | BR | 572 |
| 24 | Charlotte/Douglas International Airport |  | US | 569 |
| 25 | Charles de Gaulle International Airport |  | FR | 565 |
| 26 | Tenerife Norte Airport |  | ES | 549 |
| 27 | Ninoy Aquino International Airport |  | PH | 534 |
| 28 | Daniel K Inouye International Airport |  | US | 532 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 520 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 500 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 492 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 483 |
| 34 | Vitoria/Foronda Airport |  | ES | 475 |
| 35 | Don Mueang International Airport |  | TH | 454 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 454 |
| 37 | O. R. Tambo International Airport |  | ZA | 447 |
| 38 | Amsterdam Airport Schiphol |  | NL | 446 |
| 39 | Calgary International Airport |  | CA | 434 |
| 40 | Reno/Tahoe International Airport |  | US | 425 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 362 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 255 | 21m | 244 km | 1,073.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 211 | 24m | 225 km | 818.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 105 | 14m | 154 km | 278.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 93 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N767CG |  | Council Bluffs Municipal Airport (KCBF) | Volkens Field (97IA) | 2026-05-07 17:38 UTC | 2026-05-07 17:59 UTC | 21m |
| UAV13 | UAV | Krey Field (0CL1) | Sun Hill Ranch Airport (CA70) | 2026-05-07 17:33 UTC | 2026-05-07 17:58 UTC | 25m |
| N964SB |  | Santa Ynez/Kunkle Field (KIZA) | San Luis Obispo County Regional Airport (KSBP) | 2026-05-07 17:31 UTC | 2026-05-07 17:57 UTC | 25m |
| N600SV |  | Pullman/Moscow Regional Airport (KPUW) | Pullman/Moscow Regional Airport (KPUW) | 2026-05-07 17:40 UTC | 2026-05-07 17:51 UTC | 10m |
| N832KX |  | Portland-Hillsboro Airport (KHIO) | Newport Municipal Airport (KONP) | 2026-05-07 16:38 UTC | 2026-05-07 17:49 UTC | 1h 10m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-07 17:36 UTC | 2026-05-07 17:46 UTC | 10m |
| N4126U |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Cuylers Airport (02PR) | 2026-05-07 17:21 UTC | 2026-05-07 17:46 UTC | 24m |
| NWX382 | NWX | Aero Valley Airport (K52F) | Jim Sears Airport (3TA7) | 2026-05-07 16:57 UTC | 2026-05-07 17:41 UTC | 44m |
| N25497 |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-05-07 17:16 UTC | 2026-05-07 17:40 UTC | 24m |
| N892CN |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-05-07 17:00 UTC | 2026-05-07 17:37 UTC | 37m |
| N666TR |  | Westchester County Airport (KHPN) | Stephen A Bean Municipal Airport (K8B0) | 2026-05-07 17:04 UTC | 2026-05-07 17:34 UTC | 30m |
| N369TA |  | Fairview Airport (3MD4) | Fairview Airport (3MD4) | 2026-05-07 17:00 UTC | 2026-05-07 17:33 UTC | 33m |
| N227MM |  | Naples Municipal Airport (KAPF) | Marco Island Executive Airport (KMKY) | 2026-05-07 16:33 UTC | 2026-05-07 17:33 UTC | 59m |
| EASY04 | EAS | Beaufort Mcas (Merritt Field) Airport (KNBC) | Macdill Afb Airport (KMCF) | 2026-05-07 16:11 UTC | 2026-05-07 17:31 UTC | 1h 20m |
| SNAKE1 | SNA | Ksa Orchards Airport (OK11) | Ksa Orchards Airport (OK11) | 2026-05-07 17:07 UTC | 2026-05-07 17:29 UTC | 21m |
| PAT960 | PAT | Robert Gray Army Air Field (KGRK) | TX11 (TX11) | 2026-05-07 17:01 UTC | 2026-05-07 17:26 UTC | 24m |
| N988LE |  | Grand Junction Regional Airport (KGJT) | Telluride Regional Airport (KTEX) | 2026-05-07 16:49 UTC | 2026-05-07 17:22 UTC | 33m |
| N16304 |  | Middletown Regional/Hook Field (KMWO) | Ohio State University Airport (KOSU) | 2026-05-07 16:42 UTC | 2026-05-07 17:22 UTC | 39m |
| N474SM |  | Mc Clellan-Palomar Airport (KCRQ) | Blackinton Airport (2CA4) | 2026-05-07 16:43 UTC | 2026-05-07 17:20 UTC | 36m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-07 15:26 UTC | 2026-05-07 17:20 UTC | 1h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
