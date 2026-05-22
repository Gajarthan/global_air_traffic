# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_11:49:18_UTC-green)

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

**Latest saved flight:** 2026-05-22 11:49:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 11:49:18 UTC

- **91,153** saved flights
- **32,406** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,153** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,124,102.1 tonnes** estimated CO2 emissions
- **65,165,340 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3877 |
| 2 | SkyWest Airlines | 3374 |
| 3 | IndiGo | 1906 |
| 4 | EJA | 1726 |
| 5 | American Airlines | 1388 |
| 6 | Southwest Airlines | 1322 |
| 7 | ENY | 1123 |
| 8 | Lufthansa | 1121 |
| 9 | Delta Air Lines | 997 |
| 10 | Vueling | 867 |
| 11 | LATAM Airlines | 818 |
| 12 | AXM | 806 |
| 13 | WIF | 797 |
| 14 | AZU | 722 |
| 15 | Swiss International | 690 |
| 16 | All Nippon Airways | 685 |
| 17 | LXJ | 685 |
| 18 | Alaska Airlines | 644 |
| 19 | QLK | 644 |
| 20 | easyJet | 594 |
| 21 | EJU | 583 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 557 |
| 24 | VIV | 540 |
| 25 | Air France | 532 |
| 26 | Japan Airlines | 484 |
| 27 | CXK | 480 |
| 28 | MXY | 469 |
| 29 | AXB | 464 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 75164 |
| 2 | 🇪🇸 ES | 6447 |
| 3 | 🇮🇳 IN | 5994 |
| 4 | 🇦🇺 AU | 5688 |
| 5 | 🇩🇪 DE | 5016 |
| 6 | 🇧🇷 BR | 4988 |
| 7 | 🇮🇹 IT | 4982 |
| 8 | 🇨🇦 CA | 4585 |
| 9 | 🇯🇵 JP | 4444 |
| 10 | 🇬🇧 GB | 3895 |
| 11 | 🇫🇷 FR | 3651 |
| 12 | 🇨🇴 CO | 3141 |
| 13 | 🇲🇽 MX | 2806 |
| 14 | 🇬🇷 GR | 2615 |
| 15 | 🇳🇴 NO | 2543 |
| 16 | 🇨🇭 CH | 2392 |
| 17 | 🇲🇾 MY | 2031 |
| 18 | 🇿🇦 ZA | 1661 |
| 19 | 🇹🇷 TR | 1661 |
| 20 | 🇳🇿 NZ | 1571 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1492 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1396 |
| 25 | 🇬🇹 GT | 1361 |
| 26 | 🇲🇦 MA | 1049 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 921 |
| 29 | 🇳🇱 NL | 919 |
| 30 | 🇭🇷 HR | 825 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1986 |
| 2 | Denver International Airport |  | US | 1527 |
| 3 | Tokyo International Airport |  | JP | 1480 |
| 4 | Indira Gandhi International Airport |  | IN | 1300 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1228 |
| 6 | Harry Reid International Airport |  | US | 1167 |
| 7 | Frankfurt am Main International Airport |  | DE | 1129 |
| 8 | Guaymaral Airport |  | CO | 1083 |
| 9 | Zurich Airport |  | CH | 1073 |
| 10 | La Aurora Airport |  | GT | 1040 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1000 |
| 13 | El Dorado International Airport |  | CO | 993 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 921 |
| 15 | Chicago O'Hare International Airport |  | US | 876 |
| 16 | Madrid Barajas International Airport |  | ES | 826 |
| 17 | Kuala Lumpur International Airport |  | MY | 804 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 774 |
| 19 | Salt Lake City International Airport |  | US | 766 |
| 20 | Capua Airport |  | IT | 761 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 739 |
| 22 | Malpensa International Airport |  | IT | 730 |
| 23 | Bengaluru International Airport |  | IN | 719 |
| 24 | Charles de Gaulle International Airport |  | FR | 709 |
| 25 | Charlotte/Douglas International Airport |  | US | 702 |
| 26 | Congonhas Airport |  | BR | 696 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 662 |
| 29 | Ninoy Aquino International Airport |  | PH | 640 |
| 30 | Barcelona International Airport |  | ES | 613 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 603 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 596 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 575 |
| 35 | Vitoria/Foronda Airport |  | ES | 574 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 38 | Amsterdam Airport Schiphol |  | NL | 564 |
| 39 | Calgary International Airport |  | CA | 543 |
| 40 | O. R. Tambo International Airport |  | ZA | 525 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 443 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 237 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 235 | 1h 26m | 910 km | 3,687.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 232 | 28m | 304 km | 1,216.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 211 | 1h 10m | 770 km | 2,803.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 199 | 19m | 165 km | 566.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 149 | 21m | 99 km | 255.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 133 | 27m | 152 km | 347.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 132 | 14m | 154 km | 349.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 124 | 20m | 250 km | 535.6 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 118 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 118 | 18m | 144 km | 293.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-22 09:53 UTC | 2026-05-22 11:49 UTC | 1h 55m |
| UAE9964 | Emirates | Los Angeles International Airport (KLAX) | Zhuhai Airport (ZGSD) | 2026-05-21 10:24 UTC | 2026-05-22 11:47 UTC | 25h 23m |
| FHBVM | FHB | Ste Leocadie Airport (LFYS) | Ste Leocadie Airport (LFYS) | 2026-05-22 11:33 UTC | 2026-05-22 11:44 UTC | 10m |
| LOT4KK | LOT Polish Airlines | Riga International Airport (EVRA) | Valenciunai Airport (EYLN) | 2026-05-22 11:31 UTC | 2026-05-22 11:43 UTC | 11m |
| N62770 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-22 10:42 UTC | 2026-05-22 11:39 UTC | 56m |
| TEST123 | TES | Vilnius International Airport (EYVI) | Vilnius International Airport (EYVI) | 2026-05-22 11:16 UTC | 2026-05-22 11:34 UTC | 18m |
| DKYHB | DKY | Burg Feuerstein Airport (EDQE) | Zell-Haidberg Airport (EDNZ) | 2026-05-22 09:50 UTC | 2026-05-22 11:24 UTC | 1h 34m |
| SKY726 | SKY | New Chitose Airport (RJCC) | Fukushima Airport (RJSF) | 2026-05-22 10:43 UTC | 2026-05-22 11:19 UTC | 36m |
| TPA4009 | TPA | Miami International Airport (KMIA) | Madrid Air Base (SKMA) | 2026-05-22 08:15 UTC | 2026-05-22 11:18 UTC | 3h 2m |
| SWA1394 | Southwest Airlines | John Glenn Columbus International Airport (KCMH) | Lafayette Municipal Airport (K3M7) | 2026-05-22 10:41 UTC | 2026-05-22 11:18 UTC | 36m |
| BTX1A | BTX | Brussels Airport (EBBR) | Gaspe (Michel-Pouliot) Airport (CYGP) | 2026-05-22 05:42 UTC | 2026-05-22 11:18 UTC | 5h 35m |
| SAMU49 | SAM | Soucelles Airport (LF50) | Soucelles Airport (LF50) | 2026-05-22 11:16 UTC | 2026-05-22 11:17 UTC | 1m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-05-22 11:00 UTC | 2026-05-22 11:16 UTC | 16m |
| FD533 |  | Adelaide International Airport (YPAD) | Port Pirie Airport (YPIR) | 2026-05-22 10:43 UTC | 2026-05-22 11:16 UTC | 33m |
| GTUGY | GTU | EG32 (EG32) | EG32 (EG32) | 2026-05-22 10:59 UTC | 2026-05-22 11:13 UTC | 13m |
| GBTAK | GBT | Gloucestershire Airport (EGBJ) | Ledbury Airport (EG34) | 2026-05-22 10:48 UTC | 2026-05-22 11:06 UTC | 18m |
| SCQ1S | SCQ | Stockholm Vasteras Airport (ESOW) | Stockholm Vasteras Airport (ESOW) | 2026-05-22 11:01 UTC | 2026-05-22 11:06 UTC | 4m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-22 10:08 UTC | 2026-05-22 11:05 UTC | 57m |
| RJA101 | Royal Jordanian | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-22 10:40 UTC | 2026-05-22 11:04 UTC | 24m |
| WIF8HT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-22 10:45 UTC | 2026-05-22 11:01 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
