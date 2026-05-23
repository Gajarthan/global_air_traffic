# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_16:27:19_UTC-green)

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

**Latest saved flight:** 2026-05-23 16:27:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 16:27:19 UTC

- **92,684** saved flights
- **32,852** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,684** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,139,772.9 tonnes** estimated CO2 emissions
- **66,073,790 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3921 |
| 2 | SkyWest Airlines | 3432 |
| 3 | IndiGo | 1931 |
| 4 | EJA | 1757 |
| 5 | American Airlines | 1402 |
| 6 | Southwest Airlines | 1336 |
| 7 | ENY | 1143 |
| 8 | Lufthansa | 1126 |
| 9 | Delta Air Lines | 1015 |
| 10 | Vueling | 882 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 739 |
| 15 | LXJ | 701 |
| 16 | Swiss International | 694 |
| 17 | All Nippon Airways | 689 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 605 |
| 21 | EJU | 591 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 562 |
| 24 | VIV | 549 |
| 25 | Air France | 543 |
| 26 | CXK | 490 |
| 27 | Japan Airlines | 487 |
| 28 | MXY | 485 |
| 29 | AXB | 471 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76566 |
| 2 | 🇪🇸 ES | 6519 |
| 3 | 🇮🇳 IN | 6085 |
| 4 | 🇦🇺 AU | 5727 |
| 5 | 🇩🇪 DE | 5094 |
| 6 | 🇧🇷 BR | 5068 |
| 7 | 🇮🇹 IT | 5042 |
| 8 | 🇨🇦 CA | 4689 |
| 9 | 🇯🇵 JP | 4476 |
| 10 | 🇬🇧 GB | 3946 |
| 11 | 🇫🇷 FR | 3740 |
| 12 | 🇨🇴 CO | 3217 |
| 13 | 🇲🇽 MX | 2850 |
| 14 | 🇬🇷 GR | 2653 |
| 15 | 🇳🇴 NO | 2580 |
| 16 | 🇨🇭 CH | 2427 |
| 17 | 🇲🇾 MY | 2065 |
| 18 | 🇹🇷 TR | 1695 |
| 19 | 🇿🇦 ZA | 1681 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1571 |
| 22 | 🇵🇱 PL | 1517 |
| 23 | 🇰🇷 KR | 1475 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1395 |
| 26 | 🇲🇦 MA | 1062 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 931 |
| 29 | 🇲🇪 ME | 929 |
| 30 | 🇭🇷 HR | 837 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2008 |
| 2 | Denver International Airport |  | US | 1556 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1324 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1237 |
| 6 | Harry Reid International Airport |  | US | 1192 |
| 7 | Frankfurt am Main International Airport |  | DE | 1135 |
| 8 | Guaymaral Airport |  | CO | 1117 |
| 9 | Zurich Airport |  | CH | 1085 |
| 10 | La Aurora Airport |  | GT | 1065 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1015 |
| 13 | El Dorado International Airport |  | CO | 1013 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 927 |
| 15 | Chicago O'Hare International Airport |  | US | 885 |
| 16 | Madrid Barajas International Airport |  | ES | 833 |
| 17 | Kuala Lumpur International Airport |  | MY | 815 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 781 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 769 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 738 |
| 23 | Bengaluru International Airport |  | IN | 732 |
| 24 | Charles de Gaulle International Airport |  | FR | 723 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 704 |
| 27 | Daniel K Inouye International Airport |  | US | 670 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 623 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 614 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 604 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 598 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 580 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 571 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 550 |
| 40 | O. R. Tambo International Airport |  | ZA | 532 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 459 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 342 | 21m | 244 km | 1,440.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 128 | 20m | 250 km | 552.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6141J |  | Mitchell Municipal Airport (KMHE) | Mitchell Municipal Airport (KMHE) | 2026-05-23 15:53 UTC | 2026-05-23 16:27 UTC | 34m |
| N7524R |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-05-23 16:06 UTC | 2026-05-23 16:27 UTC | 20m |
| N33ET |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-05-23 16:06 UTC | 2026-05-23 16:26 UTC | 20m |
| N750AY |  | CARK (CARK) | CARK (CARK) | 2026-05-23 15:33 UTC | 2026-05-23 16:18 UTC | 44m |
| NWX382 | NWX | Aero Valley Airport (K52F) | Spectre Field (XA07) | 2026-05-23 15:42 UTC | 2026-05-23 16:14 UTC | 31m |
| FGIBV | FGI | Chambery-Challes-les-Eaux Airport (LFLE) | Chambery-Savoie Airport (LFLB) | 2026-05-23 15:17 UTC | 2026-05-23 16:09 UTC | 51m |
| N360DF |  | Reedley Municipal Airport (KO32) | Lake Tahoe Airport (KTVL) | 2026-05-23 15:40 UTC | 2026-05-23 16:08 UTC | 27m |
| N80912 |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-05-23 15:38 UTC | 2026-05-23 16:06 UTC | 28m |
| N390SB |  | Rocky Mountain Metro Airport (KBJC) | Santa Fe Regional Airport (KSAF) | 2026-05-23 15:22 UTC | 2026-05-23 16:03 UTC | 41m |
| N9390M |  | K61B (K61B) | K61B (K61B) | 2026-05-23 15:59 UTC | 2026-05-23 16:03 UTC | 4m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-05-23 14:41 UTC | 2026-05-23 16:02 UTC | 1h 21m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-05-23 15:55 UTC | 2026-05-23 16:01 UTC | 5m |
| N224LA |  | San Gabriel Valley Airport (KEMT) | Van Nuys Airport (KVNY) | 2026-05-23 15:33 UTC | 2026-05-23 16:00 UTC | 27m |
| SCA42 | SCA | Scottsdale Airport (KSDL) | Lake Havasu City Airport (KHII) | 2026-05-23 14:29 UTC | 2026-05-23 16:00 UTC | 1h 31m |
| N913SB |  | El Peco Ranch Airport (49CL) | Palo Alto Airport (KPAO) | 2026-05-23 15:33 UTC | 2026-05-23 16:00 UTC | 27m |
| N7824W |  | Truckee-Tahoe Airport (KTRK) | Auburn Municipal Airport (KAUN) | 2026-05-23 15:30 UTC | 2026-05-23 15:58 UTC | 28m |
| DMSJA | DMS | Zell-Haidberg Airport (EDNZ) | Zell-Haidberg Airport (EDNZ) | 2026-05-23 15:42 UTC | 2026-05-23 15:52 UTC | 10m |
| N801JA |  | Pru Field (K33S) | Pru Field (K33S) | 2026-05-23 15:43 UTC | 2026-05-23 15:51 UTC | 7m |
| N62WA |  | Muscatine Municipal Airport (KMUT) | Sullivan County Airport (KSIV) | 2026-05-23 15:19 UTC | 2026-05-23 15:50 UTC | 31m |
| 2000 |  | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-05-23 15:36 UTC | 2026-05-23 15:48 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
