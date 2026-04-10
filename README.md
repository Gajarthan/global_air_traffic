# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_15:21:06_UTC-green)

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

**Latest saved flight:** 2026-04-10 15:21:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 15:21:06 UTC

- **26,900** saved flights
- **12,722** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,900** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **329,736.6 tonnes** estimated CO2 emissions
- **19,115,165 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1103 |
| 2 | SkyWest Airlines | 1085 |
| 3 | IndiGo | 727 |
| 4 | EJA | 475 |
| 5 | American Airlines | 473 |
| 6 | Southwest Airlines | 382 |
| 7 | ENY | 353 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 273 |
| 11 | LATAM Airlines | 264 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 222 |
| 15 | AZU | 218 |
| 16 | LXJ | 216 |
| 17 | Swiss International | 189 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 178 |
| 20 | easyJet | 177 |
| 21 | Japan Airlines | 177 |
| 22 | WIF | 177 |
| 23 | AEE | 173 |
| 24 | EJU | 172 |
| 25 | United Airlines | 159 |
| 26 | EDV | 157 |
| 27 | Avianca | 152 |
| 28 | AXB | 147 |
| 29 | JetBlue | 142 |
| 30 | Air France | 140 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21030 |
| 2 | 🇮🇳 IN | 2232 |
| 3 | 🇪🇸 ES | 1997 |
| 4 | 🇦🇺 AU | 1994 |
| 5 | 🇧🇷 BR | 1517 |
| 6 | 🇯🇵 JP | 1488 |
| 7 | 🇩🇪 DE | 1372 |
| 8 | 🇮🇹 IT | 1360 |
| 9 | 🇨🇴 CO | 1348 |
| 10 | 🇨🇦 CA | 1280 |
| 11 | 🇬🇧 GB | 1085 |
| 12 | 🇫🇷 FR | 1010 |
| 13 | 🇲🇽 MX | 856 |
| 14 | 🇬🇷 GR | 778 |
| 15 | 🇨🇭 CH | 742 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 593 |
| 19 | 🇿🇦 ZA | 558 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 500 |
| 22 | 🇬🇹 GT | 494 |
| 23 | 🇹🇭 TH | 479 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 408 |
| 26 | 🇲🇦 MA | 333 |
| 27 | 🇧🇸 BS | 279 |
| 28 | 🇲🇪 ME | 271 |
| 29 | 🇳🇱 NL | 266 |
| 30 | 🇮🇩 ID | 266 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 629 |
| 2 | Tokyo International Airport |  | JP | 500 |
| 3 | El Dorado International Airport |  | CO | 495 |
| 4 | Indira Gandhi International Airport |  | IN | 462 |
| 5 | Denver International Airport |  | US | 450 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 378 |
| 7 | Harry Reid International Airport |  | US | 347 |
| 8 | La Aurora Airport |  | GT | 343 |
| 9 | Zurich Airport |  | CH | 318 |
| 10 | Frankfurt am Main International Airport |  | DE | 287 |
| 11 | Guaymaral Airport |  | CO | 287 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 279 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 14 | Chicago O'Hare International Airport |  | US | 273 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 269 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Bengaluru International Airport |  | IN | 249 |
| 19 | Charlotte/Douglas International Airport |  | US | 246 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 231 |
| 22 | Madrid Barajas International Airport |  | ES | 229 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 211 |
| 24 | Malpensa International Airport |  | IT | 210 |
| 25 | Congonhas Airport |  | BR | 210 |
| 26 | Salt Lake City International Airport |  | US | 207 |
| 27 | Daniel K Inouye International Airport |  | US | 202 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 194 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 187 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 184 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 181 |
| 33 | Miami International Airport |  | US | 177 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 177 |
| 35 | O. R. Tambo International Airport |  | ZA | 176 |
| 36 | Barcelona International Airport |  | ES | 172 |
| 37 | Seattle-Tacoma International Airport |  | US | 169 |
| 38 | Vitoria/Foronda Airport |  | ES | 168 |
| 39 | Capua Airport |  | IT | 167 |
| 40 | Don Mueang International Airport |  | TH | 167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 109 | 14m | 114 km | 213.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 107 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 54 | 27m | 275 km | 255.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 46 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 42 | 20m | 147 km | 106.3 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N562F |  | St Louis Regional Airport (KALN) | Spirit Of St Louis Airport (KSUS) | 2026-04-10 15:01 UTC | 2026-04-10 15:21 UTC | 20m |
| N2914A |  | Beverly Regional Airport (KBVY) | Dillant/Hopkins Airport (KEEN) | 2026-04-10 14:35 UTC | 2026-04-10 15:19 UTC | 44m |
| ERU965 | ERU | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-10 15:04 UTC | 2026-04-10 15:18 UTC | 13m |
| CXK340 | CXK | Mckinney Ntl Airport (KTKI) | Baylie Airport (66XS) | 2026-04-10 14:21 UTC | 2026-04-10 15:15 UTC | 53m |
| SVR272 | SVR | Uktus Airport (USSK) | Beslan Airport (URMO) | 2026-04-10 05:54 UTC | 2026-04-10 15:15 UTC | 9h 20m |
| AR5 |  | Santa Cruz Airport (LPSC) | Santa Cruz Airport (LPSC) | 2026-04-10 14:29 UTC | 2026-04-10 15:14 UTC | 45m |
| DMDGM | DMD | Heppenheim Airport (EDEP) | Heppenheim Airport (EDEP) | 2026-04-10 13:34 UTC | 2026-04-10 15:10 UTC | 1h 36m |
| N369PS |  | Pickens County Airport (KJZP) | Pickens County Airport (KJZP) | 2026-04-10 15:05 UTC | 2026-04-10 15:05 UTC | 0m |
| N62F |  | Allegheny County Airport (KAGC) | Stitt Airport (PN59) | 2026-04-10 14:43 UTC | 2026-04-10 15:01 UTC | 17m |
| N942FA |  | North Exuma Airport (85FA) | North Exuma Airport (85FA) | 2026-04-10 14:43 UTC | 2026-04-10 15:01 UTC | 17m |
| CGNDP | CGN | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-04-10 14:29 UTC | 2026-04-10 15:00 UTC | 30m |
| N282AZ |  | Caddo Mills Municipal Airport (K7F3) | Commerce Municipal Airport (K2F7) | 2026-04-10 14:43 UTC | 2026-04-10 14:58 UTC | 14m |
| LJY930 | LJY | John C Tune Airport (KJWN) | Chautauqua County/Dunkirk Airport (KDKK) | 2026-04-10 13:37 UTC | 2026-04-10 14:50 UTC | 1h 13m |
| N586WD |  | Wiley Post Airport (KPWA) | KF29 (KF29) | 2026-04-10 14:20 UTC | 2026-04-10 14:50 UTC | 30m |
| HBKHR | HBK | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-04-10 14:46 UTC | 2026-04-10 14:48 UTC | 1m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-10 14:35 UTC | 2026-04-10 14:48 UTC | 12m |
| VEGA21 | VEG | 75OK (75OK) | 6OK0 (6OK0) | 2026-04-10 14:19 UTC | 2026-04-10 14:47 UTC | 27m |
| OHFMZ | OHF | Immola Airport (EFIM) | Immola Airport (EFIM) | 2026-04-10 14:41 UTC | 2026-04-10 14:47 UTC | 5m |
| N527WY |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-10 14:29 UTC | 2026-04-10 14:46 UTC | 16m |
| N712PA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-10 14:25 UTC | 2026-04-10 14:43 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
