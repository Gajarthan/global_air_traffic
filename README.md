# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_00:52:09_UTC-green)

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

**Latest saved flight:** 2026-07-16 00:52:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-16 00:52:09 UTC

- **141,786** saved flights
- **47,592** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,786** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,701,634.8 tonnes** estimated CO2 emissions
- **98,645,495 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5767 |
| 2 | SkyWest Airlines | 5185 |
| 3 | EJA | 2791 |
| 4 | IndiGo | 2591 |
| 5 | American Airlines | 2259 |
| 6 | Southwest Airlines | 2136 |
| 7 | ENY | 1759 |
| 8 | Delta Air Lines | 1677 |
| 9 | Lufthansa | 1430 |
| 10 | LATAM Airlines | 1304 |
| 11 | Vueling | 1220 |
| 12 | AZU | 1216 |
| 13 | WIF | 1216 |
| 14 | LXJ | 1088 |
| 15 | AXM | 1053 |
| 16 | Swiss International | 1008 |
| 17 | easyJet | 923 |
| 18 | All Nippon Airways | 911 |
| 19 | Alaska Airlines | 893 |
| 20 | QLK | 892 |
| 21 | EJU | 874 |
| 22 | VIV | 785 |
| 23 | AEE | 758 |
| 24 | CXK | 757 |
| 25 | Air France | 755 |
| 26 | JetBlue | 755 |
| 27 | United Airlines | 738 |
| 28 | MXY | 734 |
| 29 | Cathay Pacific | 733 |
| 30 | GLO | 725 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121931 |
| 2 | 🇪🇸 ES | 9261 |
| 3 | 🇦🇺 AU | 8134 |
| 4 | 🇮🇳 IN | 8119 |
| 5 | 🇧🇷 BR | 7996 |
| 6 | 🇨🇦 CA | 7459 |
| 7 | 🇮🇹 IT | 7389 |
| 8 | 🇩🇪 DE | 7361 |
| 9 | 🇬🇧 GB | 6471 |
| 10 | 🇯🇵 JP | 5953 |
| 11 | 🇫🇷 FR | 5639 |
| 12 | 🇨🇴 CO | 4518 |
| 13 | 🇲🇽 MX | 4115 |
| 14 | 🇬🇷 GR | 4031 |
| 15 | 🇳🇴 NO | 3805 |
| 16 | 🇨🇭 CH | 3668 |
| 17 | 🇹🇷 TR | 3352 |
| 18 | 🇲🇾 MY | 2747 |
| 19 | 🇵🇱 PL | 2375 |
| 20 | 🇿🇦 ZA | 2316 |
| 21 | 🇳🇿 NZ | 2172 |
| 22 | 🇹🇭 TH | 2120 |
| 23 | 🇰🇷 KR | 2019 |
| 24 | 🇵🇭 PH | 1914 |
| 25 | 🇬🇹 GT | 1866 |
| 26 | 🇲🇦 MA | 1488 |
| 27 | 🇲🇪 ME | 1404 |
| 28 | 🇳🇱 NL | 1333 |
| 29 | 🇭🇷 HR | 1290 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2917 |
| 2 | Denver International Airport |  | US | 2370 |
| 3 | Tokyo International Airport |  | JP | 1924 |
| 4 | Indira Gandhi International Airport |  | IN | 1801 |
| 5 | Harry Reid International Airport |  | US | 1777 |
| 6 | Guaymaral Airport |  | CO | 1728 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1625 |
| 8 | Zurich Airport |  | CH | 1576 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1485 |
| 10 | La Aurora Airport |  | GT | 1443 |
| 11 | Frankfurt am Main International Airport |  | DE | 1380 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1348 |
| 13 | Chicago O'Hare International Airport |  | US | 1329 |
| 14 | Salt Lake City International Airport |  | US | 1269 |
| 15 | El Dorado International Airport |  | CO | 1254 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1241 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1159 |
| 19 | Madrid Barajas International Airport |  | ES | 1143 |
| 20 | Congonhas Airport |  | BR | 1137 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1128 |
| 22 | Kuala Lumpur International Airport |  | MY | 1060 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1031 |
| 24 | Charlotte/Douglas International Airport |  | US | 1027 |
| 25 | Charles de Gaulle International Airport |  | FR | 1000 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 989 |
| 27 | Bengaluru International Airport |  | IN | 971 |
| 28 | Malpensa International Airport |  | IT | 918 |
| 29 | Ninoy Aquino International Airport |  | PH | 893 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 867 |
| 31 | Daniel K Inouye International Airport |  | US | 866 |
| 32 | Barcelona International Airport |  | ES | 863 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 837 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Seattle-Tacoma International Airport |  | US | 804 |
| 37 | Viracopos International Airport |  | BR | 803 |
| 38 | Scottsdale Airport |  | US | 803 |
| 39 | Amsterdam Airport Schiphol |  | NL | 801 |
| 40 | Oslo Gardermoen Airport |  | NO | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 728 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 516 | 21m | 244 km | 2,172.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 345 | 24m | 225 km | 1,338.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 336 | 1h 9m | 770 km | 4,463.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 208 | 22m | 55 km | 197.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 191 | 1h 46m | 1,423 km | 4,687.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 166 | 44m | 452 km | 1,293.7 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 163 | 1h 1m | 695 km | 1,953.9 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 159 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5125B |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-07-16 00:38 UTC | 2026-07-16 00:52 UTC | 13m |
| CIRCF2B | CIR | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-16 00:39 UTC | 2026-07-16 00:51 UTC | 12m |
| N438H |  | Newark Liberty International Airport (KEWR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-15 23:36 UTC | 2026-07-16 00:50 UTC | 1h 13m |
| G26042 |  | New Castle Airport (KILG) | Millville Municipal Airport (KMIV) | 2026-07-16 00:20 UTC | 2026-07-16 00:49 UTC | 29m |
| HOOVR35 | HOO | Offutt Afb Airport (KOFF) | 82IN (82IN) | 2026-07-15 23:36 UTC | 2026-07-16 00:47 UTC | 1h 11m |
| N965LA |  | Barrett Airport (MN18) | St Paul Downtown Holman Field (KSTP) | 2026-07-15 23:58 UTC | 2026-07-16 00:45 UTC | 47m |
| AAL1925 | American Airlines | George Bush Intcntl/Houston Airport (KIAH) | Philadelphia International Airport (KPHL) | 2026-07-15 21:41 UTC | 2026-07-16 00:43 UTC | 3h 1m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-16 00:01 UTC | 2026-07-16 00:40 UTC | 38m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-15 22:39 UTC | 2026-07-16 00:38 UTC | 1h 59m |
| TKR106 | TKR | Grand Junction Regional Airport (KGJT) | Pinyon Airport (CO43) | 2026-07-16 00:33 UTC | 2026-07-16 00:36 UTC | 3m |
| STGRY32 | STG | Whites Airport (47TE) | Easterwood Field (KCLL) | 2026-07-15 23:42 UTC | 2026-07-16 00:36 UTC | 53m |
| TKR184 | TKR | Grand Junction Regional Airport (KGJT) | Pinyon Airport (CO43) | 2026-07-16 00:30 UTC | 2026-07-16 00:34 UTC | 4m |
| CGTIM | CGT | Thunder Bay Airport (CYQT) | Pikangikum Airport (CYPM) | 2026-07-15 22:53 UTC | 2026-07-16 00:34 UTC | 1h 40m |
| TKR104 | TKR | Desert Wings Sky Ranch Airport (04CL) | San Bernardino International Airport (KSBD) | 2026-07-16 00:15 UTC | 2026-07-16 00:33 UTC | 17m |
| HK5297G |  | El Eden Airport (SKAR) | El Eden Airport (SKAR) | 2026-07-15 23:40 UTC | 2026-07-16 00:32 UTC | 52m |
| AAL3319 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-15 19:33 UTC | 2026-07-16 00:31 UTC | 4h 57m |
| N619PF |  | Willaview Airport (2DE2) | DE10 (DE10) | 2026-07-16 00:19 UTC | 2026-07-16 00:31 UTC | 11m |
| AAL1590 | American Airlines | Hartsfield/Jackson Atlanta International Airport (KATL) | Philadelphia International Airport (KPHL) | 2026-07-15 22:46 UTC | 2026-07-16 00:31 UTC | 1h 45m |
| CASTL30 | CAS | New Castle Airport (KILG) | New Castle Airport (KILG) | 2026-07-15 23:22 UTC | 2026-07-16 00:30 UTC | 1h 8m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-07-16 00:01 UTC | 2026-07-16 00:29 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
