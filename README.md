# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_01:13:41_UTC-green)

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

**Latest saved flight:** 2026-09-30 01:13:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-30 01:13:41 UTC

- **272,752** saved flights
- **79,699** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,752** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,303,904.9 tonnes** estimated CO2 emissions
- **191,530,721 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10720 |
| 2 | SkyWest Airlines | 9505 |
| 3 | EJA | 5340 |
| 4 | IndiGo | 4551 |
| 5 | American Airlines | 4234 |
| 6 | Southwest Airlines | 4014 |
| 7 | Delta Air Lines | 3391 |
| 8 | ENY | 3201 |
| 9 | LATAM Airlines | 2631 |
| 10 | AZU | 2562 |
| 11 | Vueling | 2266 |
| 12 | WIF | 2217 |
| 13 | LXJ | 2148 |
| 14 | Lufthansa | 2061 |
| 15 | easyJet | 1820 |
| 16 | Swiss International | 1783 |
| 17 | QLK | 1759 |
| 18 | EJU | 1702 |
| 19 | AXM | 1679 |
| 20 | United Airlines | 1668 |
| 21 | Alaska Airlines | 1608 |
| 22 | All Nippon Airways | 1562 |
| 23 | PGT | 1538 |
| 24 | GLO | 1522 |
| 25 | WMT | 1517 |
| 26 | Air France | 1499 |
| 27 | VIV | 1494 |
| 28 | Wizz Air | 1480 |
| 29 | CXK | 1348 |
| 30 | AEE | 1304 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227417 |
| 2 | 🇪🇸 ES | 17058 |
| 3 | 🇧🇷 BR | 15999 |
| 4 | 🇦🇺 AU | 15737 |
| 5 | 🇨🇦 CA | 15203 |
| 6 | 🇮🇹 IT | 14720 |
| 7 | 🇮🇳 IN | 14402 |
| 8 | 🇩🇪 DE | 13062 |
| 9 | 🇨🇴 CO | 12588 |
| 10 | 🇬🇧 GB | 12584 |
| 11 | 🇫🇷 FR | 10819 |
| 12 | 🇯🇵 JP | 10430 |
| 13 | 🇹🇷 TR | 8260 |
| 14 | 🇬🇷 GR | 7854 |
| 15 | 🇲🇽 MX | 7540 |
| 16 | 🇨🇭 CH | 7242 |
| 17 | 🇳🇴 NO | 6728 |
| 18 | 🇹🇭 TH | 4880 |
| 19 | 🇲🇾 MY | 4550 |
| 20 | 🇿🇦 ZA | 4537 |
| 21 | 🇵🇱 PL | 4464 |
| 22 | 🇳🇿 NZ | 3852 |
| 23 | 🇵🇭 PH | 3599 |
| 24 | 🇬🇹 GT | 3428 |
| 25 | 🇭🇷 HR | 3104 |
| 26 | 🇰🇷 KR | 3074 |
| 27 | 🇲🇦 MA | 2701 |
| 28 | 🇲🇪 ME | 2556 |
| 29 | 🇳🇱 NL | 2445 |
| 30 | 🇮🇩 ID | 2266 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5555 |
| 2 | Denver International Airport |  | US | 4451 |
| 3 | Indira Gandhi International Airport |  | IN | 3254 |
| 4 | Tokyo International Airport |  | JP | 3125 |
| 5 | El Dorado International Airport |  | CO | 2994 |
| 6 | Harry Reid International Airport |  | US | 2934 |
| 7 | Guaymaral Airport |  | CO | 2833 |
| 8 | Zurich Airport |  | CH | 2826 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2735 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2615 |
| 11 | La Aurora Airport |  | GT | 2605 |
| 12 | Salt Lake City International Airport |  | US | 2420 |
| 13 | Congonhas Airport |  | BR | 2328 |
| 14 | Chicago O'Hare International Airport |  | US | 2317 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2233 |
| 16 | Capua Airport |  | IT | 2108 |
| 17 | Madrid Barajas International Airport |  | ES | 2099 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2067 |
| 19 | Frankfurt am Main International Airport |  | DE | 2057 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1936 |
| 21 | Malpensa International Airport |  | IT | 1935 |
| 22 | Charles de Gaulle International Airport |  | FR | 1935 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1933 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1912 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1768 |
| 28 | Charlotte/Douglas International Airport |  | US | 1707 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1688 |
| 31 | Viracopos International Airport |  | BR | 1640 |
| 32 | Kuala Lumpur International Airport |  | MY | 1630 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1601 |
| 34 | Seattle-Tacoma International Airport |  | US | 1599 |
| 35 | Calgary International Airport |  | CA | 1548 |
| 36 | Don Mueang International Airport |  | TH | 1543 |
| 37 | Bengaluru International Airport |  | IN | 1530 |
| 38 | Oslo Gardermoen Airport |  | NO | 1527 |
| 39 | Vancouver International Airport |  | CA | 1525 |
| 40 | Reno/Tahoe International Airport |  | US | 1465 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1127 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1023 | 21m | 244 km | 4,307.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 758 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 688 | 1h 6m | 770 km | 9,139.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 682 | 24m | 225 km | 2,645.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 456 | 44m | 555 km | 4,366.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 438 | 27m | 275 km | 2,075.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 431 | 1h 50m | 1,423 km | 10,577.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 369 | 21m | 250 km | 1,593.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 367 | 23m | 55 km | 348.8 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 349 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 309 | 1h 14m | 961 km | 5,121.8 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 306 | 18m | 14 km | 76.5 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| C2301 |  | Miami-Opa Locka Executive Airport (KOPF) | Dade-Collier Training And Transition Airport (KTNT) | 2026-09-30 00:11 UTC | 2026-09-30 01:13 UTC | 1h 2m |
| MTU07 | MTU | Cedar Glade Aerodrome (TN83) | Cedar Glade Aerodrome (TN83) | 2026-09-30 00:48 UTC | 2026-09-30 01:10 UTC | 22m |
| TANDM22 | TAN | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-09-30 00:53 UTC | 2026-09-30 01:09 UTC | 16m |
| N805KG |  | Teterboro Airport (KTEB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-29 23:57 UTC | 2026-09-30 01:08 UTC | 1h 10m |
| LS31 |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-30 00:41 UTC | 2026-09-30 01:05 UTC | 24m |
| LDACE21 | LDA | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-09-30 00:01 UTC | 2026-09-30 01:05 UTC | 1h 3m |
| X2A |  | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-09-30 00:36 UTC | 2026-09-30 01:04 UTC | 28m |
| N478CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-30 00:01 UTC | 2026-09-30 01:01 UTC | 1h 0m |
| UAL2834 | United Airlines | Laguardia Airport (KLGA) | Denver International Airport (KDEN) | 2026-09-29 21:19 UTC | 2026-09-30 01:01 UTC | 3h 42m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-30 00:13 UTC | 2026-09-30 01:00 UTC | 46m |
| N281NX |  | Mesa Gateway Airport (KIWA) | Mid-Way Regional Airport (KJWY) | 2026-09-29 22:48 UTC | 2026-09-30 00:56 UTC | 2h 8m |
| ZKDSR | ZKD | Waiheke Reeve Airport (NZKE) | Ardmore Airport (NZAR) | 2026-09-30 00:39 UTC | 2026-09-30 00:53 UTC | 14m |
| BRG652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-09-30 00:24 UTC | 2026-09-30 00:52 UTC | 28m |
| CFR94 | CFR | Redding Regional Airport (KRDD) | Rogue Valley International/Medford Airport (KMFR) | 2026-09-30 00:00 UTC | 2026-09-30 00:46 UTC | 46m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-30 00:34 UTC | 2026-09-30 00:44 UTC | 10m |
| N7503W |  | Skypark Airport (KBTF) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-30 00:12 UTC | 2026-09-30 00:44 UTC | 31m |
| CGTNM | CGT | High River Airport (CEN4) | Lethbridge / J3 Airfield (CLJ3) | 2026-09-30 00:17 UTC | 2026-09-30 00:43 UTC | 25m |
| TANDM22 | TAN | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-09-30 00:04 UTC | 2026-09-30 00:40 UTC | 35m |
| C2714 |  | Mc Clellan Airfield (KMCC) | Longbell Ranch Airport (2CL3) | 2026-09-29 23:57 UTC | 2026-09-30 00:38 UTC | 41m |
| GRYHK11 | GRY | CL35 (CL35) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-09-30 00:23 UTC | 2026-09-30 00:38 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
