# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_19:35:56_UTC-green)

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

**Latest saved flight:** 2026-05-15 19:35:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 19:35:56 UTC

- **83,453** saved flights
- **30,182** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,453** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,026,337.9 tonnes** estimated CO2 emissions
- **59,497,852 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3571 |
| 2 | SkyWest Airlines | 3086 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1567 |
| 5 | American Airlines | 1283 |
| 6 | Southwest Airlines | 1217 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1038 |
| 9 | Delta Air Lines | 913 |
| 10 | Vueling | 790 |
| 11 | LATAM Airlines | 753 |
| 12 | AXM | 751 |
| 13 | WIF | 726 |
| 14 | AZU | 656 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 647 |
| 17 | QLK | 615 |
| 18 | LXJ | 610 |
| 19 | Alaska Airlines | 589 |
| 20 | easyJet | 547 |
| 21 | EJU | 534 |
| 22 | AEE | 529 |
| 23 | Cathay Pacific | 518 |
| 24 | VIV | 499 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 443 |
| 28 | CXK | 441 |
| 29 | MXY | 415 |
| 30 | AIQ | 410 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68302 |
| 2 | 🇪🇸 ES | 5919 |
| 3 | 🇮🇳 IN | 5654 |
| 4 | 🇦🇺 AU | 5322 |
| 5 | 🇩🇪 DE | 4663 |
| 6 | 🇮🇹 IT | 4611 |
| 7 | 🇧🇷 BR | 4605 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4152 |
| 10 | 🇬🇧 GB | 3556 |
| 11 | 🇫🇷 FR | 3318 |
| 12 | 🇨🇴 CO | 2784 |
| 13 | 🇲🇽 MX | 2534 |
| 14 | 🇬🇷 GR | 2426 |
| 15 | 🇳🇴 NO | 2331 |
| 16 | 🇨🇭 CH | 2216 |
| 17 | 🇲🇾 MY | 1889 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1482 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1452 |
| 22 | 🇵🇱 PL | 1388 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1267 |
| 26 | 🇲🇦 MA | 969 |
| 27 | 🇲🇴 MO | 953 |
| 28 | 🇲🇪 ME | 884 |
| 29 | 🇳🇱 NL | 858 |
| 30 | 🇭🇷 HR | 747 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1829 |
| 2 | Tokyo International Airport |  | JP | 1406 |
| 3 | Denver International Airport |  | US | 1397 |
| 4 | Indira Gandhi International Airport |  | IN | 1201 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1179 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1037 |
| 8 | Zurich Airport |  | CH | 992 |
| 9 | La Aurora Airport |  | GT | 961 |
| 10 | Macau International Airport |  | MO | 953 |
| 11 | Guaymaral Airport |  | CO | 943 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 928 |
| 13 | El Dorado International Airport |  | CO | 894 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 835 |
| 15 | Chicago O'Hare International Airport |  | US | 806 |
| 16 | Madrid Barajas International Airport |  | ES | 762 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 723 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 20 | Malpensa International Airport |  | IT | 696 |
| 21 | Salt Lake City International Airport |  | US | 695 |
| 22 | Bengaluru International Airport |  | IN | 694 |
| 23 | Capua Airport |  | IT | 678 |
| 24 | Charles de Gaulle International Airport |  | FR | 653 |
| 25 | Charlotte/Douglas International Airport |  | US | 650 |
| 26 | Congonhas Airport |  | BR | 648 |
| 27 | Tenerife Norte Airport |  | ES | 605 |
| 28 | Daniel K Inouye International Airport |  | US | 603 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 561 |
| 32 | Barcelona International Airport |  | ES | 559 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 556 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 539 |
| 35 | Vitoria/Foronda Airport |  | ES | 530 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 521 |
| 38 | Amsterdam Airport Schiphol |  | NL | 519 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 488 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 301 | 21m | 244 km | 1,267.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 213 | 14m | 114 km | 417.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 125 | 27m | 152 km | 326.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 117 | 23m | 55 km | 111.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 100 | 1h 18m | 961 km | 1,657.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N471AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-15 18:29 UTC | 2026-05-15 19:35 UTC | 1h 6m |
| N87VB |  | John Wayne/Orange County Airport (KSNA) | Santa Ynez/Kunkle Field (KIZA) | 2026-05-15 18:34 UTC | 2026-05-15 19:33 UTC | 58m |
| N144PW |  | Charlotte/Monroe Executive Airport (KEQY) | SC79 (SC79) | 2026-05-15 19:09 UTC | 2026-05-15 19:30 UTC | 20m |
| N15MW |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-15 19:18 UTC | 2026-05-15 19:28 UTC | 10m |
| N133CT |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-05-15 19:12 UTC | 2026-05-15 19:27 UTC | 15m |
| AAE125 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-05-15 07:56 UTC | 2026-05-15 19:27 UTC | 11h 30m |
| BOE146 | BOE | Quincy Municipal Airport (K80T) | Boeing Field/King County International Airport (KBFI) | 2026-05-15 18:51 UTC | 2026-05-15 19:26 UTC | 34m |
| N6544K |  | G & N Airport (PS05) | Erie International/Tom Ridge Field (KERI) | 2026-05-15 19:13 UTC | 2026-05-15 19:25 UTC | 12m |
| C6539 |  | San Francisco International Airport (KSFO) | San Francisco International Airport (KSFO) | 2026-05-15 19:09 UTC | 2026-05-15 19:24 UTC | 15m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-15 18:37 UTC | 2026-05-15 19:24 UTC | 46m |
| N524RG |  | Wurtsboro/Sullivan County Airport (KN82) | Lancaster Airport (KLNS) | 2026-05-15 18:25 UTC | 2026-05-15 19:22 UTC | 57m |
| N204SG |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | K5W8 (K5W8) | 2026-05-15 18:49 UTC | 2026-05-15 19:22 UTC | 32m |
| BOX714 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-15 04:27 UTC | 2026-05-15 19:20 UTC | 14h 53m |
| N8837Z |  | Siskiyou County Airport (KSIY) | Rogue Valley International/Medford Airport (KMFR) | 2026-05-15 18:59 UTC | 2026-05-15 19:14 UTC | 15m |
| N543JW |  | Logan-Cache Airport (KLGU) | K36U (K36U) | 2026-05-15 18:37 UTC | 2026-05-15 19:14 UTC | 36m |
| N40ER |  | Savannah/Hilton Head International Airport (KSAV) | Swaids Field (2GA2) | 2026-05-15 18:56 UTC | 2026-05-15 19:09 UTC | 13m |
| N782MM |  | Dubuque Regional Airport (KDBQ) | Harry Reid International Airport (KLAS) | 2026-05-15 16:07 UTC | 2026-05-15 19:08 UTC | 3h 1m |
| N466LP |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-05-15 18:57 UTC | 2026-05-15 19:08 UTC | 11m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-05-15 18:55 UTC | 2026-05-15 19:08 UTC | 12m |
| N2965W |  | Boise Air Trml/Gowen Field (KBOI) | Mountain Home Municipal Airport (KU76) | 2026-05-15 18:49 UTC | 2026-05-15 19:07 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
