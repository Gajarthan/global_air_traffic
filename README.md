# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_03:00:03_UTC-green)

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

**Latest saved flight:** 2026-04-02 03:00:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 03:00:03 UTC

- **10,160** saved flights
- **6,029** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,160** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **123,206.2 tonnes** estimated CO2 emissions
- **7,142,391 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 469 |
| 2 | Ryanair | 383 |
| 3 | IndiGo | 265 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 159 |
| 8 | ENY | 139 |
| 9 | Vueling | 106 |
| 10 | AXM | 105 |
| 11 | LATAM Airlines | 104 |
| 12 | LXJ | 98 |
| 13 | Delta Air Lines | 86 |
| 14 | All Nippon Airways | 84 |
| 15 | QLK | 83 |
| 16 | WIF | 80 |
| 17 | Swiss International | 73 |
| 18 | VIV | 72 |
| 19 | AZU | 71 |
| 20 | Alaska Airlines | 67 |
| 21 | EDV | 65 |
| 22 | United Airlines | 65 |
| 23 | AXB | 63 |
| 24 | Japan Airlines | 61 |
| 25 | Avianca | 60 |
| 26 | BRC | 58 |
| 27 | Cathay Pacific | 58 |
| 28 | easyJet | 57 |
| 29 | EJU | 55 |
| 30 | AEE | 51 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8474 |
| 2 | 🇮🇳 IN | 814 |
| 3 | 🇦🇺 AU | 804 |
| 4 | 🇪🇸 ES | 766 |
| 5 | 🇧🇷 BR | 534 |
| 6 | 🇩🇪 DE | 529 |
| 7 | 🇨🇴 CO | 524 |
| 8 | 🇨🇦 CA | 503 |
| 9 | 🇯🇵 JP | 484 |
| 10 | 🇮🇹 IT | 438 |
| 11 | 🇲🇽 MX | 375 |
| 12 | 🇬🇧 GB | 352 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇳🇿 NZ | 241 |
| 16 | 🇲🇾 MY | 235 |
| 17 | 🇬🇷 GR | 227 |
| 18 | 🇨🇭 CH | 225 |
| 19 | 🇬🇹 GT | 209 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 189 |
| 22 | 🇰🇷 KR | 164 |
| 23 | 🇹🇷 TR | 163 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 123 |
| 26 | 🇲🇦 MA | 117 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇴 MO | 103 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 251 |
| 2 | Denver International Airport |  | US | 188 |
| 3 | Indira Gandhi International Airport |  | IN | 179 |
| 4 | El Dorado International Airport |  | CO | 173 |
| 5 | Tokyo International Airport |  | JP | 172 |
| 6 | Frankfurt am Main International Airport |  | DE | 166 |
| 7 | Guaymaral Airport |  | CO | 148 |
| 8 | La Aurora Airport |  | GT | 146 |
| 9 | Harry Reid International Airport |  | US | 144 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 123 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 117 |
| 12 | Zurich Airport |  | CH | 113 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 15 | Chicago O'Hare International Airport |  | US | 105 |
| 16 | Macau International Airport |  | MO | 103 |
| 17 | Reno/Tahoe International Airport |  | US | 93 |
| 18 | Charlotte/Douglas International Airport |  | US | 92 |
| 19 | Tenerife Norte Airport |  | ES | 92 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 91 |
| 21 | Madrid Barajas International Airport |  | ES | 91 |
| 22 | Bengaluru International Airport |  | IN | 88 |
| 23 | Kuala Lumpur International Airport |  | MY | 87 |
| 24 | Ninoy Aquino International Airport |  | PH | 86 |
| 25 | Congonhas Airport |  | BR | 81 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 76 |
| 27 | Salt Lake City International Airport |  | US | 75 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 75 |
| 29 | Daniel K Inouye International Airport |  | US | 74 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 31 | Malpensa International Airport |  | IT | 73 |
| 32 | Austin-Bergstrom International Airport |  | US | 71 |
| 33 | Vitoria/Foronda Airport |  | ES | 71 |
| 34 | Pune Airport |  | IN | 71 |
| 35 | Seattle-Tacoma International Airport |  | US | 71 |
| 36 | Charles de Gaulle International Airport |  | FR | 69 |
| 37 | Barcelona International Airport |  | ES | 69 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | Calgary International Airport |  | CA | 67 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 65 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 42 | 1h 7m | 706 km | 511.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 36 | 24m | 225 km | 139.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 31 | 30m | 304 km | 162.5 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 31 | 1h 44m | 1,156 km | 618.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 28 | 53m | 556 km | 268.4 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 27 | 20m | 165 km | 76.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 26 | 15m | 206 km | 92.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 24 | 1h 26m | 910 km | 376.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 23 | 30m | 369 km | 146.4 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 20 | 53m | 546 km | 188.3 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 20 | 1h 55m | 1,304 km | 449.9 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 22 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 15 | 17m | 183 km | 47.3 t |
| 28 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 15 | 30m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 15 | 54m | 630 km | 162.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CARGO19 | CAR | Clayton Municipal Airport (K11A) | Clayton Municipal Airport (K11A) | 2026-04-02 02:45 UTC | 2026-04-02 03:00 UTC | 14m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-02 02:25 UTC | 2026-04-02 02:51 UTC | 25m |
| PVF | PVF | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-02 02:24 UTC | 2026-04-02 02:41 UTC | 16m |
| KDJ | KDJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-02 02:17 UTC | 2026-04-02 02:33 UTC | 16m |
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-02 01:57 UTC | 2026-04-02 02:31 UTC | 34m |
| CGCFB | CGC | Calgary International Airport (CYYC) | Fort St. John Airport (CYXJ) | 2026-04-02 00:22 UTC | 2026-04-02 02:17 UTC | 1h 54m |
| SKW377A | SkyWest Airlines | Denver International Airport (KDEN) | Laramie Regional Airport (KLAR) | 2026-04-02 01:57 UTC | 2026-04-02 02:17 UTC | 19m |
| IGO697L | IndiGo | Bengaluru International Airport (VOBL) | Coimbatore Air Force Station (VOSX) | 2026-04-02 01:52 UTC | 2026-04-02 02:16 UTC | 23m |
| BLCAT55 | BLC | Atsugi Naval Air Facility (RJTA) | Matsuyama Airport (RJOM) | 2026-04-02 00:20 UTC | 2026-04-02 02:15 UTC | 1h 55m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-02 01:37 UTC | 2026-04-02 02:15 UTC | 37m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-02 02:02 UTC | 2026-04-02 02:14 UTC | 12m |
| VIV7435 | VIV | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-02 01:32 UTC | 2026-04-02 02:12 UTC | 39m |
| FBIR100 | FBI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-02 02:12 UTC | 2026-04-02 02:12 UTC | 0m |
| CMF2942 | CMF | Chico Regional Airport (KCIC) | Hayward Executive Airport (KHWD) | 2026-04-02 00:50 UTC | 2026-04-02 02:09 UTC | 1h 18m |
| CGNKP | CGN | Toronto Pearson International Airport (CYYZ) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-01 22:52 UTC | 2026-04-02 02:09 UTC | 3h 16m |
| ANA981 | All Nippon Airways | Tokyo International Airport (RJTT) | Kumamoto Airport (RJFT) | 2026-04-02 00:46 UTC | 2026-04-02 02:08 UTC | 1h 22m |
| CARGO13 | CAR | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Hidden Springs Airpark (36AL) | 2026-04-02 01:19 UTC | 2026-04-02 02:08 UTC | 49m |
| ASA1113 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Lihue Airport (PHLI) | 2026-04-02 01:52 UTC | 2026-04-02 02:07 UTC | 15m |
| CPA672 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-01 14:55 UTC | 2026-04-02 02:06 UTC | 11h 10m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-04-02 01:28 UTC | 2026-04-02 02:02 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
