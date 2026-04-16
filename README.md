# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_11:19:14_UTC-green)

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

**Latest saved flight:** 2026-04-16 11:19:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 11:19:14 UTC

- **37,131** saved flights
- **16,091** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,131** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **450,166.2 tonnes** estimated CO2 emissions
- **26,096,591 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1576 |
| 2 | SkyWest Airlines | 1460 |
| 3 | IndiGo | 923 |
| 4 | EJA | 630 |
| 5 | American Airlines | 623 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 484 |
| 8 | AXM | 399 |
| 9 | Lufthansa | 385 |
| 10 | LATAM Airlines | 376 |
| 11 | Vueling | 372 |
| 12 | All Nippon Airways | 337 |
| 13 | AZU | 330 |
| 14 | Delta Air Lines | 314 |
| 15 | QLK | 313 |
| 16 | LXJ | 293 |
| 17 | Swiss International | 280 |
| 18 | WIF | 275 |
| 19 | AEE | 250 |
| 20 | Alaska Airlines | 247 |
| 21 | easyJet | 245 |
| 22 | EJU | 241 |
| 23 | VIV | 234 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 211 |
| 26 | EDV | 206 |
| 27 | United Airlines | 206 |
| 28 | AIQ | 197 |
| 29 | GLO | 196 |
| 30 | JetBlue | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29067 |
| 2 | 🇮🇳 IN | 2825 |
| 3 | 🇪🇸 ES | 2763 |
| 4 | 🇦🇺 AU | 2650 |
| 5 | 🇧🇷 BR | 2180 |
| 6 | 🇯🇵 JP | 2035 |
| 7 | 🇮🇹 IT | 1969 |
| 8 | 🇩🇪 DE | 1906 |
| 9 | 🇨🇦 CA | 1823 |
| 10 | 🇨🇴 CO | 1817 |
| 11 | 🇬🇧 GB | 1532 |
| 12 | 🇫🇷 FR | 1398 |
| 13 | 🇲🇽 MX | 1161 |
| 14 | 🇬🇷 GR | 1119 |
| 15 | 🇨🇭 CH | 1018 |
| 16 | 🇲🇾 MY | 958 |
| 17 | 🇳🇴 NO | 892 |
| 18 | 🇿🇦 ZA | 791 |
| 19 | 🇳🇿 NZ | 787 |
| 20 | 🇵🇭 PH | 700 |
| 21 | 🇹🇭 TH | 687 |
| 22 | 🇹🇷 TR | 669 |
| 23 | 🇰🇷 KR | 627 |
| 24 | 🇬🇹 GT | 626 |
| 25 | 🇵🇱 PL | 582 |
| 26 | 🇲🇦 MA | 467 |
| 27 | 🇳🇱 NL | 370 |
| 28 | 🇲🇪 ME | 366 |
| 29 | 🇧🇸 BS | 356 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 871 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 648 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 608 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 552 |
| 7 | Harry Reid International Airport |  | US | 484 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 452 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 12 | Kuala Lumpur International Airport |  | MY | 372 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 370 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Frankfurt am Main International Airport |  | DE | 344 |
| 17 | Macau International Airport |  | MO | 337 |
| 18 | Madrid Barajas International Airport |  | ES | 337 |
| 19 | Tenerife Norte Airport |  | ES | 332 |
| 20 | Charlotte/Douglas International Airport |  | US | 329 |
| 21 | Bengaluru International Airport |  | IN | 326 |
| 22 | Congonhas Airport |  | BR | 325 |
| 23 | Ninoy Aquino International Airport |  | PH | 324 |
| 24 | Malpensa International Airport |  | IT | 300 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 288 |
| 26 | Daniel K Inouye International Airport |  | US | 278 |
| 27 | Salt Lake City International Airport |  | US | 278 |
| 28 | Charles de Gaulle International Airport |  | FR | 276 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 263 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 263 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Reno/Tahoe International Airport |  | US | 255 |
| 33 | O. R. Tambo International Airport |  | ZA | 253 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 252 |
| 35 | Vitoria/Foronda Airport |  | ES | 245 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 37 | Barcelona International Airport |  | ES | 240 |
| 38 | Don Mueang International Airport |  | TH | 234 |
| 39 | Viracopos International Airport |  | BR | 230 |
| 40 | Seattle-Tacoma International Airport |  | US | 229 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 101 | 19m | 165 km | 287.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 95 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 89 | 21m | 244 km | 374.8 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 81 | 27m | 275 km | 383.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 55 | 1h 41m | 1,423 km | 1,349.8 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 55 | 16m | 162 km | 154.2 t |
| 27 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 53 | 26m | 215 km | 196.3 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NSZ2MP | NSZ | Nice-Cote d'Azur Airport (LFMN) | Stockholm-Arlanda Airport (ESSA) | 2026-04-16 08:43 UTC | 2026-04-16 11:19 UTC | 2h 35m |
| UAL1802 | United Airlines | Portland International Airport (KPDX) | Newark Liberty International Airport (KEWR) | 2026-04-16 06:28 UTC | 2026-04-16 11:14 UTC | 4h 46m |
| HBLVB | HBL | Bern Belp Airport (LSZB) | Friedrichshafen Airport (EDNY) | 2026-04-16 10:19 UTC | 2026-04-16 11:04 UTC | 44m |
|  |  | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Val-d'Or Airport (CYVO) | 2026-04-16 10:04 UTC | 2026-04-16 10:55 UTC | 50m |
| YEL1 | YEL | Harry Reid International Airport (KLAS) | Van Nuys Airport (KVNY) | 2026-04-16 10:07 UTC | 2026-04-16 10:47 UTC | 40m |
| HTY206 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-16 10:20 UTC | 2026-04-16 10:47 UTC | 26m |
| PHSVD | PHS | Eelde Airport (EHGG) | Eelde Airport (EHGG) | 2026-04-16 09:44 UTC | 2026-04-16 10:43 UTC | 58m |
| DRAGO03 | DRA | A 511 Airport (RKSG) | A 511 Airport (RKSG) | 2026-04-16 10:39 UTC | 2026-04-16 10:42 UTC | 3m |
| URSA05 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-16 09:16 UTC | 2026-04-16 10:38 UTC | 1h 22m |
| AFL1517 | AFL | Sochi International Airport (URSS) | Kimry Airport (UUEI) | 2026-04-15 20:13 UTC | 2026-04-16 10:34 UTC | 14h 21m |
| OEANN | OEA | Hohenems-Dornbirn Airport (LOIH) | Samedan Airport (LSZS) | 2026-04-16 09:48 UTC | 2026-04-16 10:31 UTC | 42m |
| SWR1792 | Swiss International | Zurich Airport (LSZH) | Luqa Airport (LMML) | 2026-04-16 08:32 UTC | 2026-04-16 10:31 UTC | 1h 59m |
| AIB77TN | AIB | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-04-16 09:59 UTC | 2026-04-16 10:31 UTC | 32m |
| EJU52HC | EJU | Amsterdam Airport Schiphol (EHAM) | Václav Havel Airport (LKPR) | 2026-04-16 09:23 UTC | 2026-04-16 10:31 UTC | 1h 7m |
| FDX1874 | FDX | Oakland San Francisco Bay Airport (KOAK) | Harry Reid International Airport (KLAS) | 2026-04-16 09:24 UTC | 2026-04-16 10:23 UTC | 58m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-16 09:58 UTC | 2026-04-16 10:18 UTC | 19m |
| AG204 |  | Seoul Air Base (RKSM) | G 417 Airport (RK34) | 2026-04-16 10:02 UTC | 2026-04-16 10:16 UTC | 13m |
| LHX6UW | LHX | Munich International Airport (EDDM) | Arad International Airport (LRAR) | 2026-04-16 09:14 UTC | 2026-04-16 10:15 UTC | 1h 0m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-16 09:02 UTC | 2026-04-16 10:12 UTC | 1h 9m |
| EJU9 | EJU | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-04-16 09:22 UTC | 2026-04-16 10:11 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
