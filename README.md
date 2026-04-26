# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_19:23:46_UTC-green)

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

**Latest saved flight:** 2026-04-26 19:23:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 19:23:46 UTC

- **55,833** saved flights
- **21,935** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,833** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **674,675.2 tonnes** estimated CO2 emissions
- **39,111,606 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2372 |
| 2 | SkyWest Airlines | 2103 |
| 3 | IndiGo | 1275 |
| 4 | EJA | 986 |
| 5 | American Airlines | 889 |
| 6 | Southwest Airlines | 786 |
| 7 | ENY | 701 |
| 8 | Lufthansa | 691 |
| 9 | Vueling | 562 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 538 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 470 |
| 14 | WIF | 465 |
| 15 | Delta Air Lines | 458 |
| 16 | Swiss International | 438 |
| 17 | QLK | 429 |
| 18 | LXJ | 400 |
| 19 | AEE | 369 |
| 20 | Alaska Airlines | 369 |
| 21 | EJU | 361 |
| 22 | VIV | 356 |
| 23 | easyJet | 355 |
| 24 | Air France | 327 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 313 |
| 27 | AXB | 305 |
| 28 | GLO | 284 |
| 29 | JetBlue | 284 |
| 30 | AIQ | 283 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44150 |
| 2 | 🇪🇸 ES | 4092 |
| 3 | 🇮🇳 IN | 4024 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3226 |
| 6 | 🇩🇪 DE | 3063 |
| 7 | 🇮🇹 IT | 3052 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2765 |
| 10 | 🇨🇴 CO | 2529 |
| 11 | 🇬🇧 GB | 2352 |
| 12 | 🇫🇷 FR | 2210 |
| 13 | 🇲🇽 MX | 1767 |
| 14 | 🇬🇷 GR | 1661 |
| 15 | 🇨🇭 CH | 1585 |
| 16 | 🇳🇴 NO | 1503 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1151 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1024 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 905 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 832 |
| 26 | 🇲🇦 MA | 711 |
| 27 | 🇲🇪 ME | 608 |
| 28 | 🇳🇱 NL | 583 |
| 29 | 🇲🇴 MO | 572 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1265 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 920 |
| 4 | Indira Gandhi International Airport |  | IN | 852 |
| 5 | El Dorado International Airport |  | CO | 850 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 818 |
| 7 | Guaymaral Airport |  | CO | 774 |
| 8 | Harry Reid International Airport |  | US | 708 |
| 9 | Frankfurt am Main International Airport |  | DE | 676 |
| 10 | Zurich Airport |  | CH | 672 |
| 11 | La Aurora Airport |  | GT | 625 |
| 12 | Macau International Airport |  | MO | 572 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 554 |
| 14 | Chicago O'Hare International Airport |  | US | 546 |
| 15 | Madrid Barajas International Airport |  | ES | 526 |
| 16 | Kuala Lumpur International Airport |  | MY | 523 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 519 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 483 |
| 20 | Bengaluru International Airport |  | IN | 479 |
| 21 | Congonhas Airport |  | BR | 465 |
| 22 | Charlotte/Douglas International Airport |  | US | 450 |
| 23 | Tenerife Norte Airport |  | ES | 449 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 431 |
| 26 | Salt Lake City International Airport |  | US | 425 |
| 27 | Capua Airport |  | IT | 415 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 411 |
| 29 | Daniel K Inouye International Airport |  | US | 409 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 402 |
| 31 | Vitoria/Foronda Airport |  | ES | 384 |
| 32 | Barcelona International Airport |  | ES | 383 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 375 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 372 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 365 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 360 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 333 |
| 40 | Amsterdam Airport Schiphol |  | NL | 331 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 316 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 204 | 14m | 114 km | 400.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 176 | 21m | 244 km | 741.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 134 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 87 | 27m | 152 km | 227.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 78 | 1h 1m | 695 km | 935.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 53m | 1,304 km | 1,709.8 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 73 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13081 |  | Lawrence Municipal Airport (KLWM) | Laconia Municipal Airport (KLCI) | 2026-04-26 18:45 UTC | 2026-04-26 19:23 UTC | 38m |
| TEK63 | TEK | Manassas Regional/Harry P Davis Field (KHEF) | Chester County G O Carlson Airport (KMQS) | 2026-04-26 18:36 UTC | 2026-04-26 19:18 UTC | 42m |
| DFEEL | DFE | Hamburg Airport (EDDH) | Leipzig Halle Airport (EDDP) | 2026-04-26 18:28 UTC | 2026-04-26 19:13 UTC | 44m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-26 18:53 UTC | 2026-04-26 19:07 UTC | 13m |
| BRG661 | BRG | Point Hope Airport (PAPO) | Kivalina Airport (PAVL) | 2026-04-26 18:42 UTC | 2026-04-26 19:06 UTC | 24m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-26 18:44 UTC | 2026-04-26 19:04 UTC | 20m |
| VOC4062 | VOC | Licenciado Benito Juarez International Airport (MMMX) | La Aurora Airport (MGGT) | 2026-04-26 17:10 UTC | 2026-04-26 19:01 UTC | 1h 51m |
| N513LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-26 18:28 UTC | 2026-04-26 19:00 UTC | 31m |
| EJA286 | EJA | San Luis Obispo County Regional Airport (KSBP) | Bermuda Dunes Airport (KUDD) | 2026-04-26 18:15 UTC | 2026-04-26 18:51 UTC | 36m |
| N52795 |  | Leeward Air Ranch Airport (FD04) | Post Oak Ranch Airport (1FA1) | 2026-04-26 18:33 UTC | 2026-04-26 18:48 UTC | 15m |
| N408SH |  | St Pete-Clearwater International Airport (KPIE) | Clearwater Executive Airport (KCLW) | 2026-04-26 18:44 UTC | 2026-04-26 18:48 UTC | 4m |
| N493PJ |  | Red Bluff Municipal Airport (KRBL) | Lake California Air Park (68CA) | 2026-04-26 18:41 UTC | 2026-04-26 18:47 UTC | 5m |
| N22TE |  | 2OR7 (2OR7) | Mt Hope Airport (OG10) | 2026-04-26 18:14 UTC | 2026-04-26 18:43 UTC | 29m |
| N12RH |  | Bowman Field (KLOU) | Bowman Field (KLOU) | 2026-04-26 18:22 UTC | 2026-04-26 18:43 UTC | 21m |
| VVSA72 | VVS | CA84 (CA84) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-26 18:17 UTC | 2026-04-26 18:41 UTC | 23m |
| N50KL |  | Auburn University Regional Airport (KAUO) | AL02 (AL02) | 2026-04-26 18:24 UTC | 2026-04-26 18:41 UTC | 17m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-26 18:29 UTC | 2026-04-26 18:40 UTC | 10m |
| RYR1TU | Ryanair | Girona Airport (LEGE) | Poznań-Ławica Airport (EPPO) | 2026-04-26 16:29 UTC | 2026-04-26 18:39 UTC | 2h 10m |
| EIN723 | Aer Lingus | London Heathrow Airport (EGLL) | Cork Airport (EICK) | 2026-04-26 17:43 UTC | 2026-04-26 18:38 UTC | 54m |
| WIF3F | WIF | Bergen Airport Flesland (ENBR) | Stavanger Airport Sola (ENZV) | 2026-04-26 18:20 UTC | 2026-04-26 18:38 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
