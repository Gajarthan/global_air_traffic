# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_20:46:39_UTC-green)

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

**Latest saved flight:** 2026-05-23 20:46:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 20:46:39 UTC

- **93,123** saved flights
- **32,981** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,123** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,145,573.8 tonnes** estimated CO2 emissions
- **66,410,073 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3935 |
| 2 | SkyWest Airlines | 3454 |
| 3 | IndiGo | 1936 |
| 4 | EJA | 1765 |
| 5 | American Airlines | 1413 |
| 6 | Southwest Airlines | 1349 |
| 7 | ENY | 1152 |
| 8 | Lufthansa | 1130 |
| 9 | Delta Air Lines | 1020 |
| 10 | Vueling | 886 |
| 11 | LATAM Airlines | 828 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 742 |
| 15 | LXJ | 705 |
| 16 | Swiss International | 695 |
| 17 | All Nippon Airways | 689 |
| 18 | Alaska Airlines | 648 |
| 19 | QLK | 648 |
| 20 | easyJet | 608 |
| 21 | EJU | 597 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 565 |
| 24 | VIV | 553 |
| 25 | Air France | 546 |
| 26 | CXK | 496 |
| 27 | MXY | 490 |
| 28 | Japan Airlines | 487 |
| 29 | AXB | 472 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77033 |
| 2 | 🇪🇸 ES | 6539 |
| 3 | 🇮🇳 IN | 6102 |
| 4 | 🇦🇺 AU | 5731 |
| 5 | 🇩🇪 DE | 5113 |
| 6 | 🇧🇷 BR | 5096 |
| 7 | 🇮🇹 IT | 5061 |
| 8 | 🇨🇦 CA | 4715 |
| 9 | 🇯🇵 JP | 4476 |
| 10 | 🇬🇧 GB | 3969 |
| 11 | 🇫🇷 FR | 3754 |
| 12 | 🇨🇴 CO | 3235 |
| 13 | 🇲🇽 MX | 2868 |
| 14 | 🇬🇷 GR | 2673 |
| 15 | 🇳🇴 NO | 2585 |
| 16 | 🇨🇭 CH | 2432 |
| 17 | 🇲🇾 MY | 2066 |
| 18 | 🇹🇷 TR | 1711 |
| 19 | 🇿🇦 ZA | 1683 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1572 |
| 22 | 🇵🇱 PL | 1521 |
| 23 | 🇰🇷 KR | 1476 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1407 |
| 26 | 🇲🇦 MA | 1068 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 934 |
| 29 | 🇲🇪 ME | 930 |
| 30 | 🇭🇷 HR | 842 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2019 |
| 2 | Denver International Airport |  | US | 1567 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1329 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1240 |
| 6 | Harry Reid International Airport |  | US | 1201 |
| 7 | Frankfurt am Main International Airport |  | DE | 1140 |
| 8 | Guaymaral Airport |  | CO | 1128 |
| 9 | Zurich Airport |  | CH | 1086 |
| 10 | La Aurora Airport |  | GT | 1075 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1021 |
| 13 | El Dorado International Airport |  | CO | 1016 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 934 |
| 15 | Chicago O'Hare International Airport |  | US | 889 |
| 16 | Madrid Barajas International Airport |  | ES | 836 |
| 17 | Kuala Lumpur International Airport |  | MY | 816 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 787 |
| 19 | Salt Lake City International Airport |  | US | 780 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 744 |
| 22 | Malpensa International Airport |  | IT | 739 |
| 23 | Bengaluru International Airport |  | IN | 734 |
| 24 | Charles de Gaulle International Airport |  | FR | 727 |
| 25 | Charlotte/Douglas International Airport |  | US | 711 |
| 26 | Congonhas Airport |  | BR | 708 |
| 27 | Daniel K Inouye International Airport |  | US | 672 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 627 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 621 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 607 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 587 |
| 35 | Vitoria/Foronda Airport |  | ES | 583 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 574 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 551 |
| 40 | O. R. Tambo International Airport |  | ZA | 533 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 463 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 344 | 21m | 244 km | 1,448.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 248 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 114 | 1h 40m | 1,156 km | 2,274.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CEPTOR | CEP | Aarhus Airport (EKAH) | Aarhus Airport (EKAH) | 2026-05-23 20:31 UTC | 2026-05-23 20:46 UTC | 15m |
| TMN125 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-05-23 11:04 UTC | 2026-05-23 20:45 UTC | 9h 41m |
| MXD820 | MXD | Kuala Lumpur International Airport (WMKK) | Incheon International Airport (RKSI) | 2026-05-23 14:27 UTC | 2026-05-23 20:35 UTC | 6h 7m |
| GH71 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-23 20:18 UTC | 2026-05-23 20:32 UTC | 14m |
| N78AS |  | Mitchell Municipal Airport (KMHE) | Andersen Farms Airport (SD19) | 2026-05-23 18:24 UTC | 2026-05-23 20:30 UTC | 2h 6m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 19:23 UTC | 2026-05-23 20:29 UTC | 1h 5m |
| N320KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 19:32 UTC | 2026-05-23 20:29 UTC | 56m |
| N625PL |  | Yucca Valley Airport (KL22) | Crosswinds Airport (2CA3) | 2026-05-23 19:17 UTC | 2026-05-23 20:27 UTC | 1h 9m |
| N910MR |  | Gillespie Field (KSEE) | Hemet-Ryan Airport (KHMT) | 2026-05-23 19:49 UTC | 2026-05-23 20:25 UTC | 35m |
| CRUSH51 | CRU | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | Ajax Airport (OR46) | 2026-05-23 19:06 UTC | 2026-05-23 20:23 UTC | 1h 17m |
| LXJ616 | LXJ | Napa County Airport (KAPC) | Northern Colorado Regional Airport (KFNL) | 2026-05-23 18:21 UTC | 2026-05-23 20:20 UTC | 1h 59m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-23 20:03 UTC | 2026-05-23 20:19 UTC | 15m |
| N12772 |  | Trinity Center Airport (KO86) | Prospect State Airport (K64S) | 2026-05-23 18:58 UTC | 2026-05-23 20:16 UTC | 1h 17m |
| TAA708 | TAA | Plan De Guadalupe International Airport (MMIO) | Monclova International Airport (MMMV) | 2026-05-23 19:52 UTC | 2026-05-23 20:12 UTC | 19m |
| N247EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-23 17:29 UTC | 2026-05-23 20:12 UTC | 2h 43m |
| MAC394F | MAC | Madrid Barajas International Airport (LEMD) | Beni Mellal Airport (GMMD) | 2026-05-23 18:53 UTC | 2026-05-23 20:09 UTC | 1h 16m |
| N761SP |  | Faribault Municipal-Liz Wall Strohfus Field (KFBL) | Faribault Municipal-Liz Wall Strohfus Field (KFBL) | 2026-05-23 20:04 UTC | 2026-05-23 20:06 UTC | 1m |
| SCA54 | SCA | Scottsdale Airport (KSDL) | 42AZ (42AZ) | 2026-05-23 19:25 UTC | 2026-05-23 20:04 UTC | 38m |
| RYR5909 | Ryanair | Nimes-Arles-Camargue Airport (LFTW) | Fes Sefrou Airport (GMFU) | 2026-05-23 18:21 UTC | 2026-05-23 20:03 UTC | 1h 41m |
| N202EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-05-23 19:38 UTC | 2026-05-23 20:03 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
