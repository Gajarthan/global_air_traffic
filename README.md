# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_14:35:15_UTC-green)

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

**Latest saved flight:** 2026-04-05 14:35:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 14:35:15 UTC

- **18,043** saved flights
- **9,258** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,043** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **228,901.0 tonnes** estimated CO2 emissions
- **13,269,625 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 771 |
| 2 | Ryanair | 736 |
| 3 | IndiGo | 527 |
| 4 | EJA | 328 |
| 5 | American Airlines | 326 |
| 6 | Lufthansa | 253 |
| 7 | Southwest Airlines | 249 |
| 8 | ENY | 235 |
| 9 | Vueling | 201 |
| 10 | LATAM Airlines | 191 |
| 11 | AXM | 190 |
| 12 | All Nippon Airways | 161 |
| 13 | Delta Air Lines | 154 |
| 14 | QLK | 154 |
| 15 | LXJ | 150 |
| 16 | AZU | 139 |
| 17 | Swiss International | 135 |
| 18 | VIV | 134 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 120 |
| 22 | Avianca | 118 |
| 23 | United Airlines | 117 |
| 24 | AEE | 115 |
| 25 | AXB | 112 |
| 26 | EJU | 112 |
| 27 | EDV | 109 |
| 28 | WIF | 106 |
| 29 | Cathay Pacific | 104 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14009 |
| 2 | 🇮🇳 IN | 1603 |
| 3 | 🇪🇸 ES | 1498 |
| 4 | 🇦🇺 AU | 1310 |
| 5 | 🇧🇷 BR | 1039 |
| 6 | 🇯🇵 JP | 993 |
| 7 | 🇨🇴 CO | 940 |
| 8 | 🇩🇪 DE | 936 |
| 9 | 🇮🇹 IT | 850 |
| 10 | 🇨🇦 CA | 784 |
| 11 | 🇬🇧 GB | 714 |
| 12 | 🇫🇷 FR | 663 |
| 13 | 🇲🇽 MX | 615 |
| 14 | 🇬🇷 GR | 510 |
| 15 | 🇨🇭 CH | 486 |
| 16 | 🇲🇾 MY | 436 |
| 17 | 🇿🇦 ZA | 401 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇳🇴 NO | 355 |
| 20 | 🇵🇭 PH | 350 |
| 21 | 🇬🇹 GT | 348 |
| 22 | 🇹🇷 TR | 343 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 271 |
| 25 | 🇵🇱 PL | 261 |
| 26 | 🇲🇦 MA | 225 |
| 27 | 🇮🇩 ID | 205 |
| 28 | 🇲🇴 MO | 196 |
| 29 | 🇧🇸 BS | 196 |
| 30 | 🇲🇪 ME | 191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 423 |
| 2 | El Dorado International Airport |  | CO | 359 |
| 3 | Tokyo International Airport |  | JP | 339 |
| 4 | Indira Gandhi International Airport |  | IN | 333 |
| 5 | Denver International Airport |  | US | 327 |
| 6 | La Aurora Airport |  | GT | 243 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 239 |
| 8 | Harry Reid International Airport |  | US | 232 |
| 9 | Frankfurt am Main International Airport |  | DE | 226 |
| 10 | Zurich Airport |  | CH | 220 |
| 11 | Macau International Airport |  | MO | 196 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 186 |
| 15 | Guaymaral Airport |  | CO | 185 |
| 16 | Bengaluru International Airport |  | IN | 178 |
| 17 | Chicago O'Hare International Airport |  | US | 175 |
| 18 | Madrid Barajas International Airport |  | ES | 172 |
| 19 | Charlotte/Douglas International Airport |  | US | 167 |
| 20 | Tenerife Norte Airport |  | ES | 162 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 160 |
| 22 | Ninoy Aquino International Airport |  | PH | 160 |
| 23 | Kuala Lumpur International Airport |  | MY | 155 |
| 24 | Congonhas Airport |  | BR | 155 |
| 25 | Daniel K Inouye International Airport |  | US | 146 |
| 26 | Salt Lake City International Airport |  | US | 143 |
| 27 | Malpensa International Airport |  | IT | 140 |
| 28 | Vitoria/Foronda Airport |  | ES | 140 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 30 | Charles de Gaulle International Airport |  | FR | 137 |
| 31 | Reno/Tahoe International Airport |  | US | 136 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 135 |
| 33 | Barcelona International Airport |  | ES | 126 |
| 34 | Miami International Airport |  | US | 124 |
| 35 | Pune Airport |  | IN | 123 |
| 36 | O. R. Tambo International Airport |  | ZA | 123 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 120 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 117 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 40 | Seattle-Tacoma International Airport |  | US | 115 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 70 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 54 | 27m | 152 km | 141.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 53 | 1h 44m | 1,156 km | 1,057.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 48 | 22m | 99 km | 82.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 46 | 27m | 275 km | 218.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 39 | 1h 54m | 1,304 km | 877.4 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 36 | 23m | 252 km | 156.3 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 34 | 1h 43m | 1,423 km | 834.4 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 33 | 13m | 99 km | 56.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 29 | 17m | 183 km | 91.4 t |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZVU | HBZ | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-04-05 13:36 UTC | 2026-04-05 14:35 UTC | 58m |
| N47296 |  | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-04-05 14:02 UTC | 2026-04-05 14:30 UTC | 28m |
| N20332 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-04-05 13:41 UTC | 2026-04-05 14:28 UTC | 46m |
| WZZ1523 | Wizz Air | Copenhagen Kastrup Airport (EKCH) | Oksywie Military Air Base (EPOK) | 2026-04-05 13:49 UTC | 2026-04-05 14:20 UTC | 30m |
| HB3187 |  | Mont-Dauphin - St-Crepin Airport (LFNC) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-05 12:40 UTC | 2026-04-05 14:18 UTC | 1h 38m |
| VTE473 | VTE | Smyrna Airport (KMQY) | Terry Field (74KY) | 2026-04-05 13:39 UTC | 2026-04-05 14:10 UTC | 30m |
| ANE45ZG | ANE | Barcelona International Airport (LEBL) | Altarejos-Guadalcanal Airport (LEGC) | 2026-04-05 12:48 UTC | 2026-04-05 13:54 UTC | 1h 5m |
| DKKSV | DKK | Sisteron - Theze Airport (LFNS) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-05 10:58 UTC | 2026-04-05 13:54 UTC | 2h 55m |
| EZS48KU | EZS | Geneva Cointrin International Airport (LSGG) | Tivat Airport (LYTV) | 2026-04-05 12:24 UTC | 2026-04-05 13:52 UTC | 1h 27m |
| SKW5557 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | 1PS4 (1PS4) | 2026-04-05 12:51 UTC | 2026-04-05 13:51 UTC | 59m |
| GPMMC | GPM | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-04-05 13:49 UTC | 2026-04-05 13:49 UTC | 0m |
| N1910R |  | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-04-05 13:23 UTC | 2026-04-05 13:49 UTC | 26m |
| EZY85KR | easyJet | London Gatwick Airport (EGKK) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-05 13:03 UTC | 2026-04-05 13:47 UTC | 43m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-05 13:35 UTC | 2026-04-05 13:46 UTC | 11m |
| WSN1 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-05 13:09 UTC | 2026-04-05 13:46 UTC | 37m |
| SWA309 | Southwest Airlines | Los Angeles International Airport (KLAX) | San Francisco International Airport (KSFO) | 2026-04-05 12:49 UTC | 2026-04-05 13:45 UTC | 55m |
| RYR82HK | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Tortoli' / Arbatax Airport (LIET) | 2026-04-05 12:13 UTC | 2026-04-05 13:42 UTC | 1h 28m |
| SKW6020 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Root Field (82VA) | 2026-04-05 12:32 UTC | 2026-04-05 13:42 UTC | 1h 9m |
| VAR469 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-05 13:41 UTC | 2026-04-05 13:41 UTC | 0m |
| RYR1145 | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Capua Airport (LIAU) | 2026-04-05 12:56 UTC | 2026-04-05 13:40 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
