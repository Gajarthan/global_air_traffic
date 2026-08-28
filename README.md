# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_22:31:28_UTC-green)

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

**Latest saved flight:** 2026-08-28 22:31:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-28 22:31:28 UTC

- **240,517** saved flights
- **73,048** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,517** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,895,470.7 tonnes** estimated CO2 emissions
- **167,853,374 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9654 |
| 2 | SkyWest Airlines | 8443 |
| 3 | EJA | 4658 |
| 4 | IndiGo | 4050 |
| 5 | American Airlines | 3876 |
| 6 | Southwest Airlines | 3622 |
| 7 | Delta Air Lines | 3064 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2310 |
| 10 | AZU | 2239 |
| 11 | Vueling | 2067 |
| 12 | Lufthansa | 1937 |
| 13 | WIF | 1905 |
| 14 | LXJ | 1868 |
| 15 | easyJet | 1673 |
| 16 | Swiss International | 1613 |
| 17 | AXM | 1593 |
| 18 | EJU | 1540 |
| 19 | QLK | 1536 |
| 20 | United Airlines | 1513 |
| 21 | Alaska Airlines | 1436 |
| 22 | All Nippon Airways | 1426 |
| 23 | WMT | 1353 |
| 24 | GLO | 1340 |
| 25 | VIV | 1320 |
| 26 | Air France | 1315 |
| 27 | PGT | 1313 |
| 28 | Wizz Air | 1292 |
| 29 | AEE | 1190 |
| 30 | JetBlue | 1190 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199307 |
| 2 | 🇪🇸 ES | 15475 |
| 3 | 🇧🇷 BR | 14028 |
| 4 | 🇦🇺 AU | 13664 |
| 5 | 🇨🇦 CA | 13381 |
| 6 | 🇮🇹 IT | 13158 |
| 7 | 🇮🇳 IN | 12615 |
| 8 | 🇩🇪 DE | 11876 |
| 9 | 🇬🇧 GB | 11361 |
| 10 | 🇨🇴 CO | 10329 |
| 11 | 🇫🇷 FR | 9693 |
| 12 | 🇯🇵 JP | 9674 |
| 13 | 🇹🇷 TR | 7134 |
| 14 | 🇬🇷 GR | 7084 |
| 15 | 🇲🇽 MX | 6651 |
| 16 | 🇨🇭 CH | 6433 |
| 17 | 🇳🇴 NO | 5935 |
| 18 | 🇹🇭 TH | 4354 |
| 19 | 🇲🇾 MY | 4268 |
| 20 | 🇿🇦 ZA | 4213 |
| 21 | 🇵🇱 PL | 4024 |
| 22 | 🇳🇿 NZ | 3303 |
| 23 | 🇵🇭 PH | 3301 |
| 24 | 🇬🇹 GT | 3026 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2777 |
| 27 | 🇲🇦 MA | 2432 |
| 28 | 🇲🇪 ME | 2251 |
| 29 | 🇳🇱 NL | 2176 |
| 30 | 🇮🇩 ID | 2108 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4968 |
| 2 | Denver International Airport |  | US | 3880 |
| 3 | Indira Gandhi International Airport |  | IN | 2936 |
| 4 | Tokyo International Airport |  | JP | 2881 |
| 5 | Guaymaral Airport |  | CO | 2696 |
| 6 | Harry Reid International Airport |  | US | 2554 |
| 7 | Zurich Airport |  | CH | 2514 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2461 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2399 |
| 10 | El Dorado International Airport |  | CO | 2334 |
| 11 | La Aurora Airport |  | GT | 2306 |
| 12 | Chicago O'Hare International Airport |  | US | 2143 |
| 13 | Salt Lake City International Airport |  | US | 2120 |
| 14 | Congonhas Airport |  | BR | 2052 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1998 |
| 16 | Frankfurt am Main International Airport |  | DE | 1903 |
| 17 | Madrid Barajas International Airport |  | ES | 1896 |
| 18 | Capua Airport |  | IT | 1896 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1810 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1768 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1687 |
| 24 | Charles de Gaulle International Airport |  | FR | 1683 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1603 |
| 27 | Kuala Lumpur International Airport |  | MY | 1543 |
| 28 | Charlotte/Douglas International Airport |  | US | 1539 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1533 |
| 30 | Barcelona International Airport |  | ES | 1532 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1455 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1404 |
| 34 | Bengaluru International Airport |  | IN | 1404 |
| 35 | Seattle-Tacoma International Airport |  | US | 1403 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1398 |
| 37 | Calgary International Airport |  | CA | 1381 |
| 38 | Oslo Gardermoen Airport |  | NO | 1347 |
| 39 | Vancouver International Airport |  | CA | 1323 |
| 40 | O. R. Tambo International Airport |  | ZA | 1313 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1092 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 884 | 21m | 244 km | 3,722.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 620 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 610 | 24m | 225 km | 2,366.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 544 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 378 | 1h 50m | 1,423 km | 9,276.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 364 | 44m | 555 km | 3,485.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 348 | 44m | 241 km | 1,445.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 327 | 24m | 218 km | 1,231.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 319 | 1h 40m | 1,156 km | 6,363.9 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 293 | 27m | 215 km | 1,085.1 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 279 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 278 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 274 | 1h 14m | 961 km | 4,541.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N685DW |  | Lebanon Municipal Airport (KLEB) | Concord Municipal Airport (KCON) | 2026-08-28 22:02 UTC | 2026-08-28 22:31 UTC | 29m |
| EVA6036 | EVA Air | Suvarnabhumi Airport (VTBS) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-28 19:21 UTC | 2026-08-28 22:31 UTC | 3h 9m |
| N102AC |  | Ohio State University Airport (KOSU) | Madison County Airport (KUYF) | 2026-08-28 21:42 UTC | 2026-08-28 22:28 UTC | 46m |
| N913SB |  | 66CL (66CL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-28 22:01 UTC | 2026-08-28 22:24 UTC | 23m |
| WIRE31 | WIR | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-28 21:34 UTC | 2026-08-28 22:21 UTC | 47m |
| TKR136 | TKR | Coeur D'Alene Airport (KCOE) | Art Sutcliffe Field (CAJ3) | 2026-08-28 22:04 UTC | 2026-08-28 22:21 UTC | 16m |
| N5355P |  | 16PA (16PA) | 9PN1 (9PN1) | 2026-08-28 21:57 UTC | 2026-08-28 22:18 UTC | 21m |
| CGRQH | CGR | Banff Airport (CYBA) | Sparwood Elk Valley Airport (CYSW) | 2026-08-28 22:05 UTC | 2026-08-28 22:16 UTC | 10m |
| THY3006 | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-28 19:09 UTC | 2026-08-28 22:16 UTC | 3h 6m |
| FPP | FPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-28 21:54 UTC | 2026-08-28 22:14 UTC | 19m |
| N979CC |  | Wadsworth Municipal Airport (K3G3) | Plane Country Airport (45OI) | 2026-08-28 21:58 UTC | 2026-08-28 22:13 UTC | 15m |
| N53630 |  | Arlington Municipal Airport (KAWO) | Cross Winds Airport (WA07) | 2026-08-28 21:42 UTC | 2026-08-28 22:12 UTC | 29m |
| N165JY |  | Albert Whitted Airport (KSPG) | Sarasota/Bradenton International Airport (KSRQ) | 2026-08-28 20:50 UTC | 2026-08-28 22:11 UTC | 1h 21m |
| N3546T |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-28 20:50 UTC | 2026-08-28 22:11 UTC | 1h 20m |
| N329ME |  | Ankeny Regional Airport (KIKV) | Fort Dodge Regional Airport (KFOD) | 2026-08-28 21:37 UTC | 2026-08-28 22:10 UTC | 32m |
| N5217H |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-28 21:07 UTC | 2026-08-28 22:03 UTC | 56m |
| TKR10 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-08-28 21:51 UTC | 2026-08-28 22:02 UTC | 11m |
| N1910R |  | Santa Cruz del Quiche Airport (MGQC) | Coban Airport (MGCB) | 2026-08-28 21:42 UTC | 2026-08-28 21:58 UTC | 15m |
| N677AA |  | Trenton Mercer Airport (KTTN) | Trenton Mercer Airport (KTTN) | 2026-08-28 21:34 UTC | 2026-08-28 21:55 UTC | 21m |
| N82EM |  | Ellington Airport (KEFD) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-28 19:15 UTC | 2026-08-28 21:55 UTC | 2h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
