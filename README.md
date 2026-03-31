# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_22:49:32_UTC-green)

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

**Latest saved flight:** 2026-03-31 22:49:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 22:49:32 UTC

- **7,750** saved flights
- **4,941** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,750** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **95,556.8 tonnes** estimated CO2 emissions
- **5,539,524 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 378 |
| 2 | Ryanair | 293 |
| 3 | IndiGo | 200 |
| 4 | EJA | 164 |
| 5 | American Airlines | 151 |
| 6 | Southwest Airlines | 128 |
| 7 | Lufthansa | 115 |
| 8 | ENY | 111 |
| 9 | Vueling | 82 |
| 10 | AXM | 78 |
| 11 | LATAM Airlines | 78 |
| 12 | LXJ | 72 |
| 13 | Delta Air Lines | 69 |
| 14 | WIF | 59 |
| 15 | QLK | 58 |
| 16 | All Nippon Airways | 57 |
| 17 | Swiss International | 55 |
| 18 | VIV | 55 |
| 19 | AZU | 54 |
| 20 | United Airlines | 53 |
| 21 | Alaska Airlines | 52 |
| 22 | AXB | 52 |
| 23 | EDV | 52 |
| 24 | Cathay Pacific | 47 |
| 25 | Japan Airlines | 47 |
| 26 | BRC | 45 |
| 27 | Avianca | 43 |
| 28 | easyJet | 43 |
| 29 | EJU | 42 |
| 30 | MXY | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6734 |
| 2 | 🇮🇳 IN | 608 |
| 3 | 🇪🇸 ES | 586 |
| 4 | 🇦🇺 AU | 532 |
| 5 | 🇧🇷 BR | 384 |
| 6 | 🇩🇪 DE | 381 |
| 7 | 🇨🇦 CA | 369 |
| 8 | 🇨🇴 CO | 366 |
| 9 | 🇮🇹 IT | 346 |
| 10 | 🇯🇵 JP | 342 |
| 11 | 🇲🇽 MX | 275 |
| 12 | 🇬🇧 GB | 265 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 198 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 175 |
| 17 | 🇨🇭 CH | 168 |
| 18 | 🇬🇹 GT | 167 |
| 19 | 🇿🇦 ZA | 161 |
| 20 | 🇳🇿 NZ | 152 |
| 21 | 🇹🇷 TR | 137 |
| 22 | 🇵🇭 PH | 136 |
| 23 | 🇹🇭 TH | 95 |
| 24 | 🇲🇦 MA | 94 |
| 25 | 🇵🇱 PL | 94 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇲🇴 MO | 82 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 74 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 194 |
| 2 | Denver International Airport |  | US | 151 |
| 3 | Indira Gandhi International Airport |  | IN | 138 |
| 4 | El Dorado International Airport |  | CO | 125 |
| 5 | Tokyo International Airport |  | JP | 122 |
| 6 | La Aurora Airport |  | GT | 118 |
| 7 | Frankfurt am Main International Airport |  | DE | 115 |
| 8 | Harry Reid International Airport |  | US | 111 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 103 |
| 10 | Guaymaral Airport |  | CO | 90 |
| 11 | Zurich Airport |  | CH | 88 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 85 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 14 | Macau International Airport |  | MO | 82 |
| 15 | Chicago O'Hare International Airport |  | US | 80 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 76 |
| 17 | Tenerife Norte Airport |  | ES | 75 |
| 18 | Reno/Tahoe International Airport |  | US | 73 |
| 19 | Madrid Barajas International Airport |  | ES | 70 |
| 20 | Bengaluru International Airport |  | IN | 68 |
| 21 | Charlotte/Douglas International Airport |  | US | 67 |
| 22 | Kuala Lumpur International Airport |  | MY | 65 |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 63 |
| 25 | Daniel K Inouye International Airport |  | US | 62 |
| 26 | Salt Lake City International Airport |  | US | 62 |
| 27 | Ninoy Aquino International Airport |  | PH | 61 |
| 28 | Malpensa International Airport |  | IT | 59 |
| 29 | Vitoria/Foronda Airport |  | ES | 59 |
| 30 | Miami International Airport |  | US | 57 |
| 31 | Seattle-Tacoma International Airport |  | US | 57 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 56 |
| 33 | Congonhas Airport |  | BR | 56 |
| 34 | Pune Airport |  | IN | 54 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 36 | Charles de Gaulle International Airport |  | FR | 52 |
| 37 | Barcelona International Airport |  | ES | 51 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 50 |
| 39 | Centennial Airport |  | US | 50 |
| 40 | Austin-Bergstrom International Airport |  | US | 47 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 29 | 1h 6m | 706 km | 353.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 23 | 1h 46m | 1,156 km | 458.8 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 22 | 24m | 99 km | 37.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 21 | 15m | 206 km | 74.7 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 18 | 52m | 556 km | 172.5 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 17 | 30m | 369 km | 108.2 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 20 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 21 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 23 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 24 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 26 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 13 | 1h 55m | 1,304 km | 292.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-03-31 20:01 UTC | 2026-03-31 22:49 UTC | 2h 47m |
| N65045 |  | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-03-31 22:08 UTC | 2026-03-31 22:48 UTC | 39m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-03-31 22:02 UTC | 2026-03-31 22:32 UTC | 30m |
| JST433 | JST | Gold Coast Airport (YBCG) | Melbourne International Airport (YMML) | 2026-03-31 20:34 UTC | 2026-03-31 22:31 UTC | 1h 57m |
| LXJ268 | LXJ | Harry Reid International Airport (KLAS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-03-31 21:30 UTC | 2026-03-31 22:27 UTC | 56m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-03-31 22:08 UTC | 2026-03-31 22:19 UTC | 11m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-31 21:55 UTC | 2026-03-31 22:16 UTC | 21m |
| N2699L |  | Caddo Mills Municipal Airport (K7F3) | Commerce Municipal Airport (K2F7) | 2026-03-31 21:29 UTC | 2026-03-31 22:15 UTC | 45m |
| N511PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-03-31 21:38 UTC | 2026-03-31 22:13 UTC | 35m |
| ZJA | ZJA | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-03-31 21:46 UTC | 2026-03-31 22:09 UTC | 23m |
| DIV | DIV | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-03-31 21:07 UTC | 2026-03-31 22:05 UTC | 57m |
| RN119 |  | Five Oaks Estate Airport (FD03) | Five Oaks Estate Airport (FD03) | 2026-03-31 22:03 UTC | 2026-03-31 22:04 UTC | 1m |
| N5277F |  | William P Hobby Airport (KHOU) | West Houston Airport (KIWS) | 2026-03-31 21:35 UTC | 2026-03-31 22:03 UTC | 27m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-31 21:50 UTC | 2026-03-31 22:02 UTC | 12m |
| STT5064 | STT | Daniel K Inouye International Airport (PHNL) | Bradshaw Army Airfield (PHSF) | 2026-03-31 21:41 UTC | 2026-03-31 22:00 UTC | 19m |
| BOMR745 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-03-31 21:19 UTC | 2026-03-31 21:58 UTC | 38m |
| N641AT |  | Merrill Field (PAMR) | PAFW (PAFW) | 2026-03-31 21:10 UTC | 2026-03-31 21:52 UTC | 42m |
| N2662Z |  | Johnsen Airport (4CA7) | Pope Valley Airport (05CL) | 2026-03-31 21:12 UTC | 2026-03-31 21:49 UTC | 36m |
| RN181 |  | Whiting Field Nas North Airport (KNSE) | 55FD (55FD) | 2026-03-31 21:39 UTC | 2026-03-31 21:48 UTC | 8m |
| XSR817 | XSR | William P Hobby Airport (KHOU) | Austin-Bergstrom International Airport (KAUS) | 2026-03-31 21:19 UTC | 2026-03-31 21:48 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
