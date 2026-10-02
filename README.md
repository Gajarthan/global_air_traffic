# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_23:25:02_UTC-green)

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

**Latest saved flight:** 2026-10-02 23:25:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-02 23:25:02 UTC

- **274,986** saved flights
- **80,161** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,986** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,327,434.9 tonnes** estimated CO2 emissions
- **192,894,777 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10787 |
| 2 | SkyWest Airlines | 9571 |
| 3 | EJA | 5388 |
| 4 | IndiGo | 4579 |
| 5 | American Airlines | 4256 |
| 6 | Southwest Airlines | 4041 |
| 7 | Delta Air Lines | 3417 |
| 8 | ENY | 3220 |
| 9 | LATAM Airlines | 2663 |
| 10 | AZU | 2586 |
| 11 | Vueling | 2281 |
| 12 | WIF | 2241 |
| 13 | LXJ | 2173 |
| 14 | Lufthansa | 2070 |
| 15 | easyJet | 1828 |
| 16 | Swiss International | 1801 |
| 17 | QLK | 1774 |
| 18 | EJU | 1710 |
| 19 | AXM | 1688 |
| 20 | United Airlines | 1678 |
| 21 | Alaska Airlines | 1617 |
| 22 | All Nippon Airways | 1569 |
| 23 | PGT | 1546 |
| 24 | GLO | 1536 |
| 25 | WMT | 1530 |
| 26 | Air France | 1509 |
| 27 | VIV | 1507 |
| 28 | Wizz Air | 1485 |
| 29 | CXK | 1356 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 229468 |
| 2 | 🇪🇸 ES | 17190 |
| 3 | 🇧🇷 BR | 16152 |
| 4 | 🇦🇺 AU | 15867 |
| 5 | 🇨🇦 CA | 15336 |
| 6 | 🇮🇹 IT | 14815 |
| 7 | 🇮🇳 IN | 14493 |
| 8 | 🇩🇪 DE | 13159 |
| 9 | 🇨🇴 CO | 12746 |
| 10 | 🇬🇧 GB | 12657 |
| 11 | 🇫🇷 FR | 10871 |
| 12 | 🇯🇵 JP | 10483 |
| 13 | 🇹🇷 TR | 8310 |
| 14 | 🇬🇷 GR | 7894 |
| 15 | 🇲🇽 MX | 7600 |
| 16 | 🇨🇭 CH | 7295 |
| 17 | 🇳🇴 NO | 6788 |
| 18 | 🇹🇭 TH | 4917 |
| 19 | 🇲🇾 MY | 4569 |
| 20 | 🇿🇦 ZA | 4558 |
| 21 | 🇵🇱 PL | 4484 |
| 22 | 🇳🇿 NZ | 3895 |
| 23 | 🇵🇭 PH | 3627 |
| 24 | 🇬🇹 GT | 3454 |
| 25 | 🇭🇷 HR | 3129 |
| 26 | 🇰🇷 KR | 3093 |
| 27 | 🇲🇦 MA | 2714 |
| 28 | 🇲🇪 ME | 2576 |
| 29 | 🇳🇱 NL | 2457 |
| 30 | 🇮🇩 ID | 2272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5584 |
| 2 | Denver International Airport |  | US | 4488 |
| 3 | Indira Gandhi International Airport |  | IN | 3280 |
| 4 | Tokyo International Airport |  | JP | 3142 |
| 5 | El Dorado International Airport |  | CO | 3036 |
| 6 | Harry Reid International Airport |  | US | 2961 |
| 7 | Zurich Airport |  | CH | 2854 |
| 8 | Guaymaral Airport |  | CO | 2849 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2748 |
| 10 | La Aurora Airport |  | GT | 2626 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2626 |
| 12 | Salt Lake City International Airport |  | US | 2443 |
| 13 | Congonhas Airport |  | BR | 2351 |
| 14 | Chicago O'Hare International Airport |  | US | 2325 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2249 |
| 16 | Capua Airport |  | IT | 2133 |
| 17 | Madrid Barajas International Airport |  | ES | 2114 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2096 |
| 19 | Frankfurt am Main International Airport |  | DE | 2067 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1950 |
| 22 | Charles de Gaulle International Airport |  | FR | 1945 |
| 23 | Malpensa International Airport |  | IT | 1943 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1838 |
| 26 | Macau International Airport |  | MO | 1790 |
| 27 | Ninoy Aquino International Airport |  | PH | 1783 |
| 28 | Charlotte/Douglas International Airport |  | US | 1717 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1711 |
| 30 | Barcelona International Airport |  | ES | 1697 |
| 31 | Viracopos International Airport |  | BR | 1646 |
| 32 | Kuala Lumpur International Airport |  | MY | 1635 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1616 |
| 34 | Seattle-Tacoma International Airport |  | US | 1613 |
| 35 | Calgary International Airport |  | CA | 1563 |
| 36 | Don Mueang International Airport |  | TH | 1551 |
| 37 | Vancouver International Airport |  | CA | 1543 |
| 38 | Oslo Gardermoen Airport |  | NO | 1542 |
| 39 | Bengaluru International Airport |  | IN | 1536 |
| 40 | Reno/Tahoe International Airport |  | US | 1492 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1133 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1033 | 21m | 244 km | 4,349.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 694 | 1h 6m | 770 km | 9,219.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 691 | 24m | 225 km | 2,680.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 610 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 434 | 1h 50m | 1,423 km | 10,651.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 393 | 24m | 218 km | 1,480.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 349 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 345 | 1h 6m | 706 km | 4,200.4 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 320 | 19m | 144 km | 796.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 316 | 18m | 14 km | 79.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 307 | 42m | 535 km | 2,835.3 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AA52 |  | Mountain Valley Airport (KL94) | 6CL4 (6CL4) | 2026-10-02 21:47 UTC | 2026-10-02 23:25 UTC | 1h 37m |
| TKR10 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-10-02 23:07 UTC | 2026-10-02 23:21 UTC | 14m |
| N692PD |  | Runway Ranch Airport (2MO9) | Kansas City Downtown/Wheeler Field (KMKC) | 2026-10-02 21:36 UTC | 2026-10-02 23:20 UTC | 1h 43m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-02 23:06 UTC | 2026-10-02 23:17 UTC | 10m |
| N6946F |  | Mount Pleasant Landing Strip (67NJ) | Lehigh Valley International Airport (KABE) | 2026-10-02 22:54 UTC | 2026-10-02 23:16 UTC | 21m |
| TKR168 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-10-02 22:55 UTC | 2026-10-02 23:11 UTC | 16m |
| DSTY612 | DST | First Flight Airport (KFFA) | First Flight Airport (KFFA) | 2026-10-02 22:12 UTC | 2026-10-02 23:11 UTC | 59m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-10-02 22:49 UTC | 2026-10-02 23:07 UTC | 18m |
| N6036Y |  | Monterey Regional Airport (KMRY) | San Carlos Airport (KSQL) | 2026-10-02 22:34 UTC | 2026-10-02 23:07 UTC | 33m |
| TKR910 | TKR | San Bernardino International Airport (KSBD) | Lake Tahoe Airport (KTVL) | 2026-10-02 22:08 UTC | 2026-10-02 23:04 UTC | 56m |
| IDD621 | IDD | Boise Air Trml/Gowen Field (KBOI) | Cascade Airport (KU70) | 2026-10-02 22:51 UTC | 2026-10-02 23:03 UTC | 11m |
|  |  | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-10-02 22:54 UTC | 2026-10-02 23:02 UTC | 8m |
| TKR164 | TKR | Paradise Skypark Airport (CA92) | Sierraville Dearwater Airport (KO79) | 2026-10-02 22:50 UTC | 2026-10-02 23:02 UTC | 12m |
| N617DC |  | Long Beach (Daugherty Field) Airport (KLGB) | 3CA9 (3CA9) | 2026-10-02 21:46 UTC | 2026-10-02 23:01 UTC | 1h 14m |
| N69P |  | Montgomery-Gibbs Executive Airport (KMYF) | Jacqueline Cochran Regional Airport (KTRM) | 2026-10-02 22:41 UTC | 2026-10-02 23:00 UTC | 18m |
| SLG2 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Nipawin Airport (CYBU) | 2026-10-02 22:27 UTC | 2026-10-02 22:56 UTC | 28m |
| N713SQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-10-02 22:17 UTC | 2026-10-02 22:54 UTC | 37m |
| TKR137 | TKR | Redding Regional Airport (KRDD) | CA38 (CA38) | 2026-10-02 22:37 UTC | 2026-10-02 22:53 UTC | 16m |
| XSN25 | XSN | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-10-02 21:22 UTC | 2026-10-02 22:53 UTC | 1h 30m |
| N4800G |  | Tacoma Narrows Airport (KTIW) | Tacoma Narrows Airport (KTIW) | 2026-10-02 22:36 UTC | 2026-10-02 22:53 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
