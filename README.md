# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_09:58:50_UTC-green)

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

**Latest saved flight:** 2026-04-20 09:58:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 09:58:50 UTC

- **44,775** saved flights
- **18,537** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,775** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **540,960.2 tonnes** estimated CO2 emissions
- **31,360,014 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1890 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1078 |
| 4 | EJA | 779 |
| 5 | American Airlines | 741 |
| 6 | Southwest Airlines | 642 |
| 7 | ENY | 584 |
| 8 | AXM | 450 |
| 9 | Vueling | 448 |
| 10 | Lufthansa | 447 |
| 11 | LATAM Airlines | 446 |
| 12 | All Nippon Airways | 404 |
| 13 | AZU | 389 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 366 |
| 16 | LXJ | 354 |
| 17 | WIF | 350 |
| 18 | Swiss International | 345 |
| 19 | Alaska Airlines | 308 |
| 20 | AEE | 306 |
| 21 | EJU | 294 |
| 22 | easyJet | 286 |
| 23 | VIV | 285 |
| 24 | Japan Airlines | 274 |
| 25 | Air France | 256 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 237 |
| 28 | AXB | 235 |
| 29 | GLO | 234 |
| 30 | Cathay Pacific | 232 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35423 |
| 2 | 🇮🇳 IN | 3340 |
| 3 | 🇪🇸 ES | 3279 |
| 4 | 🇦🇺 AU | 3126 |
| 5 | 🇧🇷 BR | 2664 |
| 6 | 🇯🇵 JP | 2466 |
| 7 | 🇮🇹 IT | 2387 |
| 8 | 🇩🇪 DE | 2283 |
| 9 | 🇨🇦 CA | 2176 |
| 10 | 🇨🇴 CO | 2057 |
| 11 | 🇬🇧 GB | 1816 |
| 12 | 🇫🇷 FR | 1697 |
| 13 | 🇲🇽 MX | 1399 |
| 14 | 🇬🇷 GR | 1385 |
| 15 | 🇨🇭 CH | 1219 |
| 16 | 🇳🇴 NO | 1111 |
| 17 | 🇲🇾 MY | 1102 |
| 18 | 🇿🇦 ZA | 938 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇵🇭 PH | 805 |
| 21 | 🇹🇭 TH | 804 |
| 22 | 🇹🇷 TR | 788 |
| 23 | 🇰🇷 KR | 738 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 710 |
| 26 | 🇲🇦 MA | 552 |
| 27 | 🇲🇪 ME | 475 |
| 28 | 🇳🇱 NL | 455 |
| 29 | 🇲🇴 MO | 418 |
| 30 | 🇧🇸 BS | 411 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1051 |
| 2 | Tokyo International Airport |  | JP | 840 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | Indira Gandhi International Airport |  | IN | 722 |
| 5 | El Dorado International Airport |  | CO | 719 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 687 |
| 7 | Harry Reid International Airport |  | US | 580 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 535 |
| 11 | Chicago O'Hare International Airport |  | US | 442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 13 | Kuala Lumpur International Airport |  | MY | 439 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Frankfurt am Main International Airport |  | DE | 420 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 420 |
| 17 | Macau International Airport |  | MO | 418 |
| 18 | Madrid Barajas International Airport |  | ES | 398 |
| 19 | Bengaluru International Airport |  | IN | 396 |
| 20 | Tenerife Norte Airport |  | ES | 391 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Congonhas Airport |  | BR | 381 |
| 23 | Malpensa International Airport |  | IT | 380 |
| 24 | Ninoy Aquino International Airport |  | PH | 373 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Daniel K Inouye International Airport |  | US | 333 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 333 |
| 29 | Charles de Gaulle International Airport |  | FR | 331 |
| 30 | Capua Airport |  | IT | 312 |
| 31 | Reno/Tahoe International Airport |  | US | 311 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 311 |
| 33 | Vitoria/Foronda Airport |  | ES | 308 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 302 |
| 35 | O. R. Tambo International Airport |  | ZA | 299 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 299 |
| 37 | Barcelona International Airport |  | ES | 289 |
| 38 | Calgary International Airport |  | CA | 273 |
| 39 | Don Mueang International Airport |  | TH | 272 |
| 40 | Viracopos International Airport |  | BR | 270 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 210 | 1h 7m | 706 km | 2,556.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 135 | 28m | 304 km | 707.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 127 | 21m | 244 km | 534.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 121 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 119 | 19m | 165 km | 338.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 97 | 54m | 546 km | 913.3 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 74 | 20m | 250 km | 319.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 69 | 26m | 215 km | 255.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 63 | 13m | 99 km | 108.0 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 62 | 57m | 493 km | 527.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-20 09:05 UTC | 2026-04-20 09:58 UTC | 53m |
| RDF4 | RDF | EDPR (EDPR) | EDPR (EDPR) | 2026-04-20 09:02 UTC | 2026-04-20 09:54 UTC | 51m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-19 20:03 UTC | 2026-04-20 09:52 UTC | 13h 49m |
| GOLGE | GOL | Bournemouth Airport (EGHH) | Cranfield Airport (EGTC) | 2026-04-20 08:56 UTC | 2026-04-20 09:50 UTC | 53m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-04-20 09:36 UTC | 2026-04-20 09:46 UTC | 10m |
| IJM400 | IJM | Oberpfaffenhofen Airport (EDMO) | Ingolstadt Manching Airport (ETSI) | 2026-04-20 09:24 UTC | 2026-04-20 09:45 UTC | 21m |
| MAU53 | MAU | London Gatwick Airport (EGKK) | Heidelburg Airport (FAHG) | 2026-04-19 15:38 UTC | 2026-04-20 09:42 UTC | 18h 3m |
| GTI554 | GTI | Tizayuca Airport (MM28) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-20 02:18 UTC | 2026-04-20 09:31 UTC | 7h 13m |
| RYR2381 | Ryanair | Perugia / San Egidio Airport (LIRZ) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-20 07:49 UTC | 2026-04-20 09:22 UTC | 1h 33m |
| T7FIS |  | Waterkloof Air Force Base (FAWK) | Waterkloof Air Force Base (FAWK) | 2026-04-20 08:17 UTC | 2026-04-20 09:22 UTC | 1h 5m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-19 19:17 UTC | 2026-04-20 09:20 UTC | 14h 3m |
| FD542 |  | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-04-20 08:42 UTC | 2026-04-20 09:18 UTC | 35m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-04-20 09:06 UTC | 2026-04-20 09:17 UTC | 10m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-04-20 08:45 UTC | 2026-04-20 09:17 UTC | 31m |
| WASP81 | WAS | Kecskemet Airport (LHKE) | LHER (LHER) | 2026-04-20 09:02 UTC | 2026-04-20 09:16 UTC | 14m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-19 21:36 UTC | 2026-04-20 09:09 UTC | 11h 32m |
| AXM429 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-20 08:45 UTC | 2026-04-20 09:08 UTC | 22m |
| SXARH | SXA | Eleftherios Venizelos International Airport (LGAV) | Syros Airport (LGSO) | 2026-04-20 08:42 UTC | 2026-04-20 09:05 UTC | 23m |
| KOJ | KOJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-20 08:26 UTC | 2026-04-20 09:03 UTC | 37m |
| KLM1828 | KLM Royal Dutch | Stuttgart Airport (EDDS) | Amsterdam Airport Schiphol (EHAM) | 2026-04-20 08:02 UTC | 2026-04-20 09:02 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
