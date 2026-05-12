# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_06:29:09_UTC-green)

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

**Latest saved flight:** 2026-05-12 06:29:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 06:29:09 UTC

- **78,493** saved flights
- **28,626** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,493** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **971,775.4 tonnes** estimated CO2 emissions
- **56,334,808 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3381 |
| 2 | SkyWest Airlines | 2924 |
| 3 | IndiGo | 1735 |
| 4 | EJA | 1450 |
| 5 | American Airlines | 1225 |
| 6 | Southwest Airlines | 1154 |
| 7 | Lufthansa | 1027 |
| 8 | ENY | 980 |
| 9 | Delta Air Lines | 858 |
| 10 | Vueling | 752 |
| 11 | AXM | 723 |
| 12 | LATAM Airlines | 714 |
| 13 | WIF | 676 |
| 14 | All Nippon Airways | 630 |
| 15 | AZU | 621 |
| 16 | Swiss International | 600 |
| 17 | QLK | 592 |
| 18 | LXJ | 571 |
| 19 | Alaska Airlines | 553 |
| 20 | easyJet | 525 |
| 21 | AEE | 509 |
| 22 | EJU | 509 |
| 23 | Cathay Pacific | 500 |
| 24 | VIV | 467 |
| 25 | Air France | 463 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 436 |
| 28 | CXK | 402 |
| 29 | MXY | 394 |
| 30 | AIQ | 390 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63599 |
| 2 | 🇪🇸 ES | 5617 |
| 3 | 🇮🇳 IN | 5446 |
| 4 | 🇦🇺 AU | 5065 |
| 5 | 🇩🇪 DE | 4443 |
| 6 | 🇧🇷 BR | 4347 |
| 7 | 🇮🇹 IT | 4346 |
| 8 | 🇯🇵 JP | 4046 |
| 9 | 🇨🇦 CA | 3885 |
| 10 | 🇬🇧 GB | 3373 |
| 11 | 🇫🇷 FR | 3114 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2388 |
| 14 | 🇬🇷 GR | 2314 |
| 15 | 🇳🇴 NO | 2145 |
| 16 | 🇨🇭 CH | 2111 |
| 17 | 🇲🇾 MY | 1813 |
| 18 | 🇿🇦 ZA | 1488 |
| 19 | 🇹🇷 TR | 1418 |
| 20 | 🇳🇿 NZ | 1400 |
| 21 | 🇹🇭 TH | 1394 |
| 22 | 🇵🇱 PL | 1310 |
| 23 | 🇵🇭 PH | 1252 |
| 24 | 🇰🇷 KR | 1222 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 925 |
| 27 | 🇲🇴 MO | 916 |
| 28 | 🇲🇪 ME | 841 |
| 29 | 🇳🇱 NL | 817 |
| 30 | 🇭🇷 HR | 681 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1731 |
| 2 | Tokyo International Airport |  | JP | 1361 |
| 3 | Denver International Airport |  | US | 1316 |
| 4 | Indira Gandhi International Airport |  | IN | 1154 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1135 |
| 6 | Frankfurt am Main International Airport |  | DE | 1031 |
| 7 | Harry Reid International Airport |  | US | 974 |
| 8 | Zurich Airport |  | CH | 927 |
| 9 | Macau International Airport |  | MO | 916 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 872 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 797 |
| 15 | Chicago O'Hare International Airport |  | US | 765 |
| 16 | Kuala Lumpur International Airport |  | MY | 726 |
| 17 | Madrid Barajas International Airport |  | ES | 725 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 696 |
| 19 | Malpensa International Airport |  | IT | 680 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 21 | Bengaluru International Airport |  | IN | 673 |
| 22 | Salt Lake City International Airport |  | US | 644 |
| 23 | Capua Airport |  | IT | 632 |
| 24 | Charlotte/Douglas International Airport |  | US | 621 |
| 25 | Charles de Gaulle International Airport |  | FR | 616 |
| 26 | Congonhas Airport |  | BR | 614 |
| 27 | Tenerife Norte Airport |  | ES | 584 |
| 28 | Daniel K Inouye International Airport |  | US | 571 |
| 29 | Ninoy Aquino International Airport |  | PH | 570 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 559 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 531 |
| 32 | Barcelona International Airport |  | ES | 529 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 515 |
| 35 | Vitoria/Foronda Airport |  | ES | 500 |
| 36 | Don Mueang International Airport |  | TH | 497 |
| 37 | Amsterdam Airport Schiphol |  | NL | 493 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 486 |
| 39 | O. R. Tambo International Airport |  | ZA | 469 |
| 40 | Calgary International Airport |  | CA | 464 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 283 | 21m | 244 km | 1,191.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 226 | 24m | 225 km | 876.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 210 | 1h 27m | 910 km | 3,295.4 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 187 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 173 | 1h 12m | 770 km | 2,298.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 168 | 26m | 275 km | 796.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 111 | 14m | 154 km | 294.1 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 103 | 23m | 55 km | 97.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BHA171 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-05-12 06:18 UTC | 2026-05-12 06:29 UTC | 10m |
| N407CR |  | Sleepy Hollow Airport (18GA) | Rollins Airport (GA53) | 2026-05-12 05:45 UTC | 2026-05-12 06:21 UTC | 36m |
| EWG6110 | EWG | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-05-12 05:25 UTC | 2026-05-12 06:14 UTC | 48m |
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-12 05:10 UTC | 2026-05-12 06:09 UTC | 58m |
| SRR6646 | SRR | Francisco de Sá Carneiro Airport (LPPR) | Lisbon Portela Airport (LPPT) | 2026-05-12 05:28 UTC | 2026-05-12 06:05 UTC | 37m |
| N815SS |  | Soldotna Airport (PASX) | Mcgahan Industrial Airpark (AK73) | 2026-05-12 05:46 UTC | 2026-05-12 05:56 UTC | 10m |
| KLM49K | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Hamburg Airport (EDDH) | 2026-05-12 05:03 UTC | 2026-05-12 05:47 UTC | 43m |
| BSM | BSM | Sunshine Coast Airport (YBMC) | Brisbane Archerfield Airport (YBAF) | 2026-05-12 05:19 UTC | 2026-05-12 05:42 UTC | 22m |
| HL5248 |  | Gimpo International Airport (RKSS) | G 417 Airport (RK34) | 2026-05-12 05:07 UTC | 2026-05-12 05:39 UTC | 32m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-05-12 05:00 UTC | 2026-05-12 05:39 UTC | 38m |
| LJX | LJX | Sunshine Coast Airport (YBMC) | Maryborough Airport (YMYB) | 2026-05-12 05:18 UTC | 2026-05-12 05:34 UTC | 15m |
| AEE304 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-05-12 05:07 UTC | 2026-05-12 05:32 UTC | 24m |
| CRUSH53 | CRU | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | Crown Creek Ranch Airport (57WA) | 2026-05-12 04:15 UTC | 2026-05-12 05:31 UTC | 1h 15m |
| JAL2765 | Japan Airlines | Okadama Airport (RJCO) | Tokachi Airport (RJCT) | 2026-05-12 05:06 UTC | 2026-05-12 05:24 UTC | 17m |
| VJQ | VJQ | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-05-12 04:55 UTC | 2026-05-12 05:24 UTC | 29m |
| EVE121P | EVE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-05-12 04:58 UTC | 2026-05-12 05:23 UTC | 25m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-12 04:55 UTC | 2026-05-12 05:22 UTC | 26m |
| AIQ3239 | AIQ | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-05-12 04:48 UTC | 2026-05-12 05:22 UTC | 34m |
| ISR043 | ISR | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-05-12 05:01 UTC | 2026-05-12 05:22 UTC | 20m |
| AFR6161 | Air France | Marseille Provence Airport (LFML) | Lyon Saint-Exupery Airport (LFLL) | 2026-05-12 04:52 UTC | 2026-05-12 05:21 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
