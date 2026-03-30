# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_21:04:50_UTC-green)

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

**Latest saved flight:** 2026-03-30 21:04:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 21:04:50 UTC

- **5,445** saved flights
- **3,739** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,445** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **68,991.6 tonnes** estimated CO2 emissions
- **3,999,514 km** total distance flown
- **872 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 282 |
| 2 | Ryanair | 206 |
| 3 | IndiGo | 136 |
| 4 | EJA | 122 |
| 5 | American Airlines | 111 |
| 6 | Southwest Airlines | 89 |
| 7 | ENY | 85 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 62 |
| 10 | AXM | 58 |
| 11 | Vueling | 54 |
| 12 | LXJ | 53 |
| 13 | Delta Air Lines | 52 |
| 14 | VIV | 42 |
| 15 | WIF | 42 |
| 16 | United Airlines | 41 |
| 17 | All Nippon Airways | 39 |
| 18 | Swiss International | 38 |
| 19 | AZU | 37 |
| 20 | Cathay Pacific | 37 |
| 21 | Japan Airlines | 37 |
| 22 | Avianca | 34 |
| 23 | AXB | 34 |
| 24 | EDV | 33 |
| 25 | QLK | 33 |
| 26 | Alaska Airlines | 32 |
| 27 | VOE | 31 |
| 28 | EJU | 30 |
| 29 | Air France | 27 |
| 30 | BRC | 27 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 4811 |
| 2 | 🇮🇳 IN | 409 |
| 3 | 🇪🇸 ES | 404 |
| 4 | 🇦🇺 AU | 299 |
| 5 | 🇧🇷 BR | 282 |
| 6 | 🇨🇴 CO | 274 |
| 7 | 🇮🇹 IT | 256 |
| 8 | 🇯🇵 JP | 252 |
| 9 | 🇩🇪 DE | 241 |
| 10 | 🇨🇦 CA | 226 |
| 11 | 🇲🇽 MX | 202 |
| 12 | 🇬🇧 GB | 183 |
| 13 | 🇫🇷 FR | 169 |
| 14 | 🇳🇴 NO | 141 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇨🇭 CH | 124 |
| 17 | 🇿🇦 ZA | 123 |
| 18 | 🇬🇹 GT | 121 |
| 19 | 🇬🇷 GR | 117 |
| 20 | 🇵🇭 PH | 109 |
| 21 | 🇹🇷 TR | 90 |
| 22 | 🇹🇭 TH | 73 |
| 23 | 🇳🇿 NZ | 73 |
| 24 | 🇲🇦 MA | 66 |
| 25 | 🇵🇱 PL | 64 |
| 26 | 🇲🇴 MO | 63 |
| 27 | 🇧🇸 BS | 59 |
| 28 | 🇮🇩 ID | 58 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 49 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 149 |
| 2 | Denver International Airport |  | US | 107 |
| 3 | El Dorado International Airport |  | CO | 99 |
| 4 | Indira Gandhi International Airport |  | IN | 93 |
| 5 | Tokyo International Airport |  | JP | 85 |
| 6 | La Aurora Airport |  | GT | 83 |
| 7 | Frankfurt am Main International Airport |  | DE | 79 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 70 |
| 9 | Zurich Airport |  | CH | 65 |
| 10 | Guaymaral Airport |  | CO | 65 |
| 11 | Chicago O'Hare International Airport |  | US | 63 |
| 12 | Macau International Airport |  | MO | 63 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 62 |
| 14 | Tenerife Norte Airport |  | ES | 62 |
| 15 | Harry Reid International Airport |  | US | 61 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 51 |
| 18 | Reno/Tahoe International Airport |  | US | 48 |
| 19 | Madrid Barajas International Airport |  | ES | 48 |
| 20 | Ninoy Aquino International Airport |  | PH | 48 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 22 | Kuala Lumpur International Airport |  | MY | 46 |
| 23 | Charlotte/Douglas International Airport |  | US | 45 |
| 24 | Miami International Airport |  | US | 45 |
| 25 | Bengaluru International Airport |  | IN | 45 |
| 26 | Salt Lake City International Airport |  | US | 44 |
| 27 | Charles de Gaulle International Airport |  | FR | 43 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 43 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 43 |
| 30 | Malpensa International Airport |  | IT | 42 |
| 31 | O. R. Tambo International Airport |  | ZA | 42 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 40 |
| 33 | Congonhas Airport |  | BR | 40 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 39 |
| 35 | Centennial Airport |  | US | 39 |
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
| 12 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 14 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 13 | 30m | 369 km | 82.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 16 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 13 | 4m | - | - |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 18 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 12 | 29m | 69 km | 14.3 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 11 | 1h 56m | 1,304 km | 247.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 9 | 1h 3m | 723 km | 112.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N947SF |  | Jim & Julie's Airport (96WA) | Renton Municipal Airport (KRNT) | 2026-03-30 19:36 UTC | 2026-03-30 21:04 UTC | 1h 28m |
| N6715A |  | Flying Cloud Airport (KFCM) | Fuhr Flying Svc Airport (60MN) | 2026-03-30 19:34 UTC | 2026-03-30 21:03 UTC | 1h 28m |
| N759UL |  | MY03 (MY03) | MY03 (MY03) | 2026-03-30 20:34 UTC | 2026-03-30 21:01 UTC | 26m |
| WJA430 | WJA | Edmonton International Airport (CYEG) | Toronto Pearson International Airport (CYYZ) | 2026-03-30 17:45 UTC | 2026-03-30 20:55 UTC | 3h 10m |
| N163JC |  | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | La Sarre Airport (CSR8) | 2026-03-30 19:48 UTC | 2026-03-30 20:52 UTC | 1h 4m |
| N984LH |  | Indianapolis Executive Airport (KTYQ) | Tracy Municipal Airport (KTKC) | 2026-03-30 19:35 UTC | 2026-03-30 20:51 UTC | 1h 15m |
| N567JW |  | City Of Colorado Springs Municipal Airport (KCOS) | High Plains Airport Airport (CD15) | 2026-03-30 20:23 UTC | 2026-03-30 20:47 UTC | 24m |
| N390PH |  | Fox Fire Airport (33VA) | William M Tuck Airport (KW78) | 2026-03-30 20:37 UTC | 2026-03-30 20:46 UTC | 9m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-30 06:13 UTC | 2026-03-30 20:46 UTC | 14h 32m |
| N7430Z |  | CN12 (CN12) | CN12 (CN12) | 2026-03-30 20:37 UTC | 2026-03-30 20:42 UTC | 4m |
| SH037 |  | Whiting Field Nas North Airport (KNSE) | Monroe County Aeroplex Airport (KMVC) | 2026-03-30 20:15 UTC | 2026-03-30 20:40 UTC | 25m |
| N5225D |  | Lanett Regional Airport (K7A3) | Lanett Regional Airport (K7A3) | 2026-03-30 20:26 UTC | 2026-03-30 20:38 UTC | 12m |
| XACIC | XAC | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-03-30 20:05 UTC | 2026-03-30 20:33 UTC | 28m |
| URSA31 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-03-30 20:24 UTC | 2026-03-30 20:30 UTC | 6m |
| BRCAT14 | BRC | Roswell Air Center Airport (KROW) | Roswell Air Center Airport (KROW) | 2026-03-30 19:47 UTC | 2026-03-30 20:29 UTC | 42m |
| RENO71 | REN | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-03-30 20:03 UTC | 2026-03-30 20:27 UTC | 24m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-03-30 20:13 UTC | 2026-03-30 20:27 UTC | 13m |
| LYM3710 | LYM | Phoenix Sky Harbor International Airport (KPHX) | Telluride Regional Airport (KTEX) | 2026-03-30 19:26 UTC | 2026-03-30 20:26 UTC | 59m |
| SCU48 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Gregg Airport (7OK1) | 2026-03-30 19:59 UTC | 2026-03-30 20:25 UTC | 26m |
| PERRIS7 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-03-30 19:32 UTC | 2026-03-30 20:25 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
