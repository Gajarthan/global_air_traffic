# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_16:21:39_UTC-green)

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

**Latest saved flight:** 2026-05-01 16:21:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 16:21:39 UTC

- **62,459** saved flights
- **23,934** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **62,459** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **762,277.2 tonnes** estimated CO2 emissions
- **44,189,982 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2622 |
| 2 | SkyWest Airlines | 2307 |
| 3 | IndiGo | 1431 |
| 4 | EJA | 1123 |
| 5 | American Airlines | 971 |
| 6 | Southwest Airlines | 882 |
| 7 | Lufthansa | 805 |
| 8 | ENY | 766 |
| 9 | Vueling | 611 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 589 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 531 |
| 14 | Delta Air Lines | 518 |
| 15 | AZU | 511 |
| 16 | QLK | 498 |
| 17 | Swiss International | 483 |
| 18 | LXJ | 444 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 409 |
| 21 | easyJet | 405 |
| 22 | EJU | 400 |
| 23 | VIV | 391 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 362 |
| 27 | AXB | 347 |
| 28 | AIQ | 319 |
| 29 | CXK | 311 |
| 30 | MXY | 304 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49354 |
| 2 | 🇪🇸 ES | 4518 |
| 3 | 🇮🇳 IN | 4516 |
| 4 | 🇦🇺 AU | 4288 |
| 5 | 🇧🇷 BR | 3544 |
| 6 | 🇩🇪 DE | 3481 |
| 7 | 🇯🇵 JP | 3409 |
| 8 | 🇮🇹 IT | 3394 |
| 9 | 🇨🇦 CA | 3072 |
| 10 | 🇬🇧 GB | 2657 |
| 11 | 🇨🇴 CO | 2637 |
| 12 | 🇫🇷 FR | 2461 |
| 13 | 🇲🇽 MX | 1961 |
| 14 | 🇬🇷 GR | 1859 |
| 15 | 🇨🇭 CH | 1749 |
| 16 | 🇳🇴 NO | 1733 |
| 17 | 🇲🇾 MY | 1489 |
| 18 | 🇿🇦 ZA | 1277 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1127 |
| 21 | 🇹🇷 TR | 1101 |
| 22 | 🇵🇭 PH | 1062 |
| 23 | 🇵🇱 PL | 1008 |
| 24 | 🇰🇷 KR | 1008 |
| 25 | 🇬🇹 GT | 960 |
| 26 | 🇲🇦 MA | 766 |
| 27 | 🇲🇴 MO | 702 |
| 28 | 🇲🇪 ME | 679 |
| 29 | 🇳🇱 NL | 653 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1374 |
| 2 | Tokyo International Airport |  | JP | 1152 |
| 3 | Denver International Airport |  | US | 1029 |
| 4 | Indira Gandhi International Airport |  | IN | 948 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 910 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 832 |
| 8 | Frankfurt am Main International Airport |  | DE | 804 |
| 9 | Harry Reid International Airport |  | US | 794 |
| 10 | Zurich Airport |  | CH | 743 |
| 11 | La Aurora Airport |  | GT | 717 |
| 12 | Macau International Airport |  | MO | 702 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 612 |
| 14 | Kuala Lumpur International Airport |  | MY | 590 |
| 15 | Madrid Barajas International Airport |  | ES | 587 |
| 16 | Chicago O'Hare International Airport |  | US | 586 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 566 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 543 |
| 20 | Malpensa International Airport |  | IT | 537 |
| 21 | Congonhas Airport |  | BR | 511 |
| 22 | Charlotte/Douglas International Airport |  | US | 496 |
| 23 | Salt Lake City International Airport |  | US | 487 |
| 24 | Tenerife Norte Airport |  | ES | 486 |
| 25 | Charles de Gaulle International Airport |  | FR | 484 |
| 26 | Ninoy Aquino International Airport |  | PH | 482 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 461 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 455 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 448 |
| 31 | Barcelona International Airport |  | ES | 417 |
| 32 | Vitoria/Foronda Airport |  | ES | 417 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 411 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 408 |
| 35 | O. R. Tambo International Airport |  | ZA | 403 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 393 |
| 37 | Reno/Tahoe International Airport |  | US | 388 |
| 38 | Don Mueang International Airport |  | TH | 387 |
| 39 | Amsterdam Airport Schiphol |  | NL | 386 |
| 40 | Calgary International Airport |  | CA | 369 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 342 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 208 | 21m | 244 km | 875.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 153 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 111 | 21m | 99 km | 190.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 102 | 20m | 250 km | 440.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 96 | 28m | 152 km | 250.9 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 94 | 20m | 147 km | 237.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 86 | 1h 1m | 695 km | 1,030.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 83 | 23m | 55 km | 78.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 80 | 1h 43m | 1,423 km | 1,963.3 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SEH921 | SEH | Madrid Barajas International Airport (LEMD) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-01 13:21 UTC | 2026-05-01 16:21 UTC | 2h 59m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-05-01 15:31 UTC | 2026-05-01 16:13 UTC | 41m |
| PAT973 | PAT | Maxwell Afb Airport (KMXF) | Nelson Airfield (TN99) | 2026-05-01 15:04 UTC | 2026-05-01 16:08 UTC | 1h 4m |
| N253EA |  | Prescott Regional/Ernest A Love Field (KPRC) | AZ86 (AZ86) | 2026-05-01 15:53 UTC | 2026-05-01 16:05 UTC | 11m |
| RTV2M | RTV | Vilar Da Luz Airport (LPVL) | Viseu Airport (LPVZ) | 2026-05-01 14:43 UTC | 2026-05-01 16:05 UTC | 1h 22m |
| AZG784 | AZG | Frankfurt-Hahn Airport (EDFH) | Zhuhai Airport (ZGSD) | 2026-04-30 23:48 UTC | 2026-05-01 16:03 UTC | 16h 14m |
| BSM31 | BSM | Durant Regional/Eaker Field (KDUA) | Madill Municipal Airport (K1F4) | 2026-05-01 15:46 UTC | 2026-05-01 16:02 UTC | 15m |
| TGGUH | TGG | San Jose Airport (MGSJ) | La Aurora Airport (MGGT) | 2026-05-01 15:46 UTC | 2026-05-01 16:02 UTC | 15m |
| N881LA |  | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-05-01 15:02 UTC | 2026-05-01 15:59 UTC | 56m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-05-01 12:42 UTC | 2026-05-01 15:55 UTC | 3h 13m |
| N102GK |  | Bend Municipal Airport (KBDN) | OG12 (OG12) | 2026-05-01 15:42 UTC | 2026-05-01 15:55 UTC | 12m |
| N8316Z |  | Corona Municipal Airport (KAJO) | Big Bear City Airport (KL35) | 2026-05-01 15:28 UTC | 2026-05-01 15:53 UTC | 25m |
| OST48 | OST | Boice Field (88OK) | Flying G Ranch Airport (3OK8) | 2026-05-01 15:35 UTC | 2026-05-01 15:51 UTC | 16m |
| N101CH |  | Josephs Field (IG07) | Josephs Field (IG07) | 2026-05-01 15:43 UTC | 2026-05-01 15:50 UTC | 6m |
| WIF158 | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-01 14:54 UTC | 2026-05-01 15:49 UTC | 55m |
| N318SV |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-05-01 15:15 UTC | 2026-05-01 15:48 UTC | 33m |
| N97VS |  | Iowa City Municipal Airport (KIOW) | Scottsdale Airport (KSDL) | 2026-05-01 12:38 UTC | 2026-05-01 15:46 UTC | 3h 8m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 15:19 UTC | 2026-05-01 15:44 UTC | 25m |
| KLM35U | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Nuremberg Airport (EDDN) | 2026-05-01 14:51 UTC | 2026-05-01 15:44 UTC | 53m |
| N739TS |  | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-05-01 14:51 UTC | 2026-05-01 15:44 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
