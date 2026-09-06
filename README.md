# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_22:51:24_UTC-green)

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

**Latest saved flight:** 2026-09-06 22:51:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 22:51:24 UTC

- **250,086** saved flights
- **75,120** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **250,086** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,010,934.4 tonnes** estimated CO2 emissions
- **174,546,920 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10014 |
| 2 | SkyWest Airlines | 8728 |
| 3 | EJA | 4828 |
| 4 | IndiGo | 4176 |
| 5 | American Airlines | 4002 |
| 6 | Southwest Airlines | 3715 |
| 7 | Delta Air Lines | 3169 |
| 8 | ENY | 2992 |
| 9 | LATAM Airlines | 2416 |
| 10 | AZU | 2328 |
| 11 | Vueling | 2135 |
| 12 | WIF | 1999 |
| 13 | Lufthansa | 1982 |
| 14 | LXJ | 1940 |
| 15 | easyJet | 1724 |
| 16 | Swiss International | 1680 |
| 17 | AXM | 1628 |
| 18 | EJU | 1609 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1566 |
| 21 | Alaska Airlines | 1493 |
| 22 | All Nippon Airways | 1465 |
| 23 | WMT | 1419 |
| 24 | GLO | 1392 |
| 25 | PGT | 1373 |
| 26 | VIV | 1371 |
| 27 | Air France | 1361 |
| 28 | Wizz Air | 1360 |
| 29 | AEE | 1228 |
| 30 | JetBlue | 1227 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207412 |
| 2 | 🇪🇸 ES | 16000 |
| 3 | 🇧🇷 BR | 14610 |
| 4 | 🇦🇺 AU | 14164 |
| 5 | 🇨🇦 CA | 13896 |
| 6 | 🇮🇹 IT | 13702 |
| 7 | 🇮🇳 IN | 13028 |
| 8 | 🇩🇪 DE | 12295 |
| 9 | 🇬🇧 GB | 11733 |
| 10 | 🇨🇴 CO | 10981 |
| 11 | 🇫🇷 FR | 10079 |
| 12 | 🇯🇵 JP | 9861 |
| 13 | 🇹🇷 TR | 7457 |
| 14 | 🇬🇷 GR | 7356 |
| 15 | 🇲🇽 MX | 6913 |
| 16 | 🇨🇭 CH | 6744 |
| 17 | 🇳🇴 NO | 6190 |
| 18 | 🇹🇭 TH | 4504 |
| 19 | 🇲🇾 MY | 4369 |
| 20 | 🇿🇦 ZA | 4307 |
| 21 | 🇵🇱 PL | 4178 |
| 22 | 🇳🇿 NZ | 3417 |
| 23 | 🇵🇭 PH | 3397 |
| 24 | 🇬🇹 GT | 3133 |
| 25 | 🇰🇷 KR | 2896 |
| 26 | 🇭🇷 HR | 2875 |
| 27 | 🇲🇦 MA | 2530 |
| 28 | 🇲🇪 ME | 2351 |
| 29 | 🇳🇱 NL | 2261 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5164 |
| 2 | Denver International Airport |  | US | 4043 |
| 3 | Indira Gandhi International Airport |  | IN | 3039 |
| 4 | Tokyo International Airport |  | JP | 2944 |
| 5 | Guaymaral Airport |  | CO | 2737 |
| 6 | Harry Reid International Airport |  | US | 2660 |
| 7 | Zurich Airport |  | CH | 2618 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2539 |
| 9 | El Dorado International Airport |  | CO | 2530 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2478 |
| 11 | La Aurora Airport |  | GT | 2389 |
| 12 | Salt Lake City International Airport |  | US | 2209 |
| 13 | Chicago O'Hare International Airport |  | US | 2185 |
| 14 | Congonhas Airport |  | BR | 2146 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2056 |
| 16 | Capua Airport |  | IT | 1971 |
| 17 | Madrid Barajas International Airport |  | ES | 1966 |
| 18 | Frankfurt am Main International Airport |  | DE | 1952 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1879 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1821 |
| 21 | Malpensa International Airport |  | IT | 1802 |
| 22 | Charles de Gaulle International Airport |  | FR | 1752 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1744 |
| 25 | Ninoy Aquino International Airport |  | PH | 1656 |
| 26 | Macau International Airport |  | MO | 1648 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1585 |
| 29 | Barcelona International Airport |  | ES | 1583 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1532 |
| 32 | Viracopos International Airport |  | BR | 1496 |
| 33 | Seattle-Tacoma International Airport |  | US | 1472 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1451 |
| 35 | Don Mueang International Airport |  | TH | 1442 |
| 36 | Calgary International Airport |  | CA | 1439 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1409 |
| 39 | Vancouver International Airport |  | CA | 1399 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 398 | 1h 50m | 1,423 km | 9,767.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 388 | 44m | 555 km | 3,715.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 371 | 44m | 241 km | 1,541.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 289 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA085 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-06 08:14 UTC | 2026-09-06 22:51 UTC | 14h 36m |
| N567HA |  | Martin State Airport (KMTN) | Martin State Airport (KMTN) | 2026-09-06 22:36 UTC | 2026-09-06 22:48 UTC | 12m |
| FDB445 | flydubai | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-06 20:01 UTC | 2026-09-06 22:44 UTC | 2h 43m |
| UAE9780 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-06 15:23 UTC | 2026-09-06 22:43 UTC | 7h 19m |
| IGO018 | IndiGo | Istanbul Airport (LTFM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-06 15:20 UTC | 2026-09-06 22:26 UTC | 7h 6m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-06 21:44 UTC | 2026-09-06 22:25 UTC | 40m |
| N7392U |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-09-06 22:01 UTC | 2026-09-06 22:23 UTC | 22m |
| N40JF |  | 0OI4 (0OI4) | 1OI1 (1OI1) | 2026-09-06 22:10 UTC | 2026-09-06 22:23 UTC | 13m |
| AMD1 | AMD | Christchurch International Airport (NZCH) | Christchurch International Airport (NZCH) | 2026-09-06 22:18 UTC | 2026-09-06 22:21 UTC | 3m |
| CKS701 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-09-06 13:24 UTC | 2026-09-06 22:21 UTC | 8h 57m |
| N961LA |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-09-06 20:57 UTC | 2026-09-06 22:18 UTC | 1h 21m |
| CAP843 | CAP | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-06 21:23 UTC | 2026-09-06 22:15 UTC | 51m |
| N300TA |  | Charleston Afb/International Airport (KCHS) | Aiken Regional Airport (KAIK) | 2026-09-06 21:42 UTC | 2026-09-06 22:12 UTC | 30m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-09-06 21:06 UTC | 2026-09-06 22:11 UTC | 1h 4m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-09-06 17:28 UTC | 2026-09-06 22:09 UTC | 4h 41m |
| N569DW |  | Millard Airport (KMLE) | Plattsmouth Municipal/Douglas V Duey Field (KPMV) | 2026-09-06 21:31 UTC | 2026-09-06 22:08 UTC | 37m |
| ELY027 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-09-06 21:45 UTC | 2026-09-06 22:05 UTC | 19m |
| QXE2001 | QXE | Seattle-Tacoma International Airport (KSEA) | 74WT (74WT) | 2026-09-06 21:45 UTC | 2026-09-06 22:02 UTC | 17m |
| N885WA |  | Seattle Paine Field International Airport (KPAE) | William R Fairchild International Airport (KCLM) | 2026-09-06 21:14 UTC | 2026-09-06 22:00 UTC | 46m |
| NGF7658 | NGF | Boeing Field/King County International Airport (KBFI) | 74WT (74WT) | 2026-09-06 21:37 UTC | 2026-09-06 21:57 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
