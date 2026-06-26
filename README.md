# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_21:32:14_UTC-green)

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

**Latest saved flight:** 2026-06-26 21:32:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 21:32:14 UTC

- **121,506** saved flights
- **41,735** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **121,506** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,468,467.1 tonnes** estimated CO2 emissions
- **85,128,526 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4983 |
| 2 | SkyWest Airlines | 4491 |
| 3 | EJA | 2348 |
| 4 | IndiGo | 2324 |
| 5 | American Airlines | 1880 |
| 6 | Southwest Airlines | 1817 |
| 7 | ENY | 1515 |
| 8 | Delta Air Lines | 1437 |
| 9 | Lufthansa | 1321 |
| 10 | Vueling | 1084 |
| 11 | LATAM Airlines | 1080 |
| 12 | WIF | 1076 |
| 13 | AZU | 1017 |
| 14 | AXM | 983 |
| 15 | LXJ | 922 |
| 16 | Swiss International | 848 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 800 |
| 19 | easyJet | 784 |
| 20 | QLK | 774 |
| 21 | EJU | 764 |
| 22 | Cathay Pacific | 680 |
| 23 | AEE | 672 |
| 24 | Air France | 666 |
| 25 | VIV | 663 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 635 |
| 29 | JetBlue | 607 |
| 30 | AXB | 602 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103196 |
| 2 | 🇪🇸 ES | 8222 |
| 3 | 🇮🇳 IN | 7304 |
| 4 | 🇦🇺 AU | 7126 |
| 5 | 🇧🇷 BR | 6689 |
| 6 | 🇩🇪 DE | 6475 |
| 7 | 🇮🇹 IT | 6463 |
| 8 | 🇨🇦 CA | 6392 |
| 9 | 🇯🇵 JP | 5389 |
| 10 | 🇬🇧 GB | 5344 |
| 11 | 🇫🇷 FR | 4822 |
| 12 | 🇨🇴 CO | 4024 |
| 13 | 🇲🇽 MX | 3535 |
| 14 | 🇬🇷 GR | 3468 |
| 15 | 🇳🇴 NO | 3352 |
| 16 | 🇨🇭 CH | 3121 |
| 17 | 🇲🇾 MY | 2549 |
| 18 | 🇹🇷 TR | 2511 |
| 19 | 🇿🇦 ZA | 2027 |
| 20 | 🇵🇱 PL | 1994 |
| 21 | 🇳🇿 NZ | 1962 |
| 22 | 🇹🇭 TH | 1921 |
| 23 | 🇰🇷 KR | 1917 |
| 24 | 🇵🇭 PH | 1740 |
| 25 | 🇬🇹 GT | 1690 |
| 26 | 🇲🇦 MA | 1306 |
| 27 | 🇲🇪 ME | 1211 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1158 |
| 30 | 🇭🇷 HR | 1052 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2549 |
| 2 | Denver International Airport |  | US | 2042 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1609 |
| 5 | Guaymaral Airport |  | CO | 1514 |
| 6 | Harry Reid International Airport |  | US | 1513 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1469 |
| 8 | Zurich Airport |  | CH | 1346 |
| 9 | La Aurora Airport |  | GT | 1305 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1292 |
| 11 | Frankfurt am Main International Airport |  | DE | 1275 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1196 |
| 13 | Chicago O'Hare International Airport |  | US | 1181 |
| 14 | Macau International Airport |  | MO | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1059 |
| 17 | Capua Airport |  | IT | 1040 |
| 18 | Madrid Barajas International Airport |  | ES | 1018 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1013 |
| 20 | Kuala Lumpur International Airport |  | MY | 988 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 954 |
| 22 | Congonhas Airport |  | BR | 937 |
| 23 | Charlotte/Douglas International Airport |  | US | 915 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 900 |
| 25 | Charles de Gaulle International Airport |  | FR | 891 |
| 26 | Bengaluru International Airport |  | IN | 877 |
| 27 | Malpensa International Airport |  | IT | 847 |
| 28 | Ninoy Aquino International Airport |  | PH | 806 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 789 |
| 30 | Daniel K Inouye International Airport |  | US | 783 |
| 31 | Barcelona International Airport |  | ES | 763 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 745 |
| 34 | Calgary International Airport |  | CA | 712 |
| 35 | Vitoria/Foronda Airport |  | ES | 708 |
| 36 | Amsterdam Airport Schiphol |  | NL | 701 |
| 37 | Scottsdale Airport |  | US | 699 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 698 |
| 39 | Seattle-Tacoma International Airport |  | US | 697 |
| 40 | Don Mueang International Airport |  | TH | 694 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 631 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 443 | 21m | 244 km | 1,865.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 318 | 24m | 225 km | 1,233.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 309 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 239 | 26m | 275 km | 1,132.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 225 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 165 | 27m | 152 km | 431.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 156 | 31m | 369 km | 993.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 153 | 1h 44m | 1,423 km | 3,754.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 152 | 18m | 144 km | 378.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 137 | 1h 17m | 961 km | 2,270.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 133 | 29m | 49 km | 112.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RDHK705 | RDH | Felker Army Air Field (KFAF) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-06-26 21:05 UTC | 2026-06-26 21:32 UTC | 26m |
| N8PQ |  | San Bernardino International Airport (KSBD) | 9CL4 (9CL4) | 2026-06-26 21:01 UTC | 2026-06-26 21:30 UTC | 29m |
| N9637Q |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-06-26 20:53 UTC | 2026-06-26 21:29 UTC | 36m |
| N737BC |  | San Luis Obispo County Regional Airport (KSBP) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-26 21:08 UTC | 2026-06-26 21:26 UTC | 18m |
| SFE2 | SFE | Spicewood Airport (K88R) | Bud Dryden Airport (TX05) | 2026-06-26 21:11 UTC | 2026-06-26 21:23 UTC | 11m |
| LS36 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-26 19:55 UTC | 2026-06-26 21:22 UTC | 1h 26m |
| BULET41 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-26 20:09 UTC | 2026-06-26 21:22 UTC | 1h 12m |
| PBR680 | PBR | Victoria International Airport (CYYJ) | Boundary Bay Airport (CZBB) | 2026-06-26 21:07 UTC | 2026-06-26 21:20 UTC | 12m |
| N798DS |  | Nevada County Airport (KGOO) | San Carlos Airport (KSQL) | 2026-06-26 19:52 UTC | 2026-06-26 21:18 UTC | 1h 25m |
| TRA6935 | TRA | Amsterdam Airport Schiphol (EHAM) | Niksic Airport (LYNK) | 2026-06-26 19:22 UTC | 2026-06-26 21:10 UTC | 1h 47m |
| N334BG |  | Wood County Airport (K1G0) | Bluffton Airport (K5G7) | 2026-06-26 20:44 UTC | 2026-06-26 21:06 UTC | 21m |
| N446SP |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-06-26 20:28 UTC | 2026-06-26 21:05 UTC | 37m |
| N948CH |  | Santa Fe Regional Airport (KSAF) | Los Alamos Airport (KLAM) | 2026-06-26 20:39 UTC | 2026-06-26 21:00 UTC | 20m |
| CGMPY | CGM | Edmonton International Airport (CYEG) | Regina Beach Airport (CKL9) | 2026-06-26 19:31 UTC | 2026-06-26 20:56 UTC | 1h 25m |
| N456TC |  | Austin-Bergstrom International Airport (KAUS) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-06-26 19:04 UTC | 2026-06-26 20:53 UTC | 1h 48m |
| N137MH |  | Flying W Airport (KN14) | Inductotherm Airport (3NJ6) | 2026-06-26 20:41 UTC | 2026-06-26 20:51 UTC | 10m |
| N406DS |  | Delaware Airpark (K33N) | Lancaster Airport (KLNS) | 2026-06-26 20:02 UTC | 2026-06-26 20:50 UTC | 48m |
| SYB183 | SYB | Reno/Tahoe International Airport (KRNO) | Calgary International Airport (CYYC) | 2026-06-26 19:13 UTC | 2026-06-26 20:50 UTC | 1h 37m |
| JBU96 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-26 20:20 UTC | 2026-06-26 20:49 UTC | 29m |
| EJA567 | EJA | Chester County G O Carlson Airport (KMQS) | Odell Williamson Municipal Airport (K60J) | 2026-06-26 19:38 UTC | 2026-06-26 20:44 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
