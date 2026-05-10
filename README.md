# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_20:08:07_UTC-green)

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

**Latest saved flight:** 2026-05-10 20:08:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 20:08:07 UTC

- **77,535** saved flights
- **28,340** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,535** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **961,229.2 tonnes** estimated CO2 emissions
- **55,723,434 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3332 |
| 2 | SkyWest Airlines | 2881 |
| 3 | IndiGo | 1724 |
| 4 | EJA | 1427 |
| 5 | American Airlines | 1209 |
| 6 | Southwest Airlines | 1138 |
| 7 | Lufthansa | 1015 |
| 8 | ENY | 965 |
| 9 | Delta Air Lines | 831 |
| 10 | Vueling | 742 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 709 |
| 13 | WIF | 667 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 616 |
| 16 | QLK | 591 |
| 17 | Swiss International | 591 |
| 18 | LXJ | 567 |
| 19 | Alaska Airlines | 546 |
| 20 | easyJet | 520 |
| 21 | EJU | 504 |
| 22 | AEE | 502 |
| 23 | Cathay Pacific | 498 |
| 24 | VIV | 463 |
| 25 | Air France | 457 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 431 |
| 28 | CXK | 397 |
| 29 | MXY | 388 |
| 30 | AIQ | 386 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62580 |
| 2 | 🇪🇸 ES | 5562 |
| 3 | 🇮🇳 IN | 5409 |
| 4 | 🇦🇺 AU | 5030 |
| 5 | 🇩🇪 DE | 4395 |
| 6 | 🇧🇷 BR | 4311 |
| 7 | 🇮🇹 IT | 4282 |
| 8 | 🇯🇵 JP | 4019 |
| 9 | 🇨🇦 CA | 3842 |
| 10 | 🇬🇧 GB | 3342 |
| 11 | 🇫🇷 FR | 3081 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2371 |
| 14 | 🇬🇷 GR | 2294 |
| 15 | 🇳🇴 NO | 2128 |
| 16 | 🇨🇭 CH | 2096 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇹🇷 TR | 1393 |
| 20 | 🇳🇿 NZ | 1391 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1294 |
| 23 | 🇵🇭 PH | 1242 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1204 |
| 26 | 🇲🇦 MA | 916 |
| 27 | 🇲🇴 MO | 911 |
| 28 | 🇲🇪 ME | 827 |
| 29 | 🇳🇱 NL | 809 |
| 30 | 🇭🇷 HR | 674 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1713 |
| 2 | Tokyo International Airport |  | JP | 1350 |
| 3 | Denver International Airport |  | US | 1292 |
| 4 | Indira Gandhi International Airport |  | IN | 1144 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1126 |
| 6 | Frankfurt am Main International Airport |  | DE | 1018 |
| 7 | Harry Reid International Airport |  | US | 963 |
| 8 | Zurich Airport |  | CH | 915 |
| 9 | Macau International Airport |  | MO | 911 |
| 10 | La Aurora Airport |  | GT | 904 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 816 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 778 |
| 15 | Chicago O'Hare International Airport |  | US | 758 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 721 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 686 |
| 19 | Malpensa International Airport |  | IT | 674 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 673 |
| 21 | Bengaluru International Airport |  | IN | 670 |
| 22 | Salt Lake City International Airport |  | US | 636 |
| 23 | Capua Airport |  | IT | 616 |
| 24 | Charlotte/Douglas International Airport |  | US | 611 |
| 25 | Charles de Gaulle International Airport |  | FR | 611 |
| 26 | Congonhas Airport |  | BR | 609 |
| 27 | Tenerife Norte Airport |  | ES | 578 |
| 28 | Ninoy Aquino International Airport |  | PH | 565 |
| 29 | Daniel K Inouye International Airport |  | US | 562 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 555 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 527 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 33 | Barcelona International Airport |  | ES | 525 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 506 |
| 35 | Vitoria/Foronda Airport |  | ES | 493 |
| 36 | Don Mueang International Airport |  | TH | 490 |
| 37 | Amsterdam Airport Schiphol |  | NL | 487 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 482 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 459 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 277 | 21m | 244 km | 1,166.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 196 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 184 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 118 | 27m | 215 km | 437.0 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 104 | 1h 1m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 103 | 1h 42m | 1,423 km | 2,527.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 101 | 23m | 55 km | 96.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 97 | 18m | 144 km | 241.3 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 96 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL160 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 19:55 UTC | 2026-05-10 20:08 UTC | 12m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-10 19:27 UTC | 2026-05-10 20:08 UTC | 40m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-05-10 19:55 UTC | 2026-05-10 20:05 UTC | 10m |
| QFA25 | Qantas | Sydney Kingsford Smith International Airport (YSSY) | Tokyo International Airport (RJTT) | 2026-05-10 10:32 UTC | 2026-05-10 20:03 UTC | 9h 31m |
| N21SZ |  | Whiteman Airport (KWHP) | Meadows Field (KBFL) | 2026-05-10 19:16 UTC | 2026-05-10 20:02 UTC | 46m |
| N1489L |  | Naper Aero Club Airport (LL10) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-10 19:36 UTC | 2026-05-10 20:00 UTC | 23m |
| EDV4852 | EDV | Tappen Airstrip (8NA0) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 19:04 UTC | 2026-05-10 19:56 UTC | 51m |
| EJA927 | EJA | San Luis Obispo County Regional Airport (KSBP) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-10 19:14 UTC | 2026-05-10 19:49 UTC | 35m |
| DAL2550 | Delta Air Lines | John Glenn Columbus International Airport (KCMH) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 18:06 UTC | 2026-05-10 19:49 UTC | 1h 42m |
| DAL2057 | Delta Air Lines | Cleveland-Hopkins International Airport (KCLE) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 18:04 UTC | 2026-05-10 19:47 UTC | 1h 42m |
| N281CE |  | John Wayne/Orange County Airport (KSNA) | Rocky Mountain Metro Airport (KBJC) | 2026-05-10 17:52 UTC | 2026-05-10 19:46 UTC | 1h 53m |
| N6338D |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-10 19:01 UTC | 2026-05-10 19:45 UTC | 44m |
| N455SM |  | Jacksonville International Airport (KJAX) | Addison Airport (KADS) | 2026-05-10 16:21 UTC | 2026-05-10 19:41 UTC | 3h 20m |
| SWR5AT | Swiss International | John Paul II International Airport Kraków-Balice Airport (EPKK) | Zurich Airport (LSZH) | 2026-05-10 18:11 UTC | 2026-05-10 19:40 UTC | 1h 28m |
| N77YA |  | Lee Airport (KANP) | K38J (K38J) | 2026-05-10 17:03 UTC | 2026-05-10 19:40 UTC | 2h 36m |
| N825JW |  | Phoenix Sky Harbor International Airport (KPHX) | Chiriaco Summit Airport (KL77) | 2026-05-10 19:08 UTC | 2026-05-10 19:39 UTC | 30m |
| GPD954 | GPD | Luis Munoz Marin International Airport (TJSJ) | Cyril E King Airport (TIST) | 2026-05-10 19:23 UTC | 2026-05-10 19:38 UTC | 14m |
| N2673G |  | Boerne Stage Airfield (K5C1) | Boerne Stage Airfield (K5C1) | 2026-05-10 19:22 UTC | 2026-05-10 19:37 UTC | 14m |
| EZS43HQ | EZS | Geneva Cointrin International Airport (LSGG) | Václav Havel Airport (LKPR) | 2026-05-10 18:28 UTC | 2026-05-10 19:34 UTC | 1h 6m |
| N893MA |  | Drake Field (KFYV) | Smith Airport (43KS) | 2026-05-10 18:45 UTC | 2026-05-10 19:34 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
