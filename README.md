# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_05:46:59_UTC-green)

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

**Latest saved flight:** 2026-04-20 05:46:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 05:46:59 UTC

- **44,559** saved flights
- **18,488** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,559** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **536,623.4 tonnes** estimated CO2 emissions
- **31,108,602 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1871 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1075 |
| 4 | EJA | 779 |
| 5 | American Airlines | 740 |
| 6 | Southwest Airlines | 642 |
| 7 | ENY | 584 |
| 8 | AXM | 447 |
| 9 | LATAM Airlines | 446 |
| 10 | Vueling | 445 |
| 11 | Lufthansa | 438 |
| 12 | All Nippon Airways | 401 |
| 13 | AZU | 389 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 360 |
| 16 | LXJ | 354 |
| 17 | WIF | 345 |
| 18 | Swiss International | 339 |
| 19 | Alaska Airlines | 307 |
| 20 | AEE | 303 |
| 21 | EJU | 292 |
| 22 | VIV | 285 |
| 23 | easyJet | 284 |
| 24 | Japan Airlines | 272 |
| 25 | Air France | 250 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 237 |
| 28 | GLO | 234 |
| 29 | AXB | 233 |
| 30 | Cathay Pacific | 226 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35409 |
| 2 | 🇮🇳 IN | 3314 |
| 3 | 🇪🇸 ES | 3261 |
| 4 | 🇦🇺 AU | 3094 |
| 5 | 🇧🇷 BR | 2664 |
| 6 | 🇯🇵 JP | 2446 |
| 7 | 🇮🇹 IT | 2355 |
| 8 | 🇩🇪 DE | 2242 |
| 9 | 🇨🇦 CA | 2175 |
| 10 | 🇨🇴 CO | 2057 |
| 11 | 🇬🇧 GB | 1796 |
| 12 | 🇫🇷 FR | 1684 |
| 13 | 🇲🇽 MX | 1398 |
| 14 | 🇬🇷 GR | 1370 |
| 15 | 🇨🇭 CH | 1204 |
| 16 | 🇳🇴 NO | 1096 |
| 17 | 🇲🇾 MY | 1094 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇵🇭 PH | 800 |
| 21 | 🇹🇭 TH | 794 |
| 22 | 🇹🇷 TR | 787 |
| 23 | 🇰🇷 KR | 733 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 704 |
| 26 | 🇲🇦 MA | 551 |
| 27 | 🇲🇪 ME | 467 |
| 28 | 🇳🇱 NL | 452 |
| 29 | 🇧🇸 BS | 411 |
| 30 | 🇲🇴 MO | 409 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1050 |
| 2 | Tokyo International Airport |  | JP | 834 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | El Dorado International Airport |  | CO | 719 |
| 5 | Indira Gandhi International Airport |  | IN | 713 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 681 |
| 7 | Harry Reid International Airport |  | US | 580 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 528 |
| 11 | Chicago O'Hare International Airport |  | US | 442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 13 | Kuala Lumpur International Airport |  | MY | 434 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 414 |
| 16 | Frankfurt am Main International Airport |  | DE | 413 |
| 17 | Macau International Airport |  | MO | 409 |
| 18 | Madrid Barajas International Airport |  | ES | 394 |
| 19 | Bengaluru International Airport |  | IN | 394 |
| 20 | Tenerife Norte Airport |  | ES | 390 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Congonhas Airport |  | BR | 381 |
| 23 | Malpensa International Airport |  | IT | 374 |
| 24 | Ninoy Aquino International Airport |  | PH | 370 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Daniel K Inouye International Airport |  | US | 331 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 331 |
| 29 | Charles de Gaulle International Airport |  | FR | 325 |
| 30 | Reno/Tahoe International Airport |  | US | 311 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 311 |
| 32 | Vitoria/Foronda Airport |  | ES | 307 |
| 33 | Capua Airport |  | IT | 306 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 302 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 287 |
| 38 | Calgary International Airport |  | CA | 273 |
| 39 | Viracopos International Airport |  | BR | 270 |
| 40 | Don Mueang International Airport |  | TH | 269 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 208 | 1h 7m | 706 km | 2,532.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 161 | 24m | 225 km | 624.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 133 | 28m | 304 km | 697.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 126 | 21m | 244 km | 530.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 119 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 119 | 19m | 165 km | 338.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 92 | 44m | 452 km | 717.0 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 63 | 13m | 99 km | 108.0 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 62 | 57m | 493 km | 527.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAR548 | AAR | Budapest Ferenc Liszt International Airport (LHBP) | Incheon International Airport (RKSI) | 2026-04-19 19:54 UTC | 2026-04-20 05:46 UTC | 9h 52m |
| J999KT |  | Adi Sutjipto International Airport (WARJ) | Cibeureum Airport (WICM) | 2026-04-20 05:21 UTC | 2026-04-20 05:44 UTC | 23m |
| BTN701 | BTN | Netaji Subhash Chandra Bose International Airport (VECC) | Tribhuvan International Airport (VNKT) | 2026-04-20 02:54 UTC | 2026-04-20 05:38 UTC | 2h 43m |
| N138PH |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-04-20 05:08 UTC | 2026-04-20 05:18 UTC | 9m |
| 8WK |  | Melbourne Essendon Airport (YMEN) | Sea Lake Airport (YSLK) | 2026-04-20 04:50 UTC | 2026-04-20 05:17 UTC | 26m |
| N808TP |  | Bremerton Ntl Airport (KPWT) | Portland-Hillsboro Airport (KHIO) | 2026-04-20 03:32 UTC | 2026-04-20 05:12 UTC | 1h 40m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-20 04:41 UTC | 2026-04-20 05:10 UTC | 28m |
| N78US |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-04-20 04:08 UTC | 2026-04-20 05:08 UTC | 59m |
| SWA4122 | Southwest Airlines | San Diego International Airport (KSAN) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-20 04:05 UTC | 2026-04-20 05:08 UTC | 1h 2m |
| LLR802 | LLR | Shimla Airport (VISM) | Shimla Airport (VISM) | 2026-04-20 04:47 UTC | 2026-04-20 05:05 UTC | 18m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-20 04:18 UTC | 2026-04-20 05:02 UTC | 44m |
| SEH1TK | SEH | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-20 04:35 UTC | 2026-04-20 05:00 UTC | 25m |
| NIJ | NIJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-20 04:41 UTC | 2026-04-20 04:59 UTC | 18m |
| AZU4411 | AZU | Fazenda Baluarte Airport (SJBU) | Benedito Mutran Airport (SIBD) | 2026-04-20 03:19 UTC | 2026-04-20 04:54 UTC | 1h 35m |
| DLA8FM | DLA | Luxembourg-Findel International Airport (ELLX) | Frankfurt am Main International Airport (EDDF) | 2026-04-20 04:21 UTC | 2026-04-20 04:54 UTC | 32m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-04-20 04:31 UTC | 2026-04-20 04:53 UTC | 21m |
| ETD841 | Etihad Airways | OM11 (OM11) | Bezymyanka Airfield (UWWG) | 2026-04-19 22:48 UTC | 2026-04-20 04:51 UTC | 6h 3m |
| ANZ623 | ANZ | Auckland International Airport (NZAA) | Glenorchy Airport (NZGY) | 2026-04-20 03:25 UTC | 2026-04-20 04:50 UTC | 1h 24m |
| RYR13KA | Ryanair | Torino / Caselle International Airport (LIMF) | Decimomannu Airport (LIED) | 2026-04-20 03:59 UTC | 2026-04-20 04:48 UTC | 49m |
| EJA353 | EJA | Birmingham-Shuttlesworth International Airport (KBHM) | Ohkay Owingeh Airport (KE14) | 2026-04-20 01:49 UTC | 2026-04-20 04:48 UTC | 2h 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
