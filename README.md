# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_06:35:02_UTC-green)

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

**Latest saved flight:** 2026-04-06 06:35:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 06:35:02 UTC

- **19,453** saved flights
- **9,812** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,453** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **245,333.6 tonnes** estimated CO2 emissions
- **14,222,240 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 793 |
| 3 | IndiGo | 547 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 257 |
| 9 | Vueling | 211 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 192 |
| 12 | Delta Air Lines | 177 |
| 13 | LXJ | 171 |
| 14 | All Nippon Airways | 165 |
| 15 | QLK | 158 |
| 16 | AZU | 149 |
| 17 | VIV | 149 |
| 18 | Swiss International | 143 |
| 19 | United Airlines | 133 |
| 20 | Alaska Airlines | 132 |
| 21 | Avianca | 130 |
| 22 | Japan Airlines | 127 |
| 23 | easyJet | 124 |
| 24 | AEE | 122 |
| 25 | EJU | 122 |
| 26 | EDV | 118 |
| 27 | WIF | 116 |
| 28 | AXB | 114 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15348 |
| 2 | 🇮🇳 IN | 1667 |
| 3 | 🇪🇸 ES | 1573 |
| 4 | 🇦🇺 AU | 1375 |
| 5 | 🇧🇷 BR | 1124 |
| 6 | 🇨🇴 CO | 1056 |
| 7 | 🇯🇵 JP | 1036 |
| 8 | 🇩🇪 DE | 969 |
| 9 | 🇮🇹 IT | 912 |
| 10 | 🇨🇦 CA | 857 |
| 11 | 🇬🇧 GB | 744 |
| 12 | 🇫🇷 FR | 704 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 547 |
| 15 | 🇨🇭 CH | 506 |
| 16 | 🇬🇹 GT | 452 |
| 17 | 🇲🇾 MY | 446 |
| 18 | 🇿🇦 ZA | 419 |
| 19 | 🇳🇿 NZ | 414 |
| 20 | 🇳🇴 NO | 391 |
| 21 | 🇹🇷 TR | 371 |
| 22 | 🇵🇭 PH | 368 |
| 23 | 🇰🇷 KR | 335 |
| 24 | 🇹🇭 TH | 289 |
| 25 | 🇵🇱 PL | 280 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 209 |
| 29 | 🇲🇴 MO | 199 |
| 30 | 🇲🇪 ME | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 482 |
| 2 | El Dorado International Airport |  | CO | 404 |
| 3 | Denver International Airport |  | US | 363 |
| 4 | Tokyo International Airport |  | JP | 355 |
| 5 | Indira Gandhi International Airport |  | IN | 346 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 257 |
| 8 | Harry Reid International Airport |  | US | 256 |
| 9 | Zurich Airport |  | CH | 234 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 216 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 13 | Chicago O'Hare International Airport |  | US | 210 |
| 14 | Guaymaral Airport |  | CO | 201 |
| 15 | Macau International Airport |  | MO | 199 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 199 |
| 17 | Charlotte/Douglas International Airport |  | US | 190 |
| 18 | Bengaluru International Airport |  | IN | 186 |
| 19 | Madrid Barajas International Airport |  | ES | 185 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 179 |
| 21 | Tenerife Norte Airport |  | ES | 174 |
| 22 | Ninoy Aquino International Airport |  | PH | 168 |
| 23 | Congonhas Airport |  | BR | 167 |
| 24 | Salt Lake City International Airport |  | US | 157 |
| 25 | Reno/Tahoe International Airport |  | US | 156 |
| 26 | Kuala Lumpur International Airport |  | MY | 155 |
| 27 | Daniel K Inouye International Airport |  | US | 153 |
| 28 | Malpensa International Airport |  | IT | 148 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 31 | Charles de Gaulle International Airport |  | FR | 143 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 142 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 133 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 37 | Pune Airport |  | IN | 131 |
| 38 | Barcelona International Airport |  | ES | 130 |
| 39 | O. R. Tambo International Airport |  | ZA | 130 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 89 | 1h 8m | 706 km | 1,083.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 71 | 24m | 225 km | 275.4 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 57 | 1h 27m | 910 km | 894.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 56 | 1h 43m | 1,156 km | 1,117.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 55 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 41 | 1h 12m | 770 km | 544.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 39 | 23m | 252 km | 169.3 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 39 | 54m | 546 km | 367.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 34 | 46m | 452 km | 265.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 31 | 20m | 250 km | 133.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR46YA | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Cagliari / Elmas Airport (LIEE) | 2026-04-06 04:41 UTC | 2026-04-06 06:35 UTC | 1h 53m |
| EJA550 | EJA | Boeing Field/King County International Airport (KBFI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-06 04:11 UTC | 2026-04-06 06:03 UTC | 1h 52m |
| HAM | HAM | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-04-06 05:42 UTC | 2026-04-06 06:00 UTC | 18m |
| DLH8PL | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-04-06 04:55 UTC | 2026-04-06 05:59 UTC | 1h 3m |
| AM295 |  | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-04-06 05:10 UTC | 2026-04-06 05:55 UTC | 45m |
| RYR7273 | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Otocac Airport (LDRO) | 2026-04-06 04:49 UTC | 2026-04-06 05:52 UTC | 1h 3m |
| IGO497 | IndiGo | Bengaluru International Airport (VOBL) | Ambala Air Force Station (VIAM) | 2026-04-06 02:06 UTC | 2026-04-06 05:49 UTC | 3h 43m |
| VTFSP | VTF | Bhiwani Airport (VIBW) | Jhunjhunu Airport (VI69) | 2026-04-06 05:12 UTC | 2026-04-06 05:47 UTC | 35m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-06 05:18 UTC | 2026-04-06 05:45 UTC | 27m |
| TNU080 | TNU | Yalgoo Airport (YYAL) | Perth International Airport (YPPH) | 2026-04-06 05:05 UTC | 2026-04-06 05:44 UTC | 39m |
| ROT621R | ROT | Henri Coanda International Airport (LROP) | Oradea International Airport (LROD) | 2026-04-06 04:31 UTC | 2026-04-06 05:44 UTC | 1h 13m |
| VLG5QN | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-04-06 04:53 UTC | 2026-04-06 05:43 UTC | 49m |
| APG711 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-04-06 05:15 UTC | 2026-04-06 05:43 UTC | 27m |
| EOK351 | EOK | New Chitose Airport (RJCC) | Cheongju International Airport (RKTU) | 2026-04-06 03:00 UTC | 2026-04-06 05:41 UTC | 2h 41m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-04-06 05:26 UTC | 2026-04-06 05:41 UTC | 14m |
| SKYFALL2 | SKY | Blythe Airport (KBLH) | Blythe Airport (KBLH) | 2026-04-06 05:30 UTC | 2026-04-06 05:40 UTC | 10m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-04-06 05:12 UTC | 2026-04-06 05:40 UTC | 28m |
| TVF38YC | TVF | Biarritz-Anglet-Bayonne Airport (LFBZ) | Paris-Orly Airport (LFPO) | 2026-04-06 04:41 UTC | 2026-04-06 05:40 UTC | 59m |
| SNJ35 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-06 04:10 UTC | 2026-04-06 05:39 UTC | 1h 29m |
| VTJHP | VTJ | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-06 05:19 UTC | 2026-04-06 05:37 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
