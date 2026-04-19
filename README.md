# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_08:43:30_UTC-green)

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

**Latest saved flight:** 2026-04-19 08:43:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 08:43:30 UTC

- **42,606** saved flights
- **17,859** unique routes
- **122** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,606** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **511,357.4 tonnes** estimated CO2 emissions
- **29,643,905 km** total distance flown
- **835 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1781 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1040 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 439 |
| 9 | Vueling | 426 |
| 10 | LATAM Airlines | 425 |
| 11 | Lufthansa | 420 |
| 12 | All Nippon Airways | 388 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 354 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 327 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 290 |
| 20 | AEE | 285 |
| 21 | EJU | 280 |
| 22 | easyJet | 272 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 266 |
| 25 | Air France | 237 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | GLO | 224 |
| 29 | AXB | 222 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33686 |
| 2 | 🇮🇳 IN | 3191 |
| 3 | 🇪🇸 ES | 3113 |
| 4 | 🇦🇺 AU | 3022 |
| 5 | 🇧🇷 BR | 2547 |
| 6 | 🇯🇵 JP | 2383 |
| 7 | 🇮🇹 IT | 2207 |
| 8 | 🇩🇪 DE | 2149 |
| 9 | 🇨🇦 CA | 2083 |
| 10 | 🇨🇴 CO | 1973 |
| 11 | 🇬🇧 GB | 1714 |
| 12 | 🇫🇷 FR | 1631 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1294 |
| 15 | 🇨🇭 CH | 1183 |
| 16 | 🇲🇾 MY | 1071 |
| 17 | 🇳🇴 NO | 1037 |
| 18 | 🇳🇿 NZ | 875 |
| 19 | 🇿🇦 ZA | 873 |
| 20 | 🇵🇭 PH | 785 |
| 21 | 🇹🇭 TH | 760 |
| 22 | 🇹🇷 TR | 747 |
| 23 | 🇰🇷 KR | 717 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 666 |
| 26 | 🇲🇦 MA | 526 |
| 27 | 🇳🇱 NL | 436 |
| 28 | 🇲🇪 ME | 436 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 392 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 813 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | El Dorado International Airport |  | CO | 691 |
| 5 | Indira Gandhi International Airport |  | IN | 690 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 642 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 512 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 390 |
| 17 | Macau International Airport |  | MO | 382 |
| 18 | Madrid Barajas International Airport |  | ES | 380 |
| 19 | Bengaluru International Airport |  | IN | 375 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 369 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 363 |
| 24 | Malpensa International Airport |  | IT | 348 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 318 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 314 |
| 29 | Charles de Gaulle International Airport |  | FR | 308 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 298 |
| 32 | Reno/Tahoe International Airport |  | US | 294 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 34 | O. R. Tambo International Airport |  | ZA | 283 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 283 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 271 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Don Mueang International Airport |  | TH | 257 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 202 | 1h 8m | 706 km | 2,459.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 159 | 24m | 225 km | 616.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 130 | 28m | 304 km | 681.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 127 | 1h 27m | 910 km | 1,992.9 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 117 | 21m | 244 km | 492.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 116 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 114 | 19m | 165 km | 324.3 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 94 | 54m | 546 km | 885.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 90 | 44m | 452 km | 701.4 t |
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
| CLX4806 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-18 21:57 UTC | 2026-04-19 08:43 UTC | 10h 45m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-19 01:19 UTC | 2026-04-19 08:30 UTC | 7h 11m |
| FJLEM | FJL | Saint-Cyr-l'Ecole Airport (LFPZ) | Chavenay Villepreux Airport (LFPX) | 2026-04-19 08:08 UTC | 2026-04-19 08:23 UTC | 15m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Tribhuvan International Airport (VNKT) | 2026-04-19 05:04 UTC | 2026-04-19 08:19 UTC | 3h 14m |
| NOZ806 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Stockholm-Arlanda Airport (ESSA) | 2026-04-19 07:33 UTC | 2026-04-19 08:19 UTC | 45m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-04-19 08:10 UTC | 2026-04-19 08:18 UTC | 8m |
| IFJ42B | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-04-19 07:40 UTC | 2026-04-19 08:17 UTC | 37m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-18 20:45 UTC | 2026-04-19 08:11 UTC | 11h 25m |
| TAM3547 | LATAM Airlines | Frutal Airport (SNFU) | Fronteira Airport (SSFR) | 2026-04-19 07:58 UTC | 2026-04-19 08:10 UTC | 12m |
| DLH9MT | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-19 07:36 UTC | 2026-04-19 08:10 UTC | 33m |
| RYR80PC | Ryanair | Napoli / Capodichino International Airport (LIRN) | Malpensa International Airport (LIMC) | 2026-04-19 06:54 UTC | 2026-04-19 08:08 UTC | 1h 14m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-19 06:38 UTC | 2026-04-19 08:07 UTC | 1h 29m |
| RYR6012 | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-04-19 08:07 UTC | 2026-04-19 08:07 UTC | 0m |
| ANZ625 | ANZ | Auckland International Airport (NZAA) | Glenorchy Airport (NZGY) | 2026-04-19 06:42 UTC | 2026-04-19 08:05 UTC | 1h 23m |
| THY4BQ | Turkish Airlines | Ataturk International Airport (LTBA) | Gazipasa Airport (LTFG) | 2026-04-19 07:15 UTC | 2026-04-19 08:02 UTC | 47m |
| AFR78RT | Air France | Charles de Gaulle International Airport (LFPG) | Lyon Saint-Exupery Airport (LFLL) | 2026-04-19 07:15 UTC | 2026-04-19 08:00 UTC | 45m |
| RSC80PF | RSC | Tenerife Norte Airport (GCXO) | La Gomera Airport (GCGM) | 2026-04-19 07:33 UTC | 2026-04-19 07:56 UTC | 22m |
| CEB915 | CEB | Diosdado Macapagal International Airport (RPLC) | Wasig Airport (RPVL) | 2026-04-19 07:28 UTC | 2026-04-19 07:55 UTC | 27m |
| SWR1XG | Swiss International | Munich International Airport (EDDM) | Zurich Airport (LSZH) | 2026-04-19 07:21 UTC | 2026-04-19 07:55 UTC | 33m |
| TLM220 | TLM | Don Mueang International Airport (VTBD) | VE89 (VE89) | 2026-04-19 05:08 UTC | 2026-04-19 07:55 UTC | 2h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
