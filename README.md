# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_06:35:21_UTC-green)

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

**Latest saved flight:** 2026-04-18 06:35:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 06:35:21 UTC

- **40,645** saved flights
- **17,289** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,645** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **489,313.3 tonnes** estimated CO2 emissions
- **28,365,990 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1695 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 992 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 422 |
| 9 | Vueling | 402 |
| 10 | LATAM Airlines | 400 |
| 11 | Lufthansa | 388 |
| 12 | All Nippon Airways | 362 |
| 13 | AZU | 361 |
| 14 | Delta Air Lines | 347 |
| 15 | QLK | 338 |
| 16 | LXJ | 325 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 274 |
| 20 | AEE | 270 |
| 21 | easyJet | 264 |
| 22 | VIV | 264 |
| 23 | EJU | 262 |
| 24 | Japan Airlines | 249 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 206 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32279 |
| 2 | 🇮🇳 IN | 3026 |
| 3 | 🇪🇸 ES | 2985 |
| 4 | 🇦🇺 AU | 2882 |
| 5 | 🇧🇷 BR | 2409 |
| 6 | 🇯🇵 JP | 2207 |
| 7 | 🇮🇹 IT | 2100 |
| 8 | 🇩🇪 DE | 2027 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1641 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1216 |
| 15 | 🇨🇭 CH | 1100 |
| 16 | 🇲🇾 MY | 1026 |
| 17 | 🇳🇴 NO | 1005 |
| 18 | 🇳🇿 NZ | 844 |
| 19 | 🇿🇦 ZA | 827 |
| 20 | 🇵🇭 PH | 740 |
| 21 | 🇹🇭 TH | 720 |
| 22 | 🇹🇷 TR | 707 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 660 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 500 |
| 27 | 🇳🇱 NL | 407 |
| 28 | 🇲🇪 ME | 404 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 371 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 752 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 677 |
| 5 | Indira Gandhi International Airport |  | IN | 652 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 605 |
| 7 | Harry Reid International Airport |  | US | 529 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 485 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 12 | Kuala Lumpur International Airport |  | MY | 402 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 389 |
| 16 | Macau International Airport |  | MO | 371 |
| 17 | Madrid Barajas International Airport |  | ES | 366 |
| 18 | Charlotte/Douglas International Airport |  | US | 358 |
| 19 | Tenerife Norte Airport |  | ES | 358 |
| 20 | Bengaluru International Airport |  | IN | 355 |
| 21 | Frankfurt am Main International Airport |  | DE | 353 |
| 22 | Congonhas Airport |  | BR | 353 |
| 23 | Ninoy Aquino International Airport |  | PH | 344 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 305 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 291 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 281 |
| 32 | Reno/Tahoe International Airport |  | US | 279 |
| 33 | Vitoria/Foronda Airport |  | ES | 278 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Calgary International Airport |  | CA | 247 |
| 39 | Viracopos International Airport |  | BR | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 188 | 1h 8m | 706 km | 2,288.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 147 | 24m | 225 km | 570.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 118 | 28m | 304 km | 618.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 116 | 1h 27m | 910 km | 1,820.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 108 | 21m | 244 km | 454.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 108 | 19m | 165 km | 307.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 106 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 94 | 26m | 275 km | 445.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 87 | 54m | 546 km | 819.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 82 | 44m | 452 km | 639.1 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 74 | 31m | 369 km | 471.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 63 | 20m | 147 km | 159.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 62 | 1h 41m | 1,423 km | 1,521.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 57 | 59m | 695 km | 683.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ALFT5 | ALF | Windsock Airport (4WA4) | Boeing Field/King County International Airport (KBFI) | 2026-04-18 06:02 UTC | 2026-04-18 06:35 UTC | 33m |
| N334CA |  | Bisbee Douglas International Airport (KDUG) | Douglas Municipal Airport (KDGL) | 2026-04-18 06:09 UTC | 2026-04-18 06:35 UTC | 25m |
| N874BU |  | Hidden River Airport (22FA) | Peter O Knight Airport (KTPF) | 2026-04-18 06:08 UTC | 2026-04-18 06:29 UTC | 21m |
| POLICER | POL | Hoefen Airport (LOIR) | Hoefen Airport (LOIR) | 2026-04-18 06:13 UTC | 2026-04-18 06:29 UTC | 16m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-18 06:07 UTC | 2026-04-18 06:28 UTC | 21m |
| ZKIWD | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-18 06:09 UTC | 2026-04-18 06:28 UTC | 18m |
| JA94NH |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-04-18 05:42 UTC | 2026-04-18 06:04 UTC | 21m |
| POLICER | POL | Hoefen Airport (LOIR) | Hoefen Airport (LOIR) | 2026-04-18 05:39 UTC | 2026-04-18 05:58 UTC | 19m |
| N69P |  | Montgomery-Gibbs Executive Airport (KMYF) | Jacqueline Cochran Regional Airport (KTRM) | 2026-04-18 05:36 UTC | 2026-04-18 05:56 UTC | 19m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-18 05:17 UTC | 2026-04-18 05:50 UTC | 32m |
| KLM70B | KLM Royal Dutch | Václav Havel Airport (LKPR) | Lelystad Airport (EHLE) | 2026-04-18 04:30 UTC | 2026-04-18 05:48 UTC | 1h 17m |
| N694AM |  | Mojave Air & Space Port/Rutan Field (KMHV) | Kelso Valley Airport (CN37) | 2026-04-18 05:37 UTC | 2026-04-18 05:47 UTC | 10m |
| RAM578 | Royal Air Maroc | Banjul International Airport (GBYD) | Beni Mellal Airport (GMMD) | 2026-04-18 02:55 UTC | 2026-04-18 05:46 UTC | 2h 50m |
| RYR6612 | Ryanair | Madrid Barajas International Airport (LEMD) | Ifrane Airport (GMFI) | 2026-04-18 04:42 UTC | 2026-04-18 05:45 UTC | 1h 3m |
| NLQ | NLQ | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-18 05:11 UTC | 2026-04-18 05:45 UTC | 33m |
| ROT703E | ROT | Henri Coanda International Airport (LROP) | Suceava Stefan cel Mare Airport (LRSV) | 2026-04-18 05:07 UTC | 2026-04-18 05:44 UTC | 37m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-18 05:21 UTC | 2026-04-18 05:34 UTC | 13m |
| SNJ35 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-18 04:02 UTC | 2026-04-18 05:33 UTC | 1h 31m |
| UBG145 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-18 04:58 UTC | 2026-04-18 05:31 UTC | 33m |
| AZU4411 | AZU | Fazenda Baluarte Airport (SJBU) | Frisama Eldorado Airport (SJHL) | 2026-04-18 03:53 UTC | 2026-04-18 05:30 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
