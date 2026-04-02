# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_23:08:18_UTC-green)

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

**Latest saved flight:** 2026-04-02 23:08:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 23:08:18 UTC

- **12,389** saved flights
- **7,080** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,389** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **154,574.1 tonnes** estimated CO2 emissions
- **8,960,817 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 552 |
| 2 | Ryanair | 482 |
| 3 | IndiGo | 329 |
| 4 | EJA | 246 |
| 5 | American Airlines | 231 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 186 |
| 8 | ENY | 161 |
| 9 | Vueling | 131 |
| 10 | LATAM Airlines | 126 |
| 11 | AXM | 120 |
| 12 | LXJ | 117 |
| 13 | QLK | 104 |
| 14 | All Nippon Airways | 103 |
| 15 | Delta Air Lines | 97 |
| 16 | Swiss International | 95 |
| 17 | WIF | 95 |
| 18 | AZU | 92 |
| 19 | VIV | 91 |
| 20 | Alaska Airlines | 84 |
| 21 | Cathay Pacific | 83 |
| 22 | United Airlines | 82 |
| 23 | AXB | 81 |
| 24 | EDV | 77 |
| 25 | easyJet | 77 |
| 26 | Japan Airlines | 77 |
| 27 | EJU | 73 |
| 28 | BRC | 71 |
| 29 | Avianca | 70 |
| 30 | GLO | 70 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10134 |
| 2 | 🇮🇳 IN | 1020 |
| 3 | 🇪🇸 ES | 956 |
| 4 | 🇦🇺 AU | 939 |
| 5 | 🇧🇷 BR | 695 |
| 6 | 🇩🇪 DE | 671 |
| 7 | 🇨🇴 CO | 611 |
| 8 | 🇯🇵 JP | 597 |
| 9 | 🇨🇦 CA | 581 |
| 10 | 🇮🇹 IT | 558 |
| 11 | 🇬🇧 GB | 467 |
| 12 | 🇲🇽 MX | 454 |
| 13 | 🇫🇷 FR | 399 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 297 |
| 17 | 🇳🇿 NZ | 283 |
| 18 | 🇲🇾 MY | 273 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 234 |
| 21 | 🇵🇭 PH | 218 |
| 22 | 🇹🇷 TR | 213 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 151 |
| 26 | 🇲🇴 MO | 151 |
| 27 | 🇲🇦 MA | 145 |
| 28 | 🇮🇩 ID | 143 |
| 29 | 🇧🇸 BS | 127 |
| 30 | 🇲🇪 ME | 122 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 306 |
| 2 | Denver International Airport |  | US | 227 |
| 3 | Indira Gandhi International Airport |  | IN | 221 |
| 4 | Tokyo International Airport |  | JP | 213 |
| 5 | El Dorado International Airport |  | CO | 212 |
| 6 | Frankfurt am Main International Airport |  | DE | 185 |
| 7 | Harry Reid International Airport |  | US | 169 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Guaymaral Airport |  | CO | 153 |
| 10 | Macau International Airport |  | MO | 151 |
| 11 | Zurich Airport |  | CH | 148 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 142 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 138 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 123 |
| 16 | Chicago O'Hare International Airport |  | US | 121 |
| 17 | Bengaluru International Airport |  | IN | 114 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 111 |
| 19 | Charlotte/Douglas International Airport |  | US | 109 |
| 20 | Congonhas Airport |  | BR | 109 |
| 21 | Madrid Barajas International Airport |  | ES | 108 |
| 22 | Tenerife Norte Airport |  | ES | 106 |
| 23 | Kuala Lumpur International Airport |  | MY | 104 |
| 24 | Ninoy Aquino International Airport |  | PH | 98 |
| 25 | Reno/Tahoe International Airport |  | US | 97 |
| 26 | Daniel K Inouye International Airport |  | US | 93 |
| 27 | Vitoria/Foronda Airport |  | ES | 92 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 29 | Salt Lake City International Airport |  | US | 92 |
| 30 | Malpensa International Airport |  | IT | 91 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 91 |
| 32 | Barcelona International Airport |  | ES | 88 |
| 33 | Charles de Gaulle International Airport |  | FR | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 85 |
| 35 | Seattle-Tacoma International Airport |  | US | 83 |
| 36 | Austin-Bergstrom International Airport |  | US | 82 |
| 37 | Pune Airport |  | IN | 82 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Miami International Airport |  | US | 78 |
| 40 | Bodø Airport |  | NO | 78 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 59 | 14m | 114 km | 115.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 26 | 30m | 369 km | 165.5 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 20 | 13m | 99 km | 34.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |
| 28 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 29 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 18 | 8h 30m | 38 km | 11.7 t |
| 30 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR838 | Qatar Airways | Hamad International Airport (OTHH) | Don Mueang International Airport (VTBD) | 2026-04-02 16:55 UTC | 2026-04-02 23:08 UTC | 6h 12m |
| N771DF |  | Nut Tree Airport (KVCB) | Bermuda Dunes Airport (KUDD) | 2026-04-02 22:09 UTC | 2026-04-02 23:07 UTC | 57m |
| N982RM |  | David Wayne Hooks Memorial Airport (KDWH) | David Wayne Hooks Memorial Airport (KDWH) | 2026-04-02 21:56 UTC | 2026-04-02 23:02 UTC | 1h 6m |
| N4032L |  | 94GA (94GA) | Perry-Houston County Airport (KPXE) | 2026-04-02 21:50 UTC | 2026-04-02 23:01 UTC | 1h 11m |
| BOE716 | BOE | Renton Municipal Airport (KRNT) | 8WA5 (8WA5) | 2026-04-02 21:26 UTC | 2026-04-02 23:00 UTC | 1h 33m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-02 12:00 UTC | 2026-04-02 22:58 UTC | 10h 57m |
| GOON39 | GOO | Grapevine Airstrip (88AZ) | Davis Monthan Afb Airport (KDMA) | 2026-04-02 22:11 UTC | 2026-04-02 22:54 UTC | 42m |
| N64BE |  | Buffalo Niagara International Airport (KBUF) | Chautauqua County/Dunkirk Airport (KDKK) | 2026-04-02 22:17 UTC | 2026-04-02 22:54 UTC | 37m |
| N116MB |  | Addison Airport (KADS) | Jonesboro Municipal Airport (KJBR) | 2026-04-02 21:56 UTC | 2026-04-02 22:52 UTC | 56m |
| CXK173 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-04-02 21:37 UTC | 2026-04-02 22:50 UTC | 1h 12m |
| N952G |  | University-Oxford Airport (KUOX) | Waynesville-St Robert Regional Forney Field (KTBN) | 2026-04-02 21:46 UTC | 2026-04-02 22:49 UTC | 1h 3m |
| N188JB |  | Santa Fe Regional Airport (KSAF) | Blanding Municipal Airport (KBDG) | 2026-04-02 21:28 UTC | 2026-04-02 22:44 UTC | 1h 16m |
| GEIV01 | GEI | Santos Dumont Airport (SBRJ) | Congonhas Airport (SBSP) | 2026-04-02 21:56 UTC | 2026-04-02 22:40 UTC | 43m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-04-02 11:26 UTC | 2026-04-02 22:40 UTC | 11h 13m |
| N1132X |  | KFTG (KFTG) | Pine Bluffs Municipal Airport (K82V) | 2026-04-02 21:49 UTC | 2026-04-02 22:38 UTC | 49m |
| BRG682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-02 22:08 UTC | 2026-04-02 22:38 UTC | 29m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-02 10:29 UTC | 2026-04-02 22:37 UTC | 12h 8m |
| BRG570 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-02 22:07 UTC | 2026-04-02 22:35 UTC | 27m |
| XARUV | XAR | Abraham Gonzalez International Airport (MMCS) | Hermanos Serdan International Airport (MMPB) | 2026-04-02 20:17 UTC | 2026-04-02 22:35 UTC | 2h 17m |
| STGRY26 | STG | Easterwood Field (KCLL) | Easterwood Field (KCLL) | 2026-04-02 22:28 UTC | 2026-04-02 22:34 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
