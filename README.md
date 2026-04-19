# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_21:17:11_UTC-green)

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

**Latest saved flight:** 2026-04-19 21:17:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 21:17:11 UTC

- **44,091** saved flights
- **18,345** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,091** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **530,081.1 tonnes** estimated CO2 emissions
- **30,729,336 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1867 |
| 2 | SkyWest Airlines | 1713 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 764 |
| 5 | American Airlines | 730 |
| 6 | Southwest Airlines | 626 |
| 7 | ENY | 573 |
| 8 | AXM | 446 |
| 9 | Vueling | 442 |
| 10 | Lufthansa | 438 |
| 11 | LATAM Airlines | 436 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 385 |
| 14 | Delta Air Lines | 377 |
| 15 | QLK | 354 |
| 16 | LXJ | 351 |
| 17 | WIF | 344 |
| 18 | Swiss International | 339 |
| 19 | AEE | 301 |
| 20 | Alaska Airlines | 297 |
| 21 | EJU | 291 |
| 22 | easyJet | 282 |
| 23 | VIV | 279 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | United Airlines | 237 |
| 27 | JetBlue | 234 |
| 28 | AXB | 232 |
| 29 | GLO | 230 |
| 30 | EDV | 225 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34915 |
| 2 | 🇮🇳 IN | 3299 |
| 3 | 🇪🇸 ES | 3252 |
| 4 | 🇦🇺 AU | 3034 |
| 5 | 🇧🇷 BR | 2626 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2338 |
| 8 | 🇩🇪 DE | 2238 |
| 9 | 🇨🇦 CA | 2145 |
| 10 | 🇨🇴 CO | 2037 |
| 11 | 🇬🇧 GB | 1788 |
| 12 | 🇫🇷 FR | 1683 |
| 13 | 🇲🇽 MX | 1371 |
| 14 | 🇬🇷 GR | 1360 |
| 15 | 🇨🇭 CH | 1204 |
| 16 | 🇳🇴 NO | 1095 |
| 17 | 🇲🇾 MY | 1090 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 877 |
| 20 | 🇵🇭 PH | 792 |
| 21 | 🇹🇷 TR | 781 |
| 22 | 🇹🇭 TH | 780 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 726 |
| 25 | 🇵🇱 PL | 702 |
| 26 | 🇲🇦 MA | 548 |
| 27 | 🇲🇪 ME | 465 |
| 28 | 🇳🇱 NL | 451 |
| 29 | 🇧🇸 BS | 409 |
| 30 | 🇲🇴 MO | 402 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1034 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 732 |
| 4 | El Dorado International Airport |  | CO | 711 |
| 5 | Indira Gandhi International Airport |  | IN | 710 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 676 |
| 7 | Harry Reid International Airport |  | US | 564 |
| 8 | Guaymaral Airport |  | CO | 557 |
| 9 | La Aurora Airport |  | GT | 536 |
| 10 | Zurich Airport |  | CH | 528 |
| 11 | Chicago O'Hare International Airport |  | US | 436 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 435 |
| 13 | Kuala Lumpur International Airport |  | MY | 432 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 429 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 402 |
| 18 | Madrid Barajas International Airport |  | ES | 392 |
| 19 | Bengaluru International Airport |  | IN | 392 |
| 20 | Tenerife Norte Airport |  | ES | 389 |
| 21 | Charlotte/Douglas International Airport |  | US | 384 |
| 22 | Congonhas Airport |  | BR | 375 |
| 23 | Malpensa International Airport |  | IT | 367 |
| 24 | Ninoy Aquino International Airport |  | PH | 367 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 333 |
| 26 | Salt Lake City International Airport |  | US | 333 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Daniel K Inouye International Airport |  | US | 325 |
| 29 | Charles de Gaulle International Airport |  | FR | 324 |
| 30 | Reno/Tahoe International Airport |  | US | 307 |
| 31 | Vitoria/Foronda Airport |  | ES | 307 |
| 32 | Capua Airport |  | IT | 305 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 304 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 299 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 285 |
| 38 | Viracopos International Airport |  | BR | 267 |
| 39 | Calgary International Airport |  | CA | 265 |
| 40 | Don Mueang International Airport |  | TH | 265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 224 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 122 | 21m | 244 km | 513.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 109 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 91 | 20m | 99 km | 155.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 52m | 1,304 km | 1,372.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RFS731 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-04-19 21:01 UTC | 2026-04-19 21:17 UTC | 15m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-04-19 17:55 UTC | 2026-04-19 21:16 UTC | 3h 21m |
| CODY02 | COD | Mc Guire Field (Joint Base Mc Guire Dix Lakehurst) Airport (KWRI) | Westover Arb/Metro Airport (KCEF) | 2026-04-19 20:21 UTC | 2026-04-19 21:08 UTC | 47m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-19 20:49 UTC | 2026-04-19 20:59 UTC | 10m |
| CTP338 | CTP | Santa Barbara Municipal Airport (KSBA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-19 20:21 UTC | 2026-04-19 20:57 UTC | 36m |
| XSR724 | XSR | Harry Reid International Airport (KLAS) | Colonel James Jabara Airport (KAAO) | 2026-04-19 18:59 UTC | 2026-04-19 20:55 UTC | 1h 55m |
| N220EA |  | Noahs Ark Airport (06MO) | Noahs Ark Airport (06MO) | 2026-04-19 20:02 UTC | 2026-04-19 20:53 UTC | 51m |
| N866P |  | Grassy Meadows/Sky Ranch Landowners Assn Airport (UT47) | Caas Airport (NV98) | 2026-04-19 20:12 UTC | 2026-04-19 20:52 UTC | 40m |
| N501AT |  | Lovell Field (KCHA) | Savannah-Hardin County Airport (KSNH) | 2026-04-19 20:17 UTC | 2026-04-19 20:51 UTC | 34m |
| N4819N |  | University Airport (KEDU) | Ells Field/Willits Municipal Airport (KO28) | 2026-04-19 19:59 UTC | 2026-04-19 20:47 UTC | 47m |
| N723BG |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-19 20:30 UTC | 2026-04-19 20:47 UTC | 16m |
| LXJ476 | LXJ | Dallas Love Field (KDAL) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-19 19:00 UTC | 2026-04-19 20:46 UTC | 1h 45m |
| N40PC |  | Kleberg County Airport (KIKG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-19 18:53 UTC | 2026-04-19 20:43 UTC | 1h 49m |
| N529PM |  | Aiken Regional Airport (KAIK) | Virgil I Grissom Municipal Airport (KBFR) | 2026-04-19 18:35 UTC | 2026-04-19 20:41 UTC | 2h 5m |
| N525BD |  | Baton Rouge Metro, Ryan Field (KBTR) | Marksville Municipal Airport (KMKV) | 2026-04-19 20:26 UTC | 2026-04-19 20:40 UTC | 14m |
| N801JA |  | Mesquite Airport (K67L) | Mesquite Airport (K67L) | 2026-04-19 20:28 UTC | 2026-04-19 20:39 UTC | 10m |
| EJA260 | EJA | Palm Springs International Airport (KPSP) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-19 19:43 UTC | 2026-04-19 20:39 UTC | 55m |
| VLG8XR | Vueling | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-04-19 19:25 UTC | 2026-04-19 20:37 UTC | 1h 11m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-19 20:23 UTC | 2026-04-19 20:37 UTC | 13m |
| N725TW |  | Fort Lauderdale Executive Airport (KFXE) | Georgetown County Airport (KGGE) | 2026-04-19 19:21 UTC | 2026-04-19 20:35 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
