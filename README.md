# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_14:17:10_UTC-green)

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

**Latest saved flight:** 2026-05-02 14:17:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 14:17:10 UTC

- **64,190** saved flights
- **24,436** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,190** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **787,047.3 tonnes** estimated CO2 emissions
- **45,625,929 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2713 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1483 |
| 4 | EJA | 1145 |
| 5 | American Airlines | 992 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 826 |
| 8 | ENY | 785 |
| 9 | Vueling | 632 |
| 10 | AXM | 630 |
| 11 | LATAM Airlines | 597 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 532 |
| 15 | AZU | 521 |
| 16 | QLK | 502 |
| 17 | Swiss International | 495 |
| 18 | LXJ | 456 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 421 |
| 21 | AEE | 417 |
| 22 | EJU | 410 |
| 23 | VIV | 402 |
| 24 | Cathay Pacific | 389 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 374 |
| 27 | AXB | 359 |
| 28 | AIQ | 330 |
| 29 | CXK | 323 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50632 |
| 2 | 🇮🇳 IN | 4671 |
| 3 | 🇪🇸 ES | 4666 |
| 4 | 🇦🇺 AU | 4341 |
| 5 | 🇧🇷 BR | 3618 |
| 6 | 🇩🇪 DE | 3591 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3488 |
| 9 | 🇨🇦 CA | 3141 |
| 10 | 🇬🇧 GB | 2753 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2541 |
| 13 | 🇲🇽 MX | 2023 |
| 14 | 🇬🇷 GR | 1924 |
| 15 | 🇨🇭 CH | 1803 |
| 16 | 🇳🇴 NO | 1758 |
| 17 | 🇲🇾 MY | 1543 |
| 18 | 🇿🇦 ZA | 1320 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1145 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇰🇷 KR | 1056 |
| 24 | 🇵🇱 PL | 1049 |
| 25 | 🇬🇹 GT | 994 |
| 26 | 🇲🇦 MA | 788 |
| 27 | 🇲🇴 MO | 727 |
| 28 | 🇲🇪 ME | 694 |
| 29 | 🇳🇱 NL | 677 |
| 30 | 🇮🇩 ID | 544 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1405 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1048 |
| 4 | Indira Gandhi International Airport |  | IN | 982 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 938 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 827 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 764 |
| 11 | La Aurora Airport |  | GT | 744 |
| 12 | Macau International Airport |  | MO | 727 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Kuala Lumpur International Airport |  | MY | 612 |
| 15 | Chicago O'Hare International Airport |  | US | 608 |
| 16 | Madrid Barajas International Airport |  | ES | 604 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 563 |
| 20 | Malpensa International Airport |  | IT | 552 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Tenerife Norte Airport |  | ES | 506 |
| 23 | Salt Lake City International Airport |  | US | 503 |
| 24 | Charlotte/Douglas International Airport |  | US | 502 |
| 25 | Charles de Gaulle International Airport |  | FR | 501 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 474 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 473 |
| 29 | Capua Airport |  | IT | 468 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 460 |
| 31 | Barcelona International Airport |  | ES | 436 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 427 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 34 | Vitoria/Foronda Airport |  | ES | 422 |
| 35 | O. R. Tambo International Airport |  | ZA | 416 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 399 |
| 38 | Amsterdam Airport Schiphol |  | NL | 398 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 218 | 21m | 244 km | 917.9 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 142 | 26m | 275 km | 672.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 90 | 1h 42m | 1,156 km | 1,795.5 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 2m | 695 km | 1,066.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 88 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 83 | 1h 43m | 1,423 km | 2,037.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N11684 |  | East Texas Regional Airport (KGGG) | Panola County-Sharpe Field (K4F2) | 2026-05-02 14:00 UTC | 2026-05-02 14:17 UTC | 16m |
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-05-02 12:59 UTC | 2026-05-02 14:10 UTC | 1h 11m |
| N1254D |  | Addison Airport (KADS) | Decatur Municipal Airport (KLUD) | 2026-05-02 12:40 UTC | 2026-05-02 14:10 UTC | 1h 29m |
| HKE135 | HKE | Kaohsiung International Airport (RCKH) | Chek Lap Kok International Airport (VHHH) | 2026-05-02 12:59 UTC | 2026-05-02 14:09 UTC | 1h 10m |
| CXK1041 | CXK | Page Field (KFMY) | Ott's Landing Airport (0FA1) | 2026-05-02 13:42 UTC | 2026-05-02 14:05 UTC | 23m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-02 13:39 UTC | 2026-05-02 13:55 UTC | 16m |
| N2230D |  | Phoenix Deer Valley Airport (KDVT) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-05-02 13:23 UTC | 2026-05-02 13:51 UTC | 28m |
| N988AM |  | Centennial Airport (KAPA) | Chaparral Airport (CO18) | 2026-05-02 13:25 UTC | 2026-05-02 13:48 UTC | 22m |
| N7040Q |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-05-02 13:35 UTC | 2026-05-02 13:46 UTC | 11m |
| N457FD |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-02 13:16 UTC | 2026-05-02 13:46 UTC | 29m |
| RTY690 | RTY | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-05-02 13:06 UTC | 2026-05-02 13:41 UTC | 35m |
| RYR467T | Ryanair | Palermo / Punta Raisi Airport (LICJ) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-02 11:33 UTC | 2026-05-02 13:41 UTC | 2h 8m |
| N854G |  | Deland Municipal-Sidney H Taylor Field (KDED) | Spruce Creek Airport (7FL6) | 2026-05-02 13:32 UTC | 2026-05-02 13:39 UTC | 7m |
| LYM292 | LYM | Denver International Airport (KDEN) | Crawford Airport (K99V) | 2026-05-02 12:54 UTC | 2026-05-02 13:33 UTC | 38m |
| HB3296 |  | Amlikon Glider Airport (LSPA) | Samedan Airport (LSZS) | 2026-05-02 11:25 UTC | 2026-05-02 13:32 UTC | 2h 6m |
| AFR53EJ | Air France | Charles de Gaulle International Airport (LFPG) | Helsinki Vantaa Airport (EFHK) | 2026-05-02 11:01 UTC | 2026-05-02 13:30 UTC | 2h 28m |
| N403TB |  | David Wayne Hooks Memorial Airport (KDWH) | Ksa Orchards Airport (OK11) | 2026-05-02 12:43 UTC | 2026-05-02 13:29 UTC | 45m |
| RYR8TQ | Ryanair | Copenhagen Kastrup Airport (EKCH) | Vienna International Airport (LOWW) | 2026-05-02 12:04 UTC | 2026-05-02 13:29 UTC | 1h 24m |
| N745N |  | Porter County Regional Airport (KVPZ) | Starke County Airport (KOXI) | 2026-05-02 13:06 UTC | 2026-05-02 13:28 UTC | 21m |
| N34JF |  | IN35 (IN35) | Purdue University Airport (KLAF) | 2026-05-02 13:05 UTC | 2026-05-02 13:26 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
