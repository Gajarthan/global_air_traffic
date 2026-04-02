# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_21:19:58_UTC-green)

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

**Latest saved flight:** 2026-04-02 21:19:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 21:19:58 UTC

- **12,123** saved flights
- **6,946** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,123** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **150,363.3 tonnes** estimated CO2 emissions
- **8,716,714 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 531 |
| 2 | Ryanair | 481 |
| 3 | IndiGo | 328 |
| 4 | EJA | 239 |
| 5 | American Airlines | 219 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 181 |
| 8 | ENY | 158 |
| 9 | Vueling | 130 |
| 10 | LATAM Airlines | 124 |
| 11 | AXM | 120 |
| 12 | LXJ | 114 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | Swiss International | 95 |
| 16 | WIF | 95 |
| 17 | Delta Air Lines | 94 |
| 18 | AZU | 88 |
| 19 | VIV | 88 |
| 20 | Alaska Airlines | 81 |
| 21 | AXB | 81 |
| 22 | United Airlines | 79 |
| 23 | Japan Airlines | 77 |
| 24 | EDV | 75 |
| 25 | easyJet | 75 |
| 26 | Cathay Pacific | 73 |
| 27 | EJU | 73 |
| 28 | BRC | 71 |
| 29 | Avianca | 70 |
| 30 | GLO | 66 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9820 |
| 2 | 🇮🇳 IN | 1017 |
| 3 | 🇪🇸 ES | 954 |
| 4 | 🇦🇺 AU | 908 |
| 5 | 🇧🇷 BR | 668 |
| 6 | 🇩🇪 DE | 668 |
| 7 | 🇨🇴 CO | 599 |
| 8 | 🇯🇵 JP | 595 |
| 9 | 🇨🇦 CA | 559 |
| 10 | 🇮🇹 IT | 553 |
| 11 | 🇬🇧 GB | 461 |
| 12 | 🇲🇽 MX | 440 |
| 13 | 🇫🇷 FR | 398 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 296 |
| 17 | 🇲🇾 MY | 273 |
| 18 | 🇳🇿 NZ | 272 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 230 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇹🇷 TR | 212 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇲🇦 MA | 145 |
| 27 | 🇮🇩 ID | 143 |
| 28 | 🇲🇴 MO | 139 |
| 29 | 🇲🇪 ME | 121 |
| 30 | 🇳🇱 NL | 120 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 295 |
| 2 | Indira Gandhi International Airport |  | IN | 220 |
| 3 | Denver International Airport |  | US | 219 |
| 4 | Tokyo International Airport |  | JP | 213 |
| 5 | El Dorado International Airport |  | CO | 207 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 163 |
| 8 | La Aurora Airport |  | GT | 160 |
| 9 | Guaymaral Airport |  | CO | 153 |
| 10 | Zurich Airport |  | CH | 147 |
| 11 | Macau International Airport |  | MO | 139 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 138 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 119 |
| 16 | Chicago O'Hare International Airport |  | US | 118 |
| 17 | Bengaluru International Airport |  | IN | 114 |
| 18 | Madrid Barajas International Airport |  | ES | 108 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 107 |
| 20 | Charlotte/Douglas International Airport |  | US | 107 |
| 21 | Tenerife Norte Airport |  | ES | 106 |
| 22 | Kuala Lumpur International Airport |  | MY | 104 |
| 23 | Congonhas Airport |  | BR | 103 |
| 24 | Reno/Tahoe International Airport |  | US | 97 |
| 25 | Ninoy Aquino International Airport |  | PH | 97 |
| 26 | Vitoria/Foronda Airport |  | ES | 92 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 28 | Salt Lake City International Airport |  | US | 92 |
| 29 | Daniel K Inouye International Airport |  | US | 91 |
| 30 | Malpensa International Airport |  | IT | 90 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 89 |
| 32 | Charles de Gaulle International Airport |  | FR | 86 |
| 33 | Barcelona International Airport |  | ES | 86 |
| 34 | Austin-Bergstrom International Airport |  | US | 81 |
| 35 | Pune Airport |  | IN | 81 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 81 |
| 37 | Seattle-Tacoma International Airport |  | US | 79 |
| 38 | Bodø Airport |  | NO | 78 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 77 |
| 40 | Gimpo International Airport |  | KR | 75 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 57 | 14m | 114 km | 111.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 31 | 15m | 206 km | 110.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 25 | 1h 56m | 1,304 km | 562.4 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 20 | 13m | 99 km | 34.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 30 | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 17 | 44m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N737MF |  | Sacramento Executive Airport (KSAC) | Franklin Field (KF72) | 2026-04-02 20:47 UTC | 2026-04-02 21:19 UTC | 32m |
| N5470W |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-04-02 20:24 UTC | 2026-04-02 21:19 UTC | 55m |
| GARMN12 | GAR | New Century Aircenter Airport (KIXD) | Landmark Mfg Corporation Airport (1MO4) | 2026-04-02 20:18 UTC | 2026-04-02 21:17 UTC | 58m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-02 17:03 UTC | 2026-04-02 21:14 UTC | 4h 11m |
| N4174B |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-04-02 20:48 UTC | 2026-04-02 21:11 UTC | 22m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-02 20:53 UTC | 2026-04-02 21:05 UTC | 12m |
| BRCAT14 | BRC | 81NM (81NM) | 81NM (81NM) | 2026-04-02 20:46 UTC | 2026-04-02 21:04 UTC | 18m |
| CNS976 | CNS | Boca Raton Airport (KBCT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-02 19:02 UTC | 2026-04-02 20:58 UTC | 1h 55m |
| ERU57 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-04-02 20:01 UTC | 2026-04-02 20:57 UTC | 55m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-02 20:44 UTC | 2026-04-02 20:54 UTC | 10m |
| N100HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-02 20:44 UTC | 2026-04-02 20:48 UTC | 3m |
| LYM3710 | LYM | Phoenix Sky Harbor International Airport (KPHX) | Telluride Regional Airport (KTEX) | 2026-04-02 19:46 UTC | 2026-04-02 20:45 UTC | 59m |
| KPO505 | KPO | Palm Beach International Airport (KPBI) | Washington Dulles International Airport (KIAD) | 2026-04-02 18:32 UTC | 2026-04-02 20:43 UTC | 2h 10m |
| QTR8770 | Qatar Airways | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-04-02 10:12 UTC | 2026-04-02 20:42 UTC | 10h 29m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-02 06:03 UTC | 2026-04-02 20:38 UTC | 14h 35m |
| NAC772 | NAC | Ted Stevens Anchorage International Airport (PANC) | New Stuyahok Airport (PANW) | 2026-04-02 19:57 UTC | 2026-04-02 20:36 UTC | 38m |
| BCS692 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-02 09:26 UTC | 2026-04-02 20:34 UTC | 11h 8m |
| VTE3094 | VTE | Chicago O'Hare International Airport (KORD) | II81 (II81) | 2026-04-02 19:55 UTC | 2026-04-02 20:34 UTC | 39m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-02 18:14 UTC | 2026-04-02 20:33 UTC | 2h 18m |
| N726GB |  | Askey Field (9TN5) | MS98 (MS98) | 2026-04-02 19:15 UTC | 2026-04-02 20:33 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
