# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_03:28:19_UTC-green)

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

**Latest saved flight:** 2026-04-24 03:28:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 03:28:19 UTC

- **50,638** saved flights
- **20,364** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,638** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **604,731.5 tonnes** estimated CO2 emissions
- **35,056,898 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2129 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1171 |
| 4 | EJA | 878 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 723 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 580 |
| 9 | Vueling | 502 |
| 10 | AXM | 497 |
| 11 | LATAM Airlines | 492 |
| 12 | All Nippon Airways | 457 |
| 13 | AZU | 430 |
| 14 | Delta Air Lines | 418 |
| 15 | WIF | 417 |
| 16 | QLK | 408 |
| 17 | LXJ | 382 |
| 18 | Swiss International | 376 |
| 19 | AEE | 343 |
| 20 | Alaska Airlines | 335 |
| 21 | EJU | 325 |
| 22 | VIV | 322 |
| 23 | easyJet | 317 |
| 24 | Japan Airlines | 301 |
| 25 | Air France | 284 |
| 26 | AXB | 268 |
| 27 | Cathay Pacific | 266 |
| 28 | JetBlue | 263 |
| 29 | United Airlines | 263 |
| 30 | AIQ | 257 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40367 |
| 2 | 🇮🇳 IN | 3677 |
| 3 | 🇪🇸 ES | 3638 |
| 4 | 🇦🇺 AU | 3516 |
| 5 | 🇧🇷 BR | 2932 |
| 6 | 🇯🇵 JP | 2764 |
| 7 | 🇮🇹 IT | 2699 |
| 8 | 🇩🇪 DE | 2682 |
| 9 | 🇨🇦 CA | 2536 |
| 10 | 🇨🇴 CO | 2346 |
| 11 | 🇬🇧 GB | 2070 |
| 12 | 🇫🇷 FR | 1927 |
| 13 | 🇲🇽 MX | 1571 |
| 14 | 🇬🇷 GR | 1530 |
| 15 | 🇨🇭 CH | 1384 |
| 16 | 🇳🇴 NO | 1350 |
| 17 | 🇲🇾 MY | 1213 |
| 18 | 🇿🇦 ZA | 1038 |
| 19 | 🇳🇿 NZ | 980 |
| 20 | 🇹🇭 TH | 919 |
| 21 | 🇹🇷 TR | 890 |
| 22 | 🇵🇭 PH | 878 |
| 23 | 🇰🇷 KR | 841 |
| 24 | 🇵🇱 PL | 811 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 622 |
| 27 | 🇲🇪 ME | 537 |
| 28 | 🇳🇱 NL | 508 |
| 29 | 🇲🇴 MO | 475 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 938 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 802 |
| 5 | Indira Gandhi International Airport |  | IN | 788 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 756 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 666 |
| 9 | Zurich Airport |  | CH | 587 |
| 10 | La Aurora Airport |  | GT | 574 |
| 11 | Frankfurt am Main International Airport |  | DE | 560 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Kuala Lumpur International Airport |  | MY | 484 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 16 | Macau International Airport |  | MO | 475 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 460 |
| 18 | Madrid Barajas International Airport |  | ES | 458 |
| 19 | Bengaluru International Airport |  | IN | 439 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 420 |
| 22 | Malpensa International Airport |  | IT | 413 |
| 23 | Tenerife Norte Airport |  | ES | 408 |
| 24 | Ninoy Aquino International Airport |  | PH | 404 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Salt Lake City International Airport |  | US | 377 |
| 27 | Charles de Gaulle International Airport |  | FR | 375 |
| 28 | Daniel K Inouye International Airport |  | US | 372 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 32 | Reno/Tahoe International Airport |  | US | 342 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 34 | Vitoria/Foronda Airport |  | ES | 340 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 337 |
| 36 | Barcelona International Airport |  | ES | 334 |
| 37 | O. R. Tambo International Airport |  | ZA | 332 |
| 38 | Don Mueang International Airport |  | TH | 312 |
| 39 | Calgary International Airport |  | CA | 309 |
| 40 | Viracopos International Airport |  | BR | 299 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 237 | 1h 7m | 706 km | 2,885.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 194 | 14m | 114 km | 380.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 172 | 24m | 225 km | 667.3 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 152 | 21m | 244 km | 640.0 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 151 | 28m | 304 km | 791.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 144 | 1h 27m | 910 km | 2,259.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 127 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 104 | 44m | 452 km | 810.5 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 89 | 1h 11m | 770 km | 1,182.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 86 | 20m | 250 km | 371.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-24 02:20 UTC | 2026-04-24 03:28 UTC | 1h 7m |
| N67490 |  | Addington Field (4TX8) | Lazy 9 Ranch Airport (TX64) | 2026-04-24 02:25 UTC | 2026-04-24 03:17 UTC | 52m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-24 00:25 UTC | 2026-04-24 03:15 UTC | 2h 50m |
| N402AM |  | Waukegan Ntl Airport (KUGN) | Gary/Chicago International Airport (KGYY) | 2026-04-24 02:09 UTC | 2026-04-24 03:09 UTC | 1h 0m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-24 01:56 UTC | 2026-04-24 03:07 UTC | 1h 10m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-24 02:54 UTC | 2026-04-24 03:07 UTC | 13m |
| STA601 | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-04-24 02:43 UTC | 2026-04-24 03:03 UTC | 20m |
| FDX1213 | FDX | Bob Hope Airport (KBUR) | Andrew Othole Memorial Airport (KXNI) | 2026-04-24 02:03 UTC | 2026-04-24 03:03 UTC | 1h 0m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-04-24 02:47 UTC | 2026-04-24 02:59 UTC | 12m |
| KII437 | KII | Tulsa International Airport (KTUL) | St Louis Lambert International Airport (KSTL) | 2026-04-24 02:06 UTC | 2026-04-24 02:57 UTC | 50m |
| CDQ20 | CDQ | Jeongseok Airport (RKPD) | Jeongseok Airport (RKPD) | 2026-04-24 02:30 UTC | 2026-04-24 02:55 UTC | 24m |
| N600RH |  | Coleman A Young Municipal Airport (KDET) | Witham Field (KSUA) | 2026-04-24 00:49 UTC | 2026-04-24 02:55 UTC | 2h 5m |
| N759PA |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-04-24 01:38 UTC | 2026-04-24 02:53 UTC | 1h 14m |
| NRD | NRD | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-24 02:51 UTC | 2026-04-24 02:51 UTC | 0m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-24 02:36 UTC | 2026-04-24 02:51 UTC | 14m |
| BRMA51 | BRM | CFB Trenton (CYTR) | CFB Trenton (CYTR) | 2026-04-24 02:39 UTC | 2026-04-24 02:43 UTC | 4m |
| C2702 |  | Mc Clellan Airfield (KMCC) | Lake Tahoe Airport (KTVL) | 2026-04-24 02:24 UTC | 2026-04-24 02:41 UTC | 16m |
| TORTGA34 | TOR | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-24 01:48 UTC | 2026-04-24 02:40 UTC | 51m |
| LCT815 | LCT | Abraham Gonzalez International Airport (MMCS) | Leon Gonzales Pie De La Cuesta Airport (MM41) | 2026-04-23 22:32 UTC | 2026-04-24 02:38 UTC | 4h 6m |
| EJA466 | EJA | Van Nuys Airport (KVNY) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-24 01:43 UTC | 2026-04-24 02:38 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
