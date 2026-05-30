# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_18:56:20_UTC-green)

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

**Latest saved flight:** 2026-05-30 18:56:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 18:56:20 UTC

- **97,737** saved flights
- **34,347** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **97,737** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,195,828.8 tonnes** estimated CO2 emissions
- **69,323,410 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4102 |
| 2 | SkyWest Airlines | 3639 |
| 3 | IndiGo | 2008 |
| 4 | EJA | 1849 |
| 5 | American Airlines | 1479 |
| 6 | Southwest Airlines | 1415 |
| 7 | ENY | 1200 |
| 8 | Lufthansa | 1171 |
| 9 | Delta Air Lines | 1068 |
| 10 | Vueling | 925 |
| 11 | LATAM Airlines | 873 |
| 12 | WIF | 866 |
| 13 | AXM | 854 |
| 14 | AZU | 793 |
| 15 | LXJ | 744 |
| 16 | Swiss International | 726 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 676 |
| 19 | QLK | 669 |
| 20 | easyJet | 641 |
| 21 | EJU | 622 |
| 22 | Cathay Pacific | 587 |
| 23 | AEE | 586 |
| 24 | VIV | 575 |
| 25 | Air France | 574 |
| 26 | CXK | 526 |
| 27 | MXY | 516 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 492 |
| 30 | AIQ | 466 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 80934 |
| 2 | 🇪🇸 ES | 6844 |
| 3 | 🇮🇳 IN | 6341 |
| 4 | 🇦🇺 AU | 5928 |
| 5 | 🇧🇷 BR | 5388 |
| 6 | 🇩🇪 DE | 5382 |
| 7 | 🇮🇹 IT | 5282 |
| 8 | 🇨🇦 CA | 4967 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4196 |
| 11 | 🇫🇷 FR | 3957 |
| 12 | 🇨🇴 CO | 3423 |
| 13 | 🇲🇽 MX | 2997 |
| 14 | 🇬🇷 GR | 2829 |
| 15 | 🇳🇴 NO | 2746 |
| 16 | 🇨🇭 CH | 2568 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1836 |
| 19 | 🇿🇦 ZA | 1737 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1590 |
| 23 | 🇰🇷 KR | 1589 |
| 24 | 🇬🇹 GT | 1469 |
| 25 | 🇵🇭 PH | 1457 |
| 26 | 🇲🇦 MA | 1106 |
| 27 | 🇲🇴 MO | 1044 |
| 28 | 🇳🇱 NL | 991 |
| 29 | 🇲🇪 ME | 955 |
| 30 | 🇭🇷 HR | 881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2116 |
| 2 | Denver International Airport |  | US | 1651 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1375 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1286 |
| 6 | Harry Reid International Airport |  | US | 1251 |
| 7 | Guaymaral Airport |  | CO | 1230 |
| 8 | Frankfurt am Main International Airport |  | DE | 1174 |
| 9 | Zurich Airport |  | CH | 1141 |
| 10 | La Aurora Airport |  | GT | 1129 |
| 11 | El Dorado International Airport |  | CO | 1054 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1050 |
| 13 | Macau International Airport |  | MO | 1044 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 981 |
| 15 | Chicago O'Hare International Airport |  | US | 937 |
| 16 | Madrid Barajas International Airport |  | ES | 863 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 822 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 816 |
| 20 | Capua Airport |  | IT | 813 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 763 |
| 23 | Charles de Gaulle International Airport |  | FR | 759 |
| 24 | Bengaluru International Airport |  | IN | 759 |
| 25 | Congonhas Airport |  | BR | 745 |
| 26 | Charlotte/Douglas International Airport |  | US | 744 |
| 27 | Daniel K Inouye International Airport |  | US | 689 |
| 28 | Tenerife Norte Airport |  | ES | 685 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Barcelona International Airport |  | ES | 656 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 629 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 624 |
| 34 | Amsterdam Airport Schiphol |  | NL | 610 |
| 35 | Vitoria/Foronda Airport |  | ES | 603 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 578 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 554 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 509 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 359 | 21m | 244 km | 1,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 249 | 14m | 114 km | 488.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 194 | 26m | 275 km | 919.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 126 | 18m | 144 km | 313.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 117 | 1h 43m | 1,423 km | 2,871.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N226LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-05-30 17:51 UTC | 2026-05-30 18:56 UTC | 1h 5m |
| N49BP |  | West Papoose Lake Airpark (44AK) | Wasilla Airport (PAWS) | 2026-05-30 17:52 UTC | 2026-05-30 18:42 UTC | 49m |
| N436CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-05-30 17:38 UTC | 2026-05-30 18:35 UTC | 57m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Crystal Lakes Airport (25CO) | 2026-05-30 18:16 UTC | 2026-05-30 18:33 UTC | 16m |
| N32296 |  | SC08 (SC08) | Rock Hill/York County/Bryant Field (KUZA) | 2026-05-30 18:25 UTC | 2026-05-30 18:33 UTC | 7m |
| LFA690 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Executive Airport (KORL) | 2026-05-30 17:28 UTC | 2026-05-30 18:31 UTC | 1h 2m |
| CAP2750 | CAP | Sierraville Dearwater Airport (KO79) | CA38 (CA38) | 2026-05-30 18:15 UTC | 2026-05-30 18:29 UTC | 14m |
| N600NC |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-05-30 18:26 UTC | 2026-05-30 18:28 UTC | 2m |
| SCA88 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-05-30 17:48 UTC | 2026-05-30 18:25 UTC | 37m |
| LXJ477 | LXJ | Centennial Airport (KAPA) | Truckee-Tahoe Airport (KTRK) | 2026-05-30 16:38 UTC | 2026-05-30 18:25 UTC | 1h 46m |
| BRU8157 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-05-30 18:06 UTC | 2026-05-30 18:24 UTC | 17m |
| N248TV |  | Kissimmee Gateway Airport (KISM) | Mills Field (KK22) | 2026-05-30 16:12 UTC | 2026-05-30 18:23 UTC | 2h 10m |
| N814SS |  | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-05-30 18:12 UTC | 2026-05-30 18:22 UTC | 9m |
| N990WM |  | Oakland County International Airport (KPTK) | Tweed/New Haven Airport (KHVN) | 2026-05-30 17:01 UTC | 2026-05-30 18:22 UTC | 1h 21m |
| NTR701 | NTR | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-05-30 17:31 UTC | 2026-05-30 18:22 UTC | 50m |
| N912EH |  | Cable Airport (KCCB) | Southern California Logistics Airport (KVCV) | 2026-05-30 17:52 UTC | 2026-05-30 18:20 UTC | 28m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-05-30 17:38 UTC | 2026-05-30 18:19 UTC | 40m |
| N875DM |  | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Meadows Field (KBFL) | 2026-05-30 17:48 UTC | 2026-05-30 18:18 UTC | 29m |
| N9340Y |  | Buchanan Field (KCCR) | San Carlos Airport (KSQL) | 2026-05-30 17:49 UTC | 2026-05-30 18:17 UTC | 27m |
| N55928 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-05-30 17:37 UTC | 2026-05-30 18:16 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
