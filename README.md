# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_17:59:22_UTC-green)

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

**Latest saved flight:** 2026-04-23 17:59:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 17:59:22 UTC

- **50,136** saved flights
- **20,190** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,136** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **598,020.6 tonnes** estimated CO2 emissions
- **34,667,863 km** total distance flown
- **831 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2125 |
| 2 | SkyWest Airlines | 1919 |
| 3 | IndiGo | 1169 |
| 4 | EJA | 864 |
| 5 | American Airlines | 815 |
| 6 | Southwest Airlines | 709 |
| 7 | ENY | 642 |
| 8 | Lufthansa | 580 |
| 9 | Vueling | 501 |
| 10 | AXM | 495 |
| 11 | LATAM Airlines | 487 |
| 12 | All Nippon Airways | 455 |
| 13 | AZU | 426 |
| 14 | WIF | 417 |
| 15 | Delta Air Lines | 412 |
| 16 | QLK | 404 |
| 17 | LXJ | 378 |
| 18 | Swiss International | 376 |
| 19 | AEE | 343 |
| 20 | Alaska Airlines | 332 |
| 21 | EJU | 325 |
| 22 | easyJet | 317 |
| 23 | VIV | 316 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 284 |
| 26 | AXB | 268 |
| 27 | JetBlue | 263 |
| 28 | United Airlines | 261 |
| 29 | Cathay Pacific | 259 |
| 30 | AIQ | 256 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39794 |
| 2 | 🇮🇳 IN | 3667 |
| 3 | 🇪🇸 ES | 3631 |
| 4 | 🇦🇺 AU | 3471 |
| 5 | 🇧🇷 BR | 2910 |
| 6 | 🇯🇵 JP | 2739 |
| 7 | 🇮🇹 IT | 2693 |
| 8 | 🇩🇪 DE | 2678 |
| 9 | 🇨🇦 CA | 2478 |
| 10 | 🇨🇴 CO | 2328 |
| 11 | 🇬🇧 GB | 2063 |
| 12 | 🇫🇷 FR | 1923 |
| 13 | 🇲🇽 MX | 1545 |
| 14 | 🇬🇷 GR | 1530 |
| 15 | 🇨🇭 CH | 1383 |
| 16 | 🇳🇴 NO | 1346 |
| 17 | 🇲🇾 MY | 1207 |
| 18 | 🇿🇦 ZA | 1038 |
| 19 | 🇳🇿 NZ | 956 |
| 20 | 🇹🇭 TH | 914 |
| 21 | 🇹🇷 TR | 888 |
| 22 | 🇵🇭 PH | 872 |
| 23 | 🇰🇷 KR | 827 |
| 24 | 🇵🇱 PL | 811 |
| 25 | 🇬🇹 GT | 765 |
| 26 | 🇲🇦 MA | 618 |
| 27 | 🇲🇪 ME | 536 |
| 28 | 🇳🇱 NL | 507 |
| 29 | 🇲🇴 MO | 460 |
| 30 | 🇧🇸 BS | 441 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1162 |
| 2 | Tokyo International Airport |  | JP | 930 |
| 3 | Denver International Airport |  | US | 832 |
| 4 | El Dorado International Airport |  | CO | 795 |
| 5 | Indira Gandhi International Airport |  | IN | 784 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 756 |
| 7 | Guaymaral Airport |  | CO | 686 |
| 8 | Harry Reid International Airport |  | US | 648 |
| 9 | Zurich Airport |  | CH | 586 |
| 10 | La Aurora Airport |  | GT | 570 |
| 11 | Frankfurt am Main International Airport |  | DE | 559 |
| 12 | Chicago O'Hare International Airport |  | US | 496 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 490 |
| 14 | Kuala Lumpur International Airport |  | MY | 482 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 475 |
| 16 | Macau International Airport |  | MO | 460 |
| 17 | Madrid Barajas International Airport |  | ES | 457 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 19 | Bengaluru International Airport |  | IN | 438 |
| 20 | Charlotte/Douglas International Airport |  | US | 421 |
| 21 | Congonhas Airport |  | BR | 417 |
| 22 | Malpensa International Airport |  | IT | 412 |
| 23 | Tenerife Norte Airport |  | ES | 408 |
| 24 | Ninoy Aquino International Airport |  | PH | 402 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 379 |
| 26 | Salt Lake City International Airport |  | US | 374 |
| 27 | Charles de Gaulle International Airport |  | FR | 374 |
| 28 | Daniel K Inouye International Airport |  | US | 371 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 341 |
| 32 | Vitoria/Foronda Airport |  | ES | 340 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 339 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 337 |
| 35 | Reno/Tahoe International Airport |  | US | 334 |
| 36 | O. R. Tambo International Airport |  | ZA | 332 |
| 37 | Barcelona International Airport |  | ES | 332 |
| 38 | Don Mueang International Airport |  | TH | 311 |
| 39 | Calgary International Airport |  | CA | 300 |
| 40 | Viracopos International Airport |  | BR | 296 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 235 | 1h 7m | 706 km | 2,861.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 192 | 14m | 114 km | 376.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 151 | 21m | 244 km | 635.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 149 | 28m | 304 km | 781.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 120 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 103 | 44m | 452 km | 802.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 86 | 20m | 250 km | 371.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 78 | 52m | 556 km | 747.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 70 | 1h 0m | 695 km | 839.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 66 | 11m | 15 km | 17.4 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-04-23 17:45 UTC | 2026-04-23 17:59 UTC | 13m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-23 17:44 UTC | 2026-04-23 17:59 UTC | 14m |
| MTU82 | MTU | Murfreesboro Municipal Airport (KMBT) | Long Meadow Airstrip (TN65) | 2026-04-23 17:38 UTC | 2026-04-23 17:56 UTC | 17m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-23 17:29 UTC | 2026-04-23 17:54 UTC | 25m |
| SCARY71 | SCA | Randolph Afb Airport (KRND) | San Christoval Ranch Airport (XS71) | 2026-04-23 17:23 UTC | 2026-04-23 17:54 UTC | 31m |
| N553XB |  | New York Stewart International Airport (KSWF) | Newark Liberty International Airport (KEWR) | 2026-04-23 17:30 UTC | 2026-04-23 17:49 UTC | 19m |
| SFE1 | SFE | Hank Sasser/Breakaway Airport (40XS) | Bud Dryden Airport (TX05) | 2026-04-23 17:34 UTC | 2026-04-23 17:43 UTC | 9m |
| AMMO83 | AMM | Boron Airstrip (57CL) | Boron Airstrip (57CL) | 2026-04-23 16:17 UTC | 2026-04-23 17:43 UTC | 1h 26m |
| N433FR |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-04-23 17:27 UTC | 2026-04-23 17:42 UTC | 15m |
| N96575 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-23 17:18 UTC | 2026-04-23 17:42 UTC | 23m |
| MYSTIC49 | MYS | John Murtha Johnstown/Cambria County Airport (KJST) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-04-23 17:21 UTC | 2026-04-23 17:38 UTC | 17m |
| N823SF |  | Marco Island Executive Airport (KMKY) | London/Corbin/Magee Airport (KLOZ) | 2026-04-23 15:02 UTC | 2026-04-23 17:38 UTC | 2h 36m |
| N48BF |  | KU77 (KU77) | KU77 (KU77) | 2026-04-23 17:27 UTC | 2026-04-23 17:38 UTC | 10m |
| N15102 |  | Van Dyke Strip (25CL) | Sanborn Airport (38CN) | 2026-04-23 17:22 UTC | 2026-04-23 17:35 UTC | 13m |
| 170281 |  | Mesa Gateway Airport (KIWA) | Four Pillars Airport (AZ21) | 2026-04-23 16:57 UTC | 2026-04-23 17:35 UTC | 37m |
| CXK579 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-04-23 17:16 UTC | 2026-04-23 17:33 UTC | 16m |
| N123FA |  | Sacramento Executive Airport (KSAC) | Sacramento Executive Airport (KSAC) | 2026-04-23 17:18 UTC | 2026-04-23 17:33 UTC | 14m |
| RN156 |  | J-22 Ranch Airport (16FL) | Flomaton Airport (0AL5) | 2026-04-23 16:42 UTC | 2026-04-23 17:32 UTC | 49m |
| WIRE31 | WIR | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-04-23 17:04 UTC | 2026-04-23 17:30 UTC | 25m |
| EJA831 | EJA | Fort Lauderdale/Hollywood International Airport (KFLL) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-23 15:27 UTC | 2026-04-23 17:29 UTC | 2h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
