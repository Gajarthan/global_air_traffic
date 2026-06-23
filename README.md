# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_20:23:47_UTC-green)

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

**Latest saved flight:** 2026-06-23 20:23:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 20:23:47 UTC

- **118,290** saved flights
- **40,821** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,290** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,434,112.1 tonnes** estimated CO2 emissions
- **83,136,936 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4871 |
| 2 | SkyWest Airlines | 4374 |
| 3 | EJA | 2291 |
| 4 | IndiGo | 2279 |
| 5 | American Airlines | 1843 |
| 6 | Southwest Airlines | 1768 |
| 7 | ENY | 1482 |
| 8 | Delta Air Lines | 1396 |
| 9 | Lufthansa | 1300 |
| 10 | Vueling | 1071 |
| 11 | LATAM Airlines | 1047 |
| 12 | WIF | 1045 |
| 13 | AZU | 987 |
| 14 | AXM | 969 |
| 15 | LXJ | 900 |
| 16 | Swiss International | 834 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 784 |
| 19 | QLK | 759 |
| 20 | easyJet | 758 |
| 21 | EJU | 740 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 660 |
| 24 | VIV | 651 |
| 25 | Air France | 648 |
| 26 | United Airlines | 648 |
| 27 | CXK | 636 |
| 28 | MXY | 623 |
| 29 | AXB | 585 |
| 30 | GLO | 578 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 100062 |
| 2 | 🇪🇸 ES | 8069 |
| 3 | 🇮🇳 IN | 7165 |
| 4 | 🇦🇺 AU | 6985 |
| 5 | 🇧🇷 BR | 6523 |
| 6 | 🇮🇹 IT | 6313 |
| 7 | 🇩🇪 DE | 6301 |
| 8 | 🇨🇦 CA | 6224 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5180 |
| 11 | 🇫🇷 FR | 4704 |
| 12 | 🇨🇴 CO | 4000 |
| 13 | 🇲🇽 MX | 3470 |
| 14 | 🇬🇷 GR | 3375 |
| 15 | 🇳🇴 NO | 3248 |
| 16 | 🇨🇭 CH | 3033 |
| 17 | 🇲🇾 MY | 2519 |
| 18 | 🇹🇷 TR | 2425 |
| 19 | 🇿🇦 ZA | 1991 |
| 20 | 🇵🇱 PL | 1946 |
| 21 | 🇳🇿 NZ | 1921 |
| 22 | 🇹🇭 TH | 1900 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1280 |
| 27 | 🇲🇪 ME | 1170 |
| 28 | 🇲🇴 MO | 1170 |
| 29 | 🇳🇱 NL | 1136 |
| 30 | 🇭🇷 HR | 1026 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2494 |
| 2 | Denver International Airport |  | US | 1983 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1571 |
| 5 | Guaymaral Airport |  | CO | 1490 |
| 6 | Harry Reid International Airport |  | US | 1472 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1439 |
| 8 | Zurich Airport |  | CH | 1321 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1262 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1256 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1173 |
| 13 | El Dorado International Airport |  | CO | 1171 |
| 14 | Macau International Airport |  | MO | 1170 |
| 15 | Chicago O'Hare International Airport |  | US | 1159 |
| 16 | Capua Airport |  | IT | 1021 |
| 17 | Salt Lake City International Airport |  | US | 1011 |
| 18 | Madrid Barajas International Airport |  | ES | 997 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 992 |
| 20 | Kuala Lumpur International Airport |  | MY | 974 |
| 21 | Congonhas Airport |  | BR | 908 |
| 22 | Charlotte/Douglas International Airport |  | US | 898 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 891 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 25 | Bengaluru International Airport |  | IN | 870 |
| 26 | Charles de Gaulle International Airport |  | FR | 867 |
| 27 | Malpensa International Airport |  | IT | 833 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 775 |
| 30 | Daniel K Inouye International Airport |  | US | 767 |
| 31 | Tenerife Norte Airport |  | ES | 760 |
| 32 | Barcelona International Airport |  | ES | 751 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Calgary International Airport |  | CA | 694 |
| 35 | Vitoria/Foronda Airport |  | ES | 694 |
| 36 | Amsterdam Airport Schiphol |  | NL | 690 |
| 37 | Don Mueang International Airport |  | TH | 687 |
| 38 | Seattle-Tacoma International Airport |  | US | 675 |
| 39 | Scottsdale Airport |  | US | 672 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 671 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 619 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 429 | 21m | 244 km | 1,806.4 t |
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
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 170 | 26m | 215 km | 629.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 160 | 44m | 241 km | 664.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 148 | 1h 44m | 1,423 km | 3,632.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 148 | 18m | 144 km | 368.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXS4RX | SXS | Antalya International Airport (LTAI) | Cologne Bonn Airport (EDDK) | 2026-06-23 16:55 UTC | 2026-06-23 20:23 UTC | 3h 28m |
| N9469H |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-06-23 20:02 UTC | 2026-06-23 20:19 UTC | 17m |
| N976TR |  | Bradley International Airport (KBDL) | Laguardia Airport (KLGA) | 2026-06-23 19:33 UTC | 2026-06-23 20:14 UTC | 40m |
| N238F |  | Zamperini Field (KTOA) | San Bernardino International Airport (KSBD) | 2026-06-23 19:29 UTC | 2026-06-23 20:11 UTC | 42m |
| N12441 |  | Dupage Airport (KDPA) | 26LL (26LL) | 2026-06-23 19:49 UTC | 2026-06-23 20:11 UTC | 22m |
| N732ZY |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-06-23 19:22 UTC | 2026-06-23 20:11 UTC | 48m |
| G20304 |  | Alley Oop Airport (68IN) | Lansing Municipal Airport (KIGQ) | 2026-06-23 19:47 UTC | 2026-06-23 20:09 UTC | 22m |
| N725XL |  | K36U (K36U) | Rocky Mountain Metro Airport (KBJC) | 2026-06-23 19:16 UTC | 2026-06-23 20:08 UTC | 52m |
| EJA948 | EJA | Nashville International Airport (KBNA) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-23 19:25 UTC | 2026-06-23 20:06 UTC | 41m |
|  |  | Dyersburg Regional Airport (KDYR) | Dyersburg Regional Airport (KDYR) | 2026-06-23 19:49 UTC | 2026-06-23 20:04 UTC | 15m |
| EJA559 | EJA | Bangor International Airport (KBGR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-23 19:19 UTC | 2026-06-23 20:03 UTC | 44m |
| N81034 |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-06-23 19:11 UTC | 2026-06-23 20:00 UTC | 48m |
| ABK355 | ABK | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-06-23 18:08 UTC | 2026-06-23 19:56 UTC | 1h 48m |
| EJM377 | EJM | Scottsdale Airport (KSDL) | Twin Lakes Airport (MI55) | 2026-06-23 16:49 UTC | 2026-06-23 19:55 UTC | 3h 5m |
| N66BP |  | Jaars-Townsend Airport (KN52) | Jaars-Townsend Airport (KN52) | 2026-06-23 19:47 UTC | 2026-06-23 19:51 UTC | 4m |
| WNG64B | WNG | Cape Girardeau Regional Airport (KCGI) | Cairo Regional Airport (KCIR) | 2026-06-23 19:28 UTC | 2026-06-23 19:50 UTC | 21m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-23 19:09 UTC | 2026-06-23 19:50 UTC | 40m |
| THY8CD | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-06-23 16:43 UTC | 2026-06-23 19:49 UTC | 3h 6m |
| TKR10 | TKR | Lincoln County Airport (K1L1) | Seligman Airport (KP23) | 2026-06-23 19:22 UTC | 2026-06-23 19:48 UTC | 26m |
| N362SP |  | Clermont County Airport (KI69) | Clermont County Airport (KI69) | 2026-06-23 19:32 UTC | 2026-06-23 19:47 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
