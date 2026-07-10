# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_17:41:41_UTC-green)

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

**Latest saved flight:** 2026-07-10 17:41:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 17:41:41 UTC

- **136,009** saved flights
- **45,951** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,009** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,635,014.7 tonnes** estimated CO2 emissions
- **94,783,458 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5510 |
| 2 | SkyWest Airlines | 4996 |
| 3 | EJA | 2667 |
| 4 | IndiGo | 2508 |
| 5 | American Airlines | 2138 |
| 6 | Southwest Airlines | 2045 |
| 7 | ENY | 1707 |
| 8 | Delta Air Lines | 1621 |
| 9 | Lufthansa | 1398 |
| 10 | LATAM Airlines | 1246 |
| 11 | Vueling | 1183 |
| 12 | WIF | 1181 |
| 13 | AZU | 1165 |
| 14 | LXJ | 1047 |
| 15 | AXM | 1028 |
| 16 | Swiss International | 967 |
| 17 | All Nippon Airways | 882 |
| 18 | easyJet | 880 |
| 19 | Alaska Airlines | 861 |
| 20 | QLK | 851 |
| 21 | EJU | 834 |
| 22 | VIV | 745 |
| 23 | AEE | 736 |
| 24 | CXK | 729 |
| 25 | Air France | 727 |
| 26 | Cathay Pacific | 725 |
| 27 | United Airlines | 718 |
| 28 | JetBlue | 715 |
| 29 | MXY | 706 |
| 30 | GLO | 695 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116826 |
| 2 | 🇪🇸 ES | 8979 |
| 3 | 🇮🇳 IN | 7871 |
| 4 | 🇦🇺 AU | 7826 |
| 5 | 🇧🇷 BR | 7667 |
| 6 | 🇨🇦 CA | 7197 |
| 7 | 🇩🇪 DE | 7087 |
| 8 | 🇮🇹 IT | 7049 |
| 9 | 🇬🇧 GB | 6148 |
| 10 | 🇯🇵 JP | 5771 |
| 11 | 🇫🇷 FR | 5395 |
| 12 | 🇨🇴 CO | 4280 |
| 13 | 🇲🇽 MX | 3952 |
| 14 | 🇬🇷 GR | 3866 |
| 15 | 🇳🇴 NO | 3683 |
| 16 | 🇨🇭 CH | 3518 |
| 17 | 🇹🇷 TR | 3119 |
| 18 | 🇲🇾 MY | 2670 |
| 19 | 🇵🇱 PL | 2252 |
| 20 | 🇿🇦 ZA | 2241 |
| 21 | 🇳🇿 NZ | 2117 |
| 22 | 🇹🇭 TH | 2071 |
| 23 | 🇰🇷 KR | 1992 |
| 24 | 🇵🇭 PH | 1861 |
| 25 | 🇬🇹 GT | 1831 |
| 26 | 🇲🇦 MA | 1431 |
| 27 | 🇲🇪 ME | 1348 |
| 28 | 🇳🇱 NL | 1266 |
| 29 | 🇭🇷 HR | 1211 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2831 |
| 2 | Denver International Airport |  | US | 2282 |
| 3 | Tokyo International Airport |  | JP | 1884 |
| 4 | Indira Gandhi International Airport |  | IN | 1739 |
| 5 | Harry Reid International Airport |  | US | 1701 |
| 6 | Guaymaral Airport |  | CO | 1654 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1584 |
| 8 | Zurich Airport |  | CH | 1512 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1440 |
| 10 | La Aurora Airport |  | GT | 1414 |
| 11 | Frankfurt am Main International Airport |  | DE | 1352 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1307 |
| 13 | Chicago O'Hare International Airport |  | US | 1288 |
| 14 | El Dorado International Airport |  | CO | 1214 |
| 15 | Salt Lake City International Airport |  | US | 1210 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1178 |
| 18 | Madrid Barajas International Airport |  | ES | 1108 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1106 |
| 20 | Capua Airport |  | IT | 1105 |
| 21 | Congonhas Airport |  | BR | 1090 |
| 22 | Kuala Lumpur International Airport |  | MY | 1036 |
| 23 | Charlotte/Douglas International Airport |  | US | 998 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 985 |
| 25 | Charles de Gaulle International Airport |  | FR | 970 |
| 26 | Bengaluru International Airport |  | IN | 946 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 935 |
| 28 | Malpensa International Airport |  | IT | 891 |
| 29 | Ninoy Aquino International Airport |  | PH | 866 |
| 30 | Daniel K Inouye International Airport |  | US | 841 |
| 31 | Barcelona International Airport |  | ES | 832 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 829 |
| 33 | Tenerife Norte Airport |  | ES | 809 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 798 |
| 35 | Calgary International Airport |  | CA | 793 |
| 36 | Scottsdale Airport |  | US | 783 |
| 37 | Seattle-Tacoma International Airport |  | US | 776 |
| 38 | Viracopos International Airport |  | BR | 774 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 759 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 696 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 492 | 21m | 244 km | 2,071.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 334 | 24m | 225 km | 1,295.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 325 | 1h 10m | 770 km | 4,317.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 292 | 14m | 114 km | 572.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 255 | 26m | 275 km | 1,208.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 247 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 201 | 22m | 55 km | 191.0 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 188 | 26m | 215 km | 696.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 183 | 1h 46m | 1,423 km | 4,491.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 167 | 20m | 250 km | 721.3 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 162 | 30m | 49 km | 136.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 161 | 44m | 452 km | 1,254.8 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 155 | 1h 38m | 1,156 km | 3,092.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N233ME |  | 95CA (95CA) | Poso-Kern County Airport (KL73) | 2026-07-10 17:05 UTC | 2026-07-10 17:41 UTC | 36m |
| N178FV |  | Council Bluffs Municipal Airport (KCBF) | Ridge Airport (IA01) | 2026-07-10 17:25 UTC | 2026-07-10 17:41 UTC | 15m |
| N999AB |  | Giesen-Lutzellinden Airport (EDFL) | Bonn-Hangelar Airport (EDKB) | 2026-07-10 17:08 UTC | 2026-07-10 17:38 UTC | 29m |
| N988HP |  | Palm Springs International Airport (KPSP) | Palm Springs International Airport (KPSP) | 2026-07-10 17:22 UTC | 2026-07-10 17:37 UTC | 15m |
| N954JH |  | Sky Acres Airport (K44N) | 0NK8 (0NK8) | 2026-07-10 17:00 UTC | 2026-07-10 17:36 UTC | 36m |
| VAR403 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-07-10 17:18 UTC | 2026-07-10 17:34 UTC | 15m |
| N7209F |  | New Garden Airport (KN57) | New Garden Airport (KN57) | 2026-07-10 17:23 UTC | 2026-07-10 17:34 UTC | 10m |
| N62VY |  | Bend Municipal Airport (KBDN) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-07-10 17:09 UTC | 2026-07-10 17:22 UTC | 12m |
| N129FR |  | NY09 (NY09) | 0NK8 (0NK8) | 2026-07-10 17:04 UTC | 2026-07-10 17:20 UTC | 15m |
| HOTWAX6 | HOT | 2MS9 (2MS9) | 2MS9 (2MS9) | 2026-07-10 17:06 UTC | 2026-07-10 17:20 UTC | 13m |
| ASP508 | ASP | Calgary International Airport (CYYC) | Calgary International Airport (CYYC) | 2026-07-10 16:42 UTC | 2026-07-10 17:19 UTC | 36m |
| HLE27 | HLE | London Biggin Hill Airport (EGKB) | London City Airport (EGLC) | 2026-07-10 16:50 UTC | 2026-07-10 17:19 UTC | 28m |
| N441CJ |  | Boise Air Trml/Gowen Field (KBOI) | Lexington Airport (K9S9) | 2026-07-10 15:25 UTC | 2026-07-10 17:16 UTC | 1h 50m |
| UAL306 | United Airlines | Zemunik Airport (LDZD) | Newark Liberty International Airport (KEWR) | 2026-07-10 08:04 UTC | 2026-07-10 17:16 UTC | 9h 11m |
| PAG09 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Virden/R.J. (Bob) Andrew Field Regional Aerodrome (CYVD) | 2026-07-10 16:32 UTC | 2026-07-10 17:14 UTC | 41m |
| N629LH |  | Carson City Airport (KCXP) | Carson City Airport (KCXP) | 2026-07-10 17:03 UTC | 2026-07-10 17:13 UTC | 10m |
| N712PA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-10 16:57 UTC | 2026-07-10 17:12 UTC | 14m |
| N12973 |  | Montgomery County Airpark (KGAI) | Montgomery County Airpark (KGAI) | 2026-07-10 17:03 UTC | 2026-07-10 17:07 UTC | 4m |
| N7688M |  | Cable Airport (KCCB) | Whiteman Airport (KWHP) | 2026-07-10 16:42 UTC | 2026-07-10 17:04 UTC | 22m |
| OKSLM | OKS | Pribram Airport (LKPM) | Otocac Airport (LDRO) | 2026-07-10 15:59 UTC | 2026-07-10 17:04 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
