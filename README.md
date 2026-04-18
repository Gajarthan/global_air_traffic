# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_13:12:27_UTC-green)

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

**Latest saved flight:** 2026-04-18 13:12:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 13:12:27 UTC

- **41,116** saved flights
- **17,393** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,116** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **494,678.2 tonnes** estimated CO2 emissions
- **28,676,997 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1732 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 1017 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 431 |
| 9 | Vueling | 412 |
| 10 | LATAM Airlines | 404 |
| 11 | Lufthansa | 399 |
| 12 | All Nippon Airways | 376 |
| 13 | AZU | 364 |
| 14 | Delta Air Lines | 348 |
| 15 | QLK | 341 |
| 16 | LXJ | 325 |
| 17 | WIF | 322 |
| 18 | Swiss International | 315 |
| 19 | Alaska Airlines | 277 |
| 20 | AEE | 274 |
| 21 | EJU | 270 |
| 22 | easyJet | 268 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 234 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 221 |
| 28 | EDV | 216 |
| 29 | AXB | 214 |
| 30 | GLO | 213 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32328 |
| 2 | 🇮🇳 IN | 3102 |
| 3 | 🇪🇸 ES | 3035 |
| 4 | 🇦🇺 AU | 2912 |
| 5 | 🇧🇷 BR | 2437 |
| 6 | 🇯🇵 JP | 2287 |
| 7 | 🇮🇹 IT | 2142 |
| 8 | 🇩🇪 DE | 2076 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1954 |
| 11 | 🇬🇧 GB | 1671 |
| 12 | 🇫🇷 FR | 1585 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1241 |
| 15 | 🇨🇭 CH | 1143 |
| 16 | 🇲🇾 MY | 1047 |
| 17 | 🇳🇴 NO | 1022 |
| 18 | 🇿🇦 ZA | 855 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 754 |
| 21 | 🇹🇭 TH | 737 |
| 22 | 🇹🇷 TR | 720 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 686 |
| 25 | 🇵🇱 PL | 651 |
| 26 | 🇲🇦 MA | 503 |
| 27 | 🇳🇱 NL | 421 |
| 28 | 🇲🇪 ME | 419 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 782 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 678 |
| 5 | Indira Gandhi International Airport |  | IN | 668 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 616 |
| 7 | Harry Reid International Airport |  | US | 531 |
| 8 | Guaymaral Airport |  | CO | 518 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 498 |
| 11 | Kuala Lumpur International Airport |  | MY | 412 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 392 |
| 16 | Macau International Airport |  | MO | 375 |
| 17 | Madrid Barajas International Airport |  | ES | 371 |
| 18 | Frankfurt am Main International Airport |  | DE | 366 |
| 19 | Bengaluru International Airport |  | IN | 366 |
| 20 | Tenerife Norte Airport |  | ES | 361 |
| 21 | Charlotte/Douglas International Airport |  | US | 358 |
| 22 | Congonhas Airport |  | BR | 354 |
| 23 | Ninoy Aquino International Airport |  | PH | 350 |
| 24 | Malpensa International Airport |  | IT | 334 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 306 |
| 28 | Charles de Gaulle International Airport |  | FR | 303 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 297 |
| 30 | Vitoria/Foronda Airport |  | ES | 288 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 284 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 284 |
| 33 | Reno/Tahoe International Airport |  | US | 280 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 278 |
| 35 | O. R. Tambo International Airport |  | ZA | 277 |
| 36 | Capua Airport |  | IT | 274 |
| 37 | Barcelona International Airport |  | ES | 263 |
| 38 | Viracopos International Airport |  | BR | 250 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Don Mueang International Airport |  | TH | 245 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 207 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 111 | 19m | 165 km | 315.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 109 | 21m | 244 km | 459.0 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 97 | 26m | 275 km | 459.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 67 | 20m | 250 km | 289.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 65 | 20m | 147 km | 164.5 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 62 | 16m | 162 km | 173.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGJBC | FGJ | Quiberon Airport (LFEQ) | Quiberon Airport (LFEQ) | 2026-04-18 13:01 UTC | 2026-04-18 13:12 UTC | 10m |
| HB3500 |  | Lodrino Air Base (LSML) | Ambri Airport (LSPM) | 2026-04-18 12:20 UTC | 2026-04-18 13:03 UTC | 42m |
| N824KS |  | Boca Raton Airport (KBCT) | Duda Airstrip (FA69) | 2026-04-18 12:31 UTC | 2026-04-18 13:01 UTC | 29m |
| ANA99 | All Nippon Airways | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-18 12:19 UTC | 2026-04-18 12:58 UTC | 39m |
| ERU894 | ERU | Daytona Beach International Airport (KDAB) | FL47 (FL47) | 2026-04-18 12:14 UTC | 2026-04-18 12:53 UTC | 38m |
| N74KM |  | Austin Executive Airport (KEDC) | Tin Top Ranch Airport (3TA4) | 2026-04-18 12:27 UTC | 2026-04-18 12:51 UTC | 23m |
| FXC22 | FXC | Westchester County Airport (KHPN) | Teterboro Airport (KTEB) | 2026-04-18 12:36 UTC | 2026-04-18 12:48 UTC | 12m |
| N307CM |  | KORC (KORC) | Laramie Regional Airport (KLAR) | 2026-04-18 11:10 UTC | 2026-04-18 12:45 UTC | 1h 34m |
| DFLIP | DFL | Hodkovice Nad Mohelkou Airport (LKHD) | Hodkovice Nad Mohelkou Airport (LKHD) | 2026-04-18 11:54 UTC | 2026-04-18 12:42 UTC | 48m |
| D6907 |  | Ambri Airport (LSPM) | Muenster Aero Airport (LSPU) | 2026-04-18 11:40 UTC | 2026-04-18 12:37 UTC | 57m |
| ANA97 | All Nippon Airways | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-18 11:59 UTC | 2026-04-18 12:36 UTC | 36m |
| JAL229 | Japan Airlines | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-18 11:55 UTC | 2026-04-18 12:32 UTC | 37m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-18 11:54 UTC | 2026-04-18 12:31 UTC | 37m |
| SBE560 | SBE | Dallas Love Field (KDAL) | 5XS7 (5XS7) | 2026-04-18 11:36 UTC | 2026-04-18 12:30 UTC | 54m |
| DLH3LC | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-18 11:55 UTC | 2026-04-18 12:29 UTC | 33m |
| ZSGAK | ZSG | Barcelonnette - Saint-Pons Airport (LFMR) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-18 11:39 UTC | 2026-04-18 12:28 UTC | 48m |
| APJ312 | APJ | Narita International Airport (RJAA) | Kansai International Airport (RJBB) | 2026-04-18 11:37 UTC | 2026-04-18 12:24 UTC | 46m |
| IGO477H | IndiGo | Bengaluru International Airport (VOBL) | Bharkot Airport (VI82) | 2026-04-18 09:57 UTC | 2026-04-18 12:20 UTC | 2h 22m |
| PSVTA | PSV | Campo de Marte Airport (SBMT) | Monte Verde Airport (SNEJ) | 2026-04-18 12:04 UTC | 2026-04-18 12:18 UTC | 14m |
| N9886K |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-04-18 11:44 UTC | 2026-04-18 12:17 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
