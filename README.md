# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_11:22:23_UTC-green)

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

**Latest saved flight:** 2026-04-17 11:22:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 11:22:23 UTC

- **38,826** saved flights
- **16,670** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,826** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **469,365.0 tonnes** estimated CO2 emissions
- **27,209,564 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1632 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 961 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 412 |
| 9 | Vueling | 391 |
| 10 | LATAM Airlines | 388 |
| 11 | Lufthansa | 385 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 345 |
| 14 | QLK | 327 |
| 15 | Delta Air Lines | 326 |
| 16 | LXJ | 309 |
| 17 | WIF | 297 |
| 18 | Swiss International | 293 |
| 19 | AEE | 258 |
| 20 | Alaska Airlines | 258 |
| 21 | easyJet | 256 |
| 22 | EJU | 251 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 218 |
| 26 | EDV | 212 |
| 27 | United Airlines | 212 |
| 28 | AIQ | 201 |
| 29 | GLO | 201 |
| 30 | AXB | 200 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30459 |
| 2 | 🇮🇳 IN | 2941 |
| 3 | 🇪🇸 ES | 2893 |
| 4 | 🇦🇺 AU | 2781 |
| 5 | 🇧🇷 BR | 2277 |
| 6 | 🇯🇵 JP | 2128 |
| 7 | 🇮🇹 IT | 2039 |
| 8 | 🇩🇪 DE | 1976 |
| 9 | 🇨🇦 CA | 1905 |
| 10 | 🇨🇴 CO | 1899 |
| 11 | 🇬🇧 GB | 1596 |
| 12 | 🇫🇷 FR | 1472 |
| 13 | 🇲🇽 MX | 1217 |
| 14 | 🇬🇷 GR | 1173 |
| 15 | 🇨🇭 CH | 1065 |
| 16 | 🇲🇾 MY | 1001 |
| 17 | 🇳🇴 NO | 953 |
| 18 | 🇿🇦 ZA | 809 |
| 19 | 🇳🇿 NZ | 809 |
| 20 | 🇵🇭 PH | 720 |
| 21 | 🇹🇭 TH | 711 |
| 22 | 🇹🇷 TR | 693 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 608 |
| 26 | 🇲🇦 MA | 482 |
| 27 | 🇳🇱 NL | 394 |
| 28 | 🇲🇪 ME | 385 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 727 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 648 |
| 5 | Indira Gandhi International Airport |  | IN | 634 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 582 |
| 7 | Harry Reid International Airport |  | US | 507 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 468 |
| 11 | Kuala Lumpur International Airport |  | MY | 393 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 378 |
| 15 | Chicago O'Hare International Airport |  | US | 373 |
| 16 | Macau International Airport |  | MO | 355 |
| 17 | Madrid Barajas International Airport |  | ES | 353 |
| 18 | Tenerife Norte Airport |  | ES | 350 |
| 19 | Frankfurt am Main International Airport |  | DE | 349 |
| 20 | Charlotte/Douglas International Airport |  | US | 343 |
| 21 | Bengaluru International Airport |  | IN | 341 |
| 22 | Congonhas Airport |  | BR | 338 |
| 23 | Ninoy Aquino International Airport |  | PH | 334 |
| 24 | Malpensa International Airport |  | IT | 315 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 293 |
| 27 | Daniel K Inouye International Airport |  | US | 288 |
| 28 | Charles de Gaulle International Airport |  | FR | 285 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 282 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 31 | Vitoria/Foronda Airport |  | ES | 265 |
| 32 | Capua Airport |  | IT | 262 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 260 |
| 34 | O. R. Tambo International Airport |  | ZA | 259 |
| 35 | Reno/Tahoe International Airport |  | US | 257 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 252 |
| 38 | Don Mueang International Airport |  | TH | 239 |
| 39 | Viracopos International Airport |  | BR | 237 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 104 | 19m | 165 km | 295.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 98 | 21m | 244 km | 412.7 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
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
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 59 | 1h 41m | 1,423 km | 1,448.0 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 59 | 16m | 162 km | 165.4 t |
| 25 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 26 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 57 | 26m | 215 km | 211.1 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 56 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 30 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N812DA |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-17 11:03 UTC | 2026-04-17 11:22 UTC | 19m |
| UAL2303 | United Airlines | Los Angeles International Airport (KLAX) | Newark Liberty International Airport (KEWR) | 2026-04-17 07:00 UTC | 2026-04-17 11:20 UTC | 4h 19m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-04-17 10:59 UTC | 2026-04-17 11:10 UTC | 11m |
| SCPTR1 | SCP | RAF Cranwell (EGYD) | EGYI (EGYI) | 2026-04-17 09:50 UTC | 2026-04-17 10:42 UTC | 52m |
| RYR8V | Ryanair | Sandefjord Airport Torp (ENTO) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-17 08:56 UTC | 2026-04-17 10:34 UTC | 1h 37m |
| OKOVA | OKO | Mnichovo Hradiste Airport (LKMH) | Mnichovo Hradiste Airport (LKMH) | 2026-04-17 10:00 UTC | 2026-04-17 10:33 UTC | 32m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-04-17 09:33 UTC | 2026-04-17 10:29 UTC | 56m |
| RYR484F | Ryanair | London Stansted Airport (EGSS) | La Roche-sur-Yon Airport (LFRI) | 2026-04-17 09:32 UTC | 2026-04-17 10:26 UTC | 53m |
| PHKLM | PHK | Teuge Airport (EHTE) | Hoogeveen Airport (EHHO) | 2026-04-17 10:08 UTC | 2026-04-17 10:25 UTC | 16m |
| HAKAR | HAK | Belgrade Nikola Tesla Airport (LYBE) | Visoko Sport Airfield (LQVI) | 2026-04-17 09:51 UTC | 2026-04-17 10:20 UTC | 29m |
| FNA570 | FNA | Reykjavik Airport (BIRK) | Grundarfjörður Airport (BIGF) | 2026-04-17 09:59 UTC | 2026-04-17 10:17 UTC | 18m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-17 09:46 UTC | 2026-04-17 10:15 UTC | 28m |
| EWG3PV | EWG | Palma De Mallorca Airport (LEPA) | Dusseldorf International Airport (EDDL) | 2026-04-17 08:09 UTC | 2026-04-17 10:14 UTC | 2h 5m |
| TRA62U | TRA | Barcelona International Airport (LEBL) | Rotterdam Airport (EHRD) | 2026-04-17 08:25 UTC | 2026-04-17 10:14 UTC | 1h 48m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-04-17 09:23 UTC | 2026-04-17 10:12 UTC | 48m |
| BNOB | BNO | Bodø Airport (ENBO) | Røst Airport (ENRS) | 2026-04-17 09:57 UTC | 2026-04-17 10:10 UTC | 13m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-17 09:48 UTC | 2026-04-17 10:10 UTC | 21m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-17 08:55 UTC | 2026-04-17 10:09 UTC | 1h 13m |
| EZY59ZF | easyJet | London Gatwick Airport (EGKK) | Santorini Airport (LGSR) | 2026-04-17 06:51 UTC | 2026-04-17 10:06 UTC | 3h 15m |
| CTV992 | CTV | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-04-17 09:50 UTC | 2026-04-17 10:06 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
