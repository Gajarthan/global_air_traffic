# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_17:25:21_UTC-green)

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

**Latest saved flight:** 2026-04-07 17:25:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 17:25:21 UTC

- **21,858** saved flights
- **10,791** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,858** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **272,610.5 tonnes** estimated CO2 emissions
- **15,803,508 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 918 |
| 3 | IndiGo | 620 |
| 4 | American Airlines | 412 |
| 5 | EJA | 405 |
| 6 | Southwest Airlines | 309 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 278 |
| 9 | Vueling | 232 |
| 10 | LATAM Airlines | 227 |
| 11 | AXM | 214 |
| 12 | All Nippon Airways | 193 |
| 13 | Delta Air Lines | 190 |
| 14 | LXJ | 186 |
| 15 | QLK | 183 |
| 16 | AZU | 169 |
| 17 | Swiss International | 162 |
| 18 | VIV | 157 |
| 19 | easyJet | 149 |
| 20 | Alaska Airlines | 148 |
| 21 | Japan Airlines | 148 |
| 22 | United Airlines | 143 |
| 23 | EJU | 142 |
| 24 | Avianca | 139 |
| 25 | AEE | 137 |
| 26 | WIF | 134 |
| 27 | EDV | 127 |
| 28 | AXB | 125 |
| 29 | Air France | 119 |
| 30 | Wizz Air | 113 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17069 |
| 2 | 🇮🇳 IN | 1887 |
| 3 | 🇪🇸 ES | 1729 |
| 4 | 🇦🇺 AU | 1551 |
| 5 | 🇧🇷 BR | 1239 |
| 6 | 🇯🇵 JP | 1210 |
| 7 | 🇨🇴 CO | 1175 |
| 8 | 🇮🇹 IT | 1114 |
| 9 | 🇩🇪 DE | 1093 |
| 10 | 🇨🇦 CA | 965 |
| 11 | 🇬🇧 GB | 871 |
| 12 | 🇫🇷 FR | 808 |
| 13 | 🇲🇽 MX | 727 |
| 14 | 🇬🇷 GR | 622 |
| 15 | 🇨🇭 CH | 602 |
| 16 | 🇲🇾 MY | 501 |
| 17 | 🇿🇦 ZA | 490 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇴 NO | 462 |
| 20 | 🇳🇿 NZ | 444 |
| 21 | 🇹🇷 TR | 428 |
| 22 | 🇵🇭 PH | 413 |
| 23 | 🇰🇷 KR | 388 |
| 24 | 🇹🇭 TH | 348 |
| 25 | 🇵🇱 PL | 317 |
| 26 | 🇲🇦 MA | 268 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 410 |
| 4 | Denver International Airport |  | US | 393 |
| 5 | Indira Gandhi International Airport |  | IN | 380 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 298 |
| 8 | Harry Reid International Airport |  | US | 286 |
| 9 | Zurich Airport |  | CH | 267 |
| 10 | Frankfurt am Main International Airport |  | DE | 245 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 233 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 231 |
| 14 | Guaymaral Airport |  | CO | 230 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 217 |
| 16 | Bengaluru International Airport |  | IN | 213 |
| 17 | Charlotte/Douglas International Airport |  | US | 208 |
| 18 | Macau International Airport |  | MO | 201 |
| 19 | Tenerife Norte Airport |  | ES | 201 |
| 20 | Madrid Barajas International Airport |  | ES | 199 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 191 |
| 22 | Ninoy Aquino International Airport |  | PH | 189 |
| 23 | Congonhas Airport |  | BR | 182 |
| 24 | Kuala Lumpur International Airport |  | MY | 178 |
| 25 | Malpensa International Airport |  | IT | 171 |
| 26 | Daniel K Inouye International Airport |  | US | 170 |
| 27 | Salt Lake City International Airport |  | US | 170 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 169 |
| 29 | Reno/Tahoe International Airport |  | US | 168 |
| 30 | Charles de Gaulle International Airport |  | FR | 162 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | O. R. Tambo International Airport |  | ZA | 152 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 150 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 148 |
| 36 | Vitoria/Foronda Airport |  | ES | 146 |
| 37 | Pune Airport |  | IN | 146 |
| 38 | Barcelona International Airport |  | ES | 145 |
| 39 | Seattle-Tacoma International Airport |  | US | 138 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 103 | 1h 8m | 706 km | 1,254.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 51 | 19m | 165 km | 145.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 46 | 55m | 546 km | 433.1 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 44 | 31m | 369 km | 280.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 41 | 20m | 250 km | 177.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TIGER31 | TIG | 2TX3 (2TX3) | Benson Airstrip (2XS8) | 2026-04-07 17:00 UTC | 2026-04-07 17:25 UTC | 24m |
| HNL12A | HNL | De Kooy Airport (EHKD) | De Kooy Airport (EHKD) | 2026-04-07 17:08 UTC | 2026-04-07 17:23 UTC | 14m |
| N51794 |  | Gregg Airport (7OK1) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-07 17:01 UTC | 2026-04-07 17:19 UTC | 17m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-07 17:03 UTC | 2026-04-07 17:17 UTC | 13m |
| N582BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-07 16:24 UTC | 2026-04-07 17:17 UTC | 53m |
| OXF1098 | OXF | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-04-07 16:57 UTC | 2026-04-07 17:16 UTC | 19m |
| N68BC |  | Everitt Airport (1CO8) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-07 16:13 UTC | 2026-04-07 17:16 UTC | 1h 3m |
| HTY292 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-07 16:49 UTC | 2026-04-07 17:16 UTC | 27m |
| DLH147 | Lufthansa | Nuremberg Airport (EDDN) | Aschaffenburg Airport (EDFC) | 2026-04-07 16:39 UTC | 2026-04-07 17:16 UTC | 37m |
| KLM1316 | KLM Royal Dutch | Eisenhuttenstadt Airport (EDAE) | Aero Club Salland (EHDS) | 2026-04-07 16:13 UTC | 2026-04-07 17:16 UTC | 1h 3m |
| SXS1 | SXS | LOXA (LOXA) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-07 16:13 UTC | 2026-04-07 17:16 UTC | 1h 3m |
| DLH1AN | Lufthansa | Stuttgart Airport (EDDS) | Mosbach-Lohrbach Airport (EDGM) | 2026-04-07 16:44 UTC | 2026-04-07 17:15 UTC | 30m |
| MTU85 | MTU | Murfreesboro Municipal Airport (KMBT) | Murfreesboro Municipal Airport (KMBT) | 2026-04-07 16:57 UTC | 2026-04-07 17:14 UTC | 16m |
| N266SP |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-04-07 16:30 UTC | 2026-04-07 17:14 UTC | 43m |
| AUA16N | Austrian Airlines | Arnbruck Airport (EDNB) | Essen Mulheim Airport (EDLE) | 2026-04-07 16:13 UTC | 2026-04-07 17:13 UTC | 1h 0m |
| DLH4UP | Lufthansa | Parma Airport (LIMP) | Heppenheim Airport (EDEP) | 2026-04-07 16:13 UTC | 2026-04-07 17:13 UTC | 1h 0m |
| N816VA |  | Lovell Field (KCHA) | Dalton Municipal Airport (KDNN) | 2026-04-07 16:43 UTC | 2026-04-07 17:09 UTC | 25m |
| N460LE |  | Bend Municipal Airport (KBDN) | Bend Municipal Airport (KBDN) | 2026-04-07 16:52 UTC | 2026-04-07 17:08 UTC | 16m |
| N15HR |  | Timberdoodle Airport (93VA) | Aiken Regional Airport (KAIK) | 2026-04-07 16:13 UTC | 2026-04-07 17:08 UTC | 55m |
| N11RM |  | Redlands Municipal Airport (KREI) | Hemet-Ryan Airport (KHMT) | 2026-04-07 16:42 UTC | 2026-04-07 17:07 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
