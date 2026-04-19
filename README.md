# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_21:49:42_UTC-green)

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

**Latest saved flight:** 2026-04-19 21:49:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 21:49:42 UTC

- **44,195** saved flights
- **18,387** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,195** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **531,886.2 tonnes** estimated CO2 emissions
- **30,833,984 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1868 |
| 2 | SkyWest Airlines | 1722 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 766 |
| 5 | American Airlines | 734 |
| 6 | Southwest Airlines | 627 |
| 7 | ENY | 574 |
| 8 | AXM | 446 |
| 9 | Vueling | 443 |
| 10 | Lufthansa | 438 |
| 11 | LATAM Airlines | 438 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 385 |
| 14 | Delta Air Lines | 379 |
| 15 | QLK | 355 |
| 16 | LXJ | 352 |
| 17 | WIF | 344 |
| 18 | Swiss International | 339 |
| 19 | AEE | 301 |
| 20 | Alaska Airlines | 299 |
| 21 | EJU | 291 |
| 22 | easyJet | 284 |
| 23 | VIV | 282 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 235 |
| 28 | AXB | 232 |
| 29 | GLO | 231 |
| 30 | EDV | 225 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35051 |
| 2 | 🇮🇳 IN | 3300 |
| 3 | 🇪🇸 ES | 3257 |
| 4 | 🇦🇺 AU | 3036 |
| 5 | 🇧🇷 BR | 2632 |
| 6 | 🇯🇵 JP | 2413 |
| 7 | 🇮🇹 IT | 2342 |
| 8 | 🇩🇪 DE | 2240 |
| 9 | 🇨🇦 CA | 2149 |
| 10 | 🇨🇴 CO | 2043 |
| 11 | 🇬🇧 GB | 1793 |
| 12 | 🇫🇷 FR | 1683 |
| 13 | 🇲🇽 MX | 1378 |
| 14 | 🇬🇷 GR | 1360 |
| 15 | 🇨🇭 CH | 1204 |
| 16 | 🇳🇴 NO | 1095 |
| 17 | 🇲🇾 MY | 1090 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 881 |
| 20 | 🇵🇭 PH | 792 |
| 21 | 🇹🇷 TR | 781 |
| 22 | 🇹🇭 TH | 780 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 726 |
| 25 | 🇵🇱 PL | 702 |
| 26 | 🇲🇦 MA | 550 |
| 27 | 🇲🇪 ME | 466 |
| 28 | 🇳🇱 NL | 452 |
| 29 | 🇧🇸 BS | 411 |
| 30 | 🇲🇴 MO | 406 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1038 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 737 |
| 4 | El Dorado International Airport |  | CO | 713 |
| 5 | Indira Gandhi International Airport |  | IN | 711 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 676 |
| 7 | Harry Reid International Airport |  | US | 567 |
| 8 | Guaymaral Airport |  | CO | 559 |
| 9 | La Aurora Airport |  | GT | 536 |
| 10 | Zurich Airport |  | CH | 528 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 436 |
| 12 | Chicago O'Hare International Airport |  | US | 436 |
| 13 | Kuala Lumpur International Airport |  | MY | 432 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 430 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 406 |
| 18 | Madrid Barajas International Airport |  | ES | 393 |
| 19 | Bengaluru International Airport |  | IN | 392 |
| 20 | Tenerife Norte Airport |  | ES | 390 |
| 21 | Charlotte/Douglas International Airport |  | US | 384 |
| 22 | Congonhas Airport |  | BR | 376 |
| 23 | Malpensa International Airport |  | IT | 370 |
| 24 | Ninoy Aquino International Airport |  | PH | 367 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 335 |
| 26 | Salt Lake City International Airport |  | US | 334 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Daniel K Inouye International Airport |  | US | 326 |
| 29 | Charles de Gaulle International Airport |  | FR | 324 |
| 30 | Reno/Tahoe International Airport |  | US | 307 |
| 31 | Vitoria/Foronda Airport |  | ES | 307 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 306 |
| 33 | Capua Airport |  | IT | 305 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 300 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 285 |
| 38 | Calgary International Airport |  | CA | 267 |
| 39 | Viracopos International Airport |  | BR | 267 |
| 40 | Don Mueang International Airport |  | TH | 265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 123 | 21m | 244 km | 517.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 109 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 91 | 20m | 99 km | 155.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 61 | 1h 21m | 961 km | 1,011.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 0m | 695 km | 719.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VIV2034 | VIV | General Mariano Escobedo International Airport (MMMY) | Plan De Guadalupe International Airport (MMIO) | 2026-04-19 21:30 UTC | 2026-04-19 21:49 UTC | 19m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-19 10:39 UTC | 2026-04-19 21:48 UTC | 11h 9m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-19 17:46 UTC | 2026-04-19 21:47 UTC | 4h 0m |
| N172EL |  | Palo Alto Airport (KPAO) | Sacramento Executive Airport (KSAC) | 2026-04-19 21:06 UTC | 2026-04-19 21:45 UTC | 38m |
| N5539T |  | Cable Airport (KCCB) | Big Bear City Airport (KL35) | 2026-04-19 21:26 UTC | 2026-04-19 21:44 UTC | 17m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-19 10:55 UTC | 2026-04-19 21:42 UTC | 10h 46m |
| N872FS |  | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-04-19 20:57 UTC | 2026-04-19 21:36 UTC | 39m |
| GTI9445 | GTI | RAF Fairford (EGVA) | Macau International Airport (VMMC) | 2026-04-19 10:08 UTC | 2026-04-19 21:32 UTC | 11h 23m |
| N25BQ |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-19 20:44 UTC | 2026-04-19 21:31 UTC | 47m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-19 21:11 UTC | 2026-04-19 21:31 UTC | 19m |
| N29GB |  | Double Eagle Ii Airport (KAEG) | Double Eagle Ii Airport (KAEG) | 2026-04-19 21:16 UTC | 2026-04-19 21:30 UTC | 13m |
| N278AW |  | Addison Airport (KADS) | Pearson Field (AR13) | 2026-04-19 20:34 UTC | 2026-04-19 21:29 UTC | 54m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-04-19 21:11 UTC | 2026-04-19 21:29 UTC | 17m |
| OUA16 | OUA | Ada Regional Airport (KADH) | Fountainhead Lodge Airpark (K0F7) | 2026-04-19 20:56 UTC | 2026-04-19 21:29 UTC | 32m |
| N4409X |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-19 20:56 UTC | 2026-04-19 21:28 UTC | 31m |
| AWH97R | AWH | Speyer Airport (EDRY) | Kiel-Holtenau Airport (EDHK) | 2026-04-19 20:05 UTC | 2026-04-19 21:27 UTC | 1h 21m |
| VLG19XM | Vueling | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-04-19 21:10 UTC | 2026-04-19 21:26 UTC | 15m |
| KPO181 | KPO | Napa County Airport (KAPC) | North Valley Airport (9CA6) | 2026-04-19 20:56 UTC | 2026-04-19 21:25 UTC | 29m |
| N3288 |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-19 20:36 UTC | 2026-04-19 21:24 UTC | 47m |
| N68NX |  | Napa County Airport (KAPC) | Madera Municipal Airport (KMAE) | 2026-04-19 20:47 UTC | 2026-04-19 21:24 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
