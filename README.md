# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_05:33:47_UTC-green)

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

**Latest saved flight:** 2026-04-14 05:33:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 05:33:47 UTC

- **33,465** saved flights
- **14,929** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,465** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **411,851.3 tonnes** estimated CO2 emissions
- **23,875,437 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1414 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 842 |
| 4 | American Airlines | 583 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 351 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 335 |
| 12 | All Nippon Airways | 303 |
| 13 | AZU | 297 |
| 14 | Delta Air Lines | 285 |
| 15 | QLK | 280 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 252 |
| 18 | Alaska Airlines | 227 |
| 19 | WIF | 226 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | VIV | 218 |
| 23 | AEE | 217 |
| 24 | Japan Airlines | 211 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 183 |
| 28 | Avianca | 181 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26419 |
| 2 | 🇮🇳 IN | 2579 |
| 3 | 🇪🇸 ES | 2498 |
| 4 | 🇦🇺 AU | 2339 |
| 5 | 🇧🇷 BR | 1969 |
| 6 | 🇯🇵 JP | 1825 |
| 7 | 🇮🇹 IT | 1772 |
| 8 | 🇨🇴 CO | 1675 |
| 9 | 🇩🇪 DE | 1667 |
| 10 | 🇨🇦 CA | 1642 |
| 11 | 🇬🇧 GB | 1360 |
| 12 | 🇫🇷 FR | 1223 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 971 |
| 15 | 🇨🇭 CH | 922 |
| 16 | 🇲🇾 MY | 847 |
| 17 | 🇳🇴 NO | 748 |
| 18 | 🇳🇿 NZ | 718 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇵🇭 PH | 638 |
| 21 | 🇹🇷 TR | 620 |
| 22 | 🇹🇭 TH | 605 |
| 23 | 🇬🇹 GT | 600 |
| 24 | 🇰🇷 KR | 571 |
| 25 | 🇵🇱 PL | 519 |
| 26 | 🇲🇦 MA | 425 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 330 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇮🇩 ID | 321 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 802 |
| 2 | Tokyo International Airport |  | JP | 619 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 547 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 474 |
| 7 | Harry Reid International Airport |  | US | 441 |
| 8 | La Aurora Airport |  | GT | 437 |
| 9 | Zurich Airport |  | CH | 413 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Frankfurt am Main International Airport |  | DE | 326 |
| 15 | Kuala Lumpur International Airport |  | MY | 325 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 320 |
| 17 | Macau International Airport |  | MO | 317 |
| 18 | Charlotte/Douglas International Airport |  | US | 305 |
| 19 | Madrid Barajas International Airport |  | ES | 303 |
| 20 | Bengaluru International Airport |  | IN | 300 |
| 21 | Ninoy Aquino International Airport |  | PH | 295 |
| 22 | Tenerife Norte Airport |  | ES | 294 |
| 23 | Congonhas Airport |  | BR | 292 |
| 24 | Malpensa International Airport |  | IT | 272 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 26 | Daniel K Inouye International Airport |  | US | 257 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 241 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 236 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 228 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 223 |
| 37 | Miami International Airport |  | US | 214 |
| 38 | Barcelona International Airport |  | ES | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 211 |
| 40 | Viracopos International Airport |  | BR | 206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 156 | 1h 8m | 706 km | 1,899.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 124 | 24m | 225 km | 481.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 108 | 28m | 304 km | 566.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 95 | 1h 27m | 910 km | 1,490.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 86 | 19m | 165 km | 244.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 81 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 76 | 54m | 546 km | 715.5 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 75 | 21m | 244 km | 315.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 69 | 1h 12m | 770 km | 916.6 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 62 | 45m | 452 km | 483.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 53 | 20m | 147 km | 134.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 46 | 59m | 695 km | 551.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BBC371 | BBC | VGZR (VGZR) | Langtang Airport (VNLT) | 2026-04-14 04:22 UTC | 2026-04-14 05:33 UTC | 1h 11m |
| N5241F |  | Yokota Air Base (RJTY) | Yokota Air Base (RJTY) | 2026-04-14 04:58 UTC | 2026-04-14 05:32 UTC | 33m |
| BDG | BDG | Gympie Airport (YGYM) | Sunshine Coast Airport (YBMC) | 2026-04-14 05:11 UTC | 2026-04-14 05:26 UTC | 15m |
| N904LR |  | Tacoma Narrows Airport (KTIW) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-14 03:48 UTC | 2026-04-14 05:26 UTC | 1h 37m |
| J936G |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-04-14 05:11 UTC | 2026-04-14 05:21 UTC | 10m |
| XBM | XBM | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-14 05:04 UTC | 2026-04-14 05:21 UTC | 16m |
| AFL233 | AFL | Indira Gandhi International Airport (VIDP) | Sheremetyevo International Airport (UUEE) | 2026-04-14 00:11 UTC | 2026-04-14 05:18 UTC | 5h 6m |
| N223LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-14 03:49 UTC | 2026-04-14 04:59 UTC | 1h 9m |
| J054KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-04-14 04:34 UTC | 2026-04-14 04:51 UTC | 16m |
| JA303G |  | Takamatsu Airport (RJOT) | Okayama Airport (RJOB) | 2026-04-14 04:45 UTC | 2026-04-14 04:51 UTC | 5m |
| ZHT | ZHT | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-14 04:27 UTC | 2026-04-14 04:50 UTC | 23m |
| TACO21 | TAC | Albuquerque International Sunport Airport (KABQ) | KE80 (KE80) | 2026-04-14 03:18 UTC | 2026-04-14 04:47 UTC | 1h 29m |
| DU203 |  | Al Maktoum International Airport (OMDW) | Fujairah International Airport (OMFJ) | 2026-04-14 04:11 UTC | 2026-04-14 04:44 UTC | 33m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-14 04:04 UTC | 2026-04-14 04:42 UTC | 38m |
| SITKA22 | SIT | Merle K (Mudhole) Smith Airport (PACV) | Elmendorf Afb Airport (PAED) | 2026-04-14 03:03 UTC | 2026-04-14 04:41 UTC | 1h 37m |
| JST293 | JST | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-04-14 03:26 UTC | 2026-04-14 04:36 UTC | 1h 10m |
| STA621D | STA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-14 04:30 UTC | 2026-04-14 04:33 UTC | 3m |
| WIF5MB | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-14 04:17 UTC | 2026-04-14 04:30 UTC | 12m |
| SHADE41 | SHA | RAAF Base Edinburgh (YPED) | Quondong Airport (YQON) | 2026-04-14 03:51 UTC | 2026-04-14 04:24 UTC | 32m |
|  |  | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-14 04:15 UTC | 2026-04-14 04:19 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
