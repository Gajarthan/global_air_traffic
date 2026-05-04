# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_12:50:40_UTC-green)

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

**Latest saved flight:** 2026-05-04 12:50:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 12:50:40 UTC

- **67,537** saved flights
- **25,403** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,537** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **830,681.4 tonnes** estimated CO2 emissions
- **48,155,444 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2898 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1567 |
| 4 | EJA | 1204 |
| 5 | American Airlines | 1041 |
| 6 | Southwest Airlines | 947 |
| 7 | Lufthansa | 870 |
| 8 | ENY | 829 |
| 9 | Vueling | 665 |
| 10 | AXM | 656 |
| 11 | LATAM Airlines | 629 |
| 12 | All Nippon Airways | 579 |
| 13 | Delta Air Lines | 564 |
| 14 | WIF | 564 |
| 15 | AZU | 546 |
| 16 | QLK | 523 |
| 17 | Swiss International | 523 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 458 |
| 20 | easyJet | 452 |
| 21 | AEE | 449 |
| 22 | EJU | 437 |
| 23 | VIV | 419 |
| 24 | Cathay Pacific | 410 |
| 25 | Japan Airlines | 399 |
| 26 | Air France | 398 |
| 27 | AXB | 382 |
| 28 | AIQ | 346 |
| 29 | CXK | 344 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53242 |
| 2 | 🇪🇸 ES | 4952 |
| 3 | 🇮🇳 IN | 4942 |
| 4 | 🇦🇺 AU | 4497 |
| 5 | 🇧🇷 BR | 3788 |
| 6 | 🇩🇪 DE | 3786 |
| 7 | 🇮🇹 IT | 3706 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3300 |
| 10 | 🇬🇧 GB | 2936 |
| 11 | 🇫🇷 FR | 2687 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2140 |
| 14 | 🇬🇷 GR | 2044 |
| 15 | 🇨🇭 CH | 1889 |
| 16 | 🇳🇴 NO | 1837 |
| 17 | 🇲🇾 MY | 1627 |
| 18 | 🇿🇦 ZA | 1365 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1233 |
| 21 | 🇹🇷 TR | 1213 |
| 22 | 🇵🇭 PH | 1135 |
| 23 | 🇵🇱 PL | 1106 |
| 24 | 🇬🇹 GT | 1093 |
| 25 | 🇰🇷 KR | 1089 |
| 26 | 🇲🇦 MA | 827 |
| 27 | 🇲🇴 MO | 767 |
| 28 | 🇲🇪 ME | 734 |
| 29 | 🇳🇱 NL | 710 |
| 30 | 🇮🇩 ID | 579 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1482 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1032 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 997 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 874 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 841 |
| 10 | La Aurora Airport |  | GT | 811 |
| 11 | Zurich Airport |  | CH | 804 |
| 12 | Macau International Airport |  | MO | 767 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 663 |
| 14 | Kuala Lumpur International Airport |  | MY | 651 |
| 15 | Madrid Barajas International Airport |  | ES | 647 |
| 16 | Chicago O'Hare International Airport |  | US | 645 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 600 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 20 | Malpensa International Airport |  | IT | 589 |
| 21 | Congonhas Airport |  | BR | 545 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 535 |
| 24 | Charles de Gaulle International Airport |  | FR | 533 |
| 25 | Charlotte/Douglas International Airport |  | US | 529 |
| 26 | Ninoy Aquino International Airport |  | PH | 516 |
| 27 | Capua Airport |  | IT | 512 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 499 |
| 29 | Daniel K Inouye International Airport |  | US | 490 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 474 |
| 31 | Barcelona International Airport |  | ES | 467 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 454 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 448 |
| 34 | Vitoria/Foronda Airport |  | ES | 448 |
| 35 | Don Mueang International Airport |  | TH | 432 |
| 36 | O. R. Tambo International Airport |  | ZA | 431 |
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
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 169 | 20m | 165 km | 480.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 161 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 151 | 26m | 275 km | 715.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 113 | 31m | 369 km | 719.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 112 | 27m | 152 km | 292.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 102 | 20m | 147 km | 258.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 95 | 14m | 154 km | 251.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 2m | 695 km | 1,102.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 91 | 1h 43m | 1,423 km | 2,233.3 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N613LG |  | Trenton Mercer Airport (KTTN) | Wings Field (KLOM) | 2026-05-04 12:24 UTC | 2026-05-04 12:50 UTC | 26m |
| N273TM |  | Des Moines International Airport (KDSM) | Joe Foss Field (KFSD) | 2026-05-04 12:06 UTC | 2026-05-04 12:41 UTC | 35m |
| RESCUEBW | RES | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-05-04 12:22 UTC | 2026-05-04 12:41 UTC | 19m |
| N2959U |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-05-04 12:18 UTC | 2026-05-04 12:40 UTC | 22m |
| ASA56 | Alaska Airlines | Ted Stevens Anchorage International Airport (PANC) | Harry Reid International Airport (KLAS) | 2026-05-04 08:04 UTC | 2026-05-04 12:39 UTC | 4h 35m |
| GAF319 | GAF | Evreux-Fauville (BA 105) Air Base (LFOE) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-05-04 11:42 UTC | 2026-05-04 12:38 UTC | 55m |
| PRE54 | PRE | Eagle Soaring Airport (1CD4) | Questa Municipal Nr 2 Airport (KN24) | 2026-05-04 11:53 UTC | 2026-05-04 12:29 UTC | 36m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-05-04 12:02 UTC | 2026-05-04 12:29 UTC | 26m |
| N604D |  | Richmond International Airport (KRIC) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-04 11:19 UTC | 2026-05-04 12:23 UTC | 1h 4m |
| N836FS |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-05-04 12:04 UTC | 2026-05-04 12:22 UTC | 18m |
| N248SG |  | Pocono Mountains Regional Airport (KMPO) | Essex County Airport (KCDW) | 2026-05-04 11:58 UTC | 2026-05-04 12:20 UTC | 22m |
| N748RE |  | Waukegan Ntl Airport (KUGN) | Dane County Regional/Truax Field (KMSN) | 2026-05-04 11:55 UTC | 2026-05-04 12:16 UTC | 20m |
| CXK141 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-04 11:39 UTC | 2026-05-04 12:14 UTC | 35m |
| RYR11CX | Ryanair | Bremen Airport (EDDW) | Otocac Airport (LDRO) | 2026-05-04 10:54 UTC | 2026-05-04 12:14 UTC | 1h 20m |
| N563M |  | Chippewa Valley Regional Airport (KEAU) | Joe Foss Field (KFSD) | 2026-05-04 11:25 UTC | 2026-05-04 12:11 UTC | 46m |
| N723BG |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-04 11:46 UTC | 2026-05-04 12:05 UTC | 18m |
| CXK1106 | CXK | Centennial Airport (KAPA) | Lone Tree Ranch Airport (35CO) | 2026-05-04 11:36 UTC | 2026-05-04 12:01 UTC | 25m |
| N972FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-04 11:02 UTC | 2026-05-04 11:59 UTC | 57m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-05-04 10:54 UTC | 2026-05-04 11:57 UTC | 1h 3m |
| EJU412C | EJU | Nice-Cote d'Azur Airport (LFMN) | Paris-Orly Airport (LFPO) | 2026-05-04 10:50 UTC | 2026-05-04 11:55 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
