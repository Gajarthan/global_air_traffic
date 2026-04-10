# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_11:52:59_UTC-green)

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

**Latest saved flight:** 2026-04-10 11:52:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 11:52:59 UTC

- **26,647** saved flights
- **12,633** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,647** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **327,579.9 tonnes** estimated CO2 emissions
- **18,990,141 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1091 |
| 2 | SkyWest Airlines | 1082 |
| 3 | IndiGo | 716 |
| 4 | EJA | 473 |
| 5 | American Airlines | 471 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | AXM | 279 |
| 10 | Vueling | 272 |
| 11 | LATAM Airlines | 260 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 211 |
| 17 | Swiss International | 186 |
| 18 | Alaska Airlines | 180 |
| 19 | Japan Airlines | 177 |
| 20 | VIV | 176 |
| 21 | easyJet | 174 |
| 22 | WIF | 174 |
| 23 | EJU | 172 |
| 24 | AEE | 171 |
| 25 | United Airlines | 159 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 146 |
| 29 | JetBlue | 140 |
| 30 | Air France | 138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20843 |
| 2 | 🇮🇳 IN | 2204 |
| 3 | 🇦🇺 AU | 1994 |
| 4 | 🇪🇸 ES | 1979 |
| 5 | 🇧🇷 BR | 1490 |
| 6 | 🇯🇵 JP | 1488 |
| 7 | 🇩🇪 DE | 1360 |
| 8 | 🇮🇹 IT | 1356 |
| 9 | 🇨🇴 CO | 1322 |
| 10 | 🇨🇦 CA | 1268 |
| 11 | 🇬🇧 GB | 1076 |
| 12 | 🇫🇷 FR | 1004 |
| 13 | 🇲🇽 MX | 851 |
| 14 | 🇬🇷 GR | 770 |
| 15 | 🇨🇭 CH | 729 |
| 16 | 🇲🇾 MY | 674 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 584 |
| 19 | 🇿🇦 ZA | 554 |
| 20 | 🇵🇭 PH | 508 |
| 21 | 🇹🇷 TR | 499 |
| 22 | 🇬🇹 GT | 490 |
| 23 | 🇹🇭 TH | 473 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 401 |
| 26 | 🇲🇦 MA | 327 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇲🇪 ME | 270 |
| 29 | 🇮🇩 ID | 266 |
| 30 | 🇳🇱 NL | 263 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 624 |
| 2 | Tokyo International Airport |  | JP | 500 |
| 3 | El Dorado International Airport |  | CO | 492 |
| 4 | Indira Gandhi International Airport |  | IN | 455 |
| 5 | Denver International Airport |  | US | 448 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 375 |
| 7 | Harry Reid International Airport |  | US | 345 |
| 8 | La Aurora Airport |  | GT | 340 |
| 9 | Zurich Airport |  | CH | 312 |
| 10 | Frankfurt am Main International Airport |  | DE | 287 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 12 | Guaymaral Airport |  | CO | 276 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 14 | Chicago O'Hare International Airport |  | US | 272 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 269 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 249 |
| 18 | Bengaluru International Airport |  | IN | 244 |
| 19 | Charlotte/Douglas International Airport |  | US | 243 |
| 20 | Ninoy Aquino International Airport |  | PH | 236 |
| 21 | Tenerife Norte Airport |  | ES | 230 |
| 22 | Madrid Barajas International Airport |  | ES | 227 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 209 |
| 24 | Malpensa International Airport |  | IT | 209 |
| 25 | Salt Lake City International Airport |  | US | 206 |
| 26 | Congonhas Airport |  | BR | 206 |
| 27 | Daniel K Inouye International Airport |  | US | 201 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 192 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 183 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 176 |
| 34 | O. R. Tambo International Airport |  | ZA | 175 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 173 |
| 36 | Barcelona International Airport |  | ES | 172 |
| 37 | Seattle-Tacoma International Airport |  | US | 169 |
| 38 | Vitoria/Foronda Airport |  | ES | 167 |
| 39 | Capua Airport |  | IT | 167 |
| 40 | Don Mueang International Airport |  | TH | 165 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 67 | 19m | 165 km | 190.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 54 | 27m | 275 km | 255.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 42 | 20m | 147 km | 106.3 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3171E |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-10 11:32 UTC | 2026-04-10 11:52 UTC | 20m |
| FGCQE | FGC | Toussus-le-Noble Airport (LFPN) | Les Mureaux Airport (LFXU) | 2026-04-10 11:31 UTC | 2026-04-10 11:52 UTC | 20m |
| CXK503 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-10 11:32 UTC | 2026-04-10 11:33 UTC | 1m |
| GAF621 | GAF | Cologne Bonn Airport (EDDK) | Brest Bretagne Airport (LFRB) | 2026-04-10 07:09 UTC | 2026-04-10 11:16 UTC | 4h 6m |
| ANA860 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Tokyo International Airport (RJTT) | 2026-04-10 06:56 UTC | 2026-04-10 11:09 UTC | 4h 13m |
| ANE78XP | ANE | Madrid Barajas International Airport (LEMD) | Santo Tome Del Puerto Airport (LETP) | 2026-04-10 10:45 UTC | 2026-04-10 11:05 UTC | 19m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-04-10 10:25 UTC | 2026-04-10 11:04 UTC | 38m |
| FLJ63T | FLJ | Guernsey Airport (EGJB) | Guernsey Airport (EGJB) | 2026-04-10 11:03 UTC | 2026-04-10 11:03 UTC | 0m |
| LOT4NJ | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Szczecin-Goleniow Solidarność Airport (EPSC) | 2026-04-10 10:07 UTC | 2026-04-10 11:01 UTC | 53m |
| NJM455 | NJM | Gerald R Ford International Airport (KGRR) | Dane County Regional/Truax Field (KMSN) | 2026-04-10 10:20 UTC | 2026-04-10 10:58 UTC | 38m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-10 10:21 UTC | 2026-04-10 10:58 UTC | 37m |
| JES3156 | JES | Ministro Pistarini International Airport (SAEZ) | El Dorado Airport (SATD) | 2026-04-10 09:38 UTC | 2026-04-10 10:58 UTC | 1h 19m |
| RYR9ZE | Ryanair | Kithira Airport (LGKC) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-10 08:21 UTC | 2026-04-10 10:56 UTC | 2h 35m |
| N818AG |  | North Fork Airport (8NY3) | Tweed/New Haven Airport (KHVN) | 2026-04-10 10:15 UTC | 2026-04-10 10:48 UTC | 33m |
| MAS1057 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-10 10:28 UTC | 2026-04-10 10:48 UTC | 20m |
| ABL8823 | ABL | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-10 10:21 UTC | 2026-04-10 10:47 UTC | 26m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-04-10 09:49 UTC | 2026-04-10 10:47 UTC | 57m |
| AM339 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-04-10 10:26 UTC | 2026-04-10 10:46 UTC | 20m |
| EJU59GM | EJU | Amsterdam Airport Schiphol (EHAM) | Brac Airport (LDSB) | 2026-04-10 09:06 UTC | 2026-04-10 10:44 UTC | 1h 37m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-04-10 10:14 UTC | 2026-04-10 10:41 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
