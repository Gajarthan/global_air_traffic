# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_20:54:35_UTC-green)

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

**Latest saved flight:** 2026-07-29 20:54:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 20:54:35 UTC

- **159,234** saved flights
- **52,720** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,234** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,910,777.8 tonnes** estimated CO2 emissions
- **110,769,725 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6393 |
| 2 | SkyWest Airlines | 5816 |
| 3 | EJA | 3164 |
| 4 | IndiGo | 2802 |
| 5 | American Airlines | 2525 |
| 6 | Southwest Airlines | 2499 |
| 7 | ENY | 1983 |
| 8 | Delta Air Lines | 1890 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1495 |
| 11 | AZU | 1403 |
| 12 | WIF | 1350 |
| 13 | Vueling | 1335 |
| 14 | LXJ | 1228 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1098 |
| 17 | easyJet | 1039 |
| 18 | Alaska Airlines | 995 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 976 |
| 22 | VIV | 874 |
| 23 | CXK | 845 |
| 24 | United Airlines | 842 |
| 25 | GLO | 839 |
| 26 | AEE | 837 |
| 27 | Cathay Pacific | 836 |
| 28 | Air France | 829 |
| 29 | MXY | 829 |
| 30 | JetBlue | 818 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 137443 |
| 2 | 🇪🇸 ES | 10235 |
| 3 | 🇧🇷 BR | 9117 |
| 4 | 🇦🇺 AU | 8957 |
| 5 | 🇮🇳 IN | 8814 |
| 6 | 🇨🇦 CA | 8634 |
| 7 | 🇮🇹 IT | 8235 |
| 8 | 🇩🇪 DE | 8063 |
| 9 | 🇬🇧 GB | 7303 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6302 |
| 12 | 🇨🇴 CO | 5604 |
| 13 | 🇲🇽 MX | 4575 |
| 14 | 🇬🇷 GR | 4568 |
| 15 | 🇳🇴 NO | 4219 |
| 16 | 🇨🇭 CH | 4169 |
| 17 | 🇹🇷 TR | 3799 |
| 18 | 🇲🇾 MY | 2893 |
| 19 | 🇵🇱 PL | 2709 |
| 20 | 🇿🇦 ZA | 2573 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2276 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2036 |
| 26 | 🇲🇦 MA | 1616 |
| 27 | 🇲🇪 ME | 1524 |
| 28 | 🇭🇷 HR | 1478 |
| 29 | 🇳🇱 NL | 1454 |
| 30 | 🇲🇴 MO | 1317 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3257 |
| 2 | Denver International Airport |  | US | 2653 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 2004 |
| 5 | Indira Gandhi International Airport |  | IN | 1963 |
| 6 | Harry Reid International Airport |  | US | 1942 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1767 |
| 8 | Zurich Airport |  | CH | 1705 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1672 |
| 10 | La Aurora Airport |  | GT | 1579 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1487 |
| 12 | Frankfurt am Main International Airport |  | DE | 1464 |
| 13 | El Dorado International Airport |  | CO | 1455 |
| 14 | Chicago O'Hare International Airport |  | US | 1442 |
| 15 | Salt Lake City International Airport |  | US | 1430 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1328 |
| 17 | Congonhas Airport |  | BR | 1321 |
| 18 | Macau International Airport |  | MO | 1317 |
| 19 | Madrid Barajas International Airport |  | ES | 1263 |
| 20 | Capua Airport |  | IT | 1257 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1223 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1138 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1134 |
| 24 | Charlotte/Douglas International Airport |  | US | 1119 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Malpensa International Airport |  | IT | 1053 |
| 28 | Bengaluru International Airport |  | IN | 1049 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 970 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 969 |
| 32 | Barcelona International Airport |  | ES | 950 |
| 33 | Daniel K Inouye International Airport |  | US | 939 |
| 34 | Seattle-Tacoma International Airport |  | US | 927 |
| 35 | Calgary International Airport |  | CA | 911 |
| 36 | Viracopos International Airport |  | BR | 910 |
| 37 | Scottsdale Airport |  | US | 901 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 874 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 841 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 578 | 21m | 244 km | 2,433.8 t |
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
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 191 | 30m | 49 km | 161.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 189 | 1h 15m | 961 km | 3,132.8 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 181 | 50m | 556 km | 1,735.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N250DV |  | Somerville Airport (2MI5) | KHLM (KHLM) | 2026-07-29 20:38 UTC | 2026-07-29 20:54 UTC | 16m |
| N963SP |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-07-29 20:20 UTC | 2026-07-29 20:47 UTC | 26m |
| VIV7370 | VIV | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-29 16:37 UTC | 2026-07-29 20:43 UTC | 4h 5m |
| CFNYX | CFN | Thunder Bay Airport (CYQT) | Thunder Bay Airport (CYQT) | 2026-07-29 20:06 UTC | 2026-07-29 20:42 UTC | 36m |
| N13715 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-07-29 20:27 UTC | 2026-07-29 20:40 UTC | 12m |
| N814SS |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-29 20:15 UTC | 2026-07-29 20:39 UTC | 23m |
| N555GA |  | Dallas Love Field (KDAL) | Faith Municipal Airport (KD07) | 2026-07-29 18:59 UTC | 2026-07-29 20:38 UTC | 1h 39m |
| N724JH |  | Chandler Municipal Airport (KCHD) | Pegasus Airpark (5AZ3) | 2026-07-29 20:25 UTC | 2026-07-29 20:37 UTC | 11m |
| QTR1366 | Qatar Airways | O. R. Tambo International Airport (FAOR) | Doha International Airport (OTBD) | 2026-07-29 12:37 UTC | 2026-07-29 20:33 UTC | 7h 56m |
| QTR9C | Qatar Airways | Munich International Airport (EDDM) | Hamad International Airport (OTHH) | 2026-07-29 14:48 UTC | 2026-07-29 20:33 UTC | 5h 44m |
| QTR302 | Qatar Airways | Helsinki Vantaa Airport (EFHK) | Hamad International Airport (OTHH) | 2026-07-29 14:24 UTC | 2026-07-29 20:33 UTC | 6h 8m |
| N500CF |  | Boeing Field/King County International Airport (KBFI) | Port Mcneill Airport (CAT5) | 2026-07-29 19:51 UTC | 2026-07-29 20:30 UTC | 38m |
| TIBKC | TIB | Juan Santamaria International Airport (MROC) | Portalon Airport (MRPL) | 2026-07-29 20:11 UTC | 2026-07-29 20:30 UTC | 19m |
| N24VF |  | 1XA0 (1XA0) | 69TE (69TE) | 2026-07-29 19:09 UTC | 2026-07-29 20:28 UTC | 1h 19m |
| PAV543H | PAV | Zaragoza Air Base (LEZG) | E. Castellanos-Villacastin Airport (LEEV) | 2026-07-29 19:46 UTC | 2026-07-29 20:27 UTC | 41m |
| N52620 |  | Mc Clellan-Palomar Airport (KCRQ) | CA84 (CA84) | 2026-07-29 19:53 UTC | 2026-07-29 20:27 UTC | 34m |
| TKR210 | TKR | Roberts Field (KRDM) | NV44 (NV44) | 2026-07-29 19:05 UTC | 2026-07-29 20:24 UTC | 1h 19m |
| N253TA |  | Trading Bay Production Airport (5AK0) | Trading Bay Production Airport (5AK0) | 2026-07-29 20:21 UTC | 2026-07-29 20:24 UTC | 2m |
| N695ND |  | Allentown Queen City Municipal Airport (KXLL) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-29 19:20 UTC | 2026-07-29 20:22 UTC | 1h 2m |
| N50XX |  | Nashville International Airport (KBNA) | Maury County Regional Airport (KMRC) | 2026-07-29 20:11 UTC | 2026-07-29 20:22 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
