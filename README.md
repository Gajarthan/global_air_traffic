# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_19:00:57_UTC-green)

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

**Latest saved flight:** 2026-04-06 19:00:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 19:00:57 UTC

- **20,387** saved flights
- **10,192** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,387** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **256,043.5 tonnes** estimated CO2 emissions
- **14,843,103 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 874 |
| 2 | Ryanair | 848 |
| 3 | IndiGo | 579 |
| 4 | American Airlines | 387 |
| 5 | EJA | 375 |
| 6 | Southwest Airlines | 287 |
| 7 | ENY | 270 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 221 |
| 10 | LATAM Airlines | 213 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 178 |
| 13 | All Nippon Airways | 176 |
| 14 | LXJ | 174 |
| 15 | QLK | 164 |
| 16 | AZU | 159 |
| 17 | Swiss International | 152 |
| 18 | VIV | 151 |
| 19 | easyJet | 139 |
| 20 | United Airlines | 136 |
| 21 | Alaska Airlines | 135 |
| 22 | EJU | 134 |
| 23 | Japan Airlines | 134 |
| 24 | Avianca | 132 |
| 25 | AEE | 127 |
| 26 | WIF | 124 |
| 27 | EDV | 121 |
| 28 | AXB | 118 |
| 29 | Air France | 111 |
| 30 | BRC | 109 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15913 |
| 2 | 🇮🇳 IN | 1767 |
| 3 | 🇪🇸 ES | 1638 |
| 4 | 🇦🇺 AU | 1411 |
| 5 | 🇧🇷 BR | 1168 |
| 6 | 🇨🇴 CO | 1109 |
| 7 | 🇯🇵 JP | 1090 |
| 8 | 🇩🇪 DE | 1028 |
| 9 | 🇮🇹 IT | 1007 |
| 10 | 🇨🇦 CA | 898 |
| 11 | 🇬🇧 GB | 809 |
| 12 | 🇫🇷 FR | 751 |
| 13 | 🇲🇽 MX | 692 |
| 14 | 🇬🇷 GR | 579 |
| 15 | 🇨🇭 CH | 562 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 460 |
| 18 | 🇿🇦 ZA | 457 |
| 19 | 🇳🇴 NO | 425 |
| 20 | 🇳🇿 NZ | 416 |
| 21 | 🇹🇷 TR | 398 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 300 |
| 26 | 🇲🇦 MA | 252 |
| 27 | 🇧🇸 BS | 225 |
| 28 | 🇲🇪 ME | 217 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 494 |
| 2 | El Dorado International Airport |  | CO | 419 |
| 3 | Tokyo International Airport |  | JP | 377 |
| 4 | Denver International Airport |  | US | 367 |
| 5 | Indira Gandhi International Airport |  | IN | 362 |
| 6 | La Aurora Airport |  | GT | 316 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 274 |
| 8 | Harry Reid International Airport |  | US | 266 |
| 9 | Zurich Airport |  | CH | 252 |
| 10 | Frankfurt am Main International Airport |  | DE | 235 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 220 |
| 12 | Chicago O'Hare International Airport |  | US | 219 |
| 13 | Guaymaral Airport |  | CO | 218 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 214 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Bengaluru International Airport |  | IN | 199 |
| 18 | Charlotte/Douglas International Airport |  | US | 193 |
| 19 | Madrid Barajas International Airport |  | ES | 189 |
| 20 | Tenerife Norte Airport |  | ES | 189 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 182 |
| 22 | Congonhas Airport |  | BR | 174 |
| 23 | Ninoy Aquino International Airport |  | PH | 172 |
| 24 | Reno/Tahoe International Airport |  | US | 161 |
| 25 | Kuala Lumpur International Airport |  | MY | 161 |
| 26 | Salt Lake City International Airport |  | US | 160 |
| 27 | Malpensa International Airport |  | IT | 156 |
| 28 | Daniel K Inouye International Airport |  | US | 156 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 154 |
| 30 | Charles de Gaulle International Airport |  | FR | 152 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 148 |
| 32 | Vitoria/Foronda Airport |  | ES | 145 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 143 |
| 34 | Miami International Airport |  | US | 142 |
| 35 | O. R. Tambo International Airport |  | ZA | 142 |
| 36 | Barcelona International Airport |  | ES | 136 |
| 37 | Pune Airport |  | IN | 135 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 134 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 132 |
| 40 | Seattle-Tacoma International Airport |  | US | 129 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 90 | 14m | 114 km | 176.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 79 | 27m | - | - |
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
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 41 | 52m | 556 km | 393.0 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 38 | 13m | 99 km | 65.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 38 | 20m | 250 km | 164.1 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 32 | 12m | 15 km | 8.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 31 | 20m | 147 km | 78.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WZZ1736 | Wizz Air | Gothenburg-Landvetter Airport (ESGG) | Oksywie Military Air Base (EPOK) | 2026-04-06 18:24 UTC | 2026-04-06 19:00 UTC | 36m |
| N348BW |  | Santa Barbara Municipal Airport (KSBA) | Van Nuys Airport (KVNY) | 2026-04-06 18:28 UTC | 2026-04-06 18:59 UTC | 31m |
| CXK232 | CXK | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-06 17:58 UTC | 2026-04-06 18:58 UTC | 1h 0m |
| N190FT |  | Westchester County Airport (KHPN) | Hudson Valley Regional Airport (KPOU) | 2026-04-06 18:36 UTC | 2026-04-06 18:54 UTC | 18m |
| AEE5LM | AEE | Marseille Provence Airport (LFML) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-06 16:32 UTC | 2026-04-06 18:45 UTC | 2h 13m |
| N164S |  | Renton Municipal Airport (KRNT) | Anderson Field (KS97) | 2026-04-06 18:14 UTC | 2026-04-06 18:45 UTC | 31m |
| N759G |  | Jenkins Airport (3XS4) | Lbj Ranch Airport (0TE7) | 2026-04-06 17:51 UTC | 2026-04-06 18:43 UTC | 51m |
| N431W |  | Elton Hensley Memorial Airport (KFTT) | Elton Hensley Memorial Airport (KFTT) | 2026-04-06 18:28 UTC | 2026-04-06 18:41 UTC | 12m |
| N604TT |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-04-06 17:54 UTC | 2026-04-06 18:40 UTC | 45m |
| N62647 |  | Flying Cloud Airport (KFCM) | Bishman Airport (90MN) | 2026-04-06 17:23 UTC | 2026-04-06 18:39 UTC | 1h 16m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-06 18:17 UTC | 2026-04-06 18:36 UTC | 19m |
| N502FS |  | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-06 18:27 UTC | 2026-04-06 18:36 UTC | 9m |
| N7778U |  | K43U (K43U) | KU77 (KU77) | 2026-04-06 18:17 UTC | 2026-04-06 18:32 UTC | 15m |
| N48SE |  | William P Hobby Airport (KHOU) | William P Hobby Airport (KHOU) | 2026-04-06 18:25 UTC | 2026-04-06 18:31 UTC | 6m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 17:53 UTC | 2026-04-06 18:31 UTC | 37m |
| N4739L |  | Millard Airport (KMLE) | Millard Airport (KMLE) | 2026-04-06 18:11 UTC | 2026-04-06 18:30 UTC | 19m |
| N9469H |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-04-06 18:00 UTC | 2026-04-06 18:29 UTC | 28m |
| N90YK |  | Carson City Airport (KCXP) | Dayton Valley Airpark (KA34) | 2026-04-06 18:23 UTC | 2026-04-06 18:29 UTC | 6m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-06 18:17 UTC | 2026-04-06 18:26 UTC | 9m |
| TRP5 | TRP | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-06 18:21 UTC | 2026-04-06 18:24 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
