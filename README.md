# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_19:23:08_UTC-green)

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

**Latest saved flight:** 2026-04-24 19:23:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 19:23:08 UTC

- **52,262** saved flights
- **20,893** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,262** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **623,725.6 tonnes** estimated CO2 emissions
- **36,158,005 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2199 |
| 2 | SkyWest Airlines | 1973 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 912 |
| 5 | American Airlines | 838 |
| 6 | Southwest Airlines | 740 |
| 7 | ENY | 661 |
| 8 | Lufthansa | 611 |
| 9 | Vueling | 524 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 499 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 444 |
| 14 | WIF | 436 |
| 15 | Delta Air Lines | 431 |
| 16 | QLK | 412 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 389 |
| 19 | AEE | 354 |
| 20 | Alaska Airlines | 343 |
| 21 | EJU | 332 |
| 22 | easyJet | 330 |
| 23 | VIV | 330 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 272 |
| 28 | JetBlue | 269 |
| 29 | United Airlines | 266 |
| 30 | GLO | 265 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 41557 |
| 2 | 🇪🇸 ES | 3778 |
| 3 | 🇮🇳 IN | 3770 |
| 4 | 🇦🇺 AU | 3570 |
| 5 | 🇧🇷 BR | 3013 |
| 6 | 🇮🇹 IT | 2811 |
| 7 | 🇯🇵 JP | 2809 |
| 8 | 🇩🇪 DE | 2795 |
| 9 | 🇨🇦 CA | 2602 |
| 10 | 🇨🇴 CO | 2406 |
| 11 | 🇬🇧 GB | 2172 |
| 12 | 🇫🇷 FR | 2033 |
| 13 | 🇲🇽 MX | 1608 |
| 14 | 🇬🇷 GR | 1584 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1415 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1085 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 940 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 836 |
| 25 | 🇬🇹 GT | 803 |
| 26 | 🇲🇦 MA | 642 |
| 27 | 🇲🇪 ME | 558 |
| 28 | 🇳🇱 NL | 531 |
| 29 | 🇲🇴 MO | 497 |
| 30 | 🇧🇸 BS | 456 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1194 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 863 |
| 4 | El Dorado International Airport |  | CO | 819 |
| 5 | Indira Gandhi International Airport |  | IN | 805 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 785 |
| 7 | Guaymaral Airport |  | CO | 713 |
| 8 | Harry Reid International Airport |  | US | 673 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 600 |
| 11 | Frankfurt am Main International Airport |  | DE | 598 |
| 12 | Chicago O'Hare International Airport |  | US | 518 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 507 |
| 14 | Macau International Airport |  | MO | 497 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 496 |
| 16 | Kuala Lumpur International Airport |  | MY | 491 |
| 17 | Madrid Barajas International Airport |  | ES | 480 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Malpensa International Airport |  | IT | 436 |
| 21 | Congonhas Airport |  | BR | 436 |
| 22 | Charlotte/Douglas International Airport |  | US | 431 |
| 23 | Tenerife Norte Airport |  | ES | 415 |
| 24 | Ninoy Aquino International Airport |  | PH | 414 |
| 25 | Charles de Gaulle International Airport |  | FR | 397 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 389 |
| 27 | Salt Lake City International Airport |  | US | 384 |
| 28 | Daniel K Inouye International Airport |  | US | 379 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 364 |
| 31 | Vitoria/Foronda Airport |  | ES | 357 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 353 |
| 33 | Barcelona International Airport |  | ES | 350 |
| 34 | Reno/Tahoe International Airport |  | US | 348 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 347 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 345 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 313 |
| 40 | Viracopos International Airport |  | BR | 307 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 289 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 157 | 21m | 244 km | 661.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 130 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 122 | 26m | 275 km | 578.1 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 95 | 20m | 99 km | 162.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 81 | 52m | 556 km | 776.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 80 | 27m | 152 km | 209.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 74 | 1h 0m | 695 km | 887.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 53m | 1,304 km | 1,529.8 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 28 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 67 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU466 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-04-24 18:42 UTC | 2026-04-24 19:23 UTC | 40m |
| N15U |  | Oxnard Airport (KOXR) | Oxnard Airport (KOXR) | 2026-04-24 18:57 UTC | 2026-04-24 19:19 UTC | 22m |
| BCS87W | BCS | Ljubljana Joze Pucnik Airport (LJLJ) | Malpensa International Airport (LIMC) | 2026-04-24 18:29 UTC | 2026-04-24 19:17 UTC | 48m |
| N4308P |  | Old Bridge Airport (K3N6) | Atlantic City International Airport (KACY) | 2026-04-24 18:40 UTC | 2026-04-24 19:14 UTC | 33m |
| N974PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-04-24 18:21 UTC | 2026-04-24 19:12 UTC | 50m |
| SKEETR4 | SKE | Molnau Airpark (1MN5) | Flying Cloud Airport (KFCM) | 2026-04-24 16:56 UTC | 2026-04-24 19:12 UTC | 2h 15m |
| N5105M |  | Skypark Airport (KBTF) | Fort Ranch Airport (2UT3) | 2026-04-24 18:35 UTC | 2026-04-24 19:11 UTC | 36m |
| MYAVA | MYA | Paris-Le Bourget Airport (LFPB) | Brest Bretagne Airport (LFRB) | 2026-04-24 18:17 UTC | 2026-04-24 19:10 UTC | 53m |
| BOE403 | BOE | Boeing Field/King County International Airport (KBFI) | Othello Municipal Airport (KS70) | 2026-04-24 17:50 UTC | 2026-04-24 19:08 UTC | 1h 17m |
| N645PV |  | Redstone Army Air Field (KHUA) | Redstone Army Air Field (KHUA) | 2026-04-24 18:12 UTC | 2026-04-24 19:08 UTC | 55m |
| EDV5339 | EDV | Hartsfield/Jackson Atlanta International Airport (KATL) | Blairsville Airport (KDZJ) | 2026-04-24 18:26 UTC | 2026-04-24 19:07 UTC | 41m |
| CXK668 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-04-24 17:46 UTC | 2026-04-24 19:06 UTC | 1h 20m |
| N49ER |  | Gnoss Field (KDVO) | Sacramento Executive Airport (KSAC) | 2026-04-24 18:33 UTC | 2026-04-24 19:06 UTC | 32m |
| ROGUE1 | ROG | Randolph Afb Airport (KRND) | Rusty's Flying Service Airport (4TS8) | 2026-04-24 18:53 UTC | 2026-04-24 19:05 UTC | 11m |
| N22823 |  | Lake Havasu City Airport (KHII) | Gene Wash Reservoir Airport (5CL7) | 2026-04-24 18:42 UTC | 2026-04-24 19:02 UTC | 20m |
| N67322 |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-24 18:20 UTC | 2026-04-24 18:59 UTC | 38m |
| N307FD |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-04-24 17:54 UTC | 2026-04-24 18:57 UTC | 1h 3m |
| BB119 |  | Thomas Farms Airport (85FL) | Evergreen Regional/Middleton Field (KGZH) | 2026-04-24 18:36 UTC | 2026-04-24 18:57 UTC | 20m |
| HARM32 | HAR | Harrison Field Of Knox City Airport (KF75) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-04-24 18:41 UTC | 2026-04-24 18:56 UTC | 15m |
| N786AK |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-04-24 18:39 UTC | 2026-04-24 18:55 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
