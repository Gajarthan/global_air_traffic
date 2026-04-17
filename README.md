# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_22:38:32_UTC-green)

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

**Latest saved flight:** 2026-04-17 22:38:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 22:38:32 UTC

- **40,278** saved flights
- **17,202** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,278** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **485,633.3 tonnes** estimated CO2 emissions
- **28,152,653 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1692 |
| 2 | SkyWest Airlines | 1577 |
| 3 | IndiGo | 978 |
| 4 | EJA | 707 |
| 5 | American Airlines | 677 |
| 6 | Southwest Airlines | 565 |
| 7 | ENY | 520 |
| 8 | AXM | 413 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 396 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 360 |
| 13 | All Nippon Airways | 351 |
| 14 | Delta Air Lines | 344 |
| 15 | QLK | 327 |
| 16 | LXJ | 323 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 271 |
| 20 | AEE | 266 |
| 21 | easyJet | 264 |
| 22 | EJU | 262 |
| 23 | VIV | 259 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 218 |
| 28 | EDV | 216 |
| 29 | GLO | 211 |
| 30 | Cathay Pacific | 204 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32004 |
| 2 | 🇮🇳 IN | 2984 |
| 3 | 🇪🇸 ES | 2980 |
| 4 | 🇦🇺 AU | 2797 |
| 5 | 🇧🇷 BR | 2396 |
| 6 | 🇯🇵 JP | 2135 |
| 7 | 🇮🇹 IT | 2099 |
| 8 | 🇩🇪 DE | 2018 |
| 9 | 🇨🇦 CA | 1997 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1641 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1275 |
| 14 | 🇬🇷 GR | 1203 |
| 15 | 🇨🇭 CH | 1099 |
| 16 | 🇳🇴 NO | 1005 |
| 17 | 🇲🇾 MY | 1003 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 821 |
| 20 | 🇵🇭 PH | 724 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 705 |
| 23 | 🇬🇹 GT | 687 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 497 |
| 27 | 🇳🇱 NL | 405 |
| 28 | 🇲🇪 ME | 402 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 368 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 942 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 667 |
| 5 | Indira Gandhi International Airport |  | IN | 642 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 599 |
| 7 | Harry Reid International Airport |  | US | 522 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 507 |
| 10 | Zurich Airport |  | CH | 484 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 397 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 395 |
| 13 | Kuala Lumpur International Airport |  | MY | 394 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 368 |
| 17 | Madrid Barajas International Airport |  | ES | 364 |
| 18 | Charlotte/Douglas International Airport |  | US | 358 |
| 19 | Tenerife Norte Airport |  | ES | 358 |
| 20 | Frankfurt am Main International Airport |  | DE | 351 |
| 21 | Congonhas Airport |  | BR | 350 |
| 22 | Bengaluru International Airport |  | IN | 348 |
| 23 | Ninoy Aquino International Airport |  | PH | 336 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 315 |
| 26 | Salt Lake City International Airport |  | US | 310 |
| 27 | Daniel K Inouye International Airport |  | US | 301 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 278 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 277 |
| 32 | Vitoria/Foronda Airport |  | ES | 276 |
| 33 | Reno/Tahoe International Airport |  | US | 274 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Viracopos International Airport |  | BR | 247 |
| 39 | Calgary International Airport |  | CA | 245 |
| 40 | Seattle-Tacoma International Airport |  | US | 240 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 106 | 21m | 244 km | 446.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 74 | 27m | 152 km | 193.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 73 | 31m | 369 km | 464.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 64 | 52m | 556 km | 613.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 58 | 1h 53m | 1,304 km | 1,304.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAE9832 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-17 16:16 UTC | 2026-04-17 22:38 UTC | 6h 21m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-04-17 11:54 UTC | 2026-04-17 22:32 UTC | 10h 38m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-04-17 10:52 UTC | 2026-04-17 22:30 UTC | 11h 37m |
| N80896 |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-04-17 21:47 UTC | 2026-04-17 22:29 UTC | 41m |
| DTH2207 | DTH | Es Senia Airport (DAOO) | Boufarik Airport (DAAK) | 2026-04-17 22:01 UTC | 2026-04-17 22:29 UTC | 28m |
| N993DT |  | Rogue Valley International/Medford Airport (KMFR) | Siskiyou County Airport (KSIY) | 2026-04-17 21:43 UTC | 2026-04-17 22:26 UTC | 42m |
| N64RU |  | Bremerton Ntl Airport (KPWT) | Renton Municipal Airport (KRNT) | 2026-04-17 21:56 UTC | 2026-04-17 22:21 UTC | 25m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-17 22:04 UTC | 2026-04-17 22:17 UTC | 13m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-17 21:45 UTC | 2026-04-17 22:17 UTC | 31m |
| SKW9908 | SkyWest Airlines | Tucson International Airport (KTUS) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-04-17 21:31 UTC | 2026-04-17 22:10 UTC | 39m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-17 21:54 UTC | 2026-04-17 22:10 UTC | 15m |
| N450MH |  | Harrisburg International Airport (KMDT) | John F Kennedy International Airport (KJFK) | 2026-04-17 21:27 UTC | 2026-04-17 22:10 UTC | 43m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-04-17 20:17 UTC | 2026-04-17 22:09 UTC | 1h 52m |
| N975KA |  | Pierre Regional Airport (KPIR) | Wall Municipal Airport (K6V4) | 2026-04-17 21:46 UTC | 2026-04-17 22:08 UTC | 21m |
| N131JR |  | Hammond Northshore Regional Airport (KHDC) | Laurence G Hanscom Field (KBED) | 2026-04-17 19:25 UTC | 2026-04-17 22:06 UTC | 2h 41m |
| N715JR |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-17 21:28 UTC | 2026-04-17 22:01 UTC | 33m |
| EJA183 | EJA | Austin-Bergstrom International Airport (KAUS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-17 18:53 UTC | 2026-04-17 21:59 UTC | 3h 5m |
| N441WF |  | Centennial Airport (KAPA) | Idlers Field (CO84) | 2026-04-17 21:32 UTC | 2026-04-17 21:57 UTC | 25m |
| N4347R |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-17 21:56 UTC | 2026-04-17 21:57 UTC | 0m |
| N594AF |  | Laguardia Airport (KLGA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 21:20 UTC | 2026-04-17 21:56 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
