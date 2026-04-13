# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_14:11:42_UTC-green)

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

**Latest saved flight:** 2026-04-13 14:11:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 14:11:42 UTC

- **32,213** saved flights
- **14,508** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,213** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **396,860.9 tonnes** estimated CO2 emissions
- **23,006,429 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1367 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 831 |
| 4 | EJA | 558 |
| 5 | American Airlines | 555 |
| 6 | Southwest Airlines | 466 |
| 7 | ENY | 431 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 344 |
| 10 | Vueling | 328 |
| 11 | LATAM Airlines | 326 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 287 |
| 14 | Delta Air Lines | 266 |
| 15 | QLK | 266 |
| 16 | LXJ | 255 |
| 17 | Swiss International | 243 |
| 18 | WIF | 217 |
| 19 | Alaska Airlines | 215 |
| 20 | EJU | 215 |
| 21 | easyJet | 213 |
| 22 | VIV | 208 |
| 23 | AEE | 206 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | Air France | 174 |
| 28 | GLO | 174 |
| 29 | Avianca | 171 |
| 30 | JetBlue | 171 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25178 |
| 2 | 🇮🇳 IN | 2540 |
| 3 | 🇪🇸 ES | 2424 |
| 4 | 🇦🇺 AU | 2252 |
| 5 | 🇧🇷 BR | 1902 |
| 6 | 🇯🇵 JP | 1777 |
| 7 | 🇮🇹 IT | 1712 |
| 8 | 🇩🇪 DE | 1637 |
| 9 | 🇨🇴 CO | 1608 |
| 10 | 🇨🇦 CA | 1556 |
| 11 | 🇬🇧 GB | 1324 |
| 12 | 🇫🇷 FR | 1197 |
| 13 | 🇲🇽 MX | 1025 |
| 14 | 🇬🇷 GR | 937 |
| 15 | 🇨🇭 CH | 903 |
| 16 | 🇲🇾 MY | 834 |
| 17 | 🇳🇴 NO | 727 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 669 |
| 20 | 🇵🇭 PH | 610 |
| 21 | 🇹🇭 TH | 595 |
| 22 | 🇹🇷 TR | 594 |
| 23 | 🇬🇹 GT | 591 |
| 24 | 🇰🇷 KR | 558 |
| 25 | 🇵🇱 PL | 494 |
| 26 | 🇲🇦 MA | 417 |
| 27 | 🇧🇸 BS | 334 |
| 28 | 🇲🇪 ME | 320 |
| 29 | 🇮🇩 ID | 309 |
| 30 | 🇳🇱 NL | 308 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 767 |
| 2 | Tokyo International Airport |  | JP | 603 |
| 3 | El Dorado International Airport |  | CO | 571 |
| 4 | Indira Gandhi International Airport |  | IN | 540 |
| 5 | Denver International Airport |  | US | 539 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 459 |
| 7 | La Aurora Airport |  | GT | 428 |
| 8 | Harry Reid International Airport |  | US | 420 |
| 9 | Zurich Airport |  | CH | 400 |
| 10 | Guaymaral Airport |  | CO | 391 |
| 11 | Chicago O'Hare International Airport |  | US | 331 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 322 |
| 15 | Kuala Lumpur International Airport |  | MY | 320 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 305 |
| 18 | Madrid Barajas International Airport |  | ES | 291 |
| 19 | Bengaluru International Airport |  | IN | 291 |
| 20 | Charlotte/Douglas International Airport |  | US | 290 |
| 21 | Tenerife Norte Airport |  | ES | 287 |
| 22 | Ninoy Aquino International Airport |  | PH | 282 |
| 23 | Congonhas Airport |  | BR | 279 |
| 24 | Malpensa International Airport |  | IT | 261 |
| 25 | Daniel K Inouye International Airport |  | US | 247 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 245 |
| 27 | Salt Lake City International Airport |  | US | 245 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 236 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 231 |
| 31 | Capua Airport |  | IT | 223 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 223 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 222 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 219 |
| 35 | O. R. Tambo International Airport |  | ZA | 218 |
| 36 | Vitoria/Foronda Airport |  | ES | 213 |
| 37 | Miami International Airport |  | US | 210 |
| 38 | Barcelona International Airport |  | ES | 207 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Don Mueang International Airport |  | TH | 201 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 152 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 77 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 69 | 27m | 275 km | 327.0 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 68 | 21m | 244 km | 286.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 56 | 20m | 250 km | 241.9 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 48 | 16m | 162 km | 134.6 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 45 | 12m | 15 km | 11.9 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 45 | 1h 21m | 961 km | 745.9 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RNGR822 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | San Jose Island Airport (XS67) | 2026-04-13 13:52 UTC | 2026-04-13 14:11 UTC | 19m |
| UAE4DU | Emirates | Dubai International Airport (OMDB) | Heidelburg Airport (FAHG) | 2026-04-13 06:32 UTC | 2026-04-13 14:11 UTC | 7h 38m |
| N497CA |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-04-13 13:05 UTC | 2026-04-13 14:07 UTC | 1h 2m |
| BRW149 | BRW | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-04-13 13:21 UTC | 2026-04-13 14:05 UTC | 44m |
| N744EF |  | Skywagon Ranch Airport (6CO6) | Rocky Mountain Metro Airport (KBJC) | 2026-04-13 13:40 UTC | 2026-04-13 13:55 UTC | 14m |
| NSZ3516 | NSZ | Copenhagen Kastrup Airport (EKCH) | London Gatwick Airport (EGKK) | 2026-04-13 12:20 UTC | 2026-04-13 13:53 UTC | 1h 33m |
| N1330N |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-13 13:28 UTC | 2026-04-13 13:52 UTC | 23m |
| N664FL |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-04-13 13:28 UTC | 2026-04-13 13:50 UTC | 22m |
| FFT1815 | FFT | Austin-Bergstrom International Airport (KAUS) | Denver International Airport (KDEN) | 2026-04-13 11:58 UTC | 2026-04-13 13:46 UTC | 1h 48m |
| N88CS |  | Linwood Airport (MS06) | Nashville International Airport (KBNA) | 2026-04-13 12:52 UTC | 2026-04-13 13:46 UTC | 53m |
| SWR4VZ | Swiss International | Bordeaux-Merignac (BA 106) Airport (LFBD) | Zurich Airport (LSZH) | 2026-04-13 12:18 UTC | 2026-04-13 13:42 UTC | 1h 23m |
| N868E |  | Pompano Beach Airpark (KPMP) | Duda Airstrip (FA69) | 2026-04-13 13:23 UTC | 2026-04-13 13:40 UTC | 16m |
| N838SP |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-13 13:16 UTC | 2026-04-13 13:38 UTC | 21m |
| VIV9452 | VIV | Santa Lucia Air Force Base (MMSM) | Quetzalcoatl International Airport (MMNL) | 2026-04-13 12:22 UTC | 2026-04-13 13:36 UTC | 1h 14m |
| DEADLY8 | DEA | Randolph Afb Airport (KRND) | T-Ranch Airport (XS86) | 2026-04-13 13:26 UTC | 2026-04-13 13:36 UTC | 10m |
| N301LG |  | Wiley Post Airport (KPWA) | Snell - North Laramie River Airport (WY25) | 2026-04-13 12:05 UTC | 2026-04-13 13:36 UTC | 1h 30m |
| TEK63 | TEK | Raleigh-Durham International Airport (KRDU) | Jim Kelly Field (KLXN) | 2026-04-13 10:51 UTC | 2026-04-13 13:34 UTC | 2h 42m |
| SAA063 | SAA | Reitz Airport (FARZ) | Heidelburg Airport (FAHG) | 2026-04-13 12:59 UTC | 2026-04-13 13:33 UTC | 33m |
| FGTYH | FGT | Grenoble-Isere Airport (LFLS) | Lyon-Bron Airport (LFLY) | 2026-04-13 13:10 UTC | 2026-04-13 13:31 UTC | 21m |
| CXK164 | CXK | Ogden-Hinckley Airport (KOGD) | UT99 (UT99) | 2026-04-13 12:36 UTC | 2026-04-13 13:31 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
