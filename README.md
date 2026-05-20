# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_08:38:55_UTC-green)

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

**Latest saved flight:** 2026-05-20 08:38:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-20 08:38:55 UTC

- **88,860** saved flights
- **31,736** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,860** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,100,262.4 tonnes** estimated CO2 emissions
- **63,783,325 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3809 |
| 2 | SkyWest Airlines | 3294 |
| 3 | IndiGo | 1880 |
| 4 | EJA | 1681 |
| 5 | American Airlines | 1361 |
| 6 | Southwest Airlines | 1292 |
| 7 | Lufthansa | 1113 |
| 8 | ENY | 1096 |
| 9 | Delta Air Lines | 974 |
| 10 | Vueling | 848 |
| 11 | LATAM Airlines | 800 |
| 12 | AXM | 788 |
| 13 | WIF | 768 |
| 14 | AZU | 704 |
| 15 | Swiss International | 685 |
| 16 | All Nippon Airways | 670 |
| 17 | LXJ | 655 |
| 18 | QLK | 631 |
| 19 | Alaska Airlines | 628 |
| 20 | easyJet | 587 |
| 21 | Cathay Pacific | 573 |
| 22 | EJU | 572 |
| 23 | AEE | 549 |
| 24 | VIV | 532 |
| 25 | Air France | 519 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 466 |
| 28 | AXB | 458 |
| 29 | MXY | 454 |
| 30 | AIQ | 432 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73040 |
| 2 | 🇪🇸 ES | 6309 |
| 3 | 🇮🇳 IN | 5896 |
| 4 | 🇦🇺 AU | 5548 |
| 5 | 🇩🇪 DE | 4934 |
| 6 | 🇮🇹 IT | 4915 |
| 7 | 🇧🇷 BR | 4878 |
| 8 | 🇨🇦 CA | 4439 |
| 9 | 🇯🇵 JP | 4355 |
| 10 | 🇬🇧 GB | 3790 |
| 11 | 🇫🇷 FR | 3564 |
| 12 | 🇨🇴 CO | 3047 |
| 13 | 🇲🇽 MX | 2759 |
| 14 | 🇬🇷 GR | 2571 |
| 15 | 🇳🇴 NO | 2467 |
| 16 | 🇨🇭 CH | 2344 |
| 17 | 🇲🇾 MY | 1980 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1611 |
| 20 | 🇳🇿 NZ | 1535 |
| 21 | 🇹🇭 TH | 1522 |
| 22 | 🇵🇱 PL | 1472 |
| 23 | 🇰🇷 KR | 1382 |
| 24 | 🇵🇭 PH | 1361 |
| 25 | 🇬🇹 GT | 1334 |
| 26 | 🇲🇴 MO | 1028 |
| 27 | 🇲🇦 MA | 1025 |
| 28 | 🇲🇪 ME | 915 |
| 29 | 🇳🇱 NL | 901 |
| 30 | 🇭🇷 HR | 804 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1942 |
| 2 | Denver International Airport |  | US | 1491 |
| 3 | Tokyo International Airport |  | JP | 1452 |
| 4 | Indira Gandhi International Airport |  | IN | 1273 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1212 |
| 6 | Harry Reid International Airport |  | US | 1133 |
| 7 | Frankfurt am Main International Airport |  | DE | 1121 |
| 8 | Zurich Airport |  | CH | 1059 |
| 9 | Guaymaral Airport |  | CO | 1040 |
| 10 | Macau International Airport |  | MO | 1028 |
| 11 | La Aurora Airport |  | GT | 1014 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 984 |
| 13 | El Dorado International Airport |  | CO | 970 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 905 |
| 15 | Chicago O'Hare International Airport |  | US | 858 |
| 16 | Madrid Barajas International Airport |  | ES | 808 |
| 17 | Kuala Lumpur International Airport |  | MY | 785 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 764 |
| 19 | Capua Airport |  | IT | 752 |
| 20 | Salt Lake City International Airport |  | US | 741 |
| 21 | Malpensa International Airport |  | IT | 725 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 721 |
| 23 | Bengaluru International Airport |  | IN | 709 |
| 24 | Charles de Gaulle International Airport |  | FR | 692 |
| 25 | Charlotte/Douglas International Airport |  | US | 684 |
| 26 | Congonhas Airport |  | BR | 680 |
| 27 | Daniel K Inouye International Airport |  | US | 650 |
| 28 | Tenerife Norte Airport |  | ES | 650 |
| 29 | Ninoy Aquino International Airport |  | PH | 624 |
| 30 | Barcelona International Airport |  | ES | 600 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 586 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 561 |
| 37 | Don Mueang International Airport |  | TH | 554 |
| 38 | Amsterdam Airport Schiphol |  | NL | 552 |
| 39 | Calgary International Airport |  | CA | 528 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 426 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 331 | 21m | 244 km | 1,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 244 | 24m | 225 km | 946.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 231 | 14m | 114 km | 453.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 228 | 28m | 304 km | 1,195.2 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 227 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 129 | 27m | 215 km | 477.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 127 | 23m | 55 km | 120.7 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 115 | 13m | - | - |
| 24 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 107 | 1h 18m | 961 km | 1,773.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| T741 |  | Dubendorf Airport (LSMD) | Bern Belp Airport (LSZB) | 2026-05-20 07:59 UTC | 2026-05-20 08:38 UTC | 39m |
| LPE2404 | LPE | Cancun International Airport (MMUN) | Marambaia Airport (SDMR) | 2026-05-19 20:35 UTC | 2026-05-20 08:36 UTC | 12h 1m |
| SUI721 | SUI | Dubendorf Airport (LSMD) | Emmen Airport (LSME) | 2026-05-20 08:21 UTC | 2026-05-20 08:32 UTC | 11m |
| DHK366 | DHK | East Midlands Airport (EGNX) | John F Kennedy International Airport (KJFK) | 2026-05-20 01:26 UTC | 2026-05-20 08:29 UTC | 7h 2m |
| AAR370 | AAR | Gwangju Airport (RKJJ) | Incheon International Airport (RKSI) | 2026-05-20 07:45 UTC | 2026-05-20 08:22 UTC | 37m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-20 07:39 UTC | 2026-05-20 08:22 UTC | 42m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-05-20 06:11 UTC | 2026-05-20 08:22 UTC | 2h 10m |
| GFRGP | GFR | Coventry Airport (EGBE) | London City Airport (EGLC) | 2026-05-20 07:52 UTC | 2026-05-20 08:19 UTC | 26m |
| BSO1BA | BSO | Sabadell Airport (LELL) | Igualada/Odena Airport (LEIG) | 2026-05-20 07:55 UTC | 2026-05-20 08:09 UTC | 13m |
| EGLE835 | EGL | RAAF Gingin (YGIG) | RAAF Gingin (YGIG) | 2026-05-20 07:58 UTC | 2026-05-20 08:09 UTC | 10m |
| PGT2179 | PGT | Gaziemir Airport (LTBK) | Yalova Airport (LTBP) | 2026-05-20 07:34 UTC | 2026-05-20 08:08 UTC | 33m |
| 3AMTT |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-20 06:58 UTC | 2026-05-20 08:05 UTC | 1h 6m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-05-20 07:21 UTC | 2026-05-20 08:03 UTC | 42m |
| PGC62H | PGC | Linate Airport (LIML) | Sion Airport (LSGS) | 2026-05-20 07:25 UTC | 2026-05-20 07:54 UTC | 28m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-20 07:18 UTC | 2026-05-20 07:52 UTC | 34m |
| TVF403 | TVF | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-05-20 07:08 UTC | 2026-05-20 07:52 UTC | 43m |
| OKWAR24 | OKW | Kunovice Airport (LKKU) | Kunovice Airport (LKKU) | 2026-05-20 07:46 UTC | 2026-05-20 07:49 UTC | 2m |
| 6VHAD |  | Leopold Sedar Senghor International Airport (GOOY) | Banjul International Airport (GBYD) | 2026-05-20 07:16 UTC | 2026-05-20 07:48 UTC | 32m |
| RYR85AX | Ryanair | L'Aquila / Preturo Airport (LIAP) | Václav Havel Airport (LKPR) | 2026-05-20 06:12 UTC | 2026-05-20 07:46 UTC | 1h 33m |
| TRD23 | TRD | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-05-20 07:08 UTC | 2026-05-20 07:44 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
