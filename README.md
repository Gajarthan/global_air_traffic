# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_13:43:34_UTC-green)

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

**Latest saved flight:** 2026-05-24 13:43:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 13:43:34 UTC

- **93,815** saved flights
- **33,140** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,815** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,154,212.7 tonnes** estimated CO2 emissions
- **66,910,879 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3959 |
| 2 | SkyWest Airlines | 3474 |
| 3 | IndiGo | 1950 |
| 4 | EJA | 1772 |
| 5 | American Airlines | 1423 |
| 6 | Southwest Airlines | 1357 |
| 7 | ENY | 1159 |
| 8 | Lufthansa | 1135 |
| 9 | Delta Air Lines | 1026 |
| 10 | Vueling | 890 |
| 11 | LATAM Airlines | 843 |
| 12 | AXM | 835 |
| 13 | WIF | 816 |
| 14 | AZU | 748 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 705 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 650 |
| 20 | easyJet | 612 |
| 21 | EJU | 605 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 566 |
| 24 | Air France | 555 |
| 25 | VIV | 555 |
| 26 | CXK | 502 |
| 27 | MXY | 495 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77404 |
| 2 | 🇪🇸 ES | 6582 |
| 3 | 🇮🇳 IN | 6162 |
| 4 | 🇦🇺 AU | 5748 |
| 5 | 🇩🇪 DE | 5168 |
| 6 | 🇧🇷 BR | 5146 |
| 7 | 🇮🇹 IT | 5087 |
| 8 | 🇨🇦 CA | 4738 |
| 9 | 🇯🇵 JP | 4524 |
| 10 | 🇬🇧 GB | 4008 |
| 11 | 🇫🇷 FR | 3795 |
| 12 | 🇨🇴 CO | 3262 |
| 13 | 🇲🇽 MX | 2877 |
| 14 | 🇬🇷 GR | 2699 |
| 15 | 🇳🇴 NO | 2608 |
| 16 | 🇨🇭 CH | 2474 |
| 17 | 🇲🇾 MY | 2110 |
| 18 | 🇹🇷 TR | 1733 |
| 19 | 🇿🇦 ZA | 1701 |
| 20 | 🇹🇭 TH | 1595 |
| 21 | 🇳🇿 NZ | 1594 |
| 22 | 🇵🇱 PL | 1543 |
| 23 | 🇰🇷 KR | 1515 |
| 24 | 🇵🇭 PH | 1420 |
| 25 | 🇬🇹 GT | 1412 |
| 26 | 🇲🇦 MA | 1075 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 942 |
| 29 | 🇲🇪 ME | 936 |
| 30 | 🇭🇷 HR | 853 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2030 |
| 2 | Denver International Airport |  | US | 1579 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1342 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1246 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1149 |
| 8 | Guaymaral Airport |  | CO | 1136 |
| 9 | Zurich Airport |  | CH | 1099 |
| 10 | La Aurora Airport |  | GT | 1079 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1026 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1023 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 936 |
| 15 | Chicago O'Hare International Airport |  | US | 894 |
| 16 | Madrid Barajas International Airport |  | ES | 839 |
| 17 | Kuala Lumpur International Airport |  | MY | 837 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 789 |
| 19 | Salt Lake City International Airport |  | US | 787 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 747 |
| 22 | Malpensa International Airport |  | IT | 743 |
| 23 | Bengaluru International Airport |  | IN | 738 |
| 24 | Charles de Gaulle International Airport |  | FR | 736 |
| 25 | Charlotte/Douglas International Airport |  | US | 714 |
| 26 | Congonhas Airport |  | BR | 712 |
| 27 | Daniel K Inouye International Airport |  | US | 674 |
| 28 | Tenerife Norte Airport |  | ES | 665 |
| 29 | Ninoy Aquino International Airport |  | PH | 649 |
| 30 | Barcelona International Airport |  | ES | 629 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 625 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 611 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 601 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 35 | Vitoria/Foronda Airport |  | ES | 585 |
| 36 | Don Mueang International Airport |  | TH | 584 |
| 37 | Amsterdam Airport Schiphol |  | NL | 580 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 539 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 466 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 140 | 27m | 215 km | 518.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 121 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 116 | 1h 40m | 1,156 km | 2,314.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEEAX | DEE | Frankfurt-Egelsbach Airport (EDFE) | Mainz-Finthen Airport (EDFZ) | 2026-05-24 13:23 UTC | 2026-05-24 13:43 UTC | 19m |
| ETD96B | Etihad Airways | Eleftherios Venizelos International Airport (LGAV) | Queen Alia International Airport (OJAI) | 2026-05-24 12:12 UTC | 2026-05-24 13:43 UTC | 1h 31m |
| SCU3 | SCU | Pheasant Wings Airport (26OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-05-24 13:07 UTC | 2026-05-24 13:28 UTC | 20m |
| PGT1891 | PGT | Ercan International Airport (LCEN) | Queen Alia International Airport (OJAI) | 2026-05-24 11:19 UTC | 2026-05-24 13:27 UTC | 2h 7m |
| SWR9PX | Swiss International | Zurich Airport (LSZH) | Stockholm-Arlanda Airport (ESSA) | 2026-05-24 11:13 UTC | 2026-05-24 13:26 UTC | 2h 12m |
| N28433 |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-05-24 13:08 UTC | 2026-05-24 13:21 UTC | 13m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-24 12:43 UTC | 2026-05-24 13:20 UTC | 36m |
| HBZNH | HBZ | St Stephan Airport (LSTS) | Raron Airport (LSTA) | 2026-05-24 12:52 UTC | 2026-05-24 13:17 UTC | 24m |
| CXK198 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-05-24 11:52 UTC | 2026-05-24 13:10 UTC | 1h 17m |
| N356KF |  | Symms Airport (08ID) | Reek Ranch Airport (ID63) | 2026-05-24 12:49 UTC | 2026-05-24 13:10 UTC | 21m |
| ETD3XA | Etihad Airways | Dublin Airport (EIDW) | Queen Alia International Airport (OJAI) | 2026-05-24 08:42 UTC | 2026-05-24 13:09 UTC | 4h 27m |
| N513P |  | Laurence G Hanscom Field (KBED) | Laurence G Hanscom Field (KBED) | 2026-05-24 12:53 UTC | 2026-05-24 13:08 UTC | 15m |
| OKEUI15 | OKE | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-05-24 12:59 UTC | 2026-05-24 13:08 UTC | 9m |
| FNA570 | FNA | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-05-24 12:46 UTC | 2026-05-24 13:08 UTC | 22m |
| N282AM |  | Houston Executive Airport (KTME) | Head Airfield (2AR7) | 2026-05-24 12:02 UTC | 2026-05-24 13:06 UTC | 1h 4m |
| ELY358 | ELY | Frankfurt am Main International Airport (EDDF) | Queen Alia International Airport (OJAI) | 2026-05-24 09:38 UTC | 2026-05-24 13:05 UTC | 3h 26m |
| ISR887 | ISR | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-24 12:32 UTC | 2026-05-24 13:04 UTC | 31m |
| DKHIB | DKH | Altenstadt Army Airfield (ETHA) | Zell Am See Airport (LOWZ) | 2026-05-24 10:16 UTC | 2026-05-24 13:03 UTC | 2h 47m |
| HB2471 |  | Samedan Airport (LSZS) | Samedan Airport (LSZS) | 2026-05-24 12:02 UTC | 2026-05-24 13:02 UTC | 59m |
| ETD9XU | Etihad Airways | Manchester Airport (EGCC) | Queen Alia International Airport (OJAI) | 2026-05-24 08:46 UTC | 2026-05-24 13:00 UTC | 4h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
