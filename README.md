# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_20:21:38_UTC-green)

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

**Latest saved flight:** 2026-04-14 20:21:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 20:21:38 UTC

- **34,724** saved flights
- **15,366** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,724** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **424,774.4 tonnes** estimated CO2 emissions
- **24,624,603 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1495 |
| 2 | SkyWest Airlines | 1388 |
| 3 | IndiGo | 870 |
| 4 | American Airlines | 598 |
| 5 | EJA | 596 |
| 6 | Southwest Airlines | 497 |
| 7 | ENY | 457 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 352 |
| 11 | LATAM Airlines | 345 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 308 |
| 14 | Delta Air Lines | 293 |
| 15 | QLK | 289 |
| 16 | LXJ | 278 |
| 17 | Swiss International | 264 |
| 18 | WIF | 254 |
| 19 | easyJet | 234 |
| 20 | AEE | 233 |
| 21 | Alaska Airlines | 233 |
| 22 | EJU | 231 |
| 23 | VIV | 224 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 199 |
| 26 | United Airlines | 195 |
| 27 | Air France | 193 |
| 28 | GLO | 187 |
| 29 | JetBlue | 184 |
| 30 | Avianca | 182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27264 |
| 2 | 🇮🇳 IN | 2660 |
| 3 | 🇪🇸 ES | 2616 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 2042 |
| 6 | 🇯🇵 JP | 1873 |
| 7 | 🇮🇹 IT | 1870 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1735 |
| 10 | 🇨🇦 CA | 1681 |
| 11 | 🇬🇧 GB | 1438 |
| 12 | 🇫🇷 FR | 1299 |
| 13 | 🇲🇽 MX | 1108 |
| 14 | 🇬🇷 GR | 1036 |
| 15 | 🇨🇭 CH | 958 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 823 |
| 18 | 🇳🇿 NZ | 728 |
| 19 | 🇿🇦 ZA | 726 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 637 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 612 |
| 24 | 🇰🇷 KR | 586 |
| 25 | 🇵🇱 PL | 550 |
| 26 | 🇲🇦 MA | 440 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 341 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 824 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 616 |
| 4 | Denver International Airport |  | US | 583 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 509 |
| 7 | Harry Reid International Airport |  | US | 458 |
| 8 | La Aurora Airport |  | GT | 448 |
| 9 | Guaymaral Airport |  | CO | 435 |
| 10 | Zurich Airport |  | CH | 431 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 356 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 350 |
| 13 | Chicago O'Hare International Airport |  | US | 346 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 318 |
| 19 | Charlotte/Douglas International Airport |  | US | 310 |
| 20 | Bengaluru International Airport |  | IN | 307 |
| 21 | Tenerife Norte Airport |  | ES | 306 |
| 22 | Congonhas Airport |  | BR | 302 |
| 23 | Ninoy Aquino International Airport |  | PH | 301 |
| 24 | Malpensa International Airport |  | IT | 283 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 271 |
| 26 | Salt Lake City International Airport |  | US | 264 |
| 27 | Daniel K Inouye International Airport |  | US | 263 |
| 28 | Capua Airport |  | IT | 260 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 247 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 243 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | Vitoria/Foronda Airport |  | ES | 232 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 231 |
| 37 | Barcelona International Airport |  | ES | 226 |
| 38 | Seattle-Tacoma International Airport |  | US | 217 |
| 39 | Miami International Airport |  | US | 216 |
| 40 | Viracopos International Airport |  | BR | 214 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 170 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 142 | 14m | 114 km | 278.5 t |
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
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 48 | 1h 20m | 961 km | 795.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N555KB |  | Sacramento Mather Airport (KMHR) | Yolo County Airport (KDWA) | 2026-04-14 19:40 UTC | 2026-04-14 20:21 UTC | 40m |
| N915KF |  | March Arb Airport (KRIV) | Hemet-Ryan Airport (KHMT) | 2026-04-14 20:01 UTC | 2026-04-14 20:20 UTC | 18m |
| LS30 |  | North Island Nas (Halsey Field) Airport (KNZY) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-04-14 19:34 UTC | 2026-04-14 20:17 UTC | 42m |
| CXK473 | CXK | San Bernardino International Airport (KSBD) | Hemet-Ryan Airport (KHMT) | 2026-04-14 19:46 UTC | 2026-04-14 20:05 UTC | 19m |
| N26ND |  | Deming Municipal Airport (KDMN) | Las Cruces International Airport (KLRU) | 2026-04-14 19:28 UTC | 2026-04-14 20:04 UTC | 36m |
| UPS99 | UPS | Incheon International Airport (RKSI) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-14 12:57 UTC | 2026-04-14 20:01 UTC | 7h 3m |
| N523PC |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-04-14 19:27 UTC | 2026-04-14 20:00 UTC | 33m |
| EJA523 | EJA | William P Hobby Airport (KHOU) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-14 19:14 UTC | 2026-04-14 19:57 UTC | 43m |
| N5014R |  | Mesa Gateway Airport (KIWA) | Deming Municipal Airport (KDMN) | 2026-04-14 18:11 UTC | 2026-04-14 19:53 UTC | 1h 42m |
| FDL50 | FDL | Republic Airport (KFRG) | K3C8 (K3C8) | 2026-04-14 19:06 UTC | 2026-04-14 19:45 UTC | 38m |
| FDJ268 | FDJ | Lawton-Fort Sill Regional Airport (KLAW) | Southeast Colorado Regional Airport (KLAA) | 2026-04-14 18:44 UTC | 2026-04-14 19:44 UTC | 59m |
| N7286E |  | Seldovia Airport (PASO) | Seldovia Airport (PASO) | 2026-04-14 19:29 UTC | 2026-04-14 19:43 UTC | 13m |
| N99HS |  | Brackett Field (KPOC) | Lake Havasu City Airport (KHII) | 2026-04-14 18:27 UTC | 2026-04-14 19:42 UTC | 1h 15m |
| N748MK |  | Lancaster Airport (KLNS) | Lehigh Valley International Airport (KABE) | 2026-04-14 19:05 UTC | 2026-04-14 19:39 UTC | 34m |
| N35325 |  | Glendale Regional Airport (KGEU) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-04-14 18:52 UTC | 2026-04-14 19:38 UTC | 45m |
| NOZ328 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Harstad/Narvik Airport Evenes (ENEV) | 2026-04-14 18:20 UTC | 2026-04-14 19:35 UTC | 1h 14m |
| RYR55HD | Ryanair | Edinburgh Airport (EGPH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-14 17:20 UTC | 2026-04-14 19:33 UTC | 2h 13m |
| LXJ5599 | LXJ | Scottsdale Airport (KSDL) | 1TE6 (1TE6) | 2026-04-14 18:27 UTC | 2026-04-14 19:31 UTC | 1h 3m |
| N46168 |  | Southerly Airport (58FD) | Winter Haven Regional Airport (KGIF) | 2026-04-14 19:13 UTC | 2026-04-14 19:30 UTC | 17m |
| KNG53 | KNG | RNZAF Base Ohakea (NZOH) | Molesworth Airport (NZML) | 2026-04-14 19:07 UTC | 2026-04-14 19:30 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
