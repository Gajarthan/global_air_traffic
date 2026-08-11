# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_00:22:50_UTC-green)

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

**Latest saved flight:** 2026-08-11 00:22:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 00:22:50 UTC

- **185,646** saved flights
- **58,983** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,646** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,228,335.3 tonnes** estimated CO2 emissions
- **129,178,858 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7354 |
| 2 | SkyWest Airlines | 6779 |
| 3 | EJA | 3674 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2919 |
| 6 | American Airlines | 2899 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2189 |
| 9 | LATAM Airlines | 1738 |
| 10 | AZU | 1671 |
| 11 | Lufthansa | 1628 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1458 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1236 |
| 18 | EJU | 1146 |
| 19 | QLK | 1138 |
| 20 | All Nippon Airways | 1126 |
| 21 | Alaska Airlines | 1110 |
| 22 | VIV | 1023 |
| 23 | GLO | 997 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | United Airlines | 948 |
| 28 | Cathay Pacific | 947 |
| 29 | PGT | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158836 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10673 |
| 4 | 🇦🇺 AU | 10336 |
| 5 | 🇨🇦 CA | 10147 |
| 6 | 🇮🇳 IN | 10141 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9154 |
| 9 | 🇬🇧 GB | 8605 |
| 10 | 🇯🇵 JP | 7526 |
| 11 | 🇫🇷 FR | 7405 |
| 12 | 🇨🇴 CO | 7016 |
| 13 | 🇬🇷 GR | 5438 |
| 14 | 🇲🇽 MX | 5303 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4869 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3227 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3090 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2633 |
| 23 | 🇵🇭 PH | 2445 |
| 24 | 🇬🇹 GT | 2373 |
| 25 | 🇰🇷 KR | 2296 |
| 26 | 🇲🇦 MA | 1878 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3862 |
| 2 | Denver International Airport |  | US | 3068 |
| 3 | Tokyo International Airport |  | JP | 2332 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2178 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1821 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1668 |
| 13 | Salt Lake City International Airport |  | US | 1659 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1597 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1453 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1387 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1328 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1291 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1265 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1162 |
| 30 | Ninoy Aquino International Airport |  | PH | 1153 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1139 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Viracopos International Airport |  | BR | 1070 |
| 34 | Seattle-Tacoma International Airport |  | US | 1068 |
| 35 | Reno/Tahoe International Airport |  | US | 1067 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1053 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 681 | 21m | 244 km | 2,867.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 445 | 1h 8m | 770 km | 5,911.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 225 | 50m | 556 km | 2,156.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 216 | 31m | 369 km | 1,374.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MRA633 | MRA | Mc Laughlin Farm Airport (66OK) | Mc Alester Regional Airport (KMLC) | 2026-08-11 00:01 UTC | 2026-08-11 00:22 UTC | 21m |
| AAL2828 | American Airlines | Miami International Airport (KMIA) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-10 21:48 UTC | 2026-08-11 00:13 UTC | 2h 25m |
| N350BV |  | Meadows Field (KBFL) | Van Nuys Airport (KVNY) | 2026-08-10 23:50 UTC | 2026-08-11 00:12 UTC | 21m |
| N611AC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-10 22:49 UTC | 2026-08-11 00:07 UTC | 1h 18m |
| N330CS |  | Pilot Country Airport (KX05) | Pilot Country Airport (KX05) | 2026-08-10 23:59 UTC | 2026-08-11 00:02 UTC | 3m |
| N744DA |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-08-10 23:08 UTC | 2026-08-11 00:02 UTC | 54m |
| N331JA |  | Sarasota/Bradenton International Airport (KSRQ) | 4AR6 (4AR6) | 2026-08-10 22:04 UTC | 2026-08-10 23:59 UTC | 1h 54m |
| N81052 |  | Merrill Field (PAMR) | Seldovia Airport (PASO) | 2026-08-10 22:48 UTC | 2026-08-10 23:58 UTC | 1h 10m |
| N4727D |  | Billy Joe Airport (37CA) | Hemet-Ryan Airport (KHMT) | 2026-08-10 23:40 UTC | 2026-08-10 23:58 UTC | 18m |
| TKR16 | TKR | Casper/Natrona County International Airport (KCPR) | Chamberlain Brothers Ranch Airport (WY66) | 2026-08-10 23:51 UTC | 2026-08-10 23:57 UTC | 6m |
| LTA660 | LTA | Scholes International At Galveston Airport (KGLS) | Pierce Field (72TA) | 2026-08-10 23:08 UTC | 2026-08-10 23:57 UTC | 49m |
| VOZ924 | Virgin Australia | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-10 22:44 UTC | 2026-08-10 23:54 UTC | 1h 10m |
| FD231 |  | Melbourne Essendon Airport (YMEN) | Mount Hotham Airport (YHOT) | 2026-08-10 22:34 UTC | 2026-08-10 23:51 UTC | 1h 16m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-08-10 23:03 UTC | 2026-08-10 23:48 UTC | 44m |
| CAP2652 | CAP | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-08-10 23:10 UTC | 2026-08-10 23:47 UTC | 37m |
| THY45M | Turkish Airlines | Istanbul Airport (LTFM) | Jendarata Airport (WMAJ) | 2026-08-10 14:18 UTC | 2026-08-10 23:47 UTC | 9h 28m |
| SCU43 | SCU | Double W Airport (3OK7) | Double W Airport (3OK7) | 2026-08-10 23:31 UTC | 2026-08-10 23:45 UTC | 14m |
| QTR90C | Qatar Airways | Jendarata Airport (WMAJ) | Jendarata Airport (WMAJ) | 2026-08-10 23:45 UTC | 2026-08-10 23:45 UTC | 0m |
| TKR101 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-10 23:41 UTC | 2026-08-10 23:44 UTC | 2m |
| N3395J |  | North Perry Airport (KHWO) | Miami International Airport (KMIA) | 2026-08-10 22:32 UTC | 2026-08-10 23:43 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
