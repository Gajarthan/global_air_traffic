# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_18:42:17_UTC-green)

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

**Latest saved flight:** 2026-05-05 18:42:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 18:42:17 UTC

- **69,435** saved flights
- **25,967** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,435** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **853,765.5 tonnes** estimated CO2 emissions
- **49,493,652 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2985 |
| 2 | SkyWest Airlines | 2579 |
| 3 | IndiGo | 1598 |
| 4 | EJA | 1253 |
| 5 | American Airlines | 1080 |
| 6 | Southwest Airlines | 991 |
| 7 | Lufthansa | 898 |
| 8 | ENY | 856 |
| 9 | Vueling | 682 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 644 |
| 12 | WIF | 593 |
| 13 | All Nippon Airways | 585 |
| 14 | Delta Air Lines | 580 |
| 15 | AZU | 565 |
| 16 | Swiss International | 537 |
| 17 | QLK | 534 |
| 18 | LXJ | 501 |
| 19 | Alaska Airlines | 476 |
| 20 | easyJet | 467 |
| 21 | AEE | 452 |
| 22 | EJU | 451 |
| 23 | VIV | 433 |
| 24 | Cathay Pacific | 417 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 338 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55004 |
| 2 | 🇪🇸 ES | 5076 |
| 3 | 🇮🇳 IN | 5025 |
| 4 | 🇦🇺 AU | 4599 |
| 5 | 🇧🇷 BR | 3899 |
| 6 | 🇩🇪 DE | 3891 |
| 7 | 🇮🇹 IT | 3809 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3432 |
| 10 | 🇬🇧 GB | 3024 |
| 11 | 🇫🇷 FR | 2762 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2201 |
| 14 | 🇬🇷 GR | 2081 |
| 15 | 🇨🇭 CH | 1917 |
| 16 | 🇳🇴 NO | 1907 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1255 |
| 22 | 🇵🇭 PH | 1158 |
| 23 | 🇵🇱 PL | 1143 |
| 24 | 🇬🇹 GT | 1117 |
| 25 | 🇰🇷 KR | 1110 |
| 26 | 🇲🇦 MA | 839 |
| 27 | 🇲🇴 MO | 787 |
| 28 | 🇲🇪 ME | 751 |
| 29 | 🇳🇱 NL | 727 |
| 30 | 🇮🇩 ID | 587 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1535 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1138 |
| 4 | Indira Gandhi International Airport |  | IN | 1053 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1018 |
| 6 | Frankfurt am Main International Airport |  | DE | 892 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 864 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 831 |
| 11 | Zurich Airport |  | CH | 823 |
| 12 | Macau International Airport |  | MO | 787 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 690 |
| 14 | Kuala Lumpur International Airport |  | MY | 668 |
| 15 | Chicago O'Hare International Airport |  | US | 664 |
| 16 | Madrid Barajas International Airport |  | ES | 662 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 618 |
| 18 | Malpensa International Airport |  | IT | 605 |
| 19 | Bengaluru International Airport |  | IN | 605 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Salt Lake City International Airport |  | US | 556 |
| 22 | Congonhas Airport |  | BR | 555 |
| 23 | Charles de Gaulle International Airport |  | FR | 548 |
| 24 | Charlotte/Douglas International Airport |  | US | 547 |
| 25 | Tenerife Norte Airport |  | ES | 543 |
| 26 | Capua Airport |  | IT | 538 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 509 |
| 29 | Daniel K Inouye International Airport |  | US | 504 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 489 |
| 31 | Barcelona International Airport |  | ES | 482 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 464 |
| 34 | Vitoria/Foronda Airport |  | ES | 462 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 438 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 433 |
| 38 | Amsterdam Airport Schiphol |  | NL | 429 |
| 39 | Reno/Tahoe International Airport |  | US | 412 |
| 40 | Calgary International Airport |  | CA | 411 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 238 | 21m | 244 km | 1,002.2 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 172 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 156 | 26m | 275 km | 739.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 132 | 21m | 99 km | 226.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N26WR |  | Marina Municipal Airport (KOAR) | Santa Monica Municipal Airport (KSMO) | 2026-05-05 17:47 UTC | 2026-05-05 18:42 UTC | 55m |
| N203VS |  | Mojave Air & Space Port/Rutan Field (KMHV) | Boron Airstrip (57CL) | 2026-05-05 18:01 UTC | 2026-05-05 18:40 UTC | 39m |
| N960GV |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-05 17:41 UTC | 2026-05-05 18:39 UTC | 57m |
| VAR520 | VAR | 13AZ (13AZ) | Phoenix Goodyear Airport (KGYR) | 2026-05-05 18:03 UTC | 2026-05-05 18:35 UTC | 32m |
| RDHK707 | RDH | Norfolk Ns (Chambers Field) Airport (KNGU) | Cherrystone Airport (24VA) | 2026-05-05 18:16 UTC | 2026-05-05 18:27 UTC | 10m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-05 18:14 UTC | 2026-05-05 18:25 UTC | 11m |
| CGLII | CGL | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Goyer Field (CGF2) | 2026-05-05 18:18 UTC | 2026-05-05 18:21 UTC | 3m |
| RYR5KN | Ryanair | Sandefjord Airport Torp (ENTO) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-05 16:36 UTC | 2026-05-05 18:21 UTC | 1h 44m |
| N1481V |  | Tampa North Aero Park Airport (KX39) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-05-05 17:53 UTC | 2026-05-05 18:20 UTC | 26m |
| N630CB |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-05 17:45 UTC | 2026-05-05 18:15 UTC | 30m |
| N3VJ |  | Albany International Airport (KALB) | Lancaster Airport (KLNS) | 2026-05-05 16:44 UTC | 2026-05-05 18:14 UTC | 1h 29m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-05-05 17:13 UTC | 2026-05-05 18:11 UTC | 57m |
| N653CC |  | Jackson Regional Airport (KMKL) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-05 17:16 UTC | 2026-05-05 18:10 UTC | 54m |
| RNGR763 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-05-05 17:40 UTC | 2026-05-05 18:10 UTC | 30m |
| PAT325 | PAT | Phillips Army Air Field (KAPG) | Greater Gortner Airport (2MD8) | 2026-05-05 17:20 UTC | 2026-05-05 18:06 UTC | 46m |
|  |  | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-05-05 18:06 UTC | 2026-05-05 18:06 UTC | 0m |
| CASTOR1 | CAS | Pirassununga Airport (SDPY) | Fazenda Santa Terezinha da Barra Airport (SDST) | 2026-05-05 17:15 UTC | 2026-05-05 18:04 UTC | 49m |
| N550LV |  | Emporia-Greensville Regional Airport (KEMV) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-05-05 17:36 UTC | 2026-05-05 18:04 UTC | 28m |
| N460LD |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-05-05 17:43 UTC | 2026-05-05 18:04 UTC | 20m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-05-05 17:16 UTC | 2026-05-05 18:03 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
