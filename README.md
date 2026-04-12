# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_18:17:12_UTC-green)

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

**Latest saved flight:** 2026-04-12 18:17:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 18:17:12 UTC

- **30,979** saved flights
- **14,096** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,979** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **380,179.3 tonnes** estimated CO2 emissions
- **22,039,383 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1289 |
| 2 | SkyWest Airlines | 1249 |
| 3 | IndiGo | 804 |
| 4 | American Airlines | 535 |
| 5 | EJA | 532 |
| 6 | Southwest Airlines | 446 |
| 7 | ENY | 418 |
| 8 | Lufthansa | 368 |
| 9 | AXM | 335 |
| 10 | Vueling | 318 |
| 11 | LATAM Airlines | 310 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 270 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 256 |
| 16 | LXJ | 243 |
| 17 | Swiss International | 230 |
| 18 | EJU | 204 |
| 19 | easyJet | 204 |
| 20 | Alaska Airlines | 202 |
| 21 | WIF | 201 |
| 22 | VIV | 199 |
| 23 | Japan Airlines | 197 |
| 24 | AEE | 196 |
| 25 | EDV | 181 |
| 26 | United Airlines | 180 |
| 27 | Avianca | 169 |
| 28 | Air France | 168 |
| 29 | GLO | 166 |
| 30 | JetBlue | 165 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24323 |
| 2 | 🇮🇳 IN | 2468 |
| 3 | 🇪🇸 ES | 2310 |
| 4 | 🇦🇺 AU | 2173 |
| 5 | 🇧🇷 BR | 1811 |
| 6 | 🇯🇵 JP | 1711 |
| 7 | 🇮🇹 IT | 1624 |
| 8 | 🇩🇪 DE | 1563 |
| 9 | 🇨🇴 CO | 1553 |
| 10 | 🇨🇦 CA | 1494 |
| 11 | 🇬🇧 GB | 1250 |
| 12 | 🇫🇷 FR | 1150 |
| 13 | 🇲🇽 MX | 992 |
| 14 | 🇬🇷 GR | 885 |
| 15 | 🇨🇭 CH | 872 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 679 |
| 18 | 🇳🇿 NZ | 665 |
| 19 | 🇿🇦 ZA | 642 |
| 20 | 🇵🇭 PH | 575 |
| 21 | 🇬🇹 GT | 572 |
| 22 | 🇹🇷 TR | 570 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 473 |
| 26 | 🇲🇦 MA | 401 |
| 27 | 🇧🇸 BS | 327 |
| 28 | 🇲🇪 ME | 310 |
| 29 | 🇳🇱 NL | 297 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 736 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 551 |
| 4 | Indira Gandhi International Airport |  | IN | 520 |
| 5 | Denver International Airport |  | US | 518 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 433 |
| 7 | La Aurora Airport |  | GT | 412 |
| 8 | Harry Reid International Airport |  | US | 398 |
| 9 | Zurich Airport |  | CH | 380 |
| 10 | Guaymaral Airport |  | CO | 375 |
| 11 | Chicago O'Hare International Airport |  | US | 321 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 320 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 319 |
| 14 | Frankfurt am Main International Airport |  | DE | 312 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 290 |
| 18 | Bengaluru International Airport |  | IN | 281 |
| 19 | Charlotte/Douglas International Airport |  | US | 279 |
| 20 | Tenerife Norte Airport |  | ES | 275 |
| 21 | Madrid Barajas International Airport |  | ES | 273 |
| 22 | Ninoy Aquino International Airport |  | PH | 264 |
| 23 | Congonhas Airport |  | BR | 262 |
| 24 | Malpensa International Airport |  | IT | 250 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 238 |
| 26 | Salt Lake City International Airport |  | US | 235 |
| 27 | Daniel K Inouye International Airport |  | US | 234 |
| 28 | Reno/Tahoe International Airport |  | US | 234 |
| 29 | Charles de Gaulle International Airport |  | FR | 228 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 221 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 215 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 33 | Capua Airport |  | IT | 214 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 209 |
| 35 | Miami International Airport |  | US | 208 |
| 36 | O. R. Tambo International Airport |  | ZA | 207 |
| 37 | Vitoria/Foronda Airport |  | ES | 206 |
| 38 | Barcelona International Airport |  | ES | 197 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 146 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 128 | 14m | 114 km | 251.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 71 | 27m | 152 km | 185.5 t |
| 11 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 71 | 9m | - | - |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 66 | 27m | 275 km | 312.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 58 | 52m | 556 km | 556.0 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 57 | 21m | 244 km | 240.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 53 | 20m | 250 km | 228.9 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N350BV |  | Meadows Field (KBFL) | Henderson Executive Airport (KHND) | 2026-04-12 17:37 UTC | 2026-04-12 18:17 UTC | 39m |
| N201QJ |  | Long Island Mac Arthur Airport (KISP) | Elizabeth Field (K0B8) | 2026-04-12 17:42 UTC | 2026-04-12 18:09 UTC | 26m |
| N5YX |  | K5T6 (K5T6) | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | 2026-04-12 17:42 UTC | 2026-04-12 18:08 UTC | 25m |
| DRAGO50 | DRA | Avranches Le Val St Pere Airport (LFRW) | Nantes Atlantique Airport (LFRS) | 2026-04-12 17:17 UTC | 2026-04-12 18:05 UTC | 48m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-04-12 17:43 UTC | 2026-04-12 18:04 UTC | 21m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-04-12 17:39 UTC | 2026-04-12 17:57 UTC | 17m |
| HKC9488 | HKC | Ataturk International Airport (LTBA) | Zhuhai Airport (ZGSD) | 2026-04-12 06:04 UTC | 2026-04-12 17:56 UTC | 11h 52m |
| N900VP |  | Toronto Pearson International Airport (CYYZ) | Buffalo Niagara International Airport (KBUF) | 2026-04-12 17:34 UTC | 2026-04-12 17:56 UTC | 22m |
| N770QS |  | Palm Beach International Airport (KPBI) | Nassau Paradise Island Airport (MYPI) | 2026-04-12 17:26 UTC | 2026-04-12 17:54 UTC | 28m |
| N68AB |  | General Mitchell International Airport (KMKE) | Addington Field (4TX8) | 2026-04-12 15:47 UTC | 2026-04-12 17:50 UTC | 2h 2m |
| N15NF |  | Owosso Community Airport (KRNP) | Brighton Airport (K45G) | 2026-04-12 17:30 UTC | 2026-04-12 17:48 UTC | 17m |
| N3803Q |  | J-Bar Ranch Airport (8TE2) | J-Bar Ranch Airport (8TE2) | 2026-04-12 17:37 UTC | 2026-04-12 17:48 UTC | 11m |
| EJA447 | EJA | Reno/Tahoe International Airport (KRNO) | Palm Springs International Airport (KPSP) | 2026-04-12 16:46 UTC | 2026-04-12 17:47 UTC | 1h 0m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-12 17:19 UTC | 2026-04-12 17:35 UTC | 16m |
| N595KW |  | Batesville Regional Airport (KBVX) | Paul Bridges Field (K0M3) | 2026-04-12 17:03 UTC | 2026-04-12 17:33 UTC | 29m |
| VOE5MZ | VOE | Lyon Saint-Exupery Airport (LFLL) | Menorca Airport (LEMH) | 2026-04-12 16:30 UTC | 2026-04-12 17:31 UTC | 1h 1m |
| N784RR |  | Orlando Executive Airport (KORL) | Rye Field (MS63) | 2026-04-12 15:38 UTC | 2026-04-12 17:31 UTC | 1h 52m |
| DLH4HX | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-04-12 16:44 UTC | 2026-04-12 17:29 UTC | 45m |
| N253DC |  | Warren County/John Lane Field (KI68) | Middletown Regional/Hook Field (KMWO) | 2026-04-12 17:21 UTC | 2026-04-12 17:28 UTC | 6m |
| N789PF |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-04-12 16:59 UTC | 2026-04-12 17:26 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
