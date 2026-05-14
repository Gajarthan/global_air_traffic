# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_17:08:47_UTC-green)

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

**Latest saved flight:** 2026-05-14 17:08:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 17:08:47 UTC

- **81,960** saved flights
- **29,694** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,960** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,008,941.8 tonnes** estimated CO2 emissions
- **58,489,380 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3515 |
| 2 | SkyWest Airlines | 3030 |
| 3 | IndiGo | 1799 |
| 4 | EJA | 1536 |
| 5 | American Airlines | 1264 |
| 6 | Southwest Airlines | 1196 |
| 7 | Lufthansa | 1061 |
| 8 | ENY | 1023 |
| 9 | Delta Air Lines | 899 |
| 10 | Vueling | 777 |
| 11 | AXM | 746 |
| 12 | LATAM Airlines | 743 |
| 13 | WIF | 714 |
| 14 | All Nippon Airways | 646 |
| 15 | AZU | 644 |
| 16 | Swiss International | 639 |
| 17 | QLK | 608 |
| 18 | LXJ | 593 |
| 19 | Alaska Airlines | 578 |
| 20 | easyJet | 544 |
| 21 | EJU | 528 |
| 22 | AEE | 522 |
| 23 | Cathay Pacific | 510 |
| 24 | VIV | 486 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 441 |
| 28 | CXK | 428 |
| 29 | AIQ | 407 |
| 30 | MXY | 407 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66781 |
| 2 | 🇪🇸 ES | 5818 |
| 3 | 🇮🇳 IN | 5620 |
| 4 | 🇦🇺 AU | 5262 |
| 5 | 🇩🇪 DE | 4608 |
| 6 | 🇮🇹 IT | 4536 |
| 7 | 🇧🇷 BR | 4522 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4071 |
| 10 | 🇬🇧 GB | 3501 |
| 11 | 🇫🇷 FR | 3268 |
| 12 | 🇨🇴 CO | 2728 |
| 13 | 🇲🇽 MX | 2475 |
| 14 | 🇬🇷 GR | 2391 |
| 15 | 🇳🇴 NO | 2305 |
| 16 | 🇨🇭 CH | 2199 |
| 17 | 🇲🇾 MY | 1873 |
| 18 | 🇿🇦 ZA | 1550 |
| 19 | 🇹🇷 TR | 1459 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1436 |
| 22 | 🇵🇱 PL | 1369 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇬🇹 GT | 1256 |
| 25 | 🇰🇷 KR | 1252 |
| 26 | 🇲🇦 MA | 958 |
| 27 | 🇲🇴 MO | 939 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 847 |
| 30 | 🇭🇷 HR | 732 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1794 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1376 |
| 4 | Indira Gandhi International Airport |  | IN | 1192 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1169 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1018 |
| 8 | Zurich Airport |  | CH | 978 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 939 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 920 |
| 12 | Guaymaral Airport |  | CO | 918 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 794 |
| 16 | Madrid Barajas International Airport |  | ES | 751 |
| 17 | Kuala Lumpur International Airport |  | MY | 747 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 716 |
| 19 | Malpensa International Airport |  | IT | 692 |
| 20 | Bengaluru International Airport |  | IN | 691 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 22 | Salt Lake City International Airport |  | US | 675 |
| 23 | Capua Airport |  | IT | 671 |
| 24 | Charles de Gaulle International Airport |  | FR | 645 |
| 25 | Charlotte/Douglas International Airport |  | US | 639 |
| 26 | Congonhas Airport |  | BR | 638 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Ninoy Aquino International Airport |  | PH | 596 |
| 29 | Daniel K Inouye International Airport |  | US | 594 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 551 |
| 32 | Barcelona International Airport |  | ES | 549 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 547 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 532 |
| 35 | Don Mueang International Airport |  | TH | 517 |
| 36 | Vitoria/Foronda Airport |  | ES | 515 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 513 |
| 38 | Amsterdam Airport Schiphol |  | NL | 511 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 481 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 382 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 296 | 21m | 244 km | 1,246.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 171 | 26m | 275 km | 810.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 111 | 1h 2m | 695 km | 1,330.6 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 111 | 23m | 55 km | 105.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 103 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK527 | CXK | Mesa Gateway Airport (KIWA) | Mesa Gateway Airport (KIWA) | 2026-05-14 15:45 UTC | 2026-05-14 17:08 UTC | 1h 23m |
| ROCK91 | ROC | Sandy Creek Airport (73TX) | Comanche Ranch Airport (5TE0) | 2026-05-14 16:44 UTC | 2026-05-14 17:05 UTC | 20m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-14 16:42 UTC | 2026-05-14 17:04 UTC | 21m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-14 16:13 UTC | 2026-05-14 17:02 UTC | 48m |
| WAH | WAH | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-05-14 16:43 UTC | 2026-05-14 16:58 UTC | 14m |
| N102MU |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-05-14 16:41 UTC | 2026-05-14 16:58 UTC | 17m |
| EVIL67 | EVI | 75OK (75OK) | 6OK6 (6OK6) | 2026-05-14 15:49 UTC | 2026-05-14 16:53 UTC | 1h 4m |
| THUD61 | THU | 2TX3 (2TX3) | Benson Airstrip (2XS8) | 2026-05-14 16:33 UTC | 2026-05-14 16:48 UTC | 14m |
| N2135S |  | Clermont County Airport (KI69) | Workman's Landing Airport (OA10) | 2026-05-14 16:30 UTC | 2026-05-14 16:46 UTC | 16m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-14 16:33 UTC | 2026-05-14 16:44 UTC | 10m |
| FAC4482 | FAC | Madrid Air Base (SKMA) | Madrid Air Base (SKMA) | 2026-05-14 16:07 UTC | 2026-05-14 16:42 UTC | 34m |
| SPAGW | SPA | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-05-14 15:30 UTC | 2026-05-14 16:40 UTC | 1h 9m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-14 16:26 UTC | 2026-05-14 16:37 UTC | 10m |
| BOXER04 | BOX | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-05-14 16:25 UTC | 2026-05-14 16:35 UTC | 10m |
| N865CV |  | Scottsdale Airport (KSDL) | Cottonwood Airport (KP52) | 2026-05-14 16:17 UTC | 2026-05-14 16:35 UTC | 18m |
| N323SM |  | Denton Enterprise Airport (KDTO) | Rob Airport (95TS) | 2026-05-14 14:32 UTC | 2026-05-14 16:35 UTC | 2h 3m |
| SCU36 | SCU | Cherokee Ranch Airport (OK25) | Haskell Airport (K2K9) | 2026-05-14 16:06 UTC | 2026-05-14 16:35 UTC | 28m |
| N12ML |  | Boca Raton Airport (KBCT) | Maplewood Farm Airport (CT39) | 2026-05-14 13:46 UTC | 2026-05-14 16:32 UTC | 2h 46m |
| N192MA |  | Aurora Municipal Airport (KARR) | Aurora Municipal Airport (KARR) | 2026-05-14 16:18 UTC | 2026-05-14 16:30 UTC | 11m |
| N9358C |  | Fort Worth Meacham International Airport (KFTW) | Stephenville Clark Regional Airport (KSEP) | 2026-05-14 15:45 UTC | 2026-05-14 16:29 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
