# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_13:01:04_UTC-green)

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

**Latest saved flight:** 2026-04-03 13:01:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 13:01:04 UTC

- **13,197** saved flights
- **7,372** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,197** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **164,148.7 tonnes** estimated CO2 emissions
- **9,515,866 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 560 |
| 2 | Ryanair | 505 |
| 3 | IndiGo | 379 |
| 4 | EJA | 256 |
| 5 | American Airlines | 236 |
| 6 | Lufthansa | 204 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 141 |
| 10 | AXM | 139 |
| 11 | LATAM Airlines | 135 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 102 |
| 16 | Swiss International | 102 |
| 17 | AZU | 97 |
| 18 | WIF | 97 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | AXB | 87 |
| 22 | Japan Airlines | 87 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 81 |
| 26 | EJU | 79 |
| 27 | EDV | 78 |
| 28 | AEE | 75 |
| 29 | ANZ | 72 |
| 30 | BRC | 72 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10402 |
| 2 | 🇮🇳 IN | 1165 |
| 3 | 🇦🇺 AU | 1076 |
| 4 | 🇪🇸 ES | 1012 |
| 5 | 🇧🇷 BR | 733 |
| 6 | 🇯🇵 JP | 720 |
| 7 | 🇩🇪 DE | 712 |
| 8 | 🇨🇴 CO | 625 |
| 9 | 🇨🇦 CA | 608 |
| 10 | 🇮🇹 IT | 582 |
| 11 | 🇬🇧 GB | 501 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 453 |
| 14 | 🇬🇷 GR | 346 |
| 15 | 🇨🇭 CH | 345 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 313 |
| 18 | 🇳🇴 NO | 308 |
| 19 | 🇿🇦 ZA | 275 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 240 |
| 22 | 🇰🇷 KR | 235 |
| 23 | 🇬🇹 GT | 234 |
| 24 | 🇵🇱 PL | 186 |
| 25 | 🇹🇭 TH | 176 |
| 26 | 🇮🇩 ID | 162 |
| 27 | 🇲🇦 MA | 159 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇲🇪 ME | 138 |
| 30 | 🇳🇱 NL | 133 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 253 |
| 3 | Indira Gandhi International Airport |  | IN | 247 |
| 4 | Denver International Airport |  | US | 233 |
| 5 | El Dorado International Airport |  | CO | 219 |
| 6 | Frankfurt am Main International Airport |  | DE | 193 |
| 7 | Harry Reid International Airport |  | US | 181 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Zurich Airport |  | CH | 161 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 159 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 154 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Bengaluru International Airport |  | IN | 130 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 121 |
| 19 | Madrid Barajas International Airport |  | ES | 117 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 21 | Kuala Lumpur International Airport |  | MY | 114 |
| 22 | Congonhas Airport |  | BR | 114 |
| 23 | Charlotte/Douglas International Airport |  | US | 113 |
| 24 | Tenerife Norte Airport |  | ES | 108 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 106 |
| 26 | Vitoria/Foronda Airport |  | ES | 100 |
| 27 | Salt Lake City International Airport |  | US | 98 |
| 28 | Daniel K Inouye International Airport |  | US | 97 |
| 29 | Reno/Tahoe International Airport |  | US | 97 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 97 |
| 31 | Charles de Gaulle International Airport |  | FR | 96 |
| 32 | Malpensa International Airport |  | IT | 95 |
| 33 | Barcelona International Airport |  | ES | 93 |
| 34 | Pune Airport |  | IN | 90 |
| 35 | Seattle-Tacoma International Airport |  | US | 86 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 37 | Austin-Bergstrom International Airport |  | US | 85 |
| 38 | Gimpo International Airport |  | KR | 85 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 80 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 40 | 1h 46m | 1,156 km | 798.0 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
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
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 24 | 20m | 147 km | 60.7 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
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
| N370MD |  | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-03 12:49 UTC | 2026-04-03 13:01 UTC | 11m |
| ERU414 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-04-03 12:34 UTC | 2026-04-03 12:55 UTC | 21m |
| 5503 |  | Evreux-Fauville (BA 105) Air Base (LFOE) | Orleans-Bricy (BA 123) Air Base (LFOJ) | 2026-04-03 12:18 UTC | 2026-04-03 12:49 UTC | 31m |
| SXBDZ | SXB | Megara Airport (LGMG) | Sparti Airport (LGSP) | 2026-04-03 11:51 UTC | 2026-04-03 12:43 UTC | 52m |
| AEE855 | AEE | Geneva Cointrin International Airport (LSGG) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-03 10:08 UTC | 2026-04-03 12:31 UTC | 2h 22m |
| HBZLW | HBZ | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-03 11:39 UTC | 2026-04-03 12:30 UTC | 50m |
| RVR12T | RVR | Liverpool John Lennon Airport (EGGP) | Blackpool International Airport (EGNH) | 2026-04-03 11:48 UTC | 2026-04-03 12:28 UTC | 39m |
| OEFGE | OEF | Monchengladbach Airport (EDLN) | St. Johann In Tirol Airport (LOIJ) | 2026-04-03 10:43 UTC | 2026-04-03 12:27 UTC | 1h 44m |
| N905NY |  | Capitan FAP Carlos Martinez De Pinillos International Airport (SPRU) | Quiruvilca Airport (SPQR) | 2026-04-03 12:14 UTC | 2026-04-03 12:24 UTC | 10m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-04-03 11:24 UTC | 2026-04-03 12:23 UTC | 58m |
| N484LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-03 11:10 UTC | 2026-04-03 12:13 UTC | 1h 3m |
| VOE82XX | VOE | Nantes Atlantique Airport (LFRS) | Jayena Airport (LE84) | 2026-04-03 10:49 UTC | 2026-04-03 12:12 UTC | 1h 23m |
| SFR415 | SFR | Cape Town International Airport (FACT) | Brakpan Airport (FABB) | 2026-04-03 09:01 UTC | 2026-04-03 12:10 UTC | 3h 9m |
| N257EA |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-03 10:53 UTC | 2026-04-03 12:10 UTC | 1h 16m |
| N481LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-03 11:04 UTC | 2026-04-03 12:08 UTC | 1h 4m |
| HBXXW | HBX | Lugano Airport (LSZA) | Lugano Airport (LSZA) | 2026-04-03 11:47 UTC | 2026-04-03 12:05 UTC | 17m |
| GCM510 | GCM | O. R. Tambo International Airport (FAOR) | Lydenburg Airport (FALL) | 2026-04-03 11:42 UTC | 2026-04-03 12:05 UTC | 23m |
| AFR65DN | Air France | Charles de Gaulle International Airport (LFPG) | Dax Seyresse Airport (LFBY) | 2026-04-03 11:12 UTC | 2026-04-03 12:02 UTC | 49m |
| VLG6XK | Vueling | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 2026-04-03 11:12 UTC | 2026-04-03 12:02 UTC | 50m |
| AZU6020 | AZU | Congonhas Airport (SBSP) | Bunge Fertilizantes Airport (SIBF) | 2026-04-03 11:39 UTC | 2026-04-03 12:01 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
