# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_08:38:57_UTC-green)

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

**Latest saved flight:** 2026-10-02 08:38:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-02 08:38:57 UTC

- **274,403** saved flights
- **80,025** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,403** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,321,434.5 tonnes** estimated CO2 emissions
- **192,546,929 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10768 |
| 2 | SkyWest Airlines | 9544 |
| 3 | EJA | 5372 |
| 4 | IndiGo | 4572 |
| 5 | American Airlines | 4252 |
| 6 | Southwest Airlines | 4033 |
| 7 | Delta Air Lines | 3404 |
| 8 | ENY | 3212 |
| 9 | LATAM Airlines | 2651 |
| 10 | AZU | 2581 |
| 11 | Vueling | 2276 |
| 12 | WIF | 2234 |
| 13 | LXJ | 2164 |
| 14 | Lufthansa | 2068 |
| 15 | easyJet | 1824 |
| 16 | Swiss International | 1798 |
| 17 | QLK | 1774 |
| 18 | EJU | 1709 |
| 19 | AXM | 1688 |
| 20 | United Airlines | 1675 |
| 21 | Alaska Airlines | 1616 |
| 22 | All Nippon Airways | 1569 |
| 23 | PGT | 1544 |
| 24 | GLO | 1533 |
| 25 | WMT | 1530 |
| 26 | Air France | 1507 |
| 27 | VIV | 1504 |
| 28 | Wizz Air | 1485 |
| 29 | CXK | 1355 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228821 |
| 2 | 🇪🇸 ES | 17155 |
| 3 | 🇧🇷 BR | 16110 |
| 4 | 🇦🇺 AU | 15861 |
| 5 | 🇨🇦 CA | 15304 |
| 6 | 🇮🇹 IT | 14798 |
| 7 | 🇮🇳 IN | 14471 |
| 8 | 🇩🇪 DE | 13141 |
| 9 | 🇨🇴 CO | 12711 |
| 10 | 🇬🇧 GB | 12637 |
| 11 | 🇫🇷 FR | 10861 |
| 12 | 🇯🇵 JP | 10480 |
| 13 | 🇹🇷 TR | 8295 |
| 14 | 🇬🇷 GR | 7890 |
| 15 | 🇲🇽 MX | 7581 |
| 16 | 🇨🇭 CH | 7285 |
| 17 | 🇳🇴 NO | 6771 |
| 18 | 🇹🇭 TH | 4915 |
| 19 | 🇲🇾 MY | 4569 |
| 20 | 🇿🇦 ZA | 4555 |
| 21 | 🇵🇱 PL | 4476 |
| 22 | 🇳🇿 NZ | 3883 |
| 23 | 🇵🇭 PH | 3626 |
| 24 | 🇬🇹 GT | 3438 |
| 25 | 🇭🇷 HR | 3123 |
| 26 | 🇰🇷 KR | 3092 |
| 27 | 🇲🇦 MA | 2712 |
| 28 | 🇲🇪 ME | 2574 |
| 29 | 🇳🇱 NL | 2456 |
| 30 | 🇮🇩 ID | 2272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5571 |
| 2 | Denver International Airport |  | US | 4475 |
| 3 | Indira Gandhi International Airport |  | IN | 3275 |
| 4 | Tokyo International Airport |  | JP | 3141 |
| 5 | El Dorado International Airport |  | CO | 3024 |
| 6 | Harry Reid International Airport |  | US | 2952 |
| 7 | Zurich Airport |  | CH | 2848 |
| 8 | Guaymaral Airport |  | CO | 2845 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2743 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2625 |
| 11 | La Aurora Airport |  | GT | 2613 |
| 12 | Salt Lake City International Airport |  | US | 2436 |
| 13 | Congonhas Airport |  | BR | 2342 |
| 14 | Chicago O'Hare International Airport |  | US | 2322 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2246 |
| 16 | Capua Airport |  | IT | 2131 |
| 17 | Madrid Barajas International Airport |  | ES | 2111 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2086 |
| 19 | Frankfurt am Main International Airport |  | DE | 2066 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1946 |
| 22 | Malpensa International Airport |  | IT | 1943 |
| 23 | Charles de Gaulle International Airport |  | FR | 1943 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1834 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1782 |
| 28 | Charlotte/Douglas International Airport |  | US | 1715 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1702 |
| 30 | Barcelona International Airport |  | ES | 1694 |
| 31 | Viracopos International Airport |  | BR | 1644 |
| 32 | Kuala Lumpur International Airport |  | MY | 1635 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1614 |
| 34 | Seattle-Tacoma International Airport |  | US | 1608 |
| 35 | Calgary International Airport |  | CA | 1560 |
| 36 | Don Mueang International Airport |  | TH | 1551 |
| 37 | Vancouver International Airport |  | CA | 1538 |
| 38 | Oslo Gardermoen Airport |  | NO | 1537 |
| 39 | Bengaluru International Airport |  | IN | 1534 |
| 40 | Reno/Tahoe International Airport |  | US | 1487 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1132 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1032 | 21m | 244 km | 4,345.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 694 | 1h 6m | 770 km | 9,219.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 691 | 24m | 225 km | 2,680.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 605 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 442 | 27m | 275 km | 2,094.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 434 | 1h 50m | 1,423 km | 10,651.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 421 | 44m | 241 km | 1,748.7 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 352 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 344 | 1h 6m | 706 km | 4,188.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 343 | 19m | 99 km | 587.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 319 | 19m | 144 km | 793.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 314 | 18m | 14 km | 78.5 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 306 | 42m | 535 km | 2,826.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 296 | 1h 50m | 1,304 km | 6,659.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 273 | 51m | 556 km | 2,616.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-10-02 08:23 UTC | 2026-10-02 08:38 UTC | 15m |
| CAL910 | CAL | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-10-02 07:11 UTC | 2026-10-02 08:33 UTC | 1h 22m |
| SVF680 | SVF | Malmen Air Base (ESCF) | Smolensk North Airport (XUBS) | 2026-10-02 07:00 UTC | 2026-10-02 08:31 UTC | 1h 31m |
| KNP973 | KNP | Incheon International Airport (RKSI) | Incheon International Airport (RKSI) | 2026-10-02 08:14 UTC | 2026-10-02 08:28 UTC | 14m |
| ABY532 | ABY | Sharjah International Airport (OMSJ) | Simara Airport (VNSI) | 2026-10-02 04:59 UTC | 2026-10-02 08:26 UTC | 3h 26m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-10-02 08:03 UTC | 2026-10-02 08:22 UTC | 18m |
| HBXTP | HBX | Wangen-Lachen Airport (LSPV) | Reichenbach Air Base (LSGR) | 2026-10-02 07:35 UTC | 2026-10-02 08:21 UTC | 46m |
| N125DG |  | Salt Lake City International Airport (KSLC) | Heiner Airport (WY60) | 2026-10-02 07:52 UTC | 2026-10-02 08:18 UTC | 25m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-10-02 07:51 UTC | 2026-10-02 08:04 UTC | 13m |
| CLX4164 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-10-01 21:07 UTC | 2026-10-02 08:03 UTC | 10h 55m |
| UAE9852 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-10-02 00:41 UTC | 2026-10-02 07:55 UTC | 7h 14m |
| WMT5604 | WMT | Memmingen Allgau Airport (EDJA) | Sibiu International Airport (LRSB) | 2026-10-02 06:23 UTC | 2026-10-02 07:52 UTC | 1h 29m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-10-01 20:45 UTC | 2026-10-02 07:52 UTC | 11h 6m |
| FGIBV | FGI | Ghisonaccia Alzitone Airport (LFKG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-10-02 07:24 UTC | 2026-10-02 07:51 UTC | 26m |
| THY70 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-10-01 22:44 UTC | 2026-10-02 07:50 UTC | 9h 6m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Kristiansand Airport (ENCN) | 2026-10-02 07:16 UTC | 2026-10-02 07:49 UTC | 33m |
| N153AE |  | Double Eagle Ii Airport (KAEG) | NM74 (NM74) | 2026-10-02 07:28 UTC | 2026-10-02 07:48 UTC | 20m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-10-02 07:22 UTC | 2026-10-02 07:48 UTC | 26m |
| AAR713 | AAR | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-10-02 05:46 UTC | 2026-10-02 07:48 UTC | 2h 1m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-10-02 07:41 UTC | 2026-10-02 07:48 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
