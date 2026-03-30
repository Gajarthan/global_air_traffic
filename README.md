# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_09:25:55_UTC-green)

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

**Latest saved flight:** 2026-03-30 09:25:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 09:25:55 UTC

- **4,027** saved flights
- **2,907** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,027** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **53,455.2 tonnes** estimated CO2 emissions
- **3,098,850 km** total distance flown
- **904 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 138 |
| 3 | IndiGo | 101 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 57 |
| 9 | AXM | 52 |
| 10 | Delta Air Lines | 42 |
| 11 | Vueling | 41 |
| 12 | LATAM Airlines | 40 |
| 13 | LXJ | 37 |
| 14 | All Nippon Airways | 35 |
| 15 | United Airlines | 33 |
| 16 | QLK | 32 |
| 17 | VIV | 31 |
| 18 | Cathay Pacific | 30 |
| 19 | Japan Airlines | 30 |
| 20 | Avianca | 28 |
| 21 | AXB | 28 |
| 22 | EDV | 27 |
| 23 | Swiss International | 27 |
| 24 | WIF | 26 |
| 25 | Alaska Airlines | 25 |
| 26 | AZU | 22 |
| 27 | ARE | 21 |
| 28 | MXY | 21 |
| 29 | VOE | 21 |
| 30 | JST | 20 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3543 |
| 2 | 🇪🇸 ES | 303 |
| 3 | 🇮🇳 IN | 298 |
| 4 | 🇦🇺 AU | 273 |
| 5 | 🇨🇴 CO | 227 |
| 6 | 🇯🇵 JP | 220 |
| 7 | 🇧🇷 BR | 181 |
| 8 | 🇩🇪 DE | 174 |
| 9 | 🇨🇦 CA | 167 |
| 10 | 🇲🇽 MX | 161 |
| 11 | 🇮🇹 IT | 154 |
| 12 | 🇬🇧 GB | 133 |
| 13 | 🇲🇾 MY | 110 |
| 14 | 🇫🇷 FR | 106 |
| 15 | 🇵🇭 PH | 99 |
| 16 | 🇬🇹 GT | 98 |
| 17 | 🇿🇦 ZA | 95 |
| 18 | 🇨🇭 CH | 90 |
| 19 | 🇳🇴 NO | 83 |
| 20 | 🇬🇷 GR | 76 |
| 21 | 🇳🇿 NZ | 63 |
| 22 | 🇹🇷 TR | 57 |
| 23 | 🇮🇩 ID | 55 |
| 24 | 🇹🇭 TH | 54 |
| 25 | 🇲🇴 MO | 51 |
| 26 | 🇧🇸 BS | 46 |
| 27 | 🇵🇱 PL | 46 |
| 28 | 🇰🇷 KR | 45 |
| 29 | 🇲🇦 MA | 45 |
| 30 | 🇫🇮 FI | 38 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | Tokyo International Airport |  | JP | 73 |
| 5 | Indira Gandhi International Airport |  | IN | 65 |
| 6 | La Aurora Airport |  | GT | 64 |
| 7 | Frankfurt am Main International Airport |  | DE | 60 |
| 8 | Guaymaral Airport |  | CO | 54 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 10 | Tenerife Norte Airport |  | ES | 51 |
| 11 | Macau International Airport |  | MO | 51 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 13 | Harry Reid International Airport |  | US | 47 |
| 14 | Zurich Airport |  | CH | 46 |
| 15 | Chicago O'Hare International Airport |  | US | 45 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 45 |
| 17 | Ninoy Aquino International Airport |  | PH | 43 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 19 | Kuala Lumpur International Airport |  | MY | 40 |
| 20 | Charlotte/Douglas International Airport |  | US | 38 |
| 21 | Eleftherios Venizelos International Airport |  | GR | 34 |
| 22 | Reno/Tahoe International Airport |  | US | 33 |
| 23 | Miami International Airport |  | US | 33 |
| 24 | Madrid Barajas International Airport |  | ES | 33 |
| 25 | O. R. Tambo International Airport |  | ZA | 33 |
| 26 | Los Angeles International Airport |  | US | 32 |
| 27 | Bengaluru International Airport |  | IN | 32 |
| 28 | Vitoria/Foronda Airport |  | ES | 31 |
| 29 | Centennial Airport |  | US | 31 |
| 30 | Salt Lake City International Airport |  | US | 31 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 30 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 29 |
| 33 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 34 | Daniel K Inouye International Airport |  | US | 28 |
| 35 | CO86 |  |  | 28 |
| 36 | Tampa International Airport |  | US | 28 |
| 37 | Austin-Bergstrom International Airport |  | US | 28 |
| 38 | Charles de Gaulle International Airport |  | FR | 28 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 27 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 14 | 1h 6m | 706 km | 170.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 14 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 8 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 12 | 1h 39m | 1,423 km | 294.5 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 12 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 10 | 28m | 304 km | 52.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 10 | 22m | 252 km | 43.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 10 | 1h 25m | 910 km | 156.9 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 10 | 1h 10m | 770 km | 132.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 10 | 30m | 369 km | 63.7 t |
| 18 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 10 | 11m | 127 km | 21.9 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 9 | 52m | 546 km | 84.7 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
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
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-03-30 08:48 UTC | 2026-03-30 09:25 UTC | 37m |
| PCH66K | PCH | Buochs Airport (LSZC) | Bern Belp Airport (LSZB) | 2026-03-30 08:21 UTC | 2026-03-30 09:05 UTC | 43m |
| CPA008 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-03-29 21:27 UTC | 2026-03-30 09:02 UTC | 11h 34m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-03-29 21:46 UTC | 2026-03-30 08:58 UTC | 11h 11m |
| IOS222 | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-03-30 08:19 UTC | 2026-03-30 08:56 UTC | 37m |
| QTR3277 | Qatar Airways | Kutahya Airport (LTBN) | Harad Airport (OEHR) | 2026-03-30 05:24 UTC | 2026-03-30 08:47 UTC | 3h 22m |
| VJT792 | VJT | London Luton Airport (EGGW) | Macau International Airport (VMMC) | 2026-03-29 21:00 UTC | 2026-03-30 08:44 UTC | 11h 44m |
| KII517 | KII | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-03-30 06:25 UTC | 2026-03-30 08:39 UTC | 2h 13m |
| ANE2516 | ANE | Palma De Mallorca Airport (LEPA) | Palma De Mallorca Airport (LEPA) | 2026-03-30 08:22 UTC | 2026-03-30 08:38 UTC | 16m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-03-30 08:07 UTC | 2026-03-30 08:36 UTC | 29m |
| SAS71K | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Malpensa International Airport (LIMC) | 2026-03-30 06:39 UTC | 2026-03-30 08:35 UTC | 1h 56m |
| PRVCO | PRV | Nascimento I Airport (SDNI) | Parati Airport (SDTK) | 2026-03-30 08:09 UTC | 2026-03-30 08:34 UTC | 24m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Bakki Airport (BIBA) | 2026-03-30 08:18 UTC | 2026-03-30 08:33 UTC | 14m |
| P73C |  | Buochs Airport (LSZC) | Buochs Airport (LSZC) | 2026-03-30 08:25 UTC | 2026-03-30 08:32 UTC | 6m |
| VOE7YM | VOE | Valencia Airport (LEVC) | Vitoria/Foronda Airport (LEVT) | 2026-03-30 07:40 UTC | 2026-03-30 08:28 UTC | 47m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-03-29 21:05 UTC | 2026-03-30 08:26 UTC | 11h 21m |
| EZY37NU | easyJet | London Gatwick Airport (EGKK) | Gibraltar Airport (LXGB) | 2026-03-30 06:12 UTC | 2026-03-30 08:24 UTC | 2h 11m |
| ZSMPC | ZSM | Wonderboom Airport (FAWB) | Heidelburg Airport (FAHG) | 2026-03-30 08:00 UTC | 2026-03-30 08:23 UTC | 23m |
| THY70 | Turkish Airlines | Yalova Airport (LTBP) | Macau International Airport (VMMC) | 2026-03-29 23:10 UTC | 2026-03-30 08:20 UTC | 9h 10m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-03-30 08:02 UTC | 2026-03-30 08:19 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
