# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_04:15:53_UTC-green)

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

**Latest saved flight:** 2026-04-25 04:15:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 04:15:53 UTC

- **52,994** saved flights
- **21,142** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,994** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **633,338.0 tonnes** estimated CO2 emissions
- **36,715,244 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2217 |
| 2 | SkyWest Airlines | 2007 |
| 3 | IndiGo | 1200 |
| 4 | EJA | 944 |
| 5 | American Airlines | 856 |
| 6 | Southwest Airlines | 754 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 614 |
| 9 | Vueling | 529 |
| 10 | AXM | 511 |
| 11 | LATAM Airlines | 509 |
| 12 | All Nippon Airways | 470 |
| 13 | AZU | 449 |
| 14 | Delta Air Lines | 439 |
| 15 | WIF | 437 |
| 16 | QLK | 415 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 392 |
| 19 | AEE | 355 |
| 20 | Alaska Airlines | 353 |
| 21 | VIV | 338 |
| 22 | easyJet | 333 |
| 23 | EJU | 332 |
| 24 | Japan Airlines | 310 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 280 |
| 28 | JetBlue | 272 |
| 29 | United Airlines | 272 |
| 30 | AIQ | 268 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42380 |
| 2 | 🇪🇸 ES | 3806 |
| 3 | 🇮🇳 IN | 3785 |
| 4 | 🇦🇺 AU | 3605 |
| 5 | 🇧🇷 BR | 3057 |
| 6 | 🇯🇵 JP | 2849 |
| 7 | 🇮🇹 IT | 2829 |
| 8 | 🇩🇪 DE | 2803 |
| 9 | 🇨🇦 CA | 2657 |
| 10 | 🇨🇴 CO | 2444 |
| 11 | 🇬🇧 GB | 2193 |
| 12 | 🇫🇷 FR | 2045 |
| 13 | 🇲🇽 MX | 1641 |
| 14 | 🇬🇷 GR | 1587 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1420 |
| 17 | 🇲🇾 MY | 1245 |
| 18 | 🇿🇦 ZA | 1087 |
| 19 | 🇳🇿 NZ | 1012 |
| 20 | 🇹🇭 TH | 954 |
| 21 | 🇹🇷 TR | 949 |
| 22 | 🇵🇭 PH | 911 |
| 23 | 🇰🇷 KR | 861 |
| 24 | 🇵🇱 PL | 840 |
| 25 | 🇬🇹 GT | 815 |
| 26 | 🇲🇦 MA | 653 |
| 27 | 🇲🇪 ME | 563 |
| 28 | 🇳🇱 NL | 533 |
| 29 | 🇲🇴 MO | 515 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1214 |
| 2 | Tokyo International Airport |  | JP | 966 |
| 3 | Denver International Airport |  | US | 881 |
| 4 | El Dorado International Airport |  | CO | 830 |
| 5 | Indira Gandhi International Airport |  | IN | 809 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 788 |
| 7 | Guaymaral Airport |  | CO | 730 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 609 |
| 11 | Frankfurt am Main International Airport |  | DE | 601 |
| 12 | Chicago O'Hare International Airport |  | US | 524 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 14 | Macau International Airport |  | MO | 515 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 495 |
| 17 | Madrid Barajas International Airport |  | ES | 488 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 470 |
| 19 | Bengaluru International Airport |  | IN | 451 |
| 20 | Congonhas Airport |  | BR | 442 |
| 21 | Malpensa International Airport |  | IT | 440 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Ninoy Aquino International Airport |  | PH | 421 |
| 24 | Tenerife Norte Airport |  | ES | 415 |
| 25 | Charles de Gaulle International Airport |  | FR | 399 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 397 |
| 27 | Salt Lake City International Airport |  | US | 395 |
| 28 | Daniel K Inouye International Airport |  | US | 387 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 370 |
| 31 | Vitoria/Foronda Airport |  | ES | 358 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 33 | Reno/Tahoe International Airport |  | US | 355 |
| 34 | Barcelona International Airport |  | ES | 354 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 350 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 350 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 323 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 295 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 244 | 1h 7m | 706 km | 2,970.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 162 | 21m | 244 km | 682.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 154 | 28m | 304 km | 807.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 150 | 1h 27m | 910 km | 2,353.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 95 | 1h 11m | 770 km | 1,262.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 1m | 695 km | 911.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 68 | 24m | 55 km | 64.6 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 67 | 1h 20m | 961 km | 1,110.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-25 03:57 UTC | 2026-04-25 04:15 UTC | 18m |
| JJP215 | JJP | Narita International Airport (RJAA) | Kansai International Airport (RJBB) | 2026-04-25 03:25 UTC | 2026-04-25 04:13 UTC | 47m |
| DHK855 | DHK | East Midlands Airport (EGNX) | Malpensa International Airport (LIMC) | 2026-04-25 02:14 UTC | 2026-04-25 04:09 UTC | 1h 55m |
| HSGDZ | HSG | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-04-25 03:56 UTC | 2026-04-25 04:02 UTC | 5m |
| UPG | UPG | Melbourne Moorabbin Airport (YMMB) | Tyabb Airport (YTYA) | 2026-04-25 03:34 UTC | 2026-04-25 03:49 UTC | 15m |
| SFJ23 | SFJ | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-25 03:09 UTC | 2026-04-25 03:49 UTC | 40m |
| YOX | YOX | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-25 03:11 UTC | 2026-04-25 03:47 UTC | 35m |
| HIM766 | HIM | Dubai International Airport (OMDB) | Simara Airport (VNSI) | 2026-04-24 23:55 UTC | 2026-04-25 03:41 UTC | 3h 45m |
| LHX2EJ | LHX | Helsinki Vantaa Airport (EFHK) | Khrabrovo Airport (UMKK) | 2026-04-25 03:08 UTC | 2026-04-25 03:40 UTC | 32m |
| FD626J |  | Busselton Regional Airport (YBLN) | Busselton Regional Airport (YBLN) | 2026-04-25 03:22 UTC | 2026-04-25 03:39 UTC | 17m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-25 03:07 UTC | 2026-04-25 03:32 UTC | 24m |
| EJA417 | EJA | Flying Cloud Airport (KFCM) | Mc Laughlin Municipal Airport (K5P2) | 2026-04-25 02:34 UTC | 2026-04-25 03:31 UTC | 56m |
| AMU822 | AMU | Macau International Airport (VMMC) | Incheon International Airport (RKSI) | 2026-04-25 00:42 UTC | 2026-04-25 03:25 UTC | 2h 43m |
| ADY043 | ADY | Al Ain International Airport (OMAL) | Simara Airport (VNSI) | 2026-04-24 23:29 UTC | 2026-04-25 03:22 UTC | 3h 53m |
| ANA793 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-25 02:17 UTC | 2026-04-25 03:19 UTC | 1h 2m |
| IGO7573 | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-04-25 02:47 UTC | 2026-04-25 03:18 UTC | 30m |
| ASA1082 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-04-25 02:56 UTC | 2026-04-25 03:16 UTC | 20m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-25 02:52 UTC | 2026-04-25 03:16 UTC | 23m |
| VIV7017 | VIV | Leon Gonzales Pie De La Cuesta Airport (MM41) | Tizayuca Airport (MM28) | 2026-04-25 02:38 UTC | 2026-04-25 03:14 UTC | 35m |
| GAP2664 | GAP | Godofredo P. Ramos Airport (RPVE) | RPSR (RPSR) | 2026-04-25 03:03 UTC | 2026-04-25 03:14 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
