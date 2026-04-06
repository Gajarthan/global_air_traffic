# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_09:43:13_UTC-green)

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

**Latest saved flight:** 2026-04-06 09:43:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 09:43:13 UTC

- **19,612** saved flights
- **9,866** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,612** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **247,283.6 tonnes** estimated CO2 emissions
- **14,335,283 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 808 |
| 3 | IndiGo | 555 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 257 |
| 9 | Vueling | 213 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 194 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 171 |
| 14 | LXJ | 171 |
| 15 | QLK | 162 |
| 16 | AZU | 149 |
| 17 | VIV | 149 |
| 18 | Swiss International | 146 |
| 19 | United Airlines | 133 |
| 20 | Alaska Airlines | 132 |
| 21 | easyJet | 131 |
| 22 | Avianca | 130 |
| 23 | Japan Airlines | 130 |
| 24 | EJU | 125 |
| 25 | AEE | 124 |
| 26 | EDV | 118 |
| 27 | WIF | 117 |
| 28 | AXB | 114 |
| 29 | Air France | 107 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15362 |
| 2 | 🇮🇳 IN | 1697 |
| 3 | 🇪🇸 ES | 1588 |
| 4 | 🇦🇺 AU | 1397 |
| 5 | 🇧🇷 BR | 1124 |
| 6 | 🇯🇵 JP | 1062 |
| 7 | 🇨🇴 CO | 1056 |
| 8 | 🇩🇪 DE | 979 |
| 9 | 🇮🇹 IT | 943 |
| 10 | 🇨🇦 CA | 857 |
| 11 | 🇬🇧 GB | 760 |
| 12 | 🇫🇷 FR | 714 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 554 |
| 15 | 🇨🇭 CH | 523 |
| 16 | 🇲🇾 MY | 454 |
| 17 | 🇬🇹 GT | 452 |
| 18 | 🇿🇦 ZA | 433 |
| 19 | 🇳🇿 NZ | 416 |
| 20 | 🇳🇴 NO | 396 |
| 21 | 🇹🇷 TR | 378 |
| 22 | 🇵🇭 PH | 376 |
| 23 | 🇰🇷 KR | 343 |
| 24 | 🇹🇭 TH | 296 |
| 25 | 🇵🇱 PL | 284 |
| 26 | 🇲🇦 MA | 242 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 211 |
| 29 | 🇲🇪 ME | 203 |
| 30 | 🇲🇴 MO | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 482 |
| 2 | El Dorado International Airport |  | CO | 404 |
| 3 | Tokyo International Airport |  | JP | 365 |
| 4 | Denver International Airport |  | US | 363 |
| 5 | Indira Gandhi International Airport |  | IN | 351 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 260 |
| 8 | Harry Reid International Airport |  | US | 256 |
| 9 | Zurich Airport |  | CH | 239 |
| 10 | Frankfurt am Main International Airport |  | DE | 229 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 216 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 13 | Chicago O'Hare International Airport |  | US | 210 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 203 |
| 15 | Guaymaral Airport |  | CO | 201 |
| 16 | Macau International Airport |  | MO | 199 |
| 17 | Bengaluru International Airport |  | IN | 192 |
| 18 | Charlotte/Douglas International Airport |  | US | 190 |
| 19 | Madrid Barajas International Airport |  | ES | 187 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 179 |
| 21 | Tenerife Norte Airport |  | ES | 175 |
| 22 | Ninoy Aquino International Airport |  | PH | 171 |
| 23 | Congonhas Airport |  | BR | 167 |
| 24 | Kuala Lumpur International Airport |  | MY | 158 |
| 25 | Salt Lake City International Airport |  | US | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 153 |
| 28 | Malpensa International Airport |  | IT | 149 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Charles de Gaulle International Airport |  | FR | 145 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 145 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 136 |
| 35 | O. R. Tambo International Airport |  | ZA | 134 |
| 36 | Pune Airport |  | IN | 133 |
| 37 | Barcelona International Airport |  | ES | 132 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 93 | 1h 8m | 706 km | 1,132.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 66 | 28m | 304 km | 346.0 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 58 | 1h 27m | 910 km | 910.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 55 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 42 | 1h 12m | 770 km | 557.9 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 41 | 23m | 252 km | 178.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 40 | 54m | 546 km | 376.6 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 34 | 46m | 452 km | 265.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 33 | 20m | 250 km | 142.5 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N104AE |  | Stanton Airport (KI50) | Blue Grass Airport (KLEX) | 2026-04-06 09:25 UTC | 2026-04-06 09:43 UTC | 18m |
| 83C |  | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-06 08:56 UTC | 2026-04-06 09:31 UTC | 35m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-06 08:42 UTC | 2026-04-06 09:22 UTC | 39m |
| S2AFH |  | Ishurdi Airport (VGIS) | VGZR (VGZR) | 2026-04-06 08:35 UTC | 2026-04-06 09:19 UTC | 44m |
| FIN1175 | Finnair | Helsinki Vantaa Airport (EFHK) | Oksywie Military Air Base (EPOK) | 2026-04-06 07:32 UTC | 2026-04-06 09:17 UTC | 1h 44m |
| SFS70 | SFS | Vigo Airport (LEVX) | La Morgal Airport (LEMR) | 2026-04-06 08:26 UTC | 2026-04-06 09:09 UTC | 43m |
| EZY32MN | easyJet | Amsterdam Airport Schiphol (EHAM) | Liverpool John Lennon Airport (EGGP) | 2026-04-06 08:07 UTC | 2026-04-06 09:09 UTC | 1h 1m |
| SWR2647 | Swiss International | Indira Gandhi International Airport (VIDP) | UKFB (UKFB) | 2026-04-06 03:22 UTC | 2026-04-06 09:08 UTC | 5h 46m |
| FHRSJ | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-06 08:48 UTC | 2026-04-06 09:08 UTC | 20m |
| SEJ767 | SEJ | Netaji Subhash Chandra Bose International Airport (VECC) | Bengaluru International Airport (VOBL) | 2026-04-06 06:51 UTC | 2026-04-06 09:07 UTC | 2h 16m |
| SWE11U | SWE | Umea Airport (ESNU) | Kalixfors Airport (ESUK) | 2026-04-06 08:28 UTC | 2026-04-06 09:06 UTC | 38m |
| PHCOB | PHC | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-06 08:46 UTC | 2026-04-06 09:05 UTC | 18m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-04-06 08:54 UTC | 2026-04-06 09:03 UTC | 8m |
| QFA741 | Qantas | Sydney Kingsford Smith International Airport (YSSY) | Adelaide International Airport (YPAD) | 2026-04-06 07:08 UTC | 2026-04-06 08:56 UTC | 1h 48m |
| AAR333 | AAR | Incheon International Airport (RKSI) | Incheon International Airport (RKSI) | 2026-04-06 04:18 UTC | 2026-04-06 08:55 UTC | 4h 37m |
| RYR5413 | Ryanair | Marseille Provence Airport (LFML) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-06 06:57 UTC | 2026-04-06 08:55 UTC | 1h 57m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-04-06 07:57 UTC | 2026-04-06 08:51 UTC | 54m |
| AM324 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-04-06 08:27 UTC | 2026-04-06 08:51 UTC | 23m |
| RYR6101 | Ryanair | Alghero / Fertilia Airport (LIEA) | Decimomannu Airport (LIED) | 2026-04-06 08:32 UTC | 2026-04-06 08:49 UTC | 16m |
| QTR7R | Qatar Airways | Saiq Airport (OOSQ) | Al Udeid Air Base (OTBH) | 2026-04-06 07:36 UTC | 2026-04-06 08:46 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
