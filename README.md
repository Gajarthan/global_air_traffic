# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_04:36:54_UTC-green)

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

**Latest saved flight:** 2026-04-28 04:36:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 04:36:54 UTC

- **57,650** saved flights
- **22,523** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,650** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **699,563.8 tonnes** estimated CO2 emissions
- **40,554,420 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2442 |
| 2 | SkyWest Airlines | 2190 |
| 3 | IndiGo | 1301 |
| 4 | EJA | 1031 |
| 5 | American Airlines | 916 |
| 6 | Southwest Airlines | 831 |
| 7 | ENY | 726 |
| 8 | Lufthansa | 710 |
| 9 | Vueling | 574 |
| 10 | AXM | 561 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 505 |
| 13 | AZU | 482 |
| 14 | WIF | 478 |
| 15 | Delta Air Lines | 475 |
| 16 | QLK | 452 |
| 17 | Swiss International | 450 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 394 |
| 20 | AEE | 381 |
| 21 | easyJet | 377 |
| 22 | EJU | 370 |
| 23 | VIV | 369 |
| 24 | Air France | 334 |
| 25 | Japan Airlines | 332 |
| 26 | Cathay Pacific | 330 |
| 27 | AXB | 314 |
| 28 | JetBlue | 294 |
| 29 | United Airlines | 290 |
| 30 | GLO | 288 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45856 |
| 2 | 🇪🇸 ES | 4186 |
| 3 | 🇮🇳 IN | 4108 |
| 4 | 🇦🇺 AU | 3905 |
| 5 | 🇧🇷 BR | 3294 |
| 6 | 🇩🇪 DE | 3142 |
| 7 | 🇮🇹 IT | 3140 |
| 8 | 🇯🇵 JP | 3086 |
| 9 | 🇨🇦 CA | 2856 |
| 10 | 🇨🇴 CO | 2604 |
| 11 | 🇬🇧 GB | 2442 |
| 12 | 🇫🇷 FR | 2257 |
| 13 | 🇲🇽 MX | 1829 |
| 14 | 🇬🇷 GR | 1708 |
| 15 | 🇨🇭 CH | 1606 |
| 16 | 🇳🇴 NO | 1550 |
| 17 | 🇲🇾 MY | 1360 |
| 18 | 🇿🇦 ZA | 1165 |
| 19 | 🇳🇿 NZ | 1092 |
| 20 | 🇹🇷 TR | 1048 |
| 21 | 🇹🇭 TH | 1025 |
| 22 | 🇵🇭 PH | 972 |
| 23 | 🇵🇱 PL | 925 |
| 24 | 🇰🇷 KR | 912 |
| 25 | 🇬🇹 GT | 849 |
| 26 | 🇲🇦 MA | 726 |
| 27 | 🇲🇪 ME | 623 |
| 28 | 🇲🇴 MO | 612 |
| 29 | 🇳🇱 NL | 598 |
| 30 | 🇮🇩 ID | 498 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1310 |
| 2 | Tokyo International Airport |  | JP | 1048 |
| 3 | Denver International Airport |  | US | 969 |
| 4 | El Dorado International Airport |  | CO | 878 |
| 5 | Indira Gandhi International Airport |  | IN | 873 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 842 |
| 7 | Guaymaral Airport |  | CO | 800 |
| 8 | Harry Reid International Airport |  | US | 738 |
| 9 | Frankfurt am Main International Airport |  | DE | 699 |
| 10 | Zurich Airport |  | CH | 687 |
| 11 | La Aurora Airport |  | GT | 639 |
| 12 | Macau International Airport |  | MO | 612 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 575 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Kuala Lumpur International Airport |  | MY | 537 |
| 16 | Madrid Barajas International Airport |  | ES | 536 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 509 |
| 19 | Malpensa International Airport |  | IT | 497 |
| 20 | Bengaluru International Airport |  | IN | 492 |
| 21 | Congonhas Airport |  | BR | 474 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Salt Lake City International Airport |  | US | 449 |
| 25 | Ninoy Aquino International Airport |  | PH | 447 |
| 26 | Charles de Gaulle International Airport |  | FR | 443 |
| 27 | Capua Airport |  | IT | 437 |
| 28 | Daniel K Inouye International Airport |  | US | 427 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 424 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 410 |
| 31 | Barcelona International Airport |  | ES | 392 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 33 | Vitoria/Foronda Airport |  | ES | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 379 |
| 35 | Reno/Tahoe International Airport |  | US | 374 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 37 | O. R. Tambo International Airport |  | ZA | 367 |
| 38 | Don Mueang International Airport |  | TH | 349 |
| 39 | Amsterdam Airport Schiphol |  | NL | 342 |
| 40 | Calgary International Airport |  | CA | 341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 186 | 21m | 244 km | 783.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 165 | 1h 27m | 910 km | 2,589.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 161 | 28m | 304 km | 844.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 143 | 19m | 165 km | 406.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 131 | 26m | 275 km | 620.8 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 114 | 1h 12m | 770 km | 1,514.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 77 | 58m | 493 km | 655.1 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 74 | 1h 42m | 1,423 km | 1,816.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PRPH07 | PRP | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-28 03:57 UTC | 2026-04-28 04:36 UTC | 39m |
| DSCO02 | DSC | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-28 03:36 UTC | 2026-04-28 04:30 UTC | 53m |
| JJP215 | JJP | Narita International Airport (RJAA) | Kansai International Airport (RJBB) | 2026-04-28 03:28 UTC | 2026-04-28 04:21 UTC | 53m |
| KST2612 | KST | Chiang Mai International Airport (VTCC) | Chiang Rai Airport (VTCR) | 2026-04-28 04:05 UTC | 2026-04-28 04:21 UTC | 15m |
| XUG | XUG | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-28 03:56 UTC | 2026-04-28 04:21 UTC | 24m |
| CRK305 | CRK | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-27 12:49 UTC | 2026-04-28 04:18 UTC | 15h 28m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-28 03:54 UTC | 2026-04-28 04:17 UTC | 23m |
| ZDO | ZDO | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-04-28 03:46 UTC | 2026-04-28 04:16 UTC | 30m |
| AAL1105 | American Airlines | Charlotte/Douglas International Airport (KCLT) | NM76 (NM76) | 2026-04-28 01:07 UTC | 2026-04-28 04:13 UTC | 3h 6m |
| TVR4701 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-27 21:23 UTC | 2026-04-28 04:10 UTC | 6h 47m |
| EJA529 | EJA | Tacoma Narrows Airport (KTIW) | Moffett Federal Airfield (KNUQ) | 2026-04-28 02:30 UTC | 2026-04-28 04:10 UTC | 1h 39m |
| FD425 |  | Brisbane International Airport (YBBN) | Lyndley Airport (YLYD) | 2026-04-28 03:36 UTC | 2026-04-28 04:07 UTC | 30m |
| VOZ557 | Virgin Australia | Darwin International Airport (YPDN) | Darwin International Airport (YPDN) | 2026-04-28 03:58 UTC | 2026-04-28 04:07 UTC | 8m |
| N3038N |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-04-28 03:14 UTC | 2026-04-28 04:04 UTC | 50m |
| UPS4D | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-04-27 17:11 UTC | 2026-04-28 04:01 UTC | 10h 50m |
| SFJ23 | SFJ | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-28 03:12 UTC | 2026-04-28 03:59 UTC | 46m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-27 16:25 UTC | 2026-04-28 03:59 UTC | 11h 33m |
| SHA228D | SHA | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-04-28 01:35 UTC | 2026-04-28 03:58 UTC | 2h 22m |
| AEE270 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-28 03:33 UTC | 2026-04-28 03:56 UTC | 22m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-28 03:03 UTC | 2026-04-28 03:51 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
