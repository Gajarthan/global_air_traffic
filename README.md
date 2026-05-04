# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_06:22:09_UTC-green)

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

**Latest saved flight:** 2026-05-04 06:22:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 06:22:09 UTC

- **67,199** saved flights
- **25,322** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,199** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **825,796.4 tonnes** estimated CO2 emissions
- **47,872,258 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2864 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1558 |
| 4 | EJA | 1202 |
| 5 | American Airlines | 1041 |
| 6 | Southwest Airlines | 946 |
| 7 | Lufthansa | 859 |
| 8 | ENY | 829 |
| 9 | Vueling | 662 |
| 10 | AXM | 653 |
| 11 | LATAM Airlines | 626 |
| 12 | All Nippon Airways | 577 |
| 13 | Delta Air Lines | 564 |
| 14 | WIF | 560 |
| 15 | AZU | 543 |
| 16 | QLK | 522 |
| 17 | Swiss International | 515 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 457 |
| 20 | easyJet | 444 |
| 21 | AEE | 439 |
| 22 | EJU | 433 |
| 23 | VIV | 419 |
| 24 | Cathay Pacific | 408 |
| 25 | Japan Airlines | 393 |
| 26 | Air France | 390 |
| 27 | AXB | 377 |
| 28 | CXK | 342 |
| 29 | AIQ | 341 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53172 |
| 2 | 🇪🇸 ES | 4919 |
| 3 | 🇮🇳 IN | 4895 |
| 4 | 🇦🇺 AU | 4475 |
| 5 | 🇧🇷 BR | 3774 |
| 6 | 🇩🇪 DE | 3745 |
| 7 | 🇮🇹 IT | 3662 |
| 8 | 🇯🇵 JP | 3623 |
| 9 | 🇨🇦 CA | 3294 |
| 10 | 🇬🇧 GB | 2893 |
| 11 | 🇫🇷 FR | 2660 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2137 |
| 14 | 🇬🇷 GR | 2007 |
| 15 | 🇨🇭 CH | 1870 |
| 16 | 🇳🇴 NO | 1817 |
| 17 | 🇲🇾 MY | 1618 |
| 18 | 🇿🇦 ZA | 1358 |
| 19 | 🇳🇿 NZ | 1261 |
| 20 | 🇹🇭 TH | 1221 |
| 21 | 🇹🇷 TR | 1207 |
| 22 | 🇵🇭 PH | 1128 |
| 23 | 🇵🇱 PL | 1100 |
| 24 | 🇬🇹 GT | 1091 |
| 25 | 🇰🇷 KR | 1085 |
| 26 | 🇲🇦 MA | 821 |
| 27 | 🇲🇴 MO | 761 |
| 28 | 🇲🇪 ME | 728 |
| 29 | 🇳🇱 NL | 708 |
| 30 | 🇮🇩 ID | 571 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1482 |
| 2 | Tokyo International Airport |  | JP | 1221 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1023 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 978 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 865 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 838 |
| 10 | La Aurora Airport |  | GT | 810 |
| 11 | Zurich Airport |  | CH | 794 |
| 12 | Macau International Airport |  | MO | 761 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 663 |
| 14 | Kuala Lumpur International Airport |  | MY | 648 |
| 15 | Chicago O'Hare International Airport |  | US | 643 |
| 16 | Madrid Barajas International Airport |  | ES | 641 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 598 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 590 |
| 20 | Malpensa International Airport |  | IT | 581 |
| 21 | Congonhas Airport |  | BR | 541 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 533 |
| 24 | Charlotte/Douglas International Airport |  | US | 529 |
| 25 | Charles de Gaulle International Airport |  | FR | 525 |
| 26 | Ninoy Aquino International Airport |  | PH | 513 |
| 27 | Capua Airport |  | IT | 506 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 491 |
| 29 | Daniel K Inouye International Airport |  | US | 490 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 473 |
| 31 | Barcelona International Airport |  | ES | 462 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 453 |
| 33 | Vitoria/Foronda Airport |  | ES | 446 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 445 |
| 35 | O. R. Tambo International Airport |  | ZA | 428 |
| 36 | Don Mueang International Airport |  | TH | 426 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 423 |
| 38 | Amsterdam Airport Schiphol |  | NL | 416 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 229 | 21m | 244 km | 964.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 207 | 24m | 225 km | 803.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 193 | 28m | 304 km | 1,011.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 193 | 1h 27m | 910 km | 3,028.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 168 | 20m | 165 km | 477.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 160 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 150 | 26m | 275 km | 710.8 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 148 | 1h 12m | 770 km | 1,966.1 t |
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
| QFA172 | Qantas | Wellington International Airport (NZWN) | Melbourne International Airport (YMML) | 2026-05-04 02:40 UTC | 2026-05-04 06:22 UTC | 3h 41m |
| TJT91SZ | TJT | Marseille Provence Airport (LFML) | Malpensa International Airport (LIMC) | 2026-05-04 05:02 UTC | 2026-05-04 06:12 UTC | 1h 10m |
| TJT51AL | TJT | Lyon Saint-Exupery Airport (LFLL) | Malpensa International Airport (LIMC) | 2026-05-04 05:00 UTC | 2026-05-04 05:51 UTC | 50m |
| SWR3AP | Swiss International | Valencia Airport (LEVC) | Zurich Airport (LSZH) | 2026-05-04 04:13 UTC | 2026-05-04 05:49 UTC | 1h 36m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-05-04 05:14 UTC | 2026-05-04 05:46 UTC | 32m |
| AM276 |  | Grafton Airport (YGFN) | Woodville Airport (YWVL) | 2026-05-04 05:31 UTC | 2026-05-04 05:42 UTC | 11m |
| QLK225D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Adaminaby Airport (YADI) | 2026-05-04 05:05 UTC | 2026-05-04 05:41 UTC | 36m |
| N130MU |  | Strable Landing Strip (OH99) | Ohio State University Airport (KOSU) | 2026-05-04 05:11 UTC | 2026-05-04 05:40 UTC | 29m |
| RYR9LX | Ryanair | Vienna International Airport (LOWW) | Zaluzani Airport (LQBZ) | 2026-05-04 04:54 UTC | 2026-05-04 05:39 UTC | 44m |
| IGO908 | IndiGo | Juhu Aerodrome (VAJJ) | Shillong Airport (VEBI) | 2026-05-04 03:12 UTC | 2026-05-04 05:38 UTC | 2h 25m |
| BDOG100 | BDO | RAAF Base Richmond (YSRI) | Elengerah Airport (YELG) | 2026-05-04 04:48 UTC | 2026-05-04 05:36 UTC | 47m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-03 17:44 UTC | 2026-05-04 05:35 UTC | 11h 50m |
| SAA030 | SAA | O. R. Tambo International Airport (FAOR) | Dwaalboom Airport (FADB) | 2026-05-04 05:16 UTC | 2026-05-04 05:35 UTC | 19m |
| EJU94TZ | EJU | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-05-04 04:19 UTC | 2026-05-04 05:35 UTC | 1h 16m |
| TWY188 | TWY | Miami-Opa Locka Executive Airport (KOPF) | San Francisco International Airport (KSFO) | 2026-05-03 23:42 UTC | 2026-05-04 05:31 UTC | 5h 48m |
| UBG145 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-05-04 04:57 UTC | 2026-05-04 05:30 UTC | 33m |
| VLG8RK | Vueling | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-05-04 05:05 UTC | 2026-05-04 05:30 UTC | 24m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-05-04 04:35 UTC | 2026-05-04 05:28 UTC | 53m |
| AEE105 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-04 04:50 UTC | 2026-05-04 05:27 UTC | 37m |
| MSA711 | MSA | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Luqa Airport (LMML) | 2026-05-04 04:23 UTC | 2026-05-04 05:27 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
