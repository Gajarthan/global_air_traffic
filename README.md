# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_05:04:42_UTC-green)

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

**Latest saved flight:** 2026-04-02 05:04:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 05:04:42 UTC

- **10,236** saved flights
- **6,050** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,236** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **124,716.4 tonnes** estimated CO2 emissions
- **7,229,936 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 469 |
| 2 | Ryanair | 384 |
| 3 | IndiGo | 270 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 163 |
| 8 | ENY | 139 |
| 9 | AXM | 108 |
| 10 | Vueling | 106 |
| 11 | LATAM Airlines | 104 |
| 12 | LXJ | 100 |
| 13 | All Nippon Airways | 88 |
| 14 | Delta Air Lines | 86 |
| 15 | QLK | 85 |
| 16 | WIF | 80 |
| 17 | Swiss International | 73 |
| 18 | VIV | 72 |
| 19 | AZU | 71 |
| 20 | Alaska Airlines | 70 |
| 21 | EDV | 66 |
| 22 | United Airlines | 65 |
| 23 | AXB | 64 |
| 24 | Japan Airlines | 63 |
| 25 | Avianca | 60 |
| 26 | Cathay Pacific | 60 |
| 27 | BRC | 58 |
| 28 | easyJet | 57 |
| 29 | EJU | 55 |
| 30 | ANZ | 54 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8526 |
| 2 | 🇮🇳 IN | 826 |
| 3 | 🇦🇺 AU | 821 |
| 4 | 🇪🇸 ES | 766 |
| 5 | 🇧🇷 BR | 534 |
| 6 | 🇩🇪 DE | 529 |
| 7 | 🇨🇴 CO | 524 |
| 8 | 🇨🇦 CA | 505 |
| 9 | 🇯🇵 JP | 500 |
| 10 | 🇮🇹 IT | 438 |
| 11 | 🇲🇽 MX | 377 |
| 12 | 🇬🇧 GB | 353 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇳🇿 NZ | 255 |
| 16 | 🇲🇾 MY | 241 |
| 17 | 🇬🇷 GR | 231 |
| 18 | 🇨🇭 CH | 225 |
| 19 | 🇬🇹 GT | 209 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 192 |
| 22 | 🇰🇷 KR | 165 |
| 23 | 🇹🇷 TR | 163 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 125 |
| 26 | 🇹🇭 TH | 118 |
| 27 | 🇲🇦 MA | 117 |
| 28 | 🇲🇴 MO | 108 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Denver International Airport |  | US | 188 |
| 3 | Indira Gandhi International Airport |  | IN | 183 |
| 4 | Tokyo International Airport |  | JP | 179 |
| 5 | El Dorado International Airport |  | CO | 173 |
| 6 | Frankfurt am Main International Airport |  | DE | 166 |
| 7 | Guaymaral Airport |  | CO | 148 |
| 8 | Harry Reid International Airport |  | US | 147 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 124 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 119 |
| 12 | Zurich Airport |  | CH | 113 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 112 |
| 14 | Macau International Airport |  | MO | 108 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Reno/Tahoe International Airport |  | US | 94 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 92 |
| 19 | Charlotte/Douglas International Airport |  | US | 92 |
| 20 | Tenerife Norte Airport |  | ES | 92 |
| 21 | Madrid Barajas International Airport |  | ES | 91 |
| 22 | Kuala Lumpur International Airport |  | MY | 90 |
| 23 | Bengaluru International Airport |  | IN | 88 |
| 24 | Ninoy Aquino International Airport |  | PH | 87 |
| 25 | Congonhas Airport |  | BR | 81 |
| 26 | Daniel K Inouye International Airport |  | US | 79 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 76 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 76 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 30 | Salt Lake City International Airport |  | US | 75 |
| 31 | Malpensa International Airport |  | IT | 73 |
| 32 | Austin-Bergstrom International Airport |  | US | 72 |
| 33 | Seattle-Tacoma International Airport |  | US | 72 |
| 34 | Vitoria/Foronda Airport |  | ES | 71 |
| 35 | Pune Airport |  | IN | 71 |
| 36 | Charles de Gaulle International Airport |  | FR | 69 |
| 37 | Barcelona International Airport |  | ES | 69 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | Calgary International Airport |  | CA | 67 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 65 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 44 | 1h 7m | 706 km | 535.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 36 | 24m | 225 km | 139.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 31 | 30m | 304 km | 162.5 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 31 | 1h 44m | 1,156 km | 618.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 28 | 20m | 165 km | 79.6 t |
| 12 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 28 | 53m | 556 km | 268.4 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 26 | 15m | 206 km | 92.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 25 | 1h 26m | 910 km | 392.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 24 | 30m | 369 km | 152.8 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 21 | 53m | 546 km | 197.7 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 20 | 1h 55m | 1,304 km | 449.9 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 22 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 19 | 1h 10m | 770 km | 252.4 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 18 | 11m | 127 km | 39.4 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 16 | 32m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 15 | 1h 17m | 924 km | 239.2 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 15 | 17m | 183 km | 47.3 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N708SH |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-04-02 04:37 UTC | 2026-04-02 05:04 UTC | 27m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-02 00:47 UTC | 2026-04-02 04:58 UTC | 4h 10m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-01 14:22 UTC | 2026-04-02 04:56 UTC | 14h 33m |
| LXJ338 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | Austin-Bergstrom International Airport (KAUS) | 2026-04-02 01:44 UTC | 2026-04-02 04:56 UTC | 3h 11m |
| AXB1518 | AXB | Shillong Airport (VEBI) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-02 03:53 UTC | 2026-04-02 04:48 UTC | 54m |
| CTN3T | CTN | Pula Airport (LDPL) | Sepurine Training Base (LD57) | 2026-04-02 04:09 UTC | 2026-04-02 04:23 UTC | 13m |
| EDV4714 | EDV | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Wall Municipal Airport (K6V4) | 2026-04-02 03:16 UTC | 2026-04-02 04:22 UTC | 1h 5m |
| CCA166 | Air China | Melbourne International Airport (YMML) | Macau International Airport (VMMC) | 2026-04-01 09:44 UTC | 2026-04-02 04:21 UTC | 18h 37m |
| N705SG |  | Phoenix Sky Harbor International Airport (KPHX) | Hansen Airport (11CL) | 2026-04-02 03:28 UTC | 2026-04-02 04:21 UTC | 52m |
| N106GR |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-04-02 04:03 UTC | 2026-04-02 04:19 UTC | 16m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-01 16:48 UTC | 2026-04-02 04:12 UTC | 11h 24m |
| N8VB |  | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-04-02 03:20 UTC | 2026-04-02 04:12 UTC | 51m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-02 03:44 UTC | 2026-04-02 04:09 UTC | 25m |
| N249CP |  | Lubbock Preston Smith International Airport (KLBB) | Grant Besley Airport (NM03) | 2026-04-02 03:23 UTC | 2026-04-02 04:08 UTC | 44m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-02 03:00 UTC | 2026-04-02 04:06 UTC | 1h 6m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-02 03:42 UTC | 2026-04-02 04:03 UTC | 21m |
| HS7198 |  | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-04-02 04:03 UTC | 2026-04-02 04:03 UTC | 0m |
| N395CF |  | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-04-02 03:39 UTC | 2026-04-02 03:59 UTC | 19m |
| IGO564E | IndiGo | Indira Gandhi International Airport (VIDP) | Dehradun Airport (VIDN) | 2026-04-02 03:38 UTC | 2026-04-02 03:58 UTC | 20m |
| SWA3770 | Southwest Airlines | Long Beach (Daugherty Field) Airport (KLGB) | Reno/Tahoe International Airport (KRNO) | 2026-04-02 03:04 UTC | 2026-04-02 03:58 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
