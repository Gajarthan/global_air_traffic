# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_15:49:00_UTC-green)

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

**Latest saved flight:** 2026-04-06 15:49:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 15:49:00 UTC

- **20,168** saved flights
- **10,098** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,168** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **253,551.5 tonnes** estimated CO2 emissions
- **14,698,640 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 862 |
| 2 | Ryanair | 837 |
| 3 | IndiGo | 577 |
| 4 | American Airlines | 382 |
| 5 | EJA | 370 |
| 6 | Southwest Airlines | 284 |
| 7 | ENY | 269 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 220 |
| 10 | LATAM Airlines | 213 |
| 11 | AXM | 197 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 176 |
| 14 | LXJ | 173 |
| 15 | QLK | 164 |
| 16 | AZU | 156 |
| 17 | Swiss International | 151 |
| 18 | VIV | 151 |
| 19 | easyJet | 138 |
| 20 | United Airlines | 135 |
| 21 | Japan Airlines | 134 |
| 22 | Alaska Airlines | 132 |
| 23 | Avianca | 132 |
| 24 | EJU | 131 |
| 25 | AEE | 126 |
| 26 | WIF | 123 |
| 27 | EDV | 119 |
| 28 | AXB | 118 |
| 29 | Air France | 110 |
| 30 | BRC | 106 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15653 |
| 2 | 🇮🇳 IN | 1761 |
| 3 | 🇪🇸 ES | 1628 |
| 4 | 🇦🇺 AU | 1409 |
| 5 | 🇧🇷 BR | 1162 |
| 6 | 🇨🇴 CO | 1098 |
| 7 | 🇯🇵 JP | 1090 |
| 8 | 🇩🇪 DE | 1020 |
| 9 | 🇮🇹 IT | 998 |
| 10 | 🇨🇦 CA | 873 |
| 11 | 🇬🇧 GB | 800 |
| 12 | 🇫🇷 FR | 746 |
| 13 | 🇲🇽 MX | 687 |
| 14 | 🇬🇷 GR | 577 |
| 15 | 🇨🇭 CH | 552 |
| 16 | 🇲🇾 MY | 463 |
| 17 | 🇬🇹 GT | 460 |
| 18 | 🇿🇦 ZA | 455 |
| 19 | 🇳🇴 NO | 423 |
| 20 | 🇳🇿 NZ | 416 |
| 21 | 🇹🇷 TR | 396 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 306 |
| 25 | 🇵🇱 PL | 297 |
| 26 | 🇲🇦 MA | 250 |
| 27 | 🇧🇸 BS | 221 |
| 28 | 🇮🇩 ID | 214 |
| 29 | 🇲🇪 ME | 214 |
| 30 | 🇳🇱 NL | 207 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 488 |
| 2 | El Dorado International Airport |  | CO | 418 |
| 3 | Tokyo International Airport |  | JP | 377 |
| 4 | Denver International Airport |  | US | 364 |
| 5 | Indira Gandhi International Airport |  | IN | 362 |
| 6 | La Aurora Airport |  | GT | 316 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 272 |
| 8 | Harry Reid International Airport |  | US | 262 |
| 9 | Zurich Airport |  | CH | 246 |
| 10 | Frankfurt am Main International Airport |  | DE | 235 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 218 |
| 12 | Chicago O'Hare International Airport |  | US | 213 |
| 13 | Guaymaral Airport |  | CO | 213 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Bengaluru International Airport |  | IN | 199 |
| 18 | Charlotte/Douglas International Airport |  | US | 193 |
| 19 | Madrid Barajas International Airport |  | ES | 189 |
| 20 | Tenerife Norte Airport |  | ES | 186 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 181 |
| 22 | Congonhas Airport |  | BR | 173 |
| 23 | Ninoy Aquino International Airport |  | PH | 172 |
| 24 | Kuala Lumpur International Airport |  | MY | 160 |
| 25 | Salt Lake City International Airport |  | US | 158 |
| 26 | Reno/Tahoe International Airport |  | US | 157 |
| 27 | Daniel K Inouye International Airport |  | US | 154 |
| 28 | Malpensa International Airport |  | IT | 153 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 152 |
| 30 | Charles de Gaulle International Airport |  | FR | 151 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 148 |
| 32 | Vitoria/Foronda Airport |  | ES | 145 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 142 |
| 34 | Miami International Airport |  | US | 141 |
| 35 | O. R. Tambo International Airport |  | ZA | 141 |
| 36 | Barcelona International Airport |  | ES | 136 |
| 37 | Pune Airport |  | IN | 135 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 132 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 90 | 14m | 114 km | 176.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 77 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 40 | 52m | 556 km | 383.4 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 38 | 13m | 99 km | 65.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 37 | 20m | 250 km | 159.8 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 32 | 12m | 15 km | 8.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 31 | 20m | 147 km | 78.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LYM717 | LYM | Denver International Airport (KDEN) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-04-06 14:57 UTC | 2026-04-06 15:49 UTC | 51m |
| RTY484 | RTY | Northern Colorado Regional Airport (KFNL) | 8CO0 (8CO0) | 2026-04-06 15:15 UTC | 2026-04-06 15:47 UTC | 32m |
| DECOY | DEC | Rendsburg-Schachtholm Airport (EDXR) | Kiel-Holtenau Airport (EDHK) | 2026-04-06 15:23 UTC | 2026-04-06 15:35 UTC | 11m |
| ERU59 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-06 14:53 UTC | 2026-04-06 15:31 UTC | 37m |
| BSM34 | BSM | OK44 (OK44) | OK44 (OK44) | 2026-04-06 15:31 UTC | 2026-04-06 15:31 UTC | 0m |
| N848AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-06 14:23 UTC | 2026-04-06 15:30 UTC | 1h 6m |
| N1572X |  | Raleigh-Durham International Airport (KRDU) | Triangle North Executive Airport (KLHZ) | 2026-04-06 14:45 UTC | 2026-04-06 15:28 UTC | 42m |
| N442EG |  | Fresno Yosemite International Airport (KFAT) | Santa Monica Municipal Airport (KSMO) | 2026-04-06 14:20 UTC | 2026-04-06 15:25 UTC | 1h 4m |
| N653PA |  | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-06 15:14 UTC | 2026-04-06 15:24 UTC | 10m |
| N551LX |  | Frederick Municipal Airport (KFDK) | PS25 (PS25) | 2026-04-06 15:13 UTC | 2026-04-06 15:24 UTC | 10m |
| PBD6544 | PBD | Koltsovo Airport (USSS) | Sheremetyevo International Airport (UUEE) | 2026-04-06 13:25 UTC | 2026-04-06 15:21 UTC | 1h 55m |
| N9965P |  | Addison Airport (KADS) | Mid-Way Regional Airport (KJWY) | 2026-04-06 14:58 UTC | 2026-04-06 15:21 UTC | 22m |
| FFL885 | FFL | Louisville Muhammad Ali International Airport (KSDF) | Juan Gualberto Gomez International Airport (MUVR) | 2026-04-06 13:23 UTC | 2026-04-06 15:17 UTC | 1h 54m |
| N2348K |  | UT99 (UT99) | KU42 (KU42) | 2026-04-06 14:44 UTC | 2026-04-06 15:17 UTC | 32m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-04-06 14:29 UTC | 2026-04-06 15:16 UTC | 46m |
| N858DT |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-04-06 14:34 UTC | 2026-04-06 15:14 UTC | 40m |
| N847EF |  | Phoenix Goodyear Airport (KGYR) | AZ86 (AZ86) | 2026-04-06 14:38 UTC | 2026-04-06 15:14 UTC | 35m |
| N719KX |  | Phoenix Deer Valley Airport (KDVT) | Lincoln Airport (KLNK) | 2026-04-06 13:18 UTC | 2026-04-06 15:12 UTC | 1h 54m |
| CGOSM | CGO | Oshawa Airport (CYOO) | Oshawa Airport (CYOO) | 2026-04-06 15:03 UTC | 2026-04-06 15:12 UTC | 8m |
| N276WE |  | Casper/Natrona County International Airport (KCPR) | Ohkay Owingeh Airport (KE14) | 2026-04-06 14:11 UTC | 2026-04-06 15:09 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
