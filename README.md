# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_08:52:11_UTC-green)

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

**Latest saved flight:** 2026-04-12 08:52:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 08:52:11 UTC

- **30,105** saved flights
- **13,813** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,105** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **368,175.3 tonnes** estimated CO2 emissions
- **21,343,493 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1234 |
| 2 | SkyWest Airlines | 1230 |
| 3 | IndiGo | 782 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 363 |
| 9 | AXM | 324 |
| 10 | Vueling | 307 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 273 |
| 13 | AZU | 262 |
| 14 | QLK | 259 |
| 15 | Delta Air Lines | 246 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 201 |
| 19 | Japan Airlines | 196 |
| 20 | VIV | 196 |
| 21 | easyJet | 194 |
| 22 | EJU | 193 |
| 23 | AEE | 189 |
| 24 | WIF | 187 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | GLO | 160 |
| 29 | JetBlue | 159 |
| 30 | AXB | 157 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23806 |
| 2 | 🇮🇳 IN | 2403 |
| 3 | 🇪🇸 ES | 2219 |
| 4 | 🇦🇺 AU | 2149 |
| 5 | 🇧🇷 BR | 1732 |
| 6 | 🇯🇵 JP | 1663 |
| 7 | 🇮🇹 IT | 1542 |
| 8 | 🇨🇴 CO | 1518 |
| 9 | 🇩🇪 DE | 1504 |
| 10 | 🇨🇦 CA | 1477 |
| 11 | 🇬🇧 GB | 1204 |
| 12 | 🇫🇷 FR | 1101 |
| 13 | 🇲🇽 MX | 974 |
| 14 | 🇬🇷 GR | 855 |
| 15 | 🇨🇭 CH | 844 |
| 16 | 🇲🇾 MY | 776 |
| 17 | 🇳🇿 NZ | 662 |
| 18 | 🇳🇴 NO | 633 |
| 19 | 🇿🇦 ZA | 612 |
| 20 | 🇵🇭 PH | 567 |
| 21 | 🇬🇹 GT | 553 |
| 22 | 🇹🇭 TH | 547 |
| 23 | 🇹🇷 TR | 546 |
| 24 | 🇰🇷 KR | 516 |
| 25 | 🇵🇱 PL | 452 |
| 26 | 🇲🇦 MA | 375 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 300 |
| 29 | 🇳🇱 NL | 287 |
| 30 | 🇮🇩 ID | 287 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 559 |
| 3 | El Dorado International Airport |  | CO | 541 |
| 4 | Denver International Airport |  | US | 512 |
| 5 | Indira Gandhi International Airport |  | IN | 506 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 418 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 391 |
| 9 | Zurich Airport |  | CH | 359 |
| 10 | Guaymaral Airport |  | CO | 359 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 305 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 299 |
| 16 | Kuala Lumpur International Airport |  | MY | 293 |
| 17 | Macau International Airport |  | MO | 286 |
| 18 | Charlotte/Douglas International Airport |  | US | 271 |
| 19 | Bengaluru International Airport |  | IN | 271 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Ninoy Aquino International Airport |  | PH | 260 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 242 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 231 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 214 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 31 | Capua Airport |  | IT | 205 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 204 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 202 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 201 |
| 35 | Miami International Airport |  | US | 201 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 193 |
| 38 | Seattle-Tacoma International Airport |  | US | 191 |
| 39 | Barcelona International Airport |  | ES | 190 |
| 40 | Don Mueang International Airport |  | TH | 186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 142 | 1h 8m | 706 km | 1,728.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 111 | 24m | 225 km | 430.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 102 | 28m | 304 km | 534.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 88 | 1h 27m | 910 km | 1,380.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 77 | 19m | 165 km | 219.0 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 69 | 55m | 546 km | 649.6 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 64 | 1h 12m | 770 km | 850.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 59 | 31m | 369 km | 375.5 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 56 | 45m | 452 km | 436.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 47 | 20m | 147 km | 118.9 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 40 | 55m | 630 km | 434.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RGA03 | RGA | Reichenbach Air Base (LSGR) | Bern Belp Airport (LSZB) | 2026-04-12 08:37 UTC | 2026-04-12 08:52 UTC | 14m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Simara Airport (VNSI) | 2026-04-12 05:23 UTC | 2026-04-12 08:41 UTC | 3h 17m |
| TRP7 | TRP | Clements Airport (4MD4) | Joint Base Andrews Airport (KADW) | 2026-04-12 08:19 UTC | 2026-04-12 08:33 UTC | 13m |
| AAE121 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-04-11 19:10 UTC | 2026-04-12 08:26 UTC | 13h 15m |
| FDB539 | flydubai | Dubai International Airport (OMDB) | Langtang Airport (VNLT) | 2026-04-12 04:54 UTC | 2026-04-12 08:19 UTC | 3h 24m |
| RYR21AQ | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 06:53 UTC | 2026-04-12 08:18 UTC | 1h 25m |
| BNOB | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-12 07:51 UTC | 2026-04-12 08:04 UTC | 12m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-04-12 07:12 UTC | 2026-04-12 08:01 UTC | 48m |
| IGO612Y | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-12 06:03 UTC | 2026-04-12 07:54 UTC | 1h 51m |
| DLH9MT | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-12 07:22 UTC | 2026-04-12 07:54 UTC | 32m |
| AXM278 | AXM | Kuala Lumpur International Airport (WMKK) | Anduki Airport (WBAK) | 2026-04-12 06:04 UTC | 2026-04-12 07:53 UTC | 1h 49m |
| WMT9984 | WMT | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-04-12 06:26 UTC | 2026-04-12 07:49 UTC | 1h 23m |
| VLG5PP | Vueling | Barcelona International Airport (LEBL) | Pamplona Airport (LEPP) | 2026-04-12 07:14 UTC | 2026-04-12 07:47 UTC | 33m |
| BD681 |  | Perth Jandakot Airport (YPJT) | Dale River Airport (YDVE) | 2026-04-12 07:30 UTC | 2026-04-12 07:43 UTC | 13m |
| N45NM |  | Stillwater Regional Airport (KSWO) | KL64 (KL64) | 2026-04-12 05:18 UTC | 2026-04-12 07:39 UTC | 2h 21m |
| SHA223 | SHA | Langtang Airport (VNLT) | Rukumkot Airport (VNRK) | 2026-04-12 06:58 UTC | 2026-04-12 07:38 UTC | 39m |
| QLK7802 | QLK | Canberra International Airport (YSCB) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-12 07:05 UTC | 2026-04-12 07:37 UTC | 32m |
| AFR35ZZ | Air France | Charles de Gaulle International Airport (LFPG) | San Sebastian Airport (LESO) | 2026-04-12 06:28 UTC | 2026-04-12 07:35 UTC | 1h 6m |
| ANE63GR | ANE | Malaga Airport (LEMG) | Melilla Airport (GEML) | 2026-04-12 07:03 UTC | 2026-04-12 07:34 UTC | 31m |
| JAL3114 | Japan Airlines | New Chitose Airport (RJCC) | Nagoya Airport (RJNA) | 2026-04-12 06:18 UTC | 2026-04-12 07:33 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
