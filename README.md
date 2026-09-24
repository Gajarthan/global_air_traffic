# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_01:07:48_UTC-green)

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

**Latest saved flight:** 2026-09-24 01:07:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 01:07:48 UTC

- **267,897** saved flights
- **78,672** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,897** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,248,790.3 tonnes** estimated CO2 emissions
- **188,335,667 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10570 |
| 2 | SkyWest Airlines | 9323 |
| 3 | EJA | 5209 |
| 4 | IndiGo | 4487 |
| 5 | American Airlines | 4171 |
| 6 | Southwest Airlines | 3938 |
| 7 | Delta Air Lines | 3333 |
| 8 | ENY | 3149 |
| 9 | LATAM Airlines | 2582 |
| 10 | AZU | 2511 |
| 11 | Vueling | 2240 |
| 12 | WIF | 2172 |
| 13 | LXJ | 2104 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1798 |
| 16 | Swiss International | 1759 |
| 17 | QLK | 1727 |
| 18 | EJU | 1685 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1642 |
| 21 | Alaska Airlines | 1585 |
| 22 | All Nippon Airways | 1545 |
| 23 | PGT | 1508 |
| 24 | WMT | 1500 |
| 25 | GLO | 1494 |
| 26 | Air France | 1470 |
| 27 | VIV | 1463 |
| 28 | Wizz Air | 1454 |
| 29 | CXK | 1309 |
| 30 | AEE | 1287 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222861 |
| 2 | 🇪🇸 ES | 16806 |
| 3 | 🇧🇷 BR | 15661 |
| 4 | 🇦🇺 AU | 15402 |
| 5 | 🇨🇦 CA | 14949 |
| 6 | 🇮🇹 IT | 14527 |
| 7 | 🇮🇳 IN | 14193 |
| 8 | 🇩🇪 DE | 12880 |
| 9 | 🇬🇧 GB | 12417 |
| 10 | 🇨🇴 CO | 12257 |
| 11 | 🇫🇷 FR | 10663 |
| 12 | 🇯🇵 JP | 10315 |
| 13 | 🇹🇷 TR | 8116 |
| 14 | 🇬🇷 GR | 7741 |
| 15 | 🇲🇽 MX | 7387 |
| 16 | 🇨🇭 CH | 7134 |
| 17 | 🇳🇴 NO | 6625 |
| 18 | 🇹🇭 TH | 4795 |
| 19 | 🇲🇾 MY | 4511 |
| 20 | 🇿🇦 ZA | 4482 |
| 21 | 🇵🇱 PL | 4393 |
| 22 | 🇳🇿 NZ | 3744 |
| 23 | 🇵🇭 PH | 3550 |
| 24 | 🇬🇹 GT | 3392 |
| 25 | 🇭🇷 HR | 3054 |
| 26 | 🇰🇷 KR | 3035 |
| 27 | 🇲🇦 MA | 2672 |
| 28 | 🇲🇪 ME | 2510 |
| 29 | 🇳🇱 NL | 2399 |
| 30 | 🇮🇩 ID | 2232 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5459 |
| 2 | Denver International Airport |  | US | 4350 |
| 3 | Indira Gandhi International Airport |  | IN | 3212 |
| 4 | Tokyo International Airport |  | JP | 3087 |
| 5 | El Dorado International Airport |  | CO | 2894 |
| 6 | Harry Reid International Airport |  | US | 2865 |
| 7 | Guaymaral Airport |  | CO | 2805 |
| 8 | Zurich Airport |  | CH | 2780 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2690 |
| 10 | La Aurora Airport |  | GT | 2578 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2577 |
| 12 | Salt Lake City International Airport |  | US | 2361 |
| 13 | Chicago O'Hare International Airport |  | US | 2296 |
| 14 | Congonhas Airport |  | BR | 2282 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2193 |
| 16 | Capua Airport |  | IT | 2086 |
| 17 | Madrid Barajas International Airport |  | ES | 2061 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2027 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1913 |
| 22 | Charles de Gaulle International Airport |  | FR | 1898 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1882 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1876 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1782 |
| 27 | Ninoy Aquino International Airport |  | PH | 1742 |
| 28 | Charlotte/Douglas International Airport |  | US | 1672 |
| 29 | Barcelona International Airport |  | ES | 1665 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1656 |
| 31 | Viracopos International Airport |  | BR | 1620 |
| 32 | Kuala Lumpur International Airport |  | MY | 1615 |
| 33 | Seattle-Tacoma International Airport |  | US | 1571 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1565 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1518 |
| 37 | Bengaluru International Airport |  | IN | 1511 |
| 38 | Oslo Gardermoen Airport |  | NO | 1506 |
| 39 | Vancouver International Airport |  | CA | 1502 |
| 40 | Antalya International Airport |  | TR | 1430 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1005 | 21m | 244 km | 4,231.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 675 | 1h 6m | 770 km | 8,966.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 596 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 428 | 27m | 275 km | 2,028.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 409 | 44m | 241 km | 1,698.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 363 | 21m | 250 km | 1,567.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 358 | 23m | 55 km | 340.3 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 339 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 285 | 18m | 14 km | 71.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSZ888 | CSZ | London Heathrow Airport (EGLL) | Savvatiya Air Base (ULKS) | 2026-09-23 21:29 UTC | 2026-09-24 01:07 UTC | 3h 38m |
| N8075R |  | Hanford Municipal Airport (KHJO) | Meadows Field (KBFL) | 2026-09-24 00:41 UTC | 2026-09-24 01:06 UTC | 24m |
| FFT3382 | FFT | San Francisco International Airport (KSFO) | San Diego International Airport (KSAN) | 2026-09-23 23:53 UTC | 2026-09-24 01:05 UTC | 1h 11m |
| ARROW32 | ARR | Buckley Space Force Base Airport (KBKF) | Perry Park Airport (CO93) | 2026-09-24 00:19 UTC | 2026-09-24 01:04 UTC | 45m |
| N90MF |  | NX01 (NX01) | Booneville Municipal Airport (K4M2) | 2026-09-24 00:24 UTC | 2026-09-24 01:01 UTC | 37m |
| N710KK |  | Sacramento Mather Airport (KMHR) | San Carlos Airport (KSQL) | 2026-09-24 00:23 UTC | 2026-09-24 00:55 UTC | 32m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-24 00:37 UTC | 2026-09-24 00:54 UTC | 16m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-09-23 18:00 UTC | 2026-09-24 00:52 UTC | 6h 52m |
| N217AX |  | Twentynine Palms Self Airport (KNXP) | Twentynine Palms Self Airport (KNXP) | 2026-09-23 23:22 UTC | 2026-09-24 00:52 UTC | 1h 30m |
| IGO1058 | IndiGo | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-23 22:42 UTC | 2026-09-24 00:52 UTC | 2h 10m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-09-23 20:21 UTC | 2026-09-24 00:49 UTC | 4h 28m |
| KANTO81 | KAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-09-24 00:12 UTC | 2026-09-24 00:48 UTC | 35m |
| N312SJ |  | Gary/Chicago International Airport (KGYY) | Miami Executive Airport (KTMB) | 2026-09-23 22:14 UTC | 2026-09-24 00:46 UTC | 2h 32m |
| CGAQX | CGA | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-09-24 00:24 UTC | 2026-09-24 00:46 UTC | 21m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-24 00:30 UTC | 2026-09-24 00:45 UTC | 14m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-24 00:22 UTC | 2026-09-24 00:42 UTC | 20m |
| N1MM |  | Southwest Oregon Regional Airport (KOTH) | Sierraville Dearwater Airport (KO79) | 2026-09-23 23:54 UTC | 2026-09-24 00:41 UTC | 46m |
| N737HJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-09-24 00:01 UTC | 2026-09-24 00:38 UTC | 37m |
| AAL2986 | American Airlines | Portland International Airport (KPDX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-09-23 22:15 UTC | 2026-09-24 00:38 UTC | 2h 23m |
| N44NS |  | 19OK (19OK) | 19OK (19OK) | 2026-09-24 00:28 UTC | 2026-09-24 00:28 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
