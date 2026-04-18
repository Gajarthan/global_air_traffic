# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_15:33:44_UTC-green)

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

**Latest saved flight:** 2026-04-18 15:33:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 15:33:44 UTC

- **41,332** saved flights
- **17,470** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,332** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **496,866.0 tonnes** estimated CO2 emissions
- **28,803,823 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1741 |
| 2 | SkyWest Airlines | 1593 |
| 3 | IndiGo | 1022 |
| 4 | EJA | 714 |
| 5 | American Airlines | 685 |
| 6 | Southwest Airlines | 577 |
| 7 | ENY | 523 |
| 8 | AXM | 434 |
| 9 | Vueling | 413 |
| 10 | LATAM Airlines | 410 |
| 11 | Lufthansa | 404 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 368 |
| 14 | Delta Air Lines | 348 |
| 15 | QLK | 341 |
| 16 | LXJ | 326 |
| 17 | WIF | 324 |
| 18 | Swiss International | 319 |
| 19 | AEE | 278 |
| 20 | Alaska Airlines | 277 |
| 21 | EJU | 271 |
| 22 | easyJet | 268 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 235 |
| 26 | United Airlines | 223 |
| 27 | JetBlue | 222 |
| 28 | AXB | 217 |
| 29 | GLO | 217 |
| 30 | EDV | 216 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32474 |
| 2 | 🇮🇳 IN | 3122 |
| 3 | 🇪🇸 ES | 3053 |
| 4 | 🇦🇺 AU | 2914 |
| 5 | 🇧🇷 BR | 2468 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2148 |
| 8 | 🇩🇪 DE | 2096 |
| 9 | 🇨🇦 CA | 2015 |
| 10 | 🇨🇴 CO | 1957 |
| 11 | 🇬🇧 GB | 1684 |
| 12 | 🇫🇷 FR | 1594 |
| 13 | 🇲🇽 MX | 1293 |
| 14 | 🇬🇷 GR | 1256 |
| 15 | 🇨🇭 CH | 1160 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1030 |
| 18 | 🇿🇦 ZA | 863 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 740 |
| 22 | 🇹🇷 TR | 722 |
| 23 | 🇬🇹 GT | 698 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 659 |
| 26 | 🇲🇦 MA | 508 |
| 27 | 🇳🇱 NL | 425 |
| 28 | 🇲🇪 ME | 422 |
| 29 | 🇧🇸 BS | 390 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 949 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 679 |
| 5 | Indira Gandhi International Airport |  | IN | 672 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 624 |
| 7 | Harry Reid International Airport |  | US | 531 |
| 8 | Guaymaral Airport |  | CO | 521 |
| 9 | La Aurora Airport |  | GT | 514 |
| 10 | Zurich Airport |  | CH | 501 |
| 11 | Kuala Lumpur International Airport |  | MY | 415 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 393 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 392 |
| 16 | Macau International Airport |  | MO | 376 |
| 17 | Madrid Barajas International Airport |  | ES | 376 |
| 18 | Frankfurt am Main International Airport |  | DE | 373 |
| 19 | Bengaluru International Airport |  | IN | 368 |
| 20 | Charlotte/Douglas International Airport |  | US | 361 |
| 21 | Tenerife Norte Airport |  | ES | 361 |
| 22 | Congonhas Airport |  | BR | 360 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 334 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 307 |
| 28 | Charles de Gaulle International Airport |  | FR | 304 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 302 |
| 30 | Vitoria/Foronda Airport |  | ES | 290 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 286 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 285 |
| 33 | Reno/Tahoe International Airport |  | US | 281 |
| 34 | O. R. Tambo International Airport |  | ZA | 280 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 280 |
| 36 | Capua Airport |  | IT | 274 |
| 37 | Barcelona International Airport |  | ES | 264 |
| 38 | Viracopos International Airport |  | BR | 254 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Don Mueang International Airport |  | TH | 246 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 208 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 110 | 21m | 244 km | 463.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 104 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 98 | 26m | 275 km | 464.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 68 | 20m | 250 km | 293.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 62 | 16m | 162 km | 173.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XBEOI | XBE | Cozumel International Airport (MMCZ) | Cozumel International Airport (MMCZ) | 2026-04-18 15:02 UTC | 2026-04-18 15:33 UTC | 31m |
| N521NG |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-04-18 15:16 UTC | 2026-04-18 15:30 UTC | 14m |
| DESSS | DES | Ingolstadt Manching Airport (ETSI) | Ingolstadt Manching Airport (ETSI) | 2026-04-18 14:51 UTC | 2026-04-18 15:30 UTC | 38m |
| PH1213 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-04-18 15:09 UTC | 2026-04-18 15:28 UTC | 18m |
| BYF31 | BYF | San Carlos Airport (KSQL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-18 14:58 UTC | 2026-04-18 15:17 UTC | 19m |
| N847AA |  | North Palm Beach County General Aviation Airport (KF45) | North Palm Beach County General Aviation Airport (KF45) | 2026-04-18 14:47 UTC | 2026-04-18 15:15 UTC | 27m |
| N5QD |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-04-18 15:14 UTC | 2026-04-18 15:15 UTC | 0m |
| N1484X |  | Concord-Padgett Regional Airport (KJQF) | Brown Field (46NC) | 2026-04-18 14:51 UTC | 2026-04-18 15:12 UTC | 21m |
| N492LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-18 14:11 UTC | 2026-04-18 15:11 UTC | 59m |
| BCS644 | BCS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-17 23:20 UTC | 2026-04-18 15:10 UTC | 15h 50m |
| DKKHA | DKK | Hoefen Airport (LOIR) | Samedan Airport (LSZS) | 2026-04-18 13:03 UTC | 2026-04-18 15:10 UTC | 2h 6m |
| GMILS | GMI | RAF Church Fenton (EGXG) | RAF Church Fenton (EGXG) | 2026-04-18 14:22 UTC | 2026-04-18 15:07 UTC | 44m |
| N80790 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-18 14:22 UTC | 2026-04-18 15:04 UTC | 42m |
| NSZ2CP | NSZ | Malaga Airport (LEMG) | Stockholm-Arlanda Airport (ESSA) | 2026-04-18 11:14 UTC | 2026-04-18 15:04 UTC | 3h 50m |
| N5116Q |  | Lake Norman Airpark (K14A) | Statesville Regional Airport (KSVH) | 2026-04-18 14:19 UTC | 2026-04-18 15:03 UTC | 43m |
| N1416E |  | Mcnary Field (KSLE) | Independence State Airport (K7S5) | 2026-04-18 14:48 UTC | 2026-04-18 15:03 UTC | 14m |
| N169BA |  | Garrett Ranch Airport (77XS) | TE77 (TE77) | 2026-04-18 14:47 UTC | 2026-04-18 14:58 UTC | 10m |
| HB3370 |  | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-04-18 13:35 UTC | 2026-04-18 14:55 UTC | 1h 19m |
| N623LJ |  | Minden-Tahoe Airport (KMEV) | Pinenut Airport (NV55) | 2026-04-18 14:33 UTC | 2026-04-18 14:54 UTC | 20m |
| N658DG |  | Hastings Municipal Airport (KHSI) | Harold Davidson Field (KVMR) | 2026-04-18 13:59 UTC | 2026-04-18 14:53 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
