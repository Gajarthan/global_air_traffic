# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_00:15:03_UTC-green)

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

**Latest saved flight:** 2026-09-19 00:15:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 00:15:03 UTC

- **263,059** saved flights
- **77,764** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,059** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,186,471.9 tonnes** estimated CO2 emissions
- **184,723,006 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10405 |
| 2 | SkyWest Airlines | 9157 |
| 3 | EJA | 5107 |
| 4 | IndiGo | 4416 |
| 5 | American Airlines | 4127 |
| 6 | Southwest Airlines | 3863 |
| 7 | Delta Air Lines | 3286 |
| 8 | ENY | 3103 |
| 9 | LATAM Airlines | 2535 |
| 10 | AZU | 2472 |
| 11 | Vueling | 2212 |
| 12 | WIF | 2125 |
| 13 | LXJ | 2063 |
| 14 | Lufthansa | 2030 |
| 15 | easyJet | 1777 |
| 16 | Swiss International | 1736 |
| 17 | QLK | 1701 |
| 18 | AXM | 1656 |
| 19 | EJU | 1656 |
| 20 | United Airlines | 1613 |
| 21 | Alaska Airlines | 1559 |
| 22 | All Nippon Airways | 1519 |
| 23 | WMT | 1479 |
| 24 | PGT | 1477 |
| 25 | GLO | 1469 |
| 26 | Air France | 1442 |
| 27 | VIV | 1438 |
| 28 | Wizz Air | 1428 |
| 29 | CXK | 1275 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218655 |
| 2 | 🇪🇸 ES | 16585 |
| 3 | 🇧🇷 BR | 15397 |
| 4 | 🇦🇺 AU | 15097 |
| 5 | 🇨🇦 CA | 14649 |
| 6 | 🇮🇹 IT | 14287 |
| 7 | 🇮🇳 IN | 13951 |
| 8 | 🇩🇪 DE | 12707 |
| 9 | 🇬🇧 GB | 12215 |
| 10 | 🇨🇴 CO | 11910 |
| 11 | 🇫🇷 FR | 10511 |
| 12 | 🇯🇵 JP | 10181 |
| 13 | 🇹🇷 TR | 7960 |
| 14 | 🇬🇷 GR | 7628 |
| 15 | 🇲🇽 MX | 7237 |
| 16 | 🇨🇭 CH | 7016 |
| 17 | 🇳🇴 NO | 6500 |
| 18 | 🇹🇭 TH | 4707 |
| 19 | 🇲🇾 MY | 4465 |
| 20 | 🇿🇦 ZA | 4432 |
| 21 | 🇵🇱 PL | 4335 |
| 22 | 🇳🇿 NZ | 3643 |
| 23 | 🇵🇭 PH | 3502 |
| 24 | 🇬🇹 GT | 3352 |
| 25 | 🇭🇷 HR | 3000 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2631 |
| 28 | 🇲🇪 ME | 2467 |
| 29 | 🇳🇱 NL | 2349 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5380 |
| 2 | Denver International Airport |  | US | 4253 |
| 3 | Indira Gandhi International Airport |  | IN | 3158 |
| 4 | Tokyo International Airport |  | JP | 3039 |
| 5 | Harry Reid International Airport |  | US | 2799 |
| 6 | El Dorado International Airport |  | CO | 2785 |
| 7 | Guaymaral Airport |  | CO | 2779 |
| 8 | Zurich Airport |  | CH | 2738 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2646 |
| 10 | La Aurora Airport |  | GT | 2548 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2547 |
| 12 | Salt Lake City International Airport |  | US | 2325 |
| 13 | Chicago O'Hare International Airport |  | US | 2265 |
| 14 | Congonhas Airport |  | BR | 2248 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2151 |
| 16 | Capua Airport |  | IT | 2052 |
| 17 | Madrid Barajas International Airport |  | ES | 2033 |
| 18 | Frankfurt am Main International Airport |  | DE | 2004 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1985 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1889 |
| 21 | Malpensa International Airport |  | IT | 1889 |
| 22 | Charles de Gaulle International Airport |  | FR | 1859 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1855 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1820 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1799 |
| 26 | Macau International Airport |  | MO | 1747 |
| 27 | Ninoy Aquino International Airport |  | PH | 1719 |
| 28 | Barcelona International Airport |  | ES | 1643 |
| 29 | Charlotte/Douglas International Airport |  | US | 1642 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1618 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1595 |
| 33 | Seattle-Tacoma International Airport |  | US | 1545 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1532 |
| 35 | Calgary International Airport |  | CA | 1500 |
| 36 | Don Mueang International Airport |  | TH | 1498 |
| 37 | Bengaluru International Airport |  | IN | 1493 |
| 38 | Oslo Gardermoen Airport |  | NO | 1481 |
| 39 | Vancouver International Airport |  | CA | 1472 |
| 40 | Antalya International Airport |  | TR | 1407 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 982 | 21m | 244 km | 4,134.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 720 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 426 | 44m | 555 km | 4,079.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 371 | 24m | 218 km | 1,397.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 360 | 21m | 250 km | 1,555.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 281 | 28m | 152 km | 734.4 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 280 | 42m | 535 km | 2,586.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFRQ31 | Air France | Chena Hot Springs Airport (AK13) | Eielson Afb Airport (PAEI) | 2026-09-18 23:58 UTC | 2026-09-19 00:15 UTC | 16m |
| RFS716 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-09-18 23:23 UTC | 2026-09-19 00:14 UTC | 51m |
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-18 17:37 UTC | 2026-09-19 00:12 UTC | 6h 34m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-18 23:54 UTC | 2026-09-19 00:10 UTC | 15m |
| PGT390 | PGT | Sabiha Gokcen International Airport (LTFJ) | LZSY (LZSY) | 2026-09-18 22:20 UTC | 2026-09-19 00:09 UTC | 1h 49m |
| N1737A |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-09-18 23:56 UTC | 2026-09-19 00:08 UTC | 12m |
| RZO176 | RZO | João Paulo II Airport (LPPD) | Francisco de Sá Carneiro Airport (LPPR) | 2026-09-18 22:03 UTC | 2026-09-19 00:05 UTC | 2h 1m |
| N801MM |  | Lagrange/Callaway Airport (KLGC) | University-Oxford Airport (KUOX) | 2026-09-18 23:29 UTC | 2026-09-19 00:03 UTC | 33m |
| N217AT |  | Brown Field Municipal Airport (KSDM) | Big Bear City Airport (KL35) | 2026-09-18 23:16 UTC | 2026-09-19 00:02 UTC | 45m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-18 23:43 UTC | 2026-09-19 00:00 UTC | 17m |
| N628SR |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-09-18 23:11 UTC | 2026-09-18 23:51 UTC | 39m |
| N14WG |  | Livermore Municipal Airport (KLVK) | Sacramento Executive Airport (KSAC) | 2026-09-18 23:12 UTC | 2026-09-18 23:49 UTC | 37m |
| N48AZ |  | Dekalb-Peachtree Airport (KPDK) | Waynesville-St Robert Regional Forney Field (KTBN) | 2026-09-18 21:55 UTC | 2026-09-18 23:49 UTC | 1h 53m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-18 23:34 UTC | 2026-09-18 23:48 UTC | 13m |
| N258CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-18 23:00 UTC | 2026-09-18 23:47 UTC | 47m |
| FFL626 | FFL | Riverview Ranch Airport (8OR3) | Tracy Municipal Airport (KTCY) | 2026-09-18 22:25 UTC | 2026-09-18 23:47 UTC | 1h 22m |
| N914TV |  | Teterboro Airport (KTEB) | 3NY5 (3NY5) | 2026-09-18 23:25 UTC | 2026-09-18 23:47 UTC | 21m |
| N29028 |  | MU19 (MU19) | Northwest Arkansas Ntl Airport (KXNA) | 2026-09-18 22:47 UTC | 2026-09-18 23:47 UTC | 1h 0m |
| 0XF9610 |  | Falcon Field (KFFZ) | 4AZ7 (4AZ7) | 2026-09-18 23:04 UTC | 2026-09-18 23:38 UTC | 33m |
| SKW3777 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Baker & Hall Airport (77CL) | 2026-09-18 22:31 UTC | 2026-09-18 23:37 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
