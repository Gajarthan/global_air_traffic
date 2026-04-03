# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_06:17:38_UTC-green)

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

**Latest saved flight:** 2026-04-03 06:17:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 06:17:38 UTC

- **12,705** saved flights
- **7,203** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,705** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **158,170.8 tonnes** estimated CO2 emissions
- **9,169,321 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 482 |
| 3 | IndiGo | 339 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 132 |
| 10 | LATAM Airlines | 129 |
| 11 | AXM | 126 |
| 12 | QLK | 118 |
| 13 | LXJ | 117 |
| 14 | All Nippon Airways | 111 |
| 15 | Delta Air Lines | 101 |
| 16 | Swiss International | 96 |
| 17 | AZU | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 85 |
| 21 | Cathay Pacific | 85 |
| 22 | United Airlines | 84 |
| 23 | AXB | 82 |
| 24 | Japan Airlines | 81 |
| 25 | EDV | 78 |
| 26 | easyJet | 77 |
| 27 | EJU | 73 |
| 28 | BRC | 72 |
| 29 | ANZ | 71 |
| 30 | Avianca | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10340 |
| 2 | 🇮🇳 IN | 1050 |
| 3 | 🇦🇺 AU | 1030 |
| 4 | 🇪🇸 ES | 958 |
| 5 | 🇧🇷 BR | 709 |
| 6 | 🇩🇪 DE | 674 |
| 7 | 🇯🇵 JP | 650 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 601 |
| 10 | 🇮🇹 IT | 562 |
| 11 | 🇬🇧 GB | 469 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 399 |
| 14 | 🇬🇷 GR | 315 |
| 15 | 🇳🇿 NZ | 314 |
| 16 | 🇳🇴 NO | 301 |
| 17 | 🇨🇭 CH | 301 |
| 18 | 🇲🇾 MY | 286 |
| 19 | 🇵🇭 PH | 244 |
| 20 | 🇿🇦 ZA | 237 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇹🇷 TR | 219 |
| 23 | 🇰🇷 KR | 217 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 161 |
| 26 | 🇲🇴 MO | 154 |
| 27 | 🇮🇩 ID | 153 |
| 28 | 🇲🇦 MA | 146 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 124 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Denver International Airport |  | US | 233 |
| 3 | Tokyo International Airport |  | JP | 226 |
| 4 | Indira Gandhi International Airport |  | IN | 222 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 185 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Macau International Airport |  | MO | 154 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 154 |
| 11 | Guaymaral Airport |  | CO | 153 |
| 12 | Zurich Airport |  | CH | 149 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 143 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Chicago O'Hare International Airport |  | US | 123 |
| 17 | Bengaluru International Airport |  | IN | 118 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 19 | Charlotte/Douglas International Airport |  | US | 112 |
| 20 | Ninoy Aquino International Airport |  | PH | 110 |
| 21 | Congonhas Airport |  | BR | 109 |
| 22 | Madrid Barajas International Airport |  | ES | 108 |
| 23 | Kuala Lumpur International Airport |  | MY | 108 |
| 24 | Tenerife Norte Airport |  | ES | 106 |
| 25 | Salt Lake City International Airport |  | US | 98 |
| 26 | Reno/Tahoe International Airport |  | US | 97 |
| 27 | Daniel K Inouye International Airport |  | US | 95 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 95 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 95 |
| 30 | Vitoria/Foronda Airport |  | ES | 92 |
| 31 | Malpensa International Airport |  | IT | 91 |
| 32 | Barcelona International Airport |  | ES | 89 |
| 33 | Charles de Gaulle International Airport |  | FR | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 35 | Austin-Bergstrom International Airport |  | US | 85 |
| 36 | Seattle-Tacoma International Airport |  | US | 85 |
| 37 | Pune Airport |  | IN | 84 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Miami International Airport |  | US | 79 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 78 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 53 | 1h 7m | 706 km | 645.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 47 | 24m | 225 km | 182.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 41 | 29m | 304 km | 214.9 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 36 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 32 | 1h 26m | 910 km | 502.2 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 28 | 53m | 546 km | 263.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 27 | 30m | 369 km | 171.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 24 | 1h 10m | 770 km | 318.8 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 22 | 23m | 252 km | 95.5 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 21 | 1h 0m | 723 km | 261.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 20 | 20m | 147 km | 50.6 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 19 | 44m | 452 km | 148.1 t |
| 28 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 18 | 1h 16m | 924 km | 287.1 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFT3885 | FFT | Dallas-Fort Worth International Airport (KDFW) | Harry Reid International Airport (KLAS) | 2026-04-03 03:44 UTC | 2026-04-03 06:17 UTC | 2h 33m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-04-03 06:00 UTC | 2026-04-03 06:15 UTC | 14m |
| BTN700 | BTN | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-03 06:01 UTC | 2026-04-03 06:13 UTC | 12m |
| VLG8BA | Vueling | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 2026-04-03 05:23 UTC | 2026-04-03 06:13 UTC | 50m |
| HBZYJ | HBZ | Saanen Airport (LSGK) | Sion Airport (LSGS) | 2026-04-03 05:44 UTC | 2026-04-03 06:12 UTC | 27m |
| OAL062 | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-03 05:35 UTC | 2026-04-03 05:56 UTC | 20m |
| TKJ5201 | TKJ | Trabzon International Airport (LTCG) | Yalova Airport (LTBP) | 2026-04-03 04:32 UTC | 2026-04-03 05:48 UTC | 1h 16m |
| GUEPT2 | GUE | Faa'a International Airport (NTAA) | Faa'a International Airport (NTAA) | 2026-04-03 05:19 UTC | 2026-04-03 05:36 UTC | 17m |
| COLT64 | COL | Gifu Airport (RJNG) | Tajima Airport (RJBT) | 2026-04-03 05:20 UTC | 2026-04-03 05:36 UTC | 16m |
| ITY2014 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Linate Airport (LIML) | 2026-04-03 04:48 UTC | 2026-04-03 05:36 UTC | 48m |
| AEE372 | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-03 05:12 UTC | 2026-04-03 05:31 UTC | 19m |
| AXB1518 | AXB | Lokpriya Gopinath Bordoloi International Airport (VEGT) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-03 04:28 UTC | 2026-04-03 05:31 UTC | 1h 2m |
| AWA473 | AWA | VGZR (VGZR) | Balurghat Airport (VEBG) | 2026-04-03 04:52 UTC | 2026-04-03 05:30 UTC | 38m |
| CFL08 | CFL | Wellington International Airport (NZWN) | Wellington International Airport (NZWN) | 2026-04-03 05:18 UTC | 2026-04-03 05:29 UTC | 11m |
| N640HC |  | Okc Will Rogers International Airport (KOKC) | Holley Mountain Airpark (K2A2) | 2026-04-03 04:50 UTC | 2026-04-03 05:28 UTC | 37m |
| ANZ856M | ANZ | Christchurch International Airport (NZCH) | Lake Station Airport (NZLE) | 2026-04-03 04:59 UTC | 2026-04-03 05:27 UTC | 27m |
| FDA525 | FDA | Fukuoka Airport (RJFF) | Yamagata Airport (RJSC) | 2026-04-03 04:11 UTC | 2026-04-03 05:25 UTC | 1h 13m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-03 05:04 UTC | 2026-04-03 05:23 UTC | 19m |
| N149AH |  | Rimes Lakecrest Airport (35FA) | Orlando Executive Airport (KORL) | 2026-04-03 04:40 UTC | 2026-04-03 05:22 UTC | 42m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-04-03 05:07 UTC | 2026-04-03 05:21 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
