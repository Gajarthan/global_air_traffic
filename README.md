# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_15:25:17_UTC-green)

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

**Latest saved flight:** 2026-07-28 15:25:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 15:25:17 UTC

- **156,510** saved flights
- **51,996** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **156,510** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,877,907.0 tonnes** estimated CO2 emissions
- **108,864,173 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6300 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3096 |
| 4 | IndiGo | 2772 |
| 5 | American Airlines | 2493 |
| 6 | Southwest Airlines | 2458 |
| 7 | ENY | 1952 |
| 8 | Delta Air Lines | 1862 |
| 9 | Lufthansa | 1505 |
| 10 | LATAM Airlines | 1458 |
| 11 | AZU | 1368 |
| 12 | WIF | 1321 |
| 13 | Vueling | 1312 |
| 14 | LXJ | 1202 |
| 15 | AXM | 1102 |
| 16 | Swiss International | 1089 |
| 17 | easyJet | 1022 |
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 973 |
| 20 | QLK | 972 |
| 21 | EJU | 957 |
| 22 | VIV | 859 |
| 23 | United Airlines | 837 |
| 24 | CXK | 830 |
| 25 | GLO | 820 |
| 26 | AEE | 818 |
| 27 | Cathay Pacific | 817 |
| 28 | MXY | 817 |
| 29 | Air France | 812 |
| 30 | JetBlue | 812 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134999 |
| 2 | 🇪🇸 ES | 10090 |
| 3 | 🇧🇷 BR | 8920 |
| 4 | 🇦🇺 AU | 8853 |
| 5 | 🇮🇳 IN | 8717 |
| 6 | 🇨🇦 CA | 8429 |
| 7 | 🇮🇹 IT | 8074 |
| 8 | 🇩🇪 DE | 7949 |
| 9 | 🇬🇧 GB | 7196 |
| 10 | 🇯🇵 JP | 6420 |
| 11 | 🇫🇷 FR | 6195 |
| 12 | 🇨🇴 CO | 5451 |
| 13 | 🇲🇽 MX | 4486 |
| 14 | 🇬🇷 GR | 4455 |
| 15 | 🇳🇴 NO | 4139 |
| 16 | 🇨🇭 CH | 4102 |
| 17 | 🇹🇷 TR | 3737 |
| 18 | 🇲🇾 MY | 2871 |
| 19 | 🇵🇱 PL | 2672 |
| 20 | 🇿🇦 ZA | 2540 |
| 21 | 🇳🇿 NZ | 2329 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2091 |
| 24 | 🇵🇭 PH | 2066 |
| 25 | 🇬🇹 GT | 2015 |
| 26 | 🇲🇦 MA | 1598 |
| 27 | 🇲🇪 ME | 1513 |
| 28 | 🇭🇷 HR | 1443 |
| 29 | 🇳🇱 NL | 1433 |
| 30 | 🇲🇴 MO | 1289 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3214 |
| 2 | Denver International Airport |  | US | 2626 |
| 3 | Tokyo International Airport |  | JP | 2035 |
| 4 | Guaymaral Airport |  | CO | 1962 |
| 5 | Indira Gandhi International Airport |  | IN | 1937 |
| 6 | Harry Reid International Airport |  | US | 1918 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1734 |
| 8 | Zurich Airport |  | CH | 1689 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1640 |
| 10 | La Aurora Airport |  | GT | 1562 |
| 11 | Frankfurt am Main International Airport |  | DE | 1455 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 13 | Chicago O'Hare International Airport |  | US | 1423 |
| 14 | El Dorado International Airport |  | CO | 1416 |
| 15 | Salt Lake City International Airport |  | US | 1410 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1289 |
| 18 | Congonhas Airport |  | BR | 1279 |
| 19 | Madrid Barajas International Airport |  | ES | 1244 |
| 20 | Capua Airport |  | IT | 1230 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1111 |
| 24 | Charlotte/Douglas International Airport |  | US | 1107 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1071 |
| 27 | Bengaluru International Airport |  | IN | 1037 |
| 28 | Malpensa International Airport |  | IT | 1026 |
| 29 | Ninoy Aquino International Airport |  | PH | 968 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 951 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 945 |
| 32 | Barcelona International Airport |  | ES | 933 |
| 33 | Daniel K Inouye International Airport |  | US | 924 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 895 |
| 36 | Tenerife Norte Airport |  | ES | 893 |
| 37 | Viracopos International Airport |  | BR | 888 |
| 38 | Scottsdale Airport |  | US | 885 |
| 39 | Amsterdam Airport Schiphol |  | NL | 865 |
| 40 | Oslo Gardermoen Airport |  | NO | 863 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 824 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 563 | 21m | 244 km | 2,370.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 375 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 361 | 1h 9m | 770 km | 4,795.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 217 | 44m | 241 km | 901.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 210 | 1h 47m | 1,423 km | 5,153.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 205 | 26m | 215 km | 759.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 200 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 185 | 18m | 144 km | 460.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N810BA |  | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-07-28 14:49 UTC | 2026-07-28 15:25 UTC | 35m |
| FIAMMA05 | FIA | Pratica Di Mare Airport (LIRE) | Pratica Di Mare Airport (LIRE) | 2026-07-28 15:08 UTC | 2026-07-28 15:22 UTC | 14m |
| HKS40 | HKS | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-07-28 14:53 UTC | 2026-07-28 15:21 UTC | 28m |
| HKS75 | HKS | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-07-28 14:44 UTC | 2026-07-28 15:14 UTC | 29m |
| SXN19 | SXN | Manchester Airport (EGCC) | London City Airport (EGLC) | 2026-07-28 14:17 UTC | 2026-07-28 15:12 UTC | 55m |
| AAL816 | American Airlines | John F Kennedy International Airport (KJFK) | Isla Mujeres Airport (MMIM) | 2026-07-28 11:57 UTC | 2026-07-28 15:08 UTC | 3h 11m |
| RNGR701 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-07-28 14:49 UTC | 2026-07-28 15:03 UTC | 13m |
| N88CR |  | Ocean Reef Club Airport (07FA) | Miami Executive Airport (KTMB) | 2026-07-28 13:55 UTC | 2026-07-28 15:02 UTC | 1h 6m |
| CBC511 | CBC | CL36 (CL36) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-28 14:31 UTC | 2026-07-28 15:00 UTC | 29m |
| XTX123H | XTX | Madrid Barajas International Airport (LEMD) | E. Castellanos-Villacastin Airport (LEEV) | 2026-07-28 14:43 UTC | 2026-07-28 14:59 UTC | 16m |
| N895SF |  | Salmon Falls Airport (ME61) | Skydive New England Airport (ME64) | 2026-07-28 14:40 UTC | 2026-07-28 14:57 UTC | 16m |
| N632PM |  | CA40 (CA40) | Meadows Field (KBFL) | 2026-07-28 14:31 UTC | 2026-07-28 14:56 UTC | 25m |
| N4409X |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-07-28 14:15 UTC | 2026-07-28 14:55 UTC | 40m |
| N127KC |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-07-28 13:45 UTC | 2026-07-28 14:54 UTC | 1h 9m |
| N96775 |  | 54OK (54OK) | Ragwing Acres Airport (2OK4) | 2026-07-28 14:35 UTC | 2026-07-28 14:52 UTC | 16m |
| CXK215 | CXK | Arlington Municipal Airport (KGKY) | Arlington Municipal Airport (KGKY) | 2026-07-28 14:22 UTC | 2026-07-28 14:51 UTC | 29m |
| CXK1076 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-28 14:40 UTC | 2026-07-28 14:50 UTC | 10m |
| HB1965 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-07-28 12:56 UTC | 2026-07-28 14:50 UTC | 1h 54m |
| N317VB |  | Dallas Love Field (KDAL) | Albany Municipal Airport (KT23) | 2026-07-28 14:25 UTC | 2026-07-28 14:47 UTC | 22m |
| N1931H |  | KU42 (KU42) | KU42 (KU42) | 2026-07-28 14:26 UTC | 2026-07-28 14:44 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
