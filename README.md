# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_19:18:29_UTC-green)

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

**Latest saved flight:** 2026-03-31 19:18:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 19:18:29 UTC

- **7,308** saved flights
- **4,716** unique routes
- **106** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,308** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **91,294.7 tonnes** estimated CO2 emissions
- **5,292,448 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 343 |
| 2 | Ryanair | 280 |
| 3 | IndiGo | 197 |
| 4 | EJA | 153 |
| 5 | American Airlines | 134 |
| 6 | Lufthansa | 115 |
| 7 | Southwest Airlines | 112 |
| 8 | ENY | 101 |
| 9 | AXM | 78 |
| 10 | Vueling | 75 |
| 11 | LATAM Airlines | 73 |
| 12 | Delta Air Lines | 64 |
| 13 | LXJ | 64 |
| 14 | WIF | 58 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 51 |
| 19 | VIV | 51 |
| 20 | AZU | 50 |
| 21 | United Airlines | 48 |
| 22 | Cathay Pacific | 47 |
| 23 | EDV | 47 |
| 24 | Japan Airlines | 47 |
| 25 | Alaska Airlines | 46 |
| 26 | Avianca | 42 |
| 27 | EJU | 41 |
| 28 | easyJet | 40 |
| 29 | AEE | 39 |
| 30 | BRC | 39 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6207 |
| 2 | 🇮🇳 IN | 598 |
| 3 | 🇪🇸 ES | 566 |
| 4 | 🇦🇺 AU | 510 |
| 5 | 🇩🇪 DE | 379 |
| 6 | 🇧🇷 BR | 362 |
| 7 | 🇯🇵 JP | 338 |
| 8 | 🇨🇴 CO | 337 |
| 9 | 🇮🇹 IT | 333 |
| 10 | 🇨🇦 CA | 332 |
| 11 | 🇲🇽 MX | 258 |
| 12 | 🇬🇧 GB | 256 |
| 13 | 🇫🇷 FR | 225 |
| 14 | 🇳🇴 NO | 194 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 175 |
| 17 | 🇨🇭 CH | 167 |
| 18 | 🇿🇦 ZA | 161 |
| 19 | 🇬🇹 GT | 156 |
| 20 | 🇹🇷 TR | 132 |
| 21 | 🇵🇭 PH | 132 |
| 22 | 🇳🇿 NZ | 122 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇲🇦 MA | 91 |
| 25 | 🇵🇱 PL | 90 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 72 |
| 30 | 🇲🇪 ME | 70 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 178 |
| 2 | Indira Gandhi International Airport |  | IN | 135 |
| 3 | Denver International Airport |  | US | 131 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 117 |
| 6 | Frankfurt am Main International Airport |  | DE | 115 |
| 7 | La Aurora Airport |  | GT | 109 |
| 8 | Harry Reid International Airport |  | US | 100 |
| 9 | Zurich Airport |  | CH | 87 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 84 |
| 11 | Guaymaral Airport |  | CO | 83 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 81 |
| 14 | Macau International Airport |  | MO | 81 |
| 15 | Chicago O'Hare International Airport |  | US | 79 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 17 | Tenerife Norte Airport |  | ES | 71 |
| 18 | Madrid Barajas International Airport |  | ES | 69 |
| 19 | Reno/Tahoe International Airport |  | US | 66 |
| 20 | Bengaluru International Airport |  | IN | 66 |
| 21 | Kuala Lumpur International Airport |  | MY | 65 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 63 |
| 23 | Ninoy Aquino International Airport |  | PH | 59 |
| 24 | Salt Lake City International Airport |  | US | 59 |
| 25 | Charlotte/Douglas International Airport |  | US | 58 |
| 26 | Vitoria/Foronda Airport |  | ES | 57 |
| 27 | Malpensa International Airport |  | IT | 56 |
| 28 | Daniel K Inouye International Airport |  | US | 56 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 54 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 53 |
| 32 | Miami International Airport |  | US | 52 |
| 33 | Charles de Gaulle International Airport |  | FR | 52 |
| 34 | Congonhas Airport |  | BR | 52 |
| 35 | Seattle-Tacoma International Airport |  | US | 51 |
| 36 | Pune Airport |  | IN | 49 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 48 |
| 38 | O. R. Tambo International Airport |  | ZA | 47 |
| 39 | Barcelona International Airport |  | ES | 46 |
| 40 | Amsterdam Airport Schiphol |  | NL | 45 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 33 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 24 | 26m | 152 km | 62.7 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 21 | 24m | 99 km | 36.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 20 | 1h 47m | 1,156 km | 399.0 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 19 | 15m | 206 km | 67.5 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 19 | 28m | 275 km | 90.0 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 16 | 51m | 556 km | 153.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 15 | 8m | - | - |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 22 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 13 | 1h 1m | 723 km | 162.1 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 13 | 22m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 13 | 1h 55m | 1,304 km | 292.5 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL1254 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-03-31 17:36 UTC | 2026-03-31 19:18 UTC | 1h 41m |
| N329RE |  | Pensacola International Airport (KPNS) | K4R4 (K4R4) | 2026-03-31 18:55 UTC | 2026-03-31 19:15 UTC | 20m |
| CFZCS | CFZ | Red Deer Regional Airport (CYQF) | Clearwater River Airport (CFS8) | 2026-03-31 18:39 UTC | 2026-03-31 19:14 UTC | 34m |
| N40RC |  | Santa Barbara Municipal Airport (KSBA) | Meadows Field (KBFL) | 2026-03-31 18:16 UTC | 2026-03-31 19:09 UTC | 53m |
| N500HA |  | Addison Airport (KADS) | Sulphur Springs Municipal Airport (KSLR) | 2026-03-31 17:51 UTC | 2026-03-31 19:08 UTC | 1h 17m |
| LW11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-03-31 17:00 UTC | 2026-03-31 19:04 UTC | 2h 3m |
| BTZ119 | BTZ | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-03-31 18:48 UTC | 2026-03-31 19:01 UTC | 12m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-03-31 18:44 UTC | 2026-03-31 18:57 UTC | 13m |
| SCU5 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-03-31 18:53 UTC | 2026-03-31 18:53 UTC | 0m |
| N69228 |  | Denton Enterprise Airport (KDTO) | Lazy 9 Ranch Airport (TX64) | 2026-03-31 18:01 UTC | 2026-03-31 18:51 UTC | 50m |
| N138FJ |  | Lovell Field (KCHA) | Miami Executive Airport (KTMB) | 2026-03-31 17:15 UTC | 2026-03-31 18:51 UTC | 1h 35m |
| AMQ14C | AMQ | Berlin Brandenburg Airport (EDDB) | Pruszcz Gdański Airport (EPPR) | 2026-03-31 18:15 UTC | 2026-03-31 18:50 UTC | 34m |
| N992AK |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-03-31 18:31 UTC | 2026-03-31 18:50 UTC | 19m |
| N700TX |  | Mineola Wisener Field (K3F9) | Gregory M Simmons Memorial Airport (KGZN) | 2026-03-31 18:14 UTC | 2026-03-31 18:48 UTC | 33m |
| PPLJA | PPL | Pinto Martins International Airport (SBFZ) | SWBE (SWBE) | 2026-03-31 18:27 UTC | 2026-03-31 18:47 UTC | 20m |
| ITCHY1 | ITC | Dave Eby Field (4XA5) | Anadarko Municipal Airport (KF68) | 2026-03-31 18:36 UTC | 2026-03-31 18:47 UTC | 10m |
| N759LV |  | Nary Ntl-Shefland Field (5MN1) | Estherville Municipal Airport (KEST) | 2026-03-31 17:37 UTC | 2026-03-31 18:46 UTC | 1h 8m |
| N1481V |  | Tampa North Aero Park Airport (KX39) | Zephyrhills Municipal Airport (KZPH) | 2026-03-31 18:10 UTC | 2026-03-31 18:44 UTC | 33m |
| N8306D |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-03-31 18:20 UTC | 2026-03-31 18:43 UTC | 22m |
| SKW5310 | SkyWest Airlines | Denver International Airport (KDEN) | Ohkay Owingeh Airport (KE14) | 2026-03-31 17:58 UTC | 2026-03-31 18:39 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
