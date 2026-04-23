# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_16:55:12_UTC-green)

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

**Latest saved flight:** 2026-04-23 16:55:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 16:55:12 UTC

- **49,952** saved flights
- **20,126** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,952** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **596,276.1 tonnes** estimated CO2 emissions
- **34,566,728 km** total distance flown
- **831 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2118 |
| 2 | SkyWest Airlines | 1906 |
| 3 | IndiGo | 1167 |
| 4 | EJA | 857 |
| 5 | American Airlines | 811 |
| 6 | Southwest Airlines | 704 |
| 7 | ENY | 640 |
| 8 | Lufthansa | 580 |
| 9 | Vueling | 497 |
| 10 | AXM | 495 |
| 11 | LATAM Airlines | 487 |
| 12 | All Nippon Airways | 455 |
| 13 | AZU | 424 |
| 14 | WIF | 416 |
| 15 | Delta Air Lines | 410 |
| 16 | QLK | 404 |
| 17 | LXJ | 378 |
| 18 | Swiss International | 376 |
| 19 | AEE | 341 |
| 20 | Alaska Airlines | 330 |
| 21 | EJU | 323 |
| 22 | easyJet | 316 |
| 23 | VIV | 315 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 284 |
| 26 | AXB | 268 |
| 27 | JetBlue | 262 |
| 28 | United Airlines | 260 |
| 29 | Cathay Pacific | 259 |
| 30 | AIQ | 256 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39567 |
| 2 | 🇮🇳 IN | 3663 |
| 3 | 🇪🇸 ES | 3617 |
| 4 | 🇦🇺 AU | 3471 |
| 5 | 🇧🇷 BR | 2902 |
| 6 | 🇯🇵 JP | 2739 |
| 7 | 🇮🇹 IT | 2691 |
| 8 | 🇩🇪 DE | 2670 |
| 9 | 🇨🇦 CA | 2473 |
| 10 | 🇨🇴 CO | 2320 |
| 11 | 🇬🇧 GB | 2060 |
| 12 | 🇫🇷 FR | 1918 |
| 13 | 🇲🇽 MX | 1539 |
| 14 | 🇬🇷 GR | 1525 |
| 15 | 🇨🇭 CH | 1383 |
| 16 | 🇳🇴 NO | 1340 |
| 17 | 🇲🇾 MY | 1207 |
| 18 | 🇿🇦 ZA | 1030 |
| 19 | 🇳🇿 NZ | 956 |
| 20 | 🇹🇭 TH | 914 |
| 21 | 🇹🇷 TR | 885 |
| 22 | 🇵🇭 PH | 872 |
| 23 | 🇰🇷 KR | 827 |
| 24 | 🇵🇱 PL | 807 |
| 25 | 🇬🇹 GT | 762 |
| 26 | 🇲🇦 MA | 614 |
| 27 | 🇲🇪 ME | 535 |
| 28 | 🇳🇱 NL | 506 |
| 29 | 🇲🇴 MO | 460 |
| 30 | 🇧🇸 BS | 439 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1158 |
| 2 | Tokyo International Airport |  | JP | 930 |
| 3 | Denver International Airport |  | US | 829 |
| 4 | El Dorado International Airport |  | CO | 795 |
| 5 | Indira Gandhi International Airport |  | IN | 782 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 754 |
| 7 | Guaymaral Airport |  | CO | 678 |
| 8 | Harry Reid International Airport |  | US | 646 |
| 9 | Zurich Airport |  | CH | 586 |
| 10 | La Aurora Airport |  | GT | 567 |
| 11 | Frankfurt am Main International Airport |  | DE | 559 |
| 12 | Chicago O'Hare International Airport |  | US | 490 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 488 |
| 14 | Kuala Lumpur International Airport |  | MY | 482 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 473 |
| 16 | Macau International Airport |  | MO | 460 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 18 | Madrid Barajas International Airport |  | ES | 456 |
| 19 | Bengaluru International Airport |  | IN | 438 |
| 20 | Charlotte/Douglas International Airport |  | US | 419 |
| 21 | Congonhas Airport |  | BR | 416 |
| 22 | Malpensa International Airport |  | IT | 412 |
| 23 | Tenerife Norte Airport |  | ES | 406 |
| 24 | Ninoy Aquino International Airport |  | PH | 402 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 379 |
| 26 | Charles de Gaulle International Airport |  | FR | 374 |
| 27 | Salt Lake City International Airport |  | US | 372 |
| 28 | Daniel K Inouye International Airport |  | US | 369 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 339 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 339 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 338 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 335 |
| 35 | Reno/Tahoe International Airport |  | US | 330 |
| 36 | Barcelona International Airport |  | ES | 330 |
| 37 | O. R. Tambo International Airport |  | ZA | 329 |
| 38 | Don Mueang International Airport |  | TH | 311 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 295 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 274 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 235 | 1h 7m | 706 km | 2,861.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 192 | 14m | 114 km | 376.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 150 | 21m | 244 km | 631.6 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 149 | 28m | 304 km | 781.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 103 | 44m | 452 km | 802.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 85 | 20m | 250 km | 367.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 77 | 52m | 556 km | 738.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 70 | 1h 0m | 695 km | 839.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 66 | 11m | 15 km | 17.4 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK415 | CXK | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-04-23 16:36 UTC | 2026-04-23 16:55 UTC | 19m |
| GKA263 | GKA | Laurinburg/Maxton Airport (KMEB) | Laurinburg/Maxton Airport (KMEB) | 2026-04-23 16:39 UTC | 2026-04-23 16:51 UTC | 12m |
| OOMPL | OOM | Antwerp International Airport (Deurne) (EBAW) | Kiewit Airport (EBZH) | 2026-04-23 16:21 UTC | 2026-04-23 16:48 UTC | 27m |
| N385L |  | Indianapolis International Airport (KIND) | Louisville Muhammad Ali International Airport (KSDF) | 2026-04-23 16:03 UTC | 2026-04-23 16:45 UTC | 41m |
| N461FA |  | Wilkes-Barre/Scranton International Airport (KAVP) | Lancaster Airport (KLNS) | 2026-04-23 15:58 UTC | 2026-04-23 16:41 UTC | 43m |
| PDU81 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-23 15:57 UTC | 2026-04-23 16:38 UTC | 40m |
| OEGRB | OEG | Stuttgart Airport (EDDS) | Cologne Bonn Airport (EDDK) | 2026-04-23 16:04 UTC | 2026-04-23 16:36 UTC | 31m |
| BURNY37 | BUR | Wichita Valley Airport (KF14) | Mc Neill Ranch Airport (6TE7) | 2026-04-23 16:09 UTC | 2026-04-23 16:33 UTC | 23m |
| N800WE |  | PN21 (PN21) | Tall Pines Airfield (6PA8) | 2026-04-23 11:59 UTC | 2026-04-23 16:32 UTC | 4h 33m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-23 15:06 UTC | 2026-04-23 16:31 UTC | 1h 24m |
| N118UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-04-23 16:15 UTC | 2026-04-23 16:29 UTC | 13m |
| PNC0216 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-23 15:17 UTC | 2026-04-23 16:26 UTC | 1h 8m |
| N792GE |  | Big Sandy Airport (AZ71) | Moreton Airpark (23AZ) | 2026-04-23 16:09 UTC | 2026-04-23 16:22 UTC | 12m |
| LFA536 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Executive Airport (KORL) | 2026-04-23 15:53 UTC | 2026-04-23 16:20 UTC | 27m |
| N158PT |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-04-23 16:05 UTC | 2026-04-23 16:19 UTC | 13m |
| XABNT | XAB | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-04-23 16:14 UTC | 2026-04-23 16:18 UTC | 4m |
| UAL2742 | United Airlines | Joe Foss Field (KFSD) | Denver International Airport (KDEN) | 2026-04-23 14:51 UTC | 2026-04-23 16:16 UTC | 1h 24m |
| EJA551 | EJA | Manhattan Regional Airport (KMHK) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-23 14:35 UTC | 2026-04-23 16:15 UTC | 1h 40m |
| AAH552 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-04-23 15:51 UTC | 2026-04-23 16:12 UTC | 21m |
| N220JA |  | West Virginia International Yeager Airport (KCRW) | WV71 (WV71) | 2026-04-23 15:45 UTC | 2026-04-23 16:12 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
