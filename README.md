# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_08:51:59_UTC-green)

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

**Latest saved flight:** 2026-04-01 08:51:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 08:51:59 UTC

- **8,306** saved flights
- **5,152** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,306** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **100,989.9 tonnes** estimated CO2 emissions
- **5,854,490 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 304 |
| 3 | IndiGo | 227 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 134 |
| 7 | Lufthansa | 124 |
| 8 | ENY | 116 |
| 9 | AXM | 94 |
| 10 | Vueling | 92 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | Delta Air Lines | 70 |
| 14 | QLK | 70 |
| 15 | All Nippon Airways | 68 |
| 16 | WIF | 64 |
| 17 | VIV | 59 |
| 18 | Swiss International | 58 |
| 19 | AXB | 57 |
| 20 | AZU | 57 |
| 21 | Japan Airlines | 57 |
| 22 | Alaska Airlines | 56 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | Avianca | 46 |
| 28 | EJU | 46 |
| 29 | JST | 45 |
| 30 | easyJet | 44 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7037 |
| 2 | 🇮🇳 IN | 698 |
| 3 | 🇦🇺 AU | 675 |
| 4 | 🇪🇸 ES | 619 |
| 5 | 🇯🇵 JP | 408 |
| 6 | 🇩🇪 DE | 405 |
| 7 | 🇧🇷 BR | 401 |
| 8 | 🇨🇦 CA | 388 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 360 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 271 |
| 13 | 🇫🇷 FR | 240 |
| 14 | 🇳🇴 NO | 211 |
| 15 | 🇲🇾 MY | 210 |
| 16 | 🇳🇿 NZ | 195 |
| 17 | 🇬🇷 GR | 190 |
| 18 | 🇨🇭 CH | 182 |
| 19 | 🇬🇹 GT | 172 |
| 20 | 🇿🇦 ZA | 165 |
| 21 | 🇵🇭 PH | 162 |
| 22 | 🇹🇷 TR | 142 |
| 23 | 🇰🇷 KR | 137 |
| 24 | 🇮🇩 ID | 106 |
| 25 | 🇹🇭 TH | 105 |
| 26 | 🇲🇦 MA | 95 |
| 27 | 🇵🇱 PL | 95 |
| 28 | 🇲🇴 MO | 85 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Indira Gandhi International Airport |  | IN | 157 |
| 3 | Denver International Airport |  | US | 155 |
| 4 | Tokyo International Airport |  | JP | 146 |
| 5 | El Dorado International Airport |  | CO | 132 |
| 6 | Frankfurt am Main International Airport |  | DE | 126 |
| 7 | La Aurora Airport |  | GT | 121 |
| 8 | Harry Reid International Airport |  | US | 120 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 11 | Zurich Airport |  | CH | 93 |
| 12 | Guaymaral Airport |  | CO | 90 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 89 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 15 | Macau International Airport |  | MO | 85 |
| 16 | Chicago O'Hare International Airport |  | US | 84 |
| 17 | Reno/Tahoe International Airport |  | US | 77 |
| 18 | Kuala Lumpur International Airport |  | MY | 77 |
| 19 | Tenerife Norte Airport |  | ES | 76 |
| 20 | Bengaluru International Airport |  | IN | 75 |
| 21 | Madrid Barajas International Airport |  | ES | 74 |
| 22 | Ninoy Aquino International Airport |  | PH | 73 |
| 23 | Charlotte/Douglas International Airport |  | US | 71 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 25 | Daniel K Inouye International Airport |  | US | 66 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 66 |
| 27 | Salt Lake City International Airport |  | US | 64 |
| 28 | Malpensa International Airport |  | IT | 63 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 30 | Vitoria/Foronda Airport |  | ES | 61 |
| 31 | Pune Airport |  | IN | 60 |
| 32 | Seattle-Tacoma International Airport |  | US | 59 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 34 | Miami International Airport |  | US | 57 |
| 35 | Congonhas Airport |  | BR | 57 |
| 36 | Barcelona International Airport |  | ES | 57 |
| 37 | Charles de Gaulle International Airport |  | FR | 56 |
| 38 | Bodø Airport |  | NO | 54 |
| 39 | Centennial Airport |  | US | 53 |
| 40 | Austin-Bergstrom International Airport |  | US | 52 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 33 | 1h 6m | 706 km | 401.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 27 | 29m | 304 km | 141.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 27 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 26 | 1h 45m | 1,156 km | 518.7 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 25 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 23 | 15m | 206 km | 81.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 22 | 20m | 165 km | 62.6 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 20 | 1h 26m | 910 km | 313.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 20 | 30m | 369 km | 127.3 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 18 | 53m | 546 km | 169.5 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 16 | 1h 0m | 723 km | 199.5 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 16 | 11m | 127 km | 35.0 t |
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
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-01 08:06 UTC | 2026-04-01 08:51 UTC | 45m |
| AXM1795 | AXM | Kota Kinabalu International Airport (WBKK) | Kijang Airport (WIDN) | 2026-04-01 07:01 UTC | 2026-04-01 08:46 UTC | 1h 44m |
| LNOZT | LNO | Sandefjord Airport Torp (ENTO) | Sandefjord Airport Torp (ENTO) | 2026-04-01 08:00 UTC | 2026-04-01 08:36 UTC | 36m |
| N491LG |  | Tall Timber Airport (CD28) | Athanasiou Valley Airport (CO07) | 2026-04-01 08:21 UTC | 2026-04-01 08:34 UTC | 12m |
| LICHEN2 | LIC | Lakewood Airport (78AA) | Ladd Army Air Field (PAFB) | 2026-04-01 07:35 UTC | 2026-04-01 08:32 UTC | 56m |
|  |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-01 08:05 UTC | 2026-04-01 08:24 UTC | 18m |
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-01 07:24 UTC | 2026-04-01 08:18 UTC | 54m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-04-01 07:28 UTC | 2026-04-01 08:13 UTC | 45m |
| AAB45Z | AAB | Wevelgem Airport (EBKT) | Raron Airport (LSTA) | 2026-04-01 07:12 UTC | 2026-04-01 08:11 UTC | 59m |
| IGO6937 | IndiGo | Juhu Aerodrome (VAJJ) | Sidhi Airport (VA1F) | 2026-04-01 06:39 UTC | 2026-04-01 08:09 UTC | 1h 29m |
| QLK1529 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-01 07:10 UTC | 2026-04-01 08:06 UTC | 55m |
| EZY72FE | easyJet | Bristol International Airport (EGGD) | Dubrovnik Airport (LDDU) | 2026-04-01 05:19 UTC | 2026-04-01 08:01 UTC | 2h 42m |
| ESR218 | ESR | Gwangju Airport (RKJJ) | Gimpo International Airport (RKSS) | 2026-04-01 07:27 UTC | 2026-04-01 08:00 UTC | 33m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-04-01 07:30 UTC | 2026-04-01 07:59 UTC | 29m |
| IGO6104 | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-04-01 06:59 UTC | 2026-04-01 07:58 UTC | 59m |
| SWR41D | Swiss International | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-04-01 07:22 UTC | 2026-04-01 07:57 UTC | 34m |
|  |  | Naha Airport (ROAH) | Kerama Airport (ROKR) | 2026-04-01 07:44 UTC | 2026-04-01 07:54 UTC | 10m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Sanda Airport (BISA) | 2026-04-01 07:32 UTC | 2026-04-01 07:51 UTC | 18m |
| LICHEN3 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-01 07:36 UTC | 2026-04-01 07:50 UTC | 14m |
| KAL1823 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-01 07:20 UTC | 2026-04-01 07:47 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
