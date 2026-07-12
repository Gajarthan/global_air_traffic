# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_21:13:14_UTC-green)

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

**Latest saved flight:** 2026-07-12 21:13:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 21:13:14 UTC

- **139,418** saved flights
- **46,981** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,418** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,674,603.1 tonnes** estimated CO2 emissions
- **97,078,440 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5686 |
| 2 | SkyWest Airlines | 5110 |
| 3 | EJA | 2747 |
| 4 | IndiGo | 2559 |
| 5 | American Airlines | 2201 |
| 6 | Southwest Airlines | 2098 |
| 7 | ENY | 1743 |
| 8 | Delta Air Lines | 1654 |
| 9 | Lufthansa | 1422 |
| 10 | LATAM Airlines | 1282 |
| 11 | Vueling | 1206 |
| 12 | WIF | 1200 |
| 13 | AZU | 1199 |
| 14 | LXJ | 1071 |
| 15 | AXM | 1041 |
| 16 | Swiss International | 993 |
| 17 | easyJet | 907 |
| 18 | All Nippon Airways | 893 |
| 19 | Alaska Airlines | 876 |
| 20 | QLK | 865 |
| 21 | EJU | 861 |
| 22 | VIV | 767 |
| 23 | AEE | 749 |
| 24 | Air France | 748 |
| 25 | CXK | 747 |
| 26 | JetBlue | 732 |
| 27 | United Airlines | 731 |
| 28 | Cathay Pacific | 728 |
| 29 | MXY | 724 |
| 30 | GLO | 713 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 119819 |
| 2 | 🇪🇸 ES | 9164 |
| 3 | 🇮🇳 IN | 8018 |
| 4 | 🇦🇺 AU | 7926 |
| 5 | 🇧🇷 BR | 7872 |
| 6 | 🇨🇦 CA | 7316 |
| 7 | 🇮🇹 IT | 7292 |
| 8 | 🇩🇪 DE | 7278 |
| 9 | 🇬🇧 GB | 6334 |
| 10 | 🇯🇵 JP | 5845 |
| 11 | 🇫🇷 FR | 5559 |
| 12 | 🇨🇴 CO | 4414 |
| 13 | 🇲🇽 MX | 4046 |
| 14 | 🇬🇷 GR | 3977 |
| 15 | 🇳🇴 NO | 3754 |
| 16 | 🇨🇭 CH | 3620 |
| 17 | 🇹🇷 TR | 3266 |
| 18 | 🇲🇾 MY | 2702 |
| 19 | 🇵🇱 PL | 2335 |
| 20 | 🇿🇦 ZA | 2284 |
| 21 | 🇳🇿 NZ | 2134 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2005 |
| 24 | 🇵🇭 PH | 1891 |
| 25 | 🇬🇹 GT | 1848 |
| 26 | 🇲🇦 MA | 1465 |
| 27 | 🇲🇪 ME | 1386 |
| 28 | 🇳🇱 NL | 1309 |
| 29 | 🇭🇷 HR | 1262 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2885 |
| 2 | Denver International Airport |  | US | 2333 |
| 3 | Tokyo International Airport |  | JP | 1900 |
| 4 | Indira Gandhi International Airport |  | IN | 1772 |
| 5 | Harry Reid International Airport |  | US | 1739 |
| 6 | Guaymaral Airport |  | CO | 1701 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1609 |
| 8 | Zurich Airport |  | CH | 1553 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1464 |
| 10 | La Aurora Airport |  | GT | 1428 |
| 11 | Frankfurt am Main International Airport |  | DE | 1372 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1335 |
| 13 | Chicago O'Hare International Airport |  | US | 1312 |
| 14 | Salt Lake City International Airport |  | US | 1241 |
| 15 | El Dorado International Airport |  | CO | 1239 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1195 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1147 |
| 19 | Madrid Barajas International Airport |  | ES | 1137 |
| 20 | Congonhas Airport |  | BR | 1122 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1048 |
| 23 | Charlotte/Douglas International Airport |  | US | 1019 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 999 |
| 25 | Charles de Gaulle International Airport |  | FR | 991 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 964 |
| 27 | Bengaluru International Airport |  | IN | 961 |
| 28 | Malpensa International Airport |  | IT | 906 |
| 29 | Ninoy Aquino International Airport |  | PH | 880 |
| 30 | Daniel K Inouye International Airport |  | US | 854 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 852 |
| 32 | Barcelona International Airport |  | ES | 851 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 817 |
| 34 | Tenerife Norte Airport |  | ES | 816 |
| 35 | Calgary International Airport |  | CA | 803 |
| 36 | Viracopos International Airport |  | BR | 797 |
| 37 | Seattle-Tacoma International Airport |  | US | 793 |
| 38 | Scottsdale Airport |  | US | 792 |
| 39 | Amsterdam Airport Schiphol |  | NL | 783 |
| 40 | Vitoria/Foronda Airport |  | ES | 776 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 717 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 504 | 21m | 244 km | 2,122.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 190 | 26m | 215 km | 703.7 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 184 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 155 | 14m | 154 km | 410.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 153 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N80616 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-12 20:31 UTC | 2026-07-12 21:13 UTC | 42m |
| SKW5371 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Milford Municipal/Ben And Judy Briscoe Field (KMLF) | 2026-07-12 20:10 UTC | 2026-07-12 21:11 UTC | 1h 0m |
| N14HX |  | 01UT (01UT) | Blanding Municipal Airport (KBDG) | 2026-07-12 20:55 UTC | 2026-07-12 21:09 UTC | 14m |
| AAL759 | American Airlines | Eleftherios Venizelos International Airport (LGAV) | Philadelphia International Airport (KPHL) | 2026-07-12 11:06 UTC | 2026-07-12 21:09 UTC | 10h 2m |
| CREEP31 | CRE | Enid Woodring Regional Airport (KWDG) | Lariat Ranch Airport (OK42) | 2026-07-12 20:44 UTC | 2026-07-12 21:08 UTC | 23m |
| N434M |  | John Wayne/Orange County Airport (KSNA) | Hemet-Ryan Airport (KHMT) | 2026-07-12 20:18 UTC | 2026-07-12 21:08 UTC | 49m |
| CXK1141 | CXK | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-07-12 20:39 UTC | 2026-07-12 21:07 UTC | 27m |
| ARRIS79 | ARR | Monterey Regional Airport (KMRY) | Ancient Valley/Pontious Airport (1CL2) | 2026-07-12 20:32 UTC | 2026-07-12 21:05 UTC | 33m |
| N605WM |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-07-12 20:26 UTC | 2026-07-12 21:05 UTC | 39m |
| BOE493 | BOE | Seattle Paine Field International Airport (KPAE) | Warden Airport (K2S4) | 2026-07-12 19:26 UTC | 2026-07-12 21:05 UTC | 1h 38m |
| N53LS |  | Nephi Municipal Airport (KU14) | Sanpete County Regional Airport (K41U) | 2026-07-12 19:26 UTC | 2026-07-12 21:03 UTC | 1h 37m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | K36U (K36U) | 2026-07-12 20:37 UTC | 2026-07-12 20:59 UTC | 21m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | K36U (K36U) | 2026-07-12 20:36 UTC | 2026-07-12 20:59 UTC | 22m |
| TKR168 | TKR | Flying M & M Ranch Airport (0CO6) | Blanding Municipal Airport (KBDG) | 2026-07-12 20:47 UTC | 2026-07-12 20:58 UTC | 10m |
| N102JL |  | Richmond Municipal Airport (KRID) | Richmond Municipal Airport (KRID) | 2026-07-12 20:10 UTC | 2026-07-12 20:56 UTC | 45m |
| N521MB |  | II49 (II49) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-07-12 20:07 UTC | 2026-07-12 20:55 UTC | 48m |
| N41HX |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-12 19:40 UTC | 2026-07-12 20:51 UTC | 1h 11m |
| N43RJ |  | 2AR6 (2AR6) | Eldon Model Airpark (KH79) | 2026-07-12 20:09 UTC | 2026-07-12 20:51 UTC | 41m |
| TKR895 | TKR | K43U (K43U) | K36U (K36U) | 2026-07-12 20:34 UTC | 2026-07-12 20:51 UTC | 16m |
| N162SA |  | Buchanan Field (KCCR) | Yolo County Airport (KDWA) | 2026-07-12 19:53 UTC | 2026-07-12 20:49 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
