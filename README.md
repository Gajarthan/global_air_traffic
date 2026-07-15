# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_13:35:19_UTC-green)

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

**Latest saved flight:** 2026-07-15 13:35:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-15 13:35:19 UTC

- **141,615** saved flights
- **47,556** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,615** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,699,906.4 tonnes** estimated CO2 emissions
- **98,545,301 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5767 |
| 2 | SkyWest Airlines | 5175 |
| 3 | EJA | 2788 |
| 4 | IndiGo | 2591 |
| 5 | American Airlines | 2252 |
| 6 | Southwest Airlines | 2131 |
| 7 | ENY | 1756 |
| 8 | Delta Air Lines | 1675 |
| 9 | Lufthansa | 1430 |
| 10 | LATAM Airlines | 1302 |
| 11 | Vueling | 1220 |
| 12 | AZU | 1216 |
| 13 | WIF | 1216 |
| 14 | LXJ | 1087 |
| 15 | AXM | 1053 |
| 16 | Swiss International | 1008 |
| 17 | easyJet | 923 |
| 18 | All Nippon Airways | 910 |
| 19 | Alaska Airlines | 891 |
| 20 | QLK | 887 |
| 21 | EJU | 874 |
| 22 | VIV | 781 |
| 23 | AEE | 758 |
| 24 | CXK | 757 |
| 25 | Air France | 755 |
| 26 | JetBlue | 753 |
| 27 | United Airlines | 737 |
| 28 | Cathay Pacific | 732 |
| 29 | MXY | 732 |
| 30 | GLO | 725 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121709 |
| 2 | 🇪🇸 ES | 9261 |
| 3 | 🇮🇳 IN | 8119 |
| 4 | 🇦🇺 AU | 8101 |
| 5 | 🇧🇷 BR | 7992 |
| 6 | 🇨🇦 CA | 7443 |
| 7 | 🇮🇹 IT | 7389 |
| 8 | 🇩🇪 DE | 7359 |
| 9 | 🇬🇧 GB | 6471 |
| 10 | 🇯🇵 JP | 5946 |
| 11 | 🇫🇷 FR | 5639 |
| 12 | 🇨🇴 CO | 4510 |
| 13 | 🇲🇽 MX | 4107 |
| 14 | 🇬🇷 GR | 4031 |
| 15 | 🇳🇴 NO | 3805 |
| 16 | 🇨🇭 CH | 3668 |
| 17 | 🇹🇷 TR | 3350 |
| 18 | 🇲🇾 MY | 2747 |
| 19 | 🇵🇱 PL | 2375 |
| 20 | 🇿🇦 ZA | 2316 |
| 21 | 🇳🇿 NZ | 2164 |
| 22 | 🇹🇭 TH | 2120 |
| 23 | 🇰🇷 KR | 2017 |
| 24 | 🇵🇭 PH | 1914 |
| 25 | 🇬🇹 GT | 1865 |
| 26 | 🇲🇦 MA | 1488 |
| 27 | 🇲🇪 ME | 1404 |
| 28 | 🇳🇱 NL | 1333 |
| 29 | 🇭🇷 HR | 1290 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2913 |
| 2 | Denver International Airport |  | US | 2364 |
| 3 | Tokyo International Airport |  | JP | 1922 |
| 4 | Indira Gandhi International Airport |  | IN | 1801 |
| 5 | Harry Reid International Airport |  | US | 1770 |
| 6 | Guaymaral Airport |  | CO | 1727 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1625 |
| 8 | Zurich Airport |  | CH | 1576 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1484 |
| 10 | La Aurora Airport |  | GT | 1442 |
| 11 | Frankfurt am Main International Airport |  | DE | 1380 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1347 |
| 13 | Chicago O'Hare International Airport |  | US | 1328 |
| 14 | Salt Lake City International Airport |  | US | 1264 |
| 15 | El Dorado International Airport |  | CO | 1252 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1234 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1159 |
| 19 | Madrid Barajas International Airport |  | ES | 1143 |
| 20 | Congonhas Airport |  | BR | 1135 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1127 |
| 22 | Kuala Lumpur International Airport |  | MY | 1060 |
| 23 | Charlotte/Douglas International Airport |  | US | 1027 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1024 |
| 25 | Charles de Gaulle International Airport |  | FR | 1000 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 989 |
| 27 | Bengaluru International Airport |  | IN | 971 |
| 28 | Malpensa International Airport |  | IT | 918 |
| 29 | Ninoy Aquino International Airport |  | PH | 893 |
| 30 | Daniel K Inouye International Airport |  | US | 865 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 864 |
| 32 | Barcelona International Airport |  | ES | 863 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 834 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Viracopos International Airport |  | BR | 803 |
| 37 | Scottsdale Airport |  | US | 803 |
| 38 | Seattle-Tacoma International Airport |  | US | 802 |
| 39 | Amsterdam Airport Schiphol |  | NL | 801 |
| 40 | Oslo Gardermoen Airport |  | NO | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 728 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 515 | 21m | 244 km | 2,168.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 345 | 24m | 225 km | 1,338.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 335 | 1h 9m | 770 km | 4,450.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
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
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 165 | 44m | 452 km | 1,285.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 162 | 1h 1m | 695 km | 1,941.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 158 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CAP274 | CAP | Tucson International Airport (KTUS) | Nogales International Airport (KOLS) | 2026-07-15 13:12 UTC | 2026-07-15 13:35 UTC | 22m |
| BLACK34 | BLA | Ovar Airport (LPOV) | Viseu Airport (LPVZ) | 2026-07-15 13:05 UTC | 2026-07-15 13:33 UTC | 27m |
| SCA77 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-15 13:19 UTC | 2026-07-15 13:32 UTC | 13m |
| ATAC1 | ATA | NC87 (NC87) | Ocracoke Island Airport (KW95) | 2026-07-15 13:12 UTC | 2026-07-15 13:30 UTC | 18m |
| DRAGONC | DRA | Perpignan-Rivesaltes (Llabanere) Airport (LFMP) | Nimes-Arles-Camargue Airport (LFTW) | 2026-07-15 12:11 UTC | 2026-07-15 13:29 UTC | 1h 17m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-07-15 13:03 UTC | 2026-07-15 13:26 UTC | 23m |
| ISU5 | ISU | Songer Airport (IN55) | Porter County Regional Airport (KVPZ) | 2026-07-15 12:36 UTC | 2026-07-15 13:24 UTC | 48m |
| DRAGO65 | DRA | Peyresourde Balestas Airport (LFIP) | Peyresourde Balestas Airport (LFIP) | 2026-07-15 13:08 UTC | 2026-07-15 13:18 UTC | 10m |
| N814SS |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-15 12:50 UTC | 2026-07-15 13:16 UTC | 25m |
| RPA5632 | Republic Airways | Jacksonville International Airport (KJAX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-15 10:55 UTC | 2026-07-15 13:12 UTC | 2h 17m |
| UAY84 | UAY | DCAE Cosford Airport (EGWC) | DCAE Cosford Airport (EGWC) | 2026-07-15 12:51 UTC | 2026-07-15 13:09 UTC | 18m |
| AAL2764 | American Airlines | General Edward Lawrence Logan International Airport (KBOS) | Philadelphia International Airport (KPHL) | 2026-07-15 12:11 UTC | 2026-07-15 13:09 UTC | 57m |
| N838SP |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-15 12:38 UTC | 2026-07-15 13:07 UTC | 29m |
| AFR87PQ | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-07-15 12:05 UTC | 2026-07-15 13:07 UTC | 1h 1m |
| N397BC |  | Huntingburg Airport (KHNB) | CO86 (CO86) | 2026-07-15 11:02 UTC | 2026-07-15 13:05 UTC | 2h 3m |
| VANTA01 | VAN | Cochstedt Airport (EDBC) | Cochstedt Airport (EDBC) | 2026-07-15 13:00 UTC | 2026-07-15 13:04 UTC | 4m |
| N292LA |  | Northeast Philadelphia Airport (KPNE) | Cape May County Airport (KWWD) | 2026-07-15 12:24 UTC | 2026-07-15 13:00 UTC | 35m |
| N708LA |  | Atlantic City International Airport (KACY) | Atlantic City International Airport (KACY) | 2026-07-15 12:36 UTC | 2026-07-15 12:59 UTC | 22m |
| RTY775 | RTY | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-07-15 12:30 UTC | 2026-07-15 12:59 UTC | 28m |
|  |  | 5MD0 (5MD0) | 5MD0 (5MD0) | 2026-07-15 12:56 UTC | 2026-07-15 12:58 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
