# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_15:56:06_UTC-green)

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

**Latest saved flight:** 2026-04-20 15:56:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 15:56:06 UTC

- **45,318** saved flights
- **18,711** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **45,318** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **547,535.6 tonnes** estimated CO2 emissions
- **31,741,195 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1928 |
| 2 | SkyWest Airlines | 1748 |
| 3 | IndiGo | 1087 |
| 4 | EJA | 784 |
| 5 | American Airlines | 745 |
| 6 | Southwest Airlines | 646 |
| 7 | ENY | 589 |
| 8 | Lufthansa | 470 |
| 9 | AXM | 458 |
| 10 | Vueling | 456 |
| 11 | LATAM Airlines | 450 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 392 |
| 14 | Delta Air Lines | 382 |
| 15 | QLK | 366 |
| 16 | LXJ | 356 |
| 17 | WIF | 356 |
| 18 | Swiss International | 352 |
| 19 | AEE | 309 |
| 20 | Alaska Airlines | 308 |
| 21 | EJU | 303 |
| 22 | easyJet | 290 |
| 23 | VIV | 289 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 260 |
| 26 | AXB | 240 |
| 27 | United Airlines | 240 |
| 28 | JetBlue | 238 |
| 29 | Cathay Pacific | 236 |
| 30 | GLO | 235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35742 |
| 2 | 🇮🇳 IN | 3373 |
| 3 | 🇪🇸 ES | 3342 |
| 4 | 🇦🇺 AU | 3131 |
| 5 | 🇧🇷 BR | 2684 |
| 6 | 🇯🇵 JP | 2486 |
| 7 | 🇮🇹 IT | 2443 |
| 8 | 🇩🇪 DE | 2345 |
| 9 | 🇨🇦 CA | 2191 |
| 10 | 🇨🇴 CO | 2083 |
| 11 | 🇬🇧 GB | 1864 |
| 12 | 🇫🇷 FR | 1730 |
| 13 | 🇲🇽 MX | 1411 |
| 14 | 🇬🇷 GR | 1396 |
| 15 | 🇨🇭 CH | 1246 |
| 16 | 🇳🇴 NO | 1138 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 952 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇵🇭 PH | 811 |
| 22 | 🇹🇷 TR | 803 |
| 23 | 🇰🇷 KR | 746 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 725 |
| 26 | 🇲🇦 MA | 564 |
| 27 | 🇲🇪 ME | 481 |
| 28 | 🇳🇱 NL | 464 |
| 29 | 🇲🇴 MO | 424 |
| 30 | 🇧🇸 BS | 416 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1060 |
| 2 | Tokyo International Airport |  | JP | 848 |
| 3 | Denver International Airport |  | US | 753 |
| 4 | Indira Gandhi International Airport |  | IN | 729 |
| 5 | El Dorado International Airport |  | CO | 728 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 692 |
| 7 | Harry Reid International Airport |  | US | 584 |
| 8 | Guaymaral Airport |  | CO | 569 |
| 9 | Zurich Airport |  | CH | 543 |
| 10 | La Aurora Airport |  | GT | 541 |
| 11 | Kuala Lumpur International Airport |  | MY | 449 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 444 |
| 13 | Chicago O'Hare International Airport |  | US | 444 |
| 14 | Frankfurt am Main International Airport |  | DE | 442 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 435 |
| 16 | Macau International Airport |  | MO | 424 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 421 |
| 18 | Madrid Barajas International Airport |  | ES | 407 |
| 19 | Bengaluru International Airport |  | IN | 402 |
| 20 | Tenerife Norte Airport |  | ES | 392 |
| 21 | Charlotte/Douglas International Airport |  | US | 390 |
| 22 | Malpensa International Airport |  | IT | 388 |
| 23 | Congonhas Airport |  | BR | 383 |
| 24 | Ninoy Aquino International Airport |  | PH | 376 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 341 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 337 |
| 28 | Charles de Gaulle International Airport |  | FR | 336 |
| 29 | Daniel K Inouye International Airport |  | US | 334 |
| 30 | Capua Airport |  | IT | 324 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 314 |
| 32 | Vitoria/Foronda Airport |  | ES | 313 |
| 33 | Reno/Tahoe International Airport |  | US | 312 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 307 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 306 |
| 36 | O. R. Tambo International Airport |  | ZA | 305 |
| 37 | Barcelona International Airport |  | ES | 295 |
| 38 | Don Mueang International Airport |  | TH | 275 |
| 39 | Calgary International Airport |  | CA | 274 |
| 40 | Viracopos International Airport |  | BR | 273 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 229 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 168 | 14m | 114 km | 329.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 128 | 21m | 244 km | 539.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 122 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 106 | 26m | 275 km | 502.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 80 | 31m | 369 km | 509.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 76 | 20m | 250 km | 328.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 73 | 52m | 556 km | 699.8 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 70 | 26m | 215 km | 259.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 66 | 13m | 99 km | 113.2 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 63 | 1h 52m | 1,304 km | 1,417.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 0m | 695 km | 743.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEZ2426 | AEZ | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | 2026-04-20 15:04 UTC | 2026-04-20 15:56 UTC | 51m |
| DHK536 | DHK | East Midlands Airport (EGNX) | Macau International Airport (VMMC) | 2026-04-20 00:09 UTC | 2026-04-20 15:55 UTC | 15h 46m |
| CAMEL2 | CAM | Wickenby Aerodrome (EGNW) | RAF Coningsby (EGXC) | 2026-04-20 15:29 UTC | 2026-04-20 15:55 UTC | 26m |
| N6299D |  | Glenwood Municipal Airport (KGHW) | Brooten Municipal/John O Bohmer Field (K6D1) | 2026-04-20 15:13 UTC | 2026-04-20 15:51 UTC | 37m |
| CPA603 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Langtang Airport (VNLT) | 2026-04-20 11:14 UTC | 2026-04-20 15:50 UTC | 4h 36m |
| N9469H |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-04-20 15:18 UTC | 2026-04-20 15:47 UTC | 29m |
| FDB8573 | flydubai | Dubai International Airport (OMDB) | Simara Airport (VNSI) | 2026-04-20 11:59 UTC | 2026-04-20 15:47 UTC | 3h 47m |
| N70380 |  | Council Bluffs Municipal Airport (KCBF) | Red Oak Municipal Airport (KRDK) | 2026-04-20 15:27 UTC | 2026-04-20 15:46 UTC | 19m |
| N884HB |  | Crystal Springs Ranch Airport (UT54) | Logan-Cache Airport (KLGU) | 2026-04-20 14:44 UTC | 2026-04-20 15:46 UTC | 1h 1m |
| AXEL10 | AXE | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-20 14:38 UTC | 2026-04-20 15:44 UTC | 1h 6m |
| N1928F |  | Hector International Airport (KFAR) | Alexandria Regional/Chandler Field (KAXN) | 2026-04-20 13:50 UTC | 2026-04-20 15:41 UTC | 1h 50m |
| N404PL |  | Aero Estates Airport (7IS2) | Raleigh County Memorial Airport (KBKW) | 2026-04-20 14:28 UTC | 2026-04-20 15:41 UTC | 1h 12m |
| NWX382 | NWX | Jw Airport (2TX7) | Aero Valley Airport (K52F) | 2026-04-20 15:32 UTC | 2026-04-20 15:39 UTC | 6m |
| N2282T |  | Bartlesville Municipal Airport (KBVO) | Tulsa International Airport (KTUL) | 2026-04-20 15:12 UTC | 2026-04-20 15:39 UTC | 27m |
| XBSBF | XBS | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-20 14:46 UTC | 2026-04-20 15:38 UTC | 51m |
| N91HK |  | Palm Beach International Airport (KPBI) | James H Easom Field (KM23) | 2026-04-20 14:04 UTC | 2026-04-20 15:37 UTC | 1h 32m |
| TRF572 | TRF | Addison Airport (KADS) | Fly-N-Ski Airport (31XS) | 2026-04-20 15:02 UTC | 2026-04-20 15:36 UTC | 33m |
| N5827P |  | Pueblo Memorial Airport (KPUB) | 1CO7 (1CO7) | 2026-04-20 15:01 UTC | 2026-04-20 15:29 UTC | 28m |
| N364EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-20 14:27 UTC | 2026-04-20 15:29 UTC | 1h 2m |
| CAMEL1 | CAM | RAF Cranwell (EGYD) | Wickenby Aerodrome (EGNW) | 2026-04-20 14:43 UTC | 2026-04-20 15:28 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
