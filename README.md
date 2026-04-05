# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_17:18:14_UTC-green)

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

**Latest saved flight:** 2026-04-05 17:18:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 17:18:14 UTC

- **18,397** saved flights
- **9,386** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,397** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **232,900.5 tonnes** estimated CO2 emissions
- **13,501,481 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 781 |
| 2 | Ryanair | 757 |
| 3 | IndiGo | 537 |
| 4 | American Airlines | 334 |
| 5 | EJA | 331 |
| 6 | Southwest Airlines | 256 |
| 7 | Lufthansa | 255 |
| 8 | ENY | 245 |
| 9 | Vueling | 203 |
| 10 | LATAM Airlines | 195 |
| 11 | AXM | 191 |
| 12 | All Nippon Airways | 161 |
| 13 | Delta Air Lines | 157 |
| 14 | LXJ | 156 |
| 15 | QLK | 154 |
| 16 | AZU | 140 |
| 17 | Swiss International | 140 |
| 18 | VIV | 135 |
| 19 | Alaska Airlines | 124 |
| 20 | Japan Airlines | 124 |
| 21 | easyJet | 121 |
| 22 | AEE | 120 |
| 23 | Avianca | 120 |
| 24 | United Airlines | 119 |
| 25 | EJU | 117 |
| 26 | AXB | 113 |
| 27 | WIF | 112 |
| 28 | EDV | 111 |
| 29 | Cathay Pacific | 105 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14262 |
| 2 | 🇮🇳 IN | 1631 |
| 3 | 🇪🇸 ES | 1530 |
| 4 | 🇦🇺 AU | 1312 |
| 5 | 🇧🇷 BR | 1067 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 967 |
| 8 | 🇩🇪 DE | 949 |
| 9 | 🇮🇹 IT | 876 |
| 10 | 🇨🇦 CA | 797 |
| 11 | 🇬🇧 GB | 720 |
| 12 | 🇫🇷 FR | 686 |
| 13 | 🇲🇽 MX | 618 |
| 14 | 🇬🇷 GR | 532 |
| 15 | 🇨🇭 CH | 497 |
| 16 | 🇲🇾 MY | 437 |
| 17 | 🇿🇦 ZA | 407 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇬🇹 GT | 388 |
| 20 | 🇳🇴 NO | 374 |
| 21 | 🇵🇭 PH | 355 |
| 22 | 🇹🇷 TR | 351 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 272 |
| 26 | 🇲🇦 MA | 233 |
| 27 | 🇮🇩 ID | 205 |
| 28 | 🇧🇸 BS | 202 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 436 |
| 2 | El Dorado International Airport |  | CO | 368 |
| 3 | Indira Gandhi International Airport |  | IN | 342 |
| 4 | Tokyo International Airport |  | JP | 340 |
| 5 | Denver International Airport |  | US | 334 |
| 6 | La Aurora Airport |  | GT | 271 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 252 |
| 8 | Harry Reid International Airport |  | US | 237 |
| 9 | Frankfurt am Main International Airport |  | DE | 228 |
| 10 | Zurich Airport |  | CH | 228 |
| 11 | Macau International Airport |  | MO | 198 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 194 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 192 |
| 14 | Guaymaral Airport |  | CO | 192 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 16 | Bengaluru International Airport |  | IN | 181 |
| 17 | Chicago O'Hare International Airport |  | US | 180 |
| 18 | Madrid Barajas International Airport |  | ES | 179 |
| 19 | Charlotte/Douglas International Airport |  | US | 174 |
| 20 | Tenerife Norte Airport |  | ES | 170 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 162 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 160 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Daniel K Inouye International Airport |  | US | 146 |
| 26 | Salt Lake City International Airport |  | US | 146 |
| 27 | Vitoria/Foronda Airport |  | ES | 143 |
| 28 | Malpensa International Airport |  | IT | 142 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 139 |
| 30 | Reno/Tahoe International Airport |  | US | 138 |
| 31 | Charles de Gaulle International Airport |  | FR | 138 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 137 |
| 33 | Miami International Airport |  | US | 129 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 128 |
| 35 | Barcelona International Airport |  | ES | 127 |
| 36 | Pune Airport |  | IN | 126 |
| 37 | O. R. Tambo International Airport |  | ZA | 125 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 120 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 40 | Seattle-Tacoma International Airport |  | US | 116 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 82 | 14m | 114 km | 160.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 72 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 58 | 27m | 152 km | 151.6 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 54 | 1h 44m | 1,156 km | 1,077.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 52 | 22m | 99 km | 89.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 39 | 1h 54m | 1,304 km | 877.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 38 | 52m | 556 km | 364.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 35 | 9m | - | - |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 30 | 17m | 183 km | 94.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 30 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 29 | 30m | 114 km | 57.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKALT | OKA | Bolzano Airport (LIPB) | Brno-Turany Airport (LKTB) | 2026-04-05 16:06 UTC | 2026-04-05 17:18 UTC | 1h 11m |
| MSR788 | EgyptAir | Munich International Airport (EDDM) | HE42 (HE42) | 2026-04-05 14:08 UTC | 2026-04-05 17:10 UTC | 3h 2m |
| N7882N |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-05 16:40 UTC | 2026-04-05 17:09 UTC | 28m |
| SPIKR18 | SPI | Destin Executive Airport (KDTS) | 68LA (68LA) | 2026-04-05 16:07 UTC | 2026-04-05 17:01 UTC | 54m |
| NJE663V | NJE | Eleftherios Venizelos International Airport (LGAV) | Payerne Airport (LSMP) | 2026-04-05 14:42 UTC | 2026-04-05 16:58 UTC | 2h 15m |
| LXJ366 | LXJ | Hammond Northshore Regional Airport (KHDC) | AL02 (AL02) | 2026-04-05 16:20 UTC | 2026-04-05 16:54 UTC | 34m |
| FHRIV | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-05 16:31 UTC | 2026-04-05 16:52 UTC | 20m |
| N145UA |  | North Fork Valley Airport (K7V2) | CD97 (CD97) | 2026-04-05 16:34 UTC | 2026-04-05 16:45 UTC | 11m |
| N577ND |  | Oxnard Airport (KOXR) | Meadows Field (KBFL) | 2026-04-05 15:49 UTC | 2026-04-05 16:45 UTC | 56m |
| SEH4VS | SEH | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-05 15:54 UTC | 2026-04-05 16:42 UTC | 48m |
| N182HE |  | Orlando Apopka Airport (KX04) | Market World Airport (FL16) | 2026-04-05 16:02 UTC | 2026-04-05 16:39 UTC | 37m |
| N786B |  | Mclendon Field (GE04) | Laurence G Hanscom Field (KBED) | 2026-04-05 14:24 UTC | 2026-04-05 16:34 UTC | 2h 9m |
| N6776A |  | Spokane International Airport (KGEG) | Rugg Ranches Airport (45OG) | 2026-04-05 15:19 UTC | 2026-04-05 16:34 UTC | 1h 14m |
| N909BJ |  | St Pete-Clearwater International Airport (KPIE) | Sylvanmir Farms Airport (6FL4) | 2026-04-05 15:58 UTC | 2026-04-05 16:33 UTC | 35m |
| N273ND |  | Purdue University Airport (KLAF) | Hartman Farms Field (53IN) | 2026-04-05 16:15 UTC | 2026-04-05 16:32 UTC | 17m |
| FFT1408 | FFT | Hartsfield/Jackson Atlanta International Airport (KATL) | Buffalo Niagara International Airport (KBUF) | 2026-04-05 15:03 UTC | 2026-04-05 16:31 UTC | 1h 28m |
| RYR6FR | Ryanair | Palermo / Punta Raisi Airport (LICJ) | Napoli / Capodichino International Airport (LIRN) | 2026-04-05 16:04 UTC | 2026-04-05 16:30 UTC | 25m |
| N142EB |  | Tigerbird Field (2TS3) | 1CO7 (1CO7) | 2026-04-05 14:09 UTC | 2026-04-05 16:28 UTC | 2h 19m |
| IGO601M | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-04-05 14:45 UTC | 2026-04-05 16:28 UTC | 1h 43m |
| UAL1095 | United Airlines | Washington Dulles International Airport (KIAD) | San Francisco International Airport (KSFO) | 2026-04-05 10:42 UTC | 2026-04-05 16:24 UTC | 5h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
