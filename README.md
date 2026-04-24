# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_11:47:57_UTC-green)

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

**Latest saved flight:** 2026-04-24 11:47:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 11:47:57 UTC

- **51,069** saved flights
- **20,458** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **51,069** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **611,424.9 tonnes** estimated CO2 emissions
- **35,444,922 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2154 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1192 |
| 4 | EJA | 878 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 723 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 595 |
| 9 | Vueling | 513 |
| 10 | AXM | 506 |
| 11 | LATAM Airlines | 495 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 432 |
| 14 | WIF | 421 |
| 15 | Delta Air Lines | 419 |
| 16 | QLK | 412 |
| 17 | Swiss International | 389 |
| 18 | LXJ | 382 |
| 19 | AEE | 345 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 326 |
| 22 | easyJet | 324 |
| 23 | VIV | 322 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 291 |
| 26 | AXB | 275 |
| 27 | Cathay Pacific | 269 |
| 28 | AIQ | 263 |
| 29 | JetBlue | 263 |
| 30 | United Airlines | 263 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40401 |
| 2 | 🇮🇳 IN | 3746 |
| 3 | 🇪🇸 ES | 3703 |
| 4 | 🇦🇺 AU | 3568 |
| 5 | 🇧🇷 BR | 2948 |
| 6 | 🇯🇵 JP | 2806 |
| 7 | 🇮🇹 IT | 2733 |
| 8 | 🇩🇪 DE | 2729 |
| 9 | 🇨🇦 CA | 2545 |
| 10 | 🇨🇴 CO | 2347 |
| 11 | 🇬🇧 GB | 2122 |
| 12 | 🇫🇷 FR | 1959 |
| 13 | 🇲🇽 MX | 1571 |
| 14 | 🇬🇷 GR | 1550 |
| 15 | 🇨🇭 CH | 1416 |
| 16 | 🇳🇴 NO | 1374 |
| 17 | 🇲🇾 MY | 1236 |
| 18 | 🇿🇦 ZA | 1060 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 940 |
| 21 | 🇹🇷 TR | 916 |
| 22 | 🇵🇭 PH | 895 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 824 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 628 |
| 27 | 🇲🇪 ME | 548 |
| 28 | 🇳🇱 NL | 517 |
| 29 | 🇲🇴 MO | 485 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 954 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 803 |
| 5 | Indira Gandhi International Airport |  | IN | 799 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 766 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 667 |
| 9 | Zurich Airport |  | CH | 600 |
| 10 | Frankfurt am Main International Airport |  | DE | 578 |
| 11 | La Aurora Airport |  | GT | 574 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Kuala Lumpur International Airport |  | MY | 490 |
| 15 | Macau International Airport |  | MO | 485 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 17 | Madrid Barajas International Airport |  | ES | 467 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 443 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 424 |
| 22 | Malpensa International Airport |  | IT | 420 |
| 23 | Ninoy Aquino International Airport |  | PH | 413 |
| 24 | Tenerife Norte Airport |  | ES | 410 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Charles de Gaulle International Airport |  | FR | 383 |
| 27 | Salt Lake City International Airport |  | US | 377 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 376 |
| 29 | Daniel K Inouye International Airport |  | US | 374 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 347 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 342 |
| 34 | Reno/Tahoe International Airport |  | US | 342 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 36 | Barcelona International Airport |  | ES | 341 |
| 37 | O. R. Tambo International Airport |  | ZA | 340 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 310 |
| 40 | Viracopos International Airport |  | BR | 300 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 194 | 14m | 114 km | 380.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 153 | 21m | 244 km | 644.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 128 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 119 | 26m | 275 km | 563.9 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 91 | 1h 12m | 770 km | 1,208.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 87 | 20m | 250 km | 375.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 83 | 26m | 215 km | 307.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 81 | 20m | 147 km | 205.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N541WS |  | Trenton Mercer Airport (KTTN) | Atlantic City International Airport (KACY) | 2026-04-24 10:59 UTC | 2026-04-24 11:47 UTC | 48m |
| HB2475 |  | Lodrino Air Base (LSML) | Ambri Airport (LSPM) | 2026-04-24 11:36 UTC | 2026-04-24 11:47 UTC | 11m |
| N704VY |  | FL63 (FL63) | Lake City Airpark (FL27) | 2026-04-24 10:14 UTC | 2026-04-24 11:45 UTC | 1h 30m |
| TCCZD | TCC | Paris-Le Bourget Airport (LFPB) | Istanbul Hezarfen Airfield (LTBW) | 2026-04-24 09:01 UTC | 2026-04-24 11:40 UTC | 2h 39m |
| LFA539 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-04-24 11:15 UTC | 2026-04-24 11:34 UTC | 19m |
| PHCOB | PHC | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-24 11:02 UTC | 2026-04-24 11:32 UTC | 29m |
| ETD99P | Etihad Airways | Munich International Airport (EDDM) | Queen Alia International Airport (OJAI) | 2026-04-24 08:30 UTC | 2026-04-24 11:30 UTC | 3h 0m |
| GAWGB | GAW | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-04-24 11:18 UTC | 2026-04-24 11:21 UTC | 3m |
| AFR12HA | Air France | Charles de Gaulle International Airport (LFPG) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-24 08:30 UTC | 2026-04-24 11:21 UTC | 2h 50m |
| IGO235H | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Gaya Airport (VEGY) | 2026-04-24 10:37 UTC | 2026-04-24 11:10 UTC | 33m |
| RYR53CB | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Memmingen Allgau Airport (EDJA) | 2026-04-24 09:44 UTC | 2026-04-24 11:09 UTC | 1h 24m |
| HBZYT | HBZ | Raron Airport (LSTA) | LSMF (LSMF) | 2026-04-24 10:24 UTC | 2026-04-24 11:09 UTC | 44m |
| GMA03 | GMA | Aberdeen Dyce Airport (EGPD) | Wick Airport (EGPC) | 2026-04-24 10:48 UTC | 2026-04-24 11:08 UTC | 20m |
| THA136 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-04-24 10:11 UTC | 2026-04-24 11:04 UTC | 53m |
| PSVTS | PSV | Campo de Marte Airport (SBMT) | Cascavel Airport (SBCA) | 2026-04-24 09:25 UTC | 2026-04-24 11:04 UTC | 1h 39m |
| WIF75Y | WIF | Stavanger Airport Sola (ENZV) | Trondheim Airport Vaernes (ENVA) | 2026-04-24 09:44 UTC | 2026-04-24 11:03 UTC | 1h 18m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-24 10:25 UTC | 2026-04-24 11:01 UTC | 36m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Catanduva Airport (SDCD) | 2026-04-24 10:28 UTC | 2026-04-24 11:01 UTC | 33m |
| ETP08 | ETP | MoD Boscombe Down Airport (EGDM) | MoD Boscombe Down Airport (EGDM) | 2026-04-24 10:01 UTC | 2026-04-24 10:57 UTC | 56m |
| AIQ3310 | AIQ | Don Mueang International Airport (VTBD) | Takhli Airport (VTPI) | 2026-04-24 10:38 UTC | 2026-04-24 10:54 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
