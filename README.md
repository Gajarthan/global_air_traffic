# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_04:37:25_UTC-green)

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

**Latest saved flight:** 2026-04-16 04:37:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 04:37:25 UTC

- **36,878** saved flights
- **16,037** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,878** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **447,046.4 tonnes** estimated CO2 emissions
- **25,915,735 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1562 |
| 2 | SkyWest Airlines | 1460 |
| 3 | IndiGo | 912 |
| 4 | EJA | 630 |
| 5 | American Airlines | 623 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 484 |
| 8 | AXM | 394 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 374 |
| 11 | Vueling | 370 |
| 12 | All Nippon Airways | 330 |
| 13 | AZU | 327 |
| 14 | Delta Air Lines | 313 |
| 15 | QLK | 305 |
| 16 | LXJ | 293 |
| 17 | Swiss International | 277 |
| 18 | WIF | 272 |
| 19 | AEE | 247 |
| 20 | Alaska Airlines | 246 |
| 21 | easyJet | 242 |
| 22 | EJU | 238 |
| 23 | VIV | 234 |
| 24 | Japan Airlines | 226 |
| 25 | Air France | 208 |
| 26 | EDV | 206 |
| 27 | United Airlines | 205 |
| 28 | GLO | 196 |
| 29 | AIQ | 194 |
| 30 | JetBlue | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29041 |
| 2 | 🇮🇳 IN | 2791 |
| 3 | 🇪🇸 ES | 2732 |
| 4 | 🇦🇺 AU | 2602 |
| 5 | 🇧🇷 BR | 2170 |
| 6 | 🇯🇵 JP | 1999 |
| 7 | 🇮🇹 IT | 1951 |
| 8 | 🇩🇪 DE | 1884 |
| 9 | 🇨🇦 CA | 1819 |
| 10 | 🇨🇴 CO | 1817 |
| 11 | 🇬🇧 GB | 1511 |
| 12 | 🇫🇷 FR | 1387 |
| 13 | 🇲🇽 MX | 1159 |
| 14 | 🇬🇷 GR | 1110 |
| 15 | 🇨🇭 CH | 1004 |
| 16 | 🇲🇾 MY | 945 |
| 17 | 🇳🇴 NO | 884 |
| 18 | 🇳🇿 NZ | 785 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 694 |
| 21 | 🇹🇭 TH | 680 |
| 22 | 🇹🇷 TR | 664 |
| 23 | 🇬🇹 GT | 626 |
| 24 | 🇰🇷 KR | 618 |
| 25 | 🇵🇱 PL | 573 |
| 26 | 🇲🇦 MA | 465 |
| 27 | 🇳🇱 NL | 364 |
| 28 | 🇧🇸 BS | 356 |
| 29 | 🇲🇪 ME | 355 |
| 30 | 🇮🇩 ID | 346 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 871 |
| 2 | Tokyo International Airport |  | JP | 680 |
| 3 | El Dorado International Airport |  | CO | 648 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 600 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 546 |
| 7 | Harry Reid International Airport |  | US | 482 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 369 |
| 13 | Kuala Lumpur International Airport |  | MY | 368 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 351 |
| 16 | Frankfurt am Main International Airport |  | DE | 340 |
| 17 | Macau International Airport |  | MO | 337 |
| 18 | Madrid Barajas International Airport |  | ES | 333 |
| 19 | Charlotte/Douglas International Airport |  | US | 329 |
| 20 | Tenerife Norte Airport |  | ES | 325 |
| 21 | Bengaluru International Airport |  | IN | 324 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 321 |
| 24 | Malpensa International Airport |  | IT | 299 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 287 |
| 26 | Daniel K Inouye International Airport |  | US | 277 |
| 27 | Salt Lake City International Airport |  | US | 277 |
| 28 | Charles de Gaulle International Airport |  | FR | 273 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 261 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 258 |
| 32 | Reno/Tahoe International Airport |  | US | 255 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 249 |
| 34 | O. R. Tambo International Airport |  | ZA | 248 |
| 35 | Vitoria/Foronda Airport |  | ES | 242 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Don Mueang International Airport |  | TH | 231 |
| 39 | Viracopos International Airport |  | BR | 230 |
| 40 | Seattle-Tacoma International Airport |  | US | 228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 172 | 1h 8m | 706 km | 2,094.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 135 | 24m | 225 km | 523.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 106 | 1h 27m | 910 km | 1,663.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 99 | 19m | 165 km | 281.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 88 | 21m | 244 km | 370.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 81 | 54m | 546 km | 762.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 80 | 27m | 275 km | 379.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 70 | 31m | 369 km | 445.6 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 69 | 45m | 452 km | 537.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 55 | 1h 41m | 1,423 km | 1,349.8 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SLQ | SLQ | Southport Airport (YSPT) | Gold Coast Airport (YBCG) | 2026-04-16 04:25 UTC | 2026-04-16 04:37 UTC | 12m |
| CCA437 | Air China | Ramechhap Airport (VNRC) | Langtang Airport (VNLT) | 2026-04-16 04:19 UTC | 2026-04-16 04:31 UTC | 12m |
| TRP5 | TRP | Valley Point Airport (WV29) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-16 04:11 UTC | 2026-04-16 04:16 UTC | 5m |
| AM272 |  | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-16 03:48 UTC | 2026-04-16 04:14 UTC | 26m |
| UTA572 | UTA | Sheremetyevo International Airport (UUEE) | Tunoshna Airport (UUDL) | 2026-04-15 18:47 UTC | 2026-04-16 04:14 UTC | 9h 26m |
| ERU13 | ERU | Pilots Rest Airport (AZ57) | Big Springs Ranch Airport (AZ27) | 2026-04-16 04:11 UTC | 2026-04-16 04:12 UTC | 1m |
| JST297 | JST | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-04-16 02:45 UTC | 2026-04-16 04:07 UTC | 1h 22m |
| EMD1 | EMD | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 9TA2 (9TA2) | 2026-04-16 03:15 UTC | 2026-04-16 04:00 UTC | 44m |
| FDA353 | FDA | Nagoya Airport (RJNA) | Yamagata Airport (RJSC) | 2026-04-16 03:18 UTC | 2026-04-16 03:59 UTC | 40m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Annette Island Airport (PANT) | 2026-04-16 02:30 UTC | 2026-04-16 03:58 UTC | 1h 27m |
| UXOM06 | UXO | Rainbow Beach Airport (YRBB) | Rainbow Beach Airport (YRBB) | 2026-04-16 03:41 UTC | 2026-04-16 03:57 UTC | 16m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-04-16 02:17 UTC | 2026-04-16 03:57 UTC | 1h 39m |
| JAL259 | Japan Airlines | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-16 03:03 UTC | 2026-04-16 03:54 UTC | 50m |
| N365MT |  | Millen Airport (K2J5) | Hunter Army Air Field (KSVN) | 2026-04-16 03:16 UTC | 2026-04-16 03:52 UTC | 35m |
| N605FF |  | Santa Barbara Municipal Airport (KSBA) | Hemet-Ryan Airport (KHMT) | 2026-04-16 02:23 UTC | 2026-04-16 03:51 UTC | 1h 28m |
| AIQ610 | AIQ | Don Mueang International Airport (VTBD) | Battambang Airport (VDBG) | 2026-04-16 03:22 UTC | 2026-04-16 03:50 UTC | 27m |
| AIC213 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-16 02:42 UTC | 2026-04-16 03:50 UTC | 1h 8m |
| TWY522 | TWY | Washington Dulles International Airport (KIAD) | Moffett Federal Airfield (KNUQ) | 2026-04-15 22:55 UTC | 2026-04-16 03:49 UTC | 4h 54m |
| HMZ | HMZ | Perth Jandakot Airport (YPJT) | Morawa Airport (YMRW) | 2026-04-16 03:00 UTC | 2026-04-16 03:49 UTC | 48m |
| IVW | IVW | Redcliffe Airport (YRED) | Sunshine Coast Airport (YBMC) | 2026-04-16 03:22 UTC | 2026-04-16 03:49 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
