# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_23:27:50_UTC-green)

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

**Latest saved flight:** 2026-04-01 23:27:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 23:27:50 UTC

- **10,014** saved flights
- **5,971** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,014** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **121,807.7 tonnes** estimated CO2 emissions
- **7,061,315 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 467 |
| 2 | Ryanair | 383 |
| 3 | IndiGo | 263 |
| 4 | EJA | 212 |
| 5 | American Airlines | 184 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 157 |
| 8 | ENY | 136 |
| 9 | Vueling | 106 |
| 10 | LATAM Airlines | 103 |
| 11 | AXM | 102 |
| 12 | LXJ | 98 |
| 13 | Delta Air Lines | 84 |
| 14 | All Nippon Airways | 80 |
| 15 | WIF | 80 |
| 16 | QLK | 77 |
| 17 | Swiss International | 73 |
| 18 | AZU | 71 |
| 19 | VIV | 70 |
| 20 | Alaska Airlines | 65 |
| 21 | United Airlines | 65 |
| 22 | EDV | 64 |
| 23 | AXB | 63 |
| 24 | Japan Airlines | 60 |
| 25 | Avianca | 58 |
| 26 | BRC | 58 |
| 27 | Cathay Pacific | 57 |
| 28 | easyJet | 57 |
| 29 | EJU | 55 |
| 30 | AEE | 51 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8378 |
| 2 | 🇮🇳 IN | 810 |
| 3 | 🇪🇸 ES | 766 |
| 4 | 🇦🇺 AU | 743 |
| 5 | 🇩🇪 DE | 527 |
| 6 | 🇧🇷 BR | 525 |
| 7 | 🇨🇴 CO | 508 |
| 8 | 🇨🇦 CA | 491 |
| 9 | 🇯🇵 JP | 465 |
| 10 | 🇮🇹 IT | 438 |
| 11 | 🇲🇽 MX | 367 |
| 12 | 🇬🇧 GB | 352 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 227 |
| 17 | 🇳🇿 NZ | 226 |
| 18 | 🇨🇭 CH | 225 |
| 19 | 🇬🇹 GT | 209 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 176 |
| 22 | 🇹🇷 TR | 162 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 117 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇴 MO | 101 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 246 |
| 2 | Denver International Airport |  | US | 185 |
| 3 | Indira Gandhi International Airport |  | IN | 178 |
| 4 | Tokyo International Airport |  | JP | 166 |
| 5 | Frankfurt am Main International Airport |  | DE | 166 |
| 6 | El Dorado International Airport |  | CO | 165 |
| 7 | Guaymaral Airport |  | CO | 148 |
| 8 | La Aurora Airport |  | GT | 146 |
| 9 | Harry Reid International Airport |  | US | 139 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 121 |
| 11 | Zurich Airport |  | CH | 113 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 105 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 105 |
| 15 | Chicago O'Hare International Airport |  | US | 104 |
| 16 | Macau International Airport |  | MO | 101 |
| 17 | Tenerife Norte Airport |  | ES | 92 |
| 18 | Charlotte/Douglas International Airport |  | US | 91 |
| 19 | Reno/Tahoe International Airport |  | US | 91 |
| 20 | Madrid Barajas International Airport |  | ES | 91 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 88 |
| 22 | Bengaluru International Airport |  | IN | 87 |
| 23 | Kuala Lumpur International Airport |  | MY | 85 |
| 24 | Ninoy Aquino International Airport |  | PH | 80 |
| 25 | Congonhas Airport |  | BR | 79 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 74 |
| 28 | Salt Lake City International Airport |  | US | 74 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 74 |
| 30 | Malpensa International Airport |  | IT | 73 |
| 31 | Daniel K Inouye International Airport |  | US | 72 |
| 32 | Vitoria/Foronda Airport |  | ES | 71 |
| 33 | Pune Airport |  | IN | 70 |
| 34 | Seattle-Tacoma International Airport |  | US | 70 |
| 35 | Charles de Gaulle International Airport |  | FR | 69 |
| 36 | Barcelona International Airport |  | ES | 69 |
| 37 | Austin-Bergstrom International Airport |  | US | 67 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 65 |
| 40 | Bodø Airport |  | NO | 65 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 46 | 14m | 114 km | 90.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 27 | 53m | 556 km | 258.8 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 25 | 15m | 206 km | 88.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 23 | 30m | 369 km | 146.4 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 19 | 1h 55m | 1,304 km | 427.5 t |
| 22 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 15 | 54m | 630 km | 162.9 t |
| 29 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 30 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 15 | 18m | 26 km | 6.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N182HE |  | FL47 (FL47) | Wauchula Municipal Airport (KCHN) | 2026-04-01 22:20 UTC | 2026-04-01 23:27 UTC | 1h 7m |
| MJO | MJO | Tangalooma Resort Airport (YXTA) | Tangalooma Resort Airport (YXTA) | 2026-04-01 22:51 UTC | 2026-04-01 23:14 UTC | 23m |
| CPA040 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-04-01 18:48 UTC | 2026-04-01 23:10 UTC | 4h 22m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-01 11:31 UTC | 2026-04-01 23:09 UTC | 11h 38m |
| CXK245 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-01 22:58 UTC | 2026-04-01 23:05 UTC | 7m |
| OXF2477 | OXF | Falcon Field (KFFZ) | Coolidge Municipal Airport (KP08) | 2026-04-01 21:46 UTC | 2026-04-01 23:03 UTC | 1h 16m |
| RDHK731 | RDH | Felker Army Air Field (KFAF) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-01 22:41 UTC | 2026-04-01 22:59 UTC | 17m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-01 22:40 UTC | 2026-04-01 22:59 UTC | 18m |
| STGRY44 | STG | Easterwood Field (KCLL) | Coulter Field (KCFD) | 2026-04-01 22:51 UTC | 2026-04-01 22:56 UTC | 5m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-01 11:11 UTC | 2026-04-01 22:55 UTC | 11h 44m |
| N55515 |  | Phoenix Goodyear Airport (KGYR) | Lakeside Airpark (AZ05) | 2026-04-01 22:26 UTC | 2026-04-01 22:54 UTC | 28m |
| QLK376D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-01 22:29 UTC | 2026-04-01 22:52 UTC | 23m |
| LS20 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 22:31 UTC | 2026-04-01 22:50 UTC | 18m |
| N518JG |  | Concord-Padgett Regional Airport (KJQF) | Marlboro County Jetport/H E Avent Field (KBBP) | 2026-04-01 22:36 UTC | 2026-04-01 22:50 UTC | 13m |
| N471AR |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-01 22:23 UTC | 2026-04-01 22:41 UTC | 17m |
| TRA16U | TRA | Alicante International Airport (LEAL) | Amsterdam Airport Schiphol (EHAM) | 2026-04-01 20:13 UTC | 2026-04-01 22:38 UTC | 2h 25m |
| CRN511 | CRN | Kelowna Airport (CYLW) | Kaslo Airport (CBR2) | 2026-04-01 22:13 UTC | 2026-04-01 22:38 UTC | 24m |
| DSU24 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-04-01 22:31 UTC | 2026-04-01 22:35 UTC | 4m |
| LR453 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-01 22:02 UTC | 2026-04-01 22:35 UTC | 32m |
| N68329 |  | Lehigh Valley International Airport (KABE) | Sency Airport (55PA) | 2026-04-01 22:14 UTC | 2026-04-01 22:34 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
