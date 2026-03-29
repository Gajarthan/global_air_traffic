# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_17:32:56_UTC-green)

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

**Latest saved flight:** 2026-03-29 17:32:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 17:32:56 UTC

- **2,564** saved flights
- **1,977** unique routes
- **92** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,564** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **34,383.6 tonnes** estimated CO2 emissions
- **1,993,249 km** total distance flown
- **908 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 113 |
| 2 | Ryanair | 85 |
| 3 | IndiGo | 76 |
| 4 | EJA | 50 |
| 5 | Lufthansa | 48 |
| 6 | Southwest Airlines | 47 |
| 7 | American Airlines | 44 |
| 8 | ENY | 42 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 27 |
| 11 | Vueling | 27 |
| 12 | LXJ | 24 |
| 13 | LATAM Airlines | 24 |
| 14 | United Airlines | 23 |
| 15 | Cathay Pacific | 21 |
| 16 | All Nippon Airways | 20 |
| 17 | AXB | 18 |
| 18 | Japan Airlines | 18 |
| 19 | Swiss International | 18 |
| 20 | Avianca | 17 |
| 21 | BRC | 17 |
| 22 | VIV | 17 |
| 23 | WIF | 17 |
| 24 | ARE | 16 |
| 25 | EDV | 16 |
| 26 | VOE | 15 |
| 27 | AEE | 14 |
| 28 | APG | 14 |
| 29 | Alaska Airlines | 14 |
| 30 | AZU | 14 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2130 |
| 2 | 🇮🇳 IN | 209 |
| 3 | 🇪🇸 ES | 205 |
| 4 | 🇨🇴 CO | 160 |
| 5 | 🇩🇪 DE | 138 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇦🇺 AU | 125 |
| 8 | 🇧🇷 BR | 108 |
| 9 | 🇮🇹 IT | 107 |
| 10 | 🇨🇦 CA | 101 |
| 11 | 🇬🇧 GB | 92 |
| 12 | 🇲🇽 MX | 88 |
| 13 | 🇲🇾 MY | 81 |
| 14 | 🇿🇦 ZA | 80 |
| 15 | 🇬🇹 GT | 78 |
| 16 | 🇫🇷 FR | 71 |
| 17 | 🇨🇭 CH | 63 |
| 18 | 🇵🇭 PH | 63 |
| 19 | 🇬🇷 GR | 56 |
| 20 | 🇳🇴 NO | 55 |
| 21 | 🇹🇷 TR | 46 |
| 22 | 🇹🇭 TH | 44 |
| 23 | 🇵🇱 PL | 36 |
| 24 | 🇮🇩 ID | 35 |
| 25 | 🇫🇮 FI | 33 |
| 26 | 🇧🇸 BS | 33 |
| 27 | 🇲🇦 MA | 32 |
| 28 | 🇲🇴 MO | 31 |
| 29 | 🇳🇱 NL | 27 |
| 30 | 🇰🇷 KR | 26 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 60 |
| 2 | El Dorado International Airport |  | CO | 55 |
| 3 | Frankfurt am Main International Airport |  | DE | 50 |
| 4 | La Aurora Airport |  | GT | 49 |
| 5 | Indira Gandhi International Airport |  | IN | 46 |
| 6 | Guaymaral Airport |  | CO | 46 |
| 7 | Tokyo International Airport |  | JP | 44 |
| 8 | Denver International Airport |  | US | 43 |
| 9 | Kuala Lumpur International Airport |  | MY | 33 |
| 10 | Tenerife Norte Airport |  | ES | 32 |
| 11 | Macau International Airport |  | MO | 31 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 30 |
| 13 | Zurich Airport |  | CH | 29 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 29 |
| 15 | O. R. Tambo International Airport |  | ZA | 29 |
| 16 | Harry Reid International Airport |  | US | 28 |
| 17 | Chicago O'Hare International Airport |  | US | 26 |
| 18 | Ninoy Aquino International Airport |  | PH | 26 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 20 | Eleftherios Venizelos International Airport |  | GR | 23 |
| 21 | Vitoria/Foronda Airport |  | ES | 23 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 23 |
| 23 | Miami International Airport |  | US | 22 |
| 24 | Madrid Barajas International Airport |  | ES | 22 |
| 25 | Charles de Gaulle International Airport |  | FR | 22 |
| 26 | Amsterdam Airport Schiphol |  | NL | 22 |
| 27 | VGZR |  |  | 21 |
| 28 | Salt Lake City International Airport |  | US | 21 |
| 29 | Bengaluru International Airport |  | IN | 20 |
| 30 | Charlotte/Douglas International Airport |  | US | 19 |
| 31 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 32 | Centennial Airport |  | US | 19 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 18 |
| 34 | Reno/Tahoe International Airport |  | US | 18 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 18 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 18 |
| 37 | Zhuhai Airport |  | CN | 17 |
| 38 | Helsinki Vantaa Airport |  | FI | 17 |
| 39 | Don Mueang International Airport |  | TH | 17 |
| 40 | Perales Airport |  | CO | 17 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 18 | 26m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 17 | 14m | 114 km | 33.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 4 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 13 | 24m | 99 km | 22.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 8 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 10 | 25m | 152 km | 26.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 7 | 52m | 136 km | 16.4 t |
| 17 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 7 | 34m | 69 km | 8.4 t |
| 18 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 22 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 23 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 25 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 6 | 14m | - | - |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 6 | 4m | - | - |
| 27 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 5 | 1h 20m | 967 km | 83.4 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 29 | VGZR (VGZR) | Lengpui Airport (VELP) | 5 | 22m | - | - |
| 30 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGFDE | CGF | Montréal / St-Hubert Airport (CYHU) | Montréal / St-Hubert Airport (CYHU) | 2026-03-29 16:50 UTC | 2026-03-29 17:32 UTC | 42m |
| N342FG |  | Rocky Mountain Metro Airport (KBJC) | Vance Brand Airport (KLMO) | 2026-03-29 17:08 UTC | 2026-03-29 17:31 UTC | 23m |
| NRL30 | NRL | Montréal (Mirabel) Airport (CYMX) | Weymontachie Airport (CSU5) | 2026-03-29 16:44 UTC | 2026-03-29 17:28 UTC | 43m |
| N410FC |  | Chicago Executive Airport (KPWK) | Ruder Airport (59IL) | 2026-03-29 16:37 UTC | 2026-03-29 17:24 UTC | 46m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-29 17:05 UTC | 2026-03-29 17:21 UTC | 15m |
| N248SF |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-03-29 16:28 UTC | 2026-03-29 17:17 UTC | 49m |
| N4547F |  | Mc Clellan-Palomar Airport (KCRQ) | Big Bear City Airport (KL35) | 2026-03-29 16:36 UTC | 2026-03-29 17:16 UTC | 40m |
| N2744W |  | Rocky Mountain Metro Airport (KBJC) | CO86 (CO86) | 2026-03-29 16:46 UTC | 2026-03-29 17:11 UTC | 24m |
| N8172Q |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-03-29 16:52 UTC | 2026-03-29 17:10 UTC | 17m |
| N517AF |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-03-29 16:36 UTC | 2026-03-29 17:07 UTC | 31m |
| FDB829 | flydubai | Shaibah Airport (OESB) | Shaibah Airport (OESB) | 2026-03-29 11:28 UTC | 2026-03-29 17:02 UTC | 5h 34m |
| N7562G |  | Gdap Air Ranch Airport (97TS) | Gdap Air Ranch Airport (97TS) | 2026-03-29 17:01 UTC | 2026-03-29 17:02 UTC | 1m |
| JKR56 | JKR | Fort Lauderdale/Hollywood International Airport (KFLL) | Teterboro Airport (KTEB) | 2026-03-29 14:27 UTC | 2026-03-29 16:58 UTC | 2h 31m |
| N560FW |  | Fort Worth Meacham International Airport (KFTW) | Quanah Municipal Airport (KF01) | 2026-03-29 16:27 UTC | 2026-03-29 16:58 UTC | 30m |
| N40288 |  | K5G6 (K5G6) | Ponderosa Airport (4PA5) | 2026-03-29 16:51 UTC | 2026-03-29 16:57 UTC | 6m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-03-29 16:17 UTC | 2026-03-29 16:56 UTC | 39m |
| KLM44T | KLM Royal Dutch | Nantes Atlantique Airport (LFRS) | Amsterdam Airport Schiphol (EHAM) | 2026-03-29 15:36 UTC | 2026-03-29 16:54 UTC | 1h 18m |
| N905JA |  | Modesto City-County-Harry Sham Field (KMOD) | Palo Alto Airport (KPAO) | 2026-03-29 16:23 UTC | 2026-03-29 16:52 UTC | 28m |
| DFBWG | DFB | La Mole Airport (LFTZ) | Frankfurt-Egelsbach Airport (EDFE) | 2026-03-29 14:41 UTC | 2026-03-29 16:51 UTC | 2h 10m |
| JBU2831 | JetBlue | Orlando International Airport (KMCO) | Harry Reid International Airport (KLAS) | 2026-03-29 12:17 UTC | 2026-03-29 16:51 UTC | 4h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
