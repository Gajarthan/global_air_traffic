# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_10:05:23_UTC-green)

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

**Latest saved flight:** 2026-04-15 10:05:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 10:05:23 UTC

- **35,429** saved flights
- **15,571** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,429** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **431,714.0 tonnes** estimated CO2 emissions
- **25,026,898 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1514 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 883 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 469 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 378 |
| 10 | Vueling | 358 |
| 11 | LATAM Airlines | 353 |
| 12 | All Nippon Airways | 318 |
| 13 | AZU | 315 |
| 14 | QLK | 302 |
| 15 | Delta Air Lines | 301 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 270 |
| 18 | WIF | 258 |
| 19 | AEE | 239 |
| 20 | Alaska Airlines | 237 |
| 21 | easyJet | 235 |
| 22 | EJU | 231 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 219 |
| 25 | EDV | 201 |
| 26 | United Airlines | 199 |
| 27 | Air France | 197 |
| 28 | GLO | 192 |
| 29 | JetBlue | 187 |
| 30 | Avianca | 184 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27765 |
| 2 | 🇮🇳 IN | 2701 |
| 3 | 🇪🇸 ES | 2638 |
| 4 | 🇦🇺 AU | 2528 |
| 5 | 🇧🇷 BR | 2082 |
| 6 | 🇯🇵 JP | 1934 |
| 7 | 🇮🇹 IT | 1899 |
| 8 | 🇩🇪 DE | 1807 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1726 |
| 11 | 🇬🇧 GB | 1458 |
| 12 | 🇫🇷 FR | 1317 |
| 13 | 🇲🇽 MX | 1132 |
| 14 | 🇬🇷 GR | 1061 |
| 15 | 🇨🇭 CH | 974 |
| 16 | 🇲🇾 MY | 910 |
| 17 | 🇳🇴 NO | 837 |
| 18 | 🇳🇿 NZ | 771 |
| 19 | 🇿🇦 ZA | 740 |
| 20 | 🇵🇭 PH | 680 |
| 21 | 🇹🇭 TH | 641 |
| 22 | 🇹🇷 TR | 640 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 607 |
| 25 | 🇵🇱 PL | 556 |
| 26 | 🇲🇦 MA | 442 |
| 27 | 🇳🇱 NL | 348 |
| 28 | 🇲🇪 ME | 347 |
| 29 | 🇧🇸 BS | 346 |
| 30 | 🇮🇩 ID | 339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 657 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 573 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 523 |
| 7 | Harry Reid International Airport |  | US | 467 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 438 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 13 | Chicago O'Hare International Airport |  | US | 355 |
| 14 | Kuala Lumpur International Airport |  | MY | 351 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 343 |
| 16 | Frankfurt am Main International Airport |  | DE | 334 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Charlotte/Douglas International Airport |  | US | 319 |
| 19 | Madrid Barajas International Airport |  | ES | 319 |
| 20 | Ninoy Aquino International Airport |  | PH | 314 |
| 21 | Bengaluru International Airport |  | IN | 314 |
| 22 | Congonhas Airport |  | BR | 309 |
| 23 | Tenerife Norte Airport |  | ES | 308 |
| 24 | Malpensa International Airport |  | IT | 289 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 281 |
| 26 | Salt Lake City International Airport |  | US | 270 |
| 27 | Daniel K Inouye International Airport |  | US | 269 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 261 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 248 |
| 31 | Reno/Tahoe International Airport |  | US | 247 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 243 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 243 |
| 34 | O. R. Tambo International Airport |  | ZA | 238 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 234 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 223 |
| 39 | Viracopos International Airport |  | BR | 221 |
| 40 | Miami International Airport |  | US | 219 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 166 | 1h 8m | 706 km | 2,021.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 101 | 1h 27m | 910 km | 1,584.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 93 | 19m | 165 km | 264.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 90 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 84 | 21m | 244 km | 353.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 74 | 1h 12m | 770 km | 983.0 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 68 | 31m | 369 km | 432.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 67 | 45m | 452 km | 522.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 58 | 20m | 147 km | 146.8 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 53 | 14m | 154 km | 140.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGSBC | FGS | Moret Episy Airport (LFPU) | Pont Sur Yonne Airport (LFGO) | 2026-04-15 09:35 UTC | 2026-04-15 10:05 UTC | 29m |
| HBZUO | HBZ | Courchevel Airport (LFLJ) | Raron Airport (LSTA) | 2026-04-15 05:20 UTC | 2026-04-15 10:05 UTC | 4h 44m |
| RYR8493 | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-04-15 09:46 UTC | 2026-04-15 09:59 UTC | 13m |
| KAL299T | Korean Air | Gimpo International Airport (RKSS) | Gimpo International Airport (RKSS) | 2026-04-15 09:40 UTC | 2026-04-15 09:59 UTC | 18m |
| AWH123 | AWH | Munster Osnabruck Airport (EDDG) | Munster Osnabruck Airport (EDDG) | 2026-04-15 09:25 UTC | 2026-04-15 09:53 UTC | 28m |
| ARCTS41 | ARC | Celle Airport (ETHC) | Celle Airport (ETHC) | 2026-04-15 08:24 UTC | 2026-04-15 09:52 UTC | 1h 28m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-15 09:06 UTC | 2026-04-15 09:49 UTC | 43m |
| DLA9800 | DLA | Trieste / Ronchi Dei Legionari (LIPQ) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-15 09:13 UTC | 2026-04-15 09:45 UTC | 31m |
| EIN66V | Aer Lingus | Dublin Airport (EIDW) | Vienna International Airport (LOWW) | 2026-04-15 06:31 UTC | 2026-04-15 09:41 UTC | 3h 10m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-04-15 09:13 UTC | 2026-04-15 09:41 UTC | 27m |
| FHXCB | FHX | Caen-Carpiquet Airport (LFRK) | Caen-Carpiquet Airport (LFRK) | 2026-04-15 09:37 UTC | 2026-04-15 09:39 UTC | 1m |
| LUA10T | LUA | Hamburg Airport (EDDH) | Nordholz Airport (ETMN) | 2026-04-15 09:16 UTC | 2026-04-15 09:38 UTC | 22m |
| RYR466M | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-15 07:44 UTC | 2026-04-15 09:36 UTC | 1h 52m |
| JST798 | JST | Melbourne International Airport (YMML) | Sunshine Coast Airport (YBMC) | 2026-04-15 07:41 UTC | 2026-04-15 09:30 UTC | 1h 48m |
| NOZ52K | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-15 08:47 UTC | 2026-04-15 09:24 UTC | 37m |
| HSOVJ2 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-15 08:57 UTC | 2026-04-15 09:24 UTC | 26m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-04-15 08:29 UTC | 2026-04-15 09:22 UTC | 53m |
| RYR8493 | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-04-15 09:06 UTC | 2026-04-15 09:22 UTC | 16m |
| IGO941 | IndiGo | Bengaluru International Airport (VOBL) | Agra Airport (VIAG) | 2026-04-15 07:22 UTC | 2026-04-15 09:21 UTC | 1h 59m |
| OAL012 | OAL | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-15 08:55 UTC | 2026-04-15 09:20 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
