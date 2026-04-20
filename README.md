# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_22:59:04_UTC-green)

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

**Latest saved flight:** 2026-04-20 22:59:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 22:59:04 UTC

- **46,077** saved flights
- **18,979** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,077** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **556,062.8 tonnes** estimated CO2 emissions
- **32,235,522 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1957 |
| 2 | SkyWest Airlines | 1788 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 799 |
| 5 | American Airlines | 765 |
| 6 | Southwest Airlines | 668 |
| 7 | ENY | 600 |
| 8 | Lufthansa | 477 |
| 9 | Vueling | 465 |
| 10 | AXM | 458 |
| 11 | LATAM Airlines | 455 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 395 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 368 |
| 16 | WIF | 362 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 355 |
| 19 | Alaska Airlines | 317 |
| 20 | AEE | 313 |
| 21 | EJU | 308 |
| 22 | VIV | 296 |
| 23 | easyJet | 292 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 263 |
| 26 | JetBlue | 247 |
| 27 | Cathay Pacific | 246 |
| 28 | United Airlines | 244 |
| 29 | AXB | 240 |
| 30 | GLO | 236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36690 |
| 2 | 🇮🇳 IN | 3384 |
| 3 | 🇪🇸 ES | 3378 |
| 4 | 🇦🇺 AU | 3147 |
| 5 | 🇧🇷 BR | 2704 |
| 6 | 🇯🇵 JP | 2491 |
| 7 | 🇮🇹 IT | 2490 |
| 8 | 🇩🇪 DE | 2366 |
| 9 | 🇨🇦 CA | 2244 |
| 10 | 🇨🇴 CO | 2124 |
| 11 | 🇬🇧 GB | 1890 |
| 12 | 🇫🇷 FR | 1749 |
| 13 | 🇲🇽 MX | 1436 |
| 14 | 🇬🇷 GR | 1403 |
| 15 | 🇨🇭 CH | 1254 |
| 16 | 🇳🇴 NO | 1152 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 903 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇵🇭 PH | 813 |
| 22 | 🇹🇷 TR | 813 |
| 23 | 🇰🇷 KR | 747 |
| 24 | 🇬🇹 GT | 734 |
| 25 | 🇵🇱 PL | 732 |
| 26 | 🇲🇦 MA | 569 |
| 27 | 🇲🇪 ME | 485 |
| 28 | 🇳🇱 NL | 468 |
| 29 | 🇲🇴 MO | 433 |
| 30 | 🇧🇸 BS | 419 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1086 |
| 2 | Tokyo International Airport |  | JP | 850 |
| 3 | Denver International Airport |  | US | 767 |
| 4 | El Dorado International Airport |  | CO | 740 |
| 5 | Indira Gandhi International Airport |  | IN | 731 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 698 |
| 7 | Harry Reid International Airport |  | US | 597 |
| 8 | Guaymaral Airport |  | CO | 583 |
| 9 | Zurich Airport |  | CH | 549 |
| 10 | La Aurora Airport |  | GT | 542 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 459 |
| 12 | Chicago O'Hare International Airport |  | US | 457 |
| 13 | Frankfurt am Main International Airport |  | DE | 450 |
| 14 | Kuala Lumpur International Airport |  | MY | 449 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 446 |
| 16 | Macau International Airport |  | MO | 433 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 422 |
| 18 | Madrid Barajas International Airport |  | ES | 412 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 396 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 385 |
| 24 | Ninoy Aquino International Airport |  | PH | 377 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 351 |
| 26 | Daniel K Inouye International Airport |  | US | 345 |
| 27 | Salt Lake City International Airport |  | US | 342 |
| 28 | Charles de Gaulle International Airport |  | FR | 341 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 30 | Capua Airport |  | IT | 334 |
| 31 | Reno/Tahoe International Airport |  | US | 320 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 318 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 317 |
| 34 | Vitoria/Foronda Airport |  | ES | 317 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 311 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 303 |
| 38 | Calgary International Airport |  | CA | 278 |
| 39 | Viracopos International Airport |  | BR | 276 |
| 40 | Don Mueang International Airport |  | TH | 275 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 214 | 1h 7m | 706 km | 2,605.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 172 | 14m | 114 km | 337.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 133 | 21m | 244 km | 560.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 81 | 31m | 369 km | 515.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 71 | 26m | 215 km | 263.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 68 | 13m | 99 km | 116.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 52m | 1,304 km | 1,439.8 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N19886 |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-04-20 22:20 UTC | 2026-04-20 22:59 UTC | 39m |
| N393EA |  | K00V (K00V) | Aero Bear Field (CD23) | 2026-04-20 22:19 UTC | 2026-04-20 22:53 UTC | 34m |
| ZMV | ZMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-20 22:39 UTC | 2026-04-20 22:53 UTC | 14m |
| N189K |  | Flying M Airport (2NC6) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-20 21:58 UTC | 2026-04-20 22:49 UTC | 51m |
| N734VC |  | John C Tune Airport (KJWN) | Rachel's Landing Airport (8TN6) | 2026-04-20 21:59 UTC | 2026-04-20 22:41 UTC | 41m |
| TKR131 | TKR | Mesa Gateway Airport (KIWA) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-04-20 22:10 UTC | 2026-04-20 22:36 UTC | 26m |
| N911WJ |  | Market World Airport (FL16) | Lakeland Linder International Airport (KLAL) | 2026-04-20 21:33 UTC | 2026-04-20 22:34 UTC | 1h 1m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-04-20 11:39 UTC | 2026-04-20 22:31 UTC | 10h 52m |
| N642RG |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-20 22:10 UTC | 2026-04-20 22:31 UTC | 21m |
| N441WF |  | Centennial Airport (KAPA) | Eads Municipal Airport (K9V7) | 2026-04-20 21:59 UTC | 2026-04-20 22:30 UTC | 31m |
| N6896H |  | Dupage Airport (KDPA) | IS47 (IS47) | 2026-04-20 21:47 UTC | 2026-04-20 22:30 UTC | 42m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-20 10:44 UTC | 2026-04-20 22:28 UTC | 11h 44m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-04-20 22:19 UTC | 2026-04-20 22:25 UTC | 5m |
| N445LF |  | Pru Field (K33S) | Felts Field (KSFF) | 2026-04-20 22:00 UTC | 2026-04-20 22:23 UTC | 23m |
| N799TH |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-20 20:58 UTC | 2026-04-20 22:23 UTC | 1h 24m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-20 11:48 UTC | 2026-04-20 22:19 UTC | 10h 31m |
| N9382W |  | City Of Colorado Springs Municipal Airport (KCOS) | Telluride Regional Airport (KTEX) | 2026-04-20 20:47 UTC | 2026-04-20 22:17 UTC | 1h 30m |
| CPA2040 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-20 10:37 UTC | 2026-04-20 22:13 UTC | 11h 35m |
| N157U |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-04-20 21:31 UTC | 2026-04-20 22:12 UTC | 41m |
| N73719 |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-04-20 21:11 UTC | 2026-04-20 22:12 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
