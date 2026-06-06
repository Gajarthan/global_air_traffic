# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_17:50:24_UTC-green)

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

**Latest saved flight:** 2026-06-06 17:50:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 17:50:24 UTC

- **104,329** saved flights
- **36,807** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,329** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,275,060.9 tonnes** estimated CO2 emissions
- **73,916,571 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4290 |
| 2 | SkyWest Airlines | 3917 |
| 3 | IndiGo | 2088 |
| 4 | EJA | 1988 |
| 5 | American Airlines | 1679 |
| 6 | Southwest Airlines | 1574 |
| 7 | ENY | 1303 |
| 8 | Delta Air Lines | 1233 |
| 9 | Lufthansa | 1201 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 922 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 836 |
| 15 | LXJ | 784 |
| 16 | Swiss International | 753 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 724 |
| 19 | QLK | 697 |
| 20 | easyJet | 676 |
| 21 | EJU | 656 |
| 22 | Cathay Pacific | 622 |
| 23 | AEE | 604 |
| 24 | Air France | 600 |
| 25 | VIV | 599 |
| 26 | United Airlines | 576 |
| 27 | MXY | 564 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87713 |
| 2 | 🇪🇸 ES | 7190 |
| 3 | 🇮🇳 IN | 6592 |
| 4 | 🇦🇺 AU | 6310 |
| 5 | 🇧🇷 BR | 5695 |
| 6 | 🇩🇪 DE | 5616 |
| 7 | 🇮🇹 IT | 5546 |
| 8 | 🇨🇦 CA | 5425 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4406 |
| 11 | 🇫🇷 FR | 4139 |
| 12 | 🇨🇴 CO | 3602 |
| 13 | 🇲🇽 MX | 3125 |
| 14 | 🇬🇷 GR | 2971 |
| 15 | 🇳🇴 NO | 2897 |
| 16 | 🇨🇭 CH | 2667 |
| 17 | 🇲🇾 MY | 2295 |
| 18 | 🇹🇷 TR | 1988 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1744 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1722 |
| 23 | 🇵🇱 PL | 1693 |
| 24 | 🇵🇭 PH | 1531 |
| 25 | 🇬🇹 GT | 1521 |
| 26 | 🇲🇦 MA | 1156 |
| 27 | 🇲🇴 MO | 1098 |
| 28 | 🇳🇱 NL | 1027 |
| 29 | 🇲🇪 ME | 989 |
| 30 | 🇭🇷 HR | 914 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2268 |
| 2 | Denver International Airport |  | US | 1780 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1431 |
| 5 | Harry Reid International Airport |  | US | 1336 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1326 |
| 7 | Guaymaral Airport |  | CO | 1308 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1184 |
| 10 | La Aurora Airport |  | GT | 1169 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1126 |
| 12 | El Dorado International Airport |  | CO | 1099 |
| 13 | Macau International Airport |  | MO | 1098 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1053 |
| 15 | Chicago O'Hare International Airport |  | US | 1046 |
| 16 | Madrid Barajas International Airport |  | ES | 907 |
| 17 | Kuala Lumpur International Airport |  | MY | 899 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 890 |
| 19 | Salt Lake City International Airport |  | US | 885 |
| 20 | Capua Airport |  | IT | 875 |
| 21 | Charlotte/Douglas International Airport |  | US | 810 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 796 |
| 24 | Bengaluru International Airport |  | IN | 792 |
| 25 | Congonhas Airport |  | BR | 791 |
| 26 | Malpensa International Airport |  | IT | 783 |
| 27 | Daniel K Inouye International Airport |  | US | 715 |
| 28 | Tenerife Norte Airport |  | ES | 713 |
| 29 | Ninoy Aquino International Airport |  | PH | 699 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 676 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 672 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 669 |
| 34 | Amsterdam Airport Schiphol |  | NL | 636 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 627 |
| 37 | Calgary International Airport |  | CA | 617 |
| 38 | Seattle-Tacoma International Airport |  | US | 602 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 539 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 383 | 21m | 244 km | 1,612.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 274 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 264 | 14m | 114 km | 517.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 206 | 26m | 275 km | 976.1 t |
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
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 135 | 18m | 144 km | 335.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 52m | 1,304 km | 2,699.7 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4120R |  | Potters Field (55AZ) | Farms Airport (41AZ) | 2026-06-06 16:26 UTC | 2026-06-06 17:50 UTC | 1h 23m |
| N8267Y |  | 8CL0 (8CL0) | 8CL0 (8CL0) | 2026-06-06 17:25 UTC | 2026-06-06 17:46 UTC | 20m |
| N331BR |  | Detroit Metro Wayne County Airport (KDTW) | Telluride Regional Airport (KTEX) | 2026-06-06 13:47 UTC | 2026-06-06 17:34 UTC | 3h 46m |
| N533LC |  | Page Field (KFMY) | Naples Municipal Airport (KAPF) | 2026-06-06 17:23 UTC | 2026-06-06 17:33 UTC | 10m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-06-06 17:14 UTC | 2026-06-06 17:33 UTC | 18m |
| N584CC |  | NJ58 (NJ58) | NJ58 (NJ58) | 2026-06-06 16:53 UTC | 2026-06-06 17:32 UTC | 39m |
| N7079F |  | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-06-06 17:17 UTC | 2026-06-06 17:30 UTC | 13m |
| GBMSB | GBM | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-06-06 17:29 UTC | 2026-06-06 17:29 UTC | 0m |
| N535KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 16:55 UTC | 2026-06-06 17:29 UTC | 33m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 17:05 UTC | 2026-06-06 17:25 UTC | 20m |
| N727KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 16:54 UTC | 2026-06-06 17:25 UTC | 31m |
| N929KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 16:49 UTC | 2026-06-06 17:22 UTC | 33m |
| DWC007 | DWC | Cochin International Airport (VOCI) | Ras Tanura Airport (OERT) | 2026-06-06 12:43 UTC | 2026-06-06 17:22 UTC | 4h 39m |
| N272WC |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-06-06 16:36 UTC | 2026-06-06 17:21 UTC | 45m |
| N491LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-06 16:51 UTC | 2026-06-06 17:21 UTC | 30m |
| TNDR17 | TND | CFB Trenton (CYTR) | Val-d'Or Airport (CYVO) | 2026-06-06 16:44 UTC | 2026-06-06 17:20 UTC | 36m |
| N4409X |  | Van Nuys Airport (KVNY) | Whiteman Airport (KWHP) | 2026-06-06 17:07 UTC | 2026-06-06 17:18 UTC | 10m |
| N395WJ |  | James M Cox Dayton International Airport (KDAY) | Lincoln Airport (KLNK) | 2026-06-06 15:27 UTC | 2026-06-06 17:17 UTC | 1h 50m |
| N3040F |  | Greeneville Municipal Airport (KGCY) | 75TN (75TN) | 2026-06-06 17:06 UTC | 2026-06-06 17:17 UTC | 11m |
| N4017P |  | Caddo Mills Municipal Airport (K7F3) | 4 S Ranch Airport (TS25) | 2026-06-06 16:57 UTC | 2026-06-06 17:17 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
