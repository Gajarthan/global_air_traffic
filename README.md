# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_11:06:48_UTC-green)

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

**Latest saved flight:** 2026-05-04 11:06:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 11:06:48 UTC

- **67,405** saved flights
- **25,372** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,405** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **829,162.3 tonnes** estimated CO2 emissions
- **48,067,381 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2884 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1562 |
| 4 | EJA | 1202 |
| 5 | American Airlines | 1041 |
| 6 | Southwest Airlines | 946 |
| 7 | Lufthansa | 867 |
| 8 | ENY | 829 |
| 9 | Vueling | 665 |
| 10 | AXM | 655 |
| 11 | LATAM Airlines | 627 |
| 12 | All Nippon Airways | 579 |
| 13 | Delta Air Lines | 564 |
| 14 | WIF | 562 |
| 15 | AZU | 544 |
| 16 | QLK | 523 |
| 17 | Swiss International | 521 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 457 |
| 20 | easyJet | 451 |
| 21 | AEE | 445 |
| 22 | EJU | 435 |
| 23 | VIV | 419 |
| 24 | Cathay Pacific | 409 |
| 25 | Air France | 397 |
| 26 | Japan Airlines | 397 |
| 27 | AXB | 382 |
| 28 | AIQ | 343 |
| 29 | CXK | 342 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53181 |
| 2 | 🇪🇸 ES | 4942 |
| 3 | 🇮🇳 IN | 4924 |
| 4 | 🇦🇺 AU | 4492 |
| 5 | 🇧🇷 BR | 3780 |
| 6 | 🇩🇪 DE | 3778 |
| 7 | 🇮🇹 IT | 3690 |
| 8 | 🇯🇵 JP | 3654 |
| 9 | 🇨🇦 CA | 3294 |
| 10 | 🇬🇧 GB | 2924 |
| 11 | 🇫🇷 FR | 2676 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2137 |
| 14 | 🇬🇷 GR | 2032 |
| 15 | 🇨🇭 CH | 1886 |
| 16 | 🇳🇴 NO | 1832 |
| 17 | 🇲🇾 MY | 1621 |
| 18 | 🇿🇦 ZA | 1363 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1225 |
| 21 | 🇹🇷 TR | 1210 |
| 22 | 🇵🇭 PH | 1133 |
| 23 | 🇵🇱 PL | 1102 |
| 24 | 🇬🇹 GT | 1091 |
| 25 | 🇰🇷 KR | 1088 |
| 26 | 🇲🇦 MA | 823 |
| 27 | 🇲🇴 MO | 766 |
| 28 | 🇲🇪 ME | 731 |
| 29 | 🇳🇱 NL | 710 |
| 30 | 🇮🇩 ID | 579 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1482 |
| 2 | Tokyo International Airport |  | JP | 1231 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1027 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 990 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 872 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 839 |
| 10 | La Aurora Airport |  | GT | 810 |
| 11 | Zurich Airport |  | CH | 801 |
| 12 | Macau International Airport |  | MO | 766 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 663 |
| 14 | Kuala Lumpur International Airport |  | MY | 648 |
| 15 | Chicago O'Hare International Airport |  | US | 645 |
| 16 | Madrid Barajas International Airport |  | ES | 645 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 600 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 20 | Malpensa International Airport |  | IT | 587 |
| 21 | Congonhas Airport |  | BR | 543 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 535 |
| 24 | Charles de Gaulle International Airport |  | FR | 532 |
| 25 | Charlotte/Douglas International Airport |  | US | 529 |
| 26 | Ninoy Aquino International Airport |  | PH | 515 |
| 27 | Capua Airport |  | IT | 511 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 495 |
| 29 | Daniel K Inouye International Airport |  | US | 490 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 473 |
| 31 | Barcelona International Airport |  | ES | 465 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 453 |
| 33 | Vitoria/Foronda Airport |  | ES | 448 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 446 |
| 35 | O. R. Tambo International Airport |  | ZA | 430 |
| 36 | Don Mueang International Airport |  | TH | 428 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 423 |
| 38 | Amsterdam Airport Schiphol |  | NL | 417 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 229 | 21m | 244 km | 964.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 193 | 1h 27m | 910 km | 3,028.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 168 | 20m | 165 km | 477.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 161 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 151 | 26m | 275 km | 715.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 149 | 1h 12m | 770 km | 1,979.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 112 | 31m | 369 km | 712.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 112 | 27m | 152 km | 292.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 94 | 14m | 154 km | 249.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 2m | 695 km | 1,102.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 90 | 1h 43m | 1,423 km | 2,208.7 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GCICC | GCI | Denham Aerodrome (EGLD) | Denham Aerodrome (EGLD) | 2026-05-04 10:52 UTC | 2026-05-04 11:06 UTC | 14m |
| N252FL |  | Tallahassee International Airport (KTLH) | Bartow Executive Airport (KBOW) | 2026-05-04 10:03 UTC | 2026-05-04 10:52 UTC | 49m |
| ZAM29 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-04 10:28 UTC | 2026-05-04 10:39 UTC | 10m |
| 3AMAX |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-04 10:19 UTC | 2026-05-04 10:35 UTC | 15m |
| AFR41GW | Air France | Charles de Gaulle International Airport (LFPG) | Lisbon Portela Airport (LPPT) | 2026-05-04 08:14 UTC | 2026-05-04 10:30 UTC | 2h 15m |
| DMYTD | DMY | Muhldorf Airport (EDMY) | Eggenfelden Airport (EDME) | 2026-05-04 09:57 UTC | 2026-05-04 10:28 UTC | 31m |
| KLM1 | KLM Royal Dutch | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-05-04 09:47 UTC | 2026-05-04 10:27 UTC | 39m |
| OAL068 | OAL | Eleftherios Venizelos International Airport (LGAV) | Syros Airport (LGSO) | 2026-05-04 09:59 UTC | 2026-05-04 10:26 UTC | 27m |
| EZY435N | easyJet | Liverpool John Lennon Airport (EGGP) | Belfast International Airport (EGAA) | 2026-05-04 09:53 UTC | 2026-05-04 10:24 UTC | 30m |
| IGO254J | IndiGo | Indira Gandhi International Airport (VIDP) | Akbarpur Airport (VI90) | 2026-05-04 09:26 UTC | 2026-05-04 10:19 UTC | 52m |
| JST779 | JST | Adelaide International Airport (YPAD) | Melbourne International Airport (YMML) | 2026-05-04 09:02 UTC | 2026-05-04 10:19 UTC | 1h 16m |
| AEE273 | AEE | Olimboi Airport (LG56) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-04 09:34 UTC | 2026-05-04 10:18 UTC | 44m |
| RYR80NW | Ryanair | London Luton Airport (EGGW) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-04 08:15 UTC | 2026-05-04 10:13 UTC | 1h 58m |
| AEE2Z | AEE | Mikonos Airport (LGMK) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-04 09:41 UTC | 2026-05-04 10:09 UTC | 27m |
| POLICER | POL | Innsbruck Airport (LOWI) | Innsbruck Airport (LOWI) | 2026-05-04 09:57 UTC | 2026-05-04 10:07 UTC | 10m |
| OKELA | OKE | Malaga Airport (LEMG) | Sofia Airport (LBSF) | 2026-05-04 07:05 UTC | 2026-05-04 10:05 UTC | 3h 0m |
| RYR1NL | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-05-04 08:57 UTC | 2026-05-04 10:05 UTC | 1h 7m |
| PEV101 | PEV | Voslau Airport (LOAV) | Friedrichshafen Airport (EDNY) | 2026-05-04 09:20 UTC | 2026-05-04 10:04 UTC | 44m |
| APG715 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-05-04 09:34 UTC | 2026-05-04 10:03 UTC | 29m |
| HRC637 | HRC | Ellington Airport (KEFD) | Orange County Airport (KORG) | 2026-05-04 09:45 UTC | 2026-05-04 10:01 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
