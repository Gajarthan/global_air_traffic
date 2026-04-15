# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_08:37:04_UTC-green)

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

**Latest saved flight:** 2026-04-15 08:37:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 08:37:04 UTC

- **35,329** saved flights
- **15,547** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,329** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **430,818.3 tonnes** estimated CO2 emissions
- **24,974,976 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1506 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 878 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 469 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 373 |
| 10 | Vueling | 358 |
| 11 | LATAM Airlines | 353 |
| 12 | All Nippon Airways | 316 |
| 13 | AZU | 315 |
| 14 | QLK | 301 |
| 15 | Delta Air Lines | 300 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 267 |
| 18 | WIF | 257 |
| 19 | AEE | 237 |
| 20 | Alaska Airlines | 237 |
| 21 | easyJet | 235 |
| 22 | EJU | 231 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 219 |
| 25 | EDV | 201 |
| 26 | United Airlines | 199 |
| 27 | Air France | 194 |
| 28 | GLO | 192 |
| 29 | JetBlue | 187 |
| 30 | Avianca | 184 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27761 |
| 2 | 🇮🇳 IN | 2680 |
| 3 | 🇪🇸 ES | 2634 |
| 4 | 🇦🇺 AU | 2514 |
| 5 | 🇧🇷 BR | 2082 |
| 6 | 🇯🇵 JP | 1923 |
| 7 | 🇮🇹 IT | 1888 |
| 8 | 🇩🇪 DE | 1790 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1726 |
| 11 | 🇬🇧 GB | 1453 |
| 12 | 🇫🇷 FR | 1306 |
| 13 | 🇲🇽 MX | 1132 |
| 14 | 🇬🇷 GR | 1051 |
| 15 | 🇨🇭 CH | 967 |
| 16 | 🇲🇾 MY | 901 |
| 17 | 🇳🇴 NO | 830 |
| 18 | 🇳🇿 NZ | 771 |
| 19 | 🇿🇦 ZA | 732 |
| 20 | 🇵🇭 PH | 678 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 633 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 601 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 442 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 346 |
| 29 | 🇲🇪 ME | 346 |
| 30 | 🇮🇩 ID | 336 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 654 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 571 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 517 |
| 7 | Harry Reid International Airport |  | US | 467 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 435 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 13 | Chicago O'Hare International Airport |  | US | 355 |
| 14 | Kuala Lumpur International Airport |  | MY | 347 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 343 |
| 16 | Frankfurt am Main International Airport |  | DE | 334 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Charlotte/Douglas International Airport |  | US | 319 |
| 19 | Madrid Barajas International Airport |  | ES | 319 |
| 20 | Ninoy Aquino International Airport |  | PH | 313 |
| 21 | Bengaluru International Airport |  | IN | 309 |
| 22 | Congonhas Airport |  | BR | 309 |
| 23 | Tenerife Norte Airport |  | ES | 307 |
| 24 | Malpensa International Airport |  | IT | 285 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 281 |
| 26 | Salt Lake City International Airport |  | US | 270 |
| 27 | Daniel K Inouye International Airport |  | US | 269 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 258 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 248 |
| 31 | Reno/Tahoe International Airport |  | US | 247 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 236 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 234 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 222 |
| 39 | Viracopos International Airport |  | BR | 221 |
| 40 | Miami International Airport |  | US | 219 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 165 | 1h 8m | 706 km | 2,008.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 133 | 24m | 225 km | 516.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 101 | 1h 27m | 910 km | 1,584.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 92 | 19m | 165 km | 261.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 87 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 84 | 21m | 244 km | 353.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 74 | 1h 12m | 770 km | 983.0 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 68 | 31m | 369 km | 432.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 66 | 45m | 452 km | 514.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
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
| T7ACA |  | Belgrade Nikola Tesla Airport (LYBE) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-15 07:28 UTC | 2026-04-15 08:37 UTC | 1h 8m |
| ETD2NG | Etihad Airways | Abu Dhabi International Airport (OMAA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-14 23:32 UTC | 2026-04-15 08:36 UTC | 9h 4m |
| HR611 |  | Chofu Airport (RJTF) | Tachikawa Airfield (RJTC) | 2026-04-15 08:05 UTC | 2026-04-15 08:24 UTC | 18m |
| UFX64 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-04-15 07:52 UTC | 2026-04-15 08:22 UTC | 29m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Tribhuvan International Airport (VNKT) | 2026-04-15 05:06 UTC | 2026-04-15 08:18 UTC | 3h 11m |
| ZKICU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-15 07:52 UTC | 2026-04-15 08:17 UTC | 24m |
| TLM220 | TLM | Don Mueang International Airport (VTBD) | Tribhuvan International Airport (VNKT) | 2026-04-15 05:15 UTC | 2026-04-15 08:16 UTC | 3h 1m |
| BAG12 | BAG | Linz Airport (LOWL) | Vienna International Airport (LOWW) | 2026-04-15 07:39 UTC | 2026-04-15 08:14 UTC | 35m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-04-15 07:15 UTC | 2026-04-15 08:13 UTC | 58m |
| JIGSW94 | JIG | Belfast International Airport (EGAA) | Skye Bridge Ashaig Airport (XBRO) | 2026-04-15 07:36 UTC | 2026-04-15 08:05 UTC | 29m |
| DLA9850 | DLA | Munich International Airport (EDDM) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-15 07:25 UTC | 2026-04-15 08:04 UTC | 39m |
| SRB501 | SRB | LYCA (LYCA) | Batajnica Air Base (LYBT) | 2026-04-15 07:31 UTC | 2026-04-15 08:03 UTC | 31m |
| 6VHAK |  | Leopold Sedar Senghor International Airport (GOOY) | Banjul International Airport (GBYD) | 2026-04-15 07:29 UTC | 2026-04-15 08:02 UTC | 33m |
| NOX51 | NOX | Wunstorf Airport (ETNW) | Jever Airport (ETNJ) | 2026-04-15 07:29 UTC | 2026-04-15 08:01 UTC | 32m |
| FHXCB | FHX | Caen-Carpiquet Airport (LFRK) | Caen-Carpiquet Airport (LFRK) | 2026-04-15 07:49 UTC | 2026-04-15 07:56 UTC | 7m |
| HR611 |  | Atsugi Naval Air Facility (RJTA) | Tachikawa Airfield (RJTC) | 2026-04-15 06:59 UTC | 2026-04-15 07:55 UTC | 55m |
| UAE9872 | Emirates | Al Maktoum International Airport (OMDW) | Phonngbyin Airport (VYPB) | 2026-04-14 19:32 UTC | 2026-04-15 07:54 UTC | 12h 22m |
| SAS4139 | Scandinavian Airlines | Bergen Airport Flesland (ENBR) | Haugesund Airport (ENHD) | 2026-04-15 07:43 UTC | 2026-04-15 07:54 UTC | 11m |
| SEH2JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-15 07:19 UTC | 2026-04-15 07:49 UTC | 29m |
| FD524 |  | Adelaide International Airport (YPAD) | Padthaway Station Airport (YPDY) | 2026-04-15 07:16 UTC | 2026-04-15 07:48 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
