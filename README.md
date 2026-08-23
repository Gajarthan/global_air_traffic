# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_00:28:36_UTC-green)

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

**Latest saved flight:** 2026-08-23 00:28:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 00:28:36 UTC

- **227,349** saved flights
- **70,533** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,349** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,740,780.5 tonnes** estimated CO2 emissions
- **158,885,828 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9121 |
| 2 | SkyWest Airlines | 8101 |
| 3 | EJA | 4391 |
| 4 | IndiGo | 3831 |
| 5 | American Airlines | 3739 |
| 6 | Southwest Airlines | 3547 |
| 7 | Delta Air Lines | 2918 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2183 |
| 10 | AZU | 2110 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1514 |
| 17 | AXM | 1494 |
| 18 | United Airlines | 1442 |
| 19 | EJU | 1435 |
| 20 | QLK | 1422 |
| 21 | Alaska Airlines | 1379 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1264 |
| 24 | VIV | 1252 |
| 25 | PGT | 1248 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1138 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190460 |
| 2 | 🇪🇸 ES | 14567 |
| 3 | 🇧🇷 BR | 13286 |
| 4 | 🇦🇺 AU | 12795 |
| 5 | 🇨🇦 CA | 12596 |
| 6 | 🇮🇹 IT | 12213 |
| 7 | 🇮🇳 IN | 11937 |
| 8 | 🇩🇪 DE | 11177 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9374 |
| 11 | 🇯🇵 JP | 9204 |
| 12 | 🇫🇷 FR | 9094 |
| 13 | 🇹🇷 TR | 6671 |
| 14 | 🇬🇷 GR | 6643 |
| 15 | 🇲🇽 MX | 6351 |
| 16 | 🇨🇭 CH | 5996 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 3984 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3776 |
| 22 | 🇳🇿 NZ | 3153 |
| 23 | 🇵🇭 PH | 3093 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2685 |
| 26 | 🇭🇷 HR | 2568 |
| 27 | 🇲🇦 MA | 2296 |
| 28 | 🇲🇪 ME | 2053 |
| 29 | 🇳🇱 NL | 2027 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3710 |
| 3 | Tokyo International Airport |  | JP | 2752 |
| 4 | Indira Gandhi International Airport |  | IN | 2752 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2472 |
| 7 | Zurich Airport |  | CH | 2361 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2331 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2292 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2083 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2005 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1936 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1702 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1697 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1644 |
| 22 | Malpensa International Airport |  | IT | 1614 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1591 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1491 |
| 27 | Ninoy Aquino International Airport |  | PH | 1480 |
| 28 | Kuala Lumpur International Airport |  | MY | 1447 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1382 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Viracopos International Airport |  | BR | 1347 |
| 33 | Bengaluru International Airport |  | IN | 1345 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1344 |
| 35 | Seattle-Tacoma International Airport |  | US | 1344 |
| 36 | Calgary International Airport |  | CA | 1297 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 825 | 21m | 244 km | 3,473.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 564 | 1h 6m | 770 km | 7,492.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 343 | 1h 50m | 1,423 km | 8,417.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 306 | 21m | 250 km | 1,321.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 291 | 1h 38m | 1,156 km | 5,805.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 288 | 24m | 218 km | 1,085.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 262 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N213PF |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-08-22 22:48 UTC | 2026-08-23 00:28 UTC | 1h 39m |
| N901ST |  | Gittleson Farms Airport (15IL) | Staton Airport (4LL1) | 2026-08-22 23:47 UTC | 2026-08-23 00:23 UTC | 36m |
| 7788 |  | Caloundra Airport (YCDR) | Caloundra Airport (YCDR) | 2026-08-23 00:06 UTC | 2026-08-23 00:22 UTC | 16m |
| WJA125 | WJA | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-08-22 23:07 UTC | 2026-08-23 00:18 UTC | 1h 11m |
| LTA533 | LTA | TA30 (TA30) | Underline Ok Airport (93XS) | 2026-08-23 00:01 UTC | 2026-08-23 00:14 UTC | 12m |
| RMRNR53 | RMR | North Island Nas (Halsey Field) Airport (KNZY) | San Clemente Island Nalf Airport (KNUC) | 2026-08-22 23:33 UTC | 2026-08-23 00:13 UTC | 39m |
| EJA970 | EJA | Flagstaff Pulliam Airport (KFLG) | Glendale Regional Airport (KGEU) | 2026-08-22 23:37 UTC | 2026-08-23 00:00 UTC | 23m |
| N302TP |  | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-08-22 23:31 UTC | 2026-08-22 23:58 UTC | 26m |
| WXY | WXY | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-22 23:44 UTC | 2026-08-22 23:54 UTC | 10m |
| DAL1260 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-22 22:19 UTC | 2026-08-22 23:48 UTC | 1h 29m |
| TKR16 | TKR | Albuquerque International Sunport Airport (KABQ) | Carrizozo Municipal Airport (KF37) | 2026-08-22 21:25 UTC | 2026-08-22 23:47 UTC | 2h 22m |
| TKR184 | TKR | Stillwater Creek Airport (04WN) | Christensen Field (8WA6) | 2026-08-22 23:12 UTC | 2026-08-22 23:44 UTC | 32m |
| SKY761 | SKY | Gifu Airport (RJNG) | Chitose Air Base (RJCJ) | 2026-08-22 22:20 UTC | 2026-08-22 23:42 UTC | 1h 22m |
| N7485G |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | Majors Airport (KGVT) | 2026-08-22 23:28 UTC | 2026-08-22 23:39 UTC | 10m |
| N29MA |  | Reno/Tahoe International Airport (KRNO) | Minden-Tahoe Airport (KMEV) | 2026-08-22 22:50 UTC | 2026-08-22 23:34 UTC | 43m |
| N916NT |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-22 22:54 UTC | 2026-08-22 23:34 UTC | 39m |
| SKW6259 | SkyWest Airlines | Dallas-Fort Worth International Airport (KDFW) | Santa Fe Regional Airport (KSAF) | 2026-08-22 21:57 UTC | 2026-08-22 23:33 UTC | 1h 35m |
| DAL1342 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Sacramento International Airport (KSMF) | 2026-08-22 22:10 UTC | 2026-08-22 23:31 UTC | 1h 20m |
| TKR01 | TKR | Albuquerque International Sunport Airport (KABQ) | NM49 (NM49) | 2026-08-22 23:19 UTC | 2026-08-22 23:29 UTC | 9m |
| N295HS |  | Merritt Island Airport (KCOI) | Valkaria Airport (KX59) | 2026-08-22 23:12 UTC | 2026-08-22 23:29 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
