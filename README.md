# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_01:33:51_UTC-green)

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

**Latest saved flight:** 2026-06-18 01:33:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-18 01:33:51 UTC

- **113,642** saved flights
- **39,479** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,642** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,384,300.7 tonnes** estimated CO2 emissions
- **80,249,315 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4681 |
| 2 | SkyWest Airlines | 4238 |
| 3 | EJA | 2204 |
| 4 | IndiGo | 2197 |
| 5 | American Airlines | 1790 |
| 6 | Southwest Airlines | 1692 |
| 7 | ENY | 1416 |
| 8 | Delta Air Lines | 1342 |
| 9 | Lufthansa | 1270 |
| 10 | Vueling | 1033 |
| 11 | WIF | 1008 |
| 12 | LATAM Airlines | 1002 |
| 13 | AZU | 952 |
| 14 | AXM | 947 |
| 15 | LXJ | 865 |
| 16 | Swiss International | 810 |
| 17 | All Nippon Airways | 787 |
| 18 | Alaska Airlines | 769 |
| 19 | QLK | 742 |
| 20 | easyJet | 731 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 636 |
| 24 | VIV | 630 |
| 25 | Air France | 629 |
| 26 | United Airlines | 629 |
| 27 | CXK | 602 |
| 28 | MXY | 601 |
| 29 | AXB | 557 |
| 30 | GLO | 557 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95895 |
| 2 | 🇪🇸 ES | 7755 |
| 3 | 🇮🇳 IN | 6938 |
| 4 | 🇦🇺 AU | 6750 |
| 5 | 🇧🇷 BR | 6293 |
| 6 | 🇮🇹 IT | 6099 |
| 7 | 🇩🇪 DE | 6073 |
| 8 | 🇨🇦 CA | 5976 |
| 9 | 🇯🇵 JP | 5125 |
| 10 | 🇬🇧 GB | 4905 |
| 11 | 🇫🇷 FR | 4520 |
| 12 | 🇨🇴 CO | 3867 |
| 13 | 🇲🇽 MX | 3359 |
| 14 | 🇬🇷 GR | 3228 |
| 15 | 🇳🇴 NO | 3142 |
| 16 | 🇨🇭 CH | 2903 |
| 17 | 🇲🇾 MY | 2449 |
| 18 | 🇹🇷 TR | 2282 |
| 19 | 🇿🇦 ZA | 1923 |
| 20 | 🇰🇷 KR | 1869 |
| 21 | 🇳🇿 NZ | 1868 |
| 22 | 🇵🇱 PL | 1856 |
| 23 | 🇹🇭 TH | 1843 |
| 24 | 🇵🇭 PH | 1651 |
| 25 | 🇬🇹 GT | 1622 |
| 26 | 🇲🇦 MA | 1245 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1112 |
| 29 | 🇳🇱 NL | 1103 |
| 30 | 🇭🇷 HR | 988 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2419 |
| 2 | Denver International Airport |  | US | 1926 |
| 3 | Tokyo International Airport |  | JP | 1702 |
| 4 | Indira Gandhi International Airport |  | IN | 1511 |
| 5 | Guaymaral Airport |  | CO | 1431 |
| 6 | Harry Reid International Airport |  | US | 1426 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1395 |
| 8 | Zurich Airport |  | CH | 1277 |
| 9 | La Aurora Airport |  | GT | 1251 |
| 10 | Frankfurt am Main International Airport |  | DE | 1239 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1220 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1153 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1139 |
| 15 | Chicago O'Hare International Airport |  | US | 1123 |
| 16 | Capua Airport |  | IT | 987 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 966 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 957 |
| 20 | Kuala Lumpur International Airport |  | MY | 949 |
| 21 | Charlotte/Douglas International Airport |  | US | 881 |
| 22 | Congonhas Airport |  | BR | 872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 847 |
| 24 | Charles de Gaulle International Airport |  | FR | 841 |
| 25 | Bengaluru International Airport |  | IN | 840 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 805 |
| 28 | Ninoy Aquino International Airport |  | PH | 761 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 747 |
| 30 | Daniel K Inouye International Airport |  | US | 746 |
| 31 | Tenerife Norte Airport |  | ES | 741 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 716 |
| 34 | Amsterdam Airport Schiphol |  | NL | 674 |
| 35 | Don Mueang International Airport |  | TH | 672 |
| 36 | Vitoria/Foronda Airport |  | ES | 672 |
| 37 | Calgary International Airport |  | CA | 670 |
| 38 | Seattle-Tacoma International Airport |  | US | 654 |
| 39 | Viracopos International Airport |  | BR | 651 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 650 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 593 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 412 | 21m | 244 km | 1,734.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 279 | 1h 25m | 910 km | 4,378.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 277 | 14m | 114 km | 543.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 272 | 1h 10m | 770 km | 3,613.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 226 | 19m | 165 km | 642.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 211 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 166 | 26m | 215 km | 614.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 166 | 22m | 55 km | 157.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 164 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 147 | 44m | 241 km | 610.6 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 128 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 127 | 1h 17m | 961 km | 2,105.1 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OZN934 | OZN | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-06-18 00:54 UTC | 2026-06-18 01:33 UTC | 39m |
| NRL | NRL | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-06-18 00:31 UTC | 2026-06-18 01:27 UTC | 55m |
| ASA535 | Alaska Airlines | Denver International Airport (KDEN) | Seattle-Tacoma International Airport (KSEA) | 2026-06-17 23:00 UTC | 2026-06-18 01:26 UTC | 2h 26m |
| N724FH |  | Kulik Lake Airport (PAKL) | Bootleggers Cove Airport (2AK4) | 2026-06-18 00:18 UTC | 2026-06-18 01:23 UTC | 1h 4m |
| C6561 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-06-18 00:30 UTC | 2026-06-18 01:16 UTC | 46m |
| NCJ12 | NCJ | Green Bay/Austin Straubel International Airport (KGRB) | St Paul Downtown Holman Field (KSTP) | 2026-06-18 00:25 UTC | 2026-06-18 01:15 UTC | 49m |
| JCY504 | JCY | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-06-17 23:55 UTC | 2026-06-18 01:09 UTC | 1h 14m |
| N4409X |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-06-18 00:27 UTC | 2026-06-18 01:04 UTC | 37m |
| N400AY |  | Cecil Ranch Airport (37CN) | Mc Clellan Airfield (KMCC) | 2026-06-18 00:29 UTC | 2026-06-18 01:03 UTC | 33m |
| N960KH |  | Crystal Springs Ranch Airport (UT54) | Salt Lake City International Airport (KSLC) | 2026-06-18 00:10 UTC | 2026-06-18 00:59 UTC | 49m |
| N647AG |  | Van Nuys Airport (KVNY) | Santa Monica Municipal Airport (KSMO) | 2026-06-18 00:49 UTC | 2026-06-18 00:56 UTC | 7m |
| N765KA |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-06-18 00:30 UTC | 2026-06-18 00:53 UTC | 23m |
| FFT1177 | FFT | Los Angeles International Airport (KLAX) | Flying B Airport (8WA0) | 2026-06-17 22:38 UTC | 2026-06-18 00:51 UTC | 2h 13m |
| N4325R |  | Oasis Ranger Station-U S Government Airport (9FL7) | Miami Executive Airport (KTMB) | 2026-06-18 00:02 UTC | 2026-06-18 00:51 UTC | 49m |
| JBU2468 | JetBlue | Charleston Afb/International Airport (KCHS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-17 22:57 UTC | 2026-06-18 00:50 UTC | 1h 53m |
| SHADO33 | SHA | Capital City Airport (KFFT) | Blue Grass Airport (KLEX) | 2026-06-18 00:30 UTC | 2026-06-18 00:47 UTC | 17m |
| N825TB |  | Rogers Executive - Carter Field (KROG) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-17 22:19 UTC | 2026-06-18 00:46 UTC | 2h 26m |
| N393BZ |  | Boeing Field/King County International Airport (KBFI) | San Francisco International Airport (KSFO) | 2026-06-17 23:05 UTC | 2026-06-18 00:45 UTC | 1h 39m |
| VIR11B | Virgin Atlantic | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-18 00:43 UTC | 2026-06-18 00:43 UTC | 0m |
| SWA2720 | Southwest Airlines | Sacramento International Airport (KSMF) | Western Airpark (06WN) | 2026-06-17 22:48 UTC | 2026-06-18 00:40 UTC | 1h 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
