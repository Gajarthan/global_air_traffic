# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_04:20:26_UTC-green)

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

**Latest saved flight:** 2026-03-30 04:20:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 04:20:26 UTC

- **3,787** saved flights
- **2,780** unique routes
- **99** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,787** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **48,946.1 tonnes** estimated CO2 emissions
- **2,837,456 km** total distance flown
- **884 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 124 |
| 3 | EJA | 92 |
| 4 | IndiGo | 89 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 42 |
| 10 | Delta Air Lines | 41 |
| 11 | LATAM Airlines | 39 |
| 12 | LXJ | 37 |
| 13 | Vueling | 36 |
| 14 | United Airlines | 33 |
| 15 | VIV | 31 |
| 16 | All Nippon Airways | 30 |
| 17 | Avianca | 28 |
| 18 | Cathay Pacific | 27 |
| 19 | EDV | 27 |
| 20 | QLK | 25 |
| 21 | AXB | 24 |
| 22 | Alaska Airlines | 23 |
| 23 | WIF | 23 |
| 24 | Japan Airlines | 22 |
| 25 | Swiss International | 22 |
| 26 | ARE | 21 |
| 27 | AZU | 21 |
| 28 | MXY | 21 |
| 29 | JIA | 18 |
| 30 | JST | 18 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3513 |
| 2 | 🇪🇸 ES | 273 |
| 3 | 🇮🇳 IN | 256 |
| 4 | 🇨🇴 CO | 227 |
| 5 | 🇦🇺 AU | 226 |
| 6 | 🇧🇷 BR | 175 |
| 7 | 🇯🇵 JP | 173 |
| 8 | 🇨🇦 CA | 165 |
| 9 | 🇲🇽 MX | 160 |
| 10 | 🇩🇪 DE | 160 |
| 11 | 🇮🇹 IT | 136 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇬🇹 GT | 98 |
| 14 | 🇫🇷 FR | 93 |
| 15 | 🇲🇾 MY | 89 |
| 16 | 🇵🇭 PH | 85 |
| 17 | 🇿🇦 ZA | 84 |
| 18 | 🇨🇭 CH | 74 |
| 19 | 🇳🇴 NO | 71 |
| 20 | 🇬🇷 GR | 66 |
| 21 | 🇳🇿 NZ | 54 |
| 22 | 🇹🇭 TH | 49 |
| 23 | 🇹🇷 TR | 48 |
| 24 | 🇮🇩 ID | 47 |
| 25 | 🇧🇸 BS | 46 |
| 26 | 🇵🇱 PL | 43 |
| 27 | 🇲🇦 MA | 40 |
| 28 | 🇲🇴 MO | 40 |
| 29 | 🇫🇮 FI | 38 |
| 30 | 🇰🇷 KR | 33 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | La Aurora Airport |  | GT | 64 |
| 5 | Indira Gandhi International Airport |  | IN | 59 |
| 6 | Tokyo International Airport |  | JP | 58 |
| 7 | Frankfurt am Main International Airport |  | DE | 55 |
| 8 | Guaymaral Airport |  | CO | 54 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 11 | Tenerife Norte Airport |  | ES | 49 |
| 12 | Harry Reid International Airport |  | US | 46 |
| 13 | Chicago O'Hare International Airport |  | US | 45 |
| 14 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 15 | Macau International Airport |  | MO | 40 |
| 16 | Charlotte/Douglas International Airport |  | US | 38 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 38 |
| 18 | Zurich Airport |  | CH | 37 |
| 19 | Ninoy Aquino International Airport |  | PH | 37 |
| 20 | Kuala Lumpur International Airport |  | MY | 35 |
| 21 | Reno/Tahoe International Airport |  | US | 33 |
| 22 | Miami International Airport |  | US | 33 |
| 23 | Centennial Airport |  | US | 31 |
| 24 | Salt Lake City International Airport |  | US | 31 |
| 25 | Los Angeles International Airport |  | US | 30 |
| 26 | O. R. Tambo International Airport |  | ZA | 30 |
| 27 | Madrid Barajas International Airport |  | ES | 29 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 29 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 30 | CO86 |  |  | 28 |
| 31 | Tampa International Airport |  | US | 28 |
| 32 | Vitoria/Foronda Airport |  | ES | 28 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 28 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 27 |
| 36 | Seattle-Tacoma International Airport |  | US | 27 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 27 |
| 38 | Austin-Bergstrom International Airport |  | US | 26 |
| 39 | Perales Airport |  | CO | 26 |
| 40 | Daniel K Inouye International Airport |  | US | 25 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 19 | 24m | 225 km | 73.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 11 | 1h 6m | 706 km | 133.9 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 12 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 13 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 9 | 29m | 369 km | 57.3 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 8 | 52m | 546 km | 75.3 t |
| 19 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 20 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 8 | 1h 26m | 910 km | 125.5 t |
| 22 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 23 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 24 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 8 | 4m | - | - |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 28 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 7 | 1h 10m | 770 km | 93.0 t |
| 29 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 7 | 51m | 645 km | 77.9 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 7 | 8h 38m | 38 km | 4.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YHU | YHU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-30 03:47 UTC | 2026-03-30 04:20 UTC | 32m |
| UAL962 | United Airlines | Newark Liberty International Airport (KEWR) | Berlin Brandenburg Airport (EDDB) | 2026-03-29 21:18 UTC | 2026-03-30 04:17 UTC | 6h 59m |
| CFSUG | CFS | Edmonton / Gartner Airport (CFQ7) | Hardisty Airport (CEA5) | 2026-03-30 03:49 UTC | 2026-03-30 04:11 UTC | 21m |
| CFH3 | CFH | Katoomba Airport (YKAT) | Sydney Bankstown Airport (YSBK) | 2026-03-30 03:35 UTC | 2026-03-30 03:59 UTC | 23m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-03-30 03:25 UTC | 2026-03-30 03:51 UTC | 25m |
| J985KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-03-30 03:08 UTC | 2026-03-30 03:41 UTC | 32m |
| VOI3296 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-03-30 00:48 UTC | 2026-03-30 03:39 UTC | 2h 51m |
| XSN06 | XSN | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-03-30 02:56 UTC | 2026-03-30 03:33 UTC | 37m |
| SWT1810 | SWT | Cologne Bonn Airport (EDDK) | Vitoria/Foronda Airport (LEVT) | 2026-03-30 01:59 UTC | 2026-03-30 03:31 UTC | 1h 31m |
| AM312 |  | Melbourne Essendon Airport (YMEN) | Wycheproof Airport (YWYF) | 2026-03-30 02:53 UTC | 2026-03-30 03:28 UTC | 35m |
| AAL2768 | American Airlines | Los Angeles International Airport (KLAX) | Dallas-Fort Worth International Airport (KDFW) | 2026-03-30 00:44 UTC | 2026-03-30 03:27 UTC | 2h 42m |
| QXE2414 | QXE | Seattle-Tacoma International Airport (KSEA) | Bombay Farms Airport (OG19) | 2026-03-30 02:54 UTC | 2026-03-30 03:25 UTC | 31m |
| ERU18 | ERU | Robin Airport (59AZ) | Robin Airport (59AZ) | 2026-03-30 03:20 UTC | 2026-03-30 03:24 UTC | 3m |
| VTFSO | VTF | Bhiwani Airport (VIBW) | Jhunjhunu Airport (VI69) | 2026-03-30 02:19 UTC | 2026-03-30 03:23 UTC | 1h 3m |
| NWI | NWI | Melbourne Essendon Airport (YMEN) | Lethbridge Park Airport (YLED) | 2026-03-30 02:48 UTC | 2026-03-30 03:22 UTC | 33m |
| J911KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-03-30 03:02 UTC | 2026-03-30 03:22 UTC | 19m |
| N21D |  | Tracy Municipal Airport (KTCY) | El Peco Ranch Airport (49CL) | 2026-03-30 02:37 UTC | 2026-03-30 03:18 UTC | 41m |
| ANA793 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-03-30 02:15 UTC | 2026-03-30 03:17 UTC | 1h 1m |
| SKW6470 | SkyWest Airlines | Dallas-Fort Worth International Airport (KDFW) | Jicarilla Apache Nation Airport (K24N) | 2026-03-30 01:53 UTC | 2026-03-30 03:16 UTC | 1h 22m |
| IGO5036 | IndiGo | Indira Gandhi International Airport (VIDP) | Dhorpatan Airport (VNDR) | 2026-03-30 02:31 UTC | 2026-03-30 03:15 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
