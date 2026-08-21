# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_04:15:57_UTC-green)

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

**Latest saved flight:** 2026-08-21 04:15:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 04:15:57 UTC

- **221,136** saved flights
- **69,333** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,661,145.7 tonnes** estimated CO2 emissions
- **154,269,315 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8847 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3741 |
| 5 | American Airlines | 3669 |
| 6 | Southwest Airlines | 3490 |
| 7 | Delta Air Lines | 2850 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2102 |
| 10 | AZU | 2030 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1451 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1388 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1349 |
| 22 | All Nippon Airways | 1325 |
| 23 | GLO | 1210 |
| 24 | VIV | 1206 |
| 25 | PGT | 1202 |
| 26 | Air France | 1197 |
| 27 | WMT | 1164 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186218 |
| 2 | 🇪🇸 ES | 14142 |
| 3 | 🇧🇷 BR | 12782 |
| 4 | 🇦🇺 AU | 12536 |
| 5 | 🇨🇦 CA | 12228 |
| 6 | 🇮🇹 IT | 11742 |
| 7 | 🇮🇳 IN | 11666 |
| 8 | 🇩🇪 DE | 10898 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9100 |
| 11 | 🇯🇵 JP | 8989 |
| 12 | 🇫🇷 FR | 8786 |
| 13 | 🇬🇷 GR | 6437 |
| 14 | 🇹🇷 TR | 6368 |
| 15 | 🇲🇽 MX | 6155 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3843 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇹🇭 TH | 3676 |
| 21 | 🇵🇱 PL | 3664 |
| 22 | 🇳🇿 NZ | 3074 |
| 23 | 🇵🇭 PH | 2988 |
| 24 | 🇬🇹 GT | 2791 |
| 25 | 🇰🇷 KR | 2641 |
| 26 | 🇭🇷 HR | 2447 |
| 27 | 🇲🇦 MA | 2220 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3614 |
| 3 | Tokyo International Airport |  | JP | 2698 |
| 4 | Indira Gandhi International Airport |  | IN | 2679 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2442 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2240 |
| 10 | La Aurora Airport |  | GT | 2127 |
| 11 | El Dorado International Airport |  | CO | 2072 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1629 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1585 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1558 |
| 24 | Malpensa International Airport |  | IT | 1548 |
| 25 | Charles de Gaulle International Airport |  | FR | 1519 |
| 26 | Charlotte/Douglas International Airport |  | US | 1470 |
| 27 | Ninoy Aquino International Airport |  | PH | 1422 |
| 28 | Kuala Lumpur International Airport |  | MY | 1406 |
| 29 | Barcelona International Airport |  | ES | 1356 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1344 |
| 31 | Bengaluru International Airport |  | IN | 1326 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1312 |
| 34 | Viracopos International Airport |  | BR | 1298 |
| 35 | Calgary International Airport |  | CA | 1255 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1209 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 795 | 21m | 244 km | 3,347.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 547 | 1h 7m | 770 km | 7,266.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 531 | 24m | 225 km | 2,060.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 326 | 1h 50m | 1,423 km | 8,000.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 276 | 1h 38m | 1,156 km | 5,506.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 274 | 24m | 218 km | 1,032.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 253 | 44m | 555 km | 2,422.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N454NG |  | Republic Airport (KFRG) | Worcester Regional Airport (KORH) | 2026-08-21 03:42 UTC | 2026-08-21 04:15 UTC | 33m |
| RYR7509 | Ryanair | Barcelona International Airport (LEBL) | Barcelona International Airport (LEBL) | 2026-08-20 21:47 UTC | 2026-08-21 04:07 UTC | 6h 19m |
| ANA8441 | All Nippon Airways | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-21 01:08 UTC | 2026-08-21 04:03 UTC | 2h 55m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-21 02:33 UTC | 2026-08-21 04:01 UTC | 1h 28m |
| AAL3286 | American Airlines | Harry Reid International Airport (KLAS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-21 01:23 UTC | 2026-08-21 03:58 UTC | 2h 35m |
| ANA859 | All Nippon Airways | Tokyo International Airport (RJTT) | Chek Lap Kok International Airport (VHHH) | 2026-08-21 00:09 UTC | 2026-08-21 03:57 UTC | 3h 47m |
| CFSCD | CFS | Tucson International Airport (KTUS) | Calgary International Airport (CYYC) | 2026-08-21 00:40 UTC | 2026-08-21 03:57 UTC | 3h 16m |
| BCS5959 | BCS | Leipzig Halle Airport (EDDP) | Zielona Góra-Babimost Airport (EPZG) | 2026-08-21 03:22 UTC | 2026-08-21 03:46 UTC | 23m |
| VTE3304 | VTE | Phoenix Sky Harbor International Airport (KPHX) | Flagstaff Pulliam Airport (KFLG) | 2026-08-21 03:17 UTC | 2026-08-21 03:46 UTC | 28m |
| CFSUG | CFS | Edmonton International Airport (CYEG) | Glendon Airport (CFP5) | 2026-08-21 03:15 UTC | 2026-08-21 03:41 UTC | 25m |
| N410W |  | Martin Airport (IL82) | Frasca Field (KC16) | 2026-08-21 03:19 UTC | 2026-08-21 03:36 UTC | 17m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-08-21 03:17 UTC | 2026-08-21 03:30 UTC | 13m |
| VTM5001 | VTM | Monclova International Airport (MMMV) | Plan De Guadalupe International Airport (MMIO) | 2026-08-21 03:15 UTC | 2026-08-21 03:30 UTC | 14m |
| AWH95C | AWH | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-08-21 02:50 UTC | 2026-08-21 03:28 UTC | 38m |
| TKR168 | TKR | Fairbanks International Airport (PAFA) | Fairbanks International Airport (PAFA) | 2026-08-21 02:02 UTC | 2026-08-21 03:27 UTC | 1h 24m |
| BLKT01 | BLK | RAAF Base Edinburgh (YPED) | Cabramurra Airport (YCUR) | 2026-08-21 01:55 UTC | 2026-08-21 03:26 UTC | 1h 31m |
| N57KT |  | Dane County Regional/Truax Field (KMSN) | Dane County Regional/Truax Field (KMSN) | 2026-08-21 03:01 UTC | 2026-08-21 03:25 UTC | 23m |
| IGO7719 | IndiGo | Kalka Airport (VI71) | Jaipur International Airport (VIJP) | 2026-08-21 02:30 UTC | 2026-08-21 03:23 UTC | 53m |
| PGT6266 | PGT | Copernicus Wrocław Airport (EPWR) | Antalya International Airport (LTAI) | 2026-08-21 00:40 UTC | 2026-08-21 03:23 UTC | 2h 42m |
| FOX1 | FOX | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-21 03:21 UTC | 2026-08-21 03:22 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
