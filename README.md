# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_21:39:17_UTC-green)

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

**Latest saved flight:** 2026-03-31 21:39:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 21:39:17 UTC

- **7,624** saved flights
- **4,884** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,624** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **94,557.5 tonnes** estimated CO2 emissions
- **5,481,596 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 367 |
| 2 | Ryanair | 293 |
| 3 | IndiGo | 199 |
| 4 | EJA | 162 |
| 5 | American Airlines | 149 |
| 6 | Southwest Airlines | 124 |
| 7 | Lufthansa | 115 |
| 8 | ENY | 109 |
| 9 | Vueling | 82 |
| 10 | AXM | 78 |
| 11 | LATAM Airlines | 77 |
| 12 | LXJ | 69 |
| 13 | Delta Air Lines | 66 |
| 14 | WIF | 59 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 52 |
| 19 | AZU | 52 |
| 20 | United Airlines | 52 |
| 21 | VIV | 51 |
| 22 | Alaska Airlines | 50 |
| 23 | EDV | 48 |
| 24 | Cathay Pacific | 47 |
| 25 | Japan Airlines | 47 |
| 26 | Avianca | 43 |
| 27 | easyJet | 43 |
| 28 | BRC | 42 |
| 29 | EJU | 42 |
| 30 | MXY | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6586 |
| 2 | 🇮🇳 IN | 606 |
| 3 | 🇪🇸 ES | 586 |
| 4 | 🇦🇺 AU | 512 |
| 5 | 🇩🇪 DE | 381 |
| 6 | 🇧🇷 BR | 378 |
| 7 | 🇨🇦 CA | 357 |
| 8 | 🇨🇴 CO | 356 |
| 9 | 🇮🇹 IT | 345 |
| 10 | 🇯🇵 JP | 338 |
| 11 | 🇬🇧 GB | 264 |
| 12 | 🇲🇽 MX | 263 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 198 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 175 |
| 17 | 🇨🇭 CH | 168 |
| 18 | 🇬🇹 GT | 165 |
| 19 | 🇿🇦 ZA | 161 |
| 20 | 🇳🇿 NZ | 142 |
| 21 | 🇹🇷 TR | 137 |
| 22 | 🇵🇭 PH | 132 |
| 23 | 🇹🇭 TH | 95 |
| 24 | 🇲🇦 MA | 94 |
| 25 | 🇵🇱 PL | 94 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇲🇴 MO | 82 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 73 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 188 |
| 2 | Denver International Airport |  | US | 145 |
| 3 | Indira Gandhi International Airport |  | IN | 137 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 120 |
| 6 | La Aurora Airport |  | GT | 117 |
| 7 | Frankfurt am Main International Airport |  | DE | 115 |
| 8 | Harry Reid International Airport |  | US | 107 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 99 |
| 10 | Guaymaral Airport |  | CO | 90 |
| 11 | Zurich Airport |  | CH | 88 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 82 |
| 14 | Macau International Airport |  | MO | 82 |
| 15 | Chicago O'Hare International Airport |  | US | 80 |
| 16 | Tenerife Norte Airport |  | ES | 75 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 18 | Reno/Tahoe International Airport |  | US | 71 |
| 19 | Madrid Barajas International Airport |  | ES | 70 |
| 20 | Bengaluru International Airport |  | IN | 68 |
| 21 | Charlotte/Douglas International Airport |  | US | 65 |
| 22 | Kuala Lumpur International Airport |  | MY | 65 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 63 |
| 24 | Salt Lake City International Airport |  | US | 61 |
| 25 | Daniel K Inouye International Airport |  | US | 60 |
| 26 | Ninoy Aquino International Airport |  | PH | 59 |
| 27 | Vitoria/Foronda Airport |  | ES | 59 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 59 |
| 29 | Malpensa International Airport |  | IT | 58 |
| 30 | Miami International Airport |  | US | 57 |
| 31 | Congonhas Airport |  | BR | 56 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 55 |
| 33 | Seattle-Tacoma International Airport |  | US | 55 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 35 | Pune Airport |  | IN | 53 |
| 36 | Charles de Gaulle International Airport |  | FR | 52 |
| 37 | Barcelona International Airport |  | ES | 51 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 49 |
| 39 | Centennial Airport |  | US | 49 |
| 40 | O. R. Tambo International Airport |  | ZA | 47 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 22 | 1h 46m | 1,156 km | 438.9 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 21 | 24m | 99 km | 36.0 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 20 | 15m | 206 km | 71.1 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 15 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 17 | 51m | 556 km | 163.0 t |
| 17 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 23 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 25 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 26 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 13 | 1h 55m | 1,304 km | 292.5 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG2650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-03-31 21:12 UTC | 2026-03-31 21:39 UTC | 26m |
| HAWK763 | HAW | Jiles Field (9NC4) | Nc61 Airport (NC61) | 2026-03-31 21:21 UTC | 2026-03-31 21:34 UTC | 13m |
| SCU48 | SCU | Neversweat Airport (1OK0) | Jones Memorial Airport (K3F7) | 2026-03-31 21:17 UTC | 2026-03-31 21:32 UTC | 15m |
| N51794 |  | 19OK (19OK) | Double W Airport (3OK7) | 2026-03-31 21:03 UTC | 2026-03-31 21:31 UTC | 28m |
| N121PC |  | Mckinney Ntl Airport (KTKI) | 0TX8 (0TX8) | 2026-03-31 21:04 UTC | 2026-03-31 21:30 UTC | 25m |
| AOJ69Y | AOJ | Budapest Ferenc Liszt International Airport (LHBP) | Graz Airport (LOWG) | 2026-03-31 20:59 UTC | 2026-03-31 21:28 UTC | 28m |
| N855P |  | Llano Municipal Airport (KAQO) | Commerce Municipal Airport (K2F7) | 2026-03-31 20:14 UTC | 2026-03-31 21:22 UTC | 1h 7m |
|  |  | Deep Forest Airport (FD48) | Deep Forest Airport (FD48) | 2026-03-31 21:12 UTC | 2026-03-31 21:19 UTC | 6m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-03-31 21:07 UTC | 2026-03-31 21:18 UTC | 11m |
| N273TM |  | Des Moines International Airport (KDSM) | Joe Foss Field (KFSD) | 2026-03-31 20:36 UTC | 2026-03-31 21:10 UTC | 34m |
| N306PP |  | Auburn Municipal Airport (KS50) | Heineck Farm Airport (76WA) | 2026-03-31 20:37 UTC | 2026-03-31 21:03 UTC | 26m |
| LXJ356 | LXJ | Columbus Airport (KCSG) | Lakefront Airport (KNEW) | 2026-03-31 20:05 UTC | 2026-03-31 21:00 UTC | 55m |
| 72068 |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Grant County Airport (KSVC) | 2026-03-31 19:38 UTC | 2026-03-31 20:59 UTC | 1h 20m |
| CRN101T | CRN | Kelowna Airport (CYLW) | Penticton Airport (CYYF) | 2026-03-31 20:38 UTC | 2026-03-31 20:56 UTC | 18m |
| N9421F |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-03-31 19:51 UTC | 2026-03-31 20:55 UTC | 1h 4m |
| LVJUM | LVJ | Jorge Newbery Airpark (SABE) | Carrasco International /General C L Berisso Airport (SUMU) | 2026-03-31 20:28 UTC | 2026-03-31 20:54 UTC | 26m |
| RIBEY32 | RIB | Four Square Ranch Airport (3TA0) | Four Square Ranch Airport (3TA0) | 2026-03-31 20:38 UTC | 2026-03-31 20:53 UTC | 15m |
| VTE3694 | VTE | Dallas-Fort Worth International Airport (KDFW) | Ralph C Weiser Field (KAGO) | 2026-03-31 20:19 UTC | 2026-03-31 20:50 UTC | 31m |
| N812BP |  | Creasy Airport (5TA5) | Menard Airport (XA09) | 2026-03-31 20:01 UTC | 2026-03-31 20:49 UTC | 47m |
| ASA819 | Alaska Airlines | Sacramento International Airport (KSMF) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-03-31 15:46 UTC | 2026-03-31 20:48 UTC | 5h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
