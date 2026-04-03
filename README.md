# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_20:40:01_UTC-green)

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

**Latest saved flight:** 2026-04-03 20:40:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 20:40:01 UTC

- **14,346** saved flights
- **7,900** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,346** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **177,482.5 tonnes** estimated CO2 emissions
- **10,288,843 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 622 |
| 2 | Ryanair | 551 |
| 3 | IndiGo | 403 |
| 4 | EJA | 285 |
| 5 | American Airlines | 270 |
| 6 | Lufthansa | 210 |
| 7 | Southwest Airlines | 209 |
| 8 | ENY | 187 |
| 9 | Vueling | 154 |
| 10 | LATAM Airlines | 150 |
| 11 | AXM | 142 |
| 12 | LXJ | 129 |
| 13 | All Nippon Airways | 123 |
| 14 | QLK | 123 |
| 15 | AZU | 114 |
| 16 | Delta Air Lines | 114 |
| 17 | Swiss International | 110 |
| 18 | VIV | 104 |
| 19 | WIF | 97 |
| 20 | Alaska Airlines | 93 |
| 21 | United Airlines | 92 |
| 22 | AXB | 89 |
| 23 | easyJet | 89 |
| 24 | Japan Airlines | 89 |
| 25 | AEE | 87 |
| 26 | EDV | 87 |
| 27 | EJU | 87 |
| 28 | Cathay Pacific | 85 |
| 29 | BRC | 84 |
| 30 | Avianca | 83 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11550 |
| 2 | 🇮🇳 IN | 1227 |
| 3 | 🇪🇸 ES | 1101 |
| 4 | 🇦🇺 AU | 1082 |
| 5 | 🇧🇷 BR | 844 |
| 6 | 🇩🇪 DE | 755 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 701 |
| 9 | 🇨🇦 CA | 659 |
| 10 | 🇮🇹 IT | 622 |
| 11 | 🇬🇧 GB | 553 |
| 12 | 🇫🇷 FR | 502 |
| 13 | 🇲🇽 MX | 500 |
| 14 | 🇬🇷 GR | 388 |
| 15 | 🇨🇭 CH | 373 |
| 16 | 🇳🇿 NZ | 329 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 265 |
| 21 | 🇬🇹 GT | 265 |
| 22 | 🇵🇭 PH | 265 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 199 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 173 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 155 |
| 30 | 🇲🇪 ME | 149 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 352 |
| 2 | Indira Gandhi International Airport |  | IN | 260 |
| 3 | Denver International Airport |  | US | 256 |
| 4 | El Dorado International Airport |  | CO | 255 |
| 5 | Tokyo International Airport |  | JP | 253 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 194 |
| 8 | La Aurora Airport |  | GT | 185 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 180 |
| 10 | Zurich Airport |  | CH | 174 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 158 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 140 |
| 16 | Bengaluru International Airport |  | IN | 140 |
| 17 | Chicago O'Hare International Airport |  | US | 138 |
| 18 | Charlotte/Douglas International Airport |  | US | 131 |
| 19 | Congonhas Airport |  | BR | 131 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 128 |
| 21 | Madrid Barajas International Airport |  | ES | 125 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 114 |
| 25 | Salt Lake City International Airport |  | US | 112 |
| 26 | Vitoria/Foronda Airport |  | ES | 111 |
| 27 | Reno/Tahoe International Airport |  | US | 110 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 107 |
| 30 | Daniel K Inouye International Airport |  | US | 104 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | Malpensa International Airport |  | IT | 102 |
| 33 | Pune Airport |  | IN | 98 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 98 |
| 35 | Austin-Bergstrom International Airport |  | US | 96 |
| 36 | Barcelona International Airport |  | ES | 96 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 93 |
| 38 | Miami International Airport |  | US | 92 |
| 39 | Seattle-Tacoma International Airport |  | US | 92 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 90 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 66 | 14m | 114 km | 129.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 30 | 1h 55m | 1,304 km | 674.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 19 | 30m | 213 km | 69.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-03 20:28 UTC | 2026-04-03 20:40 UTC | 11m |
| N302VM |  | Montgomery County Airpark (KGAI) | Carroll County Regional/Jack B Poage Field (KDMW) | 2026-04-03 19:39 UTC | 2026-04-03 20:36 UTC | 56m |
| N810W |  | North Exuma Airport (85FA) | 46FD (46FD) | 2026-04-03 20:14 UTC | 2026-04-03 20:34 UTC | 20m |
| N17PJ |  | James M Cox Dayton International Airport (KDAY) | Capital City Airport (KCXY) | 2026-04-03 19:33 UTC | 2026-04-03 20:32 UTC | 58m |
| CXK413 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Thrifts Airport (FL11) | 2026-04-03 19:06 UTC | 2026-04-03 20:24 UTC | 1h 17m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-03 20:13 UTC | 2026-04-03 20:24 UTC | 11m |
| N6078F |  | Scottsdale Airport (KSDL) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 19:08 UTC | 2026-04-03 20:22 UTC | 1h 14m |
| ASI934 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 19:24 UTC | 2026-04-03 20:21 UTC | 57m |
| BRCAT10 | BRC | Roswell Air Center Airport (KROW) | 81NM (81NM) | 2026-04-03 19:33 UTC | 2026-04-03 20:18 UTC | 45m |
| N968RC |  | San Martin Airport (KE16) | San Martin Airport (KE16) | 2026-04-03 20:05 UTC | 2026-04-03 20:16 UTC | 10m |
| N704LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Wemmering Airport (57VA) | 2026-04-03 19:22 UTC | 2026-04-03 20:10 UTC | 47m |
| N5253A |  | Stahl's Mountain Airport (3PN7) | Valley View Airport (7NK0) | 2026-04-03 18:44 UTC | 2026-04-03 20:10 UTC | 1h 25m |
| N38809 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-04-03 19:33 UTC | 2026-04-03 20:08 UTC | 34m |
| N501JM |  | Ryan Aerodrome (7TX7) | K54F (K54F) | 2026-04-03 19:52 UTC | 2026-04-03 20:08 UTC | 15m |
| N21131 |  | K8A0 (K8A0) | K8A0 (K8A0) | 2026-04-03 20:03 UTC | 2026-04-03 20:05 UTC | 1m |
| N11EF |  | James M Cox Dayton International Airport (KDAY) | Rolling Thunder Airport (NV96) | 2026-04-03 16:08 UTC | 2026-04-03 20:04 UTC | 3h 55m |
| N824US |  | Bolingbrook's Clow International Airport (K1C5) | Bolingbrook's Clow International Airport (K1C5) | 2026-04-03 19:30 UTC | 2026-04-03 20:02 UTC | 32m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-03 19:50 UTC | 2026-04-03 20:01 UTC | 11m |
| SKW368P | SkyWest Airlines | Denver International Airport (KDEN) | Johnson County Airport (KBYG) | 2026-04-03 19:11 UTC | 2026-04-03 19:59 UTC | 48m |
| DAGGR01 | DAG | Centennial Airport (KAPA) | Bellamy Farm Airport (27KS) | 2026-04-03 18:59 UTC | 2026-04-03 19:59 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
