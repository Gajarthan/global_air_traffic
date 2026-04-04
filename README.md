# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_06:31:08_UTC-green)

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

**Latest saved flight:** 2026-04-04 06:31:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 06:31:08 UTC

- **15,032** saved flights
- **8,166** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,032** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **186,014.1 tonnes** estimated CO2 emissions
- **10,783,427 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 567 |
| 3 | IndiGo | 425 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 211 |
| 8 | ENY | 196 |
| 9 | LATAM Airlines | 161 |
| 10 | Vueling | 157 |
| 11 | AXM | 147 |
| 12 | QLK | 137 |
| 13 | LXJ | 134 |
| 14 | All Nippon Airways | 128 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 115 |
| 17 | Swiss International | 111 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | United Airlines | 98 |
| 21 | Japan Airlines | 97 |
| 22 | WIF | 97 |
| 23 | Avianca | 95 |
| 24 | EDV | 93 |
| 25 | AEE | 92 |
| 26 | AXB | 92 |
| 27 | easyJet | 90 |
| 28 | BRC | 87 |
| 29 | Cathay Pacific | 87 |
| 30 | EJU | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12245 |
| 2 | 🇮🇳 IN | 1289 |
| 3 | 🇦🇺 AU | 1182 |
| 4 | 🇪🇸 ES | 1116 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 777 |
| 7 | 🇩🇪 DE | 765 |
| 8 | 🇨🇴 CO | 752 |
| 9 | 🇨🇦 CA | 692 |
| 10 | 🇮🇹 IT | 631 |
| 11 | 🇬🇧 GB | 566 |
| 12 | 🇲🇽 MX | 523 |
| 13 | 🇫🇷 FR | 504 |
| 14 | 🇬🇷 GR | 402 |
| 15 | 🇳🇿 NZ | 377 |
| 16 | 🇨🇭 CH | 376 |
| 17 | 🇲🇾 MY | 329 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 301 |
| 20 | 🇵🇭 PH | 286 |
| 21 | 🇹🇷 TR | 281 |
| 22 | 🇬🇹 GT | 267 |
| 23 | 🇰🇷 KR | 255 |
| 24 | 🇵🇱 PL | 204 |
| 25 | 🇹🇭 TH | 200 |
| 26 | 🇲🇦 MA | 179 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇧🇸 BS | 159 |
| 29 | 🇲🇴 MO | 158 |
| 30 | 🇲🇪 ME | 151 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 374 |
| 2 | El Dorado International Airport |  | CO | 283 |
| 3 | Denver International Airport |  | US | 280 |
| 4 | Indira Gandhi International Airport |  | IN | 273 |
| 5 | Tokyo International Airport |  | JP | 269 |
| 6 | Harry Reid International Airport |  | US | 212 |
| 7 | Frankfurt am Main International Airport |  | DE | 197 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 188 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 176 |
| 11 | Zurich Airport |  | CH | 175 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 158 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Chicago O'Hare International Airport |  | US | 147 |
| 17 | Bengaluru International Airport |  | IN | 144 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 20 | Congonhas Airport |  | BR | 135 |
| 21 | Ninoy Aquino International Airport |  | PH | 130 |
| 22 | Madrid Barajas International Airport |  | ES | 129 |
| 23 | Reno/Tahoe International Airport |  | US | 121 |
| 24 | Salt Lake City International Airport |  | US | 121 |
| 25 | Kuala Lumpur International Airport |  | MY | 119 |
| 26 | Daniel K Inouye International Airport |  | US | 118 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 118 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 29 | Tenerife Norte Airport |  | ES | 114 |
| 30 | Vitoria/Foronda Airport |  | ES | 111 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 33 | Malpensa International Airport |  | IT | 103 |
| 34 | Austin-Bergstrom International Airport |  | US | 102 |
| 35 | Pune Airport |  | IN | 102 |
| 36 | Seattle-Tacoma International Airport |  | US | 98 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 38 | Barcelona International Airport |  | ES | 97 |
| 39 | Miami International Airport |  | US | 96 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 95 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 65 | 1h 7m | 706 km | 791.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 57 | 24m | 225 km | 221.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 47 | 29m | 304 km | 246.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 42 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 40 | 1h 26m | 910 km | 627.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 31 | 30m | 369 km | 197.3 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 29 | 1h 10m | 770 km | 385.2 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 26 | 23m | 252 km | 112.9 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 23 | 45m | 452 km | 179.3 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 30 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 21 | 17m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KAL908 | Korean Air | London Heathrow Airport (EGLL) | Incheon International Airport (RKSI) | 2026-04-03 18:57 UTC | 2026-04-04 06:31 UTC | 11h 33m |
| N541LC |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-04-04 05:56 UTC | 2026-04-04 06:08 UTC | 11m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 05:46 UTC | 2026-04-04 05:58 UTC | 11m |
| CGEAJ | CGE | Pecs-Pogany Airport (LHPP) | Sarmellek International Airport (LHSM) | 2026-04-04 04:32 UTC | 2026-04-04 05:53 UTC | 1h 20m |
| JST827 | JST | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-04 04:32 UTC | 2026-04-04 05:41 UTC | 1h 9m |
| XSN06 | XSN | Sacramento Executive Airport (KSAC) | San Carlos Airport (KSQL) | 2026-04-04 05:17 UTC | 2026-04-04 05:38 UTC | 21m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Otocac Airport (LDRO) | 2026-04-04 04:42 UTC | 2026-04-04 05:38 UTC | 55m |
| AEE270 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-04 05:14 UTC | 2026-04-04 05:37 UTC | 23m |
| IGO146 | IndiGo | Chandigarh Airport (VICG) | Yongphulla Airport (VQ10) | 2026-04-04 02:00 UTC | 2026-04-04 05:36 UTC | 3h 35m |
| UBG145 | UBG | VGZR (VGZR) | Cox's Bazar Airport (VGCB) | 2026-04-04 04:51 UTC | 2026-04-04 05:34 UTC | 43m |
| DLH9KX | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-04-04 04:43 UTC | 2026-04-04 05:29 UTC | 46m |
| WMT7500 | WMT | Sibiu International Airport (LRSB) | Brussels South Charleroi Airport (EBCI) | 2026-04-04 03:17 UTC | 2026-04-04 05:26 UTC | 2h 9m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-04 05:06 UTC | 2026-04-04 05:26 UTC | 19m |
| N852AL |  | Butte Valley Airport (KA32) | Longbell Ranch Airport (2CL3) | 2026-04-04 05:07 UTC | 2026-04-04 05:25 UTC | 18m |
| FD542 |  | Adelaide International Airport (YPAD) | Waikerie Airport (YWKI) | 2026-04-04 05:02 UTC | 2026-04-04 05:25 UTC | 22m |
| EWG59Y | EWG | Cologne Bonn Airport (EDDK) | Vlora Internationa Airport (LAVL) | 2026-04-04 03:34 UTC | 2026-04-04 05:24 UTC | 1h 49m |
| JST656 | JST | Brisbane International Airport (YBBN) | Canberra International Airport (YSCB) | 2026-04-04 04:05 UTC | 2026-04-04 05:24 UTC | 1h 18m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 05:10 UTC | 2026-04-04 05:20 UTC | 10m |
| EZS21MA | EZS | Mollis Airport (LSZM) | Figari Sud-Corse Airport (LFKF) | 2026-04-04 04:18 UTC | 2026-04-04 05:20 UTC | 1h 1m |
| JAL481 | Japan Airlines | Tokyo International Airport (RJTT) | Takamatsu Airport (RJOT) | 2026-04-04 04:30 UTC | 2026-04-04 05:20 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
