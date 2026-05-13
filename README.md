# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_21:30:57_UTC-green)

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

**Latest saved flight:** 2026-05-13 21:30:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 21:30:57 UTC

- **80,867** saved flights
- **29,355** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **80,867** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **996,639.2 tonnes** estimated CO2 emissions
- **57,776,184 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3471 |
| 2 | SkyWest Airlines | 3006 |
| 3 | IndiGo | 1777 |
| 4 | EJA | 1514 |
| 5 | American Airlines | 1250 |
| 6 | Southwest Airlines | 1179 |
| 7 | Lufthansa | 1055 |
| 8 | ENY | 1010 |
| 9 | Delta Air Lines | 888 |
| 10 | Vueling | 771 |
| 11 | LATAM Airlines | 738 |
| 12 | AXM | 734 |
| 13 | WIF | 702 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 635 |
| 16 | Swiss International | 630 |
| 17 | QLK | 596 |
| 18 | LXJ | 589 |
| 19 | Alaska Airlines | 568 |
| 20 | easyJet | 537 |
| 21 | EJU | 520 |
| 22 | AEE | 517 |
| 23 | Cathay Pacific | 507 |
| 24 | VIV | 481 |
| 25 | Air France | 476 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 439 |
| 28 | CXK | 423 |
| 29 | United Airlines | 400 |
| 30 | AIQ | 399 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 65864 |
| 2 | 🇪🇸 ES | 5755 |
| 3 | 🇮🇳 IN | 5556 |
| 4 | 🇦🇺 AU | 5151 |
| 5 | 🇩🇪 DE | 4566 |
| 6 | 🇮🇹 IT | 4481 |
| 7 | 🇧🇷 BR | 4470 |
| 8 | 🇯🇵 JP | 4123 |
| 9 | 🇨🇦 CA | 4025 |
| 10 | 🇬🇧 GB | 3468 |
| 11 | 🇫🇷 FR | 3215 |
| 12 | 🇨🇴 CO | 2720 |
| 13 | 🇲🇽 MX | 2445 |
| 14 | 🇬🇷 GR | 2368 |
| 15 | 🇳🇴 NO | 2259 |
| 16 | 🇨🇭 CH | 2183 |
| 17 | 🇲🇾 MY | 1840 |
| 18 | 🇿🇦 ZA | 1530 |
| 19 | 🇹🇷 TR | 1446 |
| 20 | 🇹🇭 TH | 1419 |
| 21 | 🇳🇿 NZ | 1416 |
| 22 | 🇵🇱 PL | 1349 |
| 23 | 🇵🇭 PH | 1268 |
| 24 | 🇰🇷 KR | 1235 |
| 25 | 🇬🇹 GT | 1234 |
| 26 | 🇲🇦 MA | 947 |
| 27 | 🇲🇴 MO | 931 |
| 28 | 🇲🇪 ME | 865 |
| 29 | 🇳🇱 NL | 836 |
| 30 | 🇭🇷 HR | 716 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1772 |
| 2 | Tokyo International Airport |  | JP | 1383 |
| 3 | Denver International Airport |  | US | 1358 |
| 4 | Indira Gandhi International Airport |  | IN | 1177 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1159 |
| 6 | Frankfurt am Main International Airport |  | DE | 1065 |
| 7 | Harry Reid International Airport |  | US | 1000 |
| 8 | Zurich Airport |  | CH | 967 |
| 9 | La Aurora Airport |  | GT | 932 |
| 10 | Macau International Airport |  | MO | 931 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 914 |
| 12 | Guaymaral Airport |  | CO | 912 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 818 |
| 15 | Chicago O'Hare International Airport |  | US | 788 |
| 16 | Madrid Barajas International Airport |  | ES | 741 |
| 17 | Kuala Lumpur International Airport |  | MY | 736 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 708 |
| 19 | Malpensa International Airport |  | IT | 689 |
| 20 | Bengaluru International Airport |  | IN | 683 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 22 | Salt Lake City International Airport |  | US | 669 |
| 23 | Capua Airport |  | IT | 660 |
| 24 | Charles de Gaulle International Airport |  | FR | 633 |
| 25 | Charlotte/Douglas International Airport |  | US | 632 |
| 26 | Congonhas Airport |  | BR | 630 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Daniel K Inouye International Airport |  | US | 585 |
| 29 | Ninoy Aquino International Airport |  | PH | 579 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 579 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 543 |
| 32 | Barcelona International Airport |  | ES | 541 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 539 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 526 |
| 35 | Vitoria/Foronda Airport |  | ES | 512 |
| 36 | Don Mueang International Airport |  | TH | 508 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 508 |
| 38 | Amsterdam Airport Schiphol |  | NL | 505 |
| 39 | O. R. Tambo International Airport |  | ZA | 486 |
| 40 | Calgary International Airport |  | CA | 478 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 290 | 21m | 244 km | 1,221.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 216 | 1h 27m | 910 km | 3,389.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 206 | 9m | - | - |
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
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 108 | 57m | 493 km | 918.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 101 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-13 17:23 UTC | 2026-05-13 21:30 UTC | 4h 7m |
| N421JJ |  | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-13 20:16 UTC | 2026-05-13 21:19 UTC | 1h 2m |
| N273TM |  | Des Moines International Airport (KDSM) | Joe Foss Field (KFSD) | 2026-05-13 20:35 UTC | 2026-05-13 21:18 UTC | 42m |
| REH7 | REH | Yuba County Airport (KMYV) | Watts-Woodland Airport (KO41) | 2026-05-13 20:59 UTC | 2026-05-13 21:17 UTC | 17m |
| EPI256 | EPI | Whitehouse Nolf Airport (KNEN) | Whitehouse Nolf Airport (KNEN) | 2026-05-13 21:01 UTC | 2026-05-13 21:11 UTC | 10m |
| ASP812 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Toronto Pearson International Airport (CYYZ) | 2026-05-13 20:13 UTC | 2026-05-13 21:11 UTC | 57m |
| CARD11 | CAR | Tlc Airport (OK71) | Trust Landing Airport (OK72) | 2026-05-13 20:46 UTC | 2026-05-13 21:07 UTC | 21m |
| CARGO21 | CAR | Hidden Springs Airpark (36AL) | Dothan Regional Airport (KDHN) | 2026-05-13 20:57 UTC | 2026-05-13 21:02 UTC | 5m |
| N7912X |  | Atlanta Regional Falcon Field (KFFC) | Atlanta Regional Falcon Field (KFFC) | 2026-05-13 20:56 UTC | 2026-05-13 21:02 UTC | 5m |
| N603DW |  | Iowa City Municipal Airport (KIOW) | James G Whiting Memorial Field (KMEY) | 2026-05-13 20:19 UTC | 2026-05-13 21:02 UTC | 42m |
| BB158 |  | Brewton Municipal Airport (K12J) | Brewton Municipal Airport (K12J) | 2026-05-13 20:36 UTC | 2026-05-13 21:01 UTC | 25m |
| EJA323 | EJA | Washington Dulles International Airport (KIAD) | Lehigh Valley International Airport (KABE) | 2026-05-13 20:20 UTC | 2026-05-13 20:59 UTC | 39m |
| CSS102 | CSS | Frankfurt am Main International Airport (EDDF) | Sharypovo Airport (UNKO) | 2026-05-13 15:15 UTC | 2026-05-13 20:59 UTC | 5h 43m |
| SCU35 | SCU | Sahoma Lake Airport (03OK) | Flying G Ranch Airport (3OK8) | 2026-05-13 20:35 UTC | 2026-05-13 20:57 UTC | 21m |
| N168DC |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-05-13 20:01 UTC | 2026-05-13 20:55 UTC | 54m |
| GAOT06 | GAO | Randolph Afb Airport (KRND) | Boening Brothers Airport (7TE9) | 2026-05-13 19:59 UTC | 2026-05-13 20:54 UTC | 55m |
| N856LF |  | Felts Field (KSFF) | White Pine Flats Ranch Llc Airport (ID94) | 2026-05-13 20:32 UTC | 2026-05-13 20:52 UTC | 19m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-05-13 20:22 UTC | 2026-05-13 20:51 UTC | 29m |
| JR1 |  | NC20 (NC20) | Ocracoke Island Airport (KW95) | 2026-05-13 19:28 UTC | 2026-05-13 20:49 UTC | 1h 21m |
| PAT087 | PAT | Wheeler Army Air Field (PHHI) | Waimea-Kohala Airport (PHMU) | 2026-05-13 19:46 UTC | 2026-05-13 20:47 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
