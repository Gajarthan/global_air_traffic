# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_16:05:26_UTC-green)

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

**Latest saved flight:** 2026-03-29 16:05:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 16:05:26 UTC

- **2,315** saved flights
- **1,806** unique routes
- **90** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,315** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **31,207.0 tonnes** estimated CO2 emissions
- **1,809,099 km** total distance flown
- **910 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 98 |
| 2 | Ryanair | 81 |
| 3 | IndiGo | 71 |
| 4 | Lufthansa | 43 |
| 5 | Southwest Airlines | 42 |
| 6 | EJA | 41 |
| 7 | American Airlines | 40 |
| 8 | AXM | 38 |
| 9 | ENY | 37 |
| 10 | Delta Air Lines | 24 |
| 11 | Vueling | 24 |
| 12 | LATAM Airlines | 22 |
| 13 | United Airlines | 22 |
| 14 | Cathay Pacific | 21 |
| 15 | All Nippon Airways | 20 |
| 16 | Japan Airlines | 18 |
| 17 | LXJ | 18 |
| 18 | Swiss International | 18 |
| 19 | AXB | 17 |
| 20 | BRC | 17 |
| 21 | ARE | 16 |
| 22 | Avianca | 16 |
| 23 | VIV | 15 |
| 24 | AEE | 14 |
| 25 | EDV | 14 |
| 26 | SFR | 14 |
| 27 | VOE | 14 |
| 28 | APG | 13 |
| 29 | Alaska Airlines | 13 |
| 30 | AZU | 13 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1877 |
| 2 | 🇮🇳 IN | 198 |
| 3 | 🇪🇸 ES | 187 |
| 4 | 🇨🇴 CO | 144 |
| 5 | 🇯🇵 JP | 132 |
| 6 | 🇦🇺 AU | 125 |
| 7 | 🇩🇪 DE | 125 |
| 8 | 🇮🇹 IT | 97 |
| 9 | 🇧🇷 BR | 96 |
| 10 | 🇨🇦 CA | 85 |
| 11 | 🇬🇧 GB | 84 |
| 12 | 🇲🇾 MY | 79 |
| 13 | 🇲🇽 MX | 78 |
| 14 | 🇿🇦 ZA | 76 |
| 15 | 🇬🇹 GT | 67 |
| 16 | 🇵🇭 PH | 61 |
| 17 | 🇫🇷 FR | 60 |
| 18 | 🇨🇭 CH | 59 |
| 19 | 🇬🇷 GR | 56 |
| 20 | 🇹🇭 TH | 44 |
| 21 | 🇹🇷 TR | 43 |
| 22 | 🇳🇴 NO | 38 |
| 23 | 🇵🇱 PL | 34 |
| 24 | 🇮🇩 ID | 33 |
| 25 | 🇲🇴 MO | 30 |
| 26 | 🇫🇮 FI | 28 |
| 27 | 🇲🇦 MA | 28 |
| 28 | 🇧🇸 BS | 27 |
| 29 | 🇰🇷 KR | 26 |
| 30 | 🇳🇱 NL | 25 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 52 |
| 2 | El Dorado International Airport |  | CO | 52 |
| 3 | Frankfurt am Main International Airport |  | DE | 47 |
| 4 | Tokyo International Airport |  | JP | 44 |
| 5 | Indira Gandhi International Airport |  | IN | 42 |
| 6 | La Aurora Airport |  | GT | 42 |
| 7 | Denver International Airport |  | US | 38 |
| 8 | Guaymaral Airport |  | CO | 37 |
| 9 | Kuala Lumpur International Airport |  | MY | 32 |
| 10 | Tenerife Norte Airport |  | ES | 30 |
| 11 | Macau International Airport |  | MO | 30 |
| 12 | Zurich Airport |  | CH | 29 |
| 13 | O. R. Tambo International Airport |  | ZA | 28 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 27 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 26 |
| 16 | Ninoy Aquino International Airport |  | PH | 25 |
| 17 | Chicago O'Hare International Airport |  | US | 24 |
| 18 | Harry Reid International Airport |  | US | 24 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 24 |
| 20 | Eleftherios Venizelos International Airport |  | GR | 23 |
| 21 | Madrid Barajas International Airport |  | ES | 21 |
| 22 | Vitoria/Foronda Airport |  | ES | 21 |
| 23 | Charles de Gaulle International Airport |  | FR | 21 |
| 24 | Miami International Airport |  | US | 20 |
| 25 | Bengaluru International Airport |  | IN | 20 |
| 26 | VGZR |  |  | 20 |
| 27 | Amsterdam Airport Schiphol |  | NL | 20 |
| 28 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 19 |
| 30 | Centennial Airport |  | US | 18 |
| 31 | Zhuhai Airport |  | CN | 17 |
| 32 | Don Mueang International Airport |  | TH | 17 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 17 |
| 34 | Wasig Airport |  | PH | 16 |
| 35 | Perales Airport |  | CO | 16 |
| 36 | Salt Lake City International Airport |  | US | 16 |
| 37 | Newcastle Airport |  | ZA | 16 |
| 38 | Soekarno-Hatta International Airport |  | ID | 15 |
| 39 | Charlotte/Douglas International Airport |  | US | 15 |
| 40 | Los Angeles International Airport |  | US | 15 |

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
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 9 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 11 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 9 | 12m | 99 km | 15.4 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 9 | 25m | 152 km | 23.5 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 7 | 21m | 165 km | 19.9 t |
| 15 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 7 | 52m | 136 km | 16.4 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 20 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 6 | 37m | 69 km | 7.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 5 | 1h 44m | 1,290 km | 111.3 t |
| 26 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 27 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 28 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 5 | 30m | 127 km | 10.9 t |
| 29 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 5 | 14m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N826HW |  | Moraine Air Park (KI73) | Moraine Air Park (KI73) | 2026-03-29 15:46 UTC | 2026-03-29 16:05 UTC | 18m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-03-29 15:45 UTC | 2026-03-29 16:02 UTC | 16m |
| N84JS |  | Glendale Regional Airport (KGEU) | Phoenix Deer Valley Airport (KDVT) | 2026-03-29 14:36 UTC | 2026-03-29 15:59 UTC | 1h 23m |
| N6974H |  | Bob Maxwell Memorial Airfield (KOKB) | Hemet-Ryan Airport (KHMT) | 2026-03-29 15:33 UTC | 2026-03-29 15:58 UTC | 24m |
| HTY218 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-03-29 15:30 UTC | 2026-03-29 15:57 UTC | 26m |
| N276DB |  | Falcon Field (KFFZ) | Sarita Airport (37AZ) | 2026-03-29 14:51 UTC | 2026-03-29 15:52 UTC | 1h 0m |
| N1031X |  | Eagle Soaring Airport (1CD4) | Yampa Valley Airport (KHDN) | 2026-03-29 15:43 UTC | 2026-03-29 15:47 UTC | 3m |
| DABBA | DAB | Palma De Mallorca Airport (LEPA) | Raron Airport (LSTA) | 2026-03-29 14:28 UTC | 2026-03-29 15:43 UTC | 1h 14m |
| N9730V |  | 19TE (19TE) | Cleveland Municipal Airport (K6R3) | 2026-03-29 15:36 UTC | 2026-03-29 15:42 UTC | 6m |
| N284L |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-03-29 14:17 UTC | 2026-03-29 15:42 UTC | 1h 24m |
| BSM36 | BSM | Durant Regional/Eaker Field (KDUA) | Sandy Creek Ranch Airport (TX47) | 2026-03-29 15:35 UTC | 2026-03-29 15:36 UTC | 1m |
| MNB213 | MNB | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 16:20 UTC | 2026-03-29 15:36 UTC | 23h 15m |
| PVL852 | PVL | Québec City Jean Lesage International Airport (CYQB) | Gaspe (Michel-Pouliot) Airport (CYGP) | 2026-03-29 14:27 UTC | 2026-03-29 15:34 UTC | 1h 7m |
| DLH276 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Linate Airport (LIML) | 2026-03-29 14:44 UTC | 2026-03-29 15:32 UTC | 47m |
| CYT90 | CYT | Lovell Field (KCHA) | Bessemer Ntl Airport (KEKY) | 2026-03-29 14:50 UTC | 2026-03-29 15:28 UTC | 38m |
| TGMRP | TGM | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-03-29 15:07 UTC | 2026-03-29 15:28 UTC | 21m |
| N555WZ |  | Northwest Arkansas Ntl Airport (KXNA) | 27CO (27CO) | 2026-03-29 13:24 UTC | 2026-03-29 15:28 UTC | 2h 4m |
| PIZ73 | PIZ | Paris-Le Bourget Airport (LFPB) | Samedan Airport (LSZS) | 2026-03-29 14:09 UTC | 2026-03-29 15:27 UTC | 1h 18m |
| COL1910 | COL | Spirit Of St Louis Airport (KSUS) | Oakland San Francisco Bay Airport (KOAK) | 2026-03-29 11:27 UTC | 2026-03-29 15:27 UTC | 3h 59m |
| XAUVL | XAU | General Ignacio P. Garcia International Airport (MMHO) | General Ignacio P. Garcia International Airport (MMHO) | 2026-03-29 14:27 UTC | 2026-03-29 15:26 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
