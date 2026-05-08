# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_19:44:16_UTC-green)

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

**Latest saved flight:** 2026-05-08 19:44:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 19:44:16 UTC

- **74,133** saved flights
- **27,434** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,133** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **911,615.6 tonnes** estimated CO2 emissions
- **52,847,278 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3188 |
| 2 | SkyWest Airlines | 2745 |
| 3 | IndiGo | 1664 |
| 4 | EJA | 1364 |
| 5 | American Airlines | 1154 |
| 6 | Southwest Airlines | 1074 |
| 7 | Lufthansa | 963 |
| 8 | ENY | 927 |
| 9 | Vueling | 722 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 686 |
| 12 | Delta Air Lines | 657 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 595 |
| 16 | QLK | 573 |
| 17 | Swiss International | 565 |
| 18 | LXJ | 547 |
| 19 | Alaska Airlines | 519 |
| 20 | easyJet | 489 |
| 21 | EJU | 478 |
| 22 | AEE | 477 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 451 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 430 |
| 27 | AXB | 411 |
| 28 | CXK | 380 |
| 29 | AIQ | 366 |
| 30 | United Airlines | 360 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 59561 |
| 2 | 🇪🇸 ES | 5362 |
| 3 | 🇮🇳 IN | 5229 |
| 4 | 🇦🇺 AU | 4907 |
| 5 | 🇩🇪 DE | 4164 |
| 6 | 🇧🇷 BR | 4147 |
| 7 | 🇮🇹 IT | 4055 |
| 8 | 🇯🇵 JP | 3877 |
| 9 | 🇨🇦 CA | 3692 |
| 10 | 🇬🇧 GB | 3188 |
| 11 | 🇫🇷 FR | 2934 |
| 12 | 🇨🇴 CO | 2686 |
| 13 | 🇲🇽 MX | 2301 |
| 14 | 🇬🇷 GR | 2196 |
| 15 | 🇳🇴 NO | 2075 |
| 16 | 🇨🇭 CH | 2015 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇹🇷 TR | 1328 |
| 20 | 🇳🇿 NZ | 1328 |
| 21 | 🇹🇭 TH | 1317 |
| 22 | 🇵🇱 PL | 1242 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1169 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 880 |
| 27 | 🇲🇴 MO | 853 |
| 28 | 🇲🇪 ME | 795 |
| 29 | 🇳🇱 NL | 774 |
| 30 | 🇧🇸 BS | 623 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1641 |
| 2 | Tokyo International Airport |  | JP | 1303 |
| 3 | Denver International Airport |  | US | 1236 |
| 4 | Indira Gandhi International Airport |  | IN | 1104 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1077 |
| 6 | Frankfurt am Main International Airport |  | DE | 959 |
| 7 | Harry Reid International Airport |  | US | 920 |
| 8 | Guaymaral Airport |  | CO | 881 |
| 9 | El Dorado International Airport |  | CO | 878 |
| 10 | Zurich Airport |  | CH | 875 |
| 11 | La Aurora Airport |  | GT | 874 |
| 12 | Macau International Airport |  | MO | 853 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 747 |
| 14 | Chicago O'Hare International Airport |  | US | 719 |
| 15 | Madrid Barajas International Airport |  | ES | 697 |
| 16 | Kuala Lumpur International Airport |  | MY | 696 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 657 |
| 18 | Malpensa International Airport |  | IT | 641 |
| 19 | Bengaluru International Airport |  | IN | 641 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 604 |
| 22 | Congonhas Airport |  | BR | 586 |
| 23 | Charlotte/Douglas International Airport |  | US | 582 |
| 24 | Capua Airport |  | IT | 575 |
| 25 | Charles de Gaulle International Airport |  | FR | 574 |
| 26 | Tenerife Norte Airport |  | ES | 559 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 541 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 531 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 513 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 510 |
| 32 | Barcelona International Airport |  | ES | 510 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 500 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Amsterdam Airport Schiphol |  | NL | 466 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 465 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 442 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 366 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 261 | 21m | 244 km | 1,099.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 188 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 136 | 21m | 99 km | 233.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 116 | 27m | 152 km | 303.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 101 | 1h 2m | 695 km | 1,210.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 100 | 1h 42m | 1,423 km | 2,454.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 98 | 23m | 55 km | 93.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 91 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAE125 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-05-08 08:14 UTC | 2026-05-08 19:44 UTC | 11h 29m |
| N122BM |  | Ontario International Airport (KONT) | San Bernardino International Airport (KSBD) | 2026-05-08 19:18 UTC | 2026-05-08 19:43 UTC | 24m |
| DAL2699 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 19:26 UTC | 2026-05-08 19:38 UTC | 12m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-05-08 19:16 UTC | 2026-05-08 19:37 UTC | 21m |
| N253JG |  | Parkway Farm Strip (09WI) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-05-08 18:47 UTC | 2026-05-08 19:34 UTC | 46m |
| N467AA |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-05-08 19:20 UTC | 2026-05-08 19:33 UTC | 13m |
| CO76 |  | Campo Fontenelle Airport (SBYS) | Pirassununga Airport (SDPY) | 2026-05-08 18:48 UTC | 2026-05-08 19:32 UTC | 44m |
| ENSAIO81 | ENS | Fazenda Citricola Airport (SJAW) | Fazenda Sao Joao Airport (SING) | 2026-05-08 19:16 UTC | 2026-05-08 19:32 UTC | 16m |
| N40798 |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-05-08 18:54 UTC | 2026-05-08 19:31 UTC | 36m |
| N111BP |  | Dupage Airport (KDPA) | Auburn University Regional Airport (KAUO) | 2026-05-08 17:56 UTC | 2026-05-08 19:30 UTC | 1h 33m |
| EDV4852 | EDV | Tappen Airstrip (8NA0) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 18:40 UTC | 2026-05-08 19:30 UTC | 50m |
| N9526G |  | Peter O Knight Airport (KTPF) | Plant City Airport (KPCM) | 2026-05-08 19:02 UTC | 2026-05-08 19:28 UTC | 26m |
| N86SF |  | Tyler Pounds Regional Airport (KTYR) | Tyler Pounds Regional Airport (KTYR) | 2026-05-08 19:26 UTC | 2026-05-08 19:27 UTC | 1m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-08 19:04 UTC | 2026-05-08 19:25 UTC | 21m |
| N662JJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-05-08 18:50 UTC | 2026-05-08 19:22 UTC | 32m |
| N520TF |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-05-08 18:42 UTC | 2026-05-08 19:20 UTC | 37m |
| N673MA |  | Lewis University Airport (KLOT) | Wix Airport (03IL) | 2026-05-08 19:05 UTC | 2026-05-08 19:18 UTC | 13m |
| N886PC |  | Allentown Queen City Municipal Airport (KXLL) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-05-08 18:20 UTC | 2026-05-08 19:17 UTC | 56m |
| N2219M |  | Meylor Field (9NC9) | Richmond Executive/Chesterfield County Airport (KFCI) | 2026-05-08 18:26 UTC | 2026-05-08 19:15 UTC | 48m |
| N668SR |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-05-08 14:13 UTC | 2026-05-08 19:15 UTC | 5h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
