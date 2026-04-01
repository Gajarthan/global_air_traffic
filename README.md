# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_09:58:14_UTC-green)

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

**Latest saved flight:** 2026-04-01 09:58:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 09:58:14 UTC

- **8,401** saved flights
- **5,194** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,401** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **102,263.8 tonnes** estimated CO2 emissions
- **5,928,334 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 390 |
| 2 | Ryanair | 314 |
| 3 | IndiGo | 233 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 134 |
| 7 | Lufthansa | 128 |
| 8 | ENY | 116 |
| 9 | AXM | 97 |
| 10 | Vueling | 94 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | All Nippon Airways | 71 |
| 14 | Delta Air Lines | 71 |
| 15 | QLK | 70 |
| 16 | WIF | 64 |
| 17 | Swiss International | 59 |
| 18 | VIV | 59 |
| 19 | AXB | 58 |
| 20 | AZU | 57 |
| 21 | Japan Airlines | 57 |
| 22 | Alaska Airlines | 56 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | EJU | 47 |
| 28 | easyJet | 47 |
| 29 | Avianca | 46 |
| 30 | JST | 45 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7044 |
| 2 | 🇮🇳 IN | 715 |
| 3 | 🇦🇺 AU | 685 |
| 4 | 🇪🇸 ES | 638 |
| 5 | 🇩🇪 DE | 423 |
| 6 | 🇯🇵 JP | 422 |
| 7 | 🇧🇷 BR | 401 |
| 8 | 🇨🇦 CA | 391 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 368 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 283 |
| 13 | 🇫🇷 FR | 243 |
| 14 | 🇲🇾 MY | 215 |
| 15 | 🇳🇴 NO | 212 |
| 16 | 🇳🇿 NZ | 197 |
| 17 | 🇬🇷 GR | 196 |
| 18 | 🇨🇭 CH | 188 |
| 19 | 🇬🇹 GT | 172 |
| 20 | 🇿🇦 ZA | 171 |
| 21 | 🇵🇭 PH | 162 |
| 22 | 🇹🇷 TR | 144 |
| 23 | 🇰🇷 KR | 143 |
| 24 | 🇮🇩 ID | 112 |
| 25 | 🇹🇭 TH | 109 |
| 26 | 🇵🇱 PL | 98 |
| 27 | 🇲🇦 MA | 96 |
| 28 | 🇲🇴 MO | 86 |
| 29 | 🇲🇪 ME | 77 |
| 30 | 🇧🇸 BS | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 200 |
| 2 | Indira Gandhi International Airport |  | IN | 158 |
| 3 | Denver International Airport |  | US | 155 |
| 4 | Tokyo International Airport |  | JP | 150 |
| 5 | El Dorado International Airport |  | CO | 132 |
| 6 | Frankfurt am Main International Airport |  | DE | 129 |
| 7 | La Aurora Airport |  | GT | 121 |
| 8 | Harry Reid International Airport |  | US | 120 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 11 | Zurich Airport |  | CH | 94 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 91 |
| 13 | Guaymaral Airport |  | CO | 90 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 15 | Macau International Airport |  | MO | 86 |
| 16 | Chicago O'Hare International Airport |  | US | 84 |
| 17 | Bengaluru International Airport |  | IN | 79 |
| 18 | Tenerife Norte Airport |  | ES | 78 |
| 19 | Kuala Lumpur International Airport |  | MY | 78 |
| 20 | Reno/Tahoe International Airport |  | US | 77 |
| 21 | Madrid Barajas International Airport |  | ES | 74 |
| 22 | Ninoy Aquino International Airport |  | PH | 73 |
| 23 | Charlotte/Douglas International Airport |  | US | 71 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 67 |
| 26 | Daniel K Inouye International Airport |  | US | 66 |
| 27 | Malpensa International Airport |  | IT | 65 |
| 28 | Salt Lake City International Airport |  | US | 64 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 30 | Vitoria/Foronda Airport |  | ES | 62 |
| 31 | Pune Airport |  | IN | 62 |
| 32 | Seattle-Tacoma International Airport |  | US | 60 |
| 33 | Charles de Gaulle International Airport |  | FR | 58 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 35 | Barcelona International Airport |  | ES | 58 |
| 36 | Miami International Airport |  | US | 57 |
| 37 | Congonhas Airport |  | BR | 57 |
| 38 | Gimpo International Airport |  | KR | 54 |
| 39 | Bodø Airport |  | NO | 54 |
| 40 | Austin-Bergstrom International Airport |  | US | 53 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 34 | 1h 6m | 706 km | 414.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 28 | 29m | 304 km | 146.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 27 | 1h 44m | 1,156 km | 538.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 27 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 25 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 23 | 15m | 206 km | 81.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 23 | 20m | 165 km | 65.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 20 | 1h 26m | 910 km | 313.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 20 | 30m | 369 km | 127.3 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 18 | 53m | 546 km | 169.5 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 17 | 1h 0m | 723 km | 211.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 16 | 11m | 127 km | 35.0 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 13 | 35m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTN | YTN | Adelaide Parafield Airport (YPPF) | Maitland Airport (YMLD) | 2026-04-01 08:43 UTC | 2026-04-01 09:58 UTC | 1h 14m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-01 09:05 UTC | 2026-04-01 09:56 UTC | 50m |
| UPS474 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Montréal (Mirabel) Airport (CYMX) | 2026-04-01 08:21 UTC | 2026-04-01 09:55 UTC | 1h 34m |
| DAL144 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Amsterdam Airport Schiphol (EHAM) | 2026-04-01 00:42 UTC | 2026-04-01 09:43 UTC | 9h 0m |
| SUI787 | SUI | Bern Belp Airport (LSZB) | Emmen Airport (LSME) | 2026-04-01 09:14 UTC | 2026-04-01 09:36 UTC | 21m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-01 09:22 UTC | 2026-04-01 09:31 UTC | 9m |
| LICHEN3 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-01 08:33 UTC | 2026-04-01 09:24 UTC | 51m |
| ZFO | ZFO | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-01 09:03 UTC | 2026-04-01 09:22 UTC | 19m |
| VOE78RJ | VOE | Zaragoza Air Base (LEZG) | Menorca Airport (LEMH) | 2026-04-01 08:28 UTC | 2026-04-01 09:18 UTC | 49m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-04-01 08:48 UTC | 2026-04-01 09:12 UTC | 24m |
| AXM6044 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-01 08:51 UTC | 2026-04-01 09:10 UTC | 19m |
| SEH382 | SEH | Eleftherios Venizelos International Airport (LGAV) | Thessaloniki Macedonia International Airport (LGTS) | 2026-04-01 08:15 UTC | 2026-04-01 09:09 UTC | 53m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-01 08:28 UTC | 2026-04-01 09:09 UTC | 40m |
| EZY59ZF | easyJet | London Gatwick Airport (EGKK) | Naxos Airport (LGNX) | 2026-04-01 05:41 UTC | 2026-04-01 09:09 UTC | 3h 27m |
| EVY23 | EVY | Canberra International Airport (YSCB) | Wagga Wagga City Airport (YSWG) | 2026-04-01 08:49 UTC | 2026-04-01 09:07 UTC | 17m |
| DFKNO | DFK | St Gallen Altenrhein Airport (LSZR) | Stuttgart Airport (EDDS) | 2026-04-01 08:41 UTC | 2026-04-01 09:06 UTC | 24m |
| WZZ3EA | Wizz Air | Berlin Brandenburg Airport (EDDB) | Pristina International Airport (BKPR) | 2026-04-01 07:25 UTC | 2026-04-01 09:06 UTC | 1h 41m |
| SDM6355 | SDM | Pulkovo Airport (ULLI) | Astrakhan Airport (URWA) | 2026-04-01 06:16 UTC | 2026-04-01 09:04 UTC | 2h 48m |
| SWR4DK | Swiss International | Hannover Airport (EDDV) | Zurich Airport (LSZH) | 2026-04-01 08:08 UTC | 2026-04-01 09:02 UTC | 54m |
| SPADE10 | SPA | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-04-01 08:16 UTC | 2026-04-01 09:01 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
