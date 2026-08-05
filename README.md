# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_16:04:17_UTC-green)

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

**Latest saved flight:** 2026-08-05 16:04:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 16:04:17 UTC

- **172,436** saved flights
- **55,986** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **172,436** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,078,234.4 tonnes** estimated CO2 emissions
- **120,477,357 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6848 |
| 2 | SkyWest Airlines | 6300 |
| 3 | EJA | 3422 |
| 4 | IndiGo | 3029 |
| 5 | Southwest Airlines | 2715 |
| 6 | American Airlines | 2711 |
| 7 | ENY | 2148 |
| 8 | Delta Air Lines | 2046 |
| 9 | LATAM Airlines | 1594 |
| 10 | Lufthansa | 1573 |
| 11 | AZU | 1520 |
| 12 | WIF | 1443 |
| 13 | Vueling | 1420 |
| 14 | LXJ | 1345 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1174 |
| 17 | easyJet | 1167 |
| 18 | QLK | 1055 |
| 19 | EJU | 1054 |
| 20 | Alaska Airlines | 1051 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 948 |
| 23 | Cathay Pacific | 933 |
| 24 | CXK | 920 |
| 25 | GLO | 904 |
| 26 | United Airlines | 902 |
| 27 | AEE | 899 |
| 28 | Air France | 883 |
| 29 | MXY | 874 |
| 30 | JetBlue | 862 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 148502 |
| 2 | 🇪🇸 ES | 11047 |
| 3 | 🇧🇷 BR | 9798 |
| 4 | 🇦🇺 AU | 9642 |
| 5 | 🇮🇳 IN | 9495 |
| 6 | 🇨🇦 CA | 9428 |
| 7 | 🇮🇹 IT | 8908 |
| 8 | 🇩🇪 DE | 8572 |
| 9 | 🇬🇧 GB | 7988 |
| 10 | 🇯🇵 JP | 6937 |
| 11 | 🇫🇷 FR | 6843 |
| 12 | 🇨🇴 CO | 6315 |
| 13 | 🇬🇷 GR | 5015 |
| 14 | 🇲🇽 MX | 4929 |
| 15 | 🇨🇭 CH | 4546 |
| 16 | 🇳🇴 NO | 4494 |
| 17 | 🇹🇷 TR | 4229 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2887 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2531 |
| 22 | 🇳🇿 NZ | 2498 |
| 23 | 🇵🇭 PH | 2279 |
| 24 | 🇬🇹 GT | 2210 |
| 25 | 🇰🇷 KR | 2169 |
| 26 | 🇲🇦 MA | 1733 |
| 27 | 🇭🇷 HR | 1665 |
| 28 | 🇲🇪 ME | 1580 |
| 29 | 🇳🇱 NL | 1560 |
| 30 | 🇲🇴 MO | 1490 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3557 |
| 2 | Denver International Airport |  | US | 2851 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2144 |
| 5 | Indira Gandhi International Airport |  | IN | 2112 |
| 6 | Harry Reid International Airport |  | US | 2066 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1877 |
| 8 | Zurich Airport |  | CH | 1822 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1809 |
| 10 | La Aurora Airport |  | GT | 1704 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1592 |
| 12 | El Dorado International Airport |  | CO | 1564 |
| 13 | Chicago O'Hare International Airport |  | US | 1561 |
| 14 | Salt Lake City International Airport |  | US | 1544 |
| 15 | Frankfurt am Main International Airport |  | DE | 1535 |
| 16 | Macau International Airport |  | MO | 1490 |
| 17 | Congonhas Airport |  | BR | 1415 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1410 |
| 19 | Madrid Barajas International Airport |  | ES | 1345 |
| 20 | Capua Airport |  | IT | 1344 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1300 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1212 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1203 |
| 24 | Charlotte/Douglas International Airport |  | US | 1193 |
| 25 | Charles de Gaulle International Airport |  | FR | 1167 |
| 26 | Malpensa International Airport |  | IT | 1162 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Ninoy Aquino International Airport |  | PH | 1073 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1070 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1060 |
| 32 | Barcelona International Airport |  | ES | 1021 |
| 33 | Daniel K Inouye International Airport |  | US | 998 |
| 34 | Seattle-Tacoma International Airport |  | US | 995 |
| 35 | Viracopos International Airport |  | BR | 983 |
| 36 | Calgary International Airport |  | CA | 977 |
| 37 | Reno/Tahoe International Airport |  | US | 969 |
| 38 | Oslo Gardermoen Airport |  | NO | 960 |
| 39 | Tenerife Norte Airport |  | ES | 958 |
| 40 | Scottsdale Airport |  | US | 942 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 888 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 630 | 21m | 244 km | 2,652.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 259 | 44m | 241 km | 1,075.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 258 | 22m | 55 km | 245.2 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 236 | 1h 48m | 1,423 km | 5,791.8 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 220 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 207 | 50m | 556 km | 1,984.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 205 | 1h 15m | 961 km | 3,398.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 198 | 1h 38m | 1,156 km | 3,950.0 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 29 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 191 | 8m | - | - |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RVP953 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-08-05 15:25 UTC | 2026-08-05 16:04 UTC | 39m |
| MNL14 | MNL | Gnoss Field (KDVO) | San Carlos Airport (KSQL) | 2026-08-05 15:29 UTC | 2026-08-05 15:59 UTC | 30m |
| GLFIX | GLF | Sywell Aerodrome (EGBK) | RAF Wittering (EGXT) | 2026-08-05 15:34 UTC | 2026-08-05 15:56 UTC | 21m |
| VSB97 | VSB | Barrow Walney Island Airport (EGNL) | Bristol International Airport (EGGD) | 2026-08-05 15:12 UTC | 2026-08-05 15:55 UTC | 42m |
| BOBCT61 | BOB | Thigpen Field (K00M) | Smith County Airport (MS39) | 2026-08-05 15:35 UTC | 2026-08-05 15:53 UTC | 17m |
| N6227 |  | Austin Executive Airport (KEDC) | Bud Dryden Airport (TX05) | 2026-08-05 15:14 UTC | 2026-08-05 15:52 UTC | 38m |
| N359DG |  | Visalia Municipal Airport (KVIS) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-05 15:11 UTC | 2026-08-05 15:50 UTC | 39m |
| N53959 |  | Kissimmee Gateway Airport (KISM) | Leesburg International Airport (KLEE) | 2026-08-05 15:09 UTC | 2026-08-05 15:46 UTC | 37m |
| CGFSP | CGF | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-05 15:22 UTC | 2026-08-05 15:45 UTC | 23m |
| N155SH |  | John C Tune Airport (KJWN) | John C Tune Airport (KJWN) | 2026-08-05 15:26 UTC | 2026-08-05 15:44 UTC | 18m |
| CXK134 | CXK | Akron-Canton Regional Airport (KCAK) | Akron-Canton Regional Airport (KCAK) | 2026-08-05 14:19 UTC | 2026-08-05 15:44 UTC | 1h 25m |
| N44290 |  | Pensacola International Airport (KPNS) | Choctaw Nolf Airport (KNFJ) | 2026-08-05 15:25 UTC | 2026-08-05 15:41 UTC | 15m |
| FGIBV | FGI | Chambery-Challes-les-Eaux Airport (LFLE) | Chambery-Savoie Airport (LFLB) | 2026-08-05 15:03 UTC | 2026-08-05 15:41 UTC | 37m |
| N7660U |  | OI59 (OI59) | Ohio University Airport (KUNI) | 2026-08-05 14:55 UTC | 2026-08-05 15:36 UTC | 41m |
| WIF158 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-05 14:47 UTC | 2026-08-05 15:36 UTC | 48m |
| N630HR |  | Decatur Municipal Airport (KLUD) | Decatur Municipal Airport (KLUD) | 2026-08-05 15:24 UTC | 2026-08-05 15:35 UTC | 10m |
| FJO71P | FJO | Ibiza Airport (LEIB) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-05 14:22 UTC | 2026-08-05 15:35 UTC | 1h 12m |
| N803BD |  | Rogers Executive - Carter Field (KROG) | Petit Jean Park Airport (KMPJ) | 2026-08-05 15:16 UTC | 2026-08-05 15:34 UTC | 17m |
| SWR5643 | Swiss International | Ostend-Bruges International Airport (EBOS) | Zurich Airport (LSZH) | 2026-08-05 14:22 UTC | 2026-08-05 15:31 UTC | 1h 9m |
| ROKT81 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Gulfport-Biloxi International Airport (KGPT) | 2026-08-05 14:58 UTC | 2026-08-05 15:31 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
