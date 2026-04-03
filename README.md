# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_11:46:15_UTC-green)

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

**Latest saved flight:** 2026-04-03 11:46:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 11:46:15 UTC

- **13,111** saved flights
- **7,343** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,111** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **163,223.5 tonnes** estimated CO2 emissions
- **9,462,234 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 498 |
| 3 | IndiGo | 372 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 204 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 138 |
| 10 | AXM | 137 |
| 11 | LATAM Airlines | 132 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 102 |
| 16 | Swiss International | 101 |
| 17 | WIF | 97 |
| 18 | AZU | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Japan Airlines | 87 |
| 22 | AXB | 86 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 81 |
| 26 | EDV | 78 |
| 27 | EJU | 78 |
| 28 | AEE | 73 |
| 29 | ANZ | 72 |
| 30 | BRC | 72 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10375 |
| 2 | 🇮🇳 IN | 1146 |
| 3 | 🇦🇺 AU | 1076 |
| 4 | 🇪🇸 ES | 1003 |
| 5 | 🇧🇷 BR | 723 |
| 6 | 🇯🇵 JP | 716 |
| 7 | 🇩🇪 DE | 705 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 606 |
| 10 | 🇮🇹 IT | 581 |
| 11 | 🇬🇧 GB | 497 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 441 |
| 14 | 🇬🇷 GR | 340 |
| 15 | 🇨🇭 CH | 339 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 311 |
| 18 | 🇳🇴 NO | 305 |
| 19 | 🇿🇦 ZA | 269 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 239 |
| 22 | 🇰🇷 KR | 235 |
| 23 | 🇬🇹 GT | 234 |
| 24 | 🇵🇱 PL | 185 |
| 25 | 🇹🇭 TH | 173 |
| 26 | 🇮🇩 ID | 162 |
| 27 | 🇲🇴 MO | 156 |
| 28 | 🇲🇦 MA | 155 |
| 29 | 🇲🇪 ME | 135 |
| 30 | 🇳🇱 NL | 132 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 251 |
| 3 | Indira Gandhi International Airport |  | IN | 245 |
| 4 | Denver International Airport |  | US | 233 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 193 |
| 7 | Harry Reid International Airport |  | US | 179 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Zurich Airport |  | CH | 160 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 156 |
| 12 | Macau International Airport |  | MO | 156 |
| 13 | Guaymaral Airport |  | CO | 153 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Bengaluru International Airport |  | IN | 128 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 121 |
| 19 | Madrid Barajas International Airport |  | ES | 117 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 21 | Kuala Lumpur International Airport |  | MY | 114 |
| 22 | Charlotte/Douglas International Airport |  | US | 112 |
| 23 | Congonhas Airport |  | BR | 111 |
| 24 | Tenerife Norte Airport |  | ES | 108 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 104 |
| 26 | Salt Lake City International Airport |  | US | 98 |
| 27 | Daniel K Inouye International Airport |  | US | 97 |
| 28 | Reno/Tahoe International Airport |  | US | 97 |
| 29 | Vitoria/Foronda Airport |  | ES | 97 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 31 | Charles de Gaulle International Airport |  | FR | 95 |
| 32 | Malpensa International Airport |  | IT | 94 |
| 33 | Barcelona International Airport |  | ES | 92 |
| 34 | Pune Airport |  | IN | 90 |
| 35 | Seattle-Tacoma International Airport |  | US | 86 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 37 | Austin-Bergstrom International Airport |  | US | 85 |
| 38 | Gimpo International Airport |  | KR | 85 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 60 | 1h 7m | 706 km | 730.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 40 | 1h 46m | 1,156 km | 798.0 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 35 | 1h 26m | 910 km | 549.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 31 | 28m | 275 km | 146.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 23 | 20m | 147 km | 58.2 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 18 | 31m | 213 km | 66.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBTDZ | HBT | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-04-03 11:08 UTC | 2026-04-03 11:46 UTC | 37m |
| FGTYA | FGT | Macon-Charnay Airport (LFLM) | Lyon-Bron Airport (LFLY) | 2026-04-03 11:09 UTC | 2026-04-03 11:36 UTC | 26m |
| MTTE35 | MTT | Istres Le Tube/Istres Air Base (BA 125) Airport (LFMI) | Lyon Saint-Exupery Airport (LFLL) | 2026-04-03 07:31 UTC | 2026-04-03 11:16 UTC | 3h 44m |
| DENIG | DEN | Friedrichshafen Airport (EDNY) | Bad Ragaz Airport (LSZE) | 2026-04-03 10:36 UTC | 2026-04-03 11:13 UTC | 36m |
| EJU653N | EJU | Nice-Cote d'Azur Airport (LFMN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-03 09:37 UTC | 2026-04-03 11:02 UTC | 1h 24m |
| XAX604 | XAX | Kuala Lumpur International Airport (WMKK) | UG27 (UG27) | 2026-04-03 02:30 UTC | 2026-04-03 11:02 UTC | 8h 31m |
| 5YMMK |  | Nairobi Wilson Airport (HKNW) | Jomo Kenyatta International Airport (HKJK) | 2026-04-03 10:53 UTC | 2026-04-03 11:02 UTC | 8m |
| N144CH |  | Birmingham-Shuttlesworth International Airport (KBHM) | Birmingham-Shuttlesworth International Airport (KBHM) | 2026-04-03 10:54 UTC | 2026-04-03 10:56 UTC | 1m |
| MEDIC01 | MED | Ameland Airport (EHAL) | Leeuwarden Air Base (EHLW) | 2026-04-03 10:39 UTC | 2026-04-03 10:47 UTC | 8m |
| ZSKMM | ZSK | Witbank Airport (FAWI) | Brakpan Airport (FABB) | 2026-04-03 10:23 UTC | 2026-04-03 10:46 UTC | 22m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-04-03 09:48 UTC | 2026-04-03 10:46 UTC | 57m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Jayena Airport (LE84) | 2026-04-03 10:11 UTC | 2026-04-03 10:42 UTC | 30m |
| QLK1257 | QLK | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-04-03 08:22 UTC | 2026-04-03 10:41 UTC | 2h 19m |
| FDX1757 | FDX | Indianapolis International Airport (KIND) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-03 09:05 UTC | 2026-04-03 10:40 UTC | 1h 34m |
| ALFT6 | ALF | WN40 (WN40) | Boeing Field/King County International Airport (KBFI) | 2026-04-03 10:16 UTC | 2026-04-03 10:39 UTC | 22m |
| WZZ8EU | Wizz Air | Barcelona International Airport (LEBL) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-03 08:04 UTC | 2026-04-03 10:36 UTC | 2h 32m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-03 10:03 UTC | 2026-04-03 10:34 UTC | 31m |
| JAL265 | Japan Airlines | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-03 09:41 UTC | 2026-04-03 10:33 UTC | 52m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-03 09:24 UTC | 2026-04-03 10:32 UTC | 1h 8m |
| DLH1558 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Iasi Airport (LRIA) | 2026-04-03 08:45 UTC | 2026-04-03 10:30 UTC | 1h 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
