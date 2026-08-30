# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_12:46:11_UTC-green)

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

**Latest saved flight:** 2026-08-30 12:46:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-30 12:46:11 UTC

- **241,705** saved flights
- **73,295** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,705** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,909,396.8 tonnes** estimated CO2 emissions
- **168,660,683 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9699 |
| 2 | SkyWest Airlines | 8478 |
| 3 | EJA | 4672 |
| 4 | IndiGo | 4075 |
| 5 | American Airlines | 3891 |
| 6 | Southwest Airlines | 3633 |
| 7 | Delta Air Lines | 3080 |
| 8 | ENY | 2915 |
| 9 | LATAM Airlines | 2316 |
| 10 | AZU | 2243 |
| 11 | Vueling | 2077 |
| 12 | Lufthansa | 1945 |
| 13 | WIF | 1911 |
| 14 | LXJ | 1870 |
| 15 | easyJet | 1685 |
| 16 | Swiss International | 1632 |
| 17 | AXM | 1599 |
| 18 | EJU | 1549 |
| 19 | QLK | 1544 |
| 20 | United Airlines | 1519 |
| 21 | Alaska Airlines | 1444 |
| 22 | All Nippon Airways | 1431 |
| 23 | WMT | 1360 |
| 24 | GLO | 1347 |
| 25 | VIV | 1324 |
| 26 | PGT | 1323 |
| 27 | Air France | 1320 |
| 28 | Wizz Air | 1306 |
| 29 | JetBlue | 1197 |
| 30 | AEE | 1196 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200243 |
| 2 | 🇪🇸 ES | 15542 |
| 3 | 🇧🇷 BR | 14076 |
| 4 | 🇦🇺 AU | 13710 |
| 5 | 🇨🇦 CA | 13444 |
| 6 | 🇮🇹 IT | 13234 |
| 7 | 🇮🇳 IN | 12681 |
| 8 | 🇩🇪 DE | 11932 |
| 9 | 🇬🇧 GB | 11416 |
| 10 | 🇨🇴 CO | 10400 |
| 11 | 🇫🇷 FR | 9749 |
| 12 | 🇯🇵 JP | 9702 |
| 13 | 🇹🇷 TR | 7171 |
| 14 | 🇬🇷 GR | 7128 |
| 15 | 🇲🇽 MX | 6670 |
| 16 | 🇨🇭 CH | 6502 |
| 17 | 🇳🇴 NO | 5956 |
| 18 | 🇹🇭 TH | 4390 |
| 19 | 🇲🇾 MY | 4285 |
| 20 | 🇿🇦 ZA | 4223 |
| 21 | 🇵🇱 PL | 4055 |
| 22 | 🇳🇿 NZ | 3326 |
| 23 | 🇵🇭 PH | 3317 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2856 |
| 26 | 🇭🇷 HR | 2790 |
| 27 | 🇲🇦 MA | 2443 |
| 28 | 🇲🇪 ME | 2257 |
| 29 | 🇳🇱 NL | 2190 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4990 |
| 2 | Denver International Airport |  | US | 3898 |
| 3 | Indira Gandhi International Airport |  | IN | 2953 |
| 4 | Tokyo International Airport |  | JP | 2889 |
| 5 | Guaymaral Airport |  | CO | 2701 |
| 6 | Harry Reid International Airport |  | US | 2568 |
| 7 | Zurich Airport |  | CH | 2540 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2471 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2410 |
| 10 | El Dorado International Airport |  | CO | 2357 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2148 |
| 13 | Salt Lake City International Airport |  | US | 2130 |
| 14 | Congonhas Airport |  | BR | 2057 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2000 |
| 16 | Frankfurt am Main International Airport |  | DE | 1915 |
| 17 | Capua Airport |  | IT | 1908 |
| 18 | Madrid Barajas International Airport |  | ES | 1901 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1815 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1777 |
| 21 | Malpensa International Airport |  | IT | 1730 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1704 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1697 |
| 24 | Charles de Gaulle International Airport |  | FR | 1690 |
| 25 | Macau International Airport |  | MO | 1615 |
| 26 | Ninoy Aquino International Airport |  | PH | 1611 |
| 27 | Charlotte/Douglas International Airport |  | US | 1547 |
| 28 | Kuala Lumpur International Airport |  | MY | 1546 |
| 29 | Barcelona International Airport |  | ES | 1541 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1538 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1459 |
| 32 | Viracopos International Airport |  | BR | 1435 |
| 33 | Don Mueang International Airport |  | TH | 1413 |
| 34 | Seattle-Tacoma International Airport |  | US | 1410 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1404 |
| 37 | Calgary International Airport |  | CA | 1388 |
| 38 | Oslo Gardermoen Airport |  | NO | 1355 |
| 39 | Vancouver International Airport |  | CA | 1337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1321 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1094 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 890 | 21m | 244 km | 3,747.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 615 | 24m | 225 km | 2,385.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 381 | 1h 50m | 1,423 km | 9,350.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 370 | 44m | 555 km | 3,542.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 351 | 44m | 241 km | 1,458.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 330 | 24m | 218 km | 1,243.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 284 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 280 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 272 | 19m | 144 km | 676.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 259 | 1h 50m | 1,304 km | 5,826.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLIP | DFL | Skutec Airport (LKSK) | Skutec Airport (LKSK) | 2026-08-30 12:25 UTC | 2026-08-30 12:46 UTC | 20m |
| N101WL |  | KU77 (KU77) | KU42 (KU42) | 2026-08-30 12:12 UTC | 2026-08-30 12:36 UTC | 24m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-30 12:08 UTC | 2026-08-30 12:35 UTC | 27m |
| BBC395 | BBC | VGZR (VGZR) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-08-30 11:40 UTC | 2026-08-30 12:24 UTC | 44m |
| PSRMD | PSR | Fazenda Guaivira Airport (SNVM) | Fazenda Retiro do Cervo I Airport (SIMW) | 2026-08-30 12:05 UTC | 2026-08-30 12:21 UTC | 16m |
| N5914V |  | Linden Airport (KLDJ) | Central Jersey Regional Airport (K47N) | 2026-08-30 11:13 UTC | 2026-08-30 12:21 UTC | 1h 7m |
| N6117M |  | Fayette County Airport (KFYE) | Fayette County Airport (KFYE) | 2026-08-30 11:49 UTC | 2026-08-30 12:20 UTC | 30m |
| N507GA |  | Flagstaff Pulliam Airport (KFLG) | Flagstaff Pulliam Airport (KFLG) | 2026-08-30 12:12 UTC | 2026-08-30 12:17 UTC | 5m |
| HB3211 |  | Amlikon Glider Airport (LSPA) | Amlikon Glider Airport (LSPA) | 2026-08-30 11:47 UTC | 2026-08-30 12:12 UTC | 25m |
| N808W |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-08-30 11:55 UTC | 2026-08-30 12:08 UTC | 13m |
| RYR5605 | Ryanair | Lamezia Terme Airport (LICA) | Saarbrucken Airport (EDDR) | 2026-08-30 10:03 UTC | 2026-08-30 12:06 UTC | 2h 2m |
| GAWGB | GAW | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-08-30 11:33 UTC | 2026-08-30 12:04 UTC | 31m |
| CAN12 | CAN | Ciampino Airport (LIRA) | Foggia / Gino Lisa Airport (LIBF) | 2026-08-30 09:03 UTC | 2026-08-30 11:57 UTC | 2h 54m |
| HBKRT | HBK | Buochs Airport (LSZC) | Alpnach Air Base (LSMA) | 2026-08-30 11:38 UTC | 2026-08-30 11:57 UTC | 18m |
| N534NT |  | East Texas Regional Airport (KGGG) | Z M Jack Stell Field (KCRT) | 2026-08-30 11:35 UTC | 2026-08-30 11:56 UTC | 20m |
| FJJAH | FJJ | Calvi-Sainte-Catherine Airport (LFKC) | Corte Airport (LFKT) | 2026-08-30 11:35 UTC | 2026-08-30 11:55 UTC | 20m |
| DLH8NL | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-08-30 11:12 UTC | 2026-08-30 11:54 UTC | 42m |
| IGREI | IGR | Barcelonnette - Saint-Pons Airport (LFMR) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-08-30 11:50 UTC | 2026-08-30 11:50 UTC | 0m |
| DFHOT | DFH | Nice-Cote d'Azur Airport (LFMN) | Samedan Airport (LSZS) | 2026-08-30 10:42 UTC | 2026-08-30 11:49 UTC | 1h 6m |
| JIA5310 | JIA | Gerald R Ford International Airport (KGRR) | Philadelphia International Airport (KPHL) | 2026-08-30 10:28 UTC | 2026-08-30 11:48 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
