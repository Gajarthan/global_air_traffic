# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_05:53:32_UTC-green)

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

**Latest saved flight:** 2026-07-08 05:53:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 05:53:32 UTC

- **132,830** saved flights
- **45,052** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,830** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,598,678.1 tonnes** estimated CO2 emissions
- **92,676,991 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5392 |
| 2 | SkyWest Airlines | 4906 |
| 3 | EJA | 2607 |
| 4 | IndiGo | 2479 |
| 5 | American Airlines | 2075 |
| 6 | Southwest Airlines | 2000 |
| 7 | ENY | 1669 |
| 8 | Delta Air Lines | 1590 |
| 9 | Lufthansa | 1380 |
| 10 | LATAM Airlines | 1223 |
| 11 | Vueling | 1163 |
| 12 | WIF | 1156 |
| 13 | AZU | 1128 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 942 |
| 17 | All Nippon Airways | 870 |
| 18 | easyJet | 846 |
| 19 | Alaska Airlines | 845 |
| 20 | QLK | 830 |
| 21 | EJU | 817 |
| 22 | VIV | 734 |
| 23 | AEE | 722 |
| 24 | Air France | 718 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 713 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 700 |
| 29 | MXY | 687 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113909 |
| 2 | 🇪🇸 ES | 8813 |
| 3 | 🇮🇳 IN | 7767 |
| 4 | 🇦🇺 AU | 7686 |
| 5 | 🇧🇷 BR | 7491 |
| 6 | 🇨🇦 CA | 7026 |
| 7 | 🇩🇪 DE | 6937 |
| 8 | 🇮🇹 IT | 6917 |
| 9 | 🇬🇧 GB | 5919 |
| 10 | 🇯🇵 JP | 5707 |
| 11 | 🇫🇷 FR | 5273 |
| 12 | 🇨🇴 CO | 4167 |
| 13 | 🇲🇽 MX | 3877 |
| 14 | 🇬🇷 GR | 3804 |
| 15 | 🇳🇴 NO | 3591 |
| 16 | 🇨🇭 CH | 3428 |
| 17 | 🇹🇷 TR | 2969 |
| 18 | 🇲🇾 MY | 2643 |
| 19 | 🇵🇱 PL | 2188 |
| 20 | 🇿🇦 ZA | 2183 |
| 21 | 🇳🇿 NZ | 2097 |
| 22 | 🇹🇭 TH | 2044 |
| 23 | 🇰🇷 KR | 1970 |
| 24 | 🇵🇭 PH | 1828 |
| 25 | 🇬🇹 GT | 1808 |
| 26 | 🇲🇦 MA | 1407 |
| 27 | 🇲🇪 ME | 1316 |
| 28 | 🇳🇱 NL | 1248 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1172 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2771 |
| 2 | Denver International Airport |  | US | 2250 |
| 3 | Tokyo International Airport |  | JP | 1868 |
| 4 | Indira Gandhi International Airport |  | IN | 1717 |
| 5 | Harry Reid International Airport |  | US | 1649 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1561 |
| 8 | Zurich Airport |  | CH | 1476 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1412 |
| 10 | La Aurora Airport |  | GT | 1396 |
| 11 | Frankfurt am Main International Airport |  | DE | 1337 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1281 |
| 13 | Chicago O'Hare International Airport |  | US | 1275 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1184 |
| 16 | Salt Lake City International Airport |  | US | 1181 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1150 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1089 |
| 19 | Madrid Barajas International Airport |  | ES | 1085 |
| 20 | Capua Airport |  | IT | 1084 |
| 21 | Congonhas Airport |  | BR | 1061 |
| 22 | Kuala Lumpur International Airport |  | MY | 1028 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 966 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 936 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 911 |
| 28 | Malpensa International Airport |  | IT | 882 |
| 29 | Ninoy Aquino International Airport |  | PH | 849 |
| 30 | Daniel K Inouye International Airport |  | US | 830 |
| 31 | Barcelona International Airport |  | ES | 817 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 812 |
| 33 | Tenerife Norte Airport |  | ES | 797 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 781 |
| 35 | Calgary International Airport |  | CA | 775 |
| 36 | Seattle-Tacoma International Airport |  | US | 765 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Viracopos International Airport |  | BR | 757 |
| 39 | Vitoria/Foronda Airport |  | ES | 755 |
| 40 | Amsterdam Airport Schiphol |  | NL | 750 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 482 | 21m | 244 km | 2,029.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-07-08 05:38 UTC | 2026-07-08 05:53 UTC | 15m |
| DHL00 | DHL | Bordeaux-Merignac (BA 106) Airport (LFBD) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-07-08 05:24 UTC | 2026-07-08 05:40 UTC | 15m |
| EFC29C | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-07-08 04:25 UTC | 2026-07-08 05:33 UTC | 1h 8m |
| JBU1096 | JetBlue | Hartsfield/Jackson Atlanta International Airport (KATL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-08 03:22 UTC | 2026-07-08 05:32 UTC | 2h 9m |
| ERU48 | ERU | Robin Airport (59AZ) | AZ86 (AZ86) | 2026-07-08 05:18 UTC | 2026-07-08 05:29 UTC | 10m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-07-08 05:01 UTC | 2026-07-08 05:27 UTC | 25m |
| ABY734 | ABY | Sharjah International Airport (OMSJ) | Sharjah International Airport (OMSJ) | 2026-07-08 05:21 UTC | 2026-07-08 05:25 UTC | 4m |
| EFC18K | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-07-08 05:04 UTC | 2026-07-08 05:22 UTC | 18m |
| NKD | NKD | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-07-08 05:09 UTC | 2026-07-08 05:22 UTC | 13m |
| DAL860 | Delta Air Lines | San Francisco International Airport (KSFO) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-07 23:40 UTC | 2026-07-08 05:20 UTC | 5h 40m |
| N224JA |  | Ogden-Hinckley Airport (KOGD) | KU42 (KU42) | 2026-07-08 04:31 UTC | 2026-07-08 05:19 UTC | 47m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-07-08 04:44 UTC | 2026-07-08 05:17 UTC | 32m |
| DLH899 | Lufthansa | Vilnius International Airport (EYVI) | Frankfurt am Main International Airport (EDDF) | 2026-07-08 03:26 UTC | 2026-07-08 05:15 UTC | 1h 49m |
| BKI603 | BKI | Istanbul Airport (LTFM) | Mikonos Airport (LGMK) | 2026-07-08 04:13 UTC | 2026-07-08 05:13 UTC | 1h 0m |
| N904DR |  | Gillespie Field (KSEE) | Van Nuys Airport (KVNY) | 2026-07-08 03:57 UTC | 2026-07-08 05:13 UTC | 1h 15m |
| AWA415 | AWA | VGZR (VGZR) | Khowai Airport (VEKW) | 2026-07-08 04:44 UTC | 2026-07-08 05:12 UTC | 28m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma Snowy Mountains Airport (YCOM) | 2026-07-08 04:31 UTC | 2026-07-08 05:11 UTC | 39m |
| CXK416 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-07-08 04:23 UTC | 2026-07-08 05:08 UTC | 44m |
| OAL090 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiathos Island National Airport (LGSK) | 2026-07-08 04:45 UTC | 2026-07-08 05:06 UTC | 21m |
| N55291 |  | Riverside Airport (KRAL) | Santa Barbara Municipal Airport (KSBA) | 2026-07-08 03:17 UTC | 2026-07-08 05:02 UTC | 1h 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
