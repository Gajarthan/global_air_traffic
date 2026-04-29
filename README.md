# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_07:05:29_UTC-green)

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

**Latest saved flight:** 2026-04-29 07:05:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 07:05:29 UTC

- **58,784** saved flights
- **22,846** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,784** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **713,869.9 tonnes** estimated CO2 emissions
- **41,383,762 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2494 |
| 2 | SkyWest Airlines | 2204 |
| 3 | IndiGo | 1344 |
| 4 | EJA | 1039 |
| 5 | American Airlines | 924 |
| 6 | Southwest Airlines | 839 |
| 7 | Lufthansa | 745 |
| 8 | ENY | 732 |
| 9 | Vueling | 586 |
| 10 | AXM | 577 |
| 11 | LATAM Airlines | 558 |
| 12 | All Nippon Airways | 524 |
| 13 | WIF | 490 |
| 14 | Delta Air Lines | 487 |
| 15 | AZU | 486 |
| 16 | Swiss International | 465 |
| 17 | QLK | 463 |
| 18 | LXJ | 416 |
| 19 | Alaska Airlines | 404 |
| 20 | AEE | 392 |
| 21 | easyJet | 384 |
| 22 | EJU | 381 |
| 23 | VIV | 372 |
| 24 | Japan Airlines | 343 |
| 25 | Air France | 342 |
| 26 | Cathay Pacific | 339 |
| 27 | AXB | 322 |
| 28 | AIQ | 297 |
| 29 | JetBlue | 295 |
| 30 | United Airlines | 295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46514 |
| 2 | 🇪🇸 ES | 4271 |
| 3 | 🇮🇳 IN | 4242 |
| 4 | 🇦🇺 AU | 4011 |
| 5 | 🇧🇷 BR | 3327 |
| 6 | 🇩🇪 DE | 3247 |
| 7 | 🇮🇹 IT | 3212 |
| 8 | 🇯🇵 JP | 3192 |
| 9 | 🇨🇦 CA | 2908 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2481 |
| 12 | 🇫🇷 FR | 2326 |
| 13 | 🇲🇽 MX | 1855 |
| 14 | 🇬🇷 GR | 1750 |
| 15 | 🇨🇭 CH | 1644 |
| 16 | 🇳🇴 NO | 1594 |
| 17 | 🇲🇾 MY | 1401 |
| 18 | 🇿🇦 ZA | 1196 |
| 19 | 🇳🇿 NZ | 1106 |
| 20 | 🇹🇷 TR | 1064 |
| 21 | 🇹🇭 TH | 1060 |
| 22 | 🇵🇭 PH | 994 |
| 23 | 🇵🇱 PL | 944 |
| 24 | 🇰🇷 KR | 935 |
| 25 | 🇬🇹 GT | 860 |
| 26 | 🇲🇦 MA | 740 |
| 27 | 🇲🇪 ME | 636 |
| 28 | 🇲🇴 MO | 633 |
| 29 | 🇳🇱 NL | 613 |
| 30 | 🇮🇩 ID | 503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1321 |
| 2 | Tokyo International Airport |  | JP | 1086 |
| 3 | Denver International Airport |  | US | 982 |
| 4 | Indira Gandhi International Airport |  | IN | 891 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 862 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 748 |
| 9 | Frankfurt am Main International Airport |  | DE | 735 |
| 10 | Zurich Airport |  | CH | 707 |
| 11 | La Aurora Airport |  | GT | 649 |
| 12 | Macau International Airport |  | MO | 633 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 581 |
| 14 | Chicago O'Hare International Airport |  | US | 560 |
| 15 | Kuala Lumpur International Airport |  | MY | 552 |
| 16 | Madrid Barajas International Airport |  | ES | 546 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 543 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 19 | Bengaluru International Airport |  | IN | 510 |
| 20 | Malpensa International Airport |  | IT | 507 |
| 21 | Congonhas Airport |  | BR | 479 |
| 22 | Charlotte/Douglas International Airport |  | US | 468 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 458 |
| 25 | Salt Lake City International Airport |  | US | 454 |
| 26 | Charles de Gaulle International Airport |  | FR | 454 |
| 27 | Capua Airport |  | IT | 450 |
| 28 | Daniel K Inouye International Airport |  | US | 441 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 423 |
| 31 | Barcelona International Airport |  | ES | 400 |
| 32 | Vitoria/Foronda Airport |  | ES | 396 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 390 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 387 |
| 35 | O. R. Tambo International Airport |  | ZA | 382 |
| 36 | Reno/Tahoe International Airport |  | US | 376 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 374 |
| 38 | Don Mueang International Airport |  | TH | 361 |
| 39 | Amsterdam Airport Schiphol |  | NL | 356 |
| 40 | Calgary International Airport |  | CA | 347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 194 | 21m | 244 km | 816.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 174 | 1h 27m | 910 km | 2,730.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 165 | 28m | 304 km | 865.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 122 | 1h 12m | 770 km | 1,620.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 94 | 20m | 250 km | 406.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 81 | 1h 43m | 1,156 km | 1,615.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 74 | 14m | 154 km | 196.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| G72234 |  | Laredo International Airport (KLRD) | Quetzalcoatl International Airport (MMNL) | 2026-04-29 06:08 UTC | 2026-04-29 07:05 UTC | 57m |
| SHW02A | SHW | Esbjerg Airport (EKEB) | Westerland Sylt Airport (EDXW) | 2026-04-29 06:27 UTC | 2026-04-29 06:57 UTC | 30m |
| TUI68E | TUI | Stuttgart Airport (EDDS) | Kucove Air Base (LAKV) | 2026-04-29 05:30 UTC | 2026-04-29 06:56 UTC | 1h 26m |
| SWI | SWI | Warrnambool Airport (YWBL) | Derrinallum Airport (YDER) | 2026-04-29 06:28 UTC | 2026-04-29 06:46 UTC | 17m |
|  |  | Langtang Airport (VNLT) | Tribhuvan International Airport (VNKT) | 2026-04-29 06:36 UTC | 2026-04-29 06:37 UTC | 1m |
| JRP | JRP | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-29 05:36 UTC | 2026-04-29 06:28 UTC | 52m |
| AEE3MK | AEE | Mikonos Airport (LGMK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-29 05:59 UTC | 2026-04-29 06:25 UTC | 25m |
| ASI72 | ASI | Chandler Municipal Airport (KCHD) | Montezuma Airport (19AZ) | 2026-04-29 05:36 UTC | 2026-04-29 06:24 UTC | 48m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-29 05:39 UTC | 2026-04-29 06:21 UTC | 42m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-29 05:08 UTC | 2026-04-29 06:21 UTC | 1h 12m |
| TAM3960 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Prefeito Renato Moreira Airport (SBIZ) | 2026-04-29 03:42 UTC | 2026-04-29 06:19 UTC | 2h 37m |
| WIF8HM | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-04-29 05:41 UTC | 2026-04-29 06:18 UTC | 36m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-29 05:50 UTC | 2026-04-29 06:16 UTC | 26m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-29 05:51 UTC | 2026-04-29 06:14 UTC | 22m |
| RYR6LG | Ryanair | Stockholm-Arlanda Airport (ESSA) | Trstenik Airport (LYTR) | 2026-04-29 04:03 UTC | 2026-04-29 06:11 UTC | 2h 7m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-04-29 05:36 UTC | 2026-04-29 06:11 UTC | 34m |
| VOE2972 | VOE | Lille-Lesquin Airport (LFQQ) | Dubrovnik Airport (LDDU) | 2026-04-29 04:14 UTC | 2026-04-29 06:10 UTC | 1h 56m |
| BEL1PD | Brussels Airlines | Marseille Provence Airport (LFML) | Brussels Airport (EBBR) | 2026-04-29 04:43 UTC | 2026-04-29 06:09 UTC | 1h 25m |
| PAG13 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Mccreary Airport (CJR8) | 2026-04-29 05:42 UTC | 2026-04-29 06:09 UTC | 26m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-29 04:54 UTC | 2026-04-29 06:08 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
