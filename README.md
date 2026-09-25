# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_20:22:26_UTC-green)

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

**Latest saved flight:** 2026-09-25 20:22:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 20:22:26 UTC

- **269,450** saved flights
- **79,022** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,450** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,268,796.7 tonnes** estimated CO2 emissions
- **189,495,463 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10614 |
| 2 | SkyWest Airlines | 9377 |
| 3 | EJA | 5272 |
| 4 | IndiGo | 4513 |
| 5 | American Airlines | 4187 |
| 6 | Southwest Airlines | 3958 |
| 7 | Delta Air Lines | 3347 |
| 8 | ENY | 3165 |
| 9 | LATAM Airlines | 2599 |
| 10 | AZU | 2524 |
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
| 29 | CXK | 1321 |
| 30 | AEE | 1294 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224344 |
| 2 | 🇪🇸 ES | 16895 |
| 3 | 🇧🇷 BR | 15761 |
| 4 | 🇦🇺 AU | 15494 |
| 5 | 🇨🇦 CA | 15030 |
| 6 | 🇮🇹 IT | 14591 |
| 7 | 🇮🇳 IN | 14264 |
| 8 | 🇩🇪 DE | 12930 |
| 9 | 🇬🇧 GB | 12476 |
| 10 | 🇨🇴 CO | 12351 |
| 11 | 🇫🇷 FR | 10717 |
| 12 | 🇯🇵 JP | 10350 |
| 13 | 🇹🇷 TR | 8159 |
| 14 | 🇬🇷 GR | 7786 |
| 15 | 🇲🇽 MX | 7431 |
| 16 | 🇨🇭 CH | 7158 |
| 17 | 🇳🇴 NO | 6672 |
| 18 | 🇹🇭 TH | 4816 |
| 19 | 🇲🇾 MY | 4527 |
| 20 | 🇿🇦 ZA | 4498 |
| 21 | 🇵🇱 PL | 4409 |
| 22 | 🇳🇿 NZ | 3768 |
| 23 | 🇵🇭 PH | 3571 |
| 24 | 🇬🇹 GT | 3409 |
| 25 | 🇭🇷 HR | 3070 |
| 26 | 🇰🇷 KR | 3046 |
| 27 | 🇲🇦 MA | 2682 |
| 28 | 🇲🇪 ME | 2526 |
| 29 | 🇳🇱 NL | 2406 |
| 30 | 🇮🇩 ID | 2241 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5487 |
| 2 | Denver International Airport |  | US | 4383 |
| 3 | Indira Gandhi International Airport |  | IN | 3224 |
| 4 | Tokyo International Airport |  | JP | 3096 |
| 5 | El Dorado International Airport |  | CO | 2922 |
| 6 | Harry Reid International Airport |  | US | 2890 |
| 7 | Guaymaral Airport |  | CO | 2815 |
| 8 | Zurich Airport |  | CH | 2792 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2709 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2594 |
| 11 | La Aurora Airport |  | GT | 2591 |
| 12 | Salt Lake City International Airport |  | US | 2376 |
| 13 | Chicago O'Hare International Airport |  | US | 2303 |
| 14 | Congonhas Airport |  | BR | 2299 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2206 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2076 |
| 18 | Frankfurt am Main International Airport |  | DE | 2044 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2038 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1921 |
| 22 | Charles de Gaulle International Airport |  | FR | 1913 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1890 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1882 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1820 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1752 |
| 28 | Charlotte/Douglas International Airport |  | US | 1683 |
| 29 | Barcelona International Airport |  | ES | 1677 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1669 |
| 31 | Viracopos International Airport |  | BR | 1628 |
| 32 | Kuala Lumpur International Airport |  | MY | 1621 |
| 33 | Seattle-Tacoma International Airport |  | US | 1577 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1576 |
| 35 | Calgary International Airport |  | CA | 1537 |
| 36 | Don Mueang International Airport |  | TH | 1525 |
| 37 | Bengaluru International Airport |  | IN | 1519 |
| 38 | Oslo Gardermoen Airport |  | NO | 1512 |
| 39 | Vancouver International Airport |  | CA | 1507 |
| 40 | Reno/Tahoe International Airport |  | US | 1435 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1009 | 21m | 244 km | 4,248.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 743 | 8m | - | - |
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
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 285 | 28m | 152 km | 744.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N649GC |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-25 20:02 UTC | 2026-09-25 20:22 UTC | 20m |
| N897TD |  | Rogers Executive - Carter Field (KROG) | San Francisco International Airport (KSFO) | 2026-09-25 16:51 UTC | 2026-09-25 20:20 UTC | 3h 29m |
| N188AH |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-09-25 19:57 UTC | 2026-09-25 20:19 UTC | 21m |
| N3816Q |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 2026-09-25 19:34 UTC | 2026-09-25 20:16 UTC | 41m |
| NWX448 | NWX | Beggs Ranch/Aledo/ Airport (TX15) | Bowie Municipal Airport (K0F2) | 2026-09-25 19:46 UTC | 2026-09-25 20:15 UTC | 28m |
| N507LA |  | Ryan Field (KRYN) | Marana Regional Airport (KAVQ) | 2026-09-25 20:02 UTC | 2026-09-25 20:14 UTC | 11m |
| N828SP |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-09-25 19:50 UTC | 2026-09-25 20:12 UTC | 21m |
| N2551U |  | Dekalb-Peachtree Airport (KPDK) | Cy Nunnally Memorial Airport (KD73) | 2026-09-25 18:57 UTC | 2026-09-25 20:12 UTC | 1h 15m |
| MS4 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-09-25 18:37 UTC | 2026-09-25 20:09 UTC | 1h 31m |
| SFY558 | SFY | Broocke Air Patch Airport (FL95) | 7FL3 (7FL3) | 2026-09-25 19:31 UTC | 2026-09-25 20:07 UTC | 35m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-25 08:48 UTC | 2026-09-25 20:03 UTC | 11h 15m |
| OTLW55 | OTL | Southport Airport (CYPG) | Southport Airport (CYPG) | 2026-09-25 19:57 UTC | 2026-09-25 20:03 UTC | 5m |
| N474J |  | Quinn Airport (CA41) | Santa Monica Municipal Airport (KSMO) | 2026-09-25 19:20 UTC | 2026-09-25 20:03 UTC | 42m |
| N41HX |  | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-09-25 19:48 UTC | 2026-09-25 20:01 UTC | 12m |
| N680EA |  | Birmingham-Shuttlesworth International Airport (KBHM) | Nicholson Airport (75WV) | 2026-09-25 18:48 UTC | 2026-09-25 19:57 UTC | 1h 9m |
| PSFHI | PSF | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | Congonhas Airport (SBSP) | 2026-09-25 19:20 UTC | 2026-09-25 19:57 UTC | 37m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-25 05:59 UTC | 2026-09-25 19:57 UTC | 13h 57m |
|  |  | Ottawa / Gatineau Airport (CYND) | Ottawa / Gatineau Airport (CYND) | 2026-09-25 19:54 UTC | 2026-09-25 19:56 UTC | 2m |
| N44RL |  | Castroville Municipal Airport (KCVB) | 5XS3 (5XS3) | 2026-09-25 16:35 UTC | 2026-09-25 19:55 UTC | 3h 19m |
| N1611F |  | Thomaston-Upson County Airport (KOPN) | Dawson Municipal Airport (K16J) | 2026-09-25 19:10 UTC | 2026-09-25 19:54 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
