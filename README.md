# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_17:20:49_UTC-green)

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

**Latest saved flight:** 2026-05-20 17:20:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-20 17:20:49 UTC

- **89,155** saved flights
- **31,828** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,155** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,104,085.3 tonnes** estimated CO2 emissions
- **64,004,944 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3826 |
| 2 | SkyWest Airlines | 3304 |
| 3 | IndiGo | 1886 |
| 4 | EJA | 1685 |
| 5 | American Airlines | 1363 |
| 6 | Southwest Airlines | 1294 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1100 |
| 9 | Delta Air Lines | 976 |
| 10 | Vueling | 851 |
| 11 | LATAM Airlines | 802 |
| 12 | AXM | 790 |
| 13 | WIF | 771 |
| 14 | AZU | 707 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 671 |
| 17 | LXJ | 659 |
| 18 | QLK | 632 |
| 19 | Alaska Airlines | 630 |
| 20 | easyJet | 587 |
| 21 | Cathay Pacific | 574 |
| 22 | EJU | 574 |
| 23 | AEE | 551 |
| 24 | VIV | 533 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 467 |
| 28 | AXB | 459 |
| 29 | MXY | 455 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73257 |
| 2 | 🇪🇸 ES | 6333 |
| 3 | 🇮🇳 IN | 5913 |
| 4 | 🇦🇺 AU | 5553 |
| 5 | 🇩🇪 DE | 4948 |
| 6 | 🇮🇹 IT | 4938 |
| 7 | 🇧🇷 BR | 4897 |
| 8 | 🇨🇦 CA | 4459 |
| 9 | 🇯🇵 JP | 4367 |
| 10 | 🇬🇧 GB | 3808 |
| 11 | 🇫🇷 FR | 3586 |
| 12 | 🇨🇴 CO | 3055 |
| 13 | 🇲🇽 MX | 2765 |
| 14 | 🇬🇷 GR | 2576 |
| 15 | 🇳🇴 NO | 2475 |
| 16 | 🇨🇭 CH | 2354 |
| 17 | 🇲🇾 MY | 1984 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1625 |
| 20 | 🇳🇿 NZ | 1536 |
| 21 | 🇹🇭 TH | 1523 |
| 22 | 🇵🇱 PL | 1478 |
| 23 | 🇰🇷 KR | 1384 |
| 24 | 🇵🇭 PH | 1368 |
| 25 | 🇬🇹 GT | 1334 |
| 26 | 🇲🇴 MO | 1031 |
| 27 | 🇲🇦 MA | 1028 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 906 |
| 30 | 🇭🇷 HR | 806 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1947 |
| 2 | Denver International Airport |  | US | 1493 |
| 3 | Tokyo International Airport |  | JP | 1456 |
| 4 | Indira Gandhi International Airport |  | IN | 1277 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1213 |
| 6 | Harry Reid International Airport |  | US | 1137 |
| 7 | Frankfurt am Main International Airport |  | DE | 1124 |
| 8 | Zurich Airport |  | CH | 1065 |
| 9 | Guaymaral Airport |  | CO | 1045 |
| 10 | Macau International Airport |  | MO | 1031 |
| 11 | La Aurora Airport |  | GT | 1014 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 986 |
| 13 | El Dorado International Airport |  | CO | 971 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 908 |
| 15 | Chicago O'Hare International Airport |  | US | 859 |
| 16 | Madrid Barajas International Airport |  | ES | 810 |
| 17 | Kuala Lumpur International Airport |  | MY | 786 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 765 |
| 19 | Capua Airport |  | IT | 757 |
| 20 | Salt Lake City International Airport |  | US | 745 |
| 21 | Malpensa International Airport |  | IT | 725 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 723 |
| 23 | Bengaluru International Airport |  | IN | 711 |
| 24 | Charles de Gaulle International Airport |  | FR | 697 |
| 25 | Congonhas Airport |  | BR | 685 |
| 26 | Charlotte/Douglas International Airport |  | US | 684 |
| 27 | Daniel K Inouye International Airport |  | US | 652 |
| 28 | Tenerife Norte Airport |  | ES | 652 |
| 29 | Ninoy Aquino International Airport |  | PH | 628 |
| 30 | Barcelona International Airport |  | ES | 601 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 598 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 587 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 563 |
| 37 | Amsterdam Airport Schiphol |  | NL | 556 |
| 38 | Don Mueang International Airport |  | TH | 555 |
| 39 | Calgary International Airport |  | CA | 530 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 428 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 331 | 21m | 244 km | 1,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 244 | 24m | 225 km | 946.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 231 | 14m | 114 km | 453.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 228 | 28m | 304 km | 1,195.2 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 227 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 204 | 1h 10m | 770 km | 2,710.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 128 | 23m | 55 km | 121.7 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 126 | 14m | 154 km | 333.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 115 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 115 | 18m | 144 km | 286.1 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 108 | 1h 18m | 961 km | 1,790.2 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 6WHEM |  | Blaise Diagne International Airport (GOBD) | Leopold Sedar Senghor International Airport (GOOY) | 2026-05-20 16:57 UTC | 2026-05-20 17:20 UTC | 22m |
| N853MH |  | Long Beach (Daugherty Field) Airport (KLGB) | Catalina Airport (KAVX) | 2026-05-20 17:05 UTC | 2026-05-20 17:20 UTC | 14m |
| N711NF |  | Pensacola International Airport (KPNS) | Williamson Farm Airport (AL97) | 2026-05-20 16:51 UTC | 2026-05-20 17:17 UTC | 26m |
| RN101 |  | 49FL (49FL) | Atmore Municipal Airport (K0R1) | 2026-05-20 16:59 UTC | 2026-05-20 17:14 UTC | 15m |
| VAR657 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-20 16:14 UTC | 2026-05-20 17:14 UTC | 1h 0m |
| N89LF |  | Spicewood Airport (K88R) | Austin Executive Airport (KEDC) | 2026-05-20 16:46 UTC | 2026-05-20 17:13 UTC | 26m |
| CLY285 | CLY | Oxford (Kidlington) Airport (EGTK) | Bournemouth Airport (EGHH) | 2026-05-20 16:47 UTC | 2026-05-20 17:10 UTC | 23m |
| N331RF |  | Leoville Airport (CJT9) | Leoville Airport (CJT9) | 2026-05-20 16:44 UTC | 2026-05-20 17:10 UTC | 25m |
| 9HFAE |  | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-05-20 16:05 UTC | 2026-05-20 17:07 UTC | 1h 2m |
| RVP241 | RVP | Ponte de Sôr Airport (LPSO) | Viseu Airport (LPVZ) | 2026-05-20 16:12 UTC | 2026-05-20 17:05 UTC | 52m |
| N229CJ |  | Westchester County Airport (KHPN) | Lincoln Airport (KLNK) | 2026-05-20 14:05 UTC | 2026-05-20 17:04 UTC | 2h 58m |
| N5767G |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-05-20 16:52 UTC | 2026-05-20 17:03 UTC | 11m |
| N918CA |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-05-20 16:47 UTC | 2026-05-20 17:03 UTC | 15m |
| SIS94 | SIS | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-05-20 16:39 UTC | 2026-05-20 17:01 UTC | 21m |
| N581RS |  | Fulton County Executive/Charlie Brown Field (KFTY) | Piney Creek Airport (88TN) | 2026-05-20 16:39 UTC | 2026-05-20 17:00 UTC | 21m |
| N447RM |  | Billings Logan International Airport (KBIL) | Fort Smith Landing Strip (K5U7) | 2026-05-20 16:42 UTC | 2026-05-20 17:00 UTC | 18m |
| WCP645 | WCP | Treasure Coast International Airport (KFPR) | Baggett Airport (FD57) | 2026-05-20 16:56 UTC | 2026-05-20 16:59 UTC | 2m |
| N499DR |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-20 16:38 UTC | 2026-05-20 16:57 UTC | 19m |
| VJH357 | VJH | London City Airport (EGLC) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-20 15:21 UTC | 2026-05-20 16:57 UTC | 1h 35m |
| MANLY11 | MAN | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-05-20 16:36 UTC | 2026-05-20 16:52 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
