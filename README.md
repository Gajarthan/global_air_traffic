# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_07:46:50_UTC-green)

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

**Latest saved flight:** 2026-04-19 07:46:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 07:46:50 UTC

- **42,540** saved flights
- **17,847** unique routes
- **122** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,540** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **510,067.9 tonnes** estimated CO2 emissions
- **29,569,155 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1778 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1038 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 439 |
| 9 | Vueling | 426 |
| 10 | LATAM Airlines | 424 |
| 11 | Lufthansa | 416 |
| 12 | All Nippon Airways | 384 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 352 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 326 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 290 |
| 20 | AEE | 284 |
| 21 | EJU | 280 |
| 22 | easyJet | 272 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 264 |
| 25 | Air France | 236 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 221 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33678 |
| 2 | 🇮🇳 IN | 3182 |
| 3 | 🇪🇸 ES | 3110 |
| 4 | 🇦🇺 AU | 3015 |
| 5 | 🇧🇷 BR | 2545 |
| 6 | 🇯🇵 JP | 2365 |
| 7 | 🇮🇹 IT | 2201 |
| 8 | 🇩🇪 DE | 2139 |
| 9 | 🇨🇦 CA | 2083 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1711 |
| 12 | 🇫🇷 FR | 1622 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1290 |
| 15 | 🇨🇭 CH | 1182 |
| 16 | 🇲🇾 MY | 1071 |
| 17 | 🇳🇴 NO | 1036 |
| 18 | 🇿🇦 ZA | 873 |
| 19 | 🇳🇿 NZ | 872 |
| 20 | 🇵🇭 PH | 783 |
| 21 | 🇹🇭 TH | 755 |
| 22 | 🇹🇷 TR | 743 |
| 23 | 🇰🇷 KR | 713 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 665 |
| 26 | 🇲🇦 MA | 526 |
| 27 | 🇳🇱 NL | 436 |
| 28 | 🇲🇪 ME | 434 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 388 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 806 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 687 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 638 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 511 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 406 |
| 16 | Frankfurt am Main International Airport |  | DE | 386 |
| 17 | Madrid Barajas International Airport |  | ES | 380 |
| 18 | Macau International Airport |  | MO | 379 |
| 19 | Bengaluru International Airport |  | IN | 375 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 368 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 363 |
| 24 | Malpensa International Airport |  | IT | 345 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 318 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 313 |
| 29 | Charles de Gaulle International Airport |  | FR | 306 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 298 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 33 | Reno/Tahoe International Airport |  | US | 293 |
| 34 | O. R. Tambo International Airport |  | ZA | 283 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 283 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 271 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Calgary International Airport |  | CA | 256 |
| 40 | Seattle-Tacoma International Airport |  | US | 253 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 200 | 1h 7m | 706 km | 2,435.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 159 | 24m | 225 km | 616.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 129 | 28m | 304 km | 676.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 126 | 1h 27m | 910 km | 1,977.2 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 117 | 21m | 244 km | 492.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 116 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 114 | 19m | 165 km | 324.3 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 93 | 54m | 546 km | 875.6 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 88 | 44m | 452 km | 685.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 76 | 31m | 369 km | 483.8 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 59 | 57m | 493 km | 502.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 30 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-18 20:55 UTC | 2026-04-19 07:46 UTC | 10h 51m |
| SFJ25 | SFJ | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-19 07:00 UTC | 2026-04-19 07:40 UTC | 39m |
| POK | POK | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-04-19 07:09 UTC | 2026-04-19 07:22 UTC | 12m |
| N2DF |  | Palm Beach International Airport (KPBI) | Van Nuys Airport (KVNY) | 2026-04-19 02:12 UTC | 2026-04-19 07:21 UTC | 5h 8m |
| 4XHSC |  | LL59 (LL59) | Tel Nov Air Base (LLEK) | 2026-04-19 07:11 UTC | 2026-04-19 07:16 UTC | 5m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-04-19 07:08 UTC | 2026-04-19 07:16 UTC | 8m |
| ABP973 | ABP | Chania International Airport (LGSA) | Kalamata Airport (LGKL) | 2026-04-19 06:35 UTC | 2026-04-19 07:12 UTC | 37m |
| AWQ172 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-04-19 06:52 UTC | 2026-04-19 07:08 UTC | 15m |
| PGT5XE | PGT | Gaziemir Airport (LTBK) | Stuttgart Airport (EDDS) | 2026-04-19 04:27 UTC | 2026-04-19 07:06 UTC | 2h 39m |
| RYR3603 | Ryanair | Treviso / Sant'Angelo Airport (LIPH) | Bilbao Airport (LEBB) | 2026-04-19 05:12 UTC | 2026-04-19 07:04 UTC | 1h 51m |
| CPI191 | CPI | Ciampino Airport (LIRA) | Alghero / Fertilia Airport (LIEA) | 2026-04-19 06:27 UTC | 2026-04-19 07:04 UTC | 36m |
| TCMKA | TCM | Ataturk International Airport (LTBA) | Uzundzhovo Air Base (LBHS) | 2026-04-19 06:28 UTC | 2026-04-19 07:02 UTC | 34m |
| RYR170F | Ryanair | Napoli / Capodichino International Airport (LIRN) | Stanke Dimitrov Highway Strip (LB37) | 2026-04-19 05:59 UTC | 2026-04-19 06:58 UTC | 59m |
| IGO127 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-19 06:19 UTC | 2026-04-19 06:58 UTC | 39m |
| EW585SL |  | Borovaya Airfield (UMMB) | Borovaya Airfield (UMMB) | 2026-04-19 06:57 UTC | 2026-04-19 06:58 UTC | 0m |
| AIQ510 | AIQ | Don Mueang International Airport (VTBD) | Kluang Airport (WMAP) | 2026-04-19 05:14 UTC | 2026-04-19 06:56 UTC | 1h 41m |
| SHA734 | SHA | Langtang Airport (VNLT) | Langtang Airport (VNLT) | 2026-04-19 06:38 UTC | 2026-04-19 06:56 UTC | 17m |
| AUA251 | Austrian Airlines | Vienna International Airport (LOWW) | Hamburg Airport (EDDH) | 2026-04-19 05:43 UTC | 2026-04-19 06:55 UTC | 1h 11m |
| ALFT | ALF | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-04-19 06:48 UTC | 2026-04-19 06:52 UTC | 3m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Xieng Khouang Airport (VLXK) | 2026-04-19 06:03 UTC | 2026-04-19 06:48 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
