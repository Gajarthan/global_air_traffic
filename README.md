# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_07:03:22_UTC-green)

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

**Latest saved flight:** 2026-06-06 07:03:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 07:03:22 UTC

- **103,491** saved flights
- **36,593** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,491** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,264,875.9 tonnes** estimated CO2 emissions
- **73,326,142 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4242 |
| 2 | SkyWest Airlines | 3898 |
| 3 | IndiGo | 2065 |
| 4 | EJA | 1983 |
| 5 | American Airlines | 1675 |
| 6 | Southwest Airlines | 1566 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1226 |
| 9 | Lufthansa | 1193 |
| 10 | Vueling | 955 |
| 11 | LATAM Airlines | 916 |
| 12 | WIF | 907 |
| 13 | AXM | 891 |
| 14 | AZU | 830 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 744 |
| 17 | All Nippon Airways | 730 |
| 18 | Alaska Airlines | 723 |
| 19 | QLK | 697 |
| 20 | easyJet | 669 |
| 21 | EJU | 647 |
| 22 | Cathay Pacific | 620 |
| 23 | AEE | 601 |
| 24 | VIV | 594 |
| 25 | Air France | 590 |
| 26 | United Airlines | 574 |
| 27 | MXY | 560 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 516 |
| 30 | AXB | 507 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87151 |
| 2 | 🇪🇸 ES | 7097 |
| 3 | 🇮🇳 IN | 6519 |
| 4 | 🇦🇺 AU | 6308 |
| 5 | 🇧🇷 BR | 5650 |
| 6 | 🇩🇪 DE | 5552 |
| 7 | 🇮🇹 IT | 5479 |
| 8 | 🇨🇦 CA | 5390 |
| 9 | 🇯🇵 JP | 4784 |
| 10 | 🇬🇧 GB | 4351 |
| 11 | 🇫🇷 FR | 4096 |
| 12 | 🇨🇴 CO | 3553 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2940 |
| 15 | 🇳🇴 NO | 2874 |
| 16 | 🇨🇭 CH | 2643 |
| 17 | 🇲🇾 MY | 2278 |
| 18 | 🇹🇷 TR | 1958 |
| 19 | 🇿🇦 ZA | 1792 |
| 20 | 🇳🇿 NZ | 1742 |
| 21 | 🇹🇭 TH | 1711 |
| 22 | 🇰🇷 KR | 1702 |
| 23 | 🇵🇱 PL | 1651 |
| 24 | 🇵🇭 PH | 1526 |
| 25 | 🇬🇹 GT | 1509 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1092 |
| 28 | 🇳🇱 NL | 1018 |
| 29 | 🇲🇪 ME | 974 |
| 30 | 🇭🇷 HR | 906 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2255 |
| 2 | Denver International Airport |  | US | 1776 |
| 3 | Tokyo International Airport |  | JP | 1587 |
| 4 | Indira Gandhi International Airport |  | IN | 1414 |
| 5 | Harry Reid International Airport |  | US | 1331 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1318 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1193 |
| 9 | Zurich Airport |  | CH | 1173 |
| 10 | La Aurora Airport |  | GT | 1162 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1120 |
| 12 | Macau International Airport |  | MO | 1092 |
| 13 | El Dorado International Airport |  | CO | 1088 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1050 |
| 15 | Chicago O'Hare International Airport |  | US | 1038 |
| 16 | Madrid Barajas International Airport |  | ES | 900 |
| 17 | Kuala Lumpur International Airport |  | MY | 893 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 858 |
| 21 | Charlotte/Douglas International Airport |  | US | 807 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 785 |
| 24 | Congonhas Airport |  | BR | 785 |
| 25 | Bengaluru International Airport |  | IN | 782 |
| 26 | Malpensa International Airport |  | IT | 777 |
| 27 | Daniel K Inouye International Airport |  | US | 712 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 696 |
| 30 | Barcelona International Airport |  | ES | 680 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 672 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 630 |
| 35 | Don Mueang International Airport |  | TH | 627 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 380 | 21m | 244 km | 1,600.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 258 | 14m | 114 km | 506.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 254 | 28m | 304 km | 1,331.5 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 254 | 1h 25m | 910 km | 3,985.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 238 | 1h 10m | 770 km | 3,161.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 118 | 44m | 241 km | 490.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-06-06 06:27 UTC | 2026-06-06 07:03 UTC | 35m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-06-05 20:05 UTC | 2026-06-06 07:02 UTC | 10h 56m |
| HBLVC | HBL | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-06-06 06:45 UTC | 2026-06-06 07:00 UTC | 14m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-06-05 23:48 UTC | 2026-06-06 06:51 UTC | 7h 2m |
| EJU3637 | EJU | Malpensa International Airport (LIMC) | Lampedusa Airport (LICD) | 2026-06-06 05:04 UTC | 2026-06-06 06:44 UTC | 1h 39m |
| GTI4355 | GTI | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-06-05 19:26 UTC | 2026-06-06 06:43 UTC | 11h 16m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-06-05 18:57 UTC | 2026-06-06 06:41 UTC | 11h 44m |
| THY164 | Turkish Airlines | Istanbul Airport (LTFM) | Naypyidaw Airport (VYEL) | 2026-06-05 23:27 UTC | 2026-06-06 06:37 UTC | 7h 10m |
| RYR9WU | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Kasteli Airport (LGTL) | 2026-06-06 04:32 UTC | 2026-06-06 06:31 UTC | 1h 59m |
| ANA1689 | All Nippon Airways | Osaka International Airport (RJOO) | Hiroshima Airport (RJOA) | 2026-06-06 06:01 UTC | 2026-06-06 06:31 UTC | 30m |
| CPA740 | Cathay Pacific | Gia Lam Air Base (VVGL) | Macau International Airport (VMMC) | 2026-06-06 05:26 UTC | 2026-06-06 06:24 UTC | 58m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-06 06:00 UTC | 2026-06-06 06:22 UTC | 21m |
| EWG2AR | EWG | Hamburg Airport (EDDH) | Aquino Airport (LIAQ) | 2026-06-06 04:25 UTC | 2026-06-06 06:22 UTC | 1h 56m |
| ATG9720 | ATG | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-06-05 20:15 UTC | 2026-06-06 06:21 UTC | 10h 6m |
| QTR8472 | Qatar Airways | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-06-05 12:32 UTC | 2026-06-06 06:18 UTC | 17h 46m |
| VLG1DP | Vueling | Barcelona International Airport (LEBL) | Pamplona Airport (LEPP) | 2026-06-06 05:41 UTC | 2026-06-06 06:18 UTC | 36m |
| UAE9920 | Emirates | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-06-05 13:40 UTC | 2026-06-06 06:13 UTC | 16h 32m |
| NSZ2844 | NSZ | Helsinki Vantaa Airport (EFHK) | Sinj Glider Airport (LDSS) | 2026-06-06 03:40 UTC | 2026-06-06 06:12 UTC | 2h 32m |
| WZZ9VB | Wizz Air | Belgrade Nikola Tesla Airport (LYBE) | Kamp-Lintfort Airport (EDLC) | 2026-06-06 04:04 UTC | 2026-06-06 06:11 UTC | 2h 7m |
| ANE1097 | ANE | Madrid Barajas International Airport (LEMD) | Bilbao Airport (LEBB) | 2026-06-06 05:43 UTC | 2026-06-06 06:10 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
