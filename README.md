# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_08:59:35_UTC-green)

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

**Latest saved flight:** 2026-04-23 08:59:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 08:59:35 UTC

- **49,377** saved flights
- **19,965** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,377** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **589,763.6 tonnes** estimated CO2 emissions
- **34,189,193 km** total distance flown
- **832 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2088 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1154 |
| 4 | EJA | 852 |
| 5 | American Airlines | 810 |
| 6 | Southwest Airlines | 703 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 560 |
| 9 | Vueling | 491 |
| 10 | AXM | 490 |
| 11 | LATAM Airlines | 481 |
| 12 | All Nippon Airways | 451 |
| 13 | AZU | 421 |
| 14 | WIF | 408 |
| 15 | Delta Air Lines | 405 |
| 16 | QLK | 402 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 372 |
| 19 | AEE | 333 |
| 20 | Alaska Airlines | 330 |
| 21 | EJU | 320 |
| 22 | easyJet | 314 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 295 |
| 25 | Air France | 277 |
| 26 | AXB | 261 |
| 27 | Cathay Pacific | 259 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | AIQ | 252 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39235 |
| 2 | 🇮🇳 IN | 3608 |
| 3 | 🇪🇸 ES | 3567 |
| 4 | 🇦🇺 AU | 3457 |
| 5 | 🇧🇷 BR | 2870 |
| 6 | 🇯🇵 JP | 2714 |
| 7 | 🇮🇹 IT | 2656 |
| 8 | 🇩🇪 DE | 2604 |
| 9 | 🇨🇦 CA | 2454 |
| 10 | 🇨🇴 CO | 2289 |
| 11 | 🇬🇧 GB | 2028 |
| 12 | 🇫🇷 FR | 1874 |
| 13 | 🇲🇽 MX | 1528 |
| 14 | 🇬🇷 GR | 1497 |
| 15 | 🇨🇭 CH | 1351 |
| 16 | 🇳🇴 NO | 1304 |
| 17 | 🇲🇾 MY | 1196 |
| 18 | 🇿🇦 ZA | 1006 |
| 19 | 🇳🇿 NZ | 956 |
| 20 | 🇹🇭 TH | 900 |
| 21 | 🇹🇷 TR | 868 |
| 22 | 🇵🇭 PH | 863 |
| 23 | 🇰🇷 KR | 814 |
| 24 | 🇵🇱 PL | 789 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 601 |
| 27 | 🇲🇪 ME | 524 |
| 28 | 🇳🇱 NL | 499 |
| 29 | 🇲🇴 MO | 455 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 922 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 787 |
| 5 | Indira Gandhi International Airport |  | IN | 766 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 740 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 642 |
| 9 | Zurich Airport |  | CH | 580 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 540 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 487 |
| 14 | Kuala Lumpur International Airport |  | MY | 478 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 466 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 17 | Macau International Airport |  | MO | 455 |
| 18 | Madrid Barajas International Airport |  | ES | 446 |
| 19 | Bengaluru International Airport |  | IN | 435 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 413 |
| 22 | Malpensa International Airport |  | IT | 407 |
| 23 | Tenerife Norte Airport |  | ES | 405 |
| 24 | Ninoy Aquino International Airport |  | PH | 398 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 377 |
| 26 | Salt Lake City International Airport |  | US | 369 |
| 27 | Daniel K Inouye International Airport |  | US | 367 |
| 28 | Charles de Gaulle International Airport |  | FR | 364 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 360 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 336 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 335 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 329 |
| 35 | Reno/Tahoe International Airport |  | US | 329 |
| 36 | O. R. Tambo International Airport |  | ZA | 324 |
| 37 | Barcelona International Airport |  | ES | 322 |
| 38 | Don Mueang International Airport |  | TH | 306 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 293 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 233 | 1h 7m | 706 km | 2,836.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 189 | 14m | 114 km | 370.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 148 | 21m | 244 km | 623.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 147 | 28m | 304 km | 770.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 131 | 19m | 165 km | 372.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 116 | 26m | 275 km | 549.7 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 102 | 44m | 452 km | 794.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 102 | 54m | 546 km | 960.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 85 | 31m | 369 km | 541.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 83 | 20m | 250 km | 358.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 79 | 26m | 215 km | 292.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 68 | 57m | 493 km | 578.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHBKS | FHB | Dax Seyresse Airport (LFBY) | Itxassou Airport (LFIX) | 2026-04-23 07:56 UTC | 2026-04-23 08:59 UTC | 1h 3m |
| SWR4DK | Swiss International | Hannover Airport (EDDV) | Zurich Airport (LSZH) | 2026-04-23 08:02 UTC | 2026-04-23 08:55 UTC | 52m |
| DHEAL | DHE | Marl Loemuhle Airport (EDLM) | Borken-Hoxfeld Airport (EDLY) | 2026-04-23 06:50 UTC | 2026-04-23 08:26 UTC | 1h 36m |
| HBKGS | HBK | Mollis Airport (LSZM) | Lausanne-la Blecherette Airport (LSGL) | 2026-04-23 07:43 UTC | 2026-04-23 08:25 UTC | 42m |
| BPO323 | BPO | Bonn-Hangelar Airport (EDKB) | Norvenich Airport (ETNN) | 2026-04-23 08:01 UTC | 2026-04-23 08:23 UTC | 22m |
| DKADC | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-23 07:25 UTC | 2026-04-23 08:19 UTC | 54m |
| N479LP |  | 99AZ (99AZ) | Glendale Regional Airport (KGEU) | 2026-04-23 07:20 UTC | 2026-04-23 08:17 UTC | 56m |
| SAS89C | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Tromsø Airport (ENTC) | 2026-04-23 06:42 UTC | 2026-04-23 08:15 UTC | 1h 33m |
| SHABA1 | SHA | Stallion Army Air Field (K95E) | Stallion Army Air Field (K95E) | 2026-04-23 08:00 UTC | 2026-04-23 08:14 UTC | 14m |
| HBKNL | HBK | Locarno Airport (LSZL) | Muenster Aero Airport (LSPU) | 2026-04-23 07:44 UTC | 2026-04-23 08:10 UTC | 25m |
| ABY532 | ABY | Sharjah International Airport (OMSJ) | Simara Airport (VNSI) | 2026-04-23 04:09 UTC | 2026-04-23 08:09 UTC | 3h 59m |
| FPFLC | FPF | Chambery-Challes-les-Eaux Airport (LFLE) | L'alpe D'huez Airport (LFHU) | 2026-04-23 07:29 UTC | 2026-04-23 08:08 UTC | 38m |
| VLG74XH | Vueling | Malaga Airport (LEMG) | Bilbao Airport (LEBB) | 2026-04-23 07:07 UTC | 2026-04-23 08:07 UTC | 59m |
| HAENJ | HAE | Debrecen International Airport (LHDC) | Debrecen International Airport (LHDC) | 2026-04-23 08:03 UTC | 2026-04-23 08:03 UTC | 0m |
| DTA120 | DTA | Camembe Airport (FNCB) | Soyo Airport (FNSO) | 2026-04-23 07:26 UTC | 2026-04-23 08:01 UTC | 35m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Sion Airport (LSGS) | 2026-04-23 07:00 UTC | 2026-04-23 08:01 UTC | 1h 0m |
| VLG7KA | Vueling | Sevilla Airport (LEZL) | Bilbao Airport (LEBB) | 2026-04-23 07:04 UTC | 2026-04-23 08:01 UTC | 57m |
| ANA1645 | All Nippon Airways | Osaka International Airport (RJOO) | Kohnan Airport (RJBK) | 2026-04-23 07:44 UTC | 2026-04-23 08:01 UTC | 17m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-23 07:31 UTC | 2026-04-23 08:01 UTC | 29m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Salem Airport (VOSM) | 2026-04-23 07:22 UTC | 2026-04-23 07:55 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
