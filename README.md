# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_17:00:55_UTC-green)

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

**Latest saved flight:** 2026-05-06 17:00:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 17:00:55 UTC

- **70,795** saved flights
- **26,349** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,795** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **873,044.2 tonnes** estimated CO2 emissions
- **50,611,258 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3050 |
| 2 | SkyWest Airlines | 2630 |
| 3 | IndiGo | 1620 |
| 4 | EJA | 1289 |
| 5 | American Airlines | 1102 |
| 6 | Southwest Airlines | 1022 |
| 7 | Lufthansa | 913 |
| 8 | ENY | 881 |
| 9 | Vueling | 698 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 660 |
| 12 | WIF | 605 |
| 13 | Delta Air Lines | 595 |
| 14 | All Nippon Airways | 590 |
| 15 | AZU | 574 |
| 16 | QLK | 547 |
| 17 | Swiss International | 546 |
| 18 | LXJ | 512 |
| 19 | Alaska Airlines | 496 |
| 20 | easyJet | 474 |
| 21 | AEE | 459 |
| 22 | EJU | 458 |
| 23 | VIV | 444 |
| 24 | Cathay Pacific | 434 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 418 |
| 27 | AXB | 394 |
| 28 | AIQ | 358 |
| 29 | CXK | 351 |
| 30 | GLO | 343 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 56258 |
| 2 | 🇪🇸 ES | 5173 |
| 3 | 🇮🇳 IN | 5085 |
| 4 | 🇦🇺 AU | 4706 |
| 5 | 🇧🇷 BR | 3987 |
| 6 | 🇩🇪 DE | 3953 |
| 7 | 🇮🇹 IT | 3891 |
| 8 | 🇯🇵 JP | 3775 |
| 9 | 🇨🇦 CA | 3494 |
| 10 | 🇬🇧 GB | 3068 |
| 11 | 🇫🇷 FR | 2804 |
| 12 | 🇨🇴 CO | 2663 |
| 13 | 🇲🇽 MX | 2241 |
| 14 | 🇬🇷 GR | 2119 |
| 15 | 🇳🇴 NO | 1945 |
| 16 | 🇨🇭 CH | 1941 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1277 |
| 22 | 🇵🇱 PL | 1175 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1135 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 848 |
| 27 | 🇲🇴 MO | 823 |
| 28 | 🇲🇪 ME | 759 |
| 29 | 🇳🇱 NL | 740 |
| 30 | 🇮🇩 ID | 596 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1576 |
| 2 | Tokyo International Airport |  | JP | 1274 |
| 3 | Denver International Airport |  | US | 1172 |
| 4 | Indira Gandhi International Airport |  | IN | 1067 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1036 |
| 6 | Frankfurt am Main International Airport |  | DE | 911 |
| 7 | Harry Reid International Airport |  | US | 884 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 858 |
| 10 | La Aurora Airport |  | GT | 845 |
| 11 | Zurich Airport |  | CH | 842 |
| 12 | Macau International Airport |  | MO | 823 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 710 |
| 14 | Chicago O'Hare International Airport |  | US | 680 |
| 15 | Kuala Lumpur International Airport |  | MY | 679 |
| 16 | Madrid Barajas International Airport |  | ES | 675 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 630 |
| 18 | Malpensa International Airport |  | IT | 618 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 21 | Salt Lake City International Airport |  | US | 571 |
| 22 | Congonhas Airport |  | BR | 567 |
| 23 | Capua Airport |  | IT | 559 |
| 24 | Charlotte/Douglas International Airport |  | US | 557 |
| 25 | Charles de Gaulle International Airport |  | FR | 557 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 520 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 499 |
| 31 | Barcelona International Airport |  | ES | 493 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 481 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 472 |
| 34 | Vitoria/Foronda Airport |  | ES | 469 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 446 |
| 37 | O. R. Tambo International Airport |  | ZA | 442 |
| 38 | Amsterdam Airport Schiphol |  | NL | 441 |
| 39 | Reno/Tahoe International Airport |  | US | 419 |
| 40 | Calgary International Airport |  | CA | 419 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 355 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 246 | 21m | 244 km | 1,035.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 178 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 159 | 26m | 275 km | 753.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9924W |  | Cecil Airport (KVQQ) | Reynolds Airpark (FL60) | 2026-05-06 16:42 UTC | 2026-05-06 17:00 UTC | 17m |
| N116TX |  | Martha's Vineyard Airport (KMVY) | Lebanon Municipal Airport (KLEB) | 2026-05-06 15:55 UTC | 2026-05-06 16:50 UTC | 55m |
| MS1 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-05-06 16:08 UTC | 2026-05-06 16:50 UTC | 42m |
| N9347T |  | Lewis University Airport (KLOT) | Neiner Airport (19LL) | 2026-05-06 16:17 UTC | 2026-05-06 16:49 UTC | 32m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-06 16:33 UTC | 2026-05-06 16:47 UTC | 13m |
| N9900M |  | Seattle Paine Field International Airport (KPAE) | Renton Municipal Airport (KRNT) | 2026-05-06 16:28 UTC | 2026-05-06 16:42 UTC | 14m |
| N229LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Los Alamitos Army Air Field (KSLI) | 2026-05-06 16:30 UTC | 2026-05-06 16:42 UTC | 11m |
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-05-06 15:38 UTC | 2026-05-06 16:32 UTC | 54m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-05-06 15:59 UTC | 2026-05-06 16:30 UTC | 30m |
| AXEL90 | AXE | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Dayton Valley Airpark (KA34) | 2026-05-06 14:31 UTC | 2026-05-06 16:29 UTC | 1h 57m |
| CXK450 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Jekyll Island Airport (K09J) | 2026-05-06 15:35 UTC | 2026-05-06 16:28 UTC | 53m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-06 15:02 UTC | 2026-05-06 16:28 UTC | 1h 25m |
| N4397Q |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-05-06 15:42 UTC | 2026-05-06 16:24 UTC | 42m |
| N246SF |  | IS63 (IS63) | Colonial Acres Airport (4LL8) | 2026-05-06 16:09 UTC | 2026-05-06 16:22 UTC | 13m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-06 16:09 UTC | 2026-05-06 16:22 UTC | 12m |
| N76091 |  | Riverside Airport (KRAL) | Corona Municipal Airport (KAJO) | 2026-05-06 15:55 UTC | 2026-05-06 16:22 UTC | 27m |
| NASA859 | NAS | 91CL (91CL) | Boron Airstrip (57CL) | 2026-05-06 16:11 UTC | 2026-05-06 16:21 UTC | 9m |
| AUR209 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-05-06 16:04 UTC | 2026-05-06 16:19 UTC | 14m |
| N856MH |  | Temple Bar Airport (KU30) | Harry Reid International Airport (KLAS) | 2026-05-06 15:57 UTC | 2026-05-06 16:18 UTC | 20m |
| RN017 |  | Mobile International Airport (KBFM) | Atmore Municipal Airport (K0R1) | 2026-05-06 16:04 UTC | 2026-05-06 16:18 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
