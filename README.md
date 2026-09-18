# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_05:29:31_UTC-green)

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

**Latest saved flight:** 2026-09-18 05:29:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 05:29:31 UTC

- **262,006** saved flights
- **77,550** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,006** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,174,001.7 tonnes** estimated CO2 emissions
- **184,000,100 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10366 |
| 2 | SkyWest Airlines | 9126 |
| 3 | EJA | 5081 |
| 4 | IndiGo | 4393 |
| 5 | American Airlines | 4113 |
| 6 | Southwest Airlines | 3847 |
| 7 | Delta Air Lines | 3275 |
| 8 | ENY | 3094 |
| 9 | LATAM Airlines | 2524 |
| 10 | AZU | 2457 |
| 11 | Vueling | 2204 |
| 12 | WIF | 2113 |
| 13 | LXJ | 2050 |
| 14 | Lufthansa | 2028 |
| 15 | easyJet | 1772 |
| 16 | Swiss International | 1735 |
| 17 | QLK | 1695 |
| 18 | AXM | 1655 |
| 19 | EJU | 1650 |
| 20 | United Airlines | 1609 |
| 21 | Alaska Airlines | 1555 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1476 |
| 24 | PGT | 1466 |
| 25 | GLO | 1463 |
| 26 | Air France | 1435 |
| 27 | VIV | 1431 |
| 28 | Wizz Air | 1420 |
| 29 | TKR | 1275 |
| 30 | AEE | 1269 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217675 |
| 2 | 🇪🇸 ES | 16534 |
| 3 | 🇧🇷 BR | 15333 |
| 4 | 🇦🇺 AU | 15056 |
| 5 | 🇨🇦 CA | 14589 |
| 6 | 🇮🇹 IT | 14250 |
| 7 | 🇮🇳 IN | 13867 |
| 8 | 🇩🇪 DE | 12673 |
| 9 | 🇬🇧 GB | 12164 |
| 10 | 🇨🇴 CO | 11825 |
| 11 | 🇫🇷 FR | 10470 |
| 12 | 🇯🇵 JP | 10171 |
| 13 | 🇹🇷 TR | 7914 |
| 14 | 🇬🇷 GR | 7605 |
| 15 | 🇲🇽 MX | 7215 |
| 16 | 🇨🇭 CH | 6999 |
| 17 | 🇳🇴 NO | 6466 |
| 18 | 🇹🇭 TH | 4696 |
| 19 | 🇲🇾 MY | 4462 |
| 20 | 🇿🇦 ZA | 4420 |
| 21 | 🇵🇱 PL | 4321 |
| 22 | 🇳🇿 NZ | 3639 |
| 23 | 🇵🇭 PH | 3499 |
| 24 | 🇬🇹 GT | 3340 |
| 25 | 🇭🇷 HR | 2989 |
| 26 | 🇰🇷 KR | 2985 |
| 27 | 🇲🇦 MA | 2617 |
| 28 | 🇲🇪 ME | 2462 |
| 29 | 🇳🇱 NL | 2337 |
| 30 | 🇮🇩 ID | 2211 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5363 |
| 2 | Denver International Airport |  | US | 4240 |
| 3 | Indira Gandhi International Airport |  | IN | 3149 |
| 4 | Tokyo International Airport |  | JP | 3036 |
| 5 | Harry Reid International Airport |  | US | 2787 |
| 6 | Guaymaral Airport |  | CO | 2777 |
| 7 | El Dorado International Airport |  | CO | 2760 |
| 8 | Zurich Airport |  | CH | 2732 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2638 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2543 |
| 11 | La Aurora Airport |  | GT | 2537 |
| 12 | Salt Lake City International Airport |  | US | 2314 |
| 13 | Chicago O'Hare International Airport |  | US | 2263 |
| 14 | Congonhas Airport |  | BR | 2238 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2140 |
| 16 | Capua Airport |  | IT | 2045 |
| 17 | Madrid Barajas International Airport |  | ES | 2026 |
| 18 | Frankfurt am Main International Airport |  | DE | 2000 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1978 |
| 20 | Malpensa International Airport |  | IT | 1885 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1880 |
| 22 | Charles de Gaulle International Airport |  | FR | 1851 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1798 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1797 |
| 26 | Macau International Airport |  | MO | 1741 |
| 27 | Ninoy Aquino International Airport |  | PH | 1716 |
| 28 | Barcelona International Airport |  | ES | 1634 |
| 29 | Charlotte/Douglas International Airport |  | US | 1632 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1613 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1585 |
| 33 | Seattle-Tacoma International Airport |  | US | 1540 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1525 |
| 35 | Don Mueang International Airport |  | TH | 1497 |
| 36 | Calgary International Airport |  | CA | 1496 |
| 37 | Bengaluru International Airport |  | IN | 1487 |
| 38 | Oslo Gardermoen Airport |  | NO | 1471 |
| 39 | Vancouver International Airport |  | CA | 1467 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1402 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 978 | 21m | 244 km | 4,118.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 711 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 658 | 1h 6m | 770 km | 8,741.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 588 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 425 | 44m | 555 km | 4,069.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 413 | 1h 50m | 1,423 km | 10,135.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 399 | 44m | 241 km | 1,657.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 369 | 24m | 218 km | 1,390.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 322 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 302 | 1h 14m | 961 km | 5,005.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 302 | 19m | 144 km | 751.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 283 | 1h 50m | 1,304 km | 6,366.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKIME | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-09-18 05:11 UTC | 2026-09-18 05:29 UTC | 17m |
| AIC130 | Air India | London Heathrow Airport (EGLL) | Pune Airport (VAPO) | 2026-09-17 20:19 UTC | 2026-09-18 05:23 UTC | 9h 4m |
| XSN40 | XSN | Santa Monica Municipal Airport (KSMO) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-18 04:01 UTC | 2026-09-18 05:22 UTC | 1h 20m |
| AEE4320 | AEE | Diagoras Airport (LGRP) | EPKI (EPKI) | 2026-09-18 03:00 UTC | 2026-09-18 05:14 UTC | 2h 13m |
| NSQ | NSQ | Mount Gambier Airport (YMTG) | Orange Airport (YORG) | 2026-09-18 04:11 UTC | 2026-09-18 05:13 UTC | 1h 2m |
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 20:43 UTC | 2026-09-18 04:59 UTC | 8h 16m |
| EJA692 | EJA | Harry Reid International Airport (KLAS) | San Bernardino International Airport (KSBD) | 2026-09-18 04:17 UTC | 2026-09-18 04:57 UTC | 39m |
| N821FR |  | Long Beach (Daugherty Field) Airport (KLGB) | Santa Barbara Municipal Airport (KSBA) | 2026-09-18 03:44 UTC | 2026-09-18 04:54 UTC | 1h 9m |
| NSZ2602 | NSZ | Helsinki Vantaa Airport (EFHK) | Stockholm-Arlanda Airport (ESSA) | 2026-09-18 04:05 UTC | 2026-09-18 04:53 UTC | 48m |
| TRP2 | TRP | KW32 (KW32) | Joint Base Andrews Airport (KADW) | 2026-09-18 04:45 UTC | 2026-09-18 04:53 UTC | 7m |
| SEJ5023 | SEJ | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-18 02:18 UTC | 2026-09-18 04:48 UTC | 2h 29m |
| SEH2AK | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-09-18 04:15 UTC | 2026-09-18 04:48 UTC | 32m |
| ABY822 | ABY | Suvarnabhumi Airport (VTBS) | VEVZ (VEVZ) | 2026-09-18 02:21 UTC | 2026-09-18 04:43 UTC | 2h 22m |
| ETD403 | Etihad Airways | Suvarnabhumi Airport (VTBS) | VEVZ (VEVZ) | 2026-09-18 02:26 UTC | 2026-09-18 04:43 UTC | 2h 17m |
| AZU4411 | AZU | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Benedito Mutran Airport (SIBD) | 2026-09-18 00:53 UTC | 2026-09-18 04:43 UTC | 3h 49m |
| N491LG |  | Tall Timber Airport (CD28) | Erie Municipal Airport (KEIK) | 2026-09-18 03:49 UTC | 2026-09-18 04:42 UTC | 52m |
| PGT6HJ | PGT | Sabiha Gokcen International Airport (LTFJ) | Selcuk Efes Airport (LTFB) | 2026-09-18 04:08 UTC | 2026-09-18 04:41 UTC | 33m |
| OMA818 | Oman Air | Suvarnabhumi Airport (VTBS) | VEVZ (VEVZ) | 2026-09-18 02:30 UTC | 2026-09-18 04:41 UTC | 2h 11m |
| N7274G |  | Green Mountain Airport (WA67) | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | 2026-09-18 03:51 UTC | 2026-09-18 04:37 UTC | 46m |
| WIF1YL | WIF | Bodø Airport (ENBO) | Leknes Airport (ENLK) | 2026-09-18 04:27 UTC | 2026-09-18 04:37 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
