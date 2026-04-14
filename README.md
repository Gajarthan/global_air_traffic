# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_23:05:34_UTC-green)

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

**Latest saved flight:** 2026-04-14 23:05:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 23:05:34 UTC

- **35,014** saved flights
- **15,461** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,014** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **427,942.9 tonnes** estimated CO2 emissions
- **24,808,286 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1503 |
| 2 | SkyWest Airlines | 1404 |
| 3 | IndiGo | 870 |
| 4 | EJA | 609 |
| 5 | American Airlines | 606 |
| 6 | Southwest Airlines | 503 |
| 7 | ENY | 466 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 356 |
| 11 | LATAM Airlines | 349 |
| 12 | AZU | 313 |
| 13 | All Nippon Airways | 310 |
| 14 | Delta Air Lines | 298 |
| 15 | QLK | 294 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 265 |
| 18 | WIF | 254 |
| 19 | Alaska Airlines | 235 |
| 20 | AEE | 234 |
| 21 | easyJet | 234 |
| 22 | EJU | 231 |
| 23 | VIV | 227 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 201 |
| 26 | United Airlines | 199 |
| 27 | Air France | 193 |
| 28 | GLO | 190 |
| 29 | JetBlue | 186 |
| 30 | Avianca | 183 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27606 |
| 2 | 🇮🇳 IN | 2661 |
| 3 | 🇪🇸 ES | 2626 |
| 4 | 🇦🇺 AU | 2445 |
| 5 | 🇧🇷 BR | 2065 |
| 6 | 🇮🇹 IT | 1882 |
| 7 | 🇯🇵 JP | 1873 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1756 |
| 10 | 🇨🇦 CA | 1713 |
| 11 | 🇬🇧 GB | 1445 |
| 12 | 🇫🇷 FR | 1300 |
| 13 | 🇲🇽 MX | 1120 |
| 14 | 🇬🇷 GR | 1038 |
| 15 | 🇨🇭 CH | 959 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 823 |
| 18 | 🇳🇿 NZ | 744 |
| 19 | 🇿🇦 ZA | 726 |
| 20 | 🇵🇭 PH | 654 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 612 |
| 24 | 🇰🇷 KR | 586 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 441 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 344 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 839 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 624 |
| 4 | Denver International Airport |  | US | 590 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 510 |
| 7 | Harry Reid International Airport |  | US | 464 |
| 8 | La Aurora Airport |  | GT | 448 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 432 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 360 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 355 |
| 13 | Chicago O'Hare International Airport |  | US | 353 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 334 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Charlotte/Douglas International Airport |  | US | 318 |
| 19 | Madrid Barajas International Airport |  | ES | 318 |
| 20 | Tenerife Norte Airport |  | ES | 307 |
| 21 | Bengaluru International Airport |  | IN | 307 |
| 22 | Congonhas Airport |  | BR | 306 |
| 23 | Ninoy Aquino International Airport |  | PH | 302 |
| 24 | Malpensa International Airport |  | IT | 285 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 277 |
| 26 | Salt Lake City International Airport |  | US | 266 |
| 27 | Daniel K Inouye International Airport |  | US | 265 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 247 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 245 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 233 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 220 |
| 39 | Viracopos International Airport |  | BR | 219 |
| 40 | Miami International Airport |  | US | 218 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 146 | 14m | 114 km | 286.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 85 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 81 | 21m | 244 km | 341.1 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 67 | 31m | 369 km | 426.5 t |
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
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 49 | 26m | 215 km | 181.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N227SL |  | Brisbane Archerfield Airport (YBAF) | Melbourne Essendon Airport (YMEN) | 2026-04-14 20:43 UTC | 2026-04-14 23:05 UTC | 2h 21m |
| RUDY24 | RUD | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-14 22:20 UTC | 2026-04-14 22:57 UTC | 37m |
| N26SQ |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-04-14 22:34 UTC | 2026-04-14 22:57 UTC | 23m |
| N405B |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-04-14 22:25 UTC | 2026-04-14 22:50 UTC | 25m |
| ERU25 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-04-14 22:26 UTC | 2026-04-14 22:35 UTC | 8m |
| N247TC |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-14 21:58 UTC | 2026-04-14 22:30 UTC | 32m |
| LXJ397 | LXJ | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-04-14 22:00 UTC | 2026-04-14 22:28 UTC | 28m |
| N523PC |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-04-14 21:08 UTC | 2026-04-14 22:23 UTC | 1h 15m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-04-14 11:19 UTC | 2026-04-14 22:23 UTC | 11h 4m |
| KOT | KOT | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-14 22:09 UTC | 2026-04-14 22:23 UTC | 13m |
| N73047 |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-04-14 21:59 UTC | 2026-04-14 22:23 UTC | 23m |
| N327RX |  | Capital Region International Airport (KLAN) | Tweed/New Haven Airport (KHVN) | 2026-04-14 21:11 UTC | 2026-04-14 22:22 UTC | 1h 10m |
| SKW4830 | SkyWest Airlines | Charlotte/Douglas International Airport (KCLT) | Greenbrier Valley Airport (KLWB) | 2026-04-14 21:52 UTC | 2026-04-14 22:22 UTC | 30m |
| BOSOX31 | BOS | 61MA (61MA) | 61MA (61MA) | 2026-04-14 22:20 UTC | 2026-04-14 22:22 UTC | 1m |
|  |  | 1TS3 (1TS3) | 1TS3 (1TS3) | 2026-04-14 22:21 UTC | 2026-04-14 22:21 UTC | 0m |
| EJA680 | EJA | Concord Municipal Airport (KCON) | Austin-Bergstrom International Airport (KAUS) | 2026-04-14 18:00 UTC | 2026-04-14 22:21 UTC | 4h 20m |
| NSH878 | NSH | Snow Hill Airport (VA19) | John F Kennedy International Airport (KJFK) | 2026-04-14 21:27 UTC | 2026-04-14 22:21 UTC | 54m |
| N9914L |  | Montgomery-Gibbs Executive Airport (KMYF) | Borrego Air Ranch Airport (58CL) | 2026-04-14 21:44 UTC | 2026-04-14 22:21 UTC | 37m |
| JANET51 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-14 22:07 UTC | 2026-04-14 22:21 UTC | 14m |
| EJA843 | EJA | Chicago Executive Airport (KPWK) | Scottsdale Airport (KSDL) | 2026-04-14 18:50 UTC | 2026-04-14 22:19 UTC | 3h 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
