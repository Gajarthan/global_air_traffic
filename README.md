# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_15:19:57_UTC-green)

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

**Latest saved flight:** 2026-08-23 15:19:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 15:19:57 UTC

- **228,806** saved flights
- **70,751** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,806** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,759,460.7 tonnes** estimated CO2 emissions
- **159,968,734 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9190 |
| 2 | SkyWest Airlines | 8106 |
| 3 | EJA | 4399 |
| 4 | IndiGo | 3874 |
| 5 | American Airlines | 3744 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2927 |
| 8 | ENY | 2793 |
| 9 | LATAM Airlines | 2196 |
| 10 | AZU | 2124 |
| 11 | Vueling | 1943 |
| 12 | Lufthansa | 1871 |
| 13 | WIF | 1804 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1598 |
| 16 | Swiss International | 1528 |
| 17 | AXM | 1520 |
| 18 | EJU | 1458 |
| 19 | United Airlines | 1449 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1270 |
| 24 | VIV | 1254 |
| 25 | PGT | 1252 |
| 26 | WMT | 1252 |
| 27 | Air France | 1244 |
| 28 | Wizz Air | 1194 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1140 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190884 |
| 2 | 🇪🇸 ES | 14692 |
| 3 | 🇧🇷 BR | 13355 |
| 4 | 🇦🇺 AU | 12961 |
| 5 | 🇨🇦 CA | 12629 |
| 6 | 🇮🇹 IT | 12366 |
| 7 | 🇮🇳 IN | 12072 |
| 8 | 🇩🇪 DE | 11272 |
| 9 | 🇬🇧 GB | 10774 |
| 10 | 🇨🇴 CO | 9420 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9171 |
| 13 | 🇹🇷 TR | 6743 |
| 14 | 🇬🇷 GR | 6727 |
| 15 | 🇲🇽 MX | 6360 |
| 16 | 🇨🇭 CH | 6083 |
| 17 | 🇳🇴 NO | 5629 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇹🇭 TH | 3997 |
| 20 | 🇿🇦 ZA | 3991 |
| 21 | 🇵🇱 PL | 3809 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2878 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2613 |
| 27 | 🇲🇦 MA | 2319 |
| 28 | 🇲🇪 ME | 2088 |
| 29 | 🇳🇱 NL | 2049 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4773 |
| 2 | Denver International Airport |  | US | 3715 |
| 3 | Indira Gandhi International Airport |  | IN | 2791 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2648 |
| 6 | Harry Reid International Airport |  | US | 2475 |
| 7 | Zurich Airport |  | CH | 2383 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2337 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2308 |
| 10 | La Aurora Airport |  | GT | 2192 |
| 11 | El Dorado International Airport |  | CO | 2089 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2010 |
| 14 | Congonhas Airport |  | BR | 1947 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1835 |
| 17 | Madrid Barajas International Airport |  | ES | 1789 |
| 18 | Capua Airport |  | IT | 1780 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1713 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1702 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1634 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1585 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1494 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1433 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1385 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1362 |
| 32 | Viracopos International Airport |  | BR | 1359 |
| 33 | Bengaluru International Airport |  | IN | 1356 |
| 34 | Seattle-Tacoma International Airport |  | US | 1348 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1272 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | O. R. Tambo International Airport |  | ZA | 1239 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 833 | 21m | 244 km | 3,507.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 552 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 350 | 1h 50m | 1,423 km | 8,589.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 316 | 21m | 250 km | 1,364.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 295 | 24m | 218 km | 1,111.4 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 278 | 27m | 215 km | 1,029.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 240 | 28m | 152 km | 627.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AVL110 | AVL | Washington Manassas/Harry P Davis Field (KHEF) | Hanover County Municipal Airport (KOFP) | 2026-08-23 14:40 UTC | 2026-08-23 15:19 UTC | 39m |
| N65JA |  | Aurora Municipal Airport (KARR) | Walnut Creek Airport (49IL) | 2026-08-23 14:45 UTC | 2026-08-23 15:12 UTC | 27m |
| CGOLC | CGO | Vancouver International Airport (CYVR) | Stuart Island West Airport (2WA3) | 2026-08-23 14:57 UTC | 2026-08-23 15:11 UTC | 14m |
| N81441 |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-23 14:49 UTC | 2026-08-23 15:10 UTC | 21m |
| N6419V |  | Frederick Municipal Airport (KFDK) | Eastern Wv Regional/Shepherd Field (KMRB) | 2026-08-23 14:41 UTC | 2026-08-23 15:10 UTC | 29m |
| N7998U |  | Morrow County Airport (K4I9) | Morrow County Airport (K4I9) | 2026-08-23 14:55 UTC | 2026-08-23 15:08 UTC | 12m |
| CGIOZ | CGI | CPJ6 (CPJ6) | CPJ6 (CPJ6) | 2026-08-23 14:15 UTC | 2026-08-23 15:07 UTC | 51m |
| N205NB |  | Nephi Municipal Airport (KU14) | KU42 (KU42) | 2026-08-23 14:40 UTC | 2026-08-23 15:06 UTC | 25m |
| N839SP |  | Roberts Field/Redmond Municipal Airport (KRDM) | Dry Creek Airpark (OG21) | 2026-08-23 14:32 UTC | 2026-08-23 15:04 UTC | 32m |
| DMDTR | DMD | Trier-Fohren Airport (EDRT) | Luxembourg-Findel International Airport (ELLX) | 2026-08-23 14:58 UTC | 2026-08-23 15:02 UTC | 3m |
| N294NG |  | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-08-23 14:31 UTC | 2026-08-23 15:01 UTC | 29m |
| N5459K |  | Duda Airstrip (FA69) | Fort Lauderdale Executive Airport (KFXE) | 2026-08-23 14:40 UTC | 2026-08-23 14:58 UTC | 18m |
| MS5 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-08-23 14:36 UTC | 2026-08-23 14:54 UTC | 18m |
| DFLYC | DFL | Olsztyn-Mazury Airport (EPSY) | EPMX (EPMX) | 2026-08-23 14:37 UTC | 2026-08-23 14:52 UTC | 15m |
| OKRAH | OKR | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-08-23 14:12 UTC | 2026-08-23 14:50 UTC | 38m |
| N383BH |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-23 14:09 UTC | 2026-08-23 14:48 UTC | 39m |
| GCCYR | GCC | Old Warden Airfield (EGTH) | Old Warden Airfield (EGTH) | 2026-08-23 14:30 UTC | 2026-08-23 14:48 UTC | 18m |
| CAP4825 | CAP | Sheboygan County Memorial International Airport (KSBM) | Watertown Municipal Airport (KRYV) | 2026-08-23 14:20 UTC | 2026-08-23 14:47 UTC | 27m |
| MBU8AZ | MBU | Hamburg Airport (EDDH) | Chania International Airport (LGSA) | 2026-08-23 11:42 UTC | 2026-08-23 14:43 UTC | 3h 1m |
| TGACM | TGA | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-23 13:52 UTC | 2026-08-23 14:41 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
