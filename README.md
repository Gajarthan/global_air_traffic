# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_19:41:40_UTC-green)

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

**Latest saved flight:** 2026-07-30 19:41:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 19:41:40 UTC

- **161,141** saved flights
- **53,220** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,141** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,932,906.9 tonnes** estimated CO2 emissions
- **112,052,577 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6453 |
| 2 | SkyWest Airlines | 5877 |
| 3 | EJA | 3191 |
| 4 | IndiGo | 2831 |
| 5 | American Airlines | 2545 |
| 6 | Southwest Airlines | 2521 |
| 7 | ENY | 2005 |
| 8 | Delta Air Lines | 1917 |
| 9 | Lufthansa | 1520 |
| 10 | LATAM Airlines | 1511 |
| 11 | AZU | 1414 |
| 12 | WIF | 1365 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1246 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1110 |
| 17 | easyJet | 1053 |
| 18 | Alaska Airlines | 1004 |
| 19 | EJU | 992 |
| 20 | QLK | 991 |
| 21 | All Nippon Airways | 990 |
| 22 | VIV | 887 |
| 23 | CXK | 860 |
| 24 | United Airlines | 854 |
| 25 | GLO | 848 |
| 26 | Cathay Pacific | 847 |
| 27 | AEE | 846 |
| 28 | Air France | 837 |
| 29 | MXY | 835 |
| 30 | JetBlue | 824 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139130 |
| 2 | 🇪🇸 ES | 10337 |
| 3 | 🇧🇷 BR | 9202 |
| 4 | 🇦🇺 AU | 9082 |
| 5 | 🇮🇳 IN | 8909 |
| 6 | 🇨🇦 CA | 8747 |
| 7 | 🇮🇹 IT | 8313 |
| 8 | 🇩🇪 DE | 8139 |
| 9 | 🇬🇧 GB | 7397 |
| 10 | 🇯🇵 JP | 6531 |
| 11 | 🇫🇷 FR | 6388 |
| 12 | 🇨🇴 CO | 5711 |
| 13 | 🇬🇷 GR | 4625 |
| 14 | 🇲🇽 MX | 4625 |
| 15 | 🇳🇴 NO | 4261 |
| 16 | 🇨🇭 CH | 4229 |
| 17 | 🇹🇷 TR | 3846 |
| 18 | 🇲🇾 MY | 2909 |
| 19 | 🇵🇱 PL | 2735 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2366 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2117 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2069 |
| 26 | 🇲🇦 MA | 1629 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1506 |
| 29 | 🇳🇱 NL | 1479 |
| 30 | 🇲🇴 MO | 1339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3287 |
| 2 | Denver International Airport |  | US | 2684 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2030 |
| 5 | Indira Gandhi International Airport |  | IN | 1981 |
| 6 | Harry Reid International Airport |  | US | 1953 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1782 |
| 8 | Zurich Airport |  | CH | 1719 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1696 |
| 10 | La Aurora Airport |  | GT | 1606 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1501 |
| 12 | El Dorado International Airport |  | CO | 1474 |
| 13 | Frankfurt am Main International Airport |  | DE | 1471 |
| 14 | Chicago O'Hare International Airport |  | US | 1463 |
| 15 | Salt Lake City International Airport |  | US | 1450 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1345 |
| 17 | Macau International Airport |  | MO | 1339 |
| 18 | Congonhas Airport |  | BR | 1335 |
| 19 | Madrid Barajas International Airport |  | ES | 1277 |
| 20 | Capua Airport |  | IT | 1269 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1233 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1143 |
| 24 | Charlotte/Douglas International Airport |  | US | 1131 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1067 |
| 28 | Bengaluru International Airport |  | IN | 1059 |
| 29 | Ninoy Aquino International Airport |  | PH | 993 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 985 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 978 |
| 32 | Barcelona International Airport |  | ES | 958 |
| 33 | Daniel K Inouye International Airport |  | US | 948 |
| 34 | Seattle-Tacoma International Airport |  | US | 936 |
| 35 | Calgary International Airport |  | CA | 923 |
| 36 | Viracopos International Airport |  | BR | 917 |
| 37 | Scottsdale Airport |  | US | 906 |
| 38 | Tenerife Norte Airport |  | ES | 902 |
| 39 | Oslo Gardermoen Airport |  | NO | 896 |
| 40 | Amsterdam Airport Schiphol |  | NL | 886 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 852 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 587 | 21m | 244 km | 2,471.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 385 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 238 | 22m | 55 km | 226.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 230 | 44m | 241 km | 955.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 203 | 20m | 99 km | 347.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 193 | 30m | 49 km | 163.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 192 | 28m | 152 km | 501.8 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 190 | 18m | 144 km | 472.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 183 | 50m | 556 km | 1,754.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 180 | 1h 39m | 1,156 km | 3,590.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 178 | 1h 1m | 695 km | 2,133.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 171 | 23m | 218 km | 644.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N446BG |  | Wood County Airport (K1G0) | Wood County Airport (K1G0) | 2026-07-30 19:20 UTC | 2026-07-30 19:41 UTC | 20m |
| N10BB |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-07-30 19:14 UTC | 2026-07-30 19:39 UTC | 25m |
| ENY4023 | ENY | Chicago O'Hare International Airport (KORD) | Spencer Nolf Airport (KNRQ) | 2026-07-30 17:49 UTC | 2026-07-30 19:33 UTC | 1h 44m |
| CXK200 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-07-30 18:51 UTC | 2026-07-30 19:33 UTC | 41m |
| N334WB |  | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-07-30 19:15 UTC | 2026-07-30 19:33 UTC | 17m |
| PBW13 | PBW | Karlsruhe Baden-Baden Airport (EDSB) | Backnang-Heiningen Airport (EDSH) | 2026-07-30 19:05 UTC | 2026-07-30 19:33 UTC | 27m |
| N978AP |  | Gillespie Field (KSEE) | Bob Maxwell Memorial Airfield (KOKB) | 2026-07-30 18:51 UTC | 2026-07-30 19:29 UTC | 38m |
| TKR101 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Libby Airport (KS59) | 2026-07-30 19:15 UTC | 2026-07-30 19:29 UTC | 14m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-07-30 18:41 UTC | 2026-07-30 19:24 UTC | 42m |
| KSF44 | KSF | Kent State University Airport (K1G3) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-07-30 17:56 UTC | 2026-07-30 19:23 UTC | 1h 26m |
| PLF251 | PLF | Powidz Military Air Base (EPPW) | Powidz Military Air Base (EPPW) | 2026-07-30 19:03 UTC | 2026-07-30 19:21 UTC | 18m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-30 18:54 UTC | 2026-07-30 19:21 UTC | 27m |
| N8533X |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-30 18:54 UTC | 2026-07-30 19:20 UTC | 26m |
| SVR1578 | SVR | Sivas Airport (LTAR) | Kopitnari Airport (UGKO) | 2026-07-30 18:47 UTC | 2026-07-30 19:20 UTC | 33m |
| N74737 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-30 19:08 UTC | 2026-07-30 19:19 UTC | 11m |
| N345Y |  | Page Field (KFMY) | La Belle Municipal Airport (KX14) | 2026-07-30 18:28 UTC | 2026-07-30 19:18 UTC | 49m |
| HAF209 | HAF | Elefsis Airport (LGEL) | Araxos Airport (LGRX) | 2026-07-30 17:33 UTC | 2026-07-30 19:18 UTC | 1h 45m |
| N541MN |  | Toledo Executive Airport (KTDZ) | 00OH (00OH) | 2026-07-30 17:59 UTC | 2026-07-30 19:18 UTC | 1h 18m |
| CXK490 | CXK | Sacramento Executive Airport (KSAC) | Sacramento Mather Airport (KMHR) | 2026-07-30 17:59 UTC | 2026-07-30 19:17 UTC | 1h 17m |
| GFY164 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-07-30 18:35 UTC | 2026-07-30 19:17 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
