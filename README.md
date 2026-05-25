# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_08:25:32_UTC-green)

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

**Latest saved flight:** 2026-05-25 08:25:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-25 08:25:32 UTC

- **94,413** saved flights
- **33,316** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,413** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,162,315.2 tonnes** estimated CO2 emissions
- **67,380,592 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3991 |
| 2 | SkyWest Airlines | 3508 |
| 3 | IndiGo | 1958 |
| 4 | EJA | 1782 |
| 5 | American Airlines | 1436 |
| 6 | Southwest Airlines | 1371 |
| 7 | ENY | 1170 |
| 8 | Lufthansa | 1136 |
| 9 | Delta Air Lines | 1034 |
| 10 | Vueling | 903 |
| 11 | LATAM Airlines | 848 |
| 12 | AXM | 836 |
| 13 | WIF | 823 |
| 14 | AZU | 752 |
| 15 | LXJ | 712 |
| 16 | Swiss International | 709 |
| 17 | All Nippon Airways | 698 |
| 18 | QLK | 657 |
| 19 | Alaska Airlines | 655 |
| 20 | easyJet | 622 |
| 21 | EJU | 607 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 569 |
| 24 | VIV | 559 |
| 25 | Air France | 557 |
| 26 | CXK | 502 |
| 27 | MXY | 500 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77975 |
| 2 | 🇪🇸 ES | 6631 |
| 3 | 🇮🇳 IN | 6179 |
| 4 | 🇦🇺 AU | 5774 |
| 5 | 🇩🇪 DE | 5196 |
| 6 | 🇧🇷 BR | 5176 |
| 7 | 🇮🇹 IT | 5129 |
| 8 | 🇨🇦 CA | 4785 |
| 9 | 🇯🇵 JP | 4526 |
| 10 | 🇬🇧 GB | 4038 |
| 11 | 🇫🇷 FR | 3820 |
| 12 | 🇨🇴 CO | 3266 |
| 13 | 🇲🇽 MX | 2899 |
| 14 | 🇬🇷 GR | 2714 |
| 15 | 🇳🇴 NO | 2629 |
| 16 | 🇨🇭 CH | 2483 |
| 17 | 🇲🇾 MY | 2113 |
| 18 | 🇹🇷 TR | 1748 |
| 19 | 🇿🇦 ZA | 1705 |
| 20 | 🇹🇭 TH | 1600 |
| 21 | 🇳🇿 NZ | 1596 |
| 22 | 🇵🇱 PL | 1552 |
| 23 | 🇰🇷 KR | 1528 |
| 24 | 🇵🇭 PH | 1424 |
| 25 | 🇬🇹 GT | 1415 |
| 26 | 🇲🇦 MA | 1081 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 952 |
| 29 | 🇲🇪 ME | 939 |
| 30 | 🇭🇷 HR | 860 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2046 |
| 2 | Denver International Airport |  | US | 1597 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1345 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1248 |
| 6 | Harry Reid International Airport |  | US | 1211 |
| 7 | Frankfurt am Main International Airport |  | DE | 1152 |
| 8 | Guaymaral Airport |  | CO | 1140 |
| 9 | Zurich Airport |  | CH | 1105 |
| 10 | La Aurora Airport |  | GT | 1082 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1027 |
| 13 | El Dorado International Airport |  | CO | 1026 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 943 |
| 15 | Chicago O'Hare International Airport |  | US | 908 |
| 16 | Madrid Barajas International Airport |  | ES | 842 |
| 17 | Kuala Lumpur International Airport |  | MY | 839 |
| 18 | Salt Lake City International Airport |  | US | 797 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 797 |
| 20 | Capua Airport |  | IT | 785 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 754 |
| 22 | Malpensa International Airport |  | IT | 745 |
| 23 | Bengaluru International Airport |  | IN | 741 |
| 24 | Charles de Gaulle International Airport |  | FR | 739 |
| 25 | Charlotte/Douglas International Airport |  | US | 718 |
| 26 | Congonhas Airport |  | BR | 717 |
| 27 | Daniel K Inouye International Airport |  | US | 676 |
| 28 | Tenerife Norte Airport |  | ES | 673 |
| 29 | Ninoy Aquino International Airport |  | PH | 650 |
| 30 | Barcelona International Airport |  | ES | 636 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 633 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 614 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 605 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Vitoria/Foronda Airport |  | ES | 587 |
| 36 | Amsterdam Airport Schiphol |  | NL | 587 |
| 37 | Don Mueang International Airport |  | TH | 586 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 561 |
| 40 | O. R. Tambo International Airport |  | ZA | 541 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 468 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 347 | 21m | 244 km | 1,461.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 254 | 24m | 225 km | 985.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 238 | 28m | 304 km | 1,247.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 140 | 27m | 215 km | 518.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 122 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 1m | 695 km | 1,450.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 121 | 18m | 144 km | 301.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 117 | 1h 40m | 1,156 km | 2,334.1 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 52m | 1,304 km | 2,542.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LSI191 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-24 21:10 UTC | 2026-05-25 08:25 UTC | 11h 14m |
| P3301 |  | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-05-25 08:16 UTC | 2026-05-25 08:21 UTC | 5m |
| FBVVA | FBV | Perpignan-Rivesaltes (Llabanere) Airport (LFMP) | Perpignan-Rivesaltes (Llabanere) Airport (LFMP) | 2026-05-25 07:59 UTC | 2026-05-25 08:15 UTC | 15m |
| AE976 |  | Moree Airport (YMOR) | Sydney Bankstown Airport (YSBK) | 2026-05-25 07:11 UTC | 2026-05-25 08:04 UTC | 53m |
| ZKIDU | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-05-25 07:21 UTC | 2026-05-25 08:03 UTC | 42m |
| VOZ1093 | Virgin Australia | Flinders Island Airport (YFLI) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-25 06:42 UTC | 2026-05-25 08:02 UTC | 1h 20m |
| QLK637D | QLK | Wagga Wagga City Airport (YSWG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-25 07:10 UTC | 2026-05-25 08:02 UTC | 51m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-05-25 06:37 UTC | 2026-05-25 07:49 UTC | 1h 11m |
| FHOKE | FHO | Lille/Marcq-en-Baroeul Airport (LFQO) | Lille/Marcq-en-Baroeul Airport (LFQO) | 2026-05-25 07:31 UTC | 2026-05-25 07:47 UTC | 16m |
| KAL024 | Korean Air | San Francisco International Airport (KSFO) | Incheon International Airport (RKSI) | 2026-05-24 20:11 UTC | 2026-05-25 07:46 UTC | 11h 35m |
| OYCJB | OYC | Chambery-Challes-les-Eaux Airport (LFLE) | Raron Airport (LSTA) | 2026-05-25 06:38 UTC | 2026-05-25 07:42 UTC | 1h 3m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-05-25 07:17 UTC | 2026-05-25 07:39 UTC | 21m |
| KAL926 | Korean Air | Amsterdam Airport Schiphol (EHAM) | Incheon International Airport (RKSI) | 2026-05-24 19:56 UTC | 2026-05-25 07:39 UTC | 11h 43m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-05-25 07:06 UTC | 2026-05-25 07:37 UTC | 30m |
| KAL2002 | Korean Air | Chek Lap Kok International Airport (VHHH) | Incheon International Airport (RKSI) | 2026-05-25 04:31 UTC | 2026-05-25 07:37 UTC | 3h 5m |
| VOE81UT | VOE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-05-25 07:01 UTC | 2026-05-25 07:36 UTC | 35m |
| WZZ88HV | Wizz Air | Tallinn Airport (EETN) | Słupsk-Krępa Airport (EPSR) | 2026-05-25 06:42 UTC | 2026-05-25 07:33 UTC | 50m |
| RYR59PZ | Ryanair | Dublin Airport (EIDW) | Manresa Airport (LEMS) | 2026-05-25 05:37 UTC | 2026-05-25 07:30 UTC | 1h 53m |
| SXS4EC | SXS | Stuttgart Airport (EDDS) | Kaklic Airport (LTFA) | 2026-05-25 05:08 UTC | 2026-05-25 07:29 UTC | 2h 21m |
| IGO6175 | IndiGo | Indira Gandhi International Airport (VIDP) | Thamkharka Airport (VNTH) | 2026-05-25 06:16 UTC | 2026-05-25 07:28 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
