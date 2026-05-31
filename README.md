# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_10:58:47_UTC-green)

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

**Latest saved flight:** 2026-05-31 10:58:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 10:58:47 UTC

- **99,039** saved flights
- **35,240** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **99,039** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,214,840.5 tonnes** estimated CO2 emissions
- **70,425,535 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4117 |
| 2 | SkyWest Airlines | 3694 |
| 3 | IndiGo | 2016 |
| 4 | EJA | 1874 |
| 5 | American Airlines | 1602 |
| 6 | Southwest Airlines | 1492 |
| 7 | ENY | 1221 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1163 |
| 10 | Vueling | 928 |
| 11 | LATAM Airlines | 879 |
| 12 | WIF | 868 |
| 13 | AXM | 858 |
| 14 | AZU | 799 |
| 15 | LXJ | 748 |
| 16 | Swiss International | 727 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 695 |
| 19 | QLK | 674 |
| 20 | easyJet | 647 |
| 21 | EJU | 624 |
| 22 | Cathay Pacific | 592 |
| 23 | AEE | 588 |
| 24 | VIV | 577 |
| 25 | Air France | 576 |
| 26 | United Airlines | 555 |
| 27 | CXK | 528 |
| 28 | MXY | 528 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 493 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 82603 |
| 2 | 🇪🇸 ES | 6887 |
| 3 | 🇮🇳 IN | 6365 |
| 4 | 🇦🇺 AU | 5992 |
| 5 | 🇧🇷 BR | 5420 |
| 6 | 🇩🇪 DE | 5407 |
| 7 | 🇮🇹 IT | 5302 |
| 8 | 🇨🇦 CA | 5073 |
| 9 | 🇯🇵 JP | 4636 |
| 10 | 🇬🇧 GB | 4227 |
| 11 | 🇫🇷 FR | 3970 |
| 12 | 🇨🇴 CO | 3441 |
| 13 | 🇲🇽 MX | 3023 |
| 14 | 🇬🇷 GR | 2850 |
| 15 | 🇳🇴 NO | 2757 |
| 16 | 🇨🇭 CH | 2575 |
| 17 | 🇲🇾 MY | 2185 |
| 18 | 🇹🇷 TR | 1877 |
| 19 | 🇿🇦 ZA | 1745 |
| 20 | 🇳🇿 NZ | 1667 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇰🇷 KR | 1601 |
| 23 | 🇵🇱 PL | 1597 |
| 24 | 🇬🇹 GT | 1470 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1111 |
| 27 | 🇲🇴 MO | 1050 |
| 28 | 🇳🇱 NL | 994 |
| 29 | 🇲🇪 ME | 957 |
| 30 | 🇭🇷 HR | 883 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2152 |
| 2 | Denver International Airport |  | US | 1692 |
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1382 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1288 |
| 6 | Harry Reid International Airport |  | US | 1266 |
| 7 | Guaymaral Airport |  | CO | 1238 |
| 8 | Frankfurt am Main International Airport |  | DE | 1177 |
| 9 | Zurich Airport |  | CH | 1142 |
| 10 | La Aurora Airport |  | GT | 1130 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1068 |
| 12 | El Dorado International Airport |  | CO | 1060 |
| 13 | Macau International Airport |  | MO | 1050 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1005 |
| 15 | Chicago O'Hare International Airport |  | US | 989 |
| 16 | Madrid Barajas International Airport |  | ES | 869 |
| 17 | Kuala Lumpur International Airport |  | MY | 863 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 854 |
| 19 | Salt Lake City International Airport |  | US | 838 |
| 20 | Capua Airport |  | IT | 819 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 765 |
| 23 | Malpensa International Airport |  | IT | 764 |
| 24 | Charles de Gaulle International Airport |  | FR | 764 |
| 25 | Bengaluru International Airport |  | IN | 762 |
| 26 | Congonhas Airport |  | BR | 749 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 689 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 658 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 653 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 647 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 630 |
| 34 | Amsterdam Airport Schiphol |  | NL | 611 |
| 35 | Vitoria/Foronda Airport |  | ES | 607 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 582 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | Seattle-Tacoma International Airport |  | US | 563 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 512 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 251 | 14m | 114 km | 492.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 196 | 26m | 275 km | 928.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 147 | 27m | 215 km | 544.4 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 127 | 18m | 144 km | 315.9 t |
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
| DFLIP | DFL | Skutec Airport (LKSK) | Skutec Airport (LKSK) | 2026-05-31 10:34 UTC | 2026-05-31 10:58 UTC | 23m |
| HB3384 |  | Gruyeres Airport (LSGT) | Bex Airport (LSGB) | 2026-05-31 09:39 UTC | 2026-05-31 10:47 UTC | 1h 8m |
| ANA534 | All Nippon Airways | Takamatsu Airport (RJOT) | Tokyo International Airport (RJTT) | 2026-05-31 00:33 UTC | 2026-05-31 10:47 UTC | 10h 13m |
| ICE2B | ICE | Washington Dulles International Airport (KIAD) | Brussels Airport (EBBR) | 2026-05-31 00:36 UTC | 2026-05-31 10:45 UTC | 10h 8m |
| CKS701 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-05-30 21:51 UTC | 2026-05-31 10:43 UTC | 12h 51m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-30 22:45 UTC | 2026-05-31 10:38 UTC | 11h 53m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-30 20:58 UTC | 2026-05-31 10:32 UTC | 13h 33m |
| JST888 | JST | Brisbane International Airport (YBBN) | Mackay Airport (YBMK) | 2026-05-31 09:00 UTC | 2026-05-31 10:17 UTC | 1h 17m |
| SAS816 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Marl Loemuhle Airport (EDLM) | 2026-05-31 08:33 UTC | 2026-05-31 10:10 UTC | 1h 37m |
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-05-31 09:59 UTC | 2026-05-31 10:09 UTC | 9m |
| AAL2100 | American Airlines | Avinger Field (SC87) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-31 01:11 UTC | 2026-05-31 10:09 UTC | 8h 58m |
| UAE9841 | Emirates | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-05-30 17:06 UTC | 2026-05-31 10:07 UTC | 17h 1m |
| OONEY | OON | Ostend-Bruges International Airport (EBOS) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-31 08:38 UTC | 2026-05-31 10:01 UTC | 1h 22m |
| BHA137 | BHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-05-31 09:14 UTC | 2026-05-31 10:00 UTC | 46m |
| ROT617X | ROT | Henri Coanda International Airport (LROP) | Tautii Magheraus Airport (LRBM) | 2026-05-31 09:02 UTC | 2026-05-31 09:59 UTC | 57m |
| IGO6917 | IndiGo | Barrackpore Air Force Station (VEPI) | Birsa Munda Airport (VERC) | 2026-05-31 09:26 UTC | 2026-05-31 09:57 UTC | 30m |
| NOZ372 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-05-31 08:38 UTC | 2026-05-31 09:56 UTC | 1h 18m |
| MXD2405 | MXD | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-31 09:34 UTC | 2026-05-31 09:56 UTC | 21m |
| AIQ634 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-31 00:58 UTC | 2026-05-31 09:56 UTC | 8h 58m |
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-05-31 09:12 UTC | 2026-05-31 09:55 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
