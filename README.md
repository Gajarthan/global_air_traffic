# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_15:27:18_UTC-green)

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

**Latest saved flight:** 2026-04-15 15:27:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 15:27:18 UTC

- **35,938** saved flights
- **15,723** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,938** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **436,278.2 tonnes** estimated CO2 emissions
- **25,291,493 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1540 |
| 2 | SkyWest Airlines | 1415 |
| 3 | IndiGo | 899 |
| 4 | EJA | 614 |
| 5 | American Airlines | 609 |
| 6 | Southwest Airlines | 508 |
| 7 | ENY | 474 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 382 |
| 10 | LATAM Airlines | 366 |
| 11 | Vueling | 363 |
| 12 | All Nippon Airways | 321 |
| 13 | AZU | 321 |
| 14 | QLK | 302 |
| 15 | Delta Air Lines | 301 |
| 16 | LXJ | 285 |
| 17 | Swiss International | 275 |
| 18 | WIF | 264 |
| 19 | AEE | 243 |
| 20 | easyJet | 240 |
| 21 | Alaska Airlines | 237 |
| 22 | EJU | 234 |
| 23 | VIV | 230 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 203 |
| 26 | EDV | 201 |
| 27 | United Airlines | 199 |
| 28 | GLO | 193 |
| 29 | AIQ | 191 |
| 30 | JetBlue | 189 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28061 |
| 2 | 🇮🇳 IN | 2751 |
| 3 | 🇪🇸 ES | 2682 |
| 4 | 🇦🇺 AU | 2549 |
| 5 | 🇧🇷 BR | 2126 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1930 |
| 8 | 🇩🇪 DE | 1848 |
| 9 | 🇨🇴 CO | 1767 |
| 10 | 🇨🇦 CA | 1747 |
| 11 | 🇬🇧 GB | 1487 |
| 12 | 🇫🇷 FR | 1358 |
| 13 | 🇲🇽 MX | 1134 |
| 14 | 🇬🇷 GR | 1087 |
| 15 | 🇨🇭 CH | 998 |
| 16 | 🇲🇾 MY | 929 |
| 17 | 🇳🇴 NO | 862 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 760 |
| 20 | 🇵🇭 PH | 685 |
| 21 | 🇹🇭 TH | 668 |
| 22 | 🇹🇷 TR | 656 |
| 23 | 🇬🇹 GT | 619 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 567 |
| 26 | 🇲🇦 MA | 449 |
| 27 | 🇳🇱 NL | 357 |
| 28 | 🇲🇪 ME | 349 |
| 29 | 🇧🇸 BS | 347 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 848 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 630 |
| 4 | Denver International Airport |  | US | 600 |
| 5 | Indira Gandhi International Airport |  | IN | 585 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 533 |
| 7 | Harry Reid International Airport |  | US | 472 |
| 8 | La Aurora Airport |  | GT | 454 |
| 9 | Zurich Airport |  | CH | 447 |
| 10 | Guaymaral Airport |  | CO | 441 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Kuala Lumpur International Airport |  | MY | 360 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 14 | Chicago O'Hare International Airport |  | US | 356 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 335 |
| 17 | Madrid Barajas International Airport |  | ES | 324 |
| 18 | Macau International Airport |  | MO | 322 |
| 19 | Charlotte/Douglas International Airport |  | US | 321 |
| 20 | Tenerife Norte Airport |  | ES | 320 |
| 21 | Bengaluru International Airport |  | IN | 318 |
| 22 | Ninoy Aquino International Airport |  | PH | 317 |
| 23 | Congonhas Airport |  | BR | 317 |
| 24 | Malpensa International Airport |  | IT | 293 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 282 |
| 26 | Daniel K Inouye International Airport |  | US | 271 |
| 27 | Salt Lake City International Airport |  | US | 271 |
| 28 | Charles de Gaulle International Airport |  | FR | 267 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 253 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 253 |
| 32 | Reno/Tahoe International Airport |  | US | 248 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 246 |
| 34 | O. R. Tambo International Airport |  | ZA | 243 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 238 |
| 36 | Vitoria/Foronda Airport |  | ES | 235 |
| 37 | Barcelona International Airport |  | ES | 234 |
| 38 | Viracopos International Airport |  | BR | 226 |
| 39 | Don Mueang International Airport |  | TH | 226 |
| 40 | Seattle-Tacoma International Airport |  | US | 223 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 85 | 21m | 244 km | 357.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 78 | 21m | 99 km | 133.6 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 77 | 27m | 275 km | 364.9 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 59 | 20m | 147 km | 149.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 54 | 13m | 99 km | 92.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 51 | 26m | 215 km | 188.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 51 | 1h 20m | 961 km | 845.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR8400 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-15 08:22 UTC | 2026-04-15 15:27 UTC | 7h 4m |
| N98151 |  | Lakefront Airport (KNEW) | Lakefront Airport (KNEW) | 2026-04-15 14:30 UTC | 2026-04-15 15:26 UTC | 56m |
| UPS5333 | UPS | Miami International Airport (KMIA) | Dallas-Fort Worth International Airport (KDFW) | 2026-04-15 12:45 UTC | 2026-04-15 15:24 UTC | 2h 38m |
| RDHK723 | RDH | Oceana Nas (Apollo Soucek Field) Airport (KNTU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-15 15:11 UTC | 2026-04-15 15:23 UTC | 11m |
| N907JW |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-15 14:38 UTC | 2026-04-15 15:23 UTC | 45m |
| SKW4710 | SkyWest Airlines | Dorsey Ranch Airport (1SD0) | Denver International Airport (KDEN) | 2026-04-15 14:22 UTC | 2026-04-15 15:18 UTC | 56m |
| N362CD |  | Decatur Municipal Airport (KLUD) | 69XA (69XA) | 2026-04-15 14:47 UTC | 2026-04-15 15:15 UTC | 28m |
| N65112 |  | Hector International Airport (KFAR) | Angen Field (MN44) | 2026-04-15 13:45 UTC | 2026-04-15 15:09 UTC | 1h 24m |
| RNGR804 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-04-15 14:46 UTC | 2026-04-15 15:08 UTC | 21m |
| SEH307 | SEH | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-15 14:19 UTC | 2026-04-15 15:08 UTC | 48m |
| DRAGO64 | DRA | Pau Pyrenees Airport (LFBP) | Oloron Herrere Airport (LFCO) | 2026-04-15 14:44 UTC | 2026-04-15 15:07 UTC | 23m |
| CGFHA | CGF | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-04-15 14:40 UTC | 2026-04-15 15:07 UTC | 27m |
| LLN106 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | Decatur Municipal Airport (KLUD) | 2026-04-15 14:49 UTC | 2026-04-15 15:05 UTC | 15m |
| N78US |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-04-15 14:20 UTC | 2026-04-15 15:02 UTC | 41m |
| N427SE |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Stockton Lake Airport (KMO3) | 2026-04-15 14:35 UTC | 2026-04-15 15:01 UTC | 25m |
| SLICK22 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-04-15 14:35 UTC | 2026-04-15 15:00 UTC | 24m |
| AFL1855 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-15 14:56 UTC | 2026-04-15 14:59 UTC | 2m |
| N465HD |  | Salt Lake City International Airport (KSLC) | Skypark Airport (KBTF) | 2026-04-15 14:50 UTC | 2026-04-15 14:58 UTC | 8m |
| N631AA |  | North Palm Beach County General Aviation Airport (KF45) | William P Gwinn Airport (06FA) | 2026-04-15 14:49 UTC | 2026-04-15 14:57 UTC | 7m |
| N317CL |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-04-15 14:30 UTC | 2026-04-15 14:55 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
