# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_17:53:15_UTC-green)

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

**Latest saved flight:** 2026-05-12 17:53:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 17:53:15 UTC

- **79,277** saved flights
- **28,829** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,277** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **980,583.0 tonnes** estimated CO2 emissions
- **56,845,394 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3425 |
| 2 | SkyWest Airlines | 2939 |
| 3 | IndiGo | 1761 |
| 4 | EJA | 1457 |
| 5 | American Airlines | 1231 |
| 6 | Southwest Airlines | 1159 |
| 7 | Lufthansa | 1047 |
| 8 | ENY | 985 |
| 9 | Delta Air Lines | 861 |
| 10 | Vueling | 762 |
| 11 | AXM | 729 |
| 12 | LATAM Airlines | 719 |
| 13 | WIF | 688 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 623 |
| 16 | Swiss International | 617 |
| 17 | QLK | 592 |
| 18 | LXJ | 575 |
| 19 | Alaska Airlines | 555 |
| 20 | easyJet | 530 |
| 21 | EJU | 514 |
| 22 | AEE | 513 |
| 23 | Cathay Pacific | 503 |
| 24 | VIV | 472 |
| 25 | Air France | 470 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 438 |
| 28 | CXK | 408 |
| 29 | AIQ | 397 |
| 30 | MXY | 395 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64102 |
| 2 | 🇪🇸 ES | 5676 |
| 3 | 🇮🇳 IN | 5510 |
| 4 | 🇦🇺 AU | 5089 |
| 5 | 🇩🇪 DE | 4508 |
| 6 | 🇮🇹 IT | 4415 |
| 7 | 🇧🇷 BR | 4380 |
| 8 | 🇯🇵 JP | 4072 |
| 9 | 🇨🇦 CA | 3948 |
| 10 | 🇬🇧 GB | 3417 |
| 11 | 🇫🇷 FR | 3159 |
| 12 | 🇨🇴 CO | 2707 |
| 13 | 🇲🇽 MX | 2398 |
| 14 | 🇬🇷 GR | 2338 |
| 15 | 🇳🇴 NO | 2205 |
| 16 | 🇨🇭 CH | 2149 |
| 17 | 🇲🇾 MY | 1828 |
| 18 | 🇿🇦 ZA | 1510 |
| 19 | 🇹🇷 TR | 1431 |
| 20 | 🇹🇭 TH | 1408 |
| 21 | 🇳🇿 NZ | 1402 |
| 22 | 🇵🇱 PL | 1327 |
| 23 | 🇵🇭 PH | 1260 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1220 |
| 26 | 🇲🇦 MA | 937 |
| 27 | 🇲🇴 MO | 924 |
| 28 | 🇲🇪 ME | 854 |
| 29 | 🇳🇱 NL | 827 |
| 30 | 🇭🇷 HR | 699 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1736 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1324 |
| 4 | Indira Gandhi International Airport |  | IN | 1165 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1146 |
| 6 | Frankfurt am Main International Airport |  | DE | 1050 |
| 7 | Harry Reid International Airport |  | US | 982 |
| 8 | Zurich Airport |  | CH | 947 |
| 9 | Macau International Airport |  | MO | 924 |
| 10 | La Aurora Airport |  | GT | 919 |
| 11 | Guaymaral Airport |  | CO | 899 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 880 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 801 |
| 15 | Chicago O'Hare International Airport |  | US | 771 |
| 16 | Madrid Barajas International Airport |  | ES | 731 |
| 17 | Kuala Lumpur International Airport |  | MY | 730 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 697 |
| 19 | Malpensa International Airport |  | IT | 683 |
| 20 | Bengaluru International Airport |  | IN | 679 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 22 | Salt Lake City International Airport |  | US | 647 |
| 23 | Capua Airport |  | IT | 647 |
| 24 | Charlotte/Douglas International Airport |  | US | 624 |
| 25 | Charles de Gaulle International Airport |  | FR | 624 |
| 26 | Congonhas Airport |  | BR | 618 |
| 27 | Tenerife Norte Airport |  | ES | 591 |
| 28 | Daniel K Inouye International Airport |  | US | 575 |
| 29 | Ninoy Aquino International Airport |  | PH | 574 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 570 |
| 31 | Barcelona International Airport |  | ES | 534 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 533 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 529 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 522 |
| 35 | Vitoria/Foronda Airport |  | ES | 505 |
| 36 | Don Mueang International Airport |  | TH | 504 |
| 37 | Amsterdam Airport Schiphol |  | NL | 500 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 490 |
| 39 | O. R. Tambo International Airport |  | ZA | 477 |
| 40 | Calgary International Airport |  | CA | 466 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 374 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 285 | 21m | 244 km | 1,200.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 202 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 116 | 20m | 147 km | 293.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 115 | 20m | 250 km | 496.7 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 106 | 57m | 493 km | 901.8 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 105 | 1h 42m | 1,423 km | 2,576.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 105 | 1h 2m | 695 km | 1,258.6 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 100 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 100 | 18m | 144 km | 248.7 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N46385 |  | 3-M's Airport (96GA) | Thomaston-Upson County Airport (KOPN) | 2026-05-12 17:07 UTC | 2026-05-12 17:53 UTC | 45m |
| N51365 |  | Knoxville Downtown Island Airport (KDKX) | Knoxville Downtown Island Airport (KDKX) | 2026-05-12 17:27 UTC | 2026-05-12 17:51 UTC | 24m |
| N34BL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-05-12 17:25 UTC | 2026-05-12 17:47 UTC | 21m |
| QTR44R | Qatar Airways | Berlin Brandenburg Airport (EDDB) | Queen Alia International Airport (OJAI) | 2026-05-12 14:57 UTC | 2026-05-12 17:47 UTC | 2h 49m |
| N501CG |  | Montezuma Airport (19AZ) | Prescott Regional/Ernest A Love Field (KPRC) | 2026-05-12 17:25 UTC | 2026-05-12 17:44 UTC | 19m |
| N122BM |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-05-12 16:49 UTC | 2026-05-12 17:43 UTC | 53m |
| N145AH |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-05-12 16:59 UTC | 2026-05-12 17:39 UTC | 39m |
| N68DF |  | Boise Air Trml/Gowen Field (KBOI) | Z X Ranch Airport (0ID7) | 2026-05-12 17:20 UTC | 2026-05-12 17:39 UTC | 19m |
| N623D |  | Albuquerque International Sunport Airport (KABQ) | Jicarilla Apache Nation Airport (K24N) | 2026-05-12 17:04 UTC | 2026-05-12 17:36 UTC | 31m |
| N456N |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-05-12 17:18 UTC | 2026-05-12 17:36 UTC | 17m |
| PRCBJ | PRC | Congonhas Airport (SBSP) | Congonhas Airport (SBSP) | 2026-05-12 17:13 UTC | 2026-05-12 17:36 UTC | 22m |
| N739HX |  | Jackson County/Reynolds Field (KJXN) | Jackson County/Reynolds Field (KJXN) | 2026-05-12 16:35 UTC | 2026-05-12 17:27 UTC | 52m |
| OXF2880 | OXF | Falcon Field (KFFZ) | Four Pillars Airport (AZ21) | 2026-05-12 15:57 UTC | 2026-05-12 17:26 UTC | 1h 28m |
| QTR89C | Qatar Airways | Oslo Gardermoen Airport (ENGM) | Queen Alia International Airport (OJAI) | 2026-05-12 13:17 UTC | 2026-05-12 17:23 UTC | 4h 5m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-12 16:57 UTC | 2026-05-12 17:21 UTC | 23m |
| HTY292 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-05-12 16:50 UTC | 2026-05-12 17:20 UTC | 29m |
| N636KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-12 16:51 UTC | 2026-05-12 17:18 UTC | 27m |
| N424KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-12 16:50 UTC | 2026-05-12 17:18 UTC | 27m |
| RYR6221 | Ryanair | Bristol International Airport (EGGD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-12 15:12 UTC | 2026-05-12 17:18 UTC | 2h 5m |
| N864MC |  | Greenville Spartanburg International Airport (KGSP) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-05-12 16:41 UTC | 2026-05-12 17:17 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
