# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_20:47:05_UTC-green)

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

**Latest saved flight:** 2026-07-25 20:47:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 20:47:05 UTC

- **151,130** saved flights
- **50,251** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,130** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,807,944.2 tonnes** estimated CO2 emissions
- **104,808,359 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6100 |
| 2 | SkyWest Airlines | 5525 |
| 3 | EJA | 2992 |
| 4 | IndiGo | 2694 |
| 5 | American Airlines | 2397 |
| 6 | Southwest Airlines | 2295 |
| 7 | ENY | 1886 |
| 8 | Delta Air Lines | 1775 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1397 |
| 11 | AZU | 1312 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1271 |
| 14 | LXJ | 1167 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 982 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 940 |
| 20 | QLK | 931 |
| 21 | EJU | 925 |
| 22 | VIV | 833 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 793 |
| 26 | Air France | 788 |
| 27 | JetBlue | 786 |
| 28 | GLO | 784 |
| 29 | Cathay Pacific | 781 |
| 30 | United Airlines | 779 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130379 |
| 2 | 🇪🇸 ES | 9780 |
| 3 | 🇧🇷 BR | 8558 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8481 |
| 6 | 🇨🇦 CA | 8072 |
| 7 | 🇮🇹 IT | 7822 |
| 8 | 🇩🇪 DE | 7753 |
| 9 | 🇬🇧 GB | 6932 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5985 |
| 12 | 🇨🇴 CO | 5142 |
| 13 | 🇲🇽 MX | 4360 |
| 14 | 🇬🇷 GR | 4297 |
| 15 | 🇳🇴 NO | 4002 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3585 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2568 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2267 |
| 22 | 🇹🇭 TH | 2193 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1974 |
| 26 | 🇲🇦 MA | 1538 |
| 27 | 🇲🇪 ME | 1481 |
| 28 | 🇳🇱 NL | 1395 |
| 29 | 🇭🇷 HR | 1381 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3106 |
| 2 | Denver International Airport |  | US | 2535 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1904 |
| 5 | Indira Gandhi International Airport |  | IN | 1882 |
| 6 | Harry Reid International Airport |  | US | 1867 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1695 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1582 |
| 10 | La Aurora Airport |  | GT | 1529 |
| 11 | Frankfurt am Main International Airport |  | DE | 1429 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1414 |
| 13 | Chicago O'Hare International Airport |  | US | 1397 |
| 14 | El Dorado International Airport |  | CO | 1361 |
| 15 | Salt Lake City International Airport |  | US | 1360 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1291 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1226 |
| 19 | Madrid Barajas International Airport |  | ES | 1208 |
| 20 | Capua Airport |  | IT | 1205 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1171 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1074 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1063 |
| 26 | Charles de Gaulle International Airport |  | FR | 1038 |
| 27 | Bengaluru International Airport |  | IN | 1012 |
| 28 | Malpensa International Airport |  | IT | 989 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 916 |
| 31 | Barcelona International Airport |  | ES | 906 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 904 |
| 33 | Daniel K Inouye International Airport |  | US | 901 |
| 34 | Tenerife Norte Airport |  | ES | 869 |
| 35 | Seattle-Tacoma International Airport |  | US | 864 |
| 36 | Calgary International Airport |  | CA | 858 |
| 37 | Scottsdale Airport |  | US | 854 |
| 38 | Viracopos International Airport |  | BR | 853 |
| 39 | Amsterdam Airport Schiphol |  | NL | 838 |
| 40 | Oslo Gardermoen Airport |  | NO | 830 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 803 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 547 | 21m | 244 km | 2,303.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 368 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 179 | 1h 16m | 961 km | 2,967.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 178 | 30m | 49 km | 150.5 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 177 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 164 | 51m | 556 km | 1,572.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AER956 | AER | Dillingham Airport (PADL) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-25 19:37 UTC | 2026-07-25 20:47 UTC | 1h 9m |
| N6367Q |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-07-25 19:38 UTC | 2026-07-25 20:29 UTC | 50m |
| TKR140 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-07-25 20:14 UTC | 2026-07-25 20:29 UTC | 15m |
| N150VT |  | Franklin County State Airport (KFSO) | Franklin County State Airport (KFSO) | 2026-07-25 19:33 UTC | 2026-07-25 20:29 UTC | 56m |
| SCU5 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-07-25 20:09 UTC | 2026-07-25 20:28 UTC | 19m |
| LOG49XC | LOG | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-07-25 19:53 UTC | 2026-07-25 20:25 UTC | 31m |
| N4841Y |  | Ambrosich Field (4CO7) | Kelly Air Park (CO15) | 2026-07-25 20:02 UTC | 2026-07-25 20:19 UTC | 16m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-25 20:01 UTC | 2026-07-25 20:19 UTC | 17m |
| FIN950 | Finnair | Trondheim Airport Vaernes (ENVA) | Helsinki Vantaa Airport (EFHK) | 2026-07-25 18:30 UTC | 2026-07-25 20:18 UTC | 1h 47m |
| N958AL |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-07-25 20:14 UTC | 2026-07-25 20:17 UTC | 3m |
| TKR183 | TKR | Boise Air Trml/Gowen Field (KBOI) | Crowley Ranch Airstrip (78OR) | 2026-07-25 20:03 UTC | 2026-07-25 20:16 UTC | 13m |
| N8091T |  | Santa Barbara Municipal Airport (KSBA) | Van Nuys Airport (KVNY) | 2026-07-25 19:40 UTC | 2026-07-25 20:13 UTC | 33m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-07-25 19:57 UTC | 2026-07-25 20:11 UTC | 13m |
| N359KF |  | Carson City Airport (KCXP) | Dayton Valley Airpark (KA34) | 2026-07-25 19:59 UTC | 2026-07-25 20:08 UTC | 8m |
| TKR182 | TKR | Billings Logan International Airport (KBIL) | Cottonwood Airport (0MT5) | 2026-07-25 20:03 UTC | 2026-07-25 20:07 UTC | 4m |
| N476LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-25 17:22 UTC | 2026-07-25 20:07 UTC | 2h 44m |
| N501PG |  | Teterboro Airport (KTEB) | Lake County Airport (KLXV) | 2026-07-25 16:40 UTC | 2026-07-25 20:05 UTC | 3h 24m |
| N36789 |  | Grove Regional Airport (KGMJ) | 3TX2 (3TX2) | 2026-07-25 17:52 UTC | 2026-07-25 20:02 UTC | 2h 10m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-25 19:51 UTC | 2026-07-25 20:01 UTC | 10m |
| N219TF |  | Winnipeg James Armstrong Richardson International Airport (CYWG) | Rankin Inlet Airport (CYRT) | 2026-07-25 17:59 UTC | 2026-07-25 20:00 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
