# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_06:50:19_UTC-green)

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

**Latest saved flight:** 2026-04-16 06:50:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 06:50:19 UTC

- **36,950** saved flights
- **16,055** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,950** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **447,760.4 tonnes** estimated CO2 emissions
- **25,957,124 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1567 |
| 2 | SkyWest Airlines | 1460 |
| 3 | IndiGo | 916 |
| 4 | EJA | 630 |
| 5 | American Airlines | 623 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 484 |
| 8 | AXM | 395 |
| 9 | Lufthansa | 384 |
| 10 | LATAM Airlines | 374 |
| 11 | Vueling | 370 |
| 12 | All Nippon Airways | 331 |
| 13 | AZU | 327 |
| 14 | Delta Air Lines | 313 |
| 15 | QLK | 311 |
| 16 | LXJ | 293 |
| 17 | Swiss International | 277 |
| 18 | WIF | 273 |
| 19 | AEE | 247 |
| 20 | Alaska Airlines | 247 |
| 21 | easyJet | 242 |
| 22 | EJU | 238 |
| 23 | VIV | 234 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 208 |
| 26 | EDV | 206 |
| 27 | United Airlines | 205 |
| 28 | GLO | 196 |
| 29 | AIQ | 194 |
| 30 | JetBlue | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29048 |
| 2 | 🇮🇳 IN | 2800 |
| 3 | 🇪🇸 ES | 2735 |
| 4 | 🇦🇺 AU | 2636 |
| 5 | 🇧🇷 BR | 2170 |
| 6 | 🇯🇵 JP | 2008 |
| 7 | 🇮🇹 IT | 1961 |
| 8 | 🇩🇪 DE | 1890 |
| 9 | 🇨🇦 CA | 1819 |
| 10 | 🇨🇴 CO | 1817 |
| 11 | 🇬🇧 GB | 1511 |
| 12 | 🇫🇷 FR | 1389 |
| 13 | 🇲🇽 MX | 1161 |
| 14 | 🇬🇷 GR | 1112 |
| 15 | 🇨🇭 CH | 1005 |
| 16 | 🇲🇾 MY | 946 |
| 17 | 🇳🇴 NO | 886 |
| 18 | 🇳🇿 NZ | 787 |
| 19 | 🇿🇦 ZA | 776 |
| 20 | 🇵🇭 PH | 694 |
| 21 | 🇹🇭 TH | 680 |
| 22 | 🇹🇷 TR | 666 |
| 23 | 🇬🇹 GT | 626 |
| 24 | 🇰🇷 KR | 619 |
| 25 | 🇵🇱 PL | 577 |
| 26 | 🇲🇦 MA | 465 |
| 27 | 🇳🇱 NL | 365 |
| 28 | 🇲🇪 ME | 358 |
| 29 | 🇧🇸 BS | 356 |
| 30 | 🇮🇩 ID | 348 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 871 |
| 2 | Tokyo International Airport |  | JP | 683 |
| 3 | El Dorado International Airport |  | CO | 648 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 602 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 547 |
| 7 | Harry Reid International Airport |  | US | 482 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 369 |
| 13 | Kuala Lumpur International Airport |  | MY | 368 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 358 |
| 16 | Frankfurt am Main International Airport |  | DE | 342 |
| 17 | Macau International Airport |  | MO | 337 |
| 18 | Madrid Barajas International Airport |  | ES | 334 |
| 19 | Charlotte/Douglas International Airport |  | US | 329 |
| 20 | Tenerife Norte Airport |  | ES | 325 |
| 21 | Bengaluru International Airport |  | IN | 325 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 321 |
| 24 | Malpensa International Airport |  | IT | 299 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 288 |
| 26 | Daniel K Inouye International Airport |  | US | 278 |
| 27 | Salt Lake City International Airport |  | US | 278 |
| 28 | Charles de Gaulle International Airport |  | FR | 273 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 261 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 260 |
| 32 | Reno/Tahoe International Airport |  | US | 255 |
| 33 | O. R. Tambo International Airport |  | ZA | 249 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 249 |
| 35 | Vitoria/Foronda Airport |  | ES | 243 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Don Mueang International Airport |  | TH | 231 |
| 39 | Viracopos International Airport |  | BR | 230 |
| 40 | Seattle-Tacoma International Airport |  | US | 228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 172 | 1h 8m | 706 km | 2,094.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 135 | 24m | 225 km | 523.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 108 | 1h 27m | 910 km | 1,694.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 99 | 19m | 165 km | 281.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 93 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 89 | 21m | 244 km | 374.8 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 81 | 27m | 275 km | 383.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 81 | 54m | 546 km | 762.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 70 | 45m | 452 km | 545.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 70 | 31m | 369 km | 445.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 55 | 1h 41m | 1,423 km | 1,349.8 t |
| 26 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 53 | 26m | 215 km | 196.3 t |
| 27 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 28 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZUW | HBZ | Megeve Airport (LFHM) | Sion Airport (LSGS) | 2026-04-16 06:40 UTC | 2026-04-16 06:50 UTC | 10m |
| DMLED | DML | Leutkirch-Unterzeil Airport (EDNL) | Schweinfurt-Sud Airport (EDFS) | 2026-04-16 05:50 UTC | 2026-04-16 06:47 UTC | 57m |
| HLF8868 | HLF | Leipzig Halle Airport (EDDP) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-04-15 19:41 UTC | 2026-04-16 06:29 UTC | 10h 48m |
| HAENK | HAE | Debrecen International Airport (LHDC) | Debrecen International Airport (LHDC) | 2026-04-16 05:49 UTC | 2026-04-16 06:20 UTC | 31m |
| BTN773 | BTN | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-16 04:05 UTC | 2026-04-16 06:17 UTC | 2h 12m |
| TWY94 | TWY | El Platanar Airport (MSPT) | Washington Dulles International Airport (KIAD) | 2026-04-16 02:41 UTC | 2026-04-16 06:17 UTC | 3h 35m |
| QLK164D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Port Macquarie Airport (YPMQ) | 2026-04-16 05:39 UTC | 2026-04-16 06:16 UTC | 36m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-04-16 05:44 UTC | 2026-04-16 06:06 UTC | 21m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-16 05:40 UTC | 2026-04-16 06:04 UTC | 24m |
| LIFELN2 | LIF | EHND (EHND) | Rotterdam Airport (EHRD) | 2026-04-16 05:54 UTC | 2026-04-16 06:03 UTC | 8m |
| LOT9MA | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Szczecin-Goleniow Solidarność Airport (EPSC) | 2026-04-16 05:17 UTC | 2026-04-16 06:02 UTC | 45m |
| QLK42D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-16 05:32 UTC | 2026-04-16 06:00 UTC | 28m |
| PY7003 |  | Perth International Airport (YPPH) | Leonora Airport (YLEO) | 2026-04-16 05:06 UTC | 2026-04-16 05:59 UTC | 52m |
| IGO5LM | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-04-16 05:17 UTC | 2026-04-16 05:57 UTC | 39m |
| VOI3296 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-16 03:07 UTC | 2026-04-16 05:56 UTC | 2h 49m |
| IGO5025 | IndiGo | Indira Gandhi International Airport (VIDP) | Sidhi Airport (VA1F) | 2026-04-16 05:07 UTC | 2026-04-16 05:55 UTC | 48m |
| IGO497 | IndiGo | Bengaluru International Airport (VOBL) | Ambala Air Force Station (VIAM) | 2026-04-16 02:27 UTC | 2026-04-16 05:53 UTC | 3h 25m |
| AWG672P | AWG | Henri Coanda International Airport (LROP) | Václav Havel Airport (LKPR) | 2026-04-16 04:17 UTC | 2026-04-16 05:52 UTC | 1h 35m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-16 05:25 UTC | 2026-04-16 05:48 UTC | 22m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-16 05:28 UTC | 2026-04-16 05:44 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
