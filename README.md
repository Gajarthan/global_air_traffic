# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_19:57:34_UTC-green)

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

**Latest saved flight:** 2026-10-02 19:57:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-02 19:57:34 UTC

- **274,811** saved flights
- **80,119** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,811** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,326,051.7 tonnes** estimated CO2 emissions
- **192,814,590 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10786 |
| 2 | SkyWest Airlines | 9559 |
| 3 | EJA | 5385 |
| 4 | IndiGo | 4578 |
| 5 | American Airlines | 4254 |
| 6 | Southwest Airlines | 4036 |
| 7 | Delta Air Lines | 3414 |
| 8 | ENY | 3217 |
| 9 | LATAM Airlines | 2657 |
| 10 | AZU | 2584 |
| 11 | Vueling | 2280 |
| 12 | WIF | 2241 |
| 13 | LXJ | 2170 |
| 14 | Lufthansa | 2070 |
| 15 | easyJet | 1828 |
| 16 | Swiss International | 1801 |
| 17 | QLK | 1774 |
| 18 | EJU | 1710 |
| 19 | AXM | 1688 |
| 20 | United Airlines | 1676 |
| 21 | Alaska Airlines | 1617 |
| 22 | All Nippon Airways | 1569 |
| 23 | PGT | 1545 |
| 24 | GLO | 1535 |
| 25 | WMT | 1530 |
| 26 | Air France | 1509 |
| 27 | VIV | 1506 |
| 28 | Wizz Air | 1485 |
| 29 | CXK | 1356 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 229229 |
| 2 | 🇪🇸 ES | 17188 |
| 3 | 🇧🇷 BR | 16128 |
| 4 | 🇦🇺 AU | 15861 |
| 5 | 🇨🇦 CA | 15325 |
| 6 | 🇮🇹 IT | 14813 |
| 7 | 🇮🇳 IN | 14492 |
| 8 | 🇩🇪 DE | 13159 |
| 9 | 🇨🇴 CO | 12738 |
| 10 | 🇬🇧 GB | 12656 |
| 11 | 🇫🇷 FR | 10871 |
| 12 | 🇯🇵 JP | 10481 |
| 13 | 🇹🇷 TR | 8308 |
| 14 | 🇬🇷 GR | 7894 |
| 15 | 🇲🇽 MX | 7593 |
| 16 | 🇨🇭 CH | 7295 |
| 17 | 🇳🇴 NO | 6788 |
| 18 | 🇹🇭 TH | 4917 |
| 19 | 🇲🇾 MY | 4569 |
| 20 | 🇿🇦 ZA | 4558 |
| 21 | 🇵🇱 PL | 4484 |
| 22 | 🇳🇿 NZ | 3885 |
| 23 | 🇵🇭 PH | 3627 |
| 24 | 🇬🇹 GT | 3448 |
| 25 | 🇭🇷 HR | 3129 |
| 26 | 🇰🇷 KR | 3093 |
| 27 | 🇲🇦 MA | 2714 |
| 28 | 🇲🇪 ME | 2576 |
| 29 | 🇳🇱 NL | 2457 |
| 30 | 🇮🇩 ID | 2272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5578 |
| 2 | Denver International Airport |  | US | 4481 |
| 3 | Indira Gandhi International Airport |  | IN | 3280 |
| 4 | Tokyo International Airport |  | JP | 3141 |
| 5 | El Dorado International Airport |  | CO | 3033 |
| 6 | Harry Reid International Airport |  | US | 2955 |
| 7 | Zurich Airport |  | CH | 2854 |
| 8 | Guaymaral Airport |  | CO | 2848 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2747 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2626 |
| 11 | La Aurora Airport |  | GT | 2621 |
| 12 | Salt Lake City International Airport |  | US | 2443 |
| 13 | Congonhas Airport |  | BR | 2346 |
| 14 | Chicago O'Hare International Airport |  | US | 2324 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2248 |
| 16 | Capua Airport |  | IT | 2133 |
| 17 | Madrid Barajas International Airport |  | ES | 2114 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2092 |
| 19 | Frankfurt am Main International Airport |  | DE | 2067 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1949 |
| 22 | Charles de Gaulle International Airport |  | FR | 1945 |
| 23 | Malpensa International Airport |  | IT | 1943 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1837 |
| 26 | Macau International Airport |  | MO | 1790 |
| 27 | Ninoy Aquino International Airport |  | PH | 1783 |
| 28 | Charlotte/Douglas International Airport |  | US | 1716 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1708 |
| 30 | Barcelona International Airport |  | ES | 1696 |
| 31 | Viracopos International Airport |  | BR | 1645 |
| 32 | Kuala Lumpur International Airport |  | MY | 1635 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1615 |
| 34 | Seattle-Tacoma International Airport |  | US | 1610 |
| 35 | Calgary International Airport |  | CA | 1561 |
| 36 | Don Mueang International Airport |  | TH | 1551 |
| 37 | Oslo Gardermoen Airport |  | NO | 1542 |
| 38 | Vancouver International Airport |  | CA | 1540 |
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
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 608 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 434 | 1h 50m | 1,423 km | 10,651.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 393 | 24m | 218 km | 1,480.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 348 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 344 | 1h 6m | 706 km | 4,188.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 320 | 19m | 144 km | 796.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 316 | 18m | 14 km | 79.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 307 | 42m | 535 km | 2,835.3 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 297 | 1h 50m | 1,304 km | 6,681.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR168 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-10-02 19:43 UTC | 2026-10-02 19:57 UTC | 13m |
| N381U |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-10-02 18:42 UTC | 2026-10-02 19:44 UTC | 1h 2m |
| VAR485 | VAR | 29AZ (29AZ) | Phoenix Goodyear Airport (KGYR) | 2026-10-02 19:15 UTC | 2026-10-02 19:44 UTC | 28m |
| N619SM |  | Cedar Creek Ranch Airport (25AR) | Jonesboro Municipal Airport (KJBR) | 2026-10-02 19:20 UTC | 2026-10-02 19:43 UTC | 23m |
| N187D |  | St George Regional Airport (KSGU) | Colorado City Municipal Airport (KAZC) | 2026-10-02 19:07 UTC | 2026-10-02 19:41 UTC | 33m |
| DHK035 | DHK | Bahrain International Airport (OBBI) | Brussels Airport (EBBR) | 2026-10-02 13:18 UTC | 2026-10-02 19:38 UTC | 6h 19m |
| FILL31 | FIL | Enid Woodring Regional Airport (KWDG) | 6OK0 (6OK0) | 2026-10-02 19:16 UTC | 2026-10-02 19:32 UTC | 15m |
| N31GE |  | Centennial Airport (KAPA) | Salida/Harriett Alexander Field (KANK) | 2026-10-02 18:29 UTC | 2026-10-02 19:31 UTC | 1h 2m |
| SCU5 | SCU | William R Pogue Municipal Airport (KOWP) | Barcus Field (95OK) | 2026-10-02 19:17 UTC | 2026-10-02 19:30 UTC | 13m |
| JTL717 | JTL | K4I7 (K4I7) | Rocky Mountain Metro Airport (KBJC) | 2026-10-02 16:54 UTC | 2026-10-02 19:30 UTC | 2h 36m |
| N407SK |  | 1CA1 (1CA1) | 1CA1 (1CA1) | 2026-10-02 17:58 UTC | 2026-10-02 19:29 UTC | 1h 31m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-02 19:18 UTC | 2026-10-02 19:28 UTC | 10m |
| N996RP |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-10-02 18:08 UTC | 2026-10-02 19:28 UTC | 1h 20m |
| FONCF | FON | Faa'a International Airport (NTAA) | Moorea Airport (NTTM) | 2026-10-02 19:17 UTC | 2026-10-02 19:27 UTC | 10m |
| CNS2412 | CNS | Cape Cod Gateway Airport (KHYA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-10-02 18:59 UTC | 2026-10-02 19:27 UTC | 28m |
| N172WF |  | Waukegan Ntl Airport (KUGN) | Burlington Municipal Airport (KBUU) | 2026-10-02 18:45 UTC | 2026-10-02 19:25 UTC | 40m |
| N713BB |  | Rochester International Airport (KRST) | Joe Foss Field (KFSD) | 2026-10-02 18:38 UTC | 2026-10-02 19:24 UTC | 46m |
| N52853 |  | Madras Municipal Airport (KS33) | Madras Municipal Airport (KS33) | 2026-10-02 19:22 UTC | 2026-10-02 19:23 UTC | 0m |
| N486TT |  | General Downing - Peoria International Airport (KPIA) | Auburn University Regional Airport (KAUO) | 2026-10-02 17:57 UTC | 2026-10-02 19:21 UTC | 1h 24m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-10-02 19:09 UTC | 2026-10-02 19:20 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
