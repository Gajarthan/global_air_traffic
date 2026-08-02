# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_08:32:23_UTC-green)

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

**Latest saved flight:** 2026-08-02 08:32:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 08:32:23 UTC

- **166,126** saved flights
- **54,449** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,126** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,999,843.4 tonnes** estimated CO2 emissions
- **115,932,951 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6629 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2923 |
| 5 | American Airlines | 2623 |
| 6 | Southwest Airlines | 2614 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1985 |
| 9 | LATAM Airlines | 1547 |
| 10 | Lufthansa | 1538 |
| 11 | AZU | 1455 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1372 |
| 14 | LXJ | 1290 |
| 15 | AXM | 1149 |
| 16 | Swiss International | 1138 |
| 17 | easyJet | 1095 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1020 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1014 |
| 22 | VIV | 916 |
| 23 | Cathay Pacific | 886 |
| 24 | CXK | 886 |
| 25 | United Airlines | 877 |
| 26 | AEE | 874 |
| 27 | GLO | 869 |
| 28 | Air France | 857 |
| 29 | MXY | 857 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143417 |
| 2 | 🇪🇸 ES | 10617 |
| 3 | 🇧🇷 BR | 9450 |
| 4 | 🇦🇺 AU | 9326 |
| 5 | 🇮🇳 IN | 9166 |
| 6 | 🇨🇦 CA | 9022 |
| 7 | 🇮🇹 IT | 8582 |
| 8 | 🇩🇪 DE | 8294 |
| 9 | 🇬🇧 GB | 7640 |
| 10 | 🇯🇵 JP | 6710 |
| 11 | 🇫🇷 FR | 6579 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4806 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4365 |
| 16 | 🇳🇴 NO | 4343 |
| 17 | 🇹🇷 TR | 3996 |
| 18 | 🇲🇾 MY | 2992 |
| 19 | 🇵🇱 PL | 2809 |
| 20 | 🇿🇦 ZA | 2703 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2392 |
| 23 | 🇵🇭 PH | 2196 |
| 24 | 🇰🇷 KR | 2143 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1671 |
| 27 | 🇭🇷 HR | 1578 |
| 28 | 🇲🇪 ME | 1546 |
| 29 | 🇳🇱 NL | 1507 |
| 30 | 🇲🇴 MO | 1419 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3399 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2108 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2032 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1827 |
| 8 | Zurich Airport |  | CH | 1765 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1745 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1502 |
| 14 | Chicago O'Hare International Airport |  | US | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1419 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1308 |
| 20 | Capua Airport |  | IT | 1298 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1173 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1133 |
| 26 | Kuala Lumpur International Airport |  | MY | 1132 |
| 27 | Malpensa International Airport |  | IT | 1110 |
| 28 | Bengaluru International Airport |  | IN | 1084 |
| 29 | Ninoy Aquino International Airport |  | PH | 1032 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 981 |
| 33 | Daniel K Inouye International Airport |  | US | 970 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 941 |
| 37 | Scottsdale Airport |  | US | 926 |
| 38 | Tenerife Norte Airport |  | ES | 923 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 378 | 1h 9m | 770 km | 5,021.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 311 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 291 | 1h 7m | 706 km | 3,542.9 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 218 | 20m | 250 km | 941.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 195 | 19m | 144 km | 485.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 179 | 24m | 218 km | 674.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBCDE | HBC | Hausen am Albis Airport (LSZN) | Raron Airport (LSTA) | 2026-08-02 07:24 UTC | 2026-08-02 08:32 UTC | 1h 8m |
| AMU611 | AMU | Taiwan Taoyuan International Airport (RCTP) | Macau International Airport (VMMC) | 2026-08-02 07:09 UTC | 2026-08-02 08:27 UTC | 1h 18m |
| PGC24B | PGC | Palma De Mallorca Airport (LEPA) | Nimes-Arles-Camargue Airport (LFTW) | 2026-08-02 07:20 UTC | 2026-08-02 08:16 UTC | 55m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-08-01 21:12 UTC | 2026-08-02 08:02 UTC | 10h 50m |
| FBXZP | FBX | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Etrepagny Airport (LFFY) | 2026-08-02 07:43 UTC | 2026-08-02 07:59 UTC | 16m |
| SJX841 | SJX | Fukuoka Airport (RJFF) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-02 06:14 UTC | 2026-08-02 07:56 UTC | 1h 42m |
| AXM6419 | AXM | Kroh Airport (WMBH) | Batu Pahat Airport (WMAB) | 2026-08-02 07:12 UTC | 2026-08-02 07:52 UTC | 40m |
| CPA064 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-08-01 20:51 UTC | 2026-08-02 07:51 UTC | 11h 0m |
| N412P |  | Houston/Southwest Airport (KAXH) | William P Hobby Airport (KHOU) | 2026-08-02 07:43 UTC | 2026-08-02 07:50 UTC | 6m |
| RYR8KM | Ryanair | London Stansted Airport (EGSS) | Bari / Palese International Airport (LIBD) | 2026-08-02 05:41 UTC | 2026-08-02 07:49 UTC | 2h 8m |
| VLG59SX | Vueling | Paris-Orly Airport (LFPO) | Castellón De La Plana Airport (LECN) | 2026-08-02 06:26 UTC | 2026-08-02 07:48 UTC | 1h 22m |
| QLK42D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-08-02 07:18 UTC | 2026-08-02 07:47 UTC | 29m |
| AXM6331 | AXM | Kuala Lumpur International Airport (WMKK) | Penang International Airport (WMKP) | 2026-08-02 07:17 UTC | 2026-08-02 07:45 UTC | 28m |
| N776EE |  | London Stansted Airport (EGSS) | Zurich Airport (LSZH) | 2026-08-02 06:36 UTC | 2026-08-02 07:43 UTC | 1h 7m |
| KLM91Z | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Brussels Airport (EBBR) | 2026-08-02 07:12 UTC | 2026-08-02 07:43 UTC | 30m |
| ZKIGB | ZKI | Christchurch International Airport (NZCH) | Christchurch International Airport (NZCH) | 2026-08-02 06:48 UTC | 2026-08-02 07:42 UTC | 54m |
| 5YZBY |  | Nairobi Wilson Airport (HKNW) | Naivasha Airport (HKNV) | 2026-08-02 07:25 UTC | 2026-08-02 07:41 UTC | 15m |
| EZY187Q | easyJet | Glasgow International Airport (EGPF) | Belfast International Airport (EGAA) | 2026-08-02 07:15 UTC | 2026-08-02 07:40 UTC | 24m |
| ZSTOB | ZST | Lanseria Airport (FALA) | Thabazimbi Airport (FATI) | 2026-08-02 07:17 UTC | 2026-08-02 07:39 UTC | 21m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-08-02 07:09 UTC | 2026-08-02 07:39 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
