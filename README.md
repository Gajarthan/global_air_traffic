# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_18:25:24_UTC-green)

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

**Latest saved flight:** 2026-03-30 18:25:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 18:25:24 UTC

- **5,055** saved flights
- **3,519** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,055** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **63,948.7 tonnes** estimated CO2 emissions
- **3,707,169 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 249 |
| 2 | Ryanair | 189 |
| 3 | IndiGo | 134 |
| 4 | EJA | 110 |
| 5 | American Airlines | 95 |
| 6 | Southwest Airlines | 82 |
| 7 | ENY | 76 |
| 8 | Lufthansa | 75 |
| 9 | AXM | 58 |
| 10 | LATAM Airlines | 57 |
| 11 | Vueling | 53 |
| 12 | LXJ | 49 |
| 13 | Delta Air Lines | 46 |
| 14 | WIF | 40 |
| 15 | All Nippon Airways | 39 |
| 16 | Japan Airlines | 37 |
| 17 | Swiss International | 37 |
| 18 | VIV | 35 |
| 19 | Cathay Pacific | 34 |
| 20 | United Airlines | 34 |
| 21 | Avianca | 33 |
| 22 | QLK | 33 |
| 23 | AXB | 32 |
| 24 | AZU | 32 |
| 25 | EDV | 30 |
| 26 | VOE | 30 |
| 27 | Alaska Airlines | 28 |
| 28 | EJU | 28 |
| 29 | Air France | 27 |
| 30 | MXY | 26 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4358 |
| 2 | 🇮🇳 IN | 400 |
| 3 | 🇪🇸 ES | 385 |
| 4 | 🇦🇺 AU | 291 |
| 5 | 🇨🇴 CO | 266 |
| 6 | 🇧🇷 BR | 253 |
| 7 | 🇯🇵 JP | 252 |
| 8 | 🇮🇹 IT | 240 |
| 9 | 🇩🇪 DE | 231 |
| 10 | 🇨🇦 CA | 201 |
| 11 | 🇲🇽 MX | 177 |
| 12 | 🇬🇧 GB | 173 |
| 13 | 🇫🇷 FR | 164 |
| 14 | 🇳🇴 NO | 131 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇿🇦 ZA | 123 |
| 17 | 🇨🇭 CH | 120 |
| 18 | 🇬🇹 GT | 117 |
| 19 | 🇵🇭 PH | 109 |
| 20 | 🇬🇷 GR | 107 |
| 21 | 🇹🇷 TR | 84 |
| 22 | 🇹🇭 TH | 73 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇵🇱 PL | 62 |
| 25 | 🇲🇦 MA | 61 |
| 26 | 🇲🇴 MO | 59 |
| 27 | 🇮🇩 ID | 58 |
| 28 | 🇧🇸 BS | 57 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇫🇮 FI | 47 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 130 |
| 2 | El Dorado International Airport |  | CO | 97 |
| 3 | Denver International Airport |  | US | 93 |
| 4 | Indira Gandhi International Airport |  | IN | 89 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 80 |
| 7 | Frankfurt am Main International Airport |  | DE | 73 |
| 8 | Tenerife Norte Airport |  | ES | 62 |
| 9 | Zurich Airport |  | CH | 62 |
| 10 | Guaymaral Airport |  | CO | 61 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 59 |
| 12 | Macau International Airport |  | MO | 59 |
| 13 | Harry Reid International Airport |  | US | 57 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 57 |
| 15 | Chicago O'Hare International Airport |  | US | 55 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 49 |
| 17 | Ninoy Aquino International Airport |  | PH | 48 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 47 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 20 | Kuala Lumpur International Airport |  | MY | 46 |
| 21 | Bengaluru International Airport |  | IN | 44 |
| 22 | Madrid Barajas International Airport |  | ES | 43 |
| 23 | Charles de Gaulle International Airport |  | FR | 43 |
| 24 | Charlotte/Douglas International Airport |  | US | 42 |
| 25 | O. R. Tambo International Airport |  | ZA | 42 |
| 26 | Reno/Tahoe International Airport |  | US | 41 |
| 27 | Miami International Airport |  | US | 41 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 41 |
| 29 | Malpensa International Airport |  | IT | 38 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 38 |
| 32 | Vitoria/Foronda Airport |  | ES | 37 |
| 33 | Centennial Airport |  | US | 37 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 36 |
| 35 | Amsterdam Airport Schiphol |  | NL | 36 |
| 36 | Congonhas Airport |  | BR | 35 |
| 37 | Salt Lake City International Airport |  | US | 35 |
| 38 | Los Angeles International Airport |  | US | 34 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 34 |
| 40 | Daniel K Inouye International Airport |  | US | 33 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 24 | 28m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 13 | 15m | 206 km | 46.2 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 13 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 15 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 12 | 4m | - | - |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 11 | 29m | 275 km | 52.1 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 11 | 1h 55m | 1,156 km | 219.4 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 23 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 9 | 18m | 183 km | 28.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N35727 |  | Glendale Regional Airport (KGEU) | Casa Grande Municipal Airport (KCGZ) | 2026-03-30 17:23 UTC | 2026-03-30 18:25 UTC | 1h 1m |
| LFA318 | LFA | K55J (K55J) | Nassau Airport (83FL) | 2026-03-30 18:04 UTC | 2026-03-30 18:20 UTC | 16m |
| LUZON41 | LUZ | Bailey Airport (2TS8) | Bailey Airport (2TS8) | 2026-03-30 17:49 UTC | 2026-03-30 18:19 UTC | 29m |
| BYF31 | BYF | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-03-30 17:37 UTC | 2026-03-30 18:18 UTC | 40m |
| N481MR |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-03-30 18:01 UTC | 2026-03-30 18:18 UTC | 16m |
| N443DB |  | Boeing Field/King County International Airport (KBFI) | Palm Springs International Airport (KPSP) | 2026-03-30 16:13 UTC | 2026-03-30 18:17 UTC | 2h 4m |
| N673JH |  | Dubuque Regional Airport (KDBQ) | Monticello Regional Airport (KMXO) | 2026-03-30 17:23 UTC | 2026-03-30 18:17 UTC | 54m |
| N769SP |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Decatur Municipal Airport (KLUD) | 2026-03-30 18:01 UTC | 2026-03-30 18:17 UTC | 15m |
| N5577D |  | Georgetown Executive Airport (KGTU) | Burnet Municipal/Kate Craddock Field (KBMQ) | 2026-03-30 17:30 UTC | 2026-03-30 18:14 UTC | 43m |
| N194TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-03-30 17:39 UTC | 2026-03-30 18:13 UTC | 34m |
| N913SB |  | 6CL4 (6CL4) | Palo Alto Airport (KPAO) | 2026-03-30 17:43 UTC | 2026-03-30 18:12 UTC | 28m |
| N359FA |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-03-30 17:59 UTC | 2026-03-30 18:10 UTC | 10m |
| ASA1025 | Alaska Airlines | Kapalua Airport (PHJH) | Daniel K Inouye International Airport (PHNL) | 2026-03-30 17:56 UTC | 2026-03-30 18:09 UTC | 13m |
| N313VV |  | Des Moines International Airport (KDSM) | Perry Municipal Airport (KPRO) | 2026-03-30 17:34 UTC | 2026-03-30 18:07 UTC | 33m |
| JAT632 | JAT | Comodoro Arturo Merino Benitez International Airport (SCEL) | Curacavi Airport (SCCV) | 2026-03-30 10:44 UTC | 2026-03-30 18:05 UTC | 7h 20m |
| CXK159 | CXK | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-03-30 17:24 UTC | 2026-03-30 17:56 UTC | 31m |
| LFA318 | LFA | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-03-30 17:35 UTC | 2026-03-30 17:53 UTC | 17m |
| RYR6PL | Ryanair | Hamburg Airport (EDDH) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-03-30 17:05 UTC | 2026-03-30 17:51 UTC | 45m |
| N436CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Van Nuys Airport (KVNY) | 2026-03-30 16:26 UTC | 2026-03-30 17:51 UTC | 1h 25m |
| N717PA |  | King Salmon Airport (PAKN) | Port Heiden Airport (PAPH) | 2026-03-30 16:58 UTC | 2026-03-30 17:50 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
