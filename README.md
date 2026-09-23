# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_22:53:36_UTC-green)

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

**Latest saved flight:** 2026-09-23 22:53:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 22:53:36 UTC

- **267,743** saved flights
- **78,645** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,743** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,247,189.1 tonnes** estimated CO2 emissions
- **188,242,849 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10569 |
| 2 | SkyWest Airlines | 9317 |
| 3 | EJA | 5208 |
| 4 | IndiGo | 4486 |
| 5 | American Airlines | 4170 |
| 6 | Southwest Airlines | 3934 |
| 7 | Delta Air Lines | 3332 |
| 8 | ENY | 3148 |
| 9 | LATAM Airlines | 2581 |
| 10 | AZU | 2511 |
| 11 | Vueling | 2240 |
| 12 | WIF | 2172 |
| 13 | LXJ | 2103 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1798 |
| 16 | Swiss International | 1759 |
| 17 | QLK | 1722 |
| 18 | EJU | 1685 |
| 19 | AXM | 1671 |
| 20 | United Airlines | 1642 |
| 21 | Alaska Airlines | 1582 |
| 22 | All Nippon Airways | 1542 |
| 23 | PGT | 1508 |
| 24 | WMT | 1500 |
| 25 | GLO | 1494 |
| 26 | Air France | 1470 |
| 27 | VIV | 1462 |
| 28 | Wizz Air | 1454 |
| 29 | CXK | 1309 |
| 30 | AEE | 1287 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222706 |
| 2 | 🇪🇸 ES | 16806 |
| 3 | 🇧🇷 BR | 15659 |
| 4 | 🇦🇺 AU | 15370 |
| 5 | 🇨🇦 CA | 14928 |
| 6 | 🇮🇹 IT | 14527 |
| 7 | 🇮🇳 IN | 14191 |
| 8 | 🇩🇪 DE | 12880 |
| 9 | 🇬🇧 GB | 12415 |
| 10 | 🇨🇴 CO | 12247 |
| 11 | 🇫🇷 FR | 10663 |
| 12 | 🇯🇵 JP | 10303 |
| 13 | 🇹🇷 TR | 8111 |
| 14 | 🇬🇷 GR | 7741 |
| 15 | 🇲🇽 MX | 7381 |
| 16 | 🇨🇭 CH | 7134 |
| 17 | 🇳🇴 NO | 6625 |
| 18 | 🇹🇭 TH | 4792 |
| 19 | 🇲🇾 MY | 4506 |
| 20 | 🇿🇦 ZA | 4482 |
| 21 | 🇵🇱 PL | 4392 |
| 22 | 🇳🇿 NZ | 3732 |
| 23 | 🇵🇭 PH | 3550 |
| 24 | 🇬🇹 GT | 3392 |
| 25 | 🇭🇷 HR | 3054 |
| 26 | 🇰🇷 KR | 3033 |
| 27 | 🇲🇦 MA | 2672 |
| 28 | 🇲🇪 ME | 2510 |
| 29 | 🇳🇱 NL | 2399 |
| 30 | 🇮🇩 ID | 2230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5458 |
| 2 | Denver International Airport |  | US | 4349 |
| 3 | Indira Gandhi International Airport |  | IN | 3211 |
| 4 | Tokyo International Airport |  | JP | 3083 |
| 5 | El Dorado International Airport |  | CO | 2891 |
| 6 | Harry Reid International Airport |  | US | 2861 |
| 7 | Guaymaral Airport |  | CO | 2805 |
| 8 | Zurich Airport |  | CH | 2780 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2689 |
| 10 | La Aurora Airport |  | GT | 2578 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2577 |
| 12 | Salt Lake City International Airport |  | US | 2360 |
| 13 | Chicago O'Hare International Airport |  | US | 2295 |
| 14 | Congonhas Airport |  | BR | 2281 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2188 |
| 16 | Capua Airport |  | IT | 2086 |
| 17 | Madrid Barajas International Airport |  | ES | 2061 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2027 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1912 |
| 22 | Charles de Gaulle International Airport |  | FR | 1898 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1881 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1874 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1779 |
| 27 | Ninoy Aquino International Airport |  | PH | 1742 |
| 28 | Charlotte/Douglas International Airport |  | US | 1672 |
| 29 | Barcelona International Airport |  | ES | 1665 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1620 |
| 32 | Kuala Lumpur International Airport |  | MY | 1614 |
| 33 | Seattle-Tacoma International Airport |  | US | 1570 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1564 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1517 |
| 37 | Bengaluru International Airport |  | IN | 1511 |
| 38 | Oslo Gardermoen Airport |  | NO | 1506 |
| 39 | Vancouver International Airport |  | CA | 1499 |
| 40 | Antalya International Airport |  | TR | 1429 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1003 | 21m | 244 km | 4,223.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 674 | 1h 6m | 770 km | 8,953.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 596 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 428 | 27m | 275 km | 2,028.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 409 | 44m | 241 km | 1,698.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 363 | 21m | 250 km | 1,567.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 357 | 23m | 55 km | 339.3 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 339 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 285 | 18m | 14 km | 71.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FURY79 | FUR | Bradley International Airport (KBDL) | Westover Arb/Metro Airport (KCEF) | 2026-09-23 22:20 UTC | 2026-09-23 22:53 UTC | 33m |
| TUP9625 | TUP | Sheremetyevo International Airport (UUEE) | Staroselye Airport (UUBK) | 2026-09-23 22:26 UTC | 2026-09-23 22:49 UTC | 22m |
| MFX7631 | MFX | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-23 18:02 UTC | 2026-09-23 22:48 UTC | 4h 45m |
| N4337V |  | Crystal Airport (KMIC) | Crystal Airport (KMIC) | 2026-09-23 21:23 UTC | 2026-09-23 22:40 UTC | 1h 16m |
| N951RP |  | Riverside Airport (KRAL) | Hemet-Ryan Airport (KHMT) | 2026-09-23 22:25 UTC | 2026-09-23 22:39 UTC | 14m |
| N540M |  | Eugene F Kranz Toledo Express Airport (KTOL) | South Bend International Airport (KSBN) | 2026-09-23 22:17 UTC | 2026-09-23 22:38 UTC | 21m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-09-23 12:07 UTC | 2026-09-23 22:36 UTC | 10h 28m |
| CUL558 | CUL | Cecil Ranch Airport (37CN) | 6CL4 (6CL4) | 2026-09-23 21:47 UTC | 2026-09-23 22:35 UTC | 47m |
| LAE2538 | LAE | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-09-23 22:22 UTC | 2026-09-23 22:34 UTC | 12m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-23 21:58 UTC | 2026-09-23 22:31 UTC | 33m |
| N225TF |  | Corona Municipal Airport (KAJO) | Ramona Airport (KRNM) | 2026-09-23 21:50 UTC | 2026-09-23 22:31 UTC | 40m |
| N6574G |  | Fort Worth Meacham International Airport (KFTW) | Bridgeport Municipal Airport (KXBP) | 2026-09-23 21:45 UTC | 2026-09-23 22:24 UTC | 38m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-09-23 10:45 UTC | 2026-09-23 22:21 UTC | 11h 36m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-23 21:35 UTC | 2026-09-23 22:18 UTC | 43m |
| N84050 |  | Homer Airport (PAHO) | Homer Airport (PAHO) | 2026-09-23 21:35 UTC | 2026-09-23 22:17 UTC | 41m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-23 21:47 UTC | 2026-09-23 22:16 UTC | 28m |
| CXK1031 | CXK | Fayette Regional Air Center Airport (K3T5) | Fayette Regional Air Center Airport (K3T5) | 2026-09-23 22:00 UTC | 2026-09-23 22:14 UTC | 13m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-09-23 10:35 UTC | 2026-09-23 22:14 UTC | 11h 38m |
| N19DL |  | Centennial Airport (KAPA) | Addison-Henley Field (0MS7) | 2026-09-23 19:38 UTC | 2026-09-23 22:13 UTC | 2h 35m |
| N407P |  | Flying C Airport (XS25) | Houston/Southwest Airport (KAXH) | 2026-09-23 21:49 UTC | 2026-09-23 22:12 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
