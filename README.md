# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_21:26:06_UTC-green)

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

**Latest saved flight:** 2026-10-04 21:26:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-04 21:26:06 UTC

- **276,471** saved flights
- **80,440** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **276,471** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,347,273.8 tonnes** estimated CO2 emissions
- **194,044,856 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10841 |
| 2 | SkyWest Airlines | 9612 |
| 3 | EJA | 5423 |
| 4 | IndiGo | 4611 |
| 5 | American Airlines | 4275 |
| 6 | Southwest Airlines | 4057 |
| 7 | Delta Air Lines | 3434 |
| 8 | ENY | 3227 |
| 9 | LATAM Airlines | 2679 |
| 10 | AZU | 2602 |
| 11 | Vueling | 2290 |
| 12 | WIF | 2250 |
| 13 | LXJ | 2187 |
| 14 | Lufthansa | 2077 |
| 15 | easyJet | 1834 |
| 16 | Swiss International | 1806 |
| 17 | QLK | 1779 |
| 18 | EJU | 1720 |
| 19 | AXM | 1694 |
| 20 | United Airlines | 1683 |
| 21 | Alaska Airlines | 1632 |
| 22 | All Nippon Airways | 1577 |
| 23 | PGT | 1555 |
| 24 | GLO | 1543 |
| 25 | WMT | 1536 |
| 26 | Air France | 1522 |
| 27 | VIV | 1515 |
| 28 | Wizz Air | 1498 |
| 29 | CXK | 1366 |
| 30 | AEE | 1314 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230715 |
| 2 | 🇪🇸 ES | 17285 |
| 3 | 🇧🇷 BR | 16243 |
| 4 | 🇦🇺 AU | 15923 |
| 5 | 🇨🇦 CA | 15398 |
| 6 | 🇮🇹 IT | 14913 |
| 7 | 🇮🇳 IN | 14589 |
| 8 | 🇩🇪 DE | 13201 |
| 9 | 🇨🇴 CO | 12840 |
| 10 | 🇬🇧 GB | 12732 |
| 11 | 🇫🇷 FR | 10930 |
| 12 | 🇯🇵 JP | 10523 |
| 13 | 🇹🇷 TR | 8346 |
| 14 | 🇬🇷 GR | 7921 |
| 15 | 🇲🇽 MX | 7638 |
| 16 | 🇨🇭 CH | 7338 |
| 17 | 🇳🇴 NO | 6819 |
| 18 | 🇹🇭 TH | 4958 |
| 19 | 🇲🇾 MY | 4588 |
| 20 | 🇿🇦 ZA | 4576 |
| 21 | 🇵🇱 PL | 4520 |
| 22 | 🇳🇿 NZ | 3930 |
| 23 | 🇵🇭 PH | 3653 |
| 24 | 🇬🇹 GT | 3467 |
| 25 | 🇭🇷 HR | 3143 |
| 26 | 🇰🇷 KR | 3106 |
| 27 | 🇲🇦 MA | 2729 |
| 28 | 🇲🇪 ME | 2594 |
| 29 | 🇳🇱 NL | 2465 |
| 30 | 🇮🇩 ID | 2283 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5602 |
| 2 | Denver International Airport |  | US | 4510 |
| 3 | Indira Gandhi International Airport |  | IN | 3293 |
| 4 | Tokyo International Airport |  | JP | 3156 |
| 5 | El Dorado International Airport |  | CO | 3074 |
| 6 | Harry Reid International Airport |  | US | 2977 |
| 7 | Zurich Airport |  | CH | 2869 |
| 8 | Guaymaral Airport |  | CO | 2854 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2764 |
| 10 | La Aurora Airport |  | GT | 2637 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2635 |
| 12 | Salt Lake City International Airport |  | US | 2458 |
| 13 | Congonhas Airport |  | BR | 2363 |
| 14 | Chicago O'Hare International Airport |  | US | 2329 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2266 |
| 16 | Capua Airport |  | IT | 2151 |
| 17 | Madrid Barajas International Airport |  | ES | 2128 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2110 |
| 19 | Frankfurt am Main International Airport |  | DE | 2077 |
| 20 | Charles de Gaulle International Airport |  | FR | 1962 |
| 21 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 22 | Hartsfield/Jackson Atlanta International Airport |  | US | 1959 |
| 23 | Malpensa International Airport |  | IT | 1951 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1843 |
| 26 | Macau International Airport |  | MO | 1799 |
| 27 | Ninoy Aquino International Airport |  | PH | 1798 |
| 28 | Charlotte/Douglas International Airport |  | US | 1724 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1718 |
| 30 | Barcelona International Airport |  | ES | 1703 |
| 31 | Viracopos International Airport |  | BR | 1657 |
| 32 | Kuala Lumpur International Airport |  | MY | 1645 |
| 33 | Seattle-Tacoma International Airport |  | US | 1627 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1626 |
| 35 | Calgary International Airport |  | CA | 1571 |
| 36 | Don Mueang International Airport |  | TH | 1562 |
| 37 | Oslo Gardermoen Airport |  | NO | 1550 |
| 38 | Vancouver International Airport |  | CA | 1547 |
| 39 | Bengaluru International Airport |  | IN | 1543 |
| 40 | Reno/Tahoe International Airport |  | US | 1500 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1043 | 21m | 244 km | 4,391.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 698 | 24m | 225 km | 2,707.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 698 | 1h 6m | 770 km | 9,272.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 461 | 44m | 555 km | 4,414.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 437 | 1h 50m | 1,423 km | 10,724.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 425 | 44m | 241 km | 1,765.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 371 | 21m | 250 km | 1,602.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 356 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 348 | 1h 6m | 706 km | 4,236.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 343 | 26m | 215 km | 1,270.3 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 337 | 1h 40m | 1,156 km | 6,723.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 322 | 19m | 144 km | 801.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 321 | 18m | 14 km | 80.3 t |
| 23 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 312 | 42m | 535 km | 2,881.5 t |
| 24 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 287 | 28m | 152 km | 750.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 275 | 44m | 431 km | 2,046.5 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N51209 |  | Olive Branch/Taylor Field (KOLV) | Holly Springs-Marshall County Airport (KM41) | 2026-10-04 20:48 UTC | 2026-10-04 21:26 UTC | 37m |
| XSN73 | XSN | Charles M Schulz/Sonoma County Airport (KSTS) | San Carlos Airport (KSQL) | 2026-10-04 20:57 UTC | 2026-10-04 21:18 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-10-04 21:01 UTC | 2026-10-04 21:14 UTC | 13m |
| RFS715 | RFS | Tacoma Narrows Airport (KTIW) | Sanderson Field (KSHN) | 2026-10-04 20:31 UTC | 2026-10-04 21:09 UTC | 37m |
| LPE2297 | LPE | Jorge Chavez International Airport (SPJC) | Pampa Grande Airport (SPJB) | 2026-10-04 20:26 UTC | 2026-10-04 21:08 UTC | 42m |
| N28UC |  | Minden-Tahoe Airport (KMEV) | Lee Vining Airport (KO24) | 2026-10-04 19:11 UTC | 2026-10-04 21:03 UTC | 1h 51m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-04 20:45 UTC | 2026-10-04 20:56 UTC | 10m |
| N52NG |  | North Las Vegas Airport (KVGT) | Colorado City Municipal Airport (KAZC) | 2026-10-04 20:20 UTC | 2026-10-04 20:54 UTC | 34m |
| ZKIEN | ZKI | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-10-04 20:18 UTC | 2026-10-04 20:53 UTC | 35m |
| N44NC |  | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-10-04 20:39 UTC | 2026-10-04 20:50 UTC | 10m |
| SCU28 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 19OK (19OK) | 2026-10-04 20:30 UTC | 2026-10-04 20:49 UTC | 18m |
| N650MC |  | Palo Alto Airport (KPAO) | Telluride Regional Airport (KTEX) | 2026-10-04 18:06 UTC | 2026-10-04 20:49 UTC | 2h 43m |
| N15MJ |  | Palo Alto Airport (KPAO) | Half Moon Bay Airport (KHAF) | 2026-10-04 20:29 UTC | 2026-10-04 20:47 UTC | 18m |
| N805FA |  | Napa County Airport (KAPC) | Palm Springs International Airport (KPSP) | 2026-10-04 19:02 UTC | 2026-10-04 20:46 UTC | 1h 43m |
| EJA425 | EJA | Westchester County Airport (KHPN) | Lt Warren Eaton Airport (KOIC) | 2026-10-04 20:18 UTC | 2026-10-04 20:45 UTC | 26m |
| ACO1 | ACO | Jorge Chavez International Airport (SPJC) | Capitan FAP Renan Elias Olivera International Airport (SPSO) | 2026-10-04 20:14 UTC | 2026-10-04 20:44 UTC | 29m |
| EJA931 | EJA | Napa County Airport (KAPC) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-10-04 17:20 UTC | 2026-10-04 20:44 UTC | 3h 23m |
| BYF31 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-10-04 20:03 UTC | 2026-10-04 20:43 UTC | 40m |
| N797GM |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-10-04 20:06 UTC | 2026-10-04 20:42 UTC | 36m |
| NEW961 | NEW | San Francisco International Airport (KSFO) | Laguardia Airport (KLGA) | 2026-10-04 16:04 UTC | 2026-10-04 20:41 UTC | 4h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
