# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_16:26:15_UTC-green)

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

**Latest saved flight:** 2026-04-01 16:26:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 16:26:15 UTC

- **9,039** saved flights
- **5,490** unique routes
- **108** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,039** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **109,410.7 tonnes** estimated CO2 emissions
- **6,342,650 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 399 |
| 2 | Ryanair | 348 |
| 3 | IndiGo | 254 |
| 4 | EJA | 181 |
| 5 | American Airlines | 158 |
| 6 | Lufthansa | 157 |
| 7 | Southwest Airlines | 135 |
| 8 | ENY | 123 |
| 9 | AXM | 102 |
| 10 | Vueling | 98 |
| 11 | LATAM Airlines | 89 |
| 12 | All Nippon Airways | 79 |
| 13 | LXJ | 77 |
| 14 | WIF | 73 |
| 15 | Delta Air Lines | 72 |
| 16 | QLK | 70 |
| 17 | Swiss International | 70 |
| 18 | AXB | 62 |
| 19 | AZU | 60 |
| 20 | Japan Airlines | 60 |
| 21 | VIV | 60 |
| 22 | Alaska Airlines | 56 |
| 23 | EDV | 55 |
| 24 | BRC | 54 |
| 25 | United Airlines | 54 |
| 26 | EJU | 52 |
| 27 | easyJet | 52 |
| 28 | Avianca | 50 |
| 29 | Cathay Pacific | 49 |
| 30 | Air India | 47 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7360 |
| 2 | 🇮🇳 IN | 786 |
| 3 | 🇪🇸 ES | 713 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 503 |
| 6 | 🇯🇵 JP | 461 |
| 7 | 🇧🇷 BR | 447 |
| 8 | 🇨🇦 CA | 431 |
| 9 | 🇨🇴 CO | 428 |
| 10 | 🇮🇹 IT | 409 |
| 11 | 🇬🇧 GB | 326 |
| 12 | 🇲🇽 MX | 310 |
| 13 | 🇫🇷 FR | 285 |
| 14 | 🇳🇴 NO | 241 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇨🇭 CH | 214 |
| 17 | 🇬🇷 GR | 211 |
| 18 | 🇳🇿 NZ | 197 |
| 19 | 🇿🇦 ZA | 197 |
| 20 | 🇬🇹 GT | 185 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇰🇷 KR | 157 |
| 23 | 🇹🇷 TR | 154 |
| 24 | 🇮🇩 ID | 119 |
| 25 | 🇵🇱 PL | 118 |
| 26 | 🇹🇭 TH | 112 |
| 27 | 🇲🇦 MA | 105 |
| 28 | 🇲🇴 MO | 92 |
| 29 | 🇳🇱 NL | 87 |
| 30 | 🇲🇪 ME | 84 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 209 |
| 2 | Indira Gandhi International Airport |  | IN | 172 |
| 3 | Tokyo International Airport |  | JP | 165 |
| 4 | Frankfurt am Main International Airport |  | DE | 160 |
| 5 | Denver International Airport |  | US | 158 |
| 6 | El Dorado International Airport |  | CO | 142 |
| 7 | La Aurora Airport |  | GT | 130 |
| 8 | Harry Reid International Airport |  | US | 124 |
| 9 | Guaymaral Airport |  | CO | 115 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 109 |
| 11 | Zurich Airport |  | CH | 107 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 100 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 14 | Macau International Airport |  | MO | 92 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 91 |
| 16 | Chicago O'Hare International Airport |  | US | 89 |
| 17 | Tenerife Norte Airport |  | ES | 89 |
| 18 | Kuala Lumpur International Airport |  | MY | 85 |
| 19 | Bengaluru International Airport |  | IN | 84 |
| 20 | Madrid Barajas International Airport |  | ES | 81 |
| 21 | Reno/Tahoe International Airport |  | US | 78 |
| 22 | Ninoy Aquino International Airport |  | PH | 78 |
| 23 | Charlotte/Douglas International Airport |  | US | 77 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 72 |
| 25 | Malpensa International Airport |  | IT | 70 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 69 |
| 27 | Daniel K Inouye International Airport |  | US | 67 |
| 28 | Pune Airport |  | IN | 66 |
| 29 | Vitoria/Foronda Airport |  | ES | 65 |
| 30 | Charles de Gaulle International Airport |  | FR | 64 |
| 31 | Barcelona International Airport |  | ES | 64 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 64 |
| 33 | Salt Lake City International Airport |  | US | 64 |
| 34 | Congonhas Airport |  | BR | 64 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 64 |
| 36 | Miami International Airport |  | US | 60 |
| 37 | Gimpo International Airport |  | KR | 60 |
| 38 | Seattle-Tacoma International Airport |  | US | 60 |
| 39 | O. R. Tambo International Airport |  | ZA | 57 |
| 40 | Austin-Bergstrom International Airport |  | US | 56 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 46 | 28m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 40 | 14m | 114 km | 78.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 29 | 1h 45m | 1,156 km | 578.5 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 26 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 26 | 27m | 152 km | 67.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 25 | 23m | 99 km | 42.8 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 21 | 52m | 556 km | 201.3 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 20 | 9m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 20 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 18 | 1h 1m | 723 km | 224.4 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 15 | 1h 46m | 1,290 km | 333.8 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 27 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 14 | 34m | 431 km | 104.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N25JA |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-01 16:04 UTC | 2026-04-01 16:26 UTC | 21m |
| UPS2905 | UPS | Los Angeles International Airport (KLAX) | Dallas-Fort Worth International Airport (KDFW) | 2026-04-01 13:52 UTC | 2026-04-01 16:20 UTC | 2h 27m |
| FHLID | FHL | Ontur Airport (LEOT) | Alhama De Murcia Airport (LELH) | 2026-04-01 16:00 UTC | 2026-04-01 16:16 UTC | 15m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-01 15:41 UTC | 2026-04-01 16:14 UTC | 33m |
| N73113 |  | Corona Municipal Airport (KAJO) | Riverside Airport (KRAL) | 2026-04-01 15:35 UTC | 2026-04-01 16:14 UTC | 38m |
| N111WH |  | Houma-Terrebonne Airport (KHUM) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-01 16:01 UTC | 2026-04-01 16:13 UTC | 11m |
| STAB11 | STA | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-04-01 15:50 UTC | 2026-04-01 16:10 UTC | 20m |
| BR616 |  | Whiting Field Nas South Airport (KNDZ) | Choctaw Nolf Airport (KNFJ) | 2026-04-01 15:32 UTC | 2026-04-01 16:05 UTC | 33m |
| ADLER1 | ADL | Rye Field (MS63) | Rye Field (MS63) | 2026-04-01 15:49 UTC | 2026-04-01 16:04 UTC | 15m |
| QTR8040 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-04-01 09:07 UTC | 2026-04-01 16:03 UTC | 6h 55m |
| CXK1114 | CXK | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-04-01 16:02 UTC | 2026-04-01 16:02 UTC | 0m |
| N6300F |  | Boise Air Trml/Gowen Field (KBOI) | Tracy Ranch Airport (ID88) | 2026-04-01 15:40 UTC | 2026-04-01 15:57 UTC | 16m |
| EZY9 | easyJet | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-04-01 14:58 UTC | 2026-04-01 15:56 UTC | 57m |
| BOX736 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-01 01:58 UTC | 2026-04-01 15:51 UTC | 13h 53m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-01 15:16 UTC | 2026-04-01 15:48 UTC | 31m |
| RYR93BN | Ryanair | Mont Louis La Quillane Airport (LFNQ) | Cork Airport (EICK) | 2026-04-01 13:39 UTC | 2026-04-01 15:48 UTC | 2h 8m |
| EPI230 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-04-01 15:45 UTC | 2026-04-01 15:47 UTC | 1m |
| FHLID | FHL | Ontur Airport (LEOT) | Alhama De Murcia Airport (LELH) | 2026-04-01 15:36 UTC | 2026-04-01 15:47 UTC | 11m |
| N569Q |  | K00V (K00V) | Lone Tree Ranch Airport (35CO) | 2026-04-01 15:32 UTC | 2026-04-01 15:45 UTC | 13m |
| TG64 |  | Pueblo Memorial Airport (KPUB) | City Of Las Animas - Bent County Airport (K7V9) | 2026-04-01 15:11 UTC | 2026-04-01 15:44 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
