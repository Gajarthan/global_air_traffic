# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_19:18:48_UTC-green)

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

**Latest saved flight:** 2026-03-30 19:18:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 19:18:48 UTC

- **5,206** saved flights
- **3,601** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,206** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **65,501.6 tonnes** estimated CO2 emissions
- **3,797,197 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 259 |
| 2 | Ryanair | 197 |
| 3 | IndiGo | 135 |
| 4 | EJA | 115 |
| 5 | American Airlines | 98 |
| 6 | Southwest Airlines | 85 |
| 7 | ENY | 79 |
| 8 | Lufthansa | 77 |
| 9 | AXM | 58 |
| 10 | LATAM Airlines | 58 |
| 11 | Vueling | 53 |
| 12 | LXJ | 52 |
| 13 | Delta Air Lines | 47 |
| 14 | WIF | 41 |
| 15 | All Nippon Airways | 39 |
| 16 | Swiss International | 38 |
| 17 | VIV | 38 |
| 18 | Japan Airlines | 37 |
| 19 | United Airlines | 36 |
| 20 | AZU | 35 |
| 21 | Cathay Pacific | 34 |
| 22 | Avianca | 33 |
| 23 | AXB | 33 |
| 24 | QLK | 33 |
| 25 | EDV | 31 |
| 26 | VOE | 31 |
| 27 | EJU | 30 |
| 28 | Alaska Airlines | 29 |
| 29 | Air France | 27 |
| 30 | MXY | 27 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4525 |
| 2 | 🇮🇳 IN | 404 |
| 3 | 🇪🇸 ES | 392 |
| 4 | 🇦🇺 AU | 291 |
| 5 | 🇨🇴 CO | 268 |
| 6 | 🇧🇷 BR | 267 |
| 7 | 🇯🇵 JP | 252 |
| 8 | 🇮🇹 IT | 251 |
| 9 | 🇩🇪 DE | 238 |
| 10 | 🇨🇦 CA | 214 |
| 11 | 🇲🇽 MX | 185 |
| 12 | 🇬🇧 GB | 177 |
| 13 | 🇫🇷 FR | 165 |
| 14 | 🇳🇴 NO | 137 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇨🇭 CH | 123 |
| 17 | 🇿🇦 ZA | 123 |
| 18 | 🇬🇹 GT | 120 |
| 19 | 🇬🇷 GR | 112 |
| 20 | 🇵🇭 PH | 109 |
| 21 | 🇹🇷 TR | 85 |
| 22 | 🇹🇭 TH | 73 |
| 23 | 🇳🇿 NZ | 65 |
| 24 | 🇲🇦 MA | 63 |
| 25 | 🇵🇱 PL | 63 |
| 26 | 🇲🇴 MO | 59 |
| 27 | 🇮🇩 ID | 58 |
| 28 | 🇧🇸 BS | 57 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 48 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 134 |
| 2 | Denver International Airport |  | US | 97 |
| 3 | El Dorado International Airport |  | CO | 97 |
| 4 | Indira Gandhi International Airport |  | IN | 90 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 82 |
| 7 | Frankfurt am Main International Airport |  | DE | 77 |
| 8 | Zurich Airport |  | CH | 64 |
| 9 | Guaymaral Airport |  | CO | 63 |
| 10 | Tenerife Norte Airport |  | ES | 62 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 61 |
| 12 | Harry Reid International Airport |  | US | 59 |
| 13 | Macau International Airport |  | MO | 59 |
| 14 | Chicago O'Hare International Airport |  | US | 58 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 58 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 52 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 49 |
| 18 | Ninoy Aquino International Airport |  | PH | 48 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 20 | Kuala Lumpur International Airport |  | MY | 46 |
| 21 | Reno/Tahoe International Airport |  | US | 45 |
| 22 | Madrid Barajas International Airport |  | ES | 45 |
| 23 | Bengaluru International Airport |  | IN | 45 |
| 24 | Charlotte/Douglas International Airport |  | US | 43 |
| 25 | Charles de Gaulle International Airport |  | FR | 43 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 42 |
| 27 | O. R. Tambo International Airport |  | ZA | 42 |
| 28 | Miami International Airport |  | US | 41 |
| 29 | Malpensa International Airport |  | IT | 41 |
| 30 | Salt Lake City International Airport |  | US | 39 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 32 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 38 |
| 33 | Vitoria/Foronda Airport |  | ES | 37 |
| 34 | Centennial Airport |  | US | 37 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 36 |
| 36 | Amsterdam Airport Schiphol |  | NL | 36 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 36 |
| 38 | Los Angeles International Airport |  | US | 35 |
| 39 | Congonhas Airport |  | BR | 35 |
| 40 | Daniel K Inouye International Airport |  | US | 34 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
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
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 12 | 1h 54m | 1,156 km | 239.4 t |
| 16 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 12 | 4m | - | - |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 18 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 11 | 29m | 275 km | 52.1 t |
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
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 9 | 1h 3m | 723 km | 112.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N359LU |  | Southern Wisconsin Regional Airport (KJVL) | Southern Wisconsin Regional Airport (KJVL) | 2026-03-30 18:19 UTC | 2026-03-30 19:18 UTC | 59m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-30 19:00 UTC | 2026-03-30 19:13 UTC | 12m |
| RN034 |  | Skypark Estates Owners Assoc Airport (18FD) | Brewton Municipal Airport (K12J) | 2026-03-30 18:53 UTC | 2026-03-30 19:10 UTC | 17m |
| N5253X |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-03-30 18:28 UTC | 2026-03-30 19:07 UTC | 39m |
| N5407F |  | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-03-30 18:47 UTC | 2026-03-30 19:03 UTC | 16m |
| N474J |  | Santa Monica Municipal Airport (KSMO) | San Carlos Airport (KSQL) | 2026-03-30 17:51 UTC | 2026-03-30 18:59 UTC | 1h 8m |
| N365PC |  | Denton Enterprise Airport (KDTO) | 5TS4 (5TS4) | 2026-03-30 17:59 UTC | 2026-03-30 18:59 UTC | 1h 0m |
| WMT485 | WMT | Henri Coanda International Airport (LROP) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-30 17:47 UTC | 2026-03-30 18:57 UTC | 1h 9m |
|  |  | Ataturk International Airport (LTBA) | Zhuhai Airport (ZGSD) | 2026-03-30 09:52 UTC | 2026-03-30 18:56 UTC | 9h 3m |
| N546CA |  | Montgomery-Gibbs Executive Airport (KMYF) | San Bernardino International Airport (KSBD) | 2026-03-30 17:55 UTC | 2026-03-30 18:56 UTC | 1h 0m |
| BB064 |  | Whiting Field Nas North Airport (KNSE) | South Alabama Regional At Bill Benton Field (K79J) | 2026-03-30 18:01 UTC | 2026-03-30 18:52 UTC | 51m |
| GPD705 | GPD | Luis Munoz Marin International Airport (TJSJ) | Cyril E King Airport (TIST) | 2026-03-30 18:39 UTC | 2026-03-30 18:52 UTC | 13m |
| N7048Q |  | Mertens Airport (3CO2) | Mertens Airport (3CO2) | 2026-03-30 18:52 UTC | 2026-03-30 18:52 UTC | 0m |
| N822SR |  | Bolinder Field/Tooele Valley Airport (KTVY) | KU42 (KU42) | 2026-03-30 18:42 UTC | 2026-03-30 18:51 UTC | 9m |
| LNG22 | LNG | Fort Worth Nas Jrb (Carswell Field) Airport (KNFW) | TA59 (TA59) | 2026-03-30 18:12 UTC | 2026-03-30 18:50 UTC | 38m |
| N953CT |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-03-30 18:35 UTC | 2026-03-30 18:47 UTC | 12m |
| N813FM |  | Mc Clellan-Palomar Airport (KCRQ) | Lake Tahoe Airport (KTVL) | 2026-03-30 17:27 UTC | 2026-03-30 18:46 UTC | 1h 19m |
| CWA928 | CWA | Edmonton International Airport (CYEG) | Hardisty Airport (CEA5) | 2026-03-30 18:20 UTC | 2026-03-30 18:45 UTC | 24m |
| ANE80FD | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-03-30 18:11 UTC | 2026-03-30 18:44 UTC | 32m |
| N500RH |  | Concord-Padgett Regional Airport (KJQF) | SC60 (SC60) | 2026-03-30 18:25 UTC | 2026-03-30 18:44 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
