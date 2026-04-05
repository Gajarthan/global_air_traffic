# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_20:34:10_UTC-green)

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

**Latest saved flight:** 2026-04-05 20:34:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 20:34:10 UTC

- **18,929** saved flights
- **9,603** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,929** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **239,660.5 tonnes** estimated CO2 emissions
- **13,893,361 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 828 |
| 2 | Ryanair | 785 |
| 3 | IndiGo | 539 |
| 4 | American Airlines | 359 |
| 5 | EJA | 343 |
| 6 | Southwest Airlines | 269 |
| 7 | ENY | 259 |
| 8 | Lufthansa | 256 |
| 9 | Vueling | 210 |
| 10 | LATAM Airlines | 200 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 164 |
| 13 | LXJ | 164 |
| 14 | All Nippon Airways | 161 |
| 15 | QLK | 154 |
| 16 | AZU | 146 |
| 17 | Swiss International | 142 |
| 18 | VIV | 141 |
| 19 | United Airlines | 129 |
| 20 | Alaska Airlines | 126 |
| 21 | Avianca | 125 |
| 22 | easyJet | 124 |
| 23 | Japan Airlines | 124 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | EDV | 115 |
| 27 | WIF | 115 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14817 |
| 2 | 🇮🇳 IN | 1637 |
| 3 | 🇪🇸 ES | 1565 |
| 4 | 🇦🇺 AU | 1316 |
| 5 | 🇧🇷 BR | 1095 |
| 6 | 🇨🇴 CO | 1009 |
| 7 | 🇯🇵 JP | 994 |
| 8 | 🇩🇪 DE | 965 |
| 9 | 🇮🇹 IT | 904 |
| 10 | 🇨🇦 CA | 835 |
| 11 | 🇬🇧 GB | 743 |
| 12 | 🇫🇷 FR | 699 |
| 13 | 🇲🇽 MX | 643 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 505 |
| 16 | 🇲🇾 MY | 440 |
| 17 | 🇬🇹 GT | 436 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 398 |
| 20 | 🇳🇴 NO | 385 |
| 21 | 🇹🇷 TR | 364 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇵🇱 PL | 276 |
| 25 | 🇹🇭 TH | 274 |
| 26 | 🇲🇦 MA | 240 |
| 27 | 🇧🇸 BS | 212 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 461 |
| 2 | El Dorado International Airport |  | CO | 382 |
| 3 | Denver International Airport |  | US | 352 |
| 4 | Indira Gandhi International Airport |  | IN | 343 |
| 5 | Tokyo International Airport |  | JP | 340 |
| 6 | La Aurora Airport |  | GT | 301 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 247 |
| 9 | Zurich Airport |  | CH | 233 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 204 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 201 |
| 13 | Chicago O'Hare International Airport |  | US | 199 |
| 14 | Macau International Airport |  | MO | 198 |
| 15 | Guaymaral Airport |  | CO | 197 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 17 | Charlotte/Douglas International Airport |  | US | 183 |
| 18 | Madrid Barajas International Airport |  | ES | 183 |
| 19 | Bengaluru International Airport |  | IN | 181 |
| 20 | Tenerife Norte Airport |  | ES | 174 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 170 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 162 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Salt Lake City International Airport |  | US | 154 |
| 26 | Daniel K Inouye International Airport |  | US | 148 |
| 27 | Reno/Tahoe International Airport |  | US | 148 |
| 28 | Malpensa International Airport |  | IT | 145 |
| 29 | Vitoria/Foronda Airport |  | ES | 144 |
| 30 | Charles de Gaulle International Airport |  | FR | 143 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 141 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 33 | Miami International Airport |  | US | 137 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 131 |
| 35 | Barcelona International Airport |  | ES | 130 |
| 36 | Pune Airport |  | IN | 128 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 127 |
| 38 | O. R. Tambo International Airport |  | ZA | 127 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 124 |
| 40 | Seattle-Tacoma International Airport |  | US | 118 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 85 | 14m | 114 km | 166.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 62 | 22m | 99 km | 106.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 52 | 16m | 206 km | 184.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 42 | 1h 53m | 1,304 km | 944.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 37 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 35 | 30m | 114 km | 68.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N999FN |  | French Valley Airport (KF70) | Cottonwood Airport (KP52) | 2026-04-05 19:15 UTC | 2026-04-05 20:34 UTC | 1h 18m |
| LXJ339 | LXJ | Palm Springs International Airport (KPSP) | Orlando Executive Airport (KORL) | 2026-04-05 16:28 UTC | 2026-04-05 20:33 UTC | 4h 4m |
| N57HR |  | Orlando Executive Airport (KORL) | Tampa Executive Airport (KVDF) | 2026-04-05 20:01 UTC | 2026-04-05 20:29 UTC | 27m |
| RAM985A | Royal Air Maroc | Malaga Airport (LEMG) | Rabat-Sale Airport (GMME) | 2026-04-05 19:52 UTC | 2026-04-05 20:26 UTC | 33m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-05 20:13 UTC | 2026-04-05 20:25 UTC | 12m |
| PDU60 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-05 20:06 UTC | 2026-04-05 20:17 UTC | 10m |
| N111AM |  | Miami-Opa Locka Executive Airport (KOPF) | Sehoy Airport (AL05) | 2026-04-05 19:09 UTC | 2026-04-05 20:15 UTC | 1h 6m |
| N78729 |  | Oconto/J Douglas Bake Municipal Airport (KOCQ) | Central Wisconsin Airport (KCWA) | 2026-04-05 19:07 UTC | 2026-04-05 20:13 UTC | 1h 6m |
| N955SC |  | Lazy 9 Ranch Airport (TX64) | Vance Field (TE76) | 2026-04-05 19:41 UTC | 2026-04-05 20:13 UTC | 32m |
| N470LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-05 19:11 UTC | 2026-04-05 20:11 UTC | 1h 0m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-04-05 19:09 UTC | 2026-04-05 20:07 UTC | 58m |
| N72785 |  | TA11 (TA11) | TA11 (TA11) | 2026-04-05 19:10 UTC | 2026-04-05 20:07 UTC | 56m |
| TGBOP | TGB | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-05 19:37 UTC | 2026-04-05 20:04 UTC | 26m |
| BRG2650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-05 19:34 UTC | 2026-04-05 20:02 UTC | 27m |
| CGCOZ | CGC | Biggar Airport (CJF8) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-05 19:26 UTC | 2026-04-05 20:00 UTC | 33m |
| TGMOR | TGM | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 19:35 UTC | 2026-04-05 19:57 UTC | 22m |
| N3717R |  | CL36 (CL36) | Charles M Schulz/Sonoma County Airport (KSTS) | 2026-04-05 18:35 UTC | 2026-04-05 19:56 UTC | 1h 21m |
| N61908 |  | Witham Field (KSUA) | Miami Executive Airport (KTMB) | 2026-04-05 19:25 UTC | 2026-04-05 19:55 UTC | 29m |
| VLG8TM | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-04-05 19:05 UTC | 2026-04-05 19:54 UTC | 49m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-05 19:38 UTC | 2026-04-05 19:53 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
