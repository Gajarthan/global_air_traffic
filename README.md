# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_22:54:10_UTC-green)

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

**Latest saved flight:** 2026-07-25 22:54:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 22:54:10 UTC

- **151,373** saved flights
- **50,303** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,373** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,810,829.3 tonnes** estimated CO2 emissions
- **104,975,610 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6110 |
| 2 | SkyWest Airlines | 5547 |
| 3 | EJA | 2997 |
| 4 | IndiGo | 2694 |
| 5 | American Airlines | 2404 |
| 6 | Southwest Airlines | 2304 |
| 7 | ENY | 1892 |
| 8 | Delta Air Lines | 1778 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1402 |
| 11 | AZU | 1315 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1271 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 987 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 944 |
| 20 | QLK | 932 |
| 21 | EJU | 928 |
| 22 | VIV | 835 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 794 |
| 26 | Air France | 788 |
| 27 | GLO | 788 |
| 28 | JetBlue | 788 |
| 29 | United Airlines | 782 |
| 30 | Cathay Pacific | 781 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130670 |
| 2 | 🇪🇸 ES | 9788 |
| 3 | 🇧🇷 BR | 8584 |
| 4 | 🇦🇺 AU | 8507 |
| 5 | 🇮🇳 IN | 8482 |
| 6 | 🇨🇦 CA | 8085 |
| 7 | 🇮🇹 IT | 7837 |
| 8 | 🇩🇪 DE | 7756 |
| 9 | 🇬🇧 GB | 6942 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5988 |
| 12 | 🇨🇴 CO | 5157 |
| 13 | 🇲🇽 MX | 4370 |
| 14 | 🇬🇷 GR | 4298 |
| 15 | 🇳🇴 NO | 4002 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3589 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2569 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2273 |
| 22 | 🇹🇭 TH | 2193 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2011 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1542 |
| 27 | 🇲🇪 ME | 1481 |
| 28 | 🇳🇱 NL | 1395 |
| 29 | 🇭🇷 HR | 1385 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3118 |
| 2 | Denver International Airport |  | US | 2546 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1906 |
| 5 | Indira Gandhi International Airport |  | IN | 1882 |
| 6 | Harry Reid International Airport |  | US | 1870 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1695 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1587 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1430 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1416 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | El Dorado International Airport |  | CO | 1363 |
| 15 | Salt Lake City International Airport |  | US | 1362 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1292 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1228 |
| 19 | Madrid Barajas International Airport |  | ES | 1208 |
| 20 | Capua Airport |  | IT | 1205 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1173 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1077 |
| 24 | Charlotte/Douglas International Airport |  | US | 1077 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1068 |
| 26 | Charles de Gaulle International Airport |  | FR | 1038 |
| 27 | Bengaluru International Airport |  | IN | 1012 |
| 28 | Malpensa International Airport |  | IT | 993 |
| 29 | Ninoy Aquino International Airport |  | PH | 942 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 917 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 908 |
| 32 | Barcelona International Airport |  | ES | 906 |
| 33 | Daniel K Inouye International Airport |  | US | 904 |
| 34 | Tenerife Norte Airport |  | ES | 872 |
| 35 | Seattle-Tacoma International Airport |  | US | 871 |
| 36 | Calgary International Airport |  | CA | 862 |
| 37 | Viracopos International Airport |  | BR | 856 |
| 38 | Scottsdale Airport |  | US | 854 |
| 39 | Amsterdam Airport Schiphol |  | NL | 838 |
| 40 | Oslo Gardermoen Airport |  | NO | 830 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 804 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 548 | 21m | 244 km | 2,307.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 182 | 30m | 49 km | 153.8 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 165 | 51m | 556 km | 1,581.7 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ENY4165 | ENY | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 2026-07-25 21:43 UTC | 2026-07-25 22:54 UTC | 1h 11m |
| RAM207T | Royal Air Maroc | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Mohammed V International Airport (GMMN) | 2026-07-25 16:29 UTC | 2026-07-25 22:52 UTC | 6h 22m |
| RAM751P | Royal Air Maroc | Paris-Orly Airport (LFPO) | Mohammed V International Airport (GMMN) | 2026-07-25 20:24 UTC | 2026-07-25 22:46 UTC | 2h 22m |
| N55169 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-07-25 21:51 UTC | 2026-07-25 22:45 UTC | 53m |
| N20DK |  | Drake Field (KFYV) | Drake Field (KFYV) | 2026-07-25 22:01 UTC | 2026-07-25 22:44 UTC | 43m |
| N3NJ |  | Greenwood Lake Airport (K4N1) | Essex County Airport (KCDW) | 2026-07-25 22:24 UTC | 2026-07-25 22:35 UTC | 11m |
| N3765F |  | Gastonia Municipal Airport (KAKH) | York Airport (01SC) | 2026-07-25 22:15 UTC | 2026-07-25 22:35 UTC | 20m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-07-25 22:19 UTC | 2026-07-25 22:35 UTC | 15m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-25 22:16 UTC | 2026-07-25 22:26 UTC | 10m |
| N870AE |  | 4IS1 (4IS1) | Frasca Field (KC16) | 2026-07-25 22:10 UTC | 2026-07-25 22:23 UTC | 12m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-25 22:08 UTC | 2026-07-25 22:22 UTC | 13m |
| TKR01 | TKR | Boise Air Trml/Gowen Field (KBOI) | Payette Municipal Airport (KS75) | 2026-07-25 22:12 UTC | 2026-07-25 22:20 UTC | 8m |
| CFUDF | CFU | Beiseker Airport (CFV2) | Beiseker Airport (CFV2) | 2026-07-25 22:00 UTC | 2026-07-25 22:19 UTC | 18m |
| N815ML |  | Camarillo Airport (KCMA) | Oxnard Airport (KOXR) | 2026-07-25 21:36 UTC | 2026-07-25 22:19 UTC | 42m |
| VKG807 | VKG | Antalya International Airport (LTAI) | EPZK (EPZK) | 2026-07-25 19:50 UTC | 2026-07-25 22:18 UTC | 2h 28m |
| N234FF |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-07-25 20:36 UTC | 2026-07-25 22:12 UTC | 1h 35m |
| N677F |  | Rocky Mountain Metro Airport (KBJC) | Raton Municipal/Crews Field (KRTN) | 2026-07-25 20:01 UTC | 2026-07-25 22:10 UTC | 2h 9m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Symms Airport (08ID) | 2026-07-25 22:00 UTC | 2026-07-25 22:08 UTC | 7m |
| SWA3709 | Southwest Airlines | William P Hobby Airport (KHOU) | Tampa International Airport (KTPA) | 2026-07-25 20:20 UTC | 2026-07-25 22:06 UTC | 1h 46m |
| N493LG |  | Usaf Academy Davis Airfield (KAFF) | 7CO1 (7CO1) | 2026-07-25 21:52 UTC | 2026-07-25 22:06 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
