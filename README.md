# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_03:14:03_UTC-green)

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

**Latest saved flight:** 2026-04-17 03:14:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 03:14:03 UTC

- **38,402** saved flights
- **16,577** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,402** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **464,108.5 tonnes** estimated CO2 emissions
- **26,904,840 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1608 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 936 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 401 |
| 9 | LATAM Airlines | 386 |
| 10 | Lufthansa | 385 |
| 11 | Vueling | 385 |
| 12 | AZU | 342 |
| 13 | All Nippon Airways | 339 |
| 14 | Delta Air Lines | 326 |
| 15 | QLK | 319 |
| 16 | LXJ | 309 |
| 17 | WIF | 287 |
| 18 | Swiss International | 283 |
| 19 | Alaska Airlines | 256 |
| 20 | AEE | 254 |
| 21 | easyJet | 250 |
| 22 | EJU | 249 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 229 |
| 25 | Air France | 215 |
| 26 | EDV | 212 |
| 27 | United Airlines | 211 |
| 28 | GLO | 200 |
| 29 | AIQ | 199 |
| 30 | JetBlue | 199 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30392 |
| 2 | 🇮🇳 IN | 2872 |
| 3 | 🇪🇸 ES | 2835 |
| 4 | 🇦🇺 AU | 2704 |
| 5 | 🇧🇷 BR | 2261 |
| 6 | 🇯🇵 JP | 2063 |
| 7 | 🇮🇹 IT | 2014 |
| 8 | 🇩🇪 DE | 1946 |
| 9 | 🇨🇴 CO | 1896 |
| 10 | 🇨🇦 CA | 1892 |
| 11 | 🇬🇧 GB | 1573 |
| 12 | 🇫🇷 FR | 1447 |
| 13 | 🇲🇽 MX | 1216 |
| 14 | 🇬🇷 GR | 1149 |
| 15 | 🇨🇭 CH | 1038 |
| 16 | 🇲🇾 MY | 967 |
| 17 | 🇳🇴 NO | 923 |
| 18 | 🇳🇿 NZ | 802 |
| 19 | 🇿🇦 ZA | 799 |
| 20 | 🇵🇭 PH | 710 |
| 21 | 🇹🇭 TH | 694 |
| 22 | 🇹🇷 TR | 685 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 597 |
| 26 | 🇲🇦 MA | 477 |
| 27 | 🇳🇱 NL | 382 |
| 28 | 🇲🇪 ME | 377 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 358 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 702 |
| 3 | El Dorado International Airport |  | CO | 668 |
| 4 | Denver International Airport |  | US | 647 |
| 5 | Indira Gandhi International Airport |  | IN | 620 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 568 |
| 7 | Harry Reid International Airport |  | US | 505 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 458 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 13 | Kuala Lumpur International Airport |  | MY | 377 |
| 14 | Chicago O'Hare International Airport |  | US | 372 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 370 |
| 16 | Macau International Airport |  | MO | 353 |
| 17 | Madrid Barajas International Airport |  | ES | 347 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Congonhas Airport |  | BR | 334 |
| 22 | Bengaluru International Airport |  | IN | 331 |
| 23 | Ninoy Aquino International Airport |  | PH | 330 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 292 |
| 27 | Daniel K Inouye International Airport |  | US | 286 |
| 28 | Charles de Gaulle International Airport |  | FR | 282 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 270 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Vitoria/Foronda Airport |  | ES | 260 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 246 |
| 38 | Don Mueang International Airport |  | TH | 237 |
| 39 | Viracopos International Airport |  | BR | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 232 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 177 | 1h 8m | 706 km | 2,155.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 138 | 24m | 225 km | 535.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 110 | 1h 27m | 910 km | 1,726.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 97 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 96 | 21m | 244 km | 404.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 87 | 26m | 275 km | 412.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 78 | 1h 11m | 770 km | 1,036.2 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 73 | 45m | 452 km | 568.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 58 | 13m | 99 km | 99.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 57 | 1h 41m | 1,423 km | 1,398.9 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 56 | 26m | 215 km | 207.4 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 29 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 53 | 1h 21m | 961 km | 878.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU31 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | AZ86 (AZ86) | 2026-04-17 02:45 UTC | 2026-04-17 03:14 UTC | 29m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-17 02:46 UTC | 2026-04-17 03:06 UTC | 20m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-17 02:37 UTC | 2026-04-17 03:04 UTC | 27m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-17 02:41 UTC | 2026-04-17 02:53 UTC | 12m |
| CPA2014 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-04-16 16:10 UTC | 2026-04-17 02:53 UTC | 10h 43m |
| SWA2257 | Southwest Airlines | Harry Reid International Airport (KLAS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-17 01:45 UTC | 2026-04-17 02:52 UTC | 1h 7m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-17 02:19 UTC | 2026-04-17 02:50 UTC | 31m |
| XSN82 | XSN | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-04-17 02:07 UTC | 2026-04-17 02:48 UTC | 40m |
| YEL4 | YEL | Norman Y Mineta San Jose International Airport (KSJC) | Madera Municipal Airport (KMAE) | 2026-04-17 02:29 UTC | 2026-04-17 02:47 UTC | 18m |
| ERU13 | ERU | Robin Airport (59AZ) | Big Springs Ranch Airport (AZ27) | 2026-04-17 02:34 UTC | 2026-04-17 02:44 UTC | 10m |
| OUA23 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Neversweat Airport (1OK0) | 2026-04-17 02:07 UTC | 2026-04-17 02:43 UTC | 35m |
| CITT49 | CIT | Colonel James Jabara Airport (KAAO) | Colonel James Jabara Airport (KAAO) | 2026-04-17 02:27 UTC | 2026-04-17 02:40 UTC | 12m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-17 02:08 UTC | 2026-04-17 02:39 UTC | 30m |
| TOG132 | TOG | Redding Regional Airport (KRDD) | Hayfork Airport (KF62) | 2026-04-17 02:21 UTC | 2026-04-17 02:35 UTC | 14m |
| SKW5047 | SkyWest Airlines | Denver International Airport (KDEN) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-04-17 02:16 UTC | 2026-04-17 02:35 UTC | 19m |
| SLI871 | SLI | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-17 01:55 UTC | 2026-04-17 02:33 UTC | 38m |
| N911UW |  | Loeber Mcdaniel Field (WI50) | Dane County Regional/Truax Field (KMSN) | 2026-04-17 02:11 UTC | 2026-04-17 02:25 UTC | 14m |
| N244JE |  | San Fernando Airport (SADF) | SUGA (SUGA) | 2026-04-17 02:02 UTC | 2026-04-17 02:24 UTC | 22m |
| IGO960C | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Kamalpur Airport (VEKM) | 2026-04-17 01:51 UTC | 2026-04-17 02:24 UTC | 32m |
| AWA411 | AWA | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-04-17 01:56 UTC | 2026-04-17 02:22 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
