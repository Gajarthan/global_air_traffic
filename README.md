# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_03:45:49_UTC-green)

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

**Latest saved flight:** 2026-04-30 03:45:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 03:45:49 UTC

- **60,037** saved flights
- **23,212** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,037** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **729,454.4 tonnes** estimated CO2 emissions
- **42,287,214 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2548 |
| 2 | SkyWest Airlines | 2253 |
| 3 | IndiGo | 1372 |
| 4 | EJA | 1082 |
| 5 | American Airlines | 941 |
| 6 | Southwest Airlines | 854 |
| 7 | Lufthansa | 759 |
| 8 | ENY | 748 |
| 9 | Vueling | 597 |
| 10 | AXM | 583 |
| 11 | LATAM Airlines | 573 |
| 12 | All Nippon Airways | 531 |
| 13 | Delta Air Lines | 503 |
| 14 | WIF | 501 |
| 15 | AZU | 492 |
| 16 | Swiss International | 473 |
| 17 | QLK | 472 |
| 18 | LXJ | 427 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 379 |
| 24 | Cathay Pacific | 356 |
| 25 | Air France | 353 |
| 26 | Japan Airlines | 349 |
| 27 | AXB | 330 |
| 28 | AIQ | 302 |
| 29 | JetBlue | 300 |
| 30 | CXK | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47631 |
| 2 | 🇮🇳 IN | 4344 |
| 3 | 🇪🇸 ES | 4340 |
| 4 | 🇦🇺 AU | 4099 |
| 5 | 🇧🇷 BR | 3398 |
| 6 | 🇩🇪 DE | 3312 |
| 7 | 🇮🇹 IT | 3289 |
| 8 | 🇯🇵 JP | 3265 |
| 9 | 🇨🇦 CA | 2981 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2524 |
| 12 | 🇫🇷 FR | 2367 |
| 13 | 🇲🇽 MX | 1885 |
| 14 | 🇬🇷 GR | 1786 |
| 15 | 🇨🇭 CH | 1665 |
| 16 | 🇳🇴 NO | 1637 |
| 17 | 🇲🇾 MY | 1420 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1123 |
| 20 | 🇹🇭 TH | 1079 |
| 21 | 🇹🇷 TR | 1073 |
| 22 | 🇵🇭 PH | 1011 |
| 23 | 🇵🇱 PL | 969 |
| 24 | 🇰🇷 KR | 964 |
| 25 | 🇬🇹 GT | 876 |
| 26 | 🇲🇦 MA | 749 |
| 27 | 🇲🇴 MO | 655 |
| 28 | 🇲🇪 ME | 652 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇧🇸 BS | 508 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1339 |
| 2 | Tokyo International Airport |  | JP | 1105 |
| 3 | Denver International Airport |  | US | 1005 |
| 4 | Indira Gandhi International Airport |  | IN | 918 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 880 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 765 |
| 9 | Frankfurt am Main International Airport |  | DE | 750 |
| 10 | Zurich Airport |  | CH | 721 |
| 11 | La Aurora Airport |  | GT | 660 |
| 12 | Macau International Airport |  | MO | 655 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 598 |
| 14 | Chicago O'Hare International Airport |  | US | 572 |
| 15 | Kuala Lumpur International Airport |  | MY | 559 |
| 16 | Madrid Barajas International Airport |  | ES | 555 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 529 |
| 19 | Malpensa International Airport |  | IT | 520 |
| 20 | Bengaluru International Airport |  | IN | 519 |
| 21 | Congonhas Airport |  | BR | 490 |
| 22 | Charlotte/Douglas International Airport |  | US | 478 |
| 23 | Salt Lake City International Airport |  | US | 468 |
| 24 | Charles de Gaulle International Airport |  | FR | 466 |
| 25 | Capua Airport |  | IT | 466 |
| 26 | Ninoy Aquino International Airport |  | PH | 463 |
| 27 | Tenerife Norte Airport |  | ES | 463 |
| 28 | Daniel K Inouye International Airport |  | US | 453 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 434 |
| 31 | Barcelona International Airport |  | ES | 409 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 33 | Vitoria/Foronda Airport |  | ES | 400 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 394 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 382 |
| 38 | Don Mueang International Airport |  | TH | 369 |
| 39 | Amsterdam Airport Schiphol |  | NL | 368 |
| 40 | Calgary International Airport |  | CA | 357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 188 | 24m | 225 km | 729.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 177 | 1h 27m | 910 km | 2,777.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 172 | 28m | 304 km | 901.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 147 | 19m | 165 km | 418.1 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 143 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 142 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 127 | 1h 12m | 770 km | 1,687.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 112 | 44m | 452 km | 872.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 101 | 31m | 369 km | 642.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 90 | 20m | 147 km | 227.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 84 | 1h 42m | 1,156 km | 1,675.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 76 | 14m | 154 km | 201.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1151 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-30 02:30 UTC | 2026-04-30 03:45 UTC | 1h 15m |
| ALFT6 | ALF | Kimshan Ranch Airport (WN00) | Boeing Field/King County International Airport (KBFI) | 2026-04-30 03:26 UTC | 2026-04-30 03:39 UTC | 12m |
| N605FF |  | Santa Barbara Municipal Airport (KSBA) | Hemet-Ryan Airport (KHMT) | 2026-04-30 02:04 UTC | 2026-04-30 03:34 UTC | 1h 30m |
| FDX1355 | FDX | Ontario International Airport (KONT) | St Johns Industrial Air Park (KSJN) | 2026-04-30 02:47 UTC | 2026-04-30 03:32 UTC | 45m |
| N7867N |  | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-04-30 03:10 UTC | 2026-04-30 03:32 UTC | 21m |
| SAMB | SAM | RAAF Base Pearce (YPEA) | RAAF Gingin (YGIG) | 2026-04-30 02:43 UTC | 2026-04-30 03:28 UTC | 44m |
| ADY043 | ADY | Al Ain International Airport (OMAL) | Simara Airport (VNSI) | 2026-04-29 23:36 UTC | 2026-04-30 03:25 UTC | 3h 49m |
| DHX821 | DHX | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-04-29 16:55 UTC | 2026-04-30 03:25 UTC | 10h 29m |
| HIM766 | HIM | Dubai International Airport (OMDB) | Simara Airport (VNSI) | 2026-04-29 23:45 UTC | 2026-04-30 03:20 UTC | 3h 35m |
| NTRDR21 | NTR | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | San Clemente Island Nalf Airport (KNUC) | 2026-04-30 02:47 UTC | 2026-04-30 03:20 UTC | 32m |
| PAV632H | PAV | Vitoria/Foronda Airport (LEVT) | Federico Garcia Lorca Airport (LEGR) | 2026-04-30 02:20 UTC | 2026-04-30 03:19 UTC | 58m |
| CAP4680 | CAP | Sanderson Field (KSHN) | Auburn Municipal Airport (KS50) | 2026-04-30 02:45 UTC | 2026-04-30 03:11 UTC | 26m |
| N9393T |  | Hayward Executive Airport (KHWD) | Sacramento Mather Airport (KMHR) | 2026-04-30 02:41 UTC | 2026-04-30 03:10 UTC | 28m |
| N3143Q |  | Venice Municipal Airport (KVNC) | Venice Municipal Airport (KVNC) | 2026-04-30 00:54 UTC | 2026-04-30 03:07 UTC | 2h 12m |
| QLK623D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-04-30 02:32 UTC | 2026-04-30 03:06 UTC | 34m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-30 02:26 UTC | 2026-04-30 03:02 UTC | 36m |
| RXA6828 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-04-30 02:17 UTC | 2026-04-30 02:57 UTC | 39m |
| TOE | TOE | Gold Coast Airport (YBCG) | Brisbane Archerfield Airport (YBAF) | 2026-04-30 02:21 UTC | 2026-04-30 02:56 UTC | 35m |
| N182VB |  | Banning Municipal Airport (KBNG) | Riverside Airport (KRAL) | 2026-04-30 02:23 UTC | 2026-04-30 02:56 UTC | 32m |
| TVR4703 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-29 20:09 UTC | 2026-04-30 02:55 UTC | 6h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
