# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_23:27:08_UTC-green)

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

**Latest saved flight:** 2026-04-10 23:27:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 23:27:08 UTC

- **27,936** saved flights
- **13,141** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,936** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **340,086.4 tonnes** estimated CO2 emissions
- **19,715,156 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1149 |
| 2 | Ryanair | 1139 |
| 3 | IndiGo | 733 |
| 4 | EJA | 501 |
| 5 | American Airlines | 492 |
| 6 | Southwest Airlines | 402 |
| 7 | ENY | 380 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 283 |
| 11 | LATAM Airlines | 273 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 237 |
| 15 | AZU | 231 |
| 16 | LXJ | 231 |
| 17 | Swiss International | 196 |
| 18 | Alaska Airlines | 187 |
| 19 | VIV | 182 |
| 20 | easyJet | 181 |
| 21 | EJU | 179 |
| 22 | WIF | 179 |
| 23 | AEE | 178 |
| 24 | Japan Airlines | 177 |
| 25 | United Airlines | 169 |
| 26 | EDV | 166 |
| 27 | Avianca | 158 |
| 28 | JetBlue | 150 |
| 29 | AXB | 147 |
| 30 | PGT | 142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22265 |
| 2 | 🇮🇳 IN | 2250 |
| 3 | 🇪🇸 ES | 2047 |
| 4 | 🇦🇺 AU | 2006 |
| 5 | 🇧🇷 BR | 1580 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇨🇴 CO | 1399 |
| 8 | 🇮🇹 IT | 1399 |
| 9 | 🇩🇪 DE | 1392 |
| 10 | 🇨🇦 CA | 1372 |
| 11 | 🇬🇧 GB | 1120 |
| 12 | 🇫🇷 FR | 1024 |
| 13 | 🇲🇽 MX | 892 |
| 14 | 🇬🇷 GR | 799 |
| 15 | 🇨🇭 CH | 756 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 614 |
| 18 | 🇳🇴 NO | 605 |
| 19 | 🇿🇦 ZA | 567 |
| 20 | 🇬🇹 GT | 523 |
| 21 | 🇵🇭 PH | 516 |
| 22 | 🇹🇷 TR | 507 |
| 23 | 🇹🇭 TH | 481 |
| 24 | 🇰🇷 KR | 475 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 345 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 278 |
| 29 | 🇳🇱 NL | 270 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 672 |
| 2 | El Dorado International Airport |  | CO | 507 |
| 3 | Tokyo International Airport |  | JP | 500 |
| 4 | Denver International Airport |  | US | 476 |
| 5 | Indira Gandhi International Airport |  | IN | 466 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 389 |
| 7 | La Aurora Airport |  | GT | 369 |
| 8 | Harry Reid International Airport |  | US | 362 |
| 9 | Zurich Airport |  | CH | 327 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 296 |
| 12 | Chicago O'Hare International Airport |  | US | 291 |
| 13 | Frankfurt am Main International Airport |  | DE | 289 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 287 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 277 |
| 16 | Macau International Airport |  | MO | 261 |
| 17 | Charlotte/Douglas International Airport |  | US | 256 |
| 18 | Kuala Lumpur International Airport |  | MY | 254 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 239 |
| 21 | Madrid Barajas International Airport |  | ES | 237 |
| 22 | Tenerife Norte Airport |  | ES | 237 |
| 23 | Congonhas Airport |  | BR | 224 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 219 |
| 25 | Salt Lake City International Airport |  | US | 217 |
| 26 | Malpensa International Airport |  | IT | 216 |
| 27 | Daniel K Inouye International Airport |  | US | 215 |
| 28 | Reno/Tahoe International Airport |  | US | 206 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 192 |
| 31 | Miami International Airport |  | US | 189 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 187 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 185 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Seattle-Tacoma International Airport |  | US | 177 |
| 37 | Barcelona International Airport |  | ES | 175 |
| 38 | Capua Airport |  | IT | 175 |
| 39 | Vitoria/Foronda Airport |  | ES | 174 |
| 40 | Calgary International Airport |  | CA | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 113 | 14m | 114 km | 221.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 73 | 21m | 99 km | 125.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 50 | 52m | 556 km | 479.3 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 41 | 21m | 244 km | 172.6 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RDHK765 | RDH | Norfolk Ns (Chambers Field) Airport (KNGU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-10 22:38 UTC | 2026-04-10 23:27 UTC | 48m |
| ZFN | ZFN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-10 22:58 UTC | 2026-04-10 23:20 UTC | 21m |
| N960GV |  | Miami Executive Airport (KTMB) | Miami Homestead General Aviation Airport (KX51) | 2026-04-10 22:24 UTC | 2026-04-10 23:20 UTC | 55m |
| N865PC |  | Shreveport Regional Airport (KSHV) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-10 22:35 UTC | 2026-04-10 23:14 UTC | 38m |
| N8656J |  | Port Of Whitman Business Air Center Airport (KS94) | Port Of Whitman Business Air Center Airport (KS94) | 2026-04-10 23:10 UTC | 2026-04-10 23:12 UTC | 2m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-10 22:58 UTC | 2026-04-10 23:12 UTC | 14m |
| N9815P |  | AZ67 (AZ67) | AZ67 (AZ67) | 2026-04-10 22:40 UTC | 2026-04-10 23:12 UTC | 31m |
| ERU28 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-10 22:57 UTC | 2026-04-10 23:11 UTC | 13m |
| N407DV |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-10 23:01 UTC | 2026-04-10 23:05 UTC | 3m |
| VTM941 | VTM | Shreveport Regional Airport (KSHV) | Plan De Guadalupe International Airport (MMIO) | 2026-04-10 21:26 UTC | 2026-04-10 23:02 UTC | 1h 36m |
| ANVIL97 | ANV | Eastern Wv Regional/Shepherd Field (KMRB) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-10 22:30 UTC | 2026-04-10 22:57 UTC | 27m |
| TOG882 | TOG | North Texas Regional/Perrin Field (KGYI) | San Francisco International Airport (KSFO) | 2026-04-10 19:47 UTC | 2026-04-10 22:56 UTC | 3h 9m |
| CXK671 | CXK | Olive Branch/Taylor Field (KOLV) | Olive Branch/Taylor Field (KOLV) | 2026-04-10 22:44 UTC | 2026-04-10 22:52 UTC | 7m |
| N817WA |  | Fort Worth Meacham International Airport (KFTW) | Kerrville Municipal/Louis Schreiner Field (KERV) | 2026-04-10 21:58 UTC | 2026-04-10 22:51 UTC | 52m |
| CFMES | CFM | Calgary International Airport (CYYC) | Wetaskiwin Regional Airport (CEX3) | 2026-04-10 22:32 UTC | 2026-04-10 22:50 UTC | 17m |
| N1213S |  | Cortes Island (Hansen Airfield) Airport (CCI9) | Boeing Field/King County International Airport (KBFI) | 2026-04-10 21:32 UTC | 2026-04-10 22:48 UTC | 1h 15m |
| N800BD |  | Norman Y Mineta San Jose International Airport (KSJC) | 66CL (66CL) | 2026-04-10 22:30 UTC | 2026-04-10 22:46 UTC | 16m |
| BOV709 | BOV | Aeroclub Argentino Airport (SADS) | Laja Airport (SLLJ) | 2026-04-10 18:07 UTC | 2026-04-10 22:42 UTC | 4h 34m |
| SFY203 | SFY | Indian River Aerodrome (FL74) | Indian River Aerodrome (FL74) | 2026-04-10 22:39 UTC | 2026-04-10 22:39 UTC | 0m |
| NJM888 | NJM | Aiken Regional Airport (KAIK) | Witham Field (KSUA) | 2026-04-10 21:08 UTC | 2026-04-10 22:37 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
