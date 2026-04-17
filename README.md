# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_05:34:14_UTC-green)

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

**Latest saved flight:** 2026-04-17 05:34:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 05:34:14 UTC

- **38,478** saved flights
- **16,591** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,478** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **465,009.2 tonnes** estimated CO2 emissions
- **26,957,056 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1610 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 942 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 406 |
| 9 | LATAM Airlines | 386 |
| 10 | Lufthansa | 385 |
| 11 | Vueling | 385 |
| 12 | AZU | 343 |
| 13 | All Nippon Airways | 341 |
| 14 | Delta Air Lines | 326 |
| 15 | QLK | 321 |
| 16 | LXJ | 309 |
| 17 | WIF | 288 |
| 18 | Swiss International | 284 |
| 19 | Alaska Airlines | 257 |
| 20 | AEE | 256 |
| 21 | easyJet | 250 |
| 22 | EJU | 249 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 231 |
| 25 | Air France | 215 |
| 26 | EDV | 212 |
| 27 | United Airlines | 211 |
| 28 | GLO | 200 |
| 29 | AIQ | 199 |
| 30 | JetBlue | 199 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30416 |
| 2 | 🇮🇳 IN | 2883 |
| 3 | 🇪🇸 ES | 2835 |
| 4 | 🇦🇺 AU | 2737 |
| 5 | 🇧🇷 BR | 2263 |
| 6 | 🇯🇵 JP | 2075 |
| 7 | 🇮🇹 IT | 2016 |
| 8 | 🇩🇪 DE | 1946 |
| 9 | 🇨🇴 CO | 1898 |
| 10 | 🇨🇦 CA | 1896 |
| 11 | 🇬🇧 GB | 1573 |
| 12 | 🇫🇷 FR | 1447 |
| 13 | 🇲🇽 MX | 1216 |
| 14 | 🇬🇷 GR | 1155 |
| 15 | 🇨🇭 CH | 1040 |
| 16 | 🇲🇾 MY | 978 |
| 17 | 🇳🇴 NO | 924 |
| 18 | 🇳🇿 NZ | 805 |
| 19 | 🇿🇦 ZA | 799 |
| 20 | 🇵🇭 PH | 712 |
| 21 | 🇹🇭 TH | 702 |
| 22 | 🇹🇷 TR | 686 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 632 |
| 25 | 🇵🇱 PL | 597 |
| 26 | 🇲🇦 MA | 477 |
| 27 | 🇳🇱 NL | 382 |
| 28 | 🇲🇪 ME | 377 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 360 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 706 |
| 3 | El Dorado International Airport |  | CO | 669 |
| 4 | Denver International Airport |  | US | 648 |
| 5 | Indira Gandhi International Airport |  | IN | 623 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 571 |
| 7 | Harry Reid International Airport |  | US | 506 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 459 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 12 | Kuala Lumpur International Airport |  | MY | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 373 |
| 15 | Chicago O'Hare International Airport |  | US | 372 |
| 16 | Macau International Airport |  | MO | 354 |
| 17 | Madrid Barajas International Airport |  | ES | 347 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Congonhas Airport |  | BR | 334 |
| 22 | Bengaluru International Airport |  | IN | 332 |
| 23 | Ninoy Aquino International Airport |  | PH | 331 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 292 |
| 27 | Daniel K Inouye International Airport |  | US | 286 |
| 28 | Charles de Gaulle International Airport |  | FR | 282 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 272 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Vitoria/Foronda Airport |  | ES | 260 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 246 |
| 38 | Don Mueang International Airport |  | TH | 237 |
| 39 | Viracopos International Airport |  | BR | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 177 | 1h 8m | 706 km | 2,155.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 139 | 24m | 225 km | 539.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 110 | 1h 27m | 910 km | 1,726.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 97 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 96 | 21m | 244 km | 404.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 87 | 26m | 275 km | 412.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 83 | 54m | 546 km | 781.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 78 | 1h 11m | 770 km | 1,036.2 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 74 | 45m | 452 km | 576.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 23 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
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
| ANA991 | All Nippon Airways | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-17 04:54 UTC | 2026-04-17 05:34 UTC | 39m |
| R21235 |  | Moen's Ranch Airport (AK52) | Ladd Army Air Field (PAFB) | 2026-04-17 05:11 UTC | 2026-04-17 05:24 UTC | 12m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-16 14:56 UTC | 2026-04-17 05:23 UTC | 14h 26m |
| ZGU | ZGU | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-17 04:53 UTC | 2026-04-17 05:14 UTC | 21m |
| CCA437 | Air China | Ramechhap Airport (VNRC) | Tribhuvan International Airport (VNKT) | 2026-04-17 04:38 UTC | 2026-04-17 04:59 UTC | 21m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-17 04:38 UTC | 2026-04-17 04:55 UTC | 17m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-17 04:25 UTC | 2026-04-17 04:49 UTC | 23m |
| COUGR32 | COU | Sanderson Field (KSHN) | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | 2026-04-17 04:33 UTC | 2026-04-17 04:45 UTC | 12m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-04-17 04:24 UTC | 2026-04-17 04:41 UTC | 17m |
| AXM711 | AXM | Kuala Lumpur International Airport (WMKK) | Senai International Airport (WMKJ) | 2026-04-17 04:08 UTC | 2026-04-17 04:40 UTC | 31m |
| SWR2EY | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-04-17 04:07 UTC | 2026-04-17 04:37 UTC | 30m |
| JST765 | JST | Adelaide International Airport (YPAD) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-17 03:10 UTC | 2026-04-17 04:36 UTC | 1h 25m |
| JAL225 | Japan Airlines | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-17 03:55 UTC | 2026-04-17 04:34 UTC | 38m |
| AZU4411 | AZU | Fazenda Baluarte Airport (SJBU) | Benedito Mutran Airport (SIBD) | 2026-04-17 03:01 UTC | 2026-04-17 04:33 UTC | 1h 32m |
| RYR292Q | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Tortoli' / Arbatax Airport (LIET) | 2026-04-17 03:57 UTC | 2026-04-17 04:31 UTC | 33m |
| AFL1531 | AFL | Bogashevo Airport (UNTT) | Oktyabrskiy Airport (UWUK) | 2026-04-17 01:53 UTC | 2026-04-17 04:30 UTC | 2h 37m |
| BLVE | BLV | Shek Kong Air Base (VHSK) | Shek Kong Air Base (VHSK) | 2026-04-17 04:11 UTC | 2026-04-17 04:30 UTC | 18m |
| FKT | FKT | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-04-17 04:18 UTC | 2026-04-17 04:30 UTC | 12m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-17 04:23 UTC | 2026-04-17 04:30 UTC | 6m |
| AAY32 | AAY | Harry Reid International Airport (KLAS) | Harris River Ranch Airport (9CA7) | 2026-04-17 03:45 UTC | 2026-04-17 04:28 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
