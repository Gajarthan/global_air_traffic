# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_21:21:14_UTC-green)

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

**Latest saved flight:** 2026-04-14 21:21:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 21:21:14 UTC

- **34,840** saved flights
- **15,412** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,840** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **426,120.9 tonnes** estimated CO2 emissions
- **24,702,661 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1503 |
| 2 | SkyWest Airlines | 1394 |
| 3 | IndiGo | 870 |
| 4 | American Airlines | 602 |
| 5 | EJA | 602 |
| 6 | Southwest Airlines | 498 |
| 7 | ENY | 460 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 355 |
| 11 | LATAM Airlines | 348 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 310 |
| 14 | Delta Air Lines | 294 |
| 15 | QLK | 289 |
| 16 | LXJ | 279 |
| 17 | Swiss International | 265 |
| 18 | WIF | 254 |
| 19 | AEE | 234 |
| 20 | easyJet | 234 |
| 21 | Alaska Airlines | 233 |
| 22 | EJU | 231 |
| 23 | VIV | 225 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 199 |
| 26 | United Airlines | 197 |
| 27 | Air France | 193 |
| 28 | GLO | 187 |
| 29 | JetBlue | 185 |
| 30 | Avianca | 182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27399 |
| 2 | 🇮🇳 IN | 2660 |
| 3 | 🇪🇸 ES | 2624 |
| 4 | 🇦🇺 AU | 2419 |
| 5 | 🇧🇷 BR | 2052 |
| 6 | 🇮🇹 IT | 1879 |
| 7 | 🇯🇵 JP | 1873 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1747 |
| 10 | 🇨🇦 CA | 1691 |
| 11 | 🇬🇧 GB | 1443 |
| 12 | 🇫🇷 FR | 1300 |
| 13 | 🇲🇽 MX | 1114 |
| 14 | 🇬🇷 GR | 1038 |
| 15 | 🇨🇭 CH | 959 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 823 |
| 18 | 🇳🇿 NZ | 730 |
| 19 | 🇿🇦 ZA | 726 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 612 |
| 24 | 🇰🇷 KR | 586 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 441 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 343 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 830 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 620 |
| 4 | Denver International Airport |  | US | 587 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 510 |
| 7 | Harry Reid International Airport |  | US | 460 |
| 8 | La Aurora Airport |  | GT | 448 |
| 9 | Guaymaral Airport |  | CO | 439 |
| 10 | Zurich Airport |  | CH | 432 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 358 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 351 |
| 13 | Chicago O'Hare International Airport |  | US | 349 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 318 |
| 19 | Charlotte/Douglas International Airport |  | US | 311 |
| 20 | Tenerife Norte Airport |  | ES | 307 |
| 21 | Bengaluru International Airport |  | IN | 307 |
| 22 | Congonhas Airport |  | BR | 304 |
| 23 | Ninoy Aquino International Airport |  | PH | 301 |
| 24 | Malpensa International Airport |  | IT | 284 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 274 |
| 26 | Daniel K Inouye International Airport |  | US | 264 |
| 27 | Salt Lake City International Airport |  | US | 264 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 247 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 243 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | Vitoria/Foronda Airport |  | ES | 232 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 231 |
| 37 | Barcelona International Airport |  | ES | 230 |
| 38 | Miami International Airport |  | US | 218 |
| 39 | Seattle-Tacoma International Airport |  | US | 217 |
| 40 | Viracopos International Airport |  | BR | 216 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 172 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 144 | 14m | 114 km | 282.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 85 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 80 | 21m | 244 km | 336.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 49 | 26m | 215 km | 181.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 49 | 14m | 154 km | 129.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 49 | 1h 20m | 961 km | 812.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| C6056 |  | San Diego International Airport (KSAN) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-14 20:06 UTC | 2026-04-14 21:21 UTC | 1h 15m |
| N813VS |  | Peter O Knight Airport (KTPF) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-04-14 20:34 UTC | 2026-04-14 21:20 UTC | 45m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-14 21:05 UTC | 2026-04-14 21:17 UTC | 11m |
| ZKTZM | ZKT | North Shore Aerodrome (NZNE) | North Shore Aerodrome (NZNE) | 2026-04-14 20:50 UTC | 2026-04-14 21:15 UTC | 25m |
| N127HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-04-14 20:54 UTC | 2026-04-14 21:15 UTC | 20m |
| N842MA |  | 33NR (33NR) | Statesville Regional Airport (KSVH) | 2026-04-14 20:30 UTC | 2026-04-14 21:10 UTC | 40m |
| EPI823 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-04-14 21:05 UTC | 2026-04-14 21:05 UTC | 0m |
| LS30 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-14 20:27 UTC | 2026-04-14 21:04 UTC | 37m |
| WZZ56 | Wizz Air | Tallinn Airport (EETN) | Khrabrovo Airport (UMKK) | 2026-04-14 20:14 UTC | 2026-04-14 20:58 UTC | 44m |
| N973KB |  | Gnoss Field (KDVO) | Buchanan Field (KCCR) | 2026-04-14 20:44 UTC | 2026-04-14 20:58 UTC | 13m |
| QFA30 | Qantas | Chek Lap Kok International Airport (VHHH) | Melbourne International Airport (YMML) | 2026-04-14 12:32 UTC | 2026-04-14 20:55 UTC | 8h 22m |
| SPEED51 | SPE | Lamar County Airport (KM55) | AL54 (AL54) | 2026-04-14 20:35 UTC | 2026-04-14 20:54 UTC | 19m |
|  |  | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-04-14 20:17 UTC | 2026-04-14 20:53 UTC | 36m |
| N5242D |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-04-14 20:45 UTC | 2026-04-14 20:48 UTC | 2m |
| N484MM |  | Austin-Bergstrom International Airport (KAUS) | Locker Brothers Airport (1TE0) | 2026-04-14 19:35 UTC | 2026-04-14 20:48 UTC | 1h 13m |
| XBMFB | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-14 20:12 UTC | 2026-04-14 20:46 UTC | 34m |
| N523PC |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-04-14 20:23 UTC | 2026-04-14 20:45 UTC | 22m |
| N75ND |  | William R Pogue Municipal Airport (KOWP) | Ricks Field (65MN) | 2026-04-14 18:40 UTC | 2026-04-14 20:45 UTC | 2h 4m |
| N552KM |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-04-14 20:01 UTC | 2026-04-14 20:43 UTC | 41m |
| CXK153 | CXK | Long Island Mac Arthur Airport (KISP) | Talmage Field (03NY) | 2026-04-14 19:59 UTC | 2026-04-14 20:38 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
