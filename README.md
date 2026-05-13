# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_15:48:42_UTC-green)

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

**Latest saved flight:** 2026-05-13 15:48:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 15:48:42 UTC

- **80,275** saved flights
- **29,166** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **80,275** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **989,819.3 tonnes** estimated CO2 emissions
- **57,380,830 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3449 |
| 2 | SkyWest Airlines | 2971 |
| 3 | IndiGo | 1776 |
| 4 | EJA | 1486 |
| 5 | American Airlines | 1243 |
| 6 | Southwest Airlines | 1172 |
| 7 | Lufthansa | 1052 |
| 8 | ENY | 998 |
| 9 | Delta Air Lines | 876 |
| 10 | Vueling | 768 |
| 11 | AXM | 734 |
| 12 | LATAM Airlines | 730 |
| 13 | WIF | 696 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 631 |
| 16 | Swiss International | 626 |
| 17 | QLK | 596 |
| 18 | LXJ | 583 |
| 19 | Alaska Airlines | 563 |
| 20 | easyJet | 534 |
| 21 | EJU | 518 |
| 22 | AEE | 516 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 477 |
| 25 | Air France | 474 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 438 |
| 28 | CXK | 418 |
| 29 | AIQ | 399 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 65151 |
| 2 | 🇪🇸 ES | 5730 |
| 3 | 🇮🇳 IN | 5550 |
| 4 | 🇦🇺 AU | 5145 |
| 5 | 🇩🇪 DE | 4547 |
| 6 | 🇮🇹 IT | 4449 |
| 7 | 🇧🇷 BR | 4436 |
| 8 | 🇯🇵 JP | 4123 |
| 9 | 🇨🇦 CA | 4000 |
| 10 | 🇬🇧 GB | 3446 |
| 11 | 🇫🇷 FR | 3195 |
| 12 | 🇨🇴 CO | 2716 |
| 13 | 🇲🇽 MX | 2417 |
| 14 | 🇬🇷 GR | 2360 |
| 15 | 🇳🇴 NO | 2237 |
| 16 | 🇨🇭 CH | 2174 |
| 17 | 🇲🇾 MY | 1840 |
| 18 | 🇿🇦 ZA | 1528 |
| 19 | 🇹🇷 TR | 1442 |
| 20 | 🇹🇭 TH | 1419 |
| 21 | 🇳🇿 NZ | 1414 |
| 22 | 🇵🇱 PL | 1339 |
| 23 | 🇵🇭 PH | 1268 |
| 24 | 🇰🇷 KR | 1235 |
| 25 | 🇬🇹 GT | 1225 |
| 26 | 🇲🇦 MA | 941 |
| 27 | 🇲🇴 MO | 928 |
| 28 | 🇲🇪 ME | 859 |
| 29 | 🇳🇱 NL | 833 |
| 30 | 🇭🇷 HR | 709 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1758 |
| 2 | Tokyo International Airport |  | JP | 1383 |
| 3 | Denver International Airport |  | US | 1341 |
| 4 | Indira Gandhi International Airport |  | IN | 1174 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1157 |
| 6 | Frankfurt am Main International Airport |  | DE | 1059 |
| 7 | Harry Reid International Airport |  | US | 993 |
| 8 | Zurich Airport |  | CH | 962 |
| 9 | Macau International Airport |  | MO | 928 |
| 10 | La Aurora Airport |  | GT | 923 |
| 11 | Guaymaral Airport |  | CO | 908 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 900 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 810 |
| 15 | Chicago O'Hare International Airport |  | US | 779 |
| 16 | Madrid Barajas International Airport |  | ES | 737 |
| 17 | Kuala Lumpur International Airport |  | MY | 736 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 706 |
| 19 | Malpensa International Airport |  | IT | 688 |
| 20 | Bengaluru International Airport |  | IN | 682 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 22 | Salt Lake City International Airport |  | US | 657 |
| 23 | Capua Airport |  | IT | 653 |
| 24 | Charlotte/Douglas International Airport |  | US | 630 |
| 25 | Charles de Gaulle International Airport |  | FR | 629 |
| 26 | Congonhas Airport |  | BR | 626 |
| 27 | Tenerife Norte Airport |  | ES | 598 |
| 28 | Daniel K Inouye International Airport |  | US | 581 |
| 29 | Ninoy Aquino International Airport |  | PH | 579 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 578 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 540 |
| 32 | Barcelona International Airport |  | ES | 539 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 534 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 525 |
| 35 | Vitoria/Foronda Airport |  | ES | 510 |
| 36 | Don Mueang International Airport |  | TH | 508 |
| 37 | Amsterdam Airport Schiphol |  | NL | 505 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 500 |
| 39 | O. R. Tambo International Airport |  | ZA | 485 |
| 40 | Calgary International Airport |  | CA | 472 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 378 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 288 | 21m | 244 km | 1,212.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 216 | 1h 27m | 910 km | 3,389.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 203 | 9m | - | - |
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
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 108 | 1h 2m | 695 km | 1,294.6 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 108 | 57m | 493 km | 918.8 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 102 | 18m | 144 km | 253.7 t |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N580W |  | Commerce Municipal Airport (K2F7) | Commerce Municipal Airport (K2F7) | 2026-05-13 15:17 UTC | 2026-05-13 15:48 UTC | 31m |
| PAWS02 | PAW | Enid Woodring Regional Airport (KWDG) | Tulsa Riverside Airport (KRVS) | 2026-05-13 15:23 UTC | 2026-05-13 15:44 UTC | 21m |
| VLG4WQ | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-05-13 14:38 UTC | 2026-05-13 15:44 UTC | 1h 6m |
| RTV2L | RTV | Vilar Da Luz Airport (LPVL) | Braga Municipal Aerodrome (LPBR) | 2026-05-13 15:20 UTC | 2026-05-13 15:36 UTC | 15m |
| N212BS |  | Corpora Airport (1TE5) | Varisco Airport (13TE) | 2026-05-13 15:29 UTC | 2026-05-13 15:34 UTC | 5m |
| LXJ428 | LXJ | Scottsdale Airport (KSDL) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-13 13:57 UTC | 2026-05-13 15:33 UTC | 1h 36m |
| N358EA |  | Glendale Regional Airport (KGEU) | AZ00 (AZ00) | 2026-05-13 14:15 UTC | 2026-05-13 15:29 UTC | 1h 14m |
| N24155 |  | Guthrie/Edmond Regional Airport (KGOK) | 6OK0 (6OK0) | 2026-05-13 13:52 UTC | 2026-05-13 15:29 UTC | 1h 36m |
| UAL2609 | United Airlines | Okc Will Rogers International Airport (KOKC) | Denver International Airport (KDEN) | 2026-05-13 14:10 UTC | 2026-05-13 15:29 UTC | 1h 18m |
| BKN75 | BKN | St Louis Downtown Airport (KCPS) | St Louis Downtown Airport (KCPS) | 2026-05-13 15:26 UTC | 2026-05-13 15:26 UTC | 0m |
| MFRSH | MFR | Alzate Brianza Airport (LILB) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-13 14:15 UTC | 2026-05-13 15:25 UTC | 1h 10m |
| UAL1765 | United Airlines | Pittsburgh International Airport (KPIT) | Denver International Airport (KDEN) | 2026-05-13 12:28 UTC | 2026-05-13 15:24 UTC | 2h 56m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-05-13 13:50 UTC | 2026-05-13 15:23 UTC | 1h 33m |
| IGO24AH | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-13 15:12 UTC | 2026-05-13 15:22 UTC | 10m |
| RNGR763 | RNG | Mustang Beach Airport (KRAS) | Mustang Beach Airport (KRAS) | 2026-05-13 14:53 UTC | 2026-05-13 15:22 UTC | 28m |
| N602TA |  | Wexford Landing Airport (4SC7) | Wexford Landing Airport (4SC7) | 2026-05-13 14:58 UTC | 2026-05-13 15:16 UTC | 18m |
| N80135 |  | Airlake Airport (KLVN) | Airlake Airport (KLVN) | 2026-05-13 15:04 UTC | 2026-05-13 15:14 UTC | 10m |
| JFA21V | JFA | Paris-Le Bourget Airport (LFPB) | Lannion-Cote de Granit Airport (LFRO) | 2026-05-13 14:23 UTC | 2026-05-13 15:14 UTC | 50m |
| N459TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-05-13 14:49 UTC | 2026-05-13 15:12 UTC | 22m |
| PAG907T | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Erickson Municipal Airport (CKQ6) | 2026-05-13 14:31 UTC | 2026-05-13 15:11 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
