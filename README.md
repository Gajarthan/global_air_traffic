# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_22:03:53_UTC-green)

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

**Latest saved flight:** 2026-05-05 22:03:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 22:03:53 UTC

- **69,856** saved flights
- **26,090** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,856** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **859,900.8 tonnes** estimated CO2 emissions
- **49,849,323 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3007 |
| 2 | SkyWest Airlines | 2612 |
| 3 | IndiGo | 1599 |
| 4 | EJA | 1271 |
| 5 | American Airlines | 1093 |
| 6 | Southwest Airlines | 1005 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 866 |
| 9 | Vueling | 690 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 649 |
| 12 | WIF | 596 |
| 13 | Delta Air Lines | 589 |
| 14 | All Nippon Airways | 585 |
| 15 | AZU | 568 |
| 16 | Swiss International | 539 |
| 17 | QLK | 535 |
| 18 | LXJ | 506 |
| 19 | Alaska Airlines | 484 |
| 20 | easyJet | 468 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 438 |
| 24 | Cathay Pacific | 422 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 340 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55527 |
| 2 | 🇪🇸 ES | 5103 |
| 3 | 🇮🇳 IN | 5029 |
| 4 | 🇦🇺 AU | 4605 |
| 5 | 🇧🇷 BR | 3929 |
| 6 | 🇩🇪 DE | 3899 |
| 7 | 🇮🇹 IT | 3832 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3449 |
| 10 | 🇬🇧 GB | 3036 |
| 11 | 🇫🇷 FR | 2768 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2219 |
| 14 | 🇬🇷 GR | 2086 |
| 15 | 🇨🇭 CH | 1922 |
| 16 | 🇳🇴 NO | 1913 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1290 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1258 |
| 22 | 🇵🇭 PH | 1160 |
| 23 | 🇵🇱 PL | 1151 |
| 24 | 🇬🇹 GT | 1123 |
| 25 | 🇰🇷 KR | 1111 |
| 26 | 🇲🇦 MA | 843 |
| 27 | 🇲🇴 MO | 794 |
| 28 | 🇲🇪 ME | 755 |
| 29 | 🇳🇱 NL | 728 |
| 30 | 🇮🇩 ID | 588 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1556 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1158 |
| 4 | Indira Gandhi International Airport |  | IN | 1056 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1021 |
| 6 | Frankfurt am Main International Airport |  | DE | 895 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 871 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 835 |
| 11 | Zurich Airport |  | CH | 826 |
| 12 | Macau International Airport |  | MO | 794 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 700 |
| 14 | Chicago O'Hare International Airport |  | US | 669 |
| 15 | Kuala Lumpur International Airport |  | MY | 668 |
| 16 | Madrid Barajas International Airport |  | ES | 665 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 626 |
| 18 | Malpensa International Airport |  | IT | 609 |
| 19 | Bengaluru International Airport |  | IN | 605 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Salt Lake City International Airport |  | US | 565 |
| 22 | Congonhas Airport |  | BR | 559 |
| 23 | Charlotte/Douglas International Airport |  | US | 550 |
| 24 | Charles de Gaulle International Airport |  | FR | 550 |
| 25 | Tenerife Norte Airport |  | ES | 544 |
| 26 | Capua Airport |  | IT | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Daniel K Inouye International Airport |  | US | 510 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 510 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 494 |
| 31 | Barcelona International Airport |  | ES | 486 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 473 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 438 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 437 |
| 38 | Amsterdam Airport Schiphol |  | NL | 430 |
| 39 | Reno/Tahoe International Airport |  | US | 414 |
| 40 | Calgary International Airport |  | CA | 413 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 240 | 21m | 244 km | 1,010.6 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 173 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 97 | 1h 2m | 695 km | 1,162.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9924W |  | Cecil Airport (KVQQ) | Cuyler Field (FD27) | 2026-05-05 21:33 UTC | 2026-05-05 22:03 UTC | 30m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-05 10:57 UTC | 2026-05-05 22:02 UTC | 11h 4m |
| EDV5541 | EDV | Hartsfield/Jackson Atlanta International Airport (KATL) | Columbus County Regional Airport (KCPC) | 2026-05-05 20:56 UTC | 2026-05-05 22:00 UTC | 1h 4m |
| N123CF |  | Millville Municipal Airport (KMIV) | Albert J Ellis Airport (KOAJ) | 2026-05-05 20:40 UTC | 2026-05-05 21:59 UTC | 1h 18m |
| N681DC |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-05 21:40 UTC | 2026-05-05 21:58 UTC | 18m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-05 10:41 UTC | 2026-05-05 21:57 UTC | 11h 16m |
| N631DB |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Pagel's Field (67MN) | 2026-05-05 21:26 UTC | 2026-05-05 21:48 UTC | 22m |
| WC399 |  | Fernando Air Base (RPUL) | Fernando Air Base (RPUL) | 2026-05-05 21:34 UTC | 2026-05-05 21:45 UTC | 10m |
| AIH587 | AIH | Incheon International Airport (RKSI) | Ted Stevens Anchorage International Airport (PANC) | 2026-05-05 14:25 UTC | 2026-05-05 21:44 UTC | 7h 18m |
| KYOTE048 | KYO | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Deer Valley Airport (KDVT) | 2026-05-05 20:43 UTC | 2026-05-05 21:43 UTC | 1h 0m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-05 17:35 UTC | 2026-05-05 21:43 UTC | 4h 7m |
| N80298 |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-05-05 20:54 UTC | 2026-05-05 21:38 UTC | 43m |
| N900EM |  | Van Nuys Airport (KVNY) | Sequoia Field (KD86) | 2026-05-05 21:11 UTC | 2026-05-05 21:36 UTC | 25m |
| N34DG |  | Davidson County Executive Airport (KEXX) | Dublin Field (NC82) | 2026-05-05 21:12 UTC | 2026-05-05 21:35 UTC | 22m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 21:16 UTC | 2026-05-05 21:28 UTC | 12m |
| N24YP |  | Mesa Gateway Airport (KIWA) | Henderson Executive Airport (KHND) | 2026-05-05 20:43 UTC | 2026-05-05 21:27 UTC | 44m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-05 17:10 UTC | 2026-05-05 21:24 UTC | 4h 14m |
| CGIXO | CGI | Edmonton / Cooking Lake Airport (CEZ3) | Tofield Airport (CEV7) | 2026-05-05 21:13 UTC | 2026-05-05 21:24 UTC | 11m |
| LS12 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-05 20:40 UTC | 2026-05-05 21:22 UTC | 42m |
| N246SF |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-05-05 21:10 UTC | 2026-05-05 21:22 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
