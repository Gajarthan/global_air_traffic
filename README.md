# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_15:49:23_UTC-green)

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

**Latest saved flight:** 2026-05-12 15:49:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 15:49:23 UTC

- **79,051** saved flights
- **28,769** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,051** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **978,114.9 tonnes** estimated CO2 emissions
- **56,702,314 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3416 |
| 2 | SkyWest Airlines | 2925 |
| 3 | IndiGo | 1756 |
| 4 | EJA | 1454 |
| 5 | American Airlines | 1229 |
| 6 | Southwest Airlines | 1158 |
| 7 | Lufthansa | 1047 |
| 8 | ENY | 982 |
| 9 | Delta Air Lines | 860 |
| 10 | Vueling | 760 |
| 11 | AXM | 728 |
| 12 | LATAM Airlines | 717 |
| 13 | WIF | 685 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 623 |
| 16 | Swiss International | 616 |
| 17 | QLK | 592 |
| 18 | LXJ | 574 |
| 19 | Alaska Airlines | 553 |
| 20 | easyJet | 528 |
| 21 | AEE | 513 |
| 22 | EJU | 513 |
| 23 | Cathay Pacific | 503 |
| 24 | VIV | 468 |
| 25 | Air France | 467 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 438 |
| 28 | CXK | 406 |
| 29 | AIQ | 397 |
| 30 | MXY | 395 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63874 |
| 2 | 🇪🇸 ES | 5662 |
| 3 | 🇮🇳 IN | 5501 |
| 4 | 🇦🇺 AU | 5089 |
| 5 | 🇩🇪 DE | 4498 |
| 6 | 🇮🇹 IT | 4403 |
| 7 | 🇧🇷 BR | 4368 |
| 8 | 🇯🇵 JP | 4072 |
| 9 | 🇨🇦 CA | 3927 |
| 10 | 🇬🇧 GB | 3409 |
| 11 | 🇫🇷 FR | 3152 |
| 12 | 🇨🇴 CO | 2705 |
| 13 | 🇲🇽 MX | 2390 |
| 14 | 🇬🇷 GR | 2335 |
| 15 | 🇳🇴 NO | 2191 |
| 16 | 🇨🇭 CH | 2144 |
| 17 | 🇲🇾 MY | 1827 |
| 18 | 🇿🇦 ZA | 1506 |
| 19 | 🇹🇷 TR | 1428 |
| 20 | 🇹🇭 TH | 1408 |
| 21 | 🇳🇿 NZ | 1402 |
| 22 | 🇵🇱 PL | 1325 |
| 23 | 🇵🇭 PH | 1260 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1212 |
| 26 | 🇲🇦 MA | 932 |
| 27 | 🇲🇴 MO | 923 |
| 28 | 🇲🇪 ME | 854 |
| 29 | 🇳🇱 NL | 826 |
| 30 | 🇭🇷 HR | 695 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1732 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1319 |
| 4 | Indira Gandhi International Airport |  | IN | 1162 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1144 |
| 6 | Frankfurt am Main International Airport |  | DE | 1049 |
| 7 | Harry Reid International Airport |  | US | 982 |
| 8 | Zurich Airport |  | CH | 944 |
| 9 | Macau International Airport |  | MO | 923 |
| 10 | La Aurora Airport |  | GT | 911 |
| 11 | Guaymaral Airport |  | CO | 897 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 874 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 798 |
| 15 | Chicago O'Hare International Airport |  | US | 768 |
| 16 | Madrid Barajas International Airport |  | ES | 731 |
| 17 | Kuala Lumpur International Airport |  | MY | 729 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 697 |
| 19 | Malpensa International Airport |  | IT | 682 |
| 20 | Bengaluru International Airport |  | IN | 677 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 22 | Salt Lake City International Airport |  | US | 645 |
| 23 | Capua Airport |  | IT | 642 |
| 24 | Charlotte/Douglas International Airport |  | US | 624 |
| 25 | Charles de Gaulle International Airport |  | FR | 621 |
| 26 | Congonhas Airport |  | BR | 616 |
| 27 | Tenerife Norte Airport |  | ES | 588 |
| 28 | Ninoy Aquino International Airport |  | PH | 574 |
| 29 | Daniel K Inouye International Airport |  | US | 573 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 569 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 533 |
| 32 | Barcelona International Airport |  | ES | 533 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 521 |
| 35 | Don Mueang International Airport |  | TH | 504 |
| 36 | Vitoria/Foronda Airport |  | ES | 502 |
| 37 | Amsterdam Airport Schiphol |  | NL | 499 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 489 |
| 39 | O. R. Tambo International Airport |  | ZA | 475 |
| 40 | Calgary International Airport |  | CA | 466 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 373 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 284 | 21m | 244 km | 1,195.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 116 | 20m | 147 km | 293.5 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 106 | 57m | 493 km | 901.8 t |
| 23 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 105 | 23m | 55 km | 99.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 100 | 18m | 144 km | 248.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 99 | 12m | - | - |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2270 | United Airlines | Norfolk International Airport (KORF) | Denver International Airport (KDEN) | 2026-05-12 12:10 UTC | 2026-05-12 15:49 UTC | 3h 38m |
| GARMN18 | GAR | New Century Aircenter Airport (KIXD) | Buena Terra Airport (33KS) | 2026-05-12 15:24 UTC | 2026-05-12 15:46 UTC | 21m |
| VALOR56 | VAL | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-05-12 15:24 UTC | 2026-05-12 15:41 UTC | 16m |
| N34205 |  | Mid Valley Airpark (KE98) | KE80 (KE80) | 2026-05-12 15:22 UTC | 2026-05-12 15:40 UTC | 18m |
| N9731F |  | Witham Field (KSUA) | Indiantown Airport (KX58) | 2026-05-12 15:20 UTC | 2026-05-12 15:39 UTC | 18m |
| N416CS |  | 1CO7 (1CO7) | Telluride Regional Airport (KTEX) | 2026-05-12 13:29 UTC | 2026-05-12 15:37 UTC | 2h 7m |
| N350XF |  | Pompano Beach Airpark (KPMP) | FA44 (FA44) | 2026-05-12 15:11 UTC | 2026-05-12 15:36 UTC | 24m |
| SWR331F | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-05-12 15:23 UTC | 2026-05-12 15:35 UTC | 12m |
| N705SG |  | Ontario International Airport (KONT) | Henderson Executive Airport (KHND) | 2026-05-12 14:59 UTC | 2026-05-12 15:34 UTC | 35m |
| N227BM |  | John C Tune Airport (KJWN) | St Pete-Clearwater International Airport (KPIE) | 2026-05-12 13:03 UTC | 2026-05-12 15:32 UTC | 2h 28m |
| UAL2154 | United Airlines | Tulsa International Airport (KTUL) | Denver International Airport (KDEN) | 2026-05-12 14:08 UTC | 2026-05-12 15:31 UTC | 1h 23m |
| N331RF |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Eston Airport (CJR4) | 2026-05-12 14:35 UTC | 2026-05-12 15:30 UTC | 54m |
| OTLDR | OTL | Telluride Regional Airport (KTEX) | Telluride Regional Airport (KTEX) | 2026-05-12 13:58 UTC | 2026-05-12 15:27 UTC | 1h 28m |
| N54FA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-05-12 15:03 UTC | 2026-05-12 15:27 UTC | 23m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-12 15:14 UTC | 2026-05-12 15:26 UTC | 11m |
| CFIOH | CFI | Kitchener / Waterloo Airport (CYKF) | North Bay Airport (CYYB) | 2026-05-12 14:45 UTC | 2026-05-12 15:25 UTC | 40m |
| N5761G |  | 14PA (14PA) | Pottstown Municipal Airport (KN47) | 2026-05-12 14:59 UTC | 2026-05-12 15:25 UTC | 26m |
| UAL728 | United Airlines | John Glenn Columbus International Airport (KCMH) | Denver International Airport (KDEN) | 2026-05-12 12:38 UTC | 2026-05-12 15:24 UTC | 2h 46m |
| IRIVU | IRI | Alghero / Fertilia Airport (LIEA) | Alghero / Fertilia Airport (LIEA) | 2026-05-12 15:13 UTC | 2026-05-12 15:20 UTC | 7m |
| SFY2JM | SFY | Bournemouth Airport (EGHH) | Dunkeswell Airport (EGTU) | 2026-05-12 14:47 UTC | 2026-05-12 15:20 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
