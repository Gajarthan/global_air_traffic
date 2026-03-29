# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_16:49:27_UTC-green)

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

**Latest saved flight:** 2026-03-29 16:49:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 16:49:27 UTC

- **2,432** saved flights
- **1,891** unique routes
- **92** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,432** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **32,734.3 tonnes** estimated CO2 emissions
- **1,897,639 km** total distance flown
- **910 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 103 |
| 2 | Ryanair | 82 |
| 3 | IndiGo | 73 |
| 4 | Lufthansa | 47 |
| 5 | EJA | 45 |
| 6 | Southwest Airlines | 44 |
| 7 | American Airlines | 43 |
| 8 | ENY | 40 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 25 |
| 11 | Vueling | 25 |
| 12 | LATAM Airlines | 24 |
| 13 | United Airlines | 22 |
| 14 | Cathay Pacific | 21 |
| 15 | All Nippon Airways | 20 |
| 16 | LXJ | 20 |
| 17 | Japan Airlines | 18 |
| 18 | Swiss International | 18 |
| 19 | AXB | 17 |
| 20 | BRC | 17 |
| 21 | ARE | 16 |
| 22 | Avianca | 16 |
| 23 | EDV | 16 |
| 24 | VIV | 16 |
| 25 | WIF | 16 |
| 26 | AEE | 14 |
| 27 | APG | 14 |
| 28 | Alaska Airlines | 14 |
| 29 | SFR | 14 |
| 30 | VOE | 14 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1994 |
| 2 | 🇮🇳 IN | 202 |
| 3 | 🇪🇸 ES | 194 |
| 4 | 🇨🇴 CO | 148 |
| 5 | 🇩🇪 DE | 133 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇦🇺 AU | 125 |
| 8 | 🇧🇷 BR | 104 |
| 9 | 🇮🇹 IT | 102 |
| 10 | 🇨🇦 CA | 92 |
| 11 | 🇬🇧 GB | 87 |
| 12 | 🇲🇽 MX | 82 |
| 13 | 🇲🇾 MY | 81 |
| 14 | 🇿🇦 ZA | 78 |
| 15 | 🇬🇹 GT | 70 |
| 16 | 🇨🇭 CH | 63 |
| 17 | 🇵🇭 PH | 63 |
| 18 | 🇫🇷 FR | 61 |
| 19 | 🇬🇷 GR | 56 |
| 20 | 🇳🇴 NO | 50 |
| 21 | 🇹🇭 TH | 44 |
| 22 | 🇹🇷 TR | 43 |
| 23 | 🇵🇱 PL | 35 |
| 24 | 🇮🇩 ID | 33 |
| 25 | 🇫🇮 FI | 32 |
| 26 | 🇲🇦 MA | 31 |
| 27 | 🇲🇴 MO | 31 |
| 28 | 🇧🇸 BS | 28 |
| 29 | 🇰🇷 KR | 26 |
| 30 | 🇳🇱 NL | 25 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 56 |
| 2 | El Dorado International Airport |  | CO | 52 |
| 3 | Frankfurt am Main International Airport |  | DE | 49 |
| 4 | Tokyo International Airport |  | JP | 44 |
| 5 | La Aurora Airport |  | GT | 44 |
| 6 | Indira Gandhi International Airport |  | IN | 43 |
| 7 | Denver International Airport |  | US | 41 |
| 8 | Guaymaral Airport |  | CO | 39 |
| 9 | Kuala Lumpur International Airport |  | MY | 33 |
| 10 | Tenerife Norte Airport |  | ES | 31 |
| 11 | Macau International Airport |  | MO | 31 |
| 12 | Zurich Airport |  | CH | 29 |
| 13 | O. R. Tambo International Airport |  | ZA | 29 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 28 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 27 |
| 16 | Harry Reid International Airport |  | US | 26 |
| 17 | Ninoy Aquino International Airport |  | PH | 26 |
| 18 | Chicago O'Hare International Airport |  | US | 25 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 20 | Eleftherios Venizelos International Airport |  | GR | 23 |
| 21 | Miami International Airport |  | US | 22 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 22 |
| 23 | Madrid Barajas International Airport |  | ES | 21 |
| 24 | Vitoria/Foronda Airport |  | ES | 21 |
| 25 | Charles de Gaulle International Airport |  | FR | 21 |
| 26 | Bengaluru International Airport |  | IN | 20 |
| 27 | VGZR |  |  | 20 |
| 28 | Amsterdam Airport Schiphol |  | NL | 20 |
| 29 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 30 | Centennial Airport |  | US | 18 |
| 31 | Salt Lake City International Airport |  | US | 18 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 18 |
| 33 | Zhuhai Airport |  | CN | 17 |
| 34 | Helsinki Vantaa Airport |  | FI | 17 |
| 35 | Don Mueang International Airport |  | TH | 17 |
| 36 | Seattle-Tacoma International Airport |  | US | 17 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 17 |
| 38 | Reno/Tahoe International Airport |  | US | 16 |
| 39 | Wasig Airport |  | PH | 16 |
| 40 | Perales Airport |  | CO | 16 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 16 | 14m | 114 km | 31.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 15 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 4 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 11 | 25m | 99 km | 18.8 t |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 10 | 1h 39m | 1,423 km | 245.4 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 10 | 25m | 152 km | 26.1 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 12 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 9 | 12m | 99 km | 15.4 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 15 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 7 | 52m | 136 km | 16.4 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 6 | 1h 44m | 1,290 km | 133.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 21 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 6 | 37m | 69 km | 7.2 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 26 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 27 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 28 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 5 | 30m | 127 km | 10.9 t |
| 29 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 5 | 12m | - | - |
| 30 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 5 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N10BB |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-03-29 15:37 UTC | 2026-03-29 16:49 UTC | 1h 11m |
| CPV369 | CPV | Linate Airport (LIML) | Villanova D'Albenga International Airport (LIMG) | 2026-03-29 16:09 UTC | 2026-03-29 16:44 UTC | 34m |
| RGA02 | RGA | Mollis Airport (LSZM) | Fricktal-Schupfart Airport (LSZI) | 2026-03-29 16:30 UTC | 2026-03-29 16:42 UTC | 12m |
| AR2 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami Executive Airport (KTMB) | 2026-03-29 16:11 UTC | 2026-03-29 16:41 UTC | 29m |
| DLH752 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Shaibah Airport (OESB) | 2026-03-29 11:19 UTC | 2026-03-29 16:40 UTC | 5h 20m |
| N40288 |  | St Marys Municipal Airport (KOYM) | Ponderosa Airport (4PA5) | 2026-03-29 15:58 UTC | 2026-03-29 16:40 UTC | 41m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-03-29 16:21 UTC | 2026-03-29 16:34 UTC | 13m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-03-29 15:27 UTC | 2026-03-29 16:32 UTC | 1h 4m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-03-29 15:29 UTC | 2026-03-29 16:31 UTC | 1h 2m |
| N6333E |  | 4MN4 (4MN4) | 4MN4 (4MN4) | 2026-03-29 16:22 UTC | 2026-03-29 16:31 UTC | 9m |
| N916SY |  | Scottsdale Airport (KSDL) | 42AZ (42AZ) | 2026-03-29 16:13 UTC | 2026-03-29 16:31 UTC | 18m |
| N186CS |  | Palo Alto Airport (KPAO) | Hayward Executive Airport (KHWD) | 2026-03-29 15:48 UTC | 2026-03-29 16:28 UTC | 39m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-03-29 16:05 UTC | 2026-03-29 16:27 UTC | 22m |
| N359RX |  | North Central West Virginia Airport (KCKB) | Ruth Field (WV28) | 2026-03-29 14:31 UTC | 2026-03-29 16:21 UTC | 1h 50m |
| N2416Q |  | Skylark Field (KILE) | Skylark Field (KILE) | 2026-03-29 15:59 UTC | 2026-03-29 16:18 UTC | 18m |
| OKALT | OKA | Brno-Turany Airport (LKTB) | Raron Airport (LSTA) | 2026-03-29 14:20 UTC | 2026-03-29 16:18 UTC | 1h 58m |
| N8397L |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-03-29 15:36 UTC | 2026-03-29 16:17 UTC | 41m |
| QTR8796 | Qatar Airways | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-03-29 05:17 UTC | 2026-03-29 16:17 UTC | 11h 0m |
| HTY131 | HTY | Gibraltar Airport (LXGB) | Gibraltar Airport (LXGB) | 2026-03-29 16:07 UTC | 2026-03-29 16:17 UTC | 9m |
| EJA431 | EJA | Ohio State University Airport (KOSU) | Witham Field (KSUA) | 2026-03-29 14:05 UTC | 2026-03-29 16:14 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
