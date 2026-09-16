# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_09:20:10_UTC-green)

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

**Latest saved flight:** 2026-09-16 09:20:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 09:20:10 UTC

- **260,023** saved flights
- **77,130** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,023** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,150,012.8 tonnes** estimated CO2 emissions
- **182,609,440 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10291 |
| 2 | SkyWest Airlines | 9065 |
| 3 | EJA | 5044 |
| 4 | IndiGo | 4365 |
| 5 | American Airlines | 4097 |
| 6 | Southwest Airlines | 3822 |
| 7 | Delta Air Lines | 3249 |
| 8 | ENY | 3077 |
| 9 | LATAM Airlines | 2502 |
| 10 | AZU | 2439 |
| 11 | Vueling | 2194 |
| 12 | WIF | 2089 |
| 13 | LXJ | 2034 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1767 |
| 16 | Swiss International | 1732 |
| 17 | QLK | 1681 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1602 |
| 21 | Alaska Airlines | 1546 |
| 22 | All Nippon Airways | 1510 |
| 23 | WMT | 1468 |
| 24 | GLO | 1450 |
| 25 | PGT | 1449 |
| 26 | VIV | 1426 |
| 27 | Air France | 1422 |
| 28 | Wizz Air | 1413 |
| 29 | TKR | 1260 |
| 30 | AEE | 1258 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215891 |
| 2 | 🇪🇸 ES | 16449 |
| 3 | 🇧🇷 BR | 15197 |
| 4 | 🇦🇺 AU | 14875 |
| 5 | 🇨🇦 CA | 14473 |
| 6 | 🇮🇹 IT | 14143 |
| 7 | 🇮🇳 IN | 13747 |
| 8 | 🇩🇪 DE | 12621 |
| 9 | 🇬🇧 GB | 12093 |
| 10 | 🇨🇴 CO | 11698 |
| 11 | 🇫🇷 FR | 10427 |
| 12 | 🇯🇵 JP | 10124 |
| 13 | 🇹🇷 TR | 7847 |
| 14 | 🇬🇷 GR | 7559 |
| 15 | 🇲🇽 MX | 7174 |
| 16 | 🇨🇭 CH | 6976 |
| 17 | 🇳🇴 NO | 6419 |
| 18 | 🇹🇭 TH | 4675 |
| 19 | 🇲🇾 MY | 4439 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4293 |
| 22 | 🇳🇿 NZ | 3609 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3317 |
| 25 | 🇭🇷 HR | 2972 |
| 26 | 🇰🇷 KR | 2968 |
| 27 | 🇲🇦 MA | 2607 |
| 28 | 🇲🇪 ME | 2446 |
| 29 | 🇳🇱 NL | 2329 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5327 |
| 2 | Denver International Airport |  | US | 4212 |
| 3 | Indira Gandhi International Airport |  | IN | 3137 |
| 4 | Tokyo International Airport |  | JP | 3020 |
| 5 | Guaymaral Airport |  | CO | 2769 |
| 6 | Harry Reid International Airport |  | US | 2760 |
| 7 | El Dorado International Airport |  | CO | 2728 |
| 8 | Zurich Airport |  | CH | 2721 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2613 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2532 |
| 11 | La Aurora Airport |  | GT | 2516 |
| 12 | Salt Lake City International Airport |  | US | 2295 |
| 13 | Chicago O'Hare International Airport |  | US | 2253 |
| 14 | Congonhas Airport |  | BR | 2223 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2126 |
| 16 | Capua Airport |  | IT | 2028 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1956 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1870 |
| 21 | Malpensa International Airport |  | IT | 1870 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1835 |
| 23 | Charles de Gaulle International Airport |  | FR | 1834 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1790 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1770 |
| 26 | Macau International Airport |  | MO | 1722 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1626 |
| 29 | Charlotte/Douglas International Airport |  | US | 1624 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1600 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1571 |
| 33 | Seattle-Tacoma International Airport |  | US | 1528 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1513 |
| 35 | Don Mueang International Airport |  | TH | 1494 |
| 36 | Calgary International Airport |  | CA | 1486 |
| 37 | Bengaluru International Airport |  | IN | 1478 |
| 38 | Oslo Gardermoen Airport |  | NO | 1463 |
| 39 | Vancouver International Airport |  | CA | 1456 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1397 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 970 | 21m | 244 km | 4,084.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 702 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 653 | 1h 6m | 770 km | 8,674.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 583 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 394 | 44m | 241 km | 1,636.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 330 | 19m | 99 km | 565.3 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 327 | 1h 6m | 706 km | 3,981.2 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 324 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 316 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 299 | 1h 14m | 961 km | 4,956.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 276 | 42m | 535 km | 2,549.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 275 | 28m | 152 km | 718.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HST2356 | HST | Antalya International Airport (LTAI) | EPHN (EPHN) | 2026-09-16 06:48 UTC | 2026-09-16 09:20 UTC | 2h 31m |
| OEFFL | OEF | Foligno Airport (LIAF) | L'Aquila / Preturo Airport (LIAP) | 2026-09-16 07:15 UTC | 2026-09-16 09:10 UTC | 1h 55m |
| FOREST4 | FOR | Paphos International Airport (LCPH) | Paphos International Airport (LCPH) | 2026-09-16 09:00 UTC | 2026-09-16 09:07 UTC | 7m |
|  |  | Augsburg Airport (EDMA) | Augsburg Airport (EDMA) | 2026-09-16 09:04 UTC | 2026-09-16 09:04 UTC | 0m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-15 22:14 UTC | 2026-09-16 09:03 UTC | 10h 49m |
| SPHOR | SPH | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-09-16 08:33 UTC | 2026-09-16 09:02 UTC | 29m |
| HERC32 | HER | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-09-16 08:38 UTC | 2026-09-16 08:55 UTC | 17m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-16 08:38 UTC | 2026-09-16 08:54 UTC | 15m |
| UBA585 | UBA | Monywar Airport (VYMY) | Phonngbyin Airport (VYPB) | 2026-09-16 08:24 UTC | 2026-09-16 08:53 UTC | 29m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-09-16 07:39 UTC | 2026-09-16 08:53 UTC | 1h 13m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-15 21:25 UTC | 2026-09-16 08:52 UTC | 11h 27m |
| DRAGOC | DRA | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-09-16 07:31 UTC | 2026-09-16 08:50 UTC | 1h 18m |
| IGO65P | IndiGo | Dubai International Airport (OMDB) | Giridih Airport (VE41) | 2026-09-16 01:57 UTC | 2026-09-16 08:47 UTC | 6h 49m |
| SWR2GE | Swiss International | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-09-16 07:53 UTC | 2026-09-16 08:46 UTC | 52m |
| VTTWJ | VTT | HAL Airport (VOBG) | Hosur Airport (VO95) | 2026-09-16 08:28 UTC | 2026-09-16 08:46 UTC | 18m |
| R21232 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-09-16 08:18 UTC | 2026-09-16 08:46 UTC | 27m |
| PCH22T | PCH | Buochs Airport (LSZC) | Bern Belp Airport (LSZB) | 2026-09-16 07:42 UTC | 2026-09-16 08:41 UTC | 59m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-09-16 07:53 UTC | 2026-09-16 08:41 UTC | 47m |
| EWG8NU | EWG | Malpensa International Airport (LIMC) | Hannover Airport (EDDV) | 2026-09-16 07:27 UTC | 2026-09-16 08:41 UTC | 1h 14m |
| JJP983 | JJP | Fukuoka Airport (RJFF) | New Chitose Airport (RJCC) | 2026-09-16 06:52 UTC | 2026-09-16 08:40 UTC | 1h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
