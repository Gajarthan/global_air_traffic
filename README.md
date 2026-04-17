# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_17:57:24_UTC-green)

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

**Latest saved flight:** 2026-04-17 17:57:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 17:57:24 UTC

- **39,589** saved flights
- **16,964** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,589** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **477,228.4 tonnes** estimated CO2 emissions
- **27,665,415 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1665 |
| 2 | SkyWest Airlines | 1535 |
| 3 | IndiGo | 976 |
| 4 | EJA | 678 |
| 5 | American Airlines | 662 |
| 6 | Southwest Airlines | 552 |
| 7 | ENY | 507 |
| 8 | AXM | 413 |
| 9 | Vueling | 398 |
| 10 | LATAM Airlines | 392 |
| 11 | Lufthansa | 386 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 350 |
| 14 | Delta Air Lines | 336 |
| 15 | QLK | 327 |
| 16 | LXJ | 314 |
| 17 | WIF | 313 |
| 18 | Swiss International | 305 |
| 19 | AEE | 264 |
| 20 | Alaska Airlines | 262 |
| 21 | easyJet | 260 |
| 22 | EJU | 258 |
| 23 | VIV | 250 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 226 |
| 26 | United Airlines | 216 |
| 27 | EDV | 213 |
| 28 | JetBlue | 209 |
| 29 | GLO | 207 |
| 30 | AIQ | 202 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 31197 |
| 2 | 🇮🇳 IN | 2974 |
| 3 | 🇪🇸 ES | 2944 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2335 |
| 6 | 🇯🇵 JP | 2131 |
| 7 | 🇮🇹 IT | 2071 |
| 8 | 🇩🇪 DE | 2009 |
| 9 | 🇨🇦 CA | 1938 |
| 10 | 🇨🇴 CO | 1917 |
| 11 | 🇬🇧 GB | 1626 |
| 12 | 🇫🇷 FR | 1513 |
| 13 | 🇲🇽 MX | 1237 |
| 14 | 🇬🇷 GR | 1196 |
| 15 | 🇨🇭 CH | 1096 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 996 |
| 18 | 🇿🇦 ZA | 825 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 715 |
| 22 | 🇹🇷 TR | 699 |
| 23 | 🇬🇹 GT | 676 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 618 |
| 26 | 🇲🇦 MA | 490 |
| 27 | 🇳🇱 NL | 402 |
| 28 | 🇲🇪 ME | 393 |
| 29 | 🇧🇸 BS | 386 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 914 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 674 |
| 4 | Denver International Airport |  | US | 656 |
| 5 | Indira Gandhi International Airport |  | IN | 640 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 594 |
| 7 | Harry Reid International Airport |  | US | 513 |
| 8 | Guaymaral Airport |  | CO | 505 |
| 9 | La Aurora Airport |  | GT | 498 |
| 10 | Zurich Airport |  | CH | 482 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 390 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 388 |
| 14 | Chicago O'Hare International Airport |  | US | 383 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 362 |
| 17 | Madrid Barajas International Airport |  | ES | 357 |
| 18 | Tenerife Norte Airport |  | ES | 355 |
| 19 | Charlotte/Douglas International Airport |  | US | 353 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 346 |
| 22 | Congonhas Airport |  | BR | 344 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 320 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 306 |
| 26 | Salt Lake City International Airport |  | US | 301 |
| 27 | Daniel K Inouye International Airport |  | US | 293 |
| 28 | Charles de Gaulle International Airport |  | FR | 293 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 274 |
| 31 | Vitoria/Foronda Airport |  | ES | 271 |
| 32 | Capua Airport |  | IT | 271 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 265 |
| 34 | O. R. Tambo International Airport |  | ZA | 264 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 264 |
| 36 | Reno/Tahoe International Airport |  | US | 262 |
| 37 | Barcelona International Airport |  | ES | 255 |
| 38 | Viracopos International Airport |  | BR | 240 |
| 39 | Don Mueang International Airport |  | TH | 239 |
| 40 | Calgary International Airport |  | CA | 236 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 202 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 158 | 14m | 114 km | 309.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 101 | 21m | 244 km | 425.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 100 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 91 | 26m | 275 km | 431.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 83 | 21m | 99 km | 142.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 62 | 52m | 556 km | 594.3 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 60 | 26m | 215 km | 222.2 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 60 | 16m | 162 km | 168.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 55 | 1h 20m | 961 km | 911.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N492DS |  | KU77 (KU77) | KU77 (KU77) | 2026-04-17 17:36 UTC | 2026-04-17 17:57 UTC | 21m |
| N743TW |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-17 17:30 UTC | 2026-04-17 17:52 UTC | 21m |
| N984WU |  | Beaver County Airport (KBVI) | Beaver County Airport (KBVI) | 2026-04-17 17:23 UTC | 2026-04-17 17:52 UTC | 28m |
| TXH5708 | TXH | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-04-17 17:36 UTC | 2026-04-17 17:50 UTC | 13m |
| ASP812 | ASP | Vancouver International Airport (CYVR) | Calgary International Airport (CYYC) | 2026-04-17 16:48 UTC | 2026-04-17 17:48 UTC | 1h 0m |
| N712CA |  | PN69 (PN69) | Trenton Mercer Airport (KTTN) | 2026-04-17 16:50 UTC | 2026-04-17 17:48 UTC | 57m |
| EZS78KD | EZS | Geneva Cointrin International Airport (LSGG) | Taranto / Grottaglie Airport (LIBG) | 2026-04-17 16:18 UTC | 2026-04-17 17:47 UTC | 1h 29m |
| N6324K |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-04-17 17:12 UTC | 2026-04-17 17:43 UTC | 31m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-17 17:23 UTC | 2026-04-17 17:42 UTC | 18m |
| N14RD |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-17 17:27 UTC | 2026-04-17 17:40 UTC | 13m |
| N269DD |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-17 17:04 UTC | 2026-04-17 17:38 UTC | 33m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-04-17 16:54 UTC | 2026-04-17 17:38 UTC | 43m |
| N7418Y |  | Majors Airport (KGVT) | Flying Tiger Field (6TA2) | 2026-04-17 17:23 UTC | 2026-04-17 17:34 UTC | 11m |
| BOE791 | BOE | Renton Municipal Airport (KRNT) | Crown Creek Ranch Airport (57WA) | 2026-04-17 15:53 UTC | 2026-04-17 17:33 UTC | 1h 39m |
| HBSGT | HBS | Birrfeld Airport (LSZF) | Lommis Airfield (LSZT) | 2026-04-17 16:52 UTC | 2026-04-17 17:31 UTC | 38m |
| N45NS |  | Wayne County Airport (KBJJ) | Lehigh Valley International Airport (KABE) | 2026-04-17 16:39 UTC | 2026-04-17 17:29 UTC | 49m |
| N915KF |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-17 17:20 UTC | 2026-04-17 17:25 UTC | 5m |
| RYR161N | Ryanair | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-04-17 15:12 UTC | 2026-04-17 17:21 UTC | 2h 8m |
| TGNAT | TGN | Copan Ruinas Airport (MHRU) | La Aurora Airport (MGGT) | 2026-04-17 16:49 UTC | 2026-04-17 17:21 UTC | 32m |
| N784SP |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-17 16:49 UTC | 2026-04-17 17:21 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
