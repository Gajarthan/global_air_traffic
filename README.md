# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_09:02:42_UTC-green)

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

**Latest saved flight:** 2026-09-19 09:02:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 09:02:42 UTC

- **263,214** saved flights
- **77,782** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,214** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,188,777.2 tonnes** estimated CO2 emissions
- **184,856,649 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10412 |
| 2 | SkyWest Airlines | 9157 |
| 3 | EJA | 5107 |
| 4 | IndiGo | 4425 |
| 5 | American Airlines | 4127 |
| 6 | Southwest Airlines | 3868 |
| 7 | Delta Air Lines | 3286 |
| 8 | ENY | 3103 |
| 9 | LATAM Airlines | 2535 |
| 10 | AZU | 2472 |
| 11 | Vueling | 2213 |
| 12 | WIF | 2125 |
| 13 | LXJ | 2063 |
| 14 | Lufthansa | 2031 |
| 15 | easyJet | 1780 |
| 16 | Swiss International | 1737 |
| 17 | QLK | 1701 |
| 18 | AXM | 1660 |
| 19 | EJU | 1660 |
| 20 | United Airlines | 1614 |
| 21 | Alaska Airlines | 1561 |
| 22 | All Nippon Airways | 1522 |
| 23 | WMT | 1480 |
| 24 | PGT | 1479 |
| 25 | GLO | 1469 |
| 26 | Air France | 1443 |
| 27 | VIV | 1438 |
| 28 | Wizz Air | 1428 |
| 29 | CXK | 1275 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218703 |
| 2 | 🇪🇸 ES | 16592 |
| 3 | 🇧🇷 BR | 15398 |
| 4 | 🇦🇺 AU | 15104 |
| 5 | 🇨🇦 CA | 14655 |
| 6 | 🇮🇹 IT | 14299 |
| 7 | 🇮🇳 IN | 13982 |
| 8 | 🇩🇪 DE | 12718 |
| 9 | 🇬🇧 GB | 12223 |
| 10 | 🇨🇴 CO | 11916 |
| 11 | 🇫🇷 FR | 10517 |
| 12 | 🇯🇵 JP | 10200 |
| 13 | 🇹🇷 TR | 7967 |
| 14 | 🇬🇷 GR | 7637 |
| 15 | 🇲🇽 MX | 7239 |
| 16 | 🇨🇭 CH | 7023 |
| 17 | 🇳🇴 NO | 6506 |
| 18 | 🇹🇭 TH | 4720 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4434 |
| 21 | 🇵🇱 PL | 4337 |
| 22 | 🇳🇿 NZ | 3648 |
| 23 | 🇵🇭 PH | 3504 |
| 24 | 🇬🇹 GT | 3352 |
| 25 | 🇭🇷 HR | 3003 |
| 26 | 🇰🇷 KR | 2989 |
| 27 | 🇲🇦 MA | 2633 |
| 28 | 🇲🇪 ME | 2469 |
| 29 | 🇳🇱 NL | 2351 |
| 30 | 🇮🇩 ID | 2214 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5380 |
| 2 | Denver International Airport |  | US | 4257 |
| 3 | Indira Gandhi International Airport |  | IN | 3161 |
| 4 | Tokyo International Airport |  | JP | 3046 |
| 5 | Harry Reid International Airport |  | US | 2800 |
| 6 | El Dorado International Airport |  | CO | 2787 |
| 7 | Guaymaral Airport |  | CO | 2779 |
| 8 | Zurich Airport |  | CH | 2741 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2646 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2551 |
| 11 | La Aurora Airport |  | GT | 2548 |
| 12 | Salt Lake City International Airport |  | US | 2325 |
| 13 | Chicago O'Hare International Airport |  | US | 2265 |
| 14 | Congonhas Airport |  | BR | 2248 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2151 |
| 16 | Capua Airport |  | IT | 2054 |
| 17 | Madrid Barajas International Airport |  | ES | 2034 |
| 18 | Frankfurt am Main International Airport |  | DE | 2006 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1985 |
| 20 | Malpensa International Airport |  | IT | 1892 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1889 |
| 22 | Charles de Gaulle International Airport |  | FR | 1860 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1856 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1820 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1800 |
| 26 | Macau International Airport |  | MO | 1750 |
| 27 | Ninoy Aquino International Airport |  | PH | 1720 |
| 28 | Barcelona International Airport |  | ES | 1644 |
| 29 | Charlotte/Douglas International Airport |  | US | 1642 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1619 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1596 |
| 33 | Seattle-Tacoma International Airport |  | US | 1546 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1533 |
| 35 | Calgary International Airport |  | CA | 1502 |
| 36 | Don Mueang International Airport |  | TH | 1501 |
| 37 | Bengaluru International Airport |  | IN | 1495 |
| 38 | Oslo Gardermoen Airport |  | NO | 1484 |
| 39 | Vancouver International Airport |  | CA | 1472 |
| 40 | Antalya International Airport |  | TR | 1409 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 984 | 21m | 244 km | 4,143.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 720 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 661 | 1h 6m | 770 km | 8,780.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 656 | 24m | 225 km | 2,545.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 428 | 44m | 555 km | 4,098.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 374 | 24m | 218 km | 1,409.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 17 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 281 | 42m | 535 km | 2,595.2 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 281 | 28m | 152 km | 734.4 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ANE8162 | ANE | Bergamo / Orio Al Serio Airport (LIME) | Palma De Mallorca Airport (LEPA) | 2026-09-19 07:50 UTC | 2026-09-19 09:02 UTC | 1h 12m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-09-19 08:18 UTC | 2026-09-19 08:56 UTC | 38m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-09-19 08:41 UTC | 2026-09-19 08:55 UTC | 14m |
| SPILT | SPI | Wrocław-Szymanow Airport (EPWS) | Wrocław-Szymanow Airport (EPWS) | 2026-09-19 08:51 UTC | 2026-09-19 08:52 UTC | 0m |
| TCHGE | TCH | Ataturk International Airport (LTBA) | Istanbul Hezarfen Airfield (LTBW) | 2026-09-19 08:40 UTC | 2026-09-19 08:50 UTC | 10m |
| HBZIB | HBZ | Samedan Airport (LSZS) | LSMF (LSMF) | 2026-09-19 08:17 UTC | 2026-09-19 08:42 UTC | 25m |
| HBKCJ | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-09-19 08:32 UTC | 2026-09-19 08:32 UTC | 0m |
| RYR59JH | Ryanair | Faro Airport (LPFR) | London Stansted Airport (EGSS) | 2026-09-19 06:03 UTC | 2026-09-19 08:29 UTC | 2h 26m |
| HUSKY36 | HUS | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-09-19 07:39 UTC | 2026-09-19 08:27 UTC | 47m |
| DLH6UA | Lufthansa | Frankfurt am Main International Airport (EDDF) | Malpensa International Airport (LIMC) | 2026-09-19 07:30 UTC | 2026-09-19 08:26 UTC | 55m |
| RYR9FR | Ryanair | Shannon Airport (EINN) | Manchester Airport (EGCC) | 2026-09-19 07:34 UTC | 2026-09-19 08:23 UTC | 49m |
| EZY71QW | easyJet | Bristol International Airport (EGGD) | Malpensa International Airport (LIMC) | 2026-09-19 06:41 UTC | 2026-09-19 08:23 UTC | 1h 42m |
| RYR97SR | Ryanair | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Capua Airport (LIAU) | 2026-09-19 07:32 UTC | 2026-09-19 08:21 UTC | 49m |
| 9800 |  | Linz Airport (LOWL) | Linz Airport (LOWL) | 2026-09-19 07:44 UTC | 2026-09-19 08:20 UTC | 35m |
| BHA405 | BHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-09-19 07:32 UTC | 2026-09-19 08:20 UTC | 47m |
| AXM6082 | AXM | Senai International Airport (WMKJ) | Ulu Bernam Airport (WMBF) | 2026-09-19 07:47 UTC | 2026-09-19 08:19 UTC | 32m |
| THA630 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kaohsiung International Airport (RCKH) | 2026-09-19 05:15 UTC | 2026-09-19 08:16 UTC | 3h 0m |
| KLC1787 | KLC | Amsterdam Airport Schiphol (EHAM) | Hannover Airport (EDDV) | 2026-09-19 07:36 UTC | 2026-09-19 08:15 UTC | 39m |
| NYT785 | NYT | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-09-19 07:47 UTC | 2026-09-19 08:12 UTC | 24m |
| SFJ83 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-19 07:07 UTC | 2026-09-19 08:08 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
