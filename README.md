# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_16:51:13_UTC-green)

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

**Latest saved flight:** 2026-09-04 16:51:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 16:51:13 UTC

- **247,201** saved flights
- **74,531** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,201** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,973,272.1 tonnes** estimated CO2 emissions
- **172,363,601 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9908 |
| 2 | SkyWest Airlines | 8636 |
| 3 | EJA | 4766 |
| 4 | IndiGo | 4134 |
| 5 | American Airlines | 3965 |
| 6 | Southwest Airlines | 3682 |
| 7 | Delta Air Lines | 3136 |
| 8 | ENY | 2954 |
| 9 | LATAM Airlines | 2386 |
| 10 | AZU | 2297 |
| 11 | Vueling | 2115 |
| 12 | WIF | 1980 |
| 13 | Lufthansa | 1969 |
| 14 | LXJ | 1913 |
| 15 | easyJet | 1713 |
| 16 | Swiss International | 1659 |
| 17 | AXM | 1619 |
| 18 | EJU | 1590 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1553 |
| 21 | Alaska Airlines | 1476 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1394 |
| 24 | GLO | 1379 |
| 25 | VIV | 1357 |
| 26 | PGT | 1354 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1336 |
| 29 | JetBlue | 1218 |
| 30 | AEE | 1216 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204929 |
| 2 | 🇪🇸 ES | 15849 |
| 3 | 🇧🇷 BR | 14444 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13739 |
| 6 | 🇮🇹 IT | 13542 |
| 7 | 🇮🇳 IN | 12894 |
| 8 | 🇩🇪 DE | 12170 |
| 9 | 🇬🇧 GB | 11623 |
| 10 | 🇨🇴 CO | 10774 |
| 11 | 🇫🇷 FR | 9968 |
| 12 | 🇯🇵 JP | 9788 |
| 13 | 🇹🇷 TR | 7349 |
| 14 | 🇬🇷 GR | 7275 |
| 15 | 🇲🇽 MX | 6828 |
| 16 | 🇨🇭 CH | 6664 |
| 17 | 🇳🇴 NO | 6136 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4345 |
| 20 | 🇿🇦 ZA | 4279 |
| 21 | 🇵🇱 PL | 4140 |
| 22 | 🇳🇿 NZ | 3378 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3089 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2841 |
| 27 | 🇲🇦 MA | 2500 |
| 28 | 🇲🇪 ME | 2309 |
| 29 | 🇳🇱 NL | 2232 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5085 |
| 2 | Denver International Airport |  | US | 3993 |
| 3 | Indira Gandhi International Airport |  | IN | 3013 |
| 4 | Tokyo International Airport |  | JP | 2920 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2633 |
| 7 | Zurich Airport |  | CH | 2588 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2513 |
| 9 | El Dorado International Airport |  | CO | 2464 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2457 |
| 11 | La Aurora Airport |  | GT | 2351 |
| 12 | Salt Lake City International Airport |  | US | 2190 |
| 13 | Chicago O'Hare International Airport |  | US | 2168 |
| 14 | Congonhas Airport |  | BR | 2122 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2038 |
| 16 | Capua Airport |  | IT | 1945 |
| 17 | Frankfurt am Main International Airport |  | DE | 1940 |
| 18 | Madrid Barajas International Airport |  | ES | 1937 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1860 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1807 |
| 21 | Malpensa International Airport |  | IT | 1772 |
| 22 | Charles de Gaulle International Airport |  | FR | 1738 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1726 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1633 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1618 |
| 28 | Charlotte/Douglas International Airport |  | US | 1570 |
| 29 | Barcelona International Airport |  | ES | 1567 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1510 |
| 32 | Viracopos International Airport |  | BR | 1471 |
| 33 | Seattle-Tacoma International Airport |  | US | 1452 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1437 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Bengaluru International Airport |  | IN | 1426 |
| 37 | Calgary International Airport |  | CA | 1420 |
| 38 | Oslo Gardermoen Airport |  | NO | 1392 |
| 39 | Vancouver International Airport |  | CA | 1380 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1345 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 918 | 21m | 244 km | 3,865.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 650 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 620 | 1h 6m | 770 km | 8,236.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 553 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 393 | 1h 50m | 1,423 km | 9,644.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 365 | 44m | 241 km | 1,516.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 344 | 24m | 218 km | 1,296.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 268 | 1h 50m | 1,304 km | 6,029.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 254 | 28m | 152 km | 663.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-04 16:33 UTC | 2026-09-04 16:51 UTC | 18m |
| N901LF |  | 14ME (14ME) | Bangor International Airport (KBGR) | 2026-09-04 16:26 UTC | 2026-09-04 16:45 UTC | 18m |
| N233LA |  | Van Nuys Airport (KVNY) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-04 16:33 UTC | 2026-09-04 16:43 UTC | 10m |
| N297ME |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-09-04 16:28 UTC | 2026-09-04 16:42 UTC | 13m |
| OKBYG | OKB | Brno-Turany Airport (LKTB) | Frydlant Airport (LKFR) | 2026-09-04 16:11 UTC | 2026-09-04 16:41 UTC | 29m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-09-04 16:27 UTC | 2026-09-04 16:41 UTC | 14m |
| BBC337 | BBC | VGZR (VGZR) | Shaibah Airport (OESB) | 2026-09-04 12:33 UTC | 2026-09-04 16:41 UTC | 4h 8m |
| N912AT |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-09-04 15:42 UTC | 2026-09-04 16:39 UTC | 56m |
| N6025F |  | Reno/Tahoe International Airport (KRNO) | Samsarg Field (KN58) | 2026-09-04 16:19 UTC | 2026-09-04 16:39 UTC | 20m |
| N265FA |  | Wings Field (KLOM) | Harrisburg International Airport (KMDT) | 2026-09-04 15:56 UTC | 2026-09-04 16:36 UTC | 40m |
| VLG6311 | Vueling | London Heathrow Airport (EGLL) | Garray Airport (LEGY) | 2026-09-04 15:20 UTC | 2026-09-04 16:35 UTC | 1h 15m |
| N278SP |  | Trenton Mercer Airport (KTTN) | Atlantic City International Airport (KACY) | 2026-09-04 16:04 UTC | 2026-09-04 16:34 UTC | 30m |
| GN204 |  | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-09-04 16:01 UTC | 2026-09-04 16:33 UTC | 32m |
| N491LG |  | Tall Timber Airport (CD28) | CO54 (CO54) | 2026-09-04 16:04 UTC | 2026-09-04 16:33 UTC | 28m |
| N901BS |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-09-04 13:11 UTC | 2026-09-04 16:32 UTC | 3h 21m |
| N953LA |  | San Gabriel Valley Airport (KEMT) | Fullerton Municipal Airport (KFUL) | 2026-09-04 15:41 UTC | 2026-09-04 16:30 UTC | 48m |
| CCDPF | CCD | Comodoro Arturo Merino Benitez International Airport (SCEL) | Eulogio Sanchez Airport (SCTB) | 2026-09-04 16:14 UTC | 2026-09-04 16:25 UTC | 10m |
| RFS729 | RFS | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-09-04 16:02 UTC | 2026-09-04 16:25 UTC | 23m |
| N818ES |  | Kodiak Municipal Airport (PAKD) | Kodiak Municipal Airport (PAKD) | 2026-09-04 16:23 UTC | 2026-09-04 16:24 UTC | 1m |
| N701NW |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Las Cruces International Airport (KLRU) | 2026-09-04 16:07 UTC | 2026-09-04 16:22 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
