# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_16:52:30_UTC-green)

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

**Latest saved flight:** 2026-04-19 16:52:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 16:52:30 UTC

- **43,390** saved flights
- **18,117** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,390** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **522,005.6 tonnes** estimated CO2 emissions
- **30,261,197 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1829 |
| 2 | SkyWest Airlines | 1667 |
| 3 | IndiGo | 1070 |
| 4 | EJA | 740 |
| 5 | American Airlines | 710 |
| 6 | Southwest Airlines | 603 |
| 7 | ENY | 563 |
| 8 | AXM | 446 |
| 9 | Lufthansa | 437 |
| 10 | LATAM Airlines | 434 |
| 11 | Vueling | 433 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 383 |
| 14 | Delta Air Lines | 366 |
| 15 | QLK | 354 |
| 16 | LXJ | 340 |
| 17 | WIF | 339 |
| 18 | Swiss International | 337 |
| 19 | AEE | 296 |
| 20 | Alaska Airlines | 291 |
| 21 | EJU | 286 |
| 22 | easyJet | 278 |
| 23 | VIV | 272 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 249 |
| 26 | AXB | 231 |
| 27 | United Airlines | 230 |
| 28 | JetBlue | 229 |
| 29 | GLO | 227 |
| 30 | AIQ | 222 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34081 |
| 2 | 🇮🇳 IN | 3293 |
| 3 | 🇪🇸 ES | 3204 |
| 4 | 🇦🇺 AU | 3031 |
| 5 | 🇧🇷 BR | 2596 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2287 |
| 8 | 🇩🇪 DE | 2211 |
| 9 | 🇨🇦 CA | 2098 |
| 10 | 🇨🇴 CO | 2005 |
| 11 | 🇬🇧 GB | 1763 |
| 12 | 🇫🇷 FR | 1670 |
| 13 | 🇲🇽 MX | 1345 |
| 14 | 🇬🇷 GR | 1345 |
| 15 | 🇨🇭 CH | 1200 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1083 |
| 18 | 🇿🇦 ZA | 915 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 769 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 713 |
| 25 | 🇵🇱 PL | 696 |
| 26 | 🇲🇦 MA | 541 |
| 27 | 🇲🇪 ME | 455 |
| 28 | 🇳🇱 NL | 447 |
| 29 | 🇧🇸 BS | 401 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1003 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 712 |
| 4 | Indira Gandhi International Airport |  | IN | 709 |
| 5 | El Dorado International Airport |  | CO | 703 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 669 |
| 7 | Harry Reid International Airport |  | US | 549 |
| 8 | Guaymaral Airport |  | CO | 542 |
| 9 | La Aurora Airport |  | GT | 526 |
| 10 | Zurich Airport |  | CH | 524 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 424 |
| 13 | Chicago O'Hare International Airport |  | US | 418 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 417 |
| 15 | Frankfurt am Main International Airport |  | DE | 407 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Madrid Barajas International Airport |  | ES | 390 |
| 19 | Bengaluru International Airport |  | IN | 390 |
| 20 | Tenerife Norte Airport |  | ES | 379 |
| 21 | Charlotte/Douglas International Airport |  | US | 375 |
| 22 | Congonhas Airport |  | BR | 373 |
| 23 | Ninoy Aquino International Airport |  | PH | 366 |
| 24 | Malpensa International Airport |  | IT | 359 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 27 | Salt Lake City International Airport |  | US | 327 |
| 28 | Charles de Gaulle International Airport |  | FR | 323 |
| 29 | Daniel K Inouye International Airport |  | US | 321 |
| 30 | Vitoria/Foronda Airport |  | ES | 303 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 302 |
| 32 | Reno/Tahoe International Airport |  | US | 298 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 295 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 295 |
| 35 | O. R. Tambo International Airport |  | ZA | 294 |
| 36 | Capua Airport |  | IT | 294 |
| 37 | Barcelona International Airport |  | ES | 281 |
| 38 | Viracopos International Airport |  | BR | 266 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 218 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 164 | 14m | 114 km | 321.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 119 | 21m | 244 km | 501.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 107 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 101 | 26m | 275 km | 478.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 70 | 52m | 556 km | 671.0 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 61 | 13m | 99 km | 104.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 61 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N953ER |  | Summerville Airport (KDYB) | Jekyll Island Airport (K09J) | 2026-04-19 15:09 UTC | 2026-04-19 16:52 UTC | 1h 42m |
| AAL1001 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Cancun International Airport (MMUN) | 2026-04-19 14:26 UTC | 2026-04-19 16:33 UTC | 2h 7m |
| N444GM |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-04-19 16:18 UTC | 2026-04-19 16:31 UTC | 12m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-19 16:11 UTC | 2026-04-19 16:27 UTC | 16m |
| PSVTA | PSV | Campo de Marte Airport (SBMT) | Saquarema Airport (SDSK) | 2026-04-19 15:35 UTC | 2026-04-19 16:25 UTC | 49m |
| ABX305 | ABX | Cincinnati/Northern Kentucky International Airport (KCVG) | John F Kennedy International Airport (KJFK) | 2026-04-19 14:54 UTC | 2026-04-19 16:25 UTC | 1h 30m |
| NOZ64N | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-19 15:46 UTC | 2026-04-19 16:21 UTC | 34m |
|  |  | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-19 16:04 UTC | 2026-04-19 16:19 UTC | 15m |
| AFR76QE | Air France | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-04-19 16:01 UTC | 2026-04-19 16:18 UTC | 16m |
| N271CK |  | KFTG (KFTG) | Colorado Plains Regional Airport (KAKO) | 2026-04-19 15:48 UTC | 2026-04-19 16:18 UTC | 29m |
| N560PU |  | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-19 16:01 UTC | 2026-04-19 16:17 UTC | 16m |
| N727SB |  | Austin Executive Airport (KEDC) | TA89 (TA89) | 2026-04-19 15:55 UTC | 2026-04-19 16:17 UTC | 21m |
| SCU26 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-19 16:16 UTC | 2026-04-19 16:16 UTC | 0m |
| N248SF |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-19 15:37 UTC | 2026-04-19 16:16 UTC | 38m |
| ES802 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-04-19 15:28 UTC | 2026-04-19 16:15 UTC | 46m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-19 16:03 UTC | 2026-04-19 16:14 UTC | 10m |
| CXK235 | CXK | Addington Field (4TX8) | Addington Field (4TX8) | 2026-04-19 16:12 UTC | 2026-04-19 16:12 UTC | 0m |
| N723KP |  | Boeing Field/King County International Airport (KBFI) | Florence Municipal Airport (K6S2) | 2026-04-19 14:57 UTC | 2026-04-19 16:12 UTC | 1h 14m |
| SAS96D | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Bodø Airport (ENBO) | 2026-04-19 15:08 UTC | 2026-04-19 16:11 UTC | 1h 3m |
| SCU35 | SCU | Tulsa Riverside Airport (KRVS) | Haskell Airport (K2K9) | 2026-04-19 15:51 UTC | 2026-04-19 16:10 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
