# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_16:18:38_UTC-green)

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

**Latest saved flight:** 2026-06-23 16:18:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 16:18:38 UTC

- **117,879** saved flights
- **40,686** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,879** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,429,808.0 tonnes** estimated CO2 emissions
- **82,887,421 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4857 |
| 2 | SkyWest Airlines | 4361 |
| 3 | EJA | 2281 |
| 4 | IndiGo | 2279 |
| 5 | American Airlines | 1834 |
| 6 | Southwest Airlines | 1756 |
| 7 | ENY | 1473 |
| 8 | Delta Air Lines | 1389 |
| 9 | Lufthansa | 1299 |
| 10 | Vueling | 1064 |
| 11 | LATAM Airlines | 1044 |
| 12 | WIF | 1040 |
| 13 | AZU | 985 |
| 14 | AXM | 969 |
| 15 | LXJ | 898 |
| 16 | Swiss International | 834 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 781 |
| 19 | QLK | 759 |
| 20 | easyJet | 750 |
| 21 | EJU | 735 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 660 |
| 24 | VIV | 650 |
| 25 | Air France | 646 |
| 26 | United Airlines | 646 |
| 27 | CXK | 632 |
| 28 | MXY | 622 |
| 29 | AXB | 585 |
| 30 | GLO | 577 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99576 |
| 2 | 🇪🇸 ES | 8045 |
| 3 | 🇮🇳 IN | 7164 |
| 4 | 🇦🇺 AU | 6985 |
| 5 | 🇧🇷 BR | 6505 |
| 6 | 🇮🇹 IT | 6293 |
| 7 | 🇩🇪 DE | 6290 |
| 8 | 🇨🇦 CA | 6180 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5158 |
| 11 | 🇫🇷 FR | 4693 |
| 12 | 🇨🇴 CO | 3998 |
| 13 | 🇲🇽 MX | 3465 |
| 14 | 🇬🇷 GR | 3371 |
| 15 | 🇳🇴 NO | 3238 |
| 16 | 🇨🇭 CH | 3031 |
| 17 | 🇲🇾 MY | 2518 |
| 18 | 🇹🇷 TR | 2407 |
| 19 | 🇿🇦 ZA | 1989 |
| 20 | 🇵🇱 PL | 1935 |
| 21 | 🇳🇿 NZ | 1921 |
| 22 | 🇹🇭 TH | 1899 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1278 |
| 27 | 🇲🇴 MO | 1170 |
| 28 | 🇲🇪 ME | 1166 |
| 29 | 🇳🇱 NL | 1135 |
| 30 | 🇭🇷 HR | 1024 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2484 |
| 2 | Denver International Airport |  | US | 1980 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1571 |
| 5 | Guaymaral Airport |  | CO | 1488 |
| 6 | Harry Reid International Airport |  | US | 1471 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1437 |
| 8 | Zurich Airport |  | CH | 1321 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1261 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1251 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1170 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1167 |
| 15 | Chicago O'Hare International Airport |  | US | 1154 |
| 16 | Capua Airport |  | IT | 1018 |
| 17 | Salt Lake City International Airport |  | US | 1008 |
| 18 | Madrid Barajas International Airport |  | ES | 996 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 982 |
| 20 | Kuala Lumpur International Airport |  | MY | 974 |
| 21 | Congonhas Airport |  | BR | 908 |
| 22 | Charlotte/Douglas International Airport |  | US | 897 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 886 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 25 | Bengaluru International Airport |  | IN | 869 |
| 26 | Charles de Gaulle International Airport |  | FR | 865 |
| 27 | Malpensa International Airport |  | IT | 833 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 772 |
| 30 | Daniel K Inouye International Airport |  | US | 764 |
| 31 | Tenerife Norte Airport |  | ES | 759 |
| 32 | Barcelona International Airport |  | ES | 749 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 691 |
| 35 | Calgary International Airport |  | CA | 689 |
| 36 | Amsterdam Airport Schiphol |  | NL | 689 |
| 37 | Don Mueang International Airport |  | TH | 687 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 671 |
| 40 | Viracopos International Airport |  | BR | 670 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 618 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 427 | 21m | 244 km | 1,798.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 304 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 285 | 1h 10m | 770 km | 3,786.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 218 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 169 | 26m | 215 km | 625.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 159 | 44m | 241 km | 660.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 148 | 1h 44m | 1,423 km | 3,632.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N52CF |  | Kansas City Downtown/Wheeler Field (KMKC) | Miami County Airport (KK81) | 2026-06-23 16:01 UTC | 2026-06-23 16:18 UTC | 17m |
| CGELN | CGE | Stratford Municipal Airport (CYSA) | Chris Hadfield Airport (CYZR) | 2026-06-23 15:39 UTC | 2026-06-23 16:18 UTC | 39m |
| FAM3934 | FAM | Tizayuca Airport (MM28) | Ingeniero Juan Guillermo Villasana Airport (MMPC) | 2026-06-23 15:50 UTC | 2026-06-23 16:17 UTC | 27m |
| FLAT62 | FLA | Shenandoah Valley Farms Airport (0MS9) | Ball Airport (5MS8) | 2026-06-23 15:56 UTC | 2026-06-23 16:15 UTC | 18m |
| RNRG765 | RNR | Victoria Regional Airport (KVCT) | San Jose Island Airport (XS67) | 2026-06-23 15:47 UTC | 2026-06-23 16:11 UTC | 23m |
| NHZ25 | NHZ | Blackpool International Airport (EGNH) | Barrow Walney Island Airport (EGNL) | 2026-06-23 15:50 UTC | 2026-06-23 16:07 UTC | 17m |
| CSB805 | CSB | Cincinnati/Northern Kentucky International Airport (KCVG) | San Francisco International Airport (KSFO) | 2026-06-23 11:40 UTC | 2026-06-23 16:04 UTC | 4h 24m |
| EJA976 | EJA | Circle W Ranch Airport (77TX) | 5TA4 (5TA4) | 2026-06-23 14:49 UTC | 2026-06-23 16:04 UTC | 1h 15m |
| N4510E |  | MN99 (MN99) | Glencoe Municipal Airport (KGYL) | 2026-06-23 15:55 UTC | 2026-06-23 16:03 UTC | 7m |
| N915TT |  | Lake Elmo Airport (K21D) | Red Wing Regional Airport (KRGK) | 2026-06-23 15:47 UTC | 2026-06-23 16:03 UTC | 16m |
| CCG443 | CCG | Victoria International Airport (CYYJ) | Pitt Meadows Airport (CYPK) | 2026-06-23 15:31 UTC | 2026-06-23 16:03 UTC | 32m |
| N2777E |  | Corona Municipal Airport (KAJO) | Corona Municipal Airport (KAJO) | 2026-06-23 15:50 UTC | 2026-06-23 16:01 UTC | 11m |
| WIF9BY | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-06-23 15:45 UTC | 2026-06-23 16:01 UTC | 16m |
| DESERT7 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-23 15:44 UTC | 2026-06-23 16:01 UTC | 16m |
| N716X |  | Roberts Field (KRDM) | Wagontire Airport (81OR) | 2026-06-23 14:44 UTC | 2026-06-23 15:56 UTC | 1h 12m |
| UAL37 | United Airlines | Edinburgh Airport (EGPH) | Newark Liberty International Airport (KEWR) | 2026-06-23 08:38 UTC | 2026-06-23 15:56 UTC | 7h 17m |
| LXJ441 | LXJ | MT39 (MT39) | Vancouver International Airport (CYVR) | 2026-06-23 14:41 UTC | 2026-06-23 15:56 UTC | 1h 14m |
| DLH6YM | Lufthansa | Frankfurt am Main International Airport (EDDF) | Neustadt/Aisch Airport (EDQN) | 2026-06-23 15:26 UTC | 2026-06-23 15:55 UTC | 29m |
| DAGGR91 | DAG | Centennial Airport (KAPA) | Johnson County Airport (KBYG) | 2026-06-23 14:44 UTC | 2026-06-23 15:54 UTC | 1h 10m |
| N521NG |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-06-23 15:34 UTC | 2026-06-23 15:53 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
