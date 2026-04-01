# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_15:21:54_UTC-green)

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

**Latest saved flight:** 2026-04-01 15:21:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 15:21:54 UTC

- **8,898** saved flights
- **5,420** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,898** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **107,837.1 tonnes** estimated CO2 emissions
- **6,251,423 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 393 |
| 2 | Ryanair | 342 |
| 3 | IndiGo | 252 |
| 4 | EJA | 175 |
| 5 | Lufthansa | 155 |
| 6 | American Airlines | 154 |
| 7 | Southwest Airlines | 134 |
| 8 | ENY | 121 |
| 9 | AXM | 102 |
| 10 | Vueling | 97 |
| 11 | LATAM Airlines | 89 |
| 12 | All Nippon Airways | 79 |
| 13 | LXJ | 74 |
| 14 | Delta Air Lines | 72 |
| 15 | WIF | 72 |
| 16 | QLK | 70 |
| 17 | Swiss International | 68 |
| 18 | AXB | 62 |
| 19 | AZU | 60 |
| 20 | Japan Airlines | 60 |
| 21 | VIV | 60 |
| 22 | Alaska Airlines | 56 |
| 23 | BRC | 54 |
| 24 | EDV | 54 |
| 25 | United Airlines | 54 |
| 26 | Avianca | 50 |
| 27 | EJU | 50 |
| 28 | easyJet | 50 |
| 29 | Cathay Pacific | 49 |
| 30 | JST | 46 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7235 |
| 2 | 🇮🇳 IN | 778 |
| 3 | 🇪🇸 ES | 703 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 497 |
| 6 | 🇯🇵 JP | 459 |
| 7 | 🇧🇷 BR | 443 |
| 8 | 🇨🇦 CA | 415 |
| 9 | 🇨🇴 CO | 414 |
| 10 | 🇮🇹 IT | 404 |
| 11 | 🇬🇧 GB | 318 |
| 12 | 🇲🇽 MX | 308 |
| 13 | 🇫🇷 FR | 281 |
| 14 | 🇳🇴 NO | 239 |
| 15 | 🇲🇾 MY | 228 |
| 16 | 🇨🇭 CH | 211 |
| 17 | 🇬🇷 GR | 206 |
| 18 | 🇳🇿 NZ | 197 |
| 19 | 🇿🇦 ZA | 193 |
| 20 | 🇬🇹 GT | 178 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇰🇷 KR | 157 |
| 23 | 🇹🇷 TR | 152 |
| 24 | 🇮🇩 ID | 119 |
| 25 | 🇹🇭 TH | 112 |
| 26 | 🇵🇱 PL | 112 |
| 27 | 🇲🇦 MA | 104 |
| 28 | 🇲🇴 MO | 91 |
| 29 | 🇳🇱 NL | 84 |
| 30 | 🇲🇪 ME | 83 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 205 |
| 2 | Indira Gandhi International Airport |  | IN | 170 |
| 3 | Tokyo International Airport |  | JP | 165 |
| 4 | Frankfurt am Main International Airport |  | DE | 158 |
| 5 | Denver International Airport |  | US | 156 |
| 6 | El Dorado International Airport |  | CO | 141 |
| 7 | La Aurora Airport |  | GT | 124 |
| 8 | Harry Reid International Airport |  | US | 123 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 109 |
| 10 | Guaymaral Airport |  | CO | 107 |
| 11 | Zurich Airport |  | CH | 105 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 97 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 14 | Macau International Airport |  | MO | 91 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 90 |
| 16 | Chicago O'Hare International Airport |  | US | 88 |
| 17 | Tenerife Norte Airport |  | ES | 88 |
| 18 | Bengaluru International Airport |  | IN | 84 |
| 19 | Kuala Lumpur International Airport |  | MY | 84 |
| 20 | Madrid Barajas International Airport |  | ES | 80 |
| 21 | Ninoy Aquino International Airport |  | PH | 78 |
| 22 | Reno/Tahoe International Airport |  | US | 77 |
| 23 | Charlotte/Douglas International Airport |  | US | 74 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 72 |
| 25 | Malpensa International Airport |  | IT | 70 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 27 | Daniel K Inouye International Airport |  | US | 67 |
| 28 | Pune Airport |  | IN | 66 |
| 29 | Vitoria/Foronda Airport |  | ES | 65 |
| 30 | Salt Lake City International Airport |  | US | 64 |
| 31 | Congonhas Airport |  | BR | 64 |
| 32 | Charles de Gaulle International Airport |  | FR | 63 |
| 33 | Barcelona International Airport |  | ES | 63 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 61 |
| 36 | Gimpo International Airport |  | KR | 60 |
| 37 | Seattle-Tacoma International Airport |  | US | 60 |
| 38 | Miami International Airport |  | US | 59 |
| 39 | Bodø Airport |  | NO | 56 |
| 40 | O. R. Tambo International Airport |  | ZA | 56 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 42 | 29m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 40 | 14m | 114 km | 78.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 29 | 1h 45m | 1,156 km | 578.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 29 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 26 | 4m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 24 | 23m | 99 km | 41.1 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 18 | 1h 1m | 723 km | 224.4 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 15 | 1h 46m | 1,290 km | 333.8 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 27 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 14 | 34m | 431 km | 104.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHLID | FHL | Ontur Airport (LEOT) | Alhama De Murcia Airport (LELH) | 2026-04-01 15:09 UTC | 2026-04-01 15:21 UTC | 12m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-01 13:55 UTC | 2026-04-01 15:19 UTC | 1h 23m |
| HAWK295 | HAW | Kingsville Nas Airport (KNQI) | Puesta Del Sol Airport (TA44) | 2026-04-01 15:05 UTC | 2026-04-01 15:18 UTC | 12m |
| RNGR715 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-04-01 14:48 UTC | 2026-04-01 15:10 UTC | 21m |
| N404SP |  | Lubbock Preston Smith International Airport (KLBB) | Boerne Stage Airfield (K5C1) | 2026-04-01 14:21 UTC | 2026-04-01 15:06 UTC | 45m |
| MTN8310 | MTN | Newark Liberty International Airport (KEWR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-01 13:47 UTC | 2026-04-01 15:04 UTC | 1h 17m |
| BYF31 | BYF | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-01 14:24 UTC | 2026-04-01 15:04 UTC | 39m |
| STING51 | STI | Fort Clark Springs Airport (74TX) | Anacacho Ranch Airport (0XS7) | 2026-04-01 14:35 UTC | 2026-04-01 14:59 UTC | 24m |
| DU202 |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-04-01 14:47 UTC | 2026-04-01 14:58 UTC | 10m |
| GOSAX | GOS | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-04-01 14:50 UTC | 2026-04-01 14:56 UTC | 5m |
| GRZLY01 | GRZ | Melsbroek Air Base (EBMB) | Melsbroek Air Base (EBMB) | 2026-04-01 14:09 UTC | 2026-04-01 14:55 UTC | 46m |
| GES381L | GES | Madrid Barajas International Airport (LEMD) | El Castano Airport (LECT) | 2026-04-01 14:37 UTC | 2026-04-01 14:55 UTC | 17m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-01 14:30 UTC | 2026-04-01 14:54 UTC | 23m |
| FHLID | FHL | Casas de los Pinos Airport (LEPI) | Alhama De Murcia Airport (LELH) | 2026-04-01 14:37 UTC | 2026-04-01 14:53 UTC | 15m |
| SCA28 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-01 14:32 UTC | 2026-04-01 14:50 UTC | 18m |
| TGARO | TGA | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-04-01 14:28 UTC | 2026-04-01 14:50 UTC | 22m |
| N2475L |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-04-01 14:34 UTC | 2026-04-01 14:49 UTC | 14m |
| FGMQN | FGM | Paray Le Monial Airport (LFGN) | Saint-Yan Airport (LFLN) | 2026-04-01 14:30 UTC | 2026-04-01 14:47 UTC | 17m |
| DKEMC | DKE | Gap - Tallard Airport (LFNA) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-01 11:01 UTC | 2026-04-01 14:47 UTC | 3h 46m |
| VJT495 | VJT | Linate Airport (LIML) | LIAL (LIAL) | 2026-04-01 14:10 UTC | 2026-04-01 14:45 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
