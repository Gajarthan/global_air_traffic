# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_11:40:41_UTC-green)

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

**Latest saved flight:** 2026-05-05 11:40:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 11:40:41 UTC

- **69,087** saved flights
- **25,855** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,087** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **849,747.9 tonnes** estimated CO2 emissions
- **49,260,748 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2968 |
| 2 | SkyWest Airlines | 2557 |
| 3 | IndiGo | 1595 |
| 4 | EJA | 1242 |
| 5 | American Airlines | 1071 |
| 6 | Southwest Airlines | 978 |
| 7 | Lufthansa | 895 |
| 8 | ENY | 851 |
| 9 | Vueling | 677 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 641 |
| 12 | WIF | 586 |
| 13 | All Nippon Airways | 585 |
| 14 | Delta Air Lines | 580 |
| 15 | AZU | 559 |
| 16 | QLK | 534 |
| 17 | Swiss International | 534 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 473 |
| 20 | easyJet | 460 |
| 21 | AEE | 452 |
| 22 | EJU | 449 |
| 23 | VIV | 430 |
| 24 | Cathay Pacific | 416 |
| 25 | Japan Airlines | 409 |
| 26 | Air France | 407 |
| 27 | AXB | 388 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 337 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54661 |
| 2 | 🇪🇸 ES | 5053 |
| 3 | 🇮🇳 IN | 5018 |
| 4 | 🇦🇺 AU | 4597 |
| 5 | 🇩🇪 DE | 3876 |
| 6 | 🇧🇷 BR | 3868 |
| 7 | 🇮🇹 IT | 3792 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3402 |
| 10 | 🇬🇧 GB | 3001 |
| 11 | 🇫🇷 FR | 2737 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2193 |
| 14 | 🇬🇷 GR | 2072 |
| 15 | 🇨🇭 CH | 1911 |
| 16 | 🇳🇴 NO | 1885 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1385 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1244 |
| 22 | 🇵🇭 PH | 1158 |
| 23 | 🇵🇱 PL | 1137 |
| 24 | 🇬🇹 GT | 1113 |
| 25 | 🇰🇷 KR | 1110 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 786 |
| 28 | 🇲🇪 ME | 747 |
| 29 | 🇳🇱 NL | 723 |
| 30 | 🇮🇩 ID | 587 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1524 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1131 |
| 4 | Indira Gandhi International Airport |  | IN | 1049 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1013 |
| 6 | Frankfurt am Main International Airport |  | DE | 890 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 860 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 828 |
| 11 | Zurich Airport |  | CH | 819 |
| 12 | Macau International Airport |  | MO | 786 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 681 |
| 14 | Kuala Lumpur International Airport |  | MY | 668 |
| 15 | Chicago O'Hare International Airport |  | US | 660 |
| 16 | Madrid Barajas International Airport |  | ES | 659 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 617 |
| 18 | Bengaluru International Airport |  | IN | 605 |
| 19 | Malpensa International Airport |  | IT | 603 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Congonhas Airport |  | BR | 553 |
| 22 | Salt Lake City International Airport |  | US | 552 |
| 23 | Charlotte/Douglas International Airport |  | US | 543 |
| 24 | Charles de Gaulle International Airport |  | FR | 543 |
| 25 | Tenerife Norte Airport |  | ES | 542 |
| 26 | Capua Airport |  | IT | 530 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 509 |
| 29 | Daniel K Inouye International Airport |  | US | 502 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 487 |
| 31 | Barcelona International Airport |  | ES | 479 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 461 |
| 34 | Vitoria/Foronda Airport |  | ES | 457 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 437 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 430 |
| 38 | Amsterdam Airport Schiphol |  | NL | 426 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 408 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 236 | 21m | 244 km | 993.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 156 | 26m | 275 km | 739.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 131 | 21m | 99 km | 224.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 109 | 20m | 250 km | 470.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 106 | 27m | 215 km | 392.6 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| T7KIF |  | Valence-Chabeuil Airport (LFLU) | Saint-Etienne-Boutheon Airport (LFMH) | 2026-05-05 10:52 UTC | 2026-05-05 11:40 UTC | 48m |
| N29263 |  | Fulton County Executive/Charlie Brown Field (KFTY) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-05 11:13 UTC | 2026-05-05 11:31 UTC | 18m |
| THY6201 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-04 22:29 UTC | 2026-05-05 11:31 UTC | 13h 1m |
| RSCU201 | RSC | Sydney Bankstown Airport (YSBK) | Holsworthy (Military) Airport (YSHW) | 2026-05-05 10:24 UTC | 2026-05-05 11:22 UTC | 57m |
| N600HN |  | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-05-05 11:00 UTC | 2026-05-05 11:19 UTC | 19m |
| KAYI0004 | KAY | Sinop Airport (LTCM) | Sinop Airport (LTCM) | 2026-05-05 10:08 UTC | 2026-05-05 11:07 UTC | 58m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-05-05 10:53 UTC | 2026-05-05 11:05 UTC | 12m |
| ZAM40 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-05 10:33 UTC | 2026-05-05 11:03 UTC | 29m |
| WIF3BT | WIF | Bergen Airport Flesland (ENBR) | Haugesund Airport (ENHD) | 2026-05-05 10:48 UTC | 2026-05-05 11:03 UTC | 14m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-05 10:45 UTC | 2026-05-05 10:58 UTC | 13m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-05 10:34 UTC | 2026-05-05 10:57 UTC | 22m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-05 10:34 UTC | 2026-05-05 10:56 UTC | 21m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-05-05 10:17 UTC | 2026-05-05 10:54 UTC | 37m |
| RONIN30 | RON | Bournemouth Airport (EGHH) | Bournemouth Airport (EGHH) | 2026-05-05 09:17 UTC | 2026-05-05 10:54 UTC | 1h 36m |
| N183TS |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-05 10:19 UTC | 2026-05-05 10:54 UTC | 34m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-05-05 10:16 UTC | 2026-05-05 10:53 UTC | 36m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-05 10:17 UTC | 2026-05-05 10:51 UTC | 33m |
| YV671T |  | General Manuel Carlos Piar International Airport (SVPR) | Bocon Airport (SVBN) | 2026-05-05 10:13 UTC | 2026-05-05 10:50 UTC | 37m |
| CRQ703 | CRQ | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Gananoque Airport (CNN8) | 2026-05-05 10:09 UTC | 2026-05-05 10:49 UTC | 39m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-05-05 10:26 UTC | 2026-05-05 10:49 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
