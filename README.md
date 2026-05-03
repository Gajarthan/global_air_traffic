# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_20:10:54_UTC-green)

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

**Latest saved flight:** 2026-05-03 20:10:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 20:10:54 UTC

- **66,635** saved flights
- **25,175** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,635** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **817,573.9 tonnes** estimated CO2 emissions
- **47,395,587 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2848 |
| 2 | SkyWest Airlines | 2461 |
| 3 | IndiGo | 1544 |
| 4 | EJA | 1187 |
| 5 | American Airlines | 1032 |
| 6 | Southwest Airlines | 938 |
| 7 | Lufthansa | 857 |
| 8 | ENY | 820 |
| 9 | Vueling | 659 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 618 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 559 |
| 14 | WIF | 558 |
| 15 | AZU | 536 |
| 16 | Swiss International | 514 |
| 17 | QLK | 513 |
| 18 | LXJ | 484 |
| 19 | Alaska Airlines | 451 |
| 20 | easyJet | 444 |
| 21 | AEE | 435 |
| 22 | EJU | 432 |
| 23 | VIV | 415 |
| 24 | Cathay Pacific | 397 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 375 |
| 28 | CXK | 340 |
| 29 | AIQ | 339 |
| 30 | MXY | 325 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52682 |
| 2 | 🇪🇸 ES | 4900 |
| 3 | 🇮🇳 IN | 4851 |
| 4 | 🇦🇺 AU | 4410 |
| 5 | 🇩🇪 DE | 3739 |
| 6 | 🇧🇷 BR | 3735 |
| 7 | 🇮🇹 IT | 3647 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3246 |
| 10 | 🇬🇧 GB | 2891 |
| 11 | 🇨🇴 CO | 2651 |
| 12 | 🇫🇷 FR | 2647 |
| 13 | 🇲🇽 MX | 2112 |
| 14 | 🇬🇷 GR | 1997 |
| 15 | 🇨🇭 CH | 1869 |
| 16 | 🇳🇴 NO | 1814 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1201 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1099 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1060 |
| 26 | 🇲🇦 MA | 818 |
| 27 | 🇲🇴 MO | 744 |
| 28 | 🇲🇪 ME | 723 |
| 29 | 🇳🇱 NL | 707 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1465 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1096 |
| 4 | Indira Gandhi International Airport |  | IN | 1011 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 972 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 863 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 828 |
| 10 | Zurich Airport |  | CH | 793 |
| 11 | La Aurora Airport |  | GT | 788 |
| 12 | Macau International Airport |  | MO | 744 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 656 |
| 14 | Chicago O'Hare International Airport |  | US | 639 |
| 15 | Kuala Lumpur International Airport |  | MY | 639 |
| 16 | Madrid Barajas International Airport |  | ES | 638 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 598 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 576 |
| 21 | Congonhas Airport |  | BR | 538 |
| 22 | Tenerife Norte Airport |  | ES | 533 |
| 23 | Salt Lake City International Airport |  | US | 531 |
| 24 | Charlotte/Douglas International Airport |  | US | 524 |
| 25 | Charles de Gaulle International Airport |  | FR | 522 |
| 26 | Ninoy Aquino International Airport |  | PH | 504 |
| 27 | Capua Airport |  | IT | 504 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 486 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 469 |
| 31 | Barcelona International Airport |  | ES | 458 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 448 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 444 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Amsterdam Airport Schiphol |  | NL | 416 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 415 |
| 39 | Reno/Tahoe International Airport |  | US | 403 |
| 40 | Calgary International Airport |  | CA | 387 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 226 | 21m | 244 km | 951.6 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 164 | 9m | - | - |
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
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 95 | 1h 42m | 1,156 km | 1,895.2 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N172BH |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-05-03 19:18 UTC | 2026-05-03 20:10 UTC | 52m |
| GJS4171 | GJS | Birmingham-Shuttlesworth International Airport (KBHM) | Chicago O'Hare International Airport (KORD) | 2026-05-03 18:33 UTC | 2026-05-03 20:09 UTC | 1h 36m |
| RPA3495 | Republic Airways | Dane County Regional/Truax Field (KMSN) | Chicago O'Hare International Airport (KORD) | 2026-05-03 19:41 UTC | 2026-05-03 20:09 UTC | 27m |
| N45720 |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-05-03 19:54 UTC | 2026-05-03 20:06 UTC | 12m |
| N690MF |  | Fentress Airpark (XS90) | Fentress Airpark (XS90) | 2026-05-03 18:59 UTC | 2026-05-03 20:05 UTC | 1h 5m |
| N83WA |  | Harry Reid International Airport (KLAS) | Provo Municipal Airport (KPVU) | 2026-05-03 18:53 UTC | 2026-05-03 20:05 UTC | 1h 12m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-03 19:10 UTC | 2026-05-03 20:05 UTC | 55m |
| AEE3FT | AEE | Frankfurt am Main International Airport (EDDF) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-03 17:37 UTC | 2026-05-03 19:59 UTC | 2h 22m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-05-03 19:39 UTC | 2026-05-03 19:57 UTC | 18m |
| N246SF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-03 19:00 UTC | 2026-05-03 19:52 UTC | 51m |
| C6018 |  | Johnstone Point Airport (2AK5) | Merle K (Mudhole) Smith Airport (PACV) | 2026-05-03 19:21 UTC | 2026-05-03 19:48 UTC | 26m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-05-03 19:31 UTC | 2026-05-03 19:47 UTC | 15m |
| N229JP |  | Parkside Airpark (WA87) | Parkside Airpark (WA87) | 2026-05-03 19:15 UTC | 2026-05-03 19:40 UTC | 25m |
| N6012Z |  | Grand Junction Regional Airport (KGJT) | Pinyon Airport (CO43) | 2026-05-03 19:02 UTC | 2026-05-03 19:39 UTC | 36m |
| N7633B |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-05-03 19:35 UTC | 2026-05-03 19:37 UTC | 2m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Las Vegas Airport (MGRD) | 2026-05-03 19:09 UTC | 2026-05-03 19:37 UTC | 28m |
| N169BA |  | Bb Airpark (TE88) | Hidden Valley Ranch Airport (TS90) | 2026-05-03 19:27 UTC | 2026-05-03 19:37 UTC | 10m |
| BRG621 | BRG | Shungnak Airport (PAGH) | Ambler Airport (PAFM) | 2026-05-03 19:21 UTC | 2026-05-03 19:36 UTC | 14m |
| N621HR |  | Brandywine Regional Airport (KOQN) | Myrtle Beach Hardee Airpark (SC21) | 2026-05-03 17:52 UTC | 2026-05-03 19:35 UTC | 1h 42m |
| N123JK |  | Napa County Airport (KAPC) | Rocky Mountain Metro Airport (KBJC) | 2026-05-03 17:44 UTC | 2026-05-03 19:33 UTC | 1h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
