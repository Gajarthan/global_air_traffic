# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_14:15:36_UTC-green)

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

**Latest saved flight:** 2026-04-14 14:15:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 14:15:36 UTC

- **34,067** saved flights
- **15,103** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,067** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **418,789.1 tonnes** estimated CO2 emissions
- **24,277,628 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1457 |
| 2 | SkyWest Airlines | 1355 |
| 3 | IndiGo | 863 |
| 4 | American Airlines | 585 |
| 5 | EJA | 578 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 450 |
| 8 | Lufthansa | 380 |
| 9 | AXM | 363 |
| 10 | Vueling | 350 |
| 11 | LATAM Airlines | 341 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 302 |
| 14 | QLK | 289 |
| 15 | Delta Air Lines | 287 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 262 |
| 18 | WIF | 244 |
| 19 | AEE | 230 |
| 20 | easyJet | 230 |
| 21 | Alaska Airlines | 228 |
| 22 | EJU | 227 |
| 23 | VIV | 221 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | Air France | 187 |
| 28 | GLO | 184 |
| 29 | Avianca | 181 |
| 30 | JetBlue | 180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26550 |
| 2 | 🇮🇳 IN | 2644 |
| 3 | 🇪🇸 ES | 2570 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 2003 |
| 6 | 🇯🇵 JP | 1873 |
| 7 | 🇮🇹 IT | 1837 |
| 8 | 🇩🇪 DE | 1740 |
| 9 | 🇨🇴 CO | 1698 |
| 10 | 🇨🇦 CA | 1655 |
| 11 | 🇬🇧 GB | 1406 |
| 12 | 🇫🇷 FR | 1271 |
| 13 | 🇲🇽 MX | 1082 |
| 14 | 🇬🇷 GR | 1012 |
| 15 | 🇨🇭 CH | 948 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 795 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 720 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 635 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 585 |
| 25 | 🇵🇱 PL | 535 |
| 26 | 🇲🇦 MA | 434 |
| 27 | 🇧🇸 BS | 342 |
| 28 | 🇳🇱 NL | 339 |
| 29 | 🇲🇪 ME | 338 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 804 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 608 |
| 4 | Denver International Airport |  | US | 571 |
| 5 | Indira Gandhi International Airport |  | IN | 562 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 496 |
| 7 | Harry Reid International Airport |  | US | 448 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 425 |
| 10 | Guaymaral Airport |  | CO | 413 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 333 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 310 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 303 |
| 21 | Ninoy Aquino International Airport |  | PH | 301 |
| 22 | Tenerife Norte Airport |  | ES | 301 |
| 23 | Congonhas Airport |  | BR | 298 |
| 24 | Malpensa International Airport |  | IT | 281 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 261 |
| 26 | Daniel K Inouye International Airport |  | US | 259 |
| 27 | Salt Lake City International Airport |  | US | 256 |
| 28 | Charles de Gaulle International Airport |  | FR | 251 |
| 29 | Capua Airport |  | IT | 250 |
| 30 | Reno/Tahoe International Airport |  | US | 243 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 240 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 239 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 233 |
| 34 | O. R. Tambo International Airport |  | ZA | 232 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 229 |
| 36 | Vitoria/Foronda Airport |  | ES | 227 |
| 37 | Barcelona International Airport |  | ES | 223 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 212 |
| 40 | Viracopos International Airport |  | BR | 210 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 160 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 141 | 14m | 114 km | 276.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 76 | 21m | 244 km | 320.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 74 | 27m | 275 km | 350.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 59 | 20m | 250 km | 254.8 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 56 | 20m | 147 km | 141.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 49 | 12m | 15 km | 12.9 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 49 | 14m | 154 km | 129.8 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 48 | 26m | 215 km | 177.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 48 | 1h 20m | 961 km | 795.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AUA1Y | Austrian Airlines | Vienna International Airport (LOWW) | Frankfurt am Main International Airport (EDDF) | 2026-04-14 13:06 UTC | 2026-04-14 14:15 UTC | 1h 9m |
| CFE1T | CFE | London City Airport (EGLC) | London City Airport (EGLC) | 2026-04-14 13:55 UTC | 2026-04-14 14:06 UTC | 11m |
| N9944Q |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-04-14 13:45 UTC | 2026-04-14 14:06 UTC | 21m |
| CXK416 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-04-14 12:58 UTC | 2026-04-14 14:04 UTC | 1h 5m |
|  |  | Piedmont Triad International Airport (KGSO) | Piedmont Triad International Airport (KGSO) | 2026-04-14 13:54 UTC | 2026-04-14 13:54 UTC | 0m |
| GAF619 | GAF | Berlin Brandenburg Airport (EDDB) | Memmingen Allgau Airport (EDJA) | 2026-04-14 12:55 UTC | 2026-04-14 13:50 UTC | 54m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-14 13:17 UTC | 2026-04-14 13:46 UTC | 29m |
| LVHQR | LVH | San Fernando Airport (SADF) | SAVO (SAVO) | 2026-04-14 13:25 UTC | 2026-04-14 13:43 UTC | 17m |
| N210JE |  | Tampa Executive Airport (KVDF) | Market World Airport (FL16) | 2026-04-14 12:27 UTC | 2026-04-14 13:38 UTC | 1h 11m |
| SCU21 | SCU | Flying G Ranch Airport (3OK8) | Flying G Ranch Airport (3OK8) | 2026-04-14 13:33 UTC | 2026-04-14 13:38 UTC | 5m |
| CXK345 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-04-14 12:22 UTC | 2026-04-14 13:37 UTC | 1h 15m |
| N309HG |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-04-14 12:51 UTC | 2026-04-14 13:30 UTC | 39m |
| ZSSBI | ZSS | Marble Hall Airport (FAMI) | Heidelburg Airport (FAHG) | 2026-04-14 12:57 UTC | 2026-04-14 13:26 UTC | 28m |
| N343AS |  | New Garden Airport (KN57) | New Garden Airport (KN57) | 2026-04-14 12:44 UTC | 2026-04-14 13:23 UTC | 39m |
| ARG01 | ARG | Jorge Newbery Airpark (SABE) | Astor Piazzola International Airport (SAZM) | 2026-04-14 12:50 UTC | 2026-04-14 13:23 UTC | 32m |
| EJU32DG | EJU | Palma De Mallorca Airport (LEPA) | Zurich Airport (LSZH) | 2026-04-14 11:42 UTC | 2026-04-14 13:21 UTC | 1h 38m |
| IGO209H | IndiGo | Indira Gandhi International Airport (VIDP) | Giridih Airport (VE41) | 2026-04-14 12:02 UTC | 2026-04-14 13:21 UTC | 1h 18m |
| HB2546 |  | Lodrino Air Base (LSML) | Lodrino Air Base (LSML) | 2026-04-14 12:47 UTC | 2026-04-14 13:20 UTC | 32m |
| DREAD81 | DRE | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | AL81 (AL81) | 2026-04-14 12:46 UTC | 2026-04-14 13:20 UTC | 33m |
| PFA339 | PFA | Lake Montaza Airport (83FD) | Lake Montaza Airport (83FD) | 2026-04-14 13:18 UTC | 2026-04-14 13:20 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
