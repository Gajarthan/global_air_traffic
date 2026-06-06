# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_21:27:07_UTC-green)

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

**Latest saved flight:** 2026-06-06 21:27:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 21:27:07 UTC

- **104,742** saved flights
- **36,915** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,742** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,280,381.6 tonnes** estimated CO2 emissions
- **74,225,020 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4311 |
| 2 | SkyWest Airlines | 3948 |
| 3 | IndiGo | 2089 |
| 4 | EJA | 2002 |
| 5 | American Airlines | 1686 |
| 6 | Southwest Airlines | 1585 |
| 7 | ENY | 1315 |
| 8 | Delta Air Lines | 1241 |
| 9 | Lufthansa | 1202 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 924 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 840 |
| 15 | LXJ | 789 |
| 16 | Swiss International | 755 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 728 |
| 19 | QLK | 697 |
| 20 | easyJet | 682 |
| 21 | EJU | 657 |
| 22 | Cathay Pacific | 623 |
| 23 | AEE | 606 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 582 |
| 27 | MXY | 568 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88189 |
| 2 | 🇪🇸 ES | 7217 |
| 3 | 🇮🇳 IN | 6597 |
| 4 | 🇦🇺 AU | 6313 |
| 5 | 🇧🇷 BR | 5713 |
| 6 | 🇩🇪 DE | 5625 |
| 7 | 🇮🇹 IT | 5570 |
| 8 | 🇨🇦 CA | 5439 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4426 |
| 11 | 🇫🇷 FR | 4152 |
| 12 | 🇨🇴 CO | 3630 |
| 13 | 🇲🇽 MX | 3143 |
| 14 | 🇬🇷 GR | 2987 |
| 15 | 🇳🇴 NO | 2903 |
| 16 | 🇨🇭 CH | 2673 |
| 17 | 🇲🇾 MY | 2296 |
| 18 | 🇹🇷 TR | 1998 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1748 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1722 |
| 23 | 🇵🇱 PL | 1695 |
| 24 | 🇵🇭 PH | 1533 |
| 25 | 🇬🇹 GT | 1523 |
| 26 | 🇲🇦 MA | 1160 |
| 27 | 🇲🇴 MO | 1099 |
| 28 | 🇳🇱 NL | 1029 |
| 29 | 🇲🇪 ME | 996 |
| 30 | 🇭🇷 HR | 915 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2281 |
| 2 | Denver International Airport |  | US | 1797 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1433 |
| 5 | Harry Reid International Airport |  | US | 1341 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1330 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1185 |
| 10 | La Aurora Airport |  | GT | 1171 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1131 |
| 12 | El Dorado International Airport |  | CO | 1106 |
| 13 | Macau International Airport |  | MO | 1099 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1060 |
| 15 | Chicago O'Hare International Airport |  | US | 1052 |
| 16 | Madrid Barajas International Airport |  | ES | 916 |
| 17 | Kuala Lumpur International Airport |  | MY | 900 |
| 18 | Salt Lake City International Airport |  | US | 895 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 895 |
| 20 | Capua Airport |  | IT | 882 |
| 21 | Charlotte/Douglas International Airport |  | US | 814 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 798 |
| 24 | Congonhas Airport |  | BR | 794 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 785 |
| 27 | Daniel K Inouye International Airport |  | US | 718 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 701 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 680 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 678 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 670 |
| 34 | Amsterdam Airport Schiphol |  | NL | 637 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 630 |
| 37 | Calgary International Airport |  | CA | 619 |
| 38 | Seattle-Tacoma International Airport |  | US | 606 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 603 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 598 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 386 | 21m | 244 km | 1,625.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 275 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 209 | 26m | 275 km | 990.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 136 | 18m | 144 km | 338.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-06-06 21:16 UTC | 2026-06-06 21:27 UTC | 11m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-06-06 21:11 UTC | 2026-06-06 21:26 UTC | 15m |
| N303RH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Palo Alto Airport (KPAO) | 2026-06-06 21:10 UTC | 2026-06-06 21:23 UTC | 12m |
| ENY3470 | ENY | John Glenn Columbus International Airport (KCMH) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-06 19:56 UTC | 2026-06-06 21:21 UTC | 1h 25m |
| N110SD |  | Coolidge Municipal Airport (KP08) | La Cholla Airpark (57AZ) | 2026-06-06 20:59 UTC | 2026-06-06 21:19 UTC | 20m |
| DLH8P | Lufthansa | Munich International Airport (EDDM) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-06 13:47 UTC | 2026-06-06 21:17 UTC | 7h 30m |
| TFB | TFB | Gold Coast Airport (YBCG) | Redcliffe Airport (YRED) | 2026-06-06 20:49 UTC | 2026-06-06 21:12 UTC | 23m |
| N607FJ |  | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-06-06 20:17 UTC | 2026-06-06 21:09 UTC | 52m |
| N125PM |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-06-06 20:36 UTC | 2026-06-06 21:07 UTC | 31m |
| N66KA |  | Wings Field (2TN2) | Wings Field (2TN2) | 2026-06-06 20:40 UTC | 2026-06-06 21:04 UTC | 23m |
| N782AZ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-06-06 20:53 UTC | 2026-06-06 20:54 UTC | 1m |
| N816RD |  | Rocky Mountain Metro Airport (KBJC) | Mertens Airport (3CO2) | 2026-06-06 19:58 UTC | 2026-06-06 20:54 UTC | 55m |
| HK778G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-06 20:35 UTC | 2026-06-06 20:53 UTC | 18m |
| SRG199 | SRG | Glasgow Prestwick Airport (EGPK) | Glasgow International Airport (EGPF) | 2026-06-06 20:33 UTC | 2026-06-06 20:53 UTC | 19m |
| N20521 |  | Immokalee Regional Airport (KIMM) | Immokalee Regional Airport (KIMM) | 2026-06-06 19:53 UTC | 2026-06-06 20:49 UTC | 55m |
| N24YP |  | Scottsdale Airport (KSDL) | 52NM (52NM) | 2026-06-06 19:58 UTC | 2026-06-06 20:49 UTC | 50m |
| QFA98 | Qantas | Ninoy Aquino International Airport (RPLL) | Brisbane International Airport (YBBN) | 2026-06-06 14:09 UTC | 2026-06-06 20:47 UTC | 6h 38m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-06 19:19 UTC | 2026-06-06 20:44 UTC | 1h 24m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-06-06 20:30 UTC | 2026-06-06 20:43 UTC | 12m |
| HK2659 |  | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 2026-06-06 20:28 UTC | 2026-06-06 20:42 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
