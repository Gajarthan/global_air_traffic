# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_05:35:24_UTC-green)

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

**Latest saved flight:** 2026-04-19 05:35:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 05:35:24 UTC

- **42,386** saved flights
- **17,807** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,386** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **508,299.3 tonnes** estimated CO2 emissions
- **29,466,628 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1767 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1033 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 437 |
| 9 | LATAM Airlines | 423 |
| 10 | Vueling | 422 |
| 11 | Lufthansa | 414 |
| 12 | All Nippon Airways | 381 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 344 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 288 |
| 20 | AEE | 282 |
| 21 | EJU | 277 |
| 22 | easyJet | 272 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 261 |
| 25 | Air France | 236 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 221 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33655 |
| 2 | 🇮🇳 IN | 3164 |
| 3 | 🇪🇸 ES | 3095 |
| 4 | 🇦🇺 AU | 2977 |
| 5 | 🇧🇷 BR | 2543 |
| 6 | 🇯🇵 JP | 2335 |
| 7 | 🇮🇹 IT | 2186 |
| 8 | 🇩🇪 DE | 2128 |
| 9 | 🇨🇦 CA | 2081 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1709 |
| 12 | 🇫🇷 FR | 1620 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1280 |
| 15 | 🇨🇭 CH | 1178 |
| 16 | 🇲🇾 MY | 1065 |
| 17 | 🇳🇴 NO | 1034 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 868 |
| 20 | 🇵🇭 PH | 769 |
| 21 | 🇹🇭 TH | 749 |
| 22 | 🇹🇷 TR | 738 |
| 23 | 🇰🇷 KR | 708 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 665 |
| 26 | 🇲🇦 MA | 522 |
| 27 | 🇳🇱 NL | 432 |
| 28 | 🇲🇪 ME | 429 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 386 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 797 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 683 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 634 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 507 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 421 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 399 |
| 16 | Frankfurt am Main International Airport |  | DE | 383 |
| 17 | Madrid Barajas International Airport |  | ES | 379 |
| 18 | Macau International Airport |  | MO | 378 |
| 19 | Bengaluru International Airport |  | IN | 374 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 368 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 357 |
| 24 | Malpensa International Airport |  | IT | 341 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 316 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 309 |
| 29 | Charles de Gaulle International Airport |  | FR | 306 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 297 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 33 | Reno/Tahoe International Airport |  | US | 293 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 283 |
| 35 | O. R. Tambo International Airport |  | ZA | 282 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 268 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Calgary International Airport |  | CA | 255 |
| 40 | Seattle-Tacoma International Airport |  | US | 253 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 200 | 1h 7m | 706 km | 2,435.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 155 | 24m | 225 km | 601.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 128 | 28m | 304 km | 671.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 123 | 1h 27m | 910 km | 1,930.2 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 116 | 21m | 244 km | 488.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 114 | 19m | 165 km | 324.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 92 | 54m | 546 km | 866.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 87 | 44m | 452 km | 678.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 29 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IOV | IOV | YSMB (YSMB) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-19 05:19 UTC | 2026-04-19 05:35 UTC | 15m |
| TKJ9CQ | TKJ | Kutahya Airport (LTBN) | Gazipasa Airport (LTFG) | 2026-04-19 04:54 UTC | 2026-04-19 05:28 UTC | 33m |
| DAL2851 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Denver International Airport (KDEN) | 2026-04-19 03:18 UTC | 2026-04-19 05:22 UTC | 2h 3m |
| N515WC |  | AL02 (AL02) | Northwest Alabama Regional Airport (KMSL) | 2026-04-19 04:57 UTC | 2026-04-19 05:21 UTC | 23m |
| N543TC |  | Meadows Field (KBFL) | Santa Monica Municipal Airport (KSMO) | 2026-04-19 04:33 UTC | 2026-04-19 05:13 UTC | 40m |
| N41VD |  | Miami-Opa Locka Executive Airport (KOPF) | Tampa International Airport (KTPA) | 2026-04-19 04:37 UTC | 2026-04-19 05:11 UTC | 33m |
| N870AE |  | Coles County Memorial Airport (KMTO) | Frasca Field (KC16) | 2026-04-19 04:38 UTC | 2026-04-19 04:59 UTC | 20m |
| RYR7273 | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Otocac Airport (LDRO) | 2026-04-19 03:50 UTC | 2026-04-19 04:47 UTC | 56m |
| AE962 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-04-19 04:23 UTC | 2026-04-19 04:44 UTC | 20m |
| ENY4166 | ENY | Dallas-Fort Worth International Airport (KDFW) | Mistwood Airport (24MO) | 2026-04-19 03:50 UTC | 2026-04-19 04:42 UTC | 51m |
| ANZ222L | ANZ | Auckland International Airport (NZAA) | Wellsford Airport (NZWJ) | 2026-04-19 04:22 UTC | 2026-04-19 04:41 UTC | 18m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-19 04:16 UTC | 2026-04-19 04:38 UTC | 21m |
| VAR403 | VAR | Phoenix Goodyear Airport (KGYR) | AZ00 (AZ00) | 2026-04-19 03:55 UTC | 2026-04-19 04:37 UTC | 42m |
| JST293 | JST | Auckland International Airport (NZAA) | Glenorchy Airport (NZGY) | 2026-04-19 03:10 UTC | 2026-04-19 04:34 UTC | 1h 24m |
| AIQ3374 | AIQ | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-04-19 03:56 UTC | 2026-04-19 04:30 UTC | 33m |
| SEH1DQ | SEH | Eleftherios Venizelos International Airport (LGAV) | Chania International Airport (LGSA) | 2026-04-19 04:03 UTC | 2026-04-19 04:28 UTC | 25m |
| JST650 | JST | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 2026-04-19 03:03 UTC | 2026-04-19 04:21 UTC | 1h 17m |
| AZU4340 | AZU | Viracopos International Airport (SBKP) | Fazenda Saltos do Poente Airport (SWDQ) | 2026-04-19 02:46 UTC | 2026-04-19 04:20 UTC | 1h 33m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-19 03:47 UTC | 2026-04-19 04:17 UTC | 30m |
| CEB911 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-19 03:52 UTC | 2026-04-19 04:17 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
