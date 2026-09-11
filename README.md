# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_20:18:04_UTC-green)

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

**Latest saved flight:** 2026-09-11 20:18:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 20:18:04 UTC

- **255,305** saved flights
- **76,221** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,305** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,081,542.7 tonnes** estimated CO2 emissions
- **178,640,156 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10177 |
| 2 | SkyWest Airlines | 8898 |
| 3 | EJA | 4931 |
| 4 | IndiGo | 4273 |
| 5 | American Airlines | 4047 |
| 6 | Southwest Airlines | 3759 |
| 7 | Delta Air Lines | 3201 |
| 8 | ENY | 3035 |
| 9 | LATAM Airlines | 2461 |
| 10 | AZU | 2379 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2053 |
| 13 | Lufthansa | 2000 |
| 14 | LXJ | 1994 |
| 15 | easyJet | 1740 |
| 16 | Swiss International | 1711 |
| 17 | QLK | 1646 |
| 18 | AXM | 1638 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1585 |
| 21 | Alaska Airlines | 1517 |
| 22 | All Nippon Airways | 1489 |
| 23 | WMT | 1443 |
| 24 | GLO | 1421 |
| 25 | PGT | 1406 |
| 26 | VIV | 1396 |
| 27 | Air France | 1394 |
| 28 | Wizz Air | 1389 |
| 29 | JetBlue | 1240 |
| 30 | TKR | 1239 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211987 |
| 2 | 🇪🇸 ES | 16251 |
| 3 | 🇧🇷 BR | 14908 |
| 4 | 🇦🇺 AU | 14555 |
| 5 | 🇨🇦 CA | 14208 |
| 6 | 🇮🇹 IT | 13959 |
| 7 | 🇮🇳 IN | 13385 |
| 8 | 🇩🇪 DE | 12470 |
| 9 | 🇬🇧 GB | 11923 |
| 10 | 🇨🇴 CO | 11354 |
| 11 | 🇫🇷 FR | 10259 |
| 12 | 🇯🇵 JP | 9980 |
| 13 | 🇹🇷 TR | 7650 |
| 14 | 🇬🇷 GR | 7451 |
| 15 | 🇲🇽 MX | 7038 |
| 16 | 🇨🇭 CH | 6853 |
| 17 | 🇳🇴 NO | 6339 |
| 18 | 🇹🇭 TH | 4589 |
| 19 | 🇲🇾 MY | 4405 |
| 20 | 🇿🇦 ZA | 4354 |
| 21 | 🇵🇱 PL | 4233 |
| 22 | 🇳🇿 NZ | 3513 |
| 23 | 🇵🇭 PH | 3441 |
| 24 | 🇬🇹 GT | 3191 |
| 25 | 🇰🇷 KR | 2931 |
| 26 | 🇭🇷 HR | 2925 |
| 27 | 🇲🇦 MA | 2575 |
| 28 | 🇲🇪 ME | 2400 |
| 29 | 🇳🇱 NL | 2298 |
| 30 | 🇮🇩 ID | 2175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5240 |
| 2 | Denver International Airport |  | US | 4123 |
| 3 | Indira Gandhi International Airport |  | IN | 3085 |
| 4 | Tokyo International Airport |  | JP | 2979 |
| 5 | Guaymaral Airport |  | CO | 2758 |
| 6 | Harry Reid International Airport |  | US | 2702 |
| 7 | Zurich Airport |  | CH | 2674 |
| 8 | El Dorado International Airport |  | CO | 2624 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2579 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2500 |
| 11 | La Aurora Airport |  | GT | 2433 |
| 12 | Salt Lake City International Airport |  | US | 2251 |
| 13 | Chicago O'Hare International Airport |  | US | 2223 |
| 14 | Congonhas Airport |  | BR | 2189 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2089 |
| 16 | Capua Airport |  | IT | 2013 |
| 17 | Madrid Barajas International Airport |  | ES | 1994 |
| 18 | Frankfurt am Main International Airport |  | DE | 1974 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1914 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1847 |
| 21 | Malpensa International Airport |  | IT | 1834 |
| 22 | Charles de Gaulle International Airport |  | FR | 1798 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1791 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1775 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1717 |
| 26 | Macau International Airport |  | MO | 1689 |
| 27 | Ninoy Aquino International Airport |  | PH | 1682 |
| 28 | Barcelona International Airport |  | ES | 1606 |
| 29 | Charlotte/Douglas International Airport |  | US | 1601 |
| 30 | Kuala Lumpur International Airport |  | MY | 1586 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1569 |
| 32 | Viracopos International Airport |  | BR | 1527 |
| 33 | Seattle-Tacoma International Airport |  | US | 1497 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1482 |
| 35 | Don Mueang International Airport |  | TH | 1469 |
| 36 | Calgary International Airport |  | CA | 1468 |
| 37 | Bengaluru International Airport |  | IN | 1450 |
| 38 | Oslo Gardermoen Airport |  | NO | 1445 |
| 39 | Vancouver International Airport |  | CA | 1431 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 948 | 21m | 244 km | 3,991.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 683 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 639 | 1h 6m | 770 km | 8,488.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 408 | 44m | 555 km | 3,906.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 386 | 44m | 241 km | 1,603.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 355 | 24m | 218 km | 1,337.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 312 | 19m | 99 km | 534.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 303 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 293 | 1h 14m | 961 km | 4,856.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 263 | 28m | 152 km | 687.3 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JOLLY96 | JOL | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-09-11 19:21 UTC | 2026-09-11 20:18 UTC | 56m |
| N26CF |  | Johnson Airport (3AK4) | Trading Bay Production Airport (5AK0) | 2026-09-11 20:00 UTC | 2026-09-11 20:11 UTC | 10m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-09-11 05:48 UTC | 2026-09-11 20:07 UTC | 14h 18m |
| N468LA |  | Brackett Field (KPOC) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-11 19:29 UTC | 2026-09-11 20:07 UTC | 38m |
| N96598 |  | Mountain View Wilcox Memorial Field (K7M2) | Jonesboro Municipal Airport (KJBR) | 2026-09-11 19:36 UTC | 2026-09-11 20:07 UTC | 30m |
| N9262H |  | Pearson Field (KVUO) | Portland-Troutdale Airport (KTTD) | 2026-09-11 19:34 UTC | 2026-09-11 20:06 UTC | 31m |
| THY9XH | Turkish Airlines | Helsinki Vantaa Airport (EFHK) | Istanbul Hezarfen Airfield (LTBW) | 2026-09-11 16:49 UTC | 2026-09-11 20:04 UTC | 3h 15m |
| HKE623 | HKE | Tokyo International Airport (RJTT) | Chek Lap Kok International Airport (VHHH) | 2026-09-11 16:15 UTC | 2026-09-11 20:03 UTC | 3h 47m |
| N955CA |  | Lake In The Hills Airport (K3CK) | J Maddock Airport (IL38) | 2026-09-11 19:18 UTC | 2026-09-11 20:01 UTC | 42m |
| UPS99 | UPS | Incheon International Airport (RKSI) | Ted Stevens Anchorage International Airport (PANC) | 2026-09-11 13:05 UTC | 2026-09-11 20:00 UTC | 6h 55m |
| EPIC43 | EPI | New York Stewart International Airport (KSWF) | New York Stewart International Airport (KSWF) | 2026-09-11 19:35 UTC | 2026-09-11 19:59 UTC | 24m |
| BOX714 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-09-11 13:01 UTC | 2026-09-11 19:57 UTC | 6h 56m |
| N884SW |  | Carson City Airport (KCXP) | Darrow Field (26NV) | 2026-09-11 19:43 UTC | 2026-09-11 19:57 UTC | 14m |
| TGCYC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-09-11 19:34 UTC | 2026-09-11 19:56 UTC | 21m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-09-11 05:47 UTC | 2026-09-11 19:55 UTC | 14h 8m |
| LS23 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-11 17:29 UTC | 2026-09-11 19:54 UTC | 2h 25m |
| N99DQ |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-09-11 19:35 UTC | 2026-09-11 19:50 UTC | 15m |
| N836E |  | Laconia Municipal Airport (KLCI) | Portsmouth International At Pease Airport (KPSM) | 2026-09-11 19:32 UTC | 2026-09-11 19:49 UTC | 17m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-11 19:15 UTC | 2026-09-11 19:49 UTC | 34m |
| N319TB |  | Anderson Regional Airport (KAND) | Scott Municipal Airport (KSCX) | 2026-09-11 19:09 UTC | 2026-09-11 19:48 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
