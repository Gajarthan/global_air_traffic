# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_06:32:17_UTC-green)

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

**Latest saved flight:** 2026-04-07 06:32:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 06:32:17 UTC

- **21,321** saved flights
- **10,583** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,321** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **266,693.3 tonnes** estimated CO2 emissions
- **15,460,483 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 880 |
| 3 | IndiGo | 594 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 264 |
| 9 | LATAM Airlines | 226 |
| 10 | Vueling | 225 |
| 11 | AXM | 201 |
| 12 | Delta Air Lines | 189 |
| 13 | LXJ | 186 |
| 14 | All Nippon Airways | 181 |
| 15 | QLK | 176 |
| 16 | AZU | 169 |
| 17 | VIV | 157 |
| 18 | Swiss International | 156 |
| 19 | Alaska Airlines | 146 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 143 |
| 22 | Avianca | 139 |
| 23 | Japan Airlines | 136 |
| 24 | EJU | 135 |
| 25 | AEE | 132 |
| 26 | EDV | 127 |
| 27 | WIF | 126 |
| 28 | AXB | 121 |
| 29 | Air France | 111 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16950 |
| 2 | 🇮🇳 IN | 1803 |
| 3 | 🇪🇸 ES | 1668 |
| 4 | 🇦🇺 AU | 1501 |
| 5 | 🇧🇷 BR | 1231 |
| 6 | 🇨🇴 CO | 1175 |
| 7 | 🇯🇵 JP | 1126 |
| 8 | 🇮🇹 IT | 1045 |
| 9 | 🇩🇪 DE | 1031 |
| 10 | 🇨🇦 CA | 958 |
| 11 | 🇬🇧 GB | 826 |
| 12 | 🇫🇷 FR | 765 |
| 13 | 🇲🇽 MX | 726 |
| 14 | 🇬🇷 GR | 591 |
| 15 | 🇨🇭 CH | 571 |
| 16 | 🇲🇾 MY | 469 |
| 17 | 🇿🇦 ZA | 465 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇿 NZ | 438 |
| 20 | 🇳🇴 NO | 433 |
| 21 | 🇹🇷 TR | 412 |
| 22 | 🇵🇭 PH | 404 |
| 23 | 🇰🇷 KR | 359 |
| 24 | 🇹🇭 TH | 315 |
| 25 | 🇵🇱 PL | 308 |
| 26 | 🇲🇦 MA | 259 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇲🇪 ME | 221 |
| 29 | 🇮🇩 ID | 219 |
| 30 | 🇳🇱 NL | 209 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Denver International Airport |  | US | 393 |
| 4 | Tokyo International Airport |  | JP | 386 |
| 5 | Indira Gandhi International Airport |  | IN | 370 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Harry Reid International Airport |  | US | 283 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 281 |
| 9 | Zurich Airport |  | CH | 258 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 232 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Guaymaral Airport |  | CO | 230 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 229 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 212 |
| 16 | Charlotte/Douglas International Airport |  | US | 208 |
| 17 | Bengaluru International Airport |  | IN | 204 |
| 18 | Macau International Airport |  | MO | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 196 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 190 |
| 22 | Ninoy Aquino International Airport |  | PH | 185 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Salt Lake City International Airport |  | US | 170 |
| 25 | Reno/Tahoe International Airport |  | US | 168 |
| 26 | Daniel K Inouye International Airport |  | US | 167 |
| 27 | Malpensa International Airport |  | IT | 164 |
| 28 | Kuala Lumpur International Airport |  | MY | 164 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 158 |
| 31 | Charles de Gaulle International Airport |  | FR | 153 |
| 32 | Miami International Airport |  | US | 152 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 146 |
| 35 | Vitoria/Foronda Airport |  | ES | 146 |
| 36 | O. R. Tambo International Airport |  | ZA | 143 |
| 37 | Pune Airport |  | IN | 142 |
| 38 | Barcelona International Airport |  | ES | 140 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 98 | 1h 8m | 706 km | 1,193.2 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 81 | 24m | 225 km | 314.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 70 | 28m | 304 km | 367.0 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 61 | 1h 27m | 910 km | 957.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 60 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 47 | 19m | 165 km | 133.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 45 | 1h 12m | 770 km | 597.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 43 | 55m | 546 km | 404.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 37 | 46m | 452 km | 288.4 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBXBO | HBX | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-04-07 06:21 UTC | 2026-04-07 06:32 UTC | 11m |
| SAS744 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Nida Airport (EYND) | 2026-04-07 06:06 UTC | 2026-04-07 06:31 UTC | 24m |
| AUA96F | Austrian Airlines | Vienna International Airport (LOWW) | Darlowek Naval Air Base (EPDA) | 2026-04-07 05:25 UTC | 2026-04-07 06:26 UTC | 1h 1m |
| HSF8283 | HSF | G 530 Airport (RK49) | G 417 Airport (RK34) | 2026-04-07 05:54 UTC | 2026-04-07 06:25 UTC | 30m |
| VANT | VAN | RAAF Base Pearce (YPEA) | Catholic Agricultural College Bindoon Airstrip (YBOO) | 2026-04-07 05:35 UTC | 2026-04-07 06:19 UTC | 43m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-07 05:07 UTC | 2026-04-07 06:18 UTC | 1h 11m |
| OAE4068 | OAE | Sofia Airport (LBSF) | Indira Gandhi International Airport (VIDP) | 2026-04-06 22:22 UTC | 2026-04-07 06:09 UTC | 7h 46m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-07 05:29 UTC | 2026-04-07 06:04 UTC | 35m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-07 05:47 UTC | 2026-04-07 06:01 UTC | 14m |
| N700JV |  | Aurillac Airport (LFLW) | Lyon-Bron Airport (LFLY) | 2026-04-07 05:14 UTC | 2026-04-07 05:53 UTC | 38m |
| HST3481 | HST | Tallinn Airport (EETN) | Siauliai International Airport (EYSA) | 2026-04-07 05:16 UTC | 2026-04-07 05:47 UTC | 31m |
|  |  | Hakodate Airport (RJCH) | Hakodate Airport (RJCH) | 2026-04-07 05:44 UTC | 2026-04-07 05:47 UTC | 2m |
| IGO6HC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Thamkharka Airport (VNTH) | 2026-04-07 04:58 UTC | 2026-04-07 05:41 UTC | 43m |
| AEE911 | AEE | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-07 04:23 UTC | 2026-04-07 05:40 UTC | 1h 17m |
| RYR8ZU | Ryanair | Warsaw Modlin Airport (EPMO) | Capua Airport (LIAU) | 2026-04-07 03:56 UTC | 2026-04-07 05:39 UTC | 1h 42m |
| AWQ180 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-04-07 05:23 UTC | 2026-04-07 05:38 UTC | 15m |
| N202FF |  | Joe Foss Field (KFSD) | Philip Airport (KPHP) | 2026-04-07 04:38 UTC | 2026-04-07 05:38 UTC | 1h 0m |
| VTFTO | VTF | Hosur Airport (VO95) | Mysore Airport (VOMY) | 2026-04-07 04:58 UTC | 2026-04-07 05:38 UTC | 39m |
| RYR1BG | Ryanair | Frankfurt-Hahn Airport (EDFH) | LINF (LINF) | 2026-04-07 04:27 UTC | 2026-04-07 05:36 UTC | 1h 9m |
| JJP801 | JJP | Narita International Airport (RJAA) | Asahikawa Airport (RJEC) | 2026-04-07 04:31 UTC | 2026-04-07 05:36 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
