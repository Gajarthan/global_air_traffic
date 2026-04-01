# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_22:38:44_UTC-green)

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

**Latest saved flight:** 2026-04-01 22:38:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 22:38:44 UTC

- **9,928** saved flights
- **5,935** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,928** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **120,477.2 tonnes** estimated CO2 emissions
- **6,984,185 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 459 |
| 2 | Ryanair | 382 |
| 3 | IndiGo | 263 |
| 4 | EJA | 210 |
| 5 | American Airlines | 183 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 155 |
| 8 | ENY | 136 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 102 |
| 12 | LXJ | 97 |
| 13 | Delta Air Lines | 81 |
| 14 | All Nippon Airways | 80 |
| 15 | WIF | 80 |
| 16 | QLK | 74 |
| 17 | Swiss International | 73 |
| 18 | VIV | 69 |
| 19 | AZU | 68 |
| 20 | United Airlines | 64 |
| 21 | Alaska Airlines | 63 |
| 22 | AXB | 63 |
| 23 | EDV | 62 |
| 24 | Japan Airlines | 60 |
| 25 | BRC | 58 |
| 26 | easyJet | 56 |
| 27 | EJU | 55 |
| 28 | Avianca | 54 |
| 29 | Cathay Pacific | 54 |
| 30 | AEE | 51 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8305 |
| 2 | 🇮🇳 IN | 808 |
| 3 | 🇪🇸 ES | 765 |
| 4 | 🇦🇺 AU | 724 |
| 5 | 🇩🇪 DE | 527 |
| 6 | 🇧🇷 BR | 513 |
| 7 | 🇨🇴 CO | 496 |
| 8 | 🇨🇦 CA | 479 |
| 9 | 🇯🇵 JP | 465 |
| 10 | 🇮🇹 IT | 437 |
| 11 | 🇲🇽 MX | 359 |
| 12 | 🇬🇧 GB | 350 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 227 |
| 17 | 🇨🇭 CH | 225 |
| 18 | 🇳🇿 NZ | 219 |
| 19 | 🇬🇹 GT | 206 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 176 |
| 22 | 🇹🇷 TR | 161 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 117 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇴 MO | 98 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 245 |
| 2 | Denver International Airport |  | US | 182 |
| 3 | Indira Gandhi International Airport |  | IN | 178 |
| 4 | Tokyo International Airport |  | JP | 166 |
| 5 | Frankfurt am Main International Airport |  | DE | 166 |
| 6 | El Dorado International Airport |  | CO | 158 |
| 7 | Guaymaral Airport |  | CO | 147 |
| 8 | La Aurora Airport |  | GT | 144 |
| 9 | Harry Reid International Airport |  | US | 137 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 120 |
| 11 | Zurich Airport |  | CH | 113 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Chicago O'Hare International Airport |  | US | 104 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 102 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 102 |
| 16 | Macau International Airport |  | MO | 98 |
| 17 | Tenerife Norte Airport |  | ES | 92 |
| 18 | Charlotte/Douglas International Airport |  | US | 91 |
| 19 | Reno/Tahoe International Airport |  | US | 90 |
| 20 | Madrid Barajas International Airport |  | ES | 90 |
| 21 | Bengaluru International Airport |  | IN | 87 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 85 |
| 23 | Kuala Lumpur International Airport |  | MY | 85 |
| 24 | Ninoy Aquino International Airport |  | PH | 80 |
| 25 | Congonhas Airport |  | BR | 77 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 74 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 74 |
| 29 | Malpensa International Airport |  | IT | 73 |
| 30 | Daniel K Inouye International Airport |  | US | 71 |
| 31 | Vitoria/Foronda Airport |  | ES | 71 |
| 32 | Salt Lake City International Airport |  | US | 71 |
| 33 | Pune Airport |  | IN | 70 |
| 34 | Seattle-Tacoma International Airport |  | US | 70 |
| 35 | Charles de Gaulle International Airport |  | FR | 69 |
| 36 | Barcelona International Airport |  | ES | 69 |
| 37 | Austin-Bergstrom International Airport |  | US | 66 |
| 38 | Miami International Airport |  | US | 65 |
| 39 | Bodø Airport |  | NO | 65 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 64 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 45 | 14m | 114 km | 88.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 29 | 23m | 99 km | 49.7 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
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
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 18 | 1h 56m | 1,304 km | 405.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 29 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 15 | 18m | 26 km | 6.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 14 | 13m | 99 km | 24.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRA16U | TRA | Alicante International Airport (LEAL) | Amsterdam Airport Schiphol (EHAM) | 2026-04-01 20:13 UTC | 2026-04-01 22:38 UTC | 2h 25m |
| N68329 |  | Lehigh Valley International Airport (KABE) | Sency Airport (55PA) | 2026-04-01 22:14 UTC | 2026-04-01 22:34 UTC | 20m |
| TRA74H | TRA | Tenerife Norte Airport (GCXO) | Amsterdam Airport Schiphol (EHAM) | 2026-04-01 18:20 UTC | 2026-04-01 22:34 UTC | 4h 14m |
| 8WK |  | Melbourne Essendon Airport (YMEN) | Tamworth Airport (YSTW) | 2026-04-01 21:08 UTC | 2026-04-01 22:29 UTC | 1h 21m |
| N43TP |  | Del Norte International Airport (MMAN) | Agualeguas Old Airport (MM44) | 2026-04-01 21:52 UTC | 2026-04-01 22:16 UTC | 23m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-01 21:43 UTC | 2026-04-01 22:14 UTC | 31m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-04-01 11:56 UTC | 2026-04-01 22:12 UTC | 10h 16m |
| N661SA |  | Hammond Northshore Regional Airport (KHDC) | Lawson Field (99LA) | 2026-04-01 21:45 UTC | 2026-04-01 22:12 UTC | 26m |
| BCS5GU | BCS | Amsterdam Airport Schiphol (EHAM) | Leipzig Halle Airport (EDDP) | 2026-04-01 21:15 UTC | 2026-04-01 22:09 UTC | 53m |
| N125TN |  | Tyler Pounds Regional Airport (KTYR) | Austin-Bergstrom International Airport (KAUS) | 2026-04-01 21:32 UTC | 2026-04-01 22:08 UTC | 35m |
| NLQ | NLQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-01 21:51 UTC | 2026-04-01 22:08 UTC | 16m |
| N173TX |  | Torres Airport (MT18) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-04-01 20:01 UTC | 2026-04-01 22:07 UTC | 2h 6m |
| THY4HC | Turkish Airlines | Kutahya Airport (LTBN) | Nairobi Wilson Airport (HKNW) | 2026-04-01 16:34 UTC | 2026-04-01 22:06 UTC | 5h 31m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-01 21:48 UTC | 2026-04-01 22:04 UTC | 15m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-01 10:52 UTC | 2026-04-01 22:01 UTC | 11h 8m |
| N37NA |  | Monterey Bay Academy Airport (CA66) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-01 21:38 UTC | 2026-04-01 22:00 UTC | 21m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-01 17:50 UTC | 2026-04-01 21:54 UTC | 4h 4m |
| CXK184 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-04-01 20:34 UTC | 2026-04-01 21:53 UTC | 1h 19m |
| N20997 |  | Brown Field (46NC) | Edwards Airport (9NC3) | 2026-04-01 21:36 UTC | 2026-04-01 21:52 UTC | 16m |
| KXL | KXL | Sydney Bankstown Airport (YSBK) | Walcha Airport (YWCH) | 2026-04-01 21:09 UTC | 2026-04-01 21:52 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
