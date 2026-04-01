# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_18:25:29_UTC-green)

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

**Latest saved flight:** 2026-04-01 18:25:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 18:25:29 UTC

- **9,351** saved flights
- **5,639** unique routes
- **109** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,351** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **112,822.1 tonnes** estimated CO2 emissions
- **6,540,409 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 417 |
| 2 | Ryanair | 358 |
| 3 | IndiGo | 263 |
| 4 | EJA | 187 |
| 5 | American Airlines | 167 |
| 6 | Lufthansa | 161 |
| 7 | Southwest Airlines | 141 |
| 8 | ENY | 128 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 91 |
| 12 | LXJ | 85 |
| 13 | All Nippon Airways | 79 |
| 14 | WIF | 76 |
| 15 | Delta Air Lines | 74 |
| 16 | Swiss International | 72 |
| 17 | QLK | 70 |
| 18 | AXB | 62 |
| 19 | AZU | 62 |
| 20 | VIV | 62 |
| 21 | Japan Airlines | 60 |
| 22 | Alaska Airlines | 58 |
| 23 | EDV | 58 |
| 24 | BRC | 57 |
| 25 | United Airlines | 57 |
| 26 | EJU | 53 |
| 27 | Avianca | 52 |
| 28 | easyJet | 52 |
| 29 | AEE | 50 |
| 30 | Cathay Pacific | 49 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7668 |
| 2 | 🇮🇳 IN | 803 |
| 3 | 🇪🇸 ES | 740 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 516 |
| 6 | 🇧🇷 BR | 467 |
| 7 | 🇯🇵 JP | 461 |
| 8 | 🇨🇦 CA | 454 |
| 9 | 🇨🇴 CO | 448 |
| 10 | 🇮🇹 IT | 420 |
| 11 | 🇬🇧 GB | 334 |
| 12 | 🇲🇽 MX | 324 |
| 13 | 🇫🇷 FR | 293 |
| 14 | 🇳🇴 NO | 253 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 224 |
| 17 | 🇨🇭 CH | 220 |
| 18 | 🇿🇦 ZA | 201 |
| 19 | 🇳🇿 NZ | 199 |
| 20 | 🇬🇹 GT | 194 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇰🇷 KR | 157 |
| 23 | 🇹🇷 TR | 156 |
| 24 | 🇵🇱 PL | 124 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇹🇭 TH | 113 |
| 27 | 🇲🇦 MA | 111 |
| 28 | 🇲🇴 MO | 92 |
| 29 | 🇧🇸 BS | 88 |
| 30 | 🇳🇱 NL | 87 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 220 |
| 2 | Indira Gandhi International Airport |  | IN | 175 |
| 3 | Denver International Airport |  | US | 165 |
| 4 | Tokyo International Airport |  | JP | 165 |
| 5 | Frankfurt am Main International Airport |  | DE | 163 |
| 6 | El Dorado International Airport |  | CO | 145 |
| 7 | La Aurora Airport |  | GT | 137 |
| 8 | Harry Reid International Airport |  | US | 127 |
| 9 | Guaymaral Airport |  | CO | 127 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 110 |
| 11 | Zurich Airport |  | CH | 110 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 109 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 95 |
| 15 | Chicago O'Hare International Airport |  | US | 95 |
| 16 | Macau International Airport |  | MO | 92 |
| 17 | Tenerife Norte Airport |  | ES | 90 |
| 18 | Bengaluru International Airport |  | IN | 87 |
| 19 | Kuala Lumpur International Airport |  | MY | 85 |
| 20 | Reno/Tahoe International Airport |  | US | 84 |
| 21 | Madrid Barajas International Airport |  | ES | 83 |
| 22 | Charlotte/Douglas International Airport |  | US | 82 |
| 23 | Ninoy Aquino International Airport |  | PH | 78 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 77 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 73 |
| 26 | Malpensa International Airport |  | IT | 72 |
| 27 | Vitoria/Foronda Airport |  | ES | 69 |
| 28 | Pune Airport |  | IN | 69 |
| 29 | Daniel K Inouye International Airport |  | US | 68 |
| 30 | Barcelona International Airport |  | ES | 68 |
| 31 | Congonhas Airport |  | BR | 68 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 67 |
| 33 | Salt Lake City International Airport |  | US | 67 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 67 |
| 35 | Charles de Gaulle International Airport |  | FR | 65 |
| 36 | Miami International Airport |  | US | 63 |
| 37 | Seattle-Tacoma International Airport |  | US | 63 |
| 38 | Gimpo International Airport |  | KR | 60 |
| 39 | Bodø Airport |  | NO | 58 |
| 40 | Austin-Bergstrom International Airport |  | US | 57 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 51 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 41 | 14m | 114 km | 80.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 29 | 1h 45m | 1,156 km | 578.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 27 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 26 | 23m | 99 km | 44.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 24 | 52m | 556 km | 230.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 22 | 1h 42m | 1,423 km | 539.9 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 21 | 9m | - | - |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 27 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 14 | 54m | 630 km | 152.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-01 18:12 UTC | 2026-04-01 18:25 UTC | 13m |
| ZKVME | ZKV | Molesworth Airport (NZML) | Wellington International Airport (NZWN) | 2026-04-01 18:07 UTC | 2026-04-01 18:22 UTC | 14m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-01 17:33 UTC | 2026-04-01 18:18 UTC | 44m |
| LS20 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 18:04 UTC | 2026-04-01 18:17 UTC | 13m |
| AEE913 | AEE | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-01 16:47 UTC | 2026-04-01 18:17 UTC | 1h 30m |
| DLH7MN | Lufthansa | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Frankfurt am Main International Airport (EDDF) | 2026-04-01 17:05 UTC | 2026-04-01 18:11 UTC | 1h 5m |
| N73054 |  | Felts Field (KSFF) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-04-01 18:00 UTC | 2026-04-01 18:10 UTC | 10m |
| LN43MF |  | Albuquerque International Sunport Airport (KABQ) | Las Cruces International Airport (KLRU) | 2026-04-01 17:15 UTC | 2026-04-01 18:10 UTC | 55m |
| N64EJ |  | Vance Brand Airport (KLMO) | Colorado Plains Regional Airport (KAKO) | 2026-04-01 17:37 UTC | 2026-04-01 18:10 UTC | 32m |
| TIGER33 | TIG | Sandy Creek Airport (73TX) | Dunbar Ranch Airport (0XS8) | 2026-04-01 17:52 UTC | 2026-04-01 18:07 UTC | 14m |
| SXS7AM | SXS | Vienna International Airport (LOWW) | Gaziemir Airport (LTBK) | 2026-04-01 16:11 UTC | 2026-04-01 18:04 UTC | 1h 52m |
| CFMPK | CFM | Winnipeg James Armstrong Richardson International Airport (CYWG) | Matheson Island Airport (CJT2) | 2026-04-01 17:30 UTC | 2026-04-01 18:03 UTC | 33m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-01 17:35 UTC | 2026-04-01 17:57 UTC | 21m |
| XBCCT | XBC | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-01 17:20 UTC | 2026-04-01 17:52 UTC | 32m |
| N256S |  | Monroe Airpark (2FA2) | Orlando Executive Airport (KORL) | 2026-04-01 17:26 UTC | 2026-04-01 17:51 UTC | 24m |
| ASA495 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Yucca Valley Airport (KL22) | 2026-04-01 15:44 UTC | 2026-04-01 17:49 UTC | 2h 4m |
| JBU1380 | JetBlue | Fort Lauderdale/Hollywood International Airport (KFLL) | La Aurora Airport (MGGT) | 2026-04-01 15:09 UTC | 2026-04-01 17:48 UTC | 2h 38m |
| EJA432 | EJA | Marina Municipal Airport (KOAR) | Postoak Airport (76TA) | 2026-04-01 15:47 UTC | 2026-04-01 17:47 UTC | 2h 0m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-01 17:02 UTC | 2026-04-01 17:46 UTC | 44m |
| STMPD19 | STM | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 8CL0 (8CL0) | 2026-04-01 17:10 UTC | 2026-04-01 17:44 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
