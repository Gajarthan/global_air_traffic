# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_04:28:33_UTC-green)

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

**Latest saved flight:** 2026-09-22 04:28:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-22 04:28:33 UTC

- **266,030** saved flights
- **78,313** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **266,030** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,225,370.5 tonnes** estimated CO2 emissions
- **186,977,999 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10521 |
| 2 | SkyWest Airlines | 9259 |
| 3 | EJA | 5171 |
| 4 | IndiGo | 4466 |
| 5 | American Airlines | 4151 |
| 6 | Southwest Airlines | 3919 |
| 7 | Delta Air Lines | 3310 |
| 8 | ENY | 3130 |
| 9 | LATAM Airlines | 2563 |
| 10 | AZU | 2502 |
| 11 | Vueling | 2233 |
| 12 | WIF | 2150 |
| 13 | LXJ | 2089 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1788 |
| 16 | Swiss International | 1752 |
| 17 | QLK | 1720 |
| 18 | EJU | 1677 |
| 19 | AXM | 1666 |
| 20 | United Airlines | 1633 |
| 21 | Alaska Airlines | 1574 |
| 22 | All Nippon Airways | 1533 |
| 23 | PGT | 1498 |
| 24 | WMT | 1493 |
| 25 | GLO | 1483 |
| 26 | Air France | 1460 |
| 27 | VIV | 1456 |
| 28 | Wizz Air | 1447 |
| 29 | CXK | 1291 |
| 30 | AEE | 1284 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221158 |
| 2 | 🇪🇸 ES | 16715 |
| 3 | 🇧🇷 BR | 15562 |
| 4 | 🇦🇺 AU | 15254 |
| 5 | 🇨🇦 CA | 14819 |
| 6 | 🇮🇹 IT | 14470 |
| 7 | 🇮🇳 IN | 14130 |
| 8 | 🇩🇪 DE | 12809 |
| 9 | 🇬🇧 GB | 12337 |
| 10 | 🇨🇴 CO | 12130 |
| 11 | 🇫🇷 FR | 10612 |
| 12 | 🇯🇵 JP | 10254 |
| 13 | 🇹🇷 TR | 8054 |
| 14 | 🇬🇷 GR | 7702 |
| 15 | 🇲🇽 MX | 7335 |
| 16 | 🇨🇭 CH | 7088 |
| 17 | 🇳🇴 NO | 6568 |
| 18 | 🇹🇭 TH | 4769 |
| 19 | 🇲🇾 MY | 4491 |
| 20 | 🇿🇦 ZA | 4466 |
| 21 | 🇵🇱 PL | 4371 |
| 22 | 🇳🇿 NZ | 3699 |
| 23 | 🇵🇭 PH | 3535 |
| 24 | 🇬🇹 GT | 3378 |
| 25 | 🇭🇷 HR | 3030 |
| 26 | 🇰🇷 KR | 3018 |
| 27 | 🇲🇦 MA | 2656 |
| 28 | 🇲🇪 ME | 2491 |
| 29 | 🇳🇱 NL | 2380 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5422 |
| 2 | Denver International Airport |  | US | 4320 |
| 3 | Indira Gandhi International Airport |  | IN | 3193 |
| 4 | Tokyo International Airport |  | JP | 3065 |
| 5 | El Dorado International Airport |  | CO | 2853 |
| 6 | Harry Reid International Airport |  | US | 2845 |
| 7 | Guaymaral Airport |  | CO | 2793 |
| 8 | Zurich Airport |  | CH | 2763 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2671 |
| 10 | La Aurora Airport |  | GT | 2566 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2565 |
| 12 | Salt Lake City International Airport |  | US | 2350 |
| 13 | Chicago O'Hare International Airport |  | US | 2285 |
| 14 | Congonhas Airport |  | BR | 2267 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2175 |
| 16 | Capua Airport |  | IT | 2083 |
| 17 | Madrid Barajas International Airport |  | ES | 2049 |
| 18 | Frankfurt am Main International Airport |  | DE | 2025 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2012 |
| 20 | Malpensa International Airport |  | IT | 1921 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1900 |
| 22 | Charles de Gaulle International Airport |  | FR | 1884 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1871 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1863 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1810 |
| 26 | Macau International Airport |  | MO | 1770 |
| 27 | Ninoy Aquino International Airport |  | PH | 1735 |
| 28 | Barcelona International Airport |  | ES | 1661 |
| 29 | Charlotte/Douglas International Airport |  | US | 1660 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1643 |
| 31 | Viracopos International Airport |  | BR | 1614 |
| 32 | Kuala Lumpur International Airport |  | MY | 1610 |
| 33 | Seattle-Tacoma International Airport |  | US | 1560 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1554 |
| 35 | Calgary International Airport |  | CA | 1519 |
| 36 | Don Mueang International Airport |  | TH | 1513 |
| 37 | Bengaluru International Airport |  | IN | 1506 |
| 38 | Oslo Gardermoen Airport |  | NO | 1496 |
| 39 | Vancouver International Airport |  | CA | 1488 |
| 40 | Antalya International Airport |  | TR | 1425 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1115 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 996 | 21m | 244 km | 4,193.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 735 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 668 | 1h 6m | 770 km | 8,873.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 663 | 24m | 225 km | 2,572.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 438 | 44m | 555 km | 4,194.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 405 | 44m | 241 km | 1,682.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 340 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 335 | 1h 6m | 706 km | 4,078.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 332 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 330 | 26m | 215 km | 1,222.2 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 309 | 19m | 144 km | 768.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 288 | 42m | 535 km | 2,659.9 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 278 | 18m | 14 km | 69.5 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PGT43FF | PGT | Cigli Airport (LTBL) | Istanbul Airport (LTFM) | 2026-09-22 03:51 UTC | 2026-09-22 04:28 UTC | 37m |
| NIU | NIU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-22 04:00 UTC | 2026-09-22 04:21 UTC | 20m |
| GRYHK21 | GRY | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-22 02:59 UTC | 2026-09-22 04:21 UTC | 1h 21m |
| N67657 |  | Zamperini Field (KTOA) | Fullerton Municipal Airport (KFUL) | 2026-09-22 03:10 UTC | 2026-09-22 04:17 UTC | 1h 7m |
| A6FHD |  | Al Bateen Executive Airport (OMAD) | Das Island Airport (OMAS) | 2026-09-22 03:27 UTC | 2026-09-22 04:14 UTC | 47m |
| JA838N |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-09-22 04:10 UTC | 2026-09-22 04:13 UTC | 3m |
| ARC | ARC | Melbourne Moorabbin Airport (YMMB) | Wangaratta Airport (YWGT) | 2026-09-22 03:45 UTC | 2026-09-22 04:12 UTC | 27m |
| N119UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-22 03:18 UTC | 2026-09-22 04:12 UTC | 53m |
| N113UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-22 02:54 UTC | 2026-09-22 04:06 UTC | 1h 12m |
| VAMPYR01 | VAM | Somerton Airport (54AZ) | Somerton Airport (54AZ) | 2026-09-22 03:48 UTC | 2026-09-22 03:59 UTC | 11m |
| RPC9487 | RPC | Subic Bay International Airport (RPLB) | Castillejos Airport (RPUJ) | 2026-09-22 03:48 UTC | 2026-09-22 03:59 UTC | 10m |
| N499XX |  | Twentynine Palms Self Airport (KNXP) | Twentynine Palms Self Airport (KNXP) | 2026-09-22 03:39 UTC | 2026-09-22 03:54 UTC | 14m |
| WRHRS52 | WRH | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-09-22 02:42 UTC | 2026-09-22 03:49 UTC | 1h 6m |
| VAR478 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Deer Valley Airport (KDVT) | 2026-09-22 03:09 UTC | 2026-09-22 03:48 UTC | 39m |
| N3067Y |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-22 03:03 UTC | 2026-09-22 03:47 UTC | 44m |
| SWA1150 | Southwest Airlines | Harry Reid International Airport (KLAS) | Carson City Airport (KCXP) | 2026-09-22 02:37 UTC | 2026-09-22 03:42 UTC | 1h 5m |
| N214NX |  | Aurora State Airport (KUAO) | Lazy F Ranch Airport (99OR) | 2026-09-22 02:53 UTC | 2026-09-22 03:42 UTC | 49m |
| N25NX |  | Louisa County/Freeman Field (KLKU) | Lincoln Airport (KLNK) | 2026-09-21 23:31 UTC | 2026-09-22 03:41 UTC | 4h 10m |
| N112UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-22 02:35 UTC | 2026-09-22 03:39 UTC | 1h 3m |
| N111WG |  | Merrill Field (PAMR) | Tin Creek Airport (PAFL) | 2026-09-22 03:04 UTC | 2026-09-22 03:37 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
