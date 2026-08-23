# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_12:43:55_UTC-green)

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

**Latest saved flight:** 2026-08-23 12:43:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 12:43:55 UTC

- **228,389** saved flights
- **70,684** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,389** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,754,907.3 tonnes** estimated CO2 emissions
- **159,704,773 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9171 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3869 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2187 |
| 10 | AZU | 2114 |
| 11 | Vueling | 1939 |
| 12 | Lufthansa | 1870 |
| 13 | WIF | 1800 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1594 |
| 16 | Swiss International | 1523 |
| 17 | AXM | 1520 |
| 18 | QLK | 1448 |
| 19 | EJU | 1447 |
| 20 | United Airlines | 1445 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1265 |
| 24 | VIV | 1253 |
| 25 | PGT | 1252 |
| 26 | WMT | 1247 |
| 27 | Air France | 1241 |
| 28 | Wizz Air | 1189 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1139 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190682 |
| 2 | 🇪🇸 ES | 14658 |
| 3 | 🇧🇷 BR | 13304 |
| 4 | 🇦🇺 AU | 12959 |
| 5 | 🇨🇦 CA | 12622 |
| 6 | 🇮🇹 IT | 12329 |
| 7 | 🇮🇳 IN | 12063 |
| 8 | 🇩🇪 DE | 11237 |
| 9 | 🇬🇧 GB | 10754 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9144 |
| 13 | 🇹🇷 TR | 6722 |
| 14 | 🇬🇷 GR | 6709 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6050 |
| 17 | 🇳🇴 NO | 5610 |
| 18 | 🇲🇾 MY | 4057 |
| 19 | 🇹🇭 TH | 3977 |
| 20 | 🇿🇦 ZA | 3975 |
| 21 | 🇵🇱 PL | 3800 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3137 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2601 |
| 27 | 🇲🇦 MA | 2311 |
| 28 | 🇲🇪 ME | 2076 |
| 29 | 🇳🇱 NL | 2040 |
| 30 | 🇮🇩 ID | 1975 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2789 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2375 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2304 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1941 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1833 |
| 17 | Madrid Barajas International Airport |  | ES | 1784 |
| 18 | Capua Airport |  | IT | 1776 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1704 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1631 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1580 |
| 26 | Ninoy Aquino International Airport |  | PH | 1504 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1428 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1355 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1350 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1303 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | O. R. Tambo International Airport |  | ZA | 1233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 833 | 21m | 244 km | 3,507.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 349 | 1h 50m | 1,423 km | 8,565.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 314 | 21m | 250 km | 1,356.3 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 307 | 44m | 555 km | 2,939.7 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 277 | 27m | 215 km | 1,025.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 260 | 19m | 144 km | 646.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SFE1 | SFE | Bud Dryden Airport (TX05) | Bud Dryden Airport (TX05) | 2026-08-23 12:19 UTC | 2026-08-23 12:43 UTC | 24m |
| A6FTT |  | Al Minhad Air Base (OMDM) | Dubai International Airport (OMDB) | 2026-08-23 11:42 UTC | 2026-08-23 12:42 UTC | 59m |
| XAX604 | XAX | Kuala Lumpur International Airport (WMKK) | Yalova Airport (LTBP) | 2026-08-23 02:40 UTC | 2026-08-23 12:40 UTC | 9h 59m |
| EJU685P | EJU | Malpensa International Airport (LIMC) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 11:49 UTC | 2026-08-23 12:39 UTC | 50m |
| DFLIP | DFL | Kunovice Airport (LKKU) | Kunovice Airport (LKKU) | 2026-08-23 12:20 UTC | 2026-08-23 12:35 UTC | 15m |
| GGWMB | GGW | Turweston Airport (EGBT) | Turweston Airport (EGBT) | 2026-08-23 11:32 UTC | 2026-08-23 12:33 UTC | 1h 0m |
| N6282D |  | 84OL (84OL) | Grove Regional Airport (KGMJ) | 2026-08-23 11:37 UTC | 2026-08-23 12:22 UTC | 44m |
| OKPVN | OKP | Ibiza Airport (LEIB) | Barcelona International Airport (LEBL) | 2026-08-23 11:25 UTC | 2026-08-23 12:20 UTC | 54m |
| N270AM |  | Van Zandt County Regional Airport (K76F) | Van Zandt County Regional Airport (K76F) | 2026-08-23 12:20 UTC | 2026-08-23 12:20 UTC | 0m |
| FIN8Q | Finnair | Helsinki Vantaa Airport (EFHK) | Rovaniemi Airport (EFRO) | 2026-08-23 10:59 UTC | 2026-08-23 12:19 UTC | 1h 20m |
| ZSNHX | ZSN | Fraaiuitzicht Airport (FAFU) | Hartebeespoortdam Airport (FAHB) | 2026-08-23 11:39 UTC | 2026-08-23 12:17 UTC | 37m |
| GCONL | GCO | Fife Airport (EGPJ) | Cumbernauld Airport (EGPG) | 2026-08-23 11:54 UTC | 2026-08-23 12:16 UTC | 21m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-23 11:53 UTC | 2026-08-23 12:14 UTC | 20m |
| BBC395 | BBC | VGZR (VGZR) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-08-23 11:29 UTC | 2026-08-23 12:11 UTC | 42m |
| IASAR | IAS | Torino / Aeritalia Airport (LIMA) | Biella / Cerrione Airport (LILE) | 2026-08-23 11:50 UTC | 2026-08-23 12:10 UTC | 20m |
| N900BA |  | Joe Foss Field (KFSD) | Wadena Municipal Airport (KADC) | 2026-08-23 11:29 UTC | 2026-08-23 12:10 UTC | 41m |
| VJT474 | VJT | Mikonos Airport (LGMK) | Samedan Airport (LSZS) | 2026-08-23 09:59 UTC | 2026-08-23 12:07 UTC | 2h 8m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-08-23 11:57 UTC | 2026-08-23 12:07 UTC | 10m |
| RYR3615 | Ryanair | Brussels South Charleroi Airport (EBCI) | Visoko Sport Airfield (LQVI) | 2026-08-23 10:34 UTC | 2026-08-23 12:03 UTC | 1h 28m |
| AEA54NL | AEA | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-08-23 11:02 UTC | 2026-08-23 11:57 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
