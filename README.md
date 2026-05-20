# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_11:21:25_UTC-green)

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

**Latest saved flight:** 2026-05-20 11:21:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-20 11:21:25 UTC

- **88,951** saved flights
- **31,765** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,951** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,102,261.0 tonnes** estimated CO2 emissions
- **63,899,188 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3817 |
| 2 | SkyWest Airlines | 3294 |
| 3 | IndiGo | 1882 |
| 4 | EJA | 1681 |
| 5 | American Airlines | 1361 |
| 6 | Southwest Airlines | 1292 |
| 7 | Lufthansa | 1114 |
| 8 | ENY | 1096 |
| 9 | Delta Air Lines | 974 |
| 10 | Vueling | 850 |
| 11 | LATAM Airlines | 801 |
| 12 | AXM | 790 |
| 13 | WIF | 770 |
| 14 | AZU | 704 |
| 15 | Swiss International | 687 |
| 16 | All Nippon Airways | 671 |
| 17 | LXJ | 655 |
| 18 | QLK | 632 |
| 19 | Alaska Airlines | 628 |
| 20 | easyJet | 587 |
| 21 | Cathay Pacific | 574 |
| 22 | EJU | 572 |
| 23 | AEE | 549 |
| 24 | VIV | 532 |
| 25 | Air France | 522 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 467 |
| 28 | AXB | 458 |
| 29 | MXY | 454 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73052 |
| 2 | 🇪🇸 ES | 6319 |
| 3 | 🇮🇳 IN | 5903 |
| 4 | 🇦🇺 AU | 5553 |
| 5 | 🇩🇪 DE | 4941 |
| 6 | 🇮🇹 IT | 4923 |
| 7 | 🇧🇷 BR | 4882 |
| 8 | 🇨🇦 CA | 4443 |
| 9 | 🇯🇵 JP | 4367 |
| 10 | 🇬🇧 GB | 3795 |
| 11 | 🇫🇷 FR | 3580 |
| 12 | 🇨🇴 CO | 3047 |
| 13 | 🇲🇽 MX | 2759 |
| 14 | 🇬🇷 GR | 2571 |
| 15 | 🇳🇴 NO | 2473 |
| 16 | 🇨🇭 CH | 2352 |
| 17 | 🇲🇾 MY | 1984 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1619 |
| 20 | 🇳🇿 NZ | 1536 |
| 21 | 🇹🇭 TH | 1523 |
| 22 | 🇵🇱 PL | 1475 |
| 23 | 🇰🇷 KR | 1384 |
| 24 | 🇵🇭 PH | 1368 |
| 25 | 🇬🇹 GT | 1334 |
| 26 | 🇲🇴 MO | 1031 |
| 27 | 🇲🇦 MA | 1027 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 901 |
| 30 | 🇭🇷 HR | 805 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1942 |
| 2 | Denver International Airport |  | US | 1491 |
| 3 | Tokyo International Airport |  | JP | 1456 |
| 4 | Indira Gandhi International Airport |  | IN | 1275 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1212 |
| 6 | Harry Reid International Airport |  | US | 1134 |
| 7 | Frankfurt am Main International Airport |  | DE | 1122 |
| 8 | Zurich Airport |  | CH | 1063 |
| 9 | Guaymaral Airport |  | CO | 1040 |
| 10 | Macau International Airport |  | MO | 1031 |
| 11 | La Aurora Airport |  | GT | 1014 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 984 |
| 13 | El Dorado International Airport |  | CO | 970 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 905 |
| 15 | Chicago O'Hare International Airport |  | US | 858 |
| 16 | Madrid Barajas International Airport |  | ES | 810 |
| 17 | Kuala Lumpur International Airport |  | MY | 786 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 764 |
| 19 | Capua Airport |  | IT | 753 |
| 20 | Salt Lake City International Airport |  | US | 741 |
| 21 | Malpensa International Airport |  | IT | 725 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 723 |
| 23 | Bengaluru International Airport |  | IN | 709 |
| 24 | Charles de Gaulle International Airport |  | FR | 695 |
| 25 | Charlotte/Douglas International Airport |  | US | 684 |
| 26 | Congonhas Airport |  | BR | 681 |
| 27 | Tenerife Norte Airport |  | ES | 651 |
| 28 | Daniel K Inouye International Airport |  | US | 650 |
| 29 | Ninoy Aquino International Airport |  | PH | 628 |
| 30 | Barcelona International Airport |  | ES | 601 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 586 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 561 |
| 37 | Don Mueang International Airport |  | TH | 555 |
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
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 204 | 1h 10m | 770 km | 2,710.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 130 | 27m | 215 km | 481.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 127 | 23m | 55 km | 120.7 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 126 | 14m | 154 km | 333.8 t |
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
| LCO3613 | LCO | Melsbroek Air Base (EBMB) | Madrid Barajas International Airport (LEMD) | 2026-05-20 09:12 UTC | 2026-05-20 11:21 UTC | 2h 8m |
| ENF01 | ENF | Jomo Kenyatta International Airport (HKJK) | Nairobi Wilson Airport (HKNW) | 2026-05-20 11:06 UTC | 2026-05-20 11:18 UTC | 12m |
| WIF23C | WIF | Bodø Airport (ENBO) | Brønnøysund Airport (ENBN) | 2026-05-20 10:41 UTC | 2026-05-20 11:17 UTC | 35m |
| FHGTM | FHG | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-05-20 10:51 UTC | 2026-05-20 11:15 UTC | 24m |
| YOF | YOF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-20 10:18 UTC | 2026-05-20 11:05 UTC | 46m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-05-20 10:42 UTC | 2026-05-20 10:55 UTC | 12m |
| N63FS |  | Clark Regional Airport (KJVY) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-05-20 10:00 UTC | 2026-05-20 10:52 UTC | 52m |
| CXK198 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-05-20 09:42 UTC | 2026-05-20 10:52 UTC | 1h 9m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-20 07:56 UTC | 2026-05-20 10:43 UTC | 2h 46m |
| VLG9FT | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-05-20 09:48 UTC | 2026-05-20 10:42 UTC | 54m |
| IFJ42A | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-05-20 10:29 UTC | 2026-05-20 10:41 UTC | 11m |
| N243EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-20 08:16 UTC | 2026-05-20 10:39 UTC | 2h 22m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-19 20:17 UTC | 2026-05-20 10:36 UTC | 14h 19m |
| GTI8608 | GTI | Halifax Robert L. Stanfield International Airport (CYHZ) | Ted Stevens Anchorage International Airport (PANC) | 2026-05-20 03:24 UTC | 2026-05-20 10:35 UTC | 7h 10m |
| RYR7QU | Ryanair | Catania / Fontanarossa Airport (LICC) | Stanke Dimitrov Highway Strip (LB37) | 2026-05-20 09:31 UTC | 2026-05-20 10:35 UTC | 1h 3m |
| ANE21KC | ANE | Melilla Airport (GEML) | Jayena Airport (LE84) | 2026-05-20 10:03 UTC | 2026-05-20 10:33 UTC | 30m |
| RYR31CG | Ryanair | Paris Beauvais Tille Airport (LFOB) | Tirana International Airport Mother Teresa (LATI) | 2026-05-20 08:32 UTC | 2026-05-20 10:31 UTC | 1h 58m |
| APG715 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-05-20 10:00 UTC | 2026-05-20 10:29 UTC | 28m |
| N470LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-20 08:11 UTC | 2026-05-20 10:27 UTC | 2h 16m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-20 09:21 UTC | 2026-05-20 10:26 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
