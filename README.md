# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_11:48:38_UTC-green)

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

**Latest saved flight:** 2026-04-22 11:48:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 11:48:38 UTC

- **47,826** saved flights
- **19,471** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,826** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **575,194.2 tonnes** estimated CO2 emissions
- **33,344,588 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2035 |
| 2 | SkyWest Airlines | 1846 |
| 3 | IndiGo | 1127 |
| 4 | EJA | 819 |
| 5 | American Airlines | 790 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 620 |
| 8 | Lufthansa | 526 |
| 9 | AXM | 481 |
| 10 | Vueling | 478 |
| 11 | LATAM Airlines | 468 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 408 |
| 14 | Delta Air Lines | 396 |
| 15 | QLK | 386 |
| 16 | WIF | 384 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 365 |
| 19 | AEE | 324 |
| 20 | Alaska Airlines | 323 |
| 21 | EJU | 317 |
| 22 | easyJet | 305 |
| 23 | VIV | 304 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 269 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 253 |
| 28 | JetBlue | 252 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 242 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37915 |
| 2 | 🇮🇳 IN | 3508 |
| 3 | 🇪🇸 ES | 3470 |
| 4 | 🇦🇺 AU | 3313 |
| 5 | 🇧🇷 BR | 2797 |
| 6 | 🇯🇵 JP | 2644 |
| 7 | 🇮🇹 IT | 2602 |
| 8 | 🇩🇪 DE | 2505 |
| 9 | 🇨🇦 CA | 2343 |
| 10 | 🇨🇴 CO | 2210 |
| 11 | 🇬🇧 GB | 1962 |
| 12 | 🇫🇷 FR | 1822 |
| 13 | 🇲🇽 MX | 1479 |
| 14 | 🇬🇷 GR | 1462 |
| 15 | 🇨🇭 CH | 1313 |
| 16 | 🇳🇴 NO | 1232 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 992 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 865 |
| 21 | 🇵🇭 PH | 841 |
| 22 | 🇹🇷 TR | 840 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 758 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 589 |
| 27 | 🇲🇪 ME | 513 |
| 28 | 🇳🇱 NL | 488 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1123 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 795 |
| 4 | El Dorado International Airport |  | CO | 769 |
| 5 | Indira Gandhi International Airport |  | IN | 745 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 725 |
| 7 | Harry Reid International Airport |  | US | 619 |
| 8 | Guaymaral Airport |  | CO | 618 |
| 9 | Zurich Airport |  | CH | 565 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 498 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Kuala Lumpur International Airport |  | MY | 472 |
| 14 | Chicago O'Hare International Airport |  | US | 467 |
| 15 | Macau International Airport |  | MO | 454 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 426 |
| 19 | Bengaluru International Airport |  | IN | 424 |
| 20 | Charlotte/Douglas International Airport |  | US | 408 |
| 21 | Malpensa International Airport |  | IT | 402 |
| 22 | Congonhas Airport |  | BR | 401 |
| 23 | Tenerife Norte Airport |  | ES | 400 |
| 24 | Ninoy Aquino International Airport |  | PH | 389 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 362 |
| 26 | Salt Lake City International Airport |  | US | 359 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 354 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 350 |
| 31 | Reno/Tahoe International Airport |  | US | 329 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 328 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 324 |
| 34 | Vitoria/Foronda Airport |  | ES | 322 |
| 35 | O. R. Tambo International Airport |  | ZA | 318 |
| 36 | Barcelona International Airport |  | ES | 316 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 314 |
| 38 | Don Mueang International Airport |  | TH | 293 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 283 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 247 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 182 | 14m | 114 km | 357.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 110 | 26m | 275 km | 521.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 80 | 20m | 250 km | 345.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 78 | 20m | 147 km | 197.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 74 | 26m | 215 km | 274.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 67 | 1h 0m | 695 km | 803.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFGMQ | CFG | London / Chapeskie Field (CLC2) | Billy Bishop Toronto City Airport (CYTZ) | 2026-04-22 11:24 UTC | 2026-04-22 11:48 UTC | 23m |
| M28B |  | Altenstadt Army Airfield (ETHA) | Altenstadt Army Airfield (ETHA) | 2026-04-22 10:54 UTC | 2026-04-22 11:37 UTC | 42m |
| OEANN | OEA | Hohenems-Dornbirn Airport (LOIH) | Samedan Airport (LSZS) | 2026-04-22 10:38 UTC | 2026-04-22 11:21 UTC | 42m |
| N642PC |  | Roswell Air Center Airport (KROW) | Casas Adobes Airpark (NM69) | 2026-04-22 10:11 UTC | 2026-04-22 11:14 UTC | 1h 2m |
| N313CF |  | Dekalb-Peachtree Airport (KPDK) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-22 10:34 UTC | 2026-04-22 11:13 UTC | 39m |
| SAS50F | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-04-22 09:44 UTC | 2026-04-22 11:07 UTC | 1h 23m |
| NKD | NKD | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-04-22 09:31 UTC | 2026-04-22 11:05 UTC | 1h 34m |
| BDN030 | BDN | Middle Wallop Airfield (EGVP) | MoD Boscombe Down Airport (EGDM) | 2026-04-22 10:15 UTC | 2026-04-22 11:01 UTC | 45m |
| N874BU |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Peter O Knight Airport (KTPF) | 2026-04-22 10:43 UTC | 2026-04-22 11:00 UTC | 16m |
| AIQ3310 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Sawan Airport (VTPN) | 2026-04-22 10:37 UTC | 2026-04-22 10:57 UTC | 20m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-22 10:22 UTC | 2026-04-22 10:56 UTC | 33m |
| KGF170 | KGF | Praia International Airport (GVNP) | Maio Airport (GVMA) | 2026-04-22 10:51 UTC | 2026-04-22 10:54 UTC | 2m |
| EFW34BY | EFW | London Gatwick Airport (EGKK) | Dubrovnik Airport (LDDU) | 2026-04-22 08:37 UTC | 2026-04-22 10:53 UTC | 2h 15m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-04-22 10:38 UTC | 2026-04-22 10:52 UTC | 13m |
| AAO53 | AAO | Václav Havel Airport (LKPR) | Samedan Airport (LSZS) | 2026-04-22 09:56 UTC | 2026-04-22 10:51 UTC | 55m |
| JAF51E | JAF | Brussels Airport (EBBR) | Rabil Airport (GVBA) | 2026-04-22 04:34 UTC | 2026-04-22 10:49 UTC | 6h 15m |
| UPS844 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Salt Lake City International Airport (KSLC) | 2026-04-22 07:49 UTC | 2026-04-22 10:48 UTC | 2h 59m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-04-22 10:09 UTC | 2026-04-22 10:47 UTC | 38m |
| OKPRJ | OKP | Geneva Cointrin International Airport (LSGG) | Kemi-Tornio Airport (EFKE) | 2026-04-22 07:30 UTC | 2026-04-22 10:46 UTC | 3h 16m |
| DLH4P | Lufthansa | Václav Havel Airport (LKPR) | Frankfurt am Main International Airport (EDDF) | 2026-04-22 09:58 UTC | 2026-04-22 10:46 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
