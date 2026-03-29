# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_10:04:20_UTC-green)

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

**Latest saved flight:** 2026-03-29 10:04:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 10:04:20 UTC

- **1,623** saved flights
- **1,326** unique routes
- **82** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,623** saved routes in the archive
- **1h 22m** average flight duration

### Carbon Footprint Estimate

- **22,155.6 tonnes** estimated CO2 emissions
- **1,284,380 km** total distance flown
- **931 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 50 |
| 3 | Southwest Airlines | 40 |
| 4 | IndiGo | 37 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | ENY | 30 |
| 8 | AXM | 22 |
| 9 | United Airlines | 22 |
| 10 | Delta Air Lines | 20 |
| 11 | BRC | 17 |
| 12 | LXJ | 17 |
| 13 | Japan Airlines | 16 |
| 14 | All Nippon Airways | 15 |
| 15 | Cathay Pacific | 15 |
| 16 | LATAM Airlines | 15 |
| 17 | Lufthansa | 14 |
| 18 | Vueling | 14 |
| 19 | Alaska Airlines | 13 |
| 20 | Avianca | 12 |
| 21 | QLK | 12 |
| 22 | SFR | 12 |
| 23 | APG | 11 |
| 24 | EDV | 11 |
| 25 | VIV | 11 |
| 26 | JST | 10 |
| 27 | AZU | 8 |
| 28 | LYM | 8 |
| 29 | TGC | 8 |
| 30 | VOE | 8 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1554 |
| 2 | 🇦🇺 AU | 115 |
| 3 | 🇯🇵 JP | 106 |
| 4 | 🇮🇳 IN | 106 |
| 5 | 🇪🇸 ES | 96 |
| 6 | 🇨🇴 CO | 89 |
| 7 | 🇨🇦 CA | 69 |
| 8 | 🇲🇽 MX | 65 |
| 9 | 🇮🇹 IT | 55 |
| 10 | 🇬🇹 GT | 55 |
| 11 | 🇵🇭 PH | 53 |
| 12 | 🇩🇪 DE | 53 |
| 13 | 🇧🇷 BR | 53 |
| 14 | 🇬🇧 GB | 48 |
| 15 | 🇲🇾 MY | 45 |
| 16 | 🇿🇦 ZA | 42 |
| 17 | 🇬🇷 GR | 30 |
| 18 | 🇫🇷 FR | 27 |
| 19 | 🇹🇭 TH | 26 |
| 20 | 🇮🇩 ID | 24 |
| 21 | 🇰🇷 KR | 23 |
| 22 | 🇨🇭 CH | 23 |
| 23 | 🇳🇿 NZ | 22 |
| 24 | 🇲🇴 MO | 22 |
| 25 | 🇹🇷 TR | 20 |
| 26 | 🇵🇱 PL | 17 |
| 27 | 🇲🇦 MA | 16 |
| 28 | 🇧🇸 BS | 16 |
| 29 | 🇳🇱 NL | 15 |
| 30 | 🇭🇳 HN | 14 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | La Aurora Airport |  | GT | 34 |
| 4 | Tokyo International Airport |  | JP | 32 |
| 5 | El Dorado International Airport |  | CO | 32 |
| 6 | Indira Gandhi International Airport |  | IN | 24 |
| 7 | Guaymaral Airport |  | CO | 24 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 9 | Chicago O'Hare International Airport |  | US | 22 |
| 10 | Ninoy Aquino International Airport |  | PH | 22 |
| 11 | Macau International Airport |  | MO | 22 |
| 12 | Harry Reid International Airport |  | US | 21 |
| 13 | Frankfurt am Main International Airport |  | DE | 21 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 16 | Kuala Lumpur International Airport |  | MY | 18 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 18 | Miami International Airport |  | US | 17 |
| 19 | Tenerife Norte Airport |  | ES | 17 |
| 20 | Wasig Airport |  | PH | 16 |
| 21 | Salt Lake City International Airport |  | US | 16 |
| 22 | Los Angeles International Airport |  | US | 15 |
| 23 | Seattle-Tacoma International Airport |  | US | 15 |
| 24 | Amsterdam Airport Schiphol |  | NL | 14 |
| 25 | Tampa International Airport |  | US | 14 |
| 26 | O. R. Tambo International Airport |  | ZA | 14 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 14 |
| 28 | Eleftherios Venizelos International Airport |  | GR | 13 |
| 29 | CO86 |  |  | 13 |
| 30 | The Florida Keys Marathon International Airport |  | US | 13 |
| 31 | Reno/Tahoe International Airport |  | US | 13 |
| 32 | Zhuhai Airport |  | CN | 13 |
| 33 | Vancouver International Airport |  | CA | 13 |
| 34 | Vitoria/Foronda Airport |  | ES | 13 |
| 35 | Zurich Airport |  | CH | 13 |
| 36 | Bengaluru International Airport |  | IN | 13 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 38 | Soekarno-Hatta International Airport |  | ID | 12 |
| 39 | Daniel K Inouye International Airport |  | US | 12 |
| 40 | Yampa Valley Airport |  | US | 12 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 9 | 20m | 250 km | 38.9 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 7 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 6 | 28m | 304 km | 31.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 6 | 29m | 275 km | 28.4 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 6 | 22m | 252 km | 26.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 6 | 1h 6m | 706 km | 73.1 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 5 | 1h 40m | 1,423 km | 122.7 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 5 | 52m | 546 km | 47.1 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 17 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 4 | 30m | 369 km | 25.5 t |
| 20 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 4 | 11m | 127 km | 8.8 t |
| 23 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 4 | 9h 26m | 38 km | 2.6 t |
| 24 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 25 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 4 | 22m | 275 km | 19.0 t |
| 26 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 4 | 37m | 431 km | 29.7 t |
| 27 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 28 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 29 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 30 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSB507 | CSB | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-03-29 07:57 UTC | 2026-03-29 10:04 UTC | 2h 7m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-28 20:03 UTC | 2026-03-29 10:03 UTC | 13h 59m |
| GTI8507 | GTI | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-03-28 22:32 UTC | 2026-03-29 09:58 UTC | 11h 26m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-03-29 09:44 UTC | 2026-03-29 09:57 UTC | 13m |
| FHMLR | FHM | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-03-29 09:40 UTC | 2026-03-29 09:53 UTC | 13m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Zhuhai Airport (ZGSD) | 2026-03-28 23:05 UTC | 2026-03-29 09:50 UTC | 10h 44m |
| DHK814 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-03-28 22:47 UTC | 2026-03-29 09:47 UTC | 10h 59m |
| AXM136 | AXM | Kuala Lumpur International Airport (WMKK) | Chek Lap Kok International Airport (VHHH) | 2026-03-29 06:16 UTC | 2026-03-29 09:46 UTC | 3h 30m |
| BTK7041 | BTK | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-03-29 08:56 UTC | 2026-03-29 09:29 UTC | 33m |
| SVA984 | Saudia | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-03-28 17:04 UTC | 2026-03-29 09:23 UTC | 16h 18m |
| SHT6L | SHT | London Heathrow Airport (EGLL) | Glasgow International Airport (EGPF) | 2026-03-29 07:08 UTC | 2026-03-29 09:21 UTC | 2h 13m |
| N507ME |  | Allegheny County Airport (KAGC) | Allegheny County Airport (KAGC) | 2026-03-29 09:05 UTC | 2026-03-29 09:09 UTC | 4m |
| KLM1303 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-03-29 07:52 UTC | 2026-03-29 09:08 UTC | 1h 15m |
| AXM6044 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-29 08:42 UTC | 2026-03-29 09:07 UTC | 24m |
| ANA455 | All Nippon Airways | Tokyo International Airport (RJTT) | Kumamoto Airport (RJFT) | 2026-03-29 07:43 UTC | 2026-03-29 09:02 UTC | 1h 19m |
| N47296 |  | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-03-29 08:56 UTC | 2026-03-29 09:01 UTC | 5m |
| IGO2KY | IndiGo | Yongphulla Airport (VQ10) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-29 07:42 UTC | 2026-03-29 09:00 UTC | 1h 18m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-03-29 08:17 UTC | 2026-03-29 08:58 UTC | 41m |
| SDG234 | SDG | Hindon Airport (VIDX) | Ludhiana Airport (VILD) | 2026-03-29 08:27 UTC | 2026-03-29 08:56 UTC | 29m |
| AUA751W | Austrian Airlines | Vienna International Airport (LOWW) | Tivat Airport (LYTV) | 2026-03-29 08:05 UTC | 2026-03-29 08:56 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
