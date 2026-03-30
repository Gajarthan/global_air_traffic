# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_23:18:47_UTC-green)

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

**Latest saved flight:** 2026-03-30 23:18:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 23:18:47 UTC

- **5,733** saved flights
- **3,892** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,733** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **72,585.4 tonnes** estimated CO2 emissions
- **4,207,847 km** total distance flown
- **874 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 304 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 139 |
| 4 | EJA | 127 |
| 5 | American Airlines | 118 |
| 6 | Southwest Airlines | 94 |
| 7 | ENY | 90 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 66 |
| 10 | AXM | 58 |
| 11 | LXJ | 55 |
| 12 | Vueling | 54 |
| 13 | Delta Air Lines | 53 |
| 14 | United Airlines | 46 |
| 15 | Cathay Pacific | 45 |
| 16 | VIV | 44 |
| 17 | WIF | 43 |
| 18 | AZU | 41 |
| 19 | All Nippon Airways | 39 |
| 20 | EDV | 39 |
| 21 | QLK | 38 |
| 22 | Swiss International | 38 |
| 23 | Japan Airlines | 37 |
| 24 | Alaska Airlines | 35 |
| 25 | Avianca | 35 |
| 26 | AXB | 34 |
| 27 | MXY | 31 |
| 28 | VOE | 31 |
| 29 | EJU | 30 |
| 30 | GLO | 29 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5150 |
| 2 | 🇮🇳 IN | 418 |
| 3 | 🇪🇸 ES | 407 |
| 4 | 🇦🇺 AU | 337 |
| 5 | 🇧🇷 BR | 305 |
| 6 | 🇨🇴 CO | 280 |
| 7 | 🇮🇹 IT | 263 |
| 8 | 🇯🇵 JP | 254 |
| 9 | 🇨🇦 CA | 249 |
| 10 | 🇩🇪 DE | 242 |
| 11 | 🇲🇽 MX | 217 |
| 12 | 🇬🇧 GB | 184 |
| 13 | 🇫🇷 FR | 170 |
| 14 | 🇳🇴 NO | 143 |
| 15 | 🇲🇾 MY | 128 |
| 16 | 🇬🇹 GT | 126 |
| 17 | 🇨🇭 CH | 125 |
| 18 | 🇿🇦 ZA | 123 |
| 19 | 🇬🇷 GR | 117 |
| 20 | 🇵🇭 PH | 113 |
| 21 | 🇳🇿 NZ | 95 |
| 22 | 🇹🇷 TR | 91 |
| 23 | 🇲🇴 MO | 73 |
| 24 | 🇹🇭 TH | 73 |
| 25 | 🇲🇦 MA | 67 |
| 26 | 🇵🇱 PL | 65 |
| 27 | 🇧🇸 BS | 60 |
| 28 | 🇮🇩 ID | 58 |
| 29 | 🇰🇷 KR | 52 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 158 |
| 2 | Denver International Airport |  | US | 120 |
| 3 | El Dorado International Airport |  | CO | 101 |
| 4 | Indira Gandhi International Airport |  | IN | 95 |
| 5 | La Aurora Airport |  | GT | 87 |
| 6 | Tokyo International Airport |  | JP | 85 |
| 7 | Frankfurt am Main International Airport |  | DE | 80 |
| 8 | Phoenix Sky Harbor International Airport |  | US | 73 |
| 9 | Macau International Airport |  | MO | 73 |
| 10 | Chicago O'Hare International Airport |  | US | 70 |
| 11 | Harry Reid International Airport |  | US | 69 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 13 | Zurich Airport |  | CH | 66 |
| 14 | Guaymaral Airport |  | CO | 65 |
| 15 | Tenerife Norte Airport |  | ES | 62 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 55 |
| 17 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 18 | Reno/Tahoe International Airport |  | US | 51 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 51 |
| 20 | Ninoy Aquino International Airport |  | PH | 50 |
| 21 | Charlotte/Douglas International Airport |  | US | 49 |
| 22 | Madrid Barajas International Airport |  | ES | 48 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 48 |
| 24 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 25 | Malpensa International Airport |  | IT | 46 |
| 26 | Miami International Airport |  | US | 46 |
| 27 | Bengaluru International Airport |  | IN | 46 |
| 28 | Salt Lake City International Airport |  | US | 46 |
| 29 | Kuala Lumpur International Airport |  | MY | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 44 |
| 31 | Congonhas Airport |  | BR | 44 |
| 32 | Centennial Airport |  | US | 42 |
| 33 | O. R. Tambo International Airport |  | ZA | 42 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 41 |
| 35 | Seattle-Tacoma International Airport |  | US | 41 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 37 | Los Angeles International Airport |  | US | 39 |
| 38 | Austin-Bergstrom International Airport |  | US | 39 |
| 39 | Vitoria/Foronda Airport |  | ES | 38 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 38 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 24 | 24m | 225 km | 93.1 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 17 | 1h 6m | 706 km | 207.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 15 | 15m | 206 km | 53.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 14 | 1h 51m | 1,156 km | 279.3 t |
| 11 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 14 | 30m | 369 km | 89.1 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 13 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 14 | 4m | - | - |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 18 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 11 | 28m | 304 km | 57.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 25 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 11 | 1h 56m | 1,304 km | 247.5 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 10 | 1h 2m | 723 km | 124.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 10 | 26m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KN42 |  | Norfolk Ns (Chambers Field) Airport (KNGU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-03-30 22:08 UTC | 2026-03-30 23:18 UTC | 1h 10m |
| N951TG |  | Sarasota/Bradenton International Airport (KSRQ) | Peter O Knight Airport (KTPF) | 2026-03-30 22:49 UTC | 2026-03-30 23:09 UTC | 20m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 22:40 UTC | 2026-03-30 23:09 UTC | 29m |
| URSA31 | URS | Eielson Afb Airport (PAEI) | Ladd Army Air Field (PAFB) | 2026-03-30 21:41 UTC | 2026-03-30 23:06 UTC | 1h 24m |
| UAL345 | United Airlines | Washington Dulles International Airport (KIAD) | Kawaihapai Airfield (PHDH) | 2026-03-30 12:59 UTC | 2026-03-30 23:00 UTC | 10h 1m |
| RDHK705 | RDH | Aberdeen Field (31VA) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-03-30 22:51 UTC | 2026-03-30 23:00 UTC | 9m |
| LYI | LYI | Gold Coast Airport (YBCG) | Lismore Airport (YLIS) | 2026-03-30 22:26 UTC | 2026-03-30 22:59 UTC | 33m |
| N545DS |  | Pearson Field (KVUO) | Portland-Hillsboro Airport (KHIO) | 2026-03-30 22:35 UTC | 2026-03-30 22:59 UTC | 23m |
| N850UW |  | 1WI9 (1WI9) | Dane County Regional/Truax Field (KMSN) | 2026-03-30 22:43 UTC | 2026-03-30 22:58 UTC | 15m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-03-30 21:48 UTC | 2026-03-30 22:55 UTC | 1h 7m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-03-30 12:06 UTC | 2026-03-30 22:52 UTC | 10h 45m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-03-30 22:29 UTC | 2026-03-30 22:50 UTC | 21m |
| OKC116 | OKC | Wiley Post Airport (KPWA) | KF29 (KF29) | 2026-03-30 21:54 UTC | 2026-03-30 22:46 UTC | 52m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-03-30 22:04 UTC | 2026-03-30 22:41 UTC | 37m |
| N56HV |  | San Carlos Airport (KSQL) | Rohnerville Airport (KFOT) | 2026-03-30 21:51 UTC | 2026-03-30 22:40 UTC | 49m |
| CXK654 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-03-30 21:37 UTC | 2026-03-30 22:37 UTC | 1h 0m |
| YTZ | YTZ | Caboolture Airport (YCAB) | Sunshine Coast Airport (YBMC) | 2026-03-30 22:22 UTC | 2026-03-30 22:37 UTC | 14m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-03-30 22:16 UTC | 2026-03-30 22:36 UTC | 20m |
| ERU5 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-03-30 22:30 UTC | 2026-03-30 22:36 UTC | 5m |
| N690RA |  | San Bernardino International Airport (KSBD) | Ontario International Airport (KONT) | 2026-03-30 21:46 UTC | 2026-03-30 22:35 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
