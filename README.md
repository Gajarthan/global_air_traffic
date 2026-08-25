# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_16:16:31_UTC-green)

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

**Latest saved flight:** 2026-08-25 16:16:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 16:16:31 UTC

- **235,614** saved flights
- **72,056** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,614** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,837,659.7 tonnes** estimated CO2 emissions
- **164,502,011 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9448 |
| 2 | SkyWest Airlines | 8308 |
| 3 | EJA | 4561 |
| 4 | IndiGo | 3983 |
| 5 | American Airlines | 3819 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2997 |
| 8 | ENY | 2858 |
| 9 | LATAM Airlines | 2263 |
| 10 | AZU | 2195 |
| 11 | Vueling | 2018 |
| 12 | Lufthansa | 1917 |
| 13 | WIF | 1876 |
| 14 | LXJ | 1845 |
| 15 | easyJet | 1644 |
| 16 | Swiss International | 1585 |
| 17 | AXM | 1575 |
| 18 | EJU | 1508 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1489 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1315 |
| 24 | GLO | 1313 |
| 25 | VIV | 1298 |
| 26 | PGT | 1284 |
| 27 | Air France | 1280 |
| 28 | Wizz Air | 1257 |
| 29 | AEE | 1169 |
| 30 | JetBlue | 1166 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195596 |
| 2 | 🇪🇸 ES | 15145 |
| 3 | 🇧🇷 BR | 13759 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13020 |
| 6 | 🇮🇹 IT | 12845 |
| 7 | 🇮🇳 IN | 12406 |
| 8 | 🇩🇪 DE | 11626 |
| 9 | 🇬🇧 GB | 11116 |
| 10 | 🇨🇴 CO | 9965 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9465 |
| 13 | 🇹🇷 TR | 6988 |
| 14 | 🇬🇷 GR | 6943 |
| 15 | 🇲🇽 MX | 6537 |
| 16 | 🇨🇭 CH | 6307 |
| 17 | 🇳🇴 NO | 5842 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4133 |
| 21 | 🇵🇱 PL | 3932 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2949 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2710 |
| 27 | 🇲🇦 MA | 2389 |
| 28 | 🇲🇪 ME | 2191 |
| 29 | 🇳🇱 NL | 2118 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4879 |
| 2 | Denver International Airport |  | US | 3802 |
| 3 | Indira Gandhi International Airport |  | IN | 2878 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2684 |
| 6 | Harry Reid International Airport |  | US | 2522 |
| 7 | Zurich Airport |  | CH | 2470 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2404 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2359 |
| 10 | La Aurora Airport |  | GT | 2248 |
| 11 | El Dorado International Airport |  | CO | 2232 |
| 12 | Chicago O'Hare International Airport |  | US | 2123 |
| 13 | Salt Lake City International Airport |  | US | 2071 |
| 14 | Congonhas Airport |  | BR | 2007 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1975 |
| 16 | Frankfurt am Main International Airport |  | DE | 1876 |
| 17 | Madrid Barajas International Airport |  | ES | 1853 |
| 18 | Capua Airport |  | IT | 1850 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1773 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1735 |
| 21 | Malpensa International Airport |  | IT | 1688 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1669 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1641 |
| 25 | Macau International Airport |  | MO | 1612 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1517 |
| 29 | Barcelona International Airport |  | ES | 1490 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1462 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1423 |
| 32 | Viracopos International Airport |  | BR | 1405 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1379 |
| 35 | Seattle-Tacoma International Airport |  | US | 1379 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1346 |
| 38 | Oslo Gardermoen Airport |  | NO | 1322 |
| 39 | O. R. Tambo International Airport |  | ZA | 1285 |
| 40 | Vancouver International Airport |  | CA | 1285 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 863 | 21m | 244 km | 3,633.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 592 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 528 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 365 | 1h 50m | 1,423 km | 8,957.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 333 | 21m | 250 km | 1,438.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 311 | 1h 40m | 1,156 km | 6,204.3 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 289 | 27m | 215 km | 1,070.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 252 | 1h 50m | 1,304 km | 5,669.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2860 | United Airlines | Toronto Pearson International Airport (CYYZ) | Chicago O'Hare International Airport (KORD) | 2026-08-25 14:56 UTC | 2026-08-25 16:16 UTC | 1h 20m |
| HBLVC | HBL | Stuttgart Airport (EDDS) | Mengen-Hohentengen Airport (EDTM) | 2026-08-25 15:23 UTC | 2026-08-25 16:13 UTC | 50m |
| N8158N |  | Atlanta Regional Falcon Field (KFFC) | K4A7 (K4A7) | 2026-08-25 15:45 UTC | 2026-08-25 16:09 UTC | 24m |
| JEDI31 | JED | Mc Guire Field (Joint Base Mc Guire Dix Lakehurst) Airport (KWRI) | Lakehurst Maxfield Field (KNEL) | 2026-08-25 15:04 UTC | 2026-08-25 16:08 UTC | 1h 4m |
| N366CT |  | Henderson Executive Airport (KHND) | North Las Vegas Airport (KVGT) | 2026-08-25 15:32 UTC | 2026-08-25 16:08 UTC | 36m |
| BLZR243 | BLZ | Kingsville Nas Airport (KNQI) | TE63 (TE63) | 2026-08-25 15:49 UTC | 2026-08-25 16:08 UTC | 19m |
| WLDLD27 | WLD | Centennial Airport (KAPA) | Stevens Field (KPSO) | 2026-08-25 13:54 UTC | 2026-08-25 16:06 UTC | 2h 12m |
| N831MA |  | Dane County Regional/Truax Field (KMSN) | Baraboo/Wisconsin Dells Regional Airport (KDLL) | 2026-08-25 14:43 UTC | 2026-08-25 16:06 UTC | 1h 22m |
| N36LR |  | Chino Airport (KCNO) | Lone Pine/Death Valley Airport (KO26) | 2026-08-25 15:05 UTC | 2026-08-25 16:06 UTC | 1h 0m |
| N23NW |  | Lubbock Preston Smith International Airport (KLBB) | Terrell County Airport (K6R6) | 2026-08-25 14:14 UTC | 2026-08-25 16:04 UTC | 1h 49m |
| ROKT11 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-08-25 15:40 UTC | 2026-08-25 16:01 UTC | 21m |
| C2711 |  | St Pete-Clearwater International Airport (KPIE) | St Pete-Clearwater International Airport (KPIE) | 2026-08-25 13:32 UTC | 2026-08-25 15:59 UTC | 2h 26m |
| MUSL | MUS | Garner Field (02MD) | Garner Field (02MD) | 2026-08-25 15:20 UTC | 2026-08-25 15:59 UTC | 38m |
| N2949V |  | City Of Colorado Springs Municipal Airport (KCOS) | Geary Ranch Airport (CO65) | 2026-08-25 15:15 UTC | 2026-08-25 15:57 UTC | 42m |
| FLAME81 | FLA | Hughes Ranch Airport (50XS) | Maverick County Memorial International Airport (K5T9) | 2026-08-25 15:31 UTC | 2026-08-25 15:55 UTC | 23m |
| AER101 | AER | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-08-25 14:58 UTC | 2026-08-25 15:54 UTC | 56m |
| CAL5265 | CAL | Ted Stevens Anchorage International Airport (PANC) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-25 06:14 UTC | 2026-08-25 15:54 UTC | 9h 39m |
| N888RK |  | Horseshoe Bay Resort Airport (KDZB) | Skeen Ranch Airport (82NM) | 2026-08-25 14:55 UTC | 2026-08-25 15:53 UTC | 58m |
| DFITI | DFI | Voslau Airport (LOAV) | Cologne Bonn Airport (EDDK) | 2026-08-25 14:15 UTC | 2026-08-25 15:53 UTC | 1h 37m |
| DRACO72 | DRA | 4XA5 (4XA5) | OK79 (OK79) | 2026-08-25 15:09 UTC | 2026-08-25 15:52 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
