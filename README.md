# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_05:29:11_UTC-green)

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

**Latest saved flight:** 2026-09-11 05:29:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 05:29:11 UTC

- **254,592** saved flights
- **76,065** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,592** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,072,420.9 tonnes** estimated CO2 emissions
- **178,111,356 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10154 |
| 2 | SkyWest Airlines | 8882 |
| 3 | EJA | 4919 |
| 4 | IndiGo | 4260 |
| 5 | American Airlines | 4040 |
| 6 | Southwest Airlines | 3755 |
| 7 | Delta Air Lines | 3198 |
| 8 | ENY | 3032 |
| 9 | LATAM Airlines | 2453 |
| 10 | AZU | 2370 |
| 11 | Vueling | 2163 |
| 12 | WIF | 2039 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1991 |
| 15 | easyJet | 1738 |
| 16 | Swiss International | 1705 |
| 17 | QLK | 1645 |
| 18 | AXM | 1634 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1583 |
| 21 | Alaska Airlines | 1515 |
| 22 | All Nippon Airways | 1488 |
| 23 | WMT | 1439 |
| 24 | GLO | 1418 |
| 25 | PGT | 1398 |
| 26 | VIV | 1391 |
| 27 | Wizz Air | 1384 |
| 28 | Air France | 1383 |
| 29 | JetBlue | 1239 |
| 30 | AEE | 1236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211427 |
| 2 | 🇪🇸 ES | 16210 |
| 3 | 🇧🇷 BR | 14863 |
| 4 | 🇦🇺 AU | 14541 |
| 5 | 🇨🇦 CA | 14168 |
| 6 | 🇮🇹 IT | 13921 |
| 7 | 🇮🇳 IN | 13344 |
| 8 | 🇩🇪 DE | 12436 |
| 9 | 🇬🇧 GB | 11890 |
| 10 | 🇨🇴 CO | 11288 |
| 11 | 🇫🇷 FR | 10219 |
| 12 | 🇯🇵 JP | 9972 |
| 13 | 🇹🇷 TR | 7618 |
| 14 | 🇬🇷 GR | 7437 |
| 15 | 🇲🇽 MX | 7016 |
| 16 | 🇨🇭 CH | 6830 |
| 17 | 🇳🇴 NO | 6307 |
| 18 | 🇹🇭 TH | 4574 |
| 19 | 🇲🇾 MY | 4397 |
| 20 | 🇿🇦 ZA | 4339 |
| 21 | 🇵🇱 PL | 4224 |
| 22 | 🇳🇿 NZ | 3511 |
| 23 | 🇵🇭 PH | 3435 |
| 24 | 🇬🇹 GT | 3164 |
| 25 | 🇰🇷 KR | 2927 |
| 26 | 🇭🇷 HR | 2915 |
| 27 | 🇲🇦 MA | 2567 |
| 28 | 🇲🇪 ME | 2392 |
| 29 | 🇳🇱 NL | 2288 |
| 30 | 🇮🇩 ID | 2171 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5231 |
| 2 | Denver International Airport |  | US | 4115 |
| 3 | Indira Gandhi International Airport |  | IN | 3083 |
| 4 | Tokyo International Airport |  | JP | 2977 |
| 5 | Guaymaral Airport |  | CO | 2755 |
| 6 | Harry Reid International Airport |  | US | 2699 |
| 7 | Zurich Airport |  | CH | 2660 |
| 8 | El Dorado International Airport |  | CO | 2611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2574 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2498 |
| 11 | La Aurora Airport |  | GT | 2413 |
| 12 | Salt Lake City International Airport |  | US | 2247 |
| 13 | Chicago O'Hare International Airport |  | US | 2219 |
| 14 | Congonhas Airport |  | BR | 2183 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2083 |
| 16 | Capua Airport |  | IT | 2006 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1967 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1909 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1845 |
| 21 | Malpensa International Airport |  | IT | 1827 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1791 |
| 23 | Charles de Gaulle International Airport |  | FR | 1784 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1770 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1704 |
| 26 | Macau International Airport |  | MO | 1682 |
| 27 | Ninoy Aquino International Airport |  | PH | 1679 |
| 28 | Barcelona International Airport |  | ES | 1603 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1584 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1562 |
| 32 | Viracopos International Airport |  | BR | 1522 |
| 33 | Seattle-Tacoma International Airport |  | US | 1496 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1481 |
| 35 | Calgary International Airport |  | CA | 1467 |
| 36 | Don Mueang International Airport |  | TH | 1465 |
| 37 | Bengaluru International Airport |  | IN | 1448 |
| 38 | Oslo Gardermoen Airport |  | NO | 1437 |
| 39 | Vancouver International Airport |  | CA | 1428 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1373 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1108 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 946 | 21m | 244 km | 3,983.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 639 | 1h 6m | 770 km | 8,488.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 569 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 405 | 44m | 555 km | 3,878.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 383 | 44m | 241 km | 1,590.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 373 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 354 | 24m | 218 km | 1,333.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 309 | 19m | 99 km | 529.3 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 298 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 292 | 1h 14m | 961 km | 4,840.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 290 | 19m | 144 km | 721.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 265 | 41m | 535 km | 2,447.4 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| POL25 | POL | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-09-11 05:17 UTC | 2026-09-11 05:29 UTC | 11m |
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Deer Valley Airport (KDVT) | 2026-09-11 04:35 UTC | 2026-09-11 05:24 UTC | 49m |
| MSR917 | EgyptAir | Al Bateen Executive Airport (OMAD) | Hulwan (HE15) | 2026-09-11 02:24 UTC | 2026-09-11 05:14 UTC | 2h 49m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-09-10 15:03 UTC | 2026-09-11 05:14 UTC | 14h 11m |
| 4XCDE |  | Haifa International Airport (LLHA) | Haifa International Airport (LLHA) | 2026-09-11 04:20 UTC | 2026-09-11 05:12 UTC | 51m |
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-10 20:42 UTC | 2026-09-11 05:11 UTC | 8h 28m |
| N460AK |  | Cleburne Regional Airport (KCPT) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-11 01:53 UTC | 2026-09-11 05:09 UTC | 3h 15m |
| FDX8 | FDX | Charles de Gaulle International Airport (LFPG) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-10 17:53 UTC | 2026-09-11 05:06 UTC | 11h 13m |
| SIA876 | Singapore Airlines | Singapore Changi International Airport (WSSS) | Hsinchu Air Base (RCPO) | 2026-09-11 00:54 UTC | 2026-09-11 05:04 UTC | 4h 9m |
| IUJ | IUJ | Warrnambool Airport (YWBL) | Peterborough Airport (YPBH) | 2026-09-11 04:43 UTC | 2026-09-11 05:01 UTC | 18m |
| RBG316 | RBG | King Fahd International Airport (OEDF) | Hulwan (HE15) | 2026-09-11 02:36 UTC | 2026-09-11 05:01 UTC | 2h 25m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-11 04:38 UTC | 2026-09-11 04:55 UTC | 16m |
| IGO627 | IndiGo | Trivandrum International Airport (VOTV) | Pune Airport (VAPO) | 2026-09-11 03:13 UTC | 2026-09-11 04:54 UTC | 1h 41m |
| MSR684 | EgyptAir | HE13 (HE13) | Hulwan (HE15) | 2026-09-10 22:18 UTC | 2026-09-11 04:51 UTC | 6h 32m |
| TOM948P | TOM | Newcastle Airport (EGNT) | London Gatwick Airport (EGKK) | 2026-09-11 03:42 UTC | 2026-09-11 04:50 UTC | 1h 8m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-10 14:28 UTC | 2026-09-11 04:47 UTC | 14h 19m |
| WIF6PC | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-11 04:35 UTC | 2026-09-11 04:46 UTC | 11m |
| A7GQC |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-09-11 04:42 UTC | 2026-09-11 04:46 UTC | 3m |
| ADI | ADI | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-09-11 04:25 UTC | 2026-09-11 04:46 UTC | 20m |
| FR123 |  | Al Ain International Airport (OMAL) | Ras Al Khaimah International Airport (OMRK) | 2026-09-11 04:16 UTC | 2026-09-11 04:43 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
