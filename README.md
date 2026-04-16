# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_17:29:39_UTC-green)

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

**Latest saved flight:** 2026-04-16 17:29:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 17:29:39 UTC

- **37,707** saved flights
- **16,305** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,707** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **455,322.5 tonnes** estimated CO2 emissions
- **26,395,509 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1594 |
| 2 | SkyWest Airlines | 1473 |
| 3 | IndiGo | 932 |
| 4 | EJA | 642 |
| 5 | American Airlines | 629 |
| 6 | Southwest Airlines | 524 |
| 7 | ENY | 489 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | LATAM Airlines | 380 |
| 11 | Vueling | 380 |
| 12 | All Nippon Airways | 337 |
| 13 | AZU | 337 |
| 14 | Delta Air Lines | 322 |
| 15 | QLK | 313 |
| 16 | LXJ | 299 |
| 17 | WIF | 284 |
| 18 | Swiss International | 282 |
| 19 | AEE | 252 |
| 20 | Alaska Airlines | 249 |
| 21 | EJU | 248 |
| 22 | easyJet | 247 |
| 23 | VIV | 238 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 214 |
| 26 | United Airlines | 208 |
| 27 | EDV | 207 |
| 28 | GLO | 199 |
| 29 | AIQ | 198 |
| 30 | JetBlue | 194 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29582 |
| 2 | 🇮🇳 IN | 2850 |
| 3 | 🇪🇸 ES | 2806 |
| 4 | 🇦🇺 AU | 2654 |
| 5 | 🇧🇷 BR | 2226 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 1993 |
| 8 | 🇩🇪 DE | 1938 |
| 9 | 🇨🇴 CO | 1853 |
| 10 | 🇨🇦 CA | 1836 |
| 11 | 🇬🇧 GB | 1559 |
| 12 | 🇫🇷 FR | 1436 |
| 13 | 🇲🇽 MX | 1186 |
| 14 | 🇬🇷 GR | 1142 |
| 15 | 🇨🇭 CH | 1034 |
| 16 | 🇲🇾 MY | 963 |
| 17 | 🇳🇴 NO | 915 |
| 18 | 🇿🇦 ZA | 799 |
| 19 | 🇳🇿 NZ | 789 |
| 20 | 🇵🇭 PH | 703 |
| 21 | 🇹🇭 TH | 689 |
| 22 | 🇹🇷 TR | 681 |
| 23 | 🇬🇹 GT | 646 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 595 |
| 26 | 🇲🇦 MA | 473 |
| 27 | 🇳🇱 NL | 378 |
| 28 | 🇲🇪 ME | 373 |
| 29 | 🇧🇸 BS | 370 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 879 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 655 |
| 4 | Denver International Airport |  | US | 626 |
| 5 | Indira Gandhi International Airport |  | IN | 615 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 564 |
| 7 | Harry Reid International Airport |  | US | 492 |
| 8 | Guaymaral Airport |  | CO | 478 |
| 9 | La Aurora Airport |  | GT | 475 |
| 10 | Zurich Airport |  | CH | 454 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 376 |
| 12 | Kuala Lumpur International Airport |  | MY | 375 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 374 |
| 14 | Chicago O'Hare International Airport |  | US | 365 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Frankfurt am Main International Airport |  | DE | 345 |
| 17 | Madrid Barajas International Airport |  | ES | 343 |
| 18 | Macau International Airport |  | MO | 342 |
| 19 | Charlotte/Douglas International Airport |  | US | 335 |
| 20 | Tenerife Norte Airport |  | ES | 335 |
| 21 | Congonhas Airport |  | BR | 330 |
| 22 | Bengaluru International Airport |  | IN | 328 |
| 23 | Ninoy Aquino International Airport |  | PH | 326 |
| 24 | Malpensa International Airport |  | IT | 311 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 290 |
| 26 | Salt Lake City International Airport |  | US | 286 |
| 27 | Daniel K Inouye International Airport |  | US | 281 |
| 28 | Charles de Gaulle International Airport |  | FR | 279 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 268 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 268 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | O. R. Tambo International Airport |  | ZA | 256 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 256 |
| 34 | Reno/Tahoe International Airport |  | US | 255 |
| 35 | Vitoria/Foronda Airport |  | ES | 253 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 245 |
| 37 | Barcelona International Airport |  | ES | 243 |
| 38 | Don Mueang International Airport |  | TH | 235 |
| 39 | Viracopos International Airport |  | BR | 233 |
| 40 | Seattle-Tacoma International Airport |  | US | 229 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 189 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 94 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 91 | 21m | 244 km | 383.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 85 | 27m | 275 km | 402.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 57 | 1h 41m | 1,423 km | 1,398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 56 | 26m | 215 km | 207.4 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 53 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK664 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-04-16 17:01 UTC | 2026-04-16 17:29 UTC | 28m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-16 17:08 UTC | 2026-04-16 17:28 UTC | 19m |
| SPNWD | SPN | Ostrów Airport (EPOM) | Leszno Strzyzewi Airport (EPLS) | 2026-04-16 16:45 UTC | 2026-04-16 17:25 UTC | 39m |
| AXB1577 | AXB | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-16 17:22 UTC | 2026-04-16 17:22 UTC | 0m |
| CXK282 | CXK | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-04-16 17:08 UTC | 2026-04-16 17:20 UTC | 12m |
| EJM33 | EJM | Wilkes-Barre/Scranton International Airport (KAVP) | Lehigh Valley International Airport (KABE) | 2026-04-16 16:54 UTC | 2026-04-16 17:08 UTC | 13m |
| N4182T |  | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-04-16 16:51 UTC | 2026-04-16 17:06 UTC | 15m |
| JUMP3 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-04-16 16:31 UTC | 2026-04-16 17:06 UTC | 34m |
| N426MR |  | North Central State Airport (KSFZ) | North Central State Airport (KSFZ) | 2026-04-16 16:06 UTC | 2026-04-16 17:05 UTC | 59m |
| N982ST |  | Dallas Love Field (KDAL) | Perot Field/Fort Worth Alliance Airport (KAFW) | 2026-04-16 16:32 UTC | 2026-04-16 17:01 UTC | 29m |
| VAR403 | VAR | Phoenix Goodyear Airport (KGYR) | Lake Havasu City Airport (KHII) | 2026-04-16 15:54 UTC | 2026-04-16 16:56 UTC | 1h 2m |
| BASS21 | BAS | Okolona Municipal/Richard Stovall Field (K5A4) | Godspeed Airpark (8MS2) | 2026-04-16 16:42 UTC | 2026-04-16 16:56 UTC | 14m |
| BASS22 | BAS | Spearman Field (4MS4) | Godspeed Airpark (8MS2) | 2026-04-16 16:42 UTC | 2026-04-16 16:56 UTC | 13m |
| COBRA27 | COB | Boron Airstrip (57CL) | Boron Airstrip (57CL) | 2026-04-16 16:44 UTC | 2026-04-16 16:55 UTC | 11m |
| N70CR |  | Dallas Love Field (KDAL) | Lewis Private Airport (4TE2) | 2026-04-16 16:09 UTC | 2026-04-16 16:53 UTC | 44m |
| CREEP31 | CRE | 75OK (75OK) | Nelson High Point Airport (8OK7) | 2026-04-16 16:14 UTC | 2026-04-16 16:53 UTC | 38m |
| AXL474 | AXL | Argyle International Airport (TVSA) | Lauriston Airport (TGPZ) | 2026-04-16 16:33 UTC | 2026-04-16 16:47 UTC | 14m |
| N3171E |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-16 16:29 UTC | 2026-04-16 16:47 UTC | 18m |
| T7ACA |  | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-16 16:21 UTC | 2026-04-16 16:47 UTC | 25m |
| EJA801 | EJA | Tampa International Airport (KTPA) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-16 15:55 UTC | 2026-04-16 16:46 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
