# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_10:26:07_UTC-green)

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

**Latest saved flight:** 2026-05-08 10:26:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 10:26:07 UTC

- **73,049** saved flights
- **27,065** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **73,049** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **900,616.8 tonnes** estimated CO2 emissions
- **52,209,670 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3142 |
| 2 | SkyWest Airlines | 2714 |
| 3 | IndiGo | 1650 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 944 |
| 8 | ENY | 915 |
| 9 | Vueling | 714 |
| 10 | AXM | 692 |
| 11 | LATAM Airlines | 677 |
| 12 | WIF | 629 |
| 13 | Delta Air Lines | 619 |
| 14 | All Nippon Airways | 604 |
| 15 | AZU | 586 |
| 16 | QLK | 573 |
| 17 | Swiss International | 558 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 485 |
| 21 | EJU | 470 |
| 22 | AEE | 468 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 434 |
| 26 | Air France | 425 |
| 27 | AXB | 407 |
| 28 | CXK | 368 |
| 29 | AIQ | 366 |
| 30 | United Airlines | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58426 |
| 2 | 🇪🇸 ES | 5296 |
| 3 | 🇮🇳 IN | 5191 |
| 4 | 🇦🇺 AU | 4899 |
| 5 | 🇧🇷 BR | 4080 |
| 6 | 🇩🇪 DE | 4072 |
| 7 | 🇮🇹 IT | 4006 |
| 8 | 🇯🇵 JP | 3873 |
| 9 | 🇨🇦 CA | 3641 |
| 10 | 🇬🇧 GB | 3146 |
| 11 | 🇫🇷 FR | 2880 |
| 12 | 🇨🇴 CO | 2679 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2162 |
| 15 | 🇳🇴 NO | 2032 |
| 16 | 🇨🇭 CH | 1988 |
| 17 | 🇲🇾 MY | 1729 |
| 18 | 🇿🇦 ZA | 1431 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1311 |
| 21 | 🇹🇭 TH | 1310 |
| 22 | 🇵🇱 PL | 1221 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇰🇷 KR | 1150 |
| 25 | 🇬🇹 GT | 1147 |
| 26 | 🇲🇦 MA | 868 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 780 |
| 29 | 🇳🇱 NL | 765 |
| 30 | 🇧🇸 BS | 611 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1301 |
| 3 | Denver International Airport |  | US | 1218 |
| 4 | Indira Gandhi International Airport |  | IN | 1095 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1058 |
| 6 | Frankfurt am Main International Airport |  | DE | 941 |
| 7 | Harry Reid International Airport |  | US | 910 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 874 |
| 10 | Zurich Airport |  | CH | 863 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 734 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 693 |
| 16 | Madrid Barajas International Airport |  | ES | 685 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 637 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 20 | Bengaluru International Airport |  | IN | 633 |
| 21 | Salt Lake City International Airport |  | US | 595 |
| 22 | Congonhas Airport |  | BR | 575 |
| 23 | Charlotte/Douglas International Airport |  | US | 574 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 569 |
| 26 | Tenerife Norte Airport |  | ES | 556 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 534 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 528 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 505 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 495 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 490 |
| 34 | Vitoria/Foronda Airport |  | ES | 478 |
| 35 | Don Mueang International Airport |  | TH | 462 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 459 |
| 37 | Amsterdam Airport Schiphol |  | NL | 458 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 452 |
| 39 | O. R. Tambo International Airport |  | ZA | 449 |
| 40 | Calgary International Airport |  | CA | 435 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 363 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 257 | 21m | 244 km | 1,082.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 162 | 26m | 275 km | 767.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 109 | 27m | 215 km | 403.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 98 | 1h 43m | 1,423 km | 2,405.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 90 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JST419 | JST | Gold Coast Airport (YBCG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-08 09:23 UTC | 2026-05-08 10:26 UTC | 1h 2m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-08 09:24 UTC | 2026-05-08 10:20 UTC | 56m |
| HRD32 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-05-08 09:47 UTC | 2026-05-08 10:20 UTC | 33m |
| FGJSR | FGJ | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-08 09:57 UTC | 2026-05-08 10:17 UTC | 19m |
| WZZ55 | Wizz Air | London Gatwick Airport (EGKK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-08 07:57 UTC | 2026-05-08 09:58 UTC | 2h 0m |
| VTEJZ | VTE | Indira Gandhi International Airport (VIDP) | Patiala Airport (VIPL) | 2026-05-08 09:09 UTC | 2026-05-08 09:53 UTC | 43m |
| FIN515 | Finnair | Helsinki Vantaa Airport (EFHK) | Hailuoto Airport (EFHL) | 2026-05-08 08:34 UTC | 2026-05-08 09:43 UTC | 1h 8m |
| ADO87 | ADO | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-05-08 08:42 UTC | 2026-05-08 09:43 UTC | 1h 0m |
| BNOG | BNO | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-08 09:14 UTC | 2026-05-08 09:42 UTC | 28m |
| ANA667 | All Nippon Airways | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-05-08 08:08 UTC | 2026-05-08 09:40 UTC | 1h 32m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-08 08:52 UTC | 2026-05-08 09:39 UTC | 47m |
| NAY83XR | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-05-08 09:28 UTC | 2026-05-08 09:38 UTC | 10m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-05-08 09:00 UTC | 2026-05-08 09:37 UTC | 36m |
| AZU2797 | AZU | Viracopos International Airport (SBKP) | Ilha dos Porcos Grandes Airport (SILI) | 2026-05-08 09:07 UTC | 2026-05-08 09:34 UTC | 27m |
| N501DN |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 09:20 UTC | 2026-05-08 09:34 UTC | 13m |
| RYR140E | Ryanair | Brussels South Charleroi Airport (EBCI) | Decimomannu Airport (LIED) | 2026-05-08 07:47 UTC | 2026-05-08 09:34 UTC | 1h 46m |
| SDG223 | SDG | Chaudhary Charan Singh International Airport (VILK) | Jaipur International Airport (VIJP) | 2026-05-08 08:43 UTC | 2026-05-08 09:33 UTC | 50m |
| LOT3HB | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-08 08:53 UTC | 2026-05-08 09:32 UTC | 39m |
| KLM76U | KLM Royal Dutch | Humberside Airport (EGNJ) | Amsterdam Airport Schiphol (EHAM) | 2026-05-08 08:52 UTC | 2026-05-08 09:31 UTC | 39m |
| VLG5WB | Vueling | Barcelona International Airport (LEBL) | La Morgal Airport (LEMR) | 2026-05-08 08:34 UTC | 2026-05-08 09:31 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
