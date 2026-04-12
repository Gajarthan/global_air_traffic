# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_14:37:06_UTC-green)

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

**Latest saved flight:** 2026-04-12 14:37:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 14:37:06 UTC

- **30,577** saved flights
- **13,946** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,577** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **375,148.6 tonnes** estimated CO2 emissions
- **21,747,743 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1270 |
| 2 | SkyWest Airlines | 1232 |
| 3 | IndiGo | 802 |
| 4 | American Airlines | 527 |
| 5 | EJA | 524 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 409 |
| 8 | Lufthansa | 364 |
| 9 | AXM | 335 |
| 10 | Vueling | 318 |
| 11 | LATAM Airlines | 301 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 267 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 249 |
| 16 | LXJ | 241 |
| 17 | Swiss International | 226 |
| 18 | Alaska Airlines | 201 |
| 19 | EJU | 201 |
| 20 | easyJet | 201 |
| 21 | VIV | 198 |
| 22 | Japan Airlines | 197 |
| 23 | WIF | 195 |
| 24 | AEE | 193 |
| 25 | EDV | 179 |
| 26 | United Airlines | 179 |
| 27 | Avianca | 167 |
| 28 | Air France | 163 |
| 29 | AIQ | 163 |
| 30 | GLO | 162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23939 |
| 2 | 🇮🇳 IN | 2460 |
| 3 | 🇪🇸 ES | 2276 |
| 4 | 🇦🇺 AU | 2172 |
| 5 | 🇧🇷 BR | 1769 |
| 6 | 🇯🇵 JP | 1711 |
| 7 | 🇮🇹 IT | 1593 |
| 8 | 🇩🇪 DE | 1540 |
| 9 | 🇨🇴 CO | 1534 |
| 10 | 🇨🇦 CA | 1482 |
| 11 | 🇬🇧 GB | 1233 |
| 12 | 🇫🇷 FR | 1130 |
| 13 | 🇲🇽 MX | 979 |
| 14 | 🇬🇷 GR | 877 |
| 15 | 🇨🇭 CH | 862 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇿 NZ | 665 |
| 18 | 🇳🇴 NO | 658 |
| 19 | 🇿🇦 ZA | 636 |
| 20 | 🇵🇭 PH | 575 |
| 21 | 🇹🇭 TH | 569 |
| 22 | 🇹🇷 TR | 556 |
| 23 | 🇬🇹 GT | 553 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 463 |
| 26 | 🇲🇦 MA | 394 |
| 27 | 🇧🇸 BS | 322 |
| 28 | 🇲🇪 ME | 308 |
| 29 | 🇮🇩 ID | 296 |
| 30 | 🇳🇱 NL | 293 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 724 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 545 |
| 4 | Indira Gandhi International Airport |  | IN | 517 |
| 5 | Denver International Airport |  | US | 512 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 428 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 392 |
| 9 | Zurich Airport |  | CH | 373 |
| 10 | Guaymaral Airport |  | CO | 366 |
| 11 | Chicago O'Hare International Airport |  | US | 315 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 314 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 14 | Frankfurt am Main International Airport |  | DE | 308 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 290 |
| 18 | Bengaluru International Airport |  | IN | 279 |
| 19 | Charlotte/Douglas International Airport |  | US | 273 |
| 20 | Tenerife Norte Airport |  | ES | 271 |
| 21 | Madrid Barajas International Airport |  | ES | 269 |
| 22 | Ninoy Aquino International Airport |  | PH | 264 |
| 23 | Congonhas Airport |  | BR | 257 |
| 24 | Malpensa International Airport |  | IT | 248 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 235 |
| 26 | Daniel K Inouye International Airport |  | US | 232 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 221 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 214 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 212 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 210 |
| 33 | Capua Airport |  | IT | 209 |
| 34 | O. R. Tambo International Airport |  | ZA | 205 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 205 |
| 36 | Miami International Airport |  | US | 203 |
| 37 | Vitoria/Foronda Airport |  | ES | 201 |
| 38 | Barcelona International Airport |  | ES | 196 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 142 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 127 | 14m | 114 km | 249.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 14 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 64 | 27m | 275 km | 303.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 55 | 21m | 244 km | 231.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 52 | 20m | 250 km | 224.6 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 43 | 1h 21m | 961 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CLX7956 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-04-11 20:33 UTC | 2026-04-12 14:37 UTC | 18h 3m |
| N8172Q |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-04-12 14:17 UTC | 2026-04-12 14:34 UTC | 16m |
| QTR8474 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-04-12 07:31 UTC | 2026-04-12 14:30 UTC | 6h 58m |
| QTR8410 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-04-12 07:29 UTC | 2026-04-12 14:28 UTC | 6h 59m |
| N562SD |  | Wings Field (KLOM) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-12 14:04 UTC | 2026-04-12 14:24 UTC | 19m |
| AIC211 | Air India | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-12 13:09 UTC | 2026-04-12 14:23 UTC | 1h 13m |
| N7442T |  | Bostwick Farm Airport (VT23) | Franklin County State Airport (KFSO) | 2026-04-12 14:05 UTC | 2026-04-12 14:22 UTC | 17m |
| N500EX |  | Willow Point Airport (AL71) | Willow Point Airport (AL71) | 2026-04-12 14:15 UTC | 2026-04-12 14:21 UTC | 6m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-12 14:02 UTC | 2026-04-12 14:18 UTC | 15m |
| N88SM |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-12 13:49 UTC | 2026-04-12 14:17 UTC | 28m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | Skywagon Farm Airport (NM88) | 2026-04-12 13:34 UTC | 2026-04-12 14:16 UTC | 42m |
| AZG998 | AZG | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-04-11 18:32 UTC | 2026-04-12 14:16 UTC | 19h 43m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-12 13:50 UTC | 2026-04-12 14:08 UTC | 17m |
| N67ZT |  | Rocky Mountain Metro Airport (KBJC) | Northern Colorado Regional Airport (KFNL) | 2026-04-12 13:43 UTC | 2026-04-12 14:04 UTC | 21m |
| WIF3NL | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-04-12 13:21 UTC | 2026-04-12 14:03 UTC | 42m |
| N1553G |  | MS54 (MS54) | Morrilton Municipal Airport (KBDQ) | 2026-04-12 13:21 UTC | 2026-04-12 14:03 UTC | 41m |
| N331MW |  | Skyview Airpark (WY05) | Walden-Jackson County Airport (K33V) | 2026-04-12 13:39 UTC | 2026-04-12 14:02 UTC | 22m |
| FJO66L | FJO | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-04-12 13:59 UTC | 2026-04-12 13:59 UTC | 0m |
| DMYIS | DMY | Hoxter-Holzminden Airport (EDVI) | Hildesheim Airport (EDVM) | 2026-04-12 13:40 UTC | 2026-04-12 13:58 UTC | 17m |
| B8271 |  | Narita International Airport (RJAA) | Macau International Airport (VMMC) | 2026-04-12 09:25 UTC | 2026-04-12 13:57 UTC | 4h 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
