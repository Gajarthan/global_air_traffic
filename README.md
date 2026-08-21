# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_16:51:03_UTC-green)

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

**Latest saved flight:** 2026-08-21 16:51:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 16:51:03 UTC

- **222,784** saved flights
- **69,632** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,784** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,681,818.6 tonnes** estimated CO2 emissions
- **155,467,745 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8931 |
| 2 | SkyWest Airlines | 7905 |
| 3 | EJA | 4300 |
| 4 | IndiGo | 3778 |
| 5 | American Airlines | 3680 |
| 6 | Southwest Airlines | 3495 |
| 7 | Delta Air Lines | 2857 |
| 8 | ENY | 2734 |
| 9 | LATAM Airlines | 2121 |
| 10 | AZU | 2047 |
| 11 | Vueling | 1881 |
| 12 | Lufthansa | 1840 |
| 13 | WIF | 1784 |
| 14 | LXJ | 1752 |
| 15 | easyJet | 1542 |
| 16 | Swiss International | 1483 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | EJU | 1396 |
| 20 | United Airlines | 1395 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1333 |
| 23 | PGT | 1222 |
| 24 | GLO | 1220 |
| 25 | VIV | 1210 |
| 26 | Air France | 1207 |
| 27 | WMT | 1187 |
| 28 | Wizz Air | 1147 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186943 |
| 2 | 🇪🇸 ES | 14290 |
| 3 | 🇧🇷 BR | 12893 |
| 4 | 🇦🇺 AU | 12653 |
| 5 | 🇨🇦 CA | 12301 |
| 6 | 🇮🇹 IT | 11877 |
| 7 | 🇮🇳 IN | 11786 |
| 8 | 🇩🇪 DE | 11001 |
| 9 | 🇬🇧 GB | 10450 |
| 10 | 🇨🇴 CO | 9183 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8883 |
| 13 | 🇬🇷 GR | 6499 |
| 14 | 🇹🇷 TR | 6465 |
| 15 | 🇲🇽 MX | 6174 |
| 16 | 🇨🇭 CH | 5867 |
| 17 | 🇳🇴 NO | 5548 |
| 18 | 🇲🇾 MY | 3885 |
| 19 | 🇿🇦 ZA | 3847 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3702 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3020 |
| 24 | 🇬🇹 GT | 2811 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2488 |
| 27 | 🇲🇦 MA | 2241 |
| 28 | 🇲🇪 ME | 1981 |
| 29 | 🇳🇱 NL | 1979 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4663 |
| 2 | Denver International Airport |  | US | 3625 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2708 |
| 5 | Guaymaral Airport |  | CO | 2622 |
| 6 | Harry Reid International Airport |  | US | 2447 |
| 7 | Zurich Airport |  | CH | 2309 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2282 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2259 |
| 10 | La Aurora Airport |  | GT | 2142 |
| 11 | El Dorado International Airport |  | CO | 2079 |
| 12 | Chicago O'Hare International Airport |  | US | 2029 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1913 |
| 15 | Congonhas Airport |  | BR | 1886 |
| 16 | Frankfurt am Main International Airport |  | DE | 1808 |
| 17 | Madrid Barajas International Airport |  | ES | 1744 |
| 18 | Capua Airport |  | IT | 1703 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1664 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1644 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1627 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1563 |
| 25 | Charles de Gaulle International Airport |  | FR | 1534 |
| 26 | Charlotte/Douglas International Airport |  | US | 1474 |
| 27 | Ninoy Aquino International Airport |  | PH | 1438 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1374 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1348 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1315 |
| 34 | Viracopos International Airport |  | BR | 1308 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1269 |
| 36 | Calgary International Airport |  | CA | 1258 |
| 37 | Oslo Gardermoen Airport |  | NO | 1244 |
| 38 | Don Mueang International Airport |  | TH | 1239 |
| 39 | Vitoria/Foronda Airport |  | ES | 1237 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1199 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1070 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 802 | 21m | 244 km | 3,377.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 512 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 502 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 376 | 27m | 275 km | 1,781.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 331 | 1h 50m | 1,423 km | 8,123.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 298 | 21m | 250 km | 1,287.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 282 | 1h 39m | 1,156 km | 5,625.8 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 278 | 24m | 218 km | 1,047.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 274 | 19m | 99 km | 469.3 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 262 | 1h 14m | 961 km | 4,342.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 235 | 28m | 152 km | 614.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5636R |  | Ogden-Hinckley Airport (KOGD) | Flying R Airport (11UT) | 2026-08-21 16:30 UTC | 2026-08-21 16:51 UTC | 20m |
| N13083 |  | 1NC9 (1NC9) | Lincoln County Regional Airport (KIPJ) | 2026-08-21 16:24 UTC | 2026-08-21 16:44 UTC | 19m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-21 15:50 UTC | 2026-08-21 16:42 UTC | 52m |
| N8439T |  | Ramona Airport (KRNM) | Riverside Airport (KRAL) | 2026-08-21 15:53 UTC | 2026-08-21 16:41 UTC | 47m |
| N35121 |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-21 15:50 UTC | 2026-08-21 16:40 UTC | 50m |
| N4775F |  | Atlantic City International Airport (KACY) | Lehigh Valley International Airport (KABE) | 2026-08-21 15:43 UTC | 2026-08-21 16:33 UTC | 50m |
| N300PL |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Cox-Coyour Memorial Field (59MN) | 2026-08-21 15:38 UTC | 2026-08-21 16:30 UTC | 52m |
| VAL211 | VAL | Québec City Jean Lesage International Airport (CYQB) | Downs Gulch Airport (CDV2) | 2026-08-21 16:02 UTC | 2026-08-21 16:29 UTC | 26m |
| N272DS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-21 16:08 UTC | 2026-08-21 16:27 UTC | 19m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-21 16:15 UTC | 2026-08-21 16:26 UTC | 10m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-21 16:16 UTC | 2026-08-21 16:22 UTC | 5m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-08-21 16:09 UTC | 2026-08-21 16:20 UTC | 11m |
| CGHHA | CGH | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-08-21 15:49 UTC | 2026-08-21 16:20 UTC | 31m |
| N54466 |  | Somerset Airport (KSMQ) | Solberg/Hunterdon Airport (KN51) | 2026-08-21 16:00 UTC | 2026-08-21 16:18 UTC | 18m |
| N605JG |  | Sanderson Field (KSHN) | Coeur D'Alene Airport (KCOE) | 2026-08-21 15:18 UTC | 2026-08-21 16:18 UTC | 59m |
| SCU58 | SCU | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-08-21 15:22 UTC | 2026-08-21 16:17 UTC | 54m |
| N383CJ |  | Leesburg Executive Airport (KJYO) | Scottsfield Airpark (CCF9) | 2026-08-21 14:45 UTC | 2026-08-21 16:16 UTC | 1h 31m |
| N38373 |  | Stockton Metro Airport (KSCK) | Hayward Executive Airport (KHWD) | 2026-08-21 15:40 UTC | 2026-08-21 16:16 UTC | 35m |
| N750U |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-21 16:14 UTC | 2026-08-21 16:16 UTC | 2m |
| N526BP |  | Essex County Airport (KCDW) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-21 15:39 UTC | 2026-08-21 16:16 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
