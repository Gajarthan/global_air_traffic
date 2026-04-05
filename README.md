# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_23:03:07_UTC-green)

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

**Latest saved flight:** 2026-04-05 23:03:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 23:03:07 UTC

- **19,206** saved flights
- **9,730** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,206** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **242,704.2 tonnes** estimated CO2 emissions
- **14,069,807 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 844 |
| 2 | Ryanair | 789 |
| 3 | IndiGo | 540 |
| 4 | American Airlines | 369 |
| 5 | EJA | 361 |
| 6 | Southwest Airlines | 278 |
| 7 | ENY | 263 |
| 8 | Lufthansa | 256 |
| 9 | Vueling | 210 |
| 10 | LATAM Airlines | 204 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 170 |
| 13 | LXJ | 169 |
| 14 | All Nippon Airways | 161 |
| 15 | QLK | 156 |
| 16 | AZU | 149 |
| 17 | VIV | 145 |
| 18 | Swiss International | 142 |
| 19 | United Airlines | 131 |
| 20 | Alaska Airlines | 130 |
| 21 | Avianca | 128 |
| 22 | easyJet | 124 |
| 23 | Japan Airlines | 124 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | EDV | 117 |
| 27 | WIF | 116 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15155 |
| 2 | 🇮🇳 IN | 1638 |
| 3 | 🇪🇸 ES | 1569 |
| 4 | 🇦🇺 AU | 1326 |
| 5 | 🇧🇷 BR | 1117 |
| 6 | 🇨🇴 CO | 1042 |
| 7 | 🇯🇵 JP | 1000 |
| 8 | 🇩🇪 DE | 966 |
| 9 | 🇮🇹 IT | 908 |
| 10 | 🇨🇦 CA | 851 |
| 11 | 🇬🇧 GB | 744 |
| 12 | 🇫🇷 FR | 700 |
| 13 | 🇲🇽 MX | 665 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 505 |
| 16 | 🇬🇹 GT | 448 |
| 17 | 🇲🇾 MY | 441 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 406 |
| 20 | 🇳🇴 NO | 391 |
| 21 | 🇹🇷 TR | 369 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 326 |
| 24 | 🇵🇱 PL | 278 |
| 25 | 🇹🇭 TH | 274 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 474 |
| 2 | El Dorado International Airport |  | CO | 397 |
| 3 | Denver International Airport |  | US | 356 |
| 4 | Indira Gandhi International Airport |  | IN | 343 |
| 5 | Tokyo International Airport |  | JP | 341 |
| 6 | La Aurora Airport |  | GT | 307 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 253 |
| 9 | Zurich Airport |  | CH | 233 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 210 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 208 |
| 13 | Chicago O'Hare International Airport |  | US | 205 |
| 14 | Guaymaral Airport |  | CO | 200 |
| 15 | Macau International Airport |  | MO | 198 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 193 |
| 17 | Charlotte/Douglas International Airport |  | US | 188 |
| 18 | Madrid Barajas International Airport |  | ES | 184 |
| 19 | Bengaluru International Airport |  | IN | 182 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 175 |
| 21 | Tenerife Norte Airport |  | ES | 174 |
| 22 | Congonhas Airport |  | BR | 165 |
| 23 | Ninoy Aquino International Airport |  | PH | 162 |
| 24 | Salt Lake City International Airport |  | US | 155 |
| 25 | Kuala Lumpur International Airport |  | MY | 155 |
| 26 | Daniel K Inouye International Airport |  | US | 153 |
| 27 | Reno/Tahoe International Airport |  | US | 150 |
| 28 | Malpensa International Airport |  | IT | 146 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Charles de Gaulle International Airport |  | FR | 143 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 143 |
| 32 | Miami International Airport |  | US | 140 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 131 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 130 |
| 36 | Barcelona International Airport |  | ES | 130 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 128 |
| 38 | Pune Airport |  | IN | 128 |
| 39 | O. R. Tambo International Airport |  | ZA | 127 |
| 40 | Seattle-Tacoma International Airport |  | US | 121 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 87 | 14m | 114 km | 170.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 66 | 22m | 99 km | 113.1 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 41 | 1h 12m | 770 km | 544.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 35 | 30m | 114 km | 68.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXS8SD | SXS | Antalya International Airport (LTAI) | Lublin Radwiec Airport (EPLR) | 2026-04-05 20:31 UTC | 2026-04-05 23:03 UTC | 2h 31m |
| DBB | DBB | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-05 22:26 UTC | 2026-04-05 22:44 UTC | 18m |
| N950TT |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-04-05 22:30 UTC | 2026-04-05 22:42 UTC | 12m |
| KEN75 | KEN | Portland-Hillsboro Airport (KHIO) | Boeing Field/King County International Airport (KBFI) | 2026-04-05 21:58 UTC | 2026-04-05 22:40 UTC | 41m |
| AAL3128 | American Airlines | Tucson International Airport (KTUS) | Chicago O'Hare International Airport (KORD) | 2026-04-05 19:36 UTC | 2026-04-05 22:35 UTC | 2h 59m |
| CKK206 | CKK | Amsterdam Airport Schiphol (EHAM) | Sharypovo Airport (UNKO) | 2026-04-05 17:07 UTC | 2026-04-05 22:35 UTC | 5h 28m |
| AAL2458 | American Airlines | Harry Reid International Airport (KLAS) | Chicago O'Hare International Airport (KORD) | 2026-04-05 19:28 UTC | 2026-04-05 22:34 UTC | 3h 6m |
| TGMRP | TGM | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-04-05 22:04 UTC | 2026-04-05 22:33 UTC | 29m |
| N770BD |  | Forest Lake Airport (K25D) | 73MN (73MN) | 2026-04-05 21:33 UTC | 2026-04-05 22:32 UTC | 59m |
| WEN3705 | WEN | Edmonton / Gartner Airport (CFQ7) | Vernon Airport (CYVK) | 2026-04-05 21:31 UTC | 2026-04-05 22:31 UTC | 59m |
| WUP652 | WUP | Auburn University Regional Airport (KAUO) | Orlando Executive Airport (KORL) | 2026-04-05 21:30 UTC | 2026-04-05 22:30 UTC | 59m |
| ARR950 | ARR | Teterboro Airport (KTEB) | Austin-Bergstrom International Airport (KAUS) | 2026-04-05 18:32 UTC | 2026-04-05 22:29 UTC | 3h 56m |
| N42EX |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-04-05 22:13 UTC | 2026-04-05 22:28 UTC | 15m |
| N118RK |  | SN07 (SN07) | Morrilton Airport (07AR) | 2026-04-05 22:06 UTC | 2026-04-05 22:26 UTC | 20m |
| TWY17 | TWY | Manchester Boston Regional Airport (KMHT) | Lebanon Municipal Airport (KLEB) | 2026-04-05 22:00 UTC | 2026-04-05 22:24 UTC | 24m |
| N4386K |  | Mojave Air & Space Port/Rutan Field (KMHV) | Mojave Air & Space Port/Rutan Field (KMHV) | 2026-04-05 22:05 UTC | 2026-04-05 22:18 UTC | 13m |
| LXJ617 | LXJ | Dallas-Fort Worth International Airport (KDFW) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-05 18:59 UTC | 2026-04-05 22:17 UTC | 3h 17m |
| N978TC |  | William P Hobby Airport (KHOU) | 5XS3 (5XS3) | 2026-04-05 22:03 UTC | 2026-04-05 22:16 UTC | 13m |
| N28641 |  | Petaluma Municipal Airport (KO69) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-05 21:41 UTC | 2026-04-05 22:12 UTC | 30m |
| N55GP |  | Dane County Regional/Truax Field (KMSN) | Worcester Regional Airport (KORH) | 2026-04-05 20:22 UTC | 2026-04-05 22:10 UTC | 1h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
