# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_13:49:45_UTC-green)

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

**Latest saved flight:** 2026-03-31 13:49:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 13:49:45 UTC

- **6,557** saved flights
- **4,279** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,557** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **83,229.0 tonnes** estimated CO2 emissions
- **4,824,869 km** total distance flown
- **874 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 245 |
| 3 | IndiGo | 177 |
| 4 | EJA | 131 |
| 5 | American Airlines | 122 |
| 6 | Lufthansa | 103 |
| 7 | Southwest Airlines | 101 |
| 8 | ENY | 93 |
| 9 | AXM | 77 |
| 10 | LATAM Airlines | 71 |
| 11 | Vueling | 67 |
| 12 | All Nippon Airways | 57 |
| 13 | LXJ | 57 |
| 14 | Delta Air Lines | 56 |
| 15 | QLK | 56 |
| 16 | Swiss International | 52 |
| 17 | WIF | 52 |
| 18 | AXB | 47 |
| 19 | Cathay Pacific | 47 |
| 20 | Japan Airlines | 47 |
| 21 | United Airlines | 47 |
| 22 | VIV | 46 |
| 23 | AZU | 45 |
| 24 | Alaska Airlines | 40 |
| 25 | EDV | 39 |
| 26 | Avianca | 38 |
| 27 | EJU | 36 |
| 28 | VOE | 35 |
| 29 | easyJet | 34 |
| 30 | Air India | 33 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5444 |
| 2 | 🇮🇳 IN | 542 |
| 3 | 🇦🇺 AU | 506 |
| 4 | 🇪🇸 ES | 498 |
| 5 | 🇯🇵 JP | 337 |
| 6 | 🇧🇷 BR | 329 |
| 7 | 🇩🇪 DE | 329 |
| 8 | 🇨🇴 CO | 303 |
| 9 | 🇮🇹 IT | 298 |
| 10 | 🇨🇦 CA | 275 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 224 |
| 13 | 🇫🇷 FR | 204 |
| 14 | 🇲🇾 MY | 174 |
| 15 | 🇳🇴 NO | 173 |
| 16 | 🇨🇭 CH | 162 |
| 17 | 🇿🇦 ZA | 155 |
| 18 | 🇬🇷 GR | 153 |
| 19 | 🇬🇹 GT | 134 |
| 20 | 🇵🇭 PH | 131 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 108 |
| 23 | 🇹🇭 TH | 92 |
| 24 | 🇮🇩 ID | 89 |
| 25 | 🇲🇴 MO | 81 |
| 26 | 🇵🇱 PL | 81 |
| 27 | 🇲🇦 MA | 79 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇲🇪 ME | 65 |
| 30 | 🇳🇱 NL | 61 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Indira Gandhi International Airport |  | IN | 124 |
| 3 | Denver International Airport |  | US | 122 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 113 |
| 6 | Frankfurt am Main International Airport |  | DE | 104 |
| 7 | La Aurora Airport |  | GT | 91 |
| 8 | Zurich Airport |  | CH | 84 |
| 9 | Harry Reid International Airport |  | US | 83 |
| 10 | Macau International Airport |  | MO | 81 |
| 11 | Chicago O'Hare International Airport |  | US | 76 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 72 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 68 |
| 16 | Tenerife Norte Airport |  | ES | 68 |
| 17 | Guaymaral Airport |  | CO | 67 |
| 18 | Kuala Lumpur International Airport |  | MY | 63 |
| 19 | Madrid Barajas International Airport |  | ES | 60 |
| 20 | Reno/Tahoe International Airport |  | US | 59 |
| 21 | Ninoy Aquino International Airport |  | PH | 59 |
| 22 | Bengaluru International Airport |  | IN | 59 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 53 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 25 | Malpensa International Airport |  | IT | 51 |
| 26 | Charles de Gaulle International Airport |  | FR | 51 |
| 27 | Charlotte/Douglas International Airport |  | US | 50 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 50 |
| 29 | Vitoria/Foronda Airport |  | ES | 49 |
| 30 | Salt Lake City International Airport |  | US | 49 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 32 | Miami International Airport |  | US | 46 |
| 33 | Congonhas Airport |  | BR | 45 |
| 34 | O. R. Tambo International Airport |  | ZA | 45 |
| 35 | Daniel K Inouye International Airport |  | US | 44 |
| 36 | Pune Airport |  | IN | 44 |
| 37 | Seattle-Tacoma International Airport |  | US | 44 |
| 38 | Amsterdam Airport Schiphol |  | NL | 43 |
| 39 | Centennial Airport |  | US | 43 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 42 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 32 | 14m | 114 km | 62.8 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 26 | 27m | - | - |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 20 | 24m | 99 km | 34.3 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 19 | 20m | 165 km | 54.0 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 18 | 1h 48m | 1,156 km | 359.1 t |
| 11 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 18 | 1h 41m | 1,423 km | 441.7 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 18 | 5m | - | - |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 17 | 15m | 206 km | 60.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 16 | 29m | 275 km | 75.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 19 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 12 | 1h 46m | 1,290 km | 267.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 12 | 23m | - | - |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N139UD |  | Willaview Airport (2DE2) | Delaware Airpark (K33N) | 2026-03-31 13:37 UTC | 2026-03-31 13:49 UTC | 12m |
| HB3472 |  | L'alpe D'huez Airport (LFHU) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-03-31 12:48 UTC | 2026-03-31 13:43 UTC | 54m |
| N1097T |  | Atlanta Regional Falcon Field (KFFC) | Newnan Coweta County Airport (KCCO) | 2026-03-31 12:39 UTC | 2026-03-31 13:38 UTC | 59m |
| RNGR755 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Alice International Airport (KALI) | 2026-03-31 13:16 UTC | 2026-03-31 13:32 UTC | 15m |
| DLH8C | Lufthansa | Zurich Airport (LSZH) | Frankfurt am Main International Airport (EDDF) | 2026-03-31 12:44 UTC | 2026-03-31 13:31 UTC | 46m |
| N2663X |  | Clute's Hilltop Airport (69NC) | Statesville Regional Airport (KSVH) | 2026-03-31 12:56 UTC | 2026-03-31 13:22 UTC | 25m |
| FGTYD | FGT | Grenoble-Isere Airport (LFLS) | Grenoble Le Versoud Airport (LFLG) | 2026-03-31 12:40 UTC | 2026-03-31 13:19 UTC | 38m |
| BTZ119 | BTZ | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-03-31 13:06 UTC | 2026-03-31 13:19 UTC | 13m |
| N46168 |  | Orlampa Inc Airport (FA08) | Orlampa Inc Airport (FA08) | 2026-03-31 12:46 UTC | 2026-03-31 13:19 UTC | 32m |
| HBVPL | HBV | Grenchen Airport (LSZG) | Bern Belp Airport (LSZB) | 2026-03-31 12:58 UTC | 2026-03-31 13:11 UTC | 13m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Hausen am Albis Airport (LSZN) | 2026-03-31 12:37 UTC | 2026-03-31 13:06 UTC | 28m |
| N738KA |  | Savannah/Hilton Head International Airport (KSAV) | Swaids Field (2GA2) | 2026-03-31 12:55 UTC | 2026-03-31 13:06 UTC | 10m |
| SYS90 | SYS | Sleap Airport (EGCV) | RAF Shawbury (EGOS) | 2026-03-31 12:10 UTC | 2026-03-31 13:06 UTC | 55m |
| HTY126 | HTY | Gibraltar Airport (LXGB) | Gibraltar Airport (LXGB) | 2026-03-31 12:55 UTC | 2026-03-31 13:04 UTC | 9m |
| N12VP |  | Sugar Land Regional Airport (KSGR) | TX11 (TX11) | 2026-03-31 12:03 UTC | 2026-03-31 13:04 UTC | 1h 1m |
| N32YA |  | Fort Lauderdale Executive Airport (KFXE) | Fort Lauderdale Executive Airport (KFXE) | 2026-03-31 12:00 UTC | 2026-03-31 13:04 UTC | 1h 4m |
| FD471 |  | Brisbane International Airport (YBBN) | Cherrabah Airport (YCHB) | 2026-03-31 12:36 UTC | 2026-03-31 13:00 UTC | 23m |
| FGRPV | FGR | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-03-31 12:45 UTC | 2026-03-31 12:57 UTC | 12m |
| N757NJ |  | Ocala International-Jim Taylor Field (KOCF) | Bartow Executive Airport (KBOW) | 2026-03-31 12:04 UTC | 2026-03-31 12:55 UTC | 51m |
| N131DA |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-03-31 12:07 UTC | 2026-03-31 12:55 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
