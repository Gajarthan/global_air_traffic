# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_12:34:20_UTC-green)

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

**Latest saved flight:** 2026-04-20 12:34:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 12:34:20 UTC

- **44,981** saved flights
- **18,594** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,981** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **543,969.2 tonnes** estimated CO2 emissions
- **31,534,446 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1907 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1080 |
| 4 | EJA | 780 |
| 5 | American Airlines | 741 |
| 6 | Southwest Airlines | 643 |
| 7 | ENY | 584 |
| 8 | Lufthansa | 459 |
| 9 | AXM | 455 |
| 10 | Vueling | 452 |
| 11 | LATAM Airlines | 449 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 389 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 366 |
| 16 | LXJ | 354 |
| 17 | WIF | 351 |
| 18 | Swiss International | 349 |
| 19 | AEE | 308 |
| 20 | Alaska Airlines | 308 |
| 21 | EJU | 298 |
| 22 | easyJet | 290 |
| 23 | VIV | 285 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 257 |
| 26 | AXB | 238 |
| 27 | United Airlines | 238 |
| 28 | JetBlue | 237 |
| 29 | Cathay Pacific | 234 |
| 30 | GLO | 234 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35469 |
| 2 | 🇮🇳 IN | 3356 |
| 3 | 🇪🇸 ES | 3311 |
| 4 | 🇦🇺 AU | 3130 |
| 5 | 🇧🇷 BR | 2670 |
| 6 | 🇯🇵 JP | 2486 |
| 7 | 🇮🇹 IT | 2412 |
| 8 | 🇩🇪 DE | 2308 |
| 9 | 🇨🇦 CA | 2178 |
| 10 | 🇨🇴 CO | 2071 |
| 11 | 🇬🇧 GB | 1834 |
| 12 | 🇫🇷 FR | 1712 |
| 13 | 🇲🇽 MX | 1399 |
| 14 | 🇬🇷 GR | 1392 |
| 15 | 🇨🇭 CH | 1234 |
| 16 | 🇳🇴 NO | 1119 |
| 17 | 🇲🇾 MY | 1118 |
| 18 | 🇿🇦 ZA | 950 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 816 |
| 21 | 🇵🇭 PH | 809 |
| 22 | 🇹🇷 TR | 796 |
| 23 | 🇰🇷 KR | 746 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 718 |
| 26 | 🇲🇦 MA | 559 |
| 27 | 🇲🇪 ME | 478 |
| 28 | 🇳🇱 NL | 458 |
| 29 | 🇲🇴 MO | 422 |
| 30 | 🇧🇸 BS | 412 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1051 |
| 2 | Tokyo International Airport |  | JP | 848 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | El Dorado International Airport |  | CO | 725 |
| 5 | Indira Gandhi International Airport |  | IN | 725 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 690 |
| 7 | Harry Reid International Airport |  | US | 582 |
| 8 | Guaymaral Airport |  | CO | 562 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 540 |
| 11 | Kuala Lumpur International Airport |  | MY | 446 |
| 12 | Chicago O'Hare International Airport |  | US | 443 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Frankfurt am Main International Airport |  | DE | 429 |
| 16 | Macau International Airport |  | MO | 422 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 420 |
| 18 | Madrid Barajas International Airport |  | ES | 403 |
| 19 | Bengaluru International Airport |  | IN | 399 |
| 20 | Tenerife Norte Airport |  | ES | 392 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Congonhas Airport |  | BR | 383 |
| 23 | Malpensa International Airport |  | IT | 382 |
| 24 | Ninoy Aquino International Airport |  | PH | 375 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 336 |
| 28 | Daniel K Inouye International Airport |  | US | 334 |
| 29 | Charles de Gaulle International Airport |  | FR | 333 |
| 30 | Capua Airport |  | IT | 318 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 312 |
| 32 | Reno/Tahoe International Airport |  | US | 311 |
| 33 | Vitoria/Foronda Airport |  | ES | 311 |
| 34 | O. R. Tambo International Airport |  | ZA | 304 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 304 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 303 |
| 37 | Barcelona International Airport |  | ES | 291 |
| 38 | Don Mueang International Airport |  | TH | 275 |
| 39 | Calgary International Airport |  | CA | 273 |
| 40 | Viracopos International Airport |  | BR | 270 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 226 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 168 | 14m | 114 km | 329.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 128 | 21m | 244 km | 539.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 122 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 122 | 19m | 165 km | 347.0 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 104 | 26m | 275 km | 492.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 80 | 31m | 369 km | 509.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 75 | 20m | 250 km | 324.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 69 | 26m | 215 km | 255.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 66 | 13m | 99 km | 113.2 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1305B |  | Raleigh-Durham International Airport (KRDU) | Henderson/Oxford Airport (KHNZ) | 2026-04-20 11:26 UTC | 2026-04-20 12:34 UTC | 1h 7m |
| N4946L |  | Andrews University Airpark (KC20) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-04-20 12:04 UTC | 2026-04-20 12:33 UTC | 29m |
| RESCU25 | RES | Ovar Airport (LPOV) | Monte Real Airport (LPMR) | 2026-04-20 11:55 UTC | 2026-04-20 12:33 UTC | 38m |
| LLN206 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | Bowie Municipal Airport (K0F2) | 2026-04-20 12:09 UTC | 2026-04-20 12:31 UTC | 21m |
| HB3442 |  | Lodrino Air Base (LSML) | Ambri Airport (LSPM) | 2026-04-20 11:07 UTC | 2026-04-20 12:27 UTC | 1h 20m |
| VLW03 | VLW | Linate Airport (LIML) | Tekirdag Corlu Airport (LTBU) | 2026-04-20 10:40 UTC | 2026-04-20 12:23 UTC | 1h 43m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-04-19 21:51 UTC | 2026-04-20 12:22 UTC | 14h 30m |
| HBZVQ | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-04-20 11:07 UTC | 2026-04-20 12:20 UTC | 1h 12m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-20 11:29 UTC | 2026-04-20 12:18 UTC | 48m |
| CXK141 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-20 11:53 UTC | 2026-04-20 12:17 UTC | 23m |
| DAKAY | DAK | Cologne Bonn Airport (EDDK) | Stuttgart Airport (EDDS) | 2026-04-20 11:40 UTC | 2026-04-20 12:15 UTC | 35m |
| JTL611 | JTL | New Castle Airport (KILG) | Lancaster Airport (KLNS) | 2026-04-20 12:01 UTC | 2026-04-20 12:15 UTC | 13m |
| N700RH |  | General Mitchell International Airport (KMKE) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-20 11:30 UTC | 2026-04-20 12:14 UTC | 44m |
| 5YSXA |  | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-04-20 12:09 UTC | 2026-04-20 12:13 UTC | 4m |
| GDPAE | GDP | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-04-20 11:49 UTC | 2026-04-20 12:02 UTC | 12m |
| ICL773 | ICL | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-04-19 22:38 UTC | 2026-04-20 12:02 UTC | 13h 24m |
| RYR62AD | Ryanair | Copernicus Wrocław Airport (EPWR) | East Midlands Airport (EGNX) | 2026-04-20 10:05 UTC | 2026-04-20 12:01 UTC | 1h 55m |
| CPA331 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-20 04:11 UTC | 2026-04-20 11:59 UTC | 7h 47m |
| OAL092 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiathos Island National Airport (LGSK) | 2026-04-20 11:34 UTC | 2026-04-20 11:57 UTC | 23m |
| N483LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-20 10:51 UTC | 2026-04-20 11:56 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
