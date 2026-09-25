# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_23:19:10_UTC-green)

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

**Latest saved flight:** 2026-09-25 23:19:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 23:19:10 UTC

- **269,603** saved flights
- **79,057** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,603** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,270,936.9 tonnes** estimated CO2 emissions
- **189,619,528 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10614 |
| 2 | SkyWest Airlines | 9381 |
| 3 | EJA | 5273 |
| 4 | IndiGo | 4513 |
| 5 | American Airlines | 4191 |
| 6 | Southwest Airlines | 3963 |
| 7 | Delta Air Lines | 3353 |
| 8 | ENY | 3168 |
| 9 | LATAM Airlines | 2600 |
| 10 | AZU | 2526 |
| 11 | Vueling | 2246 |
| 12 | WIF | 2196 |
| 13 | LXJ | 2118 |
| 14 | Lufthansa | 2047 |
| 15 | easyJet | 1808 |
| 16 | Swiss International | 1766 |
| 17 | QLK | 1736 |
| 18 | EJU | 1690 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1652 |
| 21 | Alaska Airlines | 1589 |
| 22 | All Nippon Airways | 1549 |
| 23 | PGT | 1516 |
| 24 | WMT | 1504 |
| 25 | GLO | 1502 |
| 26 | Air France | 1481 |
| 27 | VIV | 1468 |
| 28 | Wizz Air | 1464 |
| 29 | CXK | 1324 |
| 30 | AEE | 1294 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224555 |
| 2 | 🇪🇸 ES | 16896 |
| 3 | 🇧🇷 BR | 15768 |
| 4 | 🇦🇺 AU | 15496 |
| 5 | 🇨🇦 CA | 15040 |
| 6 | 🇮🇹 IT | 14591 |
| 7 | 🇮🇳 IN | 14267 |
| 8 | 🇩🇪 DE | 12930 |
| 9 | 🇬🇧 GB | 12478 |
| 10 | 🇨🇴 CO | 12357 |
| 11 | 🇫🇷 FR | 10719 |
| 12 | 🇯🇵 JP | 10350 |
| 13 | 🇹🇷 TR | 8160 |
| 14 | 🇬🇷 GR | 7786 |
| 15 | 🇲🇽 MX | 7436 |
| 16 | 🇨🇭 CH | 7159 |
| 17 | 🇳🇴 NO | 6672 |
| 18 | 🇹🇭 TH | 4816 |
| 19 | 🇲🇾 MY | 4527 |
| 20 | 🇿🇦 ZA | 4498 |
| 21 | 🇵🇱 PL | 4411 |
| 22 | 🇳🇿 NZ | 3774 |
| 23 | 🇵🇭 PH | 3571 |
| 24 | 🇬🇹 GT | 3412 |
| 25 | 🇭🇷 HR | 3070 |
| 26 | 🇰🇷 KR | 3046 |
| 27 | 🇲🇦 MA | 2683 |
| 28 | 🇲🇪 ME | 2526 |
| 29 | 🇳🇱 NL | 2406 |
| 30 | 🇮🇩 ID | 2241 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5490 |
| 2 | Denver International Airport |  | US | 4383 |
| 3 | Indira Gandhi International Airport |  | IN | 3226 |
| 4 | Tokyo International Airport |  | JP | 3096 |
| 5 | El Dorado International Airport |  | CO | 2923 |
| 6 | Harry Reid International Airport |  | US | 2894 |
| 7 | Guaymaral Airport |  | CO | 2815 |
| 8 | Zurich Airport |  | CH | 2793 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2711 |
| 10 | La Aurora Airport |  | GT | 2594 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2594 |
| 12 | Salt Lake City International Airport |  | US | 2376 |
| 13 | Chicago O'Hare International Airport |  | US | 2305 |
| 14 | Congonhas Airport |  | BR | 2299 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2206 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2077 |
| 18 | Frankfurt am Main International Airport |  | DE | 2044 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2039 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1914 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1892 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1882 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1752 |
| 28 | Charlotte/Douglas International Airport |  | US | 1687 |
| 29 | Barcelona International Airport |  | ES | 1677 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1670 |
| 31 | Viracopos International Airport |  | BR | 1628 |
| 32 | Kuala Lumpur International Airport |  | MY | 1621 |
| 33 | Seattle-Tacoma International Airport |  | US | 1580 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1578 |
| 35 | Calgary International Airport |  | CA | 1538 |
| 36 | Don Mueang International Airport |  | TH | 1525 |
| 37 | Bengaluru International Airport |  | IN | 1519 |
| 38 | Oslo Gardermoen Airport |  | NO | 1512 |
| 39 | Vancouver International Airport |  | CA | 1508 |
| 40 | Reno/Tahoe International Airport |  | US | 1438 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1009 | 21m | 244 km | 4,248.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 744 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 678 | 1h 6m | 770 km | 9,006.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 671 | 24m | 225 km | 2,603.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 600 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 444 | 44m | 555 km | 4,251.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 432 | 27m | 275 km | 2,047.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 426 | 1h 50m | 1,423 km | 10,454.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 411 | 44m | 241 km | 1,707.2 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 361 | 23m | 55 km | 343.1 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 344 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 295 | 42m | 535 km | 2,724.5 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 290 | 18m | 14 km | 72.5 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU23 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-09-25 22:58 UTC | 2026-09-25 23:19 UTC | 20m |
| N2354E |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-25 22:50 UTC | 2026-09-25 23:12 UTC | 22m |
| BEJ17S | BEJ | Rabat-Sale Airport (GMME) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-09-25 21:05 UTC | 2026-09-25 23:04 UTC | 1h 58m |
| EJC5430 | EJC | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-09-25 22:44 UTC | 2026-09-25 22:58 UTC | 13m |
| N579WA |  | Modesto City-County-Harry Sham Field (KMOD) | Sierraville Dearwater Airport (KO79) | 2026-09-25 22:27 UTC | 2026-09-25 22:56 UTC | 29m |
| CXK163 | CXK | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-09-25 22:51 UTC | 2026-09-25 22:54 UTC | 3m |
| BDIT21 | BDI | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Gravelbourg Airport (CJM4) | 2026-09-25 22:41 UTC | 2026-09-25 22:52 UTC | 11m |
| THY3028 | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-09-25 19:32 UTC | 2026-09-25 22:51 UTC | 3h 18m |
| UPS5014 | UPS | Louisville Muhammad Ali International Airport (KSDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-25 20:43 UTC | 2026-09-25 22:50 UTC | 2h 7m |
| BOE453 | BOE | Boeing Field/King County International Airport (KBFI) | Franz Ranch Airport (33WA) | 2026-09-25 21:25 UTC | 2026-09-25 22:47 UTC | 1h 21m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-25 22:28 UTC | 2026-09-25 22:45 UTC | 17m |
| CHH769 | CHH | Beijing Capital International Airport (ZBAA) | Sharypovo Airport (UNKO) | 2026-09-25 19:22 UTC | 2026-09-25 22:44 UTC | 3h 22m |
| N62WA |  | Muscatine Municipal Airport (KMUT) | Phillips Field (MO23) | 2026-09-25 22:15 UTC | 2026-09-25 22:43 UTC | 27m |
| TRP2 | TRP | KW32 (KW32) | Joint Base Andrews Airport (KADW) | 2026-09-25 22:34 UTC | 2026-09-25 22:42 UTC | 8m |
| IOM | IOM | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-09-25 21:51 UTC | 2026-09-25 22:41 UTC | 49m |
| N747DP |  | Laurence G Hanscom Field (KBED) | Capital City Airport (KCXY) | 2026-09-25 21:48 UTC | 2026-09-25 22:41 UTC | 52m |
| VTE5424 | VTE | Charlotte/Douglas International Airport (KCLT) | Mercer County Airport (KBLF) | 2026-09-25 22:13 UTC | 2026-09-25 22:39 UTC | 26m |
| N5043J |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-09-25 22:07 UTC | 2026-09-25 22:37 UTC | 30m |
| N854AF |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-09-25 22:01 UTC | 2026-09-25 22:37 UTC | 35m |
| CWA922 | CWA | Edmonton International Airport (CYEG) | Irma Airport (CFU8) | 2026-09-25 22:14 UTC | 2026-09-25 22:36 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
