# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_13:57:23_UTC-green)

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

**Latest saved flight:** 2026-04-17 13:57:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 13:57:23 UTC

- **38,958** saved flights
- **16,714** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,958** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **471,233.4 tonnes** estimated CO2 emissions
- **27,317,878 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1638 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 967 |
| 4 | EJA | 667 |
| 5 | American Airlines | 648 |
| 6 | Southwest Airlines | 536 |
| 7 | ENY | 500 |
| 8 | AXM | 413 |
| 9 | Vueling | 392 |
| 10 | LATAM Airlines | 389 |
| 11 | Lufthansa | 385 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 345 |
| 14 | QLK | 327 |
| 15 | Delta Air Lines | 326 |
| 16 | LXJ | 310 |
| 17 | WIF | 305 |
| 18 | Swiss International | 295 |
| 19 | AEE | 258 |
| 20 | Alaska Airlines | 258 |
| 21 | easyJet | 258 |
| 22 | EJU | 254 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 219 |
| 26 | EDV | 212 |
| 27 | United Airlines | 212 |
| 28 | AIQ | 201 |
| 29 | GLO | 201 |
| 30 | AXB | 200 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30544 |
| 2 | 🇮🇳 IN | 2951 |
| 3 | 🇪🇸 ES | 2904 |
| 4 | 🇦🇺 AU | 2783 |
| 5 | 🇧🇷 BR | 2281 |
| 6 | 🇯🇵 JP | 2128 |
| 7 | 🇮🇹 IT | 2047 |
| 8 | 🇩🇪 DE | 1985 |
| 9 | 🇨🇦 CA | 1909 |
| 10 | 🇨🇴 CO | 1901 |
| 11 | 🇬🇧 GB | 1604 |
| 12 | 🇫🇷 FR | 1485 |
| 13 | 🇲🇽 MX | 1217 |
| 14 | 🇬🇷 GR | 1173 |
| 15 | 🇨🇭 CH | 1071 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 971 |
| 18 | 🇿🇦 ZA | 811 |
| 19 | 🇳🇿 NZ | 809 |
| 20 | 🇵🇭 PH | 720 |
| 21 | 🇹🇭 TH | 713 |
| 22 | 🇹🇷 TR | 694 |
| 23 | 🇬🇹 GT | 657 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 610 |
| 26 | 🇲🇦 MA | 483 |
| 27 | 🇳🇱 NL | 396 |
| 28 | 🇲🇪 ME | 387 |
| 29 | 🇧🇸 BS | 374 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 727 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 650 |
| 5 | Indira Gandhi International Airport |  | IN | 636 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 582 |
| 7 | Harry Reid International Airport |  | US | 508 |
| 8 | Guaymaral Airport |  | CO | 496 |
| 9 | La Aurora Airport |  | GT | 484 |
| 10 | Zurich Airport |  | CH | 470 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 15 | Chicago O'Hare International Airport |  | US | 374 |
| 16 | Macau International Airport |  | MO | 362 |
| 17 | Madrid Barajas International Airport |  | ES | 353 |
| 18 | Tenerife Norte Airport |  | ES | 352 |
| 19 | Frankfurt am Main International Airport |  | DE | 349 |
| 20 | Charlotte/Douglas International Airport |  | US | 344 |
| 21 | Bengaluru International Airport |  | IN | 342 |
| 22 | Congonhas Airport |  | BR | 339 |
| 23 | Ninoy Aquino International Airport |  | PH | 334 |
| 24 | Malpensa International Airport |  | IT | 318 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 293 |
| 27 | Daniel K Inouye International Airport |  | US | 289 |
| 28 | Charles de Gaulle International Airport |  | FR | 286 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 285 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 272 |
| 31 | Vitoria/Foronda Airport |  | ES | 267 |
| 32 | Capua Airport |  | IT | 263 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 261 |
| 34 | O. R. Tambo International Airport |  | ZA | 260 |
| 35 | Reno/Tahoe International Airport |  | US | 258 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 254 |
| 37 | Barcelona International Airport |  | ES | 252 |
| 38 | Don Mueang International Airport |  | TH | 239 |
| 39 | Viracopos International Airport |  | BR | 237 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 198 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 99 | 21m | 244 km | 416.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 96 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 90 | 26m | 275 km | 426.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 60 | 1h 41m | 1,423 km | 1,472.5 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 59 | 26m | 215 km | 218.5 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 59 | 16m | 162 km | 165.4 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 57 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 54 | 1h 21m | 961 km | 895.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N888HB |  | Hog Air Aviation Inc Airport (3AR9) | Kirk Field (KPGR) | 2026-04-17 13:45 UTC | 2026-04-17 13:57 UTC | 11m |
| GARDN1 | GAR | College Park Airport (KCGS) | Fairview Airport (3MD4) | 2026-04-17 12:42 UTC | 2026-04-17 13:47 UTC | 1h 5m |
| N380AU |  | Auburn University Regional Airport (KAUO) | Lagrange/Callaway Airport (KLGC) | 2026-04-17 12:30 UTC | 2026-04-17 13:36 UTC | 1h 5m |
| EJU84ZE | EJU | Palma De Mallorca Airport (LEPA) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-17 12:25 UTC | 2026-04-17 13:33 UTC | 1h 7m |
| N272LP |  | Essex County Airport (KCDW) | NK07 (NK07) | 2026-04-17 12:45 UTC | 2026-04-17 13:32 UTC | 47m |
| ACA748 | Air Canada | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 12:37 UTC | 2026-04-17 13:32 UTC | 54m |
| HSOMR2 | HSO | Emden Airport (EDWE) | Juist Airport (EDWJ) | 2026-04-17 13:08 UTC | 2026-04-17 13:30 UTC | 22m |
| N491LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-17 12:16 UTC | 2026-04-17 13:30 UTC | 1h 14m |
| CXK643 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-04-17 12:20 UTC | 2026-04-17 13:25 UTC | 1h 5m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-04-17 12:52 UTC | 2026-04-17 13:24 UTC | 31m |
| ATG7750 | ATG | OM11 (OM11) | Macau International Airport (VMMC) | 2026-04-17 07:10 UTC | 2026-04-17 13:24 UTC | 6h 13m |
| NJE376V | NJE | Geneva Cointrin International Airport (LSGG) | Lyon-Bron Airport (LFLY) | 2026-04-17 12:54 UTC | 2026-04-17 13:23 UTC | 29m |
| DEFTD | DEF | Aschaffenburg Airport (EDFC) | Aschaffenburg Airport (EDFC) | 2026-04-17 12:45 UTC | 2026-04-17 13:23 UTC | 37m |
| FHNCJ | FHN | Brienne-le-Chateau Airport (LFFN) | Brienne-le-Chateau Airport (LFFN) | 2026-04-17 13:14 UTC | 2026-04-17 13:21 UTC | 7m |
| AAY1878 | AAY | Asheville Regional Airport (KAVL) | Riconn Airport (RI11) | 2026-04-17 11:08 UTC | 2026-04-17 13:20 UTC | 2h 12m |
| WIRE31 | WIR | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-04-17 12:56 UTC | 2026-04-17 13:19 UTC | 23m |
| BRU989 | BRU | Gomel Airport (UMGG) | Smolensk North Airport (XUBS) | 2026-04-17 12:47 UTC | 2026-04-17 13:18 UTC | 31m |
| EZY67PB | easyJet | Belfast International Airport (EGAA) | Liverpool John Lennon Airport (EGGP) | 2026-04-17 12:40 UTC | 2026-04-17 13:18 UTC | 37m |
| N288SF |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-17 12:54 UTC | 2026-04-17 13:18 UTC | 24m |
| AIP1856 | AIP | Denver International Airport (KDEN) | Mc Elroy Airfield (K20V) | 2026-04-17 12:47 UTC | 2026-04-17 13:16 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
