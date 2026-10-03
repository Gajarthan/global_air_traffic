# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_19:51:50_UTC-green)

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

**Latest saved flight:** 2026-10-03 19:51:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-03 19:51:50 UTC

- **275,668** saved flights
- **80,271** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,668** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,335,696.5 tonnes** estimated CO2 emissions
- **193,373,712 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10807 |
| 2 | SkyWest Airlines | 9592 |
| 3 | EJA | 5402 |
| 4 | IndiGo | 4594 |
| 5 | American Airlines | 4267 |
| 6 | Southwest Airlines | 4048 |
| 7 | Delta Air Lines | 3425 |
| 8 | ENY | 3223 |
| 9 | LATAM Airlines | 2669 |
| 10 | AZU | 2592 |
| 11 | Vueling | 2285 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2180 |
| 14 | Lufthansa | 2074 |
| 15 | easyJet | 1833 |
| 16 | Swiss International | 1805 |
| 17 | QLK | 1775 |
| 18 | EJU | 1713 |
| 19 | AXM | 1689 |
| 20 | United Airlines | 1680 |
| 21 | Alaska Airlines | 1624 |
| 22 | All Nippon Airways | 1572 |
| 23 | PGT | 1551 |
| 24 | GLO | 1540 |
| 25 | WMT | 1534 |
| 26 | VIV | 1512 |
| 27 | Air France | 1511 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1361 |
| 30 | AEE | 1311 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230035 |
| 2 | 🇪🇸 ES | 17243 |
| 3 | 🇧🇷 BR | 16186 |
| 4 | 🇦🇺 AU | 15884 |
| 5 | 🇨🇦 CA | 15358 |
| 6 | 🇮🇹 IT | 14857 |
| 7 | 🇮🇳 IN | 14536 |
| 8 | 🇩🇪 DE | 13176 |
| 9 | 🇨🇴 CO | 12797 |
| 10 | 🇬🇧 GB | 12695 |
| 11 | 🇫🇷 FR | 10895 |
| 12 | 🇯🇵 JP | 10502 |
| 13 | 🇹🇷 TR | 8330 |
| 14 | 🇬🇷 GR | 7908 |
| 15 | 🇲🇽 MX | 7617 |
| 16 | 🇨🇭 CH | 7324 |
| 17 | 🇳🇴 NO | 6799 |
| 18 | 🇹🇭 TH | 4936 |
| 19 | 🇲🇾 MY | 4575 |
| 20 | 🇿🇦 ZA | 4562 |
| 21 | 🇵🇱 PL | 4502 |
| 22 | 🇳🇿 NZ | 3907 |
| 23 | 🇵🇭 PH | 3638 |
| 24 | 🇬🇹 GT | 3462 |
| 25 | 🇭🇷 HR | 3137 |
| 26 | 🇰🇷 KR | 3101 |
| 27 | 🇲🇦 MA | 2721 |
| 28 | 🇲🇪 ME | 2587 |
| 29 | 🇳🇱 NL | 2462 |
| 30 | 🇮🇩 ID | 2279 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5593 |
| 2 | Denver International Airport |  | US | 4500 |
| 3 | Indira Gandhi International Airport |  | IN | 3284 |
| 4 | Tokyo International Airport |  | JP | 3149 |
| 5 | El Dorado International Airport |  | CO | 3057 |
| 6 | Harry Reid International Airport |  | US | 2970 |
| 7 | Zurich Airport |  | CH | 2864 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2753 |
| 10 | La Aurora Airport |  | GT | 2634 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2630 |
| 12 | Salt Lake City International Airport |  | US | 2453 |
| 13 | Congonhas Airport |  | BR | 2355 |
| 14 | Chicago O'Hare International Airport |  | US | 2327 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2256 |
| 16 | Capua Airport |  | IT | 2141 |
| 17 | Madrid Barajas International Airport |  | ES | 2123 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2103 |
| 19 | Frankfurt am Main International Airport |  | DE | 2071 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1954 |
| 22 | Malpensa International Airport |  | IT | 1949 |
| 23 | Charles de Gaulle International Airport |  | FR | 1948 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1840 |
| 26 | Macau International Airport |  | MO | 1793 |
| 27 | Ninoy Aquino International Airport |  | PH | 1789 |
| 28 | Charlotte/Douglas International Airport |  | US | 1721 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1714 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1651 |
| 32 | Kuala Lumpur International Airport |  | MY | 1639 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1620 |
| 34 | Seattle-Tacoma International Airport |  | US | 1617 |
| 35 | Calgary International Airport |  | CA | 1565 |
| 36 | Don Mueang International Airport |  | TH | 1557 |
| 37 | Oslo Gardermoen Airport |  | NO | 1545 |
| 38 | Vancouver International Airport |  | CA | 1544 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1040 | 21m | 244 km | 4,379.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 696 | 1h 6m | 770 km | 9,245.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 694 | 24m | 225 km | 2,692.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 435 | 1h 50m | 1,423 km | 10,675.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 394 | 24m | 218 km | 1,484.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 374 | 23m | 55 km | 355.5 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 351 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 347 | 1h 6m | 706 km | 4,224.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 321 | 19m | 144 km | 798.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 318 | 18m | 14 km | 79.5 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SCU6 | SCU | Pheasant Wings Airport (26OK) | Gregg Airport (7OK1) | 2026-10-03 19:40 UTC | 2026-10-03 19:51 UTC | 11m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-10-03 19:30 UTC | 2026-10-03 19:50 UTC | 19m |
| N840JA |  | Grant County International Airport (KMWH) | Ephrata Municipal Airport (KEPH) | 2026-10-03 19:42 UTC | 2026-10-03 19:47 UTC | 5m |
| N715ML |  | San Carlos Airport (KSQL) | Santa Barbara Municipal Airport (KSBA) | 2026-10-03 17:44 UTC | 2026-10-03 19:47 UTC | 2h 3m |
| TVF864L | TVF | Paris-Orly Airport (LFPO) | Tit Mellil Airport (GMMT) | 2026-10-03 17:19 UTC | 2026-10-03 19:47 UTC | 2h 28m |
| N717AF |  | Palo Alto Airport (KPAO) | Mineta San Jose International Airport (KSJC) | 2026-10-03 19:35 UTC | 2026-10-03 19:46 UTC | 11m |
| 52248 |  | Gwinnett County/Briscoe Field (KLZU) | Cy Nunnally Memorial Airport (KD73) | 2026-10-03 18:55 UTC | 2026-10-03 19:46 UTC | 50m |
| N414UH |  | Bolinder Field/Tooele Valley Airport (KTVY) | K36U (K36U) | 2026-10-03 19:00 UTC | 2026-10-03 19:42 UTC | 42m |
| CXK1020 | CXK | Centennial Airport (KAPA) | Colorado Plains Regional Airport (KAKO) | 2026-10-03 18:46 UTC | 2026-10-03 19:38 UTC | 52m |
| N741CD |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-10-03 19:13 UTC | 2026-10-03 19:37 UTC | 23m |
| N54983 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-10-03 18:45 UTC | 2026-10-03 19:34 UTC | 49m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-10-03 19:19 UTC | 2026-10-03 19:32 UTC | 12m |
| N386CK |  | Centennial Airport (KAPA) | Hopkins Field (KAIB) | 2026-10-03 18:13 UTC | 2026-10-03 19:27 UTC | 1h 13m |
| N9849C |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-10-03 18:59 UTC | 2026-10-03 19:24 UTC | 25m |
| N703MS |  | Dekalb-Peachtree Airport (KPDK) | Southwest Georgia Regional Airport (KABY) | 2026-10-03 18:45 UTC | 2026-10-03 19:20 UTC | 35m |
| LXJ602 | LXJ | Monterey Regional Airport (KMRY) | Van Nuys Airport (KVNY) | 2026-10-03 18:35 UTC | 2026-10-03 19:18 UTC | 42m |
| N814SS |  | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-10-03 19:07 UTC | 2026-10-03 19:17 UTC | 10m |
| N600UH |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Fernando Luis Ribas Dominicci Airport (TJIG) | 2026-10-03 18:36 UTC | 2026-10-03 19:17 UTC | 41m |
| RYR45KP | Ryanair | London Gatwick Airport (EGKK) | Dublin Airport (EIDW) | 2026-10-03 18:24 UTC | 2026-10-03 19:15 UTC | 51m |
| N504KH |  | Strayhorn Ranch Airport (47FD) | Smith Airport (43KS) | 2026-10-03 16:32 UTC | 2026-10-03 19:14 UTC | 2h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
