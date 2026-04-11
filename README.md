# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_16:41:36_UTC-green)

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

**Latest saved flight:** 2026-04-11 16:41:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 16:41:36 UTC

- **29,085** saved flights
- **13,497** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,085** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **353,937.5 tonnes** estimated CO2 emissions
- **20,518,118 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1196 |
| 2 | SkyWest Airlines | 1163 |
| 3 | IndiGo | 766 |
| 4 | EJA | 506 |
| 5 | American Airlines | 500 |
| 6 | Southwest Airlines | 411 |
| 7 | ENY | 386 |
| 8 | Lufthansa | 355 |
| 9 | AXM | 314 |
| 10 | Vueling | 300 |
| 11 | LATAM Airlines | 283 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | AZU | 251 |
| 15 | Delta Air Lines | 243 |
| 16 | LXJ | 233 |
| 17 | Swiss International | 214 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 190 |
| 20 | EJU | 189 |
| 21 | VIV | 189 |
| 22 | easyJet | 188 |
| 23 | WIF | 187 |
| 24 | AEE | 182 |
| 25 | United Airlines | 174 |
| 26 | EDV | 168 |
| 27 | Avianca | 163 |
| 28 | JetBlue | 155 |
| 29 | AXB | 153 |
| 30 | Air France | 152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22839 |
| 2 | 🇮🇳 IN | 2355 |
| 3 | 🇪🇸 ES | 2154 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1670 |
| 6 | 🇯🇵 JP | 1608 |
| 7 | 🇮🇹 IT | 1493 |
| 8 | 🇩🇪 DE | 1478 |
| 9 | 🇨🇴 CO | 1457 |
| 10 | 🇨🇦 CA | 1422 |
| 11 | 🇬🇧 GB | 1173 |
| 12 | 🇫🇷 FR | 1080 |
| 13 | 🇲🇽 MX | 928 |
| 14 | 🇨🇭 CH | 831 |
| 15 | 🇬🇷 GR | 831 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 607 |
| 20 | 🇵🇭 PH | 547 |
| 21 | 🇬🇹 GT | 535 |
| 22 | 🇹🇭 TH | 532 |
| 23 | 🇹🇷 TR | 526 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 440 |
| 26 | 🇲🇦 MA | 364 |
| 27 | 🇧🇸 BS | 308 |
| 28 | 🇲🇪 ME | 293 |
| 29 | 🇳🇱 NL | 284 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 684 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 522 |
| 4 | Indira Gandhi International Airport |  | IN | 491 |
| 5 | Denver International Airport |  | US | 483 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 405 |
| 7 | La Aurora Airport |  | GT | 379 |
| 8 | Harry Reid International Airport |  | US | 369 |
| 9 | Zurich Airport |  | CH | 351 |
| 10 | Guaymaral Airport |  | CO | 336 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 300 |
| 12 | Frankfurt am Main International Airport |  | DE | 298 |
| 13 | Chicago O'Hare International Airport |  | US | 296 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 292 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 269 |
| 18 | Bengaluru International Airport |  | IN | 267 |
| 19 | Charlotte/Douglas International Airport |  | US | 261 |
| 20 | Madrid Barajas International Airport |  | ES | 254 |
| 21 | Ninoy Aquino International Airport |  | PH | 251 |
| 22 | Tenerife Norte Airport |  | ES | 251 |
| 23 | Congonhas Airport |  | BR | 242 |
| 24 | Malpensa International Airport |  | IT | 228 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 226 |
| 26 | Salt Lake City International Airport |  | US | 222 |
| 27 | Daniel K Inouye International Airport |  | US | 220 |
| 28 | Reno/Tahoe International Airport |  | US | 212 |
| 29 | Charles de Gaulle International Airport |  | FR | 207 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 201 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 196 |
| 33 | Capua Airport |  | IT | 196 |
| 34 | O. R. Tambo International Airport |  | ZA | 193 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 193 |
| 36 | Miami International Airport |  | US | 192 |
| 37 | Vitoria/Foronda Airport |  | ES | 185 |
| 38 | Barcelona International Airport |  | ES | 185 |
| 39 | Seattle-Tacoma International Airport |  | US | 182 |
| 40 | Don Mueang International Airport |  | TH | 179 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 129 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 119 | 14m | 114 km | 233.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 60 | 27m | 275 km | 284.3 t |
| 15 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 59 | 9m | - | - |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 52 | 52m | 556 km | 498.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 24 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 45 | 21m | 244 km | 189.5 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 41 | 1h 19m | 961 km | 679.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 40 | 12m | 15 km | 10.6 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DWI6021 | DWI | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Cancun International Airport (MMUN) | 2026-04-11 04:40 UTC | 2026-04-11 16:41 UTC | 12h 1m |
| N916ET |  | Atlanta Regional Falcon Field (KFFC) | Fagundes Field (6GA1) | 2026-04-11 16:07 UTC | 2026-04-11 16:39 UTC | 31m |
| N619BL |  | Gerald R Ford International Airport (KGRR) | Cherry Capital Airport (KTVC) | 2026-04-11 12:51 UTC | 2026-04-11 16:36 UTC | 3h 44m |
| CXK531 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-11 16:21 UTC | 2026-04-11 16:30 UTC | 9m |
| N523RH |  | Danbury Municipal Airport (KDXR) | Linden Airport (KLDJ) | 2026-04-11 15:54 UTC | 2026-04-11 16:30 UTC | 35m |
| NWX251 | NWX | Aero Valley Airport (K52F) | Aero Valley Airport (K52F) | 2026-04-11 15:50 UTC | 2026-04-11 16:28 UTC | 38m |
| N307DM |  | Mc Clellan-Palomar Airport (KCRQ) | Bermuda Dunes Airport (KUDD) | 2026-04-11 16:00 UTC | 2026-04-11 16:28 UTC | 28m |
| GPD437 | GPD | Adirondack Regional Airport (KSLK) | Tweed/New Haven Airport (KHVN) | 2026-04-11 15:37 UTC | 2026-04-11 16:27 UTC | 50m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-11 16:11 UTC | 2026-04-11 16:26 UTC | 15m |
| N825PR |  | Mc Clellan-Palomar Airport (KCRQ) | Jacqueline Cochran Regional Airport (KTRM) | 2026-04-11 16:03 UTC | 2026-04-11 16:20 UTC | 17m |
| HKC9492 | HKC | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-04-11 04:40 UTC | 2026-04-11 16:19 UTC | 11h 38m |
| SCA18 | SCA | Chandler Municipal Airport (KCHD) | Payson Airport (KPAN) | 2026-04-11 15:27 UTC | 2026-04-11 16:19 UTC | 51m |
| N172WN |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | 83MU (83MU) | 2026-04-11 15:50 UTC | 2026-04-11 16:17 UTC | 27m |
| AFL1315 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-10 17:08 UTC | 2026-04-11 16:14 UTC | 23h 5m |
| N18KN |  | Gwinnett County/Briscoe Field (KLZU) | 0GA4 (0GA4) | 2026-04-11 15:59 UTC | 2026-04-11 16:14 UTC | 14m |
| N2074A |  | French Valley Airport (KF70) | Hemet-Ryan Airport (KHMT) | 2026-04-11 15:55 UTC | 2026-04-11 16:13 UTC | 17m |
| N51CU |  | 2GE3 (2GE3) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-11 15:02 UTC | 2026-04-11 16:11 UTC | 1h 8m |
| CFDYL | CFD | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-04-11 15:45 UTC | 2026-04-11 16:11 UTC | 26m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-04-11 16:01 UTC | 2026-04-11 16:11 UTC | 10m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-04-11 15:00 UTC | 2026-04-11 16:10 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
