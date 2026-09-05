# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_01:02:05_UTC-green)

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

**Latest saved flight:** 2026-09-05 01:02:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 01:02:05 UTC

- **247,939** saved flights
- **74,721** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,939** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,982,056.6 tonnes** estimated CO2 emissions
- **172,872,847 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9930 |
| 2 | SkyWest Airlines | 8670 |
| 3 | EJA | 4791 |
| 4 | IndiGo | 4135 |
| 5 | American Airlines | 3975 |
| 6 | Southwest Airlines | 3692 |
| 7 | Delta Air Lines | 3151 |
| 8 | ENY | 2966 |
| 9 | LATAM Airlines | 2392 |
| 10 | AZU | 2311 |
| 11 | Vueling | 2117 |
| 12 | WIF | 1983 |
| 13 | Lufthansa | 1970 |
| 14 | LXJ | 1927 |
| 15 | easyJet | 1714 |
| 16 | Swiss International | 1662 |
| 17 | AXM | 1619 |
| 18 | EJU | 1591 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1557 |
| 21 | Alaska Airlines | 1481 |
| 22 | All Nippon Airways | 1453 |
| 23 | WMT | 1398 |
| 24 | GLO | 1382 |
| 25 | VIV | 1365 |
| 26 | PGT | 1356 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1337 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205801 |
| 2 | 🇪🇸 ES | 15869 |
| 3 | 🇧🇷 BR | 14502 |
| 4 | 🇦🇺 AU | 14092 |
| 5 | 🇨🇦 CA | 13791 |
| 6 | 🇮🇹 IT | 13566 |
| 7 | 🇮🇳 IN | 12899 |
| 8 | 🇩🇪 DE | 12178 |
| 9 | 🇬🇧 GB | 11642 |
| 10 | 🇨🇴 CO | 10820 |
| 11 | 🇫🇷 FR | 9978 |
| 12 | 🇯🇵 JP | 9794 |
| 13 | 🇹🇷 TR | 7373 |
| 14 | 🇬🇷 GR | 7285 |
| 15 | 🇲🇽 MX | 6866 |
| 16 | 🇨🇭 CH | 6671 |
| 17 | 🇳🇴 NO | 6147 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4346 |
| 20 | 🇿🇦 ZA | 4281 |
| 21 | 🇵🇱 PL | 4146 |
| 22 | 🇳🇿 NZ | 3394 |
| 23 | 🇵🇭 PH | 3374 |
| 24 | 🇬🇹 GT | 3098 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2845 |
| 27 | 🇲🇦 MA | 2505 |
| 28 | 🇲🇪 ME | 2313 |
| 29 | 🇳🇱 NL | 2234 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5108 |
| 2 | Denver International Airport |  | US | 4008 |
| 3 | Indira Gandhi International Airport |  | IN | 3015 |
| 4 | Tokyo International Airport |  | JP | 2922 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2649 |
| 7 | Zurich Airport |  | CH | 2592 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2523 |
| 9 | El Dorado International Airport |  | CO | 2477 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2459 |
| 11 | La Aurora Airport |  | GT | 2358 |
| 12 | Salt Lake City International Airport |  | US | 2199 |
| 13 | Chicago O'Hare International Airport |  | US | 2175 |
| 14 | Congonhas Airport |  | BR | 2129 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2045 |
| 16 | Capua Airport |  | IT | 1948 |
| 17 | Madrid Barajas International Airport |  | ES | 1944 |
| 18 | Frankfurt am Main International Airport |  | DE | 1941 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1863 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1812 |
| 21 | Malpensa International Airport |  | IT | 1777 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 23 | Charles de Gaulle International Airport |  | FR | 1739 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1643 |
| 26 | Macau International Airport |  | MO | 1633 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1625 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Barcelona International Airport |  | ES | 1567 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1521 |
| 32 | Viracopos International Airport |  | BR | 1481 |
| 33 | Seattle-Tacoma International Airport |  | US | 1461 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1445 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Calgary International Airport |  | CA | 1430 |
| 37 | Bengaluru International Airport |  | IN | 1426 |
| 38 | Oslo Gardermoen Airport |  | NO | 1395 |
| 39 | Vancouver International Airport |  | CA | 1388 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1346 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 920 | 21m | 244 km | 3,873.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 653 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 621 | 1h 6m | 770 km | 8,249.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 394 | 1h 50m | 1,423 km | 9,669.4 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 346 | 24m | 218 km | 1,303.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N611BZ |  | Camp Bullis Als (Cals) Airport (9TX5) | Kerrville Municipal/Louis Schreiner Field (KERV) | 2026-09-05 00:42 UTC | 2026-09-05 01:02 UTC | 19m |
| XSN82 | XSN | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-09-05 00:20 UTC | 2026-09-05 00:59 UTC | 38m |
| N787UM |  | Miami-Opa Locka Executive Airport (KOPF) | Fort Lauderdale Executive Airport (KFXE) | 2026-09-05 00:43 UTC | 2026-09-05 00:56 UTC | 12m |
| N1314T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-09-04 23:37 UTC | 2026-09-05 00:55 UTC | 1h 17m |
| N501KT |  | K3A1 (K3A1) | Auburn University Regional Airport (KAUO) | 2026-09-05 00:28 UTC | 2026-09-05 00:54 UTC | 26m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-05 00:40 UTC | 2026-09-05 00:52 UTC | 12m |
| FFT3393 | FFT | Salt Lake City International Airport (KSLC) | San Francisco International Airport (KSFO) | 2026-09-04 23:05 UTC | 2026-09-05 00:50 UTC | 1h 44m |
| XSN40 | XSN | Lake Tahoe Airport (KTVL) | Palo Alto Airport (KPAO) | 2026-09-05 00:10 UTC | 2026-09-05 00:48 UTC | 37m |
| IGO1924 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-04 16:19 UTC | 2026-09-05 00:47 UTC | 8h 28m |
| N460NG |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-09-05 00:00 UTC | 2026-09-05 00:38 UTC | 37m |
| QTR27R | Qatar Airways | Sydney Kingsford Smith International Airport (YSSY) | Hamad International Airport (OTHH) | 2026-09-04 10:59 UTC | 2026-09-05 00:36 UTC | 13h 36m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-04 23:43 UTC | 2026-09-05 00:35 UTC | 52m |
| TWY967 | TWY | Chicago Midway International Airport (KMDW) | Telluride Regional Airport (KTEX) | 2026-09-04 21:29 UTC | 2026-09-05 00:32 UTC | 3h 3m |
| XSN90 | XSN | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-09-04 23:46 UTC | 2026-09-05 00:31 UTC | 44m |
| N67973 |  | Denton Enterprise Airport (KDTO) | Bridgeport Municipal Airport (KXBP) | 2026-09-04 23:42 UTC | 2026-09-05 00:28 UTC | 46m |
| N284EX |  | French Valley Airport (KF70) | 4CL4 (4CL4) | 2026-09-05 00:03 UTC | 2026-09-05 00:24 UTC | 21m |
| ES822 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-09-05 00:14 UTC | 2026-09-05 00:19 UTC | 5m |
| N388BB |  | John C Tune Airport (KJWN) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-04 23:12 UTC | 2026-09-05 00:18 UTC | 1h 6m |
| N930F |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Hayward Executive Airport (KHWD) | 2026-09-04 23:05 UTC | 2026-09-05 00:16 UTC | 1h 11m |
| N561MT |  | 80TX (80TX) | Mc Neill Ranch Airport (6TE7) | 2026-09-04 22:33 UTC | 2026-09-05 00:16 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
