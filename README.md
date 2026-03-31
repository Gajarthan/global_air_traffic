# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_09:53:10_UTC-green)

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

**Latest saved flight:** 2026-03-31 09:53:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 09:53:10 UTC

- **6,299** saved flights
- **4,144** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,299** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **79,777.2 tonnes** estimated CO2 emissions
- **4,624,763 km** total distance flown
- **872 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 229 |
| 3 | IndiGo | 166 |
| 4 | EJA | 129 |
| 5 | American Airlines | 122 |
| 6 | Southwest Airlines | 101 |
| 7 | Lufthansa | 96 |
| 8 | ENY | 93 |
| 9 | AXM | 71 |
| 10 | LATAM Airlines | 68 |
| 11 | Vueling | 62 |
| 12 | LXJ | 57 |
| 13 | QLK | 56 |
| 14 | Delta Air Lines | 55 |
| 15 | All Nippon Airways | 54 |
| 16 | Cathay Pacific | 47 |
| 17 | WIF | 47 |
| 18 | Japan Airlines | 46 |
| 19 | United Airlines | 46 |
| 20 | VIV | 46 |
| 21 | Swiss International | 44 |
| 22 | AXB | 43 |
| 23 | AZU | 43 |
| 24 | Alaska Airlines | 40 |
| 25 | EDV | 39 |
| 26 | Avianca | 37 |
| 27 | EJU | 34 |
| 28 | VOE | 34 |
| 29 | MXY | 33 |
| 30 | JST | 32 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5369 |
| 2 | 🇮🇳 IN | 505 |
| 3 | 🇦🇺 AU | 498 |
| 4 | 🇪🇸 ES | 462 |
| 5 | 🇯🇵 JP | 321 |
| 6 | 🇧🇷 BR | 314 |
| 7 | 🇩🇪 DE | 295 |
| 8 | 🇨🇴 CO | 290 |
| 9 | 🇮🇹 IT | 279 |
| 10 | 🇨🇦 CA | 271 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 200 |
| 13 | 🇫🇷 FR | 188 |
| 14 | 🇳🇴 NO | 159 |
| 15 | 🇲🇾 MY | 157 |
| 16 | 🇨🇭 CH | 145 |
| 17 | 🇬🇷 GR | 139 |
| 18 | 🇿🇦 ZA | 133 |
| 19 | 🇬🇹 GT | 132 |
| 20 | 🇵🇭 PH | 131 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 97 |
| 23 | 🇹🇭 TH | 90 |
| 24 | 🇮🇩 ID | 84 |
| 25 | 🇲🇴 MO | 80 |
| 26 | 🇲🇦 MA | 75 |
| 27 | 🇵🇱 PL | 74 |
| 28 | 🇰🇷 KR | 70 |
| 29 | 🇧🇸 BS | 60 |
| 30 | 🇲🇪 ME | 60 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Indira Gandhi International Airport |  | IN | 116 |
| 4 | Tokyo International Airport |  | JP | 113 |
| 5 | El Dorado International Airport |  | CO | 106 |
| 6 | Frankfurt am Main International Airport |  | DE | 94 |
| 7 | La Aurora Airport |  | GT | 90 |
| 8 | Harry Reid International Airport |  | US | 81 |
| 9 | Macau International Airport |  | MO | 80 |
| 10 | Chicago O'Hare International Airport |  | US | 76 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 13 | Zurich Airport |  | CH | 73 |
| 14 | Tenerife Norte Airport |  | ES | 67 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 65 |
| 17 | Guaymaral Airport |  | CO | 65 |
| 18 | Ninoy Aquino International Airport |  | PH | 59 |
| 19 | Reno/Tahoe International Airport |  | US | 58 |
| 20 | Bengaluru International Airport |  | IN | 57 |
| 21 | Madrid Barajas International Airport |  | ES | 56 |
| 22 | Kuala Lumpur International Airport |  | MY | 56 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 24 | Charlotte/Douglas International Airport |  | US | 50 |
| 25 | Salt Lake City International Airport |  | US | 49 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 49 |
| 27 | Charles de Gaulle International Airport |  | FR | 48 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 29 | Malpensa International Airport |  | IT | 47 |
| 30 | Miami International Airport |  | US | 46 |
| 31 | Vitoria/Foronda Airport |  | ES | 45 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 45 |
| 33 | Congonhas Airport |  | BR | 45 |
| 34 | Seattle-Tacoma International Airport |  | US | 44 |
| 35 | Daniel K Inouye International Airport |  | US | 43 |
| 36 | Centennial Airport |  | US | 43 |
| 37 | O. R. Tambo International Airport |  | ZA | 43 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 39 | Pune Airport |  | IN | 41 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 41 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 24 | 1h 7m | 706 km | 292.2 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 23 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 18 | 1h 41m | 1,423 km | 441.7 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 17 | 28m | 304 km | 89.1 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 17 | 1h 48m | 1,156 km | 339.1 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 17 | 21m | 165 km | 48.4 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 13 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 16 | 4m | - | - |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 15 | 1h 25m | 910 km | 235.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 14 | 29m | 275 km | 66.3 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 14 | 1h 10m | 770 km | 186.0 t |
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
| UAE9798 | Emirates | Suvarnabhumi Airport (VTBS) | Zhuhai Airport (ZGSD) | 2026-03-30 08:15 UTC | 2026-03-31 09:53 UTC | 25h 37m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 08:58 UTC | 2026-03-31 09:49 UTC | 51m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 09:04 UTC | 2026-03-31 09:48 UTC | 44m |
| NOZ1052 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Oksywie Military Air Base (EPOK) | 2026-03-31 08:46 UTC | 2026-03-31 09:48 UTC | 1h 1m |
| EZY9 | easyJet | London Gatwick Airport (EGKK) | Durham Tees Valley Airport (EGNV) | 2026-03-31 08:03 UTC | 2026-03-31 09:44 UTC | 1h 40m |
| TRP3 | TRP | Laura's Landing Airport (22MD) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-03-31 09:19 UTC | 2026-03-31 09:40 UTC | 21m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-03-30 22:04 UTC | 2026-03-31 09:29 UTC | 11h 25m |
| SVA3024 | Saudia | Chhatrapati Shivaji International Airport (VABB) | Zhuhai Airport (ZGSD) | 2026-03-30 16:52 UTC | 2026-03-31 09:25 UTC | 16h 32m |
| DLH1VR | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-03-31 08:24 UTC | 2026-03-31 09:16 UTC | 52m |
| BENGA98 | BEN | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-03-31 08:42 UTC | 2026-03-31 09:13 UTC | 30m |
| AXM6044 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-31 08:54 UTC | 2026-03-31 09:10 UTC | 16m |
| AWQ176 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-03-31 08:54 UTC | 2026-03-31 09:09 UTC | 14m |
| SWR319V | Swiss International | Dusseldorf International Airport (EDDL) | Zurich Airport (LSZH) | 2026-03-31 08:17 UTC | 2026-03-31 09:08 UTC | 50m |
| WZZ9SF | Wizz Air | M. R. Stefanik Airport (LZIB) | Kukes Airport (LAKU) | 2026-03-31 08:06 UTC | 2026-03-31 09:08 UTC | 1h 1m |
| EJU87EB | EJU | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Paris-Orly Airport (LFPO) | 2026-03-31 07:42 UTC | 2026-03-31 09:05 UTC | 1h 22m |
| MILAN80 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-03-31 08:50 UTC | 2026-03-31 09:01 UTC | 10m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-03-31 08:42 UTC | 2026-03-31 08:59 UTC | 17m |
| AWA447 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-03-31 08:24 UTC | 2026-03-31 08:58 UTC | 34m |
| AEE1BS | AEE | Sofia Airport (LBSF) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-31 07:59 UTC | 2026-03-31 08:58 UTC | 58m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pithorgarh Airport (VIDF) | 2026-03-31 08:31 UTC | 2026-03-31 08:57 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
