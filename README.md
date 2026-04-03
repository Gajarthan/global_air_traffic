# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_15:32:32_UTC-green)

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

**Latest saved flight:** 2026-04-03 15:32:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 15:32:32 UTC

- **13,515** saved flights
- **7,520** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,515** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **167,933.0 tonnes** estimated CO2 emissions
- **9,735,248 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 563 |
| 2 | Ryanair | 520 |
| 3 | IndiGo | 390 |
| 4 | EJA | 261 |
| 5 | American Airlines | 239 |
| 6 | Lufthansa | 206 |
| 7 | Southwest Airlines | 192 |
| 8 | ENY | 170 |
| 9 | Vueling | 143 |
| 10 | AXM | 141 |
| 11 | LATAM Airlines | 140 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 119 |
| 15 | Swiss International | 106 |
| 16 | Delta Air Lines | 103 |
| 17 | AZU | 102 |
| 18 | VIV | 98 |
| 19 | WIF | 97 |
| 20 | Japan Airlines | 89 |
| 21 | AXB | 88 |
| 22 | Alaska Airlines | 87 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 83 |
| 26 | EJU | 82 |
| 27 | AEE | 79 |
| 28 | EDV | 79 |
| 29 | BRC | 75 |
| 30 | GLO | 75 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10623 |
| 2 | 🇮🇳 IN | 1194 |
| 3 | 🇦🇺 AU | 1080 |
| 4 | 🇪🇸 ES | 1039 |
| 5 | 🇧🇷 BR | 775 |
| 6 | 🇩🇪 DE | 729 |
| 7 | 🇯🇵 JP | 725 |
| 8 | 🇨🇴 CO | 634 |
| 9 | 🇨🇦 CA | 617 |
| 10 | 🇮🇹 IT | 597 |
| 11 | 🇬🇧 GB | 521 |
| 12 | 🇲🇽 MX | 473 |
| 13 | 🇫🇷 FR | 466 |
| 14 | 🇬🇷 GR | 362 |
| 15 | 🇨🇭 CH | 356 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 317 |
| 18 | 🇳🇴 NO | 311 |
| 19 | 🇿🇦 ZA | 283 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 249 |
| 22 | 🇬🇹 GT | 249 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 189 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇮🇩 ID | 166 |
| 27 | 🇲🇦 MA | 162 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇲🇪 ME | 142 |
| 30 | 🇳🇱 NL | 138 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 321 |
| 2 | Indira Gandhi International Airport |  | IN | 255 |
| 3 | Tokyo International Airport |  | JP | 253 |
| 4 | Denver International Airport |  | US | 234 |
| 5 | El Dorado International Airport |  | CO | 224 |
| 6 | Frankfurt am Main International Airport |  | DE | 194 |
| 7 | Harry Reid International Airport |  | US | 184 |
| 8 | La Aurora Airport |  | GT | 173 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 167 |
| 10 | Zurich Airport |  | CH | 165 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 154 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 146 |
| 15 | Bengaluru International Airport |  | IN | 133 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 127 |
| 17 | Chicago O'Hare International Airport |  | US | 125 |
| 18 | Congonhas Airport |  | BR | 122 |
| 19 | Ninoy Aquino International Airport |  | PH | 121 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 118 |
| 21 | Madrid Barajas International Airport |  | ES | 118 |
| 22 | Charlotte/Douglas International Airport |  | US | 116 |
| 23 | Kuala Lumpur International Airport |  | MY | 116 |
| 24 | Tenerife Norte Airport |  | ES | 111 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 108 |
| 26 | Vitoria/Foronda Airport |  | ES | 103 |
| 27 | Salt Lake City International Airport |  | US | 99 |
| 28 | Reno/Tahoe International Airport |  | US | 98 |
| 29 | Charles de Gaulle International Airport |  | FR | 98 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 98 |
| 31 | Malpensa International Airport |  | IT | 97 |
| 32 | Daniel K Inouye International Airport |  | US | 97 |
| 33 | Barcelona International Airport |  | ES | 93 |
| 34 | Pune Airport |  | IN | 92 |
| 35 | Gimpo International Airport |  | KR | 86 |
| 36 | Seattle-Tacoma International Airport |  | US | 86 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 38 | Austin-Bergstrom International Airport |  | US | 85 |
| 39 | Amsterdam Airport Schiphol |  | NL | 83 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 83 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 62 | 14m | 114 km | 121.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 42 | 1h 46m | 1,156 km | 837.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 35 | 22m | 99 km | 60.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 32 | 28m | 275 km | 151.6 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 32 | 26m | 152 km | 83.6 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 30 | 53m | 556 km | 287.6 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 28 | 1h 55m | 1,304 km | 629.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 25 | 9m | - | - |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 19 | 20m | 250 km | 82.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EPI624 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-04-03 15:17 UTC | 2026-04-03 15:32 UTC | 14m |
| N901KS |  | Lakeland Linder International Airport (KLAL) | FL00 (FL00) | 2026-04-03 14:49 UTC | 2026-04-03 15:31 UTC | 42m |
| N850TV |  | Mckinney Ntl Airport (KTKI) | Mc Alester Regional Airport (KMLC) | 2026-04-03 14:46 UTC | 2026-04-03 15:30 UTC | 44m |
| CGMIO | CGM | Oshawa Airport (CYOO) | Brampton Airport (CNC3) | 2026-04-03 14:53 UTC | 2026-04-03 15:22 UTC | 29m |
| N274MA |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-04-03 14:24 UTC | 2026-04-03 15:21 UTC | 56m |
| N189K |  | Smith Reynolds Airport (KINT) | Yonder Airport (NC65) | 2026-04-03 15:00 UTC | 2026-04-03 15:21 UTC | 21m |
| RYR9EY | Ryanair | Comiso Airport Vincenzo Magliocco (LICB) | Malpensa International Airport (LIMC) | 2026-04-03 13:41 UTC | 2026-04-03 15:20 UTC | 1h 38m |
| JUMP3 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-04-03 15:17 UTC | 2026-04-03 15:19 UTC | 2m |
| LLN106 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | 5TS4 (5TS4) | 2026-04-03 14:43 UTC | 2026-04-03 15:18 UTC | 35m |
| N114UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-04-03 14:17 UTC | 2026-04-03 15:17 UTC | 1h 0m |
| RENO71 | REN | Flysooner Field (OK50) | Ramey 1 Airport (0OK8) | 2026-04-03 14:40 UTC | 2026-04-03 15:17 UTC | 37m |
| N172CY |  | Sugar Land Regional Airport (KSGR) | Sugar Land Regional Airport (KSGR) | 2026-04-03 14:34 UTC | 2026-04-03 15:16 UTC | 41m |
| CAL109 | CAL | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-04-03 11:36 UTC | 2026-04-03 15:15 UTC | 3h 38m |
| EJA626 | EJA | Westchester County Airport (KHPN) | Miami Executive Airport (KTMB) | 2026-04-03 12:27 UTC | 2026-04-03 15:10 UTC | 2h 43m |
| TGJFC | TGJ | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-03 14:47 UTC | 2026-04-03 15:09 UTC | 22m |
| N900LN |  | Ellington Airport (KEFD) | LS90 (LS90) | 2026-04-03 14:37 UTC | 2026-04-03 15:04 UTC | 26m |
| PAIN12 | PAI | Flysooner Field (OK50) | Comanche County Airport (K3K8) | 2026-04-03 14:17 UTC | 2026-04-03 15:04 UTC | 46m |
| N314LM |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-03 14:43 UTC | 2026-04-03 15:03 UTC | 20m |
| N576MA |  | Central Il Regional/Bloomington-Normal Airport (KBMI) | Central Il Regional/Bloomington-Normal Airport (KBMI) | 2026-04-03 14:54 UTC | 2026-04-03 15:00 UTC | 5m |
| RYR54RU | Ryanair | Paris Beauvais Tille Airport (LFOB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-03 13:13 UTC | 2026-04-03 15:00 UTC | 1h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
