# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_10:14:10_UTC-green)

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

**Latest saved flight:** 2026-03-30 10:14:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 10:14:10 UTC

- **4,096** saved flights
- **2,942** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,096** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **54,508.9 tonnes** estimated CO2 emissions
- **3,159,939 km** total distance flown
- **906 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 142 |
| 3 | IndiGo | 106 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 58 |
| 9 | AXM | 53 |
| 10 | Delta Air Lines | 42 |
| 11 | Vueling | 41 |
| 12 | LATAM Airlines | 40 |
| 13 | LXJ | 37 |
| 14 | All Nippon Airways | 36 |
| 15 | QLK | 33 |
| 16 | United Airlines | 33 |
| 17 | Japan Airlines | 32 |
| 18 | VIV | 31 |
| 19 | Cathay Pacific | 30 |
| 20 | Swiss International | 30 |
| 21 | AXB | 29 |
| 22 | Avianca | 28 |
| 23 | EDV | 27 |
| 24 | WIF | 27 |
| 25 | Alaska Airlines | 25 |
| 26 | AZU | 23 |
| 27 | VOE | 22 |
| 28 | ARE | 21 |
| 29 | MXY | 21 |
| 30 | JST | 20 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3549 |
| 2 | 🇮🇳 IN | 321 |
| 3 | 🇪🇸 ES | 308 |
| 4 | 🇦🇺 AU | 283 |
| 5 | 🇯🇵 JP | 228 |
| 6 | 🇨🇴 CO | 227 |
| 7 | 🇧🇷 BR | 185 |
| 8 | 🇩🇪 DE | 182 |
| 9 | 🇨🇦 CA | 167 |
| 10 | 🇲🇽 MX | 161 |
| 11 | 🇮🇹 IT | 160 |
| 12 | 🇬🇧 GB | 135 |
| 13 | 🇫🇷 FR | 112 |
| 14 | 🇲🇾 MY | 112 |
| 15 | 🇿🇦 ZA | 105 |
| 16 | 🇵🇭 PH | 99 |
| 17 | 🇬🇹 GT | 98 |
| 18 | 🇨🇭 CH | 93 |
| 19 | 🇳🇴 NO | 87 |
| 20 | 🇬🇷 GR | 77 |
| 21 | 🇳🇿 NZ | 63 |
| 22 | 🇹🇷 TR | 60 |
| 23 | 🇹🇭 TH | 56 |
| 24 | 🇮🇩 ID | 55 |
| 25 | 🇲🇴 MO | 54 |
| 26 | 🇵🇱 PL | 50 |
| 27 | 🇰🇷 KR | 47 |
| 28 | 🇧🇸 BS | 46 |
| 29 | 🇲🇦 MA | 45 |
| 30 | 🇫🇮 FI | 39 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | Tokyo International Airport |  | JP | 75 |
| 5 | Indira Gandhi International Airport |  | IN | 74 |
| 6 | La Aurora Airport |  | GT | 64 |
| 7 | Frankfurt am Main International Airport |  | DE | 62 |
| 8 | Macau International Airport |  | MO | 54 |
| 9 | Guaymaral Airport |  | CO | 54 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 11 | Tenerife Norte Airport |  | ES | 51 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 13 | Zurich Airport |  | CH | 49 |
| 14 | Harry Reid International Airport |  | US | 47 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 16 | Chicago O'Hare International Airport |  | US | 45 |
| 17 | Ninoy Aquino International Airport |  | PH | 43 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 19 | Kuala Lumpur International Airport |  | MY | 40 |
| 20 | Charlotte/Douglas International Airport |  | US | 38 |
| 21 | O. R. Tambo International Airport |  | ZA | 36 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 34 |
| 23 | Madrid Barajas International Airport |  | ES | 34 |
| 24 | Reno/Tahoe International Airport |  | US | 33 |
| 25 | Miami International Airport |  | US | 33 |
| 26 | Bengaluru International Airport |  | IN | 33 |
| 27 | Los Angeles International Airport |  | US | 32 |
| 28 | Vitoria/Foronda Airport |  | ES | 32 |
| 29 | Charles de Gaulle International Airport |  | FR | 31 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 31 |
| 31 | Centennial Airport |  | US | 31 |
| 32 | Salt Lake City International Airport |  | US | 31 |
| 33 | Daniel K Inouye International Airport |  | US | 29 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 29 |
| 35 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 36 | CO86 |  |  | 28 |
| 37 | Tampa International Airport |  | US | 28 |
| 38 | Austin-Bergstrom International Airport |  | US | 28 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 40 | Amsterdam Airport Schiphol |  | NL | 28 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 4 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 16 | 30m | - | - |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 15 | 1h 6m | 706 km | 182.6 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 8 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 12 | 1h 39m | 1,423 km | 294.5 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 11 | 22m | 252 km | 47.8 t |
| 12 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 10 | 28m | 304 km | 52.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 10 | 1h 25m | 910 km | 156.9 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 10 | 1h 10m | 770 km | 132.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 10 | 30m | 369 km | 63.7 t |
| 18 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 10 | 11m | 127 km | 21.9 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 10 | 4m | - | - |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 9 | 52m | 546 km | 84.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
| 24 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 8 | 1h 58m | 1,156 km | 159.6 t |
| 26 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 8 | 8h 30m | 38 km | 5.2 t |
| 29 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N429CF |  | Dallas Executive Airport (KRBD) | Beulah Field (01TX) | 2026-03-30 10:01 UTC | 2026-03-30 10:14 UTC | 12m |
| RYR80NW | Ryanair | London Luton Airport (EGGW) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-03-30 08:10 UTC | 2026-03-30 10:09 UTC | 1h 58m |
| CRK260 | CRK | Chek Lap Kok International Airport (VHHH) | Longtan Air Base (RCDI) | 2026-03-30 08:46 UTC | 2026-03-30 10:02 UTC | 1h 15m |
| ZSMPC | ZSM | O. R. Tambo International Airport (FAOR) | Rooiberg Airport (FARO) | 2026-03-30 09:34 UTC | 2026-03-30 09:59 UTC | 25m |
| PVF | PVF | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-03-30 09:44 UTC | 2026-03-30 09:57 UTC | 13m |
| ZSSGC | ZSS | Lanseria Airport (FALA) | Carolina Airport (FACL) | 2026-03-30 09:32 UTC | 2026-03-30 09:53 UTC | 20m |
| LSI187 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-03-29 22:42 UTC | 2026-03-30 09:48 UTC | 11h 6m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 09:02 UTC | 2026-03-30 09:42 UTC | 40m |
| THY6061 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-03-29 19:43 UTC | 2026-03-30 09:41 UTC | 13h 58m |
| IGO7711 | IndiGo | Bengaluru International Airport (VOBL) | Salem Airport (VOSM) | 2026-03-30 09:08 UTC | 2026-03-30 09:39 UTC | 30m |
| MNB509 | MNB | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-03-30 05:14 UTC | 2026-03-30 09:33 UTC | 4h 19m |
| RYR2495 | Ryanair | Barcelona International Airport (LEBL) | Son Bonet Airport (LESB) | 2026-03-30 08:51 UTC | 2026-03-30 09:33 UTC | 41m |
| AIC2706 | Air India | Indira Gandhi International Airport (VIDP) | Shimla Airport (VISM) | 2026-03-30 09:03 UTC | 2026-03-30 09:28 UTC | 25m |
| RYR564P | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Brindisi / Casale Airport (LIBR) | 2026-03-30 08:34 UTC | 2026-03-30 09:28 UTC | 54m |
| AUA761 | Austrian Airlines | Vienna International Airport (LOWW) | Pristina International Airport (BKPR) | 2026-03-30 08:23 UTC | 2026-03-30 09:28 UTC | 1h 4m |
| WZZ4343 | Wizz Air | Dortmund Airport (EDLW) | Stenkovec Brazda Airport (LW75) | 2026-03-30 07:40 UTC | 2026-03-30 09:27 UTC | 1h 47m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-03-30 08:48 UTC | 2026-03-30 09:25 UTC | 37m |
| AZU2797 | AZU | Viracopos International Airport (SBKP) | Ubatuba Airport (SDUB) | 2026-03-30 09:03 UTC | 2026-03-30 09:25 UTC | 22m |
| AAH220 | AAH | Daniel K Inouye International Airport (PHNL) | Lanai Airport (PHNY) | 2026-03-30 09:07 UTC | 2026-03-30 09:25 UTC | 17m |
| SWR917 | Swiss International | Dresden Airport (EDDC) | Zurich Airport (LSZH) | 2026-03-30 08:27 UTC | 2026-03-30 09:21 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
