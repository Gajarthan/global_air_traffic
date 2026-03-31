# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_20:48:55_UTC-green)

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

**Latest saved flight:** 2026-03-31 20:48:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 20:48:55 UTC

- **7,522** saved flights
- **4,831** unique routes
- **106** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,522** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **93,649.3 tonnes** estimated CO2 emissions
- **5,428,946 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 361 |
| 2 | Ryanair | 287 |
| 3 | IndiGo | 198 |
| 4 | EJA | 159 |
| 5 | American Airlines | 146 |
| 6 | Southwest Airlines | 119 |
| 7 | Lufthansa | 115 |
| 8 | ENY | 108 |
| 9 | Vueling | 82 |
| 10 | AXM | 78 |
| 11 | LATAM Airlines | 76 |
| 12 | LXJ | 68 |
| 13 | Delta Air Lines | 65 |
| 14 | WIF | 58 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 52 |
| 19 | AZU | 52 |
| 20 | VIV | 51 |
| 21 | Alaska Airlines | 50 |
| 22 | United Airlines | 50 |
| 23 | EDV | 48 |
| 24 | Cathay Pacific | 47 |
| 25 | Japan Airlines | 47 |
| 26 | Avianca | 43 |
| 27 | easyJet | 43 |
| 28 | EJU | 42 |
| 29 | BRC | 41 |
| 30 | MXY | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6477 |
| 2 | 🇮🇳 IN | 604 |
| 3 | 🇪🇸 ES | 583 |
| 4 | 🇦🇺 AU | 510 |
| 5 | 🇩🇪 DE | 381 |
| 6 | 🇧🇷 BR | 374 |
| 7 | 🇨🇴 CO | 350 |
| 8 | 🇨🇦 CA | 343 |
| 9 | 🇮🇹 IT | 342 |
| 10 | 🇯🇵 JP | 338 |
| 11 | 🇬🇧 GB | 262 |
| 12 | 🇲🇽 MX | 259 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 194 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 175 |
| 17 | 🇨🇭 CH | 167 |
| 18 | 🇬🇹 GT | 165 |
| 19 | 🇿🇦 ZA | 161 |
| 20 | 🇹🇷 TR | 134 |
| 21 | 🇵🇭 PH | 132 |
| 22 | 🇳🇿 NZ | 126 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇵🇱 PL | 94 |
| 25 | 🇲🇦 MA | 91 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇲🇴 MO | 82 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 72 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 185 |
| 2 | Denver International Airport |  | US | 140 |
| 3 | Indira Gandhi International Airport |  | IN | 137 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 118 |
| 6 | La Aurora Airport |  | GT | 117 |
| 7 | Frankfurt am Main International Airport |  | DE | 115 |
| 8 | Harry Reid International Airport |  | US | 105 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 95 |
| 10 | Guaymaral Airport |  | CO | 89 |
| 11 | Zurich Airport |  | CH | 87 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 82 |
| 14 | Macau International Airport |  | MO | 82 |
| 15 | Chicago O'Hare International Airport |  | US | 80 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 17 | Tenerife Norte Airport |  | ES | 73 |
| 18 | Madrid Barajas International Airport |  | ES | 70 |
| 19 | Reno/Tahoe International Airport |  | US | 69 |
| 20 | Bengaluru International Airport |  | IN | 67 |
| 21 | Kuala Lumpur International Airport |  | MY | 65 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 63 |
| 23 | Charlotte/Douglas International Airport |  | US | 61 |
| 24 | Salt Lake City International Airport |  | US | 61 |
| 25 | Daniel K Inouye International Airport |  | US | 59 |
| 26 | Ninoy Aquino International Airport |  | PH | 59 |
| 27 | Vitoria/Foronda Airport |  | ES | 59 |
| 28 | Malpensa International Airport |  | IT | 57 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 57 |
| 30 | Miami International Airport |  | US | 56 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 55 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 33 | Seattle-Tacoma International Airport |  | US | 54 |
| 34 | Congonhas Airport |  | BR | 54 |
| 35 | Charles de Gaulle International Airport |  | FR | 52 |
| 36 | Pune Airport |  | IN | 52 |
| 37 | Barcelona International Airport |  | ES | 50 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 49 |
| 39 | Centennial Airport |  | US | 48 |
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
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 16 | 51m | 556 km | 153.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 14 | 1h 0m | 723 km | 174.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 23 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 25 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 13 | 22m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 13 | 1h 55m | 1,304 km | 292.5 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASA819 | Alaska Airlines | Sacramento International Airport (KSMF) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-03-31 15:46 UTC | 2026-03-31 20:48 UTC | 5h 2m |
| N543TC |  | Paso Robles Municipal Airport (KPRB) | Gnoss Field (KDVO) | 2026-03-31 19:29 UTC | 2026-03-31 20:42 UTC | 1h 13m |
| N1374U |  | Chesapeake Regional Airport (KCPK) | Hampton Roads Executive Airport (KPVG) | 2026-03-31 20:07 UTC | 2026-03-31 20:40 UTC | 33m |
| N1925 |  | Fort Smith Regional Airport (KFSM) | Washington Dulles International Airport (KIAD) | 2026-03-31 18:42 UTC | 2026-03-31 20:39 UTC | 1h 56m |
| N5283K |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-03-31 19:38 UTC | 2026-03-31 20:38 UTC | 1h 0m |
| LATTE92 | LAT | Lanai Airport (PHNY) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-03-31 20:20 UTC | 2026-03-31 20:34 UTC | 13m |
| SWA3077 | Southwest Airlines | Daniel K Inouye International Airport (PHNL) | Kaluakoi Airport (HI49) | 2026-03-31 20:17 UTC | 2026-03-31 20:34 UTC | 16m |
| N782MM |  | Austin-Bergstrom International Airport (KAUS) | Harry Reid International Airport (KLAS) | 2026-03-31 17:52 UTC | 2026-03-31 20:32 UTC | 2h 39m |
| N366AH |  | Concord-Padgett Regional Airport (KJQF) | Charlotte/Douglas International Airport (KCLT) | 2026-03-31 20:25 UTC | 2026-03-31 20:32 UTC | 6m |
| UAE9792 | Emirates | Fujairah International Airport (OMFJ) | Macau International Airport (VMMC) | 2026-03-31 14:41 UTC | 2026-03-31 20:31 UTC | 5h 49m |
| LW11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-03-31 19:15 UTC | 2026-03-31 20:31 UTC | 1h 15m |
| N721AZ |  | Fort Worth Meacham International Airport (KFTW) | Henderson Executive Airport (KHND) | 2026-03-31 18:08 UTC | 2026-03-31 20:27 UTC | 2h 19m |
| R21202 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-03-31 19:08 UTC | 2026-03-31 20:27 UTC | 1h 18m |
| N10F |  | Sulphur Springs Municipal Airport (KSLR) | Majors Airport (KGVT) | 2026-03-31 19:44 UTC | 2026-03-31 20:26 UTC | 41m |
| N43TP |  | Del Norte International Airport (MMAN) | Rio Grande City Municipal Airport (K67R) | 2026-03-31 20:01 UTC | 2026-03-31 20:25 UTC | 23m |
| N2459A |  | Last Chance Ranch Airport (3FD0) | Orlando Executive Airport (KORL) | 2026-03-31 17:13 UTC | 2026-03-31 20:21 UTC | 3h 7m |
| CARGO38 | CAR | Hidden Springs Airpark (36AL) | Hidden Springs Airpark (36AL) | 2026-03-31 20:07 UTC | 2026-03-31 20:14 UTC | 7m |
| SKW5854 | SkyWest Airlines | San Francisco International Airport (KSFO) | Lee Vining Airport (KO24) | 2026-03-31 19:42 UTC | 2026-03-31 20:13 UTC | 30m |
| ARCAS13 | ARC | 29TA (29TA) | TX20 (TX20) | 2026-03-31 19:57 UTC | 2026-03-31 20:11 UTC | 14m |
| BRCAT06 | BRC | Epic Paramotor Airport (NM20) | Grant Besley Airport (NM03) | 2026-03-31 19:42 UTC | 2026-03-31 20:10 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
