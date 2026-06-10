# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_21:00:29_UTC-green)

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

**Latest saved flight:** 2026-06-10 21:00:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-10 21:00:29 UTC

- **107,734** saved flights
- **37,756** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,734** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,317,356.3 tonnes** estimated CO2 emissions
- **76,368,483 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4437 |
| 2 | SkyWest Airlines | 4046 |
| 3 | IndiGo | 2136 |
| 4 | EJA | 2080 |
| 5 | American Airlines | 1714 |
| 6 | Southwest Airlines | 1621 |
| 7 | ENY | 1347 |
| 8 | Delta Air Lines | 1279 |
| 9 | Lufthansa | 1230 |
| 10 | Vueling | 986 |
| 11 | LATAM Airlines | 957 |
| 12 | WIF | 945 |
| 13 | AXM | 914 |
| 14 | AZU | 877 |
| 15 | LXJ | 813 |
| 16 | Swiss International | 783 |
| 17 | All Nippon Airways | 747 |
| 18 | Alaska Airlines | 739 |
| 19 | QLK | 714 |
| 20 | easyJet | 696 |
| 21 | EJU | 686 |
| 22 | Cathay Pacific | 648 |
| 23 | AEE | 614 |
| 24 | VIV | 614 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 580 |
| 28 | CXK | 569 |
| 29 | AXB | 530 |
| 30 | Japan Airlines | 530 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90697 |
| 2 | 🇪🇸 ES | 7391 |
| 3 | 🇮🇳 IN | 6727 |
| 4 | 🇦🇺 AU | 6432 |
| 5 | 🇧🇷 BR | 5939 |
| 6 | 🇩🇪 DE | 5779 |
| 7 | 🇮🇹 IT | 5769 |
| 8 | 🇨🇦 CA | 5648 |
| 9 | 🇯🇵 JP | 4900 |
| 10 | 🇬🇧 GB | 4578 |
| 11 | 🇫🇷 FR | 4282 |
| 12 | 🇨🇴 CO | 3734 |
| 13 | 🇲🇽 MX | 3224 |
| 14 | 🇬🇷 GR | 3055 |
| 15 | 🇳🇴 NO | 2978 |
| 16 | 🇨🇭 CH | 2740 |
| 17 | 🇲🇾 MY | 2343 |
| 18 | 🇹🇷 TR | 2095 |
| 19 | 🇿🇦 ZA | 1845 |
| 20 | 🇰🇷 KR | 1786 |
| 21 | 🇳🇿 NZ | 1783 |
| 22 | 🇹🇭 TH | 1764 |
| 23 | 🇵🇱 PL | 1760 |
| 24 | 🇵🇭 PH | 1572 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1190 |
| 27 | 🇲🇴 MO | 1130 |
| 28 | 🇳🇱 NL | 1057 |
| 29 | 🇲🇪 ME | 1040 |
| 30 | 🇭🇷 HR | 940 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2327 |
| 2 | Denver International Airport |  | US | 1829 |
| 3 | Tokyo International Airport |  | JP | 1623 |
| 4 | Indira Gandhi International Airport |  | IN | 1460 |
| 5 | Harry Reid International Airport |  | US | 1374 |
| 6 | Guaymaral Airport |  | CO | 1373 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1349 |
| 8 | Zurich Airport |  | CH | 1221 |
| 9 | Frankfurt am Main International Airport |  | DE | 1213 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1161 |
| 12 | El Dorado International Airport |  | CO | 1132 |
| 13 | Macau International Airport |  | MO | 1130 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1081 |
| 15 | Chicago O'Hare International Airport |  | US | 1075 |
| 16 | Madrid Barajas International Airport |  | ES | 938 |
| 17 | Capua Airport |  | IT | 923 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 918 |
| 19 | Kuala Lumpur International Airport |  | MY | 918 |
| 20 | Salt Lake City International Airport |  | US | 915 |
| 21 | Charlotte/Douglas International Airport |  | US | 832 |
| 22 | Congonhas Airport |  | BR | 822 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 815 |
| 24 | Charles de Gaulle International Airport |  | FR | 813 |
| 25 | Bengaluru International Airport |  | IN | 813 |
| 26 | Malpensa International Airport |  | IT | 798 |
| 27 | Daniel K Inouye International Airport |  | US | 727 |
| 28 | Ninoy Aquino International Airport |  | PH | 721 |
| 29 | Tenerife Norte Airport |  | ES | 721 |
| 30 | Barcelona International Airport |  | ES | 704 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 700 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 698 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 698 |
| 34 | Amsterdam Airport Schiphol |  | NL | 653 |
| 35 | Don Mueang International Airport |  | TH | 646 |
| 36 | Vitoria/Foronda Airport |  | ES | 643 |
| 37 | Calgary International Airport |  | CA | 635 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 618 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 568 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 395 | 21m | 244 km | 1,663.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 285 | 24m | 225 km | 1,105.7 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 282 | 1h 7m | 706 km | 3,433.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 262 | 1h 25m | 910 km | 4,111.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 249 | 1h 10m | 770 km | 3,307.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 216 | 26m | 275 km | 1,023.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 207 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 158 | 22m | 55 km | 150.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 147 | 13m | - | - |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 129 | 44m | 241 km | 535.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 126 | 1h 43m | 1,423 km | 3,092.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 122 | 1h 18m | 961 km | 2,022.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BFF20 | BFF | Halifax Robert L. Stanfield International Airport (CYHZ) | Toronto Pearson International Airport (CYYZ) | 2026-06-10 18:59 UTC | 2026-06-10 21:00 UTC | 2h 1m |
| N85DP |  | Mc Clellan-Palomar Airport (KCRQ) | Santa Monica Municipal Airport (KSMO) | 2026-06-10 20:26 UTC | 2026-06-10 20:59 UTC | 33m |
| N536GS |  | Yuba County Airport (KMYV) | Palo Alto Airport (KPAO) | 2026-06-10 20:17 UTC | 2026-06-10 20:57 UTC | 40m |
| ERU64 | ERU | Parsons Field (4AZ6) | Lake Havasu City Airport (KHII) | 2026-06-10 20:21 UTC | 2026-06-10 20:57 UTC | 36m |
| SPADE10 | SPA | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-06-10 20:38 UTC | 2026-06-10 20:54 UTC | 16m |
| EJM280 | EJM | Harry Reid International Airport (KLAS) | Mesawood Airport (6CO2) | 2026-06-10 20:02 UTC | 2026-06-10 20:54 UTC | 52m |
| N701EX |  | Regeneration Airport (5AZ9) | Ethnos Air Airport (2AZ9) | 2026-06-10 20:11 UTC | 2026-06-10 20:52 UTC | 41m |
| N492PJ |  | Indiana County/Jimmy Stewart Field (KIDI) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-06-10 16:42 UTC | 2026-06-10 20:50 UTC | 4h 8m |
| N222CY |  | Charles M Schulz/Sonoma County Airport (KSTS) | Mahlon Sweet Field (KEUG) | 2026-06-10 18:36 UTC | 2026-06-10 20:48 UTC | 2h 12m |
| KBAR08 | KBA | Hattiesburg Bobby L Chain Municipal Airport (KHBG) | Macdill Afb Airport (KMCF) | 2026-06-10 18:49 UTC | 2026-06-10 20:46 UTC | 1h 57m |
| ROUGH81 | ROU | Randolph Afb Airport (KRND) | Randolph Afb Airport (KRND) | 2026-06-10 20:42 UTC | 2026-06-10 20:43 UTC | 1m |
| BOX714 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-06-10 04:16 UTC | 2026-06-10 20:40 UTC | 16h 23m |
| N655DS |  | Castroville Municipal Airport (KCVB) | T-Ranch Airport (XS86) | 2026-06-10 20:27 UTC | 2026-06-10 20:36 UTC | 9m |
| N38HD |  | Bedford County Airport (KHMZ) | Capital City Airport (KCXY) | 2026-06-10 20:16 UTC | 2026-06-10 20:36 UTC | 20m |
| N38BL |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-06-10 20:17 UTC | 2026-06-10 20:35 UTC | 17m |
| GMN94 | GMN | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-06-10 19:36 UTC | 2026-06-10 20:34 UTC | 58m |
| N772CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-06-10 19:54 UTC | 2026-06-10 20:33 UTC | 39m |
| DHJLC | DHJ | Lauterbach Airport (EDFT) | Marburg-Schonstadt Airport (EDFN) | 2026-06-10 20:19 UTC | 2026-06-10 20:31 UTC | 11m |
| QTR340 | Qatar Airways | Sheremetyevo International Airport (UUEE) | Doha International Airport (OTBD) | 2026-06-10 14:32 UTC | 2026-06-10 20:31 UTC | 5h 58m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-06-10 20:22 UTC | 2026-06-10 20:30 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
