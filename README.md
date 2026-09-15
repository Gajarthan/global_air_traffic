# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_14:58:43_UTC-green)

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

**Latest saved flight:** 2026-09-15 14:58:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 14:58:43 UTC

- **259,251** saved flights
- **76,979** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,251** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,139,616.8 tonnes** estimated CO2 emissions
- **182,006,769 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10272 |
| 2 | SkyWest Airlines | 9032 |
| 3 | EJA | 5024 |
| 4 | IndiGo | 4353 |
| 5 | American Airlines | 4089 |
| 6 | Southwest Airlines | 3812 |
| 7 | Delta Air Lines | 3237 |
| 8 | ENY | 3070 |
| 9 | LATAM Airlines | 2492 |
| 10 | AZU | 2432 |
| 11 | Vueling | 2191 |
| 12 | WIF | 2083 |
| 13 | LXJ | 2025 |
| 14 | Lufthansa | 2019 |
| 15 | easyJet | 1765 |
| 16 | Swiss International | 1730 |
| 17 | QLK | 1675 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1598 |
| 21 | Alaska Airlines | 1538 |
| 22 | All Nippon Airways | 1503 |
| 23 | WMT | 1463 |
| 24 | GLO | 1443 |
| 25 | PGT | 1443 |
| 26 | VIV | 1420 |
| 27 | Air France | 1418 |
| 28 | Wizz Air | 1413 |
| 29 | AEE | 1254 |
| 30 | TKR | 1252 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215169 |
| 2 | 🇪🇸 ES | 16421 |
| 3 | 🇧🇷 BR | 15148 |
| 4 | 🇦🇺 AU | 14800 |
| 5 | 🇨🇦 CA | 14434 |
| 6 | 🇮🇹 IT | 14110 |
| 7 | 🇮🇳 IN | 13704 |
| 8 | 🇩🇪 DE | 12599 |
| 9 | 🇬🇧 GB | 12077 |
| 10 | 🇨🇴 CO | 11650 |
| 11 | 🇫🇷 FR | 10410 |
| 12 | 🇯🇵 JP | 10093 |
| 13 | 🇹🇷 TR | 7828 |
| 14 | 🇬🇷 GR | 7545 |
| 15 | 🇲🇽 MX | 7148 |
| 16 | 🇨🇭 CH | 6966 |
| 17 | 🇳🇴 NO | 6403 |
| 18 | 🇹🇭 TH | 4662 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4286 |
| 22 | 🇳🇿 NZ | 3590 |
| 23 | 🇵🇭 PH | 3479 |
| 24 | 🇬🇹 GT | 3281 |
| 25 | 🇭🇷 HR | 2969 |
| 26 | 🇰🇷 KR | 2961 |
| 27 | 🇲🇦 MA | 2598 |
| 28 | 🇲🇪 ME | 2442 |
| 29 | 🇳🇱 NL | 2326 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5312 |
| 2 | Denver International Airport |  | US | 4191 |
| 3 | Indira Gandhi International Airport |  | IN | 3132 |
| 4 | Tokyo International Airport |  | JP | 3010 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2754 |
| 7 | Zurich Airport |  | CH | 2719 |
| 8 | El Dorado International Airport |  | CO | 2716 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2609 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2528 |
| 11 | La Aurora Airport |  | GT | 2493 |
| 12 | Salt Lake City International Airport |  | US | 2287 |
| 13 | Chicago O'Hare International Airport |  | US | 2250 |
| 14 | Congonhas Airport |  | BR | 2216 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2118 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2014 |
| 18 | Frankfurt am Main International Airport |  | DE | 1993 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1948 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1867 |
| 21 | Malpensa International Airport |  | IT | 1862 |
| 22 | Charles de Gaulle International Airport |  | FR | 1828 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1826 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1789 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1762 |
| 26 | Macau International Airport |  | MO | 1719 |
| 27 | Ninoy Aquino International Airport |  | PH | 1706 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1622 |
| 30 | Kuala Lumpur International Airport |  | MY | 1595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1592 |
| 32 | Viracopos International Airport |  | BR | 1566 |
| 33 | Seattle-Tacoma International Airport |  | US | 1520 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1511 |
| 35 | Don Mueang International Airport |  | TH | 1489 |
| 36 | Calgary International Airport |  | CA | 1483 |
| 37 | Bengaluru International Airport |  | IN | 1473 |
| 38 | Oslo Gardermoen Airport |  | NO | 1460 |
| 39 | Vancouver International Airport |  | CA | 1452 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1394 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 966 | 21m | 244 km | 4,067.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 699 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 649 | 1h 6m | 770 km | 8,621.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 580 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 420 | 44m | 555 km | 4,021.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 393 | 44m | 241 km | 1,632.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 346 | 23m | 55 km | 328.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 323 | 19m | 99 km | 553.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 313 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 279 | 1h 50m | 1,304 km | 6,276.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 272 | 28m | 152 km | 710.8 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-09-15 13:54 UTC | 2026-09-15 14:58 UTC | 1h 4m |
| CGNDP | CGN | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-09-15 14:28 UTC | 2026-09-15 14:56 UTC | 27m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Somerset Airport (KSMQ) | 2026-09-15 13:20 UTC | 2026-09-15 14:52 UTC | 1h 32m |
| CONGO65 | CON | City Of Colorado Springs Municipal Airport (KCOS) | 1CO7 (1CO7) | 2026-09-15 14:12 UTC | 2026-09-15 14:51 UTC | 39m |
| N121MS |  | Danbury Municipal Airport (KDXR) | Danbury Municipal Airport (KDXR) | 2026-09-15 14:25 UTC | 2026-09-15 14:51 UTC | 25m |
| ERU22 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-09-15 14:37 UTC | 2026-09-15 14:50 UTC | 12m |
| UAE508 | Emirates | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-15 12:24 UTC | 2026-09-15 14:47 UTC | 2h 22m |
| N609LH |  | Northeast Philadelphia Airport (KPNE) | Ocean County Airport (KMJX) | 2026-09-15 13:48 UTC | 2026-09-15 14:44 UTC | 56m |
| N67573 |  | North Perry Airport (KHWO) | North Perry Airport (KHWO) | 2026-09-15 14:25 UTC | 2026-09-15 14:43 UTC | 18m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-09-15 14:17 UTC | 2026-09-15 14:43 UTC | 25m |
| N298PC |  | Redding Regional Airport (KRDD) | Mahlon Sweet Field (KEUG) | 2026-09-15 13:59 UTC | 2026-09-15 14:42 UTC | 42m |
| TGKCS | TGK | Copan Ruinas Airport (MHRU) | La Aurora Airport (MGGT) | 2026-09-15 14:11 UTC | 2026-09-15 14:41 UTC | 30m |
| FHMZR | FHM | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-09-15 14:25 UTC | 2026-09-15 14:41 UTC | 15m |
| ARCAT55 | ARC | Montgomery-Gibbs Executive Airport (KMYF) | Osborne Airport (8CA0) | 2026-09-15 14:13 UTC | 2026-09-15 14:38 UTC | 25m |
| PRO4826 | PRO | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Bathurst Airport (CZBF) | 2026-09-15 13:13 UTC | 2026-09-15 14:37 UTC | 1h 24m |
| N36456 |  | Beverly Regional Airport (KBVY) | Beverly Regional Airport (KBVY) | 2026-09-15 13:44 UTC | 2026-09-15 14:36 UTC | 52m |
| OKCTP | OKC | Parnu Airport (EEPU) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-15 12:27 UTC | 2026-09-15 14:35 UTC | 2h 7m |
| EFY7834 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-15 14:04 UTC | 2026-09-15 14:35 UTC | 30m |
| N240TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-15 14:16 UTC | 2026-09-15 14:33 UTC | 17m |
| HOTROD2 | HOT | Rostock-Laage Airport (ETNL) | Peenemunde Airport (EDCP) | 2026-09-15 13:51 UTC | 2026-09-15 14:32 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
