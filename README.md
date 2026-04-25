# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_13:26:01_UTC-green)

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

**Latest saved flight:** 2026-04-25 13:26:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 13:26:01 UTC

- **53,372** saved flights
- **21,223** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,372** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **639,804.0 tonnes** estimated CO2 emissions
- **37,090,088 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2244 |
| 2 | SkyWest Airlines | 2007 |
| 3 | IndiGo | 1219 |
| 4 | EJA | 944 |
| 5 | American Airlines | 857 |
| 6 | Southwest Airlines | 754 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 620 |
| 9 | Vueling | 537 |
| 10 | AXM | 520 |
| 11 | LATAM Airlines | 513 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 450 |
| 14 | WIF | 443 |
| 15 | Delta Air Lines | 440 |
| 16 | QLK | 416 |
| 17 | Swiss International | 412 |
| 18 | LXJ | 393 |
| 19 | AEE | 358 |
| 20 | Alaska Airlines | 353 |
| 21 | easyJet | 343 |
| 22 | EJU | 338 |
| 23 | VIV | 338 |
| 24 | Japan Airlines | 313 |
| 25 | Air France | 306 |
| 26 | AXB | 285 |
| 27 | Cathay Pacific | 284 |
| 28 | AIQ | 276 |
| 29 | JetBlue | 272 |
| 30 | United Airlines | 272 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42428 |
| 2 | 🇪🇸 ES | 3871 |
| 3 | 🇮🇳 IN | 3840 |
| 4 | 🇦🇺 AU | 3619 |
| 5 | 🇧🇷 BR | 3073 |
| 6 | 🇯🇵 JP | 2889 |
| 7 | 🇮🇹 IT | 2872 |
| 8 | 🇩🇪 DE | 2838 |
| 9 | 🇨🇦 CA | 2660 |
| 10 | 🇨🇴 CO | 2453 |
| 11 | 🇬🇧 GB | 2232 |
| 12 | 🇫🇷 FR | 2076 |
| 13 | 🇲🇽 MX | 1641 |
| 14 | 🇬🇷 GR | 1609 |
| 15 | 🇨🇭 CH | 1512 |
| 16 | 🇳🇴 NO | 1439 |
| 17 | 🇲🇾 MY | 1265 |
| 18 | 🇿🇦 ZA | 1111 |
| 19 | 🇳🇿 NZ | 1016 |
| 20 | 🇹🇭 TH | 974 |
| 21 | 🇹🇷 TR | 958 |
| 22 | 🇵🇭 PH | 913 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 855 |
| 25 | 🇬🇹 GT | 818 |
| 26 | 🇲🇦 MA | 661 |
| 27 | 🇲🇪 ME | 576 |
| 28 | 🇳🇱 NL | 543 |
| 29 | 🇲🇴 MO | 525 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1214 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 881 |
| 4 | El Dorado International Airport |  | CO | 833 |
| 5 | Indira Gandhi International Airport |  | IN | 816 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 795 |
| 7 | Guaymaral Airport |  | CO | 734 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 633 |
| 10 | La Aurora Airport |  | GT | 611 |
| 11 | Frankfurt am Main International Airport |  | DE | 608 |
| 12 | Macau International Airport |  | MO | 525 |
| 13 | Chicago O'Hare International Airport |  | US | 525 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 504 |
| 17 | Madrid Barajas International Airport |  | ES | 495 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 458 |
| 20 | Malpensa International Airport |  | IT | 448 |
| 21 | Congonhas Airport |  | BR | 442 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Tenerife Norte Airport |  | ES | 426 |
| 24 | Ninoy Aquino International Airport |  | PH | 421 |
| 25 | Charles de Gaulle International Airport |  | FR | 402 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 397 |
| 27 | Salt Lake City International Airport |  | US | 395 |
| 28 | Daniel K Inouye International Airport |  | US | 388 |
| 29 | Capua Airport |  | IT | 381 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 381 |
| 31 | Vitoria/Foronda Airport |  | ES | 365 |
| 32 | Barcelona International Airport |  | ES | 360 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 34 | Reno/Tahoe International Airport |  | US | 355 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 354 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 354 |
| 37 | O. R. Tambo International Airport |  | ZA | 349 |
| 38 | Don Mueang International Airport |  | TH | 331 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 313 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 297 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 163 | 21m | 244 km | 686.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 124 | 26m | 275 km | 587.6 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 76 | 1h 41m | 1,156 km | 1,516.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 1m | 695 km | 911.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 70 | 13m | - | - |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 69 | 24m | 55 km | 65.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N733HK |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-25 12:48 UTC | 2026-04-25 13:26 UTC | 37m |
| LAE1801 | LAE | Miami International Airport (KMIA) | La Aurora Airport (MGGT) | 2026-04-25 11:01 UTC | 2026-04-25 13:20 UTC | 2h 18m |
| N407BW |  | New Bedford Regional Airport (KEWB) | Tweed/New Haven Airport (KHVN) | 2026-04-25 12:11 UTC | 2026-04-25 13:05 UTC | 54m |
| N2903T |  | FD84 (FD84) | Plant City Airport (KPCM) | 2026-04-25 11:58 UTC | 2026-04-25 13:05 UTC | 1h 6m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-25 06:36 UTC | 2026-04-25 12:59 UTC | 6h 22m |
| HBCDE | HBC | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-04-25 12:32 UTC | 2026-04-25 12:55 UTC | 22m |
| N1377M |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-25 12:41 UTC | 2026-04-25 12:53 UTC | 12m |
| N344BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-25 12:51 UTC | 2026-04-25 12:52 UTC | 0m |
| N577CB |  | South Lakeland Airport (KX49) | South Lakeland Airport (KX49) | 2026-04-25 12:36 UTC | 2026-04-25 12:48 UTC | 11m |
| N865D |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-04-25 12:21 UTC | 2026-04-25 12:45 UTC | 23m |
| OEBXS | OEB | Graz Airport (LOWG) | Graz Airport (LOWG) | 2026-04-25 12:24 UTC | 2026-04-25 12:43 UTC | 19m |
| HRD31 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-25 11:34 UTC | 2026-04-25 12:42 UTC | 1h 8m |
| HK5298G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-25 11:58 UTC | 2026-04-25 12:39 UTC | 40m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-25 12:07 UTC | 2026-04-25 12:37 UTC | 30m |
| N292KF |  | Triangle North Executive Airport (KLHZ) | Triangle North Executive Airport (KLHZ) | 2026-04-25 12:35 UTC | 2026-04-25 12:36 UTC | 1m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-25 12:25 UTC | 2026-04-25 12:36 UTC | 10m |
| PSCPG | PSC | Fazenda Irmaos Munaretto Airport (SDYF) | Fazenda Nossa Senhora das Gracas Airport (SWNG) | 2026-04-25 12:22 UTC | 2026-04-25 12:34 UTC | 11m |
| DKULT | DKU | LIVD (LIVD) | Innsbruck Airport (LOWI) | 2026-04-25 12:15 UTC | 2026-04-25 12:29 UTC | 14m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-25 12:17 UTC | 2026-04-25 12:29 UTC | 11m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-04-25 11:42 UTC | 2026-04-25 12:27 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
