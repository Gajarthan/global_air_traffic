# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_17:23:39_UTC-green)

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

**Latest saved flight:** 2026-04-02 17:23:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 17:23:39 UTC

- **11,489** saved flights
- **6,622** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,489** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **141,394.0 tonnes** estimated CO2 emissions
- **8,196,755 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 487 |
| 2 | Ryanair | 458 |
| 3 | IndiGo | 325 |
| 4 | EJA | 225 |
| 5 | American Airlines | 200 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 170 |
| 8 | ENY | 144 |
| 9 | Vueling | 124 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 116 |
| 12 | LXJ | 106 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | WIF | 95 |
| 16 | Swiss International | 93 |
| 17 | Delta Air Lines | 88 |
| 18 | AZU | 82 |
| 19 | AXB | 80 |
| 20 | VIV | 79 |
| 21 | Japan Airlines | 77 |
| 22 | Alaska Airlines | 73 |
| 23 | Cathay Pacific | 69 |
| 24 | EDV | 69 |
| 25 | United Airlines | 69 |
| 26 | EJU | 68 |
| 27 | easyJet | 68 |
| 28 | Avianca | 66 |
| 29 | BRC | 64 |
| 30 | GLO | 61 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9087 |
| 2 | 🇮🇳 IN | 1002 |
| 3 | 🇪🇸 ES | 909 |
| 4 | 🇦🇺 AU | 904 |
| 5 | 🇩🇪 DE | 657 |
| 6 | 🇧🇷 BR | 625 |
| 7 | 🇯🇵 JP | 593 |
| 8 | 🇨🇴 CO | 571 |
| 9 | 🇨🇦 CA | 531 |
| 10 | 🇮🇹 IT | 525 |
| 11 | 🇬🇧 GB | 433 |
| 12 | 🇲🇽 MX | 410 |
| 13 | 🇫🇷 FR | 383 |
| 14 | 🇳🇴 NO | 300 |
| 15 | 🇬🇷 GR | 295 |
| 16 | 🇨🇭 CH | 283 |
| 17 | 🇲🇾 MY | 272 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 233 |
| 20 | 🇬🇹 GT | 223 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 194 |
| 24 | 🇵🇱 PL | 167 |
| 25 | 🇹🇭 TH | 149 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇦 MA | 136 |
| 28 | 🇲🇴 MO | 134 |
| 29 | 🇳🇱 NL | 119 |
| 30 | 🇲🇪 ME | 114 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 266 |
| 2 | Indira Gandhi International Airport |  | IN | 215 |
| 3 | Tokyo International Airport |  | JP | 213 |
| 4 | Denver International Airport |  | US | 198 |
| 5 | El Dorado International Airport |  | CO | 193 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 157 |
| 8 | La Aurora Airport |  | GT | 155 |
| 9 | Guaymaral Airport |  | CO | 152 |
| 10 | Zurich Airport |  | CH | 137 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 134 |
| 12 | Macau International Airport |  | MO | 134 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 128 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 114 |
| 16 | Bengaluru International Airport |  | IN | 112 |
| 17 | Chicago O'Hare International Airport |  | US | 111 |
| 18 | Kuala Lumpur International Airport |  | MY | 104 |
| 19 | Madrid Barajas International Airport |  | ES | 102 |
| 20 | Tenerife Norte Airport |  | ES | 102 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 100 |
| 22 | Charlotte/Douglas International Airport |  | US | 99 |
| 23 | Ninoy Aquino International Airport |  | PH | 97 |
| 24 | Congonhas Airport |  | BR | 97 |
| 25 | Reno/Tahoe International Airport |  | US | 96 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Malpensa International Airport |  | IT | 88 |
| 28 | Vitoria/Foronda Airport |  | ES | 86 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 86 |
| 30 | Daniel K Inouye International Airport |  | US | 83 |
| 31 | Charles de Gaulle International Airport |  | FR | 82 |
| 32 | Barcelona International Airport |  | ES | 82 |
| 33 | Pune Airport |  | IN | 78 |
| 34 | Bodø Airport |  | NO | 78 |
| 35 | Salt Lake City International Airport |  | US | 77 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 77 |
| 37 | Austin-Bergstrom International Airport |  | US | 76 |
| 38 | Gimpo International Airport |  | KR | 75 |
| 39 | Seattle-Tacoma International Airport |  | US | 74 |
| 40 | Amsterdam Airport Schiphol |  | NL | 73 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 53 | 14m | 114 km | 104.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 36 | 1h 46m | 1,156 km | 718.2 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 28 | 15m | 206 km | 99.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 27 | 29m | 275 km | 127.9 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 25 | 1h 43m | 1,423 km | 613.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 23 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 22 | 1h 57m | 1,304 km | 494.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 19 | 13m | 99 km | 32.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 17 | 8h 31m | 38 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N285MA |  | Berkeley County Airport (KMKS) | Berkeley County Airport (KMKS) | 2026-04-02 17:04 UTC | 2026-04-02 17:23 UTC | 18m |
| PAT173 | PAT | Buckley Space Force Base Airport (KBKF) | Salina Regional Airport (KSLN) | 2026-04-02 16:02 UTC | 2026-04-02 17:20 UTC | 1h 17m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-02 17:04 UTC | 2026-04-02 17:17 UTC | 12m |
| N288BL |  | Winter Haven Regional Airport (KGIF) | Lakeland Linder International Airport (KLAL) | 2026-04-02 15:56 UTC | 2026-04-02 17:11 UTC | 1h 15m |
| TALON61 | TAL | Salina Regional Airport (KSLN) | Salina Regional Airport (KSLN) | 2026-04-02 16:51 UTC | 2026-04-02 17:09 UTC | 18m |
| AEE852 | AEE | Eleftherios Venizelos International Airport (LGAV) | Zurich Airport (LSZH) | 2026-04-02 13:53 UTC | 2026-04-02 17:05 UTC | 3h 11m |
| N828TR |  | Mc Clellan Airfield (KMCC) | Spokane International Airport (KGEG) | 2026-04-02 15:27 UTC | 2026-04-02 17:04 UTC | 1h 37m |
| VAR624 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-02 16:21 UTC | 2026-04-02 17:04 UTC | 42m |
| CXK396 | CXK | Mesa Gateway Airport (KIWA) | Mesa Gateway Airport (KIWA) | 2026-04-02 16:09 UTC | 2026-04-02 17:01 UTC | 51m |
| N223WT |  | Renton Municipal Airport (KRNT) | William R Fairchild International Airport (KCLM) | 2026-04-02 16:20 UTC | 2026-04-02 17:00 UTC | 40m |
| N359CV |  | Felts Field (KSFF) | 2SD2 (2SD2) | 2026-04-02 13:40 UTC | 2026-04-02 17:00 UTC | 3h 19m |
| TG62 |  | Pueblo Memorial Airport (KPUB) | Lone Tree Ranch Airport (35CO) | 2026-04-02 16:19 UTC | 2026-04-02 16:53 UTC | 33m |
| N714NA |  | Porto Sao Sebastiao Airport (SWPS) | Porto Sao Sebastiao Airport (SWPS) | 2026-04-02 14:44 UTC | 2026-04-02 16:52 UTC | 2h 8m |
| N578CF |  | SD41 (SD41) | Laramie Regional Airport (KLAR) | 2026-04-02 15:59 UTC | 2026-04-02 16:51 UTC | 51m |
| TEAL43 | TEA | Trent Lott International Airport (KPQL) | Magee Municipal Airport (K17M) | 2026-04-02 16:19 UTC | 2026-04-02 16:45 UTC | 25m |
| STMPD19 | STM | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-02 16:12 UTC | 2026-04-02 16:44 UTC | 32m |
| EB707 |  | Whiting Field Nas South Airport (KNDZ) | Spencer Nolf Airport (KNRQ) | 2026-04-02 16:13 UTC | 2026-04-02 16:43 UTC | 30m |
| N733FF |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-04-02 16:15 UTC | 2026-04-02 16:41 UTC | 26m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-02 15:17 UTC | 2026-04-02 16:39 UTC | 1h 22m |
| EB714 |  | Whiting Field Nas South Airport (KNDZ) | FD82 (FD82) | 2026-04-02 16:23 UTC | 2026-04-02 16:39 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
