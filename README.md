# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_18:27:06_UTC-green)

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

**Latest saved flight:** 2026-07-29 18:27:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 18:27:06 UTC

- **158,874** saved flights
- **52,612** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **158,874** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,906,362.7 tonnes** estimated CO2 emissions
- **110,513,779 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6382 |
| 2 | SkyWest Airlines | 5796 |
| 3 | EJA | 3143 |
| 4 | IndiGo | 2802 |
| 5 | American Airlines | 2516 |
| 6 | Southwest Airlines | 2493 |
| 7 | ENY | 1978 |
| 8 | Delta Air Lines | 1885 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1492 |
| 11 | AZU | 1402 |
| 12 | WIF | 1346 |
| 13 | Vueling | 1333 |
| 14 | LXJ | 1224 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1096 |
| 17 | easyJet | 1034 |
| 18 | Alaska Airlines | 993 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 973 |
| 22 | VIV | 871 |
| 23 | CXK | 843 |
| 24 | United Airlines | 838 |
| 25 | GLO | 837 |
| 26 | AEE | 834 |
| 27 | Cathay Pacific | 833 |
| 28 | Air France | 829 |
| 29 | MXY | 824 |
| 30 | JetBlue | 818 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 137000 |
| 2 | 🇪🇸 ES | 10224 |
| 3 | 🇧🇷 BR | 9100 |
| 4 | 🇦🇺 AU | 8955 |
| 5 | 🇮🇳 IN | 8810 |
| 6 | 🇨🇦 CA | 8602 |
| 7 | 🇮🇹 IT | 8221 |
| 8 | 🇩🇪 DE | 8060 |
| 9 | 🇬🇧 GB | 7291 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6296 |
| 12 | 🇨🇴 CO | 5586 |
| 13 | 🇲🇽 MX | 4565 |
| 14 | 🇬🇷 GR | 4555 |
| 15 | 🇳🇴 NO | 4211 |
| 16 | 🇨🇭 CH | 4165 |
| 17 | 🇹🇷 TR | 3798 |
| 18 | 🇲🇾 MY | 2892 |
| 19 | 🇵🇱 PL | 2704 |
| 20 | 🇿🇦 ZA | 2572 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2274 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2034 |
| 26 | 🇲🇦 MA | 1616 |
| 27 | 🇲🇪 ME | 1523 |
| 28 | 🇭🇷 HR | 1470 |
| 29 | 🇳🇱 NL | 1451 |
| 30 | 🇲🇴 MO | 1313 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3248 |
| 2 | Denver International Airport |  | US | 2643 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 1996 |
| 5 | Indira Gandhi International Airport |  | IN | 1961 |
| 6 | Harry Reid International Airport |  | US | 1936 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1763 |
| 8 | Zurich Airport |  | CH | 1704 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1666 |
| 10 | La Aurora Airport |  | GT | 1578 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1480 |
| 12 | Frankfurt am Main International Airport |  | DE | 1464 |
| 13 | El Dorado International Airport |  | CO | 1450 |
| 14 | Chicago O'Hare International Airport |  | US | 1436 |
| 15 | Salt Lake City International Airport |  | US | 1426 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1325 |
| 17 | Congonhas Airport |  | BR | 1319 |
| 18 | Macau International Airport |  | MO | 1313 |
| 19 | Madrid Barajas International Airport |  | ES | 1262 |
| 20 | Capua Airport |  | IT | 1252 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1220 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1138 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1133 |
| 24 | Charlotte/Douglas International Airport |  | US | 1116 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Malpensa International Airport |  | IT | 1051 |
| 28 | Bengaluru International Airport |  | IN | 1049 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 967 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 966 |
| 32 | Barcelona International Airport |  | ES | 949 |
| 33 | Daniel K Inouye International Airport |  | US | 937 |
| 34 | Seattle-Tacoma International Airport |  | US | 926 |
| 35 | Calgary International Airport |  | CA | 910 |
| 36 | Viracopos International Airport |  | BR | 909 |
| 37 | Scottsdale Airport |  | US | 898 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 885 |
| 40 | Amsterdam Airport Schiphol |  | NL | 873 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 837 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 576 | 21m | 244 km | 2,425.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 225 | 44m | 241 km | 934.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 189 | 1h 15m | 961 km | 3,132.8 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 180 | 50m | 556 km | 1,725.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 178 | 1h 39m | 1,156 km | 3,551.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 169 | 23m | 218 km | 636.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAE192 | AAE | Václav Havel Airport (LKPR) | Macau International Airport (VMMC) | 2026-07-29 07:49 UTC | 2026-07-29 18:27 UTC | 10h 37m |
| FIRE3 | FIR | Van Nuys Airport (KVNY) | Bob Hope Airport (KBUR) | 2026-07-29 18:08 UTC | 2026-07-29 18:22 UTC | 14m |
| STGRY37 | STG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Alice International Airport (KALI) | 2026-07-29 17:25 UTC | 2026-07-29 18:22 UTC | 56m |
| N362LU |  | Lewis University Airport (KLOT) | Dubuque Regional Airport (KDBQ) | 2026-07-29 17:02 UTC | 2026-07-29 18:21 UTC | 1h 19m |
| OYPTR | OYP | Kolding Vamdrup Airport (EKVD) | Kolding Vamdrup Airport (EKVD) | 2026-07-29 15:57 UTC | 2026-07-29 18:19 UTC | 2h 22m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-07-29 17:20 UTC | 2026-07-29 18:12 UTC | 51m |
| N5327R |  | KFTG (KFTG) | Trinchera Ranch Airstrip (CO92) | 2026-07-29 17:21 UTC | 2026-07-29 18:11 UTC | 50m |
| SLH909 | SLH | Salt Lake City International Airport (KSLC) | Lincoln Airport (KLNK) | 2026-07-29 16:14 UTC | 2026-07-29 18:08 UTC | 1h 54m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-07-29 17:51 UTC | 2026-07-29 18:07 UTC | 15m |
| N605T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-07-29 15:57 UTC | 2026-07-29 18:07 UTC | 2h 9m |
| N733KK |  | Bend Municipal Airport (KBDN) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-07-29 17:27 UTC | 2026-07-29 18:07 UTC | 39m |
| N26BQ |  | Dupage Airport (KDPA) | IS47 (IS47) | 2026-07-29 17:41 UTC | 2026-07-29 18:06 UTC | 24m |
| SCU27 | SCU | Haskell Airport (K2K9) | Gregg Airport (7OK1) | 2026-07-29 17:52 UTC | 2026-07-29 18:04 UTC | 11m |
| N455RS |  | Julian Hinds Pump Plant Airstrip (73CL) | Big Bear City Airport (KL35) | 2026-07-29 17:41 UTC | 2026-07-29 18:00 UTC | 18m |
| N831MT |  | Norman Y Mineta San Jose International Airport (KSJC) | Boeing Field/King County International Airport (KBFI) | 2026-07-29 16:26 UTC | 2026-07-29 17:58 UTC | 1h 32m |
| FIRE3 | FIR | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-29 17:22 UTC | 2026-07-29 17:56 UTC | 34m |
| CGLII | CGL | Tofield Airport (CEV7) | Edmonton / Goyer Field (CGF2) | 2026-07-29 17:50 UTC | 2026-07-29 17:56 UTC | 6m |
| BB010 |  | 5AL1 (5AL1) | Evergreen Regional/Middleton Field (KGZH) | 2026-07-29 17:19 UTC | 2026-07-29 17:56 UTC | 36m |
| N73CH |  | Dubuque Regional Airport (KDBQ) | 01IA (01IA) | 2026-07-29 17:27 UTC | 2026-07-29 17:55 UTC | 28m |
| STT937 | STT | Molokai Airport (PHMK) | Molokai Airport (PHMK) | 2026-07-29 17:45 UTC | 2026-07-29 17:54 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
