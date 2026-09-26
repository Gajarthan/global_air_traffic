# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_16:16:43_UTC-green)

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

**Latest saved flight:** 2026-09-26 16:16:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-26 16:16:43 UTC

- **270,134** saved flights
- **79,153** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,134** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,276,809.8 tonnes** estimated CO2 emissions
- **189,959,989 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10631 |
| 2 | SkyWest Airlines | 9396 |
| 3 | EJA | 5274 |
| 4 | IndiGo | 4525 |
| 5 | American Airlines | 4196 |
| 6 | Southwest Airlines | 3971 |
| 7 | Delta Air Lines | 3358 |
| 8 | ENY | 3173 |
| 9 | LATAM Airlines | 2602 |
| 10 | AZU | 2532 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2198 |
| 13 | LXJ | 2121 |
| 14 | Lufthansa | 2053 |
| 15 | easyJet | 1810 |
| 16 | Swiss International | 1770 |
| 17 | QLK | 1738 |
| 18 | EJU | 1693 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1653 |
| 21 | Alaska Airlines | 1593 |
| 22 | All Nippon Airways | 1553 |
| 23 | PGT | 1522 |
| 24 | WMT | 1509 |
| 25 | GLO | 1504 |
| 26 | Air France | 1485 |
| 27 | VIV | 1471 |
| 28 | Wizz Air | 1469 |
| 29 | CXK | 1325 |
| 30 | AEE | 1295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224917 |
| 2 | 🇪🇸 ES | 16935 |
| 3 | 🇧🇷 BR | 15795 |
| 4 | 🇦🇺 AU | 15527 |
| 5 | 🇨🇦 CA | 15060 |
| 6 | 🇮🇹 IT | 14609 |
| 7 | 🇮🇳 IN | 14317 |
| 8 | 🇩🇪 DE | 12970 |
| 9 | 🇬🇧 GB | 12503 |
| 10 | 🇨🇴 CO | 12389 |
| 11 | 🇫🇷 FR | 10740 |
| 12 | 🇯🇵 JP | 10372 |
| 13 | 🇹🇷 TR | 8180 |
| 14 | 🇬🇷 GR | 7796 |
| 15 | 🇲🇽 MX | 7448 |
| 16 | 🇨🇭 CH | 7186 |
| 17 | 🇳🇴 NO | 6681 |
| 18 | 🇹🇭 TH | 4829 |
| 19 | 🇲🇾 MY | 4531 |
| 20 | 🇿🇦 ZA | 4516 |
| 21 | 🇵🇱 PL | 4428 |
| 22 | 🇳🇿 NZ | 3785 |
| 23 | 🇵🇭 PH | 3582 |
| 24 | 🇬🇹 GT | 3418 |
| 25 | 🇭🇷 HR | 3082 |
| 26 | 🇰🇷 KR | 3051 |
| 27 | 🇲🇦 MA | 2685 |
| 28 | 🇲🇪 ME | 2535 |
| 29 | 🇳🇱 NL | 2414 |
| 30 | 🇮🇩 ID | 2251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5497 |
| 2 | Denver International Airport |  | US | 4394 |
| 3 | Indira Gandhi International Airport |  | IN | 3237 |
| 4 | Tokyo International Airport |  | JP | 3105 |
| 5 | El Dorado International Airport |  | CO | 2935 |
| 6 | Harry Reid International Airport |  | US | 2896 |
| 7 | Guaymaral Airport |  | CO | 2817 |
| 8 | Zurich Airport |  | CH | 2800 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2715 |
| 10 | La Aurora Airport |  | GT | 2598 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2597 |
| 12 | Salt Lake City International Airport |  | US | 2381 |
| 13 | Chicago O'Hare International Airport |  | US | 2307 |
| 14 | Congonhas Airport |  | BR | 2303 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2209 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2082 |
| 18 | Frankfurt am Main International Airport |  | DE | 2047 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2042 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1918 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1898 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1888 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1758 |
| 28 | Charlotte/Douglas International Airport |  | US | 1689 |
| 29 | Barcelona International Airport |  | ES | 1680 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1673 |
| 31 | Viracopos International Airport |  | BR | 1630 |
| 32 | Kuala Lumpur International Airport |  | MY | 1623 |
| 33 | Seattle-Tacoma International Airport |  | US | 1582 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1579 |
| 35 | Calgary International Airport |  | CA | 1538 |
| 36 | Don Mueang International Airport |  | TH | 1528 |
| 37 | Bengaluru International Airport |  | IN | 1523 |
| 38 | Oslo Gardermoen Airport |  | NO | 1514 |
| 39 | Vancouver International Airport |  | CA | 1510 |
| 40 | Antalya International Airport |  | TR | 1441 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1122 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1011 | 21m | 244 km | 4,257.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 747 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 682 | 1h 6m | 770 km | 9,059.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 676 | 24m | 225 km | 2,622.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 601 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 446 | 44m | 555 km | 4,270.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 434 | 27m | 275 km | 2,056.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 412 | 44m | 241 km | 1,711.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 386 | 24m | 218 km | 1,454.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 363 | 23m | 55 km | 345.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 345 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 340 | 19m | 99 km | 582.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 305 | 1h 14m | 961 km | 5,055.5 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 298 | 42m | 535 km | 2,752.2 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 293 | 18m | 14 km | 73.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N365C |  | Orlando North Airpark (FA83) | FA46 (FA46) | 2026-09-26 15:25 UTC | 2026-09-26 16:16 UTC | 50m |
| N708JA |  | Indianapolis Regional Airport (KMQJ) | Indianapolis Regional Airport (KMQJ) | 2026-09-26 15:14 UTC | 2026-09-26 16:16 UTC | 1h 1m |
| N909SR |  | Visalia Municipal Airport (KVIS) | San Luis Obispo County Regional Airport (KSBP) | 2026-09-26 15:39 UTC | 2026-09-26 16:13 UTC | 34m |
| N125PM |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-09-26 14:40 UTC | 2026-09-26 16:12 UTC | 1h 32m |
| N132TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-26 15:49 UTC | 2026-09-26 16:09 UTC | 19m |
| MS4 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-09-26 15:03 UTC | 2026-09-26 16:08 UTC | 1h 5m |
| N7485G |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | Athens Municipal Airport (KF44) | 2026-09-26 15:31 UTC | 2026-09-26 16:06 UTC | 34m |
| TRF552 | TRF | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-09-26 14:57 UTC | 2026-09-26 16:06 UTC | 1h 8m |
| N6490X |  | Wexford County Airport (KCAD) | Greenville Municipal Airport (K6D6) | 2026-09-26 15:21 UTC | 2026-09-26 16:02 UTC | 40m |
| N486BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-09-26 15:07 UTC | 2026-09-26 16:02 UTC | 54m |
| XAEFA | XAE | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-09-26 15:16 UTC | 2026-09-26 16:00 UTC | 44m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-09-26 15:46 UTC | 2026-09-26 16:00 UTC | 14m |
| N402AA |  | Sacramento Mather Airport (KMHR) | Tracy Municipal Airport (KTCY) | 2026-09-26 15:12 UTC | 2026-09-26 15:57 UTC | 44m |
| UAE9863 | Emirates | Chek Lap Kok International Airport (VHHH) | Chanmyathazi Airport (VYCZ) | 2026-09-26 13:39 UTC | 2026-09-26 15:57 UTC | 2h 17m |
| N9571H |  | 0TS2 (0TS2) | Bridgeport Municipal Airport (KXBP) | 2026-09-26 15:24 UTC | 2026-09-26 15:56 UTC | 31m |
| N105RF |  | Provo Municipal Airport (KPVU) | Goldys Field (CO47) | 2026-09-26 14:25 UTC | 2026-09-26 15:52 UTC | 1h 27m |
|  |  | Tres Marias Airport (SDWL) | Fazenda Real Airport (SIZQ) | 2026-09-26 15:32 UTC | 2026-09-26 15:48 UTC | 16m |
| N606LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-26 15:34 UTC | 2026-09-26 15:46 UTC | 11m |
| N1293E |  | Airglades Airport (K2IS) | Airglades Airport (K2IS) | 2026-09-26 15:39 UTC | 2026-09-26 15:45 UTC | 6m |
| SIA446 | Singapore Airlines | Singapore Changi International Airport (WSSS) | Naypyidaw Airport (VYEL) | 2026-09-26 13:03 UTC | 2026-09-26 15:43 UTC | 2h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
