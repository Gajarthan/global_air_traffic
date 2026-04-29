# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_16:42:16_UTC-green)

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

**Latest saved flight:** 2026-04-29 16:42:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 16:42:16 UTC

- **59,226** saved flights
- **22,958** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,226** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **718,933.3 tonnes** estimated CO2 emissions
- **41,677,296 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2521 |
| 2 | SkyWest Airlines | 2215 |
| 3 | IndiGo | 1360 |
| 4 | EJA | 1045 |
| 5 | American Airlines | 925 |
| 6 | Southwest Airlines | 841 |
| 7 | Lufthansa | 756 |
| 8 | ENY | 735 |
| 9 | Vueling | 592 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 562 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 500 |
| 14 | Delta Air Lines | 489 |
| 15 | AZU | 487 |
| 16 | Swiss International | 469 |
| 17 | QLK | 463 |
| 18 | LXJ | 419 |
| 19 | Alaska Airlines | 404 |
| 20 | AEE | 396 |
| 21 | easyJet | 390 |
| 22 | EJU | 387 |
| 23 | VIV | 372 |
| 24 | Air France | 352 |
| 25 | Japan Airlines | 346 |
| 26 | Cathay Pacific | 340 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 297 |
| 30 | United Airlines | 296 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46727 |
| 2 | 🇪🇸 ES | 4305 |
| 3 | 🇮🇳 IN | 4303 |
| 4 | 🇦🇺 AU | 4025 |
| 5 | 🇧🇷 BR | 3346 |
| 6 | 🇩🇪 DE | 3298 |
| 7 | 🇮🇹 IT | 3262 |
| 8 | 🇯🇵 JP | 3225 |
| 9 | 🇨🇦 CA | 2930 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2508 |
| 12 | 🇫🇷 FR | 2357 |
| 13 | 🇲🇽 MX | 1857 |
| 14 | 🇬🇷 GR | 1780 |
| 15 | 🇨🇭 CH | 1657 |
| 16 | 🇳🇴 NO | 1630 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1208 |
| 19 | 🇳🇿 NZ | 1108 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1070 |
| 22 | 🇵🇭 PH | 1002 |
| 23 | 🇵🇱 PL | 963 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 864 |
| 26 | 🇲🇦 MA | 744 |
| 27 | 🇲🇪 ME | 644 |
| 28 | 🇲🇴 MO | 637 |
| 29 | 🇳🇱 NL | 627 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1325 |
| 2 | Tokyo International Airport |  | JP | 1096 |
| 3 | Denver International Airport |  | US | 989 |
| 4 | Indira Gandhi International Airport |  | IN | 902 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 877 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 753 |
| 9 | Frankfurt am Main International Airport |  | DE | 746 |
| 10 | Zurich Airport |  | CH | 715 |
| 11 | La Aurora Airport |  | GT | 652 |
| 12 | Macau International Airport |  | MO | 637 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 584 |
| 14 | Chicago O'Hare International Airport |  | US | 562 |
| 15 | Kuala Lumpur International Airport |  | MY | 555 |
| 16 | Madrid Barajas International Airport |  | ES | 550 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 543 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 19 | Malpensa International Airport |  | IT | 516 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 482 |
| 22 | Charlotte/Douglas International Airport |  | US | 469 |
| 23 | Charles de Gaulle International Airport |  | FR | 464 |
| 24 | Capua Airport |  | IT | 464 |
| 25 | Tenerife Norte Airport |  | ES | 461 |
| 26 | Ninoy Aquino International Airport |  | PH | 460 |
| 27 | Salt Lake City International Airport |  | US | 456 |
| 28 | Daniel K Inouye International Airport |  | US | 444 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 430 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 31 | Barcelona International Airport |  | ES | 404 |
| 32 | Vitoria/Foronda Airport |  | ES | 398 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 394 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 391 |
| 35 | O. R. Tambo International Airport |  | ZA | 387 |
| 36 | Reno/Tahoe International Airport |  | US | 377 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 376 |
| 38 | Amsterdam Airport Schiphol |  | NL | 366 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 351 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 196 | 21m | 244 km | 825.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 168 | 28m | 304 km | 880.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 126 | 1h 12m | 770 km | 1,673.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 99 | 31m | 369 km | 630.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 95 | 20m | 250 km | 410.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 90 | 20m | 147 km | 227.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 89 | 28m | 152 km | 232.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 83 | 1h 43m | 1,156 km | 1,655.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 77 | 1h 43m | 1,423 km | 1,889.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 75 | 14m | 154 km | 198.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO321F | IndiGo | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-04-29 15:06 UTC | 2026-04-29 16:42 UTC | 1h 35m |
| SHINR81 | SHI | Cottonwood Airport (OK66) | Miller Brothers Airport (OK47) | 2026-04-29 16:14 UTC | 2026-04-29 16:41 UTC | 26m |
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-29 15:55 UTC | 2026-04-29 16:39 UTC | 44m |
| AIC5RT | Air India | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-29 14:24 UTC | 2026-04-29 16:38 UTC | 2h 14m |
| AKJ1826 | AKJ | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-04-29 14:59 UTC | 2026-04-29 16:34 UTC | 1h 34m |
| N124PH |  | Salt Lake City International Airport (KSLC) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-29 15:55 UTC | 2026-04-29 16:33 UTC | 37m |
| N135JS |  | Dupage Airport (KDPA) | IS80 (IS80) | 2026-04-29 16:09 UTC | 2026-04-29 16:31 UTC | 22m |
| SCPR263 | SCP | Little Deer Airport (16FA) | Lindbergh's Landing Airport (FA35) | 2026-04-29 14:51 UTC | 2026-04-29 16:29 UTC | 1h 37m |
| AHK769 | AHK | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-29 13:53 UTC | 2026-04-29 16:27 UTC | 2h 33m |
| DRAGOU | DRA | Le Havre Octeville Airport (LFOH) | Le Havre St Romain Airport (LFOY) | 2026-04-29 15:40 UTC | 2026-04-29 16:25 UTC | 45m |
| CREEP31 | CRE | Enid Woodring Regional Airport (KWDG) | Perry Municipal Airport (KF22) | 2026-04-29 15:55 UTC | 2026-04-29 16:25 UTC | 30m |
| CVF4 | CVF | AR55 (AR55) | Yazoo County Airport (K87I) | 2026-04-29 15:51 UTC | 2026-04-29 16:17 UTC | 26m |
| EZY9 | easyJet | Durham Tees Valley Airport (EGNV) | Durham Tees Valley Airport (EGNV) | 2026-04-29 15:13 UTC | 2026-04-29 16:16 UTC | 1h 3m |
| PPCFJ | PPC | Pinto Martins International Airport (SBFZ) | Usina Colorado Airport (SDGB) | 2026-04-29 13:39 UTC | 2026-04-29 16:15 UTC | 2h 36m |
| N4856J |  | Boulder Municipal Airport (KBDU) | Wirth Field (CO06) | 2026-04-29 15:35 UTC | 2026-04-29 16:14 UTC | 38m |
| N425KD |  | Grand Junction Regional Airport (KGJT) | Santa Fe Regional Airport (KSAF) | 2026-04-29 15:12 UTC | 2026-04-29 16:12 UTC | 59m |
| AFR32SB | Air France | Charles de Gaulle International Airport (LFPG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-04-29 15:16 UTC | 2026-04-29 16:11 UTC | 54m |
| UBG115 | UBG | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-04-29 15:44 UTC | 2026-04-29 16:11 UTC | 26m |
| T7VRS |  | Copenhagen Kastrup Airport (EKCH) | Queen Alia International Airport (OJAI) | 2026-04-29 12:33 UTC | 2026-04-29 16:10 UTC | 3h 36m |
| N51236 |  | Gregg Airport (7OK1) | Gregg Airport (7OK1) | 2026-04-29 15:10 UTC | 2026-04-29 16:08 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
