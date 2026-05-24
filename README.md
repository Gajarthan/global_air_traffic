# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_11:50:08_UTC-green)

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

**Latest saved flight:** 2026-05-24 11:50:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 11:50:08 UTC

- **93,665** saved flights
- **33,099** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,665** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,151,937.5 tonnes** estimated CO2 emissions
- **66,778,988 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3951 |
| 2 | SkyWest Airlines | 3474 |
| 3 | IndiGo | 1949 |
| 4 | EJA | 1771 |
| 5 | American Airlines | 1423 |
| 6 | Southwest Airlines | 1357 |
| 7 | ENY | 1159 |
| 8 | Lufthansa | 1132 |
| 9 | Delta Air Lines | 1026 |
| 10 | Vueling | 890 |
| 11 | LATAM Airlines | 836 |
| 12 | AXM | 831 |
| 13 | WIF | 815 |
| 14 | AZU | 744 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 701 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 650 |
| 20 | easyJet | 611 |
| 21 | EJU | 601 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 566 |
| 24 | VIV | 555 |
| 25 | Air France | 552 |
| 26 | CXK | 501 |
| 27 | MXY | 495 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 478 |
| 30 | AIQ | 454 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77377 |
| 2 | 🇪🇸 ES | 6572 |
| 3 | 🇮🇳 IN | 6154 |
| 4 | 🇦🇺 AU | 5747 |
| 5 | 🇩🇪 DE | 5141 |
| 6 | 🇧🇷 BR | 5123 |
| 7 | 🇮🇹 IT | 5080 |
| 8 | 🇨🇦 CA | 4736 |
| 9 | 🇯🇵 JP | 4523 |
| 10 | 🇬🇧 GB | 3998 |
| 11 | 🇫🇷 FR | 3784 |
| 12 | 🇨🇴 CO | 3250 |
| 13 | 🇲🇽 MX | 2877 |
| 14 | 🇬🇷 GR | 2689 |
| 15 | 🇳🇴 NO | 2604 |
| 16 | 🇨🇭 CH | 2458 |
| 17 | 🇲🇾 MY | 2098 |
| 18 | 🇹🇷 TR | 1728 |
| 19 | 🇿🇦 ZA | 1699 |
| 20 | 🇳🇿 NZ | 1594 |
| 21 | 🇹🇭 TH | 1590 |
| 22 | 🇵🇱 PL | 1536 |
| 23 | 🇰🇷 KR | 1514 |
| 24 | 🇵🇭 PH | 1419 |
| 25 | 🇬🇹 GT | 1409 |
| 26 | 🇲🇦 MA | 1073 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 939 |
| 29 | 🇲🇪 ME | 935 |
| 30 | 🇭🇷 HR | 849 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2030 |
| 2 | Denver International Airport |  | US | 1579 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1341 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1242 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1144 |
| 8 | Guaymaral Airport |  | CO | 1133 |
| 9 | Zurich Airport |  | CH | 1095 |
| 10 | La Aurora Airport |  | GT | 1077 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1023 |
| 13 | El Dorado International Airport |  | CO | 1021 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 936 |
| 15 | Chicago O'Hare International Airport |  | US | 893 |
| 16 | Madrid Barajas International Airport |  | ES | 838 |
| 17 | Kuala Lumpur International Airport |  | MY | 830 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 789 |
| 19 | Salt Lake City International Airport |  | US | 787 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 747 |
| 22 | Malpensa International Airport |  | IT | 742 |
| 23 | Bengaluru International Airport |  | IN | 737 |
| 24 | Charles de Gaulle International Airport |  | FR | 733 |
| 25 | Charlotte/Douglas International Airport |  | US | 713 |
| 26 | Congonhas Airport |  | BR | 710 |
| 27 | Daniel K Inouye International Airport |  | US | 674 |
| 28 | Tenerife Norte Airport |  | ES | 665 |
| 29 | Ninoy Aquino International Airport |  | PH | 648 |
| 30 | Barcelona International Airport |  | ES | 629 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 625 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 610 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 595 |
| 35 | Vitoria/Foronda Airport |  | ES | 584 |
| 36 | Don Mueang International Airport |  | TH | 582 |
| 37 | Amsterdam Airport Schiphol |  | NL | 579 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 539 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 465 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 202 | 19m | 165 km | 574.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 139 | 27m | 215 km | 514.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 137 | 14m | 154 km | 363.0 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 121 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 115 | 1h 40m | 1,156 km | 2,294.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EMC6 | EMC | London Stansted Airport (EGSS) | Newcastle Airport (EGNT) | 2026-05-24 10:55 UTC | 2026-05-24 11:50 UTC | 54m |
| HBTDZ | HBT | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-05-24 11:32 UTC | 2026-05-24 11:45 UTC | 12m |
| HB2471 |  | Langkampfen Airport (LOIK) | Hoefen Airport (LOIR) | 2026-05-24 09:34 UTC | 2026-05-24 11:35 UTC | 2h 0m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-05-24 07:21 UTC | 2026-05-24 11:23 UTC | 4h 1m |
| HBTDZ | HBT | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-05-24 11:07 UTC | 2026-05-24 11:22 UTC | 15m |
|  |  | Colerne Airport (EGUO) | Colerne Airport (EGUO) | 2026-05-24 11:11 UTC | 2026-05-24 11:12 UTC | 0m |
| WIF8HK | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-05-24 10:49 UTC | 2026-05-24 11:07 UTC | 18m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-24 10:53 UTC | 2026-05-24 11:04 UTC | 10m |
| THA136 | Thai Airways | Suvarnabhumi Airport (VTBS) | VLXL (VLXL) | 2026-05-24 10:09 UTC | 2026-05-24 11:02 UTC | 53m |
| SAS33D | Scandinavian Airlines | Palma De Mallorca Airport (LEPA) | Copenhagen Kastrup Airport (EKCH) | 2026-05-24 08:06 UTC | 2026-05-24 10:57 UTC | 2h 51m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-24 09:56 UTC | 2026-05-24 10:52 UTC | 55m |
| PBD855 | PBD | Ganja Airport (UBBG) | Gyumri Shirak Airport (UDSG) | 2026-05-24 10:28 UTC | 2026-05-24 10:52 UTC | 23m |
| IGO6393 | IndiGo | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-05-24 09:11 UTC | 2026-05-24 10:51 UTC | 1h 39m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-05-24 10:35 UTC | 2026-05-24 10:49 UTC | 13m |
| MAS1276 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-05-24 10:36 UTC | 2026-05-24 10:48 UTC | 12m |
| LOT3KY | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Stanke Dimitrov Highway Strip (LB37) | 2026-05-24 09:23 UTC | 2026-05-24 10:47 UTC | 1h 24m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-05-24 09:18 UTC | 2026-05-24 10:46 UTC | 1h 27m |
| AIQ3310 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Sawan Airport (VTPN) | 2026-05-24 10:21 UTC | 2026-05-24 10:40 UTC | 19m |
| TAM3660 | LATAM Airlines | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Eurico de Aguiar Salles Airport (SBVT) | 2026-05-24 09:58 UTC | 2026-05-24 10:39 UTC | 41m |
| EUP007 | EUP | Nice-Cote d'Azur Airport (LFMN) | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | 2026-05-24 09:57 UTC | 2026-05-24 10:39 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
