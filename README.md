# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_10:13:35_UTC-green)

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

**Latest saved flight:** 2026-04-25 10:13:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 10:13:35 UTC

- **53,181** saved flights
- **21,180** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,181** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **636,345.9 tonnes** estimated CO2 emissions
- **36,889,616 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2230 |
| 2 | SkyWest Airlines | 2007 |
| 3 | IndiGo | 1211 |
| 4 | EJA | 944 |
| 5 | American Airlines | 857 |
| 6 | Southwest Airlines | 754 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 617 |
| 9 | Vueling | 532 |
| 10 | AXM | 516 |
| 11 | LATAM Airlines | 509 |
| 12 | All Nippon Airways | 475 |
| 13 | AZU | 449 |
| 14 | WIF | 441 |
| 15 | Delta Air Lines | 440 |
| 16 | QLK | 415 |
| 17 | Swiss International | 405 |
| 18 | LXJ | 392 |
| 19 | AEE | 357 |
| 20 | Alaska Airlines | 353 |
| 21 | easyJet | 341 |
| 22 | VIV | 338 |
| 23 | EJU | 337 |
| 24 | Japan Airlines | 312 |
| 25 | Air France | 305 |
| 26 | AXB | 283 |
| 27 | Cathay Pacific | 281 |
| 28 | AIQ | 273 |
| 29 | JetBlue | 272 |
| 30 | United Airlines | 272 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42391 |
| 2 | 🇪🇸 ES | 3840 |
| 3 | 🇮🇳 IN | 3817 |
| 4 | 🇦🇺 AU | 3615 |
| 5 | 🇧🇷 BR | 3057 |
| 6 | 🇯🇵 JP | 2878 |
| 7 | 🇮🇹 IT | 2852 |
| 8 | 🇩🇪 DE | 2821 |
| 9 | 🇨🇦 CA | 2657 |
| 10 | 🇨🇴 CO | 2444 |
| 11 | 🇬🇧 GB | 2217 |
| 12 | 🇫🇷 FR | 2063 |
| 13 | 🇲🇽 MX | 1641 |
| 14 | 🇬🇷 GR | 1600 |
| 15 | 🇨🇭 CH | 1489 |
| 16 | 🇳🇴 NO | 1431 |
| 17 | 🇲🇾 MY | 1254 |
| 18 | 🇿🇦 ZA | 1099 |
| 19 | 🇳🇿 NZ | 1014 |
| 20 | 🇹🇭 TH | 967 |
| 21 | 🇹🇷 TR | 951 |
| 22 | 🇵🇭 PH | 913 |
| 23 | 🇰🇷 KR | 869 |
| 24 | 🇵🇱 PL | 843 |
| 25 | 🇬🇹 GT | 815 |
| 26 | 🇲🇦 MA | 655 |
| 27 | 🇲🇪 ME | 570 |
| 28 | 🇳🇱 NL | 541 |
| 29 | 🇲🇴 MO | 517 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1214 |
| 2 | Tokyo International Airport |  | JP | 975 |
| 3 | Denver International Airport |  | US | 881 |
| 4 | El Dorado International Airport |  | CO | 830 |
| 5 | Indira Gandhi International Airport |  | IN | 811 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 792 |
| 7 | Guaymaral Airport |  | CO | 730 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 623 |
| 10 | La Aurora Airport |  | GT | 609 |
| 11 | Frankfurt am Main International Airport |  | DE | 605 |
| 12 | Chicago O'Hare International Airport |  | US | 524 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 14 | Macau International Airport |  | MO | 517 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 499 |
| 17 | Madrid Barajas International Airport |  | ES | 492 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 456 |
| 20 | Malpensa International Airport |  | IT | 443 |
| 21 | Congonhas Airport |  | BR | 442 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Ninoy Aquino International Airport |  | PH | 421 |
| 24 | Tenerife Norte Airport |  | ES | 419 |
| 25 | Charles de Gaulle International Airport |  | FR | 401 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 397 |
| 27 | Salt Lake City International Airport |  | US | 395 |
| 28 | Daniel K Inouye International Airport |  | US | 387 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 380 |
| 30 | Capua Airport |  | IT | 374 |
| 31 | Vitoria/Foronda Airport |  | ES | 363 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 33 | Barcelona International Airport |  | ES | 357 |
| 34 | Reno/Tahoe International Airport |  | US | 355 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 351 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 350 |
| 37 | O. R. Tambo International Airport |  | ZA | 346 |
| 38 | Don Mueang International Airport |  | TH | 327 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 295 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 162 | 21m | 244 km | 682.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 151 | 1h 27m | 910 km | 2,369.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 137 | 19m | 165 km | 389.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 106 | 44m | 452 km | 826.1 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 1m | 695 km | 911.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 69 | 24m | 55 km | 65.6 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 68 | 13m | - | - |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TOPCLFE1 | TOP | RAF Topcliffe (EGXZ) | RAF Topcliffe (EGXZ) | 2026-04-25 09:30 UTC | 2026-04-25 10:13 UTC | 43m |
| VJT569 | VJT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-04-25 09:43 UTC | 2026-04-25 10:11 UTC | 28m |
| RNA409 | RNA | Langtang Airport (VNLT) | Zhuhai Airport (ZGSD) | 2026-04-25 06:50 UTC | 2026-04-25 10:06 UTC | 3h 16m |
| SXBDZ | SXB | Megara Airport (LGMG) | Megara Airport (LGMG) | 2026-04-25 08:58 UTC | 2026-04-25 10:01 UTC | 1h 3m |
| UAH438 | UAH | RAF Cranwell (EGYD) | RAF Cranwell (EGYD) | 2026-04-25 09:34 UTC | 2026-04-25 09:54 UTC | 20m |
| WIF5NH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-25 09:09 UTC | 2026-04-25 09:36 UTC | 26m |
| VJT569 | VJT | London Luton Airport (EGGW) | Newquay Cornwall Airport (EGHQ) | 2026-04-25 08:44 UTC | 2026-04-25 09:30 UTC | 46m |
| AM376 |  | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-04-25 08:52 UTC | 2026-04-25 09:30 UTC | 38m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-04-25 09:26 UTC | 2026-04-25 09:30 UTC | 4m |
| RYR738U | Ryanair | L'Aquila / Preturo Airport (LIAP) | Pantelleria Airport (LICG) | 2026-04-25 09:03 UTC | 2026-04-25 09:29 UTC | 26m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-25 08:52 UTC | 2026-04-25 09:29 UTC | 36m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-24 22:10 UTC | 2026-04-25 09:29 UTC | 11h 19m |
| FLORIAN2 | FLO | Luneburg Airport (EDHG) | Luneburg Airport (EDHG) | 2026-04-25 08:43 UTC | 2026-04-25 09:24 UTC | 41m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Reykholar Airport (BIRE) | 2026-04-25 09:02 UTC | 2026-04-25 09:23 UTC | 21m |
| LNK871S | LNK | O. R. Tambo International Airport (FAOR) | Montrose Airport (FAMV) | 2026-04-25 08:56 UTC | 2026-04-25 09:16 UTC | 19m |
| D0621 |  | Wittmundhafen Airport (ETNT) | Wittmundhafen Airport (ETNT) | 2026-04-25 08:43 UTC | 2026-04-25 09:12 UTC | 28m |
| JAL669 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-25 08:04 UTC | 2026-04-25 09:07 UTC | 1h 3m |
| 4XHSC |  | LL59 (LL59) | LLSD (LLSD) | 2026-04-25 09:04 UTC | 2026-04-25 09:06 UTC | 2m |
| OCN4AP | OCN | Munich International Airport (EDDM) | Mikonos Airport (LGMK) | 2026-04-25 06:58 UTC | 2026-04-25 09:06 UTC | 2h 8m |
| EJU181X | EJU | Nice-Cote d'Azur Airport (LFMN) | Paris-Orly Airport (LFPO) | 2026-04-25 07:54 UTC | 2026-04-25 09:04 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
