# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_21:34:39_UTC-green)

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

**Latest saved flight:** 2026-05-22 21:34:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 21:34:39 UTC

- **91,985** saved flights
- **32,662** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,985** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,131,843.5 tonnes** estimated CO2 emissions
- **65,614,118 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3904 |
| 2 | SkyWest Airlines | 3411 |
| 3 | IndiGo | 1913 |
| 4 | EJA | 1743 |
| 5 | American Airlines | 1395 |
| 6 | Southwest Airlines | 1329 |
| 7 | ENY | 1135 |
| 8 | Lufthansa | 1123 |
| 9 | Delta Air Lines | 1009 |
| 10 | Vueling | 877 |
| 11 | LATAM Airlines | 822 |
| 12 | AXM | 806 |
| 13 | WIF | 806 |
| 14 | AZU | 732 |
| 15 | LXJ | 699 |
| 16 | Swiss International | 691 |
| 17 | All Nippon Airways | 685 |
| 18 | Alaska Airlines | 645 |
| 19 | QLK | 644 |
| 20 | easyJet | 603 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 558 |
| 24 | VIV | 545 |
| 25 | Air France | 540 |
| 26 | CXK | 484 |
| 27 | Japan Airlines | 484 |
| 28 | MXY | 474 |
| 29 | AXB | 466 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76048 |
| 2 | 🇪🇸 ES | 6492 |
| 3 | 🇮🇳 IN | 6013 |
| 4 | 🇦🇺 AU | 5691 |
| 5 | 🇩🇪 DE | 5050 |
| 6 | 🇧🇷 BR | 5035 |
| 7 | 🇮🇹 IT | 5023 |
| 8 | 🇨🇦 CA | 4641 |
| 9 | 🇯🇵 JP | 4444 |
| 10 | 🇬🇧 GB | 3925 |
| 11 | 🇫🇷 FR | 3711 |
| 12 | 🇨🇴 CO | 3186 |
| 13 | 🇲🇽 MX | 2833 |
| 14 | 🇬🇷 GR | 2627 |
| 15 | 🇳🇴 NO | 2572 |
| 16 | 🇨🇭 CH | 2406 |
| 17 | 🇲🇾 MY | 2033 |
| 18 | 🇹🇷 TR | 1672 |
| 19 | 🇿🇦 ZA | 1667 |
| 20 | 🇳🇿 NZ | 1573 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1503 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1398 |
| 25 | 🇬🇹 GT | 1383 |
| 26 | 🇲🇦 MA | 1058 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇳🇱 NL | 927 |
| 29 | 🇲🇪 ME | 925 |
| 30 | 🇭🇷 HR | 830 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1997 |
| 2 | Denver International Airport |  | US | 1549 |
| 3 | Tokyo International Airport |  | JP | 1480 |
| 4 | Indira Gandhi International Airport |  | IN | 1305 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1230 |
| 6 | Harry Reid International Airport |  | US | 1181 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1107 |
| 9 | Zurich Airport |  | CH | 1079 |
| 10 | La Aurora Airport |  | GT | 1058 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1009 |
| 13 | El Dorado International Airport |  | CO | 1002 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 923 |
| 15 | Chicago O'Hare International Airport |  | US | 881 |
| 16 | Madrid Barajas International Airport |  | ES | 830 |
| 17 | Kuala Lumpur International Airport |  | MY | 805 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 768 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 740 |
| 22 | Malpensa International Airport |  | IT | 734 |
| 23 | Bengaluru International Airport |  | IN | 724 |
| 24 | Charles de Gaulle International Airport |  | FR | 718 |
| 25 | Charlotte/Douglas International Airport |  | US | 705 |
| 26 | Congonhas Airport |  | BR | 702 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 641 |
| 30 | Barcelona International Airport |  | ES | 621 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 609 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 600 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 580 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | Amsterdam Airport Schiphol |  | NL | 568 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 546 |
| 40 | O. R. Tambo International Airport |  | ZA | 528 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 454 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 243 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 237 | 14m | 114 km | 464.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 235 | 1h 26m | 910 km | 3,687.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 232 | 28m | 304 km | 1,216.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 211 | 1h 10m | 770 km | 2,803.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 199 | 19m | 165 km | 566.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 150 | 21m | 99 km | 256.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 137 | 27m | 215 km | 507.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 132 | 14m | 154 km | 349.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 126 | 20m | 250 km | 544.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 118 | 1h 1m | 695 km | 1,414.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N224LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-05-22 20:25 UTC | 2026-05-22 21:34 UTC | 1h 8m |
| N23HW |  | CL35 (CL35) | Barstow-Daggett Airport (KDAG) | 2026-05-22 19:38 UTC | 2026-05-22 21:30 UTC | 1h 52m |
| N8650E |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-22 21:07 UTC | 2026-05-22 21:30 UTC | 22m |
| N1954T |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-05-22 20:13 UTC | 2026-05-22 21:23 UTC | 1h 9m |
| AZU4176 | AZU | Santos Dumont Airport (SBRJ) | Amarais Airport (SDAM) | 2026-05-22 20:35 UTC | 2026-05-22 21:21 UTC | 45m |
| AZU2654 | AZU | Viracopos International Airport (SBKP) | Sitio Limoeiro Airport (SSEW) | 2026-05-22 20:58 UTC | 2026-05-22 21:21 UTC | 23m |
| TAM3401 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Siqueira Campos Airport (SSQC) | 2026-05-22 20:43 UTC | 2026-05-22 21:19 UTC | 35m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-05-22 21:01 UTC | 2026-05-22 21:13 UTC | 12m |
| CHX87 | CHX | Dachau-Grobenried Airport (EDMD) | Dachau-Grobenried Airport (EDMD) | 2026-05-22 21:09 UTC | 2026-05-22 21:13 UTC | 3m |
| N604TT |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-05-22 21:08 UTC | 2026-05-22 21:12 UTC | 4m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-05-22 13:32 UTC | 2026-05-22 21:08 UTC | 7h 35m |
| N511KV |  | Grand Junction Regional Airport (KGJT) | Weed Airport (KO46) | 2026-05-22 18:10 UTC | 2026-05-22 21:06 UTC | 2h 55m |
| RYR3T | Ryanair | Catania / Fontanarossa Airport (LICC) | Luqa Airport (LMML) | 2026-05-22 20:41 UTC | 2026-05-22 21:05 UTC | 23m |
| N152WA |  | Long Beach (Daugherty Field) Airport (KLGB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-22 20:19 UTC | 2026-05-22 21:04 UTC | 44m |
| DAH3013 | DAH | Istanbul Airport (LTFM) | Houari Boumediene Airport (DAAG) | 2026-05-22 18:14 UTC | 2026-05-22 21:04 UTC | 2h 49m |
| N79US |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-22 20:04 UTC | 2026-05-22 21:03 UTC | 59m |
| N733BY |  | City Of Colorado Springs Municipal Airport (KCOS) | Lebeau Ranch Airport (0CO5) | 2026-05-22 20:29 UTC | 2026-05-22 21:01 UTC | 31m |
| N528MP |  | Bradshaw Army Airfield (PHSF) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-05-22 20:43 UTC | 2026-05-22 20:59 UTC | 15m |
| N150VT |  | Franklin County State Airport (KFSO) | Franklin County State Airport (KFSO) | 2026-05-22 20:48 UTC | 2026-05-22 20:57 UTC | 8m |
| SKW5310 | SkyWest Airlines | Denver International Airport (KDEN) | Ohkay Owingeh Airport (KE14) | 2026-05-22 20:10 UTC | 2026-05-22 20:52 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
