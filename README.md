# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_17:26:07_UTC-green)

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

**Latest saved flight:** 2026-04-12 17:26:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 17:26:07 UTC

- **30,855** saved flights
- **14,051** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,855** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **378,543.0 tonnes** estimated CO2 emissions
- **21,944,520 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1286 |
| 2 | SkyWest Airlines | 1242 |
| 3 | IndiGo | 803 |
| 4 | American Airlines | 531 |
| 5 | EJA | 528 |
| 6 | Southwest Airlines | 440 |
| 7 | ENY | 414 |
| 8 | Lufthansa | 366 |
| 9 | AXM | 335 |
| 10 | Vueling | 318 |
| 11 | LATAM Airlines | 307 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 269 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 252 |
| 16 | LXJ | 242 |
| 17 | Swiss International | 229 |
| 18 | easyJet | 204 |
| 19 | EJU | 203 |
| 20 | Alaska Airlines | 202 |
| 21 | WIF | 200 |
| 22 | VIV | 199 |
| 23 | Japan Airlines | 197 |
| 24 | AEE | 196 |
| 25 | EDV | 180 |
| 26 | United Airlines | 180 |
| 27 | Air France | 168 |
| 28 | Avianca | 167 |
| 29 | GLO | 165 |
| 30 | JetBlue | 164 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24197 |
| 2 | 🇮🇳 IN | 2465 |
| 3 | 🇪🇸 ES | 2301 |
| 4 | 🇦🇺 AU | 2173 |
| 5 | 🇧🇷 BR | 1795 |
| 6 | 🇯🇵 JP | 1711 |
| 7 | 🇮🇹 IT | 1616 |
| 8 | 🇩🇪 DE | 1558 |
| 9 | 🇨🇴 CO | 1540 |
| 10 | 🇨🇦 CA | 1493 |
| 11 | 🇬🇧 GB | 1247 |
| 12 | 🇫🇷 FR | 1143 |
| 13 | 🇲🇽 MX | 985 |
| 14 | 🇬🇷 GR | 885 |
| 15 | 🇨🇭 CH | 870 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 676 |
| 18 | 🇳🇿 NZ | 665 |
| 19 | 🇿🇦 ZA | 640 |
| 20 | 🇵🇭 PH | 575 |
| 21 | 🇹🇭 TH | 569 |
| 22 | 🇬🇹 GT | 568 |
| 23 | 🇹🇷 TR | 566 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 472 |
| 26 | 🇲🇦 MA | 400 |
| 27 | 🇧🇸 BS | 324 |
| 28 | 🇲🇪 ME | 309 |
| 29 | 🇳🇱 NL | 296 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 729 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 545 |
| 4 | Indira Gandhi International Airport |  | IN | 519 |
| 5 | Denver International Airport |  | US | 518 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 433 |
| 7 | La Aurora Airport |  | GT | 408 |
| 8 | Harry Reid International Airport |  | US | 395 |
| 9 | Zurich Airport |  | CH | 379 |
| 10 | Guaymaral Airport |  | CO | 372 |
| 11 | Chicago O'Hare International Airport |  | US | 319 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 318 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 315 |
| 14 | Frankfurt am Main International Airport |  | DE | 310 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 290 |
| 18 | Bengaluru International Airport |  | IN | 280 |
| 19 | Charlotte/Douglas International Airport |  | US | 276 |
| 20 | Tenerife Norte Airport |  | ES | 274 |
| 21 | Madrid Barajas International Airport |  | ES | 272 |
| 22 | Ninoy Aquino International Airport |  | PH | 264 |
| 23 | Congonhas Airport |  | BR | 260 |
| 24 | Malpensa International Airport |  | IT | 250 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 236 |
| 26 | Salt Lake City International Airport |  | US | 234 |
| 27 | Daniel K Inouye International Airport |  | US | 233 |
| 28 | Reno/Tahoe International Airport |  | US | 231 |
| 29 | Charles de Gaulle International Airport |  | FR | 226 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 219 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 215 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 33 | Capua Airport |  | IT | 212 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 207 |
| 35 | O. R. Tambo International Airport |  | ZA | 206 |
| 36 | Miami International Airport |  | US | 206 |
| 37 | Vitoria/Foronda Airport |  | ES | 205 |
| 38 | Barcelona International Airport |  | ES | 196 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 145 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 127 | 14m | 114 km | 249.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 71 | 27m | 152 km | 185.5 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 12 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 70 | 9m | - | - |
| 13 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 66 | 27m | 275 km | 312.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 56 | 21m | 244 km | 235.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 52 | 20m | 250 km | 224.6 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 47 | 1h 42m | 1,423 km | 1,153.5 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N789PF |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-04-12 16:59 UTC | 2026-04-12 17:26 UTC | 26m |
| N2466T |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-12 16:30 UTC | 2026-04-12 17:14 UTC | 44m |
| NOZ66Y | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-12 16:36 UTC | 2026-04-12 17:14 UTC | 37m |
| N900VP |  | Boca Raton Airport (KBCT) | Toronto Pearson International Airport (CYYZ) | 2026-04-12 13:58 UTC | 2026-04-12 17:07 UTC | 3h 9m |
| N8258P |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-04-12 16:45 UTC | 2026-04-12 17:06 UTC | 21m |
| FD513 |  | Adelaide International Airport (YPAD) | YCVA (YCVA) | 2026-04-12 16:41 UTC | 2026-04-12 17:02 UTC | 21m |
| TGKCS | TGK | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-12 16:30 UTC | 2026-04-12 17:00 UTC | 30m |
| TGBOP | TGB | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-12 16:28 UTC | 2026-04-12 16:57 UTC | 28m |
| N5983B |  | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-04-12 16:13 UTC | 2026-04-12 16:55 UTC | 42m |
| HTY218 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-12 15:51 UTC | 2026-04-12 16:55 UTC | 1h 3m |
| N271SB |  | Huntsville International-Carl T Jones Field (KHSV) | Lamar County Airport (KM55) | 2026-04-12 16:37 UTC | 2026-04-12 16:54 UTC | 16m |
| N6461Z |  | Noble County Airport (KI10) | Monroe County Airport (K4G5) | 2026-04-12 14:32 UTC | 2026-04-12 16:53 UTC | 2h 20m |
| RYR62PQ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 15:34 UTC | 2026-04-12 16:53 UTC | 1h 19m |
| N194TD |  | Nashville International Airport (KBNA) | Auburn University Regional Airport (KAUO) | 2026-04-12 16:14 UTC | 2026-04-12 16:53 UTC | 38m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-04-12 16:05 UTC | 2026-04-12 16:52 UTC | 46m |
| N421MQ |  | Orange County Airport (KMGJ) | Orange County Airport (KMGJ) | 2026-04-12 16:26 UTC | 2026-04-12 16:49 UTC | 23m |
| JBU2834 | JetBlue | Southwest Florida International Airport (KRSW) | Worcester Regional Airport (KORH) | 2026-04-12 13:57 UTC | 2026-04-12 16:48 UTC | 2h 50m |
| DEDVU | DED | Uelzen Airport (EDVU) | Uelzen Airport (EDVU) | 2026-04-12 16:35 UTC | 2026-04-12 16:48 UTC | 12m |
| N790R |  | Faro Airport (LPFR) | Bangor International Airport (KBGR) | 2026-04-12 09:26 UTC | 2026-04-12 16:42 UTC | 7h 16m |
| N721SE |  | Salt Lake City International Airport (KSLC) | Wayne Wonderland Airport (K38U) | 2026-04-12 16:14 UTC | 2026-04-12 16:41 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
