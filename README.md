# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_22:41:34_UTC-green)

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

**Latest saved flight:** 2026-07-10 22:41:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 22:41:34 UTC

- **136,207** saved flights
- **46,015** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,207** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,637,240.3 tonnes** estimated CO2 emissions
- **94,912,483 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5515 |
| 2 | SkyWest Airlines | 5007 |
| 3 | EJA | 2676 |
| 4 | IndiGo | 2509 |
| 5 | American Airlines | 2143 |
| 6 | Southwest Airlines | 2050 |
| 7 | ENY | 1711 |
| 8 | Delta Air Lines | 1623 |
| 9 | Lufthansa | 1398 |
| 10 | LATAM Airlines | 1248 |
| 11 | Vueling | 1183 |
| 12 | WIF | 1181 |
| 13 | AZU | 1169 |
| 14 | LXJ | 1049 |
| 15 | AXM | 1028 |
| 16 | Swiss International | 967 |
| 17 | All Nippon Airways | 882 |
| 18 | easyJet | 880 |
| 19 | Alaska Airlines | 861 |
| 20 | QLK | 852 |
| 21 | EJU | 834 |
| 22 | VIV | 746 |
| 23 | AEE | 736 |
| 24 | CXK | 729 |
| 25 | Air France | 727 |
| 26 | Cathay Pacific | 726 |
| 27 | United Airlines | 718 |
| 28 | JetBlue | 717 |
| 29 | MXY | 709 |
| 30 | GLO | 696 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117091 |
| 2 | 🇪🇸 ES | 8985 |
| 3 | 🇮🇳 IN | 7873 |
| 4 | 🇦🇺 AU | 7833 |
| 5 | 🇧🇷 BR | 7681 |
| 6 | 🇨🇦 CA | 7206 |
| 7 | 🇩🇪 DE | 7087 |
| 8 | 🇮🇹 IT | 7052 |
| 9 | 🇬🇧 GB | 6153 |
| 10 | 🇯🇵 JP | 5773 |
| 11 | 🇫🇷 FR | 5398 |
| 12 | 🇨🇴 CO | 4284 |
| 13 | 🇲🇽 MX | 3958 |
| 14 | 🇬🇷 GR | 3867 |
| 15 | 🇳🇴 NO | 3683 |
| 16 | 🇨🇭 CH | 3519 |
| 17 | 🇹🇷 TR | 3124 |
| 18 | 🇲🇾 MY | 2670 |
| 19 | 🇵🇱 PL | 2254 |
| 20 | 🇿🇦 ZA | 2241 |
| 21 | 🇳🇿 NZ | 2119 |
| 22 | 🇹🇭 TH | 2071 |
| 23 | 🇰🇷 KR | 1992 |
| 24 | 🇵🇭 PH | 1867 |
| 25 | 🇬🇹 GT | 1834 |
| 26 | 🇲🇦 MA | 1432 |
| 27 | 🇲🇪 ME | 1350 |
| 28 | 🇳🇱 NL | 1266 |
| 29 | 🇭🇷 HR | 1213 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2834 |
| 2 | Denver International Airport |  | US | 2287 |
| 3 | Tokyo International Airport |  | JP | 1885 |
| 4 | Indira Gandhi International Airport |  | IN | 1739 |
| 5 | Harry Reid International Airport |  | US | 1705 |
| 6 | Guaymaral Airport |  | CO | 1654 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1584 |
| 8 | Zurich Airport |  | CH | 1512 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1443 |
| 10 | La Aurora Airport |  | GT | 1417 |
| 11 | Frankfurt am Main International Airport |  | DE | 1352 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1308 |
| 13 | Chicago O'Hare International Airport |  | US | 1291 |
| 14 | El Dorado International Airport |  | CO | 1214 |
| 15 | Salt Lake City International Airport |  | US | 1210 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1178 |
| 18 | Madrid Barajas International Airport |  | ES | 1109 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1107 |
| 20 | Capua Airport |  | IT | 1105 |
| 21 | Congonhas Airport |  | BR | 1091 |
| 22 | Kuala Lumpur International Airport |  | MY | 1036 |
| 23 | Charlotte/Douglas International Airport |  | US | 999 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 985 |
| 25 | Charles de Gaulle International Airport |  | FR | 970 |
| 26 | Bengaluru International Airport |  | IN | 946 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 937 |
| 28 | Malpensa International Airport |  | IT | 893 |
| 29 | Ninoy Aquino International Airport |  | PH | 869 |
| 30 | Daniel K Inouye International Airport |  | US | 841 |
| 31 | Barcelona International Airport |  | ES | 832 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 831 |
| 33 | Tenerife Norte Airport |  | ES | 811 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 804 |
| 35 | Calgary International Airport |  | CA | 796 |
| 36 | Scottsdale Airport |  | US | 784 |
| 37 | Viracopos International Airport |  | BR | 778 |
| 38 | Seattle-Tacoma International Airport |  | US | 777 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 759 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 696 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 492 | 21m | 244 km | 2,071.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 334 | 24m | 225 km | 1,295.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 326 | 1h 10m | 770 km | 4,330.7 t |
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
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 168 | 31m | 369 km | 1,069.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 167 | 20m | 250 km | 721.3 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
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
| CFMES | CFM | Calgary International Airport (CYYC) | Edmonton International Airport (CYEG) | 2026-07-10 22:12 UTC | 2026-07-10 22:41 UTC | 29m |
| TKR104 | TKR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-10 22:13 UTC | 2026-07-10 22:40 UTC | 26m |
| BOE160 | BOE | Renton Municipal Airport (KRNT) | Warden Airport (K2S4) | 2026-07-10 21:05 UTC | 2026-07-10 22:36 UTC | 1h 30m |
| N6479Y |  | Crane County Airport (KE13) | 74XS (74XS) | 2026-07-10 22:13 UTC | 2026-07-10 22:34 UTC | 20m |
| AAL1838 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Philadelphia International Airport (KPHL) | 2026-07-10 21:19 UTC | 2026-07-10 22:33 UTC | 1h 13m |
| TRP3 | TRP | Valley Point Airport (WV29) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-07-10 22:21 UTC | 2026-07-10 22:27 UTC | 5m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-07-10 11:26 UTC | 2026-07-10 22:26 UTC | 10h 59m |
| TKR107 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | CD82 (CD82) | 2026-07-10 20:18 UTC | 2026-07-10 22:25 UTC | 2h 6m |
| EJA920 | EJA | Rogers Field (KO05) | Moffett Federal Airfield (KNUQ) | 2026-07-10 21:40 UTC | 2026-07-10 22:23 UTC | 43m |
| JAS918 | JAS | Laurence G Hanscom Field (KBED) | Thunder Bay Airport (CYQT) | 2026-07-10 20:13 UTC | 2026-07-10 22:20 UTC | 2h 6m |
| N33MC |  | Roberts Field (KRDM) | Truckee-Tahoe Airport (KTRK) | 2026-07-10 21:21 UTC | 2026-07-10 22:20 UTC | 58m |
| SHOOT11 | SHO | Fort Smith Regional Airport (KFSM) | Petit Jean Park Airport (KMPJ) | 2026-07-10 22:09 UTC | 2026-07-10 22:20 UTC | 10m |
| N3802C |  | Cortez Municipal Airport (KCEZ) | Tanner Field (CO27) | 2026-07-10 21:28 UTC | 2026-07-10 22:19 UTC | 50m |
| KOW523 | KOW | City Of Colorado Springs Municipal Airport (KCOS) | Truckee-Tahoe Airport (KTRK) | 2026-07-10 20:05 UTC | 2026-07-10 22:17 UTC | 2h 12m |
| N38617 |  | Skypark Airport (KBTF) | Wendover Airport (KENV) | 2026-07-10 21:29 UTC | 2026-07-10 22:16 UTC | 46m |
| FSR410 | FSR | Chicago Executive Airport (KPWK) | Wall Municipal Airport (K6V4) | 2026-07-10 20:36 UTC | 2026-07-10 22:15 UTC | 1h 38m |
| N115YS |  | Visalia Municipal Airport (KVIS) | Lake Tahoe Airport (KTVL) | 2026-07-10 21:35 UTC | 2026-07-10 22:14 UTC | 39m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-10 21:41 UTC | 2026-07-10 22:14 UTC | 32m |
| TKR138 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-10 21:28 UTC | 2026-07-10 22:13 UTC | 44m |
| N552TJ |  | Trenton Mercer Airport (KTTN) | Philadelphia International Airport (KPHL) | 2026-07-10 21:57 UTC | 2026-07-10 22:13 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
