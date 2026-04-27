# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_17:57:49_UTC-green)

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

**Latest saved flight:** 2026-04-27 17:57:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 17:57:49 UTC

- **57,065** saved flights
- **22,330** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,065** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **693,244.7 tonnes** estimated CO2 emissions
- **40,188,100 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2426 |
| 2 | SkyWest Airlines | 2153 |
| 3 | IndiGo | 1298 |
| 4 | EJA | 1021 |
| 5 | American Airlines | 905 |
| 6 | Southwest Airlines | 817 |
| 7 | ENY | 718 |
| 8 | Lufthansa | 705 |
| 9 | Vueling | 574 |
| 10 | AXM | 553 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 501 |
| 13 | AZU | 477 |
| 14 | WIF | 473 |
| 15 | Delta Air Lines | 471 |
| 16 | Swiss International | 450 |
| 17 | QLK | 439 |
| 18 | LXJ | 408 |
| 19 | Alaska Airlines | 384 |
| 20 | AEE | 377 |
| 21 | EJU | 370 |
| 22 | easyJet | 370 |
| 23 | VIV | 364 |
| 24 | Air France | 334 |
| 25 | Cathay Pacific | 328 |
| 26 | Japan Airlines | 327 |
| 27 | AXB | 312 |
| 28 | JetBlue | 291 |
| 29 | GLO | 287 |
| 30 | AIQ | 286 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45227 |
| 2 | 🇪🇸 ES | 4172 |
| 3 | 🇮🇳 IN | 4092 |
| 4 | 🇦🇺 AU | 3812 |
| 5 | 🇧🇷 BR | 3280 |
| 6 | 🇩🇪 DE | 3126 |
| 7 | 🇮🇹 IT | 3124 |
| 8 | 🇯🇵 JP | 3048 |
| 9 | 🇨🇦 CA | 2821 |
| 10 | 🇨🇴 CO | 2583 |
| 11 | 🇬🇧 GB | 2416 |
| 12 | 🇫🇷 FR | 2248 |
| 13 | 🇲🇽 MX | 1810 |
| 14 | 🇬🇷 GR | 1695 |
| 15 | 🇨🇭 CH | 1605 |
| 16 | 🇳🇴 NO | 1541 |
| 17 | 🇲🇾 MY | 1343 |
| 18 | 🇿🇦 ZA | 1165 |
| 19 | 🇳🇿 NZ | 1072 |
| 20 | 🇹🇷 TR | 1042 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 964 |
| 23 | 🇵🇱 PL | 923 |
| 24 | 🇰🇷 KR | 904 |
| 25 | 🇬🇹 GT | 847 |
| 26 | 🇲🇦 MA | 722 |
| 27 | 🇲🇪 ME | 622 |
| 28 | 🇲🇴 MO | 607 |
| 29 | 🇳🇱 NL | 597 |
| 30 | 🇧🇸 BS | 488 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1290 |
| 2 | Tokyo International Airport |  | JP | 1034 |
| 3 | Denver International Airport |  | US | 948 |
| 4 | El Dorado International Airport |  | CO | 869 |
| 5 | Indira Gandhi International Airport |  | IN | 868 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 835 |
| 7 | Guaymaral Airport |  | CO | 796 |
| 8 | Harry Reid International Airport |  | US | 726 |
| 9 | Frankfurt am Main International Airport |  | DE | 694 |
| 10 | Zurich Airport |  | CH | 686 |
| 11 | La Aurora Airport |  | GT | 638 |
| 12 | Macau International Airport |  | MO | 607 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 568 |
| 14 | Chicago O'Hare International Airport |  | US | 553 |
| 15 | Madrid Barajas International Airport |  | ES | 533 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 530 |
| 17 | Kuala Lumpur International Airport |  | MY | 529 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 501 |
| 19 | Malpensa International Airport |  | IT | 497 |
| 20 | Bengaluru International Airport |  | IN | 490 |
| 21 | Congonhas Airport |  | BR | 472 |
| 22 | Charlotte/Douglas International Airport |  | US | 459 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Ninoy Aquino International Airport |  | PH | 443 |
| 25 | Salt Lake City International Airport |  | US | 440 |
| 26 | Charles de Gaulle International Airport |  | FR | 440 |
| 27 | Capua Airport |  | IT | 433 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 421 |
| 29 | Daniel K Inouye International Airport |  | US | 420 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 409 |
| 31 | Barcelona International Airport |  | ES | 391 |
| 32 | Vitoria/Foronda Airport |  | ES | 388 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 385 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 379 |
| 35 | Reno/Tahoe International Airport |  | US | 370 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 37 | O. R. Tambo International Airport |  | ZA | 367 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 341 |
| 40 | Calgary International Airport |  | CA | 339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 325 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 209 | 14m | 114 km | 409.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 183 | 21m | 244 km | 770.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 163 | 1h 27m | 910 km | 2,557.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 111 | 1h 12m | 770 km | 1,474.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 109 | 44m | 452 km | 849.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 96 | 31m | 369 km | 611.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 86 | 52m | 556 km | 824.4 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 53m | 1,304 km | 1,732.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 73 | 1h 42m | 1,423 km | 1,791.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N681MA |  | Trenton Mercer Airport (KTTN) | Malone Airport (NJ61) | 2026-04-27 17:12 UTC | 2026-04-27 17:57 UTC | 45m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-04-27 08:21 UTC | 2026-04-27 17:48 UTC | 9h 26m |
| SCARY71 | SCA | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-04-27 17:10 UTC | 2026-04-27 17:41 UTC | 31m |
| HOVER91 | HOV | 2TX3 (2TX3) | Tularosa Airport (TA31) | 2026-04-27 17:29 UTC | 2026-04-27 17:41 UTC | 11m |
| QTR49U | Qatar Airways | Munich International Airport (EDDM) | Queen Alia International Airport (OJAI) | 2026-04-27 14:59 UTC | 2026-04-27 17:40 UTC | 2h 41m |
| N37CJ |  | Phoenix Goodyear Airport (KGYR) | Glendale Regional Airport (KGEU) | 2026-04-27 17:26 UTC | 2026-04-27 17:40 UTC | 14m |
| JEDDA66 | JED | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-04-27 17:28 UTC | 2026-04-27 17:38 UTC | 10m |
| CTM1245 | CTM | Toulouse-Francazal (BA 101) Air Base (LFBF) | Toulouse-Francazal (BA 101) Air Base (LFBF) | 2026-04-27 17:06 UTC | 2026-04-27 17:36 UTC | 30m |
| BOX544 | BOX | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-27 04:19 UTC | 2026-04-27 17:35 UTC | 13h 16m |
| N2533X |  | Fort Meade Executive Airport (KFME) | Ocean City Municipal Airport (KOXB) | 2026-04-27 16:40 UTC | 2026-04-27 17:35 UTC | 54m |
| N235CD |  | West Virginia International Yeager Airport (KCRW) | Richwood Municipal Airport (K3I4) | 2026-04-27 17:01 UTC | 2026-04-27 17:34 UTC | 33m |
| VLG8102 | Vueling | Barcelona International Airport (LEBL) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-27 15:04 UTC | 2026-04-27 17:33 UTC | 2h 28m |
| N314RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Hopewell Airpark (90NY) | 2026-04-27 16:50 UTC | 2026-04-27 17:32 UTC | 41m |
| N614CF |  | Ohio State University Airport (KOSU) | Delaware Municipal/Jim Moore Field (KDLZ) | 2026-04-27 16:32 UTC | 2026-04-27 17:29 UTC | 57m |
| BOE079 | BOE | Seattle Paine Field International Airport (KPAE) | Grant County International Airport (KMWH) | 2026-04-27 16:16 UTC | 2026-04-27 17:27 UTC | 1h 11m |
| N2090Z |  | Summit Airport (KEVY) | Ocean City Municipal Airport (KOXB) | 2026-04-27 16:27 UTC | 2026-04-27 17:27 UTC | 59m |
| N8119H |  | Beverly Regional Airport (KBVY) | Laconia Municipal Airport (KLCI) | 2026-04-27 16:51 UTC | 2026-04-27 17:27 UTC | 35m |
| BURNY17 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-27 17:09 UTC | 2026-04-27 17:27 UTC | 17m |
| N386ST |  | Carroll County Regional/Jack B Poage Field (KDMW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-27 16:23 UTC | 2026-04-27 17:22 UTC | 58m |
| N272BG |  | Seattle Paine Field International Airport (KPAE) | Moffett Federal Airfield (KNUQ) | 2026-04-27 15:46 UTC | 2026-04-27 17:22 UTC | 1h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
