# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_19:40:23_UTC-green)

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

**Latest saved flight:** 2026-04-10 19:40:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 19:40:23 UTC

- **27,551** saved flights
- **12,976** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,551** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **335,561.4 tonnes** estimated CO2 emissions
- **19,452,837 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1128 |
| 2 | SkyWest Airlines | 1121 |
| 3 | IndiGo | 733 |
| 4 | EJA | 489 |
| 5 | American Airlines | 485 |
| 6 | Southwest Airlines | 389 |
| 7 | ENY | 369 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 282 |
| 11 | LATAM Airlines | 270 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 232 |
| 15 | AZU | 226 |
| 16 | LXJ | 226 |
| 17 | Swiss International | 194 |
| 18 | Alaska Airlines | 184 |
| 19 | easyJet | 179 |
| 20 | VIV | 179 |
| 21 | WIF | 179 |
| 22 | AEE | 178 |
| 23 | EJU | 177 |
| 24 | Japan Airlines | 177 |
| 25 | United Airlines | 165 |
| 26 | EDV | 162 |
| 27 | Avianca | 156 |
| 28 | AXB | 147 |
| 29 | JetBlue | 147 |
| 30 | PGT | 142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21782 |
| 2 | 🇮🇳 IN | 2249 |
| 3 | 🇪🇸 ES | 2039 |
| 4 | 🇦🇺 AU | 1996 |
| 5 | 🇧🇷 BR | 1554 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇩🇪 DE | 1390 |
| 8 | 🇮🇹 IT | 1387 |
| 9 | 🇨🇴 CO | 1384 |
| 10 | 🇨🇦 CA | 1327 |
| 11 | 🇬🇧 GB | 1111 |
| 12 | 🇫🇷 FR | 1021 |
| 13 | 🇲🇽 MX | 874 |
| 14 | 🇬🇷 GR | 799 |
| 15 | 🇨🇭 CH | 753 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇴 NO | 602 |
| 18 | 🇳🇿 NZ | 602 |
| 19 | 🇿🇦 ZA | 566 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 507 |
| 22 | 🇬🇹 GT | 506 |
| 23 | 🇹🇭 TH | 480 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 418 |
| 26 | 🇲🇦 MA | 339 |
| 27 | 🇧🇸 BS | 294 |
| 28 | 🇲🇪 ME | 276 |
| 29 | 🇳🇱 NL | 269 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 656 |
| 2 | El Dorado International Airport |  | CO | 503 |
| 3 | Tokyo International Airport |  | JP | 500 |
| 4 | Indira Gandhi International Airport |  | IN | 466 |
| 5 | Denver International Airport |  | US | 461 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 389 |
| 7 | Harry Reid International Airport |  | US | 353 |
| 8 | La Aurora Airport |  | GT | 353 |
| 9 | Zurich Airport |  | CH | 325 |
| 10 | Guaymaral Airport |  | CO | 307 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 291 |
| 12 | Chicago O'Hare International Airport |  | US | 289 |
| 13 | Frankfurt am Main International Airport |  | DE | 289 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 282 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Charlotte/Douglas International Airport |  | US | 251 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Madrid Barajas International Airport |  | ES | 235 |
| 22 | Tenerife Norte Airport |  | ES | 235 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 217 |
| 24 | Congonhas Airport |  | BR | 217 |
| 25 | Malpensa International Airport |  | IT | 215 |
| 26 | Salt Lake City International Airport |  | US | 214 |
| 27 | Daniel K Inouye International Airport |  | US | 209 |
| 28 | Reno/Tahoe International Airport |  | US | 200 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 190 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 186 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 33 | Miami International Airport |  | US | 184 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 183 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Barcelona International Airport |  | ES | 175 |
| 37 | Vitoria/Foronda Airport |  | ES | 174 |
| 38 | Seattle-Tacoma International Airport |  | US | 173 |
| 39 | Capua Airport |  | IT | 173 |
| 40 | Don Mueang International Airport |  | TH | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 117 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 112 | 14m | 114 km | 219.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 72 | 21m | 99 km | 123.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 49 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 48 | 52m | 556 km | 460.1 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 44 | 13m | 99 km | 75.4 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4032L |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-04-10 18:31 UTC | 2026-04-10 19:40 UTC | 1h 8m |
| JPR12 | JPR | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-10 18:27 UTC | 2026-04-10 19:38 UTC | 1h 11m |
| N330DB |  | Portland-Hillsboro Airport (KHIO) | Mcnary Field (KSLE) | 2026-04-10 19:18 UTC | 2026-04-10 19:37 UTC | 18m |
| NJM888 | NJM | Witham Field (KSUA) | Aiken Regional Airport (KAIK) | 2026-04-10 18:14 UTC | 2026-04-10 19:32 UTC | 1h 18m |
| N784LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-04-10 18:47 UTC | 2026-04-10 19:30 UTC | 42m |
| PRE31 | PRE | Centennial Airport (KAPA) | Torrington Municipal Airport (KTOR) | 2026-04-10 18:57 UTC | 2026-04-10 19:28 UTC | 31m |
| N125CL |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-04-10 18:59 UTC | 2026-04-10 19:24 UTC | 25m |
| KING87 | KIN | KGBN (KGBN) | Davis Monthan Afb Airport (KDMA) | 2026-04-10 18:18 UTC | 2026-04-10 19:24 UTC | 1h 6m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-04-10 18:28 UTC | 2026-04-10 19:20 UTC | 51m |
| JSX9001 | JSX | John Wayne/Orange County Airport (KSNA) | Alpine-Casparis Municipal Airport (KE38) | 2026-04-10 17:31 UTC | 2026-04-10 19:18 UTC | 1h 47m |
| N600CA |  | Atkinson Municipal Airport (KPTS) | Colonel James Jabara Airport (KAAO) | 2026-04-10 18:41 UTC | 2026-04-10 19:18 UTC | 37m |
| OAL053 | OAL | Dionysios Solomos Airport (LGZA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-10 18:33 UTC | 2026-04-10 19:15 UTC | 41m |
| EJA828 | EJA | Oakland County International Airport (KPTK) | Clearfield-Lawrence Airport (KFIG) | 2026-04-10 18:39 UTC | 2026-04-10 19:13 UTC | 33m |
| N198ED |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-10 18:45 UTC | 2026-04-10 19:12 UTC | 27m |
| N298RD |  | 4MI3 (4MI3) | Orlando Executive Airport (KORL) | 2026-04-10 17:08 UTC | 2026-04-10 19:12 UTC | 2h 4m |
| TWY281 | TWY | Santa Barbara Municipal Airport (KSBA) | Truckee-Tahoe Airport (KTRK) | 2026-04-10 18:22 UTC | 2026-04-10 19:09 UTC | 47m |
| N737AV |  | Phoenix Goodyear Airport (KGYR) | Montezuma Airport (19AZ) | 2026-04-10 18:31 UTC | 2026-04-10 19:08 UTC | 37m |
| EJA436 | EJA | Sacramento International Airport (KSMF) | Bermuda Dunes Airport (KUDD) | 2026-04-10 18:00 UTC | 2026-04-10 19:08 UTC | 1h 7m |
| VAR630 | VAR | Phoenix Goodyear Airport (KGYR) | 13AZ (13AZ) | 2026-04-10 17:47 UTC | 2026-04-10 19:06 UTC | 1h 19m |
| VTE3539 | VTE | Chicago O'Hare International Airport (KORD) | Rolla Ntl Airport (KVIH) | 2026-04-10 18:13 UTC | 2026-04-10 19:05 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
