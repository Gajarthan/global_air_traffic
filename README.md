# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_21:34:45_UTC-green)

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

**Latest saved flight:** 2026-07-27 21:34:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 21:34:45 UTC

- **155,501** saved flights
- **51,757** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,501** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,864,702.5 tonnes** estimated CO2 emissions
- **108,098,696 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6259 |
| 2 | SkyWest Airlines | 5707 |
| 3 | EJA | 3087 |
| 4 | IndiGo | 2754 |
| 5 | American Airlines | 2482 |
| 6 | Southwest Airlines | 2447 |
| 7 | ENY | 1942 |
| 8 | Delta Air Lines | 1853 |
| 9 | Lufthansa | 1499 |
| 10 | LATAM Airlines | 1446 |
| 11 | AZU | 1355 |
| 12 | WIF | 1310 |
| 13 | Vueling | 1301 |
| 14 | LXJ | 1195 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1083 |
| 17 | easyJet | 1014 |
| 18 | Alaska Airlines | 977 |
| 19 | All Nippon Airways | 967 |
| 20 | QLK | 966 |
| 21 | EJU | 953 |
| 22 | VIV | 857 |
| 23 | United Airlines | 834 |
| 24 | CXK | 824 |
| 25 | MXY | 813 |
| 26 | AEE | 812 |
| 27 | GLO | 812 |
| 28 | JetBlue | 812 |
| 29 | Air France | 807 |
| 30 | Cathay Pacific | 795 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134379 |
| 2 | 🇪🇸 ES | 10017 |
| 3 | 🇧🇷 BR | 8856 |
| 4 | 🇦🇺 AU | 8774 |
| 5 | 🇮🇳 IN | 8651 |
| 6 | 🇨🇦 CA | 8371 |
| 7 | 🇮🇹 IT | 8023 |
| 8 | 🇩🇪 DE | 7898 |
| 9 | 🇬🇧 GB | 7137 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6145 |
| 12 | 🇨🇴 CO | 5379 |
| 13 | 🇲🇽 MX | 4469 |
| 14 | 🇬🇷 GR | 4417 |
| 15 | 🇳🇴 NO | 4104 |
| 16 | 🇨🇭 CH | 4059 |
| 17 | 🇹🇷 TR | 3703 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2649 |
| 20 | 🇿🇦 ZA | 2509 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2040 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1585 |
| 27 | 🇲🇪 ME | 1509 |
| 28 | 🇭🇷 HR | 1431 |
| 29 | 🇳🇱 NL | 1424 |
| 30 | 🇲🇴 MO | 1270 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3200 |
| 2 | Denver International Airport |  | US | 2616 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1954 |
| 5 | Indira Gandhi International Airport |  | IN | 1917 |
| 6 | Harry Reid International Airport |  | US | 1913 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1724 |
| 8 | Zurich Airport |  | CH | 1681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1631 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1450 |
| 12 | Frankfurt am Main International Airport |  | DE | 1447 |
| 13 | Chicago O'Hare International Airport |  | US | 1421 |
| 14 | Salt Lake City International Airport |  | US | 1404 |
| 15 | El Dorado International Airport |  | CO | 1401 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1318 |
| 17 | Macau International Airport |  | MO | 1270 |
| 18 | Congonhas Airport |  | BR | 1265 |
| 19 | Madrid Barajas International Airport |  | ES | 1235 |
| 20 | Capua Airport |  | IT | 1228 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1195 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1106 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1104 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1063 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1014 |
| 29 | Ninoy Aquino International Airport |  | PH | 956 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 945 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 941 |
| 32 | Barcelona International Airport |  | ES | 923 |
| 33 | Daniel K Inouye International Airport |  | US | 922 |
| 34 | Seattle-Tacoma International Airport |  | US | 906 |
| 35 | Tenerife Norte Airport |  | ES | 891 |
| 36 | Calgary International Airport |  | CA | 889 |
| 37 | Scottsdale Airport |  | US | 881 |
| 38 | Viracopos International Airport |  | BR | 880 |
| 39 | Amsterdam Airport Schiphol |  | NL | 862 |
| 40 | Oslo Gardermoen Airport |  | NO | 854 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 561 | 21m | 244 km | 2,362.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 214 | 44m | 241 km | 888.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 199 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 196 | 20m | 250 km | 846.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 183 | 18m | 144 km | 455.2 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 180 | 31m | 369 km | 1,145.7 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 175 | 50m | 556 km | 1,677.5 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 173 | 1h 39m | 1,156 km | 3,451.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 164 | 1h 50m | 1,304 km | 3,689.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N828AK |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-07-27 20:22 UTC | 2026-07-27 21:34 UTC | 1h 12m |
| ANA113 | All Nippon Airways | George Bush Intcntl/Houston Airport (KIAH) | Nampa / Hockey (CNP6) | 2026-07-27 17:32 UTC | 2026-07-27 21:31 UTC | 3h 59m |
| KAL240 | Korean Air | Chicago O'Hare International Airport (KORD) | Debolt Airport (CFG4) | 2026-07-27 17:59 UTC | 2026-07-27 21:31 UTC | 3h 32m |
| KAL8235 | Korean Air | Ted Stevens Anchorage International Airport (PANC) | Fort St. John Airport (CYXJ) | 2026-07-27 19:27 UTC | 2026-07-27 21:31 UTC | 2h 4m |
| CAO1049 | CAO | Ted Stevens Anchorage International Airport (PANC) | Debolt Airport (CFG4) | 2026-07-27 19:17 UTC | 2026-07-27 21:31 UTC | 2h 14m |
| BAW87 | British Airways | London Heathrow Airport (EGLL) | Grimshaw Airport (CFD5) | 2026-07-27 13:32 UTC | 2026-07-27 21:31 UTC | 7h 59m |
| RAM819I | Royal Air Maroc | Manchester Airport (EGCC) | Mohammed V International Airport (GMMN) | 2026-07-27 18:24 UTC | 2026-07-27 21:19 UTC | 2h 54m |
| TKR210 | TKR | Roberts Field (KRDM) | Muddy Creek Airport (OG27) | 2026-07-27 20:54 UTC | 2026-07-27 21:14 UTC | 20m |
| ENSAIO83 | ENS | Fazenda Sao Francisco do Itaquere Airport (SDNL) | Fazenda Santa Maria Airport (SDDJ) | 2026-07-27 20:58 UTC | 2026-07-27 21:14 UTC | 16m |
| SH185 |  | Skypark Estates Owners Assoc Airport (18FD) | Monroe County Aeroplex Airport (KMVC) | 2026-07-27 21:04 UTC | 2026-07-27 21:14 UTC | 10m |
| GRZLY01 | GRZ | Brussels Airport (EBBR) | Melsbroek Air Base (EBMB) | 2026-07-27 20:11 UTC | 2026-07-27 20:58 UTC | 46m |
| QTR69T | Qatar Airways | Dublin Airport (EIDW) | Al Khawr Airport (OTBK) | 2026-07-27 14:32 UTC | 2026-07-27 20:55 UTC | 6h 22m |
| VAR488 | VAR | Phoenix Goodyear Airport (KGYR) | Gila Bend Municipal Airport (KE63) | 2026-07-27 20:35 UTC | 2026-07-27 20:53 UTC | 17m |
| CAP3733 | CAP | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-07-27 20:05 UTC | 2026-07-27 20:51 UTC | 45m |
| N101PV |  | Harry Reid International Airport (KLAS) | Mcnary Field (KSLE) | 2026-07-27 19:12 UTC | 2026-07-27 20:49 UTC | 1h 36m |
| N875MR |  | Dillingham Airport (PADL) | King Salmon Airport (PAKN) | 2026-07-27 20:24 UTC | 2026-07-27 20:47 UTC | 23m |
| N93BH |  | General Edward Lawrence Logan International Airport (KBOS) | Katama Airpark (K1B2) | 2026-07-27 20:04 UTC | 2026-07-27 20:47 UTC | 43m |
| N5317W |  | Livermore Municipal Airport (KLVK) | Byron Airport (KC83) | 2026-07-27 20:38 UTC | 2026-07-27 20:46 UTC | 7m |
| N621HD |  | Orlando International Airport (KMCO) | Flying Cloud Airport (KFCM) | 2026-07-27 17:39 UTC | 2026-07-27 20:43 UTC | 3h 4m |
| N5195Y |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-07-27 20:42 UTC | 2026-07-27 20:43 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
