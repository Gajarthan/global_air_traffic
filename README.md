# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_14:37:12_UTC-green)

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

**Latest saved flight:** 2026-04-20 14:37:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 14:37:12 UTC

- **45,123** saved flights
- **18,638** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **45,123** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **545,454.2 tonnes** estimated CO2 emissions
- **31,620,536 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1916 |
| 2 | SkyWest Airlines | 1744 |
| 3 | IndiGo | 1084 |
| 4 | EJA | 780 |
| 5 | American Airlines | 742 |
| 6 | Southwest Airlines | 643 |
| 7 | ENY | 585 |
| 8 | Lufthansa | 463 |
| 9 | AXM | 457 |
| 10 | Vueling | 454 |
| 11 | LATAM Airlines | 449 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 392 |
| 14 | Delta Air Lines | 382 |
| 15 | QLK | 366 |
| 16 | WIF | 355 |
| 17 | LXJ | 354 |
| 18 | Swiss International | 350 |
| 19 | AEE | 308 |
| 20 | Alaska Airlines | 308 |
| 21 | EJU | 299 |
| 22 | easyJet | 290 |
| 23 | VIV | 289 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 259 |
| 26 | United Airlines | 239 |
| 27 | AXB | 238 |
| 28 | JetBlue | 237 |
| 29 | Cathay Pacific | 235 |
| 30 | GLO | 234 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35563 |
| 2 | 🇮🇳 IN | 3363 |
| 3 | 🇪🇸 ES | 3327 |
| 4 | 🇦🇺 AU | 3131 |
| 5 | 🇧🇷 BR | 2680 |
| 6 | 🇯🇵 JP | 2486 |
| 7 | 🇮🇹 IT | 2423 |
| 8 | 🇩🇪 DE | 2324 |
| 9 | 🇨🇦 CA | 2184 |
| 10 | 🇨🇴 CO | 2075 |
| 11 | 🇬🇧 GB | 1844 |
| 12 | 🇫🇷 FR | 1722 |
| 13 | 🇲🇽 MX | 1407 |
| 14 | 🇬🇷 GR | 1392 |
| 15 | 🇨🇭 CH | 1244 |
| 16 | 🇳🇴 NO | 1129 |
| 17 | 🇲🇾 MY | 1122 |
| 18 | 🇿🇦 ZA | 952 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇵🇭 PH | 811 |
| 22 | 🇹🇷 TR | 797 |
| 23 | 🇰🇷 KR | 746 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 720 |
| 26 | 🇲🇦 MA | 562 |
| 27 | 🇲🇪 ME | 478 |
| 28 | 🇳🇱 NL | 460 |
| 29 | 🇲🇴 MO | 423 |
| 30 | 🇧🇸 BS | 413 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1053 |
| 2 | Tokyo International Airport |  | JP | 848 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | Indira Gandhi International Airport |  | IN | 727 |
| 5 | El Dorado International Airport |  | CO | 725 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 690 |
| 7 | Harry Reid International Airport |  | US | 582 |
| 8 | Guaymaral Airport |  | CO | 566 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 541 |
| 11 | Kuala Lumpur International Airport |  | MY | 448 |
| 12 | Chicago O'Hare International Airport |  | US | 443 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 435 |
| 15 | Frankfurt am Main International Airport |  | DE | 434 |
| 16 | Macau International Airport |  | MO | 423 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 421 |
| 18 | Madrid Barajas International Airport |  | ES | 405 |
| 19 | Bengaluru International Airport |  | IN | 399 |
| 20 | Tenerife Norte Airport |  | ES | 392 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Malpensa International Airport |  | IT | 386 |
| 23 | Congonhas Airport |  | BR | 383 |
| 24 | Ninoy Aquino International Airport |  | PH | 376 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 341 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 337 |
| 28 | Charles de Gaulle International Airport |  | FR | 335 |
| 29 | Daniel K Inouye International Airport |  | US | 334 |
| 30 | Capua Airport |  | IT | 321 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 312 |
| 32 | Reno/Tahoe International Airport |  | US | 311 |
| 33 | Vitoria/Foronda Airport |  | ES | 311 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 306 |
| 35 | O. R. Tambo International Airport |  | ZA | 305 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 303 |
| 37 | Barcelona International Airport |  | ES | 295 |
| 38 | Don Mueang International Airport |  | TH | 275 |
| 39 | Calgary International Airport |  | CA | 273 |
| 40 | Viracopos International Airport |  | BR | 273 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 228 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 168 | 14m | 114 km | 329.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 128 | 21m | 244 km | 539.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 122 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 104 | 26m | 275 km | 492.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 80 | 31m | 369 km | 509.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 76 | 20m | 250 km | 328.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 70 | 26m | 215 km | 259.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 66 | 13m | 99 km | 113.2 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 63 | 1h 52m | 1,304 km | 1,417.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 0m | 695 km | 743.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXAFJ | LXA | Bergerac-Roumaniere Airport (LFBE) | Biscarrosse Parentis Airport (LFBS) | 2026-04-20 14:04 UTC | 2026-04-20 14:37 UTC | 32m |
| N601BM |  | Hector International Airport (KFAR) | Lincoln Airport (KLNK) | 2026-04-20 11:46 UTC | 2026-04-20 14:36 UTC | 2h 49m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-20 14:19 UTC | 2026-04-20 14:32 UTC | 12m |
| DESRT159 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-20 14:10 UTC | 2026-04-20 14:30 UTC | 19m |
| N7159W |  | Arnold Palmer Regional Airport (KLBE) | Lancaster Airport (KLNS) | 2026-04-20 12:59 UTC | 2026-04-20 14:29 UTC | 1h 29m |
| N56849 |  | OI34 (OI34) | 79OI (79OI) | 2026-04-20 14:04 UTC | 2026-04-20 14:23 UTC | 19m |
| RNA402 | RNA | Suvarnabhumi Airport (VTBS) | Simara Airport (VNSI) | 2026-04-20 11:26 UTC | 2026-04-20 14:22 UTC | 2h 56m |
| AFL1688 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-20 07:05 UTC | 2026-04-20 14:21 UTC | 7h 16m |
| N98VL |  | Kenosha Regional Airport (KENW) | Burlington Municipal Airport (KBUU) | 2026-04-20 13:09 UTC | 2026-04-20 14:21 UTC | 1h 12m |
| N9232J |  | Griffiss International Airport (KRME) | Griffiss International Airport (KRME) | 2026-04-20 14:06 UTC | 2026-04-20 14:20 UTC | 13m |
| JUMP8 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-04-20 13:46 UTC | 2026-04-20 14:19 UTC | 33m |
| JAS81 | JAS | Teterboro Airport (KTEB) | Lehigh Valley International Airport (KABE) | 2026-04-20 13:58 UTC | 2026-04-20 14:19 UTC | 21m |
| CHH490 | CHH | Berlin Brandenburg Airport (EDDB) | Tunoshna Airport (UUDL) | 2026-04-20 12:07 UTC | 2026-04-20 14:17 UTC | 2h 10m |
| HK5178G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-20 13:34 UTC | 2026-04-20 14:10 UTC | 35m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-20 13:38 UTC | 2026-04-20 14:08 UTC | 29m |
| N2600L |  | Brown Field (46NC) | Brown Field (46NC) | 2026-04-20 14:06 UTC | 2026-04-20 14:06 UTC | 0m |
| N812KC |  | Midland International Air And Space Port Airport (KMAF) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-04-20 13:41 UTC | 2026-04-20 14:05 UTC | 23m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-20 13:06 UTC | 2026-04-20 14:04 UTC | 57m |
| N8243W |  | Felts Field (KSFF) | Pullman/Moscow Regional Airport (KPUW) | 2026-04-20 13:31 UTC | 2026-04-20 14:04 UTC | 33m |
| SHA228 | SHA | Jumla Airport (VNJL) | Simara Airport (VNSI) | 2026-04-20 12:57 UTC | 2026-04-20 14:01 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
