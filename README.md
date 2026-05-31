# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_15:39:42_UTC-green)

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

**Latest saved flight:** 2026-05-31 15:39:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 15:39:42 UTC

- **99,203** saved flights
- **35,295** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **99,203** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,216,444.8 tonnes** estimated CO2 emissions
- **70,518,537 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4125 |
| 2 | SkyWest Airlines | 3697 |
| 3 | IndiGo | 2019 |
| 4 | EJA | 1876 |
| 5 | American Airlines | 1603 |
| 6 | Southwest Airlines | 1492 |
| 7 | ENY | 1225 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1164 |
| 10 | Vueling | 930 |
| 11 | LATAM Airlines | 882 |
| 12 | WIF | 871 |
| 13 | AXM | 858 |
| 14 | AZU | 801 |
| 15 | LXJ | 748 |
| 16 | Swiss International | 730 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 695 |
| 19 | QLK | 674 |
| 20 | easyJet | 648 |
| 21 | EJU | 626 |
| 22 | Cathay Pacific | 593 |
| 23 | AEE | 588 |
| 24 | Air France | 577 |
| 25 | VIV | 577 |
| 26 | United Airlines | 555 |
| 27 | CXK | 530 |
| 28 | MXY | 529 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 494 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 82745 |
| 2 | 🇪🇸 ES | 6905 |
| 3 | 🇮🇳 IN | 6371 |
| 4 | 🇦🇺 AU | 5992 |
| 5 | 🇧🇷 BR | 5433 |
| 6 | 🇩🇪 DE | 5414 |
| 7 | 🇮🇹 IT | 5312 |
| 8 | 🇨🇦 CA | 5080 |
| 9 | 🇯🇵 JP | 4637 |
| 10 | 🇬🇧 GB | 4235 |
| 11 | 🇫🇷 FR | 3986 |
| 12 | 🇨🇴 CO | 3449 |
| 13 | 🇲🇽 MX | 3025 |
| 14 | 🇬🇷 GR | 2852 |
| 15 | 🇳🇴 NO | 2768 |
| 16 | 🇨🇭 CH | 2580 |
| 17 | 🇲🇾 MY | 2185 |
| 18 | 🇹🇷 TR | 1884 |
| 19 | 🇿🇦 ZA | 1747 |
| 20 | 🇳🇿 NZ | 1667 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇰🇷 KR | 1601 |
| 23 | 🇵🇱 PL | 1599 |
| 24 | 🇬🇹 GT | 1475 |
| 25 | 🇵🇭 PH | 1459 |
| 26 | 🇲🇦 MA | 1112 |
| 27 | 🇲🇴 MO | 1051 |
| 28 | 🇳🇱 NL | 998 |
| 29 | 🇲🇪 ME | 957 |
| 30 | 🇭🇷 HR | 885 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2156 |
| 2 | Denver International Airport |  | US | 1693 |
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1383 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1288 |
| 6 | Harry Reid International Airport |  | US | 1266 |
| 7 | Guaymaral Airport |  | CO | 1244 |
| 8 | Frankfurt am Main International Airport |  | DE | 1177 |
| 9 | Zurich Airport |  | CH | 1146 |
| 10 | La Aurora Airport |  | GT | 1134 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1068 |
| 12 | El Dorado International Airport |  | CO | 1061 |
| 13 | Macau International Airport |  | MO | 1051 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1005 |
| 15 | Chicago O'Hare International Airport |  | US | 990 |
| 16 | Madrid Barajas International Airport |  | ES | 872 |
| 17 | Kuala Lumpur International Airport |  | MY | 863 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 854 |
| 19 | Salt Lake City International Airport |  | US | 839 |
| 20 | Capua Airport |  | IT | 820 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 767 |
| 23 | Charles de Gaulle International Airport |  | FR | 766 |
| 24 | Malpensa International Airport |  | IT | 764 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 753 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 690 |
| 29 | Ninoy Aquino International Airport |  | PH | 666 |
| 30 | Barcelona International Airport |  | ES | 659 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 654 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 648 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 632 |
| 34 | Amsterdam Airport Schiphol |  | NL | 615 |
| 35 | Vitoria/Foronda Airport |  | ES | 608 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 583 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | Seattle-Tacoma International Airport |  | US | 563 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 515 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 266 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 252 | 14m | 114 km | 494.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 147 | 27m | 215 km | 544.4 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 127 | 18m | 144 km | 315.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 118 | 1h 43m | 1,423 km | 2,895.9 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N351LA |  | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | Virginia Tech/Montgomery Executive Airport (KBCB) | 2026-05-31 15:18 UTC | 2026-05-31 15:39 UTC | 21m |
| SAMU38 | SAM | St Etienne En Devoluy Airport (LFNY) | Grenoble Le Versoud Airport (LFLG) | 2026-05-31 15:22 UTC | 2026-05-31 15:34 UTC | 11m |
| MTU63 | MTU | Murfreesboro Municipal Airport (KMBT) | Long Meadow Airstrip (TN65) | 2026-05-31 15:17 UTC | 2026-05-31 15:34 UTC | 16m |
| HK5309G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-31 15:02 UTC | 2026-05-31 15:26 UTC | 23m |
| N475RC |  | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-05-31 15:00 UTC | 2026-05-31 15:22 UTC | 22m |
| OXF3373 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-05-31 13:56 UTC | 2026-05-31 15:22 UTC | 1h 25m |
| N492LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-31 14:21 UTC | 2026-05-31 15:21 UTC | 59m |
| N58DE |  | Aero Country Airport (KT31) | Baylie Airport (66XS) | 2026-05-31 15:14 UTC | 2026-05-31 15:20 UTC | 5m |
| THY5EC | Turkish Airlines | Istanbul Airport (LTFM) | Houari Boumediene Airport (DAAG) | 2026-05-31 12:19 UTC | 2026-05-31 15:17 UTC | 2h 58m |
| N310MA |  | St Louis Downtown Airport (KCPS) | IL18 (IL18) | 2026-05-31 14:44 UTC | 2026-05-31 15:16 UTC | 31m |
| N43813 |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-05-31 14:40 UTC | 2026-05-31 15:14 UTC | 33m |
| N31734 |  | Bugs Airport (PA68) | Pocono Mountains Regional Airport (KMPO) | 2026-05-31 14:55 UTC | 2026-05-31 15:10 UTC | 14m |
| DEAPR | DEA | Lubeck Blankensee Airport (EDHL) | Lubeck Blankensee Airport (EDHL) | 2026-05-31 14:57 UTC | 2026-05-31 15:09 UTC | 12m |
| CAP543 | CAP | Fremont County Airport (K1V6) | Fremont County Airport (K1V6) | 2026-05-31 14:40 UTC | 2026-05-31 15:09 UTC | 28m |
| CAP3522 | CAP | Tulsa International Airport (KTUL) | 84OL (84OL) | 2026-05-31 15:00 UTC | 2026-05-31 15:05 UTC | 4m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-05-31 14:31 UTC | 2026-05-31 15:04 UTC | 33m |
| LJC5 | LJC | Linate Airport (LIML) | Guernsey Airport (EGJB) | 2026-05-31 13:23 UTC | 2026-05-31 15:04 UTC | 1h 40m |
| 3AMAX |  | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-31 14:40 UTC | 2026-05-31 15:01 UTC | 20m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-05-31 14:42 UTC | 2026-05-31 14:57 UTC | 15m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-05-31 14:29 UTC | 2026-05-31 14:57 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
