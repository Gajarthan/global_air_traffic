# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_14:31:41_UTC-green)

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

**Latest saved flight:** 2026-07-26 14:31:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 14:31:41 UTC

- **152,139** saved flights
- **50,488** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **152,139** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,821,005.2 tonnes** estimated CO2 emissions
- **105,565,517 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6146 |
| 2 | SkyWest Airlines | 5555 |
| 3 | EJA | 3003 |
| 4 | IndiGo | 2720 |
| 5 | American Airlines | 2410 |
| 6 | Southwest Airlines | 2314 |
| 7 | ENY | 1895 |
| 8 | Delta Air Lines | 1782 |
| 9 | Lufthansa | 1486 |
| 10 | LATAM Airlines | 1407 |
| 11 | AZU | 1323 |
| 12 | WIF | 1281 |
| 13 | Vueling | 1273 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1089 |
| 16 | Swiss International | 1067 |
| 17 | easyJet | 994 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 949 |
| 20 | QLK | 941 |
| 21 | EJU | 936 |
| 22 | VIV | 838 |
| 23 | CXK | 813 |
| 24 | AEE | 801 |
| 25 | MXY | 801 |
| 26 | Air France | 792 |
| 27 | JetBlue | 790 |
| 28 | GLO | 789 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 131018 |
| 2 | 🇪🇸 ES | 9840 |
| 3 | 🇧🇷 BR | 8626 |
| 4 | 🇦🇺 AU | 8595 |
| 5 | 🇮🇳 IN | 8552 |
| 6 | 🇨🇦 CA | 8107 |
| 7 | 🇮🇹 IT | 7889 |
| 8 | 🇩🇪 DE | 7798 |
| 9 | 🇬🇧 GB | 6986 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6032 |
| 12 | 🇨🇴 CO | 5185 |
| 13 | 🇲🇽 MX | 4379 |
| 14 | 🇬🇷 GR | 4337 |
| 15 | 🇳🇴 NO | 4021 |
| 16 | 🇨🇭 CH | 4000 |
| 17 | 🇹🇷 TR | 3627 |
| 18 | 🇲🇾 MY | 2837 |
| 19 | 🇵🇱 PL | 2605 |
| 20 | 🇿🇦 ZA | 2477 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2220 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1549 |
| 27 | 🇲🇪 ME | 1487 |
| 28 | 🇭🇷 HR | 1402 |
| 29 | 🇳🇱 NL | 1399 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3128 |
| 2 | Denver International Airport |  | US | 2548 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1908 |
| 5 | Indira Gandhi International Airport |  | IN | 1898 |
| 6 | Harry Reid International Airport |  | US | 1873 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1707 |
| 8 | Zurich Airport |  | CH | 1658 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1588 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1433 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1420 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | El Dorado International Airport |  | CO | 1371 |
| 15 | Salt Lake City International Airport |  | US | 1365 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1295 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1232 |
| 19 | Madrid Barajas International Airport |  | ES | 1214 |
| 20 | Capua Airport |  | IT | 1209 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1176 |
| 22 | Kuala Lumpur International Airport |  | MY | 1090 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1070 |
| 26 | Charles de Gaulle International Airport |  | FR | 1043 |
| 27 | Bengaluru International Airport |  | IN | 1022 |
| 28 | Malpensa International Airport |  | IT | 1000 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 920 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 909 |
| 32 | Barcelona International Airport |  | ES | 909 |
| 33 | Daniel K Inouye International Airport |  | US | 908 |
| 34 | Tenerife Norte Airport |  | ES | 877 |
| 35 | Seattle-Tacoma International Airport |  | US | 875 |
| 36 | Viracopos International Airport |  | BR | 863 |
| 37 | Calgary International Airport |  | CA | 862 |
| 38 | Scottsdale Airport |  | US | 858 |
| 39 | Amsterdam Airport Schiphol |  | NL | 842 |
| 40 | Oslo Gardermoen Airport |  | NO | 834 |

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
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 279 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 273 | 27m | 275 km | 1,293.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 206 | 44m | 241 km | 855.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 205 | 1h 47m | 1,423 km | 5,031.0 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 200 | 26m | 215 km | 740.7 t |
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
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 168 | 51m | 556 km | 1,610.4 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-07-26 14:08 UTC | 2026-07-26 14:31 UTC | 23m |
| N8604Q |  | Pueblo Memorial Airport (KPUB) | 1CO7 (1CO7) | 2026-07-26 13:58 UTC | 2026-07-26 14:30 UTC | 31m |
| N9737V |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-26 14:08 UTC | 2026-07-26 14:27 UTC | 19m |
| N257FD |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-26 14:11 UTC | 2026-07-26 14:24 UTC | 13m |
| N270AM |  | Van Zandt County Regional Airport (K76F) | Durant Regional/Eaker Field (KDUA) | 2026-07-26 13:37 UTC | 2026-07-26 14:23 UTC | 45m |
| TDT02 | TDT | London City Airport (EGLC) | Oxford (Kidlington) Airport (EGTK) | 2026-07-26 13:41 UTC | 2026-07-26 14:15 UTC | 34m |
| N79JS |  | Northeast Philadelphia Airport (KPNE) | Lehigh Valley International Airport (KABE) | 2026-07-26 13:55 UTC | 2026-07-26 14:13 UTC | 18m |
| N7725N |  | Athens Municipal Airport (KF44) | Sulphur Springs Municipal Airport (KSLR) | 2026-07-26 13:38 UTC | 2026-07-26 14:12 UTC | 34m |
| N305PT |  | Miami Executive Airport (KTMB) | Miami Homestead General Aviation Airport (KX51) | 2026-07-26 13:53 UTC | 2026-07-26 14:10 UTC | 17m |
| N1418A |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-07-26 13:24 UTC | 2026-07-26 14:10 UTC | 46m |
| DLH2WR | Lufthansa | Poznań-Ławica Airport (EPPO) | Frankfurt am Main International Airport (EDDF) | 2026-07-26 13:07 UTC | 2026-07-26 14:10 UTC | 1h 3m |
| N8106J |  | Aero Valley Airport (K52F) | Hicks Airfield (KT67) | 2026-07-26 14:00 UTC | 2026-07-26 14:08 UTC | 8m |
| N801HB |  | Scribner State Airport (KSCB) | Harlan Municipal Airport (KHNR) | 2026-07-26 12:55 UTC | 2026-07-26 14:07 UTC | 1h 11m |
| LIFE2 | LIF | George Bush Intcntl/Houston Airport (KIAH) | Houston/Southwest Airport (KAXH) | 2026-07-26 13:51 UTC | 2026-07-26 14:06 UTC | 14m |
| GJUNR | GJU | RNAS Lee-On-Solent (EGHF) | Bournemouth Airport (EGHH) | 2026-07-26 13:33 UTC | 2026-07-26 14:05 UTC | 32m |
| N9435W |  | Erie Municipal Airport (KEIK) | CO86 (CO86) | 2026-07-26 13:29 UTC | 2026-07-26 13:59 UTC | 30m |
| N801FL |  | Baldwin Airport (WI14) | Baldwin Airport (WI14) | 2026-07-26 13:36 UTC | 2026-07-26 13:56 UTC | 20m |
| ASI844 | ASI | Phoenix Deer Valley Airport (KDVT) | Buckeye Municipal Airport (KBXK) | 2026-07-26 13:00 UTC | 2026-07-26 13:55 UTC | 54m |
| SCU47 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-07-26 13:54 UTC | 2026-07-26 13:54 UTC | 0m |
| N518LM |  | Sky Ranch At Carefree Airport (18AZ) | Montezuma Airport (19AZ) | 2026-07-26 13:34 UTC | 2026-07-26 13:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
