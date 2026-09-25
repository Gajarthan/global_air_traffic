# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_17:06:40_UTC-green)

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

**Latest saved flight:** 2026-09-25 17:06:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 17:06:40 UTC

- **269,232** saved flights
- **78,965** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,232** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,265,852.5 tonnes** estimated CO2 emissions
- **189,324,784 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10608 |
| 2 | SkyWest Airlines | 9368 |
| 3 | EJA | 5257 |
| 4 | IndiGo | 4513 |
| 5 | American Airlines | 4184 |
| 6 | Southwest Airlines | 3955 |
| 7 | Delta Air Lines | 3347 |
| 8 | ENY | 3162 |
| 9 | LATAM Airlines | 2597 |
| 10 | AZU | 2521 |
| 11 | Vueling | 2246 |
| 12 | WIF | 2194 |
| 13 | LXJ | 2118 |
| 14 | Lufthansa | 2047 |
| 15 | easyJet | 1807 |
| 16 | Swiss International | 1766 |
| 17 | QLK | 1736 |
| 18 | EJU | 1689 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1649 |
| 21 | Alaska Airlines | 1588 |
| 22 | All Nippon Airways | 1549 |
| 23 | PGT | 1515 |
| 24 | WMT | 1504 |
| 25 | GLO | 1498 |
| 26 | Air France | 1481 |
| 27 | VIV | 1468 |
| 28 | Wizz Air | 1464 |
| 29 | CXK | 1319 |
| 30 | AEE | 1293 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224076 |
| 2 | 🇪🇸 ES | 16878 |
| 3 | 🇧🇷 BR | 15739 |
| 4 | 🇦🇺 AU | 15494 |
| 5 | 🇨🇦 CA | 15012 |
| 6 | 🇮🇹 IT | 14588 |
| 7 | 🇮🇳 IN | 14263 |
| 8 | 🇩🇪 DE | 12929 |
| 9 | 🇬🇧 GB | 12466 |
| 10 | 🇨🇴 CO | 12337 |
| 11 | 🇫🇷 FR | 10716 |
| 12 | 🇯🇵 JP | 10349 |
| 13 | 🇹🇷 TR | 8154 |
| 14 | 🇬🇷 GR | 7784 |
| 15 | 🇲🇽 MX | 7421 |
| 16 | 🇨🇭 CH | 7157 |
| 17 | 🇳🇴 NO | 6667 |
| 18 | 🇹🇭 TH | 4816 |
| 19 | 🇲🇾 MY | 4527 |
| 20 | 🇿🇦 ZA | 4498 |
| 21 | 🇵🇱 PL | 4408 |
| 22 | 🇳🇿 NZ | 3768 |
| 23 | 🇵🇭 PH | 3571 |
| 24 | 🇬🇹 GT | 3409 |
| 25 | 🇭🇷 HR | 3067 |
| 26 | 🇰🇷 KR | 3046 |
| 27 | 🇲🇦 MA | 2682 |
| 28 | 🇲🇪 ME | 2524 |
| 29 | 🇳🇱 NL | 2406 |
| 30 | 🇮🇩 ID | 2241 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5484 |
| 2 | Denver International Airport |  | US | 4379 |
| 3 | Indira Gandhi International Airport |  | IN | 3223 |
| 4 | Tokyo International Airport |  | JP | 3096 |
| 5 | El Dorado International Airport |  | CO | 2919 |
| 6 | Harry Reid International Airport |  | US | 2887 |
| 7 | Guaymaral Airport |  | CO | 2815 |
| 8 | Zurich Airport |  | CH | 2791 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2707 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2593 |
| 11 | La Aurora Airport |  | GT | 2591 |
| 12 | Salt Lake City International Airport |  | US | 2373 |
| 13 | Chicago O'Hare International Airport |  | US | 2302 |
| 14 | Congonhas Airport |  | BR | 2293 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2203 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2074 |
| 18 | Frankfurt am Main International Airport |  | DE | 2044 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2037 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1920 |
| 22 | Charles de Gaulle International Airport |  | FR | 1912 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1887 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1882 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1752 |
| 28 | Charlotte/Douglas International Airport |  | US | 1682 |
| 29 | Barcelona International Airport |  | ES | 1677 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1668 |
| 31 | Viracopos International Airport |  | BR | 1627 |
| 32 | Kuala Lumpur International Airport |  | MY | 1621 |
| 33 | Seattle-Tacoma International Airport |  | US | 1575 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1573 |
| 35 | Calgary International Airport |  | CA | 1536 |
| 36 | Don Mueang International Airport |  | TH | 1525 |
| 37 | Bengaluru International Airport |  | IN | 1519 |
| 38 | Oslo Gardermoen Airport |  | NO | 1511 |
| 39 | Vancouver International Airport |  | CA | 1507 |
| 40 | Antalya International Airport |  | TR | 1433 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1008 | 21m | 244 km | 4,244.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 742 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 678 | 1h 6m | 770 km | 9,006.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 671 | 24m | 225 km | 2,603.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 599 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 444 | 44m | 555 km | 4,251.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 432 | 27m | 275 km | 2,047.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 426 | 1h 50m | 1,423 km | 10,454.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 411 | 44m | 241 km | 1,707.2 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 344 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 295 | 42m | 535 km | 2,724.5 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 289 | 18m | 14 km | 72.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 285 | 28m | 152 km | 744.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N90MF |  | 1AR8 (1AR8) | Booneville Municipal Airport (K4M2) | 2026-09-25 16:18 UTC | 2026-09-25 17:06 UTC | 48m |
| N114FA |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-09-25 16:32 UTC | 2026-09-25 17:06 UTC | 34m |
| N225AZ |  | UT99 (UT99) | K36U (K36U) | 2026-09-25 16:40 UTC | 2026-09-25 17:00 UTC | 20m |
| N2395T |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-25 16:09 UTC | 2026-09-25 16:56 UTC | 46m |
| BOMR866 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | San Jose Island Airport (XS67) | 2026-09-25 16:19 UTC | 2026-09-25 16:54 UTC | 35m |
| N831AF |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-09-25 15:52 UTC | 2026-09-25 16:47 UTC | 55m |
| GLF64 | GLF | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-25 16:36 UTC | 2026-09-25 16:47 UTC | 11m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-25 15:36 UTC | 2026-09-25 16:46 UTC | 1h 10m |
| WMT367 | WMT | Ben Gurion International Airport (LLBG) | UKFB (UKFB) | 2026-09-25 15:12 UTC | 2026-09-25 16:45 UTC | 1h 32m |
| N178JC |  | Phoenix Sky Harbor International Airport (KPHX) | Negrito Airstrip (0NM7) | 2026-09-25 16:29 UTC | 2026-09-25 16:44 UTC | 15m |
| N564CH |  | Harry Reid International Airport (KLAS) | Mid-Way Regional Airport (KJWY) | 2026-09-25 14:24 UTC | 2026-09-25 16:44 UTC | 2h 19m |
| PAT264 | PAT | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Boire Field (KASH) | 2026-09-25 15:02 UTC | 2026-09-25 16:42 UTC | 1h 39m |
| N1759F |  | Barcus Field (95OK) | Sandridge Airpark Inc Airport (OK94) | 2026-09-25 16:40 UTC | 2026-09-25 16:42 UTC | 2m |
| MILAN76 | MIL | Carcassonne Airport (LFMK) | Nimes-Arles-Camargue Airport (LFTW) | 2026-09-25 15:06 UTC | 2026-09-25 16:42 UTC | 1h 36m |
| CXK679 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-25 16:21 UTC | 2026-09-25 16:42 UTC | 21m |
| N329SX |  | Chicago Midway International Airport (KMDW) | Laurence G Hanscom Field (KBED) | 2026-09-25 15:05 UTC | 2026-09-25 16:42 UTC | 1h 36m |
| N918FA |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-09-25 15:49 UTC | 2026-09-25 16:40 UTC | 51m |
| N374RV |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-09-25 16:34 UTC | 2026-09-25 16:38 UTC | 4m |
| N424SG |  | Easterwood Field (KCLL) | Boerne Stage Airfield (K5C1) | 2026-09-25 15:55 UTC | 2026-09-25 16:38 UTC | 42m |
| N1MN |  | Rocky Mountain Metro Airport (KBJC) | A Bar A Ranch Airport (WY11) | 2026-09-25 16:09 UTC | 2026-09-25 16:35 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
