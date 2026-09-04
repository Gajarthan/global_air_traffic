# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_08:56:43_UTC-green)

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

**Latest saved flight:** 2026-09-04 08:56:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 08:56:43 UTC

- **246,830** saved flights
- **74,459** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,830** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,969,662.4 tonnes** estimated CO2 emissions
- **172,154,340 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9883 |
| 2 | SkyWest Airlines | 8630 |
| 3 | EJA | 4760 |
| 4 | IndiGo | 4125 |
| 5 | American Airlines | 3963 |
| 6 | Southwest Airlines | 3682 |
| 7 | Delta Air Lines | 3133 |
| 8 | ENY | 2952 |
| 9 | LATAM Airlines | 2378 |
| 10 | AZU | 2293 |
| 11 | Vueling | 2111 |
| 12 | WIF | 1976 |
| 13 | Lufthansa | 1969 |
| 14 | LXJ | 1913 |
| 15 | easyJet | 1712 |
| 16 | Swiss International | 1658 |
| 17 | AXM | 1619 |
| 18 | EJU | 1588 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1553 |
| 21 | Alaska Airlines | 1476 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1391 |
| 24 | GLO | 1378 |
| 25 | VIV | 1356 |
| 26 | PGT | 1353 |
| 27 | Air France | 1348 |
| 28 | Wizz Air | 1336 |
| 29 | JetBlue | 1217 |
| 30 | AEE | 1215 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204634 |
| 2 | 🇪🇸 ES | 15817 |
| 3 | 🇧🇷 BR | 14408 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13733 |
| 6 | 🇮🇹 IT | 13515 |
| 7 | 🇮🇳 IN | 12872 |
| 8 | 🇩🇪 DE | 12151 |
| 9 | 🇬🇧 GB | 11608 |
| 10 | 🇨🇴 CO | 10739 |
| 11 | 🇫🇷 FR | 9953 |
| 12 | 🇯🇵 JP | 9786 |
| 13 | 🇹🇷 TR | 7330 |
| 14 | 🇬🇷 GR | 7271 |
| 15 | 🇲🇽 MX | 6818 |
| 16 | 🇨🇭 CH | 6641 |
| 17 | 🇳🇴 NO | 6126 |
| 18 | 🇹🇭 TH | 4454 |
| 19 | 🇲🇾 MY | 4341 |
| 20 | 🇿🇦 ZA | 4277 |
| 21 | 🇵🇱 PL | 4132 |
| 22 | 🇳🇿 NZ | 3378 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3086 |
| 25 | 🇰🇷 KR | 2882 |
| 26 | 🇭🇷 HR | 2834 |
| 27 | 🇲🇦 MA | 2495 |
| 28 | 🇲🇪 ME | 2305 |
| 29 | 🇳🇱 NL | 2231 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5081 |
| 2 | Denver International Airport |  | US | 3990 |
| 3 | Indira Gandhi International Airport |  | IN | 3009 |
| 4 | Tokyo International Airport |  | JP | 2919 |
| 5 | Guaymaral Airport |  | CO | 2721 |
| 6 | Harry Reid International Airport |  | US | 2629 |
| 7 | Zurich Airport |  | CH | 2586 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2512 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2456 |
| 10 | El Dorado International Airport |  | CO | 2455 |
| 11 | La Aurora Airport |  | GT | 2348 |
| 12 | Salt Lake City International Airport |  | US | 2188 |
| 13 | Chicago O'Hare International Airport |  | US | 2168 |
| 14 | Congonhas Airport |  | BR | 2116 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2035 |
| 16 | Capua Airport |  | IT | 1940 |
| 17 | Frankfurt am Main International Airport |  | DE | 1938 |
| 18 | Madrid Barajas International Airport |  | ES | 1934 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1856 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1806 |
| 21 | Malpensa International Airport |  | IT | 1768 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 23 | Charles de Gaulle International Airport |  | FR | 1734 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1726 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1608 |
| 28 | Charlotte/Douglas International Airport |  | US | 1570 |
| 29 | Barcelona International Airport |  | ES | 1564 |
| 30 | Kuala Lumpur International Airport |  | MY | 1563 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1507 |
| 32 | Viracopos International Airport |  | BR | 1467 |
| 33 | Seattle-Tacoma International Airport |  | US | 1451 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1437 |
| 35 | Don Mueang International Airport |  | TH | 1431 |
| 36 | Bengaluru International Airport |  | IN | 1425 |
| 37 | Calgary International Airport |  | CA | 1420 |
| 38 | Oslo Gardermoen Airport |  | NO | 1390 |
| 39 | Vancouver International Airport |  | CA | 1380 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1344 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 916 | 21m | 244 km | 3,857.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 646 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 619 | 1h 6m | 770 km | 8,222.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 553 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 406 | 27m | 275 km | 1,923.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 392 | 1h 50m | 1,423 km | 9,620.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 381 | 44m | 555 km | 3,648.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 364 | 44m | 241 km | 1,512.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 343 | 24m | 218 km | 1,292.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 332 | 23m | 55 km | 315.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 305 | 26m | 215 km | 1,129.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 282 | 19m | 144 km | 701.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 268 | 1h 50m | 1,304 km | 6,029.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JST125 | JST | Adelaide International Airport (YPAD) | Perth International Airport (YPPH) | 2026-09-03 21:05 UTC | 2026-09-04 08:56 UTC | 11h 50m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-09-04 07:44 UTC | 2026-09-04 08:51 UTC | 1h 6m |
| EVA005 | EVA Air | Los Angeles International Airport (KLAX) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-03 19:31 UTC | 2026-09-04 08:45 UTC | 13h 14m |
| LAE1819 | LAE | Miami International Airport (KMIA) | El Dorado International Airport (SKBO) | 2026-09-04 05:22 UTC | 2026-09-04 08:28 UTC | 3h 5m |
| DHK366 | DHK | East Midlands Airport (EGNX) | John F Kennedy International Airport (KJFK) | 2026-09-04 01:01 UTC | 2026-09-04 08:25 UTC | 7h 23m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-04 07:45 UTC | 2026-09-04 08:22 UTC | 37m |
| SIA196 | Singapore Airlines | Singapore Changi International Airport (WSSS) | Noi Bai International Airport (VVNB) | 2026-09-04 05:11 UTC | 2026-09-04 08:22 UTC | 3h 11m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-09-04 07:44 UTC | 2026-09-04 08:22 UTC | 37m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-09-04 07:59 UTC | 2026-09-04 08:20 UTC | 21m |
| BNI3MJ | BNI | EPKL (EPKL) | Gliwice Glider Airport (EPGL) | 2026-09-04 07:29 UTC | 2026-09-04 08:14 UTC | 45m |
| OEFJT | OEF | Innsbruck Airport (LOWI) | Meribel Airport (LFKX) | 2026-09-04 06:20 UTC | 2026-09-04 08:04 UTC | 1h 43m |
| A3590 |  | Thessaloniki Macedonia International Airport (LGTS) | Santorini Airport (LGSR) | 2026-09-04 06:58 UTC | 2026-09-04 08:02 UTC | 1h 4m |
| GSM012 | GSM | Stockholm-Bromma Airport (ESSB) | Hamburg Airport (EDDH) | 2026-09-04 05:58 UTC | 2026-09-04 08:01 UTC | 2h 3m |
| OOJGK | OOJ | Wevelgem Airport (EBKT) | Twenthe Airport (EHTW) | 2026-09-04 07:26 UTC | 2026-09-04 07:57 UTC | 30m |
| RYR6CX | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Palermo / Bocca Di Falco Airport (LICP) | 2026-09-04 06:57 UTC | 2026-09-04 07:57 UTC | 59m |
| WMT3662 | WMT | Bergamo / Orio Al Serio Airport (LIME) | Cluj-Napoca International Airport (LRCL) | 2026-09-04 06:29 UTC | 2026-09-04 07:54 UTC | 1h 25m |
| QLK575D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-09-04 07:17 UTC | 2026-09-04 07:52 UTC | 35m |
| JAL3114 | Japan Airlines | Chitose Air Base (RJCJ) | Chubu Centrair International Airport (RJGG) | 2026-09-04 06:35 UTC | 2026-09-04 07:52 UTC | 1h 17m |
| THY1SW | Turkish Airlines | Istanbul Airport (LTFM) | Ataturk International Airport (LTBA) | 2026-09-03 23:32 UTC | 2026-09-04 07:51 UTC | 8h 19m |
| ANA797 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-09-04 06:43 UTC | 2026-09-04 07:50 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
