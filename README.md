# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_11:19:54_UTC-green)

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

**Latest saved flight:** 2026-04-11 11:19:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 11:19:54 UTC

- **28,520** saved flights
- **13,307** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,520** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **347,413.1 tonnes** estimated CO2 emissions
- **20,139,888 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1164 |
| 2 | SkyWest Airlines | 1155 |
| 3 | IndiGo | 752 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 348 |
| 9 | AXM | 306 |
| 10 | Vueling | 291 |
| 11 | LATAM Airlines | 276 |
| 12 | All Nippon Airways | 262 |
| 13 | QLK | 254 |
| 14 | Delta Air Lines | 240 |
| 15 | AZU | 236 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 207 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 189 |
| 20 | easyJet | 186 |
| 21 | EJU | 184 |
| 22 | VIV | 183 |
| 23 | WIF | 183 |
| 24 | AEE | 180 |
| 25 | United Airlines | 173 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | AXB | 150 |
| 29 | JetBlue | 150 |
| 30 | Air France | 145 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22467 |
| 2 | 🇮🇳 IN | 2313 |
| 3 | 🇪🇸 ES | 2102 |
| 4 | 🇦🇺 AU | 2082 |
| 5 | 🇧🇷 BR | 1603 |
| 6 | 🇯🇵 JP | 1598 |
| 7 | 🇮🇹 IT | 1447 |
| 8 | 🇩🇪 DE | 1437 |
| 9 | 🇨🇴 CO | 1407 |
| 10 | 🇨🇦 CA | 1395 |
| 11 | 🇬🇧 GB | 1153 |
| 12 | 🇫🇷 FR | 1052 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 822 |
| 15 | 🇨🇭 CH | 794 |
| 16 | 🇲🇾 MY | 734 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 617 |
| 19 | 🇿🇦 ZA | 587 |
| 20 | 🇵🇭 PH | 543 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 515 |
| 23 | 🇹🇭 TH | 511 |
| 24 | 🇰🇷 KR | 495 |
| 25 | 🇵🇱 PL | 430 |
| 26 | 🇲🇦 MA | 348 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 285 |
| 29 | 🇳🇱 NL | 277 |
| 30 | 🇮🇩 ID | 275 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 536 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Indira Gandhi International Airport |  | IN | 481 |
| 5 | Denver International Airport |  | US | 478 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 402 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 365 |
| 9 | Zurich Airport |  | CH | 342 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 294 |
| 13 | Frankfurt am Main International Airport |  | DE | 293 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 274 |
| 17 | Macau International Airport |  | MO | 263 |
| 18 | Bengaluru International Airport |  | IN | 259 |
| 19 | Charlotte/Douglas International Airport |  | US | 257 |
| 20 | Ninoy Aquino International Airport |  | PH | 249 |
| 21 | Madrid Barajas International Airport |  | ES | 247 |
| 22 | Tenerife Norte Airport |  | ES | 242 |
| 23 | Congonhas Airport |  | BR | 230 |
| 24 | Malpensa International Airport |  | IT | 222 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 26 | Salt Lake City International Airport |  | US | 220 |
| 27 | Daniel K Inouye International Airport |  | US | 219 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 200 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 195 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 192 |
| 33 | Miami International Airport |  | US | 189 |
| 34 | Capua Airport |  | IT | 188 |
| 35 | O. R. Tambo International Airport |  | ZA | 186 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 37 | Seattle-Tacoma International Airport |  | US | 181 |
| 38 | Vitoria/Foronda Airport |  | ES | 179 |
| 39 | Barcelona International Airport |  | ES | 178 |
| 40 | Don Mueang International Airport |  | TH | 173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 137 | 1h 8m | 706 km | 1,668.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 85 | 1h 27m | 910 km | 1,333.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 72 | 19m | 165 km | 204.8 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 64 | 55m | 546 km | 602.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 58 | 27m | 275 km | 274.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 55 | 31m | 369 km | 350.1 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 45 | 1h 42m | 1,423 km | 1,104.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 39 | 31m | 304 km | 204.2 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 38 | 26m | 215 km | 140.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA038 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-04-11 00:30 UTC | 2026-04-11 11:19 UTC | 10h 49m |
| BFD65H | BFD | Paderborn Lippstadt Airport (EDLP) | Trento / Mattarello Airport (LIDT) | 2026-04-11 10:04 UTC | 2026-04-11 11:02 UTC | 57m |
| GPAFF | GPA | Rochester Airport (EGTO) | Rochester Airport (EGTO) | 2026-04-11 10:52 UTC | 2026-04-11 10:56 UTC | 3m |
| MPC003 | MPC | Ciampino Airport (LIRA) | Tivat Airport (LYTV) | 2026-04-11 10:10 UTC | 2026-04-11 10:51 UTC | 40m |
| GUIDO | GUI | Redhill Aerodrome (EGKR) | Redhill Aerodrome (EGKR) | 2026-04-11 10:29 UTC | 2026-04-11 10:48 UTC | 18m |
| RYR9QK | Ryanair | Madrid Barajas International Airport (LEMD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-11 07:48 UTC | 2026-04-11 10:46 UTC | 2h 57m |
| DLH6NJ | Lufthansa | Munich International Airport (EDDM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-11 09:41 UTC | 2026-04-11 10:42 UTC | 1h 0m |
| ANE1113 | ANE | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-11 09:56 UTC | 2026-04-11 10:41 UTC | 45m |
| AIZ1211 | AIZ | Ben Gurion International Airport (LLBG) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-11 07:25 UTC | 2026-04-11 10:41 UTC | 3h 15m |
| HEY01P | HEY | Wevelgem Airport (EBKT) | Samedan Airport (LSZS) | 2026-04-11 09:29 UTC | 2026-04-11 10:40 UTC | 1h 10m |
| IGO6413 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-04-11 10:17 UTC | 2026-04-11 10:39 UTC | 22m |
| IBE0445 | Iberia | Madrid Barajas International Airport (LEMD) | Pamplona Airport (LEPP) | 2026-04-11 10:08 UTC | 2026-04-11 10:35 UTC | 26m |
| ANA860 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Tokyo International Airport (RJTT) | 2026-04-11 06:48 UTC | 2026-04-11 10:33 UTC | 3h 45m |
| JAL265 | Japan Airlines | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-11 09:35 UTC | 2026-04-11 10:33 UTC | 58m |
| RTV2N | RTV | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-04-11 10:22 UTC | 2026-04-11 10:33 UTC | 10m |
| EZY34UJ | easyJet | Bristol International Airport (EGGD) | Zemunik Airport (LDZD) | 2026-04-11 08:38 UTC | 2026-04-11 10:32 UTC | 1h 53m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-11 09:00 UTC | 2026-04-11 10:31 UTC | 1h 30m |
| IE747 |  | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-04-11 10:18 UTC | 2026-04-11 10:24 UTC | 6m |
| ABL8823 | ABL | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-11 09:55 UTC | 2026-04-11 10:23 UTC | 27m |
| APJ456 | APJ | New Chitose Airport (RJCC) | Iwami Airport (RJOW) | 2026-04-11 08:22 UTC | 2026-04-11 10:22 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
