# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_13:55:26_UTC-green)

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

**Latest saved flight:** 2026-05-09 13:55:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 13:55:26 UTC

- **75,307** saved flights
- **27,733** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,307** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **928,907.5 tonnes** estimated CO2 emissions
- **53,849,712 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3222 |
| 2 | SkyWest Airlines | 2788 |
| 3 | IndiGo | 1691 |
| 4 | EJA | 1388 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1090 |
| 7 | Lufthansa | 975 |
| 8 | ENY | 937 |
| 9 | Vueling | 727 |
| 10 | AXM | 712 |
| 11 | Delta Air Lines | 711 |
| 12 | LATAM Airlines | 697 |
| 13 | WIF | 654 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 604 |
| 16 | QLK | 579 |
| 17 | Swiss International | 575 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 499 |
| 21 | AEE | 483 |
| 22 | EJU | 483 |
| 23 | Cathay Pacific | 475 |
| 24 | VIV | 455 |
| 25 | Japan Airlines | 443 |
| 26 | Air France | 437 |
| 27 | AXB | 418 |
| 28 | CXK | 386 |
| 29 | AIQ | 377 |
| 30 | MXY | 365 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60522 |
| 2 | 🇪🇸 ES | 5401 |
| 3 | 🇮🇳 IN | 5302 |
| 4 | 🇦🇺 AU | 4952 |
| 5 | 🇩🇪 DE | 4234 |
| 6 | 🇧🇷 BR | 4220 |
| 7 | 🇮🇹 IT | 4114 |
| 8 | 🇯🇵 JP | 3959 |
| 9 | 🇨🇦 CA | 3746 |
| 10 | 🇬🇧 GB | 3242 |
| 11 | 🇫🇷 FR | 2992 |
| 12 | 🇨🇴 CO | 2694 |
| 13 | 🇲🇽 MX | 2328 |
| 14 | 🇬🇷 GR | 2220 |
| 15 | 🇳🇴 NO | 2094 |
| 16 | 🇨🇭 CH | 2050 |
| 17 | 🇲🇾 MY | 1772 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1366 |
| 20 | 🇹🇷 TR | 1354 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1261 |
| 23 | 🇵🇭 PH | 1214 |
| 24 | 🇬🇹 GT | 1186 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 889 |
| 27 | 🇲🇴 MO | 873 |
| 28 | 🇲🇪 ME | 804 |
| 29 | 🇳🇱 NL | 781 |
| 30 | 🇭🇷 HR | 634 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1329 |
| 3 | Denver International Airport |  | US | 1260 |
| 4 | Indira Gandhi International Airport |  | IN | 1113 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1089 |
| 6 | Frankfurt am Main International Airport |  | DE | 976 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | Zurich Airport |  | CH | 890 |
| 9 | La Aurora Airport |  | GT | 889 |
| 10 | Guaymaral Airport |  | CO | 888 |
| 11 | El Dorado International Airport |  | CO | 879 |
| 12 | Macau International Airport |  | MO | 873 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 730 |
| 15 | Kuala Lumpur International Airport |  | MY | 712 |
| 16 | Madrid Barajas International Airport |  | ES | 702 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 665 |
| 18 | Bengaluru International Airport |  | IN | 657 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 650 |
| 20 | Malpensa International Airport |  | IT | 647 |
| 21 | Salt Lake City International Airport |  | US | 617 |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 612 |
| 23 | Congonhas Airport |  | BR | 597 |
| 24 | Charlotte/Douglas International Airport |  | US | 591 |
| 25 | Charles de Gaulle International Airport |  | FR | 585 |
| 26 | Capua Airport |  | IT | 581 |
| 27 | Tenerife Norte Airport |  | ES | 562 |
| 28 | Daniel K Inouye International Airport |  | US | 550 |
| 29 | Ninoy Aquino International Airport |  | PH | 550 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 540 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 519 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 504 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 501 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Don Mueang International Airport |  | TH | 475 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 473 |
| 38 | Amsterdam Airport Schiphol |  | NL | 470 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 369 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 267 | 21m | 244 km | 1,124.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 177 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 138 | 20m | 99 km | 236.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 113 | 27m | 215 km | 418.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 113 | 20m | 147 km | 286.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SVA986 | Saudia | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-08 18:52 UTC | 2026-05-09 13:55 UTC | 19h 2m |
| N49KC |  | Flying Cloud Airport (KFCM) | Joe Foss Field (KFSD) | 2026-05-09 13:07 UTC | 2026-05-09 13:54 UTC | 46m |
| FHSMB | FHS | Valence-Chabeuil Airport (LFLU) | Macon-Charnay Airport (LFLM) | 2026-05-09 13:01 UTC | 2026-05-09 13:54 UTC | 52m |
| FFT1150 | FFT | Denver International Airport (KDEN) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 12:20 UTC | 2026-05-09 13:50 UTC | 1h 29m |
| LOT2CG | LOT Polish Airlines | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-09 13:25 UTC | 2026-05-09 13:45 UTC | 19m |
| CCA107 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-05-09 11:05 UTC | 2026-05-09 13:45 UTC | 2h 39m |
| UFX62 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-05-09 13:18 UTC | 2026-05-09 13:40 UTC | 21m |
| N4542T |  | Fort Lauderdale Executive Airport (KFXE) | Palm Beach County Park Airport (KLNA) | 2026-05-09 12:51 UTC | 2026-05-09 13:37 UTC | 46m |
| D9720 |  | Schanis Airport (LSZX) | Bad Ragaz Airport (LSZE) | 2026-05-09 11:10 UTC | 2026-05-09 13:37 UTC | 2h 26m |
| N773SP |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-05-09 13:23 UTC | 2026-05-09 13:36 UTC | 13m |
| EZY34YK | easyJet | Jersey Airport (EGJJ) | London Gatwick Airport (EGKK) | 2026-05-09 13:00 UTC | 2026-05-09 13:35 UTC | 35m |
| SWA2573 | Southwest Airlines | Louis Armstrong New Orleans International Airport (KMSY) | Denver International Airport (KDEN) | 2026-05-09 11:01 UTC | 2026-05-09 13:34 UTC | 2h 33m |
| D4727 |  | Flensburg-Schäferhaus Airport (EDXF) | Flensburg-Schäferhaus Airport (EDXF) | 2026-05-09 13:18 UTC | 2026-05-09 13:29 UTC | 10m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | Grenoble Le Versoud Airport (LFLG) | 2026-05-09 13:11 UTC | 2026-05-09 13:29 UTC | 17m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 12:50 UTC | 2026-05-09 13:26 UTC | 36m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-09 13:18 UTC | 2026-05-09 13:26 UTC | 8m |
| ZKIGG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-05-09 13:12 UTC | 2026-05-09 13:24 UTC | 12m |
| N80790 |  | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-05-09 12:51 UTC | 2026-05-09 13:24 UTC | 33m |
| CXK644 | CXK | Dupage Airport (KDPA) | IS47 (IS47) | 2026-05-09 12:04 UTC | 2026-05-09 13:15 UTC | 1h 11m |
| N467AA |  | Addington Field (4TX8) | Denton Enterprise Airport (KDTO) | 2026-05-09 12:55 UTC | 2026-05-09 13:11 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
