# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_19:31:27_UTC-green)

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

**Latest saved flight:** 2026-07-13 19:31:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 19:31:27 UTC

- **140,631** saved flights
- **47,303** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **140,631** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,688,399.0 tonnes** estimated CO2 emissions
- **97,878,201 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5736 |
| 2 | SkyWest Airlines | 5148 |
| 3 | EJA | 2775 |
| 4 | IndiGo | 2576 |
| 5 | American Airlines | 2227 |
| 6 | Southwest Airlines | 2114 |
| 7 | ENY | 1749 |
| 8 | Delta Air Lines | 1667 |
| 9 | Lufthansa | 1428 |
| 10 | LATAM Airlines | 1291 |
| 11 | Vueling | 1213 |
| 12 | AZU | 1210 |
| 13 | WIF | 1210 |
| 14 | LXJ | 1078 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 1005 |
| 17 | easyJet | 918 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 884 |
| 20 | QLK | 877 |
| 21 | EJU | 867 |
| 22 | VIV | 775 |
| 23 | AEE | 755 |
| 24 | Air France | 754 |
| 25 | CXK | 754 |
| 26 | JetBlue | 742 |
| 27 | United Airlines | 734 |
| 28 | Cathay Pacific | 730 |
| 29 | MXY | 730 |
| 30 | GLO | 719 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120853 |
| 2 | 🇪🇸 ES | 9227 |
| 3 | 🇮🇳 IN | 8067 |
| 4 | 🇦🇺 AU | 8018 |
| 5 | 🇧🇷 BR | 7938 |
| 6 | 🇨🇦 CA | 7368 |
| 7 | 🇮🇹 IT | 7350 |
| 8 | 🇩🇪 DE | 7331 |
| 9 | 🇬🇧 GB | 6424 |
| 10 | 🇯🇵 JP | 5895 |
| 11 | 🇫🇷 FR | 5608 |
| 12 | 🇨🇴 CO | 4464 |
| 13 | 🇲🇽 MX | 4078 |
| 14 | 🇬🇷 GR | 4006 |
| 15 | 🇳🇴 NO | 3785 |
| 16 | 🇨🇭 CH | 3660 |
| 17 | 🇹🇷 TR | 3325 |
| 18 | 🇲🇾 MY | 2731 |
| 19 | 🇵🇱 PL | 2355 |
| 20 | 🇿🇦 ZA | 2308 |
| 21 | 🇳🇿 NZ | 2144 |
| 22 | 🇹🇭 TH | 2110 |
| 23 | 🇰🇷 KR | 2013 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1862 |
| 26 | 🇲🇦 MA | 1475 |
| 27 | 🇲🇪 ME | 1399 |
| 28 | 🇳🇱 NL | 1326 |
| 29 | 🇭🇷 HR | 1273 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2900 |
| 2 | Denver International Airport |  | US | 2351 |
| 3 | Tokyo International Airport |  | JP | 1909 |
| 4 | Indira Gandhi International Airport |  | IN | 1787 |
| 5 | Harry Reid International Airport |  | US | 1752 |
| 6 | Guaymaral Airport |  | CO | 1714 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1617 |
| 8 | Zurich Airport |  | CH | 1571 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1475 |
| 10 | La Aurora Airport |  | GT | 1440 |
| 11 | Frankfurt am Main International Airport |  | DE | 1378 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1342 |
| 13 | Chicago O'Hare International Airport |  | US | 1323 |
| 14 | Salt Lake City International Airport |  | US | 1253 |
| 15 | El Dorado International Airport |  | CO | 1247 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1210 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1155 |
| 19 | Madrid Barajas International Airport |  | ES | 1141 |
| 20 | Congonhas Airport |  | BR | 1130 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1125 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 998 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 976 |
| 27 | Bengaluru International Airport |  | IN | 966 |
| 28 | Malpensa International Airport |  | IT | 912 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Daniel K Inouye International Airport |  | US | 860 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 859 |
| 32 | Barcelona International Airport |  | ES | 858 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 825 |
| 34 | Tenerife Norte Airport |  | ES | 819 |
| 35 | Calgary International Airport |  | CA | 806 |
| 36 | Viracopos International Airport |  | BR | 800 |
| 37 | Amsterdam Airport Schiphol |  | NL | 799 |
| 38 | Seattle-Tacoma International Airport |  | US | 798 |
| 39 | Scottsdale Airport |  | US | 796 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 723 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 510 | 21m | 244 km | 2,147.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 207 | 22m | 55 km | 196.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 188 | 20m | 99 km | 322.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 186 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 169 | 18m | 144 km | 420.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 160 | 1h 38m | 1,156 km | 3,191.9 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 155 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA3485 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-07-13 04:54 UTC | 2026-07-13 19:31 UTC | 14h 37m |
| N328KT |  | Bend Municipal Airport (KBDN) | Dry Creek Airpark (OG21) | 2026-07-13 19:11 UTC | 2026-07-13 19:27 UTC | 16m |
| N22UK |  | Tommy's Airpark (9LL5) | Tommy's Airpark (9LL5) | 2026-07-13 18:43 UTC | 2026-07-13 19:27 UTC | 44m |
| N891JC |  | Roseland Airport (32MD) | Whalen Field (25MD) | 2026-07-13 18:53 UTC | 2026-07-13 19:25 UTC | 32m |
| N555ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-07-13 18:58 UTC | 2026-07-13 19:25 UTC | 27m |
| N320CM |  | Harris Field (73IA) | Mason City Municipal Airport (KMCW) | 2026-07-13 17:02 UTC | 2026-07-13 19:25 UTC | 2h 23m |
| N9421F |  | Pennridge Airport (KCKZ) | Pennridge Airport (KCKZ) | 2026-07-13 19:09 UTC | 2026-07-13 19:25 UTC | 16m |
| STW011 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-07-13 16:23 UTC | 2026-07-13 19:21 UTC | 2h 58m |
| AAL1151 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-13 14:16 UTC | 2026-07-13 19:20 UTC | 5h 4m |
| HLE61 | HLE | Caernarfon Airport (EGCK) | Welshpool Airport (EGCW) | 2026-07-13 18:43 UTC | 2026-07-13 19:19 UTC | 36m |
| N6332G |  | 7CL0 (7CL0) | Dos Palos Airport (28CA) | 2026-07-13 18:38 UTC | 2026-07-13 19:17 UTC | 38m |
| N622FB |  | Phoenix Deer Valley Airport (KDVT) | Phoenix Sky Harbor International Airport (KPHX) | 2026-07-13 18:34 UTC | 2026-07-13 19:17 UTC | 42m |
| GJS3375 | GJS | St Louis Lambert International Airport (KSTL) | St Louis Lambert International Airport (KSTL) | 2026-07-13 19:01 UTC | 2026-07-13 19:16 UTC | 15m |
| N45BP |  | Harry Reid International Airport (KLAS) | Four Corners Regional Airport (KFMN) | 2026-07-13 18:22 UTC | 2026-07-13 19:10 UTC | 47m |
| N427BC |  | Lubbock Preston Smith International Airport (KLBB) | Terry County Airport (KBFE) | 2026-07-13 18:59 UTC | 2026-07-13 19:09 UTC | 10m |
| RYR42UP | Ryanair | Vilnius International Airport (EYVI) | Suwałki Airport (EPSU) | 2026-07-13 18:52 UTC | 2026-07-13 19:08 UTC | 16m |
| N777ZA |  | General Edward Lawrence Logan International Airport (KBOS) | Laguardia Airport (KLGA) | 2026-07-13 17:34 UTC | 2026-07-13 19:07 UTC | 1h 33m |
| BOE733 | BOE | Renton Municipal Airport (KRNT) | Franz Ranch Airport (33WA) | 2026-07-13 17:21 UTC | 2026-07-13 19:05 UTC | 1h 44m |
| CXK1057 | CXK | Mesa Gateway Airport (KIWA) | Coolidge Municipal Airport (KP08) | 2026-07-13 17:50 UTC | 2026-07-13 19:05 UTC | 1h 14m |
| N803QS |  | Newcastle Airport (EGNT) | Bangor International Airport (KBGR) | 2026-07-13 13:04 UTC | 2026-07-13 19:04 UTC | 6h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
