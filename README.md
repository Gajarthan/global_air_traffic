# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_20:49:44_UTC-green)

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

**Latest saved flight:** 2026-08-19 20:49:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 20:49:44 UTC

- **217,287** saved flights
- **68,538** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,287** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,614,415.6 tonnes** estimated CO2 emissions
- **151,560,322 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8697 |
| 2 | SkyWest Airlines | 7766 |
| 3 | EJA | 4233 |
| 4 | IndiGo | 3692 |
| 5 | American Airlines | 3622 |
| 6 | Southwest Airlines | 3450 |
| 7 | Delta Air Lines | 2810 |
| 8 | ENY | 2683 |
| 9 | LATAM Airlines | 2055 |
| 10 | AZU | 1991 |
| 11 | Vueling | 1826 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1716 |
| 15 | easyJet | 1510 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1374 |
| 19 | EJU | 1353 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1328 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1191 |
| 24 | GLO | 1182 |
| 25 | PGT | 1178 |
| 26 | Air France | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1108 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183245 |
| 2 | 🇪🇸 ES | 13933 |
| 3 | 🇧🇷 BR | 12531 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11967 |
| 6 | 🇮🇹 IT | 11540 |
| 7 | 🇮🇳 IN | 11493 |
| 8 | 🇩🇪 DE | 10760 |
| 9 | 🇬🇧 GB | 10207 |
| 10 | 🇨🇴 CO | 8913 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8662 |
| 13 | 🇬🇷 GR | 6345 |
| 14 | 🇹🇷 TR | 6247 |
| 15 | 🇲🇽 MX | 6067 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3588 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 3000 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2757 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2387 |
| 27 | 🇲🇦 MA | 2188 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1902 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4562 |
| 2 | Denver International Airport |  | US | 3542 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2627 |
| 5 | Guaymaral Airport |  | CO | 2594 |
| 6 | Harry Reid International Airport |  | US | 2408 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2233 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2211 |
| 10 | La Aurora Airport |  | GT | 2097 |
| 11 | El Dorado International Airport |  | CO | 2029 |
| 12 | Chicago O'Hare International Airport |  | US | 1998 |
| 13 | Salt Lake City International Airport |  | US | 1920 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1896 |
| 15 | Congonhas Airport |  | BR | 1829 |
| 16 | Frankfurt am Main International Airport |  | DE | 1778 |
| 17 | Madrid Barajas International Airport |  | ES | 1702 |
| 18 | Capua Airport |  | IT | 1654 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1637 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1612 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1593 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1527 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1492 |
| 26 | Charlotte/Douglas International Airport |  | US | 1458 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1332 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1326 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1297 |
| 33 | Seattle-Tacoma International Airport |  | US | 1286 |
| 34 | Viracopos International Airport |  | BR | 1271 |
| 35 | Calgary International Airport |  | CA | 1222 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1193 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 774 | 21m | 244 km | 3,259.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 490 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 481 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 245 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 234 | 1h 49m | 1,304 km | 5,264.4 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7140J |  | Laconia Municipal Airport (KLCI) | Laconia Municipal Airport (KLCI) | 2026-08-19 20:09 UTC | 2026-08-19 20:49 UTC | 40m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-19 18:40 UTC | 2026-08-19 20:48 UTC | 2h 7m |
| LIFELN1 | LIF | Elk Park Ranch Airport (34CD) | Northern Colorado Regional Airport (KFNL) | 2026-08-19 20:33 UTC | 2026-08-19 20:45 UTC | 11m |
| N538SA |  | Pompano Beach Airpark (KPMP) | Witham Field (KSUA) | 2026-08-19 20:12 UTC | 2026-08-19 20:44 UTC | 32m |
| N846RS |  | Salinas Municipal Airport (KSNS) | Clark Ranch Airport (3CA9) | 2026-08-19 19:38 UTC | 2026-08-19 20:38 UTC | 59m |
| N1976F |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-19 19:38 UTC | 2026-08-19 20:36 UTC | 58m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-08-19 06:10 UTC | 2026-08-19 20:35 UTC | 14h 24m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-19 19:19 UTC | 2026-08-19 20:32 UTC | 1h 13m |
| PIKES42 | PIK | Boulder Municipal Airport (KBDU) | CO86 (CO86) | 2026-08-19 20:18 UTC | 2026-08-19 20:32 UTC | 13m |
| BLIND63 | BLI | City Of Colorado Springs Municipal Airport (KCOS) | Perry Park Airport (CO93) | 2026-08-19 20:06 UTC | 2026-08-19 20:31 UTC | 25m |
| N54466 |  | Somerset Airport (KSMQ) | Solberg/Hunterdon Airport (KN51) | 2026-08-19 19:38 UTC | 2026-08-19 20:28 UTC | 50m |
| CXK1051 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-19 20:11 UTC | 2026-08-19 20:26 UTC | 14m |
| N779PT |  | Jackson County Airport (K24A) | Macon County Airport (K1A5) | 2026-08-19 20:14 UTC | 2026-08-19 20:24 UTC | 10m |
| N1959C |  | Samsarg Field (KN58) | Reno/Tahoe International Airport (KRNO) | 2026-08-19 20:17 UTC | 2026-08-19 20:24 UTC | 6m |
| EPIC43 | EPI | New York Stewart International Airport (KSWF) | New York Stewart International Airport (KSWF) | 2026-08-19 20:11 UTC | 2026-08-19 20:24 UTC | 12m |
| N5262Y |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-08-19 19:40 UTC | 2026-08-19 20:23 UTC | 43m |
| TKR16 | TKR | Jicarilla Apache Nation Airport (K24N) | Ohkay Owingeh Airport (KE14) | 2026-08-19 20:11 UTC | 2026-08-19 20:22 UTC | 11m |
| AEA34NW | AEA | Sevilla Airport (LEZL) | Madrid Barajas International Airport (LEMD) | 2026-08-19 19:33 UTC | 2026-08-19 20:20 UTC | 46m |
| N254FJ |  | Triangle Ranch Private Airport (2TA3) | Austin Executive Airport (KEDC) | 2026-08-19 19:22 UTC | 2026-08-19 20:19 UTC | 57m |
| N414LF |  | Summit Ridge Ranch Airstrip (ID95) | Boise Air Trml/Gowen Field (KBOI) | 2026-08-19 20:09 UTC | 2026-08-19 20:18 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
