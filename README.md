# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_12:52:12_UTC-green)

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

**Latest saved flight:** 2026-07-26 12:52:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 12:52:12 UTC

- **151,983** saved flights
- **50,440** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,983** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,819,429.1 tonnes** estimated CO2 emissions
- **105,474,149 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6138 |
| 2 | SkyWest Airlines | 5554 |
| 3 | EJA | 3000 |
| 4 | IndiGo | 2716 |
| 5 | American Airlines | 2410 |
| 6 | Southwest Airlines | 2310 |
| 7 | ENY | 1895 |
| 8 | Delta Air Lines | 1781 |
| 9 | Lufthansa | 1484 |
| 10 | LATAM Airlines | 1407 |
| 11 | AZU | 1318 |
| 12 | WIF | 1279 |
| 13 | Vueling | 1273 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1088 |
| 16 | Swiss International | 1067 |
| 17 | easyJet | 994 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 949 |
| 20 | QLK | 941 |
| 21 | EJU | 933 |
| 22 | VIV | 836 |
| 23 | CXK | 812 |
| 24 | AEE | 800 |
| 25 | MXY | 798 |
| 26 | Air France | 792 |
| 27 | JetBlue | 790 |
| 28 | GLO | 788 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130907 |
| 2 | 🇪🇸 ES | 9829 |
| 3 | 🇧🇷 BR | 8607 |
| 4 | 🇦🇺 AU | 8595 |
| 5 | 🇮🇳 IN | 8545 |
| 6 | 🇨🇦 CA | 8098 |
| 7 | 🇮🇹 IT | 7875 |
| 8 | 🇩🇪 DE | 7787 |
| 9 | 🇬🇧 GB | 6976 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6030 |
| 12 | 🇨🇴 CO | 5175 |
| 13 | 🇲🇽 MX | 4375 |
| 14 | 🇬🇷 GR | 4330 |
| 15 | 🇳🇴 NO | 4016 |
| 16 | 🇨🇭 CH | 3997 |
| 17 | 🇹🇷 TR | 3623 |
| 18 | 🇲🇾 MY | 2836 |
| 19 | 🇵🇱 PL | 2598 |
| 20 | 🇿🇦 ZA | 2472 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2217 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2023 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1548 |
| 27 | 🇲🇪 ME | 1487 |
| 28 | 🇳🇱 NL | 1397 |
| 29 | 🇭🇷 HR | 1397 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3128 |
| 2 | Denver International Airport |  | US | 2547 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1907 |
| 5 | Indira Gandhi International Airport |  | IN | 1897 |
| 6 | Harry Reid International Airport |  | US | 1873 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1705 |
| 8 | Zurich Airport |  | CH | 1657 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1587 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1420 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | El Dorado International Airport |  | CO | 1369 |
| 15 | Salt Lake City International Airport |  | US | 1365 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1295 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1231 |
| 19 | Madrid Barajas International Airport |  | ES | 1213 |
| 20 | Capua Airport |  | IT | 1207 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1175 |
| 22 | Kuala Lumpur International Airport |  | MY | 1090 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1070 |
| 26 | Charles de Gaulle International Airport |  | FR | 1043 |
| 27 | Bengaluru International Airport |  | IN | 1021 |
| 28 | Malpensa International Airport |  | IT | 997 |
| 29 | Ninoy Aquino International Airport |  | PH | 947 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 918 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 909 |
| 32 | Daniel K Inouye International Airport |  | US | 908 |
| 33 | Barcelona International Airport |  | ES | 908 |
| 34 | Tenerife Norte Airport |  | ES | 877 |
| 35 | Seattle-Tacoma International Airport |  | US | 875 |
| 36 | Calgary International Airport |  | CA | 862 |
| 37 | Viracopos International Airport |  | BR | 858 |
| 38 | Scottsdale Airport |  | US | 855 |
| 39 | Amsterdam Airport Schiphol |  | NL | 840 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 834 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 804 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 552 | 21m | 244 km | 2,324.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 278 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 273 | 27m | 275 km | 1,293.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 205 | 1h 47m | 1,423 km | 5,031.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 199 | 26m | 215 km | 737.0 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 197 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 184 | 30m | 49 km | 155.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 168 | 51m | 556 km | 1,610.4 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FBUMC | FBU | Redon Bains-sur-Oust Airport (LFER) | Redon Bains-sur-Oust Airport (LFER) | 2026-07-26 12:25 UTC | 2026-07-26 12:52 UTC | 26m |
| SCQ26R | SCQ | Gullknapp Flpl Airport (ENGK) | Kristiansand Airport (ENCN) | 2026-07-26 12:29 UTC | 2026-07-26 12:50 UTC | 21m |
| N43956 |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-07-26 12:34 UTC | 2026-07-26 12:46 UTC | 12m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-26 12:09 UTC | 2026-07-26 12:38 UTC | 29m |
| N821SS |  | Newark Liberty International Airport (KEWR) | Teterboro Airport (KTEB) | 2026-07-26 12:23 UTC | 2026-07-26 12:27 UTC | 3m |
| CXK461 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-26 11:56 UTC | 2026-07-26 12:24 UTC | 27m |
| DEEWY | DEE | Thiene Airport (LIDH) | Thiene Airport (LIDH) | 2026-07-26 12:04 UTC | 2026-07-26 12:14 UTC | 10m |
| A6FTK |  | Al Minhad Air Base (OMDM) | Al Maktoum International Airport (OMDW) | 2026-07-26 11:57 UTC | 2026-07-26 12:14 UTC | 17m |
| HK5463X |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-07-26 11:43 UTC | 2026-07-26 12:13 UTC | 29m |
| A6FNG |  | Al Saqr Field (OMRS) | Ras Al Khaimah International Airport (OMRK) | 2026-07-26 12:09 UTC | 2026-07-26 12:09 UTC | 0m |
| AEE244 | AEE | Eleftherios Venizelos International Airport (LGAV) | Samos Airport (LGSM) | 2026-07-26 11:30 UTC | 2026-07-26 12:06 UTC | 36m |
| NSZ4513 | NSZ | Stockholm-Arlanda Airport (ESSA) | Hamburg Airport (EDDH) | 2026-07-26 10:51 UTC | 2026-07-26 12:06 UTC | 1h 14m |
| EAI23C | EAI | Glasgow International Airport (EGPF) | Dublin Airport (EIDW) | 2026-07-26 11:09 UTC | 2026-07-26 12:03 UTC | 53m |
| AAH50 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-26 11:41 UTC | 2026-07-26 12:02 UTC | 21m |
| EZY2427 | easyJet | London Luton Airport (EGGW) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-26 10:15 UTC | 2026-07-26 12:01 UTC | 1h 45m |
| RYR5YZ | Ryanair | Bristol International Airport (EGGD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-26 09:53 UTC | 2026-07-26 11:59 UTC | 2h 6m |
| SPHOR | SPH | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-07-26 11:50 UTC | 2026-07-26 11:57 UTC | 7m |
| UIA8977 | UIA | Taipei Songshan Airport (RCSS) | Longtan Air Base (RCDI) | 2026-07-26 11:43 UTC | 2026-07-26 11:56 UTC | 13m |
| N150RF |  | Syracuse Hancock International Airport (KSYR) | Billy Bishop Toronto City Airport (CYTZ) | 2026-07-26 11:18 UTC | 2026-07-26 11:56 UTC | 37m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-26 11:44 UTC | 2026-07-26 11:55 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
