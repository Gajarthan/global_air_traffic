# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_01:28:10_UTC-green)

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

**Latest saved flight:** 2026-03-30 01:28:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 01:28:10 UTC

- **3,711** saved flights
- **2,738** unique routes
- **99** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,711** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **48,105.1 tonnes** estimated CO2 emissions
- **2,788,701 km** total distance flown
- **887 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 212 |
| 2 | Ryanair | 124 |
| 3 | EJA | 92 |
| 4 | American Airlines | 83 |
| 5 | IndiGo | 83 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 53 |
| 9 | Delta Air Lines | 41 |
| 10 | AXM | 40 |
| 11 | LATAM Airlines | 39 |
| 12 | LXJ | 37 |
| 13 | Vueling | 36 |
| 14 | United Airlines | 32 |
| 15 | VIV | 31 |
| 16 | Avianca | 28 |
| 17 | Cathay Pacific | 27 |
| 18 | EDV | 26 |
| 19 | All Nippon Airways | 23 |
| 20 | Alaska Airlines | 23 |
| 21 | QLK | 23 |
| 22 | Swiss International | 22 |
| 23 | WIF | 22 |
| 24 | ARE | 21 |
| 25 | AZU | 21 |
| 26 | MXY | 21 |
| 27 | Japan Airlines | 20 |
| 28 | AXB | 19 |
| 29 | JIA | 18 |
| 30 | VOE | 18 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3472 |
| 2 | 🇪🇸 ES | 272 |
| 3 | 🇮🇳 IN | 229 |
| 4 | 🇨🇴 CO | 227 |
| 5 | 🇦🇺 AU | 210 |
| 6 | 🇧🇷 BR | 175 |
| 7 | 🇨🇦 CA | 163 |
| 8 | 🇩🇪 DE | 158 |
| 9 | 🇲🇽 MX | 156 |
| 10 | 🇯🇵 JP | 150 |
| 11 | 🇮🇹 IT | 136 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇬🇹 GT | 98 |
| 14 | 🇫🇷 FR | 93 |
| 15 | 🇲🇾 MY | 86 |
| 16 | 🇿🇦 ZA | 84 |
| 17 | 🇵🇭 PH | 81 |
| 18 | 🇨🇭 CH | 74 |
| 19 | 🇳🇴 NO | 69 |
| 20 | 🇬🇷 GR | 66 |
| 21 | 🇳🇿 NZ | 50 |
| 22 | 🇹🇷 TR | 48 |
| 23 | 🇹🇭 TH | 47 |
| 24 | 🇧🇸 BS | 46 |
| 25 | 🇵🇱 PL | 43 |
| 26 | 🇲🇦 MA | 40 |
| 27 | 🇲🇴 MO | 40 |
| 28 | 🇫🇮 FI | 38 |
| 29 | 🇮🇩 ID | 37 |
| 30 | 🇳🇱 NL | 32 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 107 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | La Aurora Airport |  | GT | 64 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 8 | Indira Gandhi International Airport |  | IN | 52 |
| 9 | Tokyo International Airport |  | JP | 50 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 49 |
| 11 | Tenerife Norte Airport |  | ES | 49 |
| 12 | Harry Reid International Airport |  | US | 46 |
| 13 | Chicago O'Hare International Airport |  | US | 45 |
| 14 | Macau International Airport |  | MO | 40 |
| 15 | Atizapan De Zaragoza Airport |  | MX | 40 |
| 16 | Charlotte/Douglas International Airport |  | US | 38 |
| 17 | Zurich Airport |  | CH | 37 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 36 |
| 19 | Ninoy Aquino International Airport |  | PH | 35 |
| 20 | Kuala Lumpur International Airport |  | MY | 34 |
| 21 | Reno/Tahoe International Airport |  | US | 33 |
| 22 | Miami International Airport |  | US | 33 |
| 23 | Salt Lake City International Airport |  | US | 31 |
| 24 | Centennial Airport |  | US | 30 |
| 25 | O. R. Tambo International Airport |  | ZA | 30 |
| 26 | Los Angeles International Airport |  | US | 29 |
| 27 | Madrid Barajas International Airport |  | ES | 29 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 29 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 30 | CO86 |  |  | 28 |
| 31 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 28 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 27 |
| 34 | Tampa International Airport |  | US | 27 |
| 35 | Vitoria/Foronda Airport |  | ES | 27 |
| 36 | Austin-Bergstrom International Airport |  | US | 26 |
| 37 | Perales Airport |  | CO | 26 |
| 38 | Daniel K Inouye International Airport |  | US | 25 |
| 39 | Charles de Gaulle International Airport |  | FR | 25 |
| 40 | Seattle-Tacoma International Airport |  | US | 25 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 18 | 23m | 225 km | 69.8 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 10 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 11 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 12 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 9 | 29m | 369 km | 57.3 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
| 18 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 19 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 20 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 21 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 24 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 7 | 52m | 546 km | 65.9 t |
| 25 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 7 | 1h 10m | 770 km | 93.0 t |
| 26 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 7 | 51m | 645 km | 77.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 7 | 8h 38m | 38 km | 4.6 t |
| 29 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 7 | 54m | 630 km | 76.0 t |
| 30 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 7 | 1h 26m | 910 km | 109.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IDB | IDB | Warnervale Airport (YWVA) | Sydney Bankstown Airport (YSBK) | 2026-03-30 00:54 UTC | 2026-03-30 01:28 UTC | 33m |
| N5043J |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-03-30 00:16 UTC | 2026-03-30 01:21 UTC | 1h 5m |
| N1947L |  | University Airport (KEDU) | Tracy Municipal Airport (KTCY) | 2026-03-30 00:08 UTC | 2026-03-30 01:13 UTC | 1h 4m |
| N777WF |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-03-30 00:15 UTC | 2026-03-30 01:10 UTC | 55m |
| BRG652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-03-30 00:39 UTC | 2026-03-30 01:08 UTC | 28m |
| RKJ16 | RKJ | Austin-Bergstrom International Airport (KAUS) | NV13 (NV13) | 2026-03-29 22:18 UTC | 2026-03-30 01:05 UTC | 2h 47m |
| N25VR |  | Brown Field Municipal Airport (KSDM) | Aurora State Airport (KUAO) | 2026-03-29 22:53 UTC | 2026-03-30 00:59 UTC | 2h 6m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 00:22 UTC | 2026-03-30 00:58 UTC | 36m |
| ERU9 | ERU | Mc Clellan-Palomar Airport (KCRQ) | AZ86 (AZ86) | 2026-03-29 19:08 UTC | 2026-03-30 00:58 UTC | 5h 49m |
| BLKT07 | BLK | RAAF Base Edinburgh (YPED) | West Sale Airport (YWSL) | 2026-03-29 23:49 UTC | 2026-03-30 00:57 UTC | 1h 8m |
| N507ME |  | 9PN1 (9PN1) | Allegheny County Airport (KAGC) | 2026-03-30 00:45 UTC | 2026-03-30 00:56 UTC | 10m |
| N245DS |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-03-30 00:40 UTC | 2026-03-30 00:55 UTC | 15m |
| VT517 |  | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-03-29 23:59 UTC | 2026-03-30 00:53 UTC | 54m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-03-30 00:38 UTC | 2026-03-30 00:53 UTC | 15m |
| N1821 |  | KM33 (KM33) | John C Tune Airport (KJWN) | 2026-03-30 00:37 UTC | 2026-03-30 00:53 UTC | 15m |
| N139TJ |  | Wings Field (KLOM) | Northeast Philadelphia Airport (KPNE) | 2026-03-30 00:44 UTC | 2026-03-30 00:51 UTC | 6m |
| N946SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-03-30 00:50 UTC | 2026-03-30 00:51 UTC | 0m |
| AAL2987 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Okc Will Rogers International Airport (KOKC) | 2026-03-30 00:08 UTC | 2026-03-30 00:48 UTC | 39m |
| ANZ323L | ANZ | Wellington International Airport (NZWN) | Nelson Airport (NZNS) | 2026-03-30 00:20 UTC | 2026-03-30 00:47 UTC | 27m |
| CXK1037 | CXK | Sheboygan County Memorial International Airport (KSBM) | Dubuque Regional Airport (KDBQ) | 2026-03-29 23:09 UTC | 2026-03-30 00:46 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
