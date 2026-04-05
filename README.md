# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_06:15:54_UTC-green)

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

**Latest saved flight:** 2026-04-05 06:15:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 06:15:54 UTC

- **17,335** saved flights
- **9,038** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,335** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **217,727.5 tonnes** estimated CO2 emissions
- **12,621,885 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 693 |
| 3 | IndiGo | 493 |
| 4 | EJA | 328 |
| 5 | American Airlines | 322 |
| 6 | Southwest Airlines | 247 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 234 |
| 9 | Vueling | 190 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 168 |
| 12 | Delta Air Lines | 150 |
| 13 | LXJ | 149 |
| 14 | All Nippon Airways | 147 |
| 15 | QLK | 146 |
| 16 | VIV | 131 |
| 17 | AZU | 130 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 122 |
| 20 | United Airlines | 116 |
| 21 | Avianca | 113 |
| 22 | Japan Airlines | 113 |
| 23 | EJU | 109 |
| 24 | EDV | 108 |
| 25 | AEE | 107 |
| 26 | easyJet | 107 |
| 27 | AXB | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | Cathay Pacific | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13888 |
| 2 | 🇮🇳 IN | 1504 |
| 3 | 🇪🇸 ES | 1405 |
| 4 | 🇦🇺 AU | 1264 |
| 5 | 🇧🇷 BR | 998 |
| 6 | 🇯🇵 JP | 908 |
| 7 | 🇨🇴 CO | 905 |
| 8 | 🇩🇪 DE | 874 |
| 9 | 🇮🇹 IT | 793 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 664 |
| 12 | 🇫🇷 FR | 610 |
| 13 | 🇲🇽 MX | 608 |
| 14 | 🇬🇷 GR | 467 |
| 15 | 🇨🇭 CH | 446 |
| 16 | 🇳🇿 NZ | 394 |
| 17 | 🇲🇾 MY | 384 |
| 18 | 🇿🇦 ZA | 354 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 337 |
| 21 | 🇵🇭 PH | 334 |
| 22 | 🇹🇷 TR | 314 |
| 23 | 🇰🇷 KR | 302 |
| 24 | 🇹🇭 TH | 241 |
| 25 | 🇵🇱 PL | 239 |
| 26 | 🇲🇦 MA | 210 |
| 27 | 🇧🇸 BS | 191 |
| 28 | 🇮🇩 ID | 183 |
| 29 | 🇲🇴 MO | 182 |
| 30 | 🇲🇪 ME | 175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 419 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Denver International Airport |  | US | 327 |
| 4 | Indira Gandhi International Airport |  | IN | 313 |
| 5 | Tokyo International Airport |  | JP | 312 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 218 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 204 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 183 |
| 13 | Macau International Airport |  | MO | 182 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 167 |
| 18 | Charlotte/Douglas International Airport |  | US | 164 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 20 | Madrid Barajas International Airport |  | ES | 157 |
| 21 | Congonhas Airport |  | BR | 154 |
| 22 | Ninoy Aquino International Airport |  | PH | 152 |
| 23 | Tenerife Norte Airport |  | ES | 150 |
| 24 | Daniel K Inouye International Airport |  | US | 143 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 137 |
| 27 | Kuala Lumpur International Airport |  | MY | 136 |
| 28 | Reno/Tahoe International Airport |  | US | 135 |
| 29 | Malpensa International Airport |  | IT | 133 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 31 | Vitoria/Foronda Airport |  | ES | 127 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 120 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | Seattle-Tacoma International Airport |  | US | 113 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 77 | 1h 8m | 706 km | 937.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 64 | 24m | 225 km | 248.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 58 | 29m | 304 km | 304.1 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 50 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 48 | 16m | 206 km | 170.7 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 48 | 1h 27m | 910 km | 753.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 41 | 28m | 275 km | 194.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 39 | 19m | 165 km | 110.9 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 36 | 1h 11m | 770 km | 478.2 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 33 | 54m | 546 km | 310.7 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 30 | 46m | 452 km | 233.8 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N862YB |  | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-04-05 05:51 UTC | 2026-04-05 06:15 UTC | 24m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-05 05:53 UTC | 2026-04-05 06:04 UTC | 10m |
| UAE9658 | Emirates | Zaragoza Air Base (LEZG) | Macau International Airport (VMMC) | 2026-04-04 14:56 UTC | 2026-04-05 06:02 UTC | 15h 5m |
| FKT | FKT | Heck Field Airport (YHEC) | Sunshine Coast Airport (YBMC) | 2026-04-05 05:26 UTC | 2026-04-05 06:00 UTC | 34m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-05 05:30 UTC | 2026-04-05 05:54 UTC | 24m |
| N911DG |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-04-05 05:12 UTC | 2026-04-05 05:50 UTC | 37m |
| CLX4796 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-04 18:45 UTC | 2026-04-05 05:45 UTC | 10h 59m |
| WZZ9445 | Wizz Air | Larnaca International Airport (LCLK) | Gyumri Shirak Airport (UDSG) | 2026-04-05 03:41 UTC | 2026-04-05 05:42 UTC | 2h 1m |
| JST656 | JST | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 2026-04-05 04:09 UTC | 2026-04-05 05:30 UTC | 1h 21m |
| SKW3285 | SkyWest Airlines | Seattle-Tacoma International Airport (KSEA) | Bermuda Dunes Airport (KUDD) | 2026-04-05 03:12 UTC | 2026-04-05 05:29 UTC | 2h 16m |
| AAL3299 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Denver International Airport (KDEN) | 2026-04-05 02:22 UTC | 2026-04-05 05:28 UTC | 3h 5m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-04-05 04:38 UTC | 2026-04-05 05:25 UTC | 46m |
| BBC601 | BBC | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-04-05 05:09 UTC | 2026-04-05 05:25 UTC | 15m |
| WJA2051 | WJA | Cancun International Airport (MMUN) | Vancouver International Airport (CYVR) | 2026-04-04 23:05 UTC | 2026-04-05 05:25 UTC | 6h 19m |
| N986LF |  | Bartow Executive Airport (KBOW) | Bartow Executive Airport (KBOW) | 2026-04-05 05:18 UTC | 2026-04-05 05:21 UTC | 3m |
| ASL84H | ASL | Belgrade Nikola Tesla Airport (LYBE) | Niksic Airport (LYNK) | 2026-04-05 04:48 UTC | 2026-04-05 05:21 UTC | 33m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-05 04:50 UTC | 2026-04-05 05:21 UTC | 30m |
| EZS69AF | EZS | Mollis Airport (LSZM) | Zemunik Airport (LDZD) | 2026-04-05 04:23 UTC | 2026-04-05 05:19 UTC | 56m |
| VLG2UT | Vueling | Alicante International Airport (LEAL) | Vitoria/Foronda Airport (LEVT) | 2026-04-05 04:30 UTC | 2026-04-05 05:19 UTC | 49m |
| JAL481 | Japan Airlines | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-05 04:22 UTC | 2026-04-05 05:18 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
