# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_09:56:57_UTC-green)

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

**Latest saved flight:** 2026-04-13 09:56:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 09:56:57 UTC

- **31,889** saved flights
- **14,404** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,889** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **392,916.7 tonnes** estimated CO2 emissions
- **22,777,782 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1343 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 819 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 464 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 339 |
| 10 | LATAM Airlines | 324 |
| 11 | Vueling | 324 |
| 12 | All Nippon Airways | 293 |
| 13 | AZU | 284 |
| 14 | Delta Air Lines | 265 |
| 15 | QLK | 265 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 237 |
| 18 | Alaska Airlines | 215 |
| 19 | easyJet | 212 |
| 20 | WIF | 211 |
| 21 | EJU | 208 |
| 22 | AEE | 205 |
| 23 | VIV | 204 |
| 24 | Japan Airlines | 202 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 173 |
| 28 | Air France | 172 |
| 29 | Avianca | 171 |
| 30 | JetBlue | 169 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25054 |
| 2 | 🇮🇳 IN | 2510 |
| 3 | 🇪🇸 ES | 2380 |
| 4 | 🇦🇺 AU | 2240 |
| 5 | 🇧🇷 BR | 1890 |
| 6 | 🇯🇵 JP | 1749 |
| 7 | 🇮🇹 IT | 1679 |
| 8 | 🇩🇪 DE | 1616 |
| 9 | 🇨🇴 CO | 1598 |
| 10 | 🇨🇦 CA | 1540 |
| 11 | 🇬🇧 GB | 1294 |
| 12 | 🇫🇷 FR | 1173 |
| 13 | 🇲🇽 MX | 1015 |
| 14 | 🇬🇷 GR | 927 |
| 15 | 🇨🇭 CH | 887 |
| 16 | 🇲🇾 MY | 818 |
| 17 | 🇳🇴 NO | 709 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 654 |
| 20 | 🇵🇭 PH | 600 |
| 21 | 🇬🇹 GT | 587 |
| 22 | 🇹🇷 TR | 586 |
| 23 | 🇹🇭 TH | 585 |
| 24 | 🇰🇷 KR | 551 |
| 25 | 🇵🇱 PL | 484 |
| 26 | 🇲🇦 MA | 410 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 316 |
| 29 | 🇮🇩 ID | 306 |
| 30 | 🇳🇱 NL | 305 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 766 |
| 2 | Tokyo International Airport |  | JP | 590 |
| 3 | El Dorado International Airport |  | CO | 568 |
| 4 | Denver International Airport |  | US | 538 |
| 5 | Indira Gandhi International Airport |  | IN | 534 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 454 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 415 |
| 9 | Zurich Airport |  | CH | 392 |
| 10 | Guaymaral Airport |  | CO | 388 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 12 | Chicago O'Hare International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 312 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 311 |
| 17 | Macau International Airport |  | MO | 303 |
| 18 | Charlotte/Douglas International Airport |  | US | 289 |
| 19 | Bengaluru International Airport |  | IN | 286 |
| 20 | Madrid Barajas International Airport |  | ES | 285 |
| 21 | Tenerife Norte Airport |  | ES | 284 |
| 22 | Ninoy Aquino International Airport |  | PH | 277 |
| 23 | Congonhas Airport |  | BR | 277 |
| 24 | Malpensa International Airport |  | IT | 257 |
| 25 | Daniel K Inouye International Airport |  | US | 245 |
| 26 | Salt Lake City International Airport |  | US | 244 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 243 |
| 28 | Reno/Tahoe International Airport |  | US | 242 |
| 29 | Charles de Gaulle International Airport |  | FR | 233 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 229 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 220 |
| 32 | Capua Airport |  | IT | 220 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 220 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 216 |
| 35 | O. R. Tambo International Airport |  | ZA | 213 |
| 36 | Miami International Airport |  | US | 210 |
| 37 | Vitoria/Foronda Airport |  | ES | 210 |
| 38 | Barcelona International Airport |  | ES | 203 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Viracopos International Airport |  | BR | 196 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 148 | 1h 8m | 706 km | 1,801.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 105 | 28m | 304 km | 550.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 92 | 1h 28m | 910 km | 1,443.7 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 82 | 19m | 165 km | 233.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 77 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 72 | 55m | 546 km | 677.9 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 68 | 27m | 275 km | 322.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 67 | 1h 12m | 770 km | 890.0 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 66 | 21m | 244 km | 277.9 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 62 | 31m | 369 km | 394.6 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 59 | 45m | 452 km | 459.8 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 55 | 20m | 250 km | 237.6 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 47 | 16m | 162 km | 131.7 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EXS7RH | EXS | Leeds Bradford Airport (EGNM) | Faro Airport (LPFR) | 2026-04-13 07:25 UTC | 2026-04-13 09:56 UTC | 2h 31m |
| JA07DR |  | Shimofusa Airport (RJTL) | Shimofusa Airport (RJTL) | 2026-04-13 08:31 UTC | 2026-04-13 09:32 UTC | 1h 1m |
| THY8XS | Turkish Airlines | Antalya International Airport (LTAI) | Isparta Airport (LTBM) | 2026-04-13 09:19 UTC | 2026-04-13 09:30 UTC | 10m |
| QTR49Q | Qatar Airways | Hamad International Airport (OTHH) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-13 04:38 UTC | 2026-04-13 09:19 UTC | 4h 41m |
| AEE253 | AEE | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-13 08:13 UTC | 2026-04-13 09:12 UTC | 59m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Ålesund Airport (ENAL) | 2026-04-13 08:42 UTC | 2026-04-13 09:11 UTC | 28m |
| WIS101 | WIS | MN95 (MN95) | Hector International Airport (KFAR) | 2026-04-13 08:52 UTC | 2026-04-13 09:10 UTC | 17m |
| HAKAR | HAK | Medulin Campanoz Airport (LDPM) | Otocac Airport (LDRO) | 2026-04-13 08:59 UTC | 2026-04-13 09:09 UTC | 10m |
| VOE65LF | VOE | Barcelona International Airport (LEBL) | Leon Airport (LELN) | 2026-04-13 08:04 UTC | 2026-04-13 09:06 UTC | 1h 1m |
| DEKBC | DEK | Sun View Field (03PR) | Straubing Airport (EDMS) | 2026-04-13 08:11 UTC | 2026-04-13 09:05 UTC | 53m |
| AIC5YE | Air India | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-13 03:33 UTC | 2026-04-13 08:58 UTC | 5h 24m |
| HGB2369 | HGB | Fukuoka Airport (RJFF) | Chek Lap Kok International Airport (VHHH) | 2026-04-13 05:53 UTC | 2026-04-13 08:57 UTC | 3h 3m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-13 08:43 UTC | 2026-04-13 08:57 UTC | 14m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-04-13 07:28 UTC | 2026-04-13 08:56 UTC | 1h 27m |
| LLR831 | LLR | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-04-13 08:22 UTC | 2026-04-13 08:53 UTC | 31m |
| AEE274 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-13 08:29 UTC | 2026-04-13 08:52 UTC | 23m |
| RYR80FX | Ryanair | Nuremberg Airport (EDDN) | Capua Airport (LIAU) | 2026-04-13 07:29 UTC | 2026-04-13 08:51 UTC | 1h 22m |
| LNK861C | LNK | O. R. Tambo International Airport (FAOR) | Lydenburg Airport (FALL) | 2026-04-13 08:27 UTC | 2026-04-13 08:51 UTC | 23m |
| QFA937 | Qantas | Brisbane International Airport (YBBN) | Perth International Airport (YPPH) | 2026-04-13 03:53 UTC | 2026-04-13 08:50 UTC | 4h 56m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-04-13 07:55 UTC | 2026-04-13 08:49 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
