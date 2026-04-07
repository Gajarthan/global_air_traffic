# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_21:48:58_UTC-green)

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

**Latest saved flight:** 2026-04-07 21:48:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 21:48:58 UTC

- **22,203** saved flights
- **10,952** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,203** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **275,367.2 tonnes** estimated CO2 emissions
- **15,963,314 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 953 |
| 2 | Ryanair | 929 |
| 3 | IndiGo | 622 |
| 4 | American Airlines | 416 |
| 5 | EJA | 412 |
| 6 | Southwest Airlines | 320 |
| 7 | ENY | 296 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 227 |
| 11 | AXM | 214 |
| 12 | All Nippon Airways | 193 |
| 13 | Delta Air Lines | 192 |
| 14 | LXJ | 188 |
| 15 | QLK | 184 |
| 16 | AZU | 173 |
| 17 | Swiss International | 162 |
| 18 | VIV | 159 |
| 19 | Alaska Airlines | 150 |
| 20 | easyJet | 149 |
| 21 | Japan Airlines | 148 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | WIF | 134 |
| 27 | EDV | 130 |
| 28 | AXB | 126 |
| 29 | Air France | 119 |
| 30 | Wizz Air | 114 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17525 |
| 2 | 🇮🇳 IN | 1897 |
| 3 | 🇪🇸 ES | 1739 |
| 4 | 🇦🇺 AU | 1557 |
| 5 | 🇧🇷 BR | 1256 |
| 6 | 🇯🇵 JP | 1212 |
| 7 | 🇨🇴 CO | 1179 |
| 8 | 🇮🇹 IT | 1128 |
| 9 | 🇩🇪 DE | 1108 |
| 10 | 🇨🇦 CA | 984 |
| 11 | 🇬🇧 GB | 882 |
| 12 | 🇫🇷 FR | 814 |
| 13 | 🇲🇽 MX | 734 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 604 |
| 16 | 🇲🇾 MY | 501 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇴 NO | 465 |
| 19 | 🇬🇹 GT | 465 |
| 20 | 🇳🇿 NZ | 446 |
| 21 | 🇹🇷 TR | 428 |
| 22 | 🇵🇭 PH | 413 |
| 23 | 🇰🇷 KR | 388 |
| 24 | 🇹🇭 TH | 349 |
| 25 | 🇵🇱 PL | 321 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 239 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 539 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 410 |
| 4 | Denver International Airport |  | US | 399 |
| 5 | Indira Gandhi International Airport |  | IN | 382 |
| 6 | La Aurora Airport |  | GT | 320 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 8 | Harry Reid International Airport |  | US | 295 |
| 9 | Zurich Airport |  | CH | 269 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 235 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 235 |
| 13 | Chicago O'Hare International Airport |  | US | 235 |
| 14 | Guaymaral Airport |  | CO | 234 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 217 |
| 16 | Bengaluru International Airport |  | IN | 214 |
| 17 | Charlotte/Douglas International Airport |  | US | 211 |
| 18 | Tenerife Norte Airport |  | ES | 202 |
| 19 | Macau International Airport |  | MO | 201 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 22 | Ninoy Aquino International Airport |  | PH | 189 |
| 23 | Congonhas Airport |  | BR | 184 |
| 24 | Salt Lake City International Airport |  | US | 178 |
| 25 | Kuala Lumpur International Airport |  | MY | 178 |
| 26 | Malpensa International Airport |  | IT | 174 |
| 27 | Reno/Tahoe International Airport |  | US | 173 |
| 28 | Daniel K Inouye International Airport |  | US | 172 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 169 |
| 30 | Charles de Gaulle International Airport |  | FR | 162 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 160 |
| 32 | Miami International Airport |  | US | 154 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 149 |
| 36 | Pune Airport |  | IN | 149 |
| 37 | Vitoria/Foronda Airport |  | ES | 147 |
| 38 | Barcelona International Airport |  | ES | 145 |
| 39 | Seattle-Tacoma International Airport |  | US | 142 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 139 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 103 | 1h 8m | 706 km | 1,254.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 86 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 61 | 1h 43m | 1,156 km | 1,216.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 51 | 19m | 165 km | 145.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 46 | 55m | 546 km | 433.1 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 44 | 31m | 369 km | 280.1 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N653PA |  | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-07 21:32 UTC | 2026-04-07 21:48 UTC | 16m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-07 20:23 UTC | 2026-04-07 21:48 UTC | 1h 25m |
| N838EF |  | Phoenix Goodyear Airport (KGYR) | North Las Vegas Airport (KVGT) | 2026-04-07 19:33 UTC | 2026-04-07 21:47 UTC | 2h 14m |
| WMT5PL | WMT | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-04-07 20:21 UTC | 2026-04-07 21:39 UTC | 1h 17m |
| N300LJ |  | Naples Municipal Airport (KAPF) | Sugar Loaf Shores Airport (7FA1) | 2026-04-07 21:19 UTC | 2026-04-07 21:37 UTC | 18m |
| N33RK |  | North Perry Airport (KHWO) | Orlando Executive Airport (KORL) | 2026-04-07 19:34 UTC | 2026-04-07 21:35 UTC | 2h 0m |
| KEEN81 | KEE | Danaher Airport (7TX0) | 2XA0 (2XA0) | 2026-04-07 21:12 UTC | 2026-04-07 21:33 UTC | 20m |
| N54474 |  | Hopkinsville-Christian County Airport (KHVC) | Lake Barkley State Park Airport (K1M9) | 2026-04-07 21:19 UTC | 2026-04-07 21:31 UTC | 12m |
| PAT100 | PAT | Reno/Tahoe International Airport (KRNO) | Nellis Afb Airport (KLSV) | 2026-04-07 20:17 UTC | 2026-04-07 21:28 UTC | 1h 11m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-07 17:11 UTC | 2026-04-07 21:25 UTC | 4h 13m |
| SCA43 | SCA | Scottsdale Airport (KSDL) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-04-07 20:26 UTC | 2026-04-07 21:20 UTC | 53m |
| N103DS |  | St Pete-Clearwater International Airport (KPIE) | Flying X Ranch Airport (5AL3) | 2026-04-07 20:10 UTC | 2026-04-07 21:18 UTC | 1h 7m |
| N6089F |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-04-07 19:58 UTC | 2026-04-07 21:15 UTC | 1h 17m |
| N8158P |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-04-07 21:13 UTC | 2026-04-07 21:13 UTC | 0m |
| N563BB |  | Dallas Love Field (KDAL) | KL64 (KL64) | 2026-04-07 18:54 UTC | 2026-04-07 21:13 UTC | 2h 18m |
| N878EM |  | Mc Clellan-Palomar Airport (KCRQ) | Hayward Executive Airport (KHWD) | 2026-04-07 20:09 UTC | 2026-04-07 21:12 UTC | 1h 3m |
| VAR520 | VAR | Gene Wash Reservoir Airport (5CL7) | Lake Havasu City Airport (KHII) | 2026-04-07 21:01 UTC | 2026-04-07 21:10 UTC | 8m |
| N913TF |  | Aiken Regional Airport (KAIK) | Montvale Airpark (TN87) | 2026-04-07 20:41 UTC | 2026-04-07 21:09 UTC | 28m |
| C2309 |  | Cape Cod Coast Guard Air Station (KFMH) | Cape Cod Coast Guard Air Station (KFMH) | 2026-04-07 19:30 UTC | 2026-04-07 21:08 UTC | 1h 38m |
| N747AU |  | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-04-07 20:25 UTC | 2026-04-07 21:07 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
