# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_09:57:03_UTC-green)

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

**Latest saved flight:** 2026-04-02 09:57:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 09:57:03 UTC

- **10,595** saved flights
- **6,198** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,595** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **131,188.3 tonnes** estimated CO2 emissions
- **7,605,120 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 405 |
| 3 | IndiGo | 295 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 174 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | AXM | 115 |
| 10 | Vueling | 115 |
| 11 | LATAM Airlines | 106 |
| 12 | LXJ | 100 |
| 13 | QLK | 99 |
| 14 | All Nippon Airways | 97 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 83 |
| 17 | Swiss International | 80 |
| 18 | Japan Airlines | 73 |
| 19 | Alaska Airlines | 72 |
| 20 | VIV | 72 |
| 21 | AXB | 71 |
| 22 | AZU | 71 |
| 23 | Cathay Pacific | 66 |
| 24 | EDV | 66 |
| 25 | United Airlines | 66 |
| 26 | Avianca | 60 |
| 27 | EJU | 60 |
| 28 | easyJet | 59 |
| 29 | BRC | 58 |
| 30 | ANZ | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8554 |
| 2 | 🇮🇳 IN | 898 |
| 3 | 🇦🇺 AU | 896 |
| 4 | 🇪🇸 ES | 813 |
| 5 | 🇩🇪 DE | 576 |
| 6 | 🇯🇵 JP | 557 |
| 7 | 🇧🇷 BR | 542 |
| 8 | 🇨🇴 CO | 524 |
| 9 | 🇨🇦 CA | 513 |
| 10 | 🇮🇹 IT | 463 |
| 11 | 🇲🇽 MX | 379 |
| 12 | 🇬🇧 GB | 376 |
| 13 | 🇫🇷 FR | 323 |
| 14 | 🇳🇴 NO | 270 |
| 15 | 🇳🇿 NZ | 260 |
| 16 | 🇲🇾 MY | 258 |
| 17 | 🇬🇷 GR | 254 |
| 18 | 🇨🇭 CH | 248 |
| 19 | 🇿🇦 ZA | 217 |
| 20 | 🇵🇭 PH | 210 |
| 21 | 🇬🇹 GT | 209 |
| 22 | 🇰🇷 KR | 190 |
| 23 | 🇹🇷 TR | 166 |
| 24 | 🇮🇩 ID | 135 |
| 25 | 🇹🇭 TH | 132 |
| 26 | 🇵🇱 PL | 132 |
| 27 | 🇲🇴 MO | 127 |
| 28 | 🇲🇦 MA | 120 |
| 29 | 🇲🇪 ME | 102 |
| 30 | 🇳🇱 NL | 99 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Tokyo International Airport |  | JP | 200 |
| 3 | Indira Gandhi International Airport |  | IN | 196 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | El Dorado International Airport |  | CO | 173 |
| 6 | Frankfurt am Main International Airport |  | DE | 173 |
| 7 | Harry Reid International Airport |  | US | 149 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 132 |
| 11 | Macau International Airport |  | MO | 127 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 13 | Zurich Airport |  | CH | 121 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 120 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Bengaluru International Airport |  | IN | 101 |
| 18 | Kuala Lumpur International Airport |  | MY | 97 |
| 19 | Reno/Tahoe International Airport |  | US | 95 |
| 20 | Madrid Barajas International Airport |  | ES | 95 |
| 21 | Ninoy Aquino International Airport |  | PH | 94 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 23 | Charlotte/Douglas International Airport |  | US | 92 |
| 24 | Tenerife Norte Airport |  | ES | 92 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 84 |
| 26 | Daniel K Inouye International Airport |  | US | 81 |
| 27 | Congonhas Airport |  | BR | 81 |
| 28 | Malpensa International Airport |  | IT | 80 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 80 |
| 30 | Vitoria/Foronda Airport |  | ES | 77 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 32 | Salt Lake City International Airport |  | US | 75 |
| 33 | Pune Airport |  | IN | 74 |
| 34 | Barcelona International Airport |  | ES | 74 |
| 35 | Austin-Bergstrom International Airport |  | US | 72 |
| 36 | Charles de Gaulle International Airport |  | FR | 72 |
| 37 | Seattle-Tacoma International Airport |  | US | 72 |
| 38 | Gimpo International Airport |  | KR | 71 |
| 39 | Bodø Airport |  | NO | 69 |
| 40 | Miami International Airport |  | US | 67 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 50 | 1h 7m | 706 km | 608.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 37 | 29m | 304 km | 194.0 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 33 | 1h 44m | 1,156 km | 658.3 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 32 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 31 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 31 | 20m | 165 km | 88.2 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 27 | 1h 26m | 910 km | 423.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 24 | 53m | 546 km | 226.0 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 21 | 1h 10m | 770 km | 279.0 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 19 | 11m | 127 km | 41.6 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 18 | 23m | 252 km | 78.2 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 16 | 44m | 452 km | 124.7 t |
| 29 | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 16 | 28m | 212 km | 58.5 t |
| 30 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 16 | 18m | 26 km | 7.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DHTAF | DHT | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-02 09:40 UTC | 2026-04-02 09:57 UTC | 16m |
| OEFDD | OEF | Urbe Airport (LIRU) | Guidonia Airport (LIRG) | 2026-04-02 09:36 UTC | 2026-04-02 09:51 UTC | 15m |
| ZEF | ZEF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-02 08:56 UTC | 2026-04-02 09:45 UTC | 49m |
| HUF175 | HUF | Kecskemet Airport (LHKE) | Otocac Airport (LDRO) | 2026-04-02 09:04 UTC | 2026-04-02 09:40 UTC | 35m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-02 09:06 UTC | 2026-04-02 09:36 UTC | 30m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-02 08:44 UTC | 2026-04-02 09:28 UTC | 44m |
| N371PA |  | Patrick Leahy Burlington International Airport (KBTV) | Franklin County State Airport (KFSO) | 2026-04-02 08:35 UTC | 2026-04-02 09:26 UTC | 51m |
| FMY8035 | FMY | Lille-Lesquin Airport (LFQQ) | La Rochelle-Ile de Re Airport (LFBH) | 2026-04-02 08:07 UTC | 2026-04-02 09:23 UTC | 1h 15m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-01 22:09 UTC | 2026-04-02 09:21 UTC | 11h 12m |
| RYR95VG | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Palma De Mallorca Airport (LEPA) | 2026-04-02 07:16 UTC | 2026-04-02 09:18 UTC | 2h 1m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-01 21:35 UTC | 2026-04-02 09:15 UTC | 11h 40m |
| TVF21CG | TVF | Paris-Orly Airport (LFPO) | Paros Airport (LGPA) | 2026-04-02 06:18 UTC | 2026-04-02 09:15 UTC | 2h 57m |
| N996RS |  | Hemet-Ryan Airport (KHMT) | Mc Conville Airstrip (CA42) | 2026-04-02 07:52 UTC | 2026-04-02 09:13 UTC | 1h 21m |
| LOT4NC | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Hamburg Airport (EDDH) | 2026-04-02 08:02 UTC | 2026-04-02 09:12 UTC | 1h 9m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-02 01:48 UTC | 2026-04-02 09:07 UTC | 7h 18m |
| AXB1537 | AXB | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-02 07:00 UTC | 2026-04-02 09:06 UTC | 2h 6m |
| AM6073 |  | Kota Kinabalu International Airport (WBKK) | Lutong Airport (WMLU) | 2026-04-02 08:31 UTC | 2026-04-02 09:06 UTC | 35m |
| LLR875 | LLR | Dehradun Airport (VIDN) | Pithorgarh Airport (VIDF) | 2026-04-02 08:40 UTC | 2026-04-02 09:05 UTC | 24m |
| AXM6044 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-02 08:44 UTC | 2026-04-02 09:04 UTC | 20m |
|  |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-02 08:49 UTC | 2026-04-02 09:04 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
