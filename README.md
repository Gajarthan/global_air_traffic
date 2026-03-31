# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_03:11:20_UTC-green)

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

**Latest saved flight:** 2026-03-31 03:11:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 03:11:20 UTC

- **5,902** saved flights
- **3,972** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,902** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **74,426.6 tonnes** estimated CO2 emissions
- **4,314,588 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 148 |
| 4 | EJA | 129 |
| 5 | American Airlines | 120 |
| 6 | Southwest Airlines | 98 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 67 |
| 10 | AXM | 60 |
| 11 | LXJ | 57 |
| 12 | Delta Air Lines | 55 |
| 13 | Vueling | 55 |
| 14 | Cathay Pacific | 46 |
| 15 | United Airlines | 46 |
| 16 | VIV | 46 |
| 17 | QLK | 44 |
| 18 | All Nippon Airways | 43 |
| 19 | AZU | 43 |
| 20 | WIF | 43 |
| 21 | EDV | 39 |
| 22 | Japan Airlines | 39 |
| 23 | Swiss International | 38 |
| 24 | Alaska Airlines | 37 |
| 25 | Avianca | 37 |
| 26 | AXB | 34 |
| 27 | MXY | 32 |
| 28 | VOE | 31 |
| 29 | EJU | 30 |
| 30 | GLO | 29 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5285 |
| 2 | 🇮🇳 IN | 440 |
| 3 | 🇪🇸 ES | 408 |
| 4 | 🇦🇺 AU | 385 |
| 5 | 🇧🇷 BR | 312 |
| 6 | 🇨🇴 CO | 288 |
| 7 | 🇯🇵 JP | 273 |
| 8 | 🇮🇹 IT | 264 |
| 9 | 🇨🇦 CA | 263 |
| 10 | 🇩🇪 DE | 242 |
| 11 | 🇲🇽 MX | 226 |
| 12 | 🇬🇧 GB | 184 |
| 13 | 🇫🇷 FR | 171 |
| 14 | 🇳🇴 NO | 145 |
| 15 | 🇲🇾 MY | 133 |
| 16 | 🇬🇹 GT | 130 |
| 17 | 🇨🇭 CH | 125 |
| 18 | 🇿🇦 ZA | 123 |
| 19 | 🇵🇭 PH | 118 |
| 20 | 🇬🇷 GR | 117 |
| 21 | 🇳🇿 NZ | 105 |
| 22 | 🇹🇷 TR | 92 |
| 23 | 🇹🇭 TH | 76 |
| 24 | 🇲🇴 MO | 75 |
| 25 | 🇲🇦 MA | 69 |
| 26 | 🇵🇱 PL | 65 |
| 27 | 🇮🇩 ID | 64 |
| 28 | 🇧🇸 BS | 60 |
| 29 | 🇰🇷 KR | 55 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 162 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | El Dorado International Airport |  | CO | 105 |
| 4 | Indira Gandhi International Airport |  | IN | 100 |
| 5 | Tokyo International Airport |  | JP | 93 |
| 6 | La Aurora Airport |  | GT | 89 |
| 7 | Frankfurt am Main International Airport |  | DE | 80 |
| 8 | Chicago O'Hare International Airport |  | US | 76 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 10 | Macau International Airport |  | MO | 75 |
| 11 | Harry Reid International Airport |  | US | 74 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 13 | Zurich Airport |  | CH | 66 |
| 14 | Guaymaral Airport |  | CO | 65 |
| 15 | Tenerife Norte Airport |  | ES | 62 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 62 |
| 17 | Reno/Tahoe International Airport |  | US | 55 |
| 18 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 19 | Ninoy Aquino International Airport |  | PH | 53 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 52 |
| 21 | Charlotte/Douglas International Airport |  | US | 50 |
| 22 | Bengaluru International Airport |  | IN | 49 |
| 23 | Salt Lake City International Airport |  | US | 49 |
| 24 | Madrid Barajas International Airport |  | ES | 48 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 48 |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 27 | Malpensa International Airport |  | IT | 47 |
| 28 | Kuala Lumpur International Airport |  | MY | 47 |
| 29 | Miami International Airport |  | US | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 45 |
| 31 | Congonhas Airport |  | BR | 45 |
| 32 | Seattle-Tacoma International Airport |  | US | 43 |
| 33 | Centennial Airport |  | US | 43 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 35 | O. R. Tambo International Airport |  | ZA | 42 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 40 |
| 38 | Los Angeles International Airport |  | US | 39 |
| 39 | Daniel K Inouye International Airport |  | US | 39 |
| 40 | Austin-Bergstrom International Airport |  | US | 39 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 24 | 24m | 225 km | 93.1 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 18 | 1h 7m | 706 km | 219.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 18 | 25m | 99 km | 30.8 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 15 | 1h 50m | 1,156 km | 299.2 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 15 | 4m | - | - |
| 12 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 14 | 30m | 369 km | 89.1 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 12 | 28m | 304 km | 62.9 t |
| 19 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 12 | 53m | 546 km | 113.0 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 12 | 1h 10m | 770 km | 159.4 t |
| 22 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 12 | 51m | 556 km | 115.0 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 11 | 1h 46m | 1,290 km | 244.8 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 11 | 30m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JAL374 | Japan Airlines | Yamaguchi Ube Airport (RJDC) | Tokyo International Airport (RJTT) | 2026-03-31 01:53 UTC | 2026-03-31 03:11 UTC | 1h 17m |
| N744ND |  | Oxnard Airport (KOXR) | Meadows Field (KBFL) | 2026-03-31 02:14 UTC | 2026-03-31 03:10 UTC | 56m |
| ZJF | ZJF | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-03-31 02:11 UTC | 2026-03-31 03:08 UTC | 56m |
| AOH | AOH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 02:49 UTC | 2026-03-31 03:08 UTC | 18m |
| OME71 | OME | March Arb Airport (KRIV) | Outback Ranch Airstrip (AZ01) | 2026-03-30 23:32 UTC | 2026-03-31 03:02 UTC | 3h 30m |
| LBQ791 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-03-31 00:46 UTC | 2026-03-31 03:02 UTC | 2h 15m |
| UAE9964 | Emirates | Malpensa International Airport (LIMC) | Shaibah Airport (OESB) | 2026-03-30 21:55 UTC | 2026-03-31 03:00 UTC | 5h 4m |
| N36PJ |  | Kingman Airport (KIGM) | Scottsdale Airport (KSDL) | 2026-03-31 02:16 UTC | 2026-03-31 03:00 UTC | 44m |
| N786LF |  | Aurora State Airport (KUAO) | 07OR (07OR) | 2026-03-31 02:39 UTC | 2026-03-31 02:49 UTC | 10m |
| RAM248 | Royal Air Maroc | Tit Mellil Airport (GMMT) | Bassatine Airport (GMFM) | 2026-03-31 01:59 UTC | 2026-03-31 02:49 UTC | 49m |
| NLI | NLI | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-31 02:32 UTC | 2026-03-31 02:48 UTC | 15m |
| CCA907 | Air China | Shenzhen Bao'an International Airport (ZGSZ) | Khrabrovo Airport (UMKK) | 2026-03-29 13:59 UTC | 2026-03-31 02:47 UTC | 36h 47m |
| KAL2147 | Korean Air | Incheon International Airport (RKSI) | Naha Airport (ROAH) | 2026-03-31 00:43 UTC | 2026-03-31 02:34 UTC | 1h 51m |
| LBQ792 | LBQ | Syracuse Hancock International Airport (KSYR) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-03-31 02:03 UTC | 2026-03-31 02:25 UTC | 21m |
| CPA344 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-30 11:24 UTC | 2026-03-31 02:23 UTC | 14h 59m |
| MXY609 | MXY | San Francisco International Airport (KSFO) | San Bernardino International Airport (KSBD) | 2026-03-31 01:19 UTC | 2026-03-31 02:21 UTC | 1h 2m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-31 00:00 UTC | 2026-03-31 02:20 UTC | 2h 19m |
| JEC5114 | JEC | El Dorado International Airport (SKBO) | Carmen De Bolivar Airport (SKCB) | 2026-03-31 00:06 UTC | 2026-03-31 02:18 UTC | 2h 12m |
| J997KT |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-03-31 02:03 UTC | 2026-03-31 02:18 UTC | 14m |
| IGO7324 | IndiGo | Indira Gandhi International Airport (VIDP) | Pithorgarh Airport (VIDF) | 2026-03-31 01:52 UTC | 2026-03-31 02:18 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
