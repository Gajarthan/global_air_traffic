# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_09:09:30_UTC-green)

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

**Latest saved flight:** 2026-04-19 09:09:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 09:09:30 UTC

- **42,676** saved flights
- **17,871** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,676** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **512,773.3 tonnes** estimated CO2 emissions
- **29,725,987 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1787 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1049 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 439 |
| 9 | Vueling | 427 |
| 10 | LATAM Airlines | 425 |
| 11 | Lufthansa | 420 |
| 12 | All Nippon Airways | 392 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 354 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 327 |
| 18 | WIF | 326 |
| 19 | Alaska Airlines | 290 |
| 20 | AEE | 287 |
| 21 | EJU | 281 |
| 22 | easyJet | 273 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 267 |
| 25 | Air France | 239 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | AXB | 225 |
| 29 | GLO | 224 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33688 |
| 2 | 🇮🇳 IN | 3218 |
| 3 | 🇪🇸 ES | 3118 |
| 4 | 🇦🇺 AU | 3024 |
| 5 | 🇧🇷 BR | 2547 |
| 6 | 🇯🇵 JP | 2397 |
| 7 | 🇮🇹 IT | 2213 |
| 8 | 🇩🇪 DE | 2153 |
| 9 | 🇨🇦 CA | 2083 |
| 10 | 🇨🇴 CO | 1973 |
| 11 | 🇬🇧 GB | 1720 |
| 12 | 🇫🇷 FR | 1635 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1302 |
| 15 | 🇨🇭 CH | 1184 |
| 16 | 🇲🇾 MY | 1071 |
| 17 | 🇳🇴 NO | 1041 |
| 18 | 🇿🇦 ZA | 879 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 787 |
| 21 | 🇹🇭 TH | 762 |
| 22 | 🇹🇷 TR | 749 |
| 23 | 🇰🇷 KR | 719 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 673 |
| 26 | 🇲🇦 MA | 528 |
| 27 | 🇲🇪 ME | 441 |
| 28 | 🇳🇱 NL | 436 |
| 29 | 🇧🇸 BS | 397 |
| 30 | 🇮🇩 ID | 392 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 818 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | Indira Gandhi International Airport |  | IN | 695 |
| 5 | El Dorado International Airport |  | CO | 691 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 647 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 512 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 12 | Kuala Lumpur International Airport |  | MY | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 391 |
| 17 | Macau International Airport |  | MO | 385 |
| 18 | Madrid Barajas International Airport |  | ES | 380 |
| 19 | Bengaluru International Airport |  | IN | 379 |
| 20 | Charlotte/Douglas International Airport |  | US | 371 |
| 21 | Tenerife Norte Airport |  | ES | 370 |
| 22 | Congonhas Airport |  | BR | 366 |
| 23 | Ninoy Aquino International Airport |  | PH | 364 |
| 24 | Malpensa International Airport |  | IT | 349 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Daniel K Inouye International Airport |  | US | 318 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 316 |
| 29 | Charles de Gaulle International Airport |  | FR | 310 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 298 |
| 32 | Reno/Tahoe International Airport |  | US | 294 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 286 |
| 35 | O. R. Tambo International Airport |  | ZA | 284 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 271 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Don Mueang International Airport |  | TH | 258 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 131 | 28m | 304 km | 686.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 127 | 1h 27m | 910 km | 1,992.9 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 117 | 21m | 244 km | 492.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 116 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 114 | 19m | 165 km | 324.3 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 94 | 54m | 546 km | 885.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
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
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-04-19 08:51 UTC | 2026-04-19 09:09 UTC | 18m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-18 21:40 UTC | 2026-04-19 09:04 UTC | 11h 24m |
| RYR6QZ | Ryanair | Perugia / San Egidio Airport (LIRZ) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-19 07:44 UTC | 2026-04-19 09:04 UTC | 1h 19m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-19 08:51 UTC | 2026-04-19 09:02 UTC | 11m |
| EJU95EH | EJU | Frankfurt am Main International Airport (EDDF) | Linate Airport (LIML) | 2026-04-19 08:05 UTC | 2026-04-19 09:00 UTC | 55m |
| WZZ1455 | Wizz Air | Stuttgart Airport (EDDS) | Trstenik Airport (LYTR) | 2026-04-19 07:30 UTC | 2026-04-19 08:59 UTC | 1h 29m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-18 21:55 UTC | 2026-04-19 08:59 UTC | 11h 3m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-19 07:19 UTC | 2026-04-19 08:54 UTC | 1h 35m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-04-19 08:23 UTC | 2026-04-19 08:51 UTC | 27m |
| EW585SL |  | Borovaya Airfield (UMMB) | Borovaya Airfield (UMMB) | 2026-04-19 08:48 UTC | 2026-04-19 08:50 UTC | 2m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-18 21:49 UTC | 2026-04-19 08:50 UTC | 11h 1m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-19 08:33 UTC | 2026-04-19 08:47 UTC | 13m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pithorgarh Airport (VIDF) | 2026-04-19 08:12 UTC | 2026-04-19 08:46 UTC | 34m |
| IGO6454 | IndiGo | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-04-19 08:21 UTC | 2026-04-19 08:44 UTC | 22m |
| SPPMT | SPP | Gdańsk Lech Wałęsa Airport (EPGD) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-04-19 08:43 UTC | 2026-04-19 08:44 UTC | 1m |
| CLX4806 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-18 21:57 UTC | 2026-04-19 08:43 UTC | 10h 45m |
| DIKSI | DIK | Braunschweig Wolfsburg Airport (EDVE) | Raron Airport (LSTA) | 2026-04-19 07:14 UTC | 2026-04-19 08:43 UTC | 1h 28m |
| RYR67JA | Ryanair | London Stansted Airport (EGSS) | Dolna Banya Airport (LBDB) | 2026-04-19 06:12 UTC | 2026-04-19 08:42 UTC | 2h 30m |
| DRK541 | DRK | Singapore Changi International Airport (WSSS) | Shillong Airport (VEBI) | 2026-04-19 04:44 UTC | 2026-04-19 08:41 UTC | 3h 56m |
| VLG6KW | Vueling | Malaga Airport (LEMG) | Bilbao Airport (LEBB) | 2026-04-19 07:39 UTC | 2026-04-19 08:40 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
