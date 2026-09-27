# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_18:49:53_UTC-green)

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

**Latest saved flight:** 2026-09-27 18:49:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 18:49:53 UTC

- **271,174** saved flights
- **79,383** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **271,174** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,288,305.8 tonnes** estimated CO2 emissions
- **190,626,423 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10674 |
| 2 | SkyWest Airlines | 9437 |
| 3 | EJA | 5294 |
| 4 | IndiGo | 4537 |
| 5 | American Airlines | 4212 |
| 6 | Southwest Airlines | 3993 |
| 7 | Delta Air Lines | 3367 |
| 8 | ENY | 3184 |
| 9 | LATAM Airlines | 2608 |
| 10 | AZU | 2544 |
| 11 | Vueling | 2256 |
| 12 | WIF | 2205 |
| 13 | LXJ | 2135 |
| 14 | Lufthansa | 2058 |
| 15 | easyJet | 1814 |
| 16 | Swiss International | 1778 |
| 17 | QLK | 1743 |
| 18 | EJU | 1698 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1657 |
| 21 | Alaska Airlines | 1599 |
| 22 | All Nippon Airways | 1557 |
| 23 | PGT | 1530 |
| 24 | WMT | 1515 |
| 25 | GLO | 1512 |
| 26 | Air France | 1492 |
| 27 | VIV | 1482 |
| 28 | Wizz Air | 1473 |
| 29 | CXK | 1333 |
| 30 | AEE | 1298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225901 |
| 2 | 🇪🇸 ES | 16981 |
| 3 | 🇧🇷 BR | 15873 |
| 4 | 🇦🇺 AU | 15565 |
| 5 | 🇨🇦 CA | 15118 |
| 6 | 🇮🇹 IT | 14659 |
| 7 | 🇮🇳 IN | 14356 |
| 8 | 🇩🇪 DE | 13011 |
| 9 | 🇬🇧 GB | 12547 |
| 10 | 🇨🇴 CO | 12449 |
| 11 | 🇫🇷 FR | 10781 |
| 12 | 🇯🇵 JP | 10401 |
| 13 | 🇹🇷 TR | 8211 |
| 14 | 🇬🇷 GR | 7818 |
| 15 | 🇲🇽 MX | 7484 |
| 16 | 🇨🇭 CH | 7214 |
| 17 | 🇳🇴 NO | 6699 |
| 18 | 🇹🇭 TH | 4847 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4524 |
| 21 | 🇵🇱 PL | 4452 |
| 22 | 🇳🇿 NZ | 3800 |
| 23 | 🇵🇭 PH | 3587 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3092 |
| 26 | 🇰🇷 KR | 3060 |
| 27 | 🇲🇦 MA | 2690 |
| 28 | 🇲🇪 ME | 2546 |
| 29 | 🇳🇱 NL | 2439 |
| 30 | 🇮🇩 ID | 2258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5519 |
| 2 | Denver International Airport |  | US | 4413 |
| 3 | Indira Gandhi International Airport |  | IN | 3243 |
| 4 | Tokyo International Airport |  | JP | 3113 |
| 5 | El Dorado International Airport |  | CO | 2955 |
| 6 | Harry Reid International Airport |  | US | 2906 |
| 7 | Guaymaral Airport |  | CO | 2823 |
| 8 | Zurich Airport |  | CH | 2811 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2719 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2393 |
| 13 | Chicago O'Hare International Airport |  | US | 2311 |
| 14 | Congonhas Airport |  | BR | 2310 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2218 |
| 16 | Capua Airport |  | IT | 2096 |
| 17 | Madrid Barajas International Airport |  | ES | 2090 |
| 18 | Frankfurt am Main International Airport |  | DE | 2051 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2049 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1929 |
| 22 | Charles de Gaulle International Airport |  | FR | 1928 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1906 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1895 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1761 |
| 28 | Charlotte/Douglas International Airport |  | US | 1697 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1688 |
| 30 | Barcelona International Airport |  | ES | 1683 |
| 31 | Viracopos International Airport |  | BR | 1632 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1589 |
| 34 | Seattle-Tacoma International Airport |  | US | 1587 |
| 35 | Calgary International Airport |  | CA | 1544 |
| 36 | Don Mueang International Airport |  | TH | 1533 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1521 |
| 39 | Vancouver International Airport |  | CA | 1516 |
| 40 | Antalya International Airport |  | TR | 1447 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1124 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1016 | 21m | 244 km | 4,278.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 750 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 451 | 44m | 555 km | 4,318.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 436 | 27m | 275 km | 2,066.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 428 | 1h 50m | 1,423 km | 10,503.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 415 | 44m | 241 km | 1,723.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 346 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 315 | 19m | 144 km | 783.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 306 | 1h 14m | 961 km | 5,072.1 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 300 | 42m | 535 km | 2,770.7 t |
| 25 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 297 | 18m | 14 km | 74.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 293 | 1h 50m | 1,304 km | 6,591.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGCBB | CGC | Mansfield Airport (CPV4) | Brampton Airport (CNC3) | 2026-09-27 18:36 UTC | 2026-09-27 18:49 UTC | 13m |
| N228BM |  | Hampton Roads Executive Airport (KPVG) | Suffolk Executive Airport (KSFQ) | 2026-09-27 18:06 UTC | 2026-09-27 18:46 UTC | 40m |
| CFIAQ | CFI | CEB4 (CEB4) | CEB4 (CEB4) | 2026-09-27 18:18 UTC | 2026-09-27 18:46 UTC | 27m |
| ERU19 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Cottonwood Airport (KP52) | 2026-09-27 18:13 UTC | 2026-09-27 18:33 UTC | 19m |
| STW023 | STW | Antalya International Airport (LTAI) | Bezymyanka Airfield (UWWG) | 2026-09-27 15:34 UTC | 2026-09-27 18:33 UTC | 2h 59m |
| E7GPS |  | Banja Luka International Airport (LQBK) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-27 18:05 UTC | 2026-09-27 18:31 UTC | 25m |
| N438WR |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-27 18:06 UTC | 2026-09-27 18:31 UTC | 24m |
| CXK234 | CXK | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-09-27 18:01 UTC | 2026-09-27 18:28 UTC | 26m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-09-27 18:16 UTC | 2026-09-27 18:28 UTC | 11m |
| N26ND |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-27 17:53 UTC | 2026-09-27 18:28 UTC | 34m |
| N817WA |  | Fort Worth Meacham International Airport (KFTW) | Lake County Airport (KLXV) | 2026-09-27 16:05 UTC | 2026-09-27 18:28 UTC | 2h 23m |
| N268Z |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-09-27 17:52 UTC | 2026-09-27 18:25 UTC | 33m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-27 17:00 UTC | 2026-09-27 18:25 UTC | 1h 24m |
| JTL611 | JTL | Shannon Airport (EINN) | Bangor International Airport (KBGR) | 2026-09-27 12:50 UTC | 2026-09-27 18:24 UTC | 5h 33m |
|  |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-09-27 18:21 UTC | 2026-09-27 18:21 UTC | 0m |
| N88HR |  | Visalia Municipal Airport (KVIS) | Libby Airport (KS59) | 2026-09-27 16:07 UTC | 2026-09-27 18:19 UTC | 2h 12m |
| N1293E |  | Harpers Fly-In Ranch Airport (0FL0) | Airglades Airport (K2IS) | 2026-09-27 18:06 UTC | 2026-09-27 18:17 UTC | 10m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-09-27 17:36 UTC | 2026-09-27 18:15 UTC | 39m |
| N261HB |  | City Of Colorado Springs Municipal Airport (KCOS) | Scenic Mesa Ranch Airport (CD02) | 2026-09-27 17:27 UTC | 2026-09-27 18:14 UTC | 47m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-09-27 17:58 UTC | 2026-09-27 18:14 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
