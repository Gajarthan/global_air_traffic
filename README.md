# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_09:19:11_UTC-green)

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

**Latest saved flight:** 2026-04-28 09:19:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 09:19:11 UTC

- **57,884** saved flights
- **22,573** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,884** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **703,667.7 tonnes** estimated CO2 emissions
- **40,792,332 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2458 |
| 2 | SkyWest Airlines | 2190 |
| 3 | IndiGo | 1316 |
| 4 | EJA | 1031 |
| 5 | American Airlines | 917 |
| 6 | Southwest Airlines | 831 |
| 7 | ENY | 726 |
| 8 | Lufthansa | 720 |
| 9 | Vueling | 575 |
| 10 | AXM | 565 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 514 |
| 13 | WIF | 484 |
| 14 | AZU | 482 |
| 15 | Delta Air Lines | 475 |
| 16 | QLK | 456 |
| 17 | Swiss International | 450 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 396 |
| 20 | AEE | 385 |
| 21 | easyJet | 380 |
| 22 | EJU | 374 |
| 23 | VIV | 369 |
| 24 | Air France | 338 |
| 25 | Japan Airlines | 335 |
| 26 | Cathay Pacific | 334 |
| 27 | AXB | 315 |
| 28 | JetBlue | 294 |
| 29 | AIQ | 291 |
| 30 | United Airlines | 290 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45878 |
| 2 | 🇪🇸 ES | 4202 |
| 3 | 🇮🇳 IN | 4149 |
| 4 | 🇦🇺 AU | 3945 |
| 5 | 🇧🇷 BR | 3294 |
| 6 | 🇩🇪 DE | 3166 |
| 7 | 🇮🇹 IT | 3166 |
| 8 | 🇯🇵 JP | 3128 |
| 9 | 🇨🇦 CA | 2858 |
| 10 | 🇨🇴 CO | 2604 |
| 11 | 🇬🇧 GB | 2453 |
| 12 | 🇫🇷 FR | 2276 |
| 13 | 🇲🇽 MX | 1829 |
| 14 | 🇬🇷 GR | 1722 |
| 15 | 🇨🇭 CH | 1617 |
| 16 | 🇳🇴 NO | 1566 |
| 17 | 🇲🇾 MY | 1370 |
| 18 | 🇿🇦 ZA | 1171 |
| 19 | 🇳🇿 NZ | 1092 |
| 20 | 🇹🇷 TR | 1052 |
| 21 | 🇹🇭 TH | 1045 |
| 22 | 🇵🇭 PH | 976 |
| 23 | 🇵🇱 PL | 928 |
| 24 | 🇰🇷 KR | 925 |
| 25 | 🇬🇹 GT | 849 |
| 26 | 🇲🇦 MA | 731 |
| 27 | 🇲🇪 ME | 625 |
| 28 | 🇲🇴 MO | 620 |
| 29 | 🇳🇱 NL | 599 |
| 30 | 🇮🇩 ID | 498 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1311 |
| 2 | Tokyo International Airport |  | JP | 1061 |
| 3 | Denver International Airport |  | US | 969 |
| 4 | El Dorado International Airport |  | CO | 878 |
| 5 | Indira Gandhi International Airport |  | IN | 877 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 849 |
| 7 | Guaymaral Airport |  | CO | 800 |
| 8 | Harry Reid International Airport |  | US | 738 |
| 9 | Frankfurt am Main International Airport |  | DE | 709 |
| 10 | Zurich Airport |  | CH | 688 |
| 11 | La Aurora Airport |  | GT | 639 |
| 12 | Macau International Airport |  | MO | 620 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 575 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Madrid Barajas International Airport |  | ES | 539 |
| 16 | Kuala Lumpur International Airport |  | MY | 539 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 512 |
| 19 | Malpensa International Airport |  | IT | 502 |
| 20 | Bengaluru International Airport |  | IN | 498 |
| 21 | Congonhas Airport |  | BR | 474 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Salt Lake City International Airport |  | US | 449 |
| 25 | Ninoy Aquino International Airport |  | PH | 449 |
| 26 | Charles de Gaulle International Airport |  | FR | 447 |
| 27 | Capua Airport |  | IT | 440 |
| 28 | Daniel K Inouye International Airport |  | US | 429 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 424 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 412 |
| 31 | Barcelona International Airport |  | ES | 393 |
| 32 | Vitoria/Foronda Airport |  | ES | 391 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 380 |
| 35 | Reno/Tahoe International Airport |  | US | 374 |
| 36 | O. R. Tambo International Airport |  | ZA | 370 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 38 | Don Mueang International Airport |  | TH | 355 |
| 39 | Amsterdam Airport Schiphol |  | NL | 343 |
| 40 | Calgary International Airport |  | CA | 341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 188 | 21m | 244 km | 791.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 183 | 24m | 225 km | 710.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 168 | 1h 27m | 910 km | 2,636.3 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 143 | 19m | 165 km | 406.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 131 | 26m | 275 km | 620.8 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 117 | 1h 12m | 770 km | 1,554.3 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 91 | 20m | 250 km | 393.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 77 | 58m | 493 km | 655.1 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 74 | 1h 42m | 1,423 km | 1,816.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HLF9872 | HLF | Katowice International Airport (EPKT) | Bezymyanka Airfield (UWWG) | 2026-04-28 06:46 UTC | 2026-04-28 09:19 UTC | 2h 32m |
| FHRSJ | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-28 08:50 UTC | 2026-04-28 09:04 UTC | 13m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-28 08:25 UTC | 2026-04-28 09:03 UTC | 37m |
| MAC101F | MAC | Ibn Batouta Airport (GMTT) | London Gatwick Airport (EGKK) | 2026-04-28 06:36 UTC | 2026-04-28 09:01 UTC | 2h 24m |
| LSI125 | LSI | Ghedi Airport (LIPL) | Macau International Airport (VMMC) | 2026-04-27 22:04 UTC | 2026-04-28 08:59 UTC | 10h 55m |
| THA322 | Thai Airways | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-04-28 07:46 UTC | 2026-04-28 08:55 UTC | 1h 8m |
| QTR8406 | Qatar Airways | Qarnayn Airport (OMAQ) | Macau International Airport (VMMC) | 2026-04-28 02:12 UTC | 2026-04-28 08:55 UTC | 6h 42m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-27 21:41 UTC | 2026-04-28 08:55 UTC | 11h 14m |
| TCFCF | TCF | Gaziemir Airport (LTBK) | Kaklic Airport (LTFA) | 2026-04-28 08:37 UTC | 2026-04-28 08:54 UTC | 17m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-28 01:31 UTC | 2026-04-28 08:50 UTC | 7h 19m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-27 21:37 UTC | 2026-04-28 08:49 UTC | 11h 12m |
| RHL15 | RHL | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-04-28 07:58 UTC | 2026-04-28 08:49 UTC | 51m |
| AEE272 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-28 08:23 UTC | 2026-04-28 08:49 UTC | 25m |
| SHA435 | SHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-04-28 08:11 UTC | 2026-04-28 08:47 UTC | 35m |
| EZY898G | easyJet | Birmingham International Airport (EGBB) | Glasgow International Airport (EGPF) | 2026-04-28 07:53 UTC | 2026-04-28 08:47 UTC | 53m |
| BOE8BX | BOE | Santa Fe Regional Airport (KSAF) | Monte Prieto Ranch Airport (57NM) | 2026-04-28 06:48 UTC | 2026-04-28 08:45 UTC | 1h 56m |
| 27 |  | Szolnok Airport (LHSN) | LHSU (LHSU) | 2026-04-28 08:39 UTC | 2026-04-28 08:44 UTC | 5m |
| ZSKMM | ZSK | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-04-28 08:03 UTC | 2026-04-28 08:44 UTC | 40m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-28 08:32 UTC | 2026-04-28 08:43 UTC | 11m |
| HBLVB | HBL | Emmen Airport (LSME) | Bern Belp Airport (LSZB) | 2026-04-28 08:05 UTC | 2026-04-28 08:42 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
