# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_04:40:03_UTC-green)

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

**Latest saved flight:** 2026-08-26 04:40:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 04:40:03 UTC

- **237,455** saved flights
- **72,387** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **237,455** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,858,698.8 tonnes** estimated CO2 emissions
- **165,721,669 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9501 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 3998 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3033 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2282 |
| 10 | AZU | 2216 |
| 11 | Vueling | 2028 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1588 |
| 17 | AXM | 1585 |
| 18 | EJU | 1520 |
| 19 | QLK | 1514 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1427 |
| 22 | All Nippon Airways | 1413 |
| 23 | GLO | 1329 |
| 24 | WMT | 1324 |
| 25 | VIV | 1312 |
| 26 | PGT | 1296 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1268 |
| 29 | JetBlue | 1180 |
| 30 | AEE | 1175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197374 |
| 2 | 🇪🇸 ES | 15216 |
| 3 | 🇧🇷 BR | 13883 |
| 4 | 🇦🇺 AU | 13470 |
| 5 | 🇨🇦 CA | 13169 |
| 6 | 🇮🇹 IT | 12930 |
| 7 | 🇮🇳 IN | 12464 |
| 8 | 🇩🇪 DE | 11666 |
| 9 | 🇬🇧 GB | 11179 |
| 10 | 🇨🇴 CO | 10122 |
| 11 | 🇯🇵 JP | 9598 |
| 12 | 🇫🇷 FR | 9503 |
| 13 | 🇹🇷 TR | 7046 |
| 14 | 🇬🇷 GR | 6979 |
| 15 | 🇲🇽 MX | 6602 |
| 16 | 🇨🇭 CH | 6322 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇹🇭 TH | 4248 |
| 19 | 🇲🇾 MY | 4244 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3945 |
| 22 | 🇳🇿 NZ | 3287 |
| 23 | 🇵🇭 PH | 3267 |
| 24 | 🇬🇹 GT | 2976 |
| 25 | 🇰🇷 KR | 2788 |
| 26 | 🇭🇷 HR | 2734 |
| 27 | 🇲🇦 MA | 2396 |
| 28 | 🇲🇪 ME | 2205 |
| 29 | 🇳🇱 NL | 2125 |
| 30 | 🇮🇩 ID | 2074 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2895 |
| 4 | Tokyo International Airport |  | JP | 2861 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2369 |
| 10 | El Dorado International Airport |  | CO | 2276 |
| 11 | La Aurora Airport |  | GT | 2268 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1864 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1793 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1751 |
| 21 | Malpensa International Airport |  | IT | 1699 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1668 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1582 |
| 27 | Kuala Lumpur International Airport |  | MY | 1534 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1499 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1441 |
| 32 | Viracopos International Airport |  | BR | 1418 |
| 33 | Seattle-Tacoma International Airport |  | US | 1392 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 35 | Bengaluru International Airport |  | IN | 1389 |
| 36 | Don Mueang International Airport |  | TH | 1375 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1302 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 874 | 21m | 244 km | 3,680.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 603 | 1h 6m | 770 km | 8,010.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 602 | 24m | 225 km | 2,335.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 391 | 27m | 275 km | 1,852.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 368 | 1h 50m | 1,423 km | 9,031.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 347 | 44m | 555 km | 3,322.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 319 | 1h 7m | 706 km | 3,883.8 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 318 | 24m | 218 km | 1,198.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 317 | 22m | 55 km | 301.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 316 | 1h 40m | 1,156 km | 6,304.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8086K |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-08-26 03:55 UTC | 2026-08-26 04:40 UTC | 44m |
| A7GHZ |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-26 03:53 UTC | 2026-08-26 04:37 UTC | 44m |
| VHPFL | VHP | Sembawang Air Base (WSAG) | Paya Lebar Air Base (WSAP) | 2026-08-26 04:20 UTC | 2026-08-26 04:20 UTC | 0m |
| A7GQD |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-26 02:28 UTC | 2026-08-26 04:19 UTC | 1h 51m |
| DEAD10 | DEA | Hunter Army Air Field (KSVN) | Hodges Airpark (GA39) | 2026-08-26 03:27 UTC | 2026-08-26 04:16 UTC | 48m |
| N114UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-26 03:23 UTC | 2026-08-26 04:15 UTC | 52m |
| ACA7116 | Air Canada | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-08-26 03:40 UTC | 2026-08-26 04:10 UTC | 29m |
| N677AA |  | Pocono Mountains Regional Airport (KMPO) | Lancaster Airport (KLNS) | 2026-08-26 03:24 UTC | 2026-08-26 04:09 UTC | 44m |
| 8QMAD |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-08-26 03:59 UTC | 2026-08-26 04:08 UTC | 8m |
| EFC657B | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-26 03:26 UTC | 2026-08-26 04:07 UTC | 40m |
| N108UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-26 03:06 UTC | 2026-08-26 04:07 UTC | 1h 0m |
| WWF287 | WWF | Hedditch Airport (MT72) | Fowler Field (02WN) | 2026-08-26 02:39 UTC | 2026-08-26 04:04 UTC | 1h 24m |
| FD264 |  | Swan Hill Airport (YSWH) | Prairie Airport (YPRA) | 2026-08-26 03:51 UTC | 2026-08-26 04:03 UTC | 12m |
| AM314 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-08-26 03:43 UTC | 2026-08-26 04:03 UTC | 20m |
| N115UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-26 02:44 UTC | 2026-08-26 04:03 UTC | 1h 18m |
| RAIDR51 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 8CL0 (8CL0) | 2026-08-26 03:13 UTC | 2026-08-26 04:00 UTC | 47m |
| AAL2506 | American Airlines | Philadelphia International Airport (KPHL) | San Francisco International Airport (KSFO) | 2026-08-25 22:32 UTC | 2026-08-26 04:00 UTC | 5h 28m |
| N793US |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-26 03:00 UTC | 2026-08-26 03:57 UTC | 57m |
| CVA718 | CVA | Auckland International Airport (NZAA) | Wanganui Airport (NZWU) | 2026-08-26 03:12 UTC | 2026-08-26 03:57 UTC | 44m |
| ANA859 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-08-26 03:52 UTC | 2026-08-26 03:53 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
