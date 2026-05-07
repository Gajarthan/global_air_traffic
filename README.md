# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_22:02:50_UTC-green)

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

**Latest saved flight:** 2026-05-07 22:02:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 22:02:50 UTC

- **72,664** saved flights
- **26,987** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,664** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **895,474.0 tonnes** estimated CO2 emissions
- **51,911,538 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3124 |
| 2 | SkyWest Airlines | 2713 |
| 3 | IndiGo | 1638 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 929 |
| 8 | ENY | 915 |
| 9 | Vueling | 707 |
| 10 | AXM | 688 |
| 11 | LATAM Airlines | 677 |
| 12 | WIF | 623 |
| 13 | Delta Air Lines | 610 |
| 14 | All Nippon Airways | 599 |
| 15 | AZU | 583 |
| 16 | QLK | 555 |
| 17 | Swiss International | 555 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 510 |
| 20 | easyJet | 480 |
| 21 | EJU | 468 |
| 22 | AEE | 467 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 426 |
| 26 | Air France | 423 |
| 27 | AXB | 401 |
| 28 | CXK | 368 |
| 29 | AIQ | 360 |
| 30 | United Airlines | 350 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58350 |
| 2 | 🇪🇸 ES | 5246 |
| 3 | 🇮🇳 IN | 5146 |
| 4 | 🇦🇺 AU | 4803 |
| 5 | 🇧🇷 BR | 4070 |
| 6 | 🇩🇪 DE | 4027 |
| 7 | 🇮🇹 IT | 3973 |
| 8 | 🇯🇵 JP | 3829 |
| 9 | 🇨🇦 CA | 3633 |
| 10 | 🇬🇧 GB | 3120 |
| 11 | 🇫🇷 FR | 2854 |
| 12 | 🇨🇴 CO | 2679 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2151 |
| 15 | 🇳🇴 NO | 2018 |
| 16 | 🇨🇭 CH | 1967 |
| 17 | 🇲🇾 MY | 1715 |
| 18 | 🇿🇦 ZA | 1426 |
| 19 | 🇳🇿 NZ | 1322 |
| 20 | 🇹🇷 TR | 1303 |
| 21 | 🇹🇭 TH | 1296 |
| 22 | 🇵🇱 PL | 1209 |
| 23 | 🇵🇭 PH | 1176 |
| 24 | 🇬🇹 GT | 1147 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 863 |
| 27 | 🇲🇴 MO | 850 |
| 28 | 🇲🇪 ME | 772 |
| 29 | 🇳🇱 NL | 753 |
| 30 | 🇧🇸 BS | 611 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1287 |
| 3 | Denver International Airport |  | US | 1217 |
| 4 | Indira Gandhi International Airport |  | IN | 1087 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1052 |
| 6 | Frankfurt am Main International Airport |  | DE | 923 |
| 7 | Harry Reid International Airport |  | US | 908 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 874 |
| 10 | Zurich Airport |  | CH | 857 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 850 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 732 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 689 |
| 16 | Madrid Barajas International Airport |  | ES | 681 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 632 |
| 19 | Bengaluru International Airport |  | IN | 627 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 21 | Salt Lake City International Airport |  | US | 594 |
| 22 | Congonhas Airport |  | BR | 575 |
| 23 | Charlotte/Douglas International Airport |  | US | 573 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 566 |
| 26 | Tenerife Norte Airport |  | ES | 550 |
| 27 | Ninoy Aquino International Airport |  | PH | 535 |
| 28 | Daniel K Inouye International Airport |  | US | 533 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 521 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 500 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 494 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 486 |
| 34 | Vitoria/Foronda Airport |  | ES | 476 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 458 |
| 36 | Don Mueang International Airport |  | TH | 455 |
| 37 | Amsterdam Airport Schiphol |  | NL | 448 |
| 38 | O. R. Tambo International Airport |  | ZA | 447 |
| 39 | Calgary International Airport |  | CA | 435 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 426 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 363 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 256 | 21m | 244 km | 1,077.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 211 | 24m | 225 km | 818.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 161 | 26m | 275 km | 762.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 105 | 14m | 154 km | 278.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 93 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFS58 | FFS | Hidden Lake Airport (FA40) | Hidden Lake Airport (FA40) | 2026-05-07 21:45 UTC | 2026-05-07 22:02 UTC | 17m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-05-07 10:46 UTC | 2026-05-07 21:59 UTC | 11h 12m |
| N770MW |  | Kansas City Downtown/Wheeler Field (KMKC) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-07 20:53 UTC | 2026-05-07 21:58 UTC | 1h 4m |
| CKS273 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-05-07 12:18 UTC | 2026-05-07 21:54 UTC | 9h 35m |
| N938PM |  | Mount Horeb Field (06VA) | Wings Field (KLOM) | 2026-05-07 20:38 UTC | 2026-05-07 21:53 UTC | 1h 14m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-07 10:39 UTC | 2026-05-07 21:50 UTC | 11h 11m |
| THA910 | Thai Airways | Suvarnabhumi Airport (VTBS) | Jammu Airport (VIJU) | 2026-05-07 17:55 UTC | 2026-05-07 21:50 UTC | 3h 54m |
| N5336G |  | K00V (K00V) | Lone Tree Ranch Airport (35CO) | 2026-05-07 21:19 UTC | 2026-05-07 21:49 UTC | 29m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Macau International Airport (VMMC) | 2026-05-07 11:22 UTC | 2026-05-07 21:45 UTC | 10h 22m |
| N163MD |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 0PA6 (0PA6) | 2026-05-07 21:00 UTC | 2026-05-07 21:45 UTC | 44m |
| EJA626 | EJA | 0ND7 (0ND7) | Miami Executive Airport (KTMB) | 2026-05-07 18:15 UTC | 2026-05-07 21:44 UTC | 3h 28m |
| N5506U |  | Twelve Oaks Airport (5FL7) | Orlando Executive Airport (KORL) | 2026-05-07 20:52 UTC | 2026-05-07 21:44 UTC | 51m |
| URSA15 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-07 20:47 UTC | 2026-05-07 21:43 UTC | 56m |
| SCX3073 | SCX | Cincinnati/Northern Kentucky International Airport (KCVG) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-07 20:09 UTC | 2026-05-07 21:43 UTC | 1h 33m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-07 10:58 UTC | 2026-05-07 21:42 UTC | 10h 44m |
| DAL2895 | Delta Air Lines | Newark Liberty International Airport (KEWR) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-07 19:02 UTC | 2026-05-07 21:42 UTC | 2h 40m |
| CGHAP | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-05-07 21:23 UTC | 2026-05-07 21:41 UTC | 17m |
| N158NS |  | Washington Dulles International Airport (KIAD) | Witham Field (KSUA) | 2026-05-07 19:30 UTC | 2026-05-07 21:36 UTC | 2h 6m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-07 17:32 UTC | 2026-05-07 21:35 UTC | 4h 3m |
| N1481S |  | Phoenix Deer Valley Airport (KDVT) | Scottsdale Airport (KSDL) | 2026-05-07 21:25 UTC | 2026-05-07 21:35 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
