# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_08:47:44_UTC-green)

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

**Latest saved flight:** 2026-04-21 08:47:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 08:47:44 UTC

- **46,478** saved flights
- **19,078** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,478** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **560,455.8 tonnes** estimated CO2 emissions
- **32,490,192 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1975 |
| 2 | SkyWest Airlines | 1799 |
| 3 | IndiGo | 1100 |
| 4 | EJA | 800 |
| 5 | American Airlines | 770 |
| 6 | Southwest Airlines | 670 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 488 |
| 9 | Vueling | 471 |
| 10 | AXM | 465 |
| 11 | LATAM Airlines | 459 |
| 12 | All Nippon Airways | 419 |
| 13 | AZU | 397 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 376 |
| 16 | WIF | 368 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 357 |
| 19 | Alaska Airlines | 318 |
| 20 | AEE | 316 |
| 21 | EJU | 311 |
| 22 | VIV | 298 |
| 23 | easyJet | 297 |
| 24 | Japan Airlines | 280 |
| 25 | Air France | 264 |
| 26 | Cathay Pacific | 249 |
| 27 | JetBlue | 249 |
| 28 | United Airlines | 246 |
| 29 | AXB | 244 |
| 30 | GLO | 237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36877 |
| 2 | 🇮🇳 IN | 3415 |
| 3 | 🇪🇸 ES | 3401 |
| 4 | 🇦🇺 AU | 3223 |
| 5 | 🇧🇷 BR | 2718 |
| 6 | 🇯🇵 JP | 2551 |
| 7 | 🇮🇹 IT | 2519 |
| 8 | 🇩🇪 DE | 2393 |
| 9 | 🇨🇦 CA | 2267 |
| 10 | 🇨🇴 CO | 2130 |
| 11 | 🇬🇧 GB | 1907 |
| 12 | 🇫🇷 FR | 1766 |
| 13 | 🇲🇽 MX | 1445 |
| 14 | 🇬🇷 GR | 1417 |
| 15 | 🇨🇭 CH | 1269 |
| 16 | 🇳🇴 NO | 1168 |
| 17 | 🇲🇾 MY | 1137 |
| 18 | 🇿🇦 ZA | 962 |
| 19 | 🇳🇿 NZ | 911 |
| 20 | 🇹🇭 TH | 838 |
| 21 | 🇵🇭 PH | 829 |
| 22 | 🇹🇷 TR | 820 |
| 23 | 🇰🇷 KR | 767 |
| 24 | 🇵🇱 PL | 737 |
| 25 | 🇬🇹 GT | 737 |
| 26 | 🇲🇦 MA | 575 |
| 27 | 🇲🇪 ME | 492 |
| 28 | 🇳🇱 NL | 477 |
| 29 | 🇲🇴 MO | 437 |
| 30 | 🇧🇸 BS | 420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1096 |
| 2 | Tokyo International Airport |  | JP | 867 |
| 3 | Denver International Airport |  | US | 775 |
| 4 | El Dorado International Airport |  | CO | 743 |
| 5 | Indira Gandhi International Airport |  | IN | 736 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 704 |
| 7 | Harry Reid International Airport |  | US | 600 |
| 8 | Guaymaral Airport |  | CO | 583 |
| 9 | Zurich Airport |  | CH | 551 |
| 10 | La Aurora Airport |  | GT | 545 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 12 | Frankfurt am Main International Airport |  | DE | 460 |
| 13 | Chicago O'Hare International Airport |  | US | 459 |
| 14 | Kuala Lumpur International Airport |  | MY | 455 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 447 |
| 16 | Macau International Airport |  | MO | 437 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 415 |
| 19 | Bengaluru International Airport |  | IN | 409 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 399 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 388 |
| 24 | Ninoy Aquino International Airport |  | PH | 383 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 355 |
| 26 | Daniel K Inouye International Airport |  | US | 347 |
| 27 | Salt Lake City International Airport |  | US | 346 |
| 28 | Charles de Gaulle International Airport |  | FR | 344 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 343 |
| 30 | Capua Airport |  | IT | 340 |
| 31 | Reno/Tahoe International Airport |  | US | 322 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 320 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 319 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 36 | O. R. Tambo International Airport |  | ZA | 308 |
| 37 | Barcelona International Airport |  | ES | 308 |
| 38 | Don Mueang International Airport |  | TH | 281 |
| 39 | Calgary International Airport |  | CA | 280 |
| 40 | Viracopos International Airport |  | BR | 277 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 220 | 1h 7m | 706 km | 2,678.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 174 | 14m | 114 km | 341.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 140 | 28m | 304 km | 733.9 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 135 | 21m | 244 km | 568.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 134 | 1h 27m | 910 km | 2,102.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 124 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 124 | 19m | 165 km | 352.7 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 111 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 68 | 13m | 99 km | 116.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LSI125 | LSI | Ghedi Airport (LIPL) | Macau International Airport (VMMC) | 2026-04-20 22:05 UTC | 2026-04-21 08:47 UTC | 10h 41m |
| MRX | MRX | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-21 08:13 UTC | 2026-04-21 08:41 UTC | 27m |
| BPO129 | BPO | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-04-21 08:13 UTC | 2026-04-21 08:40 UTC | 27m |
| R21234 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-21 07:58 UTC | 2026-04-21 08:36 UTC | 37m |
| RGA08 | RGA | Buochs Airport (LSZC) | Meiringen Airport (LSMM) | 2026-04-21 08:07 UTC | 2026-04-21 08:25 UTC | 18m |
| HLC238 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-21 08:19 UTC | 2026-04-21 08:19 UTC | 0m |
| N916LL |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-21 08:14 UTC | 2026-04-21 08:17 UTC | 3m |
| URSA32 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-21 07:44 UTC | 2026-04-21 08:13 UTC | 28m |
| VUBCC | VUB | Gwalior Airport (VIGR) | Akbarpur Airport (VI90) | 2026-04-21 05:23 UTC | 2026-04-21 08:12 UTC | 2h 48m |
| VOE67LC | VOE | Malaga Airport (LEMG) | La Morgal Airport (LEMR) | 2026-04-21 07:03 UTC | 2026-04-21 08:10 UTC | 1h 6m |
| GMA01 | GMA | Glasgow International Airport (EGPF) | Wick Airport (EGPC) | 2026-04-21 07:28 UTC | 2026-04-21 08:09 UTC | 40m |
| BPO760 | BPO | Luneburg Airport (EDHG) | Luneburg Airport (EDHG) | 2026-04-21 07:49 UTC | 2026-04-21 08:04 UTC | 15m |
| IGO162P | IndiGo | Bengaluru International Airport (VOBL) | VEDG (VEDG) | 2026-04-21 06:10 UTC | 2026-04-21 08:04 UTC | 1h 53m |
| HUF184 | HUF | Kecskemet Airport (LHKE) | Poprad-Tatry Airport (LZTT) | 2026-04-21 06:39 UTC | 2026-04-21 08:03 UTC | 1h 24m |
| AIQ3520 | AIQ | Don Mueang International Airport (VTBD) | Buri Ram Airport (VTUO) | 2026-04-21 07:26 UTC | 2026-04-21 08:01 UTC | 35m |
| SWR1XG | Swiss International | Munich International Airport (EDDM) | Zurich Airport (LSZH) | 2026-04-21 07:28 UTC | 2026-04-21 08:01 UTC | 33m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-04-21 07:46 UTC | 2026-04-21 08:00 UTC | 13m |
| IGO6537 | IndiGo | Bengaluru International Airport (VOBL) | Dhanbad Airport (VEDB) | 2026-04-21 06:13 UTC | 2026-04-21 07:59 UTC | 1h 46m |
| CFE772 | CFE | Glasgow International Airport (EGPF) | London City Airport (EGLC) | 2026-04-21 06:41 UTC | 2026-04-21 07:56 UTC | 1h 15m |
| VLG63LZ | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-04-21 07:15 UTC | 2026-04-21 07:54 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
