# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_23:35:37_UTC-green)

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

**Latest saved flight:** 2026-03-31 23:35:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 23:35:37 UTC

- **7,858** saved flights
- **4,986** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,858** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **96,629.0 tonnes** estimated CO2 emissions
- **5,601,683 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 382 |
| 2 | Ryanair | 293 |
| 3 | IndiGo | 201 |
| 4 | EJA | 167 |
| 5 | American Airlines | 152 |
| 6 | Southwest Airlines | 131 |
| 7 | Lufthansa | 115 |
| 8 | ENY | 115 |
| 9 | Vueling | 82 |
| 10 | LATAM Airlines | 80 |
| 11 | AXM | 78 |
| 12 | LXJ | 72 |
| 13 | Delta Air Lines | 70 |
| 14 | QLK | 61 |
| 15 | WIF | 59 |
| 16 | All Nippon Airways | 57 |
| 17 | AZU | 56 |
| 18 | Swiss International | 55 |
| 19 | VIV | 55 |
| 20 | United Airlines | 54 |
| 21 | Alaska Airlines | 53 |
| 22 | AXB | 52 |
| 23 | EDV | 52 |
| 24 | BRC | 47 |
| 25 | Cathay Pacific | 47 |
| 26 | Japan Airlines | 47 |
| 27 | Avianca | 45 |
| 28 | easyJet | 43 |
| 29 | EJU | 42 |
| 30 | MXY | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6846 |
| 2 | 🇮🇳 IN | 610 |
| 3 | 🇪🇸 ES | 586 |
| 4 | 🇦🇺 AU | 555 |
| 5 | 🇧🇷 BR | 394 |
| 6 | 🇩🇪 DE | 382 |
| 7 | 🇨🇴 CO | 374 |
| 8 | 🇨🇦 CA | 372 |
| 9 | 🇮🇹 IT | 346 |
| 10 | 🇯🇵 JP | 344 |
| 11 | 🇲🇽 MX | 286 |
| 12 | 🇬🇧 GB | 266 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 198 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 176 |
| 17 | 🇬🇹 GT | 169 |
| 18 | 🇨🇭 CH | 168 |
| 19 | 🇳🇿 NZ | 163 |
| 20 | 🇿🇦 ZA | 161 |
| 21 | 🇵🇭 PH | 140 |
| 22 | 🇹🇷 TR | 138 |
| 23 | 🇹🇭 TH | 95 |
| 24 | 🇲🇦 MA | 94 |
| 25 | 🇵🇱 PL | 94 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇰🇷 KR | 85 |
| 28 | 🇲🇴 MO | 82 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 199 |
| 2 | Denver International Airport |  | US | 153 |
| 3 | Indira Gandhi International Airport |  | IN | 139 |
| 4 | El Dorado International Airport |  | CO | 129 |
| 5 | Tokyo International Airport |  | JP | 122 |
| 6 | La Aurora Airport |  | GT | 119 |
| 7 | Frankfurt am Main International Airport |  | DE | 115 |
| 8 | Harry Reid International Airport |  | US | 114 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 104 |
| 10 | Guaymaral Airport |  | CO | 90 |
| 11 | Zurich Airport |  | CH | 88 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 86 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 14 | Macau International Airport |  | MO | 82 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 82 |
| 16 | Chicago O'Hare International Airport |  | US | 81 |
| 17 | Reno/Tahoe International Airport |  | US | 75 |
| 18 | Tenerife Norte Airport |  | ES | 75 |
| 19 | Charlotte/Douglas International Airport |  | US | 70 |
| 20 | Madrid Barajas International Airport |  | ES | 70 |
| 21 | Bengaluru International Airport |  | IN | 68 |
| 22 | Kuala Lumpur International Airport |  | MY | 65 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 64 |
| 24 | Daniel K Inouye International Airport |  | US | 63 |
| 25 | Ninoy Aquino International Airport |  | PH | 63 |
| 26 | Salt Lake City International Airport |  | US | 63 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 28 | Malpensa International Airport |  | IT | 59 |
| 29 | Vitoria/Foronda Airport |  | ES | 59 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 31 | Miami International Airport |  | US | 57 |
| 32 | Seattle-Tacoma International Airport |  | US | 57 |
| 33 | Congonhas Airport |  | BR | 56 |
| 34 | Pune Airport |  | IN | 55 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 36 | Charles de Gaulle International Airport |  | FR | 52 |
| 37 | Centennial Airport |  | US | 51 |
| 38 | Barcelona International Airport |  | ES | 51 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 50 |
| 40 | Austin-Bergstrom International Airport |  | US | 48 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 35 | 14m | 114 km | 68.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 29 | 1h 6m | 706 km | 353.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 28 | 24m | 225 km | 108.6 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 24 | 1h 46m | 1,156 km | 478.8 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 22 | 24m | 99 km | 37.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 21 | 15m | 206 km | 74.7 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 19 | 52m | 556 km | 182.1 t |
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
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 14 | 1h 56m | 1,304 km | 315.0 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1110 | CXK | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-03-31 22:24 UTC | 2026-03-31 23:35 UTC | 1h 11m |
| N335MD |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-31 23:00 UTC | 2026-03-31 23:34 UTC | 33m |
| N254EK |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-31 23:14 UTC | 2026-03-31 23:33 UTC | 19m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-03-31 22:51 UTC | 2026-03-31 23:30 UTC | 39m |
| N282MM |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-31 22:54 UTC | 2026-03-31 23:30 UTC | 35m |
| N2150Z |  | Oconee County Regional Airport (KCEU) | Oconee County Regional Airport (KCEU) | 2026-03-31 23:14 UTC | 2026-03-31 23:28 UTC | 13m |
| N844SK |  | Plant City Airport (KPCM) | Plant City Airport (KPCM) | 2026-03-31 23:15 UTC | 2026-03-31 23:27 UTC | 11m |
| N6337D |  | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-03-31 23:09 UTC | 2026-03-31 23:26 UTC | 16m |
| CXK184 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-03-31 22:16 UTC | 2026-03-31 23:23 UTC | 1h 6m |
| N284L |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-03-31 22:27 UTC | 2026-03-31 23:11 UTC | 44m |
| NPN | NPN | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-31 22:33 UTC | 2026-03-31 23:11 UTC | 37m |
| R21201 |  | Eielson Afb Airport (PAEI) | Ladd Army Air Field (PAFB) | 2026-03-31 22:56 UTC | 2026-03-31 23:09 UTC | 12m |
| N431TX |  | Greeley-Weld County Airport (KGXY) | Smith Farms Airport (0TA2) | 2026-03-31 22:06 UTC | 2026-03-31 23:03 UTC | 56m |
| N550SG |  | Portland-Hillsboro Airport (KHIO) | Fresno Chandler Executive Airport (KFCH) | 2026-03-31 21:19 UTC | 2026-03-31 23:03 UTC | 1h 43m |
| X2A |  | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-03-31 23:02 UTC | 2026-03-31 23:02 UTC | 0m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-03-31 22:18 UTC | 2026-03-31 22:56 UTC | 37m |
| N631KA |  | Tahlequah Municipal Airport (KTQH) | Petit Jean Park Airport (KMPJ) | 2026-03-31 22:39 UTC | 2026-03-31 22:56 UTC | 16m |
| NPS | NPS | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-31 22:37 UTC | 2026-03-31 22:55 UTC | 17m |
| URSA31 | URS | Greg'N Sage Airport (AK41) | Ladd Army Air Field (PAFB) | 2026-03-31 22:21 UTC | 2026-03-31 22:55 UTC | 34m |
| BULET56 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-03-31 22:45 UTC | 2026-03-31 22:54 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
