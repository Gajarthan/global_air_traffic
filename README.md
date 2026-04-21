# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_07:12:40_UTC-green)

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

**Latest saved flight:** 2026-04-21 07:12:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 07:12:40 UTC

- **46,359** saved flights
- **19,057** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,359** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **558,919.6 tonnes** estimated CO2 emissions
- **32,401,135 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1965 |
| 2 | SkyWest Airlines | 1799 |
| 3 | IndiGo | 1095 |
| 4 | EJA | 800 |
| 5 | American Airlines | 770 |
| 6 | Southwest Airlines | 670 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 483 |
| 9 | Vueling | 468 |
| 10 | AXM | 463 |
| 11 | LATAM Airlines | 459 |
| 12 | All Nippon Airways | 416 |
| 13 | AZU | 397 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 376 |
| 16 | WIF | 366 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 355 |
| 19 | Alaska Airlines | 318 |
| 20 | AEE | 315 |
| 21 | EJU | 309 |
| 22 | VIV | 298 |
| 23 | easyJet | 292 |
| 24 | Japan Airlines | 278 |
| 25 | Air France | 263 |
| 26 | Cathay Pacific | 249 |
| 27 | JetBlue | 249 |
| 28 | United Airlines | 246 |
| 29 | AXB | 242 |
| 30 | GLO | 237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36867 |
| 2 | 🇮🇳 IN | 3395 |
| 3 | 🇪🇸 ES | 3386 |
| 4 | 🇦🇺 AU | 3217 |
| 5 | 🇧🇷 BR | 2718 |
| 6 | 🇯🇵 JP | 2532 |
| 7 | 🇮🇹 IT | 2503 |
| 8 | 🇩🇪 DE | 2376 |
| 9 | 🇨🇦 CA | 2267 |
| 10 | 🇨🇴 CO | 2130 |
| 11 | 🇬🇧 GB | 1893 |
| 12 | 🇫🇷 FR | 1756 |
| 13 | 🇲🇽 MX | 1445 |
| 14 | 🇬🇷 GR | 1412 |
| 15 | 🇨🇭 CH | 1259 |
| 16 | 🇳🇴 NO | 1160 |
| 17 | 🇲🇾 MY | 1133 |
| 18 | 🇿🇦 ZA | 960 |
| 19 | 🇳🇿 NZ | 911 |
| 20 | 🇹🇭 TH | 829 |
| 21 | 🇵🇭 PH | 827 |
| 22 | 🇹🇷 TR | 816 |
| 23 | 🇰🇷 KR | 757 |
| 24 | 🇬🇹 GT | 737 |
| 25 | 🇵🇱 PL | 734 |
| 26 | 🇲🇦 MA | 570 |
| 27 | 🇲🇪 ME | 486 |
| 28 | 🇳🇱 NL | 470 |
| 29 | 🇲🇴 MO | 436 |
| 30 | 🇧🇸 BS | 420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1096 |
| 2 | Tokyo International Airport |  | JP | 863 |
| 3 | Denver International Airport |  | US | 775 |
| 4 | El Dorado International Airport |  | CO | 743 |
| 5 | Indira Gandhi International Airport |  | IN | 733 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 701 |
| 7 | Harry Reid International Airport |  | US | 600 |
| 8 | Guaymaral Airport |  | CO | 583 |
| 9 | Zurich Airport |  | CH | 549 |
| 10 | La Aurora Airport |  | GT | 545 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 12 | Chicago O'Hare International Airport |  | US | 459 |
| 13 | Frankfurt am Main International Airport |  | DE | 456 |
| 14 | Kuala Lumpur International Airport |  | MY | 453 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 447 |
| 16 | Macau International Airport |  | MO | 436 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 413 |
| 19 | Bengaluru International Airport |  | IN | 406 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 398 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 388 |
| 24 | Ninoy Aquino International Airport |  | PH | 383 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 355 |
| 26 | Daniel K Inouye International Airport |  | US | 347 |
| 27 | Salt Lake City International Airport |  | US | 346 |
| 28 | Charles de Gaulle International Airport |  | FR | 342 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 340 |
| 30 | Capua Airport |  | IT | 337 |
| 31 | Reno/Tahoe International Airport |  | US | 322 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 320 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 319 |
| 34 | Vitoria/Foronda Airport |  | ES | 317 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 36 | O. R. Tambo International Airport |  | ZA | 307 |
| 37 | Barcelona International Airport |  | ES | 305 |
| 38 | Calgary International Airport |  | CA | 280 |
| 39 | Viracopos International Airport |  | BR | 277 |
| 40 | Don Mueang International Airport |  | TH | 277 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 219 | 1h 7m | 706 km | 2,666.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 174 | 14m | 114 km | 341.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 139 | 28m | 304 km | 728.7 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 135 | 21m | 244 km | 568.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 132 | 1h 27m | 910 km | 2,071.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 124 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 111 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 68 | 13m | 99 km | 116.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBKFI | HBK | Lausanne-la Blecherette Airport (LSGL) | Bern Belp Airport (LSZB) | 2026-04-21 06:43 UTC | 2026-04-21 07:12 UTC | 28m |
| N31 |  | Tampere-Pirkkala Airport (EFTP) | Tampere-Pirkkala Airport (EFTP) | 2026-04-21 06:24 UTC | 2026-04-21 06:58 UTC | 34m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-04-21 06:14 UTC | 2026-04-21 06:52 UTC | 38m |
|  |  | Tribhuvan International Airport (VNKT) | Tikapur Airport (VNTP) | 2026-04-21 05:53 UTC | 2026-04-21 06:40 UTC | 46m |
| DYK | DYK | Dalby Airport (YDAY) | Toowoomba Airport (YTWB) | 2026-04-21 06:26 UTC | 2026-04-21 06:39 UTC | 13m |
| N334CA |  | Bisbee Municipal Airport (KP04) | Douglas Municipal Airport (KDGL) | 2026-04-21 05:19 UTC | 2026-04-21 06:32 UTC | 1h 13m |
| 4XHYI |  | LL59 (LL59) | Herzliya Airport (LLHZ) | 2026-04-21 06:17 UTC | 2026-04-21 06:30 UTC | 13m |
| WIF8VD | WIF | Bodø Airport (ENBO) | Røst Airport (ENRS) | 2026-04-21 06:14 UTC | 2026-04-21 06:29 UTC | 14m |
| THA413 | Thai Airways | Suvarnabhumi Airport (VTBS) | Hang Nadim Airport (WIDD) | 2026-04-21 04:27 UTC | 2026-04-21 06:28 UTC | 2h 1m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Tribhuvan International Airport (VNKT) | 2026-04-21 03:27 UTC | 2026-04-21 06:26 UTC | 2h 58m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-21 05:58 UTC | 2026-04-21 06:25 UTC | 27m |
| VALT | VAL | RAAF Base Pearce (YPEA) | RAAF Gingin (YGIG) | 2026-04-21 05:56 UTC | 2026-04-21 06:22 UTC | 26m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | Desiderata Ranch Airport (30CO) | 2026-04-21 06:06 UTC | 2026-04-21 06:19 UTC | 12m |
| OAL099 | OAL | Ikaria Airport (LGIK) | Limnos Airport (LGLM) | 2026-04-21 05:37 UTC | 2026-04-21 06:17 UTC | 39m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-04-21 05:48 UTC | 2026-04-21 06:17 UTC | 29m |
| AZG633 | AZG | Ben Gurion International Airport (LLBG) | Hang Nadim Airport (WIDD) | 2026-04-20 16:47 UTC | 2026-04-21 06:17 UTC | 13h 29m |
| TAM3960 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Prefeito Renato Moreira Airport (SBIZ) | 2026-04-21 03:39 UTC | 2026-04-21 06:16 UTC | 2h 37m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Wattay International Airport (VLVT) | 2026-04-21 05:27 UTC | 2026-04-21 06:15 UTC | 48m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-21 05:25 UTC | 2026-04-21 06:15 UTC | 50m |
| AE976 |  | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-04-21 05:53 UTC | 2026-04-21 06:14 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
