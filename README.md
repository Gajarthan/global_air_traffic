# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_20:23:40_UTC-green)

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

**Latest saved flight:** 2026-09-12 20:23:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 20:23:40 UTC

- **256,617** saved flights
- **76,480** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **256,617** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,100,787.6 tonnes** estimated CO2 emissions
- **179,755,806 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10211 |
| 2 | SkyWest Airlines | 8938 |
| 3 | EJA | 4957 |
| 4 | IndiGo | 4300 |
| 5 | American Airlines | 4062 |
| 6 | Southwest Airlines | 3777 |
| 7 | Delta Air Lines | 3214 |
| 8 | ENY | 3045 |
| 9 | LATAM Airlines | 2468 |
| 10 | AZU | 2387 |
| 11 | Vueling | 2171 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2011 |
| 14 | LXJ | 2002 |
| 15 | easyJet | 1755 |
| 16 | Swiss International | 1721 |
| 17 | QLK | 1653 |
| 18 | AXM | 1642 |
| 19 | EJU | 1636 |
| 20 | United Airlines | 1591 |
| 21 | Alaska Airlines | 1523 |
| 22 | All Nippon Airways | 1493 |
| 23 | WMT | 1451 |
| 24 | GLO | 1430 |
| 25 | PGT | 1417 |
| 26 | VIV | 1404 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1397 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1245 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213052 |
| 2 | 🇪🇸 ES | 16305 |
| 3 | 🇧🇷 BR | 14966 |
| 4 | 🇦🇺 AU | 14613 |
| 5 | 🇨🇦 CA | 14299 |
| 6 | 🇮🇹 IT | 14025 |
| 7 | 🇮🇳 IN | 13478 |
| 8 | 🇩🇪 DE | 12514 |
| 9 | 🇬🇧 GB | 11981 |
| 10 | 🇨🇴 CO | 11463 |
| 11 | 🇫🇷 FR | 10308 |
| 12 | 🇯🇵 JP | 10017 |
| 13 | 🇹🇷 TR | 7712 |
| 14 | 🇬🇷 GR | 7487 |
| 15 | 🇲🇽 MX | 7081 |
| 16 | 🇨🇭 CH | 6892 |
| 17 | 🇳🇴 NO | 6347 |
| 18 | 🇹🇭 TH | 4613 |
| 19 | 🇲🇾 MY | 4415 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4257 |
| 22 | 🇳🇿 NZ | 3537 |
| 23 | 🇵🇭 PH | 3446 |
| 24 | 🇬🇹 GT | 3256 |
| 25 | 🇭🇷 HR | 2945 |
| 26 | 🇰🇷 KR | 2938 |
| 27 | 🇲🇦 MA | 2584 |
| 28 | 🇲🇪 ME | 2416 |
| 29 | 🇳🇱 NL | 2314 |
| 30 | 🇮🇩 ID | 2178 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5263 |
| 2 | Denver International Airport |  | US | 4149 |
| 3 | Indira Gandhi International Airport |  | IN | 3103 |
| 4 | Tokyo International Airport |  | JP | 2991 |
| 5 | Guaymaral Airport |  | CO | 2760 |
| 6 | Harry Reid International Airport |  | US | 2715 |
| 7 | Zurich Airport |  | CH | 2691 |
| 8 | El Dorado International Airport |  | CO | 2659 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2587 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2509 |
| 11 | La Aurora Airport |  | GT | 2473 |
| 12 | Salt Lake City International Airport |  | US | 2260 |
| 13 | Chicago O'Hare International Airport |  | US | 2233 |
| 14 | Congonhas Airport |  | BR | 2198 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2096 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2004 |
| 18 | Frankfurt am Main International Airport |  | DE | 1982 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1925 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1856 |
| 21 | Malpensa International Airport |  | IT | 1850 |
| 22 | Charles de Gaulle International Airport |  | FR | 1803 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1799 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1779 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1735 |
| 26 | Macau International Airport |  | MO | 1698 |
| 27 | Ninoy Aquino International Airport |  | PH | 1685 |
| 28 | Barcelona International Airport |  | ES | 1615 |
| 29 | Charlotte/Douglas International Airport |  | US | 1607 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1572 |
| 32 | Viracopos International Airport |  | BR | 1530 |
| 33 | Seattle-Tacoma International Airport |  | US | 1502 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1489 |
| 35 | Don Mueang International Airport |  | TH | 1475 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1457 |
| 38 | Oslo Gardermoen Airport |  | NO | 1449 |
| 39 | Vancouver International Airport |  | CA | 1442 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1387 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 956 | 21m | 244 km | 4,025.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 689 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 643 | 1h 6m | 770 km | 8,541.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 640 | 24m | 225 km | 2,482.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 412 | 44m | 555 km | 3,945.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 409 | 1h 50m | 1,423 km | 10,037.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 359 | 24m | 218 km | 1,352.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 310 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 295 | 19m | 144 km | 733.8 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 269 | 41m | 535 km | 2,484.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PSOMH | PSO | Leite Lopes Airport (SBRP) | Fazenda Agua Comprida Airport (SNAF) | 2026-09-12 20:05 UTC | 2026-09-12 20:23 UTC | 18m |
| N682AC |  | Toy Airpark (15XS) | Bb Airpark (TE88) | 2026-09-12 19:23 UTC | 2026-09-12 20:23 UTC | 59m |
| N786FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-12 19:34 UTC | 2026-09-12 20:23 UTC | 48m |
| HLE22 | HLE | Colerne Airport (EGUO) | Colerne Airport (EGUO) | 2026-09-12 19:26 UTC | 2026-09-12 20:21 UTC | 55m |
| N485K |  | Marina Municipal Airport (KOAR) | Marina Municipal Airport (KOAR) | 2026-09-12 20:07 UTC | 2026-09-12 20:20 UTC | 13m |
| N135RF |  | Casas Adobes Airpark (NM69) | Casas Adobes Airpark (NM69) | 2026-09-12 20:04 UTC | 2026-09-12 20:19 UTC | 14m |
| FILL31 | FIL | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-09-12 19:41 UTC | 2026-09-12 20:14 UTC | 33m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-12 19:46 UTC | 2026-09-12 20:07 UTC | 21m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-12 06:09 UTC | 2026-09-12 20:06 UTC | 13h 56m |
| HK2218G |  | Enrique Olaya Herrera Airport (SKMD) | Madrid Air Base (SKMA) | 2026-09-12 18:57 UTC | 2026-09-12 20:05 UTC | 1h 8m |
| N7577N |  | Montgomery-Gibbs Executive Airport (KMYF) | Brown Field Municipal Airport (KSDM) | 2026-09-12 19:17 UTC | 2026-09-12 20:04 UTC | 47m |
| VJT188 | VJT | London Luton Airport (EGGW) | Pune Airport (VAPO) | 2026-09-12 10:37 UTC | 2026-09-12 20:04 UTC | 9h 26m |
| N9901 |  | Lakefront Airport (KNEW) | Diamondhead Airport (K66Y) | 2026-09-12 19:12 UTC | 2026-09-12 20:03 UTC | 50m |
| N167AR |  | Greenville Downtown Airport (KGMU) | Robert F Swinnie Airport (KPHH) | 2026-09-12 19:16 UTC | 2026-09-12 19:57 UTC | 40m |
| DLH756 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-12 11:41 UTC | 2026-09-12 19:56 UTC | 8h 14m |
| N522AM |  | Flying Cloud Airport (KFCM) | Mineta San Jose International Airport (KSJC) | 2026-09-12 15:48 UTC | 2026-09-12 19:54 UTC | 4h 6m |
| EFY7772 | EFY | La Nubia Airport (SKMZ) | Gomez Nino Apiay Air Base (SKAP) | 2026-09-12 19:14 UTC | 2026-09-12 19:51 UTC | 36m |
| N135RF |  | Casas Adobes Airpark (NM69) | Casas Adobes Airpark (NM69) | 2026-09-12 19:36 UTC | 2026-09-12 19:50 UTC | 13m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-12 18:56 UTC | 2026-09-12 19:49 UTC | 53m |
| ABD4303 | ABD | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-09-12 08:05 UTC | 2026-09-12 19:49 UTC | 11h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
