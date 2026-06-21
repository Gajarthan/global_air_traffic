# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_18:21:03_UTC-green)

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

**Latest saved flight:** 2026-06-21 18:21:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-21 18:21:03 UTC

- **116,783** saved flights
- **40,389** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **116,783** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,418,931.4 tonnes** estimated CO2 emissions
- **82,256,895 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4828 |
| 2 | SkyWest Airlines | 4328 |
| 3 | EJA | 2267 |
| 4 | IndiGo | 2260 |
| 5 | American Airlines | 1824 |
| 6 | Southwest Airlines | 1740 |
| 7 | ENY | 1456 |
| 8 | Delta Air Lines | 1374 |
| 9 | Lufthansa | 1293 |
| 10 | Vueling | 1051 |
| 11 | WIF | 1031 |
| 12 | LATAM Airlines | 1028 |
| 13 | AZU | 971 |
| 14 | AXM | 958 |
| 15 | LXJ | 889 |
| 16 | Swiss International | 826 |
| 17 | All Nippon Airways | 799 |
| 18 | Alaska Airlines | 780 |
| 19 | QLK | 751 |
| 20 | easyJet | 749 |
| 21 | EJU | 732 |
| 22 | Cathay Pacific | 673 |
| 23 | AEE | 657 |
| 24 | VIV | 644 |
| 25 | Air France | 643 |
| 26 | United Airlines | 642 |
| 27 | CXK | 625 |
| 28 | MXY | 618 |
| 29 | AXB | 579 |
| 30 | GLO | 572 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98631 |
| 2 | 🇪🇸 ES | 7968 |
| 3 | 🇮🇳 IN | 7111 |
| 4 | 🇦🇺 AU | 6884 |
| 5 | 🇧🇷 BR | 6437 |
| 6 | 🇮🇹 IT | 6252 |
| 7 | 🇩🇪 DE | 6232 |
| 8 | 🇨🇦 CA | 6122 |
| 9 | 🇯🇵 JP | 5230 |
| 10 | 🇬🇧 GB | 5109 |
| 11 | 🇫🇷 FR | 4661 |
| 12 | 🇨🇴 CO | 3988 |
| 13 | 🇲🇽 MX | 3432 |
| 14 | 🇬🇷 GR | 3341 |
| 15 | 🇳🇴 NO | 3205 |
| 16 | 🇨🇭 CH | 3001 |
| 17 | 🇲🇾 MY | 2489 |
| 18 | 🇹🇷 TR | 2379 |
| 19 | 🇿🇦 ZA | 1974 |
| 20 | 🇵🇱 PL | 1919 |
| 21 | 🇳🇿 NZ | 1906 |
| 22 | 🇹🇭 TH | 1892 |
| 23 | 🇰🇷 KR | 1889 |
| 24 | 🇵🇭 PH | 1692 |
| 25 | 🇬🇹 GT | 1648 |
| 26 | 🇲🇦 MA | 1271 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1148 |
| 29 | 🇳🇱 NL | 1126 |
| 30 | 🇭🇷 HR | 1019 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2461 |
| 2 | Denver International Airport |  | US | 1965 |
| 3 | Tokyo International Airport |  | JP | 1733 |
| 4 | Indira Gandhi International Airport |  | IN | 1561 |
| 5 | Guaymaral Airport |  | CO | 1478 |
| 6 | Harry Reid International Airport |  | US | 1457 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1428 |
| 8 | Zurich Airport |  | CH | 1307 |
| 9 | La Aurora Airport |  | GT | 1272 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1240 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1161 |
| 15 | Chicago O'Hare International Airport |  | US | 1147 |
| 16 | Capua Airport |  | IT | 1016 |
| 17 | Salt Lake City International Airport |  | US | 1001 |
| 18 | Madrid Barajas International Airport |  | ES | 988 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 975 |
| 20 | Kuala Lumpur International Airport |  | MY | 962 |
| 21 | Congonhas Airport |  | BR | 895 |
| 22 | Charlotte/Douglas International Airport |  | US | 890 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 867 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 865 |
| 25 | Charles de Gaulle International Airport |  | FR | 861 |
| 26 | Bengaluru International Airport |  | IN | 860 |
| 27 | Malpensa International Airport |  | IT | 829 |
| 28 | Ninoy Aquino International Airport |  | PH | 781 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 762 |
| 30 | Daniel K Inouye International Airport |  | US | 760 |
| 31 | Tenerife Norte Airport |  | ES | 758 |
| 32 | Barcelona International Airport |  | ES | 742 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 733 |
| 34 | Calgary International Airport |  | CA | 686 |
| 35 | Don Mueang International Airport |  | TH | 685 |
| 36 | Vitoria/Foronda Airport |  | ES | 685 |
| 37 | Amsterdam Airport Schiphol |  | NL | 683 |
| 38 | Seattle-Tacoma International Airport |  | US | 671 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 665 |
| 40 | Viracopos International Airport |  | BR | 663 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 613 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 424 | 21m | 244 km | 1,785.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 311 | 24m | 225 km | 1,206.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 300 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 285 | 1h 25m | 910 km | 4,472.3 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 281 | 1h 10m | 770 km | 3,732.9 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 230 | 19m | 165 km | 654.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 169 | 20m | 99 km | 289.5 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 159 | 27m | 152 km | 415.5 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 155 | 44m | 241 km | 643.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 145 | 1h 44m | 1,423 km | 3,558.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N405CM |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-06-21 18:06 UTC | 2026-06-21 18:21 UTC | 14m |
| N61958 |  | Gillespie Field (KSEE) | Meadows Field (KBFL) | 2026-06-21 16:27 UTC | 2026-06-21 18:19 UTC | 1h 52m |
| BOE896 | BOE | Boeing Field/King County International Airport (KBFI) | Coopers Landing Airport (0WN2) | 2026-06-21 17:25 UTC | 2026-06-21 18:12 UTC | 47m |
| JBU896 | JetBlue | Hartsfield/Jackson Atlanta International Airport (KATL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-21 16:07 UTC | 2026-06-21 18:11 UTC | 2h 4m |
| N4217W |  | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-06-21 17:19 UTC | 2026-06-21 18:11 UTC | 51m |
| OXF2583 | OXF | Falcon Field (KFFZ) | AZ86 (AZ86) | 2026-06-21 17:20 UTC | 2026-06-21 18:10 UTC | 49m |
| N252EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-21 17:11 UTC | 2026-06-21 18:09 UTC | 58m |
| N3973D |  | Tri-State Steuben County Airport (KANQ) | Tri-State Steuben County Airport (KANQ) | 2026-06-21 17:51 UTC | 2026-06-21 18:03 UTC | 11m |
| RPA5661 | Republic Airways | Gerald R Ford International Airport (KGRR) | Laguardia Airport (KLGA) | 2026-06-21 16:35 UTC | 2026-06-21 18:02 UTC | 1h 26m |
| N238TD |  | Salinas Municipal Airport (KSNS) | Lake Tahoe Airport (KTVL) | 2026-06-21 17:37 UTC | 2026-06-21 18:00 UTC | 23m |
| N513LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-21 17:41 UTC | 2026-06-21 17:58 UTC | 17m |
| N586EF |  | Monmouth Executive Airport (KBLM) | Monmouth Executive Airport (KBLM) | 2026-06-21 17:19 UTC | 2026-06-21 17:56 UTC | 36m |
| SLH4 | SLH | Chicago Midway International Airport (KMDW) | Jefferson City Memorial Airport (KJEF) | 2026-06-21 16:57 UTC | 2026-06-21 17:55 UTC | 58m |
| N38HX |  | Los Alamos Airport (KLAM) | Los Alamos Airport (KLAM) | 2026-06-21 17:48 UTC | 2026-06-21 17:55 UTC | 6m |
| LAN800 | LAN | Auckland International Airport (NZAA) | Chicureo Airport (SCHC) | 2026-06-21 07:45 UTC | 2026-06-21 17:54 UTC | 10h 9m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-06-21 17:36 UTC | 2026-06-21 17:54 UTC | 17m |
| N734M |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-06-21 17:23 UTC | 2026-06-21 17:54 UTC | 30m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-21 17:24 UTC | 2026-06-21 17:54 UTC | 30m |
| TGEAA | TGE | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-21 17:36 UTC | 2026-06-21 17:51 UTC | 15m |
| N901BS |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-06-21 15:31 UTC | 2026-06-21 17:50 UTC | 2h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
