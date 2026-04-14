# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_22:15:24_UTC-green)

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

**Latest saved flight:** 2026-04-14 22:15:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 22:15:24 UTC

- **34,915** saved flights
- **15,435** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,915** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **426,669.8 tonnes** estimated CO2 emissions
- **24,734,483 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1503 |
| 2 | SkyWest Airlines | 1400 |
| 3 | IndiGo | 870 |
| 4 | EJA | 605 |
| 5 | American Airlines | 603 |
| 6 | Southwest Airlines | 498 |
| 7 | ENY | 462 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 356 |
| 11 | LATAM Airlines | 349 |
| 12 | AZU | 311 |
| 13 | All Nippon Airways | 310 |
| 14 | Delta Air Lines | 296 |
| 15 | QLK | 290 |
| 16 | LXJ | 279 |
| 17 | Swiss International | 265 |
| 18 | WIF | 254 |
| 19 | AEE | 234 |
| 20 | easyJet | 234 |
| 21 | Alaska Airlines | 233 |
| 22 | EJU | 231 |
| 23 | VIV | 227 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 200 |
| 26 | United Airlines | 197 |
| 27 | Air France | 193 |
| 28 | GLO | 188 |
| 29 | JetBlue | 185 |
| 30 | Avianca | 182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27485 |
| 2 | 🇮🇳 IN | 2660 |
| 3 | 🇪🇸 ES | 2626 |
| 4 | 🇦🇺 AU | 2425 |
| 5 | 🇧🇷 BR | 2057 |
| 6 | 🇮🇹 IT | 1880 |
| 7 | 🇯🇵 JP | 1873 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1753 |
| 10 | 🇨🇦 CA | 1703 |
| 11 | 🇬🇧 GB | 1444 |
| 12 | 🇫🇷 FR | 1300 |
| 13 | 🇲🇽 MX | 1118 |
| 14 | 🇬🇷 GR | 1038 |
| 15 | 🇨🇭 CH | 959 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 823 |
| 18 | 🇳🇿 NZ | 738 |
| 19 | 🇿🇦 ZA | 726 |
| 20 | 🇵🇭 PH | 654 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 612 |
| 24 | 🇰🇷 KR | 586 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 441 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 343 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 832 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 622 |
| 4 | Denver International Airport |  | US | 590 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 510 |
| 7 | Harry Reid International Airport |  | US | 461 |
| 8 | La Aurora Airport |  | GT | 448 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 432 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 359 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 353 |
| 13 | Chicago O'Hare International Airport |  | US | 351 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 318 |
| 19 | Charlotte/Douglas International Airport |  | US | 313 |
| 20 | Tenerife Norte Airport |  | ES | 307 |
| 21 | Bengaluru International Airport |  | IN | 307 |
| 22 | Congonhas Airport |  | BR | 305 |
| 23 | Ninoy Aquino International Airport |  | PH | 302 |
| 24 | Malpensa International Airport |  | IT | 284 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 276 |
| 26 | Salt Lake City International Airport |  | US | 265 |
| 27 | Daniel K Inouye International Airport |  | US | 264 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 247 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 244 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | Vitoria/Foronda Airport |  | ES | 232 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 231 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 219 |
| 39 | Miami International Airport |  | US | 218 |
| 40 | Viracopos International Airport |  | BR | 217 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 145 | 14m | 114 km | 284.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 85 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 80 | 21m | 244 km | 336.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 67 | 31m | 369 km | 426.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 49 | 26m | 215 km | 181.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 49 | 14m | 154 km | 129.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N47632 |  | Harford County Airport (K0W3) | Paramount Air Airport (JY04) | 2026-04-14 21:48 UTC | 2026-04-14 22:15 UTC | 26m |
| DOG1 | DOG | Phoenix Goodyear Airport (KGYR) | Eagle Roost Airpark (27AZ) | 2026-04-14 20:34 UTC | 2026-04-14 22:07 UTC | 1h 32m |
| N757EH |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-04-14 21:12 UTC | 2026-04-14 21:59 UTC | 47m |
| BRG590 | BRG | Red Dog Airport (PADG) | Selawik Airport (PASK) | 2026-04-14 21:13 UTC | 2026-04-14 21:56 UTC | 43m |
| N33RK |  | North Perry Airport (KHWO) | Orlando Executive Airport (KORL) | 2026-04-14 19:56 UTC | 2026-04-14 21:45 UTC | 1h 49m |
| GLR2721 | GLR | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-04-14 21:15 UTC | 2026-04-14 21:41 UTC | 26m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-14 20:41 UTC | 2026-04-14 21:38 UTC | 57m |
| N904PW |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-04-14 21:08 UTC | 2026-04-14 21:37 UTC | 29m |
| G20117 |  | Hastings Airport (K9D9) | Hastings Airport (K9D9) | 2026-04-14 21:30 UTC | 2026-04-14 21:37 UTC | 6m |
| N953LA |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-04-14 21:03 UTC | 2026-04-14 21:32 UTC | 29m |
| N69PJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-14 21:00 UTC | 2026-04-14 21:31 UTC | 31m |
| DCM4121 | DCM | 87IS (87IS) | 5TE8 (5TE8) | 2026-04-14 20:06 UTC | 2026-04-14 21:29 UTC | 1h 23m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-14 21:13 UTC | 2026-04-14 21:27 UTC | 14m |
| TKR168 | TKR | Santa Fe River Ranch Airport (FA62) | Santa Fe River Ranch Airport (FA62) | 2026-04-14 19:49 UTC | 2026-04-14 21:25 UTC | 1h 35m |
| VT3344 |  | Phoenix Sky Harbor International Airport (KPHX) | Happy Canyon Airport (UT97) | 2026-04-14 20:39 UTC | 2026-04-14 21:24 UTC | 45m |
| SHWK427 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-14 20:00 UTC | 2026-04-14 21:22 UTC | 1h 22m |
| C6056 |  | San Diego International Airport (KSAN) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-14 20:06 UTC | 2026-04-14 21:21 UTC | 1h 15m |
| N813VS |  | Peter O Knight Airport (KTPF) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-04-14 20:34 UTC | 2026-04-14 21:20 UTC | 45m |
| GJS4584 | GJS | Chicago O'Hare International Airport (KORD) | 1PS4 (1PS4) | 2026-04-14 20:20 UTC | 2026-04-14 21:19 UTC | 59m |
| STY90 | STY | Palm Beach International Airport (KPBI) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-04-14 18:40 UTC | 2026-04-14 21:19 UTC | 2h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
