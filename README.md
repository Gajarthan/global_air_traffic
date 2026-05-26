# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_10:17:24_UTC-green)

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

**Latest saved flight:** 2026-05-26 10:17:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-26 10:17:24 UTC

- **94,953** saved flights
- **33,477** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,953** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,168,080.3 tonnes** estimated CO2 emissions
- **67,714,802 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4008 |
| 2 | SkyWest Airlines | 3525 |
| 3 | IndiGo | 1973 |
| 4 | EJA | 1795 |
| 5 | American Airlines | 1441 |
| 6 | Southwest Airlines | 1378 |
| 7 | ENY | 1173 |
| 8 | Lufthansa | 1142 |
| 9 | Delta Air Lines | 1041 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 851 |
| 12 | AXM | 839 |
| 13 | WIF | 831 |
| 14 | AZU | 759 |
| 15 | LXJ | 717 |
| 16 | Swiss International | 711 |
| 17 | All Nippon Airways | 702 |
| 18 | QLK | 660 |
| 19 | Alaska Airlines | 659 |
| 20 | easyJet | 623 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 572 |
| 24 | Air France | 562 |
| 25 | VIV | 562 |
| 26 | CXK | 506 |
| 27 | MXY | 504 |
| 28 | Japan Airlines | 491 |
| 29 | AXB | 480 |
| 30 | AIQ | 457 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78375 |
| 2 | 🇪🇸 ES | 6663 |
| 3 | 🇮🇳 IN | 6221 |
| 4 | 🇦🇺 AU | 5812 |
| 5 | 🇩🇪 DE | 5226 |
| 6 | 🇧🇷 BR | 5199 |
| 7 | 🇮🇹 IT | 5157 |
| 8 | 🇨🇦 CA | 4812 |
| 9 | 🇯🇵 JP | 4551 |
| 10 | 🇬🇧 GB | 4066 |
| 11 | 🇫🇷 FR | 3849 |
| 12 | 🇨🇴 CO | 3284 |
| 13 | 🇲🇽 MX | 2916 |
| 14 | 🇬🇷 GR | 2734 |
| 15 | 🇳🇴 NO | 2648 |
| 16 | 🇨🇭 CH | 2499 |
| 17 | 🇲🇾 MY | 2124 |
| 18 | 🇹🇷 TR | 1761 |
| 19 | 🇿🇦 ZA | 1715 |
| 20 | 🇳🇿 NZ | 1610 |
| 21 | 🇹🇭 TH | 1609 |
| 22 | 🇵🇱 PL | 1559 |
| 23 | 🇰🇷 KR | 1555 |
| 24 | 🇵🇭 PH | 1434 |
| 25 | 🇬🇹 GT | 1423 |
| 26 | 🇲🇦 MA | 1087 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 957 |
| 29 | 🇲🇪 ME | 941 |
| 30 | 🇭🇷 HR | 866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2049 |
| 2 | Denver International Airport |  | US | 1607 |
| 3 | Tokyo International Airport |  | JP | 1510 |
| 4 | Indira Gandhi International Airport |  | IN | 1349 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1255 |
| 6 | Harry Reid International Airport |  | US | 1222 |
| 7 | Frankfurt am Main International Airport |  | DE | 1156 |
| 8 | Guaymaral Airport |  | CO | 1151 |
| 9 | Zurich Airport |  | CH | 1113 |
| 10 | La Aurora Airport |  | GT | 1089 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1030 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1029 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 948 |
| 15 | Chicago O'Hare International Airport |  | US | 918 |
| 16 | Madrid Barajas International Airport |  | ES | 844 |
| 17 | Kuala Lumpur International Airport |  | MY | 843 |
| 18 | Salt Lake City International Airport |  | US | 801 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 799 |
| 20 | Capua Airport |  | IT | 788 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 756 |
| 22 | Malpensa International Airport |  | IT | 750 |
| 23 | Bengaluru International Airport |  | IN | 746 |
| 24 | Charles de Gaulle International Airport |  | FR | 743 |
| 25 | Charlotte/Douglas International Airport |  | US | 722 |
| 26 | Congonhas Airport |  | BR | 722 |
| 27 | Daniel K Inouye International Airport |  | US | 678 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 654 |
| 30 | Barcelona International Airport |  | ES | 641 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 638 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 617 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 608 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 591 |
| 36 | Don Mueang International Airport |  | TH | 589 |
| 37 | Vitoria/Foronda Airport |  | ES | 589 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 562 |
| 40 | O. R. Tambo International Airport |  | ZA | 544 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 472 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 349 | 21m | 244 km | 1,469.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 256 | 24m | 225 km | 993.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 252 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 239 | 28m | 304 km | 1,252.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 218 | 1h 10m | 770 km | 2,896.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 143 | 27m | 215 km | 529.6 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 141 | 14m | 154 km | 373.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 124 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 119 | 1h 39m | 1,156 km | 2,374.0 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 114 | 1h 52m | 1,304 km | 2,564.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RJA5170 | Royal Jordanian | Antalya International Airport (LTAI) | Queen Alia International Airport (OJAI) | 2026-05-26 09:24 UTC | 2026-05-26 10:17 UTC | 52m |
| LINCE81 | LIN | Torrejon Airport (LETO) | Vigo Airport (LEVX) | 2026-05-26 09:03 UTC | 2026-05-26 10:14 UTC | 1h 10m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-26 09:27 UTC | 2026-05-26 10:10 UTC | 42m |
| BRUJO61 | BRU | Torrejon Airport (LETO) | Santiago de Compostela Airport (LEST) | 2026-05-26 08:31 UTC | 2026-05-26 10:09 UTC | 1h 37m |
| 4Y13321 |  | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-05-26 09:47 UTC | 2026-05-26 10:08 UTC | 20m |
| JOKER12 | JOK | Oberpfaffenhofen Airport (EDMO) | Langkampfen Airport (LOIK) | 2026-05-26 09:57 UTC | 2026-05-26 10:04 UTC | 6m |
| ELY006 | ELY | Los Angeles International Airport (KLAX) | Queen Alia International Airport (OJAI) | 2026-05-25 20:59 UTC | 2026-05-26 10:02 UTC | 13h 2m |
| CCM940 | CCM | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | 2026-05-26 09:32 UTC | 2026-05-26 10:00 UTC | 27m |
| CATS00 | CAT | Osan Air Base (RKSO) | G 417 Airport (RK34) | 2026-05-26 09:36 UTC | 2026-05-26 09:59 UTC | 23m |
| PLF130 | PLF | Warsaw Chopin Airport (EPWA) | Vilnius International Airport (EYVI) | 2026-05-26 09:12 UTC | 2026-05-26 09:53 UTC | 41m |
| HBZSN | HBZ | Courchevel Airport (LFLJ) | Samedan Airport (LSZS) | 2026-05-26 09:01 UTC | 2026-05-26 09:50 UTC | 48m |
| MRS1306 | MRS | Kenitra Airport (GMMY) | Bassatine Airport (GMFM) | 2026-05-26 09:36 UTC | 2026-05-26 09:49 UTC | 12m |
| SWR462F | Swiss International | Warsaw Chopin Airport (EPWA) | Zurich Airport (LSZH) | 2026-05-26 08:10 UTC | 2026-05-26 09:47 UTC | 1h 37m |
|  |  | Phaplu Airport (VNPL) | Tribhuvan International Airport (VNKT) | 2026-05-26 09:18 UTC | 2026-05-26 09:36 UTC | 18m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Queen Alia International Airport (OJAI) | 2026-05-26 06:41 UTC | 2026-05-26 09:36 UTC | 2h 54m |
| RJA111 | Royal Jordanian | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-26 09:16 UTC | 2026-05-26 09:34 UTC | 18m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-05-26 08:55 UTC | 2026-05-26 09:30 UTC | 34m |
| NYT923 | NYT | Tribhuvan International Airport (VNKT) | Suketar Airport (VNTJ) | 2026-05-26 09:05 UTC | 2026-05-26 09:28 UTC | 22m |
| CHX22 | CHX | Illertissen Airport (EDMI) | Erbach Airport (EDNE) | 2026-05-26 09:19 UTC | 2026-05-26 09:27 UTC | 7m |
| AAR8735 | AAR | Gimpo International Airport (RKSS) | G 710 Airport (RK6D) | 2026-05-26 08:59 UTC | 2026-05-26 09:26 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
