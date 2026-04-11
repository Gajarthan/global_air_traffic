# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_09:40:51_UTC-green)

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

**Latest saved flight:** 2026-04-11 09:40:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 09:40:51 UTC

- **28,361** saved flights
- **13,271** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,361** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **344,566.1 tonnes** estimated CO2 emissions
- **19,974,845 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1155 |
| 2 | Ryanair | 1154 |
| 3 | IndiGo | 745 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 345 |
| 9 | AXM | 299 |
| 10 | Vueling | 289 |
| 11 | LATAM Airlines | 275 |
| 12 | All Nippon Airways | 258 |
| 13 | QLK | 254 |
| 14 | Delta Air Lines | 240 |
| 15 | AZU | 235 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 203 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 186 |
| 20 | EJU | 183 |
| 21 | VIV | 183 |
| 22 | easyJet | 182 |
| 23 | WIF | 181 |
| 24 | AEE | 180 |
| 25 | United Airlines | 173 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | JetBlue | 150 |
| 29 | AXB | 148 |
| 30 | PGT | 144 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22457 |
| 2 | 🇮🇳 IN | 2294 |
| 3 | 🇦🇺 AU | 2080 |
| 4 | 🇪🇸 ES | 2076 |
| 5 | 🇧🇷 BR | 1595 |
| 6 | 🇯🇵 JP | 1568 |
| 7 | 🇮🇹 IT | 1428 |
| 8 | 🇩🇪 DE | 1416 |
| 9 | 🇨🇴 CO | 1407 |
| 10 | 🇨🇦 CA | 1393 |
| 11 | 🇬🇧 GB | 1134 |
| 12 | 🇫🇷 FR | 1041 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 818 |
| 15 | 🇨🇭 CH | 782 |
| 16 | 🇲🇾 MY | 717 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 610 |
| 19 | 🇿🇦 ZA | 579 |
| 20 | 🇵🇭 PH | 541 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 511 |
| 23 | 🇹🇭 TH | 505 |
| 24 | 🇰🇷 KR | 488 |
| 25 | 🇵🇱 PL | 422 |
| 26 | 🇲🇦 MA | 347 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 280 |
| 29 | 🇮🇩 ID | 274 |
| 30 | 🇳🇱 NL | 272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 527 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Denver International Airport |  | US | 478 |
| 5 | Indira Gandhi International Airport |  | IN | 475 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 399 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 364 |
| 9 | Zurich Airport |  | CH | 336 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 293 |
| 13 | Frankfurt am Main International Airport |  | DE | 293 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 267 |
| 17 | Macau International Airport |  | MO | 262 |
| 18 | Bengaluru International Airport |  | IN | 259 |
| 19 | Charlotte/Douglas International Airport |  | US | 257 |
| 20 | Ninoy Aquino International Airport |  | PH | 248 |
| 21 | Madrid Barajas International Airport |  | ES | 242 |
| 22 | Tenerife Norte Airport |  | ES | 238 |
| 23 | Congonhas Airport |  | BR | 227 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 25 | Salt Lake City International Airport |  | US | 220 |
| 26 | Malpensa International Airport |  | IT | 219 |
| 27 | Daniel K Inouye International Airport |  | US | 219 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 197 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 193 |
| 32 | Miami International Airport |  | US | 189 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 186 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 35 | O. R. Tambo International Airport |  | ZA | 183 |
| 36 | Capua Airport |  | IT | 181 |
| 37 | Seattle-Tacoma International Airport |  | US | 180 |
| 38 | Barcelona International Airport |  | ES | 178 |
| 39 | Vitoria/Foronda Airport |  | ES | 177 |
| 40 | Don Mueang International Airport |  | TH | 173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 135 | 1h 8m | 706 km | 1,643.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 98 | 28m | 304 km | 513.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 83 | 1h 27m | 910 km | 1,302.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 72 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 70 | 19m | 165 km | 199.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 63 | 55m | 546 km | 593.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 57 | 27m | 275 km | 270.1 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 54 | 31m | 369 km | 343.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 52 | 46m | 452 km | 405.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OEFFL | OEF | Foggia / Gino Lisa Airport (LIBF) | L'Aquila / Preturo Airport (LIAP) | 2026-04-11 08:53 UTC | 2026-04-11 09:40 UTC | 47m |
| SWR8KW | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-04-11 08:38 UTC | 2026-04-11 09:27 UTC | 49m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-11 08:20 UTC | 2026-04-11 09:23 UTC | 1h 3m |
| HBZZX | HBZ | Saanen Airport (LSGK) | Sion Airport (LSGS) | 2026-04-11 09:02 UTC | 2026-04-11 09:16 UTC | 13m |
| OOAAC | OOA | Antwerp International Airport (Deurne) (EBAW) | Antwerp International Airport (Deurne) (EBAW) | 2026-04-11 08:31 UTC | 2026-04-11 09:15 UTC | 43m |
| N464SF |  | Kirk Field (KPGR) | Jonesboro Municipal Airport (KJBR) | 2026-04-11 09:02 UTC | 2026-04-11 09:13 UTC | 10m |
| IGO2KY | IndiGo | Yongphulla Airport (VQ10) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-11 07:41 UTC | 2026-04-11 08:58 UTC | 1h 17m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-11 07:03 UTC | 2026-04-11 08:57 UTC | 1h 54m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Sarsawa Air Force Station (VISP) | 2026-04-11 06:48 UTC | 2026-04-11 08:51 UTC | 2h 3m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-11 08:36 UTC | 2026-04-11 08:50 UTC | 13m |
| RYR5905 | Ryanair | Torino / Caselle International Airport (LIMF) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-11 07:07 UTC | 2026-04-11 08:48 UTC | 1h 41m |
| TVF29MG | TVF | Nantes Atlantique Airport (LFRS) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-11 05:53 UTC | 2026-04-11 08:46 UTC | 2h 53m |
| LNK861C | LNK | O. R. Tambo International Airport (FAOR) | Lydenburg Airport (FALL) | 2026-04-11 08:25 UTC | 2026-04-11 08:45 UTC | 19m |
| FYS17ZD | FYS | Cuatro Vientos Airport (LECU) | E. Castellanos-Villacastin Airport (LEEV) | 2026-04-11 08:08 UTC | 2026-04-11 08:45 UTC | 36m |
| ITY1263 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Capua Airport (LIAU) | 2026-04-11 08:23 UTC | 2026-04-11 08:44 UTC | 21m |
| RYR6671 | Ryanair | Madeira Airport (LPMA) | Malpensa International Airport (LIMC) | 2026-04-11 05:05 UTC | 2026-04-11 08:39 UTC | 3h 34m |
| ITY451 | ITY | Munich International Airport (EDDM) | Linate Airport (LIML) | 2026-04-11 07:51 UTC | 2026-04-11 08:39 UTC | 47m |
| VOE8DL | VOE | Valencia Airport (LEVC) | La Morgal Airport (LEMR) | 2026-04-11 07:42 UTC | 2026-04-11 08:36 UTC | 54m |
| EZY49YR | easyJet | London Gatwick Airport (EGKK) | Luqa Airport (LMML) | 2026-04-11 05:51 UTC | 2026-04-11 08:35 UTC | 2h 44m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-11 08:07 UTC | 2026-04-11 08:35 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
