# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_05:57:37_UTC-green)

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

**Latest saved flight:** 2026-04-01 05:57:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 05:57:37 UTC

- **8,136** saved flights
- **5,089** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **99,410.7 tonnes** estimated CO2 emissions
- **5,762,939 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 294 |
| 3 | IndiGo | 212 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 134 |
| 7 | ENY | 116 |
| 8 | Lufthansa | 115 |
| 9 | AXM | 91 |
| 10 | Vueling | 84 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | Delta Air Lines | 70 |
| 14 | All Nippon Airways | 66 |
| 15 | QLK | 66 |
| 16 | WIF | 62 |
| 17 | VIV | 59 |
| 18 | AZU | 56 |
| 19 | Alaska Airlines | 55 |
| 20 | AXB | 55 |
| 21 | Swiss International | 55 |
| 22 | United Airlines | 54 |
| 23 | EDV | 53 |
| 24 | Japan Airlines | 53 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | Avianca | 46 |
| 28 | easyJet | 43 |
| 29 | JST | 43 |
| 30 | EJU | 42 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7008 |
| 2 | 🇮🇳 IN | 650 |
| 3 | 🇦🇺 AU | 644 |
| 4 | 🇪🇸 ES | 594 |
| 5 | 🇧🇷 BR | 398 |
| 6 | 🇯🇵 JP | 388 |
| 7 | 🇨🇦 CA | 386 |
| 8 | 🇩🇪 DE | 383 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 348 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 266 |
| 13 | 🇫🇷 FR | 228 |
| 14 | 🇳🇴 NO | 204 |
| 15 | 🇲🇾 MY | 201 |
| 16 | 🇳🇿 NZ | 190 |
| 17 | 🇬🇷 GR | 188 |
| 18 | 🇬🇹 GT | 171 |
| 19 | 🇨🇭 CH | 168 |
| 20 | 🇿🇦 ZA | 161 |
| 21 | 🇵🇭 PH | 154 |
| 22 | 🇹🇷 TR | 140 |
| 23 | 🇰🇷 KR | 109 |
| 24 | 🇮🇩 ID | 98 |
| 25 | 🇹🇭 TH | 98 |
| 26 | 🇲🇦 MA | 94 |
| 27 | 🇵🇱 PL | 94 |
| 28 | 🇲🇴 MO | 85 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Denver International Airport |  | US | 155 |
| 3 | Indira Gandhi International Airport |  | IN | 147 |
| 4 | Tokyo International Airport |  | JP | 139 |
| 5 | El Dorado International Airport |  | CO | 132 |
| 6 | Harry Reid International Airport |  | US | 120 |
| 7 | La Aurora Airport |  | GT | 120 |
| 8 | Frankfurt am Main International Airport |  | DE | 116 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 95 |
| 11 | Guaymaral Airport |  | CO | 90 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 88 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 14 | Zurich Airport |  | CH | 88 |
| 15 | Macau International Airport |  | MO | 85 |
| 16 | Chicago O'Hare International Airport |  | US | 84 |
| 17 | Reno/Tahoe International Airport |  | US | 77 |
| 18 | Tenerife Norte Airport |  | ES | 76 |
| 19 | Kuala Lumpur International Airport |  | MY | 75 |
| 20 | Charlotte/Douglas International Airport |  | US | 71 |
| 21 | Madrid Barajas International Airport |  | ES | 71 |
| 22 | Ninoy Aquino International Airport |  | PH | 70 |
| 23 | Bengaluru International Airport |  | IN | 70 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 25 | Daniel K Inouye International Airport |  | US | 65 |
| 26 | Salt Lake City International Airport |  | US | 64 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 28 | Malpensa International Airport |  | IT | 61 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 61 |
| 30 | Vitoria/Foronda Airport |  | ES | 59 |
| 31 | Seattle-Tacoma International Airport |  | US | 59 |
| 32 | Pune Airport |  | IN | 58 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 34 | Miami International Airport |  | US | 57 |
| 35 | Congonhas Airport |  | BR | 57 |
| 36 | Charles de Gaulle International Airport |  | FR | 53 |
| 37 | Centennial Airport |  | US | 53 |
| 38 | Barcelona International Airport |  | ES | 53 |
| 39 | Austin-Bergstrom International Airport |  | US | 52 |
| 40 | Bodø Airport |  | NO | 52 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 32 | 1h 6m | 706 km | 389.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 32 | 24m | 225 km | 124.1 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 27 | 31m | - | - |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 25 | 1h 45m | 1,156 km | 498.7 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 24 | 4m | - | - |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 23 | 29m | 304 km | 120.6 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 22 | 15m | 206 km | 78.2 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 22 | 20m | 165 km | 62.6 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 19 | 1h 25m | 910 km | 298.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 19 | 30m | 369 km | 120.9 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 17 | 53m | 546 km | 160.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 17 | 1h 10m | 770 km | 225.8 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 16 | 11m | 127 km | 35.0 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N920AH |  | Woods And Lakes Airpark (FA38) | Orlando Executive Airport (KORL) | 2026-04-01 05:30 UTC | 2026-04-01 05:57 UTC | 27m |
| RUH | RUH | Longwarry Airport (YLOY) | Melbourne Essendon Airport (YMEN) | 2026-04-01 05:30 UTC | 2026-04-01 05:52 UTC | 21m |
| ACA519 | Air Canada | Vancouver International Airport (CYVR) | Daniel K Inouye International Airport (PHNL) | 2026-04-01 00:19 UTC | 2026-04-01 05:47 UTC | 5h 28m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-01 04:50 UTC | 2026-04-01 05:33 UTC | 42m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-01 05:14 UTC | 2026-04-01 05:28 UTC | 14m |
| DRK211 | DRK | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-01 04:55 UTC | 2026-04-01 05:21 UTC | 26m |
| N172AD |  | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-04-01 04:16 UTC | 2026-04-01 05:16 UTC | 1h 0m |
| SEH1AM | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-01 04:46 UTC | 2026-04-01 05:12 UTC | 25m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-04-01 04:37 UTC | 2026-04-01 05:10 UTC | 33m |
| N49KC |  | Rochester International Airport (KRST) | Joe Foss Field (KFSD) | 2026-04-01 04:16 UTC | 2026-04-01 05:08 UTC | 51m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-04-01 04:51 UTC | 2026-04-01 05:07 UTC | 16m |
| VLG74AM | Vueling | Barcelona International Airport (LEBL) | Son Bonet Airport (LESB) | 2026-04-01 04:41 UTC | 2026-04-01 05:04 UTC | 22m |
| ZGU | ZGU | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-01 04:39 UTC | 2026-04-01 05:03 UTC | 23m |
| NPS | NPS | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-01 04:49 UTC | 2026-04-01 05:01 UTC | 12m |
| VAR409 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-01 04:51 UTC | 2026-04-01 04:57 UTC | 5m |
| CFH23 | CFH | Port Macquarie Airport (YPMQ) | Scone Airport (YSCO) | 2026-04-01 04:31 UTC | 2026-04-01 04:56 UTC | 25m |
| BRU925 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-03-31 14:46 UTC | 2026-04-01 04:53 UTC | 14h 6m |
| HPP | HPP | Toowoomba Airport (YTWB) | Maryborough Airport (YMYB) | 2026-04-01 04:20 UTC | 2026-04-01 04:52 UTC | 32m |
| AEE282 | AEE | Eleftherios Venizelos International Airport (LGAV) | Aktion National Airport (LGPZ) | 2026-04-01 04:20 UTC | 2026-04-01 04:47 UTC | 27m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-01 04:27 UTC | 2026-04-01 04:47 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
