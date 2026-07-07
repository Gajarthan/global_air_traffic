# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_11:18:41_UTC-green)

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

**Latest saved flight:** 2026-07-07 11:18:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-07 11:18:41 UTC

- **131,796** saved flights
- **44,755** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,796** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,589,818.9 tonnes** estimated CO2 emissions
- **92,163,416 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5366 |
| 2 | SkyWest Airlines | 4886 |
| 3 | EJA | 2584 |
| 4 | IndiGo | 2462 |
| 5 | American Airlines | 2053 |
| 6 | Southwest Airlines | 1984 |
| 7 | ENY | 1657 |
| 8 | Delta Air Lines | 1580 |
| 9 | Lufthansa | 1373 |
| 10 | LATAM Airlines | 1209 |
| 11 | Vueling | 1159 |
| 12 | WIF | 1149 |
| 13 | AZU | 1119 |
| 14 | AXM | 1017 |
| 15 | LXJ | 1017 |
| 16 | Swiss International | 927 |
| 17 | All Nippon Airways | 868 |
| 18 | easyJet | 843 |
| 19 | Alaska Airlines | 842 |
| 20 | QLK | 825 |
| 21 | EJU | 812 |
| 22 | VIV | 730 |
| 23 | AEE | 716 |
| 24 | Air France | 716 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 707 |
| 27 | United Airlines | 702 |
| 28 | JetBlue | 692 |
| 29 | MXY | 686 |
| 30 | GLO | 676 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112955 |
| 2 | 🇪🇸 ES | 8786 |
| 3 | 🇮🇳 IN | 7717 |
| 4 | 🇦🇺 AU | 7604 |
| 5 | 🇧🇷 BR | 7423 |
| 6 | 🇨🇦 CA | 6968 |
| 7 | 🇩🇪 DE | 6894 |
| 8 | 🇮🇹 IT | 6871 |
| 9 | 🇬🇧 GB | 5889 |
| 10 | 🇯🇵 JP | 5685 |
| 11 | 🇫🇷 FR | 5239 |
| 12 | 🇨🇴 CO | 4129 |
| 13 | 🇲🇽 MX | 3846 |
| 14 | 🇬🇷 GR | 3770 |
| 15 | 🇳🇴 NO | 3571 |
| 16 | 🇨🇭 CH | 3395 |
| 17 | 🇹🇷 TR | 2934 |
| 18 | 🇲🇾 MY | 2633 |
| 19 | 🇿🇦 ZA | 2175 |
| 20 | 🇵🇱 PL | 2171 |
| 21 | 🇳🇿 NZ | 2091 |
| 22 | 🇹🇭 TH | 2034 |
| 23 | 🇰🇷 KR | 1968 |
| 24 | 🇵🇭 PH | 1817 |
| 25 | 🇬🇹 GT | 1788 |
| 26 | 🇲🇦 MA | 1400 |
| 27 | 🇲🇪 ME | 1304 |
| 28 | 🇳🇱 NL | 1236 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1159 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2756 |
| 2 | Denver International Airport |  | US | 2245 |
| 3 | Tokyo International Airport |  | JP | 1865 |
| 4 | Indira Gandhi International Airport |  | IN | 1704 |
| 5 | Harry Reid International Airport |  | US | 1641 |
| 6 | Guaymaral Airport |  | CO | 1595 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1551 |
| 8 | Zurich Airport |  | CH | 1457 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1405 |
| 10 | La Aurora Airport |  | GT | 1382 |
| 11 | Frankfurt am Main International Airport |  | DE | 1329 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1269 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1179 |
| 16 | Salt Lake City International Airport |  | US | 1175 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1137 |
| 18 | Madrid Barajas International Airport |  | ES | 1084 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1080 |
| 20 | Capua Airport |  | IT | 1078 |
| 21 | Congonhas Airport |  | BR | 1049 |
| 22 | Kuala Lumpur International Airport |  | MY | 1023 |
| 23 | Charlotte/Douglas International Airport |  | US | 979 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 957 |
| 25 | Charles de Gaulle International Airport |  | FR | 954 |
| 26 | Bengaluru International Airport |  | IN | 932 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 901 |
| 28 | Malpensa International Airport |  | IT | 880 |
| 29 | Ninoy Aquino International Airport |  | PH | 843 |
| 30 | Daniel K Inouye International Airport |  | US | 824 |
| 31 | Barcelona International Airport |  | ES | 815 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 808 |
| 33 | Tenerife Norte Airport |  | ES | 795 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 775 |
| 35 | Calgary International Airport |  | CA | 769 |
| 36 | Seattle-Tacoma International Airport |  | US | 759 |
| 37 | Vitoria/Foronda Airport |  | ES | 754 |
| 38 | Viracopos International Airport |  | BR | 753 |
| 39 | Scottsdale Airport |  | US | 753 |
| 40 | Amsterdam Airport Schiphol |  | NL | 746 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 668 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 477 | 21m | 244 km | 2,008.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 329 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 282 | 14m | 114 km | 553.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 249 | 26m | 275 km | 1,179.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 192 | 22m | 55 km | 182.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 180 | 20m | 99 km | 308.3 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 174 | 1h 46m | 1,423 km | 4,270.2 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 159 | 30m | 49 km | 134.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 155 | 1h 1m | 695 km | 1,858.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-07-07 08:22 UTC | 2026-07-07 11:18 UTC | 2h 55m |
| SPSDW | SPS | Krosno Airport (EPKR) | Krosno Airport (EPKR) | 2026-07-07 10:53 UTC | 2026-07-07 11:09 UTC | 15m |
| HYP011 | HYP | Nice-Cote d'Azur Airport (LFMN) | Sondrio Caiolo Airport (LILO) | 2026-07-07 10:03 UTC | 2026-07-07 10:58 UTC | 55m |
| UPS768 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-07 09:10 UTC | 2026-07-07 10:47 UTC | 1h 37m |
| ABY338 | ABY | Queen Alia International Airport (OJAI) | Sirri Island Airport (OIBS) | 2026-07-07 08:27 UTC | 2026-07-07 10:46 UTC | 2h 19m |
| SYS41 | SYS | RAF Shawbury (EGOS) | Caernarfon Airport (EGCK) | 2026-07-07 09:52 UTC | 2026-07-07 10:38 UTC | 46m |
| UPS204 | UPS | Cologne Bonn Airport (EDDK) | Philadelphia International Airport (KPHL) | 2026-07-07 02:53 UTC | 2026-07-07 10:37 UTC | 7h 44m |
| HBXCL | HBX | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-07-07 09:43 UTC | 2026-07-07 10:37 UTC | 53m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-07 09:40 UTC | 2026-07-07 10:35 UTC | 55m |
| JBU494 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-07 09:25 UTC | 2026-07-07 10:33 UTC | 1h 7m |
| WZZ4SM | Wizz Air | Katowice International Airport (EPKT) | Dinslaken/Schwarze Heide Airport (EDLD) | 2026-07-07 08:51 UTC | 2026-07-07 10:32 UTC | 1h 40m |
| N404CR |  | La Cerdanya Airport (LECD) | La Cerdanya Airport (LECD) | 2026-07-07 10:21 UTC | 2026-07-07 10:31 UTC | 10m |
| JL3555 |  | Hofu Airport (RJOF) | Hiroshima Airport (RJOA) | 2026-07-07 10:05 UTC | 2026-07-07 10:25 UTC | 19m |
| LRQ287G | LRQ | Beziers-Vias Airport (LFMU) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-07-07 09:49 UTC | 2026-07-07 10:24 UTC | 35m |
| WZZ5107 | Wizz Air | Swidnik Lotnisko Airport (EPSW) | Otocac Airport (LDRO) | 2026-07-07 09:10 UTC | 2026-07-07 10:24 UTC | 1h 13m |
| RYR28SK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Bari / Palese International Airport (LIBD) | 2026-07-07 09:27 UTC | 2026-07-07 10:22 UTC | 55m |
| CSI531 | CSI | Albuquerque International Sunport Airport (KABQ) | Navajo Lake Airport (K1V0) | 2026-07-07 09:56 UTC | 2026-07-07 10:20 UTC | 23m |
| CTV764 | CTV | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-07-07 09:42 UTC | 2026-07-07 10:20 UTC | 38m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Harstad/Narvik Airport Evenes (ENEV) | 2026-07-07 09:07 UTC | 2026-07-07 10:20 UTC | 1h 12m |
| AE998 |  | Sydney Bankstown Airport (YSBK) | Temora Airport (YTEM) | 2026-07-07 09:41 UTC | 2026-07-07 10:19 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
