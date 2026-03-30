# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_07:52:04_UTC-green)

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

**Latest saved flight:** 2026-03-30 07:52:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 07:52:04 UTC

- **3,951** saved flights
- **2,865** unique routes
- **101** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,951** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **51,680.0 tonnes** estimated CO2 emissions
- **2,995,942 km** total distance flown
- **893 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 136 |
| 3 | IndiGo | 97 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 55 |
| 9 | AXM | 49 |
| 10 | Delta Air Lines | 42 |
| 11 | Vueling | 41 |
| 12 | LATAM Airlines | 39 |
| 13 | LXJ | 37 |
| 14 | United Airlines | 33 |
| 15 | QLK | 31 |
| 16 | VIV | 31 |
| 17 | All Nippon Airways | 30 |
| 18 | Cathay Pacific | 29 |
| 19 | Avianca | 28 |
| 20 | Japan Airlines | 28 |
| 21 | AXB | 27 |
| 22 | EDV | 27 |
| 23 | WIF | 26 |
| 24 | Alaska Airlines | 25 |
| 25 | Swiss International | 25 |
| 26 | AZU | 22 |
| 27 | ARE | 21 |
| 28 | MXY | 21 |
| 29 | JST | 20 |
| 30 | JIA | 18 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3537 |
| 2 | 🇪🇸 ES | 291 |
| 3 | 🇮🇳 IN | 285 |
| 4 | 🇦🇺 AU | 269 |
| 5 | 🇨🇴 CO | 227 |
| 6 | 🇯🇵 JP | 202 |
| 7 | 🇧🇷 BR | 177 |
| 8 | 🇩🇪 DE | 170 |
| 9 | 🇨🇦 CA | 167 |
| 10 | 🇲🇽 MX | 161 |
| 11 | 🇮🇹 IT | 148 |
| 12 | 🇬🇧 GB | 127 |
| 13 | 🇲🇾 MY | 105 |
| 14 | 🇫🇷 FR | 102 |
| 15 | 🇬🇹 GT | 98 |
| 16 | 🇵🇭 PH | 95 |
| 17 | 🇿🇦 ZA | 91 |
| 18 | 🇨🇭 CH | 83 |
| 19 | 🇳🇴 NO | 77 |
| 20 | 🇬🇷 GR | 73 |
| 21 | 🇳🇿 NZ | 63 |
| 22 | 🇮🇩 ID | 53 |
| 23 | 🇹🇷 TR | 53 |
| 24 | 🇹🇭 TH | 49 |
| 25 | 🇧🇸 BS | 46 |
| 26 | 🇲🇴 MO | 46 |
| 27 | 🇵🇱 PL | 44 |
| 28 | 🇰🇷 KR | 43 |
| 29 | 🇲🇦 MA | 42 |
| 30 | 🇫🇮 FI | 38 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | Tokyo International Airport |  | JP | 66 |
| 5 | Indira Gandhi International Airport |  | IN | 65 |
| 6 | La Aurora Airport |  | GT | 64 |
| 7 | Frankfurt am Main International Airport |  | DE | 58 |
| 8 | Guaymaral Airport |  | CO | 54 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 10 | Tenerife Norte Airport |  | ES | 51 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 12 | Harry Reid International Airport |  | US | 46 |
| 13 | Macau International Airport |  | MO | 46 |
| 14 | Chicago O'Hare International Airport |  | US | 45 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 45 |
| 16 | Zurich Airport |  | CH | 44 |
| 17 | Ninoy Aquino International Airport |  | PH | 42 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 19 | Kuala Lumpur International Airport |  | MY | 39 |
| 20 | Charlotte/Douglas International Airport |  | US | 38 |
| 21 | Reno/Tahoe International Airport |  | US | 33 |
| 22 | Miami International Airport |  | US | 33 |
| 23 | Eleftherios Venizelos International Airport |  | GR | 32 |
| 24 | Los Angeles International Airport |  | US | 32 |
| 25 | O. R. Tambo International Airport |  | ZA | 32 |
| 26 | Madrid Barajas International Airport |  | ES | 31 |
| 27 | Centennial Airport |  | US | 31 |
| 28 | Salt Lake City International Airport |  | US | 31 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 30 |
| 30 | Vitoria/Foronda Airport |  | ES | 29 |
| 31 | Bengaluru International Airport |  | IN | 29 |
| 32 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 33 | Daniel K Inouye International Airport |  | US | 28 |
| 34 | CO86 |  |  | 28 |
| 35 | Tampa International Airport |  | US | 28 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 28 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 27 |
| 39 | Austin-Bergstrom International Airport |  | US | 27 |
| 40 | Seattle-Tacoma International Airport |  | US | 27 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 22 | 24m | 225 km | 85.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 14 | 30m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 7 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 12 | 1h 39m | 1,423 km | 294.5 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 12 | 1h 6m | 706 km | 146.1 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 13 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 10 | 30m | 369 km | 63.7 t |
| 14 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 9 | 28m | 304 km | 47.2 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 9 | 52m | 546 km | 84.7 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 9 | 1h 10m | 770 km | 119.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 9 | 11m | 127 km | 19.7 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 9 | 1h 26m | 910 km | 141.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 9 | 4m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 8 | 1h 58m | 1,156 km | 159.6 t |
| 25 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 8 | 8h 30m | 38 km | 5.2 t |
| 28 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 8 | 32m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 6VHAW |  | Leopold Sedar Senghor International Airport (GOOY) | Banjul International Airport (GBYD) | 2026-03-30 07:18 UTC | 2026-03-30 07:52 UTC | 33m |
| OKPTT | OKP | Tocna Praha Glider Airport (LKTC) | Sondrio Caiolo Airport (LILO) | 2026-03-30 06:08 UTC | 2026-03-30 07:27 UTC | 1h 18m |
| CLX4327 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-03-29 20:15 UTC | 2026-03-30 07:25 UTC | 11h 10m |
| J046KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-03-30 07:04 UTC | 2026-03-30 07:19 UTC | 14m |
| ZKHUP | ZKH | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-03-30 07:06 UTC | 2026-03-30 07:18 UTC | 11m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 06:40 UTC | 2026-03-30 07:18 UTC | 37m |
| DHTAF | DHT | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-03-30 07:17 UTC | 2026-03-30 07:17 UTC | 0m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-29 23:41 UTC | 2026-03-30 07:15 UTC | 7h 33m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-03-29 19:13 UTC | 2026-03-30 07:14 UTC | 12h 0m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-03-30 06:58 UTC | 2026-03-30 07:09 UTC | 11m |
| RYR76HY | Ryanair | Brussels South Charleroi Airport (EBCI) | Nador International Airport (GMMW) | 2026-03-30 05:00 UTC | 2026-03-30 07:06 UTC | 2h 6m |
| PGC65L | PGC | Eleftherios Venizelos International Airport (LGAV) | Lecce / Lepore Airport (LINL) | 2026-03-30 06:06 UTC | 2026-03-30 07:01 UTC | 55m |
| BOX510 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-03-29 20:09 UTC | 2026-03-30 06:59 UTC | 10h 50m |
| RSC18ZJ | RSC | Tenerife Norte Airport (GCXO) | La Gomera Airport (GCGM) | 2026-03-30 06:48 UTC | 2026-03-30 06:58 UTC | 10m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-03-29 19:32 UTC | 2026-03-30 06:57 UTC | 11h 25m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-03-30 06:24 UTC | 2026-03-30 06:54 UTC | 30m |
| SKY145 | SKY | Okayama Airport (RJOB) | Saga Airport (RJFS) | 2026-03-30 06:08 UTC | 2026-03-30 06:54 UTC | 45m |
| LOG41EG | LOG | Edinburgh Airport (EGPH) | Wick Airport (EGPC) | 2026-03-30 06:09 UTC | 2026-03-30 06:52 UTC | 42m |
| DHK597 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-03-29 20:03 UTC | 2026-03-30 06:52 UTC | 10h 49m |
| AXM6496 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-03-30 06:35 UTC | 2026-03-30 06:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
