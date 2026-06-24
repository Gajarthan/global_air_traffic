# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_13:25:23_UTC-green)

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

**Latest saved flight:** 2026-06-24 13:25:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-24 13:25:23 UTC

- **118,820** saved flights
- **40,953** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,820** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,440,340.2 tonnes** estimated CO2 emissions
- **83,497,982 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4903 |
| 2 | SkyWest Airlines | 4383 |
| 3 | IndiGo | 2298 |
| 4 | EJA | 2295 |
| 5 | American Airlines | 1846 |
| 6 | Southwest Airlines | 1770 |
| 7 | ENY | 1484 |
| 8 | Delta Air Lines | 1398 |
| 9 | Lufthansa | 1307 |
| 10 | Vueling | 1076 |
| 11 | WIF | 1053 |
| 12 | LATAM Airlines | 1051 |
| 13 | AZU | 993 |
| 14 | AXM | 973 |
| 15 | LXJ | 902 |
| 16 | Swiss International | 837 |
| 17 | All Nippon Airways | 816 |
| 18 | Alaska Airlines | 789 |
| 19 | easyJet | 765 |
| 20 | QLK | 763 |
| 21 | EJU | 746 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 663 |
| 24 | Air France | 652 |
| 25 | VIV | 652 |
| 26 | United Airlines | 649 |
| 27 | CXK | 636 |
| 28 | MXY | 623 |
| 29 | AXB | 591 |
| 30 | GLO | 582 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 100351 |
| 2 | 🇪🇸 ES | 8115 |
| 3 | 🇮🇳 IN | 7217 |
| 4 | 🇦🇺 AU | 7014 |
| 5 | 🇧🇷 BR | 6553 |
| 6 | 🇩🇪 DE | 6353 |
| 7 | 🇮🇹 IT | 6347 |
| 8 | 🇨🇦 CA | 6240 |
| 9 | 🇯🇵 JP | 5320 |
| 10 | 🇬🇧 GB | 5219 |
| 11 | 🇫🇷 FR | 4739 |
| 12 | 🇨🇴 CO | 4004 |
| 13 | 🇲🇽 MX | 3479 |
| 14 | 🇬🇷 GR | 3395 |
| 15 | 🇳🇴 NO | 3267 |
| 16 | 🇨🇭 CH | 3057 |
| 17 | 🇲🇾 MY | 2531 |
| 18 | 🇹🇷 TR | 2442 |
| 19 | 🇿🇦 ZA | 2009 |
| 20 | 🇵🇱 PL | 1957 |
| 21 | 🇳🇿 NZ | 1926 |
| 22 | 🇹🇭 TH | 1909 |
| 23 | 🇰🇷 KR | 1898 |
| 24 | 🇵🇭 PH | 1714 |
| 25 | 🇬🇹 GT | 1665 |
| 26 | 🇲🇦 MA | 1289 |
| 27 | 🇲🇪 ME | 1178 |
| 28 | 🇲🇴 MO | 1172 |
| 29 | 🇳🇱 NL | 1144 |
| 30 | 🇭🇷 HR | 1028 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2500 |
| 2 | Denver International Airport |  | US | 1989 |
| 3 | Tokyo International Airport |  | JP | 1762 |
| 4 | Indira Gandhi International Airport |  | IN | 1585 |
| 5 | Guaymaral Airport |  | CO | 1494 |
| 6 | Harry Reid International Airport |  | US | 1475 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1444 |
| 8 | Zurich Airport |  | CH | 1329 |
| 9 | La Aurora Airport |  | GT | 1287 |
| 10 | Frankfurt am Main International Airport |  | DE | 1266 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1258 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1177 |
| 13 | Macau International Airport |  | MO | 1172 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1161 |
| 16 | Capua Airport |  | IT | 1025 |
| 17 | Salt Lake City International Airport |  | US | 1014 |
| 18 | Madrid Barajas International Airport |  | ES | 1002 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 993 |
| 20 | Kuala Lumpur International Airport |  | MY | 979 |
| 21 | Congonhas Airport |  | BR | 913 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 903 |
| 23 | Charlotte/Douglas International Airport |  | US | 901 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 883 |
| 25 | Charles de Gaulle International Airport |  | FR | 873 |
| 26 | Bengaluru International Airport |  | IN | 872 |
| 27 | Malpensa International Airport |  | IT | 835 |
| 28 | Ninoy Aquino International Airport |  | PH | 793 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 777 |
| 30 | Daniel K Inouye International Airport |  | US | 769 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 756 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 697 |
| 35 | Calgary International Airport |  | CA | 694 |
| 36 | Amsterdam Airport Schiphol |  | NL | 692 |
| 37 | Don Mueang International Airport |  | TH | 691 |
| 38 | Seattle-Tacoma International Airport |  | US | 680 |
| 39 | Viracopos International Airport |  | BR | 675 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 672 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 621 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 431 | 21m | 244 km | 1,814.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 314 | 24m | 225 km | 1,218.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 306 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 290 | 1h 25m | 910 km | 4,550.8 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 287 | 1h 10m | 770 km | 3,812.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 221 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 171 | 26m | 215 km | 633.3 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 163 | 44m | 241 km | 677.1 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 149 | 18m | 144 km | 370.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 140 | 1h 38m | 1,156 km | 2,792.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 134 | 1h 17m | 961 km | 2,221.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZAM37 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-24 12:53 UTC | 2026-06-24 13:25 UTC | 31m |
| N8054B |  | TN62 (TN62) | William B Greene Jr Regional Airport (K0A9) | 2026-06-24 12:51 UTC | 2026-06-24 13:21 UTC | 30m |
| N7296Q |  | Fort Worth Meacham International Airport (KFTW) | Decatur Municipal Airport (KLUD) | 2026-06-24 12:53 UTC | 2026-06-24 13:21 UTC | 27m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-24 13:06 UTC | 2026-06-24 13:20 UTC | 14m |
| ECKJQ | ECK | Almeria International Airport (LEAM) | Federico Garcia Lorca Airport (LEGR) | 2026-06-24 12:48 UTC | 2026-06-24 13:14 UTC | 25m |
| N22019 |  | Greene County Airport (KWAY) | Rostraver Airport (KFWQ) | 2026-06-24 12:54 UTC | 2026-06-24 13:09 UTC | 15m |
| N8891V |  | Heritage Field (KPTW) | Lancaster Airport (KLNS) | 2026-06-24 12:47 UTC | 2026-06-24 13:06 UTC | 19m |
| SGE62 | SGE | Fort Worth Meacham International Airport (KFTW) | Kenneth Copeland Airport (K4T2) | 2026-06-24 12:55 UTC | 2026-06-24 13:06 UTC | 10m |
| N438RM |  | Billings Logan International Airport (KBIL) | Cottonwood Airport (0MT5) | 2026-06-24 12:46 UTC | 2026-06-24 12:59 UTC | 12m |
| EMD429 | EMD | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-06-24 12:36 UTC | 2026-06-24 12:50 UTC | 14m |
| TKJ68A | TKJ | Sabiha Gokcen International Airport (LTFJ) | Trabzon International Airport (LTCG) | 2026-06-24 11:52 UTC | 2026-06-24 12:50 UTC | 58m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-24 12:35 UTC | 2026-06-24 12:49 UTC | 14m |
| N236MA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-06-24 12:35 UTC | 2026-06-24 12:48 UTC | 13m |
| AZU8750 | AZU | Viracopos International Airport (SBKP) | Lisbon Portela Airport (LPPT) | 2026-06-24 03:01 UTC | 2026-06-24 12:46 UTC | 9h 45m |
| N670MA |  | Kissimmee Gateway Airport (KISM) | Tampa Executive Airport (KVDF) | 2026-06-24 12:12 UTC | 2026-06-24 12:46 UTC | 34m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-24 12:09 UTC | 2026-06-24 12:46 UTC | 37m |
| D9720 |  | Schanis Airport (LSZX) | Muenster Aero Airport (LSPU) | 2026-06-24 10:05 UTC | 2026-06-24 12:45 UTC | 2h 40m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | KDRA (KDRA) | 2026-06-24 12:31 UTC | 2026-06-24 12:41 UTC | 10m |
| SEH3TK | SEH | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-06-24 12:16 UTC | 2026-06-24 12:41 UTC | 25m |
| DETRY | DET | Aschaffenburg Airport (EDFC) | Aschaffenburg Airport (EDFC) | 2026-06-24 12:25 UTC | 2026-06-24 12:41 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
