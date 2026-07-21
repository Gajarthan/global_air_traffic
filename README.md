# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_21:44:22_UTC-green)

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

**Latest saved flight:** 2026-07-21 21:44:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-21 21:44:22 UTC

- **143,397** saved flights
- **48,048** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,397** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,719,984.6 tonnes** estimated CO2 emissions
- **99,709,250 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5835 |
| 2 | SkyWest Airlines | 5247 |
| 3 | EJA | 2823 |
| 4 | IndiGo | 2610 |
| 5 | American Airlines | 2298 |
| 6 | Southwest Airlines | 2159 |
| 7 | ENY | 1778 |
| 8 | Delta Air Lines | 1699 |
| 9 | Lufthansa | 1439 |
| 10 | LATAM Airlines | 1322 |
| 11 | Vueling | 1233 |
| 12 | AZU | 1231 |
| 13 | WIF | 1225 |
| 14 | LXJ | 1100 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1021 |
| 17 | easyJet | 939 |
| 18 | All Nippon Airways | 920 |
| 19 | Alaska Airlines | 907 |
| 20 | QLK | 906 |
| 21 | EJU | 880 |
| 22 | VIV | 798 |
| 23 | CXK | 766 |
| 24 | AEE | 763 |
| 25 | Air France | 761 |
| 26 | JetBlue | 760 |
| 27 | United Airlines | 745 |
| 28 | MXY | 744 |
| 29 | Cathay Pacific | 741 |
| 30 | GLO | 731 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123356 |
| 2 | 🇪🇸 ES | 9341 |
| 3 | 🇦🇺 AU | 8228 |
| 4 | 🇮🇳 IN | 8179 |
| 5 | 🇧🇷 BR | 8084 |
| 6 | 🇨🇦 CA | 7559 |
| 7 | 🇮🇹 IT | 7476 |
| 8 | 🇩🇪 DE | 7414 |
| 9 | 🇬🇧 GB | 6564 |
| 10 | 🇯🇵 JP | 6028 |
| 11 | 🇫🇷 FR | 5692 |
| 12 | 🇨🇴 CO | 4605 |
| 13 | 🇲🇽 MX | 4164 |
| 14 | 🇬🇷 GR | 4076 |
| 15 | 🇳🇴 NO | 3834 |
| 16 | 🇨🇭 CH | 3717 |
| 17 | 🇹🇷 TR | 3382 |
| 18 | 🇲🇾 MY | 2773 |
| 19 | 🇵🇱 PL | 2416 |
| 20 | 🇿🇦 ZA | 2338 |
| 21 | 🇳🇿 NZ | 2203 |
| 22 | 🇹🇭 TH | 2129 |
| 23 | 🇰🇷 KR | 2035 |
| 24 | 🇵🇭 PH | 1932 |
| 25 | 🇬🇹 GT | 1881 |
| 26 | 🇲🇦 MA | 1496 |
| 27 | 🇲🇪 ME | 1422 |
| 28 | 🇳🇱 NL | 1347 |
| 29 | 🇭🇷 HR | 1305 |
| 30 | 🇲🇴 MO | 1201 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2955 |
| 2 | Denver International Airport |  | US | 2408 |
| 3 | Tokyo International Airport |  | JP | 1940 |
| 4 | Indira Gandhi International Airport |  | IN | 1814 |
| 5 | Harry Reid International Airport |  | US | 1799 |
| 6 | Guaymaral Airport |  | CO | 1744 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1638 |
| 8 | Zurich Airport |  | CH | 1590 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1505 |
| 10 | La Aurora Airport |  | GT | 1456 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1355 |
| 13 | Chicago O'Hare International Airport |  | US | 1338 |
| 14 | Salt Lake City International Airport |  | US | 1285 |
| 15 | El Dorado International Airport |  | CO | 1269 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1258 |
| 17 | Macau International Airport |  | MO | 1201 |
| 18 | Capua Airport |  | IT | 1167 |
| 19 | Congonhas Airport |  | BR | 1149 |
| 20 | Madrid Barajas International Airport |  | ES | 1149 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1132 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1041 |
| 24 | Charlotte/Douglas International Airport |  | US | 1034 |
| 25 | Charles de Gaulle International Airport |  | FR | 1006 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1002 |
| 27 | Bengaluru International Airport |  | IN | 976 |
| 28 | Malpensa International Airport |  | IT | 923 |
| 29 | Ninoy Aquino International Airport |  | PH | 902 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 878 |
| 31 | Barcelona International Airport |  | ES | 874 |
| 32 | Daniel K Inouye International Airport |  | US | 873 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 853 |
| 34 | Tenerife Norte Airport |  | ES | 826 |
| 35 | Seattle-Tacoma International Airport |  | US | 817 |
| 36 | Calgary International Airport |  | CA | 816 |
| 37 | Viracopos International Airport |  | BR | 811 |
| 38 | Amsterdam Airport Schiphol |  | NL | 809 |
| 39 | Scottsdale Airport |  | US | 808 |
| 40 | Vitoria/Foronda Airport |  | ES | 787 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 735 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 522 | 21m | 244 km | 2,198.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 348 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 213 | 22m | 55 km | 202.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 193 | 26m | 215 km | 714.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 178 | 20m | 250 km | 768.9 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 167 | 1h 16m | 961 km | 2,768.1 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EMB64 | EMB | Ibiporanga da Felicidade Airport (SJVC) | Ibiporanga da Felicidade Airport (SJVC) | 2026-07-21 21:33 UTC | 2026-07-21 21:44 UTC | 11m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-21 21:15 UTC | 2026-07-21 21:43 UTC | 28m |
| QTR8542 | Qatar Airways | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-07-21 16:39 UTC | 2026-07-21 21:40 UTC | 5h 1m |
| TKR104 | TKR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-21 21:13 UTC | 2026-07-21 21:39 UTC | 26m |
| N5469K |  | K3M3 (K3M3) | Flying G Ranch Airport (86GA) | 2026-07-21 21:26 UTC | 2026-07-21 21:36 UTC | 10m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-07-21 10:12 UTC | 2026-07-21 21:27 UTC | 11h 15m |
| N849AA |  | Palm Beach County Park Airport (KLNA) | Duda Airstrip (FA69) | 2026-07-21 20:53 UTC | 2026-07-21 21:23 UTC | 30m |
| N484JB |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-07-21 20:45 UTC | 2026-07-21 21:23 UTC | 37m |
| URSA05 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-21 19:19 UTC | 2026-07-21 21:21 UTC | 2h 1m |
| BULET47 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | San Clemente Island Nalf Airport (KNUC) | 2026-07-21 20:18 UTC | 2026-07-21 21:20 UTC | 1h 1m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-07-21 20:55 UTC | 2026-07-21 21:20 UTC | 24m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-07-21 20:50 UTC | 2026-07-21 21:20 UTC | 29m |
| EMB88 | EMB | Fazenda Sao Francisco do Itaquere Airport (SDNL) | Ibiporanga da Felicidade Airport (SJVC) | 2026-07-21 20:38 UTC | 2026-07-21 21:19 UTC | 40m |
| C6040 |  | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-07-21 20:26 UTC | 2026-07-21 21:18 UTC | 52m |
| N9737V |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-21 20:25 UTC | 2026-07-21 21:17 UTC | 52m |
| TKR914 | TKR | Mc Clellan Airfield (KMCC) | Gansner Field (K2O1) | 2026-07-21 21:03 UTC | 2026-07-21 21:17 UTC | 14m |
| LXJ347 | LXJ | John Glenn Columbus International Airport (KCMH) | Gaylord Regional Airport (KGLR) | 2026-07-21 20:15 UTC | 2026-07-21 21:11 UTC | 56m |
| N95RZ |  | Wood County Airport (K1G0) | Aerodrome Les Noyers Airport (50OH) | 2026-07-21 21:02 UTC | 2026-07-21 21:11 UTC | 9m |
| N4411X |  | Riverside Airport (KRAL) | San Bernardino International Airport (KSBD) | 2026-07-21 20:58 UTC | 2026-07-21 21:08 UTC | 10m |
| N716S |  | Belleview Landing Airport (45OK) | Warren County Memorial Airport (KRNC) | 2026-07-21 19:53 UTC | 2026-07-21 21:08 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
