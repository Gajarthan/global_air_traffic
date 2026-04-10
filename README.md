# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_14:29:17_UTC-green)

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

**Latest saved flight:** 2026-04-10 14:29:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 14:29:17 UTC

- **26,781** saved flights
- **12,676** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,781** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **328,774.5 tonnes** estimated CO2 emissions
- **19,059,393 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1099 |
| 2 | SkyWest Airlines | 1084 |
| 3 | IndiGo | 722 |
| 4 | EJA | 475 |
| 5 | American Airlines | 473 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 351 |
| 8 | Lufthansa | 338 |
| 9 | AXM | 284 |
| 10 | Vueling | 272 |
| 11 | LATAM Airlines | 264 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 222 |
| 15 | AZU | 215 |
| 16 | LXJ | 213 |
| 17 | Swiss International | 187 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 178 |
| 20 | Japan Airlines | 177 |
| 21 | WIF | 176 |
| 22 | easyJet | 174 |
| 23 | AEE | 172 |
| 24 | EJU | 172 |
| 25 | United Airlines | 159 |
| 26 | EDV | 156 |
| 27 | Avianca | 151 |
| 28 | AXB | 146 |
| 29 | JetBlue | 142 |
| 30 | Air France | 139 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20942 |
| 2 | 🇮🇳 IN | 2220 |
| 3 | 🇦🇺 AU | 1994 |
| 4 | 🇪🇸 ES | 1985 |
| 5 | 🇧🇷 BR | 1507 |
| 6 | 🇯🇵 JP | 1488 |
| 7 | 🇩🇪 DE | 1366 |
| 8 | 🇮🇹 IT | 1358 |
| 9 | 🇨🇴 CO | 1336 |
| 10 | 🇨🇦 CA | 1273 |
| 11 | 🇬🇧 GB | 1080 |
| 12 | 🇫🇷 FR | 1007 |
| 13 | 🇲🇽 MX | 856 |
| 14 | 🇬🇷 GR | 772 |
| 15 | 🇨🇭 CH | 733 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 588 |
| 19 | 🇿🇦 ZA | 556 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 500 |
| 22 | 🇬🇹 GT | 492 |
| 23 | 🇹🇭 TH | 477 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 407 |
| 26 | 🇲🇦 MA | 332 |
| 27 | 🇧🇸 BS | 275 |
| 28 | 🇲🇪 ME | 271 |
| 29 | 🇮🇩 ID | 266 |
| 30 | 🇳🇱 NL | 265 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 626 |
| 2 | Tokyo International Airport |  | JP | 500 |
| 3 | El Dorado International Airport |  | CO | 493 |
| 4 | Indira Gandhi International Airport |  | IN | 460 |
| 5 | Denver International Airport |  | US | 449 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 376 |
| 7 | Harry Reid International Airport |  | US | 346 |
| 8 | La Aurora Airport |  | GT | 342 |
| 9 | Zurich Airport |  | CH | 313 |
| 10 | Frankfurt am Main International Airport |  | DE | 287 |
| 11 | Guaymaral Airport |  | CO | 282 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 278 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 14 | Chicago O'Hare International Airport |  | US | 272 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 269 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Bengaluru International Airport |  | IN | 245 |
| 19 | Charlotte/Douglas International Airport |  | US | 244 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 230 |
| 22 | Madrid Barajas International Airport |  | ES | 228 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 211 |
| 24 | Malpensa International Airport |  | IT | 210 |
| 25 | Congonhas Airport |  | BR | 208 |
| 26 | Salt Lake City International Airport |  | US | 206 |
| 27 | Daniel K Inouye International Airport |  | US | 202 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 193 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 187 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 184 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 180 |
| 33 | Miami International Airport |  | US | 177 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 177 |
| 35 | O. R. Tambo International Airport |  | ZA | 176 |
| 36 | Barcelona International Airport |  | ES | 172 |
| 37 | Seattle-Tacoma International Airport |  | US | 169 |
| 38 | Vitoria/Foronda Airport |  | ES | 167 |
| 39 | Capua Airport |  | IT | 167 |
| 40 | Don Mueang International Airport |  | TH | 166 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 105 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 54 | 27m | 275 km | 255.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 46 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 42 | 20m | 147 km | 106.3 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N38549 |  | Laconia Municipal Airport (KLCI) | Laconia Municipal Airport (KLCI) | 2026-04-10 13:56 UTC | 2026-04-10 14:29 UTC | 32m |
| SCA77 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-10 13:56 UTC | 2026-04-10 14:12 UTC | 15m |
| N738DM |  | Lincoln County Regional Airport (KIPJ) | Lincoln County Regional Airport (KIPJ) | 2026-04-10 13:28 UTC | 2026-04-10 14:12 UTC | 44m |
| SPSMQ | SPS | Poznań-Ławica Airport (EPPO) | Pila Airport (EPPI) | 2026-04-10 13:35 UTC | 2026-04-10 14:11 UTC | 35m |
| TASI313 | TAS | Perot Field/Fort Worth Alliance Airport (KAFW) | 5TA4 (5TA4) | 2026-04-10 13:00 UTC | 2026-04-10 14:08 UTC | 1h 8m |
| N133VU |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-04-10 13:18 UTC | 2026-04-10 14:07 UTC | 48m |
| N177CN |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-10 13:42 UTC | 2026-04-10 14:03 UTC | 21m |
| GHOST32 | GHO | Hill Top Airport (OK08) | Ramsak Airport (OK67) | 2026-04-10 13:34 UTC | 2026-04-10 14:03 UTC | 29m |
| N13693 |  | Estherville Municipal Airport (KEST) | Rosenberg Airport (MY80) | 2026-04-10 13:44 UTC | 2026-04-10 14:03 UTC | 19m |
| SCU48 | SCU | 2OL2 (2OL2) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-10 13:46 UTC | 2026-04-10 14:03 UTC | 16m |
| N745TW |  | KU42 (KU42) | KU42 (KU42) | 2026-04-10 13:44 UTC | 2026-04-10 14:01 UTC | 17m |
| N497CA |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-04-10 13:39 UTC | 2026-04-10 13:55 UTC | 16m |
| IGO1161 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-04-10 12:33 UTC | 2026-04-10 13:55 UTC | 1h 22m |
| DUSTY78 | DUS | Rosenthal-Field Plossen Airport (EDQP) | Grafenwohr Army Air Field (ETIC) | 2026-04-10 13:44 UTC | 2026-04-10 13:54 UTC | 10m |
| CONGO65 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-04-10 13:20 UTC | 2026-04-10 13:51 UTC | 30m |
| MABTE | MAB | London Stansted Airport (EGSS) | Bournemouth Airport (EGHH) | 2026-04-10 11:54 UTC | 2026-04-10 13:51 UTC | 1h 56m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | OMU9 (OMU9) | 2026-04-10 13:34 UTC | 2026-04-10 13:47 UTC | 13m |
| CGSAG | CGS | Montréal / St-Hubert Airport (CYHU) | Princeton Municipal Airport (KPNN) | 2026-04-10 12:52 UTC | 2026-04-10 13:47 UTC | 55m |
| N67KP |  | Youvan Airport (7KS3) | Voller Airport (ND41) | 2026-04-10 12:23 UTC | 2026-04-10 13:46 UTC | 1h 23m |
| N71F |  | Hampton Roads Executive Airport (KPVG) | Crazy Horse Airport (12WV) | 2026-04-10 12:52 UTC | 2026-04-10 13:45 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
