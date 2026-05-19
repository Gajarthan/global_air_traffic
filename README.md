# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_20:39:28_UTC-green)

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

**Latest saved flight:** 2026-05-19 20:39:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 20:39:28 UTC

- **88,506** saved flights
- **31,624** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,506** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,095,078.9 tonnes** estimated CO2 emissions
- **63,482,835 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3795 |
| 2 | SkyWest Airlines | 3282 |
| 3 | IndiGo | 1876 |
| 4 | EJA | 1676 |
| 5 | American Airlines | 1359 |
| 6 | Southwest Airlines | 1288 |
| 7 | Lufthansa | 1112 |
| 8 | ENY | 1095 |
| 9 | Delta Air Lines | 971 |
| 10 | Vueling | 846 |
| 11 | LATAM Airlines | 795 |
| 12 | AXM | 786 |
| 13 | WIF | 765 |
| 14 | AZU | 701 |
| 15 | Swiss International | 682 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 649 |
| 18 | Alaska Airlines | 626 |
| 19 | QLK | 626 |
| 20 | easyJet | 586 |
| 21 | EJU | 569 |
| 22 | Cathay Pacific | 563 |
| 23 | AEE | 547 |
| 24 | VIV | 531 |
| 25 | Air France | 519 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 466 |
| 28 | AXB | 458 |
| 29 | MXY | 452 |
| 30 | AIQ | 431 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72740 |
| 2 | 🇪🇸 ES | 6290 |
| 3 | 🇮🇳 IN | 5883 |
| 4 | 🇦🇺 AU | 5504 |
| 5 | 🇩🇪 DE | 4920 |
| 6 | 🇮🇹 IT | 4904 |
| 7 | 🇧🇷 BR | 4856 |
| 8 | 🇨🇦 CA | 4427 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3774 |
| 11 | 🇫🇷 FR | 3547 |
| 12 | 🇨🇴 CO | 3029 |
| 13 | 🇲🇽 MX | 2749 |
| 14 | 🇬🇷 GR | 2561 |
| 15 | 🇳🇴 NO | 2459 |
| 16 | 🇨🇭 CH | 2334 |
| 17 | 🇲🇾 MY | 1974 |
| 18 | 🇿🇦 ZA | 1637 |
| 19 | 🇹🇷 TR | 1603 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1519 |
| 22 | 🇵🇱 PL | 1471 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1357 |
| 25 | 🇬🇹 GT | 1330 |
| 26 | 🇲🇦 MA | 1023 |
| 27 | 🇲🇴 MO | 1021 |
| 28 | 🇲🇪 ME | 914 |
| 29 | 🇳🇱 NL | 899 |
| 30 | 🇭🇷 HR | 798 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1941 |
| 2 | Denver International Airport |  | US | 1484 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1269 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1210 |
| 6 | Harry Reid International Airport |  | US | 1128 |
| 7 | Frankfurt am Main International Airport |  | DE | 1119 |
| 8 | Zurich Airport |  | CH | 1055 |
| 9 | Guaymaral Airport |  | CO | 1037 |
| 10 | Macau International Airport |  | MO | 1021 |
| 11 | La Aurora Airport |  | GT | 1011 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 979 |
| 13 | El Dorado International Airport |  | CO | 963 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 902 |
| 15 | Chicago O'Hare International Airport |  | US | 857 |
| 16 | Madrid Barajas International Airport |  | ES | 805 |
| 17 | Kuala Lumpur International Airport |  | MY | 784 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 759 |
| 19 | Capua Airport |  | IT | 749 |
| 20 | Salt Lake City International Airport |  | US | 739 |
| 21 | Malpensa International Airport |  | IT | 725 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 708 |
| 24 | Charles de Gaulle International Airport |  | FR | 690 |
| 25 | Charlotte/Douglas International Airport |  | US | 683 |
| 26 | Congonhas Airport |  | BR | 677 |
| 27 | Daniel K Inouye International Airport |  | US | 649 |
| 28 | Tenerife Norte Airport |  | ES | 648 |
| 29 | Ninoy Aquino International Airport |  | PH | 622 |
| 30 | Barcelona International Airport |  | ES | 599 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 585 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 557 |
| 37 | Don Mueang International Airport |  | TH | 553 |
| 38 | Amsterdam Airport Schiphol |  | NL | 550 |
| 39 | Calgary International Airport |  | CA | 525 |
| 40 | O. R. Tambo International Airport |  | ZA | 518 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 425 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 330 | 21m | 244 km | 1,389.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 229 | 14m | 114 km | 449.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 226 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 129 | 27m | 215 km | 477.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 125 | 23m | 55 km | 118.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 114 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 000000 |  | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-05-19 20:06 UTC | 2026-05-19 20:39 UTC | 32m |
| N7725N |  | Athens Municipal Airport (KF44) | Athens Municipal Airport (KF44) | 2026-05-19 20:15 UTC | 2026-05-19 20:34 UTC | 19m |
| TAY8KN | TAY | Kaunas International Airport (EYKA) | Václav Havel Airport (LKPR) | 2026-05-19 18:08 UTC | 2026-05-19 20:34 UTC | 2h 26m |
| BXR800 | BXR | Red Bluff Municipal Airport (KRBL) | Red Bluff Municipal Airport (KRBL) | 2026-05-19 20:10 UTC | 2026-05-19 20:33 UTC | 23m |
| CFR72 | CFR | Palmdale Usaf Plant 42 Airport (KPMD) | San Bernardino International Airport (KSBD) | 2026-05-19 20:14 UTC | 2026-05-19 20:33 UTC | 19m |
| N187TC |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-05-19 20:00 UTC | 2026-05-19 20:32 UTC | 32m |
| N809CN |  | Frederick W Smith International Airport (KMEM) | Mobile International Airport (KBFM) | 2026-05-19 19:38 UTC | 2026-05-19 20:31 UTC | 52m |
| FHMZM | FHM | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-05-19 19:45 UTC | 2026-05-19 20:30 UTC | 45m |
| CFR89 | CFR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-05-19 20:17 UTC | 2026-05-19 20:30 UTC | 12m |
| T73 |  | Crystal Airport (46CN) | San Bernardino International Airport (KSBD) | 2026-05-19 20:07 UTC | 2026-05-19 20:29 UTC | 22m |
| N407JH |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-05-19 19:34 UTC | 2026-05-19 20:28 UTC | 54m |
| ARRIS10 | ARR | Trona Airport (KL72) | Boron Airstrip (57CL) | 2026-05-19 20:16 UTC | 2026-05-19 20:28 UTC | 11m |
| NIT444 | NIT | Lt Landing Airport (23GE) | W H 'Bud' Barron Airport (KDBN) | 2026-05-19 20:19 UTC | 2026-05-19 20:26 UTC | 7m |
| N737AF |  | Long Beach (Daugherty Field) Airport (KLGB) | Fullerton Municipal Airport (KFUL) | 2026-05-19 20:06 UTC | 2026-05-19 20:26 UTC | 19m |
| N976TR |  | Bradley International Airport (KBDL) | Hartford-Brainard Airport (KHFD) | 2026-05-19 18:59 UTC | 2026-05-19 20:25 UTC | 1h 25m |
| N112FS |  | Stockton Metro Airport (KSCK) | Tracy Municipal Airport (KTCY) | 2026-05-19 20:06 UTC | 2026-05-19 20:21 UTC | 15m |
| WAH | WAH | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-05-19 20:06 UTC | 2026-05-19 20:14 UTC | 7m |
| N2899J |  | Ted Stevens Anchorage International Airport (PANC) | Point Mac Airport (AK36) | 2026-05-19 19:34 UTC | 2026-05-19 20:12 UTC | 37m |
| N700DL |  | Allegheny County Airport (KAGC) | Washington County Airport (KAFJ) | 2026-05-19 19:51 UTC | 2026-05-19 20:10 UTC | 18m |
| N36BM |  | Tweed/New Haven Airport (KHVN) | Boeing Field/King County International Airport (KBFI) | 2026-05-19 15:16 UTC | 2026-05-19 20:09 UTC | 4h 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
