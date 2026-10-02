# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_15:23:47_UTC-green)

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

**Latest saved flight:** 2026-10-02 15:23:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-02 15:23:47 UTC

- **274,585** saved flights
- **80,059** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,585** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,323,387.5 tonnes** estimated CO2 emissions
- **192,660,145 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10778 |
| 2 | SkyWest Airlines | 9546 |
| 3 | EJA | 5377 |
| 4 | IndiGo | 4578 |
| 5 | American Airlines | 4252 |
| 6 | Southwest Airlines | 4033 |
| 7 | Delta Air Lines | 3407 |
| 8 | ENY | 3212 |
| 9 | LATAM Airlines | 2655 |
| 10 | AZU | 2583 |
| 11 | Vueling | 2277 |
| 12 | WIF | 2236 |
| 13 | LXJ | 2166 |
| 14 | Lufthansa | 2069 |
| 15 | easyJet | 1824 |
| 16 | Swiss International | 1798 |
| 17 | QLK | 1774 |
| 18 | EJU | 1710 |
| 19 | AXM | 1688 |
| 20 | United Airlines | 1675 |
| 21 | Alaska Airlines | 1616 |
| 22 | All Nippon Airways | 1569 |
| 23 | PGT | 1545 |
| 24 | GLO | 1534 |
| 25 | WMT | 1530 |
| 26 | Air France | 1508 |
| 27 | VIV | 1504 |
| 28 | Wizz Air | 1485 |
| 29 | CXK | 1356 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228966 |
| 2 | 🇪🇸 ES | 17170 |
| 3 | 🇧🇷 BR | 16121 |
| 4 | 🇦🇺 AU | 15861 |
| 5 | 🇨🇦 CA | 15313 |
| 6 | 🇮🇹 IT | 14809 |
| 7 | 🇮🇳 IN | 14486 |
| 8 | 🇩🇪 DE | 13153 |
| 9 | 🇨🇴 CO | 12722 |
| 10 | 🇬🇧 GB | 12645 |
| 11 | 🇫🇷 FR | 10867 |
| 12 | 🇯🇵 JP | 10481 |
| 13 | 🇹🇷 TR | 8304 |
| 14 | 🇬🇷 GR | 7892 |
| 15 | 🇲🇽 MX | 7584 |
| 16 | 🇨🇭 CH | 7289 |
| 17 | 🇳🇴 NO | 6779 |
| 18 | 🇹🇭 TH | 4917 |
| 19 | 🇲🇾 MY | 4569 |
| 20 | 🇿🇦 ZA | 4558 |
| 21 | 🇵🇱 PL | 4482 |
| 22 | 🇳🇿 NZ | 3883 |
| 23 | 🇵🇭 PH | 3627 |
| 24 | 🇬🇹 GT | 3446 |
| 25 | 🇭🇷 HR | 3125 |
| 26 | 🇰🇷 KR | 3093 |
| 27 | 🇲🇦 MA | 2713 |
| 28 | 🇲🇪 ME | 2574 |
| 29 | 🇳🇱 NL | 2457 |
| 30 | 🇮🇩 ID | 2272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5573 |
| 2 | Denver International Airport |  | US | 4476 |
| 3 | Indira Gandhi International Airport |  | IN | 3278 |
| 4 | Tokyo International Airport |  | JP | 3141 |
| 5 | El Dorado International Airport |  | CO | 3027 |
| 6 | Harry Reid International Airport |  | US | 2953 |
| 7 | Zurich Airport |  | CH | 2849 |
| 8 | Guaymaral Airport |  | CO | 2845 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2744 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2625 |
| 11 | La Aurora Airport |  | GT | 2619 |
| 12 | Salt Lake City International Airport |  | US | 2436 |
| 13 | Congonhas Airport |  | BR | 2344 |
| 14 | Chicago O'Hare International Airport |  | US | 2322 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2246 |
| 16 | Capua Airport |  | IT | 2133 |
| 17 | Madrid Barajas International Airport |  | ES | 2112 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2090 |
| 19 | Frankfurt am Main International Airport |  | DE | 2066 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1947 |
| 22 | Charles de Gaulle International Airport |  | FR | 1944 |
| 23 | Malpensa International Airport |  | IT | 1943 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1836 |
| 26 | Macau International Airport |  | MO | 1790 |
| 27 | Ninoy Aquino International Airport |  | PH | 1783 |
| 28 | Charlotte/Douglas International Airport |  | US | 1716 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1704 |
| 30 | Barcelona International Airport |  | ES | 1695 |
| 31 | Viracopos International Airport |  | BR | 1645 |
| 32 | Kuala Lumpur International Airport |  | MY | 1635 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1614 |
| 34 | Seattle-Tacoma International Airport |  | US | 1608 |
| 35 | Calgary International Airport |  | CA | 1560 |
| 36 | Don Mueang International Airport |  | TH | 1551 |
| 37 | Oslo Gardermoen Airport |  | NO | 1540 |
| 38 | Vancouver International Airport |  | CA | 1539 |
| 39 | Bengaluru International Airport |  | IN | 1535 |
| 40 | Reno/Tahoe International Airport |  | US | 1488 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1132 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1032 | 21m | 244 km | 4,345.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 694 | 1h 6m | 770 km | 9,219.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 691 | 24m | 225 km | 2,680.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 607 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 434 | 1h 50m | 1,423 km | 10,651.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 422 | 44m | 241 km | 1,752.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 352 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 344 | 1h 6m | 706 km | 4,188.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 319 | 19m | 144 km | 793.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 314 | 18m | 14 km | 78.5 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 307 | 42m | 535 km | 2,835.3 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 296 | 1h 50m | 1,304 km | 6,659.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N235CD |  | Iberlin Strip (WY23) | Iberlin Strip (WY23) | 2026-10-02 15:02 UTC | 2026-10-02 15:23 UTC | 21m |
| DMYGX | DMY | Wurzburg-Schenkenturm Airport (EDFW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-10-02 14:25 UTC | 2026-10-02 15:23 UTC | 58m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-10-02 14:59 UTC | 2026-10-02 15:21 UTC | 21m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-10-02 14:47 UTC | 2026-10-02 15:15 UTC | 28m |
| ABY401 | ABY | Sharjah International Airport (OMSJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-10-02 12:45 UTC | 2026-10-02 15:12 UTC | 2h 26m |
| AAR745 | AAR | Incheon International Airport (RKSI) | Chek Lap Kok International Airport (VHHH) | 2026-10-02 12:02 UTC | 2026-10-02 15:08 UTC | 3h 6m |
| XBOWB | XBO | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-10-02 14:03 UTC | 2026-10-02 15:05 UTC | 1h 2m |
| CXK660 | CXK | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-10-02 15:03 UTC | 2026-10-02 15:04 UTC | 1m |
| N118PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Kelso Valley Airport (CN37) | 2026-10-02 14:31 UTC | 2026-10-02 15:00 UTC | 29m |
| N5322A |  | Deland Municipal-Sidney H Taylor Field (KDED) | K1J6 (K1J6) | 2026-10-02 14:39 UTC | 2026-10-02 15:00 UTC | 20m |
| FIN7EN | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-10-02 14:04 UTC | 2026-10-02 14:57 UTC | 52m |
| CCA928 | Air China | Kansai International Airport (RJBB) | Savvatiya Air Base (ULKS) | 2026-10-01 05:12 UTC | 2026-10-02 14:57 UTC | 33h 45m |
| N9M |  | Provo Municipal Airport (KPVU) | Logan-Cache Airport (KLGU) | 2026-10-02 14:36 UTC | 2026-10-02 14:56 UTC | 19m |
| ZUJCG | ZUJ | Delta 200 Airstrip (FADX) | Fisantekraal Airport (FAFK) | 2026-10-02 14:50 UTC | 2026-10-02 14:55 UTC | 4m |
| JSY2M | JSY | Comiso Airport Vincenzo Magliocco (LICB) | Pavullo Airport (LIDP) | 2026-10-02 13:47 UTC | 2026-10-02 14:54 UTC | 1h 6m |
| APLO125 | APL | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Briercrest South Airport (CBS7) | 2026-10-02 14:18 UTC | 2026-10-02 14:54 UTC | 36m |
| FGIBV | FGI | Ghisonaccia Alzitone Airport (LFKG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-10-02 14:28 UTC | 2026-10-02 14:53 UTC | 25m |
| N228SB |  | Hugoton Municipal Airport (KHQG) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-10-02 14:13 UTC | 2026-10-02 14:51 UTC | 37m |
| N745JS |  | Mc Clellan-Palomar Airport (KCRQ) | Reno/Tahoe International Airport (KRNO) | 2026-10-02 13:41 UTC | 2026-10-02 14:51 UTC | 1h 9m |
| VPBTU | VPB | Harry Reid International Airport (KLAS) | Harvard Airport (CN23) | 2026-10-02 14:33 UTC | 2026-10-02 14:50 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
