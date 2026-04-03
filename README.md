# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_23:01:52_UTC-green)

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

**Latest saved flight:** 2026-04-03 23:01:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 23:01:52 UTC

- **14,700** saved flights
- **8,052** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,700** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **181,771.6 tonnes** estimated CO2 emissions
- **10,537,482 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 657 |
| 2 | Ryanair | 565 |
| 3 | IndiGo | 404 |
| 4 | EJA | 296 |
| 5 | American Airlines | 280 |
| 6 | Southwest Airlines | 216 |
| 7 | Lufthansa | 210 |
| 8 | ENY | 192 |
| 9 | LATAM Airlines | 157 |
| 10 | Vueling | 157 |
| 11 | AXM | 142 |
| 12 | LXJ | 132 |
| 13 | QLK | 127 |
| 14 | All Nippon Airways | 123 |
| 15 | Delta Air Lines | 120 |
| 16 | AZU | 115 |
| 17 | Swiss International | 111 |
| 18 | VIV | 108 |
| 19 | Alaska Airlines | 98 |
| 20 | United Airlines | 97 |
| 21 | WIF | 97 |
| 22 | Avianca | 93 |
| 23 | EDV | 93 |
| 24 | easyJet | 90 |
| 25 | AXB | 89 |
| 26 | Japan Airlines | 89 |
| 27 | AEE | 88 |
| 28 | EJU | 87 |
| 29 | BRC | 86 |
| 30 | Cathay Pacific | 85 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12000 |
| 2 | 🇮🇳 IN | 1230 |
| 3 | 🇪🇸 ES | 1111 |
| 4 | 🇦🇺 AU | 1108 |
| 5 | 🇧🇷 BR | 865 |
| 6 | 🇩🇪 DE | 757 |
| 7 | 🇨🇴 CO | 742 |
| 8 | 🇯🇵 JP | 731 |
| 9 | 🇨🇦 CA | 680 |
| 10 | 🇮🇹 IT | 628 |
| 11 | 🇬🇧 GB | 561 |
| 12 | 🇲🇽 MX | 513 |
| 13 | 🇫🇷 FR | 503 |
| 14 | 🇬🇷 GR | 391 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 353 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 269 |
| 21 | 🇬🇹 GT | 266 |
| 22 | 🇵🇭 PH | 265 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 202 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 179 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇧🇸 BS | 158 |
| 29 | 🇲🇴 MO | 157 |
| 30 | 🇲🇪 ME | 150 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 367 |
| 2 | El Dorado International Airport |  | CO | 278 |
| 3 | Denver International Airport |  | US | 270 |
| 4 | Indira Gandhi International Airport |  | IN | 261 |
| 5 | Tokyo International Airport |  | JP | 254 |
| 6 | Harry Reid International Airport |  | US | 201 |
| 7 | Frankfurt am Main International Airport |  | DE | 196 |
| 8 | La Aurora Airport |  | GT | 186 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 182 |
| 10 | Zurich Airport |  | CH | 175 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 165 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 164 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 152 |
| 16 | Chicago O'Hare International Airport |  | US | 145 |
| 17 | Bengaluru International Airport |  | IN | 140 |
| 18 | Charlotte/Douglas International Airport |  | US | 139 |
| 19 | Congonhas Airport |  | BR | 134 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 132 |
| 21 | Madrid Barajas International Airport |  | ES | 127 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Salt Lake City International Airport |  | US | 116 |
| 25 | Tenerife Norte Airport |  | ES | 114 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 114 |
| 27 | Reno/Tahoe International Airport |  | US | 113 |
| 28 | Vitoria/Foronda Airport |  | ES | 111 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 30 | Daniel K Inouye International Airport |  | US | 109 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 33 | Malpensa International Airport |  | IT | 103 |
| 34 | Austin-Bergstrom International Airport |  | US | 100 |
| 35 | Pune Airport |  | IN | 99 |
| 36 | Barcelona International Airport |  | ES | 97 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 97 |
| 38 | Seattle-Tacoma International Airport |  | US | 96 |
| 39 | Miami International Airport |  | US | 95 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 93 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 68 | 14m | 114 km | 133.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 35 | 15m | 206 km | 124.4 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 28 | 1h 10m | 770 km | 372.0 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KLW | KLW | Sunshine Coast Airport (YBMC) | Tangalooma Airport (YTGA) | 2026-04-03 22:36 UTC | 2026-04-03 23:01 UTC | 25m |
| N9463K |  | Allentown Queen City Municipal Airport (KXLL) | Quakertown Airport (KUKT) | 2026-04-03 22:42 UTC | 2026-04-03 23:01 UTC | 19m |
| N528SV |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-03 22:46 UTC | 2026-04-03 23:00 UTC | 13m |
| N74426 |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-04-03 22:11 UTC | 2026-04-03 22:55 UTC | 43m |
| N403AP |  | Limberlost Ranch Airport (CA21) | Limberlost Ranch Airport (CA21) | 2026-04-03 22:02 UTC | 2026-04-03 22:54 UTC | 52m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-03 22:12 UTC | 2026-04-03 22:43 UTC | 31m |
| EJA454 | EJA | George Bush Intcntl/Houston Airport (KIAH) | Flying B Ranch Airstrip (35TX) | 2026-04-03 21:50 UTC | 2026-04-03 22:42 UTC | 51m |
| N289KC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-03 22:19 UTC | 2026-04-03 22:41 UTC | 22m |
| N7190C |  | Chandler Municipal Airport (KCHD) | Pegasus Airpark (5AZ3) | 2026-04-03 22:28 UTC | 2026-04-03 22:39 UTC | 10m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-03 22:30 UTC | 2026-04-03 22:38 UTC | 7m |
| N353HP |  | Salt Lake City International Airport (KSLC) | K36U (K36U) | 2026-04-03 22:25 UTC | 2026-04-03 22:37 UTC | 11m |
| N878EM |  | John Wayne/Orange County Airport (KSNA) | Napa County Airport (KAPC) | 2026-04-03 21:34 UTC | 2026-04-03 22:36 UTC | 1h 1m |
| N15CH |  | Orlando Apopka Airport (KX04) | Winter Haven Regional Airport (KGIF) | 2026-04-03 21:54 UTC | 2026-04-03 22:32 UTC | 37m |
| N113AH |  | Hartsfield/Jackson Atlanta International Airport (KATL) | Rollins Airport (GA53) | 2026-04-03 22:19 UTC | 2026-04-03 22:32 UTC | 12m |
| N88CB |  | Phoenix Deer Valley Airport (KDVT) | Chapman Ranch Airstrip (58AZ) | 2026-04-03 22:09 UTC | 2026-04-03 22:32 UTC | 22m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-03 22:19 UTC | 2026-04-03 22:31 UTC | 12m |
| JPL5 | JPL | Boeing Field/King County International Airport (KBFI) | Van Nuys Airport (KVNY) | 2026-04-03 20:31 UTC | 2026-04-03 22:29 UTC | 1h 58m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-04-03 21:31 UTC | 2026-04-03 22:29 UTC | 58m |
| BULET47 | BUL | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-04-03 22:05 UTC | 2026-04-03 22:29 UTC | 24m |
| N6132J |  | Westfield-Barnes Regional Airport (KBAF) | Northampton Airport (K7B2) | 2026-04-03 22:17 UTC | 2026-04-03 22:26 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
