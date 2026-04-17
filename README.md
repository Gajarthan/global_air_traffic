# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_19:53:32_UTC-green)

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

**Latest saved flight:** 2026-04-17 19:53:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 19:53:32 UTC

- **39,911** saved flights
- **17,084** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,911** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **480,460.5 tonnes** estimated CO2 emissions
- **27,852,785 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1675 |
| 2 | SkyWest Airlines | 1557 |
| 3 | IndiGo | 977 |
| 4 | EJA | 692 |
| 5 | American Airlines | 668 |
| 6 | Southwest Airlines | 559 |
| 7 | ENY | 515 |
| 8 | AXM | 413 |
| 9 | Vueling | 400 |
| 10 | LATAM Airlines | 395 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 354 |
| 13 | All Nippon Airways | 351 |
| 14 | Delta Air Lines | 340 |
| 15 | QLK | 327 |
| 16 | LXJ | 317 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 266 |
| 20 | AEE | 265 |
| 21 | easyJet | 263 |
| 22 | EJU | 260 |
| 23 | VIV | 255 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 227 |
| 26 | United Airlines | 220 |
| 27 | EDV | 215 |
| 28 | JetBlue | 212 |
| 29 | GLO | 208 |
| 30 | AIQ | 203 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 31581 |
| 2 | 🇮🇳 IN | 2980 |
| 3 | 🇪🇸 ES | 2965 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2362 |
| 6 | 🇯🇵 JP | 2131 |
| 7 | 🇮🇹 IT | 2088 |
| 8 | 🇩🇪 DE | 2016 |
| 9 | 🇨🇦 CA | 1957 |
| 10 | 🇨🇴 CO | 1929 |
| 11 | 🇬🇧 GB | 1634 |
| 12 | 🇫🇷 FR | 1529 |
| 13 | 🇲🇽 MX | 1254 |
| 14 | 🇬🇷 GR | 1200 |
| 15 | 🇨🇭 CH | 1099 |
| 16 | 🇳🇴 NO | 1005 |
| 17 | 🇲🇾 MY | 1003 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 702 |
| 23 | 🇬🇹 GT | 680 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 620 |
| 26 | 🇲🇦 MA | 491 |
| 27 | 🇳🇱 NL | 404 |
| 28 | 🇲🇪 ME | 397 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 927 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 677 |
| 4 | Denver International Airport |  | US | 661 |
| 5 | Indira Gandhi International Airport |  | IN | 640 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 597 |
| 7 | Harry Reid International Airport |  | US | 516 |
| 8 | Guaymaral Airport |  | CO | 511 |
| 9 | La Aurora Airport |  | GT | 500 |
| 10 | Zurich Airport |  | CH | 484 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 392 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 391 |
| 14 | Chicago O'Hare International Airport |  | US | 389 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 363 |
| 17 | Madrid Barajas International Airport |  | ES | 361 |
| 18 | Tenerife Norte Airport |  | ES | 356 |
| 19 | Charlotte/Douglas International Airport |  | US | 354 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 348 |
| 22 | Congonhas Airport |  | BR | 346 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 323 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 310 |
| 26 | Salt Lake City International Airport |  | US | 307 |
| 27 | Daniel K Inouye International Airport |  | US | 296 |
| 28 | Charles de Gaulle International Airport |  | FR | 294 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Vitoria/Foronda Airport |  | ES | 276 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 276 |
| 32 | Capua Airport |  | IT | 274 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 271 |
| 34 | Reno/Tahoe International Airport |  | US | 270 |
| 35 | O. R. Tambo International Airport |  | ZA | 265 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 265 |
| 37 | Barcelona International Airport |  | ES | 256 |
| 38 | Viracopos International Airport |  | BR | 243 |
| 39 | Don Mueang International Airport |  | TH | 240 |
| 40 | Calgary International Airport |  | CA | 239 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 205 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 159 | 14m | 114 km | 311.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 103 | 21m | 244 km | 433.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 100 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 63 | 52m | 556 km | 603.9 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 57 | 1h 53m | 1,304 km | 1,282.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 55 | 1h 20m | 961 km | 911.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGVPT | FGV | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-17 19:19 UTC | 2026-04-17 19:53 UTC | 34m |
| N213AN |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-17 19:26 UTC | 2026-04-17 19:45 UTC | 19m |
| N256AA |  | Mefford Field (KTLR) | Meadows Field (KBFL) | 2026-04-17 19:22 UTC | 2026-04-17 19:40 UTC | 18m |
| N471AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-17 18:44 UTC | 2026-04-17 19:39 UTC | 54m |
| N98561 |  | Butler County Regional/Hogan Field (KHAO) | Richmond Municipal Airport (KRID) | 2026-04-17 19:23 UTC | 2026-04-17 19:39 UTC | 15m |
| N1213P |  | Reno/Tahoe International Airport (KRNO) | Pleasant Valley Airport (5CO8) | 2026-04-17 17:48 UTC | 2026-04-17 19:39 UTC | 1h 50m |
| MNL14 | MNL | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-04-17 19:04 UTC | 2026-04-17 19:38 UTC | 34m |
| N357EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-17 18:29 UTC | 2026-04-17 19:38 UTC | 1h 8m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-17 18:51 UTC | 2026-04-17 19:36 UTC | 44m |
| N1743L |  | Allegheny County Airport (KAGC) | Allegheny County Airport (KAGC) | 2026-04-17 19:13 UTC | 2026-04-17 19:35 UTC | 21m |
| N68767 |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-17 19:33 UTC | 2026-04-17 19:34 UTC | 1m |
| N46SD |  | Ashland Regional Airport (KDWU) | Ashland Regional Airport (KDWU) | 2026-04-17 18:34 UTC | 2026-04-17 19:32 UTC | 57m |
| N414UH |  | UT13 (UT13) | UT08 (UT08) | 2026-04-17 19:19 UTC | 2026-04-17 19:29 UTC | 10m |
| N993DT |  | Rogue Valley International/Medford Airport (KMFR) | Siskiyou County Airport (KSIY) | 2026-04-17 19:13 UTC | 2026-04-17 19:28 UTC | 14m |
| RYR104A | Ryanair | Stockholm-Arlanda Airport (ESSA) | Borglanda Airport (ESMB) | 2026-04-17 18:55 UTC | 2026-04-17 19:25 UTC | 29m |
| EJA518 | EJA | Teterboro Airport (KTEB) | Tweed/New Haven Airport (KHVN) | 2026-04-17 19:01 UTC | 2026-04-17 19:25 UTC | 23m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-17 19:11 UTC | 2026-04-17 19:24 UTC | 13m |
| N3288 |  | Half Moon Bay Airport (KHAF) | Palo Alto Airport (KPAO) | 2026-04-17 18:58 UTC | 2026-04-17 19:22 UTC | 24m |
| N995AX |  | Cliff Dwellers Airport (AZ03) | Quanah Municipal Airport (KF01) | 2026-04-17 17:40 UTC | 2026-04-17 19:21 UTC | 1h 41m |
| N34EF |  | Princeton Airport (K39N) | Trenton-Robbinsville Airport (KN87) | 2026-04-17 18:37 UTC | 2026-04-17 19:20 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
