# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_14:30:04_UTC-green)

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

**Latest saved flight:** 2026-06-17 14:30:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 14:30:04 UTC

- **113,052** saved flights
- **39,293** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **113,052** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,378,395.8 tonnes** estimated CO2 emissions
- **79,907,001 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4659 |
| 2 | SkyWest Airlines | 4205 |
| 3 | IndiGo | 2194 |
| 4 | EJA | 2191 |
| 5 | American Airlines | 1784 |
| 6 | Southwest Airlines | 1682 |
| 7 | ENY | 1409 |
| 8 | Delta Air Lines | 1337 |
| 9 | Lufthansa | 1269 |
| 10 | Vueling | 1031 |
| 11 | WIF | 1001 |
| 12 | LATAM Airlines | 997 |
| 13 | AXM | 945 |
| 14 | AZU | 945 |
| 15 | LXJ | 861 |
| 16 | Swiss International | 808 |
| 17 | All Nippon Airways | 786 |
| 18 | Alaska Airlines | 764 |
| 19 | QLK | 739 |
| 20 | easyJet | 729 |
| 21 | EJU | 715 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 633 |
| 24 | Air France | 628 |
| 25 | VIV | 628 |
| 26 | United Airlines | 627 |
| 27 | MXY | 599 |
| 28 | CXK | 597 |
| 29 | AXB | 556 |
| 30 | GLO | 556 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95234 |
| 2 | 🇪🇸 ES | 7736 |
| 3 | 🇮🇳 IN | 6931 |
| 4 | 🇦🇺 AU | 6722 |
| 5 | 🇧🇷 BR | 6260 |
| 6 | 🇮🇹 IT | 6072 |
| 7 | 🇩🇪 DE | 6051 |
| 8 | 🇨🇦 CA | 5939 |
| 9 | 🇯🇵 JP | 5112 |
| 10 | 🇬🇧 GB | 4888 |
| 11 | 🇫🇷 FR | 4503 |
| 12 | 🇨🇴 CO | 3824 |
| 13 | 🇲🇽 MX | 3339 |
| 14 | 🇬🇷 GR | 3211 |
| 15 | 🇳🇴 NO | 3128 |
| 16 | 🇨🇭 CH | 2894 |
| 17 | 🇲🇾 MY | 2443 |
| 18 | 🇹🇷 TR | 2263 |
| 19 | 🇿🇦 ZA | 1921 |
| 20 | 🇰🇷 KR | 1868 |
| 21 | 🇳🇿 NZ | 1856 |
| 22 | 🇵🇱 PL | 1845 |
| 23 | 🇹🇭 TH | 1843 |
| 24 | 🇵🇭 PH | 1651 |
| 25 | 🇬🇹 GT | 1612 |
| 26 | 🇲🇦 MA | 1241 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1109 |
| 29 | 🇳🇱 NL | 1098 |
| 30 | 🇭🇷 HR | 982 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2408 |
| 2 | Denver International Airport |  | US | 1911 |
| 3 | Tokyo International Airport |  | JP | 1697 |
| 4 | Indira Gandhi International Airport |  | IN | 1510 |
| 5 | Guaymaral Airport |  | CO | 1421 |
| 6 | Harry Reid International Airport |  | US | 1417 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1391 |
| 8 | Zurich Airport |  | CH | 1269 |
| 9 | La Aurora Airport |  | GT | 1242 |
| 10 | Frankfurt am Main International Airport |  | DE | 1237 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1214 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1145 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1132 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 983 |
| 17 | Madrid Barajas International Airport |  | ES | 978 |
| 18 | Salt Lake City International Airport |  | US | 955 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 949 |
| 20 | Kuala Lumpur International Airport |  | MY | 947 |
| 21 | Charlotte/Douglas International Airport |  | US | 876 |
| 22 | Congonhas Airport |  | BR | 870 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 845 |
| 24 | Charles de Gaulle International Airport |  | FR | 840 |
| 25 | Bengaluru International Airport |  | IN | 839 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 787 |
| 28 | Ninoy Aquino International Airport |  | PH | 761 |
| 29 | Daniel K Inouye International Airport |  | US | 745 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 742 |
| 31 | Tenerife Norte Airport |  | ES | 739 |
| 32 | Barcelona International Airport |  | ES | 733 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 714 |
| 34 | Don Mueang International Airport |  | TH | 672 |
| 35 | Amsterdam Airport Schiphol |  | NL | 672 |
| 36 | Vitoria/Foronda Airport |  | ES | 670 |
| 37 | Calgary International Airport |  | CA | 667 |
| 38 | Seattle-Tacoma International Airport |  | US | 651 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 648 |
| 40 | Viracopos International Airport |  | BR | 646 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 590 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 411 | 21m | 244 km | 1,730.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 277 | 1h 25m | 910 km | 4,346.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 270 | 1h 10m | 770 km | 3,586.7 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 227 | 26m | 275 km | 1,075.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 211 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 165 | 26m | 215 km | 611.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 145 | 44m | 241 km | 602.3 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 136 | 1h 1m | 695 km | 1,630.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SHERPA3 | SHE | Bishop Airfield (1AZ0) | Bishop Airfield (1AZ0) | 2026-06-17 14:11 UTC | 2026-06-17 14:30 UTC | 18m |
| N9298J |  | Albert Whitted Airport (KSPG) | Ott's Landing Airport (0FA1) | 2026-06-17 13:57 UTC | 2026-06-17 14:29 UTC | 32m |
| N665CS |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-06-17 13:16 UTC | 2026-06-17 14:23 UTC | 1h 7m |
| RNGR773 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | San Jose Island Airport (XS67) | 2026-06-17 13:54 UTC | 2026-06-17 14:21 UTC | 26m |
| N9204J |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-06-17 13:59 UTC | 2026-06-17 14:21 UTC | 21m |
| N7050Q |  | Council Bluffs Municipal Airport (KCBF) | Volkens Field (97IA) | 2026-06-17 13:48 UTC | 2026-06-17 14:15 UTC | 26m |
| N6618D |  | East Penn Airport (PA30) | 9PA5 (9PA5) | 2026-06-17 13:53 UTC | 2026-06-17 14:15 UTC | 22m |
| CLX491 | CLX | Luxembourg-Findel International Airport (ELLX) | Tedderfield Air Park (FATA) | 2026-06-17 04:25 UTC | 2026-06-17 14:12 UTC | 9h 46m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-17 13:56 UTC | 2026-06-17 14:09 UTC | 13m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-06-17 13:37 UTC | 2026-06-17 14:07 UTC | 29m |
| JYRJK | JYR | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-06-17 13:41 UTC | 2026-06-17 14:05 UTC | 23m |
| PGR1969 | PGR | Henderson Executive Airport (KHND) | Music Mountain Air Ranch Airport (68AZ) | 2026-06-17 13:35 UTC | 2026-06-17 14:05 UTC | 29m |
| FTO388 | FTO | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-06-17 13:26 UTC | 2026-06-17 14:04 UTC | 38m |
| N98TS |  | Northway Airport (NY97) | Northway Airport (NY97) | 2026-06-17 14:03 UTC | 2026-06-17 14:03 UTC | 0m |
| RYR7UL | Ryanair | Stapleford Aerodrome (EGSG) | Sywell Aerodrome (EGBK) | 2026-06-17 13:46 UTC | 2026-06-17 13:57 UTC | 11m |
| N64962 |  | Montgomery County Airpark (KGAI) | Lancaster Airport (KLNS) | 2026-06-17 13:10 UTC | 2026-06-17 13:57 UTC | 47m |
| N6960 |  | KU77 (KU77) | KU77 (KU77) | 2026-06-17 13:35 UTC | 2026-06-17 13:54 UTC | 19m |
| N61739 |  | Airglades Airport (K2IS) | Immokalee Regional Airport (KIMM) | 2026-06-17 13:34 UTC | 2026-06-17 13:54 UTC | 20m |
| SCU21 | SCU | Haskell Airport (K2K9) | Jantzen Airport (93OK) | 2026-06-17 13:37 UTC | 2026-06-17 13:53 UTC | 16m |
| SRD375 | SRD | RNAS Lee-On-Solent (EGHF) | RNAS Lee-On-Solent (EGHF) | 2026-06-17 13:53 UTC | 2026-06-17 13:53 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
