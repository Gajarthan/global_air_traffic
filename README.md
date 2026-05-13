# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_19:56:17_UTC-green)

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

**Latest saved flight:** 2026-05-13 19:56:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 19:56:17 UTC

- **80,694** saved flights
- **29,296** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **80,694** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **993,902.9 tonnes** estimated CO2 emissions
- **57,617,558 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3463 |
| 2 | SkyWest Airlines | 2997 |
| 3 | IndiGo | 1777 |
| 4 | EJA | 1505 |
| 5 | American Airlines | 1247 |
| 6 | Southwest Airlines | 1177 |
| 7 | Lufthansa | 1054 |
| 8 | ENY | 1006 |
| 9 | Delta Air Lines | 886 |
| 10 | Vueling | 770 |
| 11 | AXM | 734 |
| 12 | LATAM Airlines | 733 |
| 13 | WIF | 702 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 632 |
| 16 | Swiss International | 628 |
| 17 | QLK | 596 |
| 18 | LXJ | 588 |
| 19 | Alaska Airlines | 566 |
| 20 | easyJet | 536 |
| 21 | EJU | 519 |
| 22 | AEE | 517 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 479 |
| 25 | Air France | 476 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 438 |
| 28 | CXK | 422 |
| 29 | AIQ | 399 |
| 30 | MXY | 399 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 65653 |
| 2 | 🇪🇸 ES | 5751 |
| 3 | 🇮🇳 IN | 5553 |
| 4 | 🇦🇺 AU | 5147 |
| 5 | 🇩🇪 DE | 4561 |
| 6 | 🇮🇹 IT | 4472 |
| 7 | 🇧🇷 BR | 4449 |
| 8 | 🇯🇵 JP | 4123 |
| 9 | 🇨🇦 CA | 4009 |
| 10 | 🇬🇧 GB | 3463 |
| 11 | 🇫🇷 FR | 3213 |
| 12 | 🇨🇴 CO | 2720 |
| 13 | 🇲🇽 MX | 2430 |
| 14 | 🇬🇷 GR | 2368 |
| 15 | 🇳🇴 NO | 2257 |
| 16 | 🇨🇭 CH | 2181 |
| 17 | 🇲🇾 MY | 1840 |
| 18 | 🇿🇦 ZA | 1530 |
| 19 | 🇹🇷 TR | 1446 |
| 20 | 🇹🇭 TH | 1419 |
| 21 | 🇳🇿 NZ | 1414 |
| 22 | 🇵🇱 PL | 1345 |
| 23 | 🇵🇭 PH | 1268 |
| 24 | 🇰🇷 KR | 1235 |
| 25 | 🇬🇹 GT | 1232 |
| 26 | 🇲🇦 MA | 947 |
| 27 | 🇲🇴 MO | 928 |
| 28 | 🇲🇪 ME | 864 |
| 29 | 🇳🇱 NL | 836 |
| 30 | 🇭🇷 HR | 711 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1768 |
| 2 | Tokyo International Airport |  | JP | 1383 |
| 3 | Denver International Airport |  | US | 1353 |
| 4 | Indira Gandhi International Airport |  | IN | 1175 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1159 |
| 6 | Frankfurt am Main International Airport |  | DE | 1063 |
| 7 | Harry Reid International Airport |  | US | 997 |
| 8 | Zurich Airport |  | CH | 965 |
| 9 | La Aurora Airport |  | GT | 930 |
| 10 | Macau International Airport |  | MO | 928 |
| 11 | Guaymaral Airport |  | CO | 912 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 911 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 815 |
| 15 | Chicago O'Hare International Airport |  | US | 787 |
| 16 | Madrid Barajas International Airport |  | ES | 740 |
| 17 | Kuala Lumpur International Airport |  | MY | 736 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 708 |
| 19 | Malpensa International Airport |  | IT | 688 |
| 20 | Bengaluru International Airport |  | IN | 683 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 22 | Salt Lake City International Airport |  | US | 665 |
| 23 | Capua Airport |  | IT | 659 |
| 24 | Charlotte/Douglas International Airport |  | US | 632 |
| 25 | Charles de Gaulle International Airport |  | FR | 632 |
| 26 | Congonhas Airport |  | BR | 627 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Daniel K Inouye International Airport |  | US | 584 |
| 29 | Ninoy Aquino International Airport |  | PH | 579 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 579 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 541 |
| 32 | Barcelona International Airport |  | ES | 541 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 535 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 525 |
| 35 | Vitoria/Foronda Airport |  | ES | 512 |
| 36 | Don Mueang International Airport |  | TH | 508 |
| 37 | Amsterdam Airport Schiphol |  | NL | 505 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 504 |
| 39 | O. R. Tambo International Airport |  | ZA | 486 |
| 40 | Calgary International Airport |  | CA | 474 |

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
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 108 | 1h 2m | 695 km | 1,294.6 t |
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
| N25497 |  | Denton Enterprise Airport (KDTO) | Windy Tales Airport (TX34) | 2026-05-13 19:25 UTC | 2026-05-13 19:56 UTC | 30m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-13 17:43 UTC | 2026-05-13 19:44 UTC | 2h 0m |
| N100PC |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-05-13 19:29 UTC | 2026-05-13 19:40 UTC | 11m |
| N786CP |  | Atlanta Regional Falcon Field (KFFC) | Richard B Russell Regional - J H Towers Field (KRMG) | 2026-05-13 18:50 UTC | 2026-05-13 19:40 UTC | 49m |
| NTF279M | NTF | Poprad-Tatry Airport (LZTT) | M. R. Stefanik Airport (LZIB) | 2026-05-13 18:57 UTC | 2026-05-13 19:36 UTC | 38m |
| CHX26 | CHX | Wilhelmshaven-Mariensiel Airport (EDWI) | Wangerooge Airport (EDWG) | 2026-05-13 19:26 UTC | 2026-05-13 19:35 UTC | 8m |
| N510KB |  | Mc Alester Regional Airport (KMLC) | Mc Alester Regional Airport (KMLC) | 2026-05-13 18:32 UTC | 2026-05-13 19:30 UTC | 58m |
| N223AL |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-13 19:16 UTC | 2026-05-13 19:30 UTC | 14m |
| N858MG |  | Dubuque Regional Airport (KDBQ) | Rochester International Airport (KRST) | 2026-05-13 18:56 UTC | 2026-05-13 19:23 UTC | 27m |
| EJA467 | EJA | Centennial Airport (KAPA) | Moffett Federal Airfield (KNUQ) | 2026-05-13 17:09 UTC | 2026-05-13 19:21 UTC | 2h 12m |
| N551JW |  | Scottsdale Airport (KSDL) | Chapman Ranch Airstrip (58AZ) | 2026-05-13 18:56 UTC | 2026-05-13 19:19 UTC | 22m |
| N818MT |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-13 19:12 UTC | 2026-05-13 19:18 UTC | 6m |
| N479L |  | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-05-13 18:50 UTC | 2026-05-13 19:18 UTC | 28m |
| N714WP |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-13 19:14 UTC | 2026-05-13 19:17 UTC | 3m |
| N245CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-05-13 19:03 UTC | 2026-05-13 19:16 UTC | 13m |
| N747EE |  | John F Kennedy International Airport (KJFK) | Teterboro Airport (KTEB) | 2026-05-13 19:07 UTC | 2026-05-13 19:16 UTC | 8m |
| N458CP |  | Canton Municipal Airport (K7G9) | Mitchell Municipal Airport (KMHE) | 2026-05-13 18:45 UTC | 2026-05-13 19:14 UTC | 29m |
| N181JP |  | Rio Vista Municipal Airport (KO88) | Truckee-Tahoe Airport (KTRK) | 2026-05-13 18:35 UTC | 2026-05-13 19:13 UTC | 38m |
| N571CH |  | Harry Reid International Airport (KLAS) | Smith Airport (6LL5) | 2026-05-13 16:35 UTC | 2026-05-13 19:09 UTC | 2h 34m |
| BRG621 | BRG | Kobuk Airport (PAOB) | Ambler Airport (PAFM) | 2026-05-13 18:59 UTC | 2026-05-13 19:09 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
