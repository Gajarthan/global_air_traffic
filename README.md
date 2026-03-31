# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_11:01:08_UTC-green)

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

**Latest saved flight:** 2026-03-31 11:01:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 11:01:08 UTC

- **6,368** saved flights
- **4,178** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,368** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **80,920.2 tonnes** estimated CO2 emissions
- **4,691,025 km** total distance flown
- **874 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 233 |
| 3 | IndiGo | 172 |
| 4 | EJA | 129 |
| 5 | American Airlines | 122 |
| 6 | Southwest Airlines | 101 |
| 7 | Lufthansa | 98 |
| 8 | ENY | 93 |
| 9 | AXM | 73 |
| 10 | LATAM Airlines | 68 |
| 11 | Vueling | 64 |
| 12 | LXJ | 57 |
| 13 | All Nippon Airways | 56 |
| 14 | QLK | 56 |
| 15 | Delta Air Lines | 55 |
| 16 | Swiss International | 49 |
| 17 | WIF | 48 |
| 18 | Cathay Pacific | 47 |
| 19 | Japan Airlines | 47 |
| 20 | United Airlines | 47 |
| 21 | VIV | 46 |
| 22 | AXB | 44 |
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
| 1 | 🇺🇸 US | 5375 |
| 2 | 🇮🇳 IN | 523 |
| 3 | 🇦🇺 AU | 500 |
| 4 | 🇪🇸 ES | 478 |
| 5 | 🇯🇵 JP | 329 |
| 6 | 🇧🇷 BR | 317 |
| 7 | 🇩🇪 DE | 305 |
| 8 | 🇨🇴 CO | 293 |
| 9 | 🇮🇹 IT | 283 |
| 10 | 🇨🇦 CA | 271 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 206 |
| 13 | 🇫🇷 FR | 189 |
| 14 | 🇲🇾 MY | 163 |
| 15 | 🇳🇴 NO | 163 |
| 16 | 🇨🇭 CH | 150 |
| 17 | 🇬🇷 GR | 141 |
| 18 | 🇿🇦 ZA | 141 |
| 19 | 🇬🇹 GT | 132 |
| 20 | 🇵🇭 PH | 131 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 97 |
| 23 | 🇹🇭 TH | 92 |
| 24 | 🇮🇩 ID | 84 |
| 25 | 🇲🇴 MO | 80 |
| 26 | 🇵🇱 PL | 76 |
| 27 | 🇰🇷 KR | 75 |
| 28 | 🇲🇦 MA | 75 |
| 29 | 🇲🇪 ME | 61 |
| 30 | 🇧🇸 BS | 60 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Indira Gandhi International Airport |  | IN | 119 |
| 4 | Tokyo International Airport |  | JP | 117 |
| 5 | El Dorado International Airport |  | CO | 109 |
| 6 | Frankfurt am Main International Airport |  | DE | 97 |
| 7 | La Aurora Airport |  | GT | 90 |
| 8 | Harry Reid International Airport |  | US | 81 |
| 9 | Macau International Airport |  | MO | 80 |
| 10 | Zurich Airport |  | CH | 78 |
| 11 | Chicago O'Hare International Airport |  | US | 76 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 14 | Tenerife Norte Airport |  | ES | 68 |
| 15 | Eleftherios Venizelos International Airport |  | GR | 67 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 17 | Guaymaral Airport |  | CO | 65 |
| 18 | Reno/Tahoe International Airport |  | US | 59 |
| 19 | Ninoy Aquino International Airport |  | PH | 59 |
| 20 | Kuala Lumpur International Airport |  | MY | 59 |
| 21 | Bengaluru International Airport |  | IN | 58 |
| 22 | Madrid Barajas International Airport |  | ES | 57 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 24 | Charlotte/Douglas International Airport |  | US | 50 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 50 |
| 26 | Charles de Gaulle International Airport |  | FR | 49 |
| 27 | Salt Lake City International Airport |  | US | 49 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 48 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 30 | Malpensa International Airport |  | IT | 47 |
| 31 | Miami International Airport |  | US | 46 |
| 32 | Vitoria/Foronda Airport |  | ES | 46 |
| 33 | Congonhas Airport |  | BR | 45 |
| 34 | O. R. Tambo International Airport |  | ZA | 45 |
| 35 | Seattle-Tacoma International Airport |  | US | 44 |
| 36 | Daniel K Inouye International Airport |  | US | 43 |
| 37 | Pune Airport |  | IN | 43 |
| 38 | Centennial Airport |  | US | 43 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 40 | Amsterdam Airport Schiphol |  | NL | 41 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 26 | 1h 6m | 706 km | 316.6 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 23 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 18 | 1h 48m | 1,156 km | 359.1 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 18 | 1h 41m | 1,423 km | 441.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 17 | 21m | 165 km | 48.4 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 16 | 4m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 15 | 29m | 275 km | 71.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 15 | 1h 10m | 770 km | 199.3 t |
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
| INR50220 | INR | Reus Air Base (LERS) | Reus Air Base (LERS) | 2026-03-31 10:49 UTC | 2026-03-31 11:01 UTC | 11m |
| SWIFT322 | SWI | Moi Air Base (HKRE) | Nairobi Wilson Airport (HKNW) | 2026-03-31 10:34 UTC | 2026-03-31 10:42 UTC | 7m |
| SAS157 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Gothenburg-Landvetter Airport (ESGG) | 2026-03-31 09:45 UTC | 2026-03-31 10:28 UTC | 43m |
| GOBBI | GOB | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-03-31 10:22 UTC | 2026-03-31 10:22 UTC | 0m |
| DHK815 | DHK | Leipzig Halle Airport (EDDP) | John F Kennedy International Airport (KJFK) | 2026-03-31 01:21 UTC | 2026-03-31 10:21 UTC | 8h 59m |
| RYR877 | Ryanair | Torino / Caselle International Airport (LIMF) | Crotone Airport (LIBC) | 2026-03-31 09:02 UTC | 2026-03-31 10:20 UTC | 1h 17m |
| UAL3917 | United Airlines | Kalaeloa (John Rodgers Field) Airport (PHJR) | Chek Lap Kok International Airport (VHHH) | 2026-03-30 22:10 UTC | 2026-03-31 10:14 UTC | 12h 4m |
| SAS68R | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-31 07:23 UTC | 2026-03-31 10:11 UTC | 2h 48m |
| MRL01 | MRL | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-03-31 09:32 UTC | 2026-03-31 10:09 UTC | 36m |
| N425AM |  | Joplin Regional Airport (KJLN) | Joplin Regional Airport (KJLN) | 2026-03-31 09:59 UTC | 2026-03-31 10:02 UTC | 2m |
| TWB690 | TWB | Kaohsiung International Airport (RCKH) | G 505 Airport (RKUC) | 2026-03-31 05:55 UTC | 2026-03-31 10:00 UTC | 4h 5m |
| PSAMF | PSA | Posto de Protecao Ambiental Santa Maria Airport (SWWV) | Estancia Barbosa Airport (SWOX) | 2026-03-31 09:42 UTC | 2026-03-31 09:54 UTC | 11m |
| UAE9798 | Emirates | Suvarnabhumi Airport (VTBS) | Zhuhai Airport (ZGSD) | 2026-03-30 08:15 UTC | 2026-03-31 09:53 UTC | 25h 37m |
| ANE2328 | ANE | Palma De Mallorca Airport (LEPA) | Igualada/Odena Airport (LEIG) | 2026-03-31 09:10 UTC | 2026-03-31 09:51 UTC | 41m |
| AUA801C | Austrian Airlines | Vienna International Airport (LOWW) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-31 07:54 UTC | 2026-03-31 09:51 UTC | 1h 57m |
| ANA667 | All Nippon Airways | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-03-31 08:25 UTC | 2026-03-31 09:50 UTC | 1h 24m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-03-31 08:42 UTC | 2026-03-31 09:49 UTC | 1h 7m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 08:58 UTC | 2026-03-31 09:49 UTC | 51m |
| SWR4LM | Swiss International | Palma De Mallorca Airport (LEPA) | Zurich Airport (LSZH) | 2026-03-31 07:57 UTC | 2026-03-31 09:49 UTC | 1h 51m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 09:04 UTC | 2026-03-31 09:48 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
