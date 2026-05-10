# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_09:43:41_UTC-green)

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

**Latest saved flight:** 2026-05-10 09:43:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 09:43:41 UTC

- **76,781** saved flights
- **28,105** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,781** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **951,787.5 tonnes** estimated CO2 emissions
- **55,176,088 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3292 |
| 2 | SkyWest Airlines | 2847 |
| 3 | IndiGo | 1710 |
| 4 | EJA | 1410 |
| 5 | American Airlines | 1201 |
| 6 | Southwest Airlines | 1118 |
| 7 | Lufthansa | 999 |
| 8 | ENY | 961 |
| 9 | Delta Air Lines | 796 |
| 10 | Vueling | 739 |
| 11 | AXM | 718 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 656 |
| 14 | All Nippon Airways | 623 |
| 15 | AZU | 611 |
| 16 | QLK | 590 |
| 17 | Swiss International | 580 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 541 |
| 20 | easyJet | 511 |
| 21 | Cathay Pacific | 498 |
| 22 | AEE | 496 |
| 23 | EJU | 495 |
| 24 | VIV | 458 |
| 25 | Japan Airlines | 449 |
| 26 | Air France | 448 |
| 27 | AXB | 425 |
| 28 | CXK | 391 |
| 29 | AIQ | 385 |
| 30 | MXY | 376 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61904 |
| 2 | 🇪🇸 ES | 5492 |
| 3 | 🇮🇳 IN | 5364 |
| 4 | 🇦🇺 AU | 5022 |
| 5 | 🇩🇪 DE | 4328 |
| 6 | 🇧🇷 BR | 4278 |
| 7 | 🇮🇹 IT | 4224 |
| 8 | 🇯🇵 JP | 4007 |
| 9 | 🇨🇦 CA | 3815 |
| 10 | 🇬🇧 GB | 3297 |
| 11 | 🇫🇷 FR | 3043 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2357 |
| 14 | 🇬🇷 GR | 2269 |
| 15 | 🇳🇴 NO | 2104 |
| 16 | 🇨🇭 CH | 2074 |
| 17 | 🇲🇾 MY | 1791 |
| 18 | 🇿🇦 ZA | 1470 |
| 19 | 🇳🇿 NZ | 1391 |
| 20 | 🇹🇷 TR | 1380 |
| 21 | 🇹🇭 TH | 1377 |
| 22 | 🇵🇱 PL | 1281 |
| 23 | 🇵🇭 PH | 1238 |
| 24 | 🇰🇷 KR | 1208 |
| 25 | 🇬🇹 GT | 1199 |
| 26 | 🇲🇴 MO | 911 |
| 27 | 🇲🇦 MA | 907 |
| 28 | 🇲🇪 ME | 821 |
| 29 | 🇳🇱 NL | 800 |
| 30 | 🇭🇷 HR | 666 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1707 |
| 2 | Tokyo International Airport |  | JP | 1345 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1131 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1112 |
| 6 | Frankfurt am Main International Airport |  | DE | 999 |
| 7 | Harry Reid International Airport |  | US | 953 |
| 8 | Macau International Airport |  | MO | 911 |
| 9 | Zurich Airport |  | CH | 903 |
| 10 | La Aurora Airport |  | GT | 900 |
| 11 | Guaymaral Airport |  | CO | 890 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 14 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 754 |
| 15 | Chicago O'Hare International Airport |  | US | 751 |
| 16 | Kuala Lumpur International Airport |  | MY | 719 |
| 17 | Madrid Barajas International Airport |  | ES | 716 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 670 |
| 20 | Bengaluru International Airport |  | IN | 666 |
| 21 | Malpensa International Airport |  | IT | 665 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Charlotte/Douglas International Airport |  | US | 604 |
| 24 | Congonhas Airport |  | BR | 604 |
| 25 | Capua Airport |  | IT | 602 |
| 26 | Charles de Gaulle International Airport |  | FR | 599 |
| 27 | Tenerife Norte Airport |  | ES | 569 |
| 28 | Ninoy Aquino International Airport |  | PH | 563 |
| 29 | Daniel K Inouye International Airport |  | US | 560 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 550 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 520 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 517 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 503 |
| 35 | Don Mueang International Airport |  | TH | 489 |
| 36 | Vitoria/Foronda Airport |  | ES | 486 |
| 37 | Amsterdam Airport Schiphol |  | NL | 480 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 39 | O. R. Tambo International Airport |  | ZA | 460 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 275 | 21m | 244 km | 1,157.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 215 | 28m | 304 km | 1,127.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 208 | 1h 27m | 910 km | 3,264.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 183 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 171 | 1h 12m | 770 km | 2,271.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 165 | 26m | 275 km | 781.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 102 | 57m | 493 km | 867.8 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 94 | 1h 2m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FJO62L | FJO | Torino / Caselle International Airport (LIMF) | Torino / Caselle International Airport (LIMF) | 2026-05-10 09:05 UTC | 2026-05-10 09:43 UTC | 38m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-05-10 08:25 UTC | 2026-05-10 09:35 UTC | 1h 9m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-09 21:44 UTC | 2026-05-10 09:24 UTC | 11h 40m |
| DOC33 | DOC | Bergen Airport Flesland (ENBR) | Bergen Airport Flesland (ENBR) | 2026-05-10 09:11 UTC | 2026-05-10 09:22 UTC | 11m |
| GTI8292 | GTI | Zaragoza Air Base (LEZG) | Macau International Airport (VMMC) | 2026-05-09 18:00 UTC | 2026-05-10 09:17 UTC | 15h 16m |
| JLG855 | JLG | Lovell Field (KCHA) | Nelson Airfield (TN99) | 2026-05-10 08:38 UTC | 2026-05-10 09:09 UTC | 30m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-05-09 21:56 UTC | 2026-05-10 09:08 UTC | 11h 12m |
| N105VE |  | Wels Airport (LOLW) | Wels Airport (LOLW) | 2026-05-10 08:48 UTC | 2026-05-10 09:03 UTC | 14m |
| RYR2EY | Ryanair | Faro Airport (LPFR) | East Midlands Airport (EGNX) | 2026-05-10 06:28 UTC | 2026-05-10 08:59 UTC | 2h 31m |
| DAL1471 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 08:57 UTC | 2026-05-10 08:57 UTC | 0m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-05-10 08:32 UTC | 2026-05-10 08:57 UTC | 24m |
| SAS42G | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-05-10 08:15 UTC | 2026-05-10 08:54 UTC | 38m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-09 21:49 UTC | 2026-05-10 08:54 UTC | 11h 5m |
| BNOB | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-10 08:42 UTC | 2026-05-10 08:54 UTC | 12m |
| WZZ1455 | Wizz Air | Stuttgart Airport (EDDS) | Trstenik Airport (LYTR) | 2026-05-10 07:26 UTC | 2026-05-10 08:54 UTC | 1h 27m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-05-10 08:06 UTC | 2026-05-10 08:50 UTC | 44m |
| ADN87D | ADN | Antalya International Airport (LTAI) | LW70 (LW70) | 2026-05-10 07:12 UTC | 2026-05-10 08:50 UTC | 1h 38m |
| CFG3RW | CFG | Frankfurt am Main International Airport (EDDF) | Malpensa International Airport (LIMC) | 2026-05-10 07:59 UTC | 2026-05-10 08:50 UTC | 50m |
| RYR41ZK | Ryanair | Brindisi / Casale Airport (LIBR) | Malpensa International Airport (LIMC) | 2026-05-10 07:23 UTC | 2026-05-10 08:46 UTC | 1h 22m |
| VOE7XB | VOE | Alicante International Airport (LEAL) | Vitoria/Foronda Airport (LEVT) | 2026-05-10 07:55 UTC | 2026-05-10 08:45 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
