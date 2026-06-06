# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_13:50:38_UTC-green)

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

**Latest saved flight:** 2026-06-06 13:50:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 13:50:38 UTC

- **103,827** saved flights
- **36,674** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,827** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,269,149.8 tonnes** estimated CO2 emissions
- **73,573,902 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4262 |
| 2 | SkyWest Airlines | 3898 |
| 3 | IndiGo | 2077 |
| 4 | EJA | 1983 |
| 5 | American Airlines | 1675 |
| 6 | Southwest Airlines | 1567 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1227 |
| 9 | Lufthansa | 1195 |
| 10 | Vueling | 962 |
| 11 | LATAM Airlines | 919 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 835 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 751 |
| 17 | All Nippon Airways | 733 |
| 18 | Alaska Airlines | 723 |
| 19 | QLK | 697 |
| 20 | easyJet | 672 |
| 21 | EJU | 649 |
| 22 | Cathay Pacific | 621 |
| 23 | AEE | 601 |
| 24 | Air France | 595 |
| 25 | VIV | 594 |
| 26 | United Airlines | 575 |
| 27 | MXY | 562 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 511 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87233 |
| 2 | 🇪🇸 ES | 7143 |
| 3 | 🇮🇳 IN | 6561 |
| 4 | 🇦🇺 AU | 6309 |
| 5 | 🇧🇷 BR | 5674 |
| 6 | 🇩🇪 DE | 5587 |
| 7 | 🇮🇹 IT | 5514 |
| 8 | 🇨🇦 CA | 5395 |
| 9 | 🇯🇵 JP | 4816 |
| 10 | 🇬🇧 GB | 4378 |
| 11 | 🇫🇷 FR | 4118 |
| 12 | 🇨🇴 CO | 3566 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2952 |
| 15 | 🇳🇴 NO | 2895 |
| 16 | 🇨🇭 CH | 2659 |
| 17 | 🇲🇾 MY | 2295 |
| 18 | 🇹🇷 TR | 1973 |
| 19 | 🇿🇦 ZA | 1802 |
| 20 | 🇳🇿 NZ | 1744 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1721 |
| 23 | 🇵🇱 PL | 1674 |
| 24 | 🇵🇭 PH | 1530 |
| 25 | 🇬🇹 GT | 1513 |
| 26 | 🇲🇦 MA | 1143 |
| 27 | 🇲🇴 MO | 1093 |
| 28 | 🇳🇱 NL | 1021 |
| 29 | 🇲🇪 ME | 985 |
| 30 | 🇭🇷 HR | 909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2255 |
| 2 | Denver International Airport |  | US | 1776 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1424 |
| 5 | Harry Reid International Airport |  | US | 1331 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1320 |
| 7 | Guaymaral Airport |  | CO | 1292 |
| 8 | Frankfurt am Main International Airport |  | DE | 1193 |
| 9 | Zurich Airport |  | CH | 1181 |
| 10 | La Aurora Airport |  | GT | 1164 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1121 |
| 12 | Macau International Airport |  | MO | 1093 |
| 13 | El Dorado International Airport |  | CO | 1092 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1051 |
| 15 | Chicago O'Hare International Airport |  | US | 1039 |
| 16 | Madrid Barajas International Airport |  | ES | 902 |
| 17 | Kuala Lumpur International Airport |  | MY | 899 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 865 |
| 21 | Charlotte/Douglas International Airport |  | US | 807 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 791 |
| 24 | Bengaluru International Airport |  | IN | 787 |
| 25 | Congonhas Airport |  | BR | 787 |
| 26 | Malpensa International Airport |  | IT | 780 |
| 27 | Daniel K Inouye International Airport |  | US | 713 |
| 28 | Tenerife Norte Airport |  | ES | 706 |
| 29 | Ninoy Aquino International Airport |  | PH | 698 |
| 30 | Barcelona International Airport |  | ES | 683 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 672 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 665 |
| 34 | Amsterdam Airport Schiphol |  | NL | 632 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 623 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 533 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 381 | 21m | 244 km | 1,604.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 260 | 14m | 114 km | 509.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 160 | 20m | 99 km | 274.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 135 | 18m | 144 km | 335.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 121 | 1h 43m | 1,423 km | 2,969.5 t |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N928GP |  | Rabb Dusting Inc Airport (XS66) | Cabaniss Field Nolf Airport (KNGW) | 2026-06-06 13:17 UTC | 2026-06-06 13:50 UTC | 33m |
| ANE2506 | ANE | Palma De Mallorca Airport (LEPA) | Palma De Mallorca Airport (LEPA) | 2026-06-06 13:28 UTC | 2026-06-06 13:48 UTC | 19m |
| AXY973W | AXY | Nice-Cote d'Azur Airport (LFMN) | Palma De Mallorca Airport (LEPA) | 2026-06-06 12:26 UTC | 2026-06-06 13:48 UTC | 1h 21m |
| SWT7887 | SWT | Palma De Mallorca Airport (LEPA) | Palma De Mallorca Airport (LEPA) | 2026-06-06 13:24 UTC | 2026-06-06 13:48 UTC | 23m |
| ERU319 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-06-06 13:21 UTC | 2026-06-06 13:47 UTC | 25m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-06 13:32 UTC | 2026-06-06 13:46 UTC | 13m |
| DEBPC | DEB | Munster Osnabruck Airport (EDDG) | Osnabruck-Atterheide Airport (EDWO) | 2026-06-06 13:29 UTC | 2026-06-06 13:42 UTC | 13m |
| N840CT |  | Jonesboro Municipal Airport (KJBR) | Jonesboro Municipal Airport (KJBR) | 2026-06-06 12:50 UTC | 2026-06-06 13:39 UTC | 48m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-06-06 13:22 UTC | 2026-06-06 13:35 UTC | 13m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-06-06 13:21 UTC | 2026-06-06 13:34 UTC | 12m |
| N800FV |  | 1AR0 (1AR0) | JAMI (JAMI) | 2026-06-06 13:14 UTC | 2026-06-06 13:30 UTC | 16m |
| N221V |  | Montezuma Airport (19AZ) | Montezuma Airport (19AZ) | 2026-06-06 13:04 UTC | 2026-06-06 13:29 UTC | 25m |
| N27BN |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Johnson County Airport (KBYG) | 2026-06-06 12:38 UTC | 2026-06-06 13:28 UTC | 50m |
| PNC0801 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-06 12:57 UTC | 2026-06-06 13:26 UTC | 29m |
| N7874N |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-06-06 12:36 UTC | 2026-06-06 13:26 UTC | 49m |
| PTGCR | PTG | Cascais Airport (LPCS) | Capua Airport (LIAU) | 2026-06-06 10:51 UTC | 2026-06-06 13:22 UTC | 2h 30m |
| EPI222 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-06-06 13:14 UTC | 2026-06-06 13:17 UTC | 3m |
| N55716 |  | Southbridge Municipal Airport (K3B0) | Southbridge Municipal Airport (K3B0) | 2026-06-06 12:47 UTC | 2026-06-06 13:17 UTC | 30m |
| N608UW |  | Thiessen Field (34WI) | Dane County Regional/Truax Field (KMSN) | 2026-06-06 13:02 UTC | 2026-06-06 13:16 UTC | 14m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-06-06 13:00 UTC | 2026-06-06 13:13 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
