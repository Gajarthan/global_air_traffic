# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_03:22:20_UTC-green)

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

**Latest saved flight:** 2026-04-23 03:22:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 03:22:20 UTC

- **49,087** saved flights
- **19,906** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,087** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **586,634.5 tonnes** estimated CO2 emissions
- **34,007,797 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2073 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1140 |
| 4 | EJA | 851 |
| 5 | American Airlines | 810 |
| 6 | Southwest Airlines | 702 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 550 |
| 9 | Vueling | 487 |
| 10 | AXM | 484 |
| 11 | LATAM Airlines | 480 |
| 12 | All Nippon Airways | 440 |
| 13 | AZU | 417 |
| 14 | Delta Air Lines | 405 |
| 15 | WIF | 402 |
| 16 | QLK | 393 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 371 |
| 19 | AEE | 331 |
| 20 | Alaska Airlines | 329 |
| 21 | EJU | 318 |
| 22 | easyJet | 312 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 292 |
| 25 | Air France | 277 |
| 26 | AXB | 260 |
| 27 | Cathay Pacific | 259 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | AIQ | 247 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39187 |
| 2 | 🇮🇳 IN | 3570 |
| 3 | 🇪🇸 ES | 3534 |
| 4 | 🇦🇺 AU | 3374 |
| 5 | 🇧🇷 BR | 2858 |
| 6 | 🇯🇵 JP | 2668 |
| 7 | 🇮🇹 IT | 2639 |
| 8 | 🇩🇪 DE | 2566 |
| 9 | 🇨🇦 CA | 2446 |
| 10 | 🇨🇴 CO | 2289 |
| 11 | 🇬🇧 GB | 2020 |
| 12 | 🇫🇷 FR | 1858 |
| 13 | 🇲🇽 MX | 1525 |
| 14 | 🇬🇷 GR | 1492 |
| 15 | 🇨🇭 CH | 1333 |
| 16 | 🇳🇴 NO | 1284 |
| 17 | 🇲🇾 MY | 1182 |
| 18 | 🇿🇦 ZA | 1002 |
| 19 | 🇳🇿 NZ | 947 |
| 20 | 🇹🇭 TH | 880 |
| 21 | 🇹🇷 TR | 859 |
| 22 | 🇵🇭 PH | 851 |
| 23 | 🇰🇷 KR | 804 |
| 24 | 🇵🇱 PL | 777 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 598 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 497 |
| 29 | 🇲🇴 MO | 455 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 907 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 787 |
| 5 | Indira Gandhi International Airport |  | IN | 756 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 737 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 642 |
| 9 | Zurich Airport |  | CH | 577 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 526 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 487 |
| 14 | Kuala Lumpur International Airport |  | MY | 474 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 465 |
| 16 | Macau International Airport |  | MO | 455 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 445 |
| 18 | Madrid Barajas International Airport |  | ES | 440 |
| 19 | Bengaluru International Airport |  | IN | 432 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 413 |
| 22 | Tenerife Norte Airport |  | ES | 405 |
| 23 | Malpensa International Airport |  | IT | 404 |
| 24 | Ninoy Aquino International Airport |  | PH | 394 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 375 |
| 26 | Salt Lake City International Airport |  | US | 368 |
| 27 | Daniel K Inouye International Airport |  | US | 364 |
| 28 | Charles de Gaulle International Airport |  | FR | 362 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 356 |
| 30 | Capua Airport |  | IT | 353 |
| 31 | Vitoria/Foronda Airport |  | ES | 334 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 333 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 325 |
| 36 | O. R. Tambo International Airport |  | ZA | 323 |
| 37 | Barcelona International Airport |  | ES | 321 |
| 38 | Calgary International Airport |  | CA | 298 |
| 39 | Don Mueang International Airport |  | TH | 298 |
| 40 | Viracopos International Airport |  | BR | 290 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 231 | 1h 7m | 706 km | 2,812.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 189 | 14m | 114 km | 370.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 168 | 24m | 225 km | 651.8 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 146 | 21m | 244 km | 614.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 144 | 28m | 304 km | 754.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 140 | 1h 27m | 910 km | 2,196.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 129 | 19m | 165 km | 366.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 115 | 26m | 275 km | 544.9 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 100 | 44m | 452 km | 779.4 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 84 | 31m | 369 km | 534.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 71 | 1h 41m | 1,156 km | 1,416.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WAH | WAH | Trading Bay Production Airport (5AK0) | Kenai Municipal Airport (PAEN) | 2026-04-23 03:10 UTC | 2026-04-23 03:22 UTC | 12m |
| CBRA42 | CBR | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Swift Current Airport (CYYN) | 2026-04-23 03:02 UTC | 2026-04-23 03:16 UTC | 13m |
| EHK | EHK | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-04-23 02:44 UTC | 2026-04-23 03:15 UTC | 31m |
| YHQ | YHQ | Bunyip Airport (YBUP) | Lilydale Airport (YLIL) | 2026-04-23 02:12 UTC | 2026-04-23 03:06 UTC | 54m |
| XC6 |  | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-23 02:01 UTC | 2026-04-23 03:04 UTC | 1h 3m |
| HSGDZ | HSG | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-04-23 02:55 UTC | 2026-04-23 03:02 UTC | 7m |
| EJA428 | EJA | Chicago Midway International Airport (KMDW) | Coleman A Young Municipal Airport (KDET) | 2026-04-23 02:14 UTC | 2026-04-23 02:57 UTC | 43m |
| N616F |  | Livermore Municipal Airport (KLVK) | Sacramento Executive Airport (KSAC) | 2026-04-23 02:09 UTC | 2026-04-23 02:46 UTC | 36m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-23 02:35 UTC | 2026-04-23 02:41 UTC | 5m |
| BURNY12 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-23 02:20 UTC | 2026-04-23 02:41 UTC | 20m |
| NTX | NTX | Melbourne Moorabbin Airport (YMMB) | Shepparton Airport (YSHT) | 2026-04-23 02:03 UTC | 2026-04-23 02:37 UTC | 33m |
| DESERT8 | DES | Willow Springs Ranch Airport (1AZ8) | Lake Havasu City Airport (KHII) | 2026-04-23 02:22 UTC | 2026-04-23 02:35 UTC | 13m |
| KNIFE36 | KNI | Los Alamitos Army Air Field (KSLI) | Corona Municipal Airport (KAJO) | 2026-04-23 01:49 UTC | 2026-04-23 02:35 UTC | 45m |
| CJT590 | CJT | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-04-23 02:17 UTC | 2026-04-23 02:34 UTC | 17m |
| LLR805 | LLR | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-23 02:02 UTC | 2026-04-23 02:31 UTC | 29m |
| TOE | TOE | Gold Coast Airport (YBCG) | Ballina Byron Gateway Airport (YBNA) | 2026-04-23 01:47 UTC | 2026-04-23 02:31 UTC | 43m |
| IY21 |  | Seoul Air Base (RKSM) | G 418 Airport (RK33) | 2026-04-23 01:23 UTC | 2026-04-23 02:31 UTC | 1h 7m |
| ZKTPT | ZKT | Tekapo Aerodrome (NZTL) | Pudding Hill Aerodrome (NZPH) | 2026-04-23 02:17 UTC | 2026-04-23 02:28 UTC | 11m |
| XPP | XPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-23 02:14 UTC | 2026-04-23 02:26 UTC | 12m |
| AIQ3560 | AIQ | Don Mueang International Airport (VTBD) | Buri Ram Airport (VTUO) | 2026-04-23 01:52 UTC | 2026-04-23 02:26 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
