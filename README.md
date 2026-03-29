# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_22:59:35_UTC-green)

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

**Latest saved flight:** 2026-03-29 22:59:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 22:59:35 UTC

- **3,504** saved flights
- **2,627** unique routes
- **98** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,504** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **46,176.3 tonnes** estimated CO2 emissions
- **2,676,887 km** total distance flown
- **901 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 195 |
| 2 | Ryanair | 124 |
| 3 | EJA | 86 |
| 4 | IndiGo | 80 |
| 5 | American Airlines | 77 |
| 6 | Southwest Airlines | 66 |
| 7 | ENY | 59 |
| 8 | Lufthansa | 53 |
| 9 | Delta Air Lines | 39 |
| 10 | AXM | 38 |
| 11 | LATAM Airlines | 37 |
| 12 | LXJ | 36 |
| 13 | Vueling | 36 |
| 14 | United Airlines | 31 |
| 15 | Cathay Pacific | 27 |
| 16 | VIV | 27 |
| 17 | Avianca | 26 |
| 18 | EDV | 23 |
| 19 | Swiss International | 22 |
| 20 | WIF | 22 |
| 21 | Alaska Airlines | 21 |
| 22 | All Nippon Airways | 20 |
| 23 | ARE | 20 |
| 24 | AXB | 19 |
| 25 | MXY | 19 |
| 26 | Japan Airlines | 18 |
| 27 | JIA | 18 |
| 28 | QLK | 18 |
| 29 | VOE | 18 |
| 30 | AZU | 17 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3243 |
| 2 | 🇪🇸 ES | 272 |
| 3 | 🇮🇳 IN | 224 |
| 4 | 🇨🇴 CO | 213 |
| 5 | 🇦🇺 AU | 164 |
| 6 | 🇧🇷 BR | 163 |
| 7 | 🇩🇪 DE | 157 |
| 8 | 🇨🇦 CA | 150 |
| 9 | 🇲🇽 MX | 144 |
| 10 | 🇮🇹 IT | 136 |
| 11 | 🇯🇵 JP | 134 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇬🇹 GT | 98 |
| 14 | 🇫🇷 FR | 93 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 74 |
| 18 | 🇳🇴 NO | 69 |
| 19 | 🇬🇷 GR | 66 |
| 20 | 🇵🇭 PH | 65 |
| 21 | 🇹🇷 TR | 48 |
| 22 | 🇧🇸 BS | 46 |
| 23 | 🇹🇭 TH | 45 |
| 24 | 🇳🇿 NZ | 42 |
| 25 | 🇵🇱 PL | 42 |
| 26 | 🇲🇴 MO | 40 |
| 27 | 🇲🇦 MA | 39 |
| 28 | 🇫🇮 FI | 38 |
| 29 | 🇮🇩 ID | 37 |
| 30 | 🇳🇱 NL | 32 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 97 |
| 2 | Denver International Airport |  | US | 76 |
| 3 | El Dorado International Airport |  | CO | 76 |
| 4 | La Aurora Airport |  | GT | 64 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Indira Gandhi International Airport |  | IN | 51 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 49 |
| 9 | Tenerife Norte Airport |  | ES | 49 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 46 |
| 11 | Harry Reid International Airport |  | US | 45 |
| 12 | Tokyo International Airport |  | JP | 44 |
| 13 | Chicago O'Hare International Airport |  | US | 43 |
| 14 | Macau International Airport |  | MO | 40 |
| 15 | Zurich Airport |  | CH | 37 |
| 16 | Charlotte/Douglas International Airport |  | US | 36 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 36 |
| 18 | Miami International Airport |  | US | 33 |
| 19 | Kuala Lumpur International Airport |  | MY | 33 |
| 20 | Reno/Tahoe International Airport |  | US | 32 |
| 21 | O. R. Tambo International Airport |  | ZA | 30 |
| 22 | Madrid Barajas International Airport |  | ES | 29 |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 24 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 25 | Centennial Airport |  | US | 28 |
| 26 | Salt Lake City International Airport |  | US | 28 |
| 27 | CO86 |  |  | 27 |
| 28 | Vitoria/Foronda Airport |  | ES | 27 |
| 29 | Sydney Kingsford Smith International Airport |  | AU | 27 |
| 30 | Ninoy Aquino International Airport |  | PH | 27 |
| 31 | George Bush Intcntl/Houston Airport |  | US | 27 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 27 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 26 |
| 34 | Los Angeles International Airport |  | US | 25 |
| 35 | Tampa International Airport |  | US | 25 |
| 36 | Charles de Gaulle International Airport |  | FR | 25 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 38 | Amsterdam Airport Schiphol |  | NL | 25 |
| 39 | Perales Airport |  | CO | 24 |
| 40 | Bengaluru International Airport |  | IN | 23 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 24 | 14m | 114 km | 47.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 10 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 11 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 9 | 1h 55m | 1,304 km | 202.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 17 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 18 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 19 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 23 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 7 | 8h 38m | 38 km | 4.6 t |
| 24 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 7 | 54m | 630 km | 76.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 7 | 4m | - | - |
| 27 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 6 | 1h 49m | - | - |
| 28 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 6 | 29m | 369 km | 38.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHILD1 | CHI | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-03-29 22:49 UTC | 2026-03-29 22:59 UTC | 10m |
| N916FT |  | Oxnard Airport (KOXR) | Van Nuys Airport (KVNY) | 2026-03-29 22:21 UTC | 2026-03-29 22:48 UTC | 27m |
| MWH1 | MWH | Bellingham International Airport (KBLI) | William R Fairchild International Airport (KCLM) | 2026-03-29 21:36 UTC | 2026-03-29 22:42 UTC | 1h 5m |
| N1417M |  | San Gabriel Valley Airport (KEMT) | Big Bear City Airport (KL35) | 2026-03-29 22:08 UTC | 2026-03-29 22:41 UTC | 32m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-03-29 21:48 UTC | 2026-03-29 22:41 UTC | 53m |
| N130TP |  | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-03-29 22:33 UTC | 2026-03-29 22:39 UTC | 5m |
| N248PH |  | Redding Regional Airport (KRDD) | Hayfork Airport (KF62) | 2026-03-29 22:22 UTC | 2026-03-29 22:38 UTC | 15m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-03-29 22:03 UTC | 2026-03-29 22:37 UTC | 34m |
| N5726B |  | Minden-Tahoe Airport (KMEV) | Mariposa-Yosemite Airport (KMPI) | 2026-03-29 21:51 UTC | 2026-03-29 22:36 UTC | 44m |
| EJA524 | EJA | Monterey Regional Airport (KMRY) | Oakland San Francisco Bay Airport (KOAK) | 2026-03-29 22:11 UTC | 2026-03-29 22:36 UTC | 24m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-03-29 22:06 UTC | 2026-03-29 22:33 UTC | 27m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-29 15:09 UTC | 2026-03-29 22:33 UTC | 7h 23m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-03-29 22:20 UTC | 2026-03-29 22:31 UTC | 10m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-03-29 22:00 UTC | 2026-03-29 22:29 UTC | 28m |
| YLH | YLH | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-03-29 21:59 UTC | 2026-03-29 22:28 UTC | 29m |
| EJA480 | EJA | Mc Clellan-Palomar Airport (KCRQ) | Oakland San Francisco Bay Airport (KOAK) | 2026-03-29 21:22 UTC | 2026-03-29 22:27 UTC | 1h 4m |
| N960DT |  | Washington Dulles International Airport (KIAD) | Scottsdale Airport (KSDL) | 2026-03-29 18:14 UTC | 2026-03-29 22:26 UTC | 4h 12m |
| N3455L |  | Redhead Airport (FD35) | Woodridge Field (VG52) | 2026-03-29 20:21 UTC | 2026-03-29 22:21 UTC | 1h 59m |
| ZFY | ZFY | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-03-29 22:13 UTC | 2026-03-29 22:20 UTC | 6m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-03-29 10:49 UTC | 2026-03-29 22:19 UTC | 11h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
