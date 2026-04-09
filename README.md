# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_12:38:36_UTC-green)

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

**Latest saved flight:** 2026-04-09 12:38:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 12:38:36 UTC

- **24,965** saved flights
- **11,982** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,965** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **310,368.0 tonnes** estimated CO2 emissions
- **17,992,351 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1035 |
| 2 | SkyWest Airlines | 1021 |
| 3 | IndiGo | 694 |
| 4 | American Airlines | 449 |
| 5 | EJA | 447 |
| 6 | Southwest Airlines | 354 |
| 7 | Lufthansa | 327 |
| 8 | ENY | 324 |
| 9 | Vueling | 260 |
| 10 | AXM | 256 |
| 11 | LATAM Airlines | 247 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 209 |
| 15 | LXJ | 198 |
| 16 | AZU | 196 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 171 |
| 20 | easyJet | 165 |
| 21 | VIV | 165 |
| 22 | EJU | 161 |
| 23 | AEE | 157 |
| 24 | WIF | 155 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 146 |
| 27 | EDV | 145 |
| 28 | AXB | 142 |
| 29 | Cathay Pacific | 131 |
| 30 | ANZ | 128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19383 |
| 2 | 🇮🇳 IN | 2128 |
| 3 | 🇪🇸 ES | 1885 |
| 4 | 🇦🇺 AU | 1874 |
| 5 | 🇯🇵 JP | 1434 |
| 6 | 🇧🇷 BR | 1392 |
| 7 | 🇩🇪 DE | 1306 |
| 8 | 🇮🇹 IT | 1271 |
| 9 | 🇨🇴 CO | 1263 |
| 10 | 🇨🇦 CA | 1157 |
| 11 | 🇬🇧 GB | 1016 |
| 12 | 🇫🇷 FR | 919 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 718 |
| 15 | 🇨🇭 CH | 697 |
| 16 | 🇲🇾 MY | 616 |
| 17 | 🇳🇿 NZ | 550 |
| 18 | 🇳🇴 NO | 533 |
| 19 | 🇿🇦 ZA | 524 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 479 |
| 22 | 🇵🇭 PH | 478 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 426 |
| 25 | 🇵🇱 PL | 375 |
| 26 | 🇲🇦 MA | 307 |
| 27 | 🇮🇩 ID | 258 |
| 28 | 🇲🇪 ME | 255 |
| 29 | 🇲🇴 MO | 253 |
| 30 | 🇳🇱 NL | 252 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 586 |
| 2 | Tokyo International Airport |  | JP | 480 |
| 3 | El Dorado International Airport |  | CO | 470 |
| 4 | Indira Gandhi International Airport |  | IN | 439 |
| 5 | Denver International Airport |  | US | 433 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 348 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 328 |
| 9 | Zurich Airport |  | CH | 298 |
| 10 | Frankfurt am Main International Airport |  | DE | 272 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 256 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 15 | Macau International Airport |  | MO | 253 |
| 16 | Chicago O'Hare International Airport |  | US | 253 |
| 17 | Bengaluru International Airport |  | IN | 234 |
| 18 | Charlotte/Douglas International Airport |  | US | 230 |
| 19 | Kuala Lumpur International Airport |  | MY | 226 |
| 20 | Ninoy Aquino International Airport |  | PH | 222 |
| 21 | Madrid Barajas International Airport |  | ES | 217 |
| 22 | Tenerife Norte Airport |  | ES | 216 |
| 23 | Malpensa International Airport |  | IT | 201 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 25 | Congonhas Airport |  | BR | 198 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 193 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 178 |
| 30 | Charles de Gaulle International Airport |  | FR | 177 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 174 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 165 |
| 33 | Miami International Airport |  | US | 165 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 165 |
| 35 | O. R. Tambo International Airport |  | ZA | 164 |
| 36 | Seattle-Tacoma International Airport |  | US | 162 |
| 37 | Barcelona International Airport |  | ES | 162 |
| 38 | Pune Airport |  | IN | 160 |
| 39 | Vitoria/Foronda Airport |  | ES | 157 |
| 40 | Don Mueang International Airport |  | TH | 148 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 122 | 1h 8m | 706 km | 1,485.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 64 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 63 | 19m | 165 km | 179.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 51 | 27m | 275 km | 241.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 50 | 31m | 369 km | 318.3 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 41 | 13m | 99 km | 70.3 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FJO65K | FJO | Nice-Cote d'Azur Airport (LFMN) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-09 10:41 UTC | 2026-04-09 12:38 UTC | 1h 56m |
| CFCEI | CFC | Québec City Jean Lesage International Airport (CYQB) | Québec City Jean Lesage International Airport (CYQB) | 2026-04-09 12:13 UTC | 2026-04-09 12:32 UTC | 19m |
| BLACK33 | BLA | Ovar Airport (LPOV) | Ovar Airport (LPOV) | 2026-04-09 12:09 UTC | 2026-04-09 12:22 UTC | 13m |
| TJT35DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-09 10:50 UTC | 2026-04-09 12:07 UTC | 1h 17m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-09 11:50 UTC | 2026-04-09 12:03 UTC | 12m |
| GEIV03 | GEI | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Clube do Ceu Airport (SDIN) | 2026-04-09 11:51 UTC | 2026-04-09 12:01 UTC | 10m |
| N491LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-09 11:09 UTC | 2026-04-09 12:00 UTC | 51m |
| AIC4CR | Air India | Dehradun Airport (VIDN) | Dehradun Airport (VIDN) | 2026-04-09 11:54 UTC | 2026-04-09 12:00 UTC | 5m |
| ANA837 | All Nippon Airways | Tokyo International Airport (RJTT) | Dehradun Airport (VIDN) | 2026-04-09 03:25 UTC | 2026-04-09 12:00 UTC | 8h 35m |
| AIC4MF | Air India | Juhu Aerodrome (VAJJ) | Pilani New Airport (VI70) | 2026-04-09 10:19 UTC | 2026-04-09 12:00 UTC | 1h 40m |
| N364EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-09 10:47 UTC | 2026-04-09 11:57 UTC | 1h 10m |
| SEH3XP | SEH | Malpensa International Airport (LIMC) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-09 09:52 UTC | 2026-04-09 11:57 UTC | 2h 4m |
| IGO29YP | IndiGo | Bengaluru International Airport (VOBL) | Hindon Airport (VIDX) | 2026-04-09 09:43 UTC | 2026-04-09 11:54 UTC | 2h 11m |
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-09 10:58 UTC | 2026-04-09 11:49 UTC | 51m |
| SEH6JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-09 11:22 UTC | 2026-04-09 11:48 UTC | 26m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-04-09 11:00 UTC | 2026-04-09 11:44 UTC | 44m |
| SEH5JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-04-09 11:20 UTC | 2026-04-09 11:43 UTC | 22m |
| DAKAY | DAK | Hannover Airport (EDDV) | Leipzig Halle Airport (EDDP) | 2026-04-09 11:18 UTC | 2026-04-09 11:43 UTC | 25m |
| KLM59J | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Cewice Military Airport (EPCE) | 2026-04-09 10:23 UTC | 2026-04-09 11:38 UTC | 1h 15m |
| ANE78XP | ANE | Madrid Barajas International Airport (LEMD) | Garray Airport (LEGY) | 2026-04-09 11:17 UTC | 2026-04-09 11:38 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
