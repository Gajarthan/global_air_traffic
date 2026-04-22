# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_16:31:09_UTC-green)

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

**Latest saved flight:** 2026-04-22 16:31:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 16:31:09 UTC

- **48,259** saved flights
- **19,604** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,259** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **579,132.0 tonnes** estimated CO2 emissions
- **33,572,872 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2054 |
| 2 | SkyWest Airlines | 1857 |
| 3 | IndiGo | 1137 |
| 4 | EJA | 830 |
| 5 | American Airlines | 796 |
| 6 | Southwest Airlines | 683 |
| 7 | ENY | 625 |
| 8 | Lufthansa | 543 |
| 9 | AXM | 481 |
| 10 | Vueling | 480 |
| 11 | LATAM Airlines | 473 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 412 |
| 14 | Delta Air Lines | 397 |
| 15 | WIF | 396 |
| 16 | QLK | 386 |
| 17 | LXJ | 371 |
| 18 | Swiss International | 368 |
| 19 | AEE | 329 |
| 20 | Alaska Airlines | 324 |
| 21 | EJU | 318 |
| 22 | easyJet | 309 |
| 23 | VIV | 306 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 272 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | JetBlue | 254 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 244 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 38260 |
| 2 | 🇮🇳 IN | 3547 |
| 3 | 🇪🇸 ES | 3499 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2821 |
| 6 | 🇯🇵 JP | 2646 |
| 7 | 🇮🇹 IT | 2620 |
| 8 | 🇩🇪 DE | 2538 |
| 9 | 🇨🇦 CA | 2371 |
| 10 | 🇨🇴 CO | 2242 |
| 11 | 🇬🇧 GB | 1998 |
| 12 | 🇫🇷 FR | 1843 |
| 13 | 🇲🇽 MX | 1489 |
| 14 | 🇬🇷 GR | 1486 |
| 15 | 🇨🇭 CH | 1321 |
| 16 | 🇳🇴 NO | 1266 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 1000 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 872 |
| 21 | 🇹🇷 TR | 849 |
| 22 | 🇵🇭 PH | 843 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 770 |
| 25 | 🇬🇹 GT | 753 |
| 26 | 🇲🇦 MA | 592 |
| 27 | 🇲🇪 ME | 518 |
| 28 | 🇳🇱 NL | 495 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 433 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1129 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 801 |
| 4 | El Dorado International Airport |  | CO | 774 |
| 5 | Indira Gandhi International Airport |  | IN | 751 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 735 |
| 7 | Guaymaral Airport |  | CO | 639 |
| 8 | Harry Reid International Airport |  | US | 627 |
| 9 | Zurich Airport |  | CH | 570 |
| 10 | La Aurora Airport |  | GT | 560 |
| 11 | Frankfurt am Main International Airport |  | DE | 515 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 478 |
| 13 | Chicago O'Hare International Airport |  | US | 473 |
| 14 | Kuala Lumpur International Airport |  | MY | 472 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 455 |
| 16 | Macau International Airport |  | MO | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 435 |
| 19 | Bengaluru International Airport |  | IN | 430 |
| 20 | Charlotte/Douglas International Airport |  | US | 413 |
| 21 | Congonhas Airport |  | BR | 405 |
| 22 | Tenerife Norte Airport |  | ES | 403 |
| 23 | Malpensa International Airport |  | IT | 402 |
| 24 | Ninoy Aquino International Airport |  | PH | 390 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 366 |
| 26 | Salt Lake City International Airport |  | US | 360 |
| 27 | Charles de Gaulle International Airport |  | FR | 357 |
| 28 | Daniel K Inouye International Airport |  | US | 356 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 354 |
| 30 | Capua Airport |  | IT | 352 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 331 |
| 32 | Reno/Tahoe International Airport |  | US | 329 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 327 |
| 34 | Vitoria/Foronda Airport |  | ES | 326 |
| 35 | O. R. Tambo International Airport |  | ZA | 322 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 320 |
| 37 | Barcelona International Airport |  | ES | 317 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Calgary International Airport |  | CA | 287 |
| 40 | Viracopos International Airport |  | BR | 286 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 256 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 184 | 14m | 114 km | 360.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 141 | 21m | 244 km | 593.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 117 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 113 | 26m | 275 km | 535.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 0m | 695 km | 815.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HNL05B | HNL | De Kooy Airport (EHKD) | Texel Airport (EHTX) | 2026-04-22 15:04 UTC | 2026-04-22 16:31 UTC | 1h 26m |
| ASA308 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Bermuda Dunes Airport (KUDD) | 2026-04-22 14:23 UTC | 2026-04-22 16:27 UTC | 2h 4m |
| CFNRM | CFN | Red Deer / South 40 Airstrip (CRD4) | Rocky Mountain House Airport (CYRM) | 2026-04-22 15:47 UTC | 2026-04-22 16:17 UTC | 30m |
| NHZ22 | NHZ | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-04-22 15:44 UTC | 2026-04-22 16:14 UTC | 29m |
| ERU897 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-04-22 15:23 UTC | 2026-04-22 16:13 UTC | 49m |
| FLC78 | FLC | Eppley Airfield (KOMA) | Offutt Afb Airport (KOFF) | 2026-04-22 13:45 UTC | 2026-04-22 16:11 UTC | 2h 26m |
| PFA328 | PFA | Vero Beach Regional Airport (KVRB) | Bartow Executive Airport (KBOW) | 2026-04-22 14:58 UTC | 2026-04-22 16:05 UTC | 1h 6m |
| N95422 |  | 00OH (00OH) | 00OH (00OH) | 2026-04-22 16:04 UTC | 2026-04-22 16:04 UTC | 0m |
| PNC0927 | PNC | Guaymaral Airport (SKGY) | El Dorado International Airport (SKBO) | 2026-04-22 15:40 UTC | 2026-04-22 16:01 UTC | 21m |
| CFCON | CFC | Campbell River Airport (CYBL) | Calgary International Airport (CYYC) | 2026-04-22 14:42 UTC | 2026-04-22 15:56 UTC | 1h 13m |
| MUSL | MUS | Joint Base Andrews Airport (KADW) | Garner Field (02MD) | 2026-04-22 15:06 UTC | 2026-04-22 15:55 UTC | 49m |
| XAA4938 | XAA | Harry Reid International Airport (KLAS) | Sandhill Ranch Airport (44AZ) | 2026-04-22 15:16 UTC | 2026-04-22 15:55 UTC | 39m |
| N472LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-22 14:31 UTC | 2026-04-22 15:54 UTC | 1h 22m |
| AIC4DM | Air India | Indira Gandhi International Airport (VIDP) | Biju Patnaik Airport (VEBS) | 2026-04-22 14:05 UTC | 2026-04-22 15:49 UTC | 1h 43m |
|  |  | Jacksonville Nas (Towers Field) Airport (KNIP) | Birmingham-Shuttlesworth International Airport (KBHM) | 2026-04-22 12:53 UTC | 2026-04-22 15:49 UTC | 2h 55m |
| N729LS |  | Centennial Airport (KAPA) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-04-22 14:11 UTC | 2026-04-22 15:48 UTC | 1h 36m |
| N7261Y |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-04-22 14:56 UTC | 2026-04-22 15:47 UTC | 51m |
| N65501 |  | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-04-22 15:45 UTC | 2026-04-22 15:46 UTC | 0m |
| AUR214 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-22 15:33 UTC | 2026-04-22 15:46 UTC | 13m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-22 15:31 UTC | 2026-04-22 15:44 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
