# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_19:23:52_UTC-green)

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

**Latest saved flight:** 2026-05-03 19:23:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 19:23:52 UTC

- **66,465** saved flights
- **25,112** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,465** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **815,594.0 tonnes** estimated CO2 emissions
- **47,280,809 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2841 |
| 2 | SkyWest Airlines | 2448 |
| 3 | IndiGo | 1544 |
| 4 | EJA | 1176 |
| 5 | American Airlines | 1025 |
| 6 | Southwest Airlines | 935 |
| 7 | Lufthansa | 856 |
| 8 | ENY | 816 |
| 9 | Vueling | 657 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 617 |
| 12 | All Nippon Airways | 574 |
| 13 | WIF | 558 |
| 14 | Delta Air Lines | 557 |
| 15 | AZU | 536 |
| 16 | QLK | 513 |
| 17 | Swiss International | 513 |
| 18 | LXJ | 479 |
| 19 | Alaska Airlines | 450 |
| 20 | easyJet | 443 |
| 21 | AEE | 434 |
| 22 | EJU | 431 |
| 23 | VIV | 415 |
| 24 | Cathay Pacific | 397 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 374 |
| 28 | CXK | 340 |
| 29 | AIQ | 339 |
| 30 | GLO | 323 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52459 |
| 2 | 🇪🇸 ES | 4890 |
| 3 | 🇮🇳 IN | 4849 |
| 4 | 🇦🇺 AU | 4410 |
| 5 | 🇩🇪 DE | 3732 |
| 6 | 🇧🇷 BR | 3727 |
| 7 | 🇮🇹 IT | 3639 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3239 |
| 10 | 🇬🇧 GB | 2883 |
| 11 | 🇨🇴 CO | 2651 |
| 12 | 🇫🇷 FR | 2646 |
| 13 | 🇲🇽 MX | 2105 |
| 14 | 🇬🇷 GR | 1995 |
| 15 | 🇨🇭 CH | 1868 |
| 16 | 🇳🇴 NO | 1812 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1198 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1098 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1049 |
| 26 | 🇲🇦 MA | 818 |
| 27 | 🇲🇴 MO | 744 |
| 28 | 🇲🇪 ME | 722 |
| 29 | 🇳🇱 NL | 706 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1456 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1087 |
| 4 | Indira Gandhi International Airport |  | IN | 1010 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 971 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 861 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 825 |
| 10 | Zurich Airport |  | CH | 792 |
| 11 | La Aurora Airport |  | GT | 781 |
| 12 | Macau International Airport |  | MO | 744 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 653 |
| 14 | Kuala Lumpur International Airport |  | MY | 639 |
| 15 | Madrid Barajas International Airport |  | ES | 637 |
| 16 | Chicago O'Hare International Airport |  | US | 633 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 598 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 573 |
| 21 | Congonhas Airport |  | BR | 536 |
| 22 | Tenerife Norte Airport |  | ES | 532 |
| 23 | Salt Lake City International Airport |  | US | 528 |
| 24 | Charlotte/Douglas International Airport |  | US | 523 |
| 25 | Charles de Gaulle International Airport |  | FR | 522 |
| 26 | Ninoy Aquino International Airport |  | PH | 504 |
| 27 | Capua Airport |  | IT | 503 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 485 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 469 |
| 31 | Barcelona International Airport |  | ES | 456 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 446 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 443 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Amsterdam Airport Schiphol |  | NL | 415 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 415 |
| 39 | Reno/Tahoe International Airport |  | US | 401 |
| 40 | Calgary International Airport |  | CA | 386 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 225 | 21m | 244 km | 947.4 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 163 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 121 | 21m | 99 km | 207.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 108 | 27m | 152 km | 282.2 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 94 | 1h 42m | 1,156 km | 1,875.3 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1034 | CXK | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-05-03 19:01 UTC | 2026-05-03 19:23 UTC | 22m |
| N65447 |  | Lakefront Airport (KNEW) | Slidell Airport (KASD) | 2026-05-03 18:43 UTC | 2026-05-03 19:19 UTC | 36m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-03 18:48 UTC | 2026-05-03 19:07 UTC | 18m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-03 18:35 UTC | 2026-05-03 18:59 UTC | 23m |
| N636KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-03 18:21 UTC | 2026-05-03 18:52 UTC | 31m |
| JY91 |  | Norman Y Mineta San Jose International Airport (KSJC) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-03 18:34 UTC | 2026-05-03 18:48 UTC | 14m |
| EJA684 | EJA | Fort Lauderdale Executive Airport (KFXE) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-03 16:35 UTC | 2026-05-03 18:46 UTC | 2h 10m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-05-03 18:31 UTC | 2026-05-03 18:46 UTC | 14m |
| XBONC | XBO | Tlaxcala Airport (MMTA) | Hermanos Serdan International Airport (MMPB) | 2026-05-03 18:27 UTC | 2026-05-03 18:43 UTC | 16m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-03 18:21 UTC | 2026-05-03 18:42 UTC | 21m |
| N228YK |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-05-03 17:53 UTC | 2026-05-03 18:42 UTC | 49m |
| N12JE |  | Bowman Field (KLOU) | Flying B Ranch Airstrip (35TX) | 2026-05-03 15:57 UTC | 2026-05-03 18:40 UTC | 2h 43m |
| N599GR |  | Waterbury-Oxford Airport (KOXC) | Auburn/Lewiston Municipal Airport (KLEW) | 2026-05-03 17:25 UTC | 2026-05-03 18:40 UTC | 1h 14m |
| LXJ540 | LXJ | Chicago Midway International Airport (KMDW) | Miller-Herrold Airport (28MI) | 2026-05-03 18:03 UTC | 2026-05-03 18:40 UTC | 36m |
| BAW794 | British Airways | London Heathrow Airport (EGLL) | Lesce Bled Glider Airport (LJBL) | 2026-05-03 16:51 UTC | 2026-05-03 18:37 UTC | 1h 46m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-03 18:23 UTC | 2026-05-03 18:37 UTC | 13m |
| SCU44 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 84OL (84OL) | 2026-05-03 18:00 UTC | 2026-05-03 18:35 UTC | 34m |
| LND52 | LND | Palm Springs International Airport (KPSP) | Aerostone Airfield (03WN) | 2026-05-03 16:00 UTC | 2026-05-03 18:30 UTC | 2h 29m |
| VIO1B | VIO | Le Castellet Airport (LFMQ) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-03 16:15 UTC | 2026-05-03 18:28 UTC | 2h 12m |
| TGMIK | TGM | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-05-03 18:23 UTC | 2026-05-03 18:28 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
