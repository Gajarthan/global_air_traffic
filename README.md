# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_21:49:16_UTC-green)

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

**Latest saved flight:** 2026-03-30 21:49:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 21:49:16 UTC

- **5,545** saved flights
- **3,788** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,545** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **69,883.7 tonnes** estimated CO2 emissions
- **4,051,228 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 292 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 139 |
| 4 | EJA | 122 |
| 5 | American Airlines | 113 |
| 6 | Southwest Airlines | 93 |
| 7 | ENY | 87 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 62 |
| 10 | AXM | 58 |
| 11 | Vueling | 54 |
| 12 | LXJ | 53 |
| 13 | Delta Air Lines | 52 |
| 14 | United Airlines | 44 |
| 15 | WIF | 43 |
| 16 | VIV | 42 |
| 17 | All Nippon Airways | 39 |
| 18 | Cathay Pacific | 38 |
| 19 | Swiss International | 38 |
| 20 | AZU | 37 |
| 21 | Japan Airlines | 37 |
| 22 | Avianca | 35 |
| 23 | AXB | 34 |
| 24 | Alaska Airlines | 33 |
| 25 | EDV | 33 |
| 26 | QLK | 33 |
| 27 | VOE | 31 |
| 28 | EJU | 30 |
| 29 | BRC | 28 |
| 30 | GLO | 28 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4923 |
| 2 | 🇮🇳 IN | 416 |
| 3 | 🇪🇸 ES | 407 |
| 4 | 🇦🇺 AU | 305 |
| 5 | 🇧🇷 BR | 288 |
| 6 | 🇨🇴 CO | 280 |
| 7 | 🇮🇹 IT | 259 |
| 8 | 🇯🇵 JP | 254 |
| 9 | 🇩🇪 DE | 242 |
| 10 | 🇨🇦 CA | 233 |
| 11 | 🇲🇽 MX | 205 |
| 12 | 🇬🇧 GB | 183 |
| 13 | 🇫🇷 FR | 169 |
| 14 | 🇳🇴 NO | 143 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇨🇭 CH | 124 |
| 17 | 🇿🇦 ZA | 123 |
| 18 | 🇬🇹 GT | 121 |
| 19 | 🇬🇷 GR | 117 |
| 20 | 🇵🇭 PH | 109 |
| 21 | 🇹🇷 TR | 91 |
| 22 | 🇳🇿 NZ | 85 |
| 23 | 🇹🇭 TH | 73 |
| 24 | 🇲🇦 MA | 67 |
| 25 | 🇲🇴 MO | 65 |
| 26 | 🇵🇱 PL | 65 |
| 27 | 🇧🇸 BS | 60 |
| 28 | 🇮🇩 ID | 58 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 49 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 152 |
| 2 | Denver International Airport |  | US | 115 |
| 3 | El Dorado International Airport |  | CO | 101 |
| 4 | Indira Gandhi International Airport |  | IN | 94 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 83 |
| 7 | Frankfurt am Main International Airport |  | DE | 80 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 71 |
| 9 | Harry Reid International Airport |  | US | 66 |
| 10 | Chicago O'Hare International Airport |  | US | 65 |
| 11 | Macau International Airport |  | MO | 65 |
| 12 | Zurich Airport |  | CH | 65 |
| 13 | Guaymaral Airport |  | CO | 65 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 62 |
| 15 | Tenerife Norte Airport |  | ES | 62 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 51 |
| 18 | Reno/Tahoe International Airport |  | US | 49 |
| 19 | Madrid Barajas International Airport |  | ES | 48 |
| 20 | Ninoy Aquino International Airport |  | PH | 48 |
| 21 | Miami International Airport |  | US | 46 |
| 22 | Bengaluru International Airport |  | IN | 46 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 24 | Kuala Lumpur International Airport |  | MY | 46 |
| 25 | Charlotte/Douglas International Airport |  | US | 45 |
| 26 | Salt Lake City International Airport |  | US | 45 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 44 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 44 |
| 29 | Charles de Gaulle International Airport |  | FR | 43 |
| 30 | Malpensa International Airport |  | IT | 42 |
| 31 | Congonhas Airport |  | BR | 42 |
| 32 | O. R. Tambo International Airport |  | ZA | 42 |
| 33 | Centennial Airport |  | US | 41 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 40 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 40 |
| 36 | Los Angeles International Airport |  | US | 38 |
| 37 | Vitoria/Foronda Airport |  | ES | 38 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |
| 39 | Austin-Bergstrom International Airport |  | US | 37 |
| 40 | Daniel K Inouye International Airport |  | US | 36 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 14 | 15m | 206 km | 49.8 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 14 | 1h 51m | 1,156 km | 279.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 14 | 4m | - | - |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 18 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 11 | 1h 56m | 1,304 km | 247.5 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 10 | 1h 2m | 723 km | 124.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3570E |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-03-30 21:23 UTC | 2026-03-30 21:49 UTC | 25m |
| N70075 |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-03-30 20:52 UTC | 2026-03-30 21:48 UTC | 56m |
| HAWK293 | HAW | Kingsville Nas Airport (KNQI) | XS51 (XS51) | 2026-03-30 21:24 UTC | 2026-03-30 21:42 UTC | 17m |
| CPA953 | Cathay Pacific | Guangzhou Baiyun International Airport (ZGGG) | Macau International Airport (VMMC) | 2026-03-30 21:27 UTC | 2026-03-30 21:41 UTC | 13m |
| R21201 |  | Gold King Creek Airport (PAAN) | Ladd Army Air Field (PAFB) | 2026-03-30 20:53 UTC | 2026-03-30 21:40 UTC | 47m |
| N759LV |  | 0MN5 (0MN5) | 0MN5 (0MN5) | 2026-03-30 20:15 UTC | 2026-03-30 21:30 UTC | 1h 15m |
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-03-30 20:36 UTC | 2026-03-30 21:29 UTC | 52m |
| N33RK |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-03-30 20:56 UTC | 2026-03-30 21:28 UTC | 32m |
| GJS4470 | GJS | Tannehill Airfield (MI60) | Chicago O'Hare International Airport (KORD) | 2026-03-30 20:46 UTC | 2026-03-30 21:27 UTC | 41m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-03-30 17:08 UTC | 2026-03-30 21:24 UTC | 4h 15m |
| BYF18 | BYF | San Carlos Airport (KSQL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-03-30 20:59 UTC | 2026-03-30 21:20 UTC | 20m |
| ZKHVH | ZKH | Gore3 Airport (NZGC) | Gore3 Airport (NZGC) | 2026-03-30 20:44 UTC | 2026-03-30 21:19 UTC | 34m |
| AM370 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-03-30 20:49 UTC | 2026-03-30 21:13 UTC | 24m |
| ROKT61 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Waynesboro Municipal Airport (K2R0) | 2026-03-30 20:39 UTC | 2026-03-30 21:12 UTC | 32m |
| N321FS |  | Brigham City Regional Airport (KBMC) | Logan-Cache Airport (KLGU) | 2026-03-30 20:02 UTC | 2026-03-30 21:11 UTC | 1h 8m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-03-30 21:11 UTC | 2026-03-30 21:11 UTC | 0m |
| UAE46 | Emirates | Frankfurt am Main International Airport (EDDF) | Shaibah Airport (OESB) | 2026-03-30 15:07 UTC | 2026-03-30 21:11 UTC | 6h 4m |
| N9042Q |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-03-30 20:20 UTC | 2026-03-30 21:10 UTC | 50m |
| N758MG |  | Des Moines International Airport (KDSM) | Dubuque Regional Airport (KDBQ) | 2026-03-30 20:42 UTC | 2026-03-30 21:10 UTC | 28m |
| RAX108 | RAX | Oakland County International Airport (KPTK) | 5TA6 (5TA6) | 2026-03-30 18:30 UTC | 2026-03-30 21:08 UTC | 2h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
