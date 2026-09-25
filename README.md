# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_06:22:14_UTC-green)

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

**Latest saved flight:** 2026-09-25 06:22:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 06:22:14 UTC

- **268,923** saved flights
- **78,894** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,923** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,262,281.4 tonnes** estimated CO2 emissions
- **189,117,763 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10598 |
| 2 | SkyWest Airlines | 9356 |
| 3 | EJA | 5252 |
| 4 | IndiGo | 4506 |
| 5 | American Airlines | 4182 |
| 6 | Southwest Airlines | 3952 |
| 7 | Delta Air Lines | 3346 |
| 8 | ENY | 3159 |
| 9 | LATAM Airlines | 2593 |
| 10 | AZU | 2518 |
| 11 | Vueling | 2243 |
| 12 | WIF | 2186 |
| 13 | LXJ | 2116 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1804 |
| 16 | Swiss International | 1762 |
| 17 | QLK | 1736 |
| 18 | EJU | 1687 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1649 |
| 21 | Alaska Airlines | 1587 |
| 22 | All Nippon Airways | 1549 |
| 23 | PGT | 1511 |
| 24 | WMT | 1502 |
| 25 | GLO | 1497 |
| 26 | Air France | 1477 |
| 27 | VIV | 1468 |
| 28 | Wizz Air | 1459 |
| 29 | CXK | 1318 |
| 30 | AEE | 1293 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223857 |
| 2 | 🇪🇸 ES | 16849 |
| 3 | 🇧🇷 BR | 15715 |
| 4 | 🇦🇺 AU | 15490 |
| 5 | 🇨🇦 CA | 15003 |
| 6 | 🇮🇹 IT | 14566 |
| 7 | 🇮🇳 IN | 14247 |
| 8 | 🇩🇪 DE | 12904 |
| 9 | 🇬🇧 GB | 12443 |
| 10 | 🇨🇴 CO | 12309 |
| 11 | 🇫🇷 FR | 10693 |
| 12 | 🇯🇵 JP | 10348 |
| 13 | 🇹🇷 TR | 8139 |
| 14 | 🇬🇷 GR | 7775 |
| 15 | 🇲🇽 MX | 7413 |
| 16 | 🇨🇭 CH | 7148 |
| 17 | 🇳🇴 NO | 6651 |
| 18 | 🇹🇭 TH | 4811 |
| 19 | 🇲🇾 MY | 4524 |
| 20 | 🇿🇦 ZA | 4492 |
| 21 | 🇵🇱 PL | 4403 |
| 22 | 🇳🇿 NZ | 3768 |
| 23 | 🇵🇭 PH | 3568 |
| 24 | 🇬🇹 GT | 3403 |
| 25 | 🇭🇷 HR | 3061 |
| 26 | 🇰🇷 KR | 3044 |
| 27 | 🇲🇦 MA | 2681 |
| 28 | 🇲🇪 ME | 2519 |
| 29 | 🇳🇱 NL | 2405 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5478 |
| 2 | Denver International Airport |  | US | 4372 |
| 3 | Indira Gandhi International Airport |  | IN | 3220 |
| 4 | Tokyo International Airport |  | JP | 3096 |
| 5 | El Dorado International Airport |  | CO | 2912 |
| 6 | Harry Reid International Airport |  | US | 2881 |
| 7 | Guaymaral Airport |  | CO | 2811 |
| 8 | Zurich Airport |  | CH | 2786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2704 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2592 |
| 11 | La Aurora Airport |  | GT | 2586 |
| 12 | Salt Lake City International Airport |  | US | 2368 |
| 13 | Chicago O'Hare International Airport |  | US | 2301 |
| 14 | Congonhas Airport |  | BR | 2288 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2202 |
| 16 | Capua Airport |  | IT | 2093 |
| 17 | Madrid Barajas International Airport |  | ES | 2069 |
| 18 | Frankfurt am Main International Airport |  | DE | 2039 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2035 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1919 |
| 22 | Charles de Gaulle International Airport |  | FR | 1908 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1883 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1882 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1787 |
| 27 | Ninoy Aquino International Airport |  | PH | 1750 |
| 28 | Charlotte/Douglas International Airport |  | US | 1680 |
| 29 | Barcelona International Airport |  | ES | 1673 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1665 |
| 31 | Viracopos International Airport |  | BR | 1625 |
| 32 | Kuala Lumpur International Airport |  | MY | 1620 |
| 33 | Seattle-Tacoma International Airport |  | US | 1575 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1572 |
| 35 | Calgary International Airport |  | CA | 1533 |
| 36 | Don Mueang International Airport |  | TH | 1524 |
| 37 | Bengaluru International Airport |  | IN | 1517 |
| 38 | Oslo Gardermoen Airport |  | NO | 1509 |
| 39 | Vancouver International Airport |  | CA | 1507 |
| 40 | Antalya International Airport |  | TR | 1433 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1008 | 21m | 244 km | 4,244.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 678 | 1h 6m | 770 km | 9,006.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 671 | 24m | 225 km | 2,603.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 443 | 44m | 555 km | 4,241.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 342 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 335 | 26m | 215 km | 1,240.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 294 | 42m | 535 km | 2,715.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 287 | 18m | 14 km | 71.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AUA21V | Austrian Airlines | Vienna International Airport (LOWW) | Frankfurt am Main International Airport (EDDF) | 2026-09-25 05:16 UTC | 2026-09-25 06:22 UTC | 1h 5m |
| CPI255 | CPI | Ciampino Airport (LIRA) | Torino / Caselle International Airport (LIMF) | 2026-09-25 05:27 UTC | 2026-09-25 06:15 UTC | 48m |
|  |  | Okadama Airport (RJCO) | Okadama Airport (RJCO) | 2026-09-25 06:00 UTC | 2026-09-25 06:02 UTC | 1m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-25 05:20 UTC | 2026-09-25 05:41 UTC | 20m |
| EZS62TJ | EZS | Geneva Cointrin International Airport (LSGG) | Nantes Atlantique Airport (LFRS) | 2026-09-25 04:35 UTC | 2026-09-25 05:40 UTC | 1h 5m |
| N904SH |  | Hector International Airport (KFAR) | Fosston Municipal/Anderson Field (KFSE) | 2026-09-25 05:21 UTC | 2026-09-25 05:38 UTC | 16m |
| OHN | OHN | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-09-25 05:12 UTC | 2026-09-25 05:36 UTC | 24m |
| UAL134 | United Airlines | Newark Liberty International Airport (KEWR) | Zurich Airport (LSZH) | 2026-09-24 22:35 UTC | 2026-09-25 05:33 UTC | 6h 57m |
| APG6229 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-09-25 05:05 UTC | 2026-09-25 05:28 UTC | 22m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-25 04:17 UTC | 2026-09-25 05:26 UTC | 1h 8m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-09-25 04:38 UTC | 2026-09-25 05:25 UTC | 46m |
| 8QTAE |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-09-25 05:19 UTC | 2026-09-25 05:23 UTC | 4m |
| RYR96SX | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Decimomannu Airport (LIED) | 2026-09-25 04:04 UTC | 2026-09-25 05:21 UTC | 1h 16m |
| T36 |  | Kuopio Airport (EFKU) | Jyvaskyla Airport (EFJY) | 2026-09-25 05:02 UTC | 2026-09-25 05:20 UTC | 17m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-09-25 04:53 UTC | 2026-09-25 05:20 UTC | 27m |
| AWA473 | AWA | VGZR (VGZR) | Bagdogra Airport (VEBD) | 2026-09-25 04:47 UTC | 2026-09-25 05:19 UTC | 32m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-09-25 04:34 UTC | 2026-09-25 05:18 UTC | 43m |
| 5YSXE |  | Nairobi Wilson Airport (HKNW) | Amboseli Airport (HKAM) | 2026-09-25 04:59 UTC | 2026-09-25 05:17 UTC | 18m |
| RYR3JZ | Ryanair | Václav Havel Airport (LKPR) | Cemovsko Polje Airport (LYPO) | 2026-09-25 04:05 UTC | 2026-09-25 05:17 UTC | 1h 11m |
| IGO479 | IndiGo | Chennai International Airport (VOMM) | Hosur Airport (VO95) | 2026-09-25 04:46 UTC | 2026-09-25 05:15 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
