# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_10:14:14_UTC-green)

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

**Latest saved flight:** 2026-05-03 10:14:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 10:14:14 UTC

- **65,486** saved flights
- **24,809** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,486** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **803,686.2 tonnes** estimated CO2 emissions
- **46,590,502 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2783 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1517 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1011 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 842 |
| 8 | ENY | 806 |
| 9 | Vueling | 647 |
| 10 | AXM | 642 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 572 |
| 13 | Delta Air Lines | 547 |
| 14 | WIF | 542 |
| 15 | AZU | 526 |
| 16 | QLK | 513 |
| 17 | Swiss International | 503 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 434 |
| 21 | AEE | 425 |
| 22 | EJU | 421 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 393 |
| 25 | Japan Airlines | 387 |
| 26 | Air France | 382 |
| 27 | AXB | 366 |
| 28 | AIQ | 334 |
| 29 | CXK | 331 |
| 30 | GLO | 318 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51711 |
| 2 | 🇪🇸 ES | 4802 |
| 3 | 🇮🇳 IN | 4771 |
| 4 | 🇦🇺 AU | 4400 |
| 5 | 🇧🇷 BR | 3674 |
| 6 | 🇩🇪 DE | 3664 |
| 7 | 🇯🇵 JP | 3583 |
| 8 | 🇮🇹 IT | 3563 |
| 9 | 🇨🇦 CA | 3203 |
| 10 | 🇬🇧 GB | 2825 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2590 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1961 |
| 15 | 🇨🇭 CH | 1836 |
| 16 | 🇳🇴 NO | 1777 |
| 17 | 🇲🇾 MY | 1576 |
| 18 | 🇿🇦 ZA | 1334 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1196 |
| 21 | 🇹🇷 TR | 1182 |
| 22 | 🇵🇭 PH | 1102 |
| 23 | 🇰🇷 KR | 1070 |
| 24 | 🇵🇱 PL | 1068 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 804 |
| 27 | 🇲🇴 MO | 738 |
| 28 | 🇲🇪 ME | 710 |
| 29 | 🇳🇱 NL | 695 |
| 30 | 🇮🇩 ID | 560 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1206 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 998 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 955 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 841 |
| 8 | Guaymaral Airport |  | CO | 840 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 779 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 738 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Kuala Lumpur International Airport |  | MY | 626 |
| 15 | Madrid Barajas International Airport |  | ES | 624 |
| 16 | Chicago O'Hare International Airport |  | US | 623 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 583 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 576 |
| 20 | Malpensa International Airport |  | IT | 563 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 524 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 515 |
| 25 | Charles de Gaulle International Airport |  | FR | 511 |
| 26 | Ninoy Aquino International Airport |  | PH | 501 |
| 27 | Capua Airport |  | IT | 491 |
| 28 | Daniel K Inouye International Airport |  | US | 481 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 481 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 446 |
| 32 | Vitoria/Foronda Airport |  | ES | 439 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 436 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 435 |
| 35 | O. R. Tambo International Airport |  | ZA | 421 |
| 36 | Don Mueang International Airport |  | TH | 417 |
| 37 | Amsterdam Airport Schiphol |  | NL | 408 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 222 | 21m | 244 km | 934.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 163 | 20m | 165 km | 463.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 153 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 145 | 1h 11m | 770 km | 1,926.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 122 | 44m | 452 km | 950.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 106 | 20m | 250 km | 457.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 101 | 27m | 215 km | 374.1 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 98 | 20m | 147 km | 248.0 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 92 | 57m | 493 km | 782.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 90 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 87 | 14m | 154 km | 230.5 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PH4U9 |  | De Kooy Airport (EHKD) | Texel Airport (EHTX) | 2026-05-03 09:58 UTC | 2026-05-03 10:14 UTC | 16m |
|  |  | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-03 09:58 UTC | 2026-05-03 10:14 UTC | 16m |
| ANZ329M | ANZ | Wellington International Airport (NZWN) | Christchurch International Airport (NZCH) | 2026-05-03 09:19 UTC | 2026-05-03 10:00 UTC | 41m |
| DMUHF | DMU | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-05-03 09:39 UTC | 2026-05-03 09:59 UTC | 20m |
| OE7135 |  | Scharnstein Airport (LOLC) | Scharnstein Airport (LOLC) | 2026-05-03 09:54 UTC | 2026-05-03 09:54 UTC | 0m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-05-03 09:35 UTC | 2026-05-03 09:53 UTC | 17m |
| RTV4T | RTV | Vilar Da Luz Airport (LPVL) | Braga Municipal Aerodrome (LPBR) | 2026-05-03 09:33 UTC | 2026-05-03 09:45 UTC | 11m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-03 08:51 UTC | 2026-05-03 09:45 UTC | 53m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-02 19:05 UTC | 2026-05-03 09:42 UTC | 14h 37m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-03 09:31 UTC | 2026-05-03 09:38 UTC | 6m |
| CRK399 | CRK | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-05-03 02:17 UTC | 2026-05-03 09:34 UTC | 7h 17m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Forsaeti Airport (BIFZ) | 2026-05-03 09:21 UTC | 2026-05-03 09:32 UTC | 11m |
| ANA455 | All Nippon Airways | Tokyo International Airport (RJTT) | Kumamoto Airport (RJFT) | 2026-05-03 08:05 UTC | 2026-05-03 09:31 UTC | 1h 25m |
| RSC27XK | RSC | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-05-03 09:19 UTC | 2026-05-03 09:29 UTC | 10m |
| RYR2778 | Ryanair | Thessaloniki Macedonia International Airport (LGTS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-03 07:45 UTC | 2026-05-03 09:27 UTC | 1h 42m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-03 09:02 UTC | 2026-05-03 09:27 UTC | 24m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-05-03 09:09 UTC | 2026-05-03 09:26 UTC | 17m |
| IGO7313 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-05-03 08:13 UTC | 2026-05-03 09:25 UTC | 1h 12m |
| AIC6LX | Air India | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-05-03 08:57 UTC | 2026-05-03 09:21 UTC | 23m |
| EZY71AQ | easyJet | London Gatwick Airport (EGKK) | Isle of Man Airport (EGNS) | 2026-05-03 08:25 UTC | 2026-05-03 09:21 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
