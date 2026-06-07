# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_13:55:42_UTC-green)

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

**Latest saved flight:** 2026-06-07 13:55:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 13:55:42 UTC

- **105,362** saved flights
- **37,074** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,362** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,289,352.8 tonnes** estimated CO2 emissions
- **74,745,091 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4337 |
| 2 | SkyWest Airlines | 3961 |
| 3 | IndiGo | 2098 |
| 4 | EJA | 2009 |
| 5 | American Airlines | 1691 |
| 6 | Southwest Airlines | 1592 |
| 7 | ENY | 1320 |
| 8 | Delta Air Lines | 1246 |
| 9 | Lufthansa | 1210 |
| 10 | Vueling | 970 |
| 11 | LATAM Airlines | 929 |
| 12 | WIF | 926 |
| 13 | AXM | 908 |
| 14 | AZU | 848 |
| 15 | LXJ | 793 |
| 16 | Swiss International | 765 |
| 17 | All Nippon Airways | 737 |
| 18 | Alaska Airlines | 730 |
| 19 | QLK | 708 |
| 20 | easyJet | 685 |
| 21 | EJU | 668 |
| 22 | Cathay Pacific | 629 |
| 23 | AEE | 609 |
| 24 | VIV | 604 |
| 25 | Air France | 603 |
| 26 | United Airlines | 585 |
| 27 | MXY | 573 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 525 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88507 |
| 2 | 🇪🇸 ES | 7259 |
| 3 | 🇮🇳 IN | 6616 |
| 4 | 🇦🇺 AU | 6353 |
| 5 | 🇧🇷 BR | 5744 |
| 6 | 🇩🇪 DE | 5672 |
| 7 | 🇮🇹 IT | 5626 |
| 8 | 🇨🇦 CA | 5475 |
| 9 | 🇯🇵 JP | 4850 |
| 10 | 🇬🇧 GB | 4457 |
| 11 | 🇫🇷 FR | 4194 |
| 12 | 🇨🇴 CO | 3637 |
| 13 | 🇲🇽 MX | 3150 |
| 14 | 🇬🇷 GR | 3001 |
| 15 | 🇳🇴 NO | 2926 |
| 16 | 🇨🇭 CH | 2702 |
| 17 | 🇲🇾 MY | 2328 |
| 18 | 🇹🇷 TR | 2031 |
| 19 | 🇿🇦 ZA | 1818 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1754 |
| 22 | 🇹🇭 TH | 1749 |
| 23 | 🇵🇱 PL | 1716 |
| 24 | 🇵🇭 PH | 1557 |
| 25 | 🇬🇹 GT | 1526 |
| 26 | 🇲🇦 MA | 1167 |
| 27 | 🇲🇴 MO | 1106 |
| 28 | 🇳🇱 NL | 1035 |
| 29 | 🇲🇪 ME | 1009 |
| 30 | 🇭🇷 HR | 920 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2285 |
| 2 | Denver International Airport |  | US | 1801 |
| 3 | Tokyo International Airport |  | JP | 1606 |
| 4 | Indira Gandhi International Airport |  | IN | 1439 |
| 5 | Harry Reid International Airport |  | US | 1346 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1334 |
| 7 | Guaymaral Airport |  | CO | 1325 |
| 8 | Frankfurt am Main International Airport |  | DE | 1201 |
| 9 | Zurich Airport |  | CH | 1196 |
| 10 | La Aurora Airport |  | GT | 1174 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1134 |
| 12 | El Dorado International Airport |  | CO | 1109 |
| 13 | Macau International Airport |  | MO | 1106 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1065 |
| 15 | Chicago O'Hare International Airport |  | US | 1059 |
| 16 | Madrid Barajas International Airport |  | ES | 922 |
| 17 | Kuala Lumpur International Airport |  | MY | 913 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 900 |
| 19 | Salt Lake City International Airport |  | US | 898 |
| 20 | Capua Airport |  | IT | 892 |
| 21 | Charlotte/Douglas International Airport |  | US | 817 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 810 |
| 23 | Charles de Gaulle International Airport |  | FR | 801 |
| 24 | Congonhas Airport |  | BR | 796 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 789 |
| 27 | Daniel K Inouye International Airport |  | US | 720 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 713 |
| 30 | Barcelona International Airport |  | ES | 692 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 680 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 675 |
| 34 | Amsterdam Airport Schiphol |  | NL | 642 |
| 35 | Don Mueang International Airport |  | TH | 640 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 604 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 601 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 547 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 388 | 21m | 244 km | 1,633.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 259 | 1h 25m | 910 km | 4,064.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 243 | 1h 10m | 770 km | 3,228.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 138 | 18m | 144 km | 343.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 129 | 1h 1m | 695 km | 1,546.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 122 | 44m | 241 km | 506.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N614LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-07 13:38 UTC | 2026-06-07 13:55 UTC | 17m |
| ZXP04 | ZXP | Amsterdam Airport Schiphol (EHAM) | Rotterdam Airport (EHRD) | 2026-06-07 13:36 UTC | 2026-06-07 13:55 UTC | 18m |
| SWR2XH | Swiss International | Malaga Airport (LEMG) | Zurich Airport (LSZH) | 2026-06-07 11:37 UTC | 2026-06-07 13:53 UTC | 2h 15m |
| N2068A |  | Las Serpientes Airport (CN19) | CA54 (CA54) | 2026-06-07 12:15 UTC | 2026-06-07 13:41 UTC | 1h 26m |
| AHC2 | AHC | Squamish Airport (CYSE) | Vancouver International Airport (CYVR) | 2026-06-07 13:21 UTC | 2026-06-07 13:32 UTC | 10m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-06-07 12:24 UTC | 2026-06-07 13:31 UTC | 1h 6m |
| WIF850 | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-06-07 13:13 UTC | 2026-06-07 13:30 UTC | 16m |
| CTN344 | CTN | Zagreb Airport (LDZA) | Visoko Sport Airfield (LQVI) | 2026-06-07 13:03 UTC | 2026-06-07 13:29 UTC | 26m |
| BPX297 | BPX | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-06-07 12:58 UTC | 2026-06-07 13:19 UTC | 21m |
| HAWK239 | HAW | Kingsville Nas Airport (KNQI) | Cage Ranch Airport (7TE2) | 2026-06-07 13:09 UTC | 2026-06-07 13:17 UTC | 8m |
| N1370E |  | Cobb County International/Mccollum Field (KRYY) | Pickens County Airport (KJZP) | 2026-06-07 12:29 UTC | 2026-06-07 13:16 UTC | 47m |
| LXJ264 | LXJ | Houston Executive Airport (KTME) | Mc Elroy Airfield (K20V) | 2026-06-07 11:10 UTC | 2026-06-07 13:15 UTC | 2h 5m |
| BBC493 | BBC | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-06-07 12:44 UTC | 2026-06-07 13:15 UTC | 30m |
| N710NW |  | Richter Aviation Airport (12CN) | Richter Aviation Airport (12CN) | 2026-06-07 13:10 UTC | 2026-06-07 13:14 UTC | 3m |
| VOE7YM | VOE | Valencia Airport (LEVC) | Bilbao Airport (LEBB) | 2026-06-07 12:18 UTC | 2026-06-07 13:09 UTC | 50m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-07 12:33 UTC | 2026-06-07 13:09 UTC | 35m |
| AZU4907 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-06-07 12:18 UTC | 2026-06-07 13:09 UTC | 50m |
| MCK306 | MCK | Sion Airport (LSGS) | Oristano / Fenosu Airport (LIER) | 2026-06-07 11:58 UTC | 2026-06-07 13:08 UTC | 1h 9m |
| RYR78UB | Ryanair | Manchester Airport (EGCC) | Palma De Mallorca Airport (LEPA) | 2026-06-07 10:55 UTC | 2026-06-07 13:08 UTC | 2h 12m |
| WIF5PH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-06-07 12:39 UTC | 2026-06-07 13:06 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
