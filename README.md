# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_05:07:38_UTC-green)

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

**Latest saved flight:** 2026-03-31 05:07:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 05:07:38 UTC

- **5,978** saved flights
- **4,006** unique routes
- **104** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,978** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **75,466.6 tonnes** estimated CO2 emissions
- **4,374,876 km** total distance flown
- **872 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 152 |
| 4 | EJA | 129 |
| 5 | American Airlines | 120 |
| 6 | Southwest Airlines | 101 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 67 |
| 10 | AXM | 62 |
| 11 | LXJ | 57 |
| 12 | Delta Air Lines | 55 |
| 13 | Vueling | 55 |
| 14 | All Nippon Airways | 47 |
| 15 | Cathay Pacific | 47 |
| 16 | QLK | 47 |
| 17 | United Airlines | 46 |
| 18 | VIV | 46 |
| 19 | AZU | 43 |
| 20 | WIF | 43 |
| 21 | Japan Airlines | 41 |
| 22 | EDV | 39 |
| 23 | Alaska Airlines | 38 |
| 24 | Swiss International | 38 |
| 25 | Avianca | 37 |
| 26 | AXB | 35 |
| 27 | MXY | 33 |
| 28 | VOE | 31 |
| 29 | EJU | 30 |
| 30 | GLO | 29 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5332 |
| 2 | 🇮🇳 IN | 451 |
| 3 | 🇦🇺 AU | 412 |
| 4 | 🇪🇸 ES | 410 |
| 5 | 🇧🇷 BR | 312 |
| 6 | 🇯🇵 JP | 291 |
| 7 | 🇨🇴 CO | 288 |
| 8 | 🇨🇦 CA | 267 |
| 9 | 🇮🇹 IT | 264 |
| 10 | 🇩🇪 DE | 243 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 185 |
| 13 | 🇫🇷 FR | 172 |
| 14 | 🇳🇴 NO | 145 |
| 15 | 🇲🇾 MY | 137 |
| 16 | 🇬🇹 GT | 132 |
| 17 | 🇨🇭 CH | 125 |
| 18 | 🇿🇦 ZA | 123 |
| 19 | 🇬🇷 GR | 119 |
| 20 | 🇵🇭 PH | 118 |
| 21 | 🇳🇿 NZ | 116 |
| 22 | 🇹🇷 TR | 93 |
| 23 | 🇹🇭 TH | 80 |
| 24 | 🇲🇴 MO | 76 |
| 25 | 🇲🇦 MA | 69 |
| 26 | 🇮🇩 ID | 66 |
| 27 | 🇵🇱 PL | 65 |
| 28 | 🇧🇸 BS | 60 |
| 29 | 🇰🇷 KR | 55 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 162 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | El Dorado International Airport |  | CO | 105 |
| 4 | Indira Gandhi International Airport |  | IN | 103 |
| 5 | Tokyo International Airport |  | JP | 101 |
| 6 | La Aurora Airport |  | GT | 90 |
| 7 | Harry Reid International Airport |  | US | 80 |
| 8 | Frankfurt am Main International Airport |  | DE | 80 |
| 9 | Chicago O'Hare International Airport |  | US | 76 |
| 10 | Macau International Airport |  | MO | 76 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 13 | Zurich Airport |  | CH | 66 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 66 |
| 15 | Guaymaral Airport |  | CO | 65 |
| 16 | Tenerife Norte Airport |  | ES | 62 |
| 17 | Reno/Tahoe International Airport |  | US | 58 |
| 18 | Eleftherios Venizelos International Airport |  | GR | 55 |
| 19 | Ninoy Aquino International Airport |  | PH | 53 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 21 | Charlotte/Douglas International Airport |  | US | 50 |
| 22 | Bengaluru International Airport |  | IN | 50 |
| 23 | Salt Lake City International Airport |  | US | 49 |
| 24 | Kuala Lumpur International Airport |  | MY | 49 |
| 25 | Madrid Barajas International Airport |  | ES | 48 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 48 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 28 | Malpensa International Airport |  | IT | 47 |
| 29 | Miami International Airport |  | US | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 46 |
| 31 | Congonhas Airport |  | BR | 45 |
| 32 | Seattle-Tacoma International Airport |  | US | 44 |
| 33 | Centennial Airport |  | US | 43 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 35 | O. R. Tambo International Airport |  | ZA | 42 |
| 36 | Daniel K Inouye International Airport |  | US | 41 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 41 |
| 39 | Vitoria/Foronda Airport |  | ES | 40 |
| 40 | Los Angeles International Airport |  | US | 39 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 24 | 24m | 225 km | 93.1 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 19 | 1h 7m | 706 km | 231.3 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 16 | 1h 41m | 1,423 km | 392.7 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 15 | 1h 50m | 1,156 km | 299.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 15 | 21m | 165 km | 42.7 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 15 | 4m | - | - |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 14 | 1h 25m | 910 km | 219.7 t |
| 14 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 14 | 30m | 369 km | 89.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 13 | 1h 10m | 770 km | 172.7 t |
| 18 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 12 | 28m | 304 km | 62.9 t |
| 21 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 12 | 53m | 546 km | 113.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 12 | 11m | 127 km | 26.3 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 11 | 1h 46m | 1,290 km | 244.8 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 11 | 30m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N951TG |  | Sarasota/Bradenton International Airport (KSRQ) | Peter O Knight Airport (KTPF) | 2026-03-31 04:48 UTC | 2026-03-31 05:07 UTC | 19m |
| N6227 |  | Austin Executive Airport (KEDC) | Austin Executive Airport (KEDC) | 2026-03-31 03:21 UTC | 2026-03-31 04:55 UTC | 1h 33m |
| N9487K |  | Wickenburg Municipal Airport (KE25) | Wickenburg Municipal Airport (KE25) | 2026-03-31 04:36 UTC | 2026-03-31 04:36 UTC | 0m |
| JAL434 | Japan Airlines | Tokyo International Airport (RJTT) | Tokyo International Airport (RJTT) | 2026-03-31 00:59 UTC | 2026-03-31 04:31 UTC | 3h 32m |
| ZJA | ZJA | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-03-31 04:09 UTC | 2026-03-31 04:31 UTC | 21m |
| QUE20 | QUE | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Gaspe (Michel-Pouliot) Airport (CYGP) | 2026-03-31 03:37 UTC | 2026-03-31 04:30 UTC | 52m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-31 04:16 UTC | 2026-03-31 04:30 UTC | 13m |
| N398AA |  | Terrell Municipal Airport (KTRL) | Denton Enterprise Airport (KDTO) | 2026-03-31 03:08 UTC | 2026-03-31 04:29 UTC | 1h 20m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-03-31 03:49 UTC | 2026-03-31 04:22 UTC | 33m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-31 04:04 UTC | 2026-03-31 04:21 UTC | 17m |
| UAE67V | Emirates | Dubai International Airport (OMDB) | Shaibah Airport (OESB) | 2026-03-31 03:49 UTC | 2026-03-31 04:19 UTC | 29m |
| R21230 |  | Ladd Army Air Field (PAFB) | Nenana Municipal Airport (PANN) | 2026-03-31 03:15 UTC | 2026-03-31 04:18 UTC | 1h 3m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-03-31 03:35 UTC | 2026-03-31 04:17 UTC | 42m |
| N917SH |  | Joe Foss Field (KFSD) | Winner Regional Airport (KICR) | 2026-03-31 03:32 UTC | 2026-03-31 04:17 UTC | 44m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-03-30 16:56 UTC | 2026-03-31 04:16 UTC | 11h 20m |
| ZHC | ZHC | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 03:53 UTC | 2026-03-31 04:14 UTC | 21m |
| TEST1234 | TES | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-03-31 03:56 UTC | 2026-03-31 04:14 UTC | 17m |
| AIC2741 | Air India | Juhu Aerodrome (VAJJ) | Sarsawa Air Force Station (VISP) | 2026-03-31 02:37 UTC | 2026-03-31 04:13 UTC | 1h 35m |
| N782MM |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-03-31 04:11 UTC | 2026-03-31 04:11 UTC | 0m |
| NKS1638 | NKS | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-03-31 03:20 UTC | 2026-03-31 04:11 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
