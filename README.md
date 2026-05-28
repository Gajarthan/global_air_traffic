# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_18:57:36_UTC-green)

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

**Latest saved flight:** 2026-05-28 18:57:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-28 18:57:36 UTC

- **95,994** saved flights
- **33,775** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,994** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,177,524.7 tonnes** estimated CO2 emissions
- **68,262,299 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4035 |
| 2 | SkyWest Airlines | 3571 |
| 3 | IndiGo | 1988 |
| 4 | EJA | 1812 |
| 5 | American Airlines | 1452 |
| 6 | Southwest Airlines | 1396 |
| 7 | ENY | 1183 |
| 8 | Lufthansa | 1150 |
| 9 | Delta Air Lines | 1051 |
| 10 | Vueling | 910 |
| 11 | LATAM Airlines | 862 |
| 12 | AXM | 848 |
| 13 | WIF | 846 |
| 14 | AZU | 771 |
| 15 | LXJ | 732 |
| 16 | Swiss International | 716 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 666 |
| 19 | QLK | 663 |
| 20 | easyJet | 632 |
| 21 | EJU | 613 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 579 |
| 24 | Air France | 566 |
| 25 | VIV | 565 |
| 26 | CXK | 514 |
| 27 | MXY | 509 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 485 |
| 30 | AIQ | 462 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79348 |
| 2 | 🇪🇸 ES | 6716 |
| 3 | 🇮🇳 IN | 6273 |
| 4 | 🇦🇺 AU | 5880 |
| 5 | 🇧🇷 BR | 5270 |
| 6 | 🇩🇪 DE | 5263 |
| 7 | 🇮🇹 IT | 5198 |
| 8 | 🇨🇦 CA | 4862 |
| 9 | 🇯🇵 JP | 4584 |
| 10 | 🇬🇧 GB | 4116 |
| 11 | 🇫🇷 FR | 3898 |
| 12 | 🇨🇴 CO | 3322 |
| 13 | 🇲🇽 MX | 2942 |
| 14 | 🇬🇷 GR | 2771 |
| 15 | 🇳🇴 NO | 2692 |
| 16 | 🇨🇭 CH | 2525 |
| 17 | 🇲🇾 MY | 2152 |
| 18 | 🇹🇷 TR | 1783 |
| 19 | 🇿🇦 ZA | 1723 |
| 20 | 🇳🇿 NZ | 1634 |
| 21 | 🇹🇭 TH | 1625 |
| 22 | 🇰🇷 KR | 1580 |
| 23 | 🇵🇱 PL | 1567 |
| 24 | 🇵🇭 PH | 1444 |
| 25 | 🇬🇹 GT | 1439 |
| 26 | 🇲🇦 MA | 1091 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 968 |
| 29 | 🇲🇪 ME | 946 |
| 30 | 🇭🇷 HR | 871 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2079 |
| 2 | Denver International Airport |  | US | 1627 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1358 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1270 |
| 6 | Harry Reid International Airport |  | US | 1238 |
| 7 | Guaymaral Airport |  | CO | 1172 |
| 8 | Frankfurt am Main International Airport |  | DE | 1160 |
| 9 | Zurich Airport |  | CH | 1121 |
| 10 | La Aurora Airport |  | GT | 1103 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1037 |
| 13 | El Dorado International Airport |  | CO | 1037 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 962 |
| 15 | Chicago O'Hare International Airport |  | US | 923 |
| 16 | Kuala Lumpur International Airport |  | MY | 853 |
| 17 | Madrid Barajas International Airport |  | ES | 851 |
| 18 | Salt Lake City International Airport |  | US | 810 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 808 |
| 20 | Capua Airport |  | IT | 796 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 763 |
| 22 | Malpensa International Airport |  | IT | 753 |
| 23 | Bengaluru International Airport |  | IN | 752 |
| 24 | Charles de Gaulle International Airport |  | FR | 748 |
| 25 | Congonhas Airport |  | BR | 731 |
| 26 | Charlotte/Douglas International Airport |  | US | 728 |
| 27 | Daniel K Inouye International Airport |  | US | 684 |
| 28 | Tenerife Norte Airport |  | ES | 681 |
| 29 | Ninoy Aquino International Airport |  | PH | 659 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 643 |
| 31 | Barcelona International Airport |  | ES | 643 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 621 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 614 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 596 |
| 36 | Vitoria/Foronda Airport |  | ES | 594 |
| 37 | Don Mueang International Airport |  | TH | 593 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 570 |
| 39 | Calgary International Airport |  | CA | 566 |
| 40 | O. R. Tambo International Airport |  | ZA | 548 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 482 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 354 | 21m | 244 km | 1,490.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 256 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 244 | 14m | 114 km | 478.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 240 | 28m | 304 km | 1,258.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 154 | 21m | 99 km | 263.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 138 | 27m | 152 km | 360.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 130 | 20m | 250 km | 561.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 121 | 1h 39m | 1,156 km | 2,413.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 52m | 1,304 km | 2,609.7 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1539E |  | Ramona Airport (KRNM) | Riverside Airport (KRAL) | 2026-05-28 18:19 UTC | 2026-05-28 18:57 UTC | 37m |
| 72301 |  | Franklin County State Airport (KFSO) | Franklin County State Airport (KFSO) | 2026-05-28 18:16 UTC | 2026-05-28 18:56 UTC | 39m |
| RPA4756 | Republic Airways | Raleigh-Durham International Airport (KRDU) | Chicago O'Hare International Airport (KORD) | 2026-05-28 17:06 UTC | 2026-05-28 18:55 UTC | 1h 49m |
| N82XL |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-05-28 18:38 UTC | 2026-05-28 18:52 UTC | 14m |
| N605BG |  | Ranchaero Airport (CL56) | Sacramento Mather Airport (KMHR) | 2026-05-28 17:53 UTC | 2026-05-28 18:42 UTC | 49m |
| N938GC |  | Jekyll Island Airport (K09J) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-28 17:49 UTC | 2026-05-28 18:35 UTC | 46m |
| N199TC |  | Genesee County Airport (KGVQ) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-28 18:12 UTC | 2026-05-28 18:30 UTC | 18m |
| N76091 |  | Corona Municipal Airport (KAJO) | Riverside Airport (KRAL) | 2026-05-28 18:17 UTC | 2026-05-28 18:28 UTC | 10m |
| N996CS |  | Iowa City Municipal Airport (KIOW) | Ankeny Regional Airport (KIKV) | 2026-05-28 17:44 UTC | 2026-05-28 18:27 UTC | 43m |
| BOE701 | BOE | Boeing Field/King County International Airport (KBFI) | Grant County International Airport (KMWH) | 2026-05-28 17:46 UTC | 2026-05-28 18:24 UTC | 37m |
| TOPCT35 | TOP | Antelope County Airport (K4V9) | Booth Ranch Airport (SD36) | 2026-05-28 17:03 UTC | 2026-05-28 18:22 UTC | 1h 18m |
| N883CA |  | Austin Executive Airport (KEDC) | Austin Executive Airport (KEDC) | 2026-05-28 18:16 UTC | 2026-05-28 18:22 UTC | 6m |
| CAP4539 | CAP | 99VA (99VA) | Farmville Regional Airport (KFVX) | 2026-05-28 18:06 UTC | 2026-05-28 18:22 UTC | 15m |
| N250CR |  | XA65 (XA65) | Tilghman Airport (97XS) | 2026-05-28 18:13 UTC | 2026-05-28 18:22 UTC | 9m |
| N948HC |  | Florala Municipal Airport (K0J4) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-05-28 17:14 UTC | 2026-05-28 18:20 UTC | 1h 6m |
| JTL801 | JTL | Westchester County Airport (KHPN) | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | 2026-05-28 17:27 UTC | 2026-05-28 18:20 UTC | 52m |
|  |  | Allan C Perkinson/Blackstone Army Air Field (KBKT) | Allan C Perkinson/Blackstone Army Air Field (KBKT) | 2026-05-28 18:19 UTC | 2026-05-28 18:19 UTC | 0m |
| N3514T |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-05-28 18:17 UTC | 2026-05-28 18:18 UTC | 0m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-05-28 17:37 UTC | 2026-05-28 18:15 UTC | 37m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-28 17:50 UTC | 2026-05-28 18:14 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
