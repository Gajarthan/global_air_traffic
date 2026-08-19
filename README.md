# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_20:26:44_UTC-green)

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

**Latest saved flight:** 2026-08-19 20:26:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 20:26:44 UTC

- **217,218** saved flights
- **68,515** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,218** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,613,390.2 tonnes** estimated CO2 emissions
- **151,500,879 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8693 |
| 2 | SkyWest Airlines | 7760 |
| 3 | EJA | 4230 |
| 4 | IndiGo | 3692 |
| 5 | American Airlines | 3622 |
| 6 | Southwest Airlines | 3449 |
| 7 | Delta Air Lines | 2809 |
| 8 | ENY | 2683 |
| 9 | LATAM Airlines | 2054 |
| 10 | AZU | 1990 |
| 11 | Vueling | 1825 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1713 |
| 15 | easyJet | 1510 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1373 |
| 19 | EJU | 1353 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1328 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1191 |
| 24 | GLO | 1181 |
| 25 | Air France | 1177 |
| 26 | PGT | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1106 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183155 |
| 2 | 🇪🇸 ES | 13932 |
| 3 | 🇧🇷 BR | 12523 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11965 |
| 6 | 🇮🇹 IT | 11537 |
| 7 | 🇮🇳 IN | 11493 |
| 8 | 🇩🇪 DE | 10758 |
| 9 | 🇬🇧 GB | 10206 |
| 10 | 🇨🇴 CO | 8904 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8660 |
| 13 | 🇬🇷 GR | 6344 |
| 14 | 🇹🇷 TR | 6244 |
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
| 26 | 🇭🇷 HR | 2385 |
| 27 | 🇲🇦 MA | 2186 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1900 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4560 |
| 2 | Denver International Airport |  | US | 3539 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2627 |
| 5 | Guaymaral Airport |  | CO | 2592 |
| 6 | Harry Reid International Airport |  | US | 2406 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2232 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2211 |
| 10 | La Aurora Airport |  | GT | 2097 |
| 11 | El Dorado International Airport |  | CO | 2027 |
| 12 | Chicago O'Hare International Airport |  | US | 1997 |
| 13 | Salt Lake City International Airport |  | US | 1919 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1896 |
| 15 | Congonhas Airport |  | BR | 1828 |
| 16 | Frankfurt am Main International Airport |  | DE | 1777 |
| 17 | Madrid Barajas International Airport |  | ES | 1702 |
| 18 | Capua Airport |  | IT | 1654 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1637 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1593 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1527 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1491 |
| 26 | Charlotte/Douglas International Airport |  | US | 1458 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1331 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1326 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1297 |
| 33 | Seattle-Tacoma International Airport |  | US | 1286 |
| 34 | Viracopos International Airport |  | BR | 1270 |
| 35 | Calgary International Airport |  | CA | 1222 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1190 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 774 | 21m | 244 km | 3,259.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 490 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 480 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 293 | 22m | 55 km | 278.5 t |
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
| CXK1051 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-19 20:11 UTC | 2026-08-19 20:26 UTC | 14m |
| N779PT |  | Jackson County Airport (K24A) | Macon County Airport (K1A5) | 2026-08-19 20:14 UTC | 2026-08-19 20:24 UTC | 10m |
| EPIC43 | EPI | New York Stewart International Airport (KSWF) | New York Stewart International Airport (KSWF) | 2026-08-19 20:11 UTC | 2026-08-19 20:24 UTC | 12m |
| N5262Y |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-08-19 19:40 UTC | 2026-08-19 20:23 UTC | 43m |
| AEA34NW | AEA | Sevilla Airport (LEZL) | Madrid Barajas International Airport (LEMD) | 2026-08-19 19:33 UTC | 2026-08-19 20:20 UTC | 46m |
| N414LF |  | Summit Ridge Ranch Airstrip (ID95) | Boise Air Trml/Gowen Field (KBOI) | 2026-08-19 20:09 UTC | 2026-08-19 20:18 UTC | 9m |
| LS16 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-19 19:03 UTC | 2026-08-19 20:17 UTC | 1h 14m |
| FAST33 | FAS | 12MO (12MO) | Sedalia Regional Airport (KDMO) | 2026-08-19 20:06 UTC | 2026-08-19 20:17 UTC | 11m |
| CXK569 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-19 19:00 UTC | 2026-08-19 20:16 UTC | 1h 16m |
| HOOK47 | HOO | Cottonwood Airport (OK66) | Sandridge Airpark Inc Airport (OK94) | 2026-08-19 19:46 UTC | 2026-08-19 20:11 UTC | 24m |
| RUF120 | RUF | Bartlesville Municipal Airport (KBVO) | Candy Lake Estate Airport (98OK) | 2026-08-19 20:01 UTC | 2026-08-19 20:08 UTC | 7m |
| GRYDR1 | GRY | Old Rhinebeck Airport (NY94) | Laguardia Airport (KLGA) | 2026-08-19 19:36 UTC | 2026-08-19 20:07 UTC | 31m |
| CXK311 | CXK | Dupage Airport (KDPA) | IS80 (IS80) | 2026-08-19 19:47 UTC | 2026-08-19 20:07 UTC | 19m |
| PPCTL | PPC | Campo de Marte Airport (SBMT) | Campo de Marte Airport (SBMT) | 2026-08-19 19:57 UTC | 2026-08-19 20:07 UTC | 9m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-19 19:48 UTC | 2026-08-19 20:05 UTC | 16m |
| N2122M |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-19 19:51 UTC | 2026-08-19 20:05 UTC | 13m |
| XBBGA | XBB | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-08-19 19:23 UTC | 2026-08-19 20:04 UTC | 40m |
| N950DR |  | PS52 (PS52) | Lancaster Airport (KLNS) | 2026-08-19 18:40 UTC | 2026-08-19 20:02 UTC | 1h 21m |
| N5000Y |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-19 19:40 UTC | 2026-08-19 20:02 UTC | 21m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-19 05:56 UTC | 2026-08-19 20:01 UTC | 14h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
