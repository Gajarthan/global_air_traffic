# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_13:34:20_UTC-green)

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

**Latest saved flight:** 2026-04-08 13:34:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 13:34:20 UTC

- **23,349** saved flights
- **11,352** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,349** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **289,872.4 tonnes** estimated CO2 emissions
- **16,804,196 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 973 |
| 2 | Ryanair | 969 |
| 3 | IndiGo | 655 |
| 4 | American Airlines | 422 |
| 5 | EJA | 422 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 300 |
| 9 | Vueling | 244 |
| 10 | AXM | 243 |
| 11 | LATAM Airlines | 232 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 200 |
| 15 | LXJ | 190 |
| 16 | AZU | 183 |
| 17 | Swiss International | 173 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 158 |
| 22 | EJU | 153 |
| 23 | AEE | 148 |
| 24 | WIF | 148 |
| 25 | United Airlines | 147 |
| 26 | Avianca | 140 |
| 27 | EDV | 135 |
| 28 | AXB | 133 |
| 29 | Air France | 124 |
| 30 | PGT | 119 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18091 |
| 2 | 🇮🇳 IN | 1997 |
| 3 | 🇪🇸 ES | 1802 |
| 4 | 🇦🇺 AU | 1748 |
| 5 | 🇯🇵 JP | 1349 |
| 6 | 🇧🇷 BR | 1302 |
| 7 | 🇮🇹 IT | 1203 |
| 8 | 🇩🇪 DE | 1195 |
| 9 | 🇨🇴 CO | 1193 |
| 10 | 🇨🇦 CA | 1040 |
| 11 | 🇬🇧 GB | 952 |
| 12 | 🇫🇷 FR | 865 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 676 |
| 15 | 🇨🇭 CH | 654 |
| 16 | 🇲🇾 MY | 576 |
| 17 | 🇿🇦 ZA | 512 |
| 18 | 🇳🇴 NO | 505 |
| 19 | 🇳🇿 NZ | 497 |
| 20 | 🇬🇹 GT | 470 |
| 21 | 🇹🇷 TR | 450 |
| 22 | 🇵🇭 PH | 445 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 389 |
| 25 | 🇵🇱 PL | 342 |
| 26 | 🇲🇦 MA | 285 |
| 27 | 🇮🇩 ID | 250 |
| 28 | 🇧🇸 BS | 243 |
| 29 | 🇲🇪 ME | 241 |
| 30 | 🇳🇱 NL | 237 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 551 |
| 2 | Tokyo International Airport |  | JP | 448 |
| 3 | El Dorado International Airport |  | CO | 446 |
| 4 | Indira Gandhi International Airport |  | IN | 410 |
| 5 | Denver International Airport |  | US | 408 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 329 |
| 7 | La Aurora Airport |  | GT | 325 |
| 8 | Harry Reid International Airport |  | US | 310 |
| 9 | Zurich Airport |  | CH | 286 |
| 10 | Frankfurt am Main International Airport |  | DE | 261 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 14 | Guaymaral Airport |  | CO | 241 |
| 15 | Chicago O'Hare International Airport |  | US | 240 |
| 16 | Macau International Airport |  | MO | 226 |
| 17 | Bengaluru International Airport |  | IN | 223 |
| 18 | Charlotte/Douglas International Airport |  | US | 217 |
| 19 | Kuala Lumpur International Airport |  | MY | 210 |
| 20 | Madrid Barajas International Airport |  | ES | 209 |
| 21 | Tenerife Norte Airport |  | ES | 207 |
| 22 | Ninoy Aquino International Airport |  | PH | 205 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Malpensa International Airport |  | IT | 192 |
| 25 | Congonhas Airport |  | BR | 188 |
| 26 | Salt Lake City International Airport |  | US | 182 |
| 27 | Daniel K Inouye International Airport |  | US | 178 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Charles de Gaulle International Airport |  | FR | 172 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 163 |
| 32 | O. R. Tambo International Airport |  | ZA | 159 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 157 |
| 34 | Miami International Airport |  | US | 156 |
| 35 | Pune Airport |  | IN | 154 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 37 | Vitoria/Foronda Airport |  | ES | 151 |
| 38 | Seattle-Tacoma International Airport |  | US | 150 |
| 39 | Barcelona International Airport |  | ES | 149 |
| 40 | Gimpo International Airport |  | KR | 141 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 97 | 14m | 114 km | 190.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 89 | 26m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 64 | 1h 42m | 1,156 km | 1,276.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 43 | 20m | 250 km | 185.7 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 35 | 20m | 147 km | 88.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 35 | 12m | 15 km | 9.2 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N21725 |  | 7NY0 (7NY0) | 7NY0 (7NY0) | 2026-04-08 13:19 UTC | 2026-04-08 13:34 UTC | 14m |
| BOMR732 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Gritz Field (XS46) | 2026-04-08 12:56 UTC | 2026-04-08 13:30 UTC | 33m |
| MWT185 | MWT | Joe Foss Field (KFSD) | Dubuque Regional Airport (KDBQ) | 2026-04-08 12:19 UTC | 2026-04-08 13:24 UTC | 1h 4m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-04-08 12:58 UTC | 2026-04-08 13:22 UTC | 23m |
| N9930E |  | Harrisburg International Airport (KMDT) | Capital City Airport (KCXY) | 2026-04-08 12:17 UTC | 2026-04-08 13:21 UTC | 1h 4m |
| N738JT |  | Schenectady County Airport (KSCH) | Fulton County Airport (KNY0) | 2026-04-08 12:58 UTC | 2026-04-08 13:21 UTC | 23m |
| RNGR713 | RNG | Waldron Field Nolf Airport (KNWL) | XS10 (XS10) | 2026-04-08 12:46 UTC | 2026-04-08 13:19 UTC | 33m |
| CGSGP | CGS | Bantry Aerodrome (EIBN) | Bantry Aerodrome (EIBN) | 2026-04-08 13:14 UTC | 2026-04-08 13:16 UTC | 2m |
| EMC8T | EMC | Lydd Airport (EGMD) | Lydd Airport (EGMD) | 2026-04-08 12:12 UTC | 2026-04-08 13:16 UTC | 1h 4m |
| AWH92X | AWH | Hamburg Airport (EDDH) | Berlin Brandenburg Airport (EDDB) | 2026-04-08 12:45 UTC | 2026-04-08 13:14 UTC | 28m |
| FNY5014 | FNY | Mollis Airport (LSZM) | Lyon Saint-Exupery Airport (LFLL) | 2026-04-08 12:28 UTC | 2026-04-08 13:13 UTC | 45m |
| TVF21CH | TVF | Paris-Orly Airport (LFPO) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-08 10:26 UTC | 2026-04-08 13:13 UTC | 2h 46m |
| N8166R |  | South Alabama Regional At Bill Benton Field (K79J) | Auburn University Regional Airport (KAUO) | 2026-04-08 12:36 UTC | 2026-04-08 13:12 UTC | 36m |
| TGACC | TGA | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-08 12:53 UTC | 2026-04-08 13:09 UTC | 15m |
| KEM007 | KEM | O. R. Tambo International Airport (FAOR) | Manyani Game Lodge Airport (FAML) | 2026-04-08 12:42 UTC | 2026-04-08 13:09 UTC | 26m |
| WIF35V | WIF | Oslo Gardermoen Airport (ENGM) | Hattfjelldal Airport (ENHT) | 2026-04-08 11:49 UTC | 2026-04-08 13:09 UTC | 1h 19m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-04-08 12:11 UTC | 2026-04-08 13:08 UTC | 56m |
| ZUPBW | ZUP | Fisantekraal Airport (FAFK) | Ysterplaat Air Force Base (FAYP) | 2026-04-08 12:54 UTC | 2026-04-08 13:06 UTC | 12m |
| N400EE |  | 3OK1 (3OK1) | Sundance Airport (KHSD) | 2026-04-08 12:54 UTC | 2026-04-08 13:06 UTC | 11m |
| WIF2NB | WIF | Trondheim Airport Vaernes (ENVA) | Molde Airport (ENML) | 2026-04-08 12:31 UTC | 2026-04-08 13:04 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
